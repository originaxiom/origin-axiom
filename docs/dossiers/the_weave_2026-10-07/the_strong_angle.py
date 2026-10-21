#!/usr/bin/env python3
"""W113 -- the strong angle at every tau: which quark assignments make theta-bar constant without tuning, and does the
CKM phase survive there?  The rule is W113_RULE.md, committed and pushed before this script.  One run; its output
(the_strong_angle.json, the_strong_angle_run.txt) is committed before it is read.

Pre-run disclosure.  While the script was written, its parts were run in scratch on control cases only, to find
coding errors:
  - the T (x) T and mixed-type spaces, whose dimensions and weight-one determinant are on record (B1635, B1671);
  - the fit machinery on synthetic data in the T (x) T weight-3 space;
  - the tuned-variety code path on the T (x) T weight-3 space (w = 6, not a cell: its roots are det = 0 members).
  Three fixes came from those tests: an exact cubic for the variety's lines, a scaled root search, and skipping a
  root where a line meets the origin.
No Tbar (x) Tbar space, no candidate's spectrum, J or fit, and no tuned variety was computed before the run.

The construction (the rule's).  u = (theta_2^2, theta_3^2, theta_4^2), with Jacobi's u_2^2 = u_1^2 + u_3^2.
  u(tau + 1) = A_T u, u(-1/tau) = tau A_S u, with A_T u = (i u1, u3, u2) and A_S u = (-i u3, -i u2, -i u1).
  A sector with hands (sL, sR) (+1 for T, -1 for Tbar) has W = eta^m Y, a 3x3 matrix of polynomials of degree
  k + m/2, with W(A u) = A_L W A_R^T, A_s = conj(A) for s = +1 and A for s = -1, and every entry O(q^(m/24)).
  m = 18 (T T), 6 (Tbar Tbar), 0 (mixed).  The determinant character exponent is a = 6, 18, 0.

Layers (the rule's cells): F0-F4 the census; C1-C6 the candidate; T1-T3 the tuned assignments.
"""
import itertools
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.optimize import minimize
from sympy import QQ, QQ_I
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
mp.mp.dps = 30
T0 = time.time()

ZI = QQ_I
ONE, ZERO = ZI(1), ZI(0)
TYPES = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
NAME = {(1, 1): "T(x)T", (-1, -1): "Tbar(x)Tbar", (1, -1): "mixed (Q in T)", (-1, 1): "mixed (Q in Tbar)"}
M_ETA = {(1, 1): 18, (-1, -1): 6, (1, -1): 0, (-1, 1): 0}
A_CHAR = {(1, 1): 6, (-1, -1): 18, (1, -1): 0, (-1, 1): 0}
WEIGHTS = {(1, 1): [1, 3, 5, 7], (-1, -1): [1, 3, 5, 7], (1, -1): [0, 2, 4, 6], (-1, 1): [0, 2, 4, 6]}
K_AUTO = {(1, 1): 1, (-1, -1): 3, (1, -1): 0, (-1, 1): 0}
K_TUNED = {(1, 1): 5, (-1, -1): 7, (1, -1): 4, (-1, 1): 4}
TMAX = 40
GENERIC5 = [complex(0.17, 1.13), complex(0.31, 0.97), complex(-0.23, 1.41), complex(0.137, 1.291), complex(0.05, 1.7)]
F2_TAUS = [complex(0.137, 1.291), complex(-0.284, 2.173), complex(0.41, 0.95), complex(0.05, 1.7),
           complex(-0.33, 1.02), complex(0.21, 1.07)]
OMEGA = complex(-0.5, math.sqrt(3) / 2)
ELLIPTIC = [1j, OMEGA, OMEGA + 1]
PASS = 5.99
ZERO_OBS = 1e-12


def log(*a):
    print(f"[{time.time() - T0:8.1f}s]", *a, flush=True)


def iszero(z):
    return z.x == 0 and z.y == 0


def zconj(z):
    return ZI(z.x, -z.y)


def zc(z):
    return complex(float(Fraction(int(z.x.numerator), int(z.x.denominator))),
                   float(Fraction(int(z.y.numerator), int(z.y.denominator))))


def zmp(z):
    return mp.mpc(mp.mpf(int(z.x.numerator)) / int(z.x.denominator), mp.mpf(int(z.y.numerator)) / int(z.y.denominator))


# ------------------------------------------------------------------------------------------- polynomials in u
# (A u)_i = factor * u_target, for i = 0, 1, 2 (u1, u2, u3)
AMAP = {"S": [(2, ZI(0, -1)), (1, ZI(0, -1)), (0, ZI(0, -1))],
        "T": [(0, ZI(0, 1)), (2, ONE), (1, ONE)]}


def amat(g, conj):
    M = [[ZERO] * 3 for _ in range(3)]
    for i, (j, f) in enumerate(AMAP[g]):
        M[i][j] = zconj(f) if conj else f
    return M


def reduce_(p, zero_test):
    """normal form modulo u2^2 = u1^2 + u3^2 (u2 exponent <= 1); keys (a, b, c) or longer tuples (u part first)"""
    out = {}
    stack = list(p.items())
    while stack:
        key, x = stack.pop()
        if zero_test(x):
            continue
        a, b, c = key[0], key[1], key[2]
        if b >= 2:
            rest = key[3:]
            stack.append(((a + 2, b - 2, c) + rest, x))
            stack.append(((a, b - 2, c + 2) + rest, x))
            continue
        out[key] = out[key] + x if key in out else x
    return {k: v for k, v in out.items() if not zero_test(v)}


def normal_monomials(d):
    if d < 0:
        return []
    return [(a, 0, d - a) for a in range(d + 1)] + [(a, 1, d - 1 - a) for a in range(d)]


def subst(mon, g):
    coef, new = ONE, [0, 0, 0]
    for i, e in enumerate(mon):
        j, f = AMAP[g][i]
        for _ in range(e):
            coef = coef * f
        new[j] += e
    return reduce_({tuple(new): coef}, iszero)


