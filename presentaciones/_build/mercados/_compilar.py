"""Convierte mercados/<mk>.py (listas legibles) en mercados/<mk>.json y comprueba el número de textos de cada pieza."""
import sys, os, json, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__)); B = os.path.dirname(AQUI)
sys.path.insert(0, B); sys.path.insert(0, os.path.join(B, "piezas"))
import i18n
from construir import cargar
def compilar(mk):
    spec = importlib.util.spec_from_file_location("m_" + mk.replace("-", "_"), os.path.join(AQUI, mk + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    out = {"lang": m.LANG, "base": getattr(m, "BASE", None), "ui": getattr(m, "UI", {}), "piezas": {}}
    err = []
    for pid, v in m.PIEZAS.items():
        seg, loc, anc = v
        n = len(i18n.extraer(cargar(pid)))
        nes = len([s for s in cargar(pid).ESCENAS])
        if len(seg) != n: err.append(f"{pid}: {len(seg)} textos, se esperaban {n}")
        if len(anc) != nes - 1: err.append(f"{pid}: {len(anc)} anclas, se esperaban {nes-1}")
        low = " ".join(loc.lower().split())
        for a in anc:
            if a != "FIN" and a.lower() not in low: err.append(f"{pid}: ancla «{a}» no está en la locución")
        out["piezas"][pid] = {"seg": seg, "loc": " ".join(loc.split()), "anclas": anc}
    if err: raise SystemExit("\n".join(err))
    json.dump(out, open(os.path.join(AQUI, mk + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("ok", mk, len(out["piezas"]), "piezas,", sum(len(p["loc"]) for p in out["piezas"].values()), "caracteres de locución")
if __name__ == "__main__":
    for mk in sys.argv[1:]: compilar(mk)
