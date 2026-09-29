"""Seis unidades nuevas; cada unidad tiene una lección y práctica para cada grado."""


def question(prompt, correct, wrong1, wrong2, index=0):
    options = [str(correct), str(wrong1), str(wrong2)]
    offset = index % 3
    options = options[-offset:] + options[:-offset] if offset else options
    return {"prompt": prompt, "options": options, "answer": offset}


UNITS = [
    ("math-laboratory", "Matemáticas", "Laboratorio de números", "Descubre patrones y explica qué cambia en cada paso.", "patterns"),
    ("math-market", "Matemáticas", "El mercado de los números", "Cuenta, compra y reparte en situaciones cotidianas.", "market"),
    ("math-measures", "Matemáticas", "Exploradores de medidas", "Compara longitudes, tiempos, perímetros y áreas.", "measures"),
    ("language-vocabulary", "Lengua Castellana", "Un mundo de palabras", "Amplía tu vocabulario con sonidos, sinónimos y familias.", "vocabulary"),
    ("language-grammar", "Lengua Castellana", "Taller de oraciones", "Descubre cómo se organizan las palabras para expresar ideas.", "grammar"),
    ("language-adventure", "Lengua Castellana", "Crea tu propia aventura", "Reconoce las pistas, el orden y la intención de un relato.", "adventure"),
]
EXTRA_ACTIVITIES = [dict(key=key, subject=subject, title=title, description=description,
    curriculum=unit, kind="Aprendizaje", color="#5b5ce2" if subject == "Matemáticas" else "#b95079",
    icon="calculator" if subject == "Matemáticas" else "book", points=100, minutes=8,
    lesson=[], questions=[]) for key, subject, title, description, unit in UNITS]

