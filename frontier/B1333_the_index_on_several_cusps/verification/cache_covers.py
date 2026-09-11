"""Recognise the chiral multi-cusped covers once and cache them; PSLQ is the per-cover cost
and does not need repeating for every prime or germ."""
import sys, warnings, json, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from fractions import Fraction as Fr
from recogmc import exact_rho
from fi_lib import wev
from q12 import eye, scal
mI=scal((Fr(-1),Fr(0),Fr(0),Fr(0)),eye(2))
CACHE='/tmp/sweep/covcache.json'
db=json.load(open(CACHE)) if os.path.exists(CACHE) else {}
M0=snappy.Manifold('m004')
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for deg in range(lo,hi):
    for k,C in enumerate(M0.covers(deg)):
        if C.num_cusps()<2: continue
        try:
            if C.symmetry_group().is_amphicheiral(): continue
        except Exception: continue
        tag=f"d{deg}_{k}"
        if tag in db: continue
        got=exact_rho(C)
        if got is None:
            db[tag]={"ok":False}; print(tag,"unrecognised",flush=True); json.dump(db,open(CACHE,'w')); continue
        Mh,G,gens,rels,per,rho=got
        proj=any(wev(r,rho,2)==mI for r in rels)
        db[tag]={"ok":True,"cusps":C.num_cusps(),"gens":gens,"rels":rels,
                 "per":[list(x) for x in per],"proj":proj,
                 "rho":{g:[[[str(e) for e in rho[g][i][j]] for j in range(2)] for i in range(2)] for g in gens}}
        print(f"{tag}: cusps={C.num_cusps()} gens={len(gens)} lift={'-I' if proj else '+I'}",flush=True)
        json.dump(db,open(CACHE,'w'))
print("cached ok:",sum(1 for v in db.values() if v.get('ok')),"of",len(db))
