# Carpeta Académico — Entregables Oficiales INACAP
## Clínica Odontológica «Sonrisa Sana»

Esta carpeta reúne la totalidad de los documentos formales, diagramas y guías requeridos para la **Evaluación N° 1** de la asignatura **Modelamiento de Soluciones Informáticas (114-2-F2)**.

---

### 📄 Documentos Principales de Entrega

1. **[`Cristopher_Figueroa.docx`](./Cristopher_Figueroa.docx)**:
   - **Informe técnico oficial** para subir al Ambiente de Aprendizaje de INACAP.
   - Contiene portada formal, análisis crítico MoSCoW, 16 RF, 13 RNF (ISO 25010), Historias de Usuario Gherkin, especificación de Casos de Uso, Diccionario de Datos y los 10 diagramas integrados.
2. **[`Cristopher_Figueroa_Proyecto.xlsx`](./Cristopher_Figueroa_Proyecto.xlsx)**:
   - **Libro Excel de gestión del proyecto**, estructurado en 17 hojas idéntico al estándar oficial de la docente (`Huellitas`).
3. **[`sonrisa_sana_bd.sql`](./sonrisa_sana_bd.sql)**:
   - Script SQL físico ejecutable en MySQL/SQLite con la restricción `UNIQUE (bloque_activo)` para prevención de colisiones horarias.

---

### 📘 Guías de Estudio y Defensa Oral

- **[`GUIA_TECNICA_PASO_A_PASO.md`](./GUIA_TECNICA_PASO_A_PASO.md)**: Explicación conceptual y práctica de cada parte del sistema (para entenderlo a fondo).
- **[`GUIA_PRESENTACION_DEFENSA.md`](./GUIA_PRESENTACION_DEFENSA.md)**: Guion minuto a minuto, láminas y respuestas a las preguntas de la profesora Yaleni Gómez.
- **[`INFORME_AUDITORIA_Y_COMPARATIVA.md`](./INFORME_AUDITORIA_Y_COMPARATIVA.md)**: Matriz de evaluación contra la rúbrica oficial (60 puntos).

---

### 🖼️ Diagramas del Sistema (`diagramas/`)

- `01_casos_de_uso_general.png`: Diagrama de Casos de Uso UML 2.5 (Paciente, Secretaria, Odontólogo, Administrador).
- `02_modelo_bd_er.png`: Modelo Entidad-Relación Relacional en 3FN (12 tablas).
- `03_flujo_reserva_online.png`: Proceso TO-BE de Reserva Online.
- `04_flujo_gestion_secretaria.png`: Proceso TO-BE de Gestión y Cancelación de Citas en ≤ 2 clics.
- `05_flujo_atencion_y_recordatorios.png`: Proceso TO-BE de Atención Médica y Scheduler de Recordatorios.
- `06_mockup_reserva_online.png`: Wireframe / Mockup de Reserva en 3 pasos.
- `07_mockup_agenda_secretaria.png`: Wireframe / Mockup de Panel de Agenda.
- `08_mockup_ficha_clinica.png`: Wireframe / Mockup de Ficha Médica Cifrada con RBAC.
- `09_tablero_kanban.png`: Tablero Kanban con límites de trabajo en curso (WIP).
- `10_modelo_bd_3_niveles.png`: **Los 3 Niveles de Base de Datos:** Conceptual/Lógico, Relacional (3FN) y Físico (DDL SQL).
