#!/usr/bin/env python3
"""Banking seat V1 (fam1-v1-unset-04), Q0013: an own recomputation, sharing nothing with the producer's code.
E_s(tau) = sum' (Im tau)^s / (pi^s |m + n tau|^(2s)) by its Fourier expansion, with its y-derivative in closed form, and
by a direct lattice sum over a disc with the continuum tail added; C111 by an own lattice sum (a convolution on a box
cutoff, extrapolated in 1/N); E_2^2 against 1, E_2, ..., E_5 on this seat's own points; K4 and K5 on the continuum of
beta/alpha: on a line the stationary condition of -alpha E_3 + beta E_2^2 fixes beta/alpha = r(y) = E_3' / (2 E_2 E_2'),
and there |V_2/V_1| = q(y) = |r(y)| E_2^2 / E_3.
    python3 relays/claims/banking/q0013_own.py                 the decisive run
    python3 relays/claims/banking/q0013_own.py --plant-bound   the failing control: the bound widened to |V_2| <= |V_1|
                                                               and Im tau to [1.2, 300] on Re tau = 0, which must find a
                                                               point inside it
Exit 0 when every value comes out as the card states; 1 otherwise."""
import sys
import numpy as np
from scipy.special import kv, zeta, gamma
from scipy.signal import fftconvolve

ARGS = sys.argv[1:]
if ARGS not in ([], ["--plant-bound"]):
    print("usage: no argument, or --plant-bound"); sys.exit(2)
PLANT = ARGS == ["--plant-bound"]
KMAX = 60


def sigma(k, a):
    return sum(d ** a for d in range(1, k + 1) if k % d == 0)


SIG = {s: np.array([sigma(k, 1 - 2 * s) for k in range(1, KMAX + 1)], dtype=float) for s in (2, 3, 4, 5)}
KS = np.arange(1, KMAX + 1, dtype=float)


def E(s, x, y):
    """E_s and dE_s/dy at tau = x + iy, by the Fourier expansion"""
    nu = s - 0.5
    c0 = 2 * zeta(2 * s) * y ** s
    c1 = 2 * np.sqrt(np.pi) * gamma(s - 0.5) * zeta(2 * s - 1) / gamma(s) * y ** (1 - s)
    z = 2 * np.pi * KS * y
    K = kv(nu, z)
    dK = -0.5 * (kv(nu - 1, z) + kv(nu + 1, z))
    w = KS ** nu * SIG[s] * np.cos(2 * np.pi * KS * x)
    pre = 8 * np.pi ** s / gamma(s)
    f = c0 + c1 + pre * np.sqrt(y) * np.sum(w * K)
    df = (s * c0 / y + (1 - s) * c1 / y
          + pre * np.sum(w * (K / (2 * np.sqrt(y)) + np.sqrt(y) * 2 * np.pi * KS * dK)))
    return f / np.pi ** s, df / np.pi ** s


def E_lattice(s, x, y, R=1500):
    n = np.arange(-int(R / y) - 2, int(R / y) + 3)
    m = np.arange(-R - 2, R + 3)
    M, Nn = np.meshgrid(m, n, indexing="ij")
    r2 = (M + Nn * x) ** 2 + (Nn * y) ** 2
    sel = (r2 > 0) & (r2 <= R * R)
    total = np.sum(1.0 / r2[sel] ** s)
    tail = (2 * np.pi / y) * R ** (2 - 2 * s) / (2 * s - 2)             # the continuum beyond the disc
    return (total + tail) * (y / np.pi) ** s


def C111(x, y, N):
    """sum over p1 + p2 + p3 = 0, all nonzero, of prod (y/pi)/|p_i|^2, with p1 and p2 in the box |m|, |n| <= N"""
    m = np.arange(-N, N + 1)
    M, Nn = np.meshgrid(m, m, indexing="ij")
    r2 = (M + Nn * x) ** 2 + (Nn * y) ** 2
    f = np.where(r2 > 0, (y / np.pi) / np.where(r2 > 0, r2, 1), 0.0)
    g = fftconvolve(f, f)                                               # g(q) = sum f(p1) f(q - p1), q in |.| <= 2N
    m2 = np.arange(-2 * N, 2 * N + 1)
    M2, N2 = np.meshgrid(m2, m2, indexing="ij")
    r22 = (M2 + N2 * x) ** 2 + (N2 * y) ** 2
    f3 = np.where(r22 > 0, (y / np.pi) / np.where(r22 > 0, r22, 1), 0.0)
    return float(np.sum(g * f3))


ok = True
def show(label, got, good):
    global ok
    print("DECISIVE: %s %s" % (label, got))
    if not good:
        ok = False

# K1
pts = [(0.0, 1.0), (-0.5, np.sqrt(3) / 2), (0.2, 1.7), (0.5, 1.3), (0.1, 2.5)]
worst = max(abs(E_lattice(s, x, y) / E(s, x, y)[0] - 1) for s in (2, 3) for x, y in pts)
show("K1 E_2 and E_3, Fourier against a disc lattice sum with its tail, at five points: worst relative difference",
     "%.2e" % worst, worst < 1e-6)
