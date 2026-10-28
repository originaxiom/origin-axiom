"""P-397 curvature route, part b: (i) a line where B1742's lepton = down identity is exact at eps = 0 ((2/5, 1/5), k even:
any Higgs) -- does a profile break R2 = 1, and which? (ii) large eps on (2/5, 1/10) at Im tau 3: does R2 ever approach 3?"""
import sys, json, pathlib
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import curvature as K
HERE = pathlib.Path(__file__).resolve().parent
res = {}
for im_t in (3.0, 6.0):
    R2, R1, o = K.ratios(0.3, im_t, Fr(2, 5), Fr(1, 5), "cos2pi_x1", 0.0, K.cA_w)
    print("(2/5, 1/5) Im tau %g eps 0: R2 %.10f R1 %.10f" % (im_t, R2, R1), flush=True); res["(2/5,1/5)|%g|eps0" % im_t] = [R2, R1]
    for prof in K.PROFILES:
        for e in (0.1, 0.5):
            R2, R1, o = K.ratios(0.3, im_t, Fr(2, 5), Fr(1, 5), prof, e, K.cA_w)
            res["(2/5,1/5)|%g|%s|%g" % (im_t, prof, e)] = [R2, R1]
            print("  (2/5, 1/5) Im tau %g %-10s eps %.2f  R2 %.10f  R1 %.10f" % (im_t, prof, e, R2, R1), flush=True)
for prof in ("cos2pi_x1", "cos2pi_y1", "asym"):
    for e in (0.5, 1.0, 2.0, 4.0):
        R2, R1, o = K.ratios(0.3, 3.0, Fr(2, 5), Fr(1, 10), prof, e, K.cA_w)
        res["(2/5,1/10)|3|%s|%g" % (prof, e)] = [R2, R1]
        print("  (2/5, 1/10) Im tau 3 %-10s eps %.2f  R2 %.5f  R1 %.5f" % (prof, e, R2, R1), flush=True)
json.dump(res, open(HERE / "curvature_b.json", "w"), indent=1)
print("curvature_b exit 0")
