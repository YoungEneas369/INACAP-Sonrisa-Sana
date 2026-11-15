-- ============================================================================
-- SISTEMA DE GESTIÓN ODONTOLÓGICA "SONRISA SANA" (SGO-SonrisaSana)
-- Base de Datos Relacional en 3FN - Motor MySQL 8.0+ / InnoDB / utf8mb4
-- Alineado a Evaluación Sumativa 5 - Modelamiento de Soluciones Informáticas
-- Autores: Cristopher D. Figueroa Arthur, Fernando A. Durán Leiva, Francisco A. Lara Yévenes
-- Docente: Yaleni Gómez Peña (INACAP - Sección 114-2-F2)
-- ============================================================================

DROP DATABASE IF EXISTS sonrisa_sana_db;
CREATE DATABASE sonrisa_sana_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE sonrisa_sana_db;

-- ============================================================================
-- 1. SEGURIDAD, ROLES, ODONTÓLOGOS Y HORARIOS (HU02, HU14)
-- ============================================================================

CREATE TABLE rol (
  id_rol INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE usuario (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  id_rol INT NOT NULL,
  rut VARCHAR(12) NOT NULL UNIQUE,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(100) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  CONSTRAINT fk_usuario_rol FOREIGN KEY (id_rol) REFERENCES rol(id_rol)
) ENGINE=InnoDB;

CREATE TABLE especialidad (
  id_especialidad INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(60) NOT NULL UNIQUE,
  descripcion VARCHAR(200) NULL
) ENGINE=InnoDB;

CREATE TABLE odontologo_especialidad (
  id_odontologo INT NOT NULL,
  id_especialidad INT NOT NULL,
  registro_superint VARCHAR(30) NOT NULL UNIQUE,
  PRIMARY KEY (id_odontologo, id_especialidad),
  CONSTRAINT fk_oesp_odontologo FOREIGN KEY (id_odontologo) REFERENCES usuario(id_usuario),
  CONSTRAINT fk_oesp_especialidad FOREIGN KEY (id_especialidad) REFERENCES especialidad(id_especialidad)
) ENGINE=InnoDB;

CREATE TABLE horario_odontologo (
  id_horario INT AUTO_INCREMENT PRIMARY KEY,
  id_odontologo INT NOT NULL,
  dia_semana TINYINT NOT NULL COMMENT '1=Lunes .. 7=Domingo',
  hora_inicio TIME NOT NULL,
  hora_fin TIME NOT NULL,
  duracion_bloque_min SMALLINT NOT NULL DEFAULT 30,
  box_asignado VARCHAR(20) NOT NULL,
  CONSTRAINT chk_horario_dia CHECK (dia_semana BETWEEN 1 AND 7),
  CONSTRAINT chk_horario_rango CHECK (hora_fin > hora_inicio),
  CONSTRAINT chk_horario_duracion CHECK (duracion_bloque_min IN (15, 20, 30, 45, 60)),
  CONSTRAINT fk_horario_odontologo FOREIGN KEY (id_odontologo) REFERENCES usuario(id_usuario)
) ENGINE=InnoDB;

-- ============================================================================
-- 2. PACIENTES Y PREVISIÓN DE SALUD (HU01)
-- ============================================================================

CREATE TABLE prevision (
  id_prevision INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL UNIQUE,
  tipo ENUM('FONASA', 'ISAPRE', 'PARTICULAR') NOT NULL
) ENGINE=InnoDB;

CREATE TABLE paciente (
  id_paciente INT AUTO_INCREMENT PRIMARY KEY,
  id_prevision INT NOT NULL,
  rut VARCHAR(12) NOT NULL UNIQUE,
  nombre VARCHAR(80) NOT NULL,
  apellido VARCHAR(80) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  telefono VARCHAR(15) NOT NULL,
  correo VARCHAR(100) NOT NULL UNIQUE,
  direccion VARCHAR(150) NOT NULL,
  password_hash VARCHAR(255) NULL,
  consentimiento_datos TINYINT(1) NOT NULL DEFAULT 1 COMMENT 'Ley 19.628 / 21.719',
  fecha_registro DATE NOT NULL,
  INDEX idx_pac_apellido (apellido, nombre),
  CONSTRAINT fk_paciente_prevision FOREIGN KEY (id_prevision) REFERENCES prevision(id_prevision)
) ENGINE=InnoDB;

-- ============================================================================
-- 3. AGENDAMIENTO DE CITAS Y RECORDATORIOS AUTOMÁTICOS (HU03, HU04, HU05, HU06, HU07)
-- ============================================================================

CREATE TABLE cita (
  id_cita INT AUTO_INCREMENT PRIMARY KEY,
  id_paciente INT NOT NULL,
  id_odontologo INT NOT NULL,
  id_usuario_gestion INT NULL COMMENT 'NULL cuando es autogestión web del paciente',
  canal_origen ENUM('web_paciente', 'recepcion') NOT NULL DEFAULT 'web_paciente',
  fecha DATE NOT NULL,
  hora_inicio TIME NOT NULL,
  hora_fin TIME NOT NULL,
  motivo VARCHAR(200) NOT NULL,
  estado ENUM('pendiente', 'confirmada', 'atendida', 'cancelada', 'no_asiste') NOT NULL DEFAULT 'pendiente',
  motivo_cancelacion VARCHAR(200) NULL,
  fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_bloque_odontologo (id_odontologo, fecha, hora_inicio),
  INDEX idx_cita_agenda_dia (fecha, id_odontologo, estado),
  INDEX idx_cita_paciente (id_paciente, fecha),
  CONSTRAINT chk_cita_horas CHECK (hora_fin > hora_inicio),
  CONSTRAINT fk_cita_paciente FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente),
  CONSTRAINT fk_cita_odontologo FOREIGN KEY (id_odontologo) REFERENCES usuario(id_usuario),
  CONSTRAINT fk_cita_usuario_gestion FOREIGN KEY (id_usuario_gestion) REFERENCES usuario(id_usuario)
) ENGINE=InnoDB;

