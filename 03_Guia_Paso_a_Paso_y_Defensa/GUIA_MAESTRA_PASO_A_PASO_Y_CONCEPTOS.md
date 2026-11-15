# Guía Maestra Paso a Paso, Diccionario de Conceptos y Defensa Oral
## Proyecto: SGO Clínica Odontológica «Sonrisa Sana» (Evaluación Sumativa N° 5)

- **Asignatura:** Modelamiento de Soluciones Informáticas · **Sección:** `114-2-F2`
- **Docente:** Yaleni Gómez Peña — INACAP
- **Integrantes:** Cristopher D. Figueroa Arthur · Fernando A. Durán Leiva · Francisco A. Lara Yévenes
- **Estándar seguido:** Rúbrica oficial (60 pts / 60% exigencia) + Plantilla docente `Huellitas_Proyecto_SCRUM`

---

## Introducción: Cómo usar esta Guía para Entender y Defender el Proyecto

Este manual fue diseñado específicamente para que los tres integrantes del equipo (Cristopher D. Figueroa Arthur, Fernando A. Durán Leiva y Francisco A. Lara Yévenes) comprendan desde cero cada concepto metodológico, cada diagrama UML, de Base de Datos, de Flujo, Wireframe y Kanban y cada pestaña del libro Excel «SonrisaSana_Proyecto_SCRUM.xlsx» frente a la evaluación Sumativa N° 5 con la docente Yaleni Gómez Peña (Sección 114-2-F2, 60 puntos, 60% de exigencia).

> [!TIP]
> **Idea Central de Todo el Proyecto (La Cadena de Trazabilidad):** Nada en ingeniería de software se inventa aislado. Todo nace del dolor del cliente (cuaderno físico -> choques, lentitud, falta de recordatorios, riesgo de privacidad). Desde ese problema se sigue una línea continua y conectada: Problemática -> Requerimientos (RF/RNF) -> Priorización MoSCoW -> Historias de Usuario (HU) -> Backlog/Gantt/Kanban -> Casos de Uso (CU) y Wireframes -> Base de Datos en 3 Niveles (3FN) -> Flujos TO-BE. Si entiendes esa cadena, puedes responder cualquier pregunta de la profesora sin memorizar nada de memoria.

| Entregable Final | Archivo / Carpeta | Qué contiene y por qué importa en la rúbrica |
| --- | --- | --- |
| Libro SCRUM Excel (Estándar Docente) | SonrisaSana_Proyecto_SCRUM.xlsx | 18 hojas (las 16 exactas de «Huellitas» con fórmulas vivas + 2 extras: Wireframes y Tablero Kanban) y 19 diagramas HD incrustados. |
| Informe Técnico Formal | Informe_Evaluacion_Sumativa_5_Sonrisa_Sana.docx | Documento autocontenido (6 944 palabras, 22 tablas, 19 figuras) cubriendo los criterios 1.1.1 a 1.1.6. |
| Script SQL Físico Ejecutable | sonrisa_sana_bd.sql | Base de datos completa MySQL 8.0 InnoDB en 3FN: 18 tablas (118 columnas), índices, 4 triggers, 1 evento horario, 4 vistas y datos semilla. |
| Galería Visual de Diagramas | Diagramas_SonrisaSana/ (01 a 19 PNG) | 6 diagramas Casos de Uso UML, 3 de Base de Datos (Lógico/Relacional/Físico), 5 Flujos TO-BE, 4 Wireframes+Mockups y 1 Tablero Kanban. |
| Esta Guía de Estudio y Defensa | GUIA_MAESTRA_PASO_A_PASO_Y_CONCEPTOS.md / .docx | Explicación desde cero de conceptos, paso a paso constructivo (8 etapas), guion de exposición y 12 preguntas típicas de evaluación. |

## Parte 1: Diccionario de Conceptos desde Cero (Explicados en Simple)

### 1.1 Requerimientos Funcionales (RF) vs. No Funcionales (RNF - ISO/IEC 25010)

Esta es la distinción fundamental de todo levantamiento de requisitos (Criterio 1.1.1). Aunque ambos describen lo que la clínica necesita, responden preguntas completamente distintas:

