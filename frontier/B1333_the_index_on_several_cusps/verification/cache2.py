"""Re-cache the covers the first normalisation missed, using the multi-conjugate recogniser.
Every rep is checked against the relators before it is cached."""
import sys, warnings, json, os; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from fractions import Fraction as Fr
from recogmc2 import exact_rho2
from fi_lib import wev
from q12 import eye, scal
mI=scal((Fr(-1),Fr(0),Fr(0),Fr(0)),eye(2))
CACHE='/tmp/sweep/covcache.json'
db=json.load(open(CACHE))
M0=snappy.Manifold('m004')
todo=[t for t,v in db.items() if not v.get('ok')]
print("re-attempting:",todo)
for tag in todo:
    deg,k=int(tag.split('_')[0][1:]),int(tag.split('_')[1])
    C=M0.covers(deg)[k]
    got=exact_rho2(C)
    if got is None: print(tag,"still unrecognised"); continue
    Mh,G,gens,rels,per,rho,how=got
    st=[wev(r,rho,2) for r in rels]
    if not all(R==eye(2) or R==mI for R in st):
        print(tag,"** recognised rep FAILS the relators -- not cached **"); continue
    proj=any(R==mI for R in st)
    db[tag]={"ok":True,"cusps":C.num_cusps(),"gens":gens,"rels":rels,
             "per":[list(x) for x in per],"proj":proj,"how":how,
             "rho":{g:[[[str(e) for e in rho[g][i][j]] for j in range(2)] for i in range(2)] for g in gens}}
    print(f"{tag}: cusps={C.num_cusps()} gens={len(gens)} lift={'-I' if proj else '+I'} via {how}  RELATORS OK")
    json.dump(db,open(CACHE,'w'))
json.dump(db,open(CACHE,'w'))
print("cached ok:",sum(1 for v in db.values() if v.get('ok')),"of",len(db))
