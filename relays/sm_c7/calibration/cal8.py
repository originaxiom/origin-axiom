import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
# production cone sums against the calibrated ones and against Hecke, on the calibration matrices
import math, numpy as np, sm_c7_lib as L, time
from fractions import Fraction as Fr
def fixed_chars(M, N):
    (a, b), (c, d) = M
    return [(i, j, N) for i in range(N) for j in range(N) if (i, j) != (0, 0) and ((i*a + j*c - i) % N, (i*b + j*d - j) % N) == (0, 0)]
for M in ([[-3, -1], [-2, -1]], [[7, 4], [5, 3]]):
    geo = L.Geodesic(M); chars = fixed_chars(M, 12)[:3] + fixed_chars(M, 8)[:2]
    t = time.time()
    R = L.level_zetas(geo, chars, [1, 2, 0])
    print(M, "time", round(time.time() - t, 1))
    for ch in chars:
        i, j, N = ch
        ztot1 = sum(R[ch][1]); ztot2 = sum(R[ch][2]); z0 = R[ch][0]
        old1 = L.Z_total(geo, i, j, N, 1)
        k1 = L.hecke_side(geo, (Fr(i, N), Fr(j, N)), 1, n=48)
        print("  ", ch, "Ztot(1) new-old %.1e" % abs(ztot1 - old1), " Hecke s=1 %.1e" % abs(L.H(1)*ztot1 - k1),
              " Zsame(0)/2 vs B1737 %.1e" % abs(z0[0]/2 - L.Z0_b1737(geo, i, j, N)), " Ztot(0) %.1e" % abs(sum(z0)))
