# Proyecto Sonrisa Sana — Modelamiento de Soluciones Informáticas (INACAP)

Repositorio oficial del proyecto de modelamiento y desarrollo para la **Clínica Odontológica «Sonrisa Sana»**, correspondiente a la **Evaluación N° 1 (Unidad 1 - 20%)** de la carrera de Ingeniería en Informática / Analista Programador en **INACAP**.

**Docente:** Yaleni Gómez Peña  
**Integrantes:**
- Christopher D. Figueroa Arthur (Líder Técnico / QA)
- Fernando A. Durán Leiva (Scrum Master / BD)
- Francisco A. Lara Yévenes (Analista UX / Funcional)

---

## 📁 Estructura del Repositorio

El repositorio está organizado en las 5 carpetas solicitadas para máxima claridad y trazabilidad académica:

1. **[`01_requisitos/`](./01_requisitos)**:
   - Contiene la pauta de evaluación oficial (`1 - Evaluación Sumativa 5 - Descripción.docx`).
   - Las instrucciones institucionales (`2 - Evaluación Sumativa 5 - Instrucciones.pdf`).
   - La rúbrica detallada de calificación (`3 - Evaluación Sumativa 5 - Rubrica.docx`).
   - El libro Excel de ejemplo oficial entregado por la docente (`Huellitas_Proyecto_SCRUM`).

2. **[`02_trabajo_fernando/`](./02_trabajo_fernando)**:
   - El trabajo base y avances desarrollados por Fernando Durán (Informe inicial, Excel, diagramas y primera versión del prototipo).

3. **[`03_trabajo_final_optimizado/`](./03_trabajo_final_optimizado)**:
   - **Documentos definitivos para entrega institucional**:
     - `Cristopher_Figueroa.docx`: Informe técnico formal con formato oficial INACAP, tablas MoSCoW, historias Gherkin, especificación de Casos de Uso y los 10 diagramas integrados.
     - `Cristopher_Figueroa_Proyecto.xlsx`: Libro Excel de 17 pestañas estandarizado según la pauta de la docente.
     - `diagramas/`: Los 10 diagramas UML, de Base de Datos (en 3 niveles), Flujos TO-BE, Mockups y Tablero Kanban en alta resolución.
     - `Sistema/`: Prototipo web operativo desarrollado en **FastAPI + SQLite + Tailwind CSS**, con pruebas automatizadas (`pytest`) pasando al 100%.

4. **[`04_guias_y_explicaciones/`](./04_guias_y_explicaciones)**:
   - `GUIA_TECNICA_PASO_A_PASO.md`: Documento didáctico que explica en detalle el porqué de cada decisión técnica, arquitectónica y metodológica para entender el proyecto a fondo.
   - `GUIA_PRESENTACION_DEFENSA.md`: Guion completo minuto a minuto para la defensa oral (12-15 min), láminas recomendadas, demostración en vivo y banco de preguntas difíciles con respuestas para asegurar la **Nota 7.0**.

5. **[`05_evaluacion_comparativa/`](./05_evaluacion_comparativa)**:
   - `INFORME_AUDITORIA_Y_COMPARATIVA.md`: Matriz de cumplimiento de la rúbrica oficial, contraste entre el trabajo inicial y la versión final optimizada, y resolución de brechas técnicas.

---

## 🚀 Ejecución Rápida del Prototipo

```bash
cd 03_trabajo_final_optimizado/Sistema
python run_server.py
```
Abre en tu navegador: `http://127.0.0.1:8000`

### Ejecución de Pruebas Automatizadas
```bash
cd 03_trabajo_final_optimizado/Sistema
pytest
```
*Validación al 100% de no-colisión de horas, reprogramación y seguridad RBAC con cifrado AES-256.*
