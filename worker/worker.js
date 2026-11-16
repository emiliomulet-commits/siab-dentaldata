/* ══════════════════════════════════════════════════════════════
   DENTAL DATA · asistente público · Cloudflare Worker "dentaldata-chat"
   Software in a Box · dentaldata.softwareinabox.eu
   Basado en el proxy de ARGOS. Ver README.md.
   ══════════════════════════════════════════════════════════════ */

const ORIGENES = ['https://dentaldata.softwareinabox.eu', 'http://localhost:8765'];
const KB_BASE = 'https://dentaldata.softwareinabox.eu/kb/';
const KB_FILES = ['00-indice.md', '01-que-es-dental-data.md', '02-mercado-espana.md', '03-solucion-casos-uso.md',
  '04-ehds-normativa.md', '05-tecnologia.md', '06-piloto-hoja-ruta.md', '07-europa-paises-bajos.md',
  '08-empresa-recursos.md', '09-preguntas-frecuentes.md', '10-estudio-comparativo-en.md'];

let KB_CACHE = null, KB_TIME = 0;          // caché en memoria del isolate
const memLimites = new Map();               // límite aproximado si no hay KV

function cors(origin) {
  const ok = ORIGENES.includes(origin) ? origin : ORIGENES[0];
  return { 'Access-Control-Allow-Origin': ok, 'Access-Control-Allow-Methods': 'POST, OPTIONS',
           'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Max-Age': '86400', 'Vary': 'Origin' };
}
function json(obj, status, origin) {
  return new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json; charset=utf-8', ...cors(origin) } });
}

async function cargarKB() {
  if (KB_CACHE && Date.now() - KB_TIME < 3600_000) return KB_CACHE;
  const partes = await Promise.all(KB_FILES.map(async f => {
    const r = await fetch(KB_BASE + f, { cf: { cacheTtl: 3600, cacheEverything: true } });
    return r.ok ? `\n\n===== ${f} =====\n` + (await r.text()) : '';
  }));
  KB_CACHE = partes.join(''); KB_TIME = Date.now();
  return KB_CACHE;
}

async function dentroDeLimite(env, ip) {
  const limite = parseInt(env.LIMITE_DIA || '30', 10);
  const dia = new Date().toISOString().slice(0, 10);
  const clave = `l:${dia}:${ip}`;
  if (env.LIMITES) {
    const n = parseInt((await env.LIMITES.get(clave)) || '0', 10);
    if (n >= limite) return false;
    await env.LIMITES.put(clave, String(n + 1), { expirationTtl: 90000 });
    return true;
  }
  const n = memLimites.get(clave) || 0;
  if (n >= limite) return false;
  memLimites.set(clave, n + 1);
  if (memLimites.size > 5000) memLimites.clear();
  return true;
}

