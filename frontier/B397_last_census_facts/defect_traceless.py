"""B397(b) -- the graded traces of the u5-flipped model vs sigma_sqrt5 of the banked."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B386_crt_closed_form"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order
from tensor_gate import local_partrace_table

o1, o2 = 20, 12
T3 = local_partrace_table(3, 2, 1, 2, o1, o2)
T5_std  = local_partrace_table(5, 2, 1, 2, o1, o2)   # the banked model (u5 = 2)
T5_flip = local_partrace_table(5, 1, 1, 2, o1, o2)   # the sigma-conjugate class (u5 = 1)

def tval(T5, a, b):
    t = E.ZERO
    for j in range(o1):
        za = E.zeta((-3*j*a) % 60)
        for l in range(o2):
            t = E.add(t, E.mul(E.mul(za, E.zeta((-5*l*b) % 60)),
                               E.mul(T3[(j,l)], T5[(j,l)])))
    return E.scal(Fr(1, o1*o2), t)
def hp(t): return SC.solve_H(SC.H_avg(t))

GRADINGS = {
    "slot":   [(6,2,1),(6,10,-1),(14,2,-1),(14,10,1)],
    "3block": [(4,8,1),(4,4,-1),(0,8,-1),(0,4,1)],
}
def const(T5, cells):
    t = E.ZERO
    for (a,b,s) in cells:
        t = E.add(t, E.scal(Fr(s), tval(T5, a, b)))
    return hp(t)

res = {}
ok_all = True
for g, cells in GRADINGS.items():
    c_std  = const(T5_std, cells)
    c_flip = const(T5_flip, cells)
    conj = (c_std[0], -c_std[1], c_std[2], -c_std[3])     # sigma_sqrt5 on (1,√5,√−3,√−15)
    match = tuple(c_flip) == conj
    ok_all = ok_all and match
    res[g] = dict(std=[str(x) for x in c_std], flip=[str(x) for x in c_flip], conjugate_match=match)
    print(f"{g}: std {[str(x) for x in c_std]}  flip {[str(x) for x in c_flip]}  sigma-match: {match}")
# and at least one raw cell differs (the known contrast)
diff_cells = sum(1 for k in T5_std if E.mul(T3[k], T5_std[k]) != SC.sigma(E.mul(T3[k], T5_flip[k]), 1) and T5_std[k] != T5_flip[k])
raw_differs = any(T5_std[k] != T5_flip[k] for k in T5_std)
res["raw_cells_differ"] = raw_differs
print("raw local cells differ between models:", raw_differs, " | all graded conjugacies:", ok_all)
json.dump(res, open(os.path.join(HERE, "defect_traceless.json"), "w"), indent=1)
print("DONE")
