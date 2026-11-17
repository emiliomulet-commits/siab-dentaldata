/* Dental Data · presentaciones animadas en la web.
   - Videoteca: <div id="dd-videoteca"></div> (tarjetas filtrables por público)
   - Botones: cualquier elemento con data-pres="pNN" abre el reproductor
   - Asistente: window.DDV.chat(burbuja, idPregunta) añade «Ver animación» si hay una presentación para esa pregunta
   El progreso («Vista») se guarda solo en este navegador (localStorage), sin cookies. */
(function(){
"use strict";
var BASE = "/presentaciones/";
var PUB = [["todos","Todas"],["cadenas","Cadenas"],["aseguradoras","Aseguradoras"],["clinicas","Clínicas"],["industria","Industria e IA"],["partners","Partners y TI"]];
var RUTAS = {cadenas:["p01","p02","p04","p03","p10"],aseguradoras:["p01","p02","p05","p03","p10"],clinicas:["p01","p03","p07","p10"],
  industria:["p02","p06","p09","p10"],partners:["p02","p08","p10"],todos:["p01","p02","p03","p04","p05","p06","p07","p08","p09","p10"]};
var KB = {datos:"p03",seguridad:"p03",publicidad:"p03",cadena:"p04",aseguradora:"p05",ia:"p06",ehds:"p07",independiente:"p07",
  tecnologia:"p11",azure:"p11",arquitectura:"p11",experiencia:"p08",piloto:"p10",coste:"p10",paises:"p10"};
var CTA = {p04:"¿Hablamos del piloto para tu cadena?",p05:"¿Hablamos del piloto para tu red?",p08:"¿Eres partner de Azure? Hablemos",
  p09:"¿Hablamos de evidencia para tu producto?",p10:"Únete al piloto",p11:"¿Montamos tu nodo en Azure? Hablemos"};
var PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4v16l13-8z"/></svg>';
var V = [], byId = {}, ruta = RUTAS.todos, filtro = "todos";
var vistos = {}; try{ vistos = JSON.parse(localStorage.getItem("dd-vistos") || "{}"); }catch(_){}
function guardar(){ try{ localStorage.setItem("dd-vistos", JSON.stringify(vistos)); }catch(_){} }
function mmss(s){ s = Math.round(s); return Math.floor(s/60) + ":" + ("0" + s%60).slice(-2); }
function seg(s){ return Math.round(s) + " s"; }
function esc(t){ return String(t).replace(/[&<>"]/g, function(c){ return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]; }); }

/* ---------- reproductor */
var modal, marco, side, last = null, actual = null;
function crearModal(){
  modal = document.createElement("div"); modal.className = "dd-modal"; modal.setAttribute("role","dialog"); modal.setAttribute("aria-modal","true"); modal.setAttribute("aria-labelledby","dd-mt");
  modal.innerHTML = '<div class="dd-box" style="position:relative"><div class="dd-fr"><iframe title="Presentación animada con locución" allow="autoplay; fullscreen" allowfullscreen></iframe></div>' +
    '<div class="dd-side"><div class="k" id="dd-mk"></div><h2 id="dd-mt"></h2><p class="dd-ayuda">Presentación animada con locución. Usa la barra inferior para pausar o saltar entre escenas.</p>' +
    '<button type="button" class="dd-next"></button><div class="dd-acc"></div></div>' +
    '<details class="dd-tr"><summary>Transcripción y fuentes</summary><p class="tx"></p><p class="fu"></p></details>' +
    '<button type="button" class="dd-x" aria-label="Cerrar">×</button></div>';
  document.body.appendChild(modal);
  marco = modal.querySelector("iframe"); side = modal.querySelector(".dd-side");
  modal.querySelector(".dd-x").onclick = cerrar;
  modal.addEventListener("click", function(e){ if(e.target === modal) cerrar(); });
  document.addEventListener("keydown", function(e){ if(e.key === "Escape" && modal.classList.contains("open")) cerrar(); });
  /* la presentación (iframe) avisa al terminar o al pulsar Esc */
  window.addEventListener("message", function(e){
    if(!e.data || !actual || !modal.classList.contains("open") || e.source !== marco.contentWindow) return;
    if(e.data.dd === "cerrar") return cerrar();
    if(e.data.dd === "fin"){ if(!vistos[actual.id]){ vistos[actual.id] = 1; guardar(); marcar(); }
      var n = siguiente(); if(n){ var b = modal.querySelector(".dd-next"); b.classList.add("on"); b.focus(); } }
  });
}
function siguiente(){ if(!actual) return null; var i = ruta.indexOf(actual.id); return i > -1 && i + 1 < ruta.length ? byId[ruta[i+1]] : null; }
function abrir(id, desde){
  var v = byId[id]; if(!v) return; if(!modal) crearModal();
  last = desde || document.activeElement; actual = v;
  if(ruta.indexOf(id) < 0) ruta = RUTAS.todos;
  marco.src = v.interactiva + "?modo=video&auto=1";
  modal.querySelector("#dd-mk").textContent = v.id.toUpperCase() + " · " + seg(v.duracion);
  modal.querySelector("#dd-mt").textContent = v.titulo;
  var n = siguiente(), nb = modal.querySelector(".dd-next"); nb.classList.remove("on");
  if(n){ nb.innerHTML = PLAY.replace("<svg", '<svg style="width:14px;height:14px;fill:#C9A227"') + "<span>Siguiente: <b>" + esc(n.chip) + "</b></span>"; nb.onclick = function(){ abrir(n.id); }; nb.classList.add("on"); }
  var cta = CTA[id] || "¿Hablamos?";
  modal.querySelector(".dd-acc").innerHTML = '<a class="cta" href="#contacto" data-cerrar>' + esc(cta) + '</a>' +
    '<a href="' + v.interactiva + '?modo=video" target="_blank" rel="noopener">Abrir a pantalla completa ↗</a>' +
    '<a href="' + v.mp4 + '" download>Descargar el vídeo (MP4)</a>' +
    (n ? "" : '<a href="#videos" data-cerrar>Ver todas las presentaciones</a>');
  modal.querySelectorAll("[data-cerrar]").forEach(function(a){ a.addEventListener("click", cerrar); });
  modal.querySelector(".dd-tr .tx").textContent = v.transcripcion;
  modal.querySelector(".dd-tr .fu").textContent = v.fuentes;
  modal.classList.add("open"); document.documentElement.style.overflow = "hidden";
  modal.querySelector(".dd-x").focus();
  if(window.history && history.replaceState) history.replaceState(null, "", "#video-" + id);
}
function cerrar(){
  if(!modal) return; marco.src = "about:blank"; modal.classList.remove("open"); document.documentElement.style.overflow = "";
  if(location.hash.indexOf("#video-") === 0 && history.replaceState) history.replaceState(null, "", location.pathname + location.search);
  if(last && last.focus) last.focus();
}

/* ---------- videoteca */
function marcar(){ document.querySelectorAll(".dd-card").forEach(function(c){ c.classList.toggle("visto", !!vistos[c.dataset.pres]); }); pintarRuta(); }
function pintarRuta(){
  var r = document.querySelector(".dd-ruta"); if(!r) return;
  var lista = RUTAS[filtro], hechos = lista.filter(function(i){ return vistos[i]; }).length, pend = lista.filter(function(i){ return !vistos[i]; })[0];
  var nombre = PUB.filter(function(p){ return p[0] === filtro; })[0][1].toLowerCase();
  r.innerHTML = (filtro === "todos" ? "<span><b>" + hechos + " de " + lista.length + "</b> vistas</span>" :
     "<span>Recorrido para <b>" + esc(nombre) + "</b>: " + lista.length + " presentaciones, unos " + Math.round(lista.reduce(function(s, i){ return s + byId[i].duracion; }, 0) / 60) + " minutos · <b>" + hechos + " de " + lista.length + "</b> vistas</span>") +
    (pend ? '<button type="button">' + (hechos ? "Continuar" : "Empezar") + " · " + esc(pend.toUpperCase()) + "</button>" : "<span>✓ Recorrido completo</span>");
  var b = r.querySelector("button"); if(b) b.onclick = function(){ ruta = lista; abrir(pend, b); };
}
function videoteca(box){
  var tabs = document.createElement("div"); tabs.className = "dd-tabs"; tabs.setAttribute("role","group"); tabs.setAttribute("aria-label","Filtrar por perfil");
  PUB.forEach(function(p){ var b = document.createElement("button"); b.type = "button"; b.setAttribute("aria-pressed", p[0] === "todos"); b.dataset.f = p[0];
    b.innerHTML = esc(p[1]) + '<span class="cnt">' + RUTAS[p[0]].length + "</span>";
    b.onclick = function(){ filtro = p[0]; ruta = RUTAS[filtro]; tabs.querySelectorAll("button").forEach(function(x){ x.setAttribute("aria-pressed", x === b); });
      grid.querySelectorAll(".dd-card").forEach(function(c){ var i = RUTAS[filtro].indexOf(c.dataset.pres); c.hidden = i < 0; c.style.order = i; }); pintarRuta(); };
    tabs.appendChild(b); });
  var grid = document.createElement("div"); grid.className = "dd-grid";
  V.forEach(function(v){
    if(RUTAS.todos.indexOf(v.id) < 0) return; // P11 va destacada fuera de la videoteca
    var c = document.createElement("button"); c.type = "button"; c.className = "dd-card"; c.dataset.pres = v.id;
    c.setAttribute("aria-label", v.titulo + " (" + seg(v.duracion) + ")");
    c.innerHTML = '<span class="ph" style="background-image:url(' + v.poster + ')"><span class="pb">' + PLAY + '</span><span class="nu">' + v.id.toUpperCase() + '</span><span class="du">' + seg(v.duracion) + '</span><span class="vi">✓ Vista</span></span>' +
      '<span class="tx"><span class="h3">' + esc(v.chip) + '</span><span class="pu">' + esc(v.publico.filter(function(x){ return x !== "todos"; }).map(function(x){ return PUB.filter(function(p){ return p[0] === x; })[0][1]; }).join(" · ") || "Para todos") + "</span></span>";
    c.onclick = function(){ ruta = RUTAS[filtro]; abrir(v.id, c); };
    grid.appendChild(c); });
  var r = document.createElement("div"); r.className = "dd-ruta";
  box.appendChild(tabs); box.appendChild(grid); box.appendChild(r);
  marcar();
}

/* ---------- botones y asistente */
function boton(id, claro){
  var v = byId[id] || {duracion:0}, b = document.createElement("button"); b.type = "button"; b.className = "dd-vbtn" + (claro ? " claro" : ""); b.dataset.pres = id;
  b.innerHTML = '<span class="pl">' + PLAY + "</span><span>Ver animación <small>" + (v.duracion ? seg(v.duracion) : "") + "</small></span>"; return b;
}
document.addEventListener("click", function(e){
  var b = e.target.closest && e.target.closest("[data-pres]"); if(!b || b.classList.contains("dd-card")) return;
  e.preventDefault(); ruta = RUTAS.todos; abrir(b.dataset.pres, b);
});
/* cabecera: «sobre Microsoft Azure» lleva a la presentación de la arquitectura en Azure (P11) */
(function(){
  var sub = document.querySelector(".brand .sub"), sec = document.getElementById("arquitectura-azure");
  if(!sub || !sec) return;
  sub.classList.add("dd-azure-link"); sub.setAttribute("role", "link"); sub.setAttribute("tabindex", "0");
  sub.title = "Ver qué montamos en Microsoft Azure";
  function ir(e){ e.preventDefault(); e.stopPropagation();
    sec.scrollIntoView({behavior: "smooth", block: "start"});
    if(history.replaceState) history.replaceState(null, "", "#arquitectura-azure"); }
  sub.addEventListener("click", ir);
  sub.addEventListener("keydown", function(e){ if(e.key === "Enter" || e.key === " ") ir(e); });
})();
window.DDV = {
  open: abrir,
  chat: function(burbuja, kid){ var id = KB[kid]; if(!id) return; var b = boton(id, true), ft = burbuja.querySelector(".ft"); if(ft) burbuja.insertBefore(b, ft); else burbuja.appendChild(b); }
};

fetch(BASE + "videos.json").then(function(r){ return r.json(); }).then(function(d){
  V = d; d.forEach(function(v){ byId[v.id] = v; });
  document.querySelectorAll("[data-pres] small[data-dur]").forEach(function(s){ var v = byId[s.closest("[data-pres]").dataset.pres]; if(v) s.textContent = seg(v.duracion); });
  var box = document.getElementById("dd-videoteca"); if(box) videoteca(box);
  var m = location.hash.match(/^#video-(p\d\d)$/); if(m && byId[m[1]]) abrir(m[1]);
}).catch(function(){});
})();
