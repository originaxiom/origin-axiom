import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
# calibration C1-C3: Fourier E_c(z,s) vs brute lattice sum; Kronecker closed form vs Fourier at s=1; reduction
import math, cmath, random
import numpy as np
import sm_c7_lib as L
random.seed(1)
def brute(c, z, s, R=400):
    m = np.arange(-R, R+1)[:, None]; n = np.arange(-R, R+1)[None, :]
    w = m*z + n
    mask = ~((m == 0) & (n == 0))
    val = np.where(mask, L.e(float(c[0])*m + float(c[1])*n) * z.imag**s / np.where(mask, np.abs(w), 1.0)**(2*s), 0)
    return complex(val.sum())
from fractions import Fraction as Fr
for c in [(Fr(1,5),Fr(3,5)),(Fr(0),Fr(2,5)),(Fr(1,4),Fr(0)),(Fr(1,7),Fr(3,7))]:
    z = complex(random.uniform(-0.5, 0.5), random.uniform(0.9, 1.4))
    f3, b3 = L.E_fourier(c, z, 3), brute(c, z, 3)
    f1, k1 = L.E_fourier(c, z, 1), L.kron(c, z)
    print("c", c, "s=3 fourier-brute", abs(f3 - b3), " s=1 fourier-kron", abs(f1 - k1), " Im f1", abs(f1.imag))
# reduction: E_c at small y directly vs via reduced point
for c in [(Fr(1,5),Fr(3,5)),(Fr(1,7),Fr(3,7)),(Fr(1,4),Fr(0))]:
    z = complex(0.3137, 0.08)
    print("direct-vs-brute s=2 at y=.08", abs(L.E_fourier(c,z,2)-brute(c,z,2,R=500)))
    d = L.E_fourier(c, z, 2); r = L.at_reduced(c, z, lambda cc, w: L.E_fourier(cc, w, 2))
    k = L.kron(c, z); kr = L.at_reduced(c, z, L.kron)
    print("reduce s=2", abs(d - r), " kron reduce", abs(k - kr))
