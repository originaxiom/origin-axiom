"""B385 next layer -- per-pair (j,l)-grid det-class counts (the word-map data).

Needs ord(W_m) at level 15 per seed (exact engine, quick) + pure gamma arithmetic."""
import json, os, sys
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
from step0_exact_matrices import build_theta_W, matrix_order

BRIGHT = [(1,2),(2,3),(2,4),(3,4),(1,7),(3,7),(2,7)]
DARK   = [(1,3),(1,4),(3,5),(1,5),(4,5)]
seeds = sorted({m for p in BRIGHT+DARK for m in p})
ords = {}
for m in seeds:
    o, _ = matrix_order(build_theta_W(m), cap=200)
    ords[m] = o
print("ord(W_m):", ords)

def A(m): return [[(1+m*m) % 15, m % 15], [m % 15, 1]]
def mm(a, b): return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0]) % 15, (a[0][0]*b[0][1]+a[0][1]*b[1][1]) % 15],
                      [(a[1][0]*b[0][0]+a[1][1]*b[1][0]) % 15, (a[1][0]*b[0][1]+a[1][1]*b[1][1]) % 15]]

res = {}
for (m1, m2) in BRIGHT + DARK:
    o1, o2 = ords[m1], ords[m2]
    g1, g2 = A(m1), A(m2)
    G1 = [[[1,0],[0,1]]]
    for _ in range(o1-1): G1.append(mm(G1[-1], g1))
    G2 = [[[1,0],[0,1]]]
    for _ in range(o2-1): G2.append(mm(G2[-1], g2))
    cls = {}
    for j in range(o1):
        for l in range(o2):
            gp = mm(G1[j], G2[l])
            d = ((-gp[0][0]-1)*(-gp[1][1]-1) - gp[0][1]*gp[1][0]) % 15
            c = gcd(d, 15)
            cls[c] = cls.get(c, 0) + 1
    tot = o1*o2
    frac = {str(k): f"{v}/{tot}" for k, v in sorted(cls.items())}
    res[f"{m1},{m2}"] = dict(status=("bright" if (m1,m2) in BRIGHT else "dark"),
                             ords=[o1,o2], counts={str(k): v for k,v in sorted(cls.items())},
                             fracs=frac)
    print(f"{m1},{m2} {'B' if (m1,m2) in BRIGHT else 'D'} ords={o1}x{o2}: {frac}")

# separation scan on normalized class fractions
from fractions import Fraction as Fr
def fvec(r):
    tot = r["ords"][0]*r["ords"][1]
    return tuple((c, Fr(r["counts"].get(c, 0), tot)) for c in ("1","3","5","15"))
bv = {fvec(res[f"{a},{b}"]) for a,b in BRIGHT}
dv = {fvec(res[f"{a},{b}"]) for a,b in DARK}
sep = not (bv & dv)
print("class-fraction vector separates bright/dark:", sep)
json.dump(dict(res=res, separates=sep), open(os.path.join(HERE, "class_counts.json"), "w"), indent=1)
print("DONE")
