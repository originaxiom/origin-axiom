#!/usr/bin/env python3
"""W144 — a non-authoring proof review, on own code, of the audit lane's five checkpoints named in its relay at
17cdad33a (the rule: W144_RULE.md, committed and pushed before this script). None of the lane's code is imported or
run; the definitions are read from its notes and written fresh here.

  A1  the root cover w^2 = theta_1(z|tau): C, A, B, K1, K2, their relations, and F = N/w under them
  A2  the modular root maps L, S: the equation, the four K relations, S^2, S^4 = C, (SL)^3 = S^2, the sign test
  A3  the based words in Aut(F2), exact, and their quaternion lifts: Delta^4 = eps J_c, s^4 = eps J_c^-1
  A4  the joint action: D_a = A, D_b = C B^-1, the conjugations (5), F's laws and the scalar cocycle k
  B1  the puncture expansion F = z^(-1/2) b (1 + O(z^2))
  B2  the connecting map delta(u)_p = b^T eps u_p, its kernel U and the kernel table
  C1  the transported puncture data d, n at lifts z_y = m + n tau, and the root factors r
  C2  the transport maps (9), the epsilon and J_c checks, the spin maps (10) and the Green form (11)
  D1  projective regularity: R^0 = (d/6) I - P, holonomy, degrees, the scalar lifts, the commutant
  E1  the central kernel of SU(6) x SU(3) x SU(2) in E8, on own roots, and the block sizes
  E2  the compensation U_a, U_b and rho tensor rho

Theta arguments have periods 1 and tau: theta_n(z|tau) = jtheta(n, pi z, exp(pi i tau)).

    python3 -B the_audit_checkpoints_review.py      # writes the_audit_checkpoints_review.json beside itself
"""
import itertools
import json
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy.linalg as sl
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_audit_checkpoints_review.json"
mp.mp.dps = 50
TOL = mp.mpf("1e-40")
TAUS = [mp.mpc("0.13", "1.07"), mp.mpc("-0.31", "0.84"), mp.mpc("0.42", "1.31"), mp.mpc("0.05", "0.62")]
ZS = [mp.mpc("0.217", "0.093"), mp.mpc("-0.381", "0.274"), mp.mpc("0.149", "-0.188")]
LIFTS = [(0, 0), (1, 0), (0, 1), (1, 1), (-1, 2), (2, -1)]
I = mp.mpc(0, 1)
SQ2 = mp.sqrt(2)


# ---------------------------------------------------------------- quaternions as 2 x 2 matrices
def M2(rows):
    return mp.matrix(rows)


ONE = M2([[1, 0], [0, 1]])
QI = M2([[I, 0], [0, -I]])
QJ = M2([[0, 1], [-1, 0]])
QK = QI * QJ
GL = (ONE + QI) / SQ2                      # g_L
GR = (ONE - QJ) / SQ2                      # g_R


def inv2(g):
    return mp.inverse(g)


def mnorm(m):
    return max(abs(x) for x in m) if isinstance(m, list) else mp.mnorm(m, 1)


# ---------------------------------------------------------------- thetas, periods 1 and tau
def th(n, z, tau):
    return mp.jtheta(n, mp.pi * z, mp.exp(I * mp.pi * tau))


def dth1(z, tau):
    return mp.pi * mp.jtheta(1, mp.pi * z, mp.exp(I * mp.pi * tau), 1)


def N(z, tau):
    return mp.matrix([I * th(2, z, 2 * tau), th(3, z, 2 * tau)])


def F(x):
    tau, z, w = x
    return N(z, tau) / w


def point(tau, z):
    return (tau, z, mp.sqrt(th(1, z, tau)))


def t_(z, tau):
    return mp.exp(-I * mp.pi * tau / 2 - I * mp.pi * z)


# maps on (tau, z, w); the rightmost map acts first in a product
def C(x):
    tau, z, w = x
    return (tau, z, -w)


def A(x):
    tau, z, w = x
    return (tau, z + 1, I * w)


def Ainv(x):
    tau, z, w = x
    return (tau, z - 1, w / I)


def B(x):
    tau, z, w = x
    return (tau, z + tau, I * t_(z, tau) * w)


def Binv(x):
    tau, z, w = x
    return (tau, z - tau, w / (I * t_(z - tau, tau)))


def K1(x):
    tau, z, w = x
    return (tau, z + 2, w)


def K1inv(x):
    tau, z, w = x
    return (tau, z - 2, w)


def K2(x):
    tau, z, w = x
    return (tau, z + 2 * tau, mp.exp(-2 * I * mp.pi * tau - 2 * I * mp.pi * z) * w)


def K2inv(x):
    tau, z, w = x
    z0 = z - 2 * tau
    return (tau, z0, w / mp.exp(-2 * I * mp.pi * tau - 2 * I * mp.pi * z0))


ALPHA0, BETA0 = mp.exp(I * mp.pi / 8), mp.exp(-3 * I * mp.pi / 8)


def Lm(x, sign=1):
    tau, z, w = x
    return (tau + 1, z, sign * ALPHA0 * w)