def smul(a, b):
    out = [0] * (TMAX + 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j in range(TMAX + 1 - i):
            if b[j]:
                out[i + j] += x * b[j]
    return out


def u_series():
    th2, th3, th4 = [0] * (TMAX + 1), [0] * (TMAX + 1), [0] * (TMAX + 1)
    n = 0
    while (2 * n + 1) ** 2 <= TMAX:
        th2[(2 * n + 1) ** 2] += 2
        n += 1
    th3[0] = th4[0] = 1
    n = 1
    while 4 * n * n <= TMAX:
        th3[4 * n * n] += 2
        th4[4 * n * n] += 2 * (-1) ** n
        n += 1
    return [smul(th2, th2), smul(th3, th3), smul(th4, th4)]


USER = u_series()
_MS = {}


def mon_series(mon):
    if mon not in _MS:
        s = [1] + [0] * TMAX
        for i, e in enumerate(mon):
            for _ in range(e):
                s = smul(s, USER[i])
        _MS[mon] = s
    return _MS[mon]


# ------------------------------------------------------------------------------------------- the equivariant spaces
def space(sL, sR, k):
    """exact basis (over Q(i)) of the couplings of type (sL, sR) and weight k, as 3x3 lists of {monomial: coef}"""
    m = M_ETA[(sL, sR)]
    d = k + m // 2
    mons = normal_monomials(d)
    nm = len(mons)
    if nm == 0:
        return [], d
    idx = {mon: n for n, mon in enumerate(mons)}

    def var(i, j, n):
        return (3 * i + j) * nm + n

    rows = []
    for g in ("S", "T"):
        AL, AR = amat(g, sL == 1), amat(g, sR == 1)
        sub = [subst(mon, g) for mon in mons]
        for i in range(3):
            for j in range(3):
                eq = [dict() for _ in range(nm)]
                for mi, p in enumerate(sub):
                    for key, val in p.items():
                        e = eq[idx[key]]
                        v = var(i, j, mi)
                        e[v] = e[v] + val if v in e else val
                for kk in range(3):
                    if iszero(AL[i][kk]):
                        continue
                    for ll in range(3):
                        if iszero(AR[j][ll]):
                            continue
                        f = AL[i][kk] * AR[j][ll]
                        for n in range(nm):
                            v = var(kk, ll, n)
                            eq[n][v] = eq[n][v] - f if v in eq[n] else ZERO - f
                rows.extend(eq)
    ser = [mon_series(mon) for mon in mons]
    for i in range(3):
        for j in range(3):
            for p in range(m // 3):
                eq = {var(i, j, mi): ZI(ser[mi][p]) for mi in range(nm) if ser[mi][p] != 0}
                if eq:
                    rows.append(eq)
    sdm = {}
    for r, eq in enumerate(rows):
        clean = {v: x for v, x in eq.items() if not iszero(x)}
        if clean:
            sdm[len(sdm)] = clean
    M = DomainMatrix(sdm, (len(sdm), 9 * nm), ZI)
    ns = M.nullspace().to_list()
    basis = []
    for vec in ns:
        W = [[{} for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for n in range(nm):
                    x = vec[var(i, j, n)]
                    if not iszero(x):
                        W[i][j][mons[n]] = x
        basis.append(W)
    return basis, d


def flatten(W, mons_index, nm):
    v = [ZERO] * (9 * nm)
    for i in range(3):
        for j in range(3):
            for mon, x in W[i][j].items():
                v[(3 * i + j) * nm + mons_index[mon]] = x
    return v


def zrank(vectors, ncols):
    if not vectors:
        return 0
    sdm = {}
    for r, vec in enumerate(vectors):
        row = {c: x for c, x in enumerate(vec) if not iszero(x)}
        if row:
            sdm[len(sdm)] = row
    if not sdm:
        return 0
    return DomainMatrix(sdm, (len(sdm), ncols), ZI).rank()


def real_basis(basis, d):
    """closure under conjugation, and a real (rational) basis spanning the same complex space"""
    if not basis:
        return True, []
    mons = normal_monomials(d)
    nm = len(mons)
    idx = {mon: n for n, mon in enumerate(mons)}
    vecs = [flatten(W, idx, nm) for W in basis]
    conj = [[zconj(x) for x in v] for v in vecs]
    closed = zrank(vecs + conj, 9 * nm) == len(vecs)
    sdm = {}
    for v in vecs:
        for part in (0, 1):
            row = {c: QQ(int((x.x if part == 0 else x.y).numerator), int((x.x if part == 0 else x.y).denominator))
                   for c, x in enumerate(v) if (x.x if part == 0 else x.y) != 0}
            if row:
                sdm[len(sdm)] = row
    R = DomainMatrix(sdm, (len(sdm), 9 * nm), QQ)
    rref, piv = R.rref()
    rows = rref.to_list()[:len(piv)]
    out = []
    for row in rows:
        W = [[{} for _ in range(3)] for _ in range(3)]
        for c, x in enumerate(row):
            if x != 0:
                i, rem = divmod(c, 3 * nm)
                j, n = divmod(rem, nm)
                W[i][j][mons[n]] = Fraction(int(x.numerator), int(x.denominator))
        out.append(W)
    return closed and len(out) == len(basis), out


def sym_split(basis, d):
    mons = normal_monomials(d)
    nm = len(mons)
    idx = {mon: n for n, mon in enumerate(mons)}
    S, A = [], []
    for W in basis:
        WT = [[W[j][i] for j in range(3)] for i in range(3)]
        v, vt = flatten(W, idx, nm), flatten(WT, idx, nm)
        S.append([a + b for a, b in zip(v, vt)])
        A.append([a - b for a, b in zip(v, vt)])
    return zrank(S, 9 * nm), zrank(A, 9 * nm)


# ------------------------------------------------------------------------------------------- evaluation (mpmath)
def thetas_mp(tau):
    tau = mp.mpc(tau)
    y = tau.imag
    N = int(mp.sqrt(130 / y)) + 6
    t2 = t3 = t4 = mp.mpc(0)
    for n in range(-N, N + 1):
        t2 += mp.exp(1j * mp.pi * tau * (n + mp.mpf(1) / 2) ** 2)
        e = mp.exp(1j * mp.pi * tau * n * n)
        t3 += e
        t4 += e if n % 2 == 0 else -e
    return t2, t3, t4


def eta_mp(tau):
    tau = mp.mpc(tau)
    N = int(mp.sqrt(130 / tau.imag) / 6) + 6
    s = mp.mpc(0)
    for n in range(-N, N + 1):
        term = mp.exp(1j * mp.pi * tau * (6 * n + 1) ** 2 / 12)
        s += term if n % 2 == 0 else -term
    return s


def eis_mp(tau, k):
    q = mp.exp(2j * mp.pi * mp.mpc(tau))
    c = {4: 240, 6: -504}[k]
    s, qn = mp.mpc(1), mp.mpc(1)
    for n in range(1, 80):
        qn *= q
        s += c * sum(mp.mpf(dd) ** (k - 1) for dd in range(1, n + 1) if n % dd == 0) * qn
    return s


def u_mp(tau):
    t2, t3, t4 = thetas_mp(tau)
    return [t2 ** 2, t3 ** 2, t4 ** 2]


def poly_mp(p, u, conv):
    s = mp.mpc(0)
    for (a, b, c), x in p.items():
        s += conv(x) * u[0] ** a * u[1] ** b * u[2] ** c
    return s


def to_mpq(x):
    if isinstance(x, Fraction):
        return mp.mpf(x.numerator) / x.denominator
    return zmp(x)


def Y_mp(W, m, tau, u=None, eta=None):
    u = u_mp(tau) if u is None else u
    eta = eta_mp(tau) if eta is None else eta
    return mp.matrix([[poly_mp(W[i][j], u, to_mpq) / eta ** m for j in range(3)] for i in range(3)])


def combo(basis, coeffs):
    W = [[{} for _ in range(3)] for _ in range(3)]
    for B, c in zip(basis, coeffs):
        for i in range(3):
            for j in range(3):
                for mon, x in B[i][j].items():
                    W[i][j][mon] = W[i][j].get(mon, 0) + c * x
    return W


# ------------------------------------------------------------------------------------------- evaluation (numpy)
NN = np.arange(-12, 13)
SGN = (-1.0) ** NN


def u_eta_np(tau):
    t = np.asarray(tau, dtype=complex).reshape(-1)[:, None]
    th2 = np.exp(1j * np.pi * t * (NN + 0.5) ** 2).sum(1)
    e = np.exp(1j * np.pi * t * NN ** 2)
    th3, th4 = e.sum(1), (e * SGN).sum(1)
    eta = (SGN * np.exp(1j * np.pi * t * (6 * NN + 1) ** 2 / 12)).sum(1)
    return np.stack([th2 ** 2, th3 ** 2, th4 ** 2], 1), eta


class Sector:
    """a real basis evaluated fast: B[N, b, i, j] at many tau"""

    def __init__(self, basis, m, label):
        self.label, self.m, self.dim = label, m, len(basis)
        mons = sorted({mon for B in basis for row in B for p in row for mon in p})
        self.mons = np.array(mons, dtype=int).reshape(-1, 3)
        self.C = np.zeros((len(basis), 3, 3, len(mons)))
        pos = {mon: n for n, mon in enumerate(mons)}
        for b, B in enumerate(basis):
            for i in range(3):
                for j in range(3):
                    for mon, x in B[i][j].items():
                        self.C[b, i, j, pos[mon]] = float(x)
        self.dmax = int(self.mons.max()) if len(mons) else 0

    def mats(self, U, ETA):
        N = U.shape[0]
        P = np.ones((N, 3, self.dmax + 1), dtype=complex)
        for e in range(1, self.dmax + 1):
            P[:, :, e] = P[:, :, e - 1] * U
        mon = P[:, 0, self.mons[:, 0]] * P[:, 1, self.mons[:, 1]] * P[:, 2, self.mons[:, 2]]
        B = np.einsum("bijm,Nm->Nbij", self.C, mon)
        return B / (ETA ** self.m)[:, None, None, None]

    def Y(self, U, ETA, coeffs):
        B = self.mats(U, ETA)
        c = np.asarray(coeffs, dtype=float)
        if c.ndim == 1:
            return np.einsum("Nbij,b->Nij", B, c)
        return np.einsum("Nbij,Nb->Nij", B, c)


def svd_sorted(Y):
    U, s, _ = np.linalg.svd(Y)
    return U[..., ::-1], s[..., ::-1]


def observables(Yu, Yd):
    Uu, su = svd_sorted(Yu)
    Ud, sd = svd_sorted(Yd)
    V = np.conj(np.swapaxes(Uu, -1, -2)) @ Ud
    with np.errstate(divide="ignore", invalid="ignore"):
        obs = np.stack([su[..., 0] / su[..., 1], su[..., 1] / su[..., 2], sd[..., 0] / sd[..., 1],
                        sd[..., 1] / sd[..., 2], np.abs(V[..., 0, 1]), np.abs(V[..., 1, 2]),
                        np.abs(V[..., 0, 2]), np.abs(V[..., 2, 0])], -1)
    J = (V[..., 0, 1] * V[..., 1, 2] * np.conj(V[..., 0, 2]) * np.conj(V[..., 1, 1])).imag
    return obs, J, su, sd, V


def hier(s):
    """max(m2/m1, m3/m2) with m1 >= m2 >= m3, from ascending singular values"""
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.maximum(s[..., 1] / s[..., 2], s[..., 0] / s[..., 1])


def perm_distance(V):
    A = np.abs(V)
    return min(float(np.max(np.abs(A - np.eye(3)[list(p)]))) for p in itertools.permutations(range(3)))


def to_fd(t):
    t = complex(t)
    for _ in range(300):
        t = complex(t.real - math.floor(t.real + 0.5), t.imag)
        if abs(t) < 1 - 1e-14:
            t = -1 / t
        else:
            break
    return t


def random_tau_F(rng, n, ymax):
    out = []
    while len(out) < n:
        x, y = rng.uniform(-0.5, 0.5), rng.uniform(math.sqrt(3) / 2, ymax)
        if x * x + y * y >= 1:
            out.append(complex(x, y))
    return np.array(out)


# ------------------------------------------------------------------------------------------- data (as W66 forms it)
def load_data():
    hz = json.loads((HERE / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))
    ckm = json.loads((HERE / "received" / "B1612_data.json").read_text(encoding="utf-8"))["ckm_abs"]
    mv, ms = hz["masses_GeV"]["value"], hz["masses_GeV"]["sigma"]
    obs, rel = [], []
    for one, two in (("u", "c"), ("c", "t"), ("d", "s"), ("s", "b")):
        obs.append(mv[one] / mv[two])
        rel.append(float(np.hypot(ms[one] / mv[one], ms[two] / mv[two])))
    for i, j in ((0, 1), (1, 2), (0, 2), (2, 0)):
        obs.append(ckm["value"][i][j])
        rel.append(ckm["sigma"][i][j] / ckm["value"][i][j])
    return np.log(obs), np.array(rel)


LOGD, REL = load_data()
LABELS = ["m_u/m_c", "m_c/m_t", "m_d/m_s", "m_s/m_b", "|V_us|", "|V_cb|", "|V_ub|", "|V_td|"]


def chi2_many(obs, logd, a):
    bad = np.any(~np.isfinite(obs) | (obs < ZERO_OBS), axis=-1)
    with np.errstate(divide="ignore", invalid="ignore"):
        z = (np.log(np.where(obs > 0, obs, 1.0)) - logd) / np.hypot(REL, a)
    c = np.sum(z * z, axis=-1)
    return np.where(bad, np.inf, c)


# ------------------------------------------------------------------------------------------- F layer
def level_one_basis(w, tau):
    if w < 0:
        return []
    E4, E6, D = eis_mp(tau, 4), eis_mp(tau, 6), eta_mp(tau) ** 24
    table = {0: [mp.mpc(1)], 6: [E6], 12: [E4 ** 3, D], 18: [E4 ** 3 * E6, D * E6], 4: [E4], 8: [E4 ** 2],
             10: [E4 * E6], 14: [E4 ** 2 * E6]}
    return table[w]


def det_layer(basis, sL, sR, k, rng):
    """F2: det Y / eta^a in level-one M_w, for a random complex member, at six tau"""
    m, a = M_ETA[(sL, sR)], A_CHAR[(sL, sR)]
    w = 3 * k - a // 2
    coeffs = [ZI(int(rng.integers(-5, 6)), int(rng.integers(-5, 6))) for _ in basis]
    if all(iszero(c) for c in coeffs):
        coeffs[0] = ONE
    W = combo(basis, coeffs)
    gs, rows, scale = [], [], []
    for tau in F2_TAUS:
        u, eta = u_mp(tau), eta_mp(tau)
        Y = Y_mp(W, m, tau, u, eta)
        mx = max(abs(Y[i, j]) for i in range(3) for j in range(3))
        scale.append(mx ** 3)
        gs.append(mp.det(Y) / eta ** a)
        rows.append(level_one_basis(w, tau))
    out = {"w": w, "a": a}
    if w < 0:
        rel = max(abs(g) * abs(eta_mp(t)) ** a / s for g, s, t in zip(gs, scale, F2_TAUS))
        out.update({"det_identically_zero_rel": float(rel), "holds": bool(rel < 1e-20)})
        return out
    A = mp.matrix([[rows[r][c] for c in range(len(rows[0]))] for r in range(len(rows))])
    b = mp.matrix(gs)
    x, res = mp.qr_solve(A, b)
    nb = mp.norm(b)
    relres = float(res / nb) if nb != 0 else float(res)
    coeff = [complex(x[i]) for i in range(len(rows[0]))]
    out.update({"components": [[c.real, c.imag] for c in coeff], "relative_residual": relres})
    ok = relres < 1e-18
    if w == 12 or w == 18:
        mags = [abs(c) for c in coeff]
        out["both_components_nonzero"] = bool(min(mags) > 1e-10 * max(mags))
        ok = ok and out["both_components_nonzero"]
    if w == 0:
        out["pure_for_this_member"] = True
    out["holds"] = bool(ok)
    return out


def classify(sL, sR, k):
    w = 3 * k - A_CHAR[(sL, sR)] // 2
    if w < 0:
        return "det identically 0"
    if w == 0:
        return "automatic"
    if w % 12 == 0:
        return "tuned"
    return "impossible"


def cubic_exact(vals):
    """the exact coefficients (constant first) of the polynomial of degree <= 3 through (s, vals[s]), s = 0..3"""
    M = [[Fraction(s) ** e for e in range(4)] + [Fraction(vals[s])] for s in range(4)]
    for c in range(4):
        piv = next(r for r in range(c, 4) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        for r in range(4):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[e][4] / M[e][e] for e in range(4)]


def u_part_reduce(p):
    return reduce_(p, lambda x: x == 0)


def det_exact_pure(basis, e):
    """F3: det W = kappa(c) (u1 u2 u3)^e exactly, with symbolic real coefficients c (rational basis)"""
    nb = len(basis)

    def entry(i, j):
        out = {}
        for b, B in enumerate(basis):
            for mon, v in B[i][j].items():
                ce = [0] * nb
                ce[b] = 1
                key = tuple(mon) + tuple(ce)
                out[key] = out.get(key, 0) + v
        return out

    def mul(p, q):
        out = {}
        for k1, v1 in p.items():
            for k2, v2 in q.items():
                kk = tuple(x + y for x, y in zip(k1, k2))
                out[kk] = out.get(kk, 0) + v1 * v2
        return u_part_reduce(out)

    E = [[entry(i, j) for j in range(3)] for i in range(3)]
    det = {}
    for perm in itertools.permutations(range(3)):
        sign = 1
        for x in range(3):
            for y in range(x + 1, 3):
                if perm[x] > perm[y]:
                    sign = -sign
        prod = mul(mul(E[0][perm[0]], E[1][perm[1]]), E[2][perm[2]])
        for kk, v in prod.items():
            det[kk] = det.get(kk, 0) + sign * v
    det = {kk: v for kk, v in det.items() if v != 0}
    target = u_part_reduce({(e, e, e): Fraction(1)})
    by_u = {}
    for kk, v in det.items():
        by_u.setdefault(kk[:3], {})[kk[3:]] = v
    n0 = max(target, key=lambda t: abs(target[t]))
    kappa = {ce: v / target[n0] for ce, v in by_u.get(n0, {}).items()}
    ok = bool(kappa)
    for mon in set(by_u) | set(target):
        got = by_u.get(mon, {})
        want = {ce: v * target.get(mon, 0) for ce, v in kappa.items()}
        want = {ce: v for ce, v in want.items() if v != 0}
        if got != want:
            ok = False
            break
    return ok, {"".join(map(str, ce)): str(v) for ce, v in sorted(kappa.items())}


# ------------------------------------------------------------------------------------------- the fit machinery
class Model:
    def __init__(self, su, sd):
        self.su, self.sd = su, sd
        self.nu, self.nd = su.dim, sd.dim

    def unpack(self, p):
        x, y = p[0], p[1]
        cu = np.array(p[2:2 + self.nu], dtype=float)
        cd = np.array(p[2 + self.nu:2 + self.nu + self.nd], dtype=float)
        return complex(x, y), cu, cd

    def at(self, tau, cu, cd):
        U, E = u_eta_np(np.array([tau]))
        Yu = self.su.Y(U, E, cu / np.linalg.norm(cu))
        Yd = self.sd.Y(U, E, cd / np.linalg.norm(cd))
        return Yu[0], Yd[0]

    def eval_point(self, p, ycap):
        tau, cu, cd = self.unpack(p)
        if tau.imag <= 0.05 or np.linalg.norm(cu) < 1e-12 or np.linalg.norm(cd) < 1e-12:
            return None
        tf = to_fd(tau)
        if tf.imag > ycap:
            return None
        Yu, Yd = self.at(tf, cu, cd)
        return tf, observables(Yu[None], Yd[None])

    def many(self, taus, CU, CD):
        U, E = u_eta_np(taus)
        Yu = self.su.Y(U, E, CU / np.linalg.norm(CU, axis=1, keepdims=True))
        Yd = self.sd.Y(U, E, CD / np.linalg.norm(CD, axis=1, keepdims=True))
        return observables(Yu, Yd)


def nm(f, p0, maxfev):
    r = minimize(f, p0, method="Nelder-Mead",
                 options={"maxfev": maxfev, "maxiter": maxfev, "xatol": 1e-10, "fatol": 1e-12, "adaptive": True})
    return r.x, float(r.fun)


def fit(model, logd, a, starts, n2=200, n3=10, maxfev=10000):
    def f(p):
        r = model.eval_point(p, 8.0)
        if r is None:
            return 1e30
        c = chi2_many(r[1][0][0], logd, a)
        return float(c) if np.isfinite(c) else 1e30

    stage2 = [nm(f, p0, maxfev) for p0 in starts[:n2]]
    stage2.sort(key=lambda t: t[1])
    stage3 = [nm(f, p, maxfev) for p, _ in stage2[:n3]]
    stage3.sort(key=lambda t: t[1])
    return stage3[0], [v for _, v in stage2[:10]], f


def readout(model, p, a_used):
    tf, (obs, J, su, sd, V) = model.eval_point(p, 1e9)
    tau, cu, cd = model.unpack(p)
    cu, cd = cu / np.linalg.norm(cu), cd / np.linalg.norm(cd)
    obs = obs[0]
    pulls = ((np.log(obs) - LOGD) / np.hypot(REL, a_used)).tolist()
    delta = min(abs(tf - e) for e in ELLIPTIC)
    return {"tau_in_F": [tf.real, tf.imag], "delta_to_nearest_elliptic_point": float(delta),
            "observables": dict(zip(LABELS, obs.tolist())),
            "data": dict(zip(LABELS, np.exp(LOGD).tolist())), "pulls": dict(zip(LABELS, pulls)),
            "J": float(J[0]), "m_u/m_t": float(obs[0] * obs[1]), "m_d/m_b": float(obs[2] * obs[3]),
            "coefficients_up": cu.tolist(), "coefficients_down": cd.tolist(),
            "perm_distance_of_V": perm_distance(V[0])}


def theta_bit(sec_u, sec_d, basis_u, basis_d, tf, cu, cd, K):
    Wu, Wd = combo(basis_u, [Fraction(float(x)) for x in cu]), combo(basis_d, [Fraction(float(x)) for x in cd])
    u, eta = u_mp(tf), eta_mp(tf)
    r = mp.det(Y_mp(Wu, sec_u.m, tf, u, eta)) * mp.det(Y_mp(Wd, sec_d.m, tf, u, eta)) / eta ** (6 * K)
    return {"det_ratio": [float(r.real), float(r.imag)], "theta_bar": "0" if r.real > 0 else "pi",
            "imag_over_abs": float(abs(r.imag) / abs(r))}


# ------------------------------------------------------------------------------------------- main
def tuned_points(S, rb, typ, k, rt, U0, E0):
    """T1: real points of the tuned variety (the E4^3 part of det Y / eta^a vanishes) along 50 random real lines"""
    m, a = M_ETA[typ], A_CHAR[typ]
    p0 = m + a // 3
    ser = []
    for B in rb:
        ser.append([[[sum((x * mon_series(mon)[p] for mon, x in B[i][j].items()), Fraction(0))
                      for p in range(p0 + 1)] for j in range(3)] for i in range(3)])

    def alpha_at(c):
        E = [[[sum((c[b] * ser[b][i][j][p] for b in range(len(rb))), Fraction(0)) for p in range(p0 + 1)]
              for j in range(3)] for i in range(3)]
        tot = Fraction(0)
        for perm in itertools.permutations(range(3)):
            sign = 1
            for x in range(3):
                for y in range(x + 1, 3):
                    if perm[x] > perm[y]:
                        sign = -sign
            A_, B_, C_ = E[0][perm[0]], E[1][perm[1]], E[2][perm[2]]
            for p1 in range(p0 + 1):
                if A_[p1] == 0:
                    continue
                for p2 in range(p0 + 1 - p1):
                    if B_[p2] == 0:
                        continue
                    tot += sign * A_[p1] * B_[p2] * C_[p0 - p1 - p2]
        return tot

    pts, good, roots_total, roots_failed = [], 0, 0, 0
    for line in range(50):
        c0 = [Fraction(int(x)) for x in rt.integers(-9, 10, size=len(rb))]
        dd = [Fraction(int(x)) for x in rt.integers(-9, 10, size=len(rb))]
        vals = [alpha_at([c0[b] + s * dd[b] for b in range(len(rb))]) for s in range(4)]
        co = cubic_exact(vals)
        while co and co[-1] == 0:
            co.pop()
        if len(co) < 2:
            continue
        big = max(abs(x) for x in co)
        try:
            roots = mp.polyroots([mp.mpf((x / big).numerator) / (x / big).denominator for x in reversed(co)],
                                 maxsteps=2000, extraprec=120)
        except mp.libmp.NoConvergence:
            roots_failed += 1
            continue
        for s in roots:
            if abs(mp.im(s)) > mp.mpf(10) ** -15:
                continue
            s = mp.re(s)
            c = [mp.mpf(c0[b].numerator) / c0[b].denominator + s * mp.mpf(dd[b].numerator) / dd[b].denominator
                 for b in range(len(rb))]
            if mp.sqrt(sum(x * x for x in c)) < mp.mpf(10) ** -20 * mp.sqrt(sum(x * x for x in c0) + 1):
                continue   # the line meets the origin there; the zero coupling is not a member
            roots_total += 1
            W = [[{} for _ in range(3)] for _ in range(3)]
            for b, B in enumerate(rb):
                for i in range(3):
                    for j in range(3):
                        for mon, x in B[i][j].items():
                            W[i][j][mon] = W[i][j].get(mon, 0) + c[b] * (mp.mpf(x.numerator) / x.denominator)
            rs = []
            for tau in GENERIC5[:3]:
                u, eta = u_mp(tau), eta_mp(tau)
                Y = mp.matrix([[sum((x * u[0] ** mo[0] * u[1] ** mo[1] * u[2] ** mo[2]
                                     for mo, x in W[i][j].items()), mp.mpc(0)) / eta ** m
                                for j in range(3)] for i in range(3)])
                rs.append(mp.det(Y) / eta ** (6 * k))
            spread = float(max(abs(x - rs[0]) for x in rs) / abs(rs[0])) if rs[0] != 0 else float("inf")
            cn = np.array([float(x) for x in c])
            cn = cn / np.linalg.norm(cn)
            _, sv = svd_sorted(S.Y(U0, E0, cn))
            nondeg = bool(sv[0, 0] / sv[0, 2] > 1e-10)
            if spread < 1e-12 and nondeg:
                good += 1
                pts.append(cn)
    return pts, roots_total, good, roots_failed


def main():
    out = {"rule": "W113_RULE.md", "script": "the_strong_angle.py"}
    rng = np.random.default_rng(113)

    # ---------------- spaces
    spaces, reals, dims = {}, {}, {}
    for typ in TYPES:
        for k in WEIGHTS[typ]:
            t = time.time()
            basis, d = space(typ[0], typ[1], k)
            closed, rb = real_basis(basis, d)
            spaces[(typ, k)] = (basis, d)
            reals[(typ, k)] = (closed, rb)
            dims[(typ, k)] = len(basis)
            log(f"space {NAME[typ]} k={k}: dim {len(basis)} (degree {d}; conj-closed {closed}; {time.time() - t:.1f}s)")

    # ---------------- F0
    f0 = {"T(x)T dims k=1,3,5,7": [dims[((1, 1), k)] for k in (1, 3, 5, 7)],
          "mixed (Q in T) dims k=0,2,4,6": [dims[((1, -1), k)] for k in (0, 2, 4, 6)],
          "mixed (Q in Tbar) dims k=0,2,4,6": [dims[((-1, 1), k)] for k in (0, 2, 4, 6)]}
    ok_dims = (f0["T(x)T dims k=1,3,5,7"] == [1, 2, 4, 5] and f0["mixed (Q in T) dims k=0,2,4,6"] == [1, 2, 4, 5]
               and f0["mixed (Q in Tbar) dims k=0,2,4,6"] == [1, 2, 4, 5])
    b1, _ = spaces[((1, 1), 1)]
    zd = {}
    if len(b1) == 1:
        W1 = b1[0]
        assign, diag_max, sym_max, ratio_spread = {}, 0.0, 0.0, 0.0
        vals = []
        for tau in GENERIC5[:3]:
            u, eta = u_mp(tau), eta_mp(tau)
            Y = Y_mp(W1, 18, tau, u, eta)
            mx = max(abs(Y[i, j]) for i in range(3) for j in range(3))
            diag_max = max(diag_max, float(max(abs(Y[i, i]) for i in range(3)) / mx))
            sym_max = max(sym_max, float(max(abs(Y[i, j] - Y[j, i]) for i in range(3) for j in range(3)) / mx))
            vals.append((Y, u, eta))
        lam = {}
        for (i, j) in ((0, 1), (0, 2), (1, 2)):
            best = None
            for aidx in range(3):
                r = [v[0][i, j] / v[1][aidx] for v in vals]
                spread = float(max(abs(x - r[0]) for x in r) / abs(r[0]))
                if best is None or spread < best[0]:
                    best = (spread, aidx, r[0])
            assign[f"{i}{j}"] = ["theta_2^2", "theta_3^2", "theta_4^2"][best[1]]
            ratio_spread = max(ratio_spread, best[0])
            lam[(i, j)] = best[2]
        Y, u, eta = vals[0]
        eight = mp.det(Y) / (lam[(0, 1)] * lam[(0, 2)] * lam[(1, 2)] * eta ** 6)
        pure = [mp.det(v[0]) / v[2] ** 6 for v in vals]
        pure_spread = float(max(abs(x - pure[0]) for x in pure) / abs(pure[0]))
        okex, kappa1 = det_exact_pure([reals[((1, 1), 1)][1][0]], 10)
        zd = {"diagonal_over_max": diag_max, "antisymmetry_over_max": sym_max, "off_diagonal_entries": assign,
              "ratio_spread": ratio_spread, "det_over_lambdas_eta6": [float(eight.real), float(eight.imag)],
              "det_over_eta6_spread": pure_spread, "exact det W = kappa (u1u2u3)^10": okex}
        ok_zd = (diag_max < 1e-25 and sym_max < 1e-25 and ratio_spread < 1e-20 and len(set(assign.values())) == 3
                 and abs(eight - 8) < 1e-18 and pure_spread < 1e-20 and okex)
    else:
        ok_zd = False
    f0.update({"k=1 member": zd, "holds": bool(ok_dims and ok_zd)})
    out["F0"] = f0
    log("F0", json.dumps(f0)[:400])

    # ---------------- F1
    tb = [dims[((-1, -1), k)] for k in (1, 3, 5, 7)]
    split = sym_split(*spaces[((-1, -1), 3)]) if dims[((-1, -1), 3)] else (0, 0)
    f1 = {"Tbar(x)Tbar dims k=1,3,5,7": tb, "k=1 (read-out)": tb[0], "k=3 split (symmetric, antisymmetric)": split,
          "holds": bool(tb[1:] == [3, 4, 6] and tuple(split) == (2, 1))}
    out["F1"] = f1
    log("F1", f1)

    # ---------------- F2
    f2, f2ok = {}, True
    rng2 = np.random.default_rng(1131)
    for typ in TYPES:
        for k in WEIGHTS[typ]:
            basis, _ = spaces[(typ, k)]
            key = f"{NAME[typ]} k={k}"
            if not basis:
                f2[key] = {"dim": 0, "class": classify(*typ, k)}
                continue
            r = det_layer(basis, typ[0], typ[1], k, rng2)
            r.update({"dim": len(basis), "class": classify(*typ, k)})
            f2[key] = r
            f2ok = f2ok and r["holds"]
            log("F2", key, {kk: r[kk] for kk in r if kk != "components"})
    out["F2"] = {"rows": f2, "holds": bool(f2ok)}

    # ---------------- F3
    rb3 = reals[((-1, -1), 3)][1]
    if rb3:
        ok3, kappa = det_exact_pure(rb3, 6)
        out["F3"] = {"exact det W = kappa(c) (u1 u2 u3)^6": ok3, "kappa (cubic form; key = exponents of c)": kappa,
                     "kappa nonzero": bool(kappa), "holds": bool(ok3 and kappa)}
    else:
        out["F3"] = {"holds": False, "note": "the space is zero"}
    log("F3", out["F3"])

    # ---------------- sectors (real bases, fast evaluation)
    sec = {}
    for (typ, k), (closed, rb) in reals.items():
        if rb:
            sec[(typ, k)] = (Sector(rb, M_ETA[typ], f"{NAME[typ]} k={k}"), rb)

    # ---------------- F4: the forced pairs
    hands = list(itertools.product((1, -1), repeat=3))
    U0, E0 = u_eta_np(np.array([GENERIC5[0]]))

    def viability(tu, ku, td, kd, draws=5, seed=1132):
        r = np.random.default_rng(seed)
        if (tu, ku) not in sec or (td, kd) not in sec:
            return {"viable": False, "reason": "a sector has no coupling"}
        Su, bu = sec[(tu, ku)]
        Sd, bd = sec[(td, kd)]
        rec = []
        for _ in range(draws):
            cu, cd = r.normal(size=Su.dim), r.normal(size=Sd.dim)
            obs, J, su_, sd_, V = observables(Su.Y(U0, E0, cu), Sd.Y(U0, E0, cd))
            su_, sd_ = su_[0], sd_[0]
            degen = bool((su_[2] - su_[0]) / su_[2] < 1e-9 or (sd_[2] - sd_[0]) / sd_[2] < 1e-9)
            massless = bool(su_[0] / su_[2] < 1e-12 or sd_[0] / sd_[2] < 1e-12)
            aligned = bool(perm_distance(V[0]) < 1e-8)
            rec.append({"degenerate": degen, "massless": massless, "V_a_permutation": aligned})
        viable = all(not (x["degenerate"] or x["massless"] or x["V_a_permutation"]) for x in rec)
        return {"viable": bool(viable), "draws": rec}

    f4 = {}
    viable_auto = []
    for h in hands:
        sQ, su_, sd_ = h
        tu, td = (sQ, su_), (sQ, sd_)
        v = viability(tu, K_AUTO[tu], td, K_AUTO[td])
        v.update({"up": f"{NAME[tu]} k={K_AUTO[tu]}", "down": f"{NAME[td]} k={K_AUTO[td]}"})
        f4[str(h)] = v
        if v["viable"]:
            viable_auto.append(h)
    out["F4"] = {"hands (s_Q, s_u, s_d)": f4, "viable": [str(h) for h in viable_auto],
                 "holds": bool(viable_auto == [(-1, -1, -1)])}
    log("F4 viable automatic assignments:", viable_auto)

    # ---------------- layer C
    out["C"] = {}
    for h in viable_auto:
        sQ, su_, sd_ = h
        tu, td = (sQ, su_), (sQ, sd_)
        ku, kd = K_AUTO[tu], K_AUTO[td]
        K = ku + kd
        Su, bu = sec[(tu, ku)]
        Sd, bd = sec[(td, kd)]
        C = {"assignment": {"hand": str(h), "up": Su.label, "down": Sd.label, "K": K}}
        rc = np.random.default_rng(1133)

        # C1
        closed = reals[(tu, ku)][0] and reals[(td, kd)][0]
        dev = 0.0
        for tau in GENERIC5[:3]:
            for S_, b_ in ((Su, bu), (Sd, bd)):
                c = rc.normal(size=S_.dim)
                W = combo(b_, [Fraction(float(x)) for x in c])
                Y1 = Y_mp(W, S_.m, tau)
                Y2 = Y_mp(W, S_.m, -complex(tau).conjugate())
                mx = max(abs(Y1[i, j]) for i in range(3) for j in range(3))
                dev = max(dev, float(max(abs(Y2[i, j] - mp.conj(Y1[i, j])) for i in range(3) for j in range(3)) / mx))
        C["C1"] = {"conjugation_closed": bool(closed), "max |Y(-conj tau) - conj Y(tau)| / max|Y|": dev,
                   "holds": bool(closed and dev < 1e-20)}
        log("C1", C["C1"])

        # C2 (mpmath, 30 digits)
        taus = random_tau_F(rc, 30, 6.0)
        worst, pos, zero = 0.0, 0, 0
        pairs = [(rc.normal(size=Su.dim), rc.normal(size=Sd.dim)) for _ in range(200)]
        Wpairs = [(combo(bu, [Fraction(float(x)) for x in cu]), combo(bd, [Fraction(float(x)) for x in cd]))
                  for cu, cd in pairs]
        for tau in taus:
            u, eta = u_mp(tau), eta_mp(tau)
            e6K = eta ** (6 * K)
            for Wu, Wd in Wpairs:
                r = mp.det(Y_mp(Wu, Su.m, tau, u, eta)) * mp.det(Y_mp(Wd, Sd.m, tau, u, eta)) / e6K
                if r == 0:
                    zero += 1
                    continue
                worst = max(worst, float(abs(r.imag) / abs(r)))
                pos += int(r.real > 0)
        C["C2"] = {"max |Im r| / |r|, r = det(Y_u) det(Y_d) / eta^(6K)": worst, "pairs": 200, "taus": 30,
                   "fraction with theta-bar = 0 (r > 0)": pos / (200 * 30), "evaluations with r = 0": zero,
                   "without the counterterm": f"theta-bar = -{6 * K} arg eta - arg r (mod 2 pi), r real",
                   "holds": bool(worst < 1e-12 and zero == 0)}
        log("C2", C["C2"])

        # C3
        pairs = [(rc.normal(size=Su.dim), rc.normal(size=Sd.dim)) for _ in range(100)]
        CU, CD = np.array([p[0] for p in pairs]), np.array([p[1] for p in pairs])
        counts, Jtyp = [], []
        for tau in GENERIC5:
            _, J, _, _, _ = Model(Su, Sd).many(np.full(100, tau), CU, CD)
            counts.append(int(np.sum(np.abs(J) > 1e-8)))
            Jtyp.append(float(np.median(np.abs(J))))
        cp = {}
        for name, tau in (("Re tau = 0", 1.3j), ("Re tau = 1/2", complex(0.5, 1.2)),
                          ("|tau| = 1", complex(math.cos(math.radians(75)), math.sin(math.radians(75))))):
            _, J, _, _, _ = Model(Su, Sd).many(np.full(100, tau), CU, CD)
            cp[name] = float(np.max(np.abs(J)))
        C["C3"] = {"pairs with |J| > 1e-8, per generic tau": counts, "median |J| per generic tau": Jtyp,
                   "max |J| on the CP loci": cp,
                   "holds": bool(min(counts) >= 95 and max(cp.values()) < 1e-13)}
        log("C3", C["C3"])

        model = Model(Su, Sd)
        n1 = 100000
        taus1 = random_tau_F(rc, n1, 6.0)
        CU1, CD1 = rc.normal(size=(n1, Su.dim)), rc.normal(size=(n1, Sd.dim))
        obs1 = np.zeros((n1, 8))
        hu1, hd1 = np.zeros(n1), np.zeros(n1)
        for s in range(0, n1, 20000):
            o, _, a1, a2, _ = model.many(taus1[s:s + 20000], CU1[s:s + 20000], CD1[s:s + 20000])
            obs1[s:s + 20000] = o
            hu1[s:s + 20000], hd1[s:s + 20000] = hier(a1), hier(a2)
        P1 = np.concatenate([taus1.real[:, None], taus1.imag[:, None], CU1, CD1], 1)

        # C4 (a hierarchy)
        hm = np.maximum(hu1, hd1)[:20000]
        order = np.argsort(np.where(np.isfinite(hm), hm, np.inf))

        def fh(p):
            r = model.eval_point(p, 6.0)
            if r is None:
                return 1e30
            _, (_, _, a1, a2, _) = r
            v = float(max(hier(a1)[0], hier(a2)[0]))
            return math.log(v) if np.isfinite(v) and v > 0 else 1e30

        best_h = min((nm(fh, P1[i], 4000) for i in order[:20]), key=lambda t: t[1])
        hval = math.exp(best_h[1]) if best_h[1] < 1e29 else float("inf")
        expo = []
        for _ in range(3):
            c = rc.normal(size=Su.dim)
            ys = np.array([3.0, 4.0, 5.0, 6.0])
            U, E = u_eta_np(0.1 + 1j * ys)
            _, s = svd_sorted(Su.Y(U, E, c))
            slopes = [float(-np.polyfit(2 * np.pi * ys, np.log(s[:, i] / s[:, 2]), 1)[0]) for i in range(3)]
            expo.append(slopes)
        C["C4"] = {"min over (tau, coefficients) of max over sectors of max(m2/m1, m3/m2)": hval,
                   "at": readout(model, best_h[0], 0.10) if hval < 1e29 else None,
                   "read-out: cusp exponents of m_i / m_max for three random real members (lightest first)": expo,
                   "holds": bool(hval <= 0.1)}
        log("C4", hval, expo)

        # C5 (control) and C6 (fit)
        rcc = np.random.default_rng(1130)
        for _ in range(5000):
            tstar = random_tau_F(rcc, 1, 3.0)[0]
            if tstar.imag < 1.0:
                continue
            pstar = np.concatenate([[tstar.real, tstar.imag], rcc.normal(size=Su.dim), rcc.normal(size=Sd.dim)])
            ostar = model.eval_point(pstar, 8.0)[1][0][0]
            if np.all((ostar > 1e-6) & (ostar < 0.9)):
                break
        logd_ctrl = np.log(ostar)
        for name, logd in (("C5", logd_ctrl), ("C6", LOGD)):
            c1 = chi2_many(obs1, logd, 0.10)
            order = np.argsort(c1)
            starts = [P1[i] for i in order[:200]]
            t = time.time()
            (pbest, vbest), top10, f = fit(model, logd, 0.10, starts)
            rec = {"chi2_min (a = 0.10)": vbest, "stage-1 best chi2": float(c1[order[0]]),
                   "stage-2 best ten": top10, "seconds": time.time() - t}
            if name == "C5":
                rec.update({"synthetic point": pstar.tolist(), "synthetic observables": ostar.tolist(),
                            "holds": bool(vbest <= 0.01)})
            else:
                rec["best point"] = readout(model, pbest, 0.10)
                tf = to_fd(complex(pbest[0], pbest[1]))
                _, cu, cd = model.unpack(pbest)
                rec["theta-bar at the best point"] = theta_bit(Su, Sd, bu, bd, tf, cu / np.linalg.norm(cu),
                                                               cd / np.linalg.norm(cd), K)
                for a2 in (0.05, 0.20):
                    def fa(p, a2=a2):
                        r = model.eval_point(p, 8.0)
                        if r is None:
                            return 1e30
                        cc = chi2_many(r[1][0][0], LOGD, a2)
                        return float(cc) if np.isfinite(cc) else 1e30
                    rr = [nm(fa, starts[i], 10000) for i in range(10)]
                    rr += [nm(fa, pbest, 10000)]
                    rec[f"chi2_min (a = {a2})"] = min(v for _, v in rr)
                rec["pass mark"] = PASS
                rec["holds"] = bool(vbest <= PASS)
            C[name] = rec
            log(name, {kk: rec[kk] for kk in rec if kk in ("chi2_min (a = 0.10)", "holds", "stage-1 best chi2")})
        out["C"][str(h)] = C

    # ---------------- layer T
    T = {}
    rt = np.random.default_rng(1134)
    tuned_types = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    variety = {}
    t1 = {}
    for typ in tuned_types:
        k = K_TUNED[typ]
        if (typ, k) not in sec:
            t1[f"{NAME[typ]} k={k}"] = {"dim": 0, "holds": False}
            continue
        S, rb = sec[(typ, k)]
        pts, roots_total, good, roots_failed = tuned_points(S, rb, typ, k, rt, U0, E0)
        variety[typ] = pts
        t1[f"{NAME[typ]} k={k}"] = {"dim": len(rb), "real roots": roots_total, "pure and non-degenerate": good,
                                    "root searches that did not converge": roots_failed,
                                    "holds": bool(roots_total > 0 and good == roots_total)}
        log("T1", NAME[typ], k, t1[f"{NAME[typ]} k={k}"])
    T["T1"] = {"rows": t1, "holds": bool(all(v["holds"] for v in t1.values()))}

    # T2, T3
    tuned_assign = []
    for h in hands:
        sQ, su_, sd_ = h
        tu, td = (sQ, su_), (sQ, sd_)
        for ku, kd in itertools.product((K_AUTO[tu], K_TUNED[tu]), (K_AUTO[td], K_TUNED[td])):
            if ku == K_AUTO[tu] and kd == K_AUTO[td]:
                continue
            if (tu[0] != tu[1] and ku == 0) or (td[0] != td[1] and kd == 0):
                continue
            tuned_assign.append((h, (tu, ku), (td, kd)))
    taus3 = list(GENERIC5) + list(random_tau_F(rt, 15, 6.0))
    U3, E3 = u_eta_np(np.array(taus3))
    t2 = {}
    for h, (tu, ku), (td, kd) in tuned_assign:
        key = f"{h}: up {NAME[tu]} k={ku}, down {NAME[td]} k={kd}"

        def samples(typ, k, n, shift):
            if k == K_TUNED[typ]:
                pts = variety.get(typ, [])
                return [pts[(i + shift) % len(pts)] for i in range(n)] if pts else []
            S, _ = sec[(typ, k)]
            return [rt.normal(size=S.dim) for _ in range(n)]

        if (tu, ku) not in sec or (td, kd) not in sec:
            t2[key] = {"holds": False, "note": "a sector has no coupling"}
            continue
        Su, _ = sec[(tu, ku)]
        Sd, _ = sec[(td, kd)]
        su_s = samples(tu, ku, 20, 0)
        sd_s = samples(td, kd, 20, 1 if (tu, ku) == (td, kd) else 0)
        if not su_s or not sd_s:
            t2[key] = {"holds": False, "note": "no variety points"}
            continue
        Js, hmin = [], float("inf")
        for cu, cd in zip(su_s, sd_s):
            _, J, _, _, _ = observables(Su.Y(U0, E0, cu), Sd.Y(U0, E0, cd))
            Js.append(float(abs(J[0])))
            _, _, a1, a2, _ = observables(Su.Y(U3, E3, cu), Sd.Y(U3, E3, cd))
            hm3 = np.maximum(hier(a1), hier(a2))
            hm3 = hm3[np.isfinite(hm3)]
            if hm3.size:
                hmin = min(hmin, float(hm3.min()))
        t2[key] = {"pairs with |J| > 1e-8": int(np.sum(np.array(Js) > 1e-8)), "max |J|": max(Js),
                   "T3: smallest hierarchy measure": hmin, "holds": bool(max(Js) > 1e-8)}
    T["T2"] = {"assignments": t2, "count": len(tuned_assign),
               "holds": bool(len(tuned_assign) == 16 and all(v["holds"] for v in t2.values()))}
    log("T2", T["T2"]["count"], T["T2"]["holds"])
    out["T"] = T

    out["dims"] = {f"{NAME[t]} k={k}": v for (t, k), v in dims.items()}
    out["seconds"] = time.time() - T0
    (HERE / "the_strong_angle.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    log("written the_strong_angle.json")


if __name__ == "__main__":
    sys.exit(main())