- **Requerimiento Funcional (RF) = QUÉ HACE el sistema:** Son las acciones concretas, módulos o funciones que un usuario (Paciente, Secretaria, Odontólogo, Admin, Encargado de Insumos) o un proceso automático puede ejecutar dentro del sistema. Ejemplos: reservar una hora, cancelar una cita, abrir una ficha clínica, emitir un presupuesto o descontar stock de anestesia.
- **Requerimiento No Funcional (RNF) = CÓMO DEBE COMPORTARSE el sistema:** No es un botón ni una pantalla nueva, sino una propiedad de calidad o restricción técnica medible que protege o exige cómo operan los RF: velocidad (< 1,5 segundos), seguridad/confidencialidad (bcrypt, TLS 1.3, cifrado AES-256, RBAC), legalidad (Leyes 20.584 y 19.628/21.719), usabilidad (máx. 3 pasos / máx. 2 clics), fiabilidad (0% choques, backups diarios) y compatibilidad móvil.

> [!TIP]
> **Truco Práctico de 5 Segundos para No Confundirlos Frente a la Profesora:** Hazte esta pregunta: «Si le quito esto al sistema, ¿deja de existir una acción de negocio (ya no se puede agendar o cobrar), o la acción sigue existiendo pero funciona lento, insegura o incómoda?». Si deja de existir la acción -> es RF. Si sigue existiendo pero sin velocidad, sin seguridad o sin facilidad de uso -> es RNF. Además, todo RNF en ingeniería DEBE llevar una métrica verificable (segundos, porcentaje, estándar o algoritmo).

| Par del Caso «Sonrisa Sana» | Requerimiento Funcional (RF = QUÉ hace) | Requerimiento No Funcional (RNF = CÓMO / Calidad ISO 25010) |
| --- | --- | --- |
| Reserva de Horas Online | RF03: Permitir al paciente reservar hora online 24/7 por especialidad, odontólogo y bloque libre. | RNF04 (Eficiencia): Consulta y reserva responden en < 1,5 s (P95). · RNF08 (Fiabilidad): 0% choques con UNIQUE. |
| Modificación / Cancelación | RF05: Permitir a la secretaria modificar o cancelar citas y liberar el bloque horario al instante. | RNF06 (Usabilidad): Secretaria cancela/reprograma en máx. 2 clics (< 30 s). · RNF04: Respuesta < 1,5 s. |
| Confidencialidad Ficha Clínica | RF08–RF09: Permitir solo al Odontólogo consultar ficha/odontograma y registrar evolución diagnóstica. | RNF01–RNF02 (Seguridad): Cifrado AES-256 en reposo, TLS 1.3, RBAC estricto (HTTP 403) y log inmutable. |
| Recordatorios Automáticos | RF07: Enviar recordatorios automáticos 48h y 24h antes por correo/WhatsApp con enlace 1 clic. | RNF09 (Fiabilidad): Cron ejecutado cada hora con reintento automático. · RNF03 (Legal): Mensaje sin datos clínicos. |
| Registro de Pacientes | RF01: Registrar paciente con RUT, nombre, fecha nacimiento, teléfono, correo y previsión. | RNF12 (Localización): Validación dígito verificador RUT chileno y formato dd-mm-aaaa. · RNF03: Consentimiento Ley 19.628. |
| Calendario de Recepción | RF06: Mostrar agenda diaria/semanal filtrable por odontólogo/box y diferenciada por estado. | RNF07 (Usabilidad): Paleta de colores por estado accesible (WCAG AA) para lectura instantánea. |

### 1.2 Categorías de la Norma ISO/IEC 25010 en Nuestros 13 RNF

En lugar de inventar etiquetas sueltas, nuestros RNF01–RNF13 clasifican cada exigencia según las características de calidad internacional ISO/IEC 25010:

