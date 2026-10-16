"""W99, the paper read's checks: the numbers this seat could recompute in P9 draft 3 (main's S140 relay).

A verification read, not a sealed arc: no rule, no prediction. Every check was first run in scratch while reading
(disclosed in the NOTE's W99); this file repeats them in one run, and its output is committed as written.

Run from the repository root: python3 docs/dossiers/the_weave_2026-10-07/the_paper_read_checks.py
"""
import cmath
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = {"what": "W99, the paper read's checks of P9 draft 3 (papers/P9_what_a_grammar_fixes on main @ 4cc3658a8)"}


def mat(w):
    a, b, c, d = 1, 0, 0, 1
    for ch in w:
        if ch == "L":
            a, b, c, d = a, a + b, c, c + d
        else:
            a, b, c, d = a + b, b, c + d, d
    return a, b, c, d


def canon(s):
    return min(s[i:] + s[:i] for i in range(len(s)))


def primitive(s):
    return all(s != s[i:] + s[:i] for i in range(1, len(s)))


def lyndon(n):
    for w in itertools.product("LR", repeat=n):
        s = "".join(w)
        if len(set(s)) == 2 and all(s < s[i:] + s[:i] for i in range(1, n)):
            yield s


# ---------------------------------------------------------------- A. section 3's counts
signed = odd = 0
by6 = {"odd": 0, "trivial mod 2": 0, "transposition mod 2": 0}
for n in range(2, 9):
    for w in itertools.product("LR", repeat=n):
        if len(set(w)) < 2:
            continue
        a, b, c, d = mat(w)
        signed += 2
        odd += 2 * ((a + d) % 2)
        if n <= 6:
            if (a + d) % 2:
                by6["odd"] += 1
            else:
                by6["trivial mod 2" if b % 2 == 0 and c % 2 == 0 else "transposition mod 2"] += 1
threads6 = [s for n in range(2, 7) for s in lyndon(n)]
threads8 = [s for n in range(2, 9) for s in lyndon(n)]
swap = lambda s: s.translate(str.maketrans("LR", "RL"))


def geometries(syms):
    orb = {min(canon(f(s)) for f in syms) for s in threads8}
    return {"geometries": len(orb), "odd": sum(sum(mat(o)[::3]) % 2 for o in orb)}


OUT["A, section 3"] = {
    "signed words to length 8": signed, "of odd trace": odd, "words to length 6": by6,
    "threads to length 6": len(threads6), "odd-trace threads to length 6": sum(sum(mat(s)[::3]) % 2 for s in threads6),
    "threads to length 8": len(threads8),
    "geometries up to rotation and the L-R exchange (B1601)": geometries((lambda s: s, swap)),
    "geometries up to rotation, inversion and the mirror (the paper's words)":
        geometries((lambda s: s, lambda s: s[::-1], swap, lambda s: swap(s)[::-1])),
}

# ---------------------------------------------------------------- B. T2(2) for every word: the conjugator in 2O
E2 = np.eye(2, dtype=complex)
QI = np.array([[1j, 0], [0, -1j]])
QJ = np.array([[0, 1], [-1, 0]], dtype=complex)
QK = QI @ QJ
cands = []
for v in itertools.product([0, 1, -1, 0.5, -0.5, 1 / math.sqrt(2), -1 / math.sqrt(2)], repeat=4):
    if abs(sum(x * x for x in v) - 1) < 1e-9:
        cands.append(v[0] * E2 + v[1] * QI + v[2] * QJ + v[3] * QK)


def kind(g):
    q = sorted(np.round(np.abs([(g[0, 0] + g[1, 1]).real / 2, (g[0, 0] - g[1, 1]).imag / 2,
                                 (g[0, 1] - g[1, 0]).real / 2, (g[0, 1] + g[1, 0]).imag / 2]), 6))
    if q == [0, 0, 0, 1]:
        return "Q8"
    if q == [0.5, 0.5, 0.5, 0.5]:
        return "2T minus Q8"
    return "2O minus 2T" if q == [0, 0, round(2 ** -0.5, 6), round(2 ** -0.5, 6)] else "other"


