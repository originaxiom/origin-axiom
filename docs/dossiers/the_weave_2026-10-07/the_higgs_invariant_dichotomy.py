#!/usr/bin/env python3
"""W146 — P-357 data-free first: what can fix the Higgs's invariant I = |h.h| / |h|^2? A dichotomy for every
holomorphic or antiholomorphic Higgs in the frame's representation, the nine's target against it, a harmonic Higgs
that holds I, and the web seat's Lemmas A, A' and B on own code (the rule: W146_RULE.md, committed and pushed before
this script).

  K1  the classes, exact (sympy): x^2 + y^2 + z^2 = l1^2 + l3 l7 and |x|^2 + |y|^2 + |z|^2 = |l1|^2 + (|l3|^2 +
      |l7|^2)/2 with l1 = x, l3 = y - iz, l7 = y + iz; the dual basis (h0/sqrt2 on l3, conj h0/sqrt2 on l7); the class
      arithmetic; on the record's forms the leading q-exponents of l1, l3, l7 (from Im tau 6 and 7) in 1/8, 3/8, 7/8
      up to one common shift
  K2  the dichotomy on the record (Re tau 0.25 and 0.4, Im tau 3, 4, 5, 6): R and F_2 exactly null; the local slope
      -(ln I(y + 1) - ln I(y))/pi -> 1 for dR and F_a, a >= 6; I / (C |q|^(1/2)) -> 1 with C = 72 and 4a; for the
      e1-led F_a (a < 0) 1 - I decreasing and below 1e-3 at Im tau 6; I(conj h) = I(h)
  K3  I(f h) = I(h) for scalar f; R.dR = 0 and h_w.h_w = dR.dR, h_w = dR + (w/12) E2* R, at 12 points
  K4  main's committed target.json (B1743, at REV_MAIN): the least-squares slope of ln I against Im tau over its L2
      optima, and the largest I there
  K5  a read-out: the cusp category of every record direction and of its conjugate
  K6  the harmonic Higgs h = conj(F) + kappa F, F = eta^-3 R: h(tau + 1) = e^{-i pi/4} rho(T) h(tau), with rho(T)
      normalised by R(tau + 1) = rho(T) R(tau); I -> 2|kappa| / (1 + |kappa|^2) at Im tau 6
  L1  Lemma A: Y h = Y^T h = (h.h) u (sympy); the light left state within |g.g| |u| / m2 of conj g (20 000 draws,
      singular vectors at 30 digits)
  L2  Lemma A': the Frobenius identity (sympy), |u| / m3 <= sqrt 3 (20 000 draws, 200 local maximisations)
  L3  Lemma B: the largest real overlap (1 + |x.x|)/2 (2 000 optimisations); |<x, y>| <= cos(alpha(x) - alpha(y))
      (20 000 pairs, 200 local maximisations)

  The thetas, eta and E2 are direct sums (CONVENTIONS section 4); nothing uses a principal nome root.

    python3 -B the_higgs_invariant_dichotomy.py      # writes the_higgs_invariant_dichotomy.json beside itself
"""
import contextlib
import hashlib
import io
import json
import subprocess
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_zero_free_higgs_signs as W143  # noqa: E402  (eps_of: the forced sign of F_a)

OUT = HERE / "the_higgs_invariant_dichotomy.json"
REV_MAIN = "2bd171386e5097b28afc44c4fcdfbdabdd5e4e39"
TARGET = "frontier/B1743_the_principled_pencils_and_the_nines_target/verification/target.json"
TARGET_SHA = "c1e56539a0e52de3bfc2070398bcac4132dc5f1af9cfb72b085f90b63ffbae26"
A_LIST = (-10, -6, -2, 2, 6, 10, 14, 18, 22, 26)
CLASSES = (Fr(1, 8), Fr(3, 8), Fr(7, 8))
mp.mp.dps = 60
J = mp.mpc(0, 1)
PI = mp.pi


# ---------------------------------------------------------------- the forms, by direct sums

