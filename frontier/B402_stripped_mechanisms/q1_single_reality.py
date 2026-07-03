"""B402 Q1 -- cell-wise vs aggregate tau3-reality of the single traces."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

ID = [[E.ONE if i == j else E.ZERO for j in range(15)] for i in range(15)]
out = {}
for m in (1, 2):
    W = build_theta_W(m)
    o, pw = matrix_order(W)
    cellwise_real = 0; cellwise_imag = 0; imag_cells = []
    for j in range(o):
        t = par_trace(pw[j], ID)
        sol = SC.solve_H(SC.H_avg(t))
        if sol is None:
            imag_cells.append((j, "outsideH")); cellwise_imag += 1; continue
        if sol[2] == 0 and sol[3] == 0: cellwise_real += 1
        else: cellwise_imag += 1; imag_cells.append((j, [str(x) for x in sol]))
    out[f"m{m}"] = dict(ord=o, real_cells=cellwise_real, imag_cells=cellwise_imag,
                        examples=imag_cells[:4])
    print(f"m={m}: {cellwise_real}/{o} single traces tau3-real cell-wise; imag: {cellwise_imag}")
    for x in imag_cells[:4]: print("   imag example:", x)
json.dump(out, open(os.path.join(HERE, "q1_single_reality.json"), "w"), indent=1)
print("DONE")