CREATE TABLE recordatorio_cita (
  id_recordatorio INT AUTO_INCREMENT PRIMARY KEY,
  id_cita INT NOT NULL,
  fecha_programada DATETIME NOT NULL,
  fecha_envio DATETIME NULL,
  canal ENUM('correo', 'whatsapp') NOT NULL,
  token_confirmacion VARCHAR(64) NOT NULL UNIQUE,
  estado ENUM('pendiente', 'enviado', 'confirmado', 'cancelado_paciente', 'fallido') NOT NULL DEFAULT 'pendiente',
  INDEX idx_rec_programado (estado, fecha_programada),
  CONSTRAINT fk_rec_cita FOREIGN KEY (id_cita) REFERENCES cita(id_cita)
) ENGINE=InnoDB;

-- ============================================================================
-- 4. FICHA CLÍNICA CONFIDENCIAL, AUDITORÍA RBAC Y ODONTOGRAMA (HU08, HU09, HU10)
-- ============================================================================

CREATE TABLE ficha_clinica (
  id_ficha INT AUTO_INCREMENT PRIMARY KEY,
  id_paciente INT NOT NULL UNIQUE,
  grupo_sanguineo VARCHAR(5) NULL,
  alergias_cifradas VARBINARY(512) NULL COMMENT 'Cifrado AES-256 en reposo',
  anamnesis_medica_cifrada VARBINARY(2048) NULL COMMENT 'Cifrado AES-256 en reposo',
  fecha_apertura DATE NOT NULL,
  ultima_actualizacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_ficha_paciente FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente)
) ENGINE=InnoDB;

CREATE TABLE auditoria_acceso_ficha (
  id_auditoria BIGINT AUTO_INCREMENT PRIMARY KEY,
  id_ficha INT NOT NULL,
  id_usuario INT NOT NULL,
  accion ENUM('consulta', 'creacion', 'modificacion') NOT NULL,
  ip_origen VARCHAR(45) NOT NULL,
  fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_aud_ficha_fecha (id_ficha, fecha_hora),
  CONSTRAINT fk_aud_ficha FOREIGN KEY (id_ficha) REFERENCES ficha_clinica(id_ficha),
  CONSTRAINT fk_aud_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
) ENGINE=InnoDB;