def _tail_eps():
    return mp.mpf(10) ** (-(mp.mp.dps + 10))


def thetas(tau):
    """(th2, th3, th4) at z = 0 and their q d/dq, q = e^{2 pi i tau}; q d/dq e^{i pi tau x} = (x/2) e^{i pi tau x}"""
    eps = _tail_eps()
    t2 = d2 = mp.mpc(0)
    n = 0
    while True:
        x = (mp.mpf(2 * n + 1) / 2) ** 2
        e = mp.exp(J * PI * tau * x)
        t2 += 2 * e
        d2 += x * e
        if n > 2 and abs(e) < eps * abs(t2):
            break
        n += 1
    t3, t4, d3, d4 = mp.mpc(1), mp.mpc(1), mp.mpc(0), mp.mpc(0)
    n = 1
    while True:
        e = mp.exp(J * PI * tau * n * n)
        s = 1 if n % 2 == 0 else -1
        t3 += 2 * e
        t4 += 2 * s * e
        d3 += n * n * e
        d4 += s * n * n * e
        if n > 2 and abs(e) < eps:
            break
        n += 1
    return t2, t3, t4, d2, d3, d4


def log_eta(tau):
    """log eta = 2 pi i tau / 24 + sum log(1 - q^n), every log principal with |q^n| < 1"""
    q = mp.exp(2 * PI * J * tau)
    eps = _tail_eps()
    s, n = 2 * PI * J * tau / 24, 1
    while True:
        qn = q ** n
        s += mp.log(1 - qn)
        if abs(qn) < eps:
            return s
        n += 1


def eta_pow(tau, p):
    return mp.exp(p * log_eta(tau))


def E2(tau):
    q = mp.exp(2 * PI * J * tau)
    eps = _tail_eps()
    s, n = mp.mpc(0), 1
    while True:
        qn = q ** n
        t = n * qn / (1 - qn)
        s += t
        if abs(t) < eps:
            return 1 - 24 * s
        n += 1


def R_and_DR(tau):
    """R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4); DR = q dR/dq + E2 R / 24 (main's census Higgs, W138's)"""
    t2, t3, t4, d2, d3, d4 = thetas(tau)
    R = [-t2 / (t3 * t4), -t4 / (t2 * t3), J * t3 / (t2 * t4)]
    l2, l3, l4 = d2 / t2, d3 / t3, d4 / t4
    dlog = [l2 - l3 - l4, l4 - l2 - l3, l3 - l2 - l4]
    e2 = E2(tau)
    return R, [R[k] * dlog[k] + e2 * R[k] / 24 for k in range(3)]


def F_a(tau, a):
    """W143's F_a = eta^(3 - a) (eps th2^a, eps th4^a, i th3^a), eps = i^((a + 2)/2)"""
    t2, t3, t4 = thetas(tau)[:3]
    eps = W143.eps_of(a)
    f = eta_pow(tau, 3 - a)
    return [f * eps * t2 ** a, f * eps * t4 ** a, f * J * t3 ** a]


def record_form(name, tau):
    if name == "R":
        return R_and_DR(tau)[0]
    if name == "dR":
        return R_and_DR(tau)[1]
    return F_a(tau, int(name[1:]))


RECORD = ["R", "dR"] + ["F%d" % a for a in A_LIST]


def dot(v, w):
    return v[0] * w[0] + v[1] * w[1] + v[2] * w[2]


def nrm2(v):
    return sum(abs(x) ** 2 for x in v)


def inv(v):
    return abs(dot(v, v)) / nrm2(v)


def lines(v):
    return [v[0], v[1] - J * v[2], v[1] + J * v[2]]


def conj(v):
    return [mp.conj(x) for x in v]


def s(x, n=6):
    return mp.nstr(x, n)


# ---------------------------------------------------------------- K1

