"""Genera para cada pieza: poster.jpg, subtitulos-es.vtt y ../videos.json (catálogo para la web).
Los subtítulos usan el texto del guion (ortografía correcta) alineado con los tiempos de Whisper."""
import json, os, re, sys, subprocess, unicodedata, difflib, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(AQUI, "piezas"))
INTRO = 3.0
T = json.load(open(os.path.join(AQUI, "tiempos.json")))
LOC = json.load(open(os.path.join(AQUI, "locuciones.json")))
PUB = {"p01":["todos"],"p02":["todos"],"p03":["clinicas","cadenas"],"p04":["cadenas"],"p05":["aseguradoras"],"p06":["clinicas","industria"],
       "p07":["todos","clinicas"],"p08":["partners"],"p09":["industria"],"p10":["cadenas","aseguradoras","partners"],"p11":["partners","industria"]}
def norm(w): return re.sub(r"[^a-z0-9ñ]", "", unicodedata.normalize("NFKD", w.lower()).encode("ascii","ignore").decode())
def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60); return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"
cat = []
for pid in sorted(T):
    spec = importlib.util.spec_from_file_location(pid, os.path.join(AQUI, "piezas", pid + ".py")); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    d = T[pid]; ws = d["palabras"]  # [(t_abs, norm)]
    # alinear el guion con Whisper
    guion = LOC[pid].split(); gn = [norm(w) for w in guion]
    sm = difflib.SequenceMatcher(a=gn, b=[w for _, w in ws], autojunk=False)
    t = [None]*len(guion)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): t[a+k] = ws[b+k][0]
    # interpolar huecos
    known = [i for i, x in enumerate(t) if x is not None]
    for i in range(len(t)):
        if t[i] is None:
            prev = max([k for k in known if k < i], default=None); nxt = min([k for k in known if k > i], default=None)
            if prev is None: t[i] = t[nxt]
            elif nxt is None: t[i] = t[prev] + .35*(i-prev)
            else: t[i] = t[prev] + (t[nxt]-t[prev])*(i-prev)/(nxt-prev)
    fin = INTRO + max(w[0] for w in ws) + .8
    # cues: cortar en puntuación o a ~42 caracteres por línea (máx. 2 líneas)
    # cues: una frase por subtítulo; las frases largas se parten en trozos equilibrados (≤ 84 caracteres)
    frases, cur = [], []
    for i, w in enumerate(guion):
        cur.append(i)
        if w[-1] in ".?!" or i == len(guion)-1: frases.append(cur); cur = []
    def partir(idx):
        txt = " ".join(guion[j] for j in idx)
        if len(txt) <= 84: return [idx]
        n = -(-len(txt) // 84); objetivo = len(txt) / n; mejor, acc = None, 0
        for k, j in enumerate(idx[:-1]):
            acc += len(guion[j]) + 1
            pen = abs(acc - objetivo) - (12 if guion[j][-1] in ",;:" else 0)
            if mejor is None or pen < mejor[0]: mejor = (pen, k)
        return partir(idx[:mejor[1]+1]) + partir(idx[mejor[1]+1:])
    cues = [c for f in frases for c in partir(f)]
    vtt = ["WEBVTT", ""]
    for n, c in enumerate(cues):
        a = t[c[0]]; b = (t[cues[n+1][0]] - .05) if n+1 < len(cues) else fin
        txt = " ".join(guion[j] for j in c)
        if len(txt) > 42:  # dos líneas
            mid = len(txt)//2; cut = txt.rfind(" ", 0, mid+8); txt = txt[:cut] + "\n" + txt[cut+1:]
        vtt += [f"{ts(a)} --> {ts(b)}", txt, ""]
    open(os.path.join(RAIZ, pid, "subtitulos-es.vtt"), "w").write("\n".join(vtt))
    # póster: final de la escena 2 (contenido ya montado)
    mp4 = os.path.join(RAIZ, pid, f"dentaldata-{pid}.mp4"); seg = d["inicios"][2] - .3 if len(d["inicios"]) > 2 else 6
    subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{seg:.2f}","-i",mp4,"-frames:v","1","-vf","scale=960:-1","-q:v","4",os.path.join(RAIZ, pid, "poster.jpg")], check=True)
    esc = [n for n in re.findall(r'data-nombre="([^"]+)"', "\n".join(m.ESCENAS))]
    cat.append({"id": pid, "titulo": m.TITULO, "chip": m.CHIP, "publico": PUB[pid], "duracion": round(sum(d["dur"]), 1),
                "capitulos": [{"t": round(x, 2), "nombre": n} for x, n in zip(d["inicios"], esc)],
                "mp4": f"/presentaciones/{pid}/dentaldata-{pid}.mp4", "poster": f"/presentaciones/{pid}/poster.jpg",
                "vtt": f"/presentaciones/{pid}/subtitulos-es.vtt", "interactiva": f"/presentaciones/{pid}/",
                "transcripcion": LOC[pid], "fuentes": re.sub(r"<[^>]+>", "", m.FUENTES)})
    print(pid, len(cues), "subtítulos")
json.dump(cat, open(os.path.join(RAIZ, "videos.json"), "w"), ensure_ascii=False, indent=1)
