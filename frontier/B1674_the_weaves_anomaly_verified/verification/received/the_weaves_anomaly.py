"""W101, the weave's anomaly: the moves acting on the Standard Model's fermions (rule `W101_RULE.md`, committed first).

WEAVE: the anomaly is a character of the whole group the moves generate (Mp2(Z) through rho), taken over every
dictionary assignment of Q, u^c, d^c, L, e^c, nu^c to T or Tbar (64), none hand-picked.

One run. Its output is committed unread. Run from the repository root:
    python3 docs/dossiers/the_weave_2026-10-07/the_weaves_anomaly.py
"""
import itertools
import json
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 30
HERE = Path(__file__).resolve().parent
OUT = {"what": "W101, the weave's anomaly", "rule": "W101_RULE.md", "status": "one run",
       "precision": "mpmath 30 digits; rho's matrices for C1 in mpmath floating point (exact roots of unity)"}
CELLS = {}

# ------------------------------------------------------------------ C0. the representation
rT_u = np.array([[1j, 0, 0], [0, 0, 1], [0, 1, 0]])                  # on (theta2^2, theta3^2, theta4^2)
rS_u = -1j * np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
rT = np.exp(2j * np.pi * 21 / 24) * rT_u                             # chi_eta(t) = e^{2 pi i / 24}
rS = np.exp(-1j * np.pi / 4) ** 21 * rS_u                             # chi_eta(s) = e^{-i pi / 4}


def closure(gens):
    key = lambda M: tuple(np.round(M, 8).reshape(-1).tolist())
    seen = {key(np.eye(3)): np.eye(3, dtype=complex)}
    front = [np.eye(3, dtype=complex)]
    while front:
        nxt = []
        for g in front:
            for h in gens:
                x = g @ h
                if key(x) not in seen:
                    seen[key(x)] = x
                    nxt.append(x)
        front = nxt
    return list(seen.values())


st = rS @ rT
order = len(closure((rT, rS)))
expo = sorted(Fr(round(float(x) * 24), 24) for x in np.angle(np.linalg.eigvals(rT)) / (2 * np.pi) % 1)
chiT, chiS = np.exp(2j * np.pi / 24), np.exp(-1j * np.pi / 4)
e_t = [k for k in range(24) if abs(np.linalg.det(rT) - chiT ** k) < 1e-12]
e = e_t[0] if len(e_t) == 1 else None
c0 = {
    "s^2 = (st)^3": bool(np.allclose(rS @ rS, np.linalg.matrix_power(st, 3))),
    "s^8 = 1": bool(np.allclose(np.linalg.matrix_power(rS, 8), np.eye(3))),
    "s^4 = -1": bool(np.allclose(np.linalg.matrix_power(rS, 4), -np.eye(3))),
    "image order": order, "t-exponents (turns)": [str(x) for x in expo],
    "e with det rho(t) = chi_eta(t)^e": e_t,
    "det rho(s) = chi_eta(s)^e": bool(e is not None and abs(np.linalg.det(rS) - chiS ** e) < 1e-12)}
OUT["C0 the representation"] = c0
CELLS["C0"] = (c0["s^2 = (st)^3"] and c0["s^8 = 1"] and c0["s^4 = -1"] and order == 96
               and expo == [Fr(1, 8), Fr(3, 8), Fr(7, 8)] and e == 9 and c0["det rho(s) = chi_eta(s)^e"])

# ------------------------------------------------------------------ the modular functions


def th(tau):
    q = mp.exp(1j * mp.pi * tau)
    return mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)


def eta(tau):
    return mp.exp(2j * mp.pi * tau / 24) * mp.qp(mp.exp(2j * mp.pi * tau))


def eis(tau, k, c):
    q = mp.exp(2j * mp.pi * tau)
    return 1 + c * mp.nsum(lambda n: n ** (k - 1) * q ** n / (1 - q ** n), [1, mp.inf])


def E4(tau):
    return eis(tau, 4, 240)


def E6(tau):
    return eis(tau, 6, -504)


def jm1728(tau):
    a, b = E4(tau) ** 3, E6(tau) ** 2
    return 1728 * a / (a - b) - 1728


def detY1(tau):
    t2, t3, t4 = [x ** 2 for x in th(tau)]
    return mp.det(mp.matrix([[0, t4, t3], [t4, 0, t2], [t3, t2, 0]]))


# ------------------------------------------------------------------ C1. the control that fixes every sign