def K1():
    x, y, z = sp.symbols("x y z")
    ok_sq = sp.expand(x ** 2 + y ** 2 + z ** 2 - (x ** 2 + (y - sp.I * z) * (y + sp.I * z))) == 0
    a = sp.symbols("a1:4", real=True)
    b = sp.symbols("b1:4", real=True)
    X = [a[k] + sp.I * b[k] for k in range(3)]
    ab2 = lambda w: sp.expand(w * sp.conjugate(w))
    L = [X[0], X[1] - sp.I * X[2], X[1] + sp.I * X[2]]
    ok_norm = sp.expand(sum(ab2(w) for w in X) - (ab2(L[0]) + (ab2(L[1]) + ab2(L[2])) / 2)) == 0
    M = sp.Matrix([[1, 0, 0], [0, 1, -sp.I], [0, 1, sp.I]])
    Minv = M.inv()
    h0 = sp.Matrix([0, 1, sp.I]) / sp.sqrt(2)
    ok_dual = (sp.simplify(Minv[:, 1] - h0 / sp.sqrt(2)) == sp.zeros(3, 1)
               and sp.simplify(Minv[:, 2] - h0.conjugate() / sp.sqrt(2)) == sp.zeros(3, 1))
    c1, c3, c7 = CLASSES
    ok_arith = ((2 * c1) % 1 == (c3 + c7) % 1 == Fr(1, 4)) and ((2 * c3) % 1 == (2 * c7) % 1 == Fr(3, 4))
    tau6, tau7 = mp.mpc("0.1", 6), mp.mpc("0.1", 7)
    forms, worst = {}, mp.mpf(0)
    for name in RECORD:
        l6, l7 = lines(record_form(name, tau6)), lines(record_form(name, tau7))
        e = [-(mp.log(abs(l7[k])) - mp.log(abs(l6[k]))) / (2 * PI) for k in range(3)]
        shifts = [(e[k] - mp.mpf(CLASSES[k].numerator) / CLASSES[k].denominator) % 1 for k in range(3)]
        spread = max(min(abs(shifts[i] - shifts[j]), 1 - abs(shifts[i] - shifts[j]))
                     for i in range(3) for j in range(3))
        worst = max(worst, spread)
        lead = ["l1", "l3", "l7"][min(range(3), key=lambda k: e[k])]
        forms[name] = {"leading exponents (l1, l3, l7)": [s(t, 12) for t in e], "leading line": lead,
                       "spread of the shifts mod 1": s(spread, 3)}
    ok_R = all(abs(mp.mpf(forms["R"]["leading exponents (l1, l3, l7)"][k]) - v) < 1e-9
               for k, v in enumerate((mp.mpf(1) / 8, mp.mpf(3) / 8, -mp.mpf(1) / 8)))
    ok_classes = worst < 1e-8
    res = {"x^2 + y^2 + z^2 = l1^2 + l3 l7": ok_sq, "norm identity": ok_norm,
           "dual basis: h0/sqrt2 on l3, conj h0/sqrt2 on l7": bool(ok_dual), "class arithmetic": ok_arith,
           "record forms": forms, "largest spread of the shifts": s(worst, 3),
           "R's exponents are (1/8, 3/8, -1/8)": ok_R}
    return res, bool(ok_sq and ok_norm and ok_dual and ok_arith and ok_classes and ok_R)


# ---------------------------------------------------------------- K2, K5

K2_RE = ("0.25", "0.4")
K2_Y = (3, 4, 5, 6)
NULL_EXACT = ("R", "F2")
NULL_LED = ("dR",) + tuple("F%d" % a for a in A_LIST if a >= 6)
E1_LED = tuple("F%d" % a for a in A_LIST if a < 0)


def C_hand(name):
    return mp.mpf(72) if name == "dR" else 4 * mp.mpf(int(name[1:]))


