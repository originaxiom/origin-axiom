#!/usr/bin/env python3
"""W136 — the coupling forms: which weights carry modular forms in 1', rho' and rho' (x) sgn of the joint family
group, and what the least of them are (the rule: W136_RULE.md, committed and pushed before this script).

  L0  the instrument: the joint family group rho' = rho_T (x) chi_eta^21 (exact); the order of <s, t | s^2, (st)^3,
      t^4>; |SL(2, Z/4)| and the graph of gamma mod 4 -> rho'(gamma); v = 2 eta^3 R = (-th2^2, -th4^2, i th3^2) under
      S and T at five random tau (60 digits, thetas and eta summed in tau); Jacobi; the ring's ranks (exact q-series)
  L1  dim M_w(sigma) for sigma in {1, 1', 2, rho', rho' (x) sgn} and even w <= 24, three routes: (a) characters on
      C[v]_w/(v.v), exact; (b) W45's chi (w >= 2); (c) D_w (x) sgn^(w/2) from the rotation angles; the generating
      weights over C[E4, E6] against 12 sum(lambda)
  L2  the least forms Y2, Y4, Y6: their laws under S and T, and their identities with eta and F_a
  L3  the invariant cubics (exact), C(w), and Sym^3 rho'_k for k = 5 and 13
  L4  the read-out

    python3 -B the_coupling_forms.py      # writes the_coupling_forms.json beside itself
"""
import contextlib
import io
import itertools
import json
import random
import sys
from fractions import Fraction as Fr
from pathlib import Path

import flint
import mpmath as mp
import numpy as np
import sympy as sp
from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.free_groups import free_group

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_bridge_e6_su3 as BR  # noqa: E402  (W134: rho_exact, chi; BR.UC = W47; BR.UC.IW = W45's chi)

IW = BR.UC.IW
OUT = HERE / "the_coupling_forms.json"
IRREPS = ("1", "1'", "2", "rho'", "rho' (x) sgn")
DIMS = {"1": 1, "1'": 1, "2": 2, "rho'": 3, "rho' (x) sgn": 3}
WMAX = 24
PRED = {0: (1, 0, 0, 0, 0), 2: (0, 0, 1, 1, 0), 4: (1, 0, 1, 1, 1), 6: (1, 1, 1, 2, 1),
        8: (1, 0, 2, 2, 2), 10: (1, 1, 2, 3, 2), 12: (2, 1, 2, 3, 3)}
GENS = {"1": [0], "1'": [6], "2": [2, 4], "rho'": [2, 4, 6], "rho' (x) sgn": [4, 6, 8]}
PRED_C = {0: 0, 2: 2, 4: 3, 6: 6, 8: 6, 10: 9, 12: 10}
mp.mp.dps = 60
I = mp.mpc(0, 1)


# ------------------------------------------------------------------ exact helpers
def to_gauss(M):
    """an exact sympy matrix with Gaussian-integer entries -> tuple of tuples of complex, checked exactly"""
    rows = []
    for i in range(M.rows):
        row = []
        for j in range(M.cols):
            z = complex(sp.N(M[i, j], 50))
            a, b = int(round(z.real)), int(round(z.imag))
            assert sp.simplify(sp.expand_complex(M[i, j] - (a + b * sp.I))) == 0, (i, j, M[i, j])
            row.append(complex(a, b))
        rows.append(tuple(row))
    return tuple(rows)


def mul(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)) for i in range(n))


def eye(n):
    return tuple(tuple(complex(1 if i == j else 0) for j in range(n)) for i in range(n))


def closure(gens, mulf, ident):
    seen, frontier = {ident}, [ident]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = mulf(x, g)
                if y not in seen:
                    seen.add(y)
                    new.append(y)
        frontier = new
    return seen


def twisted(k):
    """rho_T (x) chi_eta^k on (S, T), exact, as Gaussian-integer tuples when it has such entries"""
    rS, rT = BR.rho_exact()
    cS, cT = BR.chi(k)
    return cS * rS, cT * rT


