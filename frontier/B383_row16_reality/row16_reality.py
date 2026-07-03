"""B383 -- the row-16 reality theorem (T1/T2/T3 per PREREGISTRATION.md)."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

W1 = build_theta_W(1); W2 = build_theta_W(2)
o1,pow1 = matrix_order(W1); o2,pow2 = matrix_order(W2)
C = [[par_trace(pow1[j], pow2[l]) for l in range(o2)] for j in range(o1)]

# tau3 on the full field: the Galois elements of Gal(Q(zeta60)) that flip sqrt(-3) and fix
# sqrt5: acting c on zeta60 with the H-restriction (x,y,z,s)->(x,y,-z,-s). On H the flip is
# determined; on the full field pick the coset -- the ANTI part relative to H needs only the
# H-average: anti(t) := H_avg(t) - tau3(H_avg(t)) halves. H_avg(C) in H exactly (values may
# not be in H cell-wise! -- so work with the H-average of the DFT line, not cell-wise).
# Safer, registered-equivalent formulation of T1: for each b, the row-16 DFT value
#   t(16,b) = (1/240) sum_{j,l} zeta20^{-16j} zeta12^{-lb} C[j][l]
# projected to H must have z = s = 0. (The banked support {0,4,8} plus ALL other b checked.)
def tval(a,b):
    t = E.ZERO
    for j in range(o1):
        za = E.zeta((-3*j*a) % 60)
        for l in range(o2):
            t = E.add(t, E.mul(E.mul(za, E.zeta((-5*l*b)%60)), C[j][l]))
    return E.scal(Fr(1,o1*o2), t)

res = {}
ok = True
for b in range(12):
    sol = SC.solve_H(SC.H_avg(tval(16,b)))
    res[str(b)] = [str(x) for x in sol]
    if sol[2] != 0 or sol[3] != 0: ok = False
print("T1 row 16, all b: z=s=0 everywhere:", ok)
for b,v in res.items(): print("  b=%s:"%b, v)

# T3 contrast: row 4 must be BRIGHT somewhere (z or s nonzero)
bright4 = {}
for b in range(12):
    sol = SC.solve_H(SC.H_avg(tval(4,b)))
    if sol[2] != 0 or sol[3] != 0: bright4[str(b)] = [str(x) for x in sol]
print("T3 row 4 bright cells:", bright4)

# T2 mechanism probe: the j-window zeta5^{-4j} sees j mod 5; row 4's is zeta5^{-j}.
# Examine the H-avg'd anti-content per j-class: A_l(jmod5) := sum_{j in class} C[j][l],
# then row16 kill <=> sum_c zeta5^{-4c} (DFT_l A(c)) anti-part vanishes; report the exact
# per-class anti vectors for the b in row-16's support to exhibit the cancellation pattern.
def anti_of(t):
    sol = SC.solve_H(SC.H_avg(t))
    return (sol[2], sol[3]) if sol else None
pattern = {}
for b in (0,4,8):
    per = []
    for c in range(5):
        t = E.ZERO
        for j in range(c, o1, 5):
            for l in range(o2):
                t = E.add(t, E.mul(E.mul(E.zeta(0), E.zeta((-5*l*b)%60)), C[j][l]))
        t = E.scal(Fr(1,o1*o2), t)
        per.append([str(x) for x in (anti_of(t) or ())])
    pattern[str(b)] = per
print("T2 per-(j mod 5)-class anti parts (b in support):")
for b,v in pattern.items(): print("  b=%s:"%b, v)
json.dump(dict(T1_ok=ok, row16=res, row4_bright=bright4, T2_classes=pattern),
          open(os.path.join(HERE,"row16.json"),"w"), indent=1)
print("DONE")
