/* ══════════════════════════════════════════════════════════════
   DENTAL DATA · asistente público · Cloudflare Worker "dentaldata-chat"
   Software in a Box · dentaldata.softwareinabox.eu
   Basado en el proxy de ARGOS. Ver README.md.
   ══════════════════════════════════════════════════════════════ */

const ORIGENES = ['https://dentaldata.softwareinabox.eu', 'http://localhost:8765'];
const KB_BASE = 'https://dentaldata.softwareinabox.eu/kb/';
/* Base de conocimiento por mercado: una parte común y otra del país de la página.
   Así un visitante de una página no recibe cifras, leyes ni ofertas de otro país. */
const KB_COMUN = ['01-que-es-dental-data.md', '03-solucion-casos-uso.md', '05-tecnologia.md', '08-empresa-recursos.md',
  '11-ehds-europa.md', '10-estudio-comparativo-en.md'];
const KB_PAIS = {
  es: ['02-mercado-espana.md', '04-ehds-normativa.md', '06-piloto-hoja-ruta.md', '07-europa-paises-bajos.md', '09-preguntas-frecuentes.md'],
  nl: ['pais/nl.md'],
  be: ['pais/be.md'],
  de: ['pais/de.md'],
  dk: ['pais/dk.md'],
  eu: ['pais/europa.md', '07-europa-paises-bajos.md']
};
const PAISES = { es: 'España', nl: 'Países Bajos', be: 'Bélgica', de: 'Alemania', dk: 'Dinamarca', fr: 'Francia', it: 'Italia', pt: 'Portugal', eu: 'Europa (página en inglés)' };
const IDIOMAS = {
  es: 'Responde SIEMPRE en español de España, tuteando al usuario (la parte en inglés de la base tradúcela con fidelidad). Usa «Espacio Europeo de Datos de Salud (EEDS)».',
  en: 'Answer ALWAYS in British English (the knowledge base is mostly in Spanish: translate faithfully). Say "European Health Data Space (EHDS)" and "health data access body".',
  nl: 'Antwoord ALTIJD in het Nederlands, met "u" (de kennisbank is grotendeels Spaans: vertaal getrouw). Gebruik "Europese ruimte voor gezondheidsgegevens (EHDS)".',
  fr: 'Réponds TOUJOURS en français, en vouvoyant (la base est surtout en espagnol : traduis fidèlement). Dis « Espace européen des données de santé (EEDS) ».',
  de: 'Antworte IMMER auf Deutsch und siezend (die Wissensbasis ist überwiegend Spanisch: getreu übersetzen). Sage „Europäischer Gesundheitsdatenraum (EHDS)“.',
  it: 'Rispondi SEMPRE in italiano, con il Lei (la base è soprattutto in spagnolo: traduci fedelmente). Di\' «Spazio europeo dei dati sanitari (EHDS)».',
  pt: 'Responde SEMPRE em português europeu (sem brasileirismos; a base está sobretudo em espanhol: traduz fielmente). Diz «Espaço Europeu de Dados de Saúde (EEDS)» e «médico dentista».',
  da: 'Svar ALTID på dansk (vidensbasen er mest på spansk: oversæt nøjagtigt). Skriv "Det europæiske sundhedsdataområde (EHDS)".'
};
function kbDe(pais) { return KB_COMUN.concat(KB_PAIS[pais] || KB_PAIS.eu); }

const KB_CACHE = new Map();                 // caché en memoria del isolate, por mercado
const memLimites = new Map();               // límite aproximado si no hay KV

/* ── Registro anónimo de preguntas y respuestas (D1 «REGISTRO») ───────────────
   Sin IP ni identificadores personales: solo un id aleatorio de sesión del navegador.
   Se tachan correos, teléfonos, DNI/NIE e IBAN antes de guardar. Ver README.md. */
