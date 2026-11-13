# GUÍA Y GUION PARA LA PRESENTACIÓN ORAL DEL PROYECTO
## Defensa de Evaluación N° 1: Clínica Odontológica "Sonrisa Sana"
**Asignatura:** Modelamiento de Soluciones Informáticas (Sección 114-2-F2)  
**Docente:** Yaleni Gómez Peña — INACAP  
**Expositores:** Christopher D. Figueroa Arthur (Líder Técnico) | Fernando A. Durán Leiva | Francisco A. Lara Yévenes  
**Tiempo estimado de presentación:** 12 a 15 minutos + preguntas

---

## 1. Estructura Recomendada de Diapositivas (PowerPoint / Canva)

| N° Diapositiva | Título de la Lámina | Contenido Visual Clave | Expositor Sugerido |
| :---: | :--- | :--- | :---: |
| **Lámina 1** | **Portada y Equipo** | Logo INACAP + Logo Sonrisa Sana + Nombres del equipo. | Cristopher |
| **Lámina 2** | **La Problemática del Cliente** | Imagen del cuaderno físico vs los 4 dolores de negocio. | Fernando |
| **Lámina 3** | **Levantamiento y Priorización MoSCoW** | Tabla resumen MoSCoW (16 RF y 13 RNF ISO 25010). | Francisco |
| **Lámina 4** | **Historias de Usuario (Gherkin)** | 2 ejemplos clave de Given-When-Then (HU03 y HU10). | Francisco |
| **Lámina 5** | **Diagrama de Casos de Uso (UML)** | `01_casos_de_uso_general.png` resaltando include/extend. | Cristopher |
| **Lámina 6** | **Wireframes y Experiencia de Usuario** | Mockups de Reserva (3 pasos) y Agenda Secretaría. | Francisco |
| **Lámina 7** | **Base de Datos en 3 Niveles** | `10_modelo_bd_3_niveles.png` (Lógico, Relacional, Físico). | Fernando |
| **Lámina 8** | **Diagramas de Flujo TO-BE** | Flujo de Reserva con prevención física de choques. | Fernando |
| **Lámina 9** | **Planificación Ágil: Kanban y Carta Gantt** | Tablero Kanban con límites WIP + Cronograma de Sprints. | Cristopher |
| **Lámina 10** | **Demostración en Vivo (Demo Operativa)** | Navegador web abierto con el sistema corriendo en FastAPI. | Cristopher |
| **Lámina 11** | **Conclusiones y Cumplimiento Normativo** | Métricas de éxito (P95 < 1.5s, Ley 21.719, Nota 7.0). | Todo el equipo |

---

## 2. Guion Paso a Paso: Qué decir en cada minuto

### Minuto 0:00 - 02:00 | Introducción y Problemática (Cristopher y Fernando)
> **Cristopher:** *"Buenas tardes profesora Yaleni y compañeros. Somos el equipo conformado por Fernando Durán, Francisco Lara y quien les habla, Christopher Figueroa. Hoy les presentamos la propuesta integral de modelamiento y solución informática para la Clínica Odontológica Sonrisa Sana."*  
> **Fernando:** *"Actualmente, la clínica gestiona su operación mediante un cuaderno de papel. Esto provoca cuatro graves problemas: choques de horarios por doble reserva en un mismo box, una alta tasa de pacientes que no asisten por falta de recordatorios, secretarias colapsadas por llamadas y, lo más delicado, fichas médicas en papel que no cumplen con la Ley 19.628 ni la nueva Ley 21.719 de Protección de Datos Personales en Chile."*

---

### Minuto 02:00 - 05:00 | Requerimientos, MoSCoW e Historias de Usuario (Francisco)
> **Francisco:** *"Para abordar estos dolores, levantamos 16 Requerimientos Funcionales y 13 Requerimientos No Funcionales bajo el estándar ISO/IEC 25010. Aplicamos la técnica MoSCoW para definir un MVP claro:*
> *- En los **Must Have**, priorizamos la reserva online en 3 pasos, la cancelación y reprogramación en menos de 2 clics por secretaría, el envío automático de recordatorios 24 horas antes y el control estricto de acceso a fichas clínicas.*
> *- Cada requerimiento se tradujo en Historias de Usuario con criterios de aceptación en formato Gherkin (Dado, Cuando, Entonces). Por ejemplo, en la Historia de Reserva Online, el sistema garantiza que si dos personas intentan tomar la misma hora en el mismo segundo, el motor de base de datos protege la integridad y rechaza la colisión."*

---