def perm_of(O):
    """the permutation part of a signed permutation matrix: column j goes to row p[j]"""
    p = []
    for j in range(3):
        nz = [i for i in range(3) if O[i][j] != 0]
        assert len(nz) == 1
        p.append(nz[0])
    return p


def sign(p):
    s, seen = 1, set()
    for i in range(len(p)):
        if i in seen:
            continue
        j, n = i, 0
        while j not in seen:
            seen.add(j)
            j, n = p[j], n + 1
        s *= (-1) ** (n - 1)
    return s


def characters(O):
    p = perm_of(O)
    sg = sign(p)
    tr = int(round(sum(O[i][i] for i in range(3)).real))
    fix = sum(1 for j in range(3) if p[j] == j)
    return {"1": 1, "1'": sg, "2": fix - 1, "rho'": tr, "rho' (x) sgn": tr * sg}


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def sigma_mats(OS, OT):
    """each irrep's matrices on S and T, exact (sympy), from rho'(S), rho'(T)"""
    out = {}
    for g, O in (("S", OS), ("T", OT)):
        p = perm_of(O)
        sg = sign(p)
        Om = sp.Matrix(3, 3, lambda i, j: int(round(O[i][j].real)))
        P = sp.zeros(3, 3)
        for j in range(3):
            P[p[j], j] = 1
        B = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
        X = (B.T * B).inv() * B.T * P * B
        assert B * X == P * B
        out[g] = {"1": sp.Matrix([[1]]), "1'": sp.Matrix([[sg]]), "2": X, "rho'": Om, "rho' (x) sgn": sg * Om}
    return out


def npm(M):
    return np.array([[complex(sp.N(x)) for x in row] for row in M.tolist()], dtype=complex)


# ------------------------------------------------------------------ theta numerics
def thetas(tau, N=60):
    t2 = sum((mp.exp(I * mp.pi * tau * (n + mp.mpf(1) / 2) ** 2) for n in range(-N, N)), mp.mpc(0))
    t3 = sum((mp.exp(I * mp.pi * tau * n * n) for n in range(-N, N + 1)), mp.mpc(0))
    t4 = sum(((-1) ** n * mp.exp(I * mp.pi * tau * n * n) for n in range(-N, N + 1)), mp.mpc(0))
    return t2, t3, t4


def eta(tau, N=60):
    return sum(((-1) ** n * mp.exp(2 * I * mp.pi * tau * mp.mpf((6 * n + 1) ** 2) / 24) for n in range(-N, N + 1)),
               mp.mpc(0))


def vvec(tau):
    t2, t3, t4 = thetas(tau)
    return [-t2 ** 2, -t4 ** 2, I * t3 ** 2]


