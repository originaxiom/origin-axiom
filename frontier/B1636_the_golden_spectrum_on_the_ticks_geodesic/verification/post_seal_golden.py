#!/usr/bin/env python3
"""B1636 post seal -- the mechanism behind G1, written after the sealed run (disclosed in FINDINGS).  G3 read the moduli of
O+ k = 1's entries tracking theta ratios.  Three checks:
 M1  is O+ k = 1 a constant multiple of Z(tau) = [[0, s12 u4, s13 u3], [s12 u4, 0, s23 u2], [s13 u3, s23 u2, 0]] (u_p =
     theta_p^2, s fixed signs)?  The ratios Y_jk / u_l at 8 points of H: their spread.
 M2  if so, the spectrum depends on tau only through F = sum_p |theta_p / eta|^4: Z rephases to the real matrix of the
     |u_l|, whose characteristic polynomial is lambda^3 - P lambda - Q, P = sum |u|^2, Q = 2 |u2 u3 u4| = 8 |eta|^6
     (Jacobi: theta2 theta3 theta4 = 2 eta^3), so P^3 / Q^2 = F^3 / 64 and the golden spectrum (lambda^3 - 2 lambda - 1)
     is F = 8.  Checked: F on the tick's geodesic, and the spectrum against the cubic's at random tau.
 M3  the level set {F = 8}: on 41 vertical lines Re tau in [-1/2, 1/2], every solution y of F(x + iy) = 8 in
     y in [0.3, 3] (by a sign scan and bisection); for each, the smallest |a |tau|^2 + b Re tau + c| over integer
     (a, b, c) with b^2 - 4ac = 5 and |a| <= 6 -- zero means the point lies on a geodesic of discriminant 5 (an image of
     the tick's axis; class number one).  Control: the same test against discriminant 8 (the axis of L^2 R^2) and 12.
Writes post_seal_golden.json."""
import json, pathlib, os, importlib.util, math
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("g", HERE / "golden_on_the_ticks_geodesic.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
c = g.c


def F(t):
    u, eta = c.u_eta(t)
    return sum(abs(x) ** 2 for x in u) / abs(eta) ** 4


def on_disc(t, D, amax=6):
    best = 9e9
    for a in range(-amax, amax + 1):
        for b in range(-30, 31):
            if (b * b - D) % 4 or a == 0: continue
            cc = (b * b - D) // (4 * a) if (b * b - D) % (4 * a) == 0 else None
            if cc is None: continue
            best = min(best, abs(a * abs(t) ** 2 + b * t.real + cc) / max(1, abs(a)))
    return best


def main():
    out = {}
    O1, mons = g.piece(1, "O+"); b1 = O1[0]
    rng = np.random.default_rng(16361)
    pts = [complex(rng.uniform(-0.5, 0.5), rng.uniform(0.7, 2.0)) for _ in range(8)]
    ratios = []
    for t in pts:
        Y = c.evaluate(b1, mons, t, 18); u, _ = c.u_eta(t)
        ratios.append([Y[0, 1] / u[2], Y[0, 2] / u[1], Y[1, 2] / u[0]])
    R = np.array(ratios)
    out["M1"] = {"ratios_at_first_point": [complex(round(z.real, 12), round(z.imag, 12)) for z in R[0]],
                 "max_relative_spread_over_points": float(np.max(np.abs(R - R[0]) / np.abs(R[0]))),
                 "diagonal_max": float(max(np.abs(np.diag(c.evaluate(b1, mons, t, 18))).max() for t in pts))}
    tick = g.axis(g.Lm @ g.Rm, np.linspace(0.3, math.pi - 0.3, 25))
    Fs = [F(t) for t in tick]
    dev = []
    for t in pts:
        f = F(t); P = f; Q = 8.0                        # in units |eta|^4: P = F, Q = 2|u2u3u4|/|eta|^6 = 8
        lam = np.sort(np.abs(np.roots([1, 0, -P, -Q])))[::-1]
        s = g.norm_masses(b1, mons, t)
        dev.append(float(np.max(np.abs(lam / lam[0] - s))))
    out["M2"] = {"F_on_the_tick_min_max": [min(Fs), max(Fs)], "spectrum_vs_cubic_max_deviation": max(dev),
                 "F_at_i": F(1j), "F_at_omega": F(g.c.OMEGA)}
    sols = []
    for x in np.linspace(-0.5, 0.5, 41):
        ys = np.linspace(0.3, 3.0, 271); vals = [F(complex(x, y)) - 8 for y in ys]
        for j in range(len(ys) - 1):
            if vals[j] == 0 or vals[j] * vals[j + 1] < 0:
                lo, hi = ys[j], ys[j + 1]
                for _ in range(50):
                    mid = 0.5 * (lo + hi)
                    if (F(complex(x, lo)) - 8) * (F(complex(x, mid)) - 8) <= 0: hi = mid
                    else: lo = mid
                sols.append(complex(x, 0.5 * (lo + hi)))
    d5 = [on_disc(t, 5) for t in sols]; d8 = [on_disc(t, 8) for t in sols]; d12 = [on_disc(t, 12) for t in sols]
    out["M3"] = {"level_set_points_found": len(sols), "max_distance_to_a_disc5_geodesic": max(d5) if d5 else None,
                 "fraction_within_1e-9_of_disc5": float(np.mean([d < 1e-9 for d in d5])) if d5 else None,
                 "control_disc8_fraction_within_1e-9": float(np.mean([d < 1e-9 for d in d8])) if d8 else None,
                 "control_disc12_fraction_within_1e-9": float(np.mean([d < 1e-9 for d in d12])) if d12 else None,
                 "sample": [[round(t.real, 6), round(t.imag, 9), d] for t, d in list(zip(sols, d5))[:12]]}
    json.dump(out, open(HERE / "post_seal_golden.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str)[:4000])


if __name__ == "__main__":
    main()
