"""B409 -- the stratification-transport check across all six pairs."""
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

# side 1: the table anatomy (banked)
NEST = json.load(open(os.path.join(HERE, "..", "B407_support_nesting", "nesting.json")))

# side 2: the product stratification per pair
def product_strata(m1, m2):
    o1,_ = matrix_order(build_theta_W(m1)); o2,_ = matrix_order(build_theta_W(m2))
    T3 = local_partrace_table(3, 2, m1, m2, o1, o2)
    T5 = local_partrace_table(5, 2, m1, m2, o1, o2)
    z1, z2 = 60//o1, 60//o2
    def spec(T):
        out = {}
        for a in range(o1):
            for b in range(o2):
                t = E.ZERO
                for j in range(o1):
                    za = E.zeta((-z1*j*a) % 60)
                    for l in range(o2):
                        t = E.add(t, E.mul(E.mul(za, E.zeta((-z2*l*b) % 60)), T[(j,l)]))
                t = E.scal(Fr(1, o1*o2), t)
                if any(x != 0 for x in t): out[(a,b)] = t
        return out
    X3, X5 = spec(T3), spec(T5)
    s_carry = z_only = 0
    for x3 in X3.values():
        for x5 in X5.values():
            sol = SC.solve_H(SC.H_avg(E.mul(x3, x5)))
            if sol is None: continue
            if sol[3] != 0: s_carry += 1
            elif sol[2] != 0: z_only += 1
    return s_carry, z_only

PAIRS = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
res = {}
allpass = True
for (m1, m2) in PAIRS:
    n = NEST[f"{m1},{m2}"]
    table_s = n["both"] + n["s_only"]     # s-carrying t-cells
    table_z = n["z_only"]                 # z-only t-cells
    prod_s, prod_z = product_strata(m1, m2)
    match = (table_s == prod_s and table_z == prod_z)
    allpass = allpass and match
    res[f"{m1},{m2}"] = dict(table_s=table_s, table_z=table_z,
                             prod_s=prod_s, prod_z=prod_z, match=match)
    print(f"({m1},{m2}): table(s={table_s},z={table_z}) vs product(s={prod_s},z={prod_z}) -> {'MATCH' if match else 'DIFFER'}")
res["all_match"] = allpass
print("TRANSPORT THEOREM 6/6:", allpass)
json.dump(res, open(os.path.join(HERE, "transport.json"), "w"), indent=1)
print("DONE")
