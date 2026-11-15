"""B1945 section 5 (P-860 (a)): the coupling summed over the 24 points before the SVD, with equal weights, is not a function on
the modular surface. Its mass ratios at tau and at tau + 1 differ (the canonical end is read at Re tau mod 1, so it is the
same at both), while every pointwise ratio is covariant (B1928; B1940's V2). Data-free (main, 2026-11-15)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import determinant_law as DL
from fractions import Fraction as Fr
mp = DL.mp
PTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
def summed(tx, ty, sec, rn):
    tot = None
    for a, b in PTS:
        _, _, Ys, *_ = DL.parts(tx, ty, a, b, sec)
        tot = Ys[rn] if tot is None else tot + Ys[rn]
    return tot
def sv(Y):
    s = sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True); return [float(s[1] / s[0]), float(s[2] / s[0])]
if __name__ == "__main__":
    for (tx, tx1, ty) in (("0.13", "1.13", 1.7), ("-0.31", "0.69", 2.9)):
      for sec in ("up", "down"):
          for rn in ("S", "St"):
              A, B_ = summed(tx, ty, sec, rn), summed(tx1, ty, sec, rn)
              print("tau=%s+%si %s %s: summed-Y ratios %s ; at tau+1 %s" % (tx, ty, sec, rn, ["%.6f" % v for v in sv(A)], ["%.6f" % v for v in sv(B_)]), flush=True)
