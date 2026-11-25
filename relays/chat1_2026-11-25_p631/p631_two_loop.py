#!/usr/bin/env python3
"""P-631: beyond one loop for tau. A data-free inventory of the two-loop vacuum terms of a six-dimensional field theory
on the fibre (R^4 x T^2, the torus of modulus tau and area A), against the one-loop term on record, with the
principle for Im tau sealed before any value of Im tau is read. Standard library, numpy and mpmath; reads no file.

    python3 -I p631_two_loop.py

Notation. E_s(tau) = sum' (y / (pi |m + n tau|^2))^s, y = Im tau (the non-holomorphic Eisenstein series of the
modular-graph literature); C_{1,1,1}(tau) = sum over p1 + p2 + p3 = 0, all p_i != 0 in Z + tau Z, of
prod_i y / (pi |p_i|^2). The one-loop term on record (B1686, B1704, the SM seat's W62 and its census, P-380):
V_1 = -(A E(tau, 3) + B E_twisted(tau, 3)) per unit area^3, every content on record with a positive cusp coefficient,
so V_1 runs to the cusp.

The inventory (the analytic statements; each is checked numerically below):
  S1 the sunset, three massless propagators G(x) = 1/(4 pi^3 |x|^4) joined by cubic vertices (Yukawa or gauge cubic),
     with its three images distinct: by the unique-star relation in six dimensions (weights 2 + 2 + 2 = D),
     int d^6x prod_i |x - x_i|^-4 = pi^3 / (|x_12|^2 |x_13|^2 |x_23|^2), so the term is pi^3 C_{1,1,1}(tau) / A^3 times
     the couplings, and by Zagier's identity C_{1,1,1} = E_3 + zeta(3). Its shape dependence is the one-loop function
     plus a constant. (Terms with two images coinciding are UV-divergent, absorbed into the mass and coupling
     counterterms, and scheme-dependent; not computed.)
  S2 the figure-eight, one quartic vertex (the Higgs quartic, gauge quartics): (G_reg(0))^2 with
     G_reg(0) = sum'_l G(l) proportional to E_2(tau) / A^2, so the term is proportional to E_2^2. Its constant term at
     the cusp is a^2 y^4 + 2ab y + b^2 y^-2 (E_2 = a y^2 + b y^-1 + ...), and no combination of the E_s has a y^1
     term, so E_2^2 lies outside the span of the Eisenstein series: new tau-dependence.
  S3 the cusp regime: with V = -alpha E_3 + beta E_2^2, the leading terms -alpha c3 y^3 + beta c2^2 y^4 are stationary
     at y* = 3 alpha c3 / (4 beta c2^2), where |beta E_2^2 / (alpha E_3)| = 3/4 exactly at leading order, whatever
     beta / alpha is. Each further loop brings a further power of the loop factor times y.
  S4 the couplings' circularity, priced: the two-loop coefficients carry the six-dimensional couplings over the area
     (g^2 / A, y_f^2 / A, lambda / A). None is on record (FL-05: no normalisation of the couplings). Each class is
     one free number unless derived; taken from the frame's own outputs at the same tau (its Yukawas), V(tau) depends
     on tau through them too, a fixed-point problem the record has not posed.

THE PRINCIPLE FOR Im tau, SEALED HERE (P-631, P-373): a two-loop vacuum term selects Im tau only at a stationary point
of V_1 + V_2 on the fibre's modulus at which |V_2| <= |V_1| / 3, so that the next order can be neglected; a stationary
point with |V_2| > |V_1| / 3 is not a selection; a stationary point at i or omega is the symmetry's (every invariant
function is stationary there, P-629's note), not the dynamics'.

Cells and expectations, written before the run (probabilities are this seat's):
  K1 control: E_2 and E_3 from their Fourier expansions agree with direct lattice sums (tail-corrected) to 1e-6 at
     three tau (99 %).
  K2 positive control, S1: the lattice sum C_{1,1,1}, extrapolated in its cutoff as a + (b log R + c) / R^2, agrees
     with E_3 + zeta(3) to 2e-3 at tau = i, omega and 0.2 + 1.7i (90 %).
  K3 S2: the least-squares fit of E_2^2 by {1, E_2, E_3, E_4, E_5} over 40 points of the fundamental domain leaves a
     relative rms residual above 1e-8, against an evaluation precision near 1e-14 (99 %).
  K4 S3: on the imaginary axis, for beta / alpha = 1e-2, 1e-3 and 1e-4 (alpha, beta > 0), V = -alpha E_3 +
     beta E_2^2 has one stationary point with y > 1.2, and |beta E_2^2 / (alpha E_3)| there is within 0.1 of 3/4
     (90 %).
  K5 the principle's check: over beta / alpha in +-[1e-4, 10] (60 values) and the lines Re tau = 0 and 1/2, no
     stationary point of V = -E_3 + (beta / alpha) E_2^2 with Im tau in [1.2, 20] has |V_2| <= |V_1| / 3 (85 %).
     (The sunset alone shifts the one-loop coefficient and adds a constant, so it adds no stationary point.)
"""
import math

