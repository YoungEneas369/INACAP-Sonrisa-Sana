"""Diagrama de Base de Datos en 3 niveles — Clínica «Sonrisa Sana».

Genera 3 láminas independientes y espaciosas + 1 imagen combinada:
  10a_bd_nivel_conceptual.png
  10b_bd_nivel_relacional.png
  10c_bd_nivel_fisico.png
  10_modelo_bd_3_niveles.png   (las 3 apiladas, para Word / Excel)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
from PIL import Image

OUT = "/root/repo_inacap_sonrisa_sana/03_trabajo_final_optimizado/Academico/diagramas"
DPI = 150

AZUL = "#0F4C81"
CELESTE = "#0284C7"
MAGENTA = "#9D174D"
VERDE = "#047857"
GRIS = "#334155"
TXT = "#0F172A"


def lienzo(w, h, titulo, subtitulo, color):
    fig, ax = plt.subplots(figsize=(w, h), dpi=DPI)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    # Banda de título
    ax.add_patch(FancyBboxPatch((0.4, h - 1.35), w - 0.8, 1.0, boxstyle="round,pad=0.02,rounding_size=0.15",
                                facecolor=color, edgecolor=color))
    ax.text(0.8, h - 0.85, titulo, fontsize=20, fontweight="bold", color="white", va="center")
    ax.text(0.8, h - 1.75, subtitulo, fontsize=12.5, color=GRIS, va="center", style="italic")
    return fig, ax


def guardar(fig, nombre):
    path = os.path.join(OUT, nombre)
    fig.savefig(path, dpi=DPI, facecolor="white")
    plt.close(fig)
    return path


# ---------------------------------------------------------------------------
# NIVEL 1 — CONCEPTUAL (notación Chen: entidades + rombos de relación)
# ---------------------------------------------------------------------------
def entidad(ax, cx, cy, nombre, color, w=3.2, h=1.1):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor=color, edgecolor=color, lw=2))
    ax.text(cx, cy, nombre, ha="center", va="center", fontsize=15, fontweight="bold", color="white")


def rombo(ax, cx, cy, texto, w=2.6, h=1.2):
    pts = [(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)]
    ax.add_patch(Polygon(pts, closed=True, facecolor="#E0F2FE", edgecolor=CELESTE, lw=2.2))
    ax.text(cx, cy, texto, ha="center", va="center", fontsize=12.5, fontweight="bold", color="#075985")


def linea(ax, x1, y1, x2, y2, color=GRIS, lw=2.2, ls="-"):
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw, ls=ls, solid_capstyle="round", zorder=0)


def card(ax, x, y, txt, fs=14):
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, fontweight="bold", color=TXT,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GRIS, lw=1.2), zorder=5)


def nivel_conceptual():
    W, H = 20, 11
    fig, ax = lienzo(W, H, "NIVEL 1 · MODELO CONCEPTUAL",
                     "Qué datos maneja la clínica y cómo se relacionan (lenguaje del negocio, sin detalles técnicos)", CELESTE)

    y1, y2 = 6.6, 2.4
    xs = [2.6, 10.0, 17.4]  # Paciente, Cita, Odontólogo
    # Fila superior
    entidad(ax, xs[0], y1, "PACIENTE", CELESTE)
    entidad(ax, xs[1], y1, "CITA", AZUL)
    entidad(ax, xs[2], y1, "ODONTÓLOGO", CELESTE)
    rombo(ax, 6.3, y1, "reserva")
    rombo(ax, 13.7, y1, "atiende")
    linea(ax, xs[0] + 1.6, y1, 6.3 - 1.3, y1); linea(ax, 6.3 + 1.3, y1, xs[1] - 1.6, y1)
    linea(ax, xs[1] + 1.6, y1, 13.7 - 1.3, y1); linea(ax, 13.7 + 1.3, y1, xs[2] - 1.6, y1)
    card(ax, xs[0] + 2.05, y1 + 0.5, "1"); card(ax, xs[1] - 2.05, y1 + 0.5, "N")
    card(ax, xs[1] + 2.05, y1 + 0.5, "N"); card(ax, xs[2] - 2.05, y1 + 0.5, "1")

    # Fila inferior
    entidad(ax, xs[0], y2, "FICHA CLÍNICA", MAGENTA, w=3.6)
    entidad(ax, xs[1], y2, "RECORDATORIO", VERDE, w=3.6)
    entidad(ax, xs[2], y2, "HORARIO", CELESTE)
    ym = (y1 + y2) / 2
    for x, verbo, c_top, c_bot in [(xs[0], "posee", "1", "1"), (xs[1], "genera", "1", "N"), (xs[2], "define", "1", "N")]:
        rombo(ax, x, ym, verbo)
        linea(ax, x, y1 - 0.55, x, ym + 0.6)
        linea(ax, x, ym - 0.6, x, y2 + 0.55)
        card(ax, x + 0.45, y1 - 0.95, c_top)
        card(ax, x + 0.45, y2 + 0.95, c_bot)

    ax.text(W / 2, 0.65, "Se lee así:  un PACIENTE reserva N CITAS · un ODONTÓLOGO atiende N CITAS · "
            "cada CITA genera N RECORDATORIOS · cada PACIENTE posee 1 FICHA CLÍNICA",
            ha="center", va="center", fontsize=12.5, color=GRIS,
            bbox=dict(boxstyle="round,pad=0.45", fc="#F1F5F9", ec="#CBD5E1"))
    return guardar(fig, "10a_bd_nivel_conceptual.png")


# ---------------------------------------------------------------------------
# NIVEL 2 — RELACIONAL (tablas con PK / FK y líneas ortogonales)
# ---------------------------------------------------------------------------
LH = 0.42      # alto de cada atributo
HH = 0.65      # alto de cabecera
TW = 4.0       # ancho de tabla


def tabla(ax, x, ytop, nombre, attrs, color):
    h = HH + len(attrs) * LH + 0.15
    ax.add_patch(FancyBboxPatch((x, ytop - h), TW, h, boxstyle="round,pad=0.02,rounding_size=0.1",
                                facecolor="white", edgecolor=color, lw=2.2, zorder=2))
    ax.add_patch(FancyBboxPatch((x, ytop - HH), TW, HH, boxstyle="round,pad=0.02,rounding_size=0.1",
                                facecolor=color, edgecolor=color, lw=2.2, zorder=3))
    ax.text(x + TW / 2, ytop - HH / 2, nombre, ha="center", va="center", fontsize=14,
            fontweight="bold", color="white", zorder=4)
    for i, a in enumerate(attrs):
        tag, campo = a.split(" ", 1) if a[:2] in ("PK", "FK", "UQ") else ("", a)
        yy = ytop - HH - (i + 0.6) * LH
        col = {"PK": "#B91C1C", "FK": "#1D4ED8", "UQ": VERDE}.get(tag, GRIS)
        if tag:
            ax.text(x + 0.2, yy, tag, fontsize=10.5, fontweight="bold", color=col, va="center", zorder=4)
        ax.text(x + 0.85, yy, campo, fontsize=11.5, color=TXT, va="center", zorder=4,
                fontweight="bold" if tag == "PK" else "normal")
    return {"x": x, "top": ytop, "bot": ytop - h, "cx": x + TW / 2, "r": x + TW, "h": h}


def poli(ax, pts, color, lw=2.4, ls="-"):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=1, solid_joinstyle="round")


def nivel_relacional():
    W, H = 22, 15
    fig, ax = lienzo(W, H, "NIVEL 2 · MODELO RELACIONAL (3FN)",
                     "Tablas principales con claves primarias (PK), foráneas (FK) y únicas (UQ). "
                     "Modelo completo de 12 tablas: diagrama ER de Fernando (02_modelo_bd_er.png)", AZUL)

    cols = [0.8, 6.4, 12.0, 17.6]  # separación de 1.6 entre tablas
    top1, top2 = 12.3, 5.9

    pac = tabla(ax, cols[0], top1, "paciente", ["PK id_paciente", "UQ rut", "nombre / apellido",
                                                "telefono / prevision", "consentimiento_datos"], "#1E40AF")
    cit = tabla(ax, cols[1], top1, "cita", ["PK id_cita", "FK id_paciente", "FK id_odontologo",
                                            "fecha / hora_inicio", "estado", "UQ bloque_activo"], AZUL)
    odo = tabla(ax, cols[2], top1, "odontologo", ["PK id_odontologo", "FK id_especialidad",
                                                  "UQ reg_superint", "box_asignado"], AZUL)
    esp = tabla(ax, cols[3], top1, "especialidad", ["PK id_especialidad", "UQ nombre",
                                                    "duracion_est_min"], CELESTE)

    fic = tabla(ax, cols[0], top2, "ficha_clinica", ["PK id_ficha", "FK id_paciente (UQ)",
                                                     "antecedentes_enc", "alergias_enc"], MAGENTA)
    evo = tabla(ax, cols[1], top2, "evolucion_clinica", ["PK id_evolucion", "FK id_ficha",
                                                         "FK id_cita (UQ)", "diagnostico_enc"], MAGENTA)
    rec = tabla(ax, cols[2], top2, "recordatorio", ["PK id_recordatorio", "FK id_cita",
                                                    "canal (correo / WA)", "fecha_programada"], VERDE)
    hor = tabla(ax, cols[3], top2, "horario_odontologo", ["PK id_horario", "FK id_odontologo",
                                                          "dia_semana", "hora_inicio / fin"], CELESTE)

    yrow = top1 - HH - 0.6 * LH  # altura de la fila PK
    # paciente 1 —— N cita
    poli(ax, [(pac["r"], yrow), (cit["x"], yrow)], "#1E40AF")
    card(ax, pac["r"] + 0.35, yrow + 0.35, "1", 12); card(ax, cit["x"] - 0.35, yrow + 0.35, "N", 12)
    # odontologo 1 —— N cita
    poli(ax, [(odo["x"], yrow), (cit["r"], yrow)], AZUL)
    card(ax, odo["x"] - 0.35, yrow + 0.35, "1", 12); card(ax, cit["r"] + 0.35, yrow + 0.35, "N", 12)
    # especialidad 1 —— N odontologo
    poli(ax, [(esp["x"], yrow), (odo["r"], yrow)], CELESTE)
    card(ax, esp["x"] - 0.35, yrow + 0.35, "1", 12); card(ax, odo["r"] + 0.35, yrow + 0.35, "N", 12)

    # paciente 1 —— 1 ficha (vertical)
    poli(ax, [(pac["cx"], pac["bot"]), (fic["cx"], fic["top"])], MAGENTA)
    card(ax, pac["cx"] + 0.4, pac["bot"] - 0.4, "1", 12); card(ax, fic["cx"] + 0.4, fic["top"] + 0.4, "1", 12)
    # cita 1 —— 1 evolucion (vertical)
    poli(ax, [(cit["cx"] - 0.8, cit["bot"]), (evo["cx"] - 0.8, evo["top"])], MAGENTA)
    card(ax, cit["cx"] - 0.4, cit["bot"] - 0.4, "1", 12); card(ax, evo["cx"] - 0.4, evo["top"] + 0.4, "0..1", 12)
    # cita 1 —— N recordatorio (codo)
    ymid = (cit["bot"] + rec["top"]) / 2
    poli(ax, [(cit["cx"] + 1.0, cit["bot"]), (cit["cx"] + 1.0, ymid), (rec["cx"], ymid), (rec["cx"], rec["top"])], VERDE)
    card(ax, cit["cx"] + 1.4, cit["bot"] - 0.4, "1", 12); card(ax, rec["cx"] + 0.4, rec["top"] + 0.4, "N", 12)
    # odontologo 1 —— N horario (codo)
    ymid2 = ymid - 0.35
    poli(ax, [(odo["cx"] + 1.0, odo["bot"]), (odo["cx"] + 1.0, ymid2), (hor["cx"], ymid2), (hor["cx"], hor["top"])], CELESTE)
    card(ax, odo["cx"] + 1.4, odo["bot"] - 0.4, "1", 12); card(ax, hor["cx"] + 0.4, hor["top"] + 0.4, "N", 12)
    # ficha 1 —— N evolucion
    yf = top2 - HH - 0.6 * LH
    poli(ax, [(fic["r"], yf), (evo["x"], yf)], MAGENTA)
    card(ax, fic["r"] + 0.35, yf + 0.35, "1", 12); card(ax, evo["x"] - 0.35, yf + 0.35, "N", 12)

    # Leyenda
    ax.text(0.8, 0.75, "PK", fontsize=12, fontweight="bold", color="#B91C1C")
    ax.text(1.4, 0.75, "clave primaria", fontsize=12, color=GRIS)
    ax.text(4.0, 0.75, "FK", fontsize=12, fontweight="bold", color="#1D4ED8")
    ax.text(4.6, 0.75, "clave foránea", fontsize=12, color=GRIS)
    ax.text(7.2, 0.75, "UQ", fontsize=12, fontweight="bold", color=VERDE)
    ax.text(7.9, 0.75, "valor único", fontsize=12, color=GRIS)
    ax.text(10.6, 0.75, "Tablas magenta = datos médicos cifrados (AES-256), solo rol Odontólogo",
            fontsize=12, color=MAGENTA, style="italic")
    return guardar(fig, "10b_bd_nivel_relacional.png")


# ---------------------------------------------------------------------------
# NIVEL 3 — FÍSICO (SQL real del script sonrisa_sana_bd.sql)
# ---------------------------------------------------------------------------
def codigo(ax, x, y, w, h, titulo, color, lineas, nota):
    ax.add_patch(FancyBboxPatch((x, y - h), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                facecolor="#0F172A", edgecolor=color, lw=3))
    ax.add_patch(FancyBboxPatch((x, y - 0.85), w, 0.85, boxstyle="round,pad=0.02,rounding_size=0.15",
                                facecolor=color, edgecolor=color))
    ax.text(x + 0.35, y - 0.43, titulo, fontsize=15, fontweight="bold", color="white", va="center")
    for i, l in enumerate(lineas):
        ax.text(x + 0.4, y - 1.45 - i * 0.52, l, fontsize=12, family="monospace", color="#E2E8F0", va="center")
    ax.text(x + w / 2, y - h - 0.6, nota, ha="center", va="center", fontsize=12.5, color=GRIS, style="italic")


def nivel_fisico():
    W, H = 22, 10
    fig, ax = lienzo(W, H, "NIVEL 3 · MODELO FÍSICO (SQL)",
                     "Cómo se implementa en el motor de base de datos (script sonrisa_sana_bd.sql)", VERDE)
    top = 7.6
    codigo(ax, 0.8, top, 10.0, 5.6, "1) Evitar choques de horario", "#059669", [
        "bloque_activo VARCHAR(60)",
        "  GENERATED ALWAYS AS (",
        "    CASE WHEN estado IN ('pendiente',",
        "      'confirmada','atendida')",
        "    THEN CONCAT(id_odontologo,'_',",
        "               fecha,'_',hora_inicio)",
        "    END) STORED,",
        "CONSTRAINT uq_cita_sin_choque UNIQUE (bloque_activo)",
    ], "La BD rechaza dos citas activas en el mismo bloque del mismo odontólogo")
    codigo(ax, 11.2, top, 10.0, 5.6, "2) Proteger datos médicos", MAGENTA, [
        "CREATE TABLE ficha_clinica (",
        "  id_ficha INT AUTO_INCREMENT PRIMARY KEY,",
        "  id_paciente INT NOT NULL UNIQUE,",
        "  antecedentes_medicos_enc VARBINARY(1024),",
        "  alergias_enc VARBINARY(512),",
        "  CONSTRAINT fk_ficha_paciente FOREIGN KEY",
        "    (id_paciente) REFERENCES paciente(...)",
        ") ENGINE=InnoDB;",
    ], "Se guarda cifrado (AES-256); solo el Odontólogo puede descifrarlo")
    return guardar(fig, "10c_bd_nivel_fisico.png")


def combinar(paths):
    imgs = [Image.open(p).convert("RGB") for p in paths]
    w = max(i.width for i in imgs)
    gap = 60
    imgs = [i.resize((w, int(i.height * w / i.width))) if i.width != w else i for i in imgs]
    total = sum(i.height for i in imgs) + gap * (len(imgs) - 1)
    out = Image.new("RGB", (w, total), "white")
    y = 0
    for i in imgs:
        out.paste(i, (0, y))
        y += i.height + gap
    path = os.path.join(OUT, "10_modelo_bd_3_niveles.png")
    out.save(path, optimize=True)
    return path


if __name__ == "__main__":
    p = [nivel_conceptual(), nivel_relacional(), nivel_fisico()]
    for x in p:
        print("OK", x)
    print("OK", combinar(p))
