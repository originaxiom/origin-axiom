#!/usr/bin/env python3
"""W177 — the frame's kernel norms in closed form (the rule: W177_RULE.md, committed and pushed before this script).

The kernels K_s(z) = e^{2 pi i A z} theta_s(z + ub) theta_1'(0) / (theta_s(ub) theta_1(z)) of W89 (A = Im ub / Im tau,
ub reduced to the centred cell, theta_s with argument pi z and nome e^{i pi tau}), and their regularised norms
c_s = lim [int_{cell - B_eps} |K_s|^2 + 2 pi ln eps], by the rule's closed series:

  c_s = -2 pi ln 2 pi - 2 pi gamma - pi [psi(l+) + psi(l-)] + pi (S+ + S-),

  N0  F(z, w) = theta_1'(0) theta_1(z + w) / (theta_1(z) theta_1(w)) = -2 pi i sum_n X^n / (1 - W Q^n), 200 points
  N1  K_s(z) = e^{2 pi i lambda_s z} F(z, w_s), all four s, 200 points
  N2  the series against W89's quadrature (`norm`, unchanged), within 1e-7, y in {2, 4, 6}
  N3  the remainder after c-infinity and the leading correction, within 10 max(e^{-4 pi y l+}/l+, e^{-4 pi y l-}/l-)
  N4  ub = 0, s = 2, 3, 4: the series against W87's -2 pi ln((pi/2) |theta_s(0)|^2), to 1e-25

    python3 -B docs/dossiers/the_weave_2026-10-07/the_twisted_norms_closed.py

The quadrature route is W89's `norm`, unchanged, with the theta series the record runs it with above Im tau 3: W162's
theta_series (its third launch's fix, 12 terms, each term exponentiated whole), installed as W89's np_theta exactly as
W162's and W174's workers install it.  W89's own 40-term default returns NaN there (a nome power that underflows to 0
times a sine that overflows to inf): checked data-free before this commit at Im tau = 4 and 6 with Im z = 3, and
disclosed.  A non-finite quadrature value is counted, not dropped, and fails N2.

The grid's skips (theta_s(ub) = 0, the record's cut |R_s| <= 1e-12 in every sector whose ub is sign * 3w) apply to N2
and N3 alike and are counted.  Warnings are recorded, not raised.
"""
import contextlib
import io
import json
import math
import platform
import random
import sys
import time
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_electrons_zero_checked as W89      # noqa: E402  (W89: the quadrature route, `norm`, unchanged)
    import the_census_window as W162              # noqa: E402  (W162: the theta series W174 runs W89 with)
W89.np_theta = W162.theta_series
mp.mp.dps = 40
OUT = HERE / "the_twisted_norms_closed.json"
SEED = 1770177
TOL_ID, TOL_QUAD, TOL_W87 = mp.mpf("1e-25"), 1e-7, mp.mpf("1e-25")
ZERO, CUT = mp.mpf("1e-25"), mp.mpf("1e-12")
TABLE = {1: (mp.mpf(0), 0, 0), 2: (mp.mpf("0.5"), 0, 0), 3: (mp.mpf("0.5"), 1, 1), 4: (mp.mpf(0), 1, 1)}
# s -> (real shift of w, coefficient of tau/2 in w, sigma)
SECTORS = {"up": (-3, 5), "down": (3, -1), "leptons": (3, -9)}      # (q_L + q_R, q_L - q_R) per sector (W93)
LINES = [(Fr(2, 5), Fr(k, 10)) for k in range(10)] + [(Fr(2, 11), Fr(k, 11)) for k in range(11) if k != 9]
XS = (Fr(1, 8), Fr(3, 8))
Y2 = (2, 4, 6)
Y3 = (4, 6, 8, 12, 16, 24)


# ----------------------------------------------------------------------------------------------- thetas
def q_of(tau):
    return mp.exp(1j * mp.pi * tau)


def theta(s, z, tau):
    return mp.jtheta(s, mp.pi * z, q_of(tau))


