"""B393 -- the products' full H-vectors: dark products fully real, or only s-free?"""
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

def spectra(m1, m2, q, u):
    o1,_ = matrix_order(build_theta_W(m1)); o2,_ = matrix_order(build_theta_W(m2))
    T = local_partrace_table(q, u, m1, m2, o1, o2)
    z1, z2 = 60//o1, 60//o2
    out = {}
    for a in range(o1):
        for b in range(o2):
            t = E.ZERO
            for j in range(o1):
                za = E.zeta((-z1*j*a) % 60)
                for l in range(o2):
                    t = E.add(t, E.mul(E.mul(za, E.zeta((-z2*l*b) % 60)), T[(j,l)]))
            if any(x != 0 for x in t):
                out[(a,b)] = E.scal(Fr(1, o1*o2), t)
    return out, o1, o2

res = {}
for (m1,m2,st) in ((1,3,"dark"),(1,4,"dark"),(3,5,"dark"),(3,4,"bright"),(2,3,"bright")):
    X3, o1, o2 = spectra(m1, m2, 3, 2)
    X5, _, _   = spectra(m1, m2, 5, 2)
    kinds = {"zero":0, "real(x,y)":0, "z-only":0, "s-carrying":0}
    for v, x3 in X3.items():
        for w, x5 in X5.items():
            sol = SC.solve_H(SC.H_avg(E.mul(x3, x5)))
            if sol is None: continue
            if all(x == 0 for x in sol): kinds["zero"] += 1
            elif sol[2] == 0 and sol[3] == 0: kinds["real(x,y)"] += 1
            elif sol[3] == 0: kinds["z-only"] += 1
            else: kinds["s-carrying"] += 1
    res[f"{m1},{m2}"] = dict(status=st, **kinds)
    print(f"({m1},{m2}) {st:7s}: {kinds}")
json.dump(res, open(os.path.join(HERE, "product_fields.json"), "w"), indent=1)
print("DONE")