def K2K5():
    table, ok, k5_ok = {}, True, True
    conj_worst = mp.mpf(0)
    for name in RECORD:
        rows = {}
        for re in K2_RE:
            Ivals = []
            for y in K2_Y:
                v = record_form(name, mp.mpc(re, y))
                Ivals.append(inv(v))
                conj_worst = max(conj_worst, abs(inv(conj(v)) - inv(v)) / max(inv(v), mp.mpf(10) ** -300))
            row = {"I": [s(t, 10) for t in Ivals]}
            if name in NULL_EXACT:
                row["max I"] = s(max(Ivals), 3)
                ok &= max(Ivals) < mp.mpf(10) ** -40
                cat = "exactly null"
            elif name in NULL_LED:
                slopes = [-(mp.log(Ivals[j + 1]) - mp.log(Ivals[j])) / PI for j in range(3)]
                ratio = Ivals[-1] / (C_hand(name) * mp.exp(-PI * K2_Y[-1]))
                row.update({"local slopes": [s(t, 10) for t in slopes],
                            "nearest odd integer": int(2 * mp.floor(slopes[-1] / 2) + 1),
                            "I / (C exp(-pi Im tau)) at Im tau 6": s(ratio, 10), "C": int(C_hand(name))})
                ok &= abs(slopes[-1] - 1) < 1e-3 and abs(ratio - 1) < 1e-3
                cat = "null-led, I -> 0"
            else:
                one_minus = [1 - t for t in Ivals]
                row["1 - I"] = [s(t, 6) for t in one_minus]
                ok &= all(one_minus[j + 1] < one_minus[j] for j in range(3)) and one_minus[-1] < 1e-3
                cat = "e1-led, I -> 1"
            row["category at the cusp"] = cat
            k5_ok &= Ivals[-1] < 1e-3 or Ivals[-1] > 1 - 1e-3
            rows["Re tau " + re] = row
        table[name] = rows
    ok &= conj_worst < mp.mpf(10) ** -40
    k2 = {"forms": table, "max relative |I(conj h) - I(h)|": s(conj_worst, 3)}
    k5 = {"every record direction and its conjugate at Im tau 6 has I < 1e-3 or I > 1 - 1e-3": bool(k5_ok),
          "categories": {n: table[n]["Re tau 0.25"]["category at the cusp"] for n in RECORD},
          "note": "conjugates share I with their forms (K2's check); none is of K5's harmonic kind"}
    return k2, bool(ok), k5, bool(k5_ok)


# ---------------------------------------------------------------- K3

K3_PTS = [(re, im) for im in ("1.0", "2.2") for re in ("-0.4", "-0.1", "0.1", "0.25", "0.4", "0.5")]
K3_W = (-4, 0, 2, 4, 12)


def K3():
    worst_orth, worst_pencil, worst_scale = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    for re, im in K3_PTS:
        tau = mp.mpc(re, im)
        R, DR = R_and_DR(tau)
        worst_orth = max(worst_orth, abs(dot(R, DR)) / mp.sqrt(nrm2(R) * nrm2(DR)))
        e2s = E2(tau) - 3 / (PI * mp.im(tau))
        base = dot(DR, DR)
        for w in K3_W:
            hw = [DR[k] + mp.mpf(w) / 12 * e2s * R[k] for k in range(3)]
            worst_pencil = max(worst_pencil, abs(dot(hw, hw) - base) / abs(base))
        eta = eta_pow(tau, 1)
        fs = [mp.im(tau) ** (mp.mpf(3) / 4), abs(eta) ** 5, eta_pow(tau, -7), mp.mpc("2.5", "-1.3")]
        for h in (DR, F_a(tau, 6)):
            for f in fs:
                worst_scale = max(worst_scale, abs(inv([f * x for x in h]) - inv(h)) / inv(h))
    res = {"points": len(K3_PTS), "w": list(K3_W), "max |R.dR| / (|R| |dR|)": s(worst_orth, 3),
           "max |h_w.h_w - dR.dR| / |dR.dR|": s(worst_pencil, 3), "max relative |I(f h) - I(h)|": s(worst_scale, 3)}
    tol = mp.mpf(10) ** -20
    return res, bool(worst_orth < tol and worst_pencil < tol and worst_scale < tol)


# ---------------------------------------------------------------- K4

