#!/usr/bin/env python3
"""P-632: the linear-stability spectrum on B1813's s-family, with the democratic mode as control. Data-free: nothing
is compared with a measured number, and nothing is read from any file.

    python3 -I p632_modes.py      # writes p632_modes.json beside itself

The family. B1813 (stage 1c) counts threads move by move (every word of n letters L, R with both letters) and weights
each by exp(-s * its geometric length), l_w = 2 arccosh(t_w / 2) = 2 log lambda_w. In the Farey coding (B852) that is
the transfer operator on [0, 1]
    (F_s f)(x) = (1 + x)^(-2s) [ f(x / (1 + x)) + f(1 / (1 + x)) ],
whose two inverse branches are the letters. A density rho evolves by rho -> F_s rho per move. Its linear-stability
spectrum is F_s's spectrum: the fastest-growing mode is the leading eigenfunction h_s, with growth lambda_1(s) per move
(the pressure P_F(s) = log lambda_1(s)); the others decay relative to it. At s = 0 every word weighs the same: h_0 = 1,
the democratic mode (P-471's second sense, equal weight per word), with lambda_1 = 2. At s = 1 the family has its phase
transition (B852, B1813, P-713): F_1 fixes 1/x exactly, the Farey map's infinite invariant density, which is not
integrable at x = 0, the parabolic point. The parabolic point is the cusp: x near 0 is a long run of one letter.

Method. Chebyshev collocation on [0, 1] (B852's method): F_s as a matrix on the values at N Chebyshev-Gauss nodes, by
barycentric interpolation; N = 64, 128 and 256; numpy's dense eigensolver. h_s is evaluated at 2001 points by the same
interpolation, and its mass on [0, 0.05] and on [0, 1] by integrating its Chebyshev interpolant exactly.

The cross-check by words: Z_n(s) = sum over the 2^n - 2 words of n letters with both letters of lambda_w^(-2s), at
n = 17 and 18; Z_18 / Z_17 approaches lambda_1(s).

Cells and expectations, written before the run (probabilities are this seat's):
  M0 instrument: at s = 0, lambda_1 = 2 and h_0 is constant to 1e-12 at N = 64; F_1(1/x) = 1/x at nine points of
     (0, 1] to 1e-14 (99 %).
  M1 the words: Z_18 / Z_17 is within 3 % of lambda_1(s) at s = 0.25 and 0.5 (85 %).
  M2 the fastest mode: for s = 0.1, 0.2, ..., 0.9, h_s (N = 128) is positive on [0, 1] and strictly decreasing at the
     2001 points, with no interior extremum (90 %); lambda_1 at N = 128 and 256 agree to 1e-8 for these s (90 %).
  M3 the marginal mode: lambda_1(s) is strictly decreasing over s = 0, 0.1, ..., 0.9, 0.95, with lambda_1(0.95) < 1.1;
     and h_s's mass fraction on [0, 0.05] is strictly increasing over s = 0, 0.1, ..., 0.9 (90 %).
  Reported, no expectation: lambda_1(0.95) and its mass fraction with the spread over N = 64, 128, 256; the next three
     eigenvalues by modulus at each s and N (the collocation's stand-in for the rest of the spectrum, which on spaces of
     analytic functions is continuous, [0, 1], plus eigenvalues; Prellberg, cited, not re-derived); the sign changes of
     the second eigenfunction at s = 0.5.
Reading, fixed here. If M2 and M3 hold: the fastest-growing mode is positive everywhere (as Ruelle-Perron-Frobenius
requires), is the democratic constant at s = 0 exactly, and charges the whole interval; the marginal mode at s = 1
lives at the parabolic point, the cusp. Neither picks a tau-locus, and on B1813's family the row is NEGATIVE, with the
democratic control reproducing the old circulant frame's negative (the fastest mode is the democratic one) at s = 0.
If M2 fails, the interior extremum of h_s is reported as a candidate; mapping it to tau needs a criterion written
before mapping. The decaying modes are not a selection: they shrink relative to the fastest.
"""
import itertools
import json
import math
import pathlib

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SGRID = [round(0.1 * k, 1) for k in range(10)] + [0.95]