def Sm(x, sign=1):
    tau, z, w = x
    root = BETA0 * mp.power(tau, mp.mpf(1) / 4) * mp.exp(I * mp.pi * z ** 2 / (2 * tau))
    return (-1 / tau, z / tau, sign * root * w)


def comp(*maps):
    """comp(f, g, h)(x) = f(g(h(x)))"""
    def run(x):
        for m in reversed(maps):
            x = m(x)
        return x
    return run


def dist(x, y):
    return max(abs(x[0] - y[0]), abs(x[1] - y[1]), abs(x[2] - y[2]) / max(abs(x[2]), mp.mpf(1)))


def on_curve(x):
    tau, z, w = x
    return abs(w ** 2 - th(1, z, tau)) / abs(th(1, z, tau))


def vdist(u, v):
    n = u.rows
    return max(abs(u[k] - v[k]) for k in range(n)) / max(max(abs(v[k]) for k in range(n)), mp.mpf(1))


# ---------------------------------------------------------------- A1
def A1():
    eqs, rels, flaws = [], [], []
    for tau in TAUS:
        for z in ZS:
            x = point(tau, z)
            for m in (C, A, B, K1, K2, Ainv, Binv, K1inv, K2inv):
                eqs.append(on_curve(m(x)))
            rels += [dist(C(C(x)), x), dist(comp(A, B)(x), comp(C, B, A)(x)), dist(comp(A, A)(x), comp(C, K1)(x)),
                     dist(comp(B, B)(x), comp(C, K2)(x)), dist(comp(C, A)(x), comp(A, C)(x)),
                     dist(comp(C, B)(x), comp(B, C)(x)), dist(comp(K1, K2)(x), comp(K2, K1)(x)),
                     dist(comp(Ainv, A)(x), x), dist(comp(Binv, B)(x), x), dist(comp(K2inv, K2)(x), x)]
            f = F(x)
            flaws += [vdist(F(K1(x)), f), vdist(F(K2(x)), f), vdist(F(A(x)), QI * f), vdist(F(B(x)), QJ * f),
                      vdist(F(C(x)), -f)]
    out = {"max off the curve": mp.nstr(max(eqs), 3), "max relation residual": mp.nstr(max(rels), 3),
           "max F-law residual": mp.nstr(max(flaws), 3)}
    return out, max(eqs) < TOL and max(rels) < TOL and max(flaws) < TOL


# ---------------------------------------------------------------- A2
def A2():
    eqs, rels = [], []
    sign_test = {}
    for tau in TAUS:
        for z in ZS:
            x = point(tau, z)
            eqs += [on_curve(Lm(x)), on_curve(Sm(x))]
            rels += [dist(comp(Lm, K1)(x), comp(K1, Lm)(x)), dist(comp(Lm, K2)(x), comp(K2, K1inv, Lm)(x)),
                     dist(comp(Sm, K1)(x), comp(K2inv, Sm)(x)), dist(comp(Sm, K2)(x), comp(K1, Sm)(x))]
            s2 = comp(Sm, Sm)(x)
            rels += [dist(s2, (tau, -z, -I * x[2])), dist(comp(Sm, Sm, Sm, Sm)(x), C(x))]
            SL = comp(Sm, Lm)
            rels.append(dist(comp(SL, SL, SL)(x), s2))
            for name, (sl_, ss) in {"both reversed": (-1, -1), "L reversed": (-1, 1), "S reversed": (1, -1)}.items():
                Lr = lambda y, s=sl_: Lm(y, s)
                Sr = lambda y, s=ss: Sm(y, s)
                lhs = comp(Sr, Lr, Sr, Lr, Sr, Lr)(x)
                rhs = comp(Sr, Sr)(x)
                ratio = lhs[2] / rhs[2]
                sign_test.setdefault(name, []).append(ratio)
    sgn = {k: (mp.nstr(max(abs(r - 1) for r in v), 3), mp.nstr(max(abs(r + 1) for r in v), 3))
           for k, v in sign_test.items()}
    ok_sign = (max(abs(r - 1) for r in sign_test["both reversed"]) < TOL
               and all(max(abs(r + 1) for r in sign_test[k]) < TOL for k in ("L reversed", "S reversed")))
    out = {"max off the curve": mp.nstr(max(eqs), 3), "max relation residual": mp.nstr(max(rels), 3),
           "(SL)^3 / S^2 on w: distance from +1 and from -1": sgn}
    return out, max(eqs) < TOL and max(rels) < TOL and ok_sign


# ---------------------------------------------------------------- A3: free words, exact
def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def winv(w):
    return tuple(-x for x in reversed(w))


def apply(phi, w):
    out = []
    for x in w:
        out += list(phi[x]) if x > 0 else list(winv(phi[-x]))
    return red(out)


def ocomp(phi, psi):
    """(phi psi)(x) = phi(psi(x))"""
    return {g: apply(phi, psi[g]) for g in (1, 2)}


a, b = (1,), (2,)
IDA = {1: a, 2: b}
LA = {1: a, 2: (1, 2)}
LAi = {1: a, 2: (-1, 2)}
RA = {1: (1, 2), 2: b}
RAi = {1: (1, -2), 2: b}


