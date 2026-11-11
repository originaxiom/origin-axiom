#!/usr/bin/env python3
"""The agy lane's read-out point, recomputed from the closed form of its lowest state, by a route that shares nothing
with the lane's solver.  Data-free: the integers of the field of sqrt 5, one Bessel function, a search for a maximum.

The lane's arc B1881 (branch agy/stage4-sync-2026-11-11, read at b4ddb600b) finds its lowest state by collocation and
says the state is the one that the field of sqrt 5 gives in closed form (Maass 1949), with spectral parameter
R = pi / (2 ln phi), odd under the mirror and under the exchange z -> -1/(5z).  If so, its expansion is

    psi(x + iy) = sum over n of c(n) sqrt(y) K_{iR}(2 pi n y) sin(2 pi n x),
    c(n) = sum over the ideals (alpha) of norm n of sign(N alpha) cos(R ln |alpha / alpha'|),

and nothing of the lane's code is needed to evaluate it.  This script builds c(n) from the integers a + b phi, checks
the expansion against the exchange, and looks for the maximum of psi^2.  None of the lane's code is imported or read.

    python3 -B peak_from_the_closed_form.py

THE SEAT'S EXPECTATIONS, written before the run and committed before it:
  Y0  c(2) = c(3) = 0, c(4) = +1, c(5) = -1, c(11) = -1.113183957920 (the lane's printed values)               90%
  Y1  the expansion is odd under z -> -1/(5z) to 1e-8 at twenty points: the closed form is a state of the
      lane's kind                                                                                             85%
  Y2  on the circle |z|^2 = 1/5 the maximum of psi^2 is at the lane's point 0.2515398 + 0.3697671 i,
      to 1e-5 in each coordinate                                                                              80%
  Y3  over the lane's whole domain (a grid), no value of psi^2 off the circle exceeds the circle's maximum     75%
If Y2 fails, the lane's point is not the peak of the state it names, and this script says where the peak is.
"""
import math
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar

PHI = (1 + math.sqrt(5)) / 2; R = math.pi / (2 * math.log(PHI)); NMAX = 90
LANE = complex(0.251539778829130, 0.369767144294671)
lines = []


def log(x):
    print(x, flush=True); lines.append(x)


# ---- the coefficients, from the integers a + b phi (norm a^2 + ab - b^2), one generator for each ideal
def reduced(a, b):
    """the generator alpha of the ideal (a + b phi) with alpha > 0 and 1 <= |alpha / alpha'| < phi^2"""
    for _ in range(400):
        al, co = a + b * PHI, a + b * (1 - PHI)
        if al < 0: a, b = -a, -b; continue
        t = math.log(abs(al / co))
        if t >= 2 * math.log(PHI) - 1e-12: a, b = b - a, a; continue           # times 1/phi = phi - 1
        if t < -1e-12: a, b = b, a + b; continue                                # times phi
        return a, b
    raise RuntimeError("no reduced generator")


ideals = {}
for a in range(-60, 61):
    for b in range(-60, 61):
        n = abs(a * a + a * b - b * b)
        if 1 <= n <= NMAX: ideals.setdefault(n, set()).add(reduced(a, b))
c = np.zeros(NMAX + 1)
for n, gens in ideals.items():
    for (a, b) in gens:
        al, co = a + b * PHI, a + b * (1 - PHI)
        c[n] += (1 if al * co > 0 else -1) * math.cos(R * math.log(abs(al / co)))
log("R = pi / (2 ln phi) = %.15f; ideals of norm up to %d: %d" % (R, NMAX, sum(len(g) for g in ideals.values())))
log("Y0  c(1..12) = %s" % "  ".join("%.6f" % c[n] for n in range(1, 13)))
y0 = abs(c[1] - 1) < 1e-12 and abs(c[2]) < 1e-12 and abs(c[3]) < 1e-12 and abs(c[4] - 1) < 1e-12 and abs(c[5] + 1) < 1e-12 and abs(c[11] + 1.113183957920) < 1e-9
log("    c(2) = c(3) = 0, c(4) = +1, c(5) = -1, c(11) = %.12f (the lane prints -1.113183957920): %s" % (c[11], "HOLDS" if y0 else "FAILS"))
mult = max(abs(c[m * n] - c[m] * c[n]) for m in range(2, 10) for n in range(2, 10) if math.gcd(m, n) == 1 and m * n <= NMAX)
log("    multiplicative on coprime arguments, greatest gap %.2e" % mult)

