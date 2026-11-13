# GUÍA TÉCNICA PASO A PASO: PROYECTO CLÍNICA "SONRISA SANA"
## Documento Maestro de Comprensión Integral del Proyecto
**Carrera:** Ingeniería en Informática / Analista Programador — INACAP  
**Asignatura:** Modelamiento de Soluciones Informáticas (114-2-F2)  
**Docente:** Yaleni Gómez Peña  
**Autor:** Christopher D. Figueroa Arthur (en conjunto con Fernando Durán y Francisco Lara)

---

## 1. ¿De qué trata el proyecto y cuál era el problema?

La clínica odontológica **"Sonrisa Sana"** atendía a sus pacientes y gestionaba las horas médicas con un **cuaderno de papel físico**.
Esto generaba cuatro problemas graves:
1. **Choques de horarios (colisiones):** Dos secretarias agendaban a dos pacientes a la misma hora con el mismo dentista o en el mismo box.
2. **Inasistencias elevadas ("No-shows"):** Al no haber recordatorios automáticos, muchos pacientes olvidaban su hora y el dentista quedaba desocupado perdiendo ingresos.
3. **Pérdida de tiempo y fricción:** Los pacientes solo podían pedir hora llamando por teléfono en horario de oficina.
4. **Vulnerabilidad legal y de privacidad:** Las fichas médicas con diagnósticos y tratamientos estaban expuestas sin medidas de seguridad digital, violando la **Ley N° 19.628** (Protección de la vida privada) y la nueva **Ley N° 21.719** de Protección de Datos Personales en Chile.

---

## 2. ¿Cómo resolvimos el problema? (El Paso a Paso Metodológico)

Seguimos la metodología **SDD (Spec-Driven Development)** recomendada por GitHub Spec Kit en 6 fases:

```
[1. Toma de Requerimientos] ──> [2. Priorización MoSCoW] ──> [3. Modelado UML y BD]
                                                                        │
[6. Validación con Pruebas] <── [5. Prototipo Funcional] <── [4. Wireframes / Flujos]
```

### Paso 1: Toma de Requerimientos (Criterio 1.1.1)
- Identificamos **16 Requerimientos Funcionales (RF)** (lo que el sistema debe HACER: registrar paciente, agendar cita, enviar recordatorios, cancelar, etc.).
- Identificamos **13 Requerimientos No Funcionales (RNF)** basados en la norma **ISO/IEC 25010** (cómo debe COMPORTARSE el sistema: P95 < 1.5 segundos de respuesta, cifrado AES-256 en reposo, disponibilidad 99.5%).

### Paso 2: Análisis y Priorización con MoSCoW (Criterio 1.1.2)
Para saber qué programar primero y no perdernos en funciones accesorias, clasificamos los requerimientos en:
- **Must Have (Debe tener sí o sí):** Reserva online, prevención de choques, cancelación en 2 clics, recordatorios automáticos y ficha médica con RBAC.
- **Should Have (Debería tener):** Reportes de inasistencias y gestión administrativa avanzada.
- **Could Have (Podría tener si sobra tiempo):** Integración con Google Calendar.
- **Won't Have (No tendrá en esta versión):** Pago online de tratamientos complejos y teleodontología.

### Paso 3: Historias de Usuario con Criterios Gherkin (Criterio 1.1.2)
Redactamos las historias desde la perspectiva del usuario real:
- *"Como paciente, quiero agendar online para asegurar mi atención sin ir a la clínica."*
- Definimos los criterios con la sintaxis **Dado / Cuando / Entonces (Given / When / Then)**:
  - *Dado* que selecciono fecha y odontólogo disponible,
  - *Cuando* confirmo mis datos personales y presiono reservar,
  - *Entonces* el sistema bloquea inmediatamente el horario y genera el comprobante.

### Paso 4: Modelado de Casos de Uso UML (Criterio 1.1.3)
Diseñamos el diagrama de casos de uso distinguiendo los 4 actores del sistema:
- **Paciente:** Reservar hora, consultar estado, cancelar cita.
- **Secretaria:** Gestionar agenda diaria, reprogramar en ≤ 2 clics, registrar paciente presencial.
- **Odontólogo:** Visualizar citas del día, abrir y registrar Ficha Clínica.
- **Administrador:** Gestionar usuarios, roles y especialidades.
- **Relaciones clave:**
  - `<<include>>`: Reservar Cita *incluye* necesariamente "Validar Bloque Libre" y "Autenticar Paciente".
  - `<<extend>>`: La reserva puede extenderse opcionalmente a "Notificar por WhatsApp / Correo".

