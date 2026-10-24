"""B1749, after the read (POST HOC, labelled): where the rows below the six's bar sit -- lines (alpha, b) and orders, apex
heights, horocycles, menu configurations -- under the seat's menu, through B1741's own feature code (loaded by this arc's
compare.py, unchanged).  Prints only.
    python3 -B posthoc_read.py"""
import sys, math, collections, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import compare as P      # noqa: E402  (loads B1741's compare.py as P.C, re-pointed to this census)
import importlib.util      # noqa: E402
_sp = importlib.util.spec_from_file_location("b1726_census", HERE.parents[1] / "B1726_the_two_ingredients_replicated" / "verification" / "census.py")
K26 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(K26)

if __name__ == "__main__":
    C = P.C; A = C.arrays(); T6 = A["T6"][None, :]; lines = K26.lines()
    F = C.chi2_features("seat", False)
    names = [(cfg, c) for cfg in C.SEAT for c in (1, 3)]
    per = np.array([((X - f(T6)) ** 2).sum(1) for X, f in F])          # (configs, rows)
    best = per.min(0); arg = per.argmin(0)
    good = np.where(best < 16.75)[0]
    print("rows (row x horocycle) below 16.75 under the seat's menu: %d of %d" % (len(good), len(best)))
    order = lambda a, b: math.lcm(Fr(a).denominator, Fr(b).denominator)
    byo, byl, byh, byc, hs = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter(), []
    for i in good:
        ln, re, im, hor = A["lab"][i]; a, b = lines[ln]
        byo[order(a, b)] += 1; byl[(str(Fr(a)), str(Fr(b)))] += 1; byh[hor] += 1; byc[names[arg[i]]] += 1; hs.append(im)
    print("by order:", sorted(byo.items())); print("by line:", byl.most_common(8)); print("by horocycle:", dict(byh))
    print("by configuration ((up, down, lepton) readings, c):", dict(byc))
    print("apex heights: %d distinct, %.3f-%.3f; the five lowest chi2:" % (len(set(np.round(hs, 4))), min(hs), max(hs)))
    for i in good[np.argsort(best[good])][:5]:
        ln, re, im, hor = A["lab"][i]; print("   chi2 %.2f  line %d %s  tau %.4f + %.4fi  %s  %s" % (best[i], ln, tuple(str(Fr(x)) for x in lines[ln]), re, im, hor, names[arg[i]]))
