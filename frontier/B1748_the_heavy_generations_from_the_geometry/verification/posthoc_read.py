"""B1748, after the read (POST HOC, labelled): where the rows below the bar sit -- their lines (alpha, b) and orders, the
menu entries (null line, lepton factor), and Im tau -- on L_max, from the committed census and the sealed compare.py's
own arrays and targets (imported; nothing recomputed in the frame).  Prints only.
    python3 -B posthoc_read.py"""
import sys, math, collections, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import compare as C      # noqa: E402
import census as K      # noqa: E402


def order(a, b):
    return math.lcm(Fr(a).denominator, Fr(b).denominator)


if __name__ == "__main__":
    _, R, _ = K._imports(); lines = R.CEN.lines()
    T, sg = C.targets(); A = C.arrays()
    for hor in ("L_max", "L_2"):
        chi = (((A[hor] - T) / sg) ** 2).sum(axis=2)
        good = np.argwhere(chi < C.BAR4)
        byline, byorder, bymenu, byalpha = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
        rows = set()
        for m, i in good:
            ln = A["lab"][i][0]; a, b = lines[ln]; rows.add(int(i))
            byline[(str(Fr(a)), str(Fr(b)))] += 1; byorder[order(a, b)] += 1; bymenu[C.MENU[m]] += 1; byalpha[str(Fr(a))] += 1
        print("%s: %d (row, menu) pairs below the bar on %d rows" % (hor, len(good), len(rows)))
        print("   by order:", sorted(byorder.items())); print("   by alpha:", byalpha.most_common(6))
        print("   by menu:", dict(bymenu)); print("   lines:", byline.most_common(10))
        ims = sorted({round(A["lab"][int(i)][2], 3) for _, i in good}); print("   Im tau span %.3f-%.3f, %d distinct heights" % (ims[0], ims[-1], len(ims)))