def th1p(tau):
    return mp.pi * mp.jtheta(1, 0, q_of(tau), 1)


def F_direct(z, w, tau):
    return th1p(tau) * theta(1, z + w, tau) / (theta(1, z, tau) * theta(1, w, tau))


def F_series(z, w, tau):
    X, W, Q = mp.exp(2j * mp.pi * z), mp.exp(2j * mp.pi * w), mp.exp(2j * mp.pi * tau)
    tot, n = mp.mpc(0), 0
    while True:
        a = X ** n / (1 - W * Q ** n)
        b = X ** (-n - 1) / (1 - W * Q ** (-n - 1))
        tot += a + b
        if n > 8 and abs(a) + abs(b) < mp.mpf(10) ** (-mp.mp.dps - 5) * (1 + abs(tot)):
            break
        n += 1
        if n > 4000:
            raise RuntimeError("F series did not converge")
    return -2j * mp.pi * tot


def reduce(ub, tau):
    beta = mp.im(ub) / mp.im(tau)
    alpha = mp.re(ub) - beta * mp.re(tau)
    return (alpha - mp.nint(alpha)) + (beta - mp.nint(beta)) * tau


def K_direct(s, z, ub, tau):
    ub = reduce(ub, tau)
    A = mp.im(ub) / mp.im(tau)
    return mp.exp(2j * mp.pi * A * z) * theta(s, z + ub, tau) * th1p(tau) / (theta(s, ub, tau) * theta(1, z, tau))


def lam_w(s, ub, tau):
    ub = reduce(ub, tau)
    A = mp.im(ub) / mp.im(tau)
    re_shift, half_tau, sigma = TABLE[s]
    return A + mp.mpf(sigma) / 2, ub + re_shift + half_tau * tau / 2


def K_twisted(s, z, ub, tau):
    lam, w = lam_w(s, ub, tau)
    return mp.exp(2j * mp.pi * lam * z) * F_series(z, w, tau)


# ----------------------------------------------------------------------------------------------- the closed series
def side_sum(lam, W, Q, y, skip_zero):
    """S for (lambda, W): sum over n of (|1 - W Q^n|^-2 - [n + lambda > 0]) / (n + lambda), n + lambda = 0 excluded"""
    N = int(mp.ceil((mp.mp.dps + 8) * mp.log(10) / (2 * mp.pi * y))) + int(abs(lam)) + 4
    tot = mp.mpf(0)
    for n in range(-N, N + 1):
        mu = n + lam
        if abs(mu) < mp.mpf(10) ** -30:
            if skip_zero:
                continue
        D = abs(1 - W * Q ** n) ** 2
        tot += (1 / D - (1 if mu > 0 else 0)) / mu
    return tot


def c_series(s, ub, tau, parts=False):
    lam, w = lam_w(s, ub, tau)
    y = mp.im(tau)
    W, Q = mp.exp(2j * mp.pi * w), mp.exp(2j * mp.pi * tau)
    integer = abs(lam - mp.nint(lam)) < mp.mpf(10) ** -30
    base = -2 * mp.pi * mp.log(2 * mp.pi) - 2 * mp.pi * mp.euler
    if integer:
        l0 = int(mp.nint(lam))
        lp = lm = mp.mpf(1)
        extra = 4 * mp.pi ** 2 * y / abs(1 - W * Q ** (-l0)) ** 2
    else:
        lp = lam - mp.floor(lam)
        lm = 1 - lp
        extra = mp.mpf(0)
    Sp = side_sum(lam, W, Q, y, integer)
    Sm = side_sum(-lam, 1 / W, Q, y, integer)
    c = base - mp.pi * (mp.digamma(lp) + mp.digamma(lm)) + mp.pi * (Sp + Sm) + extra
    if not parts:
        return c
    cinf = base - mp.pi * (mp.digamma(lp) + mp.digamma(lm))
    n0 = int(mp.floor(-lam)) + 1
    m0 = int(mp.floor(lam)) + 1
    lead = 2 * mp.pi * (mp.re(W * Q ** n0) / lp + mp.re(Q ** m0 / W) / lm)
    return c, cinf, lead, lp, lm


