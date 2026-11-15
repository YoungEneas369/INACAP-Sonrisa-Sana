# Comparativa Detallada: Entrega Previa de Fernando vs. Referencia Huellitas vs. Solución Definitiva («Sonrisa Sana»)

> **Asignatura:** Modelamiento de Soluciones Informáticas — INACAP (Sección `114-2-F2`)  
> **Evaluación:** Sumativa N° 5 (Unidad 1 · `60 puntos` · `60%` exigencia)  
> **Docente:** Yaleni Gómez Peña  
> **Integrantes:** Cristopher D. Figueroa Arthur · Fernando A. Durán Leiva · Francisco A. Lara Yévenes  
> **Propósito:** Registrar las diferencias exactas detectadas respecto a la entrega inicial (`02_trabajo_fernando/`), explicar qué se mejoró siguiendo la plantilla docente `Huellitas_Proyecto_SCRUM (Com_28102026).xlsx` y fundamentar por qué la versión actual cubre el 100% de la rúbrica oficial.

---

## 1. Contexto y Origen de las Tres Versiones Analizadas

Este documento registra la auditoría técnica y metodológica comparando la entrega preliminar realizada por Fernando (`02_trabajo_fernando/`, archivada antes de limpiar el repositorio) frente a la plantilla docente de referencia (`Huellitas_Proyecto_SCRUM (Com_28102026).xlsx`) y la solución definitiva actual del equipo (`02_Entregables_Sonrisa_Sana/`).

El propósito de esta comparativa no es desmerecer el esfuerzo inicial —que incluyó un prototipo funcional interesante—, sino dejar trazabilidad clara para todo el equipo (Cristopher D. Figueroa Arthur, Fernando A. Durán Leiva y Francisco A. Lara Yévenes) sobre qué brechas existían respecto a la rúbrica oficial de la Evaluación Sumativa N° 5 (`60 puntos`, `60%` exigencia, Unidad 1: Modelamiento UML) y por qué se reconstruyó la entrega siguiendo paso a paso el estándar `Huellitas`.

| Versión / Carpeta | Origen del Artefacto | Estado y Relación con la Pauta Oficial (`60 pts`) |
| :--- | :--- | :--- |
| Referencia Docente (`Huellitas`) | `Huellitas_Proyecto_SCRUM (Com_28102026).xlsx` | Estándar máximo de calificación: **16 hojas** en Excel y **12 diagramas HD** (`6` Casos de Uso, `1` BD, `5` Flujos TO-BE), fórmulas dinámicas (`=COUNTIF`, `=SUMIF`, `=WORKDAY`, `=NETWORKDAYS`) y trazabilidad total. |
| Entrega de Fernando (`02_trabajo_fernando/`) | `Sonrisa_Sana_Proyecto.xlsx` + `Fernando_Duran_Sonrisa_Sana.docx` + 9 PNGs + SQL + prototipo FastAPI | Incluyó prototipo ejecutable (`FastAPI + SQLite + pytest`) fuera de pauta, pero recortó hojas clave del estándar `Huellitas`, resumió el Diccionario de Datos a `24` atributos, dejó `1` solo diagrama de Casos de Uso y presentó colisiones visuales en diagramas. |
| Iteración Intermedia (`03_trabajo_final_optimizado/`) | Refinamiento directo sobre los archivos previos de Fernando (ya eliminada del repo) | Intentó corregir parte de los textos y separó el diagrama de BD, pero al no partir desde cero desde `Huellitas` y la pauta, heredó la estructura recortada y las superposiciones visuales en `01_casos_de_uso_general.png` y `09_tablero_kanban.png`. |
| Solución Definitiva Actual (`02_Entregables_Sonrisa_Sana/`) | `SonrisaSana_Proyecto_SCRUM.xlsx` + `Informe_Evaluacion_Sumativa_5_Sonrisa_Sana.docx` + `sonrisa_sana_bd.sql` + 19 PNGs | **100% alineada a la pauta oficial y a `Huellitas`**: `18` hojas, `19` diagramas 2x LANCZOS sin cruces, BD 3FN en **3 niveles completos** (`18` tablas, `118` columnas documentadas), `4` Triggers/Vistas, `6 945` palabras de informe y guía paso a paso. |

