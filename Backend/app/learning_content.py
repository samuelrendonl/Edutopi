"""Catálogo curricular de Edutopia y generadores de práctica por grado."""

BASE_ACTIVITIES = [
    {
        "key": "math-sums", "subject": "Matemáticas", "kind": "Aprendizaje",
        "title": "Operaciones y problemas", "description": "Aprende estrategias para calcular y resolver situaciones cotidianas.",
        "color": "#5b5ce2", "icon": "calculator", "points": 100, "minutes": 7,
        "lesson": [
            "Primero lee el problema completo y piensa qué está pasando: ¿se juntan cantidades, se quitan, se repiten o se reparten? Esa historia te da una pista sobre la operación.",
            "Para sumar, puedes separar los números en decenas y unidades. Por ejemplo, 28 + 15 es (20 + 10) + (8 + 5). Luego juntas los resultados. Si una unidad pasa de diez, cambia diez unidades por una decena.",
            "Para restar, compara las cantidades o piensa cuánto falta para llegar de un número al otro. En una resta con préstamo, una decena se convierte en diez unidades. Comprueba el resultado sumando la diferencia al número menor.",
            "En grados mayores aparecen números más grandes y decimales. La multiplicación permite sumar grupos iguales; la división sirve para repartir o descubrir cuántos grupos caben. Dibuja, separa los números por partes y revisa si el resultado tiene sentido antes de marcarlo.",
        ],
        "questions": [],
    },
    {
        "key": "reading-story", "subject": "Lengua Castellana", "kind": "Aprendizaje",
        "title": "Leemos entre líneas", "description": "Comprende una historia, identifica sus pistas y explica tus ideas.",
        "color": "#f28c28", "icon": "book", "points": 100, "minutes": 8,
        "passage": "El sábado, Tomás encontró una caja pequeña junto al viejo limonero de su abuela. No tenía candado, pero una cinta azul rodeaba la tapa. Dentro había semillas, una nota y una fotografía de un jardín lleno de girasoles. La nota decía: «Las cosas bonitas crecen cuando alguien las cuida». Tomás miró el patio, que llevaba meses vacío, y llamó a su prima Sara. Juntos llenaron varias macetas con tierra. Separaron las semillas, las cubrieron con cuidado y escribieron el nombre de cada planta en una etiqueta. Durante las semanas siguientes se turnaron para regarlas. Un día, Sara llegó corriendo: entre la tierra asomaba un brote verde. Tomás sonrió. La caja ya no guardaba un misterio; ahora guardaba una promesa que los dos habían empezado a cumplir.",
        "passage_by_grade": {
            "early": "El sábado, Tomás encontró una caja junto al limonero de su abuela. Tenía una cinta azul. Adentro había semillas, una nota y una foto de girasoles. Tomás llamó a su prima Sara. Juntos pusieron tierra en unas macetas y sembraron las semillas. Cada día se turnaron para regarlas. Una mañana apareció un brote verde. Los dos sonrieron: ahora tenían plantas para cuidar.",
            "upper": "El sábado, Tomás descubrió una caja sin candado junto al limonero de su abuela; una cinta azul mantenía cerrada la tapa. Encontró semillas, una nota y una fotografía de un jardín repleto de girasoles. «Las cosas bonitas crecen cuando alguien las cuida», decía el mensaje. Como el patio llevaba meses vacío, invitó a su prima Sara a sembrar. Organizaron las semillas en macetas, pusieron etiquetas y se turnaron para regarlas durante varias semanas. Cuando un brote verde asomó entre la tierra, Tomás entendió que la nota no escondía un secreto mágico: les proponía un proyecto que ambos podían hacer realidad con paciencia y colaboración.",
        },
        "lesson": [
            "Comprender un texto es construir su sentido, no solo pronunciar sus palabras. Mientras lees, imagina la escena y pregúntate qué quiere cada personaje.",
            "Las respuestas explícitas aparecen directamente en el texto. Para encontrarlas, busca nombres, lugares, acciones y palabras que se repiten.",
            "A veces el texto no dice todo de forma directa. Puedes inferir algo juntando varias pistas. Una inferencia debe apoyarse en lo que leíste, no en una suposición sin evidencia.",
            "Al final, resume la historia con tus propias palabras: quién participó, qué problema o situación apareció y cómo terminó. Volver a leer una frase también es una buena estrategia.",
        ],
        "questions": [
            {"prompt": "¿Qué encontró Tomás junto al limonero?", "options": ["Una caja pequeña", "Una pelota", "Un libro grande"], "answer": 0},
            {"prompt": "¿De qué color era la cinta?", "options": ["Roja", "Azul", "Verde"], "answer": 1},
            {"prompt": "¿Qué había dentro de la caja?", "options": ["Semillas, una nota y una foto", "Juguetes y dulces", "Una regadera y una pala"], "answer": 0},
            {"prompt": "¿A quién llamó Tomás para ayudarle?", "options": ["A su abuela", "A su prima Sara", "A su vecino"], "answer": 1},
            {"prompt": "¿Qué hicieron con las semillas?", "options": ["Las guardaron en un cajón", "Las plantaron en macetas", "Se las regalaron a la abuela"], "answer": 1},
            {"prompt": "¿Por qué se turnaban para regarlas?", "options": ["Para cuidar las plantas entre los dos", "Para llenar la caja", "Para limpiar el patio"], "answer": 0},
            {"prompt": "¿Qué apareció entre la tierra?", "options": ["Una flor amarilla", "Un brote verde", "Una piedra azul"], "answer": 1},
            {"prompt": "¿Qué significa aquí «las cosas bonitas crecen cuando alguien las cuida»?", "options": ["Que cuidar algo ayuda a que se desarrolle", "Que las cajas deben cerrarse", "Que las plantas crecen sin agua"], "answer": 0},
            {"prompt": "¿Cómo cambió el patio durante la historia?", "options": ["De vacío empezó a tener macetas cuidadas", "Se convirtió en una caja", "Dejó de recibir luz"], "answer": 0},
            {"prompt": "¿Cuál es la idea principal del relato?", "options": ["Tomás perdió una fotografía", "Tomás y Sara cuidaron juntos unas semillas", "La abuela compró un limonero"], "answer": 1},
        ],
    },
    {
        "key": "words-syllables", "subject": "Lengua Castellana", "kind": "Aprendizaje",
        "title": "Palabras, sílabas y acentos", "description": "Escucha cómo suenan las palabras y reconoce dónde llevan tilde.",
        "color": "#e66a9b", "icon": "book", "points": 100, "minutes": 7,
        "lesson": [
            "Las sílabas son grupos de sonidos que pronunciamos en un solo impulso de voz. Pronuncia una palabra despacio y acompaña cada golpe de voz con una palmada.",
            "Una palabra puede tener una sílaba, como sol; dos, como ca-sa; tres, como ven-ta-na; o más, como ma-ri-po-sa. Las vocales ayudan a formar el centro de cada sílaba.",
            "Todas las palabras tienen una sílaba que suena con más fuerza: la sílaba tónica. En algunas palabras se escribe una tilde para señalar esa fuerza y seguir las reglas de acentuación.",
            "Lee cada opción en voz alta, sepárala en sílabas y escucha dónde recae la voz. Después revisa la tilde: practicar con ejemplos ayuda a escribir con más seguridad.",
        ],
        "questions": [
            {"prompt": "¿Cuántas sílabas tiene «casa»?", "options": ["Una", "Dos", "Tres"], "answer": 1},
            {"prompt": "¿Cómo se separa «mariposa»?", "options": ["ma-ri-po-sa", "mar-ip-osa", "ma-rip-osa"], "answer": 0},
            {"prompt": "¿Qué palabra empieza con el sonido de M?", "options": ["Luna", "Mesa", "Rana"], "answer": 1},
            {"prompt": "¿Cuál palabra tiene tres sílabas?", "options": ["Pan", "Camino", "Flor"], "answer": 1},
            {"prompt": "¿En qué sílaba suena más fuerte «pelota»?", "options": ["pe", "lo", "ta"], "answer": 1},
            {"prompt": "¿Cuál palabra lleva tilde escrita?", "options": ["Arbol", "Árbol", "Arból"], "answer": 1},
            {"prompt": "¿Cuántas sílabas tiene «mar»?", "options": ["Una", "Dos", "Tres"], "answer": 0},
            {"prompt": "¿Cuál separación es correcta para «ventana»?", "options": ["ven-ta-na", "ve-nta-na", "vent-ana"], "answer": 0},
            {"prompt": "¿Qué palabra rima con «canción»?", "options": ["Balón", "Casa", "Lápiz"], "answer": 0},
            {"prompt": "¿Cuál opción está escrita correctamente?", "options": ["camión", "camíon", "camion"], "answer": 0},
        ],
        "grade_questions": {
            "upper": [
                {"prompt": "¿Cuántas sílabas tiene «extraordinario»?", "options": ["Cuatro", "Seis", "Ocho"], "answer": 1},
                {"prompt": "¿Cuál palabra es esdrújula?", "options": ["Brújula", "Papel", "Reloj"], "answer": 0},
                {"prompt": "¿Cuál palabra presenta hiato?", "options": ["País", "Cuidado", "Puerta"], "answer": 0},
                {"prompt": "¿Cuál palabra aguda debe llevar tilde?", "options": ["Compás", "Papel", "Reloj"], "answer": 0},
                {"prompt": "¿Cuál palabra llana está bien escrita y no necesita tilde?", "options": ["Joven", "Jóven", "Jovén"], "answer": 0},
                {"prompt": "¿Cuál palabra contiene un triptongo?", "options": ["Buey", "País", "Maíz"], "answer": 0},
                {"prompt": "¿Cómo se separa «murciélago»?", "options": ["mur-cié-la-go", "murcié-la-go", "mur-ciél-ago"], "answer": 0},
                {"prompt": "¿Cuál palabra aguda lleva tilde?", "options": ["Café", "Mesa", "Lunes"], "answer": 0},
                {"prompt": "¿Qué palabra está tildada correctamente?", "options": ["también", "tambièn", "támbien"], "answer": 0},
                {"prompt": "En «biblioteca», ¿cuál es la sílaba tónica?", "options": ["bi", "te", "ca"], "answer": 1},
            ],
        },
    },
    {
        "key": "math-fractions-geometry", "subject": "Matemáticas", "kind": "Aprendizaje",
        "title": "Fracciones y figuras", "description": "Relaciona partes y cantidades, mide y descubre formas en situaciones reales.",
        "color": "#7c65d9", "icon": "calculator", "points": 100, "minutes": 8,
        "lesson": [
            "Una fracción representa partes iguales de un todo. El número de abajo indica en cuántas partes se divide y el de arriba cuántas partes tomamos.",
            "Para comparar fracciones con el mismo denominador, observa sus numeradores: más partes tomadas significa una fracción mayor.",
            "Las figuras tienen lados, vértices y propiedades que puedes observar. Medir con cuidado y dibujar ayuda a resolver problemas de geometría.",
            "Lee cada problema, identifica los datos y representa la situación antes de elegir una respuesta. Después comprueba si el resultado tiene sentido."
        ],
        "questions": [
            {"prompt": "¿Qué fracción representa una de cuatro partes iguales?", "options": ["1/4", "4/1", "1/2"], "answer": 0},
            {"prompt": "¿Cuál es mayor?", "options": ["2/8", "5/8", "1/8"], "answer": 1},
            {"prompt": "¿Cuántos lados tiene un pentágono?", "options": ["4", "5", "6"], "answer": 1},
            {"prompt": "La mitad de 12 es…", "options": ["4", "6", "8"], "answer": 1},
            {"prompt": "¿Qué figura tiene todos sus lados iguales y cuatro vértices?", "options": ["Círculo", "Cuadrado", "Triángulo"], "answer": 1},
            {"prompt": "Si una pizza se divide en 8 partes y comes 3, ¿qué fracción comes?", "options": ["3/8", "8/3", "5/8"], "answer": 0},
            {"prompt": "¿Cuántos centímetros hay en un metro?", "options": ["10", "50", "100"], "answer": 2},
            {"prompt": "¿Qué fracción equivale a la mitad?", "options": ["1/3", "2/4", "3/4"], "answer": 1},
            {"prompt": "Un rectángulo tiene…", "options": ["3 lados", "4 lados", "5 lados"], "answer": 1},
            {"prompt": "Si recorres 3 metros y luego 2 metros, recorres…", "options": ["1 metro", "5 metros", "6 metros"], "answer": 1}
        ]
    },
    {
        "key": "language-write-create", "subject": "Lengua Castellana", "kind": "Aprendizaje",
        "title": "Construimos historias", "description": "Ordena ideas, mejora frases y escribe con intención.",
        "color": "#d7659a", "icon": "book", "points": 100, "minutes": 8,
        "lesson": [
            "Toda historia necesita personajes, un lugar y algo que sucede. Ordenar esos elementos ayuda a que el lector entienda lo que quieres contar.",
            "Una oración comienza con mayúscula y termina con un signo adecuado. El punto separa ideas completas y la coma ayuda a organizar enumeraciones.",
            "Los conectores como primero, luego, porque y finalmente unen las ideas y muestran el orden o la causa de los acontecimientos.",
            "Antes de entregar un texto, léelo en voz alta: revisa mayúsculas, tildes, signos y si cada oración comunica una idea clara."
        ],
        "questions": [
            {"prompt": "¿Cuál oración comienza correctamente?", "options": ["mañana iremos al parque.", "Mañana iremos al parque.", "mañana Iremos al parque."], "answer": 1},
            {"prompt": "¿Qué signo termina una pregunta?", "options": ["¿ ?", ".", ","], "answer": 0},
            {"prompt": "¿Cuál palabra es un personaje?", "options": ["Valentina", "Ayer", "Rápido"], "answer": 0},
            {"prompt": "¿Qué conector indica el final?", "options": ["Primero", "Porque", "Finalmente"], "answer": 2},
            {"prompt": "¿Cuál oración tiene sentido completo?", "options": ["El perro corre.", "Porque la lluvia.", "En el jardín y."], "answer": 0},
            {"prompt": "Elige la palabra escrita correctamente.", "options": ["árbol", "arbol", "árból"], "answer": 0},
            {"prompt": "¿Qué palabra describe cómo corre alguien?", "options": ["Rápidamente", "Casa", "Ayer"], "answer": 0},
            {"prompt": "¿Cuál orden cuenta mejor una receta?", "options": ["Finalmente, primero, luego", "Primero, luego, finalmente", "Luego, finalmente, primero"], "answer": 1},
            {"prompt": "¿Para qué sirve la coma en una lista?", "options": ["Separar elementos", "Terminar siempre el texto", "Cambiar una palabra"], "answer": 0},
            {"prompt": "¿Cuál es un buen título para una historia de un viaje?", "options": ["Mi aventura en la montaña", "Palabra", "El"], "answer": 0}
        ]
    },

]


