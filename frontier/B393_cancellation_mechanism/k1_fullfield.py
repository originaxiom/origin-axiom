"""B393 K1 (corrected) -- termwise test with FULL-FIELD spectra: term(a,b;A,B) =
s-part of Pi_H( X3(a,b) * X5(A-a,B-b) ); sum over (a,b) must reproduce s(t(A,B))
(sanity), and the question is whether nonzero terms exist for the cancelling pairs."""
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

def s_of(t):
    sol = SC.solve_H(SC.H_avg(t))
    return sol[3] if sol else Fr(0)

def run(m1, m2, st):
    W1 = build_theta_W(m1); W2 = build_theta_W(m2)
    o1,_ = matrix_order(W1); o2,_ = matrix_order(W2)
    T3 = local_partrace_table(3, 2, m1, m2, o1, o2)
    T5 = local_partrace_table(5, 2, m1, m2, o1, o2)
    z1, z2 = 60//o1, 60//o2
    X3, X5 = {}, {}
    for a in range(o1):
        for b in range(o2):
            t3 = E.ZERO; t5 = E.ZERO
            for j in range(o1):
                za = E.zeta((-z1*j*a) % 60)
                for l in range(o2):
                    zb = E.zeta((-z2*l*b) % 60)
                    t3 = E.add(t3, E.mul(E.mul(za, zb), T3[(j,l)]))
                    t5 = E.add(t5, E.mul(E.mul(za, zb), T5[(j,l)]))
            if any(x != 0 for x in t3): X3[(a,b)] = E.scal(Fr(1,o1*o2), t3)
            if any(x != 0 for x in t5): X5[(a,b)] = E.scal(Fr(1,o1*o2), t5)
    nonzero_terms = 0; total = 0; cells_nonzero_sum = 0
    for A in range(o1):
        for Bb in range(o2):
            ssum = Fr(0)
            for (a, b), x3 in X3.items():
                x5 = X5.get(((A-a) % o1, (Bb-b) % o2))
                if x5 is None: continue
                v = s_of(E.mul(x3, x5))
                total += 1
                if v != 0: nonzero_terms += 1; ssum += v
            if ssum != 0: cells_nonzero_sum += 1
    print(f"({m1},{m2}) {st:7s}: |X3|={len(X3)} |X5|={len(X5)} terms={total} "
          f"nonzero-terms={nonzero_terms} cells-with-nonzero-sum={cells_nonzero_sum}")
    return dict(status=st, X3=len(X3), X5=len(X5), terms=total,
                nonzero_terms=nonzero_terms, cells_nonzero_sum=cells_nonzero_sum)

if __name__ == "__main__":
    res = {}
    for (m1, m2, st) in ((1,3,"dark"),(3,5,"dark"),(3,4,"bright"),(2,3,"bright")):
        res[f"{m1},{m2}"] = run(m1, m2, st)
    json.dump(res, open(os.path.join(HERE, "k1_fullfield.json"), "w"), indent=1)
    print("DONE")
