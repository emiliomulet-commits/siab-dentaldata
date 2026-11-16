# Dental Data · asistente público (Cloudflare Worker `dentaldata-chat`)

Recibe las preguntas del chat de https://dentaldata.softwareinabox.eu/es/, añade la base de conocimiento pública (`/kb/*.md`) y consulta el modelo de Anthropic. Responde en streaming.

- `POST /chat` · `{messages:[{role,content}], idioma:"es"}` → `text/event-stream` con `{"t"}`, `{"fin"}` o `{"error"}`
- `GET /salud` → estado y si la clave está configurada (nunca la muestra)

Configuración en Cloudflare → Workers → dentaldata-chat → Settings → Variables and Secrets:
- `DENTAL_DATA` o `ANTHROPIC_API_KEY` (secreto, obligatorio: clave de la API de Anthropic)
- `MODEL` (opcional, por defecto `claude-haiku-5-5`)
- `LIMITE_DIA` (opcional, preguntas por visitante y día, por defecto 30)

Solo acepta peticiones desde https://dentaldata.softwareinabox.eu.
La base de conocimiento es PÚBLICA: no añadir a /kb documentos confidenciales (evaluaciones 0–10, precios, clientes, anclas).
Para añadir un documento: subir el .md a /kb y añadir su nombre a KB_FILES en worker.js.