# ----------------------------------------------------------------------------------------------- the cells
def rand_point(rng):
    y = rng.uniform(0.8, 6.0)
    tau = mp.mpc(rng.uniform(-0.5, 0.5), y)
    z = mp.mpc(rng.uniform(0, 1), rng.uniform(0.05, 0.95) * y)
    w = mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(-0.45, 0.45) * y)
    return tau, z, w


def N0(rng):
    worst = mp.mpf(0)
    for _ in range(200):
        tau, z, w = rand_point(rng)
        a, b = F_direct(z, w, tau), F_series(z, w, tau)
        worst = max(worst, abs(a - b) / (1 + abs(a)))
    return {"points": 200, "worst relative difference": mp.nstr(worst, 5), "holds": bool(worst <= TOL_ID)}


def N1(rng):
    worst, per = mp.mpf(0), {}
    for _ in range(200):
        tau, z, ub = rand_point(rng)
        for s in (1, 2, 3, 4):
            a, b = K_direct(s, z, ub, tau), K_twisted(s, z, ub, tau)
            d = abs(a - b) / (1 + abs(a))
            per[s] = max(per.get(s, mp.mpf(0)), d)
            worst = max(worst, d)
    return {"points": 200, "worst relative difference": mp.nstr(worst, 5),
            "per s": {str(k): mp.nstr(v, 5) for k, v in per.items()}, "holds": bool(worst <= TOL_ID)}


def residue_cut(line, sign, s, tau):
    """True when the record's cut |R_s| <= 1e-12 applies in every sector whose ub is sign * 3w"""
    a, b = line
    w = a * tau + b
    out = []
    for name, (ku, kd) in SECTORS.items():
        if (ku > 0) != (sign > 0):
            continue
        A, D = ku * a, kd * a
        kap = mp.exp(-mp.pi * (A * A + D * D) * mp.im(tau)) / abs(th1p(tau))
        R = kap * abs(theta(s, ku * w, tau)) * abs(theta(s, kd * w, tau))
        out.append(R <= CUT)
    return all(out)


def grid(ys):
    """the rule's grid: (line, sign, s, x, y, tau, ub), with the skipped points counted"""
    pts, skipped = [], {"theta zero": 0, "residue cut": 0}
    for line in LINES:
        for sign in (1, -1):
            for s in (1, 2, 3, 4):
                for x in XS:
                    for y in ys:
                        tau = mp.mpc(mp.mpf(x.numerator) / x.denominator, y)
                        w = mp.mpf(line[0].numerator) / line[0].denominator * tau + \
                            mp.mpf(line[1].numerator) / line[1].denominator
                        ub = sign * 3 * w
                        if abs(theta(s, reduce(ub, tau), tau)) < ZERO:
                            skipped["theta zero"] += 1
                        elif residue_cut(line, sign, s, tau):
                            skipped["residue cut"] += 1
                        else:
                            pts.append((line, sign, s, x, y, tau, ub))
    return pts, skipped


