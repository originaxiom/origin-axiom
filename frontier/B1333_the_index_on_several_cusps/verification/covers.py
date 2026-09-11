"""The trigger's targets: m004's MULTI-CUSPED CHIRAL covers to degree 10.
Chirality via symmetry_group().is_amphicheiral() -- the orientation-AWARE test
(is_isometric_to(mirror) is orientation-blind; that error is on the record)."""
import warnings,sys; warnings.filterwarnings("ignore")
import snappy, json
M=snappy.Manifold('m004')
rows=[]
for deg in range(2,11):
    try: covs=M.covers(deg)
    except Exception as e: print(f"deg {deg}: {e}"); continue
    for C in covs:
        nc=C.num_cusps()
        if nc<2: continue
        try: amph=C.symmetry_group().is_amphicheiral()
        except Exception: amph=None
        G=C.fundamental_group()
        rows.append(dict(deg=deg,cusps=nc,amphicheiral=amph,
                         gens=len(G.generators()),rels=len(G.relators()),
                         h1=str(C.homology()),vol=float(C.volume())))
    print(f"deg {deg}: cumulative multi-cusped {len(rows)}", flush=True)
chiral=[r for r in rows if r['amphicheiral'] is False]
print(f"\nMULTI-CUSPED covers to degree 10: {len(rows)}")
print(f"of which CHIRAL: {len(chiral)}")
from collections import Counter
print("chiral by (degree,cusps):",dict(sorted(Counter((r['deg'],r['cusps']) for r in chiral).items())))
print("chiral by generator count:",dict(sorted(Counter(r['gens'] for r in chiral).items())))
json.dump(rows,open('covers.json','w'),indent=1)
