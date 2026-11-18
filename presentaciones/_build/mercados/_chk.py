import sys,json,re,unicodedata
sys.path.insert(0,'.');sys.path.insert(0,'piezas');import i18n
from construir import cargar
def n(s): return " ".join(re.sub(r"[^a-z0-9ñæøå ]"," ",unicodedata.normalize("NFKD",s.lower()).encode("ascii","ignore").decode()).split())
for mk in sys.argv[1:]:
  d=json.load(open(f'mercados/{mk}.json'))['piezas']
  for p in sorted(d):
    s=i18n.extraer(cargar(p)); L=" "+n(d[p]['loc'])+" "
    bad=[d[p]['seg'][i] for i,(k,v) in enumerate(s) if '@data-w' in k and " "+n(d[p]['seg'][i])+" " not in L]
    if bad: print(mk,p,bad)
