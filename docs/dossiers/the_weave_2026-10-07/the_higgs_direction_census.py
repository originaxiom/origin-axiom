#!/usr/bin/env python3
"""W155 — the census over contents, Stage B: the Higgs direction at the forced line (the rule: W155_RULE.md, committed
and pushed before this script).

In Stage A's frame (W154; B1686's units, main's E_cs and S_c read with git show from 22b7d5739 through W154's module),
a bulk mass mu on the fields of a characteristic c = (p1, p2) enters each lattice term through f(x) = x^3 K_3(x) / 8,
x = mu |m + n tau| / sqrt(y).  The Higgs's three copies sit on the parity characteristics at the forced line, so their
lowest modes are twisted, with mass^2 proportional to q_c(tau) = min over (a, b) in Z^2 + c of |a tau - b|^2 / y.

  H0  the copies' twisted masses: positive on the domain; the closed forms; the values at omega and i; the moves
      permute the three (S and T, ten random tau)
  H1  the cusp lemma: (S_c^(mu)(iy)/y^3 - kappa_c) decreases in y and tends to l_c(mu) / y; the record's rows still run
      with masses on every field on a characteristic
  H2  masses that treat the parities alike: (a) the small-mass expansion, (b) the parity sum at s = 2 on a cut and in
      the limit, (d) at finite mass the global minimum at omega, i or the axis (twelve cases)
  H3  the condensate E_cond = -eps (nu - q_min)_+^2: (a) q_min = q_(0,1/2) = 1/(4y) on the domain, ties on the arc and
      at omega; (b) non-increasing in y; (c) added to Stage A's contents: A > 0 runs, A < 0 holds at Im tau >= y*,
      Re tau no better held
  R   read-outs: the held minimum under (nu, eps); the band's t-window under each; the small-mass shift of B

    python3 -B the_higgs_direction_census.py      # writes the_higgs_direction_census.json beside itself
"""
import contextlib
import io
import json
import math
import platform
import sys
import time
from pathlib import Path

import numpy as np
from scipy.special import kv

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_content_census as CC     # noqa: E402  (W154: E_vec, fourier, AB, the grid; main's B1686 module as CC.W)

OUT = HERE / "the_higgs_direction_census.json"
PAR = CC.PAR
CHARS = [(0.0, 0.0)] + PAR
OMEGA = CC.OMEGA
K31 = CC.K31
Z6 = CC.Z6
RNG = np.random.default_rng(155)


# ------------------------------------------------------------------ the massive lattice sums
_LAT = {}


def lattice(M):
    if M not in _LAT:
        m, n = np.meshgrid(np.arange(-M, M + 1), np.arange(-M, M + 1), indexing="ij")
        m, n = m.ravel().astype(float), n.ravel().astype(float)
        nz = (m != 0) | (n != 0)
        _LAT[M] = (m[nz], n[nz])
    return _LAT[M]


def fmass(x):
    """f(x) = x^3 K_3(x) / 8, with f(0) = 1"""
    x = np.asarray(x, float)
    out = np.ones_like(x)
    pos = x > 0
    out[pos] = x[pos] ** 3 * kv(3, x[pos]) / 8
    return out


def sums(tau, mu, M, s=3, minus_massless=False):
    """{c: S_c^(mu)(tau)} for the four characteristics; s = 2 only massless; minus_massless gives S^(mu) - S^(0)"""
    m, n = lattice(M)
    y = tau.imag
    L = np.abs(m + n * tau)
    base = y ** s / L ** (2 * s)
    if mu:
        g = fmass(mu * L / math.sqrt(y))
        base = base * ((g - 1.0) if minus_massless else g)
    elif minus_massless:
        base = base * 0.0
    return {c: float(np.sum(np.cos(2 * np.pi * (m * c[0] + n * c[1])) * base)) for c in CHARS}