import mpmath as mp
import numpy as np

mp.mp.dps = 30
OMEGA = complex(-0.5, math.sqrt(3) / 2)


def eis(s, tau, K=None):
    """E_s(tau) = sum' (y / (pi |m + n tau|^2))^s by its Fourier expansion."""
    s = mp.mpf(s)
    x, y = mp.mpf(tau.real), mp.mpf(tau.imag)
    total = 2 * mp.zeta(2 * s) * y ** s + 2 * mp.sqrt(mp.pi) * mp.gamma(s - 0.5) * mp.zeta(2 * s - 1) / mp.gamma(s) * y ** (1 - s)
    K = K or int(40 / (2 * math.pi * float(y))) + 8
    acc = mp.mpf(0)
    for k in range(1, K + 1):
        sig = sum(mp.mpf(d) ** (1 - 2 * s) for d in range(1, k + 1) if k % d == 0)
        acc += mp.mpf(k) ** (s - 0.5) * sig * mp.besselk(s - 0.5, 2 * mp.pi * k * y) * mp.cos(2 * mp.pi * k * x)
    total += 8 * mp.pi ** s * mp.sqrt(y) / mp.gamma(s) * acc
    return float(total / mp.pi ** s)


def lattice_points(tau, R):
    y = tau.imag
    nmax = int(R / y) + 1
    pts = []
    for n in range(-nmax, nmax + 1):
        mmax = int(R + abs(n * tau.real)) + 1
        for m in range(-mmax, mmax + 1):
            p = m + n * tau
            if 0 < abs(p) <= R:
                pts.append(p)
    return np.array(pts)


def eis_direct(s, tau, R=400.0):
    """the direct sum to |p| <= R, plus the tail by the integral (y/pi)^s * 2 pi / (y (2 s - 2) R^(2s-2))."""
    p = lattice_points(tau, R)
    y = tau.imag
    head = np.sum((y / (math.pi * np.abs(p) ** 2)) ** s)
    tail = (y / math.pi) ** s * 2 * math.pi / (y * (2 * s - 2) * R ** (2 * s - 2))
    return head + tail


def c111_cut(tau, R):
    p = lattice_points(tau, R)
    y = tau.imag
    f = y / (math.pi * np.abs(p) ** 2)
    total = 0.0
    for start in range(0, len(p), 2000):
        q = p[start:start + 2000, None] + p[None, :]
        aq = np.abs(q)
        good = aq > 1e-9
        g = np.where(good, y / (math.pi * np.where(good, aq, 1.0) ** 2), 0.0)
        total += float(np.sum(f[start:start + 2000, None] * f[None, :] * g))
    return total


def c111(tau, Rs=(20.0, 28.0, 40.0, 56.0)):
    vals = [c111_cut(tau, R) for R in Rs]
    A = np.array([[1.0, math.log(R) / R ** 2, 1 / R ** 2] for R in Rs])
    coef, res, *_ = np.linalg.lstsq(A, np.array(vals), rcond=None)
    return coef[0], vals