def ev(s):
    M = E2.copy()
    for y in s:
        M = M @ (QI if y == "a" else QJ)
    return M


tally = {}
for n in range(1, 13):
    for w in itertools.product("LR", repeat=n):
        img = {"a": "a", "b": "b"}
        for ch in w:                                   # L: b -> ab; R: a -> ab (homology rows (a, a+b), (a+b, b))
            new = {"a": "a", "b": "ab"} if ch == "L" else {"a": "ab", "b": "b"}
            img = {x: "".join(new[y] for y in img[x]) for x in "ab"}
        A, B = ev(img["a"]), ev(img["b"])
        ks = sorted({kind(g) for g in cands
                     if np.allclose(g @ QI @ g.conj().T, A) and np.allclose(g @ QJ @ g.conj().T, B)})
        a, b, c, d = mat(w)
        cls = "odd" if (a + d) % 2 else ("trivial mod 2" if b % 2 == 0 and c % 2 == 0 else "transposition mod 2")
        key = cls + ": " + ", ".join(ks)
        tally[key] = tally.get(key, 0) + 1
OUT["B, T2(2) for every word to length 12 (the class of the conjugator)"] = tally

# ---------------------------------------------------------------- C. section 4's representation
rT_u = np.array([[1j, 0, 0], [0, 0, 1], [0, 1, 0]])               # on (theta2^2, theta3^2, theta4^2)
rS_u = -1j * np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
rT = cmath.exp(2j * math.pi * 21 / 24) * rT_u
rS = cmath.exp(-1j * math.pi / 4) ** 21 * rS_u


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


def order(M):
    X = M.copy()
    for k in range(1, 200):
        if np.allclose(X, np.eye(3)):
            return k
        X = X @ M


G = closure((rT, rS))
st = rS @ rT
OUT["C, section 4"] = {
    "order of the image of chi_eta^21 x rho_u": len(G),
    "scalars in it": sum(1 for g in G if np.allclose(g, g[0, 0] * np.eye(3))),
    "order of the image of rho_u (the weight-one triplet)": len(closure((rT_u, rS_u))),
    "exponents of t (turns)": sorted(round(float(x), 6) for x in np.angle(np.linalg.eigvals(rT)) / (2 * math.pi) % 1),
    "s^2 = (st)^3 and s^8 = 1": bool(np.allclose(rS @ rS, np.linalg.matrix_power(st, 3))
                                     and np.allclose(np.linalg.matrix_power(rS, 8), np.eye(3))),
    "order at i (s)": order(rS), "order at omega (st)": order(st),
    "st's eigenlines: squared overlaps with the theta lines": sorted(
        {round(float(x), 6) for x in (np.abs(np.linalg.eig(st)[1]) ** 2).reshape(-1)}),
}
gens = {"L": ((1, 1, 0, 1), 1), "l": ((1, -1, 0, 1), -1), "R": ((1, 0, 1, 1), -1), "r": ((1, 0, -1, 1), 1)}
inv = {"L": "l", "l": "L", "R": "r", "r": "R"}
cnt = {}


def dfs(M, e, last, n):
    if M == (1, 0, 0, 1) and n:
        cnt[e] = cnt.get(e, 0) + 1
    if n == 12:
        return
    a, b, c, d = M
    for g, ((p, q, r, s), de) in gens.items():
        if last and inv[g] == last:
            continue
        dfs((a * p + b * r, a * q + b * s, c * p + d * r, c * q + d * s), e + de, g, n + 1)


dfs((1, 0, 0, 1), 0, "", 0)
OUT["C, section 4"]["non-empty reduced words to length 12 acting trivially on homology, by exponent sum"] = {
    str(k): v for k, v in sorted(cnt.items())}