def sums_grid(taus, mu, M):
    """the same, s = 3, for an array of tau, in chunks"""
    m, n = lattice(M)
    ph = {c: np.cos(2 * np.pi * (m * c[0] + n * c[1])) for c in CHARS}
    out = {c: np.zeros(len(taus)) for c in CHARS}
    for i0 in range(0, len(taus), 64):
        t = taus[i0:i0 + 64][:, None]
        y = t.imag
        L = np.abs(m[None, :] + n[None, :] * t)
        w = y ** 3 / L ** 6
        if mu:
            w = w * fmass(mu * L / np.sqrt(y))
        for c in CHARS:
            out[c][i0:i0 + 64] = w @ ph[c]
    return out


# ------------------------------------------------------------------ the copies' twisted masses
def q_brute(tau, c, R=6):
    a = np.arange(-R, R + 1) + c[0]
    b = np.arange(-R, R + 1) + c[1]
    A, B = np.meshgrid(a, b, indexing="ij")
    return float(np.min(np.abs(A * tau - B) ** 2) / tau.imag)


def q_closed(tau, c, R=6):
    y = tau.imag
    if c == (0.0, 0.5):
        return 1 / (4 * y)
    if c == (0.5, 0.0):
        return min(abs(tau - 2 * k) ** 2 for k in range(-R, R + 1)) / (4 * y)
    return min(abs(tau - k) ** 2 for k in range(-2 * R - 1, 2 * R + 2, 2)) / (4 * y)


def random_domain(k, ymax=3.0):
    out = []
    while len(out) < k:
        x, y = RNG.uniform(-0.5, 0.5), RNG.uniform(0.87, ymax)
        if x * x + y * y >= 1.0:
            out.append(complex(x, y))
    return out


TAUS = random_domain(10)


def H0():
    ch, rec = {}, {}
    xs = np.arange(-0.5, 0.50001, 0.02)
    ys = np.arange(0.86, 14.00001, 0.02)
    qmin_all = min(q_brute(complex(x, y), c) for x in xs for y in ys if x * x + y * y >= 1 for c in PAR)
    ch["q_c > 0 on the domain grid"] = qmin_all > 0
    rec["least q on the domain grid"] = qmin_all
    err = max(abs(q_brute(t, c) - q_closed(t, c)) for t in TAUS for c in PAR)
    ch["closed forms at ten domain tau (1e-14)"] = err < 1e-14
    rec["closed-form error"] = err
    qo = [q_brute(OMEGA, c) for c in PAR]
    qi = [q_brute(1j, c) for c in PAR]
    ch["omega: all three 1/(2 sqrt 3) (1e-12)"] = max(abs(v - 1 / (2 * math.sqrt(3))) for v in qo) < 1e-12
    ch["i: (1/4, 1/4, 1/2) (1e-12)"] = max(abs(a - b) for a, b in zip(qi, (0.25, 0.25, 0.5))) < 1e-12
    rec["q at omega"], rec["q at i"] = qo, qi
    worst = 0.0
    for t in TAUS:
        base = sorted(q_brute(t, c) for c in PAR)
        for g in (lambda z: z + 1, lambda z: -1 / z):
            worst = max(worst, max(abs(a - b) for a, b in zip(sorted(q_brute(g(t), c) for c in PAR), base)))
    ch["S and T permute the three (multisets, 1e-12)"] = worst < 1e-12
    rec["multiset deviation"] = worst
    return {"checks": ch, "values": rec}, all(ch.values())


# ------------------------------------------------------------------ H1, the cusp lemma
def kappa(c, power):
    return 2 * sum(math.cos(2 * math.pi * k * c[0]) / k ** power for k in range(1, 400))


ROWS = {"matter (45 Weyl in rho_Q)": (0, 0, -90), "+ the Higgs's three copies": (0, 2, -90),
        "+ the 12 gauge fields": (48, 2, -90), "+ the graviton": (57, 2, -90),
        "E8's 248 (w_rho 224)": (220, 108, 224), "E8's 248 (w_rho 448)": (220, 108, 448)}


def V_content(tau, w0, wp, wr, mu, M, S=None):
    """V = -[w0 S_00^(mu) + wp sum_c S_c^(mu) - (31/1024) wr (E3 - E2)], the rho_Q matter massless"""
    if S is None:
        S = sums(tau, mu, M)
    e3, e2 = float(CC.E3(tau.real, tau.imag)), float(CC.E2(tau.real, tau.imag))
    return -(w0 * S[(0.0, 0.0)] + wp * sum(S[c] for c in PAR) - K31 * wr * (e3 - e2))