def inner(h):
    return {1: red(h + a + winv(h)), 2: red(h + b + winv(h))}


def opow(phi, n):
    out = IDA
    for _ in range(n):
        out = ocomp(phi, out)
    return out


def rho_word(w):
    m = ONE
    for x in w:
        q = QI if abs(x) == 1 else QJ
        m = m * (q if x > 0 else inv2(q))
    return m


def intertwines(phi, g):
    return max(mnorm(rho_word(phi[x]) - g * rho_word((x,)) * inv2(g)) for x in (1, 2))


def A3():
    c = (1, -2, -1, 2)
    Delta = ocomp(LA, ocomp(RAi, LA))
    S = ocomp(RA, ocomp(LAi, RA))
    D4 = opow(Delta, 4)
    SL = ocomp(S, LA)
    checks = {
        "L L^-1 = id and R R^-1 = id": ocomp(LA, LAi) == IDA and ocomp(RA, RAi) == IDA,
        "Delta(a) = a b^-1 a^-1, Delta(b) = a": Delta == {1: (1, -2, -1), 2: a},
        "Delta^4 = I_c, c = a b^-1 a^-1 b": D4 == inner(c),
        "R L^-1 R = Delta^-1": ocomp(S, Delta) == IDA and ocomp(Delta, S) == IDA,
        "S(a) = b, S(b) = b^-1 a^-1 b": S == {1: b, 2: (-2, -1, 2)},
        "(SL)^3 = S^2 in Aut(F2)": opow(SL, 3) == opow(S, 2),
        "I_c != I_c^-1": inner(c) != inner(winv(c)),
    }
    gD = GL * inv2(GR) * GL
    gs = GR * inv2(GL) * GR
    rc = rho_word(c)
    lifts = {"g_L intertwines L": intertwines(LA, GL), "g_R intertwines R": intertwines(RA, GR),
             "g_Delta intertwines Delta": intertwines(Delta, gD), "g_s intertwines S": intertwines(S, gs)}
    num = {
        "g_Delta - (i + j)/sqrt2": mnorm(gD - (QI + QJ) / SQ2),
        "g_s - g_Delta^-1 (r l^-1 r = Delta^-1 in E)": mnorm(gs - inv2(gD)),
        "rho(c) + 1": mnorm(rc + ONE),
        "g_Delta^4 - 1 (so (Delta, g_Delta)^4 = (I_c, +1) = eps J_c)": mnorm(gD ** 4 - ONE),
        "g_s^4 - 1 (so s^4 = (I_c^-1, +1) = eps J_c^-1)": mnorm(gs ** 4 - ONE),
        "eps J_c^-1 g-part = (-1) rho(c)^-1, minus 1": mnorm(-inv2(rc) - ONE),
    }
    ok = all(checks.values()) and all(v < TOL for v in lifts.values()) and all(v < TOL for v in num.values())
    out = {"words": checks, "lifts": {k: mp.nstr(v, 3) for k, v in lifts.items()},
           "lift identities": {k: mp.nstr(v, 3) for k, v in num.items()},
           "s^4 automorphism is I_c^-1, not I_c": opow(S, 4) == inner(winv(c)) and opow(S, 4) != inner(c)}
    return out, ok and out["s^4 automorphism is I_c^-1, not I_c"]


# ---------------------------------------------------------------- A4
GS = GR * inv2(GL) * GR


def Db(x):
    return C(Binv(x))


def Dbinv(x):
    return B(C(x))


def k_l(tau):
    return ALPHA0


def k_s(tau):
    return BETA0 * mp.power(tau, mp.mpf(1) / 4)


