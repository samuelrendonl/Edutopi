"""Sesiones revocables, compartidas entre procesos mediante SQLite local.
Los datos educativos siguen en MySQL. No requiere migrar las tablas existentes.
"""
import hashlib
import secrets
import sqlite3
import time
from pathlib import Path
from flask import current_app
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

SALT = "edutopia-family-session-v2"
MAX_AGE_SECONDS = 60 * 30


def _db():
    path = current_app.config.get("SESSION_DB_PATH", str(Path(__file__).resolve().parents[2] / "sessions.sqlite3"))
    db = sqlite3.connect(path, timeout=10)
    db.execute("CREATE TABLE IF NOT EXISTS sessions (id TEXT PRIMARY KEY, parent_id INTEGER NOT NULL, expires REAL NOT NULL)")
    return db


def _digest(token):
    return hashlib.sha256(token.encode()).hexdigest()


def issue_parent_token(parent_id):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt=SALT)
    token = serializer.dumps({"parent_id": int(parent_id), "nonce": secrets.token_urlsafe(24)})
    db = _db()
    try:
        with db:
            db.execute("DELETE FROM sessions WHERE expires < ?", (time.time(),))
            db.execute("INSERT INTO sessions VALUES (?, ?, ?)", (_digest(token), int(parent_id), time.time()+MAX_AGE_SECONDS))
    finally:
        db.close()
    return token


def verify_parent_token(token):
    if not isinstance(token, str) or not token:
        return None
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"], salt=SALT)
    try:
        payload = serializer.loads(token, max_age=MAX_AGE_SECONDS)
        parent_id = int(payload["parent_id"])
    except (BadSignature, SignatureExpired, KeyError, TypeError, ValueError):
        return None
    db = _db()
    try:
        row = db.execute("SELECT parent_id FROM sessions WHERE id = ? AND expires > ?", (_digest(token), time.time())).fetchone()
        return parent_id if row and row[0] == parent_id else None
    finally:
        db.close()


def revoke_parent_token(token):
    if not isinstance(token, str) or not token:
        return
    db = _db()
    try:
        with db:
            db.execute("DELETE FROM sessions WHERE id = ?", (_digest(token),))
    finally:
        db.close()
