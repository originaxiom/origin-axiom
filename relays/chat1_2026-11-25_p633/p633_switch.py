#!/usr/bin/env python3
"""P-633: the weave's switch. The critical c of the weave's sum over threads, data-free, by the transfer operator of
the threads' own coding. Standard library and mpmath; reads no file.

    python3 -I p633_switch.py

The sum. P-633 records main's statement of 2026-10-15: all threads sourcing one field, a critical c = 6 pi h set by
the weave's volume entropy h, as the switch between a thread phase and a surface phase. The normalisation under which
c = 6 pi h is the abscissa is a weight exp(-c l / (6 pi)) per thread of geodesic length l:
    Z(c) = sum over closed threads gamma of exp(-(c / (6 pi)) l(gamma)),
which converges iff c / (6 pi) > delta, the exponent of growth of the threads' number with length. For the modular
surface (curvature -1) and every finite-index subweave of it (a lattice), delta equals the volume entropy h = 1. Below
c = 6 pi the sum is carried by long, surface-filling threads; above it by short ones.

The computation. The threads are coded by the Gauss map's periodic orbits (each closed geodesic of PSL(2, Z) by its
continued-fraction period), with l = 2 sum log(1/x_i) over an even period. Mayer's transfer operator
    (L_s f)(x) = sum over n >= 1 of (x + n)^(-2s) f(1/(x + n))      on [0, 1]
has spectral radius lambda_1(s), and the sum over threads converges iff lambda_1(s) < 1. So the critical exponent is
the s* with lambda_1(s*) = 1, and c* = 6 pi s*. The operator is discretised by collocation at 32 Chebyshev nodes, with
the terms n <= 60 summed and the tail n > 60 taken exactly by Hurwitz zeta values on the interpolant's Taylor
coefficients at 0 (mpmath, 60 digits).

Cells and expectations, written before the run (probabilities are this seat's):
  M1 control: at s = 1, lambda_1 = 1 to 1e-12 (the Gauss measure is invariant), and the second eigenvalue is the
     Gauss-Kuzmin-Wirsing constant -0.3036630028987326586 to 1e-10 (95 %).
  M2 control: d log lambda_1 / ds at s = 1 equals -pi^2 / (6 log 2), minus the Gauss map's Lyapunov exponent, to 1e-6
     (90 %).
  M3 the switch: lambda_1(s) - 1 changes sign once on [0.8, 1.2], at s* within 1e-10 of 1; so c* = 6 pi to that
     precision, 18.849555921538759 (95 %).
The record's sweep (stated in the relay, not computed here): no arc states the switch in c; B1813 and B852 carry the
same transition as the s-family's s = 1, where the cusp tail's rate falls to zero and area lives.
"""
import mpmath as mp

mp.mp.dps = 60
K, M = 32, 60


def nodes():
    return [mp.mpf(1) / 2 * (1 - mp.cos(mp.pi * (2 * j + 1) / (2 * K))) for j in range(K)]


def lagrange_tables(xs):
    """barycentric weights, and each basis polynomial's monomial coefficients (for the tail)."""
    w = []
    for j, xj in enumerate(xs):
        p = mp.mpf(1)
        for k, xk in enumerate(xs):
            if k != j:
                p *= (xj - xk)
        w.append(1 / p)
    V = mp.matrix(K, K)
    for i in range(K):
        for j in range(K):
            V[i, j] = xs[i] ** j
    Vinv = mp.inverse(V)                      # column k of Vinv: the monomial coefficients of the k-th basis polynomial
    return w, Vinv


def basis_at(u, xs, w):
    """the values of the K Lagrange basis polynomials at u (barycentric, second form)."""
    for j, xj in enumerate(xs):
        if u == xj:
            return [mp.mpf(1) if k == j else mp.mpf(0) for k in range(K)]
    t = [w[j] / (u - xs[j]) for j in range(K)]
    s = sum(t)
    return [tj / s for tj in t]


def operator(s, xs, w, Vinv):
    A = mp.matrix(K, K)
    for i, x in enumerate(xs):
        for n in range(1, M + 1):
            u = 1 / (x + n)
            f = (x + n) ** (-2 * s)
            b = basis_at(u, xs, w)
            for k in range(K):
                A[i, k] += f * b[k]
        z = [mp.zeta(2 * s + j, x + M + 1) for j in range(K)]
        for k in range(K):
            A[i, k] += sum(Vinv[j, k] * z[j] for j in range(K))
    return A


def spectrum(s, xs, w, Vinv):
    ev = mp.eig(operator(s, xs, w, Vinv), left=False, right=False)
    ev = sorted(ev, key=lambda e: -abs(e))
    return [mp.re(e) if abs(mp.im(e)) < mp.mpf(10) ** -30 else e for e in ev]


def main():
    xs = nodes()
    w, Vinv = lagrange_tables(xs)
    res = {}
    ev1 = spectrum(mp.mpf(1), xs, w, Vinv)
    gkw = mp.mpf("-0.30366300289873265859744812190155623")
    d1, d2 = abs(ev1[0] - 1), abs(ev1[1] - gkw)
    res["M1"] = d1 < 1e-12 and d2 < 1e-10
    print("M1 s = 1: lambda_1 = %s (|lambda_1 - 1| = %.2e); lambda_2 = %s (|lambda_2 - GKW| = %.2e); lambda_3 = %s"
          % (mp.nstr(ev1[0], 25), float(d1), mp.nstr(ev1[1], 25), float(d2), mp.nstr(ev1[2], 15)))
    h = mp.mpf("1e-8")
    lp = mp.log(spectrum(1 + h, xs, w, Vinv)[0])
    lm = mp.log(spectrum(1 - h, xs, w, Vinv)[0])
    der = (lp - lm) / (2 * h)
    target = -mp.pi ** 2 / (6 * mp.log(2))
    res["M2"] = abs(der - target) < 1e-6
    print("M2 d log lambda_1 / ds at s = 1: %s; -pi^2/(6 log 2) = %s; difference %.2e"
          % (mp.nstr(der, 15), mp.nstr(target, 15), float(abs(der - target))))
    grid = [mp.mpf("0.8") + mp.mpf("0.05") * k for k in range(9)]
    vals = [spectrum(s, xs, w, Vinv)[0] - 1 for s in grid]
    changes = [(grid[k], grid[k + 1]) for k in range(8) if vals[k] * vals[k + 1] < 0]
    print("M3 lambda_1(s) - 1 on s = 0.80, 0.85, ..., 1.20: %s" % ", ".join(mp.nstr(v, 6) for v in vals))
    if len(changes) == 1:
        a, b = changes[0]
        star = mp.findroot(lambda s: spectrum(s, xs, w, Vinv)[0] - 1, (a, b), solver="anderson", tol=mp.mpf(10) ** -40)
    else:
        star = None
    res["M3"] = star is not None and abs(star - 1) < 1e-10
    if star is not None:
        print("M3 one sign change; s* = %s (|s* - 1| = %.2e); c* = 6 pi s* = %s"
              % (mp.nstr(star, 25), float(abs(star - 1)), mp.nstr(6 * mp.pi * star, 20)))
    else:
        print("M3 sign changes: %d" % len(changes))
    print("\n" + ", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in res.items()))


if __name__ == "__main__":
    main()