def A4():
    conj, flaws, dc = [], [], []
    for tau in TAUS:
        for z in ZS:
            x = point(tau, z)
            conj += [dist(comp(Lm, A)(x), comp(A, Lm)(x)), dist(comp(Lm, Db)(x), comp(A, Db, Lm)(x)),
                     dist(comp(Sm, A)(x), comp(Db, Sm)(x)), dist(comp(Sm, Db)(x), comp(Dbinv, Ainv, Db, Sm)(x))]
            dc.append(dist(comp(A, Dbinv, Ainv, Db)(x), C(x)))
            f = F(x)
            flaws += [vdist(F(Lm(x)), k_l(tau) * (GL * f)), vdist(F(Sm(x)), k_s(tau) * (GS * f)),
                      vdist(F(A(x)), QI * f), vdist(F(Db(x)), QJ * f)]
    # k^2 = j mu on generators; s^4, eps; the relation word (sl)^3 s^-2
    zeta = mp.exp(I * mp.pi / 4)
    kjm = []
    for tau in TAUS:
        kjm += [abs(k_l(tau) ** 2 - 1 * zeta), abs(k_s(tau) ** 2 - mp.sqrt(tau) * zeta ** -3)]
        # k_{s^4} from the maps: F(S^4 x) = k g_s^4 F(x)
        x = point(tau, ZS[0])
        f4 = F(comp(Sm, Sm, Sm, Sm)(x))
        g4f = (GS ** 4) * F(x)
        k4 = f4[0] / g4f[0]
        kjm.append(abs(f4[1] / g4f[1] - k4))
        js4 = (mp.sqrt(-1 / tau) * mp.sqrt(tau)) ** 2                 # j_{s^2}(tau)^2, s^2 fixes tau
        kjm.append(abs(k4 ** 2 - js4 * zeta ** -12))
        k4s = k4
        # k_{J_c} from the maps: F(D_c x) = k_{J_c} rho(c) F(x), rho(c) = -1
        kjc = F(comp(A, Dbinv, Ainv, Db)(x))[0] / (-F(x)[0])
        kjm.append(abs(F(comp(A, Dbinv, Ainv, Db)(x))[1] / (-F(x)[1]) - kjc))
    # s^4 = eps J_c^-1 at fixed tau, so k_{s^4} = k_eps / k_{J_c} and k_eps = k_{s^4} k_{J_c}
    k_eps = k4s * kjc
    # the relation word (s l)^3 s^-2 in product order; the rightmost letter acts first
    word = ["s", "l", "s", "l", "s", "l", "si", "si"]
    gam = {"l": lambda t: t + 1, "s": lambda t: -1 / t, "si": lambda t: -1 / t}
    kfun = {"l": k_l, "s": k_s, "si": lambda t: 1 / k_s(-1 / t)}
    gmat = {"l": GL, "s": GS, "si": inv2(GS)}
    rel = []
    for tau in TAUS:
        t, kw, gw = tau, mp.mpc(1), ONE
        for e in reversed(word):
            kw = kfun[e](t) * kw
            gw = gmat[e] * gw
            t = gam[e](t)
        rel.append((kw, gw, abs(t - tau)))
    rel_ok = all(dtau < TOL and mnorm(kw * gw - ONE) < TOL for kw, gw, dtau in rel)
    sgn = [mp.nstr(mp.re(gw[0, 0] / ONE[0, 0]) if mnorm(gw - ONE) < TOL or mnorm(gw + ONE) < TOL else mp.nan, 3)
           for kw, gw, _ in rel]
    out = {"max conjugation residual (5)": mp.nstr(max(conj), 3), "D_c = C residual": mp.nstr(max(dc), 3),
           "max F-law residual": mp.nstr(max(flaws), 3), "k^2 = j mu residuals (l, s, s^4)": mp.nstr(max(kjm), 3),
           "k_{s^4}": mp.nstr(k4s, 6), "k_{J_c}": mp.nstr(kjc, 6), "k_eps": mp.nstr(k_eps, 6),
           "relation word (sl)^3 s^-2: g-part sign, and k g = 1": {"g-part": sgn, "k g = 1": rel_ok}}
    ok = (max(conj) < TOL and max(dc) < TOL and max(flaws) < TOL and max(kjm) < TOL
          and abs(k4s + 1) < TOL and abs(kjc - 1) < TOL and abs(k_eps + 1) < TOL and rel_ok)
    return out, ok


# ---------------------------------------------------------------- B1
def B1():
    rows, ok = [], True
    for tau in TAUS:
        v, d = N(0, tau), dth1(0, tau)
        bb = v / mp.sqrt(d)
        par = max(vdist(N(-z, tau), N(z, tau)) for z in ZS) + max(abs(th(1, -z, tau) + th(1, z, tau)) for z in ZS)
        sc = []
        for r in (mp.mpf("1e-3"), mp.mpf("1e-4")):
            z = r * mp.exp(I * mp.mpf("0.7"))
            sc.append((max(abs(N(z, tau)[k] - v[k]) for k in range(2)) / r ** 2,
                       abs(th(1, z, tau) / (d * z) - 1) / r ** 2))
        ratio = [sc[1][k] / sc[0][k] for k in range(2)]
        good = par < TOL and all(mp.mpf("0.9") < q < mp.mpf("1.1") for q in ratio) and mp.norm(bb) > mp.mpf("0.1")
        ok = ok and good
        rows.append({"tau": mp.nstr(tau, 4), "parity residual": mp.nstr(par, 3),
                     "O(z^2) ratios between z = 1e-3 and 1e-4": [mp.nstr(q, 6) for q in ratio],
                     "|b|": mp.nstr(mp.norm(bb), 6)})
    return {"per tau": rows}, ok


# ---------------------------------------------------------------- B2
EPS = np.array([[0, 1], [-1, 0]], dtype=complex)


def bvec(tau):
    v, d = N(0, tau), dth1(0, tau)
    bb = v / mp.sqrt(d)
    return np.array([complex(bb[0]), complex(bb[1])])


def delta_matrix(nrow, dscale=1.0):
    """C^6 = C^3 (copies) x C^2 (doublet), index 2p + s; delta(u)_p = nrow^T eps u_p / dscale"""
    D = np.zeros((3, 6), dtype=complex)
    row = nrow @ EPS
    for p in range(3):
        D[p, 2 * p:2 * p + 2] = row / dscale
    return D


def rank(M, tol=1e-9):
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * max(1.0, s[0])))