def H1():
    ys = (20.0, 40.0, 80.0, 160.0, 400.0)
    ch, rec = {}, {}
    ok_dec, ok_lim = True, True
    for c in CHARS:
        k6, k4 = kappa(c, 6), kappa(c, 4) / 2
        for mu in (0.5, 1.0, 3.0):
            dev = [sums(complex(0, y), mu, 80)[c] / y ** 3 - k6 for y in ys]
            ell = -(mu ** 2 / 4) * k4
            dec = all(abs(dev[i + 1]) < abs(dev[i]) for i in range(len(ys) - 1))
            lim = abs(dev[-1] * ys[-1] / ell - 1)
            ok_dec &= dec
            ok_lim &= lim <= 0.10
            rec[f"{c} mu={mu}"] = {"(S/y^3 - kappa) at y": dict(zip(map(str, ys), dev)), "decreasing": dec,
                                   "l_c": ell, "|(S/y^3 - kappa) y / l_c - 1| at 400": lim, "kappa_c": k6}
    ch["|S/y^3 - kappa| decreasing in y, every c and mu"] = ok_dec
    ch["within 10% of l_c/y at y = 400, every c and mu"] = ok_lim
    runs = {}
    ok_runs = True
    for name, (w0, wp, wr) in ROWS.items():
        for mu in (1.0, 3.0):
            vals = [V_content(complex(0, y), w0, wp, wr, mu, 80) for y in ys]
            r = all(vals[i + 1] < vals[i] for i in range(len(ys) - 1))
            ok_runs &= r
            runs[f"{name} mu={mu}"] = {"A": CC.AB(w0, wp, wr)[0], "V on the axis": dict(zip(map(str, ys), vals)),
                                       "runs": r}
    ch["every record row and E8's 248 still run with masses 1 and 3"] = ok_runs
    rec["rows"] = runs
    return {"checks": ch, "values": rec}, all(ch.values())


# ------------------------------------------------------------------ H2, masses that treat the parities alike
def lattice_E(tau, s, M):
    m, n = lattice(M)
    return float(np.sum(tau.imag ** s / np.abs(m + n * tau) ** (2 * s)))


def H2a():
    worst, rows = 0.0, []
    mu = 0.01
    for t in TAUS:
        d = sums(t, mu, 200, minus_massless=True)
        s2 = sums(t, 0.0, 200, s=2)
        r = {str(c): d[c] / (-(mu ** 2 / 8) * s2[c]) for c in CHARS}
        worst = max(worst, max(abs(v - 1) for v in r.values()))
        rows.append({"tau": [t.real, t.imag], "ratios": r})
    return {"worst |ratio - 1|": worst, "rows": rows}, worst <= 0.01


def H2b():
    w_cut, w_lim, rows = 0.0, 0.0, []
    for t in TAUS:
        s2 = sums(t, 0.0, 200, s=2)
        lhs = sum(s2[c] for c in PAR)
        rhs = 0.25 * lattice_E(t, 2, 100) - lattice_E(t, 2, 200)
        lim = -0.75 * CC.W.E_cs(t, 2)
        a, b = abs(lhs - rhs) / abs(rhs), abs(lhs / lim - 1)
        w_cut, w_lim = max(w_cut, a), max(w_lim, b)
        rows.append({"tau": [t.real, t.imag], "sum_c S_c(.,2)": lhs, "cut identity rel": a, "limit rel": b})
    return {"cut identity worst": w_cut, "limit worst": w_lim, "rows": rows}, w_cut < 1e-12 and w_lim < 1e-3


def cases():
    out = []
    for t in (1.5, 3.5, 6.0):
        A = -1.0 / t
        out.append((t, "bosons on the trivial characteristic", 1.0 + A, 0.0))
        out.append((t, "fermions on the parities", 0.0, -(16 / 15) * (1.0 + A)))
    return out