- **Seguridad / Confidencialidad / Legal (RNF01, RNF02, RNF03):** Hash bcrypt coste >= 12, HTTPS TLS 1.3, cifrado AES-256 en reposo en BD, control RBAC que responde HTTP 403 ante intrusiones y registro de auditoría conforme Ley 20.584 y Ley 19.628 / 21.719.
- **Eficiencia de desempeño (RNF04, RNF05):** Tiempos < 1,5 s (P95 con 50 usuarios concurrentes) en agenda/reservas y < 2,0 s al cargar ficha clínica + odontograma.
- **Usabilidad (RNF06, RNF07):** Reserva online en <= 3 pasos (< 90 s), gestión de secretaria en <= 2 clics (< 30 s) y colores de estado con contraste WCAG AA.
- **Fiabilidad (RNF08, RNF09, RNF10, RNF13):** Restricción transaccional anti-choques (0% colisiones), cron de recordatorios cada 1 hora, backups cifrados con 30 días de retención (y modo offline descartado en RNF13 como Won't).
- **Compatibilidad / Mantenibilidad (RNF11, RNF12):** Web responsive Mobile-First (375px, 768px, 1366px), arquitectura MVC/REST en Git, español de Chile, RUT validado y CLP.

### 1.3 Priorización MoSCoW y Delimitación de Alcance (31 Requerimientos)

MoSCoW es una técnica ágil (Criterio 1.1.2) que evita intentar construir todo al mismo tiempo y protege la fecha de entrega. Sobre los 31 requerimientos levantados (18 RF + 13 RNF), la distribución automática en la hoja Resumen MoSCoW es:

| Prioridad | Significado Práctico | RF | RNF | Total (%) | Ejemplos Exactos en Sonrisa Sana |
| --- | --- | --- | --- | --- | --- |
| Must | Imprescindible: sin esto el sistema NO puede salir a producción (MVP). | 10 | 9 | 19 (61,3%) | RF01–RF09, RF14 (Agenda, Reserva, Cancelar, Recordatorios, Ficha, RBAC) + RNF01–04, 06, 08–11. |
| Should | Importante: aporta gran valor clínico/administrativo, sigue justo tras el MVP. | 2 | 3 | 5 (16,1%) | RF10 (Recetas), RF11 (Presupuestos/Boletas CLP), RNF05 (< 2s ficha), RNF07 (WCAG), RNF12. |
| Could | Deseable: optimiza operaciones si el alcance de tiempo lo permite. | 2 | 0 | 2 (6,5%) | RF12 (Stock insumos dentales) y RF13 (Alertas automáticas de stock mínimo). |
| Won't | Fuera de alcance en v1: acordado explícitamente que NO se hará ahora. | 4 | 1 | 5 (16,1%) | RF15 (Bono IMED/FONASA online), RF16 (DICOM 3D IA), RF17 (App nativa), RF18 (Lab. externo), RNF13 (Offline). |

> [!TIP]
> **Regla de ORO sobre los Won't:** ¿Por qué RF15–RF18 y RNF13 SÍ aparecen en las hojas de Requerimientos pero NO tienen Historia de Usuario (HU) ni Caso de Uso (CU)? Porque el análisis MoSCoW sirve justamente para trazar una frontera formal frente al cliente ('esto SÍ va y esto NO va en esta versión'). Así evitas sorpresas en la evaluación y demuestras dominio del alcance.

### 1.4 SCRUM, Tablero Kanban y Matriz RACI

- **Product Owner (Dra. Valeria Morales):** Dueña del problema de negocio, define qué tiene más valor para la clínica, prioriza el Product Backlog y aprueba/rechaza avances en cada Sprint Review.
- **Scrum Master (Fernando Durán):** Facilita las ceremonias SCRUM, mantiene al día la Carta Gantt y Trello, protege las reglas Kanban (límites WIP) y destraba impedimentos en <= 48 h.
- **Equipo de Desarrollo (Cristopher Figueroa, Fernando Durán, Francisco Lara):** Autoorganizado para analizar requisitos, modelar UML/BD, programar frontend/backend y ejecutar pruebas QA.
- **Matriz RACI (hoja Roles SCRUM):** Asigna responsabilidad exacta sobre cada entregable. R = Responsable (quien ejecuta el trabajo), A = Accountable/Aprueba (una sola autoridad por entregable), C = Consultado (aporta criterio antes de cerrar), I = Informado (recibe notificación del resultado).
- **Tablero Kanban y Método Pull (Diagrama 19):** Mientras SCRUM organiza el tiempo en iteraciones (5 Sprints a ~19 SP/Sprint), Kanban visualiza el flujo en 6 columnas con Límites WIP (Work In Progress: máx. 2 tarjetas en Progreso por persona, máx. 4 en Revisión QA). Nadie 'empuja' trabajo: cuando QA o un dev se libera, 'jala' (Pull) la siguiente tarjeta prioritaria. Lead Time (3,4 días) mide desde que el ítem entra al Sprint hasta Terminado; Cycle Time (1,6 días) mide solo el tiempo activo de desarrollo.

### 1.5 Historias de Usuario (HU), Épicas y Story Points (Fibonacci)

Las 14 Historias de Usuario (HU01–HU14) traducen los requerimientos incluidos (Must/Should/Could) al punto de vista humano de quien operará la plataforma:

- **Estructura fija de 4 partes (siguiendo Huellitas):** 1) Como [Rol: Paciente / Secretaria / Odontólogo / Encargado de Insumos / Admin], 2) Necesito [Funcionalidad], 3) Con la finalidad de [Beneficio o valor], 4) Condiciones de Aceptación (viñetas verificables para que QA sepa cuándo está terminada).
- **Épicas (E0 a E6):** Carpetas temáticas que agrupan HUs relacionadas: E0 Técnica (TEC01, TEC02: infraestructura TLS, BD 3FN, cifrado), E1 Seguridad (HU14), E2 Pacientes y Agenda (HU01–HU06), E3 Recordatorios (HU07), E4 Ficha Confidencial (HU08–HU10), E5 Finanzas (HU11) y E6 Insumos (HU12–HU13).
- **Story Points (SP) con serie Fibonacci (3, 5, 8 SP):** NO miden horas de reloj, sino esfuerzo/complejidad/riesgo relativo comparado con una tarea sencilla (ej. registrar un paciente es 3 SP; programar reserva online anti-colisión en < 1,5 s es 8 SP). Suman 69 SP en las 14 HUs + 8 SP de tareas técnicas base (TEC01+TEC02) = 77 SP totales en el Product Backlog.