def _display_number(value, grade):
    if grade == 5:
        return f"{value / 100:.2f}".replace(".", ",")
    return str(value)


def questions_for_grade(activity, grade):
    """Genera ejercicios de cálculo adecuados al grado; el resto usa su banco didáctico."""
    grade = max(1, min(5, int(grade or 3)))
    if activity.get("kind") == "Juego":
        return game_questions(activity, grade)
    if activity.get("curriculum"):
        return curriculum_for_grade(activity["curriculum"], grade)["questions"]
    if activity.get("grade_questions"):
        band = "early" if grade <= 2 else "middle" if grade == 3 else "upper"
        return activity["grade_questions"].get(band, activity["questions"])
    if activity["key"] not in {"math-sums", "math-race"}:
        return activity["questions"]
    questions = []
    for index in range(10):
        if grade == 1:
            first, second = (index + 2, 3 + index % 4) if index < 5 else (10 + index - 5, index - 4)
            operator = "+" if index < 5 else "−"
            answer = first + second if operator == "+" else first - second
            step = 1
        elif grade == 2:
            first, second = (18 + index, 7 + index % 5) if index < 5 else (30 + index, 8 + index % 4)
            operator = "+" if index < 5 else "−"
            answer = first + second if operator == "+" else first - second
            step = 1
        elif grade == 3:
            first, second = (126 + index * 7, 48 + index * 3) if index < 5 else (250 + index * 5, 73 + index * 2)
            operator = "+" if index < 5 else "−"
            answer = first + second if operator == "+" else first - second
            step = 10
        elif grade == 4:
            first, second = (6 + index, 4 + index % 5) if index < 5 else (72 + index, 3 + index % 6)
            operator = "×" if index < 5 else "÷"
            answer = first * second if operator == "×" else first // second
            if operator == "÷":
                first = answer * second
            step = 1
        else:
            first, second = (125 + index * 25, 75 + index * 10) if index < 5 else (450 + index * 20, 125 + index * 10)
            operator = "+" if index < 5 else "−"
            answer = first + second if operator == "+" else first - second
            step = 10
        options = [_display_number(answer - step, grade), _display_number(answer + step, grade), _display_number(answer, grade)]
        correct_index = index % 3
        options[correct_index], options[2] = options[2], options[correct_index]
        questions.append({
            "prompt": f"{_display_number(first, grade)} {operator} {_display_number(second, grade)} = ¿cuánto?",
            "options": options,
            "answer": correct_index,
        })
    return questions

def activity_for_grade(activity, grade):
    extra = curriculum_for_grade(activity["curriculum"], grade) if activity.get("curriculum") else {}
    return {**activity, **extra, "questions": questions_for_grade(activity, grade)}


def public_activity(activity, grade=3):
    """No expone respuestas correctas al navegador."""
    activity = activity_for_grade(activity, grade)
    result = {key: value for key, value in activity.items() if key not in {"questions", "grade_questions", "passage_by_grade"}}
    if activity.get("passage_by_grade"):
        band = "early" if grade <= 2 else "upper" if grade >= 4 else "middle"
        result["passage"] = activity["passage_by_grade"][band] if band in activity["passage_by_grade"] else activity["passage"]
    result["grade"] = grade
    result["grades"] = [1, 2, 3, 4, 5]
    result["questions"] = [
        {"prompt": question["prompt"], "options": question["options"]}
        for question in questions_for_grade(activity, grade)
    ]
    return result


from .extra_content import EXTRA_ACTIVITIES, curriculum_for_grade
from juegos.backend.catalog import GAMES, game_questions
ACTIVITIES = BASE_ACTIVITIES + EXTRA_ACTIVITIES + GAMES