def classify(x, y):
    if abs(complex(x, y) - OMEGA) < 0.05 or abs(complex(x, y) - (OMEGA + 1)) < 0.05:
        return "omega"
    if abs(x) < 1e-9 and abs(y - 1) < 1e-9:
        return "i"
    if abs(x) < 1e-9:
        return "axis"
    return "elsewhere"


def H2d():
    wr = 1024 / 31
    xs = np.round(np.arange(-0.5, 0.50001, 0.05), 4)
    ys = np.round(np.arange(0.85, 6.00001, 0.05), 4)
    pts = [complex(x, y) for x in xs for y in ys if x * x + y * y >= 1 - 1e-12]
    pts += [OMEGA, 1j]
    axis = [complex(0, y) for y in np.round(np.arange(6.05, 14.00001, 0.05), 4)]
    P, Ax = np.array(pts), np.array(axis)
    e3 = CC.E3(P.real, P.imag); e2 = CC.E2(P.real, P.imag)
    e3a = CC.E3(Ax.real, Ax.imag); e2a = CC.E2(Ax.real, Ax.imag)
    res, ok = [], True
    for mu in (1.0, 3.0):
        Sg, Sa = sums_grid(P, mu, 30), sums_grid(Ax, mu, 80)
        for t, kind, w0, wp in cases():
            Vg = -(w0 * Sg[(0.0, 0.0)] + wp * sum(Sg[c] for c in PAR) - K31 * wr * (e3 - e2))
            Va = -(w0 * Sa[(0.0, 0.0)] + wp * sum(Sa[c] for c in PAR) - K31 * wr * (e3a - e2a))
            k = int(np.argmin(Vg))
            best = (float(Vg[k]), P[k].real, P[k].imag)
            ka = int(np.argmin(Va))
            if Va[ka] < best[0]:
                best = (float(Va[ka]), 0.0, Ax[ka].imag)
            where = classify(best[1], best[2])
            ok &= where in ("omega", "i", "axis")
            A, B = CC.AB(w0, wp, wr)
            stA = CC.grid_argmin(A, B)
            res.append({"mu": mu, "t": t, "realization": kind, "w0": w0, "wp": wp, "A": A, "B": B,
                        "minimum": {"V": best[0], "x": best[1], "y": best[2], "where": where},
                        "Stage A at the same (A, B)": {"V": stA[0], "x": stA[1], "y": stA[2]},
                        "top of the axis reached": bool(ka == len(Ax) - 1 and Va[ka] < best[0] + 1e-15)})
    return {"cases": res}, ok


# ------------------------------------------------------------------ H3, the condensate
def qmin(tau):
    return min(q_brute(tau, c) for c in PAR)


def E_cond(q, nu, eps):
    return -eps * np.maximum(nu - q, 0.0) ** 2