w24 = lambda k: mp.exp(2j * mp.pi * mp.mpf(k) / 24)
RT = mp.matrix([[w24(21) * 1j, 0, 0], [0, 0, w24(21)], [0, w24(21), 0]])
RS = mp.exp(-1j * mp.pi * 21 / 4) * (-1j) * mp.matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
T2, S2 = mp.matrix([[1, 1], [0, 1]]), mp.matrix([[0, -1], [1, 0]])
R2 = mp.matrix([[1, 0], [1, 1]])
assert R2 == S2 * T2 ** -1 * S2 ** -1
GEN = {"t": (T2, RT), "s": (S2, RS), "L": (T2, RT), "R": (R2, RS * RT ** -1 * RS ** -1)}


def word(w):
    M, P = mp.eye(2), mp.eye(3)
    for ch in w:
        A, B = GEN[ch]
        M, P = M * A, P * B
    return M, P


c1, worst = {}, mp.mpf(0)
for w in ["t", "s", "LR", "LLR", "LRLLR"]:
    for inv in (False, True):
        M, P = word(w)
        if inv:
            M, P = M ** -1, P ** -1
        pred = mp.det(P) ** -2
        row = []
        for tau in [mp.mpc(0.137, 1.291), mp.mpc(-0.284, 2.173), mp.mpc(0.41, 0.95)]:
            a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
            meas = detY1((a * tau + b) / (c * tau + d)) / ((c * tau + d) ** 3 * detY1(tau))
            worst = max(worst, abs(meas - pred))
            row.append(mp.nstr(meas, 8))
        c1[w + ("^-1" if inv else "")] = {"det rho^-2": mp.nstr(pred, 8), "measured at three tau": row}
OUT["C1 det Y1(gamma tau) / ((c tau + d)^3 det Y1(tau)) against det rho(gamma)^-2"] = {
    "words": c1, "worst |difference|": mp.nstr(worst, 3)}
CELLS["C1"] = bool(worst < mp.mpf(10) ** -20)

# ------------------------------------------------------------------ A1. the character layer, all 64 assignments
F = ["Q", "u", "d", "L", "e", "nu"]
W = {"SU3": {"Q": 2, "u": 1, "d": 1}, "SU2": {"Q": 3, "L": 1},
     "grav": {"Q": 6, "u": 3, "d": 3, "L": 2, "e": 1, "nu": 1}}
Y2 = {"Q": 6 * Fr(1, 6) ** 2, "u": 3 * Fr(2, 3) ** 2, "d": 3 * Fr(1, 3) ** 2, "L": 2 * Fr(1, 2) ** 2, "e": Fr(1),
      "nu": Fr(0)}
E9 = e if e is not None else 9


def n_of(G, s, with_nu=True):
    return (E9 * sum(W[G].get(f, 0) * s[f] for f in F if with_nu or f != "nu")) % 24


assign = [dict(zip(F, v)) for v in itertools.product((1, -1), repeat=6)]
su3_free = [s for s in assign if n_of("SU3", s) == 0]
pred_su3 = [s for s in assign if s["u"] == s["d"] == -s["Q"]]
su2_vals = sorted({n_of("SU2", s) for s in assign})
grav_free = [s for s in su3_free if n_of("grav", s) == 0]
pred_grav = [s for s in su3_free if s["e"] == s["nu"] == -s["L"]]
no_nu = [dict(zip(F[:5], v), nu=0) for v in itertools.product((1, -1), repeat=5)]
grav_free_no_nu = [s for s in no_nu if (E9 * sum(W["grav"].get(f, 0) * s[f] for f in F[:5])) % 24 == 0]
all_free = [s for s in assign if all(n_of(G, s) == 0 for G in W)]
OUT["A1 the character layer (exponent of chi_eta, mod 24)"] = {
    "SU3 free": len(su3_free), "SU3 free = {s_u = s_d = -s_Q}": su3_free == pred_su3,
    "SU2 values": su2_vals, "grav free among SU3 free": len(grav_free),
    "grav free = {s_e = s_nu = -s_L} among SU3 free": grav_free == pred_grav,
    "grav free without nu^c": len(grav_free_no_nu), "free in SU3, SU2 and grav at once": len(all_free),
    "U(1)_Y^2 read-out, e * sum s dim Y^2, for (all T) and (s_u = s_d = -s_Q, leptons T)": [
        str(E9 * sum(Y2[f] for f in F)),
        str(E9 * (Y2["Q"] - Y2["u"] - Y2["d"] + Y2["L"] + Y2["e"] + Y2["nu"]))]}
