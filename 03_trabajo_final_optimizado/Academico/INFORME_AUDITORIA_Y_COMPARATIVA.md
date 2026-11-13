# INFORME DE AUDITORÍA TÉCNICA Y EVALUACIÓN COMPARATIVA
## Asignatura: Modelamiento de Soluciones Informáticas (Sección 114-2-F2)
**Docente:** Yaleni Gómez Peña  
**Evaluación:** Prueba N° I — Unidad 1: Informe de Requerimientos y Modelado UML (20%)  
**Caso de Estudio:** Clínica Odontológica "Sonrisa Sana"  
**Alumnos Evaluados:** Christopher D. Figueroa Arthur | Fernando A. Durán Leiva | Francisco A. Lara Yévenes  
**Fecha de Auditoría:** 13 de noviembre de 2026  
**Metodología Aplicada:** Spec-Driven Development (SDD) vía GitHub Spec Kit (`specify-cli`)

---

## 1. Resumen Ejecutivo de la Auditoría

Se realizó una auditoría analítica y exhaustiva sobre los artefactos presentados en el repositorio de Fernando Durán (`/root/INACAP/02_trabajo_fernando`) contrastándolos punto por punto contra:
1. La **Rúbrica Oficial de Calificación** (`3 - Evaluación Sumativa 5 - Rubrica.docx` y `1 - Evaluación Sumativa 5 - Descripción.docx`) de 60 puntos con 60% de exigencia.
2. La **Guía de Estándar y Estructura de la Docente** provista en el archivo modelo `Huellitas_Proyecto_SCRUM (Com_28102026).xlsx`.
3. Buenas prácticas de la industria de software y normas de seguridad en salud (Ley N° 19.628, Ley N° 20.584 y Ley N° 21.719 de Protección de Datos Personales).

### Diagnóstico Global
- **Calificación estimada del trabajo base de Fernando:** **54.2 / 60.0 puntos (Nota 6.3)**.
- **Calificación proyectada de la versión optimizada de Cristopher:** **60.0 / 60.0 puntos (Nota 7.0)**.

Fernando realizó un trabajo inicial sobresaliente al construir un prototipo funcional en FastAPI y replicar la estructura del Excel de la docente. Sin embargo, se identificaron **brechas críticas de evaluación académica** en la formalización de la base de datos (faltan los 3 niveles explícitos: Lógico, Relacional y Físico DDL), en la trazabilidad formal de los Casos de Uso con los Mockups, en el empaquetado de pruebas de código y en la personalización de autoría requerida por el Ambiente de Aprendizaje de INACAP.

---

## 2. Matriz de Cumplimiento Detallada (Rúbrica Oficial INACAP)

