import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
# calibration C4-C5: weight-2 v-twisted G_c and u-shifted G^(u)*: Fourier vs ordered brute sum; reduction (weight 2)
import math, numpy as np, sm_c7_lib as L
from fractions import Fraction as Fr
def brute_v(c, z, M=60, Nn=200000):
    tot = 0
    n = np.arange(-Nn, Nn+1)
    for m in range(-M, M+1):
        t = L.e(float(c[0])*m + float(c[1])*n) / (m*z + n)**2
        if m == 0: t = np.where(n == 0, 0, L.e(float(c[1])*n) / np.where(n == 0, 1, n)**2.0)
        tot += t.sum()
    return complex(tot)
def brute_u(u, z, M=60, Nn=200000):
    tot = -math.pi / z.imag
    n = np.arange(-Nn, Nn+1) + float(u[1])
    for m0 in range(-M, M+1):
        m = m0 + float(u[0])
        if abs(m) < 1e-15:
            nn = n[np.abs(n) > 1e-15]; tot += np.sum(1.0 / nn**2); continue
        tot += np.sum(1.0 / (m*z + n)**2)
    return complex(tot)
z = complex(0.211, 1.07)
for c in [(Fr(1,5),Fr(3,5)), (Fr(1,4),Fr(0)), (Fr(0),Fr(2,7))]:
    print("G_v", c, abs(L.G_v(c, z) - brute_v(c, z)))
for u in [(Fr(1,5),Fr(3,5)), (Fr(0),Fr(1,3)), (Fr(1,4),Fr(0))]:
    print("G_u", u, abs(L.G_u(u, z) - brute_u(u, z)))
z2 = complex(0.3137, 0.09)
for c in [(Fr(1,5),Fr(3,5)), (Fr(1,4),Fr(0))]:
    print("reduce G_v", abs(L.G_v(c, z2) - L.w2_reduced(c, z2, L.G_v, "v")))
    print("reduce G_u", abs(L.G_u(c, z2) - L.w2_reduced(c, z2, L.G_u, "u")), abs(L.G_u(c, z2)))