### 1.6 Modelado UML de Casos de Uso (CU01–CU19): Diferencia Clave <<include>> vs <<extend>>

Un Diagrama de Casos de Uso (Criterio 1.1.3, láminas 01 a 06) responde: ¿Quién interactúa con el sistema y qué grandes servicios obtiene de él? No muestra pantallas ni código interno, sino relaciones funcionales.

- **Actores Primarios (izquierda):** Quienes inician una acción para obtener valor (Paciente, Secretaria, Odontólogo, Encargado de Insumos, Administrador).
- **Herencia / Generalización de Actores (Diagrama 01):** Secretaria, Odontólogo, Encargado de Insumos y Administrador son hijos de «Usuario» porque todos necesitan ejecutar CU01 (Iniciar/cerrar sesión). En UML, la flecha con triángulo hueco apunta del hijo específico hacia el padre general.
- **Actores Secundarios / Externos (derecha):** Servicios o disparadores que el sistema usa o que lo activan sin ser personas usuarias de la UI: «Reloj del Sistema» (Cron cada hora para CU14) y «Pasarela Correo/WhatsApp» (recibe envíos de CU09 y CU14).
- **<<include>> (Inclusión OBLIGATORIA):** El caso base SIEMPRE necesita ejecutar al caso incluido cada vez que corre. La flecha punteada sale DESDE el caso base HACIA el subcaso incluido. Ejemplo real: tanto CU05 (Reservar online) como CU06 (Agendar presencial) apuntan con <<include>> hacia CU07 (Validar disponibilidad y evitar colisión), porque jamás puedes guardar una cita sin validar choque. Igual en CU15 --<<include>>--> CU16 (Alerta stock mínimo).
- **<<extend>> (Extensión OPCIONAL / CONDICIONAL):** Ocurre SOLO si se cumple una condición excepcional en tiempo de ejecución. La flecha punteada va en sentido inverso: DESDE la extensión HACIA el caso base. Ejemplo real: CU08 (Sugerir horarios alternativos) --<<extend>>--> CU05/CU06 únicamente cuando [horario ocupado]; y CU13 (Emitir receta dental) --<<extend>>--> CU12 (Registrar atención) únicamente cuando [requiere fármacos].
- **Fichas de Especificación (hoja Especificación CU):** Los 7 procesos críticos (CU05, CU09, CU11, CU12, CU14, CU17/18, CU15/16) se detallan paso a paso con Actor, Precondición, Flujo Básico (camino feliz), Flujos Alternativos numerados (ej. 3a sin horas, 4a choque concurrente), Postcondición y Reglas de Negocio.

### 1.7 Base de Datos en 3 Niveles (Lógico, Relacional 3FN y Físico DDL)

El Criterio 1.1.4 exige esquematizar la Base de Datos demostrando sus 3 niveles de abstracción y el paso a Tercera Forma Normal (3FN). Veamos exactamente qué hace cada uno de nuestros tres diagramas de BD:

| Nivel de Abstracción | Archivo en el Proyecto | Qué muestra y qué pregunta técnica responde |
| --- | --- | --- |
| 1. Modelo Lógico / Conceptual | 07_bd_modelo_logico.png | Agrupa las 18 entidades en 4 dominios de negocio (Seguridad/Staff, Pacientes/Agenda, Clínica/Odontograma, Comercial/Inventario) mostrando solo reglas del negocio (1:N, 1:1, 0..1) sin tipos técnicos SQL. |
| 2. Modelo Relacional (3FN) | 08_bd_modelo_relacional_3fn.png | Muestra las 18 tablas normalizadas en 3FN en notación Pata de Gallo (Crow's Foot), exponiendo claves PK (llave primaria), FK (llave foránea), UQ (valor único) y resolviendo relaciones M:N como odontologo_especialidad. |
| 3. Modelo Físico (DDL MySQL 8.0) | 09_bd_modelo_fisico_ddl.png + sonrisa_sana_bd.sql | Aterriza el diseño a MySQL 8.0 InnoDB (utf8mb4): tipos exactos (INT, DATE, ENUM, VARBINARY(512/1024/2048) para AES-256), UNIQUE KEY uq_bloque_odontologo, índices B-Tree, CHECKs, 4 Triggers, 4 Vistas y 1 Event. |

- **¿Qué significa estar en Tercera Forma Normal (3FN)?:** 1FN = datos atómicos sin listas dentro de una columna (no guardamos las 32 piezas dentales en un solo texto, sino cada diente como fila en odontograma_pieza). 2FN = ninguna columna depende solo de una parte de una clave compuesta (por eso cada tabla tiene su PK bien definida). 3FN = ningún atributo no-clave depende de otro atributo no-clave (por eso 'prevision' y 'especialidad' salen a tablas propias: cero duplicación ni anomalías).
- **¿Cómo se leen las Patas de Gallo (Diagrama 08)?:** Dos rayitas || = 'exactamente uno' (padre obligatorio). Círculo y rayita o| = 'cero o uno' (ej. atención de urgencia sin cita previa: id_cita NULL). Pata de 3 dedos con rayita |< = 'uno o muchos'. Pata con círculo o< = 'cero, uno o muchos'.
- **¿Cómo evita choques la BD en milisegundos?:** En la tabla cita coexisten dos barreras físicas: UNIQUE KEY uq_bloque_odontologo (id_odontologo, fecha, hora_inicio) + el Trigger trg_cita_bi_anti_colision que verifica traslapes entre rangos hora_inicio < hora_fin para citas activas (pendiente/confirmada). Si dos usuarios reservan al mismo milisegundo, MySQL rechaza la segunda transacción y la app sugiere horarios alternativos (CU08).
- **¿Cómo blinda la BD el secreto médico?:** Aunque alguien robe un respaldo o consulte la BD directamente, alergias_cifradas, anamnesis_medica_cifrada, diagnostico_cifrado y observaciones_cifradas son VARBINARY cifrados con AES-256. Además, el backend bloquea con HTTP 403 a cualquier rol distinto de Odontólogo y registra cada lectura en auditoria_acceso_ficha (Ley 20.584).

### 1.8 Diagramas de Flujo TO-BE, Wireframes UI y Odontograma FDI

- **AS-IS vs. TO-BE:** AS-IS describe el problema actual (cuaderno físico con tachaduras, demoras de 3 a 5 min y cero recordatorios). TO-BE describe el proceso futuro optimizado con el software propuesto (diagramas 10 al 14).
- **Simbología estándar ANSI/ISO en Flujos (10–14):** Óvalo = Inicio o Fin; Paralelogramo azul = Entrada o salida de datos del usuario; Rectángulo = Proceso automático del sistema; Rombo amarillo = Decisión lógica (Sí / No); Tarjeta roja/ámbar = Manejo de error o excepción (choque horario, HTTP 403, stock negativo). Cada bloque lleva insignia numerada (P1, S1, A1, R1, F1) y bandas de fase horizontales.
- **Wireframes (baja fidelidad) vs. Mockups (alta fidelidad) en láminas 15–18:** El Wireframe (mitad izquierda) es el plano estructural en tonos neutros que valida jerarquía, orden de los 3 pasos (< 90 s) o 2 clics (< 30 s). El Mockup (mitad derecha) muestra la interfaz visual final con colores clínicos accesibles (WCAG AA), calendario por estado, confirmación por WhatsApp sin datos sensibles y Estación del Odontólogo con el Odontograma estándar FDI de 32 piezas dentales (cuadrantes 1x sup. der., 2x sup. izq., 3x inf. izq., 4x inf. der.).

## Parte 2: El Paso a Paso de Construcción (De Cero al 100% según Huellitas y Rúbrica)

Para responder cuando la docente pregunte «¿Cómo fueron construyendo esta solución?», aquí está la ruta cronológica exacta en 8 etapas siguiendo el orden real del estándar Huellitas (16 hojas base + 2 extras) y los 6 criterios de la Escala de Apreciación (60 puntos):

| Etapa | Qué se hace y por qué va en este orden | Hojas Excel y Diagramas Generados | Criterio / Ptos |
| --- | --- | --- | --- |
| Paso 1: Encuadre, Acta y Roles | Se analiza el enunciado «Sonrisa Sana», se identifican los 5 dolores del cuaderno físico (AS-IS) y se definen objetivos SMART, alcance IN/OUT, restricciones legales (Leyes 20.584 y 19.628), Stakeholders, roles SCRUM y matriz RACI. | Hojas: Portada, Acta Proyecto, Roles SCRUM | 1.1.1 y 1.1.6 |
| Paso 2: Levantamiento RF y RNF | Se separan las funciones del negocio (18 RF: 14 implementables + 4 Won't fuera de alcance) de las métricas de calidad ISO/IEC 25010 (13 RNF enfocados en velocidad < 1,5 s y confidencialidad AES-256/RBAC). | Hojas: Req Funcionales, Req No Funcionales | 1.1.1 (8,4 pts) |
| Paso 3: Análisis, Factibilidad y MoSCoW | Se evalúa factibilidad técnica, operativa, económica y legal. Luego Excel calcula automáticamente en Resumen MoSCoW con fórmulas =COUNTIF() el peso de cada bloque (19 Must = 61,3%), asegurando un MVP viable. | Hoja: Resumen MoSCoW (fórmulas automáticas) | 1.1.2 (8,4 pts) |
| Paso 4: Historias de Usuario y Backlog SCRUM | Cada RF incluido (RF01–RF14) se convierte en su Historia de Usuario (HU01–HU14) con criterios de aceptación y estimación Fibonacci (69 SP + 8 SP técnicas = 77 SP), ordenadas por dependencias técnicas en 5 Sprints (=SUMIF()). | Hojas: Historias Usuario, Product Backlog | 1.1.2 y 1.1.6 |
| Paso 5: Planificación Detallada (Tareas, Gantt, Kanban) | Se descomponen las fases e incrementos en 39 tareas (T01–T39) con cálculo de fechas hábiles =WORKDAY()/NETWORKDAYS() con feriados de Chile, Carta Gantt visual de 13 semanas, Espacio Colaborativo y Tablero Kanban con límites WIP. | Hojas: Tareas, Carta Gantt, Espacio Colaborativo, Tablero Kanban + PNG 19 | 1.1.6 (9,6 pts) |
| Paso 6: Modelado UML de Casos de Uso y Wireframes | Desde las 14 HUs se diseñan 19 Casos de Uso (CU01–CU19) agrupados en 1 Diagrama General + 5 Modulares, se especifican los 7 flujos críticos (flujo feliz y excepciones) y se prototipan Wireframes + Mockups UI alineados. | Hojas: Casos de Uso, Especificación CU, Wireframes y Mockups + PNGs 01–06 y 15–18 | 1.1.3 (14,4 pts) |
| Paso 7: Diseño de Base de Datos en 3 Niveles (3FN) | Para soportar cada dato manipulado por los CU sin redundancia ni doble reserva, se modela el Lógico (4 dominios, 18 entidades), Relacional Pata de Gallo 3FN (18 tablas), Diccionario exhaustivo (118 columnas) y Físico DDL MySQL ejecutado con Triggers, Vistas y Evento Cron. | Hojas: Modelo BD, Diccionario Datos + SQL + PNGs 07–09 | 1.1.4 (9,6 pts) |
| Paso 8: Diagramas de Flujo TO-BE e Integración de Informe | Finalmente se trazan los 5 flujos operativos completos de principio a fin (Reserva, Cancelación <30s, Atención RBAC, Cron Recordatorios, Presupuesto+Insumos) y se consolida todo en el Informe Word formal. | Hoja: Diagramas Flujo + PNGs 10–14 + Informe Word (.docx) | 1.1.5 (9,6 pts) + 1.1.6 |

> [!TIP]
> **Fórmulas Inteligentes que Demuestran Rigor en el Libro Excel (Igual que «Huellitas»):** 1) Hoja Resumen MoSCoW usa =COUNTIF('Req Funcionales'!$D$5:$D$22, A5) y =COUNTIF('Req No Funcionales'!$E$5:$E$17, A5) para que al cambiar cualquier prioridad todo se recalcule solo. 2) Hoja Product Backlog usa =SUMIF($G$5:$G$20, A24, $F$5:$F$20) para verificar automáticamente la carga por Sprint (~19 SP). 3) Hoja Tareas usa =WORKDAY() y =NETWORKDAYS() considerando feriados legales de Chile, calculando fechas de Carta Gantt sin superposiciones manuales.