export default {
  async fetch(request, env, ctx) {
    const origin = request.headers.get('Origin') || '';
    const url = new URL(request.url);
    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors(origin) });
    if (url.pathname === '/salud') return json({ ok: true, modelo: env.MODEL || 'claude-haiku-5-5', clave: !!env.ANTHROPIC_API_KEY }, 200, origin);
    if (url.pathname !== '/chat' || request.method !== 'POST') return json({ error: 'No encontrado' }, 404, origin);
    if (!ORIGENES.includes(origin)) return json({ error: 'Origen no permitido' }, 403, origin);
    if (!env.ANTHROPIC_API_KEY) return json({ error: 'El asistente aún no está configurado.' }, 500, origin);

    let cuerpo;
    try { cuerpo = await request.json(); } catch { return json({ error: 'Petición no válida' }, 400, origin); }
    const idioma = cuerpo.['en','nl'].includes(cuerpo.idioma) ? cuerpo.idioma : 'es';
    const limpios = (Array.isArray(cuerpo.messages) ? cuerpo.messages : []).slice(-12)
      .map(m => ({ role: m && m.role === 'assistant' ? 'assistant' : 'user', content: String((m && m.content) || '').trim().slice(0, 2000) }))
      .filter(m => m.content);
    while (limpios.length && limpios[0].role !== 'user') limpios.shift();
    if (!limpios.length || limpios[limpios.length - 1].role !== 'user') return json({ error: 'Petición sin pregunta' }, 400, origin);

    const ip = request.headers.get('CF-Connecting-IP') || 'anon';
    if (!(await dentroDeLimite(env, ip))) {
      return json({ error: idioma === 'en'
        ? 'Daily question limit reached. Please come back tomorrow or write to partners@softwareinabox.eu.'
        : 'Ha alcanzado el límite diario de preguntas. Vuelva mañana o escriba a partners@softwareinabox.eu.' }, 429, origin);
    }

    const kb = await cargarKB();
    const reglaIdioma = idioma === 'en' ? 'Answer ALWAYS in English (the knowledge base is mostly in Spanish: translate faithfully).'
      : idioma === 'nl' ? 'Antwoord ALTIJD in het Nederlands (de kennisbank is grotendeels Spaans: vertaal getrouw).'
      : 'Responde SIEMPRE en español de España, tuteando al usuario (la parte en inglés de la base tradúcela con fidelidad).';
    const instrucciones = `Eres el asistente de la web de Dental Data (dentaldata.softwareinabox.eu), el espacio de datos de salud dental federado de Software in a Box, preparado para el Espacio Europeo de Datos Sanitarios (EHDS) y desplegado sobre Microsoft Azure. ${reglaIdioma}
Hablas con dentistas, directivos de cadenas dentales, aseguradoras, proveedores de software y partners tecnológicos. Tono profesional, cercano y claro, sin jerga innecesaria. Máximo 5 frases por respuesta; usa **negritas** para lo esencial.
Fundamenta cada respuesta EXCLUSIVAMENTE en la base de conocimiento adjunta. Si algo no está en ella, dilo con honestidad y sugiere escribir a partners@softwareinabox.eu o usar el formulario (#contacto). Nunca inventes cifras, fechas, precios, clientes, socios ni características. No des diagnóstico ni consejo clínico ni asesoramiento jurídico personalizado. No hables en nombre de Microsoft ni afirmes acuerdos con Microsoft que no estén en la base. No pidas ni almacenes datos personales y, si el usuario los escribe, no los repitas. Si preguntan por temas ajenos a Dental Data, salud dental, datos de salud o Software in a Box, indica amablemente que solo puedes hablar de Dental Data. Cuando encaje, invita a participar en el piloto.
Al final de tu respuesta añade, cada una en su línea:
[FUENTE: nombre-del-archivo.md] — uno o dos archivos de la base que fundamentan la respuesta. Obligatoria si usaste la base.
[SEGUIR: pregunta uno | pregunta dos] — dos preguntas de seguimiento breves y naturales, en el idioma de la conversación.`;

    const resp = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-api-key': env.ANTHROPIC_API_KEY, 'anthropic-version': '2023-06-01' },
      body: JSON.stringify({
        model: env.MODEL || 'claude-haiku-5-5', max_tokens: 900, stream: true,
        system: [
          { type: 'text', text: instrucciones },
          { type: 'text', text: 'BASE DE CONOCIMIENTO DENTAL DATA:\n' + kb, cache_control: { type: 'ephemeral' } }
        ],
        messages: limpios
      })
    });
    if (!resp.ok || !resp.body) {
      let detalle = 'HTTP ' + resp.status;
      try { const j = await resp.json(); detalle = (j.error && j.error.message) || detalle; } catch {}
      console.log('anthropic_error', resp.status, detalle);
      return json({ error: (idioma === 'en' ? 'The assistant is not available right now. ' : 'El asistente no está disponible en este momento. ')
        + (idioma === 'en' ? 'Please try again later.' : 'Inténtelo más tarde.') }, 502, origin);
    }

    const enc = new TextEncoder(), dec = new TextDecoder();
    const { readable, writable } = new TransformStream();
    const w = writable.getWriter();
    const emitir = o => w.write(enc.encode('data: ' + JSON.stringify(o) + '\n\n'));
    ctx.waitUntil((async () => {
      const lector = resp.body.getReader(); let buf = '', hubo = false;
      try {
        while (true) {
          const { done, value } = await lector.read(); if (done) break;
          buf += dec.decode(value, { stream: true });
          let p;
          while ((p = buf.indexOf('\n')) !== -1) {
            const linea = buf.slice(0, p).trim(); buf = buf.slice(p + 1);
            if (!linea.startsWith('data:')) continue;
            let j; try { j = JSON.parse(linea.slice(5)); } catch { continue; }
            if (j.type === 'content_block_delta' && j.delta && j.delta.text) { hubo = true; await emitir({ t: j.delta.text }); }
            else if (j.type === 'error') { await emitir({ error: idioma === 'en' ? 'The assistant was interrupted. Please try again.' : 'El asistente se interrumpió. Inténtelo de nuevo.' }); }
          }
        }
        await emitir(hubo ? { fin: true } : { error: idioma === 'en' ? 'No answer received.' : 'No se recibió respuesta.' });
      } catch (e) {
        await emitir({ error: idioma === 'en' ? 'Connection lost.' : 'Se perdió la conexión.' });
      } finally { await w.close(); }
    })());
    return new Response(readable, { headers: { 'Content-Type': 'text/event-stream; charset=utf-8', 'Cache-Control': 'no-cache', ...cors(origin) } });
  }
};