def B2():
    bb = bvec(TAUS[0])
    D = delta_matrix(bb)
    U = np.kron(np.eye(3), bb.reshape(2, 1))
    c = EPS.T @ bb.conj()
    Up = np.kron(np.eye(3), c.reshape(2, 1))
    checks = {"rank delta = 3": rank(D) == 3, "delta U = 0": bool(np.abs(D @ U).max() < 1e-12),
              "U perp = C3 x span(eps^T conj b) (Hermitian orthogonal, dim 3)":
                  bool(np.abs(U.conj().T @ Up).max() < 1e-12) and rank(Up) == 3}
    table = {}
    for name, Z in (("0", np.zeros((6, 0), dtype=complex)), ("C6", np.eye(6, dtype=complex)), ("U", U),
                    ("U perp", Up)):
        r = rank(D @ Z) if Z.shape[1] else 0
        d = Z.shape[1]
        table[name] = [d - r, 3 - r]
    rng = np.random.default_rng(144)
    green = []
    for d in range(7):
        for _ in range(3):
            Z = rng.normal(size=(6, d)) + 1j * rng.normal(size=(6, d))
            r = rank(D @ Z) if d else 0
            UZ = np.hstack([U, Z]) if d else U
            lhs = 6 - rank(UZ)
            green.append((d, r, lhs, lhs == 3 - r, r == min(d, 3)))
    for name, Z in (("U", U), ("U perp", Up), ("C6", np.eye(6, dtype=complex))):
        r = rank(D @ Z)
        green.append((name, r, 6 - rank(np.hstack([U, Z])), 6 - rank(np.hstack([U, Z])) == 3 - r, None))
    ok = (all(checks.values()) and table == {"0": [0, 3], "C6": [3, 0], "U": [3, 3], "U perp": [0, 0]}
          and all(g[3] for g in green) and all(g[4] in (True, None) for g in green))
    return {"checks": checks, "kernel table (positive, adjoint)": table,
            "Green control rows (d, r, dim(U perp cap Lambda perp), = 3 - r, generic r = min(d, 3))":
                [list(map(str, g)) for g in green]}, ok


# ---------------------------------------------------------------- C1 and C2
def Oad(g):
    """Ad_g on the imaginary quaternions, basis (i, j, k): g q_n g^-1 = sum_m O_mn q_m"""
    Q = [QI, QJ, QK]
    gi = inv2(g)
    O = mp.matrix(3, 3)
    for n_ in range(3):
        X = g * Q[n_] * gi
        for m in range(3):
            O[m, n_] = -(Q[m] * X)[0, 0] - (Q[m] * X)[1, 1]
            O[m, n_] = O[m, n_] / 2
    return O


def kron(Aa, Bb):
    out = mp.matrix(Aa.rows * Bb.rows, Aa.cols * Bb.cols)
    for i1 in range(Aa.rows):
        for j1 in range(Aa.cols):
            for i2 in range(Bb.rows):
                for j2 in range(Bb.cols):
                    out[i1 * Bb.rows + i2, j1 * Bb.cols + j2] = Aa[i1, j1] * Bb[i2, j2]
    return out


EPSM = mp.matrix([[0, 1], [-1, 0]])


def Imap(n):
    """x in C^3 -> x tensor n in C^6"""
    out = mp.matrix(6, 3)
    for p in range(3):
        out[2 * p, p], out[2 * p + 1, p] = n[0], n[1]
    return out


def Dmap(n, d):
    row = (n.T * EPSM)
    out = mp.matrix(3, 6)
    for p in range(3):
        out[p, 2 * p], out[p, 2 * p + 1] = row[0, 0] / d, row[0, 1] / d
    return out


def transported(e, tau, zy):
    """the transported point (tau', z'), r_e(y), k_e, g_e, j_e for e = l, s, Ja, Jb"""
    if e == "l":
        return tau + 1, zy, ALPHA0, k_l(tau), GL, mp.mpc(1)
    if e == "s":
        r = BETA0 * mp.power(tau, mp.mpf(1) / 4) * mp.exp(I * mp.pi * zy ** 2 / (2 * tau))
        return -1 / tau, zy / tau, r, k_s(tau), GS, mp.sqrt(tau)
    if e == "Ja":
        return tau, zy + 1, I, mp.mpc(1), QI, mp.mpc(1)
    if e == "Jb":
        return tau, zy - tau, -1 / (I * t_(zy - tau, tau)), mp.mpc(1), QJ, mp.mpc(1)