def H3():
    ch, rec = {}, {}
    xs, ys = np.round(np.arange(-0.5, 0.50001, 0.02), 4), np.round(np.arange(0.86, 14.00001, 0.02), 4)
    bad_arg, bad_val, n = 0, 0.0, 0
    for x in xs:
        for y in ys:
            if x * x + y * y < 1:
                continue
            t = complex(x, y)
            q = [q_brute(t, c) for c in PAR]
            n += 1
            bad_val = max(bad_val, abs(min(q) - 1 / (4 * y)))
            if abs(t) ** 2 > 1 + 1e-9 and min(abs(t - OMEGA), abs(t - OMEGA - 1)) > 1e-6:
                if not (q[1] < q[0] and q[1] < q[2]):
                    bad_arg += 1
    ties, worst_tie = True, 0.0
    for th in np.linspace(math.pi / 3, 2 * math.pi / 3, 61):
        t = complex(math.cos(th), math.sin(th))
        q = [q_brute(t, c) for c in PAR]
        worst_tie = max(worst_tie, abs(q[0] - q[1]))
        if min(abs(t - OMEGA), abs(t - OMEGA - 1)) > 1e-6:
            ties &= q[2] > q[1] + 1e-12
    q3 = [q_brute(OMEGA, c) for c in PAR]
    ch["(a) q_min = 1/(4y) on the domain grid (1e-12)"] = bad_val < 1e-12
    ch["(a) (0, 1/2) strictly lightest off the arc and omega"] = bad_arg == 0
    ch["(a) tie with (1/2, 0) on the arc, (1/2, 1/2) heavier there except at omega"] = worst_tie < 1e-12 and ties
    ch["(a) three-way tie at omega"] = max(q3) - min(q3) < 1e-12
    rec["(a)"] = {"grid points": n, "worst |q_min - 1/(4y)|": bad_val, "argmin failures": bad_arg,
                  "arc tie worst": worst_tie, "q at omega": q3}
    yax = np.round(np.arange(1.0, 14.00001, 0.01), 4)
    qax = 1 / (4 * yax)
    nonincr = True
    for nu in (0.1, 0.25, 0.5):
        for eps in (0.1, 1.0, 10.0):
            e = E_cond(qax, nu, eps)
            nonincr &= bool(np.all(np.diff(e) <= 1e-15))
    ch["(b) E_cond non-increasing in y on the axis, every (nu, eps)"] = nonincr
    # (c) added to Stage A's contents
    QG = 1 / (4 * CC.GY)            # q_min on W154's grid ((a) checks it equals 1/(4y) on the domain)
    runs_ok, holds_ok, above_ok, rows = True, True, True, []
    for name, (w0, wp, wr) in ROWS.items():
        A, B = CC.AB(w0, wp, wr)
        for nu in (0.1, 0.25, 0.5):
            for eps in (0.1, 1.0, 10.0):
                vals = [float(-(A * CC.E3(0, y) + B * CC.E2(0, y))) + float(E_cond(1 / (4 * y), nu, eps))
                        for y in (8.0, 10.0, 12.0, 14.0)]
                runs_ok &= all(vals[i + 1] < vals[i] for i in range(3))
    for t in (3.5, 4.0):
        A, B = -1.0 / t, 1.0
        stA = CC.grid_argmin(A, B)
        for nu in (0.1, 0.25, 0.5):
            for eps in (0.1, 1.0, 10.0):
                V = -(A * CC.G3 + B * CC.G2) + E_cond(QG, nu, eps)
                k = np.nanargmin(V)
                i, j = np.unravel_index(k, V.shape)
                x, y, v = float(CC.GX[i, j]), float(CC.GY[i, j]), float(V[i, j])
                vo = float(-(A * CC.E3(OMEGA.real, OMEGA.imag) + B * CC.E2(OMEGA.real, OMEGA.imag))
                           + E_cond(1 / (2 * math.sqrt(3)), nu, eps))
                at_omega = vo < v
                held = (not at_omega) and y < 13.99
                holds_ok &= held
                above_ok &= at_omega or y >= stA[2] - 0.01 - 1e-9
                ok_x, rise = CC.x_rises(A, B, y)
                rows.append({"t": t, "nu": nu, "eps": eps, "minimum": {"x": x, "y": y, "V": v},
                             "omega lower": at_omega, "Stage A y*": stA[2], "held": held,
                             "Re tau rises at x = 0.1, 0.25, 0.4, 0.5 (Stage A's, E_cond cancels)": rise})
    ch["(c) A > 0 rows still run with every (nu, eps)"] = runs_ok
    ch["(c) A < 0, B > 0 still held (t = 3.5, 4), every (nu, eps)"] = holds_ok
    ch["(c) the minimum's Im tau at least Stage A's y*"] = above_ok
    rec["(c)"] = rows
    return {"checks": ch, "values": rec}, all(ch.values())


