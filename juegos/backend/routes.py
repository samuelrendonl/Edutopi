"""Retroalimentación inmediata. El puntaje final se recalcula al guardar el progreso."""
from flask import Blueprint, jsonify, request
from .catalog import GAMES, game_questions

games = Blueprint("games", __name__, url_prefix="/api/games")

@games.post('/check')
def check():
    data = request.get_json(silent=True) or {}
    grade, index, answer = data.get('grade'), data.get('round'), data.get('answer')
    if any(type(value) is not int for value in (grade, index, answer)) or not 1 <= grade <= 5:
        return jsonify(error="La ronda no es válida."), 400
    game = next((g for g in GAMES if g['key']==data.get('key')), None)
    if not game:
        return jsonify(error="No encontramos ese juego."), 404
    questions = game_questions(game, grade)
    if not 0 <= index < len(questions) or not 0 <= answer < len(questions[index]['options']):
        return jsonify(error="La respuesta no es válida."), 400
    q = questions[index]
    return jsonify(correct=answer==q['answer'], correct_answer=q['options'][q['answer']],
                   explanation=f"La respuesta es: {q['options'][q['answer']]}")
