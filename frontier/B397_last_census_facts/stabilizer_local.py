"""B397(a) -- the (2,3) stabilizer: is the property local (X5 Galois structure)?"""
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

def x5_gal(m1, m2):
    o1,_ = matrix_order(build_theta_W(m1)); o2,_ = matrix_order(build_theta_W(m2))
    T5 = local_partrace_table(5, 2, m1, m2, o1, o2)
    z1, z2 = 60//o1, 60//o2
    # the RAW local cells' Galois structure (cell-level, pre-DFT -- the local table itself)
    # sigma fixing sqrt5 but moving zeta5: c = 19 (19 mod 5 = 4 = -1: zeta5 -> zeta5^-1, fixes sqrt5)
    fixed_cells = 0; moved = 0; nonzero = 0
    for k, v in T5.items():
        if all(x == 0 for x in v): continue
        nonzero += 1
        if SC.sigma(v, 19) == v: fixed_cells += 1
        else: moved += 1
    return dict(nonzero=nonzero, sigma19_fixed=fixed_cells, moved=moved)

res = {}
for (m1, m2) in ((2,3), (1,2), (3,4)):
    r = x5_gal(m1, m2)
    res[f"{m1},{m2}"] = r
    print(f"({m1},{m2}) 5-local cells: {r}")
json.dump(res, open(os.path.join(HERE, "stabilizer_local.json"), "w"), indent=1)
print("DONE")