CREATE TABLE atencion_odontologica (
  id_atencion INT AUTO_INCREMENT PRIMARY KEY,
  id_ficha INT NOT NULL,
  id_cita INT NULL UNIQUE COMMENT 'NULL si corresponde a atención de urgencia sin cita previa',
  id_odontologo INT NOT NULL,
  fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  diagnostico_cifrado VARBINARY(1024) NOT NULL COMMENT 'Cifrado AES-256 en reposo',
  procedimiento_realizado VARCHAR(200) NOT NULL,
  observaciones_cifradas VARBINARY(1024) NULL,
  INDEX idx_atencion_ficha (id_ficha, fecha_hora),
  CONSTRAINT fk_aten_ficha FOREIGN KEY (id_ficha) REFERENCES ficha_clinica(id_ficha),
  CONSTRAINT fk_aten_cita FOREIGN KEY (id_cita) REFERENCES cita(id_cita),
  CONSTRAINT fk_aten_odontologo FOREIGN KEY (id_odontologo) REFERENCES usuario(id_usuario)
) ENGINE=InnoDB;

CREATE TABLE odontograma_pieza (
  id_odontograma_pieza INT AUTO_INCREMENT PRIMARY KEY,
  id_atencion INT NOT NULL,
  numero_pieza_fdi SMALLINT NOT NULL,
  cara_dental VARCHAR(15) NOT NULL,
  estado_hallazgo ENUM('sano', 'caries', 'obturado', 'endodoncia', 'corona', 'extraccion_indicada', 'ausente', 'implante') NOT NULL,
  tratamiento_aplicado VARCHAR(150) NOT NULL,
  CONSTRAINT chk_pieza_fdi CHECK (numero_pieza_fdi BETWEEN 11 AND 85),
  CONSTRAINT fk_odo_atencion FOREIGN KEY (id_atencion) REFERENCES atencion_odontologica(id_atencion)
) ENGINE=InnoDB;

CREATE TABLE prescripcion_dental (
  id_prescripcion INT AUTO_INCREMENT PRIMARY KEY,
  id_atencion INT NOT NULL,
  medicamento VARCHAR(120) NOT NULL,
  dosis VARCHAR(60) NOT NULL,
  frecuencia VARCHAR(60) NOT NULL,
  duracion VARCHAR(50) NOT NULL,
  indicaciones VARCHAR(250) NULL,
  CONSTRAINT fk_presc_atencion FOREIGN KEY (id_atencion) REFERENCES atencion_odontologica(id_atencion)
) ENGINE=InnoDB;

-- ============================================================================
-- 5. INSUMOS ODONTOLÓGICOS Y PRESUPUESTOS / COBRO (HU11, HU12, HU13)
-- ============================================================================

CREATE TABLE insumo_dental (
  id_insumo INT AUTO_INCREMENT PRIMARY KEY,
  codigo VARCHAR(20) NOT NULL UNIQUE,
  nombre VARCHAR(100) NOT NULL,
  unidad VARCHAR(20) NOT NULL,
  stock_actual INT NOT NULL DEFAULT 0,
  stock_minimo INT NOT NULL DEFAULT 5,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  CONSTRAINT chk_insumo_stock CHECK (stock_actual >= 0 AND stock_minimo >= 0)
) ENGINE=InnoDB;

CREATE TABLE movimiento_insumo (
  id_movimiento INT AUTO_INCREMENT PRIMARY KEY,
  id_insumo INT NOT NULL,
  id_usuario INT NOT NULL,
  tipo ENUM('ingreso', 'egreso') NOT NULL,
  cantidad INT NOT NULL,
  fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  motivo VARCHAR(200) NULL,
  CONSTRAINT chk_mov_cantidad CHECK (cantidad > 0),
  CONSTRAINT fk_mov_insumo FOREIGN KEY (id_insumo) REFERENCES insumo_dental(id_insumo),
  CONSTRAINT fk_mov_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
) ENGINE=InnoDB;

CREATE TABLE alerta_insumo (
  id_alerta INT AUTO_INCREMENT PRIMARY KEY,
  id_insumo INT NOT NULL,
  fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  stock_actual INT NOT NULL,
  stock_minimo INT NOT NULL,
  estado ENUM('activa', 'resuelta') NOT NULL DEFAULT 'activa',
  CONSTRAINT fk_alerta_insumo FOREIGN KEY (id_insumo) REFERENCES insumo_dental(id_insumo)
) ENGINE=InnoDB;