## Parte 3: Guion de Defensa Oral (12–15 Minutos) y Banco de 12 Preguntas de la Docente

### 3.1 Distribución de Roles para Exponer (Sin Leer Diapositivas)

| Bloque / Tiempo y Tema | Integrante Sugerido | Qué mostrar en pantalla y Qué explicar con tus palabras |
| --- | --- | --- |
| 0:00 – 02:30 · Problema y Toma de Requerimientos | Fernando Durán (Scrum Master / BD) | Abrir Portada y Acta Proyecto en Excel. Explicar los 5 dolores del cuaderno físico (choques horarios, espera telefónica, inasistencias, fichas expuestas) y cómo nacen los 18 RF vs 13 RNF ISO/IEC 25010. |
| 02:30 – 05:30 · MoSCoW, HUs, Backlog, Gantt y Kanban | Francisco Lara (Analista Funcional / UX) | Mostrar Resumen MoSCoW, Historias Usuario, Carta Gantt y Diagrama 19 (Tablero Kanban). Explicar por qué dejamos el 61,3% en Must, qué quedó en Won't (FONASA online, DICOM 3D, App nativa), las 39 tareas y los límites WIP del Kanban. |
| 05:30 – 09:00 · Casos de Uso UML, Wireframes y Flujos TO-BE | Francisco Lara + Cristopher Figueroa | Mostrar Diagramas 01 (General) y 03 (Agenda), más Wireframes 15–17 y Flujos 10–12. Explicar herencia de actores, <<include>> CU07 Validar disponibilidad, <<extend>> CU08/CU13, los 3 pasos de reserva (< 90 s), los 2 clics (< 30 s) y el Odontograma FDI. |
| 09:00 – 13:00 · Base de Datos en 3 Niveles, Seguridad y SQL | Cristopher Figueroa (Líder Técnico / QA) | Mostrar Diagramas 07 (Lógico), 08 (Relacional 3FN Pata de Gallo), 09 (Físico DDL) y sonrisa_sana_bd.sql. Explicar las 18 tablas (118 columnas), cómo el UNIQUE + Trigger trg_cita_bi_anti_colision elimina choques bajo concurrencia, y la doble defensa RBAC + AES-256 + auditoría. |
| 13:00 – 14:30 · Cierre y Conclusión | Todo el equipo | Recapitular métricas clave (< 1,5 s P95, 0% choques, cumplimiento Ley 20.584/19.628) y quedar atentos a las preguntas de la profesora. |

