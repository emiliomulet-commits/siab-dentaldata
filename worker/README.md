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

## Registro de preguntas y respuestas (desde el 16/11/2026)

Cada intercambio del asistente (respuesta preparada, respuesta de IA o «sin respuesta») se guarda de forma **anónima** en la base D1 `dentaldata-registro`, con la valoración 👍/👎 si el visitante la da:
- No se guarda la IP ni ningún dato del visitante: solo un id aleatorio de sesión del navegador.
- Antes de guardar se tachan correos, teléfonos, DNI/NIE e IBAN.
- Se conserva 12 meses.
- Rutas nuevas: `POST /registro` (respuestas preparadas, desde la página) y `POST /valoracion` (`{rid, voto: 1 | -1}`). Solo aceptan el origen de la web.

Cada noche (03:15 UTC) el cron exporta lo nuevo al repositorio **privado** `siab-dentaldata-dev`, en `_registro/AAAA/AAAA-MM-DD.jsonl` (una línea por intercambio; si cambia la valoración, se añade otra línea con el mismo `rid`: vale la última). Allí una tarea programada de Claude genera cada semana el Excel y el informe de mejoras.

### Puesta en marcha (una vez)
1. `wrangler d1 create dentaldata-registro` y pegar el `database_id` en `wrangler.toml`.
2. `wrangler d1 execute dentaldata-registro --remote --file=schema.sql`
3. En GitHub, crear un token *fine-grained* con acceso **solo** a `siab-dentaldata-dev` y permiso **Contents: Read and write**. Luego `wrangler secret put GITHUB_TOKEN`.
4. `wrangler deploy` (desde esta carpeta).
5. Comprobar: hacer una pregunta en la web y, al día siguiente, ver el archivo en `_registro/` del repositorio privado. Para forzar la exportación sin esperar: Cloudflare → Workers → dentaldata-chat → Settings → Triggers → ejecutar el cron.

Si falta la base D1 o el token, el asistente sigue funcionando igual; simplemente no registra o no exporta.
