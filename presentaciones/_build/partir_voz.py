"""Parte la locución conjunta de un mercado en piezas.
Uso: python3 _build/partir_voz.py <mercado> <audio_conjunto> <whisper_words.json>
Escribe presentaciones/<mk>/pNN/voz-pNN.mp3 (3 s de silencio + pieza, -16 LUFS) y _build/palabras-<mk>.json"""
import json, os, sys, subprocess
AQUI = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
from mercado_tiempos import alinear
mk, audio, wj = sys.argv[1:4]
d = json.load(open(os.path.join(AQUI, "mercados", f"{mk}.json")))
ws = json.load(open(wj))
pids = sorted(d["piezas"])
guion, idx = [], {}
for p in pids:
    w = d["piezas"][p]["loc"].split(); idx[p] = (len(guion), len(guion) + len(w)); guion += w
t = alinear(guion, ws)
# fin de cada palabra: siguiente whisper end ~ usamos inicio de la palabra siguiente
dur = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",audio]))
cortes = {}
for i, p in enumerate(pids):
    a, b = idx[p]
    ini = t[a]
    if i > 0:
        prev_last = t[a - 1]
        # fin real de la última palabra anterior según whisper
        ends = [w[1] for w in ws if w[0] <= prev_last + 0.01]
        fin_prev = max(ends) if ends else prev_last
        ini = (fin_prev + t[a]) / 2 if t[a] > fin_prev else t[a] - 0.15
    cortes[p] = 0.0 if i == 0 else max(0.0, ini)
pal = {}
for i, p in enumerate(pids):
    s = cortes[p]; e = cortes[pids[i + 1]] if i + 1 < len(pids) else dur
    pal[p] = [[round(w[0] - s, 3), round(w[1] - s, 3), w[2]] for w in ws if s <= w[0] < e]
    out = os.path.join(RAIZ, mk, p); os.makedirs(out, exist_ok=True)
    subprocess.run(["ffmpeg","-v","error","-y","-f","lavfi","-t","3","-i","anullsrc=r=44100:cl=mono",
        "-ss",f"{s:.3f}","-to",f"{e:.3f}","-i",audio,
        "-filter_complex","[1:a]aresample=44100,aformat=channel_layouts=mono,afade=t=out:st=%.3f:d=0.25[v];[0:a][v]concat=n=2:v=0:a=1,loudnorm=I=-16:TP=-1.5:LRA=11[o]" % max(0, e - s - 0.25),
        "-map","[o]","-ar","44100","-b:a","128k",os.path.join(out, f"voz-{p}.mp3")], check=True)
    print(p, f"{s:7.2f} → {e:7.2f}  ({e-s:5.1f}s)", " ".join(w[2] for w in pal[p][:4]))
json.dump(pal, open(os.path.join(AQUI, f"palabras-{mk}.json"), "w"), ensure_ascii=False)