const RID_OK = /^[A-Za-z0-9-]{8,48}$/;
function tachar(t) {
  return String(t || '')
    .replace(/[\w.+-]+@[\w-]+(\.[\w-]+)+/g, '[correo]')
    .replace(/\b[A-Z]{2}\d{2}(?:\s?[A-Z0-9]{4}){3,7}\b/gi, '[iban]')
    .replace(/\b[XYZ]?\d{7,8}[A-Z]\b/gi, '[documento]')
    .replace(/(?:\+\d{1,3}[\s.-]?)?(?:\d[\s.-]?){9,}/g, '[teléfono]');
}
function limpiarRespuesta(t) { return String(t || '').replace(/\[(FUENTE|SEGUIR)[^\]]*\]?/gi, '').trim(); }
function fuentesDe(t) {
  const m = [...String(t || '').matchAll(/\[FUENTE:\s*([^\]]+)\]/gi)].map(x => x[1]).join(',');
  return [...new Set(m.split(/[,|]/).map(x => x.trim()).filter(Boolean))].join(', ');
}
async function guardar(env, r) {
  if (!env.REGISTRO || !RID_OK.test(r.rid || '')) return;
  const ahora = new Date().toISOString();
  try {
    await env.REGISTRO.prepare(`INSERT INTO registro (rid, sid, fecha, idioma, pais, pagina, tipo, clave, pregunta, respuesta, fuentes, modelo, ms, error, voto, actualizado, exportado)
      VALUES (?1, ?2, ?3, ?4, ?14, ?5, ?6, ?7, ?8, ?9, ?10, ?11, ?12, ?13, NULL, ?3, NULL)
      ON CONFLICT(rid) DO NOTHING`)
      .bind(r.rid, RID_OK.test(r.sid || '') ? r.sid : null, ahora, r.idioma || 'es', String(r.pagina || '').slice(0, 80),
            r.tipo, r.clave ? String(r.clave).slice(0, 40) : null, tachar(r.pregunta).slice(0, 2000), tachar(r.respuesta).slice(0, 8000),
            r.fuentes || null, r.modelo || null, r.ms || null, r.error || null, r.pais || null).run();
  } catch (e) { console.log('registro_error', String(e)); }
}

/* Vuelca a GitHub (repositorio privado) lo nuevo o cambiado desde la última exportación. */
function b64(texto) {
  const bytes = new TextEncoder().encode(texto); let bin = '';
  for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
  return btoa(bin);
}
function desde64(b) { const bin = atob(String(b).replace(/\n/g, '')); return new TextDecoder().decode(Uint8Array.from(bin, c => c.charCodeAt(0))); }
async function exportar(env) {
  if (!env.REGISTRO || !env.GITHUB_TOKEN || !env.GITHUB_REPO) return { ok: false, motivo: 'sin configurar' };
  // retención: 12 meses
  await env.REGISTRO.prepare("DELETE FROM registro WHERE fecha < ?1").bind(new Date(Date.now() - 365 * 86400_000).toISOString()).run();
  const { results } = await env.REGISTRO.prepare(
    "SELECT * FROM registro WHERE exportado IS NULL OR actualizado > exportado ORDER BY fecha LIMIT 2000").all();
  if (!results.length) return { ok: true, filas: 0 };
  const porDia = {};
  for (const r of results) (porDia[r.fecha.slice(0, 10)] ||= []).push(r);
  const api = `https://api.github.com/repos/${env.GITHUB_REPO}/contents/`;
  const cab = { 'Authorization': `Bearer ${env.GITHUB_TOKEN}`, 'Accept': 'application/vnd.github+json', 'User-Agent': 'dentaldata-chat', 'X-GitHub-Api-Version': '2022-11-28' };
  const ahora = new Date().toISOString();
  for (const [dia, filas] of Object.entries(porDia)) {
    const ruta = `${env.GITHUB_DIR || '_registro'}/${dia.slice(0, 4)}/${dia}.jsonl`;
    const previo = await fetch(api + ruta + `?ref=${env.GITHUB_BRANCH || 'main'}`, { headers: cab });
    let sha, contenido = '';
    if (previo.ok) { const j = await previo.json(); sha = j.sha; contenido = desde64(j.content); }
    const nuevas = filas.map(r => JSON.stringify({ ...r, exportado: undefined })).join('\n') + '\n';
    const put = await fetch(api + ruta, { method: 'PUT', headers: { ...cab, 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: `Registro del asistente ${dia} (${filas.length})`, content: b64(contenido + nuevas), sha, branch: env.GITHUB_BRANCH || 'main' }) });
    if (!put.ok) { console.log('github_error', put.status, await put.text()); return { ok: false, motivo: 'GitHub ' + put.status }; }
    const ids = filas.map(r => r.rid);
    for (let i = 0; i < ids.length; i += 50) {
      const lote = ids.slice(i, i + 50);
      await env.REGISTRO.prepare(`UPDATE registro SET exportado = ?1 WHERE rid IN (${lote.map((_, k) => '?' + (k + 2)).join(',')})`).bind(ahora, ...lote).run();
    }
  }
  return { ok: true, filas: results.length };
}