def C1C2():
    dres, nres, maps9, green, rdiff = [], [], [], [], []
    rng = np.random.default_rng(1440)
    for tau in TAUS:
        for (m, n_) in LIFTS:
            zy = m + n_ * tau
            ny, dy = N(zy, tau), dth1(zy, tau)
            for e in ("l", "s", "Ja", "Jb"):
                tp, zp, r, k, g, j = transported(e, tau, zy)
                n2, d2 = N(zp, tp), dth1(zp, tp)
                dres.append(abs(d2 - j ** 2 * r ** 2 * dy) / abs(dy))
                nres.append(vdist(n2, r * k * (g * ny)))
                if e == "s" and (m, n_) != (0, 0):
                    rdiff.append(abs(r - k))
                if e in ("l", "s"):
                    O = Oad(g)
                    Ae = O / k
                    Me = kron(O, g) * r
                    Ce = O * (k / j ** 2)
                    maps9.append(mp.mnorm(Imap(n2) * Ae - Me * Imap(ny), 1) / mp.mnorm(Imap(ny), 1))
                    maps9.append(mp.mnorm(Dmap(n2, d2) * Me - Ce * Dmap(ny, dy), 1) / mp.mnorm(Dmap(ny, dy), 1))
                    # the Green form (11) under u -> j r B u, v -> conj(j r) B v
                    Be = kron(O, g)
                    for _ in range(2):
                        vecs = [mp.matrix([complex(x) for x in rng.normal(size=6) + 1j * rng.normal(size=6)])
                                for _ in range(4)]
                        u, v, u2, v2 = vecs
                        G0 = (u.H * v2)[0, 0] / mp.conj(dy) + (v.H * u2)[0, 0] / dy
                        tu, tv = Be * u * (j * r), Be * v * mp.conj(j * r)
                        tu2, tv2 = Be * u2 * (j * r), Be * v2 * mp.conj(j * r)
                        G1 = (tu.H * tv2)[0, 0] / mp.conj(d2) + (tv.H * tu2)[0, 0] / d2
                        green.append(abs(G1 - G0) / abs(G0))
    # r on eps, J_c, s^4 and the product law, at the lifts
    rsp = []
    for tau in TAUS:
        for (m, n_) in LIFTS:
            zy = m + n_ * tau
            y = (tau, zy, mp.mpc(1))                       # w-multiplier read on a unit w
            r4 = comp(Sm, Sm, Sm, Sm)(y)[2]
            rc = comp(A, Dbinv, Ainv, Db)(y)[2]
            tp, zp, r1, _, _, _ = transported("s", tau, zy)
            _, _, r2, _, _, _ = transported("s", tp, zp)
            rsp += [abs(r4 + 1), abs(rc + 1), abs(r2 * r1 + I)]
    # the epsilon and J_c checks
    g_eps, g_jc = -ONE, -ONE                              # g_eps = -1, g_{J_c} = rho(c) = -1
    Oe = Oad(g_eps)
    I3, I6 = mp.eye(3), mp.eye(6)
    eps_A, eps_C, eps_M = Oe / (-1), Oe * ((-1) / (-1) ** 2), kron(Oe, g_eps) * 1
    jc_A, jc_C, jc_M = Oad(g_jc) / 1, Oad(g_jc) * 1, kron(Oad(g_jc), g_jc) * (-1)
    jc_M_without_r = kron(Oad(g_jc), g_jc)
    ny = N(TAUS[0], TAUS[0])                                # a lift (0, 1); C fixes z, so n is unchanged
    without_r = mp.mnorm(Imap(ny) * jc_A - jc_M_without_r * Imap(ny), 1) / mp.mnorm(Imap(ny), 1)
    spin = {"A_spin at eps": mp.mnorm(Oe * ((-1) / (-1)) - I3, 1),
            "M_spin at eps": mp.mnorm(kron(Oe, g_eps) * ((-1) * 1) - I6, 1),
            "C_spin at eps": mp.mnorm(Oe * ((-1) / (-1)) - I3, 1)}
    epsjc = {"eps: A + I3, C + I3, M + I6": [mp.nstr(mp.mnorm(eps_A + I3, 1), 3), mp.nstr(mp.mnorm(eps_C + I3, 1), 3),
                                              mp.nstr(mp.mnorm(eps_M + I6, 1), 3)],
             "J_c: A - I3, C - I3, M - I6": [mp.nstr(mp.mnorm(jc_A - I3, 1), 3), mp.nstr(mp.mnorm(jc_C - I3, 1), 3),
                                             mp.nstr(mp.mnorm(jc_M - I6, 1), 3)],
             "J_c without r: the square's relative residual (2 means a sign)": mp.nstr(without_r, 6)}
    c1 = {"d transport residual": mp.nstr(max(dres), 3), "n transport residual": mp.nstr(max(nres), 3),
          "least |r_s - k_s| off the zero lift": mp.nstr(min(rdiff), 6),
          "r_{s^4} + 1, r_{J_c} + 1, r_s(P_s y) r_s(y) + i: max": mp.nstr(max(rsp), 3)}
    c1_ok = max(dres) < TOL and max(nres) < TOL and min(rdiff) > mp.mpf("1e-3") and max(rsp) < TOL
    c2 = {"(9) residuals, max": mp.nstr(max(maps9), 3), "Green form (11) residual, max": mp.nstr(max(green), 3),
          "eps and J_c": epsjc, "spin maps at eps": {k: mp.nstr(v, 3) for k, v in spin.items()}}
    c2_ok = (max(maps9) < TOL and max(green) < TOL
             and all(mp.mnorm(x, 1) < TOL
                     for x in (eps_A + I3, eps_C + I3, eps_M + I6, jc_A - I3, jc_C - I3, jc_M - I6))
             and abs(without_r - 2) < TOL and all(v < TOL for v in spin.values()))
    return c1, c1_ok, c2, c2_ok


