# Proyecto Sonrisa Sana — Modelamiento de Soluciones Informáticas (INACAP)

Repositorio oficial del proyecto de modelamiento y desarrollo para la **Clínica Odontológica «Sonrisa Sana»**, correspondiente a la **Evaluación N° 1 (Unidad 1 - 20%)** de la carrera de Ingeniería en Informática / Analista Programador en **INACAP**.

**Docente:** Yaleni Gómez Peña  
**Integrantes:**
- Christopher D. Figueroa Arthur (Líder Técnico / QA)
- Fernando A. Durán Leiva (Scrum Master / BD)
- Francisco A. Lara Yévenes (Analista UX / Funcional)

---

## 📌 ¿Qué se agregó en esta versión optimizada y dónde encontrarlo?

Para facilitar la revisión tanto de la docente como de los compañeros del equipo, aquí está el resumen de las mejoras añadidas:

| Componente Agregado | ¿Para qué sirve? | ¿Dónde está en el proyecto? |
| :--- | :--- | :--- |
| 📄 **Informe Word** (`Cristopher_Figueroa.docx`) | Basado en el informe de Fernando. Se agregó: criterios Gherkin, ficha del CU03, diccionario de datos, BD en 3 niveles y anexo de pruebas. | [`Academico/Cristopher_Figueroa.docx`](./03_trabajo_final_optimizado/Academico/Cristopher_Figueroa.docx) |
| 📊 **Libro Excel** (`Cristopher_Figueroa_Proyecto.xlsx`) | Mismo libro de 17 hojas de Fernando (ya seguía la plantilla `Huellitas`). Cambios: nombre `nombre_Apellido` y los diagramas de BD en 3 niveles en la hoja «Modelo BD». | [`Academico/Cristopher_Figueroa_Proyecto.xlsx`](./03_trabajo_final_optimizado/Academico/Cristopher_Figueroa_Proyecto.xlsx) |
| 🗄️ **BD en 3 niveles** (`10a`, `10b`, `10c`) | **Criterio 1.1.4:** 1) Conceptual (entidades y rombos de relación), 2) Relacional 3FN (PK/FK), 3) Físico (SQL anti-choques y AES-256). El diagrama ER de 12 tablas de Fernando se mantiene. | [`Academico/diagramas/`](./03_trabajo_final_optimizado/Academico/diagramas) |
| 📘 **Guía Técnica Paso a Paso** (`GUIA_TECNICA_PASO_A_PASO.md`) | Explicación didáctica y simple de cómo funciona cada pieza (UML, BD, seguridad AES-256) para entender el proyecto al 100%. | [`Academico/GUIA_TECNICA_PASO_A_PASO.md`](./03_trabajo_final_optimizado/Academico/GUIA_TECNICA_PASO_A_PASO.md) |
| 🎤 **Guion de Defensa Oral** (`GUIA_PRESENTACION_DEFENSA.md`) | Libreto minuto a minuto (12-15 min) para la disertación grupal, diapositivas recomendadas y respuestas a preguntas de la profesora. | [`Academico/GUIA_PRESENTACION_DEFENSA.md`](./03_trabajo_final_optimizado/Academico/GUIA_PRESENTACION_DEFENSA.md) |
| ⚖️ **Informe de Auditoría y Rúbrica** (`INFORME_AUDITORIA_Y_COMPARATIVA.md`) | Comparativa detallada entre la versión inicial (6.3) y la versión optimizada (7.0) desglosando los 60 puntos de la pauta. | [`Academico/INFORME_AUDITORIA_Y_COMPARATIVA.md`](./03_trabajo_final_optimizado/Academico/INFORME_AUDITORIA_Y_COMPARATIVA.md) |
| ⚙️ **Configuración de Pruebas** (`pytest.ini`) | Resuelve errores de importación y permite ejecutar todas las pruebas automáticas simplemente escribiendo `pytest`. | [`pytest.ini`](./03_trabajo_final_optimizado/pytest.ini) |
| 🚀 **Script de Inicio Rápido** (`iniciar_sistema.sh`) | Script ejecutable para levantar el servidor web en Linux / Android con un solo clic. | [`iniciar_sistema.sh`](./03_trabajo_final_optimizado/iniciar_sistema.sh) |

| 🖼️ **Fotos comparativas** (5 láminas) | Resumen visual de qué se mantuvo y qué se agregó. | [`05_evaluacion_comparativa/fotos/`](./05_evaluacion_comparativa/fotos) |

---

## 📁 Estructura del Repositorio

1. **[`01_requisitos/`](./01_requisitos)**:
   - Pauta de evaluación oficial (`1 - Descripción.docx`).
   - Instrucciones institucionales (`2 - Instrucciones.pdf`).
   - Rúbrica detallada de calificación (`3 - Rubrica.docx`).
   - Libro Excel modelo entregado por la docente (`Huellitas_Proyecto_SCRUM.xlsx`).

2. **[`02_trabajo_fernando/`](./02_trabajo_fernando)**:
   - Trabajo base y avances desarrollados inicialmente por Fernando Durán.

3. **[`03_trabajo_final_optimizado/`](./03_trabajo_final_optimizado)**:
   - **Versión completa y definitiva para la entrega y presentación:**
     - `Academico/`: Documentos formales (`.docx`, `.xlsx`), guías explicativas, SQL y los 10 diagramas.
     - `app/`: Backend en FastAPI con control de acceso RBAC y cifrado AES-256.
     - `static/`: Frontend web responsivo para pacientes y secretaría.
     - `tests/`: Pruebas automatizadas unitarias con Pytest.

4. **[`04_guias_y_explicaciones/`](./04_guias_y_explicaciones)**:
   - Copia de acceso rápido de la Guía Técnica Paso a Paso y el Guion de Presentación Oral.

5. **[`05_evaluacion_comparativa/`](./05_evaluacion_comparativa)**:
   - Copia de acceso rápido de la matriz de auditoría técnica y rúbrica oficial.

---

## 🚀 Ejecución Rápida del Prototipo

```bash
cd 03_trabajo_final_optimizado
python run_server.py
```
Abre en tu navegador: `http://127.0.0.1:8000`

### Ejecución de Pruebas Automatizadas
```bash
cd 03_trabajo_final_optimizado
pytest
```
*Validación al 100% de no-colisión de horas, reprogramación y seguridad RBAC con cifrado AES-256.*
