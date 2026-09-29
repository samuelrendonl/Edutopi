"""Genera las diez guías PDF desde el mismo catálogo que usa la aplicación."""
from pathlib import Path
from html import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from app.learning_content import ACTIVITIES, public_activity

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Frontend" / "public" / "guias"
OUT.mkdir(parents=True, exist_ok=True)
font = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont("DV", font))
pdfmetrics.registerFont(TTFont("DVB", font_bold))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB")
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverX", fontName="DVB", fontSize=26, leading=33, textColor=colors.HexColor("#25377d"), alignment=TA_CENTER, spaceAfter=24))
styles.add(ParagraphStyle(name="H1X", fontName="DVB", fontSize=16, leading=22, textColor=colors.HexColor("#25377d"), spaceBefore=14, spaceAfter=10))
styles.add(ParagraphStyle(name="H2X", fontName="DVB", fontSize=11, leading=16, textColor=colors.HexColor("#374395"), spaceBefore=10, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyX", fontName="DV", fontSize=9.5, leading=15, spaceAfter=9))
styles.add(ParagraphStyle(name="SmallX", fontName="DV", fontSize=8, leading=12, textColor=colors.HexColor("#53617c"), spaceAfter=5))

def P(text, style="BodyX"):
    return Paragraph(escape(str(text)), styles[style])

def footer(canvas, document):
    canvas.saveState()
    canvas.setFont("DV", 8)
    canvas.setFillColor(colors.HexColor("#66728c"))
    canvas.drawString(42, 30, "EDUTOPIA · Guía de aprendizaje")
    canvas.drawRightString(A4[0] - 42, 30, f"Página {document.page}")
    canvas.restoreState()

for subject, filename in [("Matemáticas", "Matematicas"), ("Lengua Castellana", "Lengua_Castellana")]:
    for grade in range(1, 6):
        lessons = [public_activity(item, grade) for item in ACTIVITIES if item["subject"] == subject and item["kind"] == "Aprendizaje"]
        output = OUT / f"Guia_{filename}_{grade}.pdf"
        story = [Spacer(1, 45), P("EDUTOPIA", "CoverX"), P(f"Guía de {subject}", "CoverX"), P(f"{grade}.º grado · Primaria", "H1X"), Spacer(1, 20), P(f"Nombre: {'_'*44}"), P(f"Esta guía reúne las {len(lessons)} lecciones que aparecen en Edutopia para {grade}.º grado. Puedes leer cada explicación, resolver las preguntas y luego entrar a la actividad digital para registrar tu avance."), P("Cómo estudiar: lee la lección, trabaja un ejemplo, responde sin mirar las opciones primero y revisa tus ideas. Pide ayuda si algo no se entiende; aprender también es volver a intentarlo."), PageBreak()]
        story += [P("Contenido", "H1X")]
        for i, lesson in enumerate(lessons, 1):
            story.append(P(f"{i}. {lesson['title']}", "BodyX"))
        story.append(PageBreak())
        for i, lesson in enumerate(lessons, 1):
            story += [P(f"Lección {i}. {lesson['title']}", "H1X"), P(lesson["description"]), P("Lo que vas a aprender", "H2X")]
            if lesson.get("passage"):
                story += [P("Lectura de la actividad", "H2X"), P(lesson["passage"])]
            for n, line in enumerate(lesson.get("lesson", []), 1):
                story.append(P(f"{n}. {line}"))
            story += [P("Practica a tu ritmo", "H2X"), P("Lee cada reto, piensa en una estrategia y explica tu respuesta. En la plataforma podrás elegir una opción y comprobar tu resultado.")]
            for n, q in enumerate(lesson["questions"], 1):
                story += [P(f"{n}. {q['prompt']}", "BodyX"), P("   ".join(f"{chr(65+j)}) {option}" for j, option in enumerate(q["options"])), "SmallX"), P("Respuesta y procedimiento: __________________________________________________", "SmallX")]
            story += [P("Reflexiono", "H2X"), P("¿Qué aprendí? ¿Qué estrategia me ayudó? ¿Qué necesito practicar otra vez?"), P("________________________________________________________________________"), Spacer(1, 12)]
            if i != len(lessons): story.append(PageBreak())
        doc = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=42, rightMargin=42, topMargin=48, bottomMargin=48, title=f"Edutopia: {subject} {grade}.º grado")
        doc.build(story, onFirstPage=footer, onLaterPages=footer)
        print(output.name, output.stat().st_size)
