import os
import secrets
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)
from functools import wraps
from flask import Flask, g, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from werkzeug.security import check_password_hash, generate_password_hash
import mysql.connector
from mysql.connector import Error, IntegrityError
from app.learning_routes import learning
from app.auth_sessions import issue_parent_token, verify_parent_token, revoke_parent_token

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))


def load_secret_key():
    configured = os.getenv("SECRET_KEY")
    if configured:
        return configured
    secret_path = os.path.join(PROJECT_ROOT, ".secret_key")
    try:
        with open(secret_path, "r", encoding="utf-8") as secret_file:
            existing = secret_file.read().strip()
            if existing:
                return existing
    except FileNotFoundError:
        pass
    generated = secrets.token_urlsafe(48)
    try:
        with open(secret_path, "x", encoding="utf-8") as secret_file:
            secret_file.write(generated)
        return generated
    except FileExistsError:
        with open(secret_path, "r", encoding="utf-8") as secret_file:
            return secret_file.read().strip()
    except OSError:
        return generated


app = Flask(__name__)
app.config["SECRET_KEY"] = load_secret_key()
app.register_blueprint(learning)
from juegos.backend.routes import games
app.register_blueprint(games)
CORS(app, resources={r"/api/*": {"origins": "*"}})

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DATABASE", "edutopia"),
}

def get_db():
    if "db" not in g:
        g.db = mysql.connector.connect(**DB_CONFIG)
    return g.db

@app.before_request
def initialize_learning_connection():
    if request.path.startswith("/api/learning/children/"):
        get_db()

@app.teardown_appcontext
def close_db(_error=None):
    db = g.pop("db", None)
    if db and db.is_connected(): db.close()

def query(sql, params=(), fetch=False):
    cursor = get_db().cursor(dictionary=True)
    cursor.execute(sql, params)
    result = cursor.fetchall() if fetch else cursor.lastrowid
    cursor.close()
    return result

def commit(): get_db().commit()
def row_dict(row): return dict(row) if row else None

def auth_parent(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        parent_id = verify_parent_token(request.headers.get("X-Auth-Token"))
        if not parent_id: return jsonify({"error": "Inicia sesión para continuar."}), 401
        parent = query("SELECT * FROM parents WHERE id = %s", (parent_id,), True)
        if not parent: return jsonify({"error": "La sesión no es válida."}), 401
        g.parent = parent[0]
        return fn(*args, **kwargs)
    return wrapper

@app.get("/api")
def home(): return jsonify({"mensaje": "Backend de Edutopia funcionando con MySQL"})

@app.post("/api/auth/register")
def register():
    data = request.get_json(silent=True) or {}
    name, email, password = data.get("name", "").strip(), data.get("email", "").strip().lower(), data.get("password", "")
    if not name or not email or len(password) < 6: return jsonify({"error": "Completa todos los datos. La contraseña debe tener 6 caracteres."}), 400
    try:
        parent_id = query("INSERT INTO parents (name, email, password_hash) VALUES (%s, %s, %s)", (name, email, generate_password_hash(password))); commit()
    except IntegrityError: return jsonify({"error": "Este correo ya está registrado."}), 409
    return jsonify({"parent": {"id": parent_id, "name": name, "email": email}, "token": issue_parent_token(parent_id)}), 201

@app.post("/api/auth/login")
def login():
    data = request.get_json(silent=True) or {}
    rows = query("SELECT * FROM parents WHERE email = %s", (data.get("email", "").strip().lower(),), True)
    if not rows or not check_password_hash(rows[0]["password_hash"], data.get("password", "")): return jsonify({"error": "Correo o contraseña incorrectos."}), 401
    parent = rows[0]
    return jsonify({"parent": {"id": parent["id"], "name": parent["name"], "email": parent["email"]}, "token": issue_parent_token(parent["id"])})

@app.post("/api/auth/logout")
def logout():
    data = request.get_json(silent=True) or {}
    revoke_parent_token(request.headers.get("X-Auth-Token") or data.get("token"))
    return jsonify({"ok": True})

@app.get("/api/children")
@auth_parent
def children(): return jsonify({"children": query("SELECT * FROM children WHERE parent_id = %s ORDER BY created_at DESC", (g.parent["id"],), True)})

@app.post("/api/children")
@auth_parent
def add_child():
    data = request.get_json(silent=True) or {}
    try: name, age, grade = data.get("name", "").strip(), int(data.get("age")), int(data.get("grade"))
    except (TypeError, ValueError): return jsonify({"error": "Revisa el nombre, la edad y el grado."}), 400
    if not name or age < 5 or age > 12 or grade < 1 or grade > 5: return jsonify({"error": "Usa una edad entre 5 y 12 años y un grado de 1.º a 5.º."}), 400
    child_id = query("INSERT INTO children (parent_id, name, age, grade, avatar) VALUES (%s, %s, %s, %s, %s)", (g.parent["id"], name, age, grade, data.get("avatar", "🌟"))); commit()
    return jsonify({"child": query("SELECT * FROM children WHERE id = %s", (child_id,), True)[0]}), 201

if __name__ == "__main__": app.run(debug=True, port=int(os.getenv("PORT", "5000")))
