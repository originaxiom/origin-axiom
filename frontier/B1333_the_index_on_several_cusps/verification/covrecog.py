"""Can the 54 chiral multi-cusped covers of m004 be recognised exactly over Q(zeta_12)?"""
import sys,warnings; sys.path.insert(0,'/tmp/sweep'); warnings.filterwarnings("ignore")
import snappy
from recogmc import exact_rho
from q12 import *
from fractions import Fraction as Fr

M=snappy.Manifold('m004')
mI=scal((Fr(-1),Fr(0),Fr(0),Fr(0)),eye(2))
ok=0; fail=0; rows=[]
for deg in range(2,11):
    for k,C in enumerate(M.covers(deg)):
        if C.num_cusps()<2: continue
        try:
            if C.symmetry_group().is_amphicheiral(): continue
        except Exception: continue
        tag=f"cover_d{deg}_{k}"
        try: got=exact_rho(C)
        except Exception as e: got=None
        if got is None:
            fail+=1; rows.append((tag,deg,C.num_cusps(),None,None)); continue
        Mh,G,gens,rels,per,rho=got
        st=[]
        for r in rels:
            R=eye(2)
            for ch in r: R=mm(R, rho[ch.lower()] if ch.islower() else minv(rho[ch.lower()]))
            st.append('I' if R==eye(2) else ('-I' if R==mI else 'BAD'))
        ok+=1; rows.append((tag,deg,C.num_cusps(),len(gens),set(st)))
        print(f"  {tag}: cusps={C.num_cusps()} gens={len(gens)} rels->{set(st)}", flush=True)
    print(f"deg {deg} done: recognised {ok}, unrecognised {fail}", flush=True)
print(f"\nRECOGNISED {ok} / {ok+fail} chiral multi-cusped covers")
bad=[r for r in rows if r[4] and 'BAD' in r[4]]
print(f"relators not +-I: {len(bad)}")
