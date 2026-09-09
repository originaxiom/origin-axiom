#!/usr/bin/env python3
"""B1241 -- fc R51's two residual numbers, recomputed from main's own data (B1235 chirality_112.json).

(1) the ALL-REGULAR subfamily A of the 112 (every tetrahedron the regular ideal shape omega = e^{i pi/3}):
    fc R51 says |A| = 77, amphichiral 34 / chiral 43 by the symmetry group.  Independent of fc's list: the
    shapes are recomputed here in snappy at 1e-9 and the amphicheiral flags are B1235's (main).
(2) the metallic once-punctured-torus bundles b++R^mL^m, m = 1..6 (fc R43/R51): all amphicheiral, symmetry
    order 8, CS = 0 -- recomputed with the ORIENTATION-AWARE test only (never is_isometric_to(mirror), E-class
    vacuity B1235).
"""
import json, os, sys, cmath
import snappy
ROOT = os.environ.get("OA_ROOT") or os.getcwd()
rows = json.load(open(os.path.join(ROOT, "frontier/B1235_two_seat_harvest/verification/chirality_112.json")))
assert len(rows) == 112
OMEGA = cmath.exp(1j*cmath.pi/3)
def all_regular(name, tol=1e-9):
    M = snappy.Manifold(name)
    sh = M.tetrahedra_shapes("rect")
    # a regular ideal tetrahedron has shape omega in every edge parameter (z, 1/(1-z), 1-1/z all equal omega)
    return all(abs(complex(z) - OMEGA) < tol for z in sh), len(sh)
A = []; nonreg = []
for r in rows:
    reg, n = all_regular(r["name"])
    (A if reg else nonreg).append((r["name"], r["amphicheiral"], n))
amph = sum(1 for _, a, _ in A if a is True); chi = sum(1 for _, a, _ in A if a is False)
print(f"all-regular subfamily |A| = {len(A)} of 112; amphichiral {amph}, chiral {chi}  (fc R51: 77; 34/43)")
print(f"non-regular members: {len(nonreg)} (amphichiral {sum(1 for _,a,_ in nonreg if a)}, chiral {sum(1 for _,a,_ in nonreg if a is False)})")
ok1 = (len(A), amph, chi) == (77, 34, 43)
# (2) metallic bundles
met = []
for m in range(1, 7):
    M = snappy.Manifold("b++" + "R"*m + "L"*m)
    G = M.symmetry_group()
    cs = float(M.chern_simons())
    met.append({"m": m, "name": M.name(), "volume": float(M.volume()), "amphicheiral": bool(G.is_amphicheiral()), "order": int(G.order()), "cs": cs, "h1": str(M.homology())})
    print(f"  m={m}: {M.name():>10s} vol={float(M.volume()):.6f} amphicheiral={G.is_amphicheiral()} order={G.order()} CS={cs:+.3e} H1={M.homology()}")
ok2 = all(x["amphicheiral"] and x["order"] == 8 and abs(x["cs"]) < 1e-9 for x in met)
# m=1 must be m004 itself (the figure-eight): volume 2.02988
ok3 = abs(met[0]["volume"] - 2.029883212819307) < 1e-9
print("metallic m=1..6 all amphicheiral, order 8, CS=0:", ok2, "; m=1 is the figure-eight volume:", ok3)
json.dump({"all_regular": {"size": len(A), "amphichiral": amph, "chiral": chi, "members": [n for n,_,_ in A]},
           "non_regular": [n for n,_,_ in nonreg], "metallic_bundles": met, "fc_r51_claims_hold": ok1 and ok2 and ok3},
          open(__file__.replace(".py", ".json"), "w"), indent=1)
print("R51 residuals:", "REPRODUCE" if (ok1 and ok2 and ok3) else "DIFFER")
