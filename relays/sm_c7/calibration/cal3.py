import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
# calibration C6-C7 on matrices outside B1737's population: cone sums (EM vs brute at s = 3; stability), Hecke at s = 1, 2, 3
import math, numpy as np, sm_c7_lib as L, itertools, json, sys
from fractions import Fraction as Fr
out = {}
CAL = [[[-3, -1], [-2, -1]], [[7, 4], [5, 3]]]
def fixed_chars(M, N):
    (a, b), (c, d) = M
    return [(i, j) for i in range(N) for j in range(N) if (i, j) != (0, 0) and ((i*a + j*c - i) % N, (i*b + j*d - j) % N) == (0, 0)]
for M in CAL:
    geo = L.Geodesic(M)
    for N in (5, 7, 12):
        fc = fixed_chars(M, N)
        if fc: break
    print("M", M, "N", N, "fixed chars", fc[:6], "D", geo.D, "ell", geo.ell, "sigma", geo.sigma)
    i, j = fc[0]
    chi = L.char(i, j, N)
    # C6: one cone, s = 3, EM vs brute
    w = L.find_w(geo, chi, True); G = M if geo.tr > 0 else np.array(M, dtype=object).dot(np.array(M, dtype=object)).tolist()
    em = L.cone_sum(geo, w, G, chi, 3, K=60, J=30)
    w2 = tuple(int(t) for t in np.array(G, dtype=object).dot(np.array(w, dtype=object)))
    br = 0
    kk = np.arange(1500)
    for p in L.parallelogram(w, w2):
        V0 = p[0] + kk[:, None]*w[0] + kk[None, :]*w2[0]; V1 = p[1] + kk[:, None]*w[1] + kk[None, :]*w2[1]
        Q = np.abs(geo.Q((V0, V1)))
        br += np.sum(np.exp(2j*math.pi*((i*V0 + j*V1) % N)/N) * Q**-3.0)
    print("  C6 s=3 EM vs brute:", abs(em - br), abs(em))
    for s in (1, 2):
        a = L.cone_sum(geo, w, G, chi, s, K=80, J=30); b = L.cone_sum(geo, w, G, chi, s, K=140, J=40)
        print("  C6 s=%d stability K80/J30 vs K140/J40:" % s, abs(a - b), abs(a))
    z0 = L.cone_sum(geo, w, G, chi, 0, K=40, J=20)
    exact = sum(chi(p) for p in L.parallelogram(w, w2)) / (1 - chi(w))**2
    print("  C6 s=0 vs exact:", abs(z0 - exact))
    # C7: Hecke at s = 1, 2, 3 for the first few fixed characters
    for (i, j) in fc[:4]:
        c = (Fr(i, N), Fr(j, N))
        for s in (3, 2, 1):
            lhs = L.hecke_side(geo, c, s, n=48)
            rhs = L.H(s) * L.Z_total(geo, i, j, N, s, K=100, J=34)
            print("  C7 chi=(%d,%d) s=%d  lhs %.12f%+.2ej  rhs %.12f%+.2ej  |diff| %.2e" % (i, j, s, lhs.real, lhs.imag, rhs.real, rhs.imag, abs(lhs - rhs)))