### 3.2 Banco de 12 Preguntas Típicas de la Profesora (con Respuesta Directa)

- **P1. ¿Cuál es la diferencia entre sus Requerimientos Funcionales y No Funcionales?:** «Los RF definen QUÉ funciones ofrece Sonrisa Sana (ej. RF03 reservar online, RF05 cancelar en recepción, RF08 ver ficha clínica). Los RNF bajo ISO/IEC 25010 definen CÓMO de rápido, seguro y usable debe ser eso con métricas medibles (ej. RNF04 < 1,5 s P95, RNF01 cifrado AES-256/bcrypt, RNF06 máx. 3 pasos/2 clics).»
- **P2. ¿Por qué tienen 4 RF en Won't si no aparecen en los Casos de Uso?:** «Aplicamos MoSCoW para proteger el alcance viable. Integración con bono IMED/FONASA, radiografías DICOM 3D, app nativa y seguimiento de laboratorio externo quedaron documentados como Won't acordados con la Directora Clínica para no desviar el foco del agendamiento, recordatorios y confidencialidad médica.»
- **P3. En el Diagrama de Casos de Uso 01, ¿por qué usaron <<include>> en CU07 y <<extend>> en CU08 y CU13?:** «<<include>> significa obligatoriedad: tanto reservar online (CU05) como agendar en mesón (CU06) siempre validan disponibilidad en CU07. En cambio, <<extend>> es condicional: CU08 solo sugiere horarios alternativos [si el bloque ya está ocupado], y CU13 solo emite receta [si la atención requiere fármacos].»
- **P4. ¿Por qué colocaron al Reloj del Sistema y la Pasarela Correo/WA a la derecha del diagrama UML?:** «En UML 2.5 los actores primarios que buscan un objetivo van a la izquierda y los actores secundarios o sistemas externos/temporizadores (como el Cron horario de recordatorios CU14 y la pasarela SMTP/WhatsApp) van a la derecha.»
- **P5. ¿Por qué modelaron 3 diagramas distintos de Base de Datos (07, 08 y 09)?:** «Para cumplir exactamente con el Criterio 1.1.4: el Lógico (07) muestra conceptos y 4 dominios de negocio; el Relacional (08) normaliza las 18 tablas en 3FN con PK/FK/UQ y cardinalidad Pata de Gallo; y el Físico (09 + script SQL) aterriza todo a MySQL 8.0 InnoDB con tipos VARBINARY, índices, triggers, vistas y el evento horario.»
- **P6. ¿Cómo comprueban que su base de datos está en Tercera Forma Normal (3FN)?:** «Eliminamos grupos repetitivos creando odontograma_pieza por diente FDI (1FN), garantizamos dependencia total de cada PK simple o compuesta en odontologo_especialidad (2FN) y sacamos atributos transitivos a tablas catálogo como rol, prevision, especialidad e insumo_dental para que ningún dato se duplique en paciente o cita (3FN).»
- **P7. Si dos pacientes hacen clic para reservar el mismo horario en el mismo milisegundo, ¿por qué no basta con validar en el código?:** «Porque en aplicaciones web ocurren condiciones de carrera entre leer disponibilidad e insertar. Por eso nuestro modelo físico implementa dos candados en MySQL: UNIQUE KEY uq_bloque_odontologo (id_odontologo, fecha, hora_inicio) más el trigger trg_cita_bi_anti_colision que verifica superposiciones de rango horario antes de confirmar la transacción, garantizando 0% choques físicos.»
- **P8. Si una secretaria entra al navegador en la URL de la ficha médica o mira la BD, ¿qué pasa?:** «Hay triple defensa: 1) El middleware RBAC deniega con HTTP 403 a cualquier rol distinto de Odontólogo; 2) Alergias, anamnesis, diagnósticos y observaciones están cifrados con AES-256 en columnas VARBINARY; 3) Todo acceso legítimo queda grabado en la tabla auditoria_acceso_ficha con usuario, IP y hora (Ley 20.584).»
- **P9. ¿Por qué el mensaje automático de recordatorio (Flujo 13 / UI-04) NO dice qué tratamiento tiene el paciente?:** «Por RNF03 y Ley 20.584/19.628: el WhatsApp o correo solo indica fecha, hora, box y odontólogo junto a los botones de Confirmar o Cancelar con token SHA-256 de un solo uso, protegiendo la privacidad si otra persona ve la notificación en la pantalla del teléfono.»
- **P10. ¿Qué diferencia hay entre el Wireframe de la izquierda y el Mockup de la derecha en sus láminas 15–18?:** «El Wireframe es el esquema estructural de baja fidelidad para validar jerarquía, cantidad de pasos (<= 3) y ubicación de botones sin distraer con estética. El Mockup es el diseño visual de alta fidelidad con colores clínicos accesibles (WCAG AA), estados reales y el Odontograma FDI de 32 piezas.»
- **P11. ¿Qué son los límites WIP y las métricas Lead Time / Cycle Time en su Tablero Kanban (Diagrama 19)?:** «WIP limita cuántas tarjetas simultáneas puede haber en Progreso (máx. 2/persona) o en QA (máx. 4) para evitar trabajo a medias y cuellos de botella. Lead Time (3,4 días) mide desde que una tarea entra al Sprint hasta Terminado; Cycle Time (1,6 días) mide solo el tiempo activo de trabajo.»
- **P12. ¿Por qué el libro de «Huellitas» tenía 16 hojas y el suyo tiene 18 hojas con 77 Story Points en 5 Sprints?:** «Conservamos intactas las 16 hojas, la estructura y todas las fórmulas de Huellitas (=COUNTIF, =SUMIF, =WORKDAY, =NETWORKDAYS) adaptándolas al 100% al dominio odontológico (18 tablas, odontograma FDI, citas, confidencialidad) y agregamos 2 hojas finales dedicadas —Wireframes y Mockups + Tablero Kanban— porque la rúbrica 1.1.3 y 1.1.6 las exige explícitamente.»
