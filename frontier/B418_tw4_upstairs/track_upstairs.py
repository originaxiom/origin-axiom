"""B418 TW4 -- track the object UPSTAIRS in Q(zeta60), before Pi_H. The B411 test."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

W1 = build_theta_W(1); W2 = build_theta_W(2)
o1, p1 = matrix_order(W1); o2, p2 = matrix_order(W2)
C = {(j,l): par_trace(p1[j], p2[l]) for j in range(o1) for l in range(o2)}
# RAW t-table (no H-average): t_raw(a,b) in Q(zeta60)
def traw(a,b):
    t = E.ZERO
    for j in range(o1):
        za = E.zeta((-3*j*a) % 60)
        for l in range(o2):
            t = E.add(t, E.mul(E.mul(za, E.zeta((-5*l*b) % 60)), C[(j,l)]))
    return E.scal(Fr(1, o1*o2), t)
T = {(a,b): traw(a,b) for a in range(o1) for b in range(o2)}
support = [(a,b) for (a,b),v in T.items() if v != E.ZERO]
print("raw support cells:", len(support))

UNITS = [c for c in range(1,60) if __import__("math").gcd(c,60)==1]  # 16 Galois elements
# THE B411 TEST: does the mirror t(a,-b) = sigma_c(t(a,b)) hold CELL-LOCALLY upstairs?
mirror_hits = []
for c in UNITS:
    if all(T[(a,(-b)%o2)] == SC.sigma(T[(a,b)], c) for (a,b) in support):
        mirror_hits.append(c)
print("UPSTAIRS mirror: Galois elements c with t(a,-b)=sigma_c(t(a,b)) cell-wise:", mirror_hits)
# class action sigma_cl upstairs: is there c with t(...) = sigma_cl-analog? test the a-flip / b-flip full-field
# also test the FULL isotypic decomposition: how many of the 16 isotypic components of a cell are nonzero?
def isotypic_support(v):
    # a cell lives in Q(zeta60) (deg 16); its 'H-part' is 4-dim. Count nonzero coords in the
    # 16-dim power basis as a coarse proxy for full-field richness.
    return sum(1 for x in v if x != 0)
rich = {f"{a},{b}": isotypic_support(T[(a,b)]) for (a,b) in support[:6]}
print("raw cells' power-basis richness (of 16):", rich)
res = dict(support=len(support), mirror_upstairs_galois=mirror_hits,
           sample_richness=rich)
res["verdict"] = ("mirror IS cell-local upstairs (c=%s)"%mirror_hits if mirror_hits
                  else "mirror is NOT cell-local even upstairs -- emergence is intrinsic")
print("VERDICT:", res["verdict"])
# bar check
res["bar"] = dict(any_exact_SM_match=False,
    reason="upstairs symmetry (if any) is a subgroup of Gal(Q(zeta60)/Q)=(Z/60)*, order 16 -- an abelian cyclotomic Galois group, not an SM gauge structure")
json.dump(res, open("track_upstairs.json","w"), indent=1)
print("DONE")
