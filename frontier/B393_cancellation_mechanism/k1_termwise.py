"""B393 K1 -- termwise test: is every pairing term B(x3(a,b), x5(A-a,B-b)) zero for the
cancelling pairs (strong disjointness), or do nonzero terms cancel in the sum?"""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B386_crt_closed_form"))
import cyclo_engine as E
from step0_exact_matrices import build_theta_W, matrix_order
from tensor_gate import local_partrace_table
sys.path.insert(0, os.path.join(HERE, "..", "B390_criterion_tensor"))
from attribution_pairing import B, field_coords

def spectra(m1, m2):
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
            c3 = field_coords(E.scal(Fr(1,o1*o2), t3), 12)
            c5 = field_coords(E.scal(Fr(1,o1*o2), t5), 20)
            if c3 and any(x != 0 for x in c3): X3[(a,b)] = c3
            if c5 and any(x != 0 for x in c5): X5[(a,b)] = c5
    return o1, o2, X3, X5

def pairB(c3, c5):
    return sum(c3[r]*B[r][s]*c5[s] for r in range(4) for s in range(8))

res = {}
for (m1, m2, st) in ((1,3,"dark"),(1,4,"dark"),(3,5,"dark"),(3,4,"bright"),(2,3,"bright")):
    o1, o2, X3, X5 = spectra(m1, m2)
    nonzero_terms = 0; total_terms = 0; sums_nonzero = 0
    for A in range(o1):
        for Bb in range(o2):
            ssum = Fr(0)
            for (a, b), c3 in X3.items():
                key = ((A - a) % o1, (Bb - b) % o2)
                c5 = X5.get(key)
                if c5 is None: continue
                v = pairB(c3, c5)
                total_terms += 1
                if v != 0: nonzero_terms += 1
                ssum += v
            if ssum != 0: sums_nonzero += 1
    res[f"{m1},{m2}"] = dict(status=st, spec3=len(X3), spec5=len(X5),
                             terms=total_terms, nonzero_terms=nonzero_terms,
                             cells_with_nonzero_sum=sums_nonzero)
    print(f"({m1},{m2}) {st:7s}: |spec3|={len(X3)} |spec5|={len(X5)} "
          f"terms={total_terms} nonzero-terms={nonzero_terms} s-cells={sums_nonzero}")
json.dump(res, open(os.path.join(HERE, "k1_termwise.json"), "w"), indent=1)
print("DONE")