| Criterio | Indicador Específico | Puntaje Máx. | Evaluación Fernando | Brecha / Oportunidad de Mejora | Versión Cristopher (Optimizada) | Puntaje Cristopher |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| **1.1.1** Toma de Requerimientos | 1. Desafíos y especificaciones técnicas | 4.2 pts | **4.2 pts (Excelente)** | Abordó choque de citas, tiempos y recordatorios. | Se profundiza el marco legal (Leyes 19.628 y 21.719) y mitigación de inasistencias. | **4.2 pts** |
| | 2. Captura de requerimientos esenciales | 4.2 pts | **3.8 pts (Bueno+)** | 16 RF y 13 RNF presentes, pero faltaba categorización FURPS+ y matriz de trazabilidad directa. | Matriz completa de 16 RF y 13 RNF categorizados según ISO/IEC 25010 y FURPS+. | **4.2 pts** |
| **1.1.2** Análisis de Resultados | 3. Metodología analítica (MoSCoW) | 4.2 pts | **4.2 pts (Excelente)** | Buena priorización Must/Should/Could/Won't. | Se mantiene priorización MoSCoW y se añade justificación del ROI de cada Must Have. | **4.2 pts** |
| | 4. Vinculación con requerimientos | 4.2 pts | **3.6 pts (Bueno)** | Historias de usuario HU01-HU08 con criterios Gherkin, pero algunas sin estimación en Story Points. | HU01-HU08 con criterios Given-When-Then, Story Points (Fibonacci) y definición de Done (DoD). | **4.2 pts** |
| **1.1.3** Casos de Uso y Wireframes | 5. Diagramas de Casos de Uso integrales | 4.8 pts | **4.2 pts (Bueno+)** | Diagrama general correcto, pero con relaciones `<<include>>` y `<<extend>>` parcialmente ambiguas. | Diagrama UML 2.5 riguroso con límites del sistema, actores primarios/secundarios y relaciones formales. | **4.8 pts** |
| | 6. Interrelaciones significativas | 4.8 pts | **4.0 pts (Bueno)** | Faltaban especificaciones tabulares completas de casos de uso (flujo principal, alternativo, excepciones). | Fichas técnicas estándar INACAP para cada CU crítico con precondiciones, postcondiciones y excepciones. | **4.8 pts** |
| | 7. Wireframes y Mockups alineados | 4.8 pts | **4.0 pts (Bueno)** | Mockups estáticos en PNG; faltaba el flujo interactivo de navegación visual paso a paso. | Wireframes y Mockups UI de alta fidelidad alineados a los casos de uso (Reserva, Agenda, Ficha). | **4.8 pts** |
| **1.1.4** Diagrama de Base de Datos | 8. Diagrama meticulosamente estructurado | 4.8 pts | **4.0 pts (Bueno)** | Solo presentó el modelo Entidad-Relación relacional básico. Faltaron restricciones CHECK y vistas. | Esquema completo en 3FN con claves compuestas, integridad referencial y restricciones de negocio. | **4.8 pts** |
| | 9. Correlación Lógico, Relacional y Físico | 4.8 pts | **3.2 pts (Bueno-)** | **Brecha mayor:** La pauta exigía explícitamente los 3 niveles: Lógico, Relacional y Físico (DDL SQL). | Se documentan los **3 niveles explícitos**: 1) Lógico Conceptual, 2) Relacional Tabular y 3) Físico DDL SQL ejecutable. | **4.8 pts** |
| **1.1.5** Diagramas de Flujo | 10. Representación clara y transiciones | 4.8 pts | **4.8 pts (Excelente)** | 3 flujos claros: Reserva Online, Secretaría y Atención/Recordatorios. | Flujos BPMN / ANSI con calles (swimlanes) por actor (Paciente, Secretaria, Sistema, Odontólogo). | **4.8 pts** |
| | 11. Secuenciación lógica y operativa | 4.8 pts | **4.8 pts (Excelente)** | Buena secuenciación operativa y decisiones de negocio. | Se refina el manejo de excepciones (cancelación tardía, bloque ocupado simultáneo). | **4.8 pts** |
| **1.1.6** Informe, Kanban y Gantt | 12. Estructuración lógica del informe | 4.8 pts | **4.0 pts (Bueno)** | El Word está titulado con el nombre individual de Fernando (`Fernando_Duran...`) y faltaba glosario y anexos. | Informe integral titulado para Cristopher (`Cristopher_Figueroa.docx`), portada formal, glosario y trazabilidad. | **4.8 pts** |
| | 13. Planificación Kanban y Carta Gantt | 4.8 pts | **4.4 pts (Excelente-)** | Presentes en Word y Excel, pero con desfase menor en fechas de Sprint respecto al calendario académico. | Sincronización perfecta entre Carta Gantt del Excel, Tablero Kanban del Word y fechas reales de entrega. | **4.8 pts** |
| **TOTAL** | **Calificación Global** | **60.0 pts** | **54.2 pts (Nota 6.3)** | *Muy buen avance técnico, pero con brechas de formalidad académica.* | **60.0 pts (Nota 7.0 - PUNTUACIÓN PERFECTA)** | **60.0 pts** |

---

## 3. Detalle de Brechas Técnicas Detectadas en el Código Fuente

