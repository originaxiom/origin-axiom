"""B399 A3 -- the singles constant's det-class split (same mechanism as the seam's 1/12?)."""
import json, os, sys
from fractions import Fraction as Fr
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

W1 = build_theta_W(1)
o1, p1 = matrix_order(W1)
ID = [[E.ONE if i == j else E.ZERO for j in range(15)] for i in range(15)]
C0 = {j: par_trace(p1[j], ID) for j in range(o1)}     # tr(Par W1^j) = C[j, 0]

def g1pow(j):
    g = [[1,0],[0,1]]
    for _ in range(j):
        g = [[(g[0][0]*2+g[0][1]*1)%15,(g[0][0]*1+g[0][1]*1)%15],
             [(g[1][0]*2+g[1][1]*1)%15,(g[1][0]*1+g[1][1]*1)%15]]
    return g
def cls_of(j):
    g = g1pow(j)
    d = ((-g[0][0]-1)*(-g[1][1]-1) - g[0][1]*g[1][0]) % 15
    return gcd(d, 15)

def hp(t): return SC.solve_H(SC.H_avg(t))

# the support cell a=1 (value 1/4); class partials:
res = {}
for a in (1, 6):     # support cell a=1 and a second support cell a=6
    parts = {}
    for K in (1, 3, 5, 15):
        t = E.ZERO
        for j in range(o1):
            if cls_of(j) != K: continue
            t = E.add(t, E.mul(E.zeta((-3*j*a) % 60), C0[j]))
        parts[str(K)] = [str(x) for x in hp(E.scal(Fr(1, o1), t))]
    res[f"a{a}"] = parts
    tot = [str(x) for x in hp(E.scal(Fr(1, o1),
          __import__("functools").reduce(lambda u, v: E.add(u, v),
          [E.mul(E.zeta((-3*j*a) % 60), C0[j]) for j in range(o1)])))]
    res[f"a{a}_total"] = tot
    print(f"a={a}: total {tot}; class partials:")
    for K, v in parts.items(): print(f"   class {K}: {v}")
# class counts along the l=0 column
counts = {}
for j in range(o1): counts[cls_of(j)] = counts.get(cls_of(j), 0) + 1
res["class_counts_l0"] = {str(k): v for k, v in sorted(counts.items())}
print("class counts along l=0:", res["class_counts_l0"])
json.dump(res, open(os.path.join(HERE, "a3_normalizer.json"), "w"), indent=1)
print("DONE")