def K4():
    root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE, capture_output=True, text=True,
                               check=True).stdout.strip())
    raw = subprocess.run(["git", "show", "%s:%s" % (REV_MAIN, TARGET)], cwd=root, capture_output=True,
                         check=True).stdout
    sha = hashlib.sha256(raw).hexdigest()
    d = json.loads(raw.decode("utf-8"))
    opt = d["optima"]
    hors = sorted({o["hor"] for o in opt})
    norm = lambda h: h.replace("₂", "2").replace("_", "").strip().upper()
    L2 = [o for o in opt if norm(o["hor"]) == "L2"]
    ys = np.array([float(o["tau"][1]) for o in L2])
    Is = np.array([float(o["|h.h|/|h|^2"]) for o in L2])
    slope = float(np.polyfit(ys, np.log(Is), 1)[0]) if len(L2) >= 2 else float("nan")
    ya = np.array([float(o["tau"][1]) for o in opt])
    Ia = np.array([float(o["|h.h|/|h|^2"]) for o in opt])
    slope_all = float(np.polyfit(ya, np.log(Ia), 1)[0])
    res = {"rev": REV_MAIN, "sha256": sha, "sha256 as pinned": sha == TARGET_SHA, "optima": len(opt),
           "horocycle labels": hors, "L2 optima": len(L2),
           "L2 (Im tau, I)": [[float(y), float(i)] for y, i in zip(ys, Is)],
           "least-squares slope of ln I against Im tau, L2": slope, "largest I, L2": float(Is.max()),
           "read-out: the slope over all ten optima": slope_all,
           "read-out: every optimum (hor, Im tau, I)": [[o["hor"], float(o["tau"][1]), float(o["|h.h|/|h|^2"])]
                                                       for o in opt],
           "null-led rate, -pi(1 + 2n), n >= 0": "at most %.6f" % -np.pi}
    ok = sha == TARGET_SHA and len(L2) >= 2 and -1 <= slope <= 1 and Is.max() < 0.1
    return res, bool(ok)


# ---------------------------------------------------------------- K6

def rho_T():
    r8 = mp.exp(J * PI / 4)
    return mp.matrix([[r8, 0, 0], [0, 0, J / r8], [0, -J / r8, 0]])


def apply(Mx, v):
    return [sum(Mx[i, j] * v[j] for j in range(3)) for i in range(3)]


def h_kappa(tau, kappa):
    F = [eta_pow(tau, -3) * x for x in R_and_DR(tau)[0]]
    return [mp.conj(F[k]) + kappa * F[k] for k in range(3)]


K6_PTS = [(re, im) for re in ("-0.4", "-0.2", "0") for im in ("1", "2")]
K6_KAPPA = (mp.mpf("0.009"), mp.mpf("0.1"), mp.mpc(0, "0.5"))


