"""Calcula la duración de cada escena a partir de la locución (marcas de tiempo por palabra de Whisper).
Entrada: palabras.json · Salida: _build/tiempos.json  {pid: [dur_escena1, …]}
La locución se publica con INTRO s de silencio al principio (escena de apertura)."""
import json, sys, unicodedata, re, os
INTRO, COLA, ADELANTO = 3.0, 4.2, 0.3
ANCLAS = {
 "p01": ["los datos dentales", "no por falta", "en españa", "cada clinica guarda", "los datos existen"],
 "p02": ["en un espacio", "el conector publica", "cuando alguien", "por la red", "el dato se queda"],
 "p03": ["salen los datos", "cada uso", "si una solicitud", "la clinica decide", "FIN"],
 "p04": ["una cadena", "<4 no hace falta", "la direccion", "ademas", "conecta tus"],
 "p05": ["una aseguradora", "<2 le da datos", "la red ademas", "con limites", "datos coherentes de toda"],
 "p06": ["entrenar", "<2 invierte", "los calculos", "el primer modelo", "y se prepara", "el algoritmo va"],
 "p07": ["el espacio europeo", "entre", "la mayoria", "en espana", "quien llegue"],
 "p08": ["sigue", "dentro de cada", "en las fronteras", "asi cualquier", "y no partimos", "FIN"],
 "p09": ["para la industria", "<1 les ofrece", "para los proveedores", "las reglas", "evidencia real"],
 "p10": ["buscamos", "el propio caso", "<4 consolidamos", "tambien queremos", "hablamos"],
}
def norm(w): return re.sub(r"[^a-z0-9ñ]", "", unicodedata.normalize("NFKD", w.lower()).encode("ascii","ignore").decode())
pal = json.load(open(sys.argv[1]))
res = {}
for pid, anclas in ANCLAS.items():
    ws = [(s, e, norm(t)) for s, e, t in pal[pid]]; ws = [w for w in ws if w[2]]
    fin_voz = ws[-1][1]; inicios = [0.0]; k = 0
    for a in anclas:
        if a == "FIN": inicios.append(INTRO + fin_voz + .4); continue
        atras = 0
        if a.startswith("<"): atras, a = int(a[1]), a[3:]
        toks = [norm(t) for t in a.split()]
        while k < len(ws) and [w[2] for w in ws[k:k+len(toks)]] != toks: k += 1
        if k >= len(ws): raise SystemExit(f"{pid}: no encuentro «{a}»")
        inicios.append(max(INTRO, INTRO + ws[k - atras][0] - ADELANTO)); k += len(toks)
    total = INTRO + fin_voz + COLA
    inicios[1] = INTRO  # la primera escena de contenido arranca con la voz
    durs = [round(b - a, 2) for a, b in zip(inicios, inicios[1:] + [max(total, inicios[-1] + 5.0)])]
    res[pid] = {"dur": durs, "inicios": inicios, "palabras": [(round(INTRO + s, 2), w) for s, e, w in ws]}
    print(pid, durs, "total", round(sum(durs), 1))
json.dump(res, open(os.path.join(os.path.dirname(__file__), "tiempos.json"), "w"))
