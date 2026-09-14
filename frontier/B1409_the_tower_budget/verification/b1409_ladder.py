"""B1409 addendum -- the RANK ladder: does dim H^1 = k(n-1) continue at n = 4?

sl_4 under the principal SL(2) is Sym^2 + Sym^4 + Sym^6 (3+5+7 = 15).
Predict a1 = k(n-1) = 3k: 15 at the 5-cusped ceiling, 3 at m004.
Covers selected BY PROPERTY, exact over Q(zeta_12), mp.dps pinned explicitly.
"""
import os, sys, json, warnings, time; warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)),
                                "B1333_the_index_on_several_cusps", "verification"))
import mpmath as mp
import snappy
from recogmc import exact_rho
from fi_lib import sym, blockdiag
from mcexact import analyse_exact
DPS = 60

def dims(C, germs):
    mp.mp.dps = DPS
    got = exact_rho(C)
    if got is None: return None
    _, _, gens, rels, per, rho = got
    V = {g: blockdiag([sym(rho[g], m) for m in germs]) for g in gens}
    d = sum(m + 1 for m in germs)
    A = analyse_exact(gens, rels, per, V, d)
    return A["a0"], A["a1"], A["r1"], A["n"], d

M0 = snappy.Manifold("m004")
targets = [("m004", M0, 1)]
for i, C in enumerate(M0.covers(10)):
    if C.num_cusps() == 5:
        try: amph = bool(C.symmetry_group().is_amphicheiral())
        except Exception: continue
        if not amph:
            targets.append((f"5-cusped chiral [{i}]", C, 5)); break

LADDER = [("n=2  sl_2 = Sym^2",            (2,)),
          ("n=3  sl_3 = Sym^2+Sym^4",      (2, 4)),
          ("n=4  sl_4 = Sym^2+Sym^4+Sym^6", (2, 4, 6))]
out = {}
for nm, C, k in targets:
    print(f"\n=== {nm}  (k = {k}) ===")
    for label, germs in LADDER:
        t = time.time(); r = dims(C, germs)
        if r is None:
            print(f"    {label:32s} PSLQ HALT"); continue
        a0, a1, r1, n, d = r
        n_rank = len(germs) + 1
        pred = k * (n_rank - 1)
        print(f"    {label:32s} d={d:2d}  a0={a0}  dim H^1 = {a1:2d}   "
              f"predict k(n-1) = {pred:2d}  {'OK' if a1 == pred else 'DEVIATION'}   "
              f"n=a1-r1={n}   [{time.time()-t:.1f}s]")
        out[f"{nm}|{label}"] = {"k": k, "n": n_rank, "d": d, "a0": a0, "a1": a1,
                                "pred": pred, "match": a1 == pred, "interior": n}
json.dump(out, open(os.path.join(HERE, "b1409_ladder.json"), "w"), indent=1)
allok = all(v["match"] for v in out.values())
allbdy = all(v["interior"] == 0 for v in out.values())
print(f"\n  k(n-1) holds at n = 2,3,4 on both manifolds: {allok}")
print(f"  zero interior moduli at every rank: {allbdy}")