def K6():
    M = rho_T()
    worst_norm, worst_eq = mp.mpf(0), mp.mpf(0)
    for re, im in K6_PTS:
        tau = mp.mpc(re, im)
        R0, D0 = R_and_DR(tau)
        R1, D1 = R_and_DR(tau + 1)
        for v0, v1 in ((R0, R1), (D0, D1)):
            MR = apply(M, v0)
            worst_norm = max(worst_norm, mp.sqrt(nrm2([v1[k] - MR[k] for k in range(3)]) / nrm2(v0)))
        for kap in K6_KAPPA:
            h0, h1 = h_kappa(tau, kap), h_kappa(tau + 1, kap)
            Mh = apply(M, h0)
            ph = mp.exp(-J * PI / 4)
            worst_eq = max(worst_eq, mp.sqrt(nrm2([h1[k] - ph * Mh[k] for k in range(3)]) / nrm2(h0)))
    # rho(T) in the line coordinates: diag(e^{2 pi i/8}, e^{2 pi i 3/8}, e^{2 pi i 7/8})
    Lm = mp.matrix([[1, 0, 0], [0, 1, -J], [0, 1, J]])
    D = Lm * M * mp.inverse(Lm)
    want = [mp.exp(2 * PI * J * mp.mpf(c.numerator) / c.denominator) for c in CLASSES]
    eig_dev = max(abs(D[i, j] - (want[i] if i == j else 0)) for i in range(3) for j in range(3))
    limits, worst_lim = {}, mp.mpf(0)
    for kap in K6_KAPPA:
        pred = 2 * abs(kap) / (1 + abs(kap) ** 2)
        got = {re: inv(h_kappa(mp.mpc(re, 6), kap)) for re in ("0.25", "0.4")}
        dev = max(abs(g / pred - 1) for g in got.values())
        worst_lim = max(worst_lim, dev)
        limits[s(kap, 4)] = {"2|k|/(1 + |k|^2)": s(pred, 10), "I at Im tau 6": {r: s(g, 10) for r, g in got.items()},
                             "relative deviation": s(dev, 3)}
    band = {y: s(inv(h_kappa(mp.mpc("0.4375", y), mp.mpf("0.0091"))), 6) for y in ("2.0", "2.1", "2.2", "2.3")}
    res = {"max relative |v(tau + 1) - rho(T) v(tau)|, v = R, dR": s(worst_norm, 3),
           "max relative |h(tau + 1) - e^{-i pi/4} rho(T) h(tau)|": s(worst_eq, 3),
           "rho(T) diagonal on the lines with the classes, max deviation": s(eig_dev, 3), "limits": limits,
           "read-out (not in the rule): I(h) at kappa 0.0091, Re tau 0.4375, Im tau 2.0-2.3": band}
    tol = mp.mpf(10) ** -20
    return res, bool(worst_norm < tol and worst_eq < tol and eig_dev < tol and worst_lim < 1e-3)


# ---------------------------------------------------------------- L1, L2, L3 (the web seat's lemmas)

def cross_mat(h):
    return [[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]]


def Y_of(w, u, h, lib):
    uh = u[0] * h[0] + u[1] * h[1] + u[2] * h[2]
    X = cross_mat(h)
    return [[u[i] * h[j] + h[i] * u[j] - (uh if i == j else 0) + w * X[i][j] for j in range(3)] for i in range(3)]


def L_sympy():
    w = sp.Symbol("w")
    u = sp.symbols("u1:4")
    h = sp.symbols("h1:4")
    Y = sp.Matrix(Y_of(w, u, h, sp))
    hv, uv = sp.Matrix(h), sp.Matrix(u)
    hh = sum(x * x for x in h)
    okA = sp.expand(Y * hv - hh * uv) == sp.zeros(3, 1) and sp.expand(Y.T * hv - hh * uv) == sp.zeros(3, 1)
    a = sp.symbols("a1:4", real=True)
    b = sp.symbols("b1:4", real=True)
    c = sp.symbols("c1:4", real=True)
    d = sp.symbols("d1:4", real=True)
    U = [a[k] + sp.I * b[k] for k in range(3)]
    H = [c[k] + sp.I * d[k] for k in range(3)]
    S = sp.Matrix(Y_of(0, U, H, sp))
    ab2 = lambda z: sp.expand(z * sp.conjugate(z))
    lhs = sum(ab2(S[i, j]) for i in range(3) for j in range(3))
    nu, nh = sum(ab2(z) for z in U), sum(ab2(z) for z in H)
    herm = sum(sp.conjugate(U[k]) * H[k] for k in range(3))
    bil = sum(U[k] * H[k] for k in range(3))
    rhs = 2 * nu * nh + 2 * ab2(herm) - ab2(bil)
    okAp = sp.expand(lhs - rhs) == 0
    return okA, okAp


def crandn(rng, *shape):
    return rng.normal(size=shape) + 1j * rng.normal(size=shape)


