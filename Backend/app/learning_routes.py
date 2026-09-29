"""API de actividades y progreso por perfil infantil."""

from functools import wraps
from flask import Blueprint, g, jsonify, request

from .learning_content import ACTIVITIES, activity_for_grade, public_activity
from .auth_sessions import verify_parent_token
from juegos.backend.catalog import evaluate_game

learning = Blueprint("learning", __name__, url_prefix="/api/learning")
_catalog_cache = {}


def _query(sql, params=(), fetch=False):
    cursor = g.db.cursor(dictionary=True)
    cursor.execute(sql, params)
    rows = cursor.fetchall() if fetch else cursor.lastrowid
    cursor.close()
    return rows


def _child_access(fn):
    @wraps(fn)
    def wrapped(child_id, *args, **kwargs):
        parent_id = verify_parent_token(request.headers.get("X-Auth-Token"))
        if not parent_id:
            return jsonify({"error": "Inicia sesión para continuar."}), 401
        child = _query(
            "SELECT id, name, grade FROM children WHERE id = %s AND parent_id = %s",
            (child_id, parent_id), True,
        )
        if not child:
            return jsonify({"error": "No encontramos ese perfil infantil."}), 404
        g.child = child[0]
        return fn(child_id, *args, **kwargs)
    return wrapped


@learning.get("/activities")
def activities():
    grade = request.args.get("grade", default=3, type=int)
    grade = min(5, max(1, grade or 3))
    # Catálogo inmutable en memoria por grado: lecturas rápidas sin consultar MySQL.
    if grade not in _catalog_cache:
        _catalog_cache[grade] = [public_activity(item, grade) for item in ACTIVITIES]
    return jsonify({"grade": grade, "activities": _catalog_cache[grade]})


@learning.get("/children/<int:child_id>/progress")
@_child_access
def progress(child_id):
    rows = _query(
        "SELECT activity_key, best_score, attempts, completed_at FROM child_activity_progress WHERE child_id = %s",
        (child_id,), True,
    )
    by_key = {row["activity_key"]: row for row in rows}
    total_points = sum(row["best_score"] for row in rows)
    completed = len(by_key)
    return jsonify({
        "child": g.child,
        "completed": completed,
        "total": len(ACTIVITIES),
        "progress": round(completed * 100 / len(ACTIVITIES)),
        "points": total_points,
        "activities": by_key,
    })


@learning.post("/children/<int:child_id>/submit")
@_child_access
def submit(child_id):
    data = request.get_json(silent=True) or {}
    activity_key = data.get("activity_key")
    answers = data.get("answers")
    activity = next((item for item in ACTIVITIES if item["key"] == activity_key), None)
    if activity:
        activity = activity_for_grade(activity, g.child["grade"])
    if not activity or not isinstance(answers, list) or len(answers) != len(activity["questions"]):
        return jsonify({"error": "La actividad o las respuestas no son válidas."}), 400
    if any(not isinstance(answer, int) or isinstance(answer, bool) for answer in answers):
        return jsonify({"error": "Selecciona una respuesta para cada pregunta."}), 400
    if any(answer < 0 or answer >= len(question["options"]) for answer, question in zip(answers, activity["questions"])):
        return jsonify({"error": "Una de las respuestas no es válida."}), 400

    correct = evaluate_game(activity, answers) if activity["kind"] == "Juego" else sum(answer == question["answer"] for answer, question in zip(answers, activity["questions"]))
    score = round(correct * activity["points"] / len(activity["questions"]))
    cursor = g.db.cursor()
    cursor.execute(
        """INSERT INTO child_activity_progress (child_id, activity_key, best_score, attempts)
           VALUES (%s, %s, %s, 1)
           ON DUPLICATE KEY UPDATE
             best_score = GREATEST(best_score, VALUES(best_score)),
             attempts = attempts + 1,
             completed_at = CURRENT_TIMESTAMP""",
        (child_id, activity_key, score),
    )
    cursor.close()
    g.db.commit()
    row = _query(
        "SELECT best_score, attempts FROM child_activity_progress WHERE child_id = %s AND activity_key = %s",
        (child_id, activity_key), True,
    )[0]
    return jsonify({
        "correct": correct, "total": len(activity["questions"]), "earned": score,
        "best_score": row["best_score"], "attempts": row["attempts"],
        "message": "¡Excelente trabajo!" if correct == len(activity["questions"]) else "¡Buen intento! Sigue practicando.",
    })


@learning.post("/guest/submit")
def submit_guest():
    """Evalúa una sesión de prueba sin cuenta ni escrituras en la base de datos."""
    data = request.get_json(silent=True) or {}
    activity_key = data.get("activity_key")
    answers = data.get("answers")
    activity = next((item for item in ACTIVITIES if item["key"] == activity_key), None)
    grade = data.get("grade", 3)
    if not isinstance(grade, int) or isinstance(grade, bool) or grade < 1 or grade > 5:
        return jsonify({"error": "Selecciona un grado entre 1.º y 5.º."}), 400
    if activity:
        activity = activity_for_grade(activity, grade)
    guest_limit = 3 if activity and activity["kind"] == "Juego" else (len(activity["questions"]) if activity else 0)
    if not activity or not isinstance(answers, list) or len(answers) != guest_limit:
        return jsonify({"error": "Las respuestas enviadas no corresponden a esta actividad."}), 400
    if any(not isinstance(answer, int) or isinstance(answer, bool) or answer < 0 or answer >= len(activity["questions"][index]["options"])
           for index, answer in enumerate(answers)):
        return jsonify({"error": "Una de las respuestas no es válida."}), 400
    correct = evaluate_game(activity, answers) if activity["kind"] == "Juego" else sum(answer == question["answer"] for answer, question in zip(answers, activity["questions"]))
    score = round(correct * activity["points"] / len(activity["questions"]))
    return jsonify({
        "correct": correct, "total": len(answers), "earned": score,
        "best_score": score, "attempts": 1,
        "message": "¡Excelente trabajo!" if correct == len(answers) else "¡Buen intento! Sigue practicando.",
        "saved": False,
    })