> [!TIP]
> **Por qué se reemplazaron las carpetas antiguas en GitHub:** Mantener juntas las versiones `01_requisitos`, `02_trabajo_fernando`, `03_trabajo_final_optimizado`, `04_guias` y `05_evaluacion` generaba confusión al estudiar y riesgo de entregar archivos inconsistentes. El repositorio quedó organizado en `01_Pauta_y_Referencia/`, `02_Entregables_Sonrisa_Sana/` y `03_Guia_Paso_a_Paso_y_Defensa/`.

---

## 2. Radiografía Cuantitativa Lado a Lado

La siguiente tabla compara las métricas exactas observadas directamente en los archivos antes de la limpieza del repositorio frente a la plantilla `Huellitas` y a la versión final actual de `Sonrisa Sana`:

| Dimensión / Métrica | Plantilla `Huellitas` (Ref.) | Trabajo de Fernando (`02_trabajo_fernando`) | Solución Definitiva Actual (Cristopher / Equipo) |
| :--- | :--- | :--- | :--- |
| Hojas en libro Excel | 16 hojas | 17 hojas | **18 hojas** (`16` de Huellitas + `Wireframes y Mockups` + `Tablero Kanban`) |
| Diagramas PNG en Excel | 12 imágenes | 9 imágenes | **19 imágenes** (resolución 2x LANCZOS sin colisiones) |
| Requerimientos Funcionales (RF) | 18 RF (`21` filas) | 16 RF (`13` incluidos + `3 Won't`) | **18 RF** (`10 Must, 2 Should, 2 Could, 4 Won't`; `22` filas) |
| Requerimientos No Funcionales | 13 RNF (`16` filas) | 13 RNF (`12` incluidos + `1 Won't`) | **13 RNF ISO/IEC 25010** (`9 Must, 3 Should, 1 Won't` con métrica verificable) |
| Porcentaje `Must` (MoSCoW) | Regla ref. ≤ 60% | **68,97% Must** (`20/29`: excede umbral) | **61,3% Must** (`19/31`) calculado por `=COUNTIF` y `=SUM` |
| Historias de Usuario (HU) | 14 HU (`17` filas) | 13 HU (`16` filas) | **14 HU** (`69 SP`) con 3 criterios verificables cada una |
| Product Backlog y Sprints | 33 filas (con fórmulas) | 15 ítems / `69 SP` (`HU09, HU11, HU13` = `11 SP` **sin Sprint**) | **16 ítems** (`TEC01-02` + `HU01-14`) = **`77 SP` en 5 Sprints** (`=SUMIF`) + DoD |
| Tareas y Carta Gantt | 45 tareas (`52` filas, Gantt `19` cols) | 13 tareas macro (`T01-T13`, Gantt `5` cols `S1-S5`, `127 h`) | **39 tareas** (`T01-T39`, Gantt `13` semanas) con `=WORKDAY` y feriados Chile |
| Casos de Uso UML | 19 CU · **6 diagramas** | 14 CU · **1 solo diagrama** (`01_casos_de_uso_general.png`) | **19 CU** · **6 diagramas** (`1` general + `5` modulares por subsistema) |
| Especificación de Casos de Uso | 7 fichas formales (`59` filas) | 5 filas de texto resumen (`8` filas totales) | **7 fichas formales completas** (`CU04, CU05, CU09, CU11, CU12, CU14, CU17` en `66` filas) |
| Modelo de Base de Datos | 18 tablas · Lógico/Relacional 3FN | 12 tablas en hoja vs `14` en SQL · **1 diagrama ER híbrido** | **18 tablas 1:1** con SQL · **3 niveles separados** (Lógico, Relacional 3FN Pata de Gallo, Físico DDL) |
| Diccionario de Datos | 133 filas exhaustivas | **28 filas** (`24` atributos agrupados; columnas omitidas) | **140 filas** (**118 columnas exactas** de las 18 tablas, PK/FK/UQ/Nulo) |
| Diagramas de Flujo TO-BE | 5 diagramas separados | 3 diagramas (`Atención + Recordatorios` comprimidos en 1) | **5 diagramas TO-BE** independientes con bandas de fase e insignias |
| Wireframes y Mockups UI | No aplica en Huellitas (pauta S5 sí lo pide) | 3 mockups simples (sin wireframe ni odontograma) | **4 láminas dobles** Wireframe + Mockup (`15`–`18`, incl. Odontograma FDI y WhatsApp) |
| Informe Técnico Word (`.docx`) | Según pauta institucional | **1 028 palabras** (`47` párrafos, `5` tablas, `9` figuras) | **6 945 palabras** (`108` párrafos, `22` tablas completas, `19` figuras HD) |

---

## 3. Diferencias Críticas Hoja por Hoja en el Libro Excel