def stationary_points(fun, ys):
    """sign changes of a numerical derivative along the samples ys."""
    v = np.array([fun(y) for y in ys])
    d = np.gradient(v, ys)
    out = []
    for i in range(len(ys) - 1):
        if d[i] == 0 or d[i] * d[i + 1] < 0:
            out.append(0.5 * (ys[i] + ys[i + 1]))
    return out


def main():
    res = {}
    # K1
    worst = 0.0
    for tau in (1j, OMEGA + 0j, complex(0.2, 1.7)):
        for s in (2, 3):
            a, b = eis(s, tau), eis_direct(s, tau)
            worst = max(worst, abs(a - b) / abs(a))
            print("K1 E_%d(%s): Fourier %.10f, lattice %.10f" % (s, tau, a, b))
    res["K1"] = worst < 1e-6
    print("K1 worst relative difference %.2e" % worst)
    # K2
    worst = 0.0
    for tau in (1j, OMEGA + 0j, complex(0.2, 1.7)):
        ext, vals = c111(tau)
        target = eis(3, tau) + float(mp.zeta(3))
        worst = max(worst, abs(ext - target))
        print("K2 C111(%s): cutoffs %s, extrapolated %.6f; E_3 + zeta(3) = %.6f; difference %.2e"
              % (tau, ["%.6f" % v for v in vals], ext, target, ext - target))
    res["K2"] = worst < 2e-3
    # K3
    rng = np.random.default_rng(20261125)
    taus = []
    while len(taus) < 40:
        t = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.87, 3.0))
        if abs(t) >= 1:
            taus.append(t)
    M = np.array([[1.0] + [eis(s, t) for s in (2, 3, 4, 5)] for t in taus])
    target = np.array([eis(2, t) ** 2 for t in taus])
    coef, *_ = np.linalg.lstsq(M, target, rcond=None)
    rel = math.sqrt(np.mean((target - M @ coef) ** 2)) / math.sqrt(np.mean(target ** 2))
    res["K3"] = rel > 1e-8
    print("K3 E_2^2 fitted by {1, E_2, E_3, E_4, E_5} on 40 points: relative rms residual %.3e" % rel)
    # K4
    k4 = True
    for r in (1e-2, 1e-3, 1e-4):
        fun = lambda y: -eis(3, complex(0, y)) + r * eis(2, complex(0, y)) ** 2
        grid = np.geomspace(1.2, 3.0 / r, 400)
        st = stationary_points(fun, grid)
        ratios = [r * eis(2, complex(0, y)) ** 2 / eis(3, complex(0, y)) for y in st]
        print("K4 beta/alpha = %g: stationary points at y = %s; |V_2/V_1| there %s"
              % (r, ["%.4g" % y for y in st], ["%.4f" % q for q in ratios]))
        k4 &= len(st) == 1 and abs(ratios[0] - 0.75) < 0.1
    res["K4"] = k4
    # K5
    k5 = True
    found = 0
    for sign in (1, -1):
        for r in np.geomspace(1e-4, 10, 30):
            for x in (0.0, 0.5):
                fun = lambda y: -eis(3, complex(x, y)) + sign * r * eis(2, complex(x, y)) ** 2
                grid = np.geomspace(1.2, 20.0, 300)
                for y in stationary_points(fun, grid):
                    t = complex(x, y)
                    q = abs(sign * r * eis(2, t) ** 2 / eis(3, t))
                    found += 1
                    if q <= 1 / 3:
                        k5 = False
                        print("K5 a stationary point inside the principle: beta/alpha %+g, tau %s, |V_2/V_1| %.4f"
                              % (sign * r, t, q))
    res["K5"] = k5
    print("K5 stationary points with Im tau in [1.2, 20] found: %d; any with |V_2| <= |V_1|/3: %s" % (found, not k5))
    print("\n" + ", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in res.items()))


if __name__ == "__main__":
    main()
