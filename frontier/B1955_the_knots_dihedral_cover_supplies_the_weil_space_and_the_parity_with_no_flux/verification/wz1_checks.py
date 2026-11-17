"""Main's two checks of the web seat's W-Z1 (no data): Hecke's period at s = 2 by a direct lattice sum, and the volume."""
import numpy as np, mpmath as mp
mp.mp.dps = 30
phi = (1 + mp.sqrt(5)) / 2; Lper = float(4 * mp.log(phi))
# the full lattice sum G(z, s) = sum over (c, d) != 0 of y^s / |c z + d|^(2s) = 2 zeta(2s) E(z, s), at s = 2
N = 600; c = np.arange(-N, N + 1)[:, None].astype(float); d = np.arange(-N, N + 1)[None, :].astype(float)
def G(z):
    den = (c * z.real + d) ** 2 + (c * z.imag) ** 2; den[N, N] = np.inf
    return (z.imag ** 2 / den ** 2).sum()
ts, ws = np.polynomial.legendre.leggauss(48); ts = Lper / 2 * (ts + 1); ws = ws * Lper / 2
t0 = -Lper / 2
I = sum(w * G(complex(0.5 + (np.sqrt(5) / 2) * np.tanh(t + t0), (np.sqrt(5) / 2) / np.cosh(t + t0))) for t, w in zip(ts, ws))
L5 = mp.nsum(lambda n: mp.kronecker(5, int(n)) / n ** 2, [1, mp.inf]) if hasattr(mp, "kronecker") else None
chi5 = lambda n: (0, 1, -1, -1, 1)[int(n) % 5]
L5 = sum(mp.mpf(chi5(r)) * mp.zeta(2, mp.mpf(r) / 5) for r in range(1, 5)) / 25
rhs = 2 * 5 * mp.gamma(1) ** 2 / mp.gamma(2) * mp.zeta(2) * L5
print("C1 at s = 2: the lattice sum's integral over one period of the act's geodesic (length %.6f): %.6f; 2 * 5^(s/2) Gamma(s/2)^2 / Gamma(s) * zeta(s) L(s, chi_5): %.6f; relative difference %.1e (cut %d)" % (Lper, I, float(rhs), abs(I / float(rhs) - 1), N))
chi3 = lambda n: (0, 1, -1)[int(n) % 3]
L3 = sum(mp.mpf(chi3(r)) * mp.zeta(2, mp.mpf(r) / 3) for r in range(1, 3)) / 9
vol = 12 * mp.mpf(3) ** mp.mpf("1.5") * mp.zeta(2) * L3 / (4 * mp.pi ** 2)
lob = 6 * mp.clsin(2, 2 * mp.pi / 3) / 2
print("C2: 12 * 3^(3/2) zeta_K(2) / (4 pi^2) = %s; 6 * the Lobachevsky function at pi/3 = %s; difference %.1e" % (mp.nstr(vol, 22), mp.nstr(lob, 22), float(abs(vol - lob))))
