/* Dental Data · motor de presentaciones animadas (GSAP).
   Cada presentación declara sus escenas en HTML: <section class="esc" data-nombre="…" data-dur="6">
   Los elementos se animan con data-a="up|down|left|right|pop|fade|type|draw|count|bar|barv|mover|brillo|tachar"
   y data-t="segundos desde el inicio de la escena" (data-d = duración).
   Modos: presentación (por defecto) · ?modo=web (sola y muda, botón «Activar locución») · ?modo=video (con locución)
   · &embed=1 (visor del asistente) · ?render=1 (captura de fotogramas para el MP4). */
const UI = window.DD_UI || {};
(function(){
"use strict";
const $ = (s, r=document) => r.querySelector(s), $$ = (s, r=document) => Array.from(r.querySelectorAll(s));

/* ---------- iconos de línea propios (24×24) */
const I = {
  clinica:'<path d="M3 21h18M5 21V8l7-4 7 4v13"/><path d="M10 21v-5h4v5M12 9v4M10 11h4"/>',
  muela:'<path d="M7 3c-2.5 0-4 2-4 4.5 0 3 1.5 4.5 2 7.5.5 3 1 6 2.5 6s1.8-4 2.5-6c.3-1 .7-1.5 2-1.5s1.7.5 2 1.5c.7 2 1 6 2.5 6S18.5 18 19 15c.5-3 2-4.5 2-7.5C21 5 19.5 3 17 3c-2 0-3 1-5 1S9 3 7 3z"/>',
  expediente:'<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M8 13h8M8 17h5"/>',
  rx:'<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 15c1-3 2.5-5 5-5s4 2 5 5M9 15v-2M12 15v-3M15 15v-2"/>',
  software:'<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4M7 9h5M7 12h8"/>',
  conector:'<path d="M9 2v5M15 2v5M6 7h12v4a6 6 0 0 1-12 0z"/><path d="M12 17v5"/>',
  catalogo:'<path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z"/>',
  candado:'<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4M12 15v2"/>',
  contrato:'<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M8 12h8M8 16c1.5-1.5 2.5 1 4 0s2 0 3 .5"/>',
  escudo:'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
  euro:'<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5A4 4 0 1 0 15.5 15.5M7 11h6M7 13.5h6"/>',
  red:'<circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="18" r="2.5"/><circle cx="19" cy="18" r="2.5"/><path d="M11 7.3 6.3 15.8M13 7.3l4.7 8.5M7.5 18h9"/>',
  grafica:'<path d="M4 20V4M4 20h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>',
  calendario:'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
  personas:'<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
  nube:'<path d="M7 18a5 5 0 0 1-.5-10A6 6 0 0 1 18 9a4.5 4.5 0 0 1-.5 9z"/>',
  pregunta:'<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.7.3-1 .9-1 1.7M12 17h.01"/>',
  ok:'<path d="M5 12.5l4.5 4.5L19 7.5"/>',
  no:'<path d="M6 6l12 12M18 6 6 18"/>',
  fabrica:'<path d="M3 21V10l6 4v-4l6 4V5h5v16z"/><path d="M7 17h2M12 17h2"/>',
  ia:'<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4M10 10h4v4h-4z"/>',
  mano:'<path d="M2 12l4-4 4 2 3-2 3 1 6 4"/><path d="M6 8l-4 4 6 6 2-1 2 2 2-1 2 1 4-5M10 17l2-2M13 18l2-2"/>',
  correo:'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
  telefono:'<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/>',
  globo:'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.5 5.5 3.5 9s-1 6.5-3.5 9c-2.5-2.5-3.5-5.5-3.5-9s1-6.5 3.5-9z"/>',
  aseguradora:'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M12 8v8M8 12h8"/>',
  ley:'<path d="M12 3v18M5 7h14M8 21h8"/><path d="M5 7l-3 6a3 3 0 0 0 6 0zM19 7l-3 6a3 3 0 0 0 6 0z"/>',
  flecha:'<path d="M4 12h15M13 6l6 6-6 6"/>',
  isla:'<circle cx="12" cy="12" r="8" stroke-dasharray="3 3"/><circle cx="12" cy="12" r="3"/>',
  implante:'<path d="M8 3h8l-1 5H9z"/><path d="M10 8h4M9.5 11h5M10 14h4M10.5 17h3M12 20v1"/>',
  puerta:'<path d="M4 21h16M6 21V4h9l3 3v14"/><circle cx="13" cy="13" r=".8"/>',
  reloj:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  buscar:'<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/>',
  receta:'<rect x="3" y="8" width="18" height="8" rx="4" transform="rotate(-35 12 12)"/><path d="M9.5 8.5l5 7"/>',
  estrella:'<path d="M12 3l2.6 5.8 6.4.6-4.8 4.3 1.4 6.3L12 16.8 6.4 20l1.4-6.3L3 9.4l6.4-.6z"/>'
};
function iconos(){
  $$("i[data-i]").forEach(el => {
    const s = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    s.setAttribute("viewBox", "0 0 24 24"); s.setAttribute("aria-hidden", "true");
    s.setAttribute("class", "i " + (el.className || ""));
    s.innerHTML = I[el.dataset.i] || I.pregunta;
    ["a","t","d"].forEach(k => { if(el.dataset[k]) s.dataset[k] = el.dataset[k]; });
    el.replaceWith(s);
  });
}

/* ---------- arranque */
const q = new URLSearchParams(location.search);
const RENDER = q.has("render");
const VOZ = q.get("modo") === "video";
const WEB = !RENDER && (q.get("modo") === "web" || VOZ);
document.body.classList.add(RENDER ? "render" : VOZ ? "video" : WEB ? "web" : "pres");
if(q.get("embed")) document.body.classList.add("embed");
const reducido = !RENDER && matchMedia("(prefers-reduced-motion: reduce)").matches;
if(reducido) document.body.classList.add("reducido");
iconos();

/* escala del escenario */
const stage = $("#stage");
function escala(){ const k = Math.min(innerWidth / 1600, innerHeight / 900); stage.style.transform = `scale(${k})`; }
addEventListener("resize", escala); escala();

/* ---------- construcción de la línea de tiempo */
const ESC = $$(".esc", stage);
const tl = gsap.timeline({paused:true, defaults:{ease:"power3.out"}});
const fmtNum = (n, dec, mil) => { let s = n.toFixed(dec); if(mil){ const [a, b] = s.split("."); s = a.replace(/\B(?=(\d{3})+(?!\d))/g, mil) + (b ? "," + b : ""); } else s = s.replace(".", ","); return s; };

function anima(el, at){
  const a = el.dataset.a, d = parseFloat(el.dataset.d || "0") || null;
  switch(a){
    case "up":    tl.fromTo(el, {y:40, opacity:0}, {y:0, opacity:1, duration:d||.6}, at); break;
    case "down":  tl.fromTo(el, {y:-40, opacity:0}, {y:0, opacity:1, duration:d||.6}, at); break;
    case "left":  tl.fromTo(el, {x:-80, opacity:0}, {x:0, opacity:1, duration:d||.7, ease:"expo.out"}, at); break;
    case "right": tl.fromTo(el, {x:80, opacity:0}, {x:0, opacity:1, duration:d||.7, ease:"expo.out"}, at); break;
    case "pop":   tl.fromTo(el, {scale:.55, opacity:0}, {scale:1, opacity:1, duration:d||.55, ease:"back.out(2.2)"}, at); break;
    case "fade":  tl.fromTo(el, {opacity:0}, {opacity:1, duration:d||.6, ease:"none"}, at); break;
    case "out":   tl.to(el, {opacity:0, duration:d||.5}, at); break;
    case "dim":   tl.to(el, {opacity:.28, duration:d||.5}, at); break;
    case "type": {
      const full = el.textContent; el.dataset.full = full; const o = {n:0};
      tl.set(el, {opacity:1}, at);
      tl.fromTo(o, {n:0}, {n:full.length, duration:d||Math.min(1.6, full.length * .035), ease:"none",
        onUpdate:() => { el.textContent = full.slice(0, Math.round(o.n)); }}, at);
      break; }
    case "draw": {
      const L = el.getTotalLength ? el.getTotalLength() : 1000;
      tl.fromTo(el, {strokeDasharray:L, strokeDashoffset:L, opacity:1}, {strokeDashoffset:0, duration:d||.8, ease:"power2.inOut"}, at);
      break; }
    case "count": {
      const to = parseFloat(el.dataset.to), dec = parseInt(el.dataset.dec || "0"), mil = el.dataset.mil || "", o = {v:0};
      const pre = el.dataset.pre || "", suf = el.dataset.suf || "";
      tl.fromTo(el, {opacity:0}, {opacity:1, duration:.3}, at);
      tl.fromTo(o, {v:0}, {v:to, duration:d||1.4, ease:"power2.out",
        onUpdate:() => { el.innerHTML = pre + fmtNum(o.v, dec, mil) + suf; }}, at);
      break; }
    case "bar":   tl.fromTo(el, {scaleX:0}, {scaleX:1, duration:d||.9, ease:"power2.inOut"}, at); break;
    case "barv":  tl.fromTo(el, {scaleY:0}, {scaleY:1, duration:d||.9, ease:"power2.out"}, at); break;
    case "mover": {
      const dx = parseFloat(el.dataset.dx || 0), dy = parseFloat(el.dataset.dy || 0);
      tl.fromTo(el, {x:0, y:0, opacity:0}, {opacity:1, duration:.15, ease:"none"}, at);
      tl.to(el, {x:dx, y:dy, duration:d||1, ease:"power1.inOut"}, at);
      if(el.dataset.fin !== "queda") tl.to(el, {opacity:0, duration:.2}, at + (d||1) - .1);
      break; }
    case "brillo": {
      const b = el.querySelector(".borde") || el;
      tl.to(b, {opacity:1, duration:.2}, at).to(b, {opacity:el.dataset.queda ? 1 : 0, duration:.5}, at + .6);
      break; }
    case "tachar": tl.fromTo(el, {scaleX:0, opacity:1}, {scaleX:1, duration:d||.45, ease:"power2.out"}, at); break;
  }
}
function estadoInicial(el){
  const a = el.dataset.a;
  if(["up","down","left","right","pop","fade","count","mover"].includes(a)) gsap.set(el, {opacity:0});
  if(a === "type") gsap.set(el, {opacity:0});
  if(a === "draw" && el.getTotalLength){ const L = el.getTotalLength(); gsap.set(el, {strokeDasharray:L, strokeDashoffset:L, opacity:0}); }
  if(a === "bar") gsap.set(el, {scaleX:0});
  if(a === "barv") gsap.set(el, {scaleY:0});
  if(a === "tachar") gsap.set(el, {scaleX:0});
}

const NOMBRES = [];
let t = 0;
ESC.forEach((s, i) => {
  const dur = parseFloat(s.dataset.dur || "6");
  NOMBRES.push(s.dataset.nombre || `${UI.escena || "Escena"} ${i + 1}`);
  tl.addLabel("s" + (i + 1), t);
  if(i > 0){ const prev = ESC[i - 1]; tl.to(prev, {opacity:0, duration:.45, ease:"power2.in"}, t).set(prev, {visibility:"hidden"}, t + .45); }
  tl.set(s, {visibility:"visible"}, t).to(s, {opacity:1, duration:.45, ease:"none"}, t + (i ? .3 : 0));
  // capas fijas: marca y pregunta desde la escena 2; pie en la última
  if(i === 1){ tl.to("#marca", {opacity:1, duration:.5}, t + .2).fromTo("#chip", {opacity:0, y:-12}, {opacity:1, y:0, duration:.5}, t + .35); }
  if(i === ESC.length - 1){ tl.to("#chip", {opacity:0, duration:.4}, t).to("#pie", {opacity:1, duration:.6}, t + .8); }
  $$("[data-a]", s).forEach(el => { estadoInicial(el); anima(el, t + .3 + parseFloat(el.dataset.t || "0")); });
  t += dur;
});
tl.addLabel("fin", t);
tl.to({}, {duration:.01}, t);
const ETIQ = NOMBRES.map((_, i) => tl.labels["s" + (i + 1)]).concat(t);

/* ---------- audio de locución */
const audio = $("#voz");
let vozActiva = false;
function vozPlay(){ if(!audio) return; vozActiva = true; audio.currentTime = 0; audio.play().catch(() => { vozActiva = false; }); tl.seek(0).play(); }
if(audio) audio.addEventListener("ended", () => { vozActiva = false; });
gsap.ticker.add(() => { if(vozActiva && audio && !audio.paused){ const d = audio.currentTime - tl.time(); if(Math.abs(d) > .12) tl.time(Math.min(audio.currentTime, t)); } });

/* ---------- controles */
const escBox = $("#escenas");
NOMBRES.forEach((n, i) => { const b = document.createElement("button"); b.innerHTML = `<b>${i + 1}</b><span>${n}</span><i></i>`; b.title = `${i + 1} · ${n}`; b.onclick = () => ir(i); escBox.appendChild(b); });
const bts = $$("button", escBox);
const actual = () => { const x = tl.time(); let k = 0; ETIQ.forEach((l, i) => { if(i < NOMBRES.length && x >= l - .001) k = i; }); return k; };
let tramo = null;
function pintar(){
  const x = tl.time(), k = actual();
  bts.forEach((b, i) => { b.classList.toggle("on", i === k); const a = ETIQ[i], z = ETIQ[i + 1]; b.querySelector("i").style.width = (x >= z ? 100 : x <= a ? 0 : (x - a) / (z - a) * 100) + "%"; });
  const play = tl.isActive() || (tramo && tramo.isActive()) || vozActiva;
  $("#pp").innerHTML = play ? '<path d="M7 5h4v14H7zM13 5h4v14h-4z"/>' : '<path d="M8 5v14l11-7z"/>';
  document.body.classList.toggle("al-inicio", x < .01);
  document.body.classList.toggle("al-final", x >= t - .02);
}
gsap.ticker.add(pintar);
function pararTramo(){ if(tramo){ tramo.kill(); tramo = null; } }
function ir(i){
  pararTramo(); i = Math.max(0, Math.min(NOMBRES.length - 1, i));
  if(vozActiva && audio){ audio.currentTime = ETIQ[i]; tl.seek(ETIQ[i]); return; }
  tl.pause();
  if(reducido){ tl.seek(ETIQ[i + 1] - .02, false); return; }
  tl.seek(ETIQ[i], false);
  if(WEB){ tl.play(); return; }
  tramo = tl.tweenFromTo(ETIQ[i], ETIQ[i + 1] - .01, {ease:"none"});
}
function alternar(){
  if(vozActiva && audio){ if(audio.paused){ audio.play(); } else { audio.pause(); tl.pause(); } return; }
  if(tramo && tramo.isActive()){ tramo.pause(); return; }
  if(tramo && tramo.paused() && tramo.progress() < 1){ tramo.resume(); return; }
  if(tl.isActive()){ tl.pause(); return; }
  if(WEB){ if(tl.time() >= t - .02) tl.seek(0); tl.play(); return; }
  const k = actual();
  if(tl.time() >= ETIQ[k + 1] - .05) ir(k + 1); else { pararTramo(); tramo = tl.tweenFromTo(tl.time(), ETIQ[k + 1] - .01, {ease:"none"}); }
}
const siguiente = () => { const k = actual(); if(tl.time() < .01 && !tramo) return ir(0); ir(k + 1); };
const anterior = () => ir(actual() - 1);
$("#pp").parentElement.onclick = alternar;
$("#ant").onclick = anterior; $("#sig").onclick = siguiente;
$("#pc").onclick = () => document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen();
addEventListener("keydown", e => {
  if(e.key === "ArrowRight" || e.key === " " || e.key === "PageDown"){ e.preventDefault(); WEB ? alternar() : siguiente(); }
  else if(e.key === "ArrowLeft" || e.key === "PageUp"){ e.preventDefault(); anterior(); }
  else if(/^[1-9]$/.test(e.key)) ir(+e.key - 1);
  else if(e.key === "f" || e.key === "F") $("#pc").click();
  else if(e.key === "h" || e.key === "H") document.body.classList.toggle("ui-off");
});
if(!WEB && !RENDER) stage.addEventListener("click", siguiente);

/* botón de locución (web) y arranque del vídeo */
const vb = $("#voz-btn");
/* ?modo=web&sonido=1: intenta arrancar con locución; el botón alterna «Quitar audio» / «Activar audio» */
const SONIDO = WEB && !VOZ && q.get("sonido") === "1";
function rotular(){ if(!vb) return; const on = vozActiva && audio && !audio.muted && !audio.paused;
  vb.textContent = SONIDO ? (on ? (UI.quitar || "🔇 Quitar audio") : (UI.activar || "🔊 Activar audio")) : (UI.locucion || "🔊 Activar locución"); vb.setAttribute("aria-pressed", on); }
function conSonido(){ if(!audio) return Promise.reject();
  vozActiva = true; audio.muted = false; audio.currentTime = 0;
  return audio.play().then(() => { tl.seek(0).play(); rotular(); }).catch(e => { vozActiva = false; rotular(); throw e; }); }
if(vb){ vb.hidden = !(WEB && !VOZ && audio);
  vb.onclick = e => { e.stopPropagation();
    if(!SONIDO){ vb.hidden = true; vozPlay(); return; }
    if(vozActiva && !audio.paused){ audio.muted = !audio.muted; rotular(); } else conSonido().catch(() => {}); };
  if(audio){ audio.addEventListener("play", rotular); audio.addEventListener("pause", rotular); audio.addEventListener("ended", rotular); }
  rotular(); }
/* la página puede pedir el sonido tras un clic del usuario (p. ej. el enlace de la cabecera) */
addEventListener("message", e => { if(e.source === window.parent && e.data && e.data.dd === "sonido" && WEB && !VOZ) conSonido().catch(() => tl.play(0)); });
const ini = $("#inicio span");
if(VOZ){ ini.textContent = UI.ver || "▶ Ver con locución (sonido activado)"; ini.onclick = () => vozPlay(); }

/* modo web: arranca al hacerse visible */
if(WEB && !VOZ){
  if(reducido) tl.seek(t - .02, false);
  else { const arrancar = () => SONIDO ? conSonido().catch(() => tl.play(0)) : tl.play(0);
    if("IntersectionObserver" in window){ let hecho = false; new IntersectionObserver(es => { es.forEach(e => { if(e.isIntersecting && !hecho){ hecho = true; arrancar(); } }); }, {threshold:.4}).observe(document.body); }
    else arrancar(); }
}
if(reducido && !WEB) tl.seek(ETIQ[1] - .02, false);

/* dentro de la web (iframe), como en ARGOS:
   ?modo=video&auto=1 arranca con locución si el navegador lo permite (si no, queda el botón «Ver con locución»);
   al terminar avisa a la página con {dd:"fin"} y Esc pide cerrar la ventana con {dd:"cerrar"} */
const EN_WEB = window.parent !== window;
const avisar = m => { try { window.parent.postMessage({dd: m}, "*"); } catch(e){} };
if(VOZ && audio && q.get("auto") === "1" && !reducido){
  vozActiva = true; audio.currentTime = 0;
  audio.play().then(() => tl.seek(0).play()).catch(() => { vozActiva = false; });
}
if(EN_WEB && WEB){
  let armado = false, avisado = false;
  gsap.ticker.add(() => { const x = tl.time();
    if(x > .3 && x < t - 1){ armado = true; avisado = false; }
    if(armado && !avisado && x >= t - .05){ avisado = true; armado = false; avisar("fin"); } });
  if(!q.get("embed")) addEventListener("keydown", e => { if(e.key === "Escape" && !document.fullscreenElement) avisar("cerrar"); });
}

/* API para el render del MP4 y para pruebas */
window.DD = {tl, duracion:t, escenas:NOMBRES, inicios:ETIQ, seek:x => { tl.pause(); tl.seek(x, false); }};
if(document.fonts) document.fonts.ready.then(() => { window.DD.listo = true; }); else window.DD.listo = true;
})();
