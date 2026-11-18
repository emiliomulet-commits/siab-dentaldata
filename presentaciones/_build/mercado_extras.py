"""Pósters (captura de la escena 2) y catálogo videos.json de una versión por mercado.
Uso: python3 _build/mercado_extras.py <mercado>"""
import json, os, re, sys, asyncio
AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
from construir import conf_mercado, cargar
import i18n
PUB = {"p01":["todos"],"p02":["todos"],"p03":["clinicas","cadenas"],"p04":["cadenas"],"p05":["aseguradoras"],"p06":["clinicas","industria"],
       "p07":["todos","clinicas"],"p08":["partners"],"p09":["industria"],"p10":["cadenas","aseguradoras","partners"],"p11":["partners","industria"]}
async def posters(mk, pids, T):
    from playwright.async_api import async_playwright
    import http.server, threading, functools
    raiz_web = os.path.dirname(RAIZ)
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=raiz_web)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 8765), h); threading.Thread(target=srv.serve_forever, daemon=True).start()
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1920, "height": 1080})
        for pid in pids:
            await pg.goto(f"http://127.0.0.1:8765/presentaciones/{mk}/{pid}/?modo=web")
            d = T.get(pid, {"inicios": [0, 3, 9]})
            espera = (d["inicios"][2] - .3) if len(d["inicios"]) > 2 else 6
            await pg.wait_for_timeout(int(espera * 1000) + 800)
            await pg.screenshot(path=f"/tmp/poster-{mk}-{pid}.png")
            os.system(f'ffmpeg -v error -y -i /tmp/poster-{mk}-{pid}.png -vf scale=960:-1 -q:v 4 "{RAIZ}/{mk}/{pid}/poster.jpg"')
        await b.close()
    srv.shutdown()
if __name__ == "__main__":
    mk = sys.argv[1]; c = conf_mercado(mk); lang = c["lang"].split("-")[0]
    T = json.load(open(os.path.join(AQUI, f"tiempos-{mk}.json")))
    pids = sorted(T)
    if "--sin-poster" not in sys.argv: asyncio.run(posters(mk, pids, T))
    cat = []
    for pid in pids:
        m = cargar(pid); d = i18n.aplicar(m, c["piezas"][pid]["seg"]); t = T[pid]
        esc = [x for x in re.findall(r'data-nombre="([^"]+)"', "\n".join(d["ESCENAS"]))]
        cat.append({"id": pid, "titulo": d["TITULO"], "chip": d["CHIP"], "publico": PUB[pid], "duracion": round(sum(t["dur"]), 1),
                    "capitulos": [{"t": round(x, 2), "nombre": n} for x, n in zip(t["inicios"], esc)],
                    "mp4": None, "poster": f"/presentaciones/{mk}/{pid}/poster.jpg",
                    "vtt": f"/presentaciones/{mk}/{pid}/subtitulos-{lang}.vtt", "interactiva": f"/presentaciones/{mk}/{pid}/",
                    "transcripcion": c["piezas"][pid]["loc"], "fuentes": re.sub(r"<[^>]+>", "", d["FUENTES"])})
    json.dump(cat, open(os.path.join(RAIZ, mk, "videos.json"), "w"), ensure_ascii=False, indent=1)
    print("catálogo", mk, len(cat))