# ---------------------------------------------------------------- D1
def D1():
    rng = np.random.default_rng(1441)
    rows, ok = [], True
    for d in range(7):
        Q, _ = np.linalg.qr(rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6)))
        P = Q[:, :d] @ Q[:, :d].conj().T
        R = 0.5 * np.eye(6) - P
        R0 = R - np.trace(R) / 6 * np.eye(6)
        hol = sl.expm(-2j * np.pi * R)
        ev = np.sort(np.linalg.eigvals(R).real)
        reg = np.abs(R0).max() < 1e-12
        good = (reg == (d in (0, 6)) and np.abs(hol + np.eye(6)).max() < 1e-10
                and abs(-np.trace(R).real - (d - 3)) < 1e-12)
        if d == 3:
            good = good and np.allclose(ev, [-0.5] * 3 + [0.5] * 3)
        ok = ok and good
        rows.append({"d": d, "projectively regular": bool(reg), "degree -tr R": round(-np.trace(R).real, 12),
                     "holonomy -I6": bool(np.abs(hol + np.eye(6)).max() < 1e-10)})
    scal = {q: -6 * (Fr(1, 2) - q) for q in range(-2, 4)}
    scal_ok = all(v == -3 + 6 * q for q, v in scal.items())
    # E6 = E0(p): the two extreme residues differ by a scalar
    diff = (0.5 * np.eye(6) - np.eye(6)) - 0.5 * np.eye(6)
    extremes_ok = np.allclose(diff, -np.eye(6))
    # the commutant of I3 x rho
    qi = np.array([[1j, 0], [0, -1j]])
    qj = np.array([[0, 1], [-1, 0]], dtype=complex)
    gens = [np.kron(np.eye(3), qi), np.kron(np.eye(3), qj)]
    rowsM = []
    for G in gens:
        rowsM.append(np.kron(np.eye(6), G) - np.kron(G.T, np.eye(6)))
    K = np.vstack(rowsM)
    s = np.linalg.svd(K, compute_uv=False)
    dimc = int(np.sum(s < 1e-10))
    ok = ok and scal_ok and extremes_ok and dimc == 9
    return {"ranks": rows, "scalar residue 1/2 - q gives degree -3 + 6q": scal_ok,
            "the two extremes differ by a scalar residue": bool(extremes_ok), "commutant of I3 x rho": dimc}, ok


# ---------------------------------------------------------------- E1 and E2
def e8_roots():
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [Fr(0)] * 8
                v[i], v[j] = Fr(si), Fr(sj)
                roots.append(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(Fr(s, 2) for s in signs))
    return roots


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def coweights(simple):
    """the vectors in span(simple) with <alpha_m, w_k> = delta_mk (simply laced, roots of norm 2)"""
    n = len(simple)
    G = sp.Matrix(n, n, lambda i, j: sp.Rational(dot(simple[i], simple[j])))
    Gi = G.inv()
    out = []
    for k in range(n):
        w = [Fr(0)] * 8
        for m in range(n):
            coef = Gi[m, k]
            cf = Fr(int(coef.p), int(coef.q))
            w = [x + cf * y for x, y in zip(w, simple[m])]
        out.append(tuple(w))
    return out