CELLS["A1"] = (su3_free == pred_su3 and len(su3_free) == 16 and su2_vals == [6, 12, 18]
               and grav_free == pred_grav and len(grav_free_no_nu) == 0 and len(all_free) == 0)

# ------------------------------------------------------------------ A2. the coupling layer (QCD), weights 0..7
a2, ok2 = {}, True
for sQ, su, sd in itertools.product((1, -1), repeat=3):
    m = (-E9 * (2 * sQ + su + sd)) % 24
    ku_set = [k for k in range(8) if (k % 2 == 1) == (sQ == su)]
    kd_set = [k for k in range(8) if (k % 2 == 1) == (sQ == sd)]
    canc = [(ku, kd) for ku in ku_set for kd in kd_set if (m - 6 * (ku + kd)) % 24 == 0]
    classes = sorted({(ku + kd) % 4 for ku, kd in canc})
    if su == sd == sQ:
        want = [2]
    elif su == sd == -sQ:
        want = [0]
    else:
        want = [1] if (m == 6) else [3]
    ok2 &= classes == want and all(((ku + kd) % 4) in want for ku in ku_set for kd in kd_set
                                   if (m - 6 * (ku + kd)) % 24 == 0)
    a2[f"(sQ, su, sd) = ({sQ}, {su}, {sd})"] = {"m": m, "K mod 4 cancellable": classes,
                                                "cancellable (k_u, k_d)": canc[:12], "count": len(canc)}
OUT["A2 the coupling layer: det(Y_u Y_d)/eta^(6K) of trivial character"] = a2
CELLS["A2"] = bool(ok2)

# ------------------------------------------------------------------ A3. theta-bar on the ruled branch
xs = [mp.mpf(k) / 20 for k in range(11)]
ys = [mp.mpf(90 + 5 * k) / 100 for k in range(33)]
grid = [(x, y) for y in ys for x in xs if x * x + y * y >= 1 and abs(mp.mpc(x, y) - 1j) >= mp.mpf("0.03")]
cache = {}


def vals(x, y):
    k = (mp.nstr(x, 12), mp.nstr(y, 12))
    if k not in cache:
        t = mp.mpc(x, y)
        cache[k] = (eta(t), E6(t), jm1728(t))
    return cache[k]


# A3a: weight 1, all in T, no counterterm
half = [abs(mp.sin(12 * mp.arg(eta(mp.mpc(0.5, y))) - mp.pi / 2)) for y in [0.9, 1.2, 1.5, 2.0, 2.5]]
s_pos = min(mp.sin(12 * mp.arg(vals(x, y)[0])) for x, y in grid if x > 0)
s_axis = max(abs(mp.sin(12 * mp.arg(vals(x, y)[0]))) for x, y in grid if x == 0)
mir = [abs(12 * mp.arg(eta(mp.mpc(-x, y))) + 12 * mp.arg(eta(mp.mpc(x, y))))
       for x, y in [(0.15, 1.2), (0.35, 1.5), (0.45, 0.95)]]
OUT["A3a weight 1, all in T, no counterterm: -12 arg eta (mod pi)"] = {
    "max |sin(12 arg eta - pi/2)| on Re tau = 1/2": mp.nstr(max(half), 3),
    "min sin(12 arg eta) over the grid with x > 0": mp.nstr(s_pos, 6),
    "max |sin(12 arg eta)| on x = 0": mp.nstr(s_axis, 3),
    "mirror |12 arg eta(-x+iy) + 12 arg eta(x+iy)|": [mp.nstr(v, 3) for v in mir]}
CELLS["A3a"] = bool(max(half) < mp.mpf(10) ** -20 and s_pos > 0 and s_axis < mp.mpf(10) ** -20
                    and max(mir) < mp.mpf(10) ** -20)


# A3b: weight 3, all in T, no counterterm (POST HOC: the interior curve was seen before the rule)
def P(x, y):
    et, e6, _ = vals(x, y) if (mp.nstr(x, 12), mp.nstr(y, 12)) in cache else (eta(mp.mpc(x, y)), E6(mp.mpc(x, y)),
                                                                                None)
    return 12 * mp.arg(et) + 2 * mp.arg(e6)