CREATE TABLE boleta_factura (
  id_documento INT AUTO_INCREMENT PRIMARY KEY,
  id_paciente INT NOT NULL,
  id_atencion INT NULL,
  id_usuario INT NOT NULL,
  tipo_documento ENUM('boleta', 'factura', 'presupuesto') NOT NULL,
  fecha_emision DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  monto_total INT NOT NULL,
  medio_pago ENUM('efectivo', 'debito', 'credito', 'transferencia', 'pendiente') NOT NULL DEFAULT 'pendiente',
  estado ENUM('pendiente_pago', 'pagada', 'anulada') NOT NULL DEFAULT 'pendiente_pago',
  INDEX idx_doc_fecha_estado (fecha_emision, estado),
  CONSTRAINT chk_doc_monto CHECK (monto_total >= 0),
  CONSTRAINT fk_doc_paciente FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente),
  CONSTRAINT fk_doc_atencion FOREIGN KEY (id_atencion) REFERENCES atencion_odontologica(id_atencion),
  CONSTRAINT fk_doc_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
) ENGINE=InnoDB;

-- ============================================================================
-- 6. TRIGGERS DE INTEGRIDAD, SEGURIDAD Y AUTOMATIZACIÓN
-- ============================================================================

DELIMITER $$

-- Impide choques de horario incluso ante cancelaciones/reprogramaciones concurrentes
CREATE TRIGGER trg_cita_bi_anti_colision
BEFORE INSERT ON cita
FOR EACH ROW
BEGIN
  IF EXISTS (
    SELECT 1 FROM cita
    WHERE id_odontologo = NEW.id_odontologo
      AND fecha = NEW.fecha
      AND estado IN ('pendiente', 'confirmada', 'atendida')
      AND (NEW.hora_inicio < hora_fin AND NEW.hora_fin > hora_inicio)
  ) THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Conflicto de horario: el odontólogo ya tiene una cita activa en ese bloque.';
  END IF;
END$$

-- Marca la cita asociada como 'atendida' automáticamente al guardar una atención
CREATE TRIGGER trg_atencion_ai_marcar_cita
AFTER INSERT ON atencion_odontologica
FOR EACH ROW
BEGIN
  IF NEW.id_cita IS NOT NULL THEN
    UPDATE cita SET estado = 'atendida' WHERE id_cita = NEW.id_cita;
  END IF;
  INSERT INTO auditoria_acceso_ficha (id_ficha, id_usuario, accion, ip_origen, fecha_hora)
  VALUES (NEW.id_ficha, NEW.id_odontologo, 'modificacion', '127.0.0.1', NOW());
END$$

-- Valida stock suficiente antes de registrar un egreso de insumos
CREATE TRIGGER trg_mov_insumo_bi
BEFORE INSERT ON movimiento_insumo
FOR EACH ROW
BEGIN
  DECLARE v_stock INT;
  SELECT stock_actual INTO v_stock FROM insumo_dental WHERE id_insumo = NEW.id_insumo FOR UPDATE;
  IF NEW.tipo = 'egreso' AND v_stock < NEW.cantidad THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Stock insuficiente: el egreso supera el stock disponible.';
  END IF;
END$$

-- Actualiza stock_actual y genera o resuelve alertas automáticamente
CREATE TRIGGER trg_mov_insumo_ai
AFTER INSERT ON movimiento_insumo
FOR EACH ROW
BEGIN
  DECLARE v_actual INT;
  DECLARE v_minimo INT;
  IF NEW.tipo = 'ingreso' THEN
    UPDATE insumo_dental SET stock_actual = stock_actual + NEW.cantidad WHERE id_insumo = NEW.id_insumo;
  ELSE
    UPDATE insumo_dental SET stock_actual = stock_actual - NEW.cantidad WHERE id_insumo = NEW.id_insumo;
  END IF;

  SELECT stock_actual, stock_minimo INTO v_actual, v_minimo
  FROM insumo_dental WHERE id_insumo = NEW.id_insumo;

  IF v_actual <= v_minimo THEN
    INSERT INTO alerta_insumo (id_insumo, stock_actual, stock_minimo, estado)
    VALUES (NEW.id_insumo, v_actual, v_minimo, 'activa');
  ELSE
    UPDATE alerta_insumo SET estado = 'resuelta'
    WHERE id_insumo = NEW.id_insumo AND estado = 'activa';
  END IF;
