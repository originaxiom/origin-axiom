# calibration C17 (outside the population): the frame constant C in c_s = F_u + pi log Im tau + C; E^(u)(z, 2) against a
# brute lattice sum; the shifted Hecke formula at s = 2 on a calibration matrix; the apex finder
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np, b1656_kernel as B, sm_c7_lib as L
from fractions import Fraction as Fr
random.seed(17); Cs = []
for _ in range(5):
    t = complex(random.uniform(-0.5, 0.5), random.uniform(0.8, 1.7)); p1, p2 = random.uniform(.05, .45), random.uniform(.05, .95)
    w = B.line_w(p1, p2, t); x, y = B.sector_twists(w, t, 1, 0); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
    a1 = w.imag / t.imag; a2 = w.real - a1 * t.real
    Cs.append(c["1"] - L.F_shift((a1, a2), t) - math.pi * math.log(t.imag))
print("C =", ["%.10f" % v for v in Cs], " spread %.1e" % (max(Cs) - min(Cs)))
def brute_shift(u, z, s, Rm=500):
    m = np.arange(-Rm, Rm + 1)[:, None] + u[0]; n = np.arange(-Rm, Rm + 1)[None, :] + u[1]
    a = np.abs(m * z + n); return float(np.sum(np.where(a > 1e-12, z.imag ** s / np.where(a > 1e-12, a, 1) ** (2 * s), 0)))
z = complex(0.17, 1.05)
for u in [(0.2, 0.3), (0.0, 0.25), (0.5, 0.0), (1 / 3, 2 / 3)]:
    print("E^(u)(z,2) fourier-brute", u, abs(L.E_shift(u, z, 2) - brute_shift(u, z, 2)))
geo = L.Geodesic([[7, 4], [5, 3]]); M = geo.M
for (i, j, N) in [(3, 6, 12), (1, 2, 8), (6, 0, 12)]:
    c = (Fr(i, N), Fr(j, N)); u = (-c[1], c[0])
    t, h = geo.nodes(48); lhs = h * sum(L.E_shift_reduced(u, geo.z(tt), 2) for tt in t)
    tot = 0.0
    for same in (True, False):
        w = L.cone_vectors(geo, same)[0]
        a, _ = L.shifted_cone_brute(geo, w, M, u, 2); b, _ = L.shifted_cone_brute(geo, w, M, (-u[0], -u[1]), 2)
        tot += a + b
    print("shifted Hecke s=2", (i, j, N), " lhs %.8f  rhs %.8f  rel %.1e" % (lhs, L.H(2) * tot, abs(lhs - L.H(2) * tot) / abs(lhs)))
ts, w, hgt, g = L.apex(geo)
print("apex: t*", ts, " point", w, " height", hgt, " Lagrange/2 = sqrt(D)/(2 min|c|) check:", math.sqrt(geo.D) / 2 / 5)
