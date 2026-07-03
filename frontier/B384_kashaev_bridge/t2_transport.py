"""B384 T2 -- the tower-transport bet: level-15 single-seed DFT constants (exact engine)
vs the banked level-45 identified singles (sweep45.json)."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order

N = 15
out = {}
for m in (1, 2):
    W = build_theta_W(m)
    o, pw = matrix_order(W)
    z = 60 // o
    vals = {}
    for a in range(o):
        t = E.ZERO
        for j in range(o):
            trj = E.ZERO
            for x in range(N):
                trj = E.add(trj, pw[j][(-x) % N][x])
            t = E.add(t, E.mul(E.zeta((-z*j*a) % 60), trj))
        t = E.scal(Fr(1, o), t)
        sol = SC.solve_H(SC.H_avg(t))
        if sol and any(x != 0 for x in sol):
            vals[str(a)] = [str(x) for x in sol]
    out[f"m{m}_ord{o}"] = vals
    print(f"level-15 m={m} (ord {o}) nonzero singles:")
    for a, v in vals.items(): print(f"  a={a}: {v}")
json.dump(out, open(os.path.join(HERE, "t2_level15_singles.json"), "w"), indent=1)
print("DONE")
