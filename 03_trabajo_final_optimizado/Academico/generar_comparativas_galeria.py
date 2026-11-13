"""Infografías comparativas (1920x1080) — Proyecto «Sonrisa Sana».

Diseño: poco texto, letra grande, mucho espacio. Contenido verificado contra los
archivos reales de Fernando (02_trabajo_fernando) y la versión final.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
DIAG = "/root/repo_inacap_sonrisa_sana/03_trabajo_final_optimizado/Academico/diagramas"
OUTS = [
    "/sdcard/Pictures/Comparativa_INACAP",
    "/sdcard/Download/INACAP_Sonrisa_Sana/Comparativa_Fotos",
    "/root/repo_inacap_sonrisa_sana/05_evaluacion_comparativa/fotos",
]
CAMERA = "/sdcard/DCIM/Camera"
for d in OUTS:
    os.makedirs(d, exist_ok=True)

B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
M = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


BG = (246, 248, 251)
INK = (15, 23, 42)
MUTED = (71, 85, 105)
BLUE = (15, 76, 129)
BLUE_L = (226, 236, 247)
GREEN = (4, 120, 87)
GREEN_L = (220, 245, 234)
AMBER = (180, 83, 9)
WHITE = (255, 255, 255)
LINE = (203, 213, 225)


def base(n, titulo, sub):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((90, 60), f"{n} / 5", font=f(B, 26), fill=BLUE)
    d.text((90, 100), titulo, font=f(B, 56), fill=INK)
    d.text((90, 178), sub, font=f(R, 28), fill=MUTED)
    d.line([(90, 235), (W - 90, 235)], fill=LINE, width=3)
    return img, d


def panel(d, x, y, w, h, titulo, color, fondo):
    d.rounded_rectangle([x, y, x + w, y + h], radius=28, fill=WHITE, outline=LINE, width=2)
    d.rounded_rectangle([x, y, x + w, y + 78], radius=28, fill=fondo)
    d.rectangle([x, y + 50, x + w, y + 78], fill=fondo)
    d.text((x + 40, y + 20), titulo, font=f(B, 32), fill=color)


def check(d, x, y, color):
    d.ellipse([x, y, x + 34, y + 34], fill=color)
    d.line([(x + 8, y + 18), (x + 15, y + 25), (x + 27, y + 10)], fill=WHITE, width=5)


def plus(d, x, y, color):
    d.ellipse([x, y, x + 34, y + 34], fill=color)
    d.line([(x + 17, y + 8), (x + 17, y + 26)], fill=WHITE, width=5)
    d.line([(x + 8, y + 17), (x + 26, y + 17)], fill=WHITE, width=5)


def items(d, x, y, lista, icon, color, size=30, gap=78, maxw=None):
    fnt = f(R, size)
    for t in lista:
        icon(d, x, y + 2, color)
        d.text((x + 56, y), t, font=fnt, fill=INK)
        y += gap
    return y


def pegar(img, path, box, crop=None):
    im = Image.open(path).convert("RGB")
    if crop:
        cw, ch = im.size
        im = im.crop((int(crop[0] * cw), int(crop[1] * ch), int(crop[2] * cw), int(crop[3] * ch)))
    x, y, w, h = box
    im.thumbnail((w, h), Image.LANCZOS)
    px = x + (w - im.width) // 2
    py = y + (h - im.height) // 2
    img.paste(im, (px, py))
    ImageDraw.Draw(img).rounded_rectangle([px - 2, py - 2, px + im.width + 2, py + im.height + 2],
                                          radius=6, outline=LINE, width=2)


def guardar(img, nombre, cam):
    for d in OUTS:
        img.save(os.path.join(d, nombre))
    if os.path.isdir(CAMERA):
        img.save(os.path.join(CAMERA, cam))
    print("OK", nombre)


# 1 ─ Base de datos ------------------------------------------------------------
def foto1():
    img, d = base(1, "Base de datos", "La pauta pide el diagrama en 3 niveles: Lógico, Relacional y Físico")
    pw, ph, y = 840, 760, 280
    panel(d, 90, y, pw, ph, "SE MANTIENE  ·  Diagrama de Fernando", BLUE, BLUE_L)
    pegar(img, os.path.join(DIAG, "02_modelo_bd_er.png"), (120, y + 105, pw - 60, 450), crop=(0.02, 0.345, 0.45, 0.585))
    items(d, 130, y + 600, ["Modelo ER completo: 12 tablas",
                             "Se usa tal cual en el informe (Figura 6)"], check, BLUE, size=28, gap=60)

    x2 = 90 + pw + 60
    panel(d, x2, y, pw, ph, "SE AGREGA  ·  Los 3 niveles", GREEN, GREEN_L)
    pegar(img, os.path.join(DIAG, "10a_bd_nivel_conceptual.png"), (x2 + 30, y + 105, pw - 60, 450), crop=(0.0, 0.33, 0.61, 0.83))
    items(d, x2 + 40, y + 600, ["Conceptual  ·  Relacional  ·  Físico (SQL)",
                                 "Figuras 5a, 5b y 5c del informe"], plus, GREEN, size=28, gap=60)
    guardar(img, "01_comparativa_base_de_datos.png", "IMG_20261113_01_Comparativa_Base_Datos.png")


# 2 ─ Informe Word -------------------------------------------------------------
def foto2():
    img, d = base(2, "Informe Word", "Se partió del informe de Fernando y se completaron las secciones que pide la rúbrica")
    pw, ph, y = 840, 760, 280
    panel(d, 90, y, pw, ph, "YA ESTABA  ·  Informe de Fernando", BLUE, BLUE_L)
    items(d, 130, y + 130, ["16 RF y 13 RNF (ISO/IEC 25010)",
                             "Priorización MoSCoW",
                             "Casos de uso, mockups y flujos",
                             "Kanban y Carta Gantt",
                             "Los 3 integrantes en la portada"], check, BLUE)
    d.text((130, y + 590), "5 tablas  ·  9 figuras", font=f(B, 40), fill=BLUE)

    x2 = 90 + pw + 60
    panel(d, x2, y, pw, ph, "SE AGREGA  ·  Versión final", GREEN, GREEN_L)
    items(d, x2 + 40, y + 130, ["Criterios Gherkin (Dado/Cuando/Entonces)",
                                 "Ficha detallada del caso de uso CU03",
                                 "Diccionario de datos",
                                 "BD en 3 niveles (Figuras 5a-5c)",
                                 "Anexo de pruebas automáticas"], plus, GREEN)
    d.text((x2 + 40, y + 590), "8 tablas  ·  12 figuras", font=f(B, 40), fill=GREEN)
    guardar(img, "02_comparativa_informe_word.png", "IMG_20261113_02_Comparativa_Word.png")


# 3 ─ Excel --------------------------------------------------------------------
def foto3():
    img, d = base(3, "Libro Excel", "El Excel de Fernando ya tenía las 17 hojas de la plantilla de la profesora")
    pw, ph, y = 840, 760, 280
    panel(d, 90, y, pw, ph, "YA ESTABA  ·  17 hojas", BLUE, BLUE_L)
    d.text((130, y + 120), "17", font=f(B, 150), fill=BLUE)
    d.text((340, y + 175), "hojas, igual que la\nplantilla «Huellitas»", font=f(R, 32), fill=INK, spacing=10)
    items(d, 130, y + 360, ["Requerimientos, HU y Backlog",
                             "Tareas, Carta Gantt y Kanban",
                             "Casos de uso, BD, flujos y mockups"], check, BLUE)

    x2 = 90 + pw + 60
    panel(d, x2, y, pw, ph, "SE AJUSTA", GREEN, GREEN_L)
    items(d, x2 + 40, y + 130, ["Nombre exigido: nombre_Apellido",
                                 "Hoja «Modelo BD»: + 3 niveles de BD"], plus, GREEN)
    items(d, x2 + 40, y + 286, ["Todo lo demás se mantiene igual"], check, BLUE)
    d.text((x2 + 40, y + 520), "Cristopher_Figueroa_Proyecto.xlsx", font=f(M, 30), fill=GREEN)
    guardar(img, "03_comparativa_libro_excel.png", "IMG_20261113_03_Comparativa_Excel.png")


# 4 ─ Software -----------------------------------------------------------------
def terminal(d, x, y, w, h, lineas):
    d.rounded_rectangle([x, y, x + w, y + h], radius=20, fill=(15, 23, 42))
    for i, c in enumerate([(239, 68, 68), (234, 179, 8), (34, 197, 94)]):
        d.ellipse([x + 24 + i * 34, y + 22, x + 46 + i * 34, y + 44], fill=c)
    yy = y + 80
    for t, col in lineas:
        d.text((x + 34, yy), t, font=f(M, 28), fill=col)
        yy += 52


def foto4():
    img, d = base(4, "Aplicación y pruebas", "El código de la app (FastAPI) NO se modificó. Solo se agregó configuración")
    pw, ph, y = 840, 760, 280
    panel(d, 90, y, pw, ph, "ANTES", AMBER, (254, 243, 199))
    terminal(d, 130, y + 120, pw - 80, 300, [("$ pytest", (226, 232, 240)),
                                             ("ModuleNotFoundError:", (248, 113, 113)),
                                             ("No module named 'app'", (248, 113, 113))])
    d.text((130, y + 470), "Las pruebas no se podían\nejecutar directamente", font=f(R, 32), fill=INK, spacing=12)

    x2 = 90 + pw + 60
    panel(d, x2, y, pw, ph, "DESPUÉS", GREEN, GREEN_L)
    terminal(d, x2 + 40, y + 120, pw - 80, 300, [("$ pytest", (226, 232, 240)),
                                                 ("3 passed", (74, 222, 128)),
                                                 ("(choques · secretaría · RBAC)", (148, 163, 184))])
    items(d, x2 + 40, y + 470, ["pytest.ini  (arregla la ruta)",
                                 "iniciar_sistema.sh  (abre la app)"], plus, GREEN)
    guardar(img, "04_comparativa_software_y_pruebas.png", "IMG_20261113_04_Comparativa_Software.png")


# 5 ─ Resumen por criterio -----------------------------------------------------
def foto5():
    img, d = base(5, "Resumen por criterio de la rúbrica", "Qué se completó en cada criterio (60 puntos en total)")
    filas = [
        ("1.1.1", "Toma de requerimientos", "Ya cumplía", None),
        ("1.1.2", "Análisis / Historias de usuario", "Ya cumplía", "+ criterios Gherkin"),
        ("1.1.3", "Casos de uso y mockups", "Ya cumplía", "+ ficha CU03"),
        ("1.1.4", "Base de datos", "Faltaban niveles", "+ 3 niveles explícitos"),
        ("1.1.5", "Diagramas de flujo", "Ya cumplía", None),
        ("1.1.6", "Informe y Kanban", "Ya cumplía", "+ nombre_Apellido, anexo"),
    ]
    x0, y0, rh = 90, 280, 112
    cols = [x0 + 30, x0 + 200, x0 + 900, x0 + 1260]
    d.text((cols[0], y0), "Criterio", font=f(B, 26), fill=MUTED)
    d.text((cols[2], y0), "Trabajo de Fernando", font=f(B, 26), fill=MUTED)
    d.text((cols[3], y0), "Qué se agregó", font=f(B, 26), fill=MUTED)
    y = y0 + 50
    for cod, nom, antes, add in filas:
        d.rounded_rectangle([x0, y, W - 90, y + rh - 16], radius=18, fill=WHITE, outline=LINE, width=2)
        cy = y + (rh - 16) // 2
        d.text((cols[0], cy - 18), cod, font=f(B, 32), fill=BLUE)
        d.text((cols[1], cy - 18), nom, font=f(R, 32), fill=INK)
        if antes == "Ya cumplía":
            check(d, cols[2], cy - 17, BLUE)
            d.text((cols[2] + 50, cy - 17), antes, font=f(R, 30), fill=INK)
        else:
            d.ellipse([cols[2], cy - 17, cols[2] + 34, cy + 17], fill=AMBER)
            d.text((cols[2] + 12, cy - 16), "!", font=f(B, 28), fill=WHITE)
            d.text((cols[2] + 50, cy - 17), antes, font=f(R, 30), fill=AMBER)
        if add:
            d.text((cols[3], cy - 17), add, font=f(B, 30), fill=GREEN)
        else:
            d.text((cols[3], cy - 17), "—", font=f(R, 30), fill=MUTED)
        y += rh
    guardar(img, "05_resumen_rubrica_general.png", "IMG_20261113_05_Comparativa_Rubrica.png")


if __name__ == "__main__":
    for fn in (foto1, foto2, foto3, foto4, foto5):
        fn()
