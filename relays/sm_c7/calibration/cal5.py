import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
# calibration C9: z0-independence of the u-shifted period; full precision of 4 pi^2 Z0 / P_u(Jc); quadrature convergence;
# the Siegel function: K_c = -2 pi log|g_{Jc}|, and G^(a)* + pi/y against d/dz log g_a
import math, cmath, numpy as np, sm_c7_lib as L
from fractions import Fraction as Fr
def siegel_log(a, z, R=60):
    a1, a2 = float(a[0]) % 1.0, float(a[1])
    q = cmath.exp(2j*math.pi*z)
    v = math.pi*1j*z*L.B2(a1) + cmath.log(1 - cmath.exp(2j*math.pi*(a1*z + a2)))
    for n in range(1, R):
        v += cmath.log(1 - q**n*cmath.exp(2j*math.pi*(a1*z + a2))) + cmath.log(1 - q**n*cmath.exp(-2j*math.pi*(a1*z + a2)))
    return v
geo = L.Geodesic([[7, 4], [5, 3]])
for (i, j, N) in [(1, 2, 8), (3, 6, 8), (2, 4, 8)]:
    c = (Fr(i, N), Fr(j, N)); Jc = (-c[1], c[0])
    z0 = L.Z0_b1737(geo, i, j, N)
    for n in (32, 64, 128):
        t, h = geo.nodes(n)
        P = geo.sigma*h*sum(L.w2_reduced(Jc, geo.z(tt), L.G_u, "u")*geo.dz(tt) for tt in t)
        t2, h2 = geo.nodes(n, t0=0.731)
        P2 = geo.sigma*h2*sum(L.w2_reduced(Jc, geo.z(tt), L.G_u, "u")*geo.dz(tt) for tt in t2)
        print((i, j, N), n, "4pi^2 Z0 - P:", abs(4*math.pi**2*z0 - P), " t0-shift:", abs(P - P2), " P", P)
z = complex(0.13, 1.1)
for a in [(Fr(1, 8), Fr(5, 8)), (Fr(0), Fr(1, 3)), (Fr(2, 5), Fr(0))]:
    c = (a[1], -a[0])                 # so that Jc = (-c2, c1) = a
    k = L.kron(c, z); g = siegel_log(a, z)
    hh = 1e-6
    dlog = (siegel_log(a, z + hh) - siegel_log(a, z - hh)) / (2*hh)
    Gu = L.G_u(a, z)
    print("a", a, " K_c + 2pi log|g_a| =", k + 2*math.pi*g.real, "  (G_u + pi/y)/dlog g =", (Gu + math.pi/z.imag)/dlog)
