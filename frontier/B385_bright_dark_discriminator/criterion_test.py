"""B385 -- THE CRITERION TEST on all 12 pairs:
DARK <=> for every support cell (a,b) of the t-table there is an odd anti-translation
(dj,dl) with character even there (zeta_{o1}^{-a dj} zeta_{o2}^{-b dl} = +1) -- i.e. no
support cell survives all translation-kills. Ingredients per pair: (i) odd translations of
the exact anti-table; (ii) the support = nonzero t(a,b) cells; (iii) the anti-carrying
support cells (ground truth)."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

PAIRS = [((1,2),"bright"),((2,3),"bright"),((2,4),"bright"),((3,4),"bright"),
         ((1,7),"bright"),((3,7),"bright"),((2,7),"bright"),
         ((1,3),"dark"),((1,4),"dark"),((3,5),"dark"),((1,5),"dark"),((4,5),"dark")]

def full_data(m1, m2):
    W1 = build_theta_W(m1); W2 = build_theta_W(m2)
    o1, p1 = matrix_order(W1); o2, p2 = matrix_order(W2)
    C = {}
    for j in range(o1):
        for l in range(o2):
            C[(j,l)] = par_trace(p1[j], p2[l])
    # anti-table
    A = {}
    for k, v in C.items():
        sol = SC.solve_H(SC.H_avg(v))
        A[k] = (sol[2], sol[3]) if sol else (Fr(0), Fr(0))
    # odd translations
    odd = []
    for dj in range(o1):
        for dl in range(o2):
            if (dj, dl) == (0, 0): continue
            if all(A[((j+dj)%o1,(l+dl)%o2)] == (-A[(j,l)][0], -A[(j,l)][1])
                   for j in range(o1) for l in range(o2)):
                odd.append((dj, dl))
    # t-table: support + anti cells
    z1, z2 = 60 // o1, 60 // o2
    support, anti_cells = [], []
    for a in range(o1):
        for b in range(o2):
            t = E.ZERO
            for j in range(o1):
                za = E.zeta((-z1*j*a) % 60)
                for l in range(o2):
                    t = E.add(t, E.mul(E.mul(za, E.zeta((-z2*l*b) % 60)), C[(j,l)]))
            t = E.scal(Fr(1, o1*o2), t)
            sol = SC.solve_H(SC.H_avg(t))
            if sol is None or all(x == 0 for x in sol): continue
            support.append((a, b))
            if sol[2] != 0 or sol[3] != 0: anti_cells.append((a, b))
    return o1, o2, odd, support, anti_cells

report = {}
ok_all = True
for (m1, m2), st in PAIRS:
    o1, o2, odd, sup, ac = full_data(m1, m2)
    # criterion: cell (a,b) is KILLED if some odd translation has even character there
    surv = []
    for (a, b) in sup:
        dead = False
        for (dj, dl) in odd:
            # character value on translation = zeta_{o1}^{a dj} zeta_{o2}^{b dl}; even <=> == +1
            if (a*dj) % o1 == 0 and (b*dl) % o2 == 0:
                dead = True; break
            # even also if the combined root of unity equals +1:
            num = (a*dj)*o2 + (b*dl)*o1     # exponent over lcm denominator o1*o2
            if num % (o1*o2) == 0:
                dead = True; break
        if not dead: surv.append((a, b))
    pred = "bright" if surv else "dark"
    match = (pred == st)
    truth_ok = (set(ac) <= set(surv))    # every actual anti cell must be a survivor
    ok_all = ok_all and match and truth_ok
    report[f"{m1},{m2}"] = dict(status=st, odd=[list(x) for x in odd],
                                support_n=len(sup), anti_cells=[list(x) for x in ac],
                                survivors=[list(x) for x in surv],
                                predicted=pred, match=match, anti_subset_surv=truth_ok)
    print(f"({m1},{m2}) {st:7s}: odd-translations {odd}; support {len(sup)}; "
          f"anti-cells {ac}; survivors {surv[:6]}{'...' if len(surv)>6 else ''} -> pred {pred} "
          f"{'OK' if match else 'MISS'} truth{'OK' if truth_ok else 'FAIL'}")
print("CRITERION 12/12:", ok_all)
json.dump(report, open(os.path.join(HERE, "criterion.json"), "w"), indent=1)
print("DONE")