END$$

-- ============================================================================
-- 7. EVENTO AUTOMÁTICO DIARIO DE RECORDATORIOS DE CITAS (HU07, RNF09)
-- ============================================================================

CREATE EVENT IF NOT EXISTS ev_recordatorios_citas_horario
ON SCHEDULE EVERY 1 HOUR
DO
BEGIN
  INSERT INTO recordatorio_cita (id_cita, fecha_programada, canal, token_confirmacion, estado)
  SELECT
    c.id_cita,
    NOW(),
    'whatsapp',
    SHA2(CONCAT(c.id_cita, '-', UUID()), 256),
    'pendiente'
  FROM cita c
  WHERE c.estado = 'pendiente'
    AND TIMESTAMP(c.fecha, c.hora_inicio) BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 24 HOUR)
    AND NOT EXISTS (
      SELECT 1 FROM recordatorio_cita r WHERE r.id_cita = c.id_cita
    );
END$$

DELIMITER ;

-- ============================================================================
-- 8. VISTAS SQL DE CONSULTA RÁPIDA (< 1,5 s)
-- ============================================================================

CREATE OR REPLACE VIEW v_agenda_diaria AS
SELECT
  c.id_cita,
  c.fecha,
  c.hora_inicio,
  c.hora_fin,
  c.estado,
  c.canal_origen,
  c.motivo,
  p.rut AS rut_paciente,
  CONCAT(p.nombre, ' ', p.apellido) AS nombre_paciente,
  p.telefono AS telefono_paciente,
  u.id_usuario AS id_odontologo,
  u.nombre AS nombre_odontologo
FROM cita c
JOIN paciente p ON p.id_paciente = c.id_paciente
JOIN usuario u ON u.id_usuario = c.id_odontologo
ORDER BY c.fecha, c.hora_inicio;

CREATE OR REPLACE VIEW v_historial_odontologico AS
SELECT
  a.id_atencion,
  f.id_ficha,
  p.id_paciente,
  p.rut,
  CONCAT(p.nombre, ' ', p.apellido) AS paciente,
  a.fecha_hora,
  u.nombre AS odontologo,
  a.procedimiento_realizado,
  CAST(AES_DECRYPT(a.diagnostico_cifrado, 'CLAVE_MAESTRA_SONRISA_SANA_2026') AS CHAR) AS diagnostico_descifrado,
  op.numero_pieza_fdi,
  op.estado_hallazgo,
  op.tratamiento_aplicado
FROM atencion_odontologica a
JOIN ficha_clinica f ON f.id_ficha = a.id_ficha
JOIN paciente p ON p.id_paciente = f.id_paciente
JOIN usuario u ON u.id_usuario = a.id_odontologo
LEFT JOIN odontograma_pieza op ON op.id_atencion = a.id_atencion;

CREATE OR REPLACE VIEW v_alertas_insumos_activas AS
SELECT
  al.id_alerta,
  i.codigo,
  i.nombre AS insumo,
  al.stock_actual,
  al.stock_minimo,
  al.fecha_hora,
  al.estado
FROM alerta_insumo al
JOIN insumo_dental i ON i.id_insumo = al.id_insumo
WHERE al.estado = 'activa'
ORDER BY al.fecha_hora DESC;

CREATE OR REPLACE VIEW v_ingresos_periodo AS
SELECT
  DATE(fecha_emision) AS fecha,
  tipo_documento,
  medio_pago,
  COUNT(*) AS cantidad_documentos,
  SUM(monto_total) AS total_clp
FROM boleta_factura
WHERE estado = 'pagada'
GROUP BY DATE(fecha_emision), tipo_documento, medio_pago;

-- ============================================================================
-- 9. DATOS SEMILLA INICIALES (CLÍNICA ODONTOLÓGICA "SONRISA SANA")
-- ============================================================================

INSERT INTO rol (nombre) VALUES
('Administrador'), ('Odontólogo'), ('Secretaria'), ('Encargado de Insumos');

