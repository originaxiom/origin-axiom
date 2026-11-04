"""S301-A check c30b: B1667's L_max, L_2 at the rebuilt Theorem 29 minimum tau* = -0.187113 + 2.404292i (c29; fundamental-strip
representative) and at its mirror +0.187113 + 2.404292i, with the Re tau = 1/4 column read for comparison (as c30)."""
import os, sys
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c30_l2 as C
for t in (complex(-0.187113, 2.404292), complex(0.187113, 2.404292)):
    lm, l2, res = C.L_pair(t); cm, c2 = C.col_read(t.imag)
    print("c30b tau = %s: B1667 L_max = %.10f, L_2 = %.10f (residual %.0e); column read L_max %.6f, L_2 %.6f -> off by %.2e, %.2e"
          % (t, lm, l2, res, cm, c2, cm - lm, c2 - l2), flush=True)