# ------------------------------------------------------------------ the read-outs
def R():
    out = {}
    yax = np.round(np.arange(1.0, 14.00001, 0.002), 4)
    e3, e2 = CC.E3(0 * yax, yax), CC.E2(0 * yax, yax)
    e3o, e2o = float(CC.E3(OMEGA.real, OMEGA.imag)), float(CC.E2(OMEGA.real, OMEGA.imag))
    ts = np.round(np.arange(1.0, 8.00001, 0.005), 4)
    windows = {}
    for nu in (0.0, 0.1, 0.25, 0.5):
        for eps in ((0.0,) if nu == 0.0 else (0.1, 1.0, 10.0)):
            ec = E_cond(1 / (4 * yax), nu, eps)
            eco = float(E_cond(1 / (2 * math.sqrt(3)), nu, eps))
            inband = []
            for t in ts:
                A = -1.0 / t
                V = -(A * e3 + e2) + ec
                k = int(np.argmin(V))
                vo = -(A * e3o + e2o) + eco
                y = float(yax[k]) if V[k] <= vo else float(OMEGA.imag)
                if 2.1 <= y <= 3.2 and V[k] <= vo:
                    inband.append(float(t))
            key = "Stage A (no condensate)" if nu == 0.0 else f"nu={nu} eps={eps}"
            windows[key] = {"t-window": [min(inband), max(inband)] if inband else None,
                            "points": len(inband),
                            "contiguous": bool(inband)
                            and len(inband) == round((max(inband) - min(inband)) / 0.005) + 1}
    out["the band's t-window (B = 1, the axis and omega)"] = windows
    mu, rows = 0.01, []
    for t in TAUS[:5]:
        for w0, wp in ((0.714, 0.0), (0.0, -0.3), (48.0, 2.0)):
            d = sums(t, mu, 200, minus_massless=True)
            s2 = sums(t, 0.0, 200, s=2)
            dV = -(w0 * d[(0.0, 0.0)] + wp * sum(d[c] for c in PAR))
            pred = (mu ** 2 / 8) * (w0 * s2[(0.0, 0.0)] + wp * sum(s2[c] for c in PAR))
            pred_lim = (mu ** 2 / 8) * (w0 - 0.75 * wp) * CC.W.E_cs(t, 2)
            rows.append({"tau": [t.real, t.imag], "w0": w0, "wp": wp, "dV/predicted": dV / pred,
                         "dV/(mu^2/8)(w0 - 3/4 wp)E2": dV / pred_lim})
    out["the small-mass shift of B: B -> B - (mu^2/8)(w0 - (3/4) wp)"] = rows
    return out


def guarded(out, key, fn):
    t0 = time.time()
    try:
        r = fn()
        out[key] = r
    except Exception as exc:                       # a failed part is kept and reported
        import traceback
        out[key] = {"error": repr(exc), "traceback": traceback.format_exc()}
    out.setdefault("part_seconds", {})[key] = round(time.time() - t0, 1)


def main():
    t0 = time.time()
    out = {"arc": "W155", "rule": "W155_RULE.md", "status": "one run", "python": sys.version.split()[0],
           "numpy": np.__version__, "machine": platform.machine(), "main_rev_for_B1686": CC.MAIN,
           "random domain tau": [[t.real, t.imag] for t in TAUS]}
    for key, fn in (("H0", H0), ("H1", H1), ("H2a", H2a), ("H2b", H2b), ("H2d", H2d), ("H3", H3)):
        guarded(out, key, fn)
    guarded(out, "R", R)
    cells = {}
    for key in ("H0", "H1", "H3"):
        cells[key] = isinstance(out[key], (list, tuple)) and bool(out[key][1])
    cells["H2"] = all(isinstance(out[k], (list, tuple)) and bool(out[k][1]) for k in ("H2a", "H2b", "H2d"))
    cells["H2 (a)"] = isinstance(out["H2a"], (list, tuple)) and bool(out["H2a"][1])
    cells["H2 (b)"] = isinstance(out["H2b"], (list, tuple)) and bool(out["H2b"][1])
    cells["H2 (d)"] = isinstance(out["H2d"], (list, tuple)) and bool(out["H2d"][1])
    out["cells holding"] = cells
    out["verdict"] = "every cell as predicted" if all(cells[k] for k in ("H0", "H1", "H2", "H3")) else \
        "a cell failed as worded: " + ", ".join(k for k in ("H0", "H1", "H2", "H3") if not cells[k])
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=float), encoding="utf-8")
    print("W155 written:", OUT.name, "seconds", out["seconds"])
    print("verdict:", out["verdict"])
    print("cells:", cells)


if __name__ == "__main__":
    main()