# ---- K_{iR}(x) = integral over t of exp(-x cosh t) cos(R t), tabulated and splined as exp(x) K
t = np.linspace(0.0, 9.0, 18001); w = np.full(len(t), t[1] - t[0]); w[0] = w[-1] = (t[1] - t[0]) / 2
xs = np.linspace(0.6, 60.0, 11881)
tab = np.array([np.sum(w * np.exp(-x * (np.cosh(t) - 1.0)) * np.cos(R * t)) for x in xs])          # exp(x) K_{iR}(x)
spl = CubicSpline(xs, tab)


def K(x):
    x = np.asarray(x, dtype=float); return np.where(x < 60.0, spl(np.minimum(x, 60.0)) * np.exp(-np.minimum(x, 60.0)), 0.0)


ns = np.arange(1, NMAX + 1)


def psi(z):
    z = complex(z); x, y = z.real, z.imag
    return float(math.sqrt(y) * np.sum(c[1:] * K(2 * math.pi * ns * y) * np.sin(2 * math.pi * ns * x)))


rng = np.random.default_rng(1881)
pairs = []
while len(pairs) < 20:
    z = complex(rng.uniform(-0.45, 0.45), rng.uniform(0.25, 0.6)); wz = -1.0 / (5.0 * z)
    if wz.imag >= 0.2: pairs.append((z, wz))
scale = max(abs(psi(z)) for z, _ in pairs)
gap = max(abs(psi(wz) + psi(z)) for z, wz in pairs) / scale
y1 = gap < 1e-8
log("Y1  psi(-1/(5z)) + psi(z) at 20 points, as a share of the greatest |psi| among them: %.2e: %s" % (gap, "HOLDS" if y1 else "FAILS"))
if not y1:                                    # a diagnostic only, outside the expectations: the other sign, and the cosine series
    log("    diagnostic: psi(-1/(5z)) - psi(z) gives %.2e" % (max(abs(psi(wz) - psi(z)) for z, wz in pairs) / scale))
    pc = lambda z: float(math.sqrt(z.imag) * np.sum(c[1:] * K(2 * math.pi * ns * z.imag) * np.cos(2 * math.pi * ns * z.real)))
    sc = max(abs(pc(z)) for z, _ in pairs)
    log("    diagnostic: the cosine series gives %.2e (sum) and %.2e (difference)" % (max(abs(pc(wz) + pc(z)) for z, wz in pairs) / sc, max(abs(pc(wz) - pc(z)) for z, wz in pairs) / sc))

# ---- the maximum on the circle, between its two forced zeros
on = lambda th: complex(math.cos(th), math.sin(th)) / math.sqrt(5)
lo, hi = math.atan(0.5), math.pi / 2
grid = np.linspace(lo, hi, 2001); vals = np.array([psi(on(th)) ** 2 for th in grid]); k = int(np.argmax(vals))
best = minimize_scalar(lambda th: -psi(on(th)) ** 2, bounds=(grid[max(k - 2, 0)], grid[min(k + 2, 2000)]), method="bounded", options={"xatol": 1e-12})
zc = on(best.x)
y2 = abs(zc.real - LANE.real) < 1e-5 and abs(zc.imag - LANE.imag) < 1e-5
log("    psi at the two ends of the arc (forced zeros): %.2e and %.2e" % (psi(on(lo)), psi(on(hi))))
log("Y2  the maximum of psi^2 on the circle: at %.7f + %.7f i (angle %.4f degrees); the lane's point %.7f + %.7f i: %s" % (
    zc.real, zc.imag, math.degrees(best.x), LANE.real, LANE.imag, "HOLDS" if y2 else "FAILS"))
second = sorted(vals[(np.abs(grid - best.x) > 0.05)])[-1] if len(vals) else float("nan")
log("    psi^2 there %.6f (not normalised); the greatest value on the circle more than 3 degrees away, as a share of it: %.4f" % (-best.fun, second / -best.fun))

# ---- the whole domain: x in [0, 1/2], above both circles, up to height 1.6
ybot = lambda x: max(math.sqrt(max(0.0, 0.2 - x * x)), math.sqrt(max(0.0, 0.05 - (0.5 - x) ** 2)))
top, where = 0.0, None
for x in np.linspace(0.0, 0.5, 201):
    yb = ybot(x)
    for y in np.linspace(yb + 0.004, 1.6, 400):
        v = psi(complex(x, y)) ** 2
        if v > top: top, where = v, complex(x, y)
y3 = top <= -best.fun * (1 + 1e-9)
log("Y3  the greatest psi^2 on a grid of the domain off the circle: %.6f at %.4f + %.4f i, which is %.4f of the circle's maximum: %s" % (
    top, where.real, where.imag, top / -best.fun, "HOLDS" if y3 else "FAILS"))
log("closed form exit 0")
open(__file__.replace(".py", "_out.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