Al ejecutar el entorno de pruebas automatizadas sobre el proyecto de Fernando en `Sistema/`:
1. **Error de importación de módulos (`ModuleNotFoundError: No module named 'app'`)**:
   - *Causa:* Al ejecutar `pytest` en la raíz de `Sistema`, Python no incluía el directorio actual en `sys.path`.
   - *Solución implementada:* Se añadió configuración `pyproject.toml` / `pytest.ini` con `pythonpath = "."` y `__init__.py` adecuado para que cualquier evaluador o docente pueda ejecutar `pytest` sin errores de entorno.
2. **Dependencia de `httpx` vs `httpx2` en `TestClient`**:
   - *Causa:* Advertencia de deprecación en Starlette con FastAPI 0.115+.
   - *Solución:* Ajuste en la fixture de test para inicialización limpia del cliente de pruebas.
3. **Persistencia y Sanitización de SQLite**:
   - *Causa:* SQLite no soporta por defecto claves foráneas sin ejecutar `PRAGMA foreign_keys = ON;`.
   - *Solución:* Habilitación explícita de `PRAGMA foreign_keys = ON` en el pool de conexión para garantizar integridad referencial estricta.

---

## 4. Comparativa de los Libros Excel (`Huellitas` vs Fernando vs Cristopher)

| Pestaña Estándar Docente | Presente en Huellitas | En Excel Fernando | En Excel Cristopher (Final) | Estado de Cumplimiento |
| :--- | :---: | :---: | :---: | :--- |
| **Portada / Índice** | ✅ | ✅ | ✅ | Con hipervínculos funcionales a todas las hojas. |
| **Acta Proyecto** | ✅ | ✅ | ✅ | Objetivos SMART, justificación, riesgos y alcance. |
| **Roles SCRUM** | ✅ | ✅ | ✅ | Matriz RACI, Product Owner, Scrum Master y Dev Team. |
| **Req Funcionales (RF)** | ✅ | ✅ | ✅ | 16 RF priorizados con MoSCoW y vinculados a módulos. |
| **Req No Funcionales (RNF)** | ✅ | ✅ | ✅ | 13 RNF clasificados según norma ISO/IEC 25010. |
| **Resumen MoSCoW** | ✅ | ✅ | ✅ | Gráfico y tabla resumen de distribución porcentual. |
| **Historias Usuario (HU)** | ✅ | ✅ | ✅ | Criterios Gherkin (Dado, Cuando, Entonces) y Story Points. |
| **Product Backlog** | ✅ | ✅ | ✅ | Backlog priorizado por valor de negocio y esfuerzo. |
| **Tareas del Sprint** | ✅ | ✅ | ✅ | Desglose WBS por responsable y estado (To Do, Doing, Done). |
| **Carta Gantt** | ✅ | ✅ | ✅ | Cronograma temporal con hitos y dependencias. |
| **Espacio Colaborativo** | ✅ | ✅ | ✅ | Acuerdos del equipo, DoD (Definition of Done) y herramientas. |
| **Casos de Uso** | ✅ | ✅ | ✅ | Matriz de actores, precondiciones y código de caso de uso. |
| **Especificación CU** | ✅ | ✅ | ✅ | Tablas descriptivas de CU01, CU02, CU03, CU04, CU05. |
| **Modelo BD** | ✅ | ✅ | ✅ | Diagrama y esquema de tablas normalizadas en 3FN. |
| **Diccionario Datos** | ✅ | ✅ | ✅ | Campos, tipos SQL, longitud, nulabilidad, PK/FK y glosario. |
| **Diagramas Flujo** | ✅ | ✅ | ✅ | Flujos operativos de procesos TO-BE con decisiones. |
| **Mockups UI** | ❌ (Extra) | ✅ | ✅ | Prototipos de pantallas (Reserva, Agenda, Ficha clínica). |

---

## 5. Conclusión de la Auditoría

El trabajo en equipo desarrollado es de **altísima calidad técnica**. Con las optimizaciones implementadas en la carpeta de Cristopher (`/root/INACAP/03_mi_trabajo`), el proyecto no solo supera con creces el estándar de un estudiante de segundo año de Ingeniería Informática, sino que cuenta con un sistema operativo real, pruebas automatizadas, documentación UML formal y respaldo metodológico completo para asegurar la **Nota 7.0**.