def L1(rng, n=20000):
    worst, worst_id, skipped, h0 = -mp.inf, mp.mpf(0), 0, np.array([0, 1, 1j]) / np.sqrt(2)
    with mp.workdps(30):
        for i in range(n):
            w = complex(rng.normal(), rng.normal())
            u = crandn(rng, 3) * 10 ** rng.uniform(-3, 1)
            g = h0 + 10 ** rng.uniform(-6, 0) * crandn(rng, 3) if i % 2 else crandn(rng, 3)
            g = g / np.linalg.norm(g)
            gm = [mp.mpc(x) for x in g]
            gm = [x / mp.sqrt(nrm2(gm)) for x in gm]
            um = [mp.mpc(x) for x in u]
            Y = mp.matrix(Y_of(mp.mpc(w), um, gm, mp))
            E, Q = mp.eighe(Y * Y.H)
            m = [mp.sqrt(max(e, 0)) for e in E]
            if m[1] < mp.mpf(10) ** -25:
                skipped += 1
                continue
            gbar = [mp.conj(x) for x in gm]
            ov = [abs(sum(mp.conj(Q[r, k]) * gbar[r] for r in range(3))) for k in range(3)]
            sin_t = mp.sqrt(ov[1] ** 2 + ov[2] ** 2)
            gg = abs(dot(gm, gm))
            x = gg * mp.sqrt(nrm2(um)) / m[1]
            worst = max(worst, sin_t - x)
            lhs = sum(m[k] ** 2 * ov[k] ** 2 for k in range(3))
            rhs = gg ** 2 * nrm2(um)
            worst_id = max(worst_id, abs(lhs - rhs) / max(rhs, mp.mpf(10) ** -60))
    return {"draws": n, "skipped (m2 below 1e-25)": skipped, "max (sin theta - |g.g| |u| / m2)": s(worst, 4),
            "max relative |sum m_k^2 |<conj g, l_k>|^2 - |g.g|^2 |u|^2|": s(worst_id, 3)}, \
        bool(worst <= 1e-12 and worst_id < 1e-20)


def ratio_u_m3(p):
    w = p[0] + 1j * p[1]
    u = p[2:5] + 1j * p[5:8]
    h = p[8:11] + 1j * p[11:14]
    nh = np.linalg.norm(h)
    if nh == 0:
        return 0.0
    h = h / nh
    Y = np.array(Y_of(w, u, h, np), dtype=complex)
    m3 = np.linalg.svd(Y, compute_uv=False)[0]
    return float(np.linalg.norm(u) / m3) if m3 > 0 else 0.0


def L2(rng, okAp, n=20000, starts=200):
    best_rand = max(ratio_u_m3(rng.normal(size=14)) for _ in range(n))
    best_opt = 0.0
    for _ in range(starts):
        r = minimize(lambda p: -ratio_u_m3(p), rng.normal(size=14), method="Nelder-Mead",
                     options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-12})
        best_opt = max(best_opt, -float(r.fun))
    bound = float(np.sqrt(3))
    res = {"Frobenius identity (sympy, general h; unit h is the lemma)": bool(okAp), "draws": n,
           "largest |u| / m3, random": best_rand, "local maximisations": starts,
           "largest |u| / m3, maximised": best_opt, "sqrt 3": bound}
    return res, bool(okAp and best_rand <= bound + 1e-12 and best_opt <= bound + 1e-12)


def unit_c(p):
    x = p[0:3] + 1j * p[3:6]
    return x / np.linalg.norm(x)


def alpha(x):
    return 0.5 * float(np.arccos(min(1.0, abs(np.dot(x, x)))))