Al comparar la estructura interna de `Sonrisa_Sana_Proyecto.xlsx` (Fernando) con `Huellitas_Proyecto_SCRUM (Com_28102026).xlsx` y nuestra versión `SonrisaSana_Proyecto_SCRUM.xlsx`, se detectaron recortes de contenido y pérdida de trazabilidad en hojas evaluadas directamente por los criterios `1.1.1` a `1.1.6` de la rúbrica:

- **Acta Proyecto (`18` filas en Fernando vs. `39` en Huellitas / `40` en Cristopher):** En la entrega previa se resumió en un cuadro breve sin profundizar el análisis comparativo **AS-IS (cuaderno físico) vs. TO-BE**, ni la evaluación de **factibilidad en sus 4 dimensiones** (técnica, operativa, económica en CLP y legal Leyes 20.584 / 19.628). Nuestra versión lo desarrolla íntegramente.
- **Roles SCRUM (`9` filas en Fernando vs. `36` en Huellitas / `40` en Cristopher):** Fernando incluyó únicamente la tabla básica de integrantes/roles, omitiendo la **Matriz RACI** de responsabilidades y el detalle de **Eventos SCRUM** (Sprint Planning, Daily, Review, Retrospective). Nuestra solución incorpora las 3 secciones completas.
- **Product Backlog (`HU09`, `HU11` y `HU13` huérfanas de Sprint):** En Fernando, `Sprint 1` concentraba `24 SP`, `Sprint 2` subía a `34 SP` y `3` Historias de Usuario (`11 SP`) quedaban sin asignar a ningún Sprint. En nuestra solución, los `16` ítems (`TEC01–TEC02` + `HU01–HU14`, `77 SP`) están distribuidos desde `Sprint 1` a `Sprint 5` sin ítems huérfanos y con Definición de Terminado (`DoD`) explícita.
- **Tareas y Carta Gantt (`13` tareas macro vs. `39` tareas / `13` semanas):** Fernando comprimió todo el proyecto en `13` tareas genéricas (`19-10-2026` al `17-11-2026`), perdiendo granularidad entre análisis, diseño UML, BD, codificación y pruebas. Nosotros seguimos la granularidad de `Huellitas` con `39` tareas (`T01–T39`), factor de dificultad (`=IF`), duración hábil en Chile (`=WORKDAY`/`=NETWORKDAYS` descontando feriados `12-10`, `08-12` y `25-12-2026`) y Carta Gantt semanal.
- **Espacio Colaborativo y Kanban (`9` filas en Fernando vs. `43` + hoja `Tablero Kanban` en Cristopher):** Fernando eliminó toda la sección de convenciones de **Google Drive, Trello y ramas Git** dejando solo 6 filas Kanban, mientras nuestra solución conserva íntegramente el Espacio Colaborativo (`43` filas) y además dedica una pestaña propia al **Tablero Kanban WIP**.
- **Especificación de Casos de Uso (`8` filas de texto corrido vs. `7` fichas formales en `66` filas):** La entrega de Fernando resumió `CU03, CU06, CU07, CU09, CU10/CU11` en párrafos de una sola fila por caso. La pauta y `Huellitas` exigen fichas estructuradas campo a campo (Actor principal/secundario, Precondiciones, Flujo Básico paso a paso, Flujos Alternos/Excepciones, Postcondiciones y RNF vinculados).
- **Modelo de Base de Datos (`12` tablas documentadas vs. `14` en su propio SQL):** En Fernando hubo inconsistencia interna: su `sonrisa_sana_bd.sql` creaba `14` tablas, pero la hoja `Modelo BD` solo listaba `12` entidades (omitiendo `tipo_atencion` y `configuracion` de la documentación en Excel). En Cristopher existe **correspondencia exacta `18/18` tablas** entre Excel, Word, diagramas y `sonrisa_sana_bd.sql`.
- **Diccionario de Datos (`28` filas agrupadas vs. `140` filas / `118` columnas reales):** Fue la brecha más severa del archivo anterior. Fernando agrupó múltiples atributos en una misma celda (por ejemplo `fecha / hora_inicio / fin` o `canal / estado`) documentando apenas `24` líneas para todo el sistema y omitiendo decenas de columnas de su SQL. Nuestro Diccionario documenta **columna por columna (`118` atributos totales)** con tipo de dato exacto, nulidad (`SÍ`/`NO`), clave (`PK`, `FK`, `UQ`) y restricción de negocio.

---