def Fa(a, tau):
    t2, t3, t4 = thetas(tau)
    e = eta(tau)
    eps = I ** ((a + 2) // 2)
    return [e ** (3 - a) * eps * t2 ** a, e ** (3 - a) * eps * t4 ** a, e ** (3 - a) * I * t3 ** a]


def relerr(u, w):
    num = max(abs(x - y) for x, y in zip(u, w))
    den = max(abs(y) for y in w)
    return float(num / den)


def apply(A, vec):
    return [sum((mp.mpc(A[i][j]) * vec[j] for j in range(len(vec))), mp.mpc(0)) for i in range(len(A))]


def taus():
    rng = random.Random(136)
    return [mp.mpc(mp.mpf(str(round(rng.uniform(-0.5, 0.5), 6))), mp.mpf(str(round(rng.uniform(0.8, 1.6), 6))))
            for _ in range(5)]


# ------------------------------------------------------------------ L0
def L0():
    PS21, PT21 = twisted(21)
    OS, OT = to_gauss(PS21), to_gauss(PT21)
    Pm = ((0, 1, 0), (1, 0, 0), (0, 0, 1))
    Li = ((1, 0, 0), (0, 0, 1), (0, -1, 0))
    c = {}
    c["rho'(S) = -P, rho'(T) = L^-1 (exact)"] = (OS == tuple(tuple(complex(-x) for x in r) for r in Pm)
                                                 and OT == tuple(tuple(complex(x) for x in r) for r in Li))
    E3 = eye(3)
    G = closure([OS, OT], mul, E3)
    signed = [m for m in G]
    is_sp_det1 = all(all(sum(1 for x in r if x != 0) == 1 for r in m) and all(x in (0, 1, -1) for r in m for x in r)
                     and det3(m) == 1 for m in signed)
    all_sp_det1 = set()
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            m = [[complex(0)] * 3 for _ in range(3)]
            for j in range(3):
                m[p[j]][j] = complex(s[j])
            m = tuple(tuple(r) for r in m)
            if det3(m) == 1:
                all_sp_det1.add(m)
    c["the image has 24 elements"] = len(G) == 24
    c["every element is a signed permutation of determinant 1, and all 24 such occur (the cube's rotations)"] = (
        is_sp_det1 and G == all_sp_det1)
    c["rho'(S)^2 = 1, so rho'(-I) = 1"] = mul(OS, OS) == E3
    T4 = mul(mul(OT, OT), mul(OT, OT))
    ST = mul(OS, OT)
    c["rho'(T)^4 = 1"] = T4 == E3
    c["(rho'(S) rho'(T))^3 = 1"] = mul(mul(ST, ST), ST) == E3
    F, s, t = free_group("s t")
    vd = FpGroup(F, [s ** 2, (s * t) ** 3, t ** 4]).order()
    c["<s, t | s^2, (st)^3, t^4> has order 24"] = int(vd) == 24
    sl24 = [((a, b), (cc, d)) for a, b, cc, d in itertools.product(range(4), repeat=4) if (a * d - b * cc) % 4 == 1]
    c["|SL(2, Z/4)| = 48"] = len(sl24) == 48

    def m4(A, B):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 4 for j in range(2)) for i in range(2))

    S4m, T4m = ((0, 3), (1, 0)), ((1, 1), (0, 1))
    graph = closure([(S4m, OS), (T4m, OT)], lambda x, y: (m4(x[0], y[0]), mul(x[1], y[1])), (((1, 0), (0, 1)), E3))
    firsts = {g[0] for g in graph}
    c["the pairs (gamma mod 4, rho'(gamma)) number 48 and project onto SL(2, Z/4): rho' factors through Z/4"] = (
        len(graph) == 48 and len(firsts) == 48)
    c["so the kernel is +-Gamma(4) and the group is PSL(2, Z/4) (index 24 = |image|)"] = (
        len(graph) == 48 and len(G) == 24 and int(vd) == 24)
    # v's multiplier rho_T (x) chi_eta^3 = rho' (x) chi_eta^6, paired with rho'
    PS3, PT3 = twisted(3)
    MS, MT = to_gauss(PS3), to_gauss(PT3)

    def scalar(M, O):
        i, j = next((i, j) for i in range(3) for j in range(3) if O[i][j] != 0)
        z = M[i][j] / O[i][j]
        ok = all(M[a][b] == z * O[a][b] for a in range(3) for b in range(3))
        return z, ok

    zS, okS = scalar(MS, OS)
    zT, okT = scalar(MT, OT)
    c["v's multiplier is rho' times a scalar on S and T"] = okS and okT
    pairs = closure([(MS, OS), (MT, OT)], lambda x, y: (mul(x[0], y[0]), mul(x[1], y[1])), (E3, E3))
    c["the image of SL(2, Z) on (v, rho') has 48 elements"] = len(pairs) == 48
    # numerics: v under S and T, Jacobi, theta_2 theta_3 theta_4 = 2 eta^3
    errs = {"S": [], "T": [], "Jacobi": [], "t2 t3 t4 = 2 eta^3": []}
    for tau in taus():
        v = vvec(tau)
        errs["S"].append(relerr(vvec(-1 / tau), [tau * x for x in apply(MS, v)]))
        errs["T"].append(relerr(vvec(tau + 1), apply(MT, v)))
        t2, t3, t4 = thetas(tau)
        errs["Jacobi"].append(float(abs(sum(x * x for x in v)) / abs(t3) ** 4))
        errs["t2 t3 t4 = 2 eta^3"].append(relerr([t2 * t3 * t4], [2 * eta(tau) ** 3]))
    worst = {k: max(v) for k, v in errs.items()}
    c["v transforms by rho_T (x) chi_eta^3 under S and T, to 1e-40"] = worst["S"] < 1e-40 and worst["T"] < 1e-40
    c["v.v = 0 and theta_2 theta_3 theta_4 = 2 eta^3, to 1e-40"] = (worst["Jacobi"] < 1e-40
                                                                     and worst["t2 t3 t4 = 2 eta^3"] < 1e-40)
    ranks = ring_ranks()
    c["the degree-w monomials in v span 2w + 1 q-series, w <= 12 (exact rank)"] = all(
        ranks[w] == 2 * w + 1 for w in ranks)
    out = {"checks": c, "worst numerical deviations": worst, "ranks by degree": ranks,
           "the scalar of v's multiplier over rho' on (S, T)": [str(zS), str(zT)],
           "the order of <s, t | s^2, (st)^3, t^4>": int(vd)}
    return out, all(c.values()), (OS, OT, G, pairs)


