"""Renderiza presentaciones/<ruta>/dentaldata-pNN.mp4 (1920×1080, 25 fps, H.264 CRF 20) con la locución.
Uso: python3 _build/render_mp4.py p01 [mercado]   (sirve el repositorio en 127.0.0.1:8765)"""
import sys, os, subprocess, threading, http.server, functools
from playwright.sync_api import sync_playwright
AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(os.path.dirname(AQUI))
pid = sys.argv[1]; mk = sys.argv[2] if len(sys.argv) > 2 else ""
ruta = f"presentaciones/{mk + '/' if mk else ''}{pid}"
class Q(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=RAIZ, **k)
    def log_message(self, *a): pass
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 8765), Q); threading.Thread(target=srv.serve_forever, daemon=True).start()
salida = os.path.join(RAIZ, ruta, f"dentaldata-{pid}.mp4"); voz = os.path.join(RAIZ, ruta, f"voz-{pid}.mp3")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto(f"http://127.0.0.1:8765/{ruta}/?render=1"); pg.wait_for_function("window.DD && window.DD.listo"); pg.wait_for_timeout(500)
    dur = pg.evaluate("window.DD.duracion"); n = int(dur * 25)
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", "25", "-i", "-", "-i", voz,
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                           "-t", f"{dur:.2f}", "-movflags", "+faststart", salida], stdin=subprocess.PIPE)
    for i in range(n):
        pg.evaluate(f"window.DD.seek({i/25:.3f})")
        ff.stdin.write(pg.screenshot(type="jpeg", quality=88))
    ff.stdin.close(); ff.wait(); b.close()
srv.shutdown(); print("ok", salida, round(dur, 1), "s", n, "fotogramas")