crossings, others = [], 0
for y in ys:
    row = [x for x in xs if x * x + y * y >= 1 and abs(mp.mpc(x, y) - 1j) >= mp.mpf("0.03")]
    for xa, xb in zip(row, row[1:]):
        if mp.sin(P(xa, y)) * mp.sin(P(xb, y)) < 0:
            a, b = xa, xb
            for _ in range(42):
                c = (a + b) / 2
                if mp.sin(P(a, y)) * mp.sin(P(c, y)) <= 0:
                    b = c
                else:
                    a = c
            r = (a + b) / 2
            ph = (P(r, y) + mp.pi / 2) % mp.pi - mp.pi / 2
            branch = "c_u c_d > 0" if abs(mp.cos(P(r, y)) - 1) < mp.mpf("1e-6") else "c_u c_d < 0"
            if r >= mp.mpf("0.05"):
                crossings.append({"x": mp.nstr(r, 10), "y": mp.nstr(y, 4), "|tau|": mp.nstr(abs(mp.mpc(r, y)), 6),
                                  "theta-bar = 0 for": branch, "residual": mp.nstr(ph, 3)})
            else:
                others += 1
OUT["A3b weight 3, all in T, no counterterm (POST HOC): zeros of sin(12 arg eta + 2 arg E6)"] = {
    "crossings with Re tau >= 0.05": crossings, "crossings with Re tau < 0.05 (not reported)": others}

# A3c: with the counterterm
pts = [mp.mpc(0.137, 1.291), mp.mpc(-0.284, 2.173), mp.mpc(0.41, 0.95), mp.mpc(0.05, 1.7), mp.mpc(-0.33, 1.02)]
g1 = [detY1(t) ** 2 / eta(t) ** 12 for t in pts]
g3 = [(eta(t) ** 6 * E6(t)) ** 2 / eta(t) ** 36 / jm1728(t) for t in pts]
g2 = [E6(t) ** 2 / eta(t) ** 24 / jm1728(t) for t in pts]
spread = lambda v: max(abs(z / v[0] - 1) for z in v)
arc = [mp.exp(1j * mp.pi * dg / 180) for dg in (65, 75, 85)]
dist = lambda t: abs(mp.im(jm1728(t))) / abs(jm1728(t))
on_lines = [(x, y) for x, y in grid if x == 0 or x == mp.mpf("0.5")]
off_lines = [(x, y) for x, y in grid if 0 < x < mp.mpf("0.5")]
d_on = max([dist(mp.mpc(x, y)) for x, y in on_lines] + [dist(t) for t in arc])
d_off = min(abs(mp.im(vals(x, y)[2])) / abs(vals(x, y)[2]) for x, y in off_lines)
OUT["A3c with the Dedekind counterterm"] = {
    "weight 1 (all T): det(Y1)^2 / eta^12, spread and value": [mp.nstr(spread(g1), 3), mp.nstr(g1[0], 12)],
    "weight 3 (all T): (eta^6 E6)^2 / eta^36 / (j - 1728), spread": mp.nstr(spread(g3), 3),
    "weight 2 (s_u = s_d = -s_Q): E6^2 / eta^24 / (j - 1728), spread": mp.nstr(spread(g2), 3),
    "max |sin arg(j - 1728)| on x = 0, x = 1/2 and three arc points": mp.nstr(d_on, 3),
    "min |sin arg(j - 1728)| at grid points with 0 < x < 1/2": mp.nstr(d_off, 6)}
CELLS["A3c"] = bool(spread(g1) < mp.mpf(10) ** -20 and abs(g1[0] - 64) < mp.mpf(10) ** -20
                    and spread(g3) < mp.mpf(10) ** -20 and spread(g2) < mp.mpf(10) ** -20
                    and d_on < mp.mpf(10) ** -12 and d_off > mp.mpf(10) ** -12)

# ------------------------------------------------------------------ A4. the verdict
CELLS["A4"] = all(CELLS[k] for k in ["C0", "C1", "A1", "A2", "A3a", "A3c"])
OUT["cells"] = CELLS
OUT["A4 the verdict, as the rule states it if every cell holds"] = (
    "The moves' QCD anomaly vanishes at the level of the character only for s_u = s_d = -s_Q; it is cancellable by a "
    "Dedekind counterterm exactly when the coupling weights satisfy A2's congruence; SU(2)^2 is never free at the "
    "level of the character, and gravity^2 needs nu^c. With the counterterm, theta-bar is constant at weight 1 and "
    "is -arg(j - 1728) at weights 2 and 3. 0 of 19.")
(HERE / "the_weaves_anomaly.json").write_text(json.dumps(OUT, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({"cells": CELLS}, indent=1))