LANGUAGE = {
"vocabulary": {
1: ("Sonidos y significados", "Pronuncia despacio: mesa comienza con m; sol comienza con s. Las palabras nombran seres, objetos y acciones.", [
("¿Qué palabra comienza con m?", "mesa", "luna", "sapo"), ("¿Qué palabra nombra un animal?", "gato", "mesa", "azul"), ("¿Qué palabra rima con gato?", "pato", "luna", "mesa"), ("¿Cuál es lo contrario de día?", "noche", "sol", "luz"), ("¿Qué usamos para leer?", "libro", "zapato", "vaso")]),
2: ("Palabras que se parecen", "Los sinónimos tienen significados parecidos: feliz y contento. Los antónimos expresan ideas opuestas: subir y bajar.", [
("Un sinónimo de feliz es…", "contento", "triste", "enojado"), ("El contrario de subir es…", "bajar", "trepar", "elevar"), ("¿Qué palabra pertenece a la familia de pan?", "panadero", "pantalla", "pantalón"), ("¿Cuál es el diminutivo de gato?", "gatito", "gatazo", "gatos"), ("El plural de flor es…", "flores", "florces", "flors")]),
3: ("Familias y categorías", "Una familia comparte raíz y significado: flor, florero, florista. Un campo semántico agrupa palabras por tema: rosa, tulipán y girasol son flores.", [
("¿Cuál pertenece a la familia de flor?", "florista", "flota", "flauta"), ("Rosa, tulipán y girasol son…", "flores", "frutas", "árboles"), ("Un sinónimo de veloz es…", "rápido", "lento", "quieto"), ("El antónimo de generoso es…", "egoísta", "solidario", "amable"), ("¿Cuál palabra no es un medio de transporte?", "almohada", "bicicleta", "tren")]),
4: ("El contexto da pistas", "Una palabra puede tener varios sentidos. En «me senté en el banco», banco significa asiento. El contexto permite elegir el significado adecuado.", [
("En «me senté en el banco», banco es…", "un asiento", "una entidad financiera", "un pez"), ("En «la copa del árbol», copa es…", "la parte con ramas y hojas", "un vaso", "un premio"), ("El prefijo des- en deshacer indica…", "invertir la acción", "repetir la acción", "hacerla antes"), ("Un sinónimo de observar es…", "examinar", "ignorar", "ocultar"), ("Biblioteca y librería se relacionan con…", "libros", "deportes", "alimentos")]),
5: ("Lenguaje literal y figurado", "El lenguaje figurado usa comparaciones o imágenes. «Tengo un mar de dudas» expresa muchas dudas, no agua real. Busca siempre pistas en la oración.", [
("«Tengo un mar de dudas» significa…", "tengo muchas dudas", "nado en el mar", "no tengo dudas"), ("El prefijo re- en releer indica…", "volver a leer", "dejar de leer", "leer mal"), ("¿Qué par contiene antónimos?", "abundante / escaso", "feliz / contento", "veloz / rápido"), ("En «el tiempo vuela» se expresa que…", "parece pasar muy rápido", "tiene alas", "se ha detenido"), ("¿Cuál es un término más general que perro y gato?", "animal", "labrador", "bigote")])},
"grammar": {
1: ("Oraciones pequeñas", "Una oración comunica una idea. «La niña canta.» comienza con mayúscula y termina con punto. Canta dice qué hace la niña.", [
("¿Qué oración está bien escrita?", "Ana juega.", "ana juega", "Ana juega"), ("¿Qué palabra nombra una acción?", "saltar", "mesa", "verde"), ("Completa: El gato ___.", "duerme", "azul", "la"), ("¿Con qué comienza una oración?", "mayúscula", "coma", "punto"), ("¿Qué signo cierra «El sol brilla»?", ".", ",", "¿")]),
2: ("Nombres y cualidades", "Los sustantivos nombran seres o cosas. Los adjetivos dicen cómo son: en «perro pequeño», perro es sustantivo y pequeño es adjetivo.", [
("En «flor roja», el adjetivo es…", "roja", "flor", "ninguno"), ("¿Cuál es un sustantivo?", "pelota", "correr", "suave"), ("Completa: Las niñas ___.", "juegan", "juega", "jugamos"), ("¿Cuál es un nombre propio?", "Bogotá", "ciudad", "parque"), ("Elige la concordancia correcta.", "Los gatos blancos", "Los gato blanco", "Las gatos blanca")]),
3: ("Quién y qué hace", "El sujeto indica de quién se habla. El predicado expresa lo que se dice de él. En «Laura cuida plantas», Laura es el sujeto y cuida plantas es el predicado.", [
("En «Pedro dibuja un árbol», el sujeto es…", "Pedro", "dibuja", "un árbol"), ("El predicado de «El gato duerme» es…", "duerme", "El gato", "gato"), ("¿Qué verbo está en pasado?", "cantó", "canta", "cantará"), ("Completa: Mañana nosotros ___.", "viajaremos", "viajamos ayer", "viajó"), ("¿Qué palabra sustituye a «María»?", "ella", "ellos", "nosotros")]),
4: ("Conectamos ideas", "Porque indica causa, pero introduce contraste y después indica orden. Los signos de interrogación abren y cierran una pregunta en español.", [
("Completa: No salí ___ llovía.", "porque", "pero", "aunque"), ("¿Qué conector expresa contraste?", "pero", "después", "porque"), ("¿Qué pregunta está bien puntuada?", "¿Dónde vives?", "Dónde vives?", "¿Dónde vives."), ("¿Cuál oración contiene un adverbio de lugar?", "El libro está aquí.", "El libro es rojo.", "El libro pesa mucho."), ("¿Qué oración concuerda?", "Las aves vuelan.", "Las aves vuela.", "La aves vuelan.")]),
5: ("Precisión al escribir", "Un texto claro mantiene concordancia y tiempos verbales coherentes. La coma separa elementos de una lista y la tilde puede distinguir palabras: tú es pronombre; tu indica posesión.", [
("Elige la frase correcta.", "Tú tienes tu cuaderno.", "Tu tienes tú cuaderno.", "Tú tienes tú cuaderno."), ("¿Qué oración usa bien la coma?", "Compré pan, leche y arroz.", "Compré, pan leche y arroz.", "Compré pan leche, y, arroz."), ("Completa: Si tuviera tiempo, ___ más.", "leería", "leí", "leeré ayer"), ("¿Qué conector indica consecuencia?", "por eso", "sin embargo", "aunque"), ("¿Cuál oración mantiene el tiempo pasado?", "Llegó, saludó y se sentó.", "Llegó, saluda y se sentará.", "Llega, saludó y se sentará.")])},
"adventure": {
1: ("Un comienzo y un final", "Busca quién aparece, dónde está y qué hace. Para contar una historia, empieza por el inicio y termina con lo que ocurrió al final.", [
("¿Quién lleva la semilla?", "Lina", "un pez", "Tomás"), ("¿Dónde la planta?", "en una maceta", "en un zapato", "en una caja"), ("¿Qué hace después de plantar?", "la riega", "la tira", "la esconde"), ("¿Qué aparece al final?", "una planta", "un libro", "una pelota"), ("¿Qué título corresponde?", "La semilla de Lina", "El viaje del pez", "El libro perdido")]),
2: ("Ordenamos la aventura", "Primero presenta a los personajes; después cuenta lo que hacen; finalmente explica cómo termina. Usa estas palabras para ordenar tus ideas.", [
("¿Qué hace Lina primero?", "planta una semilla", "ve una planta", "regala flores"), ("¿Por qué la riega?", "para que crezca", "para secarla", "para esconderla"), ("¿Qué palabra indica el final?", "finalmente", "primero", "antes"), ("¿Dónde ocurre la historia?", "en el patio", "en el mar", "en el cine"), ("¿Qué describe mejor a Lina?", "cuidadosa", "desinteresada", "impaciente siempre")]),
3: ("Problema y solución", "El nudo presenta un problema; el desenlace muestra cómo se resuelve. Puedes reconocer a un personaje por sus acciones, aunque el texto no diga cómo es.", [
("¿Cuál es el problema?", "la tierra está seca", "se perdió la maceta", "no existe el patio"), ("¿Cómo lo resuelven?", "organizan turnos de riego", "rompen la maceta", "dejan de cuidar"), ("¿Qué hace Mateo?", "ayuda a regar", "esconde la semilla", "corta la planta"), ("¿Qué valor demuestra la solución?", "colaboración", "egoísmo", "indiferencia"), ("¿Qué parte muestra la solución?", "desenlace", "título", "inicio")]),
4: ("Inferimos con pistas", "Inferir es relacionar pistas para comprender algo que no se dice directamente. Diferencia una pista del texto de una idea que no tiene evidencia.", [
("¿Por qué Lina propone turnarse?", "para mantener el cuidado cada día", "para vender la maceta", "para evitar a Mateo"), ("¿Qué permite inferir que perseveraron?", "la cuidaron durante semanas", "la maceta era grande", "el patio tenía suelo"), ("¿Qué significa que el brote fue una recompensa?", "vieron el resultado de su esfuerzo", "recibieron dinero", "ganaron un trofeo"), ("¿Cuál es la idea central?", "el cuidado compartido permite crecer", "las plantas no necesitan agua", "Mateo perdió el patio"), ("¿Qué afirmación tiene evidencia?", "Mateo ayudó a cuidar la planta", "Lina compró cien macetas", "la planta creció en una hora")]),
5: ("Leemos con mirada crítica", "Distingue hechos, opiniones e inferencias. Resume sin inventar detalles y reconoce la intención: narrar, informar o convencer.", [
("¿Cuál es un hecho del relato?", "organizaron turnos de riego", "es la planta más hermosa del mundo", "todos deberían sembrar"), ("¿Qué oración expresa una opinión?", "Sembrar es la mejor diversión.", "Mateo ayudó a Lina.", "La tierra estaba seca."), ("La intención principal del relato es…", "narrar una experiencia de cuidado", "vender semillas", "dar cifras de cosechas"), ("¿Cuál es el mejor resumen?", "Dos niños se organizan para cuidar una planta y ven crecer un brote.", "Un niño compra un bosque.", "Una planta crece sin ayuda en un día."), ("¿Qué conclusión se apoya en el texto?", "la constancia y la colaboración ayudaron", "todas las semillas crecen igual", "las plantas nunca necesitan luz")])}
}