def nodes(n):
    k = np.arange(n)
    return 0.5 * (np.cos(np.pi * (2 * k + 1) / (2 * n)) + 1.0), (-1.0) ** k * np.sin(np.pi * (2 * k + 1) / (2 * n))


def interp_matrix(x, bw, y):
    """rows: barycentric interpolation weights from the nodes x to the points y"""
    y = np.atleast_1d(y)
    out = np.zeros((len(y), len(x)))
    for i, yi in enumerate(y):
        d = yi - x
        hit = np.abs(d) < 1e-15
        if hit.any():
            out[i, np.argmax(hit)] = 1.0
        else:
            w = bw / d
            out[i] = w / w.sum()
    return out


def farey_matrix(s, n):
    x, bw = nodes(n)
    wt = (1.0 + x) ** (-2.0 * s)
    A = interp_matrix(x, bw, x / (1.0 + x)) + interp_matrix(x, bw, 1.0 / (1.0 + x))
    return wt[:, None] * A, x, bw


def spectrum(s, n):
    M, x, bw = farey_matrix(s, n)
    ev, V = np.linalg.eig(M)
    order = np.argsort(-np.abs(ev))
    ev, V = ev[order], V[:, order]
    h = np.real(V[:, 0])
    h = h / h[np.argmin(np.abs(x - 1.0))] if abs(h[np.argmin(np.abs(x - 1.0))]) > 0 else h
    return ev, V, h, x, bw


def cheb_coeffs(vals):
    """Chebyshev coefficients of the interpolant at Chebyshev-Gauss nodes (on [-1, 1] in t = 2x - 1)"""
    n = len(vals)
    k = np.arange(n)
    th = np.pi * (2 * k + 1) / (2 * n)
    c = np.array([2.0 / n * np.sum(vals * np.cos(j * th)) for j in range(n)])
    c[0] /= 2.0
    return c


def integral(c, a, b):
    """integral over x in [a, b] of the Chebyshev series in t = 2x - 1"""
    P = np.polynomial.chebyshev.Chebyshev(c).integ()
    return 0.5 * (P(2 * b - 1) - P(2 * a - 1))


def word_sums(n):
    L = np.array([[1, 1], [0, 1]], dtype=np.float64)
    R = np.array([[1, 0], [1, 1]], dtype=np.float64)
    tr = []
    for w in itertools.product((0, 1), repeat=n):
        if 0 < sum(w) < n:
            M = np.eye(2)
            for ch in w:
                M = M @ (L if ch == 0 else R)
            tr.append(M[0, 0] + M[1, 1])
    t = np.array(tr)
    return (t + np.sqrt(t * t - 4.0)) / 2.0