### Paso 5: Arquitectura de Base de Datos en 3 Niveles (Criterio 1.1.4)
Este punto es donde más valor agregamos frente a la rúbrica:
1. **Nivel Conceptual / Lógico:** Entidades de negocio (Paciente, Profesional, Cita, Box, Especialidad, Ficha Médica).
2. **Nivel Relacional (3FN):** 12 tablas normalizadas en Tercera Forma Normal para evitar redundancia y anomalías de actualización. Claves primarias (PK) y foráneas (FK) con integridad referencial.
3. **Nivel Físico (DDL SQL):**
   - Script SQL ejecutable en MySQL/SQLite.
   - **La solución estrella para evitar choques:** Columna generada con restricción `UNIQUE (odontologo_id, fecha_hora)` que rechaza a nivel de motor de base de datos cualquier intento de reserva simultánea.
   - Cifrado **AES-256-CBC** para los campos de diagnóstico en la tabla `ficha_clinica`.

### Paso 6: Diagramas de Flujo TO-BE (Criterio 1.1.5)
Modelamos los 3 procesos del negocio:
- **Flujo 1:** Reserva Online (el paciente busca disponibilidad, el sistema valida y confirma).
- **Flujo 2:** Gestión de Secretaría (reprogramación y cancelación rápida liberando el bloque al instante).
- **Flujo 3:** Scheduler de Recordatorios (cada 15 minutos un proceso automático busca citas a 24 horas y despacha alertas).

### Paso 7: Planificación Ágil con Kanban y Carta Gantt (Criterio 1.1.6)
- Estructuramos el proyecto en 2 Sprints (Sprint 1: Base de datos y arquitectura / Sprint 2: Reserva, seguridad y recordatorios).
- Diseñamos el **Tablero Kanban** con columnas: *Backlog*, *To Do*, *In Progress (WIP: 3)*, *Code Review (WIP: 2)* y *Done*.
- La **Carta Gantt** abarca del 19 de octubre al 17 de noviembre con todos los hitos y responsables del equipo.

---

## 3. ¿Cómo funciona el Software y las Pruebas?

En [`Sistema/`](file:///root/INACAP/03_mi_trabajo/Sistema):
- **Backend:** Desarrollado con **FastAPI (Python)** por ser ultrarrápido y moderno.
- **Seguridad:** Módulo [`security.py`](file:///root/INACAP/03_mi_trabajo/Sistema/app/security.py) con **bcrypt** para contraseñas, tokens JWT para sesiones y **AES-256** para las fichas médicas.
- **Pruebas Automatizadas:** En [`tests/test_sistema.py`](file:///root/INACAP/03_mi_trabajo/Sistema/tests/test_sistema.py), se ejecutan 3 pruebas críticas con `pytest`:
  1. `test_reserva_online_y_prevencion_choque`: Intenta reservar dos veces el mismo bloque y comprueba que la segunda es rechazada con código HTTP 409.
  2. `test_secretaria_reprograma_y_cancela`: Comprueba que una cita cancelada libera inmediatamente el bloque.
  3. `test_rbac_estricto_ficha_clinica_y_cifrado_aes256`: Comprueba que un usuario sin rol de odontólogo recibe HTTP 403 al intentar ver una ficha, y que los datos en la base de datos están cifrados.

---

## 4. Resumen de Archivos para Entregar y Mostrar

1. **Informe Principal:** [`Cristopher_Figueroa.docx`](file:///root/INACAP/03_mi_trabajo/Cristopher_Figueroa.docx) (El informe formal que se sube al aula virtual).
2. **Libro Excel del Proyecto:** [`Cristopher_Figueroa_Proyecto.xlsx`](file:///root/INACAP/03_mi_trabajo/Cristopher_Figueroa_Proyecto.xlsx) (Las 17 hojas metodológicas basadas en el estándar de la docente).
3. **Diagramas en Alta Resolución:** En [`diagramas/`](file:///root/INACAP/03_mi_trabajo/diagramas/).
4. **Sistema Operativo:** En [`Sistema/`](file:///root/INACAP/03_mi_trabajo/Sistema/) (Ejecutable con `./iniciar_sistema.sh` o `python3 run_server.py`).