def curriculum_for_grade(unit, grade):
    grade = max(1, min(5, int(grade)))
    questions = []
    if unit in LANGUAGE:
        title, explanation, rows = LANGUAGE[unit][grade]
        result = {"lesson": [f"Grado {grade}.º · {title}", explanation,
            "Lee cada ejemplo y explica con tus palabras por qué elegiste tu respuesta. Si tienes dudas, vuelve a la lección."],
            "questions": [question(*row, index=i) for i, row in enumerate(rows)]}
        if unit == "adventure":
            result["passage"] = ("Lina está en el patio. Planta una semilla en una maceta y la riega. La cuida cada día. Al final aparece una planta." if grade <= 2 else
                "Lina plantó una semilla en el patio. Un día vio que la tierra estaba seca y pidió ayuda a Mateo. Organizaron turnos para regar sin encharcar y cuidaron la maceta durante semanas. Al ver un brote, Lina dijo: «Sembrar es la mejor diversión». El brote fue la recompensa de su constancia.")
        return result
    if unit == "patterns":
        steps = [1, 2, 5, 7, 10]
        step = steps[grade-1]
        for i in range(6):
            start = (i+1)*grade
            if grade == 5:
                seq = [start * 2**j for j in range(4)]; answer = seq[-1]*2
                wrong = [answer+2, seq[-1]+2]
            else:
                seq = [start+j*step for j in range(4)]; answer = seq[-1]+step
                wrong = [answer+1, answer-1]
            questions.append(question(f"¿Qué número sigue? {', '.join(map(str,seq))}, …", answer, *wrong, i))
        example = "3, 6, 12, 24: cada número se multiplica por 2; sigue 48." if grade==5 else f"2, {2+step}, {2+2*step}: sumamos {step} cada vez; sigue {2+3*step}."
        lesson = [f"Grado {grade}.º · Patrones numéricos", "Compara cada término con el anterior. Busca una regla que funcione en todos los pasos.", example, "Comprueba el siguiente número aplicando la misma regla. Luego inventa otra secuencia con esa regla."]
    elif unit == "market":
        for i in range(6):
            if grade == 1:
                a,b=i+2,3; prompt=f"Tienes {a} manzanas y recibes {b} más. ¿Cuántas tienes?"; answer=a+b; delta=1
            elif grade == 2:
                a,b=30+i*2,12+i; prompt=f"Hay {a} panes y se venden {b}. ¿Cuántos quedan?"; answer=a-b; delta=2
            elif grade == 3:
                a,b=3+i,4; prompt=f"Hay {a} bolsas con {b} naranjas cada una. ¿Cuántas naranjas hay?"; answer=a*b; delta=4
            elif grade == 4:
                b=3+i; a=b*6; prompt=f"Repartes {a} galletas entre {b} niños por igual. ¿Cuántas recibe cada uno?"; answer=6; delta=1
            else:
                a=2000+i*500; prompt=f"Un cuaderno cuesta {a} pesos y tiene 10 % de descuento. ¿Cuántos pesos pagas?"; answer=a*9//10; delta=100
            questions.append(question(prompt,answer,answer+delta,answer-delta,i))
        lesson=[f"Grado {grade}.º · Problemas cotidianos", ["Juntar cantidades se representa con una suma: 2 manzanas y 3 más son 5.", "Cuando se venden objetos, quedan menos: si hay 30 panes y vendes 12, quedan 18.", "Los grupos iguales se calculan multiplicando: 3 bolsas de 4 naranjas son 12 naranjas.", "Repartir por igual se calcula dividiendo: 24 galletas entre 4 niños son 6 para cada uno.", "El 10 % es una décima parte: el 10 % de 2000 es 200. Con ese descuento pagas 2000 − 200 = 1800 pesos."][grade-1], "Separa los datos, elige la operación y escribe la unidad. Comprueba si el resultado tiene sentido en la historia."]
    else:
        for i in range(6):
            a=i+3
            if grade==1: prompt=f"Una cinta mide {a} cm y otra {a+2} cm. ¿Cuánto mide la más larga?"; answer=a+2; wrong=[a,a+1]
            elif grade==2: prompt=f"Caminas {a} metros y después 2 metros más. ¿Cuántos metros recorres?"; answer=a+2; wrong=[a,a-2]
            elif grade==3: prompt=f"¿Cuántos centímetros hay en {a} metros?"; answer=a*100; wrong=[a*10,a*1000]
            elif grade==4: prompt=f"Un cuadrado tiene lados de {a} cm. ¿Cuál es su perímetro en cm?"; answer=a*4; wrong=[a*2,a*4+4]
            else: prompt=f"Un rectángulo mide {a} cm de largo y 4 cm de ancho. ¿Cuál es su área en cm²?"; answer=a*4; wrong=[a*4+1,a+4]
            questions.append(question(prompt,answer,*wrong,i))
        lesson=[f"Grado {grade}.º · Medimos el mundo", ["Si medimos con la misma unidad, el número mayor indica una longitud mayor: 5 cm es más largo que 3 cm.", "Para juntar recorridos en metros, suma sus medidas: 3 m + 2 m = 5 m.", "Un metro equivale a 100 centímetros. Para pasar metros a centímetros, multiplica por 100: 3 m = 300 cm.", "El perímetro es la suma de los lados. Un cuadrado de lado 3 cm tiene perímetro 3 + 3 + 3 + 3 = 12 cm.", "El área de un rectángulo es largo por ancho. Si mide 3 cm por 4 cm, ocupa 12 cm². El área mide superficie, no el borde."][grade-1], "Dibuja la situación y escribe siempre la unidad. Puedes practicar midiendo objetos con una regla."]
    return {"lesson": lesson, "questions": questions}