def N2():
    pts, skipped = grid(Y2)
    rows, worst, nonfinite, t_series, t_quad = [], 0.0, 0, 0.0, 0.0
    by_y, by_min = {}, {}
    for line, sign, s, x, y, tau, ub in pts:
        t0 = time.time()
        cs, cinf, lead, lp, lm = c_series(s, ub, tau, parts=True)
        t1 = time.time()
        cq = W89.norm(s, complex(tau), complex(ub))
        t2 = time.time()
        t_series += t1 - t0
        t_quad += t2 - t1
        if not math.isfinite(cq):
            nonfinite += 1
            d = None
        else:
            d = abs(float(cs) - cq)
            worst = max(worst, d)
            km = mp.nstr(min(lp, lm), 6)
            by_y[y] = max(by_y.get(y, 0.0), d)
            by_min[km] = max(by_min.get(km, 0.0), d)
        rows.append([f"{line[0]},{line[1]}", sign, s, str(x), y, mp.nstr(cs, 15), repr(cq), d, mp.nstr(cinf, 15),
                     mp.nstr(lp, 8), mp.nstr(lm, 8), mp.nstr(lead, 8)])
    n = len(pts)
    return {"points": n, "skipped": skipped, "non-finite quadrature": nonfinite,
            "worst |series - quadrature|": worst,
            "worst by y": {str(k): v for k, v in sorted(by_y.items())},
            "worst by min(l+, l-)": dict(sorted(by_min.items())),
            "seconds per norm": {"series": t_series / max(n, 1), "quadrature": t_quad / max(n, 1)},
            "row columns": ["line", "sign", "s", "Re tau", "Im tau", "c series", "c quadrature", "difference",
                            "c infinity", "l+", "l-", "leading correction"],
            "holds": bool(n > 0 and nonfinite == 0 and worst <= TOL_QUAD), "rows": rows}


def N3():
    pts, skipped = grid(Y3)
    rows, fails = [], []
    for line, sign, s, x, y, tau, ub in pts:
        c, cinf, lead, lp, lm = c_series(s, ub, tau, parts=True)
        rem = abs(c - cinf - lead)
        bound = 10 * max(mp.exp(-4 * mp.pi * y * lp) / lp, mp.exp(-4 * mp.pi * y * lm) / lm)
        ok = rem <= bound
        row = [f"{line[0]},{line[1]}", sign, s, str(x), y, mp.nstr(c, 15), mp.nstr(cinf, 15),
               mp.nstr(lead, 8), mp.nstr(rem, 5), mp.nstr(bound, 5), mp.nstr(lp, 8), bool(ok)]
        rows.append(row)
        if not ok:
            fails.append(row)
    return {"points": len(pts), "skipped": skipped, "fails": fails[:50], "fail count": len(fails),
            "row columns": ["line", "sign", "s", "Re tau", "Im tau", "c", "c infinity", "leading correction",
                            "remainder", "bound", "l+", "within"],
            "holds": bool(pts) and not fails, "rows": rows}


def N4():
    worst, rows = mp.mpf(0), []
    for s in (2, 3, 4):
        for y in (1, 2, 4, 8):
            for x in (Fr(0), Fr(1, 8), Fr(3, 8)):
                tau = mp.mpc(mp.mpf(x.numerator) / x.denominator, y)
                cs = c_series(s, mp.mpc(0), tau)
                c87 = -2 * mp.pi * mp.log((mp.pi / 2) * abs(theta(s, 0, tau)) ** 2)
                d = abs(cs - c87)
                worst = max(worst, d)
                rows.append([s, y, str(x), mp.nstr(cs, 20), mp.nstr(c87, 20), mp.nstr(d, 5)])
    return {"worst |series - W87|": mp.nstr(worst, 5), "rows": rows, "holds": bool(worst <= TOL_W87)}


def main():
    t0 = time.time()
    rng = random.Random(SEED)
    cells = {}
    out = {"arc": "W177", "rule": "W177_RULE.md", "dps": mp.mp.dps, "seed": SEED,
           "python": platform.python_version(), "mpmath": mp.__version__, "numpy": np.__version__}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        out["N0 the expansion"] = N0(rng)
        out["N1 the kernels"] = N1(rng)
        out["N2 two routes"] = N2()
        out["N3 the first correction"] = N3()
        out["N4 W87's closed form"] = N4()
    out["warnings"] = sorted({f"{w.category.__name__}: {w.message}" for w in caught})
    for k in ("N0", "N1", "N2", "N3", "N4"):
        key = next(x for x in out if x.startswith(k + " "))
        cells[k] = bool(out[key]["holds"])
    out["cells"] = cells
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("written", OUT.name, "in", out["seconds"], "s;", len(out["warnings"]), "distinct warnings")


if __name__ == "__main__":
    main()