def ring_ranks():
    out = {}
    for w in range(0, 13):
        L = 4 * w + 24
        a2 = [0] * L
        a3 = [0] * L
        a4 = [0] * L
        r = range(-12, 13)
        for m in r:
            for n in r:
                e2 = 2 * (m * m + m + n * n + n) + 1
                e3 = 2 * (m * m + n * n)
                if e2 < L:
                    a2[e2] += 1
                if e3 < L:
                    a3[e3] += 1
                    a4[e3] += (-1) ** (m + n)

        def mult(u, v):
            o = [0] * L
            for i, x in enumerate(u):
                if x:
                    for j in range(L - i):
                        o[i + j] += x * v[j]
            return o

        def power(u, k):
            o = [1] + [0] * (L - 1)
            for _ in range(k):
                o = mult(o, u)
            return o

        rows = []
        for a in range(w + 1):
            for b in range(w + 1 - a):
                cexp = w - a - b
                rows.append(mult(mult(power(a2, a), power(a4, b)), power(a3, cexp)))
        out[w] = int(flint.fmpz_mat(rows).rank())
    return out


# ------------------------------------------------------------------ L1
def route_a(pairs, wmax):
    """multiplicities of each irrep in C[v]_w/(v.v), w = 0..wmax, exact (Gaussian integers)"""
    tab = {w: {s: 0 for s in IRREPS} for w in range(wmax + 1)}
    sums = {w: {s: complex(0) for s in IRREPS} for w in range(wmax + 1)}
    for M, O in pairs:
        i, j = next((i, j) for i in range(3) for j in range(3) if O[i][j] != 0)
        cM = M[i][j] / O[i][j]
        e1 = M[0][0] + M[1][1] + M[2][2]
        e2 = sum(M[a][a] * M[b][b] - M[a][b] * M[b][a] for a, b in ((0, 1), (0, 2), (1, 2)))
        e3 = det3(M)
        h = [complex(1)]
        for w in range(1, wmax + 1):
            x = e1 * h[w - 1] - (e2 * h[w - 2] if w >= 2 else 0) + (e3 * h[w - 3] if w >= 3 else 0)
            h.append(x)
        ch = characters(O)
        for w in range(wmax + 1):
            trw = h[w] - (cM * cM * h[w - 2] if w >= 2 else 0)
            for s in IRREPS:
                sums[w][s] += trw * ch[s]
    n = len(pairs)
    for w in range(wmax + 1):
        for s in IRREPS:
            z = sums[w][s]
            re, im = int(round(z.real)), int(round(z.imag))
            assert z == complex(re, im) and im == 0 and re % n == 0, (w, s, z)
            tab[w][s] = re // n
    return tab