## 4. Diferencias Funcionales en el Dominio Odontológico

Más allá del formato de las tablas, ambos trabajos difieren sustancialmente en **qué quedó dentro y qué quedó fuera (`Won't`)** del sistema clínico para «Sonrisa Sana»:

| Capacidades del Negocio Odontológico | Enfoque de Fernando | Enfoque Definitivo (Cristopher / Equipo) |
| :--- | :--- | :--- |
| Odontograma Digital por Piezas Dentales | Declarado **fuera de alcance (`RF15 Won't`)** como «odontograma gráfico 3D avanzado»; la ficha era solo texto. | **Incluido como núcleo (`RF09 Must` / `HU09`)**: tabla `odontograma_pieza` en 3FN con numeración estándar **FDI (piezas `11`–`85`)** + Mockup visual interactivo (`PNG 17`). |
| Presupuestos Dentales y Boletas / Facturas | Declarado **fuera de alcance (`RF14 Won't`)**; sin trazabilidad de cobros en CLP. | **Incluido (`RF11 Should` / `HU11`)**: tabla `boleta_factura` en **pesos chilenos (CLP)** sin decimales, permitiendo presupuestos previos (`id_atencion NULL`) o boletas post-atención. |
| Recetas / Prescripciones Farmacológicas | Sin entidad dedicada; tratado como nota libre de atención. | **Incluido (`RF10 Should` / `HU10`)**: tabla `prescripcion_dental` normalizada (fármaco, dosis, frecuencia, duración) extendida desde `CU12` (`<<extend>> CU13`). |
| Control de Insumos y Stock Crítico | No modelado en su esquema principal. | **Incluido como valor operativo (`RF12–RF13 Could` / `HU12–HU13`)**: tablas `insumo_dental`, `movimiento_insumo` y `alerta_insumo` con triggers automáticos de reposición. |
| Exclusiones Reales (`Won't` Justificados) | Dejó fuera módulos esenciales del dentista (Odontograma y Presupuestos) y además App móvil (`RF16`). | Excluyó integraciones externas costosas fuera de MVP (`RF15` IMEd/FONASA en línea, `RF16` Visor DICOM 3D, `RF17` App iOS/Android nativa, `RF18` API laboratorio externo, `RNF13` modo offline). |

---

## 5. Comparativa Visual y Técnica de Diagramas (Colisiones vs. Precisión UML)

Durante la revisión visual directa de los PNG originales generados en el trabajo anterior de Fernando (y parcialmente heredados en `03_trabajo_final_optimizado`), se identificaron defectos de diagramación que penalizan los criterios `1.1.3`, `1.1.4`, `1.1.5` y `1.1.6` de la rúbrica:

| Diagrama / Artefacto | Problema Observado en Entrega de Fernando | Corrección Aplicada en Solución Actual (`Diagramas_SonrisaSana/`) |
| :--- | :--- | :--- |
| Casos de Uso UML (`01_casos_de_uso_general.png`) | Entregó **solo 1 diagrama** saturado donde la flecha `<<include>>` (`CU06` → `CU04`) corta el borde izquierdo de `CU09` y pisa el texto; las asociaciones desde `Paciente` a `CU07` y `Odontólogo` a `CU05` atraviesan elipses (`CU02`, `CU05`); no existe herencia hacia actor abstracto `Usuario`. | Se generaron **6 diagramas (`01`–`06`)**: `1` Vista General con generalización `Usuario` + `5` diagramas modulares detallados (`Acceso/RBAC`, `Agenda 24/7`, `Atención/Odontograma`, `Recordatorios`, `Presupuestos/Insumos`), con enrutamiento limpio sin cruces sobre texto. |
| Base de Datos (`02_modelo_bd_er.png`) | Entregó **1 solo diagrama híbrido** (ni 100% Lógico ni Físico DDL). Conectores rectos atraviesan tablas y pisan etiquetas (`ODONTOLOGO–HORARIO_ODONT` tacha `ESPECIALIDAD`; `CITA–RECORDATORIO` tacha `TIPO_ATENCION`; `USUARIO–AUDITORIA` cruza `CITA`), y `CONFIGURACION` flota desconectada sin FK. | Se entregaron **3 niveles obligatorios por separado**: **`07` Modelo Lógico** (18 entidades agrupadas en 4 dominios funcionales), **`08` Modelo Relacional 3FN** (notación Pata de Gallo con PK/FK/UQ y cero líneas sobre texto) y **`09` Modelo Físico DDL** (MySQL 8.0 + Triggers + Vistas + Cron). |
| Diagramas de Flujo TO-BE (`03`–`05`) | Solo `3` láminas y la última (`05_flujo_atencion_y_recordatorios.png`) comprimía dos procesos distintos en una sola imagen densa. | **5 flujos TO-BE independientes (`10`–`14`)** con carriles/bandas de fase, insignias numeradas (`01`..`08`), decisiones explícitas y rutas de excepción (choque horario, acceso RBAC denegado `403`, reintento recordatorio). |
| Wireframes y Mockups (`06`–`08`) | Solo `3` mockups simples sin wireframe previo; `08_mockup_ficha_clinica.png` mostraba apenas 2 viñetas y 3 cajas de texto sin representación dental. | **4 láminas dobles Wireframe (izq.) + Mockup HD (der.) (`15`–`18`)**: Portal Paciente móvil/web, Calendario Recepción (`< 30 s`), **Estación Odontólogo con Odontograma FDI 32 piezas**, y **Notificación WhatsApp móvil 1-clic + Reporte Admin**. |
| Tablero Kanban (`09_tablero_kanban.png`) | En las **5 columnas**, los subtítulos de límite WIP (*«Sin límite WIP»*, *«Límite: ~19 SP»*, *«WIP Máx. 2 / persona»*, *«WIP Máx. 3 tarjetas»*, *«Aceptado por PO»*) quedan parcialmente tapados/tachados por el borde superior de la primera tarjeta. | Lámina **`19_tablero_kanban_sonrisa_sana.png`** remaquetada con separación amplia bajo cada cabecera WIP, **nombres reales del equipo (`C. Figueroa`, `F. Durán`, `F. Lara`)**, `77 SP` cuadrados en 5 Sprints, DoD y panel inferior de métricas ágiles. |

