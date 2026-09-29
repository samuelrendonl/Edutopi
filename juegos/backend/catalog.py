"""Catálogo y reglas de los juegos. No depende de Flask ni de MySQL."""
from decimal import Decimal

GAMES = [
    dict(key="math-balloons", subject="Matemáticas", game="balloons", title="Globos matemáticos", description="Atrapa el globo con la respuesta correcta. Puedes pausar el movimiento.", icon="sparkles", color="#5254c7"),
    dict(key="math-race", subject="Matemáticas", game="race", title="Misión cohete", description="Resuelve cálculos y lleva tu cohete hasta las estrellas.", icon="rocket", color="#247ba6"),
    dict(key="language-balloons", subject="Lengua Castellana", game="word-balloons", title="Burbujas de palabras", description="Atrapa palabras siguiendo pistas de sonidos, vocabulario y significado.", icon="book", color="#a84474"),
    dict(key="word-detective", subject="Lengua Castellana", game="detective", title="Detectives de palabras", description="Abre expedientes y encuentra la pista que resuelve cada caso.", icon="sparkles", color="#157965"),
]
for game in GAMES:
    game.update(kind="Juego", points=100, minutes=6, lesson=[], questions=[])


def game_questions(game, grade):
    # Importación diferida: el catálogo escolar también incorpora GAMES.
    from app.extra_content import curriculum_for_grade, question
    if game["subject"] == "Lengua Castellana":
        unit = "vocabulary" if game["game"] == "word-balloons" else "grammar"
        return curriculum_for_grade(unit, grade)["questions"]
    rows=[]
    for i in range(10):
        if grade==1:
            a,b=2+i,1+i%4; op="+" if i%2==0 else "−"; answer=a+b if op=="+" else a-b
        elif grade==2:
            a,b=25+i*3,8+i; op="+" if i%2==0 else "−"; answer=a+b if op=="+" else a-b
        elif grade==3:
            a,b=3+i,2+i%5; op="×"; answer=a*b
        elif grade==4:
            b=2+i%7; answer=3+i; a=b*answer; op="÷"
        else:
            a,b=Decimal(125+i*25)/100,Decimal(50+i*5)/100; op="+" if i%2==0 else "−"; answer=a+b if op=="+" else a-b
        display=lambda n: str(n).replace('.', ',')
        delta=Decimal('0.1') if grade==5 else 1
        rows.append(question(f"{display(a)} {op} {display(b)} = ?", display(answer), display(answer+delta), display(answer-delta), i))
    return rows


def evaluate_game(activity, answers):
    return sum(answer == q["answer"] for answer,q in zip(answers,activity["questions"]))