def route_c(G, wmax):
    """multiplicities of each irrep in D_w (x) sgn^(w/2), even w, from the rotation angles (exact)"""
    tab = {}
    for w in range(0, wmax + 1, 2):
        acc = {s: Fr(0) for s in IRREPS}
        for O in G:
            ch = characters(O)
            x = Fr(ch["rho'"] - 1, 2)
            T = [Fr(1), x]
            for m in range(2, w + 1):
                T.append(2 * x * T[-1] - T[-2])
            chiD = 1 + 2 * sum(T[1:w + 1]) if w >= 1 else Fr(1)
            tw = ch["1'"] ** (w // 2)
            for s in IRREPS:
                acc[s] += chiD * tw * ch[s]
        tab[w] = {}
        for s in IRREPS:
            v = acc[s] / len(G)
            assert v.denominator == 1, (w, s, v)
            tab[w][s] = int(v)
    return tab


def route_b(sig, wmax):
    tab, allowed_bad = {}, []
    for k2 in range(1, 2 * wmax + 1):
        w = Fr(k2, 2)
        for s in IRREPS:
            al = IW.allowed(w, npm(sig["S"][s]))
            if (w.denominator == 1 and w.numerator % 2 == 0) != al:
                allowed_bad.append([str(w), s, al])
    for w in range(2, wmax + 1, 2):
        tab[w] = {}
        for s in IRREPS:
            val, _ = IW.chi(Fr(w), npm(sig["S"][s]), npm(sig["T"][s]))
            r = int(round(val))
            assert abs(val - r) < 1e-9, (w, s, val)
            tab[w][s] = r
    return tab, allowed_bad


def L1(OS, OT, G, pairs):
    sig = sigma_mats(OS, OT)
    a = route_a(pairs, WMAX)
    c_ = route_c(G, WMAX)
    b, allowed_bad = route_b(sig, WMAX)
    evens = list(range(0, WMAX + 1, 2))
    c = {}
    c["(a) = (c) at every even w <= 24"] = all(a[w] == c_[w] for w in evens)
    c["(a) = (b) at every even w from 2 to 24"] = all(a[w] == b[w] for w in evens if w >= 2)
    c["dim M_0(sigma) = [sigma = 1] in (a) and (c)"] = all(
        a[0][s] == (1 if s == "1" else 0) == c_[0][s] for s in IRREPS)
    c["(a) gives no form at odd w for any sigma"] = all(a[w][s] == 0 for w in range(1, WMAX + 1, 2) for s in IRREPS)
    c["W45's central character allows exactly the even integral weights (w in 1/2 .. 24)"] = not allowed_bad
    c["sum over sigma of dim sigma x dim M_w(sigma) = 2w + 1 (w >= 1)"] = all(
        sum(DIMS[s] * a[w][s] for s in IRREPS) == 2 * w + 1 for w in evens if w >= 1)
    c["the predicted table holds to w = 12"] = all(tuple(a[w][s] for s in IRREPS) == PRED[w] for w in PRED)
    numer = {}
    for s in IRREPS:
        d = lambda w: a[w][s] if 0 <= w <= WMAX else 0  # noqa: E731
        numer[s] = {w: d(w) - d(w - 4) - d(w - 6) + d(w - 10) for w in evens}
    gens_found = {s: [w for w in evens for _ in range(numer[s][w])] for s in IRREPS}
    c["the numerators of the Hilbert series are the predicted generating weights, to w = 24"] = all(
        all(numer[s][w] >= 0 for w in evens) and gens_found[s] == GENS[s] for s in IRREPS)
    lam = {}
    for s in IRREPS:
        ev = np.linalg.eigvals(npm(sig["T"][s]))
        lam[s] = [Fr(int(round(4 * ((np.angle(z) / (2 * np.pi)) % 1.0))) % 4, 4) for z in ev]
    c["each sum of generating weights equals 12 sum(lambda)"] = all(
        sum(GENS[s]) == 12 * sum(lam[s]) and sum(gens_found[s]) == 12 * sum(lam[s]) for s in IRREPS)
    table = {str(w): {s: a[w][s] for s in IRREPS} for w in evens}
    out = {"checks": c, "the table, even w to 24 (route a)": table,
           "route (b) disagreements": {str(w): [s for s in IRREPS if a[w][s] != b[w][s]] for w in evens if w >= 2},
           "route (c) disagreements": {str(w): [s for s in IRREPS if a[w][s] != c_[w][s]] for w in evens},
           "the generating weights found": gens_found, "the exponents lambda of sigma(T)": {
               s: [str(x) for x in lam[s]] for s in IRREPS},
           "the central-character exceptions": allowed_bad}
    return out, all(c.values()), a, sig


# ------------------------------------------------------------------ L2
def L2(OS, OT):
    rows = {}
    sgnS = characters(OS)["1'"]
    sgnT = characters(OT)["1'"]
    lawS = {"Y2 (rho', weight 2)": (2, OS), "Y4 (rho' (x) sgn, weight 4)": (4, tuple(
        tuple(sgnS * x for x in r) for r in OS)), "Y6 (1', weight 6)": (6, ((complex(sgnS),),))}
    lawT = {"Y2 (rho', weight 2)": OT, "Y4 (rho' (x) sgn, weight 4)": tuple(tuple(sgnT * x for x in r) for r in OT),
            "Y6 (1', weight 6)": ((complex(sgnT),),)}

    def forms(tau):
        v = vvec(tau)
        p = v[0] * v[1] * v[2]
        return {"Y2 (rho', weight 2)": [v[1] * v[2], v[2] * v[0], v[0] * v[1]],
                "Y4 (rho' (x) sgn, weight 4)": [p * x for x in v], "Y6 (1', weight 6)": [p * p]}

    worst = {k: {"S": 0.0, "T": 0.0} for k in lawS}
    ident = {"Y2 = -4i eta F_-2": 0.0, "Y4 = 8i eta^9 R": 0.0, "Y4 = 4i eta^5 F_2": 0.0, "Y6 = -16 eta^12": 0.0,
             "N(F_-2) = i 2^-2 eta^9": 0.0, "N(F_2) = i 2^2 eta^9": 0.0}
    for tau in taus():
        f0, fS, fT = forms(tau), forms(-1 / tau), forms(tau + 1)
        for k, (w, A) in lawS.items():
            worst[k]["S"] = max(worst[k]["S"], relerr(fS[k], [tau ** w * x for x in apply(A, f0[k])]))
            worst[k]["T"] = max(worst[k]["T"], relerr(fT[k], apply(lawT[k], f0[k])))
        e = eta(tau)
        v = vvec(tau)
        R = [x / (2 * e ** 3) for x in v]
        Fm2, F2 = Fa(-2, tau), Fa(2, tau)
        ident["Y2 = -4i eta F_-2"] = max(ident["Y2 = -4i eta F_-2"], relerr(
            f0["Y2 (rho', weight 2)"], [-4 * I * e * x for x in Fm2]))
        ident["Y4 = 8i eta^9 R"] = max(ident["Y4 = 8i eta^9 R"], relerr(
            f0["Y4 (rho' (x) sgn, weight 4)"], [8 * I * e ** 9 * x for x in R]))
        ident["Y4 = 4i eta^5 F_2"] = max(ident["Y4 = 4i eta^5 F_2"], relerr(
            f0["Y4 (rho' (x) sgn, weight 4)"], [4 * I * e ** 5 * x for x in F2]))
        ident["Y6 = -16 eta^12"] = max(ident["Y6 = -16 eta^12"], relerr(f0["Y6 (1', weight 6)"], [-16 * e ** 12]))
        ident["N(F_-2) = i 2^-2 eta^9"] = max(ident["N(F_-2) = i 2^-2 eta^9"], relerr(
            [Fm2[0] * Fm2[1] * Fm2[2]], [I * mp.mpf(1) / 4 * e ** 9]))
        ident["N(F_2) = i 2^2 eta^9"] = max(ident["N(F_2) = i 2^2 eta^9"], relerr(
            [F2[0] * F2[1] * F2[2]], [4 * I * e ** 9]))
    c = {"each least form transforms by its irrep under S and T, to 1e-30": all(
        d["S"] < 1e-30 and d["T"] < 1e-30 for d in worst.values()),
         "the identities with eta, R and F_a hold, to 1e-30": all(x < 1e-30 for x in ident.values())}
    rows = {"worst law deviations": worst, "worst identity deviations": ident,
            "why none vanishes on the upper half plane": (
                "eta and theta_2, theta_3, theta_4 have no zero on the upper half plane (their product formulas), and "
                "each component of Y2, Y4, Y6 is a product of their powers")}
    return {"checks": c, **rows}, all(c.values())


# ------------------------------------------------------------------ L3
def L3(OS, OT, sig, tab):
    P = sp.symbols("P0:3")
    cub = [m for m in itertools.combinations_with_replacement(range(3), 3)]
    mons = [P[i] * P[j] * P[k] for i, j, k in cub]
    Om = {g: sp.Matrix(3, 3, lambda i, j: int(round(O[i][j].real))) for g, O in (("S", OS), ("T", OT))}
    dims, named_ok = {}, {}
    for s in IRREPS:
        d = DIMS[s]
        Y = sp.symbols("Y0:%d" % d)
        cs = sp.symbols("c0:%d" % (d * len(mons)))
        f = sum(cs[a * len(mons) + m] * Y[a] * mons[m] for a in range(d) for m in range(len(mons)))
        eqs = []
        for g in ("S", "T"):
            Yn = sig[g][s] * sp.Matrix(Y)
            Pn = Om[g] * sp.Matrix(P)
            sub = {**{Y[a]: Yn[a] for a in range(d)}, **{P[i]: Pn[i] for i in range(3)}}
            diff = sp.expand(f.xreplace(sub) - f)
            eqs += sp.Poly(diff, *Y, *P).coeffs()
        A = sp.Matrix([[sp.diff(e, x) for x in cs] for e in eqs]) if eqs else sp.zeros(1, len(cs))
        dims[s] = len(cs) - A.rank()
    Phi = sp.Matrix(P)

    def inv_check(s, poly, Ysyms):
        ok = True
        for g in ("S", "T"):
            Yn = sig[g][s] * sp.Matrix(Ysyms)
            Pn = Om[g] * Phi
            sub = {**{Ysyms[a]: Yn[a] for a in range(len(Ysyms))}, **{P[i]: Pn[i] for i in range(3)}}
            ok &= sp.expand(poly.xreplace(sub) - poly) == 0
        return bool(ok)

    Y1 = sp.symbols("Y0:1")
    Y3 = sp.symbols("Y0:3")
    named = {
        "1': Y Phi_1 Phi_2 Phi_3": ("1'", Y1[0] * P[0] * P[1] * P[2], Y1),
        "rho': (Y.Phi)(Phi.Phi)": ("rho'", sum(Y3[a] * P[a] for a in range(3)) * sum(P[a] ** 2 for a in range(3)), Y3),
        "rho': sum Y_a Phi_a^3": ("rho'", sum(Y3[a] * P[a] ** 3 for a in range(3)), Y3),
        "rho' (x) sgn: sum Y_a Phi_a (Phi_{a+1}^2 - Phi_{a+2}^2)": (
            "rho' (x) sgn", sum(Y3[a] * P[a] * (P[(a + 1) % 3] ** 2 - P[(a + 2) % 3] ** 2) for a in range(3)), Y3)}
    for k, (s, poly, Ys) in named.items():
        named_ok[k] = inv_check(s, poly, Ys)
    rho_ind = sp.Matrix([[sp.Poly(poly, *Y3, *P).coeff_monomial(Y3[a] * mons[m]) for a in range(3)
                          for m in range(len(mons))] for (s, poly, _) in
                         (named["rho': (Y.Phi)(Phi.Phi)"], named["rho': sum Y_a Phi_a^3"])]).rank()
    # Sym^3 for k = 5, 13 against k = 21
    sym_same = {}
    S21, T21 = twisted(21)
    for k in (5, 13):
        Sk, Tk = twisted(k)
        ok = True
        for A, B in ((Sk, S21), (Tk, T21)):
            i, j = next((i, j) for i in range(3) for j in range(3) if B[i, j] != 0)
            z = sp.simplify(A[i, j] / B[i, j])
            ok &= all(sp.simplify(sp.expand_complex(A[a, b] - z * B[a, b])) == 0 for a in range(3) for b in range(3))
            ok &= sp.simplify(sp.expand_complex(z ** 3 - 1)) == 0
        sym_same[str(k)] = bool(ok)
    C = {w: tab[w]["1'"] + 2 * tab[w]["rho'"] + tab[w]["rho' (x) sgn"] for w in range(0, WMAX + 1, 2)}
    c = {"the invariant cubics have dimensions 0, 1, 0, 2, 1": [dims[s] for s in IRREPS] == [0, 1, 0, 2, 1],
         "the named basis is invariant": all(named_ok.values()),
         "the two rho' channels are independent": rho_ind == 2,
         "Sym^3 rho'_k = Sym^3 rho'_21 for k = 5 and 13 (the scalars cube to 1)": all(sym_same.values()),
         "C(w) = 0, 2, 3, 6, 6, 9, 10 at w = 0 .. 12": all(C[w] == PRED_C[w] for w in PRED_C)}
    return {"checks": c, "dimensions of the invariant cubics": dims, "the named basis": named_ok,
            "C(w), even w to 24": {str(w): C[w] for w in C}}, all(c.values()), C


# ------------------------------------------------------------------ L4
def L4(tab, C):
    g1, g2 = sp.symbols("g1 g2")
    Y = sp.symbols("Y0:3")
    h = sp.symbols("h0:3")
    P = sp.symbols("P0:3")
    W = g1 * sum(Y[a] * P[a] for a in range(3)) * sum(P[a] ** 2 for a in range(3)) + g2 * sum(
        Y[a] * P[a] ** 3 for a in range(3))
    lam = lambda i, j, k: sp.diff(W, P[i], P[j], P[k]) / 6  # noqa: E731
    M = sp.Matrix(3, 3, lambda j, k: 3 * sum(h[i] * lam(i, j, k) for i in range(3)))
    Yv, hv = sp.Matrix(Y), sp.Matrix(h)
    pred = g1 * ((Yv.T * hv)[0] * sp.eye(3) + Yv * hv.T + hv * Yv.T) + 3 * g2 * sp.diag(*[Y[a] * h[a] for a in range(3)])
    same = sp.simplify(M - pred) == sp.zeros(3, 3)
    evens = range(0, WMAX + 1, 2)
    least = {s: min((w for w in evens if tab[w][s] > 0), default=None) for s in IRREPS}
    absent = {s: [w for w in evens if tab[w][s] == 0] for s in IRREPS}
    return {"the least weight carrying a form": least, "the even weights carrying none (to 24)": absent,
            "C(w), the independent couplings of three families at weight w": {str(w): C[w] for w in C},
            "the least couplings": {
                "weight 2, rho' (two channels)": "Y2 = (v2 v3, v3 v1, v1 v2) = -4i eta F_-2",
                "weight 4, rho' (x) sgn": "Y4 = v1 v2 v3 v = 8i eta^9 R = 4i eta^5 F_2",
                "weight 6, 1'": "Y6 = (v1 v2 v3)^2 = -16 eta^12"},
            "the weight-2 coupling's mass matrix for a Higgs direction h": str(M),
            "it equals g1[(Y.h)1 + Y h^T + h Y^T] + 3 g2 diag(Y_a h_a)": bool(same)}


def main():
    l0, ok0, (OS, OT, G, pairs) = L0()
    l1, ok1, tab, sig = L1(OS, OT, G, pairs)
    l2, ok2 = L2(OS, OT)
    l3, ok3, C = L3(OS, OT, sig, tab)
    l4 = L4(tab, C)
    cells = {"L0": ok0, "L1": ok1, "L2": ok2, "L3": ok3}
    out = {"arc": "W136", "rule": "W136_RULE.md", "status": "one run", "L0": l0, "L1": l1, "L2": l2, "L3": l3,
           "L4 (read-out)": l4, "cells": {k: bool(v) for k, v in cells.items()},
           "every cell holds": bool(all(cells.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))
    print("every cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