def L3(rng, n_over=2000, n_pairs=20000, starts=200):
    worst_over, worst_dist = 0.0, 0.0
    for _ in range(n_over):
        x = unit_c(rng.normal(size=6))

        def neg(t):
            r = np.array([np.sin(t[0]) * np.cos(t[1]), np.sin(t[0]) * np.sin(t[1]), np.cos(t[0])])
            return -abs(np.vdot(x, r)) ** 2

        best = max(-minimize(neg, rng.uniform(0, np.pi, 2), method="BFGS", options={"gtol": 1e-12}).fun
                   for _ in range(6))
        pred = (1 + abs(np.dot(x, x))) / 2
        worst_over = max(worst_over, abs(best - pred))
        worst_dist = max(worst_dist, abs(float(np.arccos(min(1.0, np.sqrt(best)))) - alpha(x)))
    worst_pair = -np.inf
    for i in range(n_pairs):
        x = unit_c(rng.normal(size=6))
        y = unit_c(rng.normal(size=6))
        if i % 3 == 1:
            x = unit_c(np.concatenate([rng.normal(size=3), 1e-3 * rng.normal(size=3)]))
        if i % 3 == 2:
            y = unit_c(np.concatenate([[0, 1, 0], [0, 0, 1]]) + 1e-3 * rng.normal(size=6))
        worst_pair = max(worst_pair, abs(np.vdot(x, y)) - np.cos(alpha(x) - alpha(y)))

    def gap(p):
        x, y = unit_c(p[:6]), unit_c(p[6:])
        return -(abs(np.vdot(x, y)) - np.cos(alpha(x) - alpha(y)))

    worst_opt = -np.inf
    for _ in range(starts):
        r = minimize(gap, rng.normal(size=12), method="Nelder-Mead", options={"maxiter": 8000, "fatol": 1e-14})
        worst_opt = max(worst_opt, -float(r.fun))
    res = {"overlap optimisations": n_over, "max |largest real overlap^2 - (1 + |x.x|)/2|": worst_over,
           "read-out: max |arccos(sqrt overlap^2) - alpha(x)|": worst_dist, "pairs": n_pairs,
           "max (|<x, y>| - cos(alpha(x) - alpha(y))), pairs": float(worst_pair), "local maximisations": starts,
           "max (|<x, y>| - cos(alpha(x) - alpha(y))), maximised": float(worst_opt)}
    return res, bool(worst_over < 1e-9 and worst_pair <= 1e-12 and worst_opt <= 1e-12)


# ---------------------------------------------------------------- main

def main():
    t0 = time.time()
    out = {"arc": "W146", "rule": "W146_RULE.md", "status": "one run", "dps": mp.mp.dps,
           "python": sys.version.split()[0], "mpmath": mp.__version__, "numpy": np.__version__, "sympy": sp.__version__}
    cells, secs = {}, {}

    def run(name, fn, *a):
        t = time.time()
        try:
            r = fn(*a)
        except Exception as exc:  # a failed part is kept and disclosed
            out[name + "_failed"] = repr(exc)
            secs[name] = round(time.time() - t, 1)
            return None
        secs[name] = round(time.time() - t, 1)
        return r

    r = run("K1", K1)
    if r:
        out["K1"], cells["K1"] = r
    r = run("K2", K2K5)
    if r:
        out["K2"], cells["K2"], out["K5"], cells["K5"] = r
    r = run("K3", K3)
    if r:
        out["K3"], cells["K3"] = r
    r = run("K4", K4)
    if r:
        out["K4"], cells["K4"] = r
    r = run("K6", K6)
    if r:
        out["K6"], cells["K6"] = r
    rng = np.random.default_rng(146)
    r = run("L_sympy", L_sympy)
    okA, okAp = r if r else (False, False)
    r = run("L1", L1, rng)
    if r:
        out["L1"], c = r
        out["L1"]["Y h = Y^T h = (h.h) u (sympy)"] = bool(okA)
        cells["L1"] = bool(c and okA)
    r = run("L2", L2, rng, okAp)
    if r:
        out["L2"], cells["L2"] = r
    r = run("L3", L3, rng)
    if r:
        out["L3"], cells["L3"] = r
    order = ("K1", "K2", "K3", "K4", "L1", "L2", "L3", "K5", "K6")
    out["cells"] = {k: bool(cells.get(k, False)) for k in order}
    out["every predicted cell holds"] = bool(all(out["cells"].values()))
    out["part_seconds"] = secs
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every predicted cell holds:", out["every predicted cell holds"])
    failed = [k for k in out if k.endswith("_failed")]
    if failed:
        print("failed parts:", failed)


if __name__ == "__main__":
    main()
