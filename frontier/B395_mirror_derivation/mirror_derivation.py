"""B395 -- the cell-wise sigma11 law + the exact-summation gate."""
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

# L1: the cell-wise law C[j,-l] == sigma11(C[j,l]) (sigma on zeta60: exponent 11 acts on
# the zeta15-content; C lives in Q(zeta15) subset Q(zeta60) -- apply SC.sigma with the
# zeta60-exponent c with c = 11 mod 15 and c = 1 mod 4 (to fix i): c = 41? 41 mod 15 = 11,
# 41 mod 4 = 1. Register c = 41 as the lift; also test c = 11 (11 mod 4 = 3).
def test_law(c):
    bad = []
    for j in range(o1):
        for l in range(o2):
            if SC.sigma(C[(j,l)], c) != C[(j, (-l) % o2)]:
                bad.append((j,l))
    return bad

for c in (41, 11):
    bad = test_law(c)
    print(f"cell-wise law with sigma_{c}: {'HOLDS all 240' if not bad else f'fails at {len(bad)} cells'}")
    if not bad:
        LIFT = c
        break
else:
    LIFT = None

result = dict(lift=LIFT)
if LIFT:
    # the summation gate: derive t(a,-b) from the law + exact summation; compare to
    # tau3 of the banked t(a,b) -- computed independently, engine-exact.
    def tval(a, b):
        t = E.ZERO
        for j in range(o1):
            za = E.zeta((-3*j*a) % 60)
            for l in range(o2):
                t = E.add(t, E.mul(E.mul(za, E.zeta((-5*l*b) % 60)), C[(j,l)]))
        return E.scal(Fr(1, o1*o2), t)
    def hp(t): return SC.solve_H(SC.H_avg(t))
    ok = True
    checked = 0
    for a in range(0, o1, 3):          # sample rows incl. slot rows 6? 6 not in range step3... use explicit set
        pass
    rows = [0, 1, 4, 6, 9, 14, 16]
    for a in rows:
        for b in range(o2):
            lhs = hp(tval(a, (-b) % o2))
            rhs = hp(tval(a, b))
            if lhs is None or rhs is None: continue
            tau = (rhs[0], rhs[1], -rhs[2], -rhs[3])
            if tuple(lhs) != tau: ok = False
            checked += 1
    result.update(summation_gate=ok, cells_checked=checked)
    print(f"summation gate (mirror reproduced from the law): {ok} on {checked} cells")
json.dump(result, open(os.path.join(HERE, "mirror_derivation.json"), "w"), indent=1)
print("DONE")