### Minuto 05:00 - 08:00 | Modelado UML y Base de Datos en 3 Niveles (Cristopher y Fernando)
> **Cristopher:** *"En el modelado UML definimos 4 actores principales: Paciente, Secretaria, Odontólogo y Administrador. Como observan en el diagrama de casos de uso, la 'Reserva de Cita Online' incluye obligatoriamente la validación del bloque libre y la autenticación del paciente, y se extiende opcionalmente al envío de confirmación por correo o WhatsApp. Esto lo acompañamos con wireframes y mockups de alta fidelidad que aseguran que cualquier paciente pueda reservar en menos de 90 segundos."*  
> **Fernando:** *"Respecto a los datos, y en estricto apego al Criterio 1.1.4 de la pauta, desarrollamos el modelo en sus **tres niveles**:*
> *1. **Conceptual/Lógico:** Identificamos las entidades clave del negocio odontológico.*
> *2. **Relacional:** Diseñamos 12 tablas normalizadas en Tercera Forma Normal (3FN), garantizando cero redundancia de datos.*
> *3. **Físico (DDL):** Implementamos restricciones físicas UNIQUE sobre una columna generada de bloque horario, eliminando el 100% de los choques a nivel de base de datos. Además, los diagnósticos médicos se almacenan con cifrado simétrico AES-256 en reposo, garantizando el secreto médico ante cualquier intento de fuga de información."*

---

### Minuto 08:00 - 11:00 | Planificación Ágil y Demostración en Vivo (Cristopher)
> **Cristopher:** *"El proyecto se planificó en dos Sprints utilizando un Tablero Kanban con límites de trabajo en curso (WIP) y una Carta Gantt sincronizada en nuestro libro Excel.*
> *Y como valor agregado de ingeniería, no nos quedamos solo en el papel: **construimos el prototipo web funcional en FastAPI y ejecutamos pruebas unitarias automatizadas con Pytest**."*
> 
> *(Aquí Cristopher o Fernando abren el navegador o muestran la terminal):*
> 1. *"Miren la pantalla: ejecutamos `pytest` y vemos cómo las tres pruebas de estrés validan la no-colisión, la liberación de bloques y la seguridad RBAC."*
> 2. *"Mostramos la interfaz: el paciente selecciona fecha y hora, y la secretaria ve la agenda actualizarse en tiempo real."*

---

### Minuto 11:00 - 13:00 | Cierre y Conclusiones (Equipo)
> **Cristopher:** *"En conclusión, la solución propuesta para Sonrisa Sana resuelve de raíz los problemas del agendamiento manual, cumple con creces cada uno de los 6 criterios de la rúbrica de evaluación y entrega un producto viable, escalable y seguro para la clínica. Muchas gracias, quedamos atentos a sus preguntas."*

---

## 3. Preguntas Típicas que la Profesora Yaleni Gómez Podría Hacer y Cómo Responder

### Pregunta 1: *"¿Por qué dicen que la base de datos previene los choques al 100% y no el código de la aplicación?"*
- **Respuesta ideal (decir esto con seguridad):**  
  *"Excelente pregunta, profesora. En sistemas concurrentes, si dos usuarios reservan al mismo milisegundo, la validación en código puede sufrir una condición de carrera (Race Condition) donde ambos leen que la hora está libre antes de escribir. Por eso, implementamos la restricción a nivel físico en la base de datos mediante una restricción `UNIQUE` sobre el odontólogo y el bloque horario dentro de una transacción ACID. Si la segunda reserva intenta entrar, el motor de base de datos arroja un error de integridad física y la rechaza de inmediato, garantizando cero colisiones."*

### Pregunta 2: *"¿Por qué eligieron MoSCoW en lugar de otra técnica de priorización?"*
- **Respuesta ideal:**  
  *"Porque MoSCoW se alinea de forma natural con los marcos ágiles como SCRUM y el límite de tiempo del proyecto (5 semanas). Nos permitió separar con total claridad lo que es indispensable para el MVP (Must Have) de lo que aporta valor pero no frena la salida a producción (Should y Could), evitando que el equipo se desvíe en funcionalidades accesorias."*

### Pregunta 3: *"¿Qué diferencia hay entre el Modelo Lógico y el Modelo Físico en su trabajo?"*
- **Respuesta ideal:**  
  *"El Modelo Lógico define las entidades del negocio, sus atributos esenciales y las relaciones 3FN con independencia del motor tecnológico. El Modelo Físico, en cambio, toma ese diseño y lo aterriza al RDBMS específico (MySQL/SQLite), definiendo tipos de datos de almacenamiento (VARCHAR, INT, DATETIME), índices compuestos B-Tree para optimizar búsquedas a menos de 1.5 segundos, llaves foráneas con reglas de borrado y los scripts DDL ejecutables."*

### Pregunta 4: *"¿Cómo protegen la confidencialidad de la ficha médica si una secretaria entra a la base de datos?"*
- **Respuesta ideal:**  
  *"Aplicamos dos capas de defensa: primero, a nivel de aplicación, un control de acceso por roles (RBAC) que deniega con código HTTP 403 a cualquier usuario que no sea el odontólogo tratante. Segundo, a nivel de almacenamiento físico, los textos de diagnóstico y recetas se cifran con el algoritmo AES-256 en modo CBC con vector de inicialización único. Si alguien abre directamente el archivo de base de datos, solo verá una cadena ilegible de bytes cifrados."*