def E1E2():
    roots = e8_roots()
    e = lambda i: tuple(Fr(1) if k == i else Fr(0) for k in range(8))
    sub = lambda u, v: tuple(x - y for x, y in zip(u, v))
    add = lambda u, v: tuple(x + y for x, y in zip(u, v))
    a1 = tuple(Fr(s, 2) for s in (1, -1, -1, -1, -1, -1, -1, 1))
    a2 = add(e(0), e(1))
    a3, a4, a5, a6, a7, a8 = (sub(e(k), e(k - 1)) for k in range(1, 7))
    theta = add(e(6), e(7))
    a0 = tuple(-x for x in theta)
    marks = {"a1": 2, "a2": 3, "a3": 4, "a4": 6, "a5": 5, "a6": 4, "a7": 3, "a8": 2}
    simple8 = [a1, a2, a3, a4, a5, a6, a7, a8]
    theta_check = tuple(sum(Fr(m) * s[k] for m, s in zip(marks.values(), simple8)) for k in range(8)) == theta
    A5 = [a5, a6, a7, a8, a0]                                       # a chain: a5-a6-a7-a8-a0
    A2 = [a1, a3]
    A1 = [a2]
    chain_ok = (all(dot(A5[k], A5[k + 1]) == -1 for k in range(4)) and dot(a1, a3) == -1
                and all(dot(x, y) == 0 for x in A5 for y in A2 + A1) and all(dot(x, y) == 0 for x in A2 for y in A1))
    w5 = coweights(A5)[0]                                           # an end node: generates the centre of SU(6)
    w3 = coweights(A2)[0]
    w2 = coweights(A1)[0]
    kernel = []
    for (p, q, r) in itertools.product(range(6), range(3), range(2)):
        H = tuple(p * x + q * y + r * zz for x, y, zz in zip(w5, w3, w2))
        if all(dot(al, H).denominator == 1 for al in roots):
            kernel.append((p, q, r))
    gens = [k for k in kernel if k[0] in (1, 5) and k[1] in (1, 2) and k[2] == 1]
    H3 = tuple(3 * x for x in w5)
    minus = sum(1 for al in roots if dot(al, H3).denominator != 1)
    H31 = tuple(3 * x + y for x, y in zip(w5, w2))
    classes = {}
    for al in roots:
        key = (dot(al, w5) % 1, dot(al, w3) % 1, dot(al, w2) % 1)
        classes[key] = classes.get(key, 0) + 1
    sizes = sorted(v + (8 if k == (0, 0, 0) else 0) for k, v in classes.items())
    e1 = {"highest root = sum of marks x simple roots": theta_check, "A5 + A2 + A1 from the extended diagram": chain_ok,
          "kernel (p, q, r) in Z6 x Z3 x Z2": [list(k) for k in kernel],
          "generators of orders (6, 3, 2)": [list(k) for k in gens],
          "(-I6, I3, -I2) = (3, 0, 1) in K": (3, 0, 1) in kernel, "(-I6, I3, I2) = (3, 0, 0) in K": (3, 0, 0) in kernel,
          "roots on which (3, 0, 0) is -1": minus,
          "(3, 0, 1) trivial on every root": all(dot(al, H31).denominator == 1 for al in roots),
          "classes by (6-ality, 3-ality, 2-ality), with the Cartan in the trivial one": sizes}
    e1_ok = (theta_check and chain_ok and len(kernel) == 6 and len(gens) >= 1 and (3, 0, 1) in kernel
             and (3, 0, 0) not in kernel and minus == 112 and sizes == sorted([46, 40, 45, 45, 36, 36]))
    # E2: the compensation in the product group, and rho tensor rho
    qi = np.array([[1j, 0], [0, -1j]])
    qj = np.array([[0, 1], [-1, 0]], dtype=complex)
    i6, j6 = np.kron(np.eye(3), qi), np.kron(np.eye(3), qj)
    comm6 = i6 @ j6 @ np.linalg.inv(i6) @ np.linalg.inv(j6)
    comm2 = qi @ qj @ np.linalg.inv(qi) @ np.linalg.inv(qj)
    sq_ok = np.allclose(i6 @ i6, -np.eye(6)) and np.allclose(qi @ qi, -np.eye(2)) and np.allclose(j6 @ j6, -np.eye(6))
    comm_ok = np.allclose(comm6, -np.eye(6)) and np.allclose(comm2, -np.eye(2))
    X, Y = np.kron(qi, qi), np.kron(qj, qj)
    rr = {"commute": bool(np.allclose(X @ Y, Y @ X)), "square to 1": bool(np.allclose(X @ X, np.eye(4))
                                                                          and np.allclose(Y @ Y, np.eye(4))),
          "traces (X, Y, XY)": [round(abs(np.trace(M)), 12) for M in (X, Y, X @ Y)]}
    w, V = np.linalg.eig(X + 2 * Y)                                  # joint eigenvalues read off one combination
    chars = sorted((int(round(np.real(x))) for x in w))
    rr["X + 2Y eigenvalues (four characters, once each)"] = chars
    Kc = np.vstack([np.kron(np.eye(2), G) - np.kron(G.T, np.eye(2)) for G in (qi, qj)])
    dimc = int(np.sum(np.linalg.svd(Kc, compute_uv=False) < 1e-10))
    e2 = {"commutator and squares are (-I6, I3, -I2)": bool(sq_ok and comm_ok), "in K (from E1)": (3, 0, 1) in kernel,
          "rho tensor rho": rr, "commutant of {i, j} in M2": dimc}
    e2_ok = (sq_ok and comm_ok and (3, 0, 1) in kernel and rr["commute"] and rr["square to 1"]
             and rr["traces (X, Y, XY)"] == [0.0, 0.0, 0.0] and chars == [-3, -1, 1, 3] and dimc == 1)
    return e1, e1_ok, e2, e2_ok


def main():
    t0 = time.time()
    res, cells = {}, {}
    for name, fn in (("A1", A1), ("A2", A2), ("A3", A3), ("A4", A4), ("B1", B1), ("B2", B2)):
        res[name], cells[name] = fn()
    c1, cells["C1"], c2, cells["C2"] = C1C2()
    res["C1"], res["C2"] = c1, c2
    res["D1"], cells["D1"] = D1()
    e1, cells["E1"], e2, cells["E2"] = E1E2()
    res["E1"], res["E2"] = e1, e2
    out = {"arc": "W144", "rule": "W144_RULE.md", "cells": {k: bool(v) for k, v in cells.items()}, **res,
           "seconds": round(time.time() - t0, 1)}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"cells": out["cells"], "seconds": out["seconds"]}, indent=1))


if __name__ == "__main__":
    main()
