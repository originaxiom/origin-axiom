"""c5b: the c5 lines whose fitted exponent was off at Im tau 2-3.5 (small ||.||: the m = 3, 5 Hurwitz-Lerch terms decay only
2-3x faster), re-measured at Im tau 5-8 with main's cA (down sector)."""
import math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
def cs(al, b, tau):
    w = B.line_w(al, b, tau); x, yy = B.sector_twists(w, tau, 1, 2); R = B.residues(x, yy, tau); return B.cA(x, yy, tau, R)
def dist(v): v = v % 1; return min(v, 1 - v)
ys = [5.0, 6.0, 7.0, 8.0]
for (al, b) in ((F(1, 7), F(3, 7)), (F(1, 7), F(0)), (F(1, 5), F(1, 10)), (F(1, 8), F(3, 8)), (F(4, 9), F(2, 9))):
    for rx in (0.17, 0.41):
        d1, d2 = [], []
        for y in ys:
            c = cs(al, b, complex(rx, y)); d1.append(c["1"] - c["i"]); d2.append(c["j"] - c["k"])
        k1 = -np.polyfit(ys, [math.log(abs(v)) for v in d1], 1)[0]; k2 = -np.polyfit(ys, [math.log(abs(v)) for v in d2], 1)[0]
        # local (pairwise) exponents too
        loc2 = [-(math.log(abs(d2[i + 1])) - math.log(abs(d2[i]))) / (ys[i + 1] - ys[i]) / (4 * math.pi) for i in range(3)]
        loc1 = [-(math.log(abs(d1[i + 1])) - math.log(abs(d1[i]))) / (ys[i + 1] - ys[i]) / (4 * math.pi) for i in range(3)]
        e = dist(3 * al)
        say("(%s,%s) Re %.2f: E1 pred %.4f meas %.4f local %s | E2 pred %.4f meas %.4f local %s | |d1|,|d2| at Im 8: %.1e, %.1e" % (
            al, b, rx, e / 2, k1 / (4 * math.pi), ["%.4f" % v for v in loc1], 0.25 - e / 2, k2 / (4 * math.pi), ["%.4f" % v for v in loc2], abs(d1[-1]), abs(d2[-1])))
pathlib.Path(__file__).with_name("c5b_p559_large_im_tau_out.txt").write_text("\n".join(out) + "\n")