hcheck = max(abs((E(s, x, y + 1e-5)[0] - E(s, x, y - 1e-5)[0]) / 2e-5 - E(s, x, y)[1]) / E(s, x, y)[0]
             for s in (2, 3) for x, y in pts + [(0.0, 5.0), (0.5, 12.0)])
show("the closed-form y-derivative against a central difference, on the scale of E_s (E_s' vanishes at tau = i): worst",
     "%.1e" % hcheck, hcheck < 1e-6)

# K2
for x, y, name in [(0.0, 1.0, "i"), (-0.5, np.sqrt(3) / 2, "omega"), (0.2, 1.7, "0.2 + 1.7i")]:
    Ns = [60, 90, 135, 200]
    vals = [C111(x, y, N) for N in Ns]
    A = np.array([[1, 1 / N, 1 / N ** 2] for N in Ns])
    ext = np.linalg.lstsq(A, np.array(vals), rcond=None)[0][0]
    target = E(3, x, y)[0] + zeta(3)
    show("K2 C111 at tau = %s: box cutoffs %s give %s, extrapolated %.6f; E_3 + zeta(3) = %.6f; difference"
         % (name, Ns, ["%.5f" % v for v in vals], ext, target), "%.2e" % (ext - target), abs(ext - target) < 2e-3)

# K3
rng = np.random.default_rng(20261128)
X = []
while len(X) < 60:
    x, y = rng.uniform(-0.5, 0.5), rng.uniform(0.87, 3.0)
    if x * x + y * y >= 1:
        X.append((x, y))
B = np.array([[1.0] + [E(s, x, y)[0] for s in (2, 3, 4, 5)] for x, y in X])
t = np.array([E(2, x, y)[0] ** 2 for x, y in X])
cf = np.linalg.lstsq(B, t, rcond=None)[0]
res = np.sqrt(np.mean((B @ cf - t) ** 2)) / np.sqrt(np.mean(t ** 2))
show("K3 E_2^2 against {1, E_2, E_3, E_4, E_5} on 60 points of the fundamental domain: relative rms residual",
     "%.3e" % res, res > 1e-8)


def r_and_q(x, ys):
    out = []
    for y in ys:
        e2, d2 = E(2, x, y); e3, d3 = E(3, x, y)
        r = d3 / (2 * e2 * d2)
        out.append((r, abs(r) * e2 * e2 / e3))
    return np.array(out)


def crossings(x, rho, ys):
    rq = r_and_q(x, ys)
    f = rq[:, 0] - rho
    idx = np.where(np.sign(f[:-1]) != np.sign(f[1:]))[0]
    res = []
    for i in idx:
        a, b = ys[i], ys[i + 1]
        for _ in range(60):
            c = 0.5 * (a + b)
            if np.sign(r_and_q(x, [c])[0, 0] - rho) == np.sign(r_and_q(x, [a])[0, 0] - rho):
                a = c
            else:
                b = c
        res.append((0.5 * (a + b), r_and_q(x, [0.5 * (a + b)])[0, 1]))
    return res

# K4
for rho in (1e-2, 1e-3, 1e-4):
    ys = np.geomspace(1.2, 3 / rho, 4000)
    cr = crossings(0.0, rho, ys)
    good = len(cr) == 1 and abs(cr[0][1] - 0.75) < 0.1
    show("K4 Re tau = 0, beta/alpha = %g, Im tau in [1.2, %g]: stationary points at y, |V_2/V_1|" % (rho, 3 / rho),
         [("%.4g" % a, "%.4f" % b) for a, b in cr], good)

# K5, on the continuum of beta/alpha
bound, top = (1.0, 300.0) if PLANT else (1 / 3, 20.0)
for x in (0.0, 0.5):
    ys = np.linspace(1.2, top, 20000)
    rq = r_and_q(x, ys)
    inr = (np.abs(rq[:, 0]) >= 1e-4) & (np.abs(rq[:, 0]) <= 10)
    qmin = float(np.min(rq[inr, 1])) if inr.any() else float("nan")
    inside = bool(np.any(rq[inr, 1] <= bound))
    show("K5 Re tau = %g, Im tau in [1.2, %g], every beta/alpha in +-[1e-4, 10]: r(y) runs over [%.4g, %.4g]; the least "
         "|V_2/V_1| at a stationary point %.4f; any with |V_2| <= |V_1| x %.3g" % (x, top, rq[:, 0].min(), rq[:, 0].max(),
                                                                                 qmin, bound), inside, not inside)
g = np.geomspace(1e-4, 10, 30)
lo, hi = 0.05115, 0.5827
print("not decisive: had beta/alpha been 30 log-spaced values in [1e-4, 10] and their negatives, %d of them fall where "
      "r(y) runs on each line, %d stationary points in all" % (int(np.sum((g >= lo) & (g <= hi))),
                                                            int(np.sum((g >= lo) & (g <= hi))) + int(np.sum((g >= lo) & (g <= 0.5799)))))
print("not decisive: at large y, E_s = 2 zeta(2s) y^s / pi^s + O(y^(1-s)) gives r(y) = 3 c_3 / (4 c_2^2 y) = 1.0231 / y "
      "and |V_2/V_1| = 3/4 exactly, to leading order")
sys.exit(0 if ok else 1)
