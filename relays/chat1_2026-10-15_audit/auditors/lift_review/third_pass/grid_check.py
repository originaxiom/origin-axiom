# c~ only: the 20x32 Chebyshev grid of lift_cells.py, built from the closed form (proxy for route A, which agrees to ~1e-12)
import math, numpy as np, mpmath as mp
from numpy.polynomial import chebyshev as Ch
mp.mp.dps = 40
X0, X1, Y0, Y1 = -0.5, 0.5, 0.86, 4.5; NX, NY = 20, 32
def ctil_closed(tau):
    q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag))
    return np.array([float(-4 * mp.pi * mp.log(abs(mp.jtheta(r, 0, q))) - 2 * mp.pi * mp.log(mp.pi / 2)
                           - mp.pi * mp.log(tau.imag)) for r in (2, 4, 3)])
def cnodes(n, a, b):
    x = np.cos(np.pi * (np.arange(n) + 0.5) / n); return 0.5 * (b - a) * x + 0.5 * (b + a), x
xs, ux = cnodes(NX, X0, X1); ys, uy = cnodes(NY, Y0, Y1)
V = np.array([[ctil_closed(complex(x, y)) for y in ys] for x in xs])
Tx, Ty = Ch.chebvander(ux, NX - 1), Ch.chebvander(uy, NY - 1)
A = np.linalg.solve(Tx, V.reshape(NX, -1)).reshape(NX, NY, 3)
CF = np.linalg.solve(Ty, A.transpose(1, 0, 2).reshape(NY, -1)).reshape(NY, NX, 3).transpose(1, 0, 2)
def ctil(T):
    T = np.asarray(T)
    tx = Ch.chebvander((2 * T.real - (X1 + X0)) / (X1 - X0), NX - 1); ty = Ch.chebvander((2 * T.imag - (Y1 + Y0)) / (Y1 - Y0), NY - 1)
    return np.einsum("na,nb,abc->nc", tx, ty, CF)
rng = np.random.default_rng(7); worst = 0.0
pts = [complex(rng.uniform(-.5, .5), 0) for _ in range(200)]
pts = [complex(p.real, rng.uniform(math.sqrt(1 - p.real**2), 4.4)) for p in pts] + [0.5 + 0.8660254037844386j, -0.5 + 4.3875j, 0.5+0.866026j]
for t in pts:
    worst = max(worst, float(np.max(np.abs(ctil(np.array([t]))[0] - ctil_closed(t)))))
print("worst |grid - closed| over", len(pts), "points:", worst)
print("tail coeff magnitudes x, y:", np.max(np.abs(CF[-1, :, :])), np.max(np.abs(CF[:, -1, :])))
