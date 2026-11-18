"""Tiempos de escena y subtítulos de una versión por mercado.
Uso: python3 _build/mercado_tiempos.py <mercado> palabras-<mercado>.json
palabras: {pid: [[ini, fin, palabra], …]} de Whisper sobre la locución SIN el silencio inicial.
Alinea el guion (texto correcto) con Whisper, calcula los inicios de escena con las anclas del guion
y escribe _build/tiempos-<mercado>.json y presentaciones/<mercado>/pNN/subtitulos-<lang>.vtt"""
import json, os, re, sys, unicodedata, difflib
AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
from construir import conf_mercado
INTRO, COLA, ADELANTO = 3.0, 4.2, 0.3
def norm(w): return re.sub(r"[^a-z0-9ñæøå]", "", unicodedata.normalize("NFKD", w.lower()).encode("ascii", "ignore").decode())
def alinear(guion, ws):
    gn = [norm(w) for w in guion]
    wn = [norm(w[2]) for w in ws]
    t = [None] * len(guion)
    sm = difflib.SequenceMatcher(a=gn, b=wn, autojunk=False)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): t[a + k] = ws[b + k][0]
    known = [i for i, x in enumerate(t) if x is not None]
    for i in range(len(t)):
        if t[i] is None:
            prev = max([k for k in known if k < i], default=None); nxt = min([k for k in known if k > i], default=None)
            if prev is None: t[i] = t[nxt] if nxt is not None else 0.0
            elif nxt is None: t[i] = t[prev] + .35 * (i - prev)
            else: t[i] = t[prev] + (t[nxt] - t[prev]) * (i - prev) / (nxt - prev)
    return t
def ts(x):
    h, r = divmod(x, 3600); m, s = divmod(r, 60); return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"
def vtt(guion, t, fin):
    frases, cur = [], []
    for i, w in enumerate(guion):
        cur.append(i)
        if w[-1] in ".?!" or i == len(guion) - 1: frases.append(cur); cur = []
    def partir(idx):
        txt = " ".join(guion[j] for j in idx)
        if len(txt) <= 84: return [idx]
        n = -(-len(txt) // 84); obj = len(txt) / n; mejor, acc = None, 0
        for k, j in enumerate(idx[:-1]):
            acc += len(guion[j]) + 1
            pen = abs(acc - obj) - (12 if guion[j][-1] in ",;:" else 0)
            if mejor is None or pen < mejor[0]: mejor = (pen, k)
        return partir(idx[:mejor[1] + 1]) + partir(idx[mejor[1] + 1:])
    cues = [c for f in frases for c in partir(f)]
    out = ["WEBVTT", ""]
    for n, c in enumerate(cues):
        a = INTRO + t[c[0]]; b = (INTRO + t[cues[n + 1][0]] - .05) if n + 1 < len(cues) else fin
        txt = " ".join(guion[j] for j in c)
        if len(txt) > 42:
            mid = len(txt) // 2; cut = txt.rfind(" ", 0, mid + 8); txt = txt[:cut] + "\n" + txt[cut + 1:]
        out += [f"{ts(a)} --> {ts(b)}", txt, ""]
    return "\n".join(out)
if __name__ == "__main__":
    mk = sys.argv[1]; pal = json.load(open(sys.argv[2]))
    c = conf_mercado(mk); lang = c["lang"].split("-")[0]
    tp = os.path.join(AQUI, f"tiempos-{mk}.json")
    res = json.load(open(tp)) if os.path.exists(tp) else {}
    for pid, ws in sorted(pal.items()):
        p = c["piezas"][pid]; guion = p["loc"].split(); t = alinear(guion, ws)
        gn = [norm(w) for w in guion]
        fin_voz = ws[-1][1]; inicios = [0.0]; k = 0
        for a in p["anclas"]:
            if a == "FIN": inicios.append(INTRO + fin_voz + .4); continue
            toks = [norm(x) for x in a.split()]
            j = k
            while j < len(gn) and gn[j:j + len(toks)] != toks: j += 1
            if j >= len(gn): raise SystemExit(f"{mk} {pid}: no encuentro el ancla «{a}» en el guion")
            inicios.append(max(INTRO, INTRO + t[j] - ADELANTO)); k = j + len(toks)
        inicios[1] = INTRO
        total = INTRO + fin_voz + COLA
        durs = [round(b - a, 2) for a, b in zip(inicios, inicios[1:] + [max(total, inicios[-1] + 5.0)])]
        res[pid] = {"dur": durs, "inicios": inicios, "palabras": [(round(INTRO + x, 2), w) for x, w in zip(t, gn) if w]}
        os.makedirs(os.path.join(RAIZ, mk, pid), exist_ok=True)
        open(os.path.join(RAIZ, mk, pid, f"subtitulos-{lang}.vtt"), "w").write(vtt(guion, t, INTRO + fin_voz + .8))
        print(mk, pid, durs, "total", round(sum(durs), 1))
    json.dump(res, open(tp, "w"))