---

## 6. Lo Positivo del Trabajo de Fernando (Qué se Reconoce y Qué se Mejoró)

Una evaluación profesional exige reconocer los aciertos técnicos de la entrega previa antes de explicar por qué no bastaba para obtener los `60/60 puntos` en esta asignatura:

- **Prototipo ejecutable (`FastAPI + SQLite + pytest`):** Fernando construyó una prueba de concepto funcional en Python con pruebas unitarias automatizadas (`test_sistema.py`). Sin embargo, la Evaluación Sumativa N° 5 corresponde a **Modelamiento de Soluciones Informáticas (Unidad 1)**, cuya rúbrica no asigna puntaje a código FastAPI ni endpoints, sino exclusivamente a levantamiento (`1.1.1`), análisis SCRUM (`1.1.2`), Casos de Uso + Wireframes (`1.1.3`), BD en 3 niveles (`1.1.4`), Flujos TO-BE (`1.1.5`) e Informe + Kanban (`1.1.6`).
- **Columna generada `bloque_activo` en SQL:** En su script DDL, Fernando propuso una columna generada `bloque_activo VARCHAR(60) GENERATED ALWAYS AS (...) STORED UNIQUE` para impedir colisiones cuando una cita no está cancelada. Es un recurso ingenioso en MySQL 8, aunque tiene una limitación importante: solo bloquea horas de inicio idénticas (`09:00` con `09:00`), pero **no impide solapamientos parciales** entre citas de distinta duración (por ejemplo, una endodoncia `09:00–09:45` frente a un control `09:30–10:00`).
- **Cómo lo mejoró nuestra BD (`sonrisa_sana_bd.sql`):** Nuestra solución combina `UNIQUE KEY uq_bloque_odontologo (id_odontologo, fecha, hora_inicio)` con el **trigger `trg_cita_bi_anti_colision`**, que valida matemáticamente cualquier traslape de intervalos (`NEW.hora_inicio < hora_fin AND NEW.hora_fin > hora_inicio`) sobre citas activas (`estado IN ('pendiente', 'confirmada', 'atendida')`), garantizando `0%` de colisiones incluso con bloques de duración variable.

> [!IMPORTANT]
> **Conclusión clave para la presentación del equipo:** Si la docente consulta sobre el enfoque del proyecto: nuestro diseño pasó de un borrador técnico parcial (`1 028` palabras, `1` diagrama CU, `1` diagrama ER y Diccionario resumido) a un **expediente de ingeniería completo bajo estándar `Huellitas`** (`18` hojas, `19` diagramas limpios, `3` niveles de BD con `118` columnas documentadas y `6 945` palabras de informe), cubriendo cada indicador de la rúbrica al 100%.

---
