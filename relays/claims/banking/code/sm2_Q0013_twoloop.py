#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): an independent recomputation for card Q0013 (two-loop terms on the fibre; the stationary points
of V1 + V2 = -alpha E_3 + beta E_2^2 against P-373's bound |V2| <= |V1|/3). numpy, mpmath and the standard library.
Written from the card's definitions only.

    python3 relays/claims/banking/code/sm2_Q0013_twoloop.py            # the card's lines, range and bound
    python3 relays/claims/banking/code/sm2_Q0013_twoloop.py --control  # bound widened to 1, axis to 300 at r = 1e-2

E_s(tau) = sum' (Im tau)^s / (pi^s |m + n tau|^(2s)). Computed by its Fourier expansion
  pi^s E_s = 2 zeta(2s) y^s + 2 sqrt(pi) Gamma(s - 1/2) zeta(2s - 1) / Gamma(s) y^(1-s)
             + 8 pi^s sqrt(y) / Gamma(s) sum_k k^(s-1/2) sigma_(1-2s)(k) K_(s-1/2)(2 pi k y) cos(2 pi k x),
checked against a direct lattice sum. C_111 by a direct lattice sum over p1, p2 in a box (p3 = -p1 - p2), extrapolated in
the box size M with the deficit a log M / M^2 + b / M^2, against E_3 + zeta(3). The span residual of E_2^2 on 1, E_2..E_5. Then, with r = beta/alpha on a dense log
grid (400 values of each sign in [1e-4, 10]), every zero of d/dy(-E_3 + r E_2^2) on Re tau = 0 and 1/2, Im tau in
[1.2, 20], and on the imaginary axis out to 3/r for r = 1e-2, 1e-3, 1e-4, with |V2/V1| = |r| E_2^2 / E_3 at each.
"""
import math, sys
import numpy as np
import mpmath as mp

mp.mp.dps = 25
CONTROL = "--control" in sys.argv
BOUND = 1.0 if CONTROL else 1.0 / 3

def sigma(k, a):
    return sum(mp.mpf(dv) ** a for dv in range(1, k + 1) if k % dv == 0)

KMAX = 12
SIG = {s: [None] + [sigma(k, 1 - 2 * s) for k in range(1, KMAX + 1)] for s in range(2, 6)}

def E(s, x, y, deriv=False):
    """E_s and, with deriv, dE_s/dy, at tau = x + i y"""
    y = mp.mpf(y); nu = s - mp.mpf(1) / 2
    c0 = 2 * mp.zeta(2 * s) / mp.pi ** s
    c1 = 2 * mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) * mp.zeta(2 * s - 1) / (mp.gamma(s) * mp.pi ** s)
    c2 = 8 / mp.gamma(s)
    val = c0 * y ** s + c1 * y ** (1 - s)
    der = c0 * s * y ** (s - 1) + c1 * (1 - s) * y ** (-s)
    for k in range(1, KMAX + 1):
        z = 2 * mp.pi * k * y
        if z > 400: break
        K = mp.besselk(nu, z); cs = mp.cos(2 * mp.pi * k * x)
        w = c2 * k ** nu * SIG[s][k] * cs
        val += w * mp.sqrt(y) * K
        if deriv:
            dK = -(mp.besselk(nu - 1, z) + mp.besselk(nu + 1, z)) / 2
            der += w * (K / (2 * mp.sqrt(y)) + mp.sqrt(y) * 2 * mp.pi * k * dK)
    return (val, der) if deriv else val

def E_lattice(s, x, y, M=400):
    m = np.arange(-M, M + 1, dtype=float)
    mm, nn = np.meshgrid(m, m)
    q = (mm + nn * x) ** 2 + (nn * y) ** 2
    q[M, M] = np.inf
    return float(np.sum(y ** s / (math.pi ** s * q ** s)))

def C111_lattice(x, y, M):
    m = np.arange(-M, M + 1, dtype=float)
    mm, nn = np.meshgrid(m, m); mm = mm.ravel(); nn = nn.ravel()
    keep = ~((mm == 0) & (nn == 0)); mm, nn = mm[keep], nn[keep]
    def w(a, b):
        q = (a + b * x) ** 2 + (b * y) ** 2
        with np.errstate(divide="ignore"):
            return np.where(q == 0, 0.0, (y / math.pi) / q)
    w1 = w(mm, nn)
    tot = 0.0
    for i in range(len(mm)):
        a3, b3 = -mm[i] - mm, -nn[i] - nn
        tot += w1[i] * float(np.sum(w1 * w(a3, b3)))
    return tot

def stationary(x, ys, r, E2, dE2, E3, dE3):
    """zeros of d/dy(-E3 + r E2^2) on the grid ys, refined by bisection; with |V2/V1| at each"""
    g = -dE3 + 2 * r * E2 * dE2
    out = []
    for i in range(len(ys) - 1):
        if g[i] == 0 or g[i] * g[i + 1] < 0:
            a, b = ys[i], ys[i + 1]
            fa = g[i]
            for _ in range(60):
                c = (a + b) / 2
                e2, d2 = E(2, x, c, True); e3, d3 = E(3, x, c, True)
                fc = float(-d3 + 2 * r * e2 * d2)
                if fa * fc <= 0: b = c
                else: a, fa = c, fc
            c = (a + b) / 2
            e2 = float(E(2, x, c)); e3 = float(E(3, x, c))
            out.append((c, abs(r) * e2 * e2 / abs(e3)))
    return out

def tables(x, ys):
    E2 = np.zeros(len(ys)); dE2 = np.zeros(len(ys)); E3 = np.zeros(len(ys)); dE3 = np.zeros(len(ys))
    for i, y in enumerate(ys):
        a, b = E(2, x, y, True); c, d = E(3, x, y, True)
        E2[i], dE2[i], E3[i], dE3[i] = float(a), float(b), float(c), float(d)
    return E2, dE2, E3, dE3

if not CONTROL:
    # 1. the Fourier expansion against a direct lattice sum
    worst = 0.0
    for (x, y) in ((0.0, 1.2), (0.5, 1.5), (0.0, 2.5), (0.5, 1.2)):
        for s in (2, 3, 4, 5):
            f = float(E(s, x, y)); l = E_lattice(s, x, y)
            worst = max(worst, abs(f - l) / abs(f))
    print("E_s by Fourier against the lattice sum (box 400), s = 2..5, four points: worst relative difference %.2e" % worst)
    # 2. C_111 against E_3 + zeta(3)
    cdiff = []
    for (x, y) in ((0.0, 1.2), (0.5, 1.5), (0.0, 2.0)):
        # the box misses the terms with p2 or p3 outside it: for p1 inside, the tail over p2 is O(1/M^2), and the sum of
        # w(p1) over the box grows like log M, so the deficit is a log M / M^2 + b / M^2 (checked: deficit * M^2 grows
        # like log M on boxes 16 to 64)
        Ms = [24, 32, 48, 64, 96]
        vals = [C111_lattice(x, y, M) for M in Ms]
        A = np.array([[1, math.log(M) / M ** 2, 1 / M ** 2] for M in Ms]); coef = np.linalg.lstsq(A, np.array(vals), rcond=None)[0]
        target = float(E(3, x, y) + mp.zeta(3))
        cdiff.append(abs(coef[0] - target))
        print("   C_111 at %.1f + %.1fi: box sums %s, extrapolated %.6f; E_3 + zeta(3) = %.6f"
              % (x, y, ["%.5f" % v for v in vals], coef[0], target))
    print("DECISIVE: C_111 - (E_3 + zeta(3)), worst over three points after extrapolation: %.1e (card's tolerance 2e-3)"
          % max(cdiff))
    # 3. E_2^2 against span(1, E_2..E_5)
    pts = [(x, y) for x in (0.0, 0.5) for y in np.linspace(1.2, 20, 20)]
    rows = []; rhs = []
    for x, y in pts:
        e2 = float(E(2, x, y)); wgt = 1 / (e2 * e2)
        rows.append([wgt] + [float(E(s, x, y)) * wgt for s in (2, 3, 4, 5)]); rhs.append(1.0)
    sol, res, *_ = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)
    rel = float(np.sqrt(np.mean((np.array(rows) @ sol - 1.0) ** 2)))
    print("DECISIVE: E_2^2 on span(1, E_2..E_5), 40 points on the two lines: relative rms residual %.2e" % rel)

# 4. the stationary points
rs = np.concatenate([-np.logspace(-4, 1, 400), np.logspace(-4, 1, 400)])
ys = np.geomspace(1.2, 20, 1500)
found_in, n_points, min_ratio = [], 0, float("inf")
lines = [] if CONTROL else [(0.0, ys), (0.5, ys)]
for x, grid in lines:
    T = tables(x, grid)
    for r in rs:
        for y, q in stationary(x, grid, r, *T):
            n_points += 1; min_ratio = min(min_ratio, q)
            if q <= BOUND: found_in.append((x, r, y, q))
axis = [(1e-2, 300.0)] if CONTROL else [(1e-2, 300.0), (1e-3, 3000.0), (1e-4, 30000.0)]
for r, top in axis:
    grid = np.geomspace(1.2, top, 3000)
    T = tables(0.0, grid)
    for y, q in stationary(0.0, grid, r, *T):
        n_points += 1; min_ratio = min(min_ratio, q)
        print("   axis, r = %g: stationary point at Im tau = %.2f, |V2/V1| = %.4f" % (r, y, q))
        if q <= BOUND: found_in.append((0.0, r, y, q))
print("DECISIVE: stationary points found: %d, over %d values of beta/alpha; smallest |V2/V1| %.4f; bound %.4f"
      % (n_points, len(rs) if not CONTROL else 1, min_ratio, BOUND))
print("DECISIVE: stationary points inside the bound: %d %s" % (len(found_in), found_in[:3]))
ok = not found_in and not CONTROL
if not CONTROL:
    ok = ok and max(cdiff) < 2e-3 and rel > 1e-8
print("RESULT: the card's claim %s" % ("holds" if ok else "does not come out"))
sys.exit(0 if ok else 1)
