import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import math, cmath, numpy as np, sm_c7_lib as L
def fixed_chars(M, N):
    (a, b), (c, d) = M
    return [(i, j, N) for i in range(N) for j in range(N) if (i, j) != (0, 0) and ((i*a + j*c - i) % N, (i*b + j*d - j) % N) == (0, 0)]
h = 0.3; pts = [h * cmath.exp(2j * math.pi * k / 8) for k in range(8)]
for M in ([[-3, -1], [-2, -1]], [[7, 4], [5, 3]]):
    geo = L.Geodesic(M); chars = fixed_chars(M, 12)[:3] + fixed_chars(M, 8)[:2]
    R = L.level_zetas(geo, chars, pts)
    for ch in chars:
        d = sum(sum(R[ch][s]) / s for s in pts) / 8
        print(M, ch, "Ztot'(0) + ell/2 = %.2e" % abs(d + geo.ell / 2), " Ztot'(0) = %.10f" % d.real)