function cors(origin) {
  const ok = ORIGENES.includes(origin) ? origin : ORIGENES[0];
  return { 'Access-Control-Allow-Origin': ok, 'Access-Control-Allow-Methods': 'POST, OPTIONS',
           'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Max-Age': '86400', 'Vary': 'Origin' };
}
function json(obj, status, origin) {
  return new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json; charset=utf-8', ...cors(origin) } });
}

async function cargarKB(pais) {
  const c = KB_CACHE.get(pais);
  if (c && Date.now() - c.t < 3600_000) return c.texto;
  const partes = await Promise.all(kbDe(pais).map(async f => {
    const r = await fetch(KB_BASE + f, { cf: { cacheTtl: 3600, cacheEverything: true } });
    return r.ok ? `\n\n===== ${f} =====\n` + (await r.text()) : '';
  }));
  const texto = partes.join('');
  KB_CACHE.set(pais, { texto, t: Date.now() });
  return texto;
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
    if (url.pathname === '/salud') return json({ ok: true, modelo: env.MODEL || 'claude-haiku-5-5', clave: !!(env.ANTHROPIC_API_KEY || env.DENTAL_DATA) }, 200, origin);
    if ((url.pathname === '/registro' || url.pathname === '/valoracion') && request.method === 'POST') {
      if (!ORIGENES.includes(origin)) return json({ error: 'Origen no permitido' }, 403, origin);
      let c; try { c = await request.json(); } catch { return json({ error: 'Petición no válida' }, 400, origin); }
      if (url.pathname === '/registro') {
        const tipo = ['preparada', 'preparada_por_palabras', 'sin_respuesta'].includes(c.tipo) ? c.tipo : null;
        if (!tipo) return json({ error: 'Tipo no válido' }, 400, origin);
        ctx.waitUntil(guardar(env, { rid: c.rid, sid: c.sid, idioma: IDIOMAS[c.idioma] ? c.idioma : 'es', pais: PAISES[c.pais] ? c.pais : null, pagina: c.pagina,
          tipo, clave: c.clave, pregunta: c.pregunta, respuesta: c.respuesta }));
      } else if (env.REGISTRO && RID_OK.test(c.rid || '') && (c.voto === 1 || c.voto === -1)) {
        ctx.waitUntil(env.REGISTRO.prepare('UPDATE registro SET voto = ?1, actualizado = ?2 WHERE rid = ?3')
          .bind(c.voto, new Date().toISOString(), c.rid).run().catch(e => console.log('voto_error', String(e))));
      }
      return json({ ok: true }, 200, origin);
    }
    if (url.pathname !== '/chat' || request.method !== 'POST') return json({ error: 'No encontrado' }, 404, origin);
    if (!ORIGENES.includes(origin)) return json({ error: 'Origen no permitido' }, 403, origin);
    if (!(env.ANTHROPIC_API_KEY || env.DENTAL_DATA)) return json({ error: 'El asistente aún no está configurado.' }, 500, origin);

    let cuerpo;
    try { cuerpo = await request.json(); } catch { return json({ error: 'Petición no válida' }, 400, origin); }
    const idioma = IDIOMAS[cuerpo.idioma] ? cuerpo.idioma : 'es';
    const pais = PAISES[cuerpo.pais] ? cuerpo.pais : (idioma === 'nl' ? 'nl' : idioma === 'es' ? 'es' : 'eu');
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

    const kb = await cargarKB(pais);
    const reglaIdioma = IDIOMAS[idioma] + ` La página desde la que te escriben es la de ${PAISES[pais]}: usa las cifras, leyes, organismos y ofertas de ese mercado; si preguntan por otro país, responde solo con lo que diga la base sobre él y, si existe, enlaza su página (https://dentaldata.softwareinabox.eu/es/, /nl/, /nl-be/, /fr-be/, /de/, /da/ o /en/).`;
    const instrucciones = `Eres el asistente de la web de Dental Data (dentaldata.softwareinabox.eu), el espacio de datos de salud dental federado de Software in a Box, preparado para el Espacio Europeo de Datos de Salud (EEDS) y desplegado sobre Microsoft Azure. ${reglaIdioma}
Hablas con dentistas, directivos de cadenas dentales, aseguradoras, proveedores de software y partners tecnológicos. Tono profesional, cercano y claro, sin jerga innecesaria. Máximo 5 frases por respuesta; usa **negritas** para lo esencial.
Fundamenta cada respuesta EXCLUSIVAMENTE en la base de conocimiento adjunta. Si algo no está en ella, dilo con honestidad y sugiere escribir a partners@softwareinabox.eu o usar el formulario (#contacto). Nunca inventes cifras, fechas, precios, clientes, socios ni características. No des diagnóstico ni consejo clínico ni asesoramiento jurídico personalizado. No hables en nombre de Microsoft ni afirmes acuerdos con Microsoft que no estén en la base. No pidas ni almacenes datos personales y, si el usuario los escribe, no los repitas. Si preguntan por temas ajenos a Dental Data, salud dental, datos de salud o Software in a Box, indica amablemente que solo puedes hablar de Dental Data. Cuando encaje, invita a contactar: al piloto en España, al programa de partners en Países Bajos, a una alianza institucional en Bélgica, a acuerdos con fabricantes de software y MVZ en Alemania, a proyectos institucionales en Dinamarca y, en el resto, a escribir a partners@softwareinabox.eu.
Al final de tu respuesta añade, cada una en su línea:
[FUENTE: nombre-del-archivo.md] — uno o dos archivos de la base que fundamentan la respuesta. Obligatoria si usaste la base.
[SEGUIR: pregunta uno | pregunta dos] — dos preguntas de seguimiento breves y naturales, en el idioma de la conversación.`;

    const resp = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-api-key': (env.ANTHROPIC_API_KEY || env.DENTAL_DATA), 'anthropic-version': '2023-06-01' },
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

    const inicio = Date.now(), pregunta = limpios[limpios.length - 1].content;
    const enc = new TextEncoder(), dec = new TextDecoder();
    const { readable, writable } = new TransformStream();
    const w = writable.getWriter();
    const emitir = o => w.write(enc.encode('data: ' + JSON.stringify(o) + '\n\n'));
    ctx.waitUntil((async () => {
      const lector = resp.body.getReader(); let buf = '', hubo = false, texto = '', fallo = null;
      try {
        while (true) {
          const { done, value } = await lector.read(); if (done) break;
          buf += dec.decode(value, { stream: true });
          let p;
          while ((p = buf.indexOf('\n')) !== -1) {
            const linea = buf.slice(0, p).trim(); buf = buf.slice(p + 1);
            if (!linea.startsWith('data:')) continue;
            let j; try { j = JSON.parse(linea.slice(5)); } catch { continue; }
            if (j.type === 'content_block_delta' && j.delta && j.delta.text) { hubo = true; texto += j.delta.text; await emitir({ t: j.delta.text }); }
            else if (j.type === 'error') { fallo = 'interrumpida'; await emitir({ error: idioma === 'en' ? 'The assistant was interrupted. Please try again.' : 'El asistente se interrumpió. Inténtelo de nuevo.' }); }
          }
        }
        await emitir(hubo ? { fin: true } : { error: idioma === 'en' ? 'No answer received.' : 'No se recibió respuesta.' });
      } catch (e) {
        fallo = 'conexión perdida';
        await emitir({ error: idioma === 'en' ? 'Connection lost.' : 'Se perdió la conexión.' });
      } finally {
        await w.close();
        await guardar(env, { rid: cuerpo.rid, sid: cuerpo.sid, idioma, pais, pagina: cuerpo.pagina, tipo: 'ia', pregunta,
          respuesta: limpiarRespuesta(texto), fuentes: fuentesDe(texto), modelo: env.MODEL || 'claude-haiku-5-5',
          ms: Date.now() - inicio, error: fallo || (hubo ? null : 'sin respuesta') });
      }
    })());
    return new Response(readable, { headers: { 'Content-Type': 'text/event-stream; charset=utf-8', 'Cache-Control': 'no-cache', ...cors(origin) } });
  },

  /* Cron diario (wrangler.toml → [triggers]): vuelca el registro al repositorio privado. */
  async scheduled(event, env, ctx) {
    ctx.waitUntil(exportar(env).then(r => console.log('exportacion', JSON.stringify(r))));
  }
};