def main():
    out, res = {}, {}
    # M0
    ev0, V0, h0, x0, _ = spectrum(0.0, 64)
    m0a = abs(ev0[0] - 2.0)
    m0b = float(np.max(np.abs(h0 - 1.0)))
    pts = np.linspace(0.1, 1.0, 9)
    f = lambda y: 1.0 / y
    m0c = float(np.max(np.abs((1 + pts) ** -2 * (f(pts / (1 + pts)) + f(1 / (1 + pts))) - f(pts)) / f(pts)))
    res["M0"] = m0a < 1e-12 and m0b < 1e-12 and m0c < 1e-14
    print("M0: |lambda_1(0) - 2| %.1e, max |h_0 - 1| %.1e; F_1(1/x) = 1/x to %.1e" % (m0a, m0b, m0c), flush=True)
    # the spectrum along s
    lam, frac, mono, pos, conv, rest = {}, {}, {}, {}, {}, {}
    grid = np.linspace(0.0, 1.0, 2001)
    for s in SGRID:
        per_n = {}
        for n in (64, 128, 256):
            ev, V, h, x, bw = spectrum(s, n)
            hv = interp_matrix(x, bw, grid) @ h
            c = cheb_coeffs(h)
            per_n[n] = {"lam": float(np.real(ev[0])), "imag": float(abs(np.imag(ev[0]))),
                        "rest": [[float(np.real(e)), float(np.imag(e))] for e in ev[1:4]],
                        "frac": float(integral(c, 0.0, 0.05) / integral(c, 0.0, 1.0)),
                        "pos": bool(np.all(hv > 0)), "dec": bool(np.all(np.diff(hv) < 0)),
                        "maxdiff": float(np.max(np.diff(hv)))}
            if n == 128 and abs(s - 0.5) < 1e-12:
                v2 = np.real(V[:, 1])
                v2g = interp_matrix(x, bw, grid) @ v2
                zc = grid[:-1][np.sign(v2g[:-1]) != np.sign(v2g[1:])]
                out["second_mode_sign_changes_s0.5"] = [float(z) for z in zc]
        lam[s] = per_n[128]["lam"]
        frac[s] = per_n[128]["frac"]
        pos[s], mono[s] = per_n[128]["pos"], per_n[128]["dec"]
        conv[s] = abs(per_n[128]["lam"] - per_n[256]["lam"])
        rest[s] = per_n
        print("s = %.2f: lambda_1 %.12f (N 64, 128, 256 spread %.1e), mass on [0, 0.05] %.4f (spread %.1e); "
              "h positive %s, strictly decreasing %s; next |lambda| at N = 128: %s" % (
                  s, lam[s], max(abs(per_n[a]["lam"] - per_n[b]["lam"]) for a in per_n for b in per_n), frac[s],
                  max(abs(per_n[a]["frac"] - per_n[b]["frac"]) for a in per_n for b in per_n), pos[s], mono[s],
                  ", ".join("%.4f" % math.hypot(*e) for e in per_n[128]["rest"])), flush=True)
    s_in = [round(0.1 * k, 1) for k in range(1, 10)]
    res["M2"] = all(pos[s] and mono[s] for s in s_in) and all(conv[s] < 1e-8 for s in s_in)
    lam_seq = [lam[s] for s in SGRID]
    frac_seq = [frac[s] for s in SGRID[:-1]]
    res["M3"] = (all(a > b for a, b in zip(lam_seq, lam_seq[1:])) and lam[0.95] < 1.1
                 and all(a < b for a, b in zip(frac_seq, frac_seq[1:])))
    print("M2: h_s positive and strictly decreasing for s = 0.1 .. 0.9: %s; N = 128 vs 256 worst %.1e"
          % (all(pos[s] and mono[s] for s in s_in), max(conv[s] for s in s_in)), flush=True)
    print("M3: lambda_1 strictly decreasing %s, lambda_1(0.95) = %.6f; mass fraction strictly increasing %s" % (
        all(a > b for a, b in zip(lam_seq, lam_seq[1:])), lam[0.95],
        all(a < b for a, b in zip(frac_seq, frac_seq[1:]))), flush=True)
    # M1
    l17, l18 = word_sums(17), word_sums(18)
    m1 = {}
    for s in (0.25, 0.5):
        ev, _, _, _, _ = spectrum(s, 128)
        ratio = float(np.sum(l18 ** (-2 * s)) / np.sum(l17 ** (-2 * s)))
        m1[s] = (ratio, float(np.real(ev[0])), abs(ratio / float(np.real(ev[0])) - 1))
        print("M1 s = %.2f: Z_18 / Z_17 = %.6f, lambda_1 = %.6f, relative difference %.2e" % (s, *m1[s]), flush=True)
    res["M1"] = all(v[2] < 0.03 for v in m1.values())
    print("second eigenfunction at s = 0.5 (N = 128) changes sign at x =",
          ", ".join("%.4f" % z for z in out.get("second_mode_sign_changes_s0.5", [])))
    out.update({"cells": res, "lambda_1": {str(k): v for k, v in lam.items()},
                "mass_fraction_0_0.05": {str(k): v for k, v in frac.items()},
                "per_n": {str(k): {str(n): v for n, v in d.items()} for k, d in rest.items()},
                "M1": {str(k): v for k, v in m1.items()}})
    json.dump(out, open(HERE / "p632_modes.json", "w"), indent=1)
    print()
    print(", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in res.items()))


if __name__ == "__main__":
    main()
