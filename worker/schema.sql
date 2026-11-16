-- Base de datos D1 «dentaldata-registro» (binding REGISTRO)
-- Registro anónimo de preguntas y respuestas del asistente. Sin IP ni datos personales.
CREATE TABLE IF NOT EXISTS registro (
  rid         TEXT PRIMARY KEY,   -- id aleatorio de cada intercambio (navegador)
  sid         TEXT,               -- id aleatorio de la sesión del navegador (sessionStorage)
  fecha       TEXT NOT NULL,      -- ISO UTC
  idioma      TEXT,               -- es | nl | en
  pagina      TEXT,               -- /es/, /nl/…
  tipo        TEXT NOT NULL,      -- ia | preparada | preparada_por_palabras | sin_respuesta
  clave       TEXT,               -- id de la respuesta preparada, si la hay
  pregunta    TEXT,               -- con correos, teléfonos, DNI/NIE e IBAN tachados
  respuesta   TEXT,
  fuentes     TEXT,               -- archivos de /kb citados por la IA
  modelo      TEXT,
  ms          INTEGER,            -- tiempo de respuesta
  error       TEXT,
  voto        INTEGER,            -- 1 útil · -1 no útil · NULL sin valorar
  actualizado TEXT,
  exportado   TEXT                -- última exportación a GitHub
);
CREATE INDEX IF NOT EXISTS idx_registro_fecha ON registro(fecha);
CREATE INDEX IF NOT EXISTS idx_registro_export ON registro(exportado, actualizado);