# ---------------------------------------------------------------- D. the joint law exactly as printed (T7)
I = sp.I
s_ = sp.symbols("s0:4")
m_ = sp.symbols("m0:4")
S = sp.Matrix([[s_[0], s_[1]], [s_[2], s_[3]]])
M = sp.Matrix([[m_[0], m_[1]], [m_[2], m_[3]]])
eps = sp.Matrix([[0, 1], [-1, 0]])
C = [eps, sp.diag(I, -I), sp.diag(I, -I) * eps]


def Y(S, M):
    return sp.Matrix(3, 3, lambda a, b: sum((C[a].T * eps * S * C[b])[p, q] * M[p, q]
                                            for p in range(2) for q in range(2)))


def Aq(M):
    m0, m1, m2, m3 = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[m0**2 + m1**2 + m2**2 + m3**2, 2*I*(m0*m2 + m1*m3), -I*(m0**2 + m1**2 - m2**2 - m3**2)],
                      [2*I*(m0*m1 + m2*m3), -4*m1*m2, 2*(m0*m1 - m2*m3)],
                      [-I*(m0**2 - m1**2 + m2**2 - m3**2), 2*(m0*m2 - m1*m3), -m0**2 + m1**2 + m2**2 - m3**2]])


Ysm = Y(S, M)
N = M * eps
rng = np.random.default_rng(1)
pv, qv = rng.normal(size=2) + 1j * rng.normal(size=2), rng.normal(size=2) + 1j * rng.normal(size=2)
Mn = sp.Matrix(np.outer(pv, qv).tolist())
cols = []
for k in range(4):
    Ek = sp.zeros(2, 2)
    Ek[k // 2, k % 2] = 1
    cols.append(np.array(Y(Ek, Mn).evalf(), dtype=complex).reshape(-1))
Gm = np.array(cols).T
nM2 = float(np.sum(np.abs(np.outer(pv, qv)) ** 2))
Sg = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
sv = np.linalg.svd(np.array(Y(sp.Matrix(Sg.tolist()), sp.Matrix((Sg @ np.array([[0, -1], [1, 0]])).tolist())).evalf(),
                            dtype=complex), compute_uv=False)
OUT["D, the joint law as printed"] = {
    "det law residual is 0": sp.expand(Ysm.det() - 4 * S.det() * M.det() * (eps * S * M.T).trace()) == 0,
    "adj law residual is 0": sp.expand(Ysm.adjugate() - (S.det() * Aq(M) + M.det() * sp.diag(1, -1, -1) * Aq(S)))
    == sp.zeros(3, 3),
    "symmetry Y(S, N eps^-1) = Y(N, S eps^-1)": sp.expand(Y(S, N * eps.inv()) - Y(N, S * eps.inv())) == sp.zeros(3, 3),
    "polar identity residual is 0": sp.expand((eps * S * M.T).trace() + ((S + N).det() - S.det() - N.det())) == 0,
    "Gram spectrum of S -> Y(S, M) over |M|^2, M null": [round(float(x), 9) for x in
                                                        np.linalg.eigvalsh(Gm.conj().T @ Gm) / nM2],
    "|A(M)| over |M|^2, M null": round(float(np.linalg.norm(np.array(Aq(Mn).evalf(), dtype=complex)) / nM2), 9),
    "m1 m3 - m2^2 at N = S": float(sv[0] * sv[2] - sv[1] ** 2),
}

# ---------------------------------------------------------------- E. D's cusp expansion (Proposition, the norm)
mp.mp.dps = 40


def D_rho2(tau):
    q = mp.exp(1j * mp.pi * tau)
    t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    e = mp.exp(1j * mp.pi * tau / 12) * mp.qp(mp.exp(2j * mp.pi * tau))
    lam = t2 ** 4 / t3 ** 4
    D = -t3 ** 4 * (lam * mp.log(abs(lam)) + (1 - lam) * mp.log(abs(1 - lam))) / (4 * mp.pi * e ** 6)
    r2 = (abs(t2) ** 4 + abs(t3) ** 4 + abs(t4) ** 4) / (4 * mp.pi ** 2 * abs(e) ** 6)
    return D, r2, q


cusp = []
for x in (0, 0.25, 0.5):
    for y in (4, 5):
        D, r2, q = D_rho2(mp.mpc(x, y))
        paper = 8 * mp.pi ** 2 * y + 8 * mp.pi * (1 - 4 * mp.log(2))
        corr = 8 * mp.pi * mp.exp(-1j * mp.pi * x / 2) * (mp.pi * y - 4 * mp.log(2) + (1 + mp.exp(-2j * mp.pi * x)) / 2)
        lhs = D / (q * r2)
        cusp.append({"tau": [x, y], "D/(q|rho|^2)": [float(lhs.real), float(lhs.imag)], "the paper's": float(paper),
                     "the corrected leading terms": [float(corr.real), float(corr.imag)],
                     "|difference| from the corrected": float(abs(lhs - corr))})
D0, _, _ = D_rho2(mp.mpc(0.1, 3))
D1, _, _ = D_rho2(mp.mpc(1.1, 3))
OUT["E, D at the cusp"] = {"points": cusp, "D(tau+1)/D(tau) at 0.1+3i": [float(mp.re(D1 / D0)), float(mp.im(D1 / D0))]}

# ---------------------------------------------------------------- F. the threads to trace 600 (B1666's count)
TMAX = 600
bytr = {}


def blk(a, b):
    return (1 + a * b, a, b, 1)


def mul(X, Z):
    a, b, c, d = X
    e, f, g, h = Z
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def walk(X, seq):
    for a in range(1, TMAX):
        if sum(mul(X, blk(a, 1))[::3]) > TMAX:
            break
        for b in range(1, TMAX):
            Z = mul(X, blk(a, b))
            t = Z[0] + Z[3]
            if t > TMAX:
                break
            s2 = seq + [a, b]
            k = len(s2) // 2
            rots = [tuple(s2[2 * i:] + s2[:2 * i]) for i in range(k)]
            if tuple(s2) == min(rots) and all(r != tuple(s2) for r in rots[1:]):
                bytr[t] = bytr.get(t, 0) + 1
            walk(Z, s2)


walk((1, 0, 0, 1), [])
OUT["F, threads by trace"] = {"trace <= 600": sum(bytr.values()),
                              "trace <= 40": sum(v for t, v in bytr.items() if t <= 40),
                              "layers t = 3..6": [bytr.get(t, 0) for t in range(3, 7)]}


# ---------------------------------------------------------------- G. the branch sign of the period phase
def eps_sign(w, steps=4000):
    a, b, c, d = mat(w)
    r = math.sqrt((a + d) ** 2 - 4)
    x1, x2 = (a - d - r) / (2 * c), (a - d + r) / (2 * c)
    ctr, rad = (x1 + x2) / 2, abs(x2 - x1) / 2
    z0 = ctr + 1j * rad
    z1 = (a * z0 + b) / (c * z0 + d)
    th0, th1 = cmath.phase(z0 - ctr), cmath.phase(z1 - ctr)
    sg = 1 if th1 > th0 else -1
    acc, prev = 0.0, None
    for k in range(steps + 1):
        ph = cmath.phase(1j * sg * cmath.exp(1j * (th0 + (th1 - th0) * k / steps)))
        if prev is not None:
            acc += (ph - prev + math.pi) % (2 * math.pi) - math.pi
        prev = ph
    v = cmath.exp(-1j * acc / 2) / cmath.exp(1j * cmath.phase(c * z0 + d))
    return 1 if abs(v - 1) < 1e-6 else (-1 if abs(v + 1) < 1e-6 else 0)


th12 = [s for n in range(2, 13) for s in lyndon(n)]
signs = [eps_sign(s) for s in th12]
OUT["G, the branch sign"] = {"threads to length 12": len(th12), "+1": signs.count(1), "-1": signs.count(-1),
                             "neither": signs.count(0)}

(HERE / "the_paper_read_checks.json").write_text(json.dumps(OUT, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(OUT, indent=1, ensure_ascii=False))
