#!/usr/bin/env python3
"""B453 (Ethogram E1) — covers of the child: b1, torsion, the virtual-fibering degree question.

Gates: vol(cover) = k * vol(child); H1(child) = Z/5.
Open: b1 + torsion of the Z/5 cyclic cover; low-index scan (deg <= 6) for minimal b1 > 0.
Controls: 5_2(5,1) child and 6_1(5,1), same pipeline.
"""
import snappy

def survey(name, degmax=6):
    M = snappy.Manifold(name)
    M.simplify()
    vol = float(M.volume())
    print(f"== {name}: vol={vol:.7f}  H1={M.homology()}", flush=True)
    out = []
    for k in range(2, degmax + 1):
        try:
            covs = M.covers(k)
        except Exception as e:
            print(f"   deg {k}: covers() failed: {e}", flush=True)
            continue
        for i, C in enumerate(covs):
            H = C.homology()
            b1 = H.betti_number()
            try:
                cv = float(C.volume())
            except Exception:
                cv = float('nan')
            ratio = cv / vol if vol else float('nan')
            out.append((k, i, str(H), b1, cv, ratio))
            print(f"   deg {k} cover #{i}: H1={H}  b1={b1}  vol={cv:.6f} (={ratio:.3f}x)", flush=True)
    pos = [o for o in out if o[3] > 0]
    if pos:
        mind = min(o[0] for o in pos)
        print(f"   MINIMAL POSITIVE-b1 DEGREE <= {degmax}: {mind}", flush=True)
    else:
        print(f"   NO positive-b1 cover found at degrees <= {degmax} (UNDECIDED-AT-DEGREE-{degmax})", flush=True)
    return out

for nm in ["4_1(5,1)", "5_2(5,1)", "6_1(5,1)"]:
    survey(nm)
    print()