INSERT INTO usuario (id_rol, rut, nombre, correo, password_hash) VALUES
(1, '15.234.890-1', 'Dra. Valeria Morales', 'vmorales@sonrisasana.cl', '$2b$12$ejemploHashBcryptAdminValeria0000000000000000000000'),
(2, '16.789.432-5', 'Dr. Matías Contreras', 'mcontreras@sonrisasana.cl', '$2b$12$ejemploHashBcryptOdontoMatias000000000000000000000'),
(2, '17.112.654-K', 'Dra. Sofía Alarcón', 'salarcon@sonrisasana.cl', '$2b$12$ejemploHashBcryptOdontoSofia0000000000000000000000'),
(3, '19.345.210-8', 'Carla Jiménez', 'recepcion@sonrisasana.cl', '$2b$12$ejemploHashBcryptSecretariaCarla000000000000000000'),
(4, '18.654.321-0', 'Rodrigo Fuentes', 'insumos@sonrisasana.cl', '$2b$12$ejemploHashBcryptInsumosRodrigo000000000000000000');

INSERT INTO especialidad (nombre, descripcion) VALUES
('Odontología General', 'Diagnóstico, limpieza, obturaciones y prevención'),
('Ortodoncia', 'Corrección de maloclusiones y alineación dental'),
('Endodoncia', 'Tratamientos de conducto y urgencias pulpares'),
('Implantología', 'Implantes óseointegrados y rehabilitación oral');

INSERT INTO odontologo_especialidad (id_odontologo, id_especialidad, registro_superint) VALUES
(2, 1, 'SUP-ODO-44812'),
(2, 3, 'SUP-END-44813'),
(3, 2, 'SUP-ORT-51209');

INSERT INTO horario_odontologo (id_odontologo, dia_semana, hora_inicio, hora_fin, duracion_bloque_min, box_asignado) VALUES
(2, 1, '09:00:00', '18:00:00', 30, 'Box 1'),
(2, 3, '09:00:00', '18:00:00', 30, 'Box 1'),
(3, 2, '10:00:00', '19:00:00', 30, 'Box 2');

INSERT INTO prevision (nombre, tipo) VALUES
('FONASA Tramo A/B', 'FONASA'),
('FONASA Tramo C/D', 'FONASA'),
('Isapre Colmena', 'ISAPRE'),
('Isapre Banmédica', 'ISAPRE'),
('Particular', 'PARTICULAR');

INSERT INTO paciente (id_prevision, rut, nombre, apellido, fecha_nacimiento, telefono, correo, direccion, consentimiento_datos, fecha_registro) VALUES
(1, '18.452.910-3', 'Camila', 'Rojas', '1995-04-12', '+56987412209', 'camila.rojas@correo.cl', 'Av. Vicuña Mackenna 4820', 1, '2026-11-01'),
(3, '14.920.114-7', 'Luis', 'Pérez', '1988-09-23', '+56971234567', 'luis.perez@correo.cl', 'Calle San Carlos 1240', 1, '2026-11-02');

INSERT INTO ficha_clinica (id_paciente, grupo_sanguineo, alergias_cifradas, anamnesis_medica_cifrada, fecha_apertura) VALUES
(1, 'O+', AES_ENCRYPT('Alergia a Penicilina y Amoxicilina', 'CLAVE_MAESTRA_SONRISA_SANA_2026'), AES_ENCRYPT('Sin patologías crónicas declaradas', 'CLAVE_MAESTRA_SONRISA_SANA_2026'), '2026-11-01');

INSERT INTO cita (id_paciente, id_odontologo, id_usuario_gestion, canal_origen, fecha, hora_inicio, hora_fin, motivo, estado) VALUES
(1, 2, NULL, 'web_paciente', '2026-11-18', '10:00:00', '10:30:00', 'Evaluación molar superior derecha', 'confirmada'),
(2, 2, 4, 'recepcion', '2026-11-18', '09:30:00', '10:00:00', 'Limpieza dental preventiva', 'pendiente');

INSERT INTO insumo_dental (codigo, nombre, unidad, stock_actual, stock_minimo) VALUES
('INS-001', 'Anestesia Lidocaína 2% c/Epinefrina (Caja 50 tubos)', 'Caja', 12, 4),
('INS-002', 'Resina Compuesta A2 Nanohíbrida Jeringa 4g', 'Unidad', 6, 3),
('INS-003', 'Guantes Nitrilo Talla M (Caja 100 u.)', 'Caja', 3, 5);
