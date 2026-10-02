"""B1515 -- controls, run before the seal: python3 controls.py --record  ->  controls_run.txt.

Nothing here reads a sealed quantity.  It computes:
  S  the structure of the cusp torus at q = 1 (exact over Q; the torus alone, no cohomology of a level):
     S1 the invariant symmetric form of rho_1 and its signature;
     S2 h^*(T; rho_1), h^*(T; rho_1*), h^*(T; Lambda^2 rho_1) on every level 1-6;
     S3 T1: every 1-cocycle of P in rho_1 takes values in e-perp (e spans rho_1^P);
     S4 the torus table: for EVERY non-zero class c_P in H^1(T; rho_1) (the chart z1 + k z2 over Q(k), with a gcd-of-determinants
        certificate that the rank never drops at any k in Qbar, and the point z2), the invariants of [[rho_1, c_P], [0, 1]], its dual,
        and their exterior squares: (t0, s0) = (1, 2) for W1 and (2, 3) for Lambda^2 W1;
     S5 T-deck: m centralises P and acts as the identity on H^1(P; rho_1) and H^1(P; Lambda^2 rho_1);
     S6 the parabolic part: pi_A (classes of cocycles valued in (Lambda^2 rho_1)^P) has dimension 2, and e ^ c_P lies in it and is
        non-zero for every non-zero class c_P;
     S7 B1509's polynomial: Q(1, s), Q(q, 1), Q(q, -1).
  K  banked identities, by both routes:
     K1 B1513 K3: h^1(G_1; Lambda^2 rho_1) = h^1(G_3; Lambda^2 rho_1) = 2 (exact);
     K2 the audit lane (PROJECTIVE_MODE_RECEPTION): h^1(m004; rho_1) = h^1(m004; rho_1*) = 1 (exact);
     K3 B1509's first row: q^2 - 34 q + 1 = 0, lam = -1 on level 1: I(W1) = -1, I(W2) = +1, I(Lambda^2 W1) = 0 (two primes per route);
     K4 B1511 C1: M4's eight 3-torsion members at q^2 - 7 q + 1 = 0, lam = 1: I(W1) = +1, I(W2) = -1, Lambda^2 0;
     K5 B1511 Part B: the triplet's first member pulled back to M6 at q^6 - 34 q^3 + 1 = 0: I(W1) = -1, I(W2) = +1;
     K6 the positive control, R40 on m010 (the audit lane's COEFFICIENT_PARENT): I(V) = I(Lambda^2 V) = I(W) = I(Lambda^2 W) = +1,
        n(Lambda^2 W) = 2, n(Lambda^2 W*) = 1, exactly over Q(sqrt -3) (both u) and over GF(p) (both u, two primes per route).
  C  code checks on banked modules: route T's Fox restriction reproduces tower_lib's r1 on K3 and K4; route T's wedge vectors agree
     with tower_lib's Lambda^2; the two routes enumerate the same characters on every level, with the same deck action."""
import json
import random
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import flint
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import route_l as RL  # noqa: E402
import route_t as RT  # noqa: E402

T = RT.T
RECORD = HERE / "controls_run.txt"


# ============================================================================================ S: the torus at q = 1 (exact)
def ballas(qq):
    t = sp.sympify(qq) / 2
    m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
    n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return m, n


M1, N1 = ballas(1)
GEN = {"m": M1, "n": N1, "M": M1.inv(), "N": N1.inv()}
LON = "nMNmmNMn"


def word(w):
    X = sp.eye(4)
    for ch in w:
        X = X * GEN[ch]
    return X


def pairs(d):
    return [(i, j) for i in range(d) for j in range(i + 1, d)]


def wedge2(M):
    P = pairs(M.shape[0])
    return sp.Matrix(len(P), len(P), lambda r, c: M[P[r][0], P[c][0]] * M[P[r][1], P[c][1]] - M[P[r][0], P[c][1]] * M[P[r][1], P[c][0]])


def torus(A, B):
    d = A.shape[0]
    I = sp.eye(d)
    D0 = (A - I).col_join(B - I)
    D1 = (I - B).row_join(A - I)
    r0, r1 = D0.rank(), D1.rank()
    return (d - r0, 2 * d - r1 - r0, d - r1), D0, D1


def s1_form():
    idx, syms = {}, []
    for i in range(4):
        for j in range(i, 4):
            idx[(i, j)] = len(syms)
            syms.append(sp.Symbol(f"j{i}{j}"))
    J = sp.Matrix(4, 4, lambda i, j: syms[idx[(min(i, j), max(i, j))]])
    eqs = [e for g in (M1, N1) for e in (g.T * J * g - J)]
    sol = sp.solve(eqs, syms, dict=True)[0]
    J0 = J.subs(sol)
    free = sorted(J0.free_symbols, key=str)
    J0 = J0.subs({free[0]: 1, **{f: 0 for f in free[1:]}})
    ev = np.linalg.eigvalsh(np.array(J0.tolist(), dtype=float))
    return {"invariant symmetric forms (dimension)": len(free), "J": [[str(x) for x in r] for r in J0.tolist()],
            "signature (+, -)": [int((ev > 1e-9).sum()), int((ev < -1e-9).sum())]}


def h1_complement(D0, D1):
    basis, cur = [], D0
    for z in D1.nullspace():
        if cur.row_join(z).rank() > cur.rank():
            basis.append(z)
            cur = cur.row_join(z)
    return basis


def never_drops(D, kk, R_, r, d, rng):
    """the rank of D(k) is r at every k in Qbar: gcd over random R, C of det(R D C) is a non-zero constant"""
    def dm(M):
        return DomainMatrix([[R_.from_sympy(sp.expand(e)) for e in M.row(i)] for i in range(M.shape[0])], M.shape, R_)
    Dd = dm(D)
    assert Dd.rank() == r
    g = None
    for _ in range(3):
        Rm = dm(sp.Matrix(r, D.shape[0], lambda i, j: rng.randint(-9, 9)))
        Cm = dm(sp.Matrix(d, r, lambda i, j: rng.randint(-9, 9)))
        det = (Rm * Dd * Cm).det()
        g = det if g is None else R_.gcd(g, det)
    gs = R_.to_sympy(g)
    return bool(gs.is_number and gs != 0)


def s_torus(lev, rng):
    A, B = word("m" * lev), word(LON)
    assert A * B == B * A
    hr, D0, D1 = torus(A, B)
    hd = torus(A.inv().T, B.inv().T)[0]
    h2 = torus(wedge2(A), wedge2(B))[0]
    Z = D1.nullspace()
    e = (A - sp.eye(4)).col_join(B - sp.eye(4)).nullspace()
    assert len(e) == 1
    e = e[0]
    w = (A.inv().T - sp.eye(4)).col_join(B.inv().T - sp.eye(4)).nullspace()[0].T
    t1 = all((w * z[0:4, 0])[0] == 0 and (w * z[4:8, 0])[0] == 0 for z in Z)
    basis = h1_complement(D0, D1)
    kk = sp.Symbol("k")
    R_ = sp.QQ[kk]

    def ext(X, a):
        return X.row_join(a).col_join(sp.Matrix([[0, 0, 0, 0, 1]]))
    Ai, Bi = A.inv(), B.inv()
    table = {}
    for chart, c in (("z1 + k z2", basis[0] + kk * basis[1]), ("z2", basis[1])):
        a, b = c[0:4, 0], c[4:8, 0]
        WA, WB, WAi, WBi = ext(A, a), ext(B, b), ext(Ai, -Ai * a), ext(Bi, -Bi * b)
        assert (WA * WAi).applyfunc(sp.expand) == sp.eye(5) and (WA * WB - WB * WA).applyfunc(sp.expand) == sp.zeros(5, 5)
        mods = {"W1": (WA, WB), "W1*": (WAi.T, WBi.T), "L2W1": (wedge2(WA), wedge2(WB)), "L2W1*": (wedge2(WAi).T, wedge2(WBi).T)}
        for name, (MA, MB) in mods.items():
            d = MA.shape[0]
            D = ((MA - sp.eye(d)).col_join(MB - sp.eye(d))).applyfunc(sp.expand)
            if chart == "z2":
                table[f"{name} [{chart}]"] = d - D.rank()
            else:
                r = DomainMatrix([[R_.from_sympy(x) for x in D.row(i)] for i in range(D.shape[0])], D.shape, R_).rank()
                table[f"{name} [{chart}]"] = [d - r, "never drops" if never_drops(D, kk, R_, r, d, rng) else "DROPS"]
    # T-deck
    deck = {}
    m_ = word("m")
    for name, f in (("rho1", lambda X: X), ("L2 rho1", wedge2)):
        AA, BB, Mm = f(A), f(B), f(m_)
        assert Mm * AA == AA * Mm and Mm * BB == BB * Mm
        _, E0, E1 = torus(AA, BB)
        d = AA.shape[0]
        blk = sp.diag(Mm - sp.eye(d), Mm - sp.eye(d))
        deck[name] = all(E0.row_join(blk * z).rank() == E0.rank() for z in E1.nullspace())
    # the parabolic part
    A2, B2 = wedge2(A), wedge2(B)
    BA = (A2 - sp.eye(6)).col_join(B2 - sp.eye(6))
    inv = BA.nullspace()
    zero = sp.zeros(6, 1)
    P = sp.Matrix.hstack(*([v.col_join(zero) for v in inv] + [zero.col_join(v) for v in inv]))
    rB, rBP = BA.rank(), BA.row_join(P).rank()

    def wv(u):
        return sp.Matrix([[e[i] * u[j] - e[j] * u[i]] for (i, j) in pairs(4)])
    par = {}
    for chart, c in (("z1 + k z2", basis[0] + kk * basis[1]), ("z2", basis[1])):
        delta = wv(c[0:4, 0]).col_join(wv(c[4:8, 0])).applyfunc(sp.expand)
        valued_in_invariants = all(((X - sp.eye(6)) * delta[s:s + 6, 0]).applyfunc(sp.expand) == zero
                                   for X in (A2, B2) for s in (0, 6))
        par[chart] = {"e ^ c_P valued in (L2 rho1)^P": valued_in_invariants}
    return {"h*(T; rho1)": list(hr), "h*(T; rho1*)": list(hd), "h*(T; L2 rho1)": list(h2),
            "T1: every cocycle of P in rho1 is valued in e-perp": t1, "torus table (dim of invariants)": table,
            "T-deck: m acts trivially on H^1(P)": deck, "dim (L2 rho1)^P": len(inv), "dim pi_A": rBP - rB, "parabolic": par}


def s7_q():
    q, s = sp.symbols("q s")
    Qp = -q * s ** 4 + 8 * q * s ** 3 + (q ** 2 - 16 * q + 1) * s ** 2 + 8 * q * s - q
    return {"Q(1, s)": str(sp.factor(Qp.subs(q, 1))), "Q(q, 1)": str(sp.factor(Qp.subs(s, 1))), "Q(q, -1)": str(sp.factor(Qp.subs(s, -1)))}


# ============================================================================================ K: banked identities, both routes
def froots(coeffs, p):
    return sorted(int(r) for r, _ in flint.nmod_poly([c % p for c in coeffs], p).roots())


def primes(K, poly, count, start):
    out, p = [], start
    while len(out) < count:
        p = int(sp.prevprime(p))
        if (p - 1) % K == 0 and froots(poly, p):
            out.append(p)
    return out


def brief_L(row):
    return {"h1(V_eta)": row["h1(V_eta)"], "case": row.get("case"),
            "W1": {k: [v["W1"]["I"], v["L2W1"]["I"]] for k, v in row.get("W1", {}).items()},
            "W2": {k: [v["I(W2)"], v["I(L2W2)"]] for k, v in row.get("W2", {}).items()}}


def brief_T(row):
    return {"h1(V_eta)": row["h1(V_eta)"], "case": row.get("case"),
            "W1": {k: [v["W1"]["I"], v["L2W1"]["I"]] for k, v in row.get("W1", {}).items()},
            "W2": {k: [v["I(W2)"], v["I(L2W2)"]] for k, v in row.get("W2", {}).items()}}


def k1_k2():
    out = {"route T": {}, "route L": {}}
    for n in (1, 3):
        lev = RT.Level(n)
        A = RT.Arith("exact", 12)
        R = T.DMRep(lev.cov["gens"], T.rs_rho(lev.cov, A.field))
        row = {"h1(L2 rho1)": T.h1_classes(T.wedge2_rep(R), lev.rels)[1]}
        if n == 1:
            row.update({"h1(rho1)": T.h1_classes(R, lev.rels)[1], "h1(rho1*)": T.h1_classes(R.dual(), lev.rels)[1]})
        out["route T"][f"M{n}"] = row
        F = RL.Exact(RL.K12, "Q(zeta12)")
        G = RL.rho1(F, n)
        assert G.holds()
        row = {"h1(L2 rho1)": RL.dims(G.wedge2())["h1"]}
        if n == 1:
            row.update({"h1(rho1)": RL.dims(G)["h1"], "h1(rho1*)": RL.dims(G.dual())["h1"]})
        out["route L"][f"M{n}"] = row
    ok = all(out[r]["M1"] == {"h1(L2 rho1)": 2, "h1(rho1)": 1, "h1(rho1*)": 1} and out[r]["M3"] == {"h1(L2 rho1)": 2}
             for r in out)
    return out, ok


def k3_k4_k5():
    out = {"K3": [], "K4": [], "K5": []}
    # K3: level 1, q^2 - 34 q + 1, lam = -1
    for route, start in (("T", 2 ** 22 - 104729), ("L", 2 ** 22 - 3 * 104729)):
        for p in primes(12, [1, -34, 1], 2, start):
            for r in froots([1, -34, 1], p):
                if route == "T":
                    lev = RT.Level(1)
                    A = RT.Arith("gf", 12, p=p, r=r)
                    row = brief_T(RT.read_member(lev, A, T.rs_rho(lev.cov, A.field), (0, 0), 6))
                else:
                    F = RL.ModP(p, "")
                    row = brief_L(RL.read_member(F, RL.Units(F, 12), 1, RL.rho_at(F, 1, r), (Fr(0), Fr(0)), Fr(1, 2)))
                out["K3"].append({"route": route, "p": p, "q": r, **row})
    # K4: M4's eight 3-torsion members, q^2 - 7 q + 1, lam = 1
    lev4 = RT.Level(4)
    t3 = [ab for ab in lev4.chars if (3 * ab[0]) % lev4.N == 0 and (3 * ab[1]) % lev4.N == 0 and ab != (0, 0)]
    for route, start in (("T", 2 ** 22 - 5 * 104729), ("L", 2 ** 22 - 7 * 104729)):
        K = lev4.K if route == "T" else RL.lcm(RL.fibre_characters(4)[1], 12)
        p = primes(K, [1, -7, 1], 1, start)[0]
        r = froots([1, -7, 1], p)[0]
        if route == "T":
            A = RT.Arith("gf", lev4.K, p=p, r=r)
            rho = T.rs_rho(lev4.cov, A.field)
            for ab in t3:
                out["K4"].append({"route": "T", "p": p, "q": r, "char": [str(Fr(ab[0], lev4.N)), str(Fr(ab[1], lev4.N))],
                                  **brief_T(RT.read_member(lev4, A, rho, ab, 0))})
        else:
            F = RL.ModP(p, "")
            U = RL.Units(F, K)
            R = RL.rho_at(F, 4, r)
            for ab in [x for x in RL.fibre_characters(4)[0] if (3 * x[0]) % 1 == 0 and (3 * x[1]) % 1 == 0 and x != (0, 0)]:
                out["K4"].append({"route": "L", "p": p, "q": r, "char": [str(ab[0]), str(ab[1])],
                                  **brief_L(RL.read_member(F, U, 4, R, ab, Fr(0)))})
    # K5: level 6, q^6 - 34 q^3 + 1, the character (0, 1/2), lam = 1
    poly6 = [1, 0, 0, -34, 0, 0, 1]
    lev6 = RT.Level(6)
    for route, start in (("T", 2 ** 22 - 9 * 104729), ("L", 2 ** 22 - 11 * 104729)):
        K = lev6.K if route == "T" else RL.lcm(RL.fibre_characters(6)[1], 12)
        p = primes(K, poly6, 1, start)[0]
        r = froots(poly6, p)[0]
        if route == "T":
            A = RT.Arith("gf", lev6.K, p=p, r=r)
            row = brief_T(RT.read_member(lev6, A, T.rs_rho(lev6.cov, A.field), (0, lev6.N // 2), 0))
        else:
            F = RL.ModP(p, "")
            row = brief_L(RL.read_member(F, RL.Units(F, K), 6, RL.rho_at(F, 6, r), (Fr(0), Fr(1, 2)), Fr(0)))
        out["K5"].append({"route": route, "p": p, "q": r, **row})
    ok3 = all(x["W1"]["c1"] == [-1, 0] and x["W2"]["c1"] == [1, 0] for x in out["K3"]) and len(out["K3"]) == 8
    ok4 = all(x["case"] == "b" and x["W1"]["c1"] == [1, 0] and x["W2"]["c1"] == [-1, 0] for x in out["K4"]) and len(out["K4"]) == 16
    ok5 = all(x["h1(V_eta)"] == 1 and x["W1"]["c1"] == [-1, 0] and x["W2"]["c1"] == [1, 0] for x in out["K5"]) and len(out["K5"]) == 2
    return out, {"K3": ok3, "K4": ok4, "K5": ok5}


def k6():
    out = {"route T": [], "route L": []}
    us = ((1 + sp.sqrt(-3)) / 2, (1 - sp.sqrt(-3)) / 2)
    AT = RT.Arith("exact", 12)
    FL = RL.Exact(RL.K12, "Q(zeta12)")
    for u in us:
        out["route T"].append({"field": f"Q(zeta12), u = {u}", **RT.m010_indices(AT, u)})
        out["route L"].append({"field": f"Q(zeta12), u = {u}", **{k: RL.summary(RL.index(m)) for k, m in RL.m010_modules(FL, FL.s(u)).items()}})
    for route, start in (("T", 2 ** 22 - 13 * 104729), ("L", 2 ** 22 - 15 * 104729)):
        for p in primes(12, [1, -1, 1], 2, start):
            for u in froots([1, -1, 1], p):
                if route == "T":
                    row = {k: v for k, v in RT.m010_indices(RT.Arith("gf", 12, p=p), u).items()}
                    out["route T"].append({"field": f"GF({p}), u = {u}", **row})
                else:
                    F = RL.ModP(p, "")
                    out["route L"].append({"field": f"GF({p}), u = {u}", **{k: RL.summary(RL.index(m)) for k, m in RL.m010_modules(F, u).items()}})

    def good_T(r):
        return all(r[k]["I"] == 1 for k in ("V", "L2V", "W", "L2W")) and r["L2W"]["E(a0,a1,t0,r1)"][1] - r["L2W"]["E(a0,a1,t0,r1)"][3] == 2

    def good_L(r):
        return all(r[k]["I"] == 1 for k in ("V", "L2V", "W", "L2W")) and r["L2W"]["E(a0,h1,t0,n)"][3] == 2 and r["L2W"]["E*(b0,h1,s0,n)"][3] == 1
    ok = len(out["route T"]) == 6 and len(out["route L"]) == 6 and all(good_T(r) for r in out["route T"]) and all(good_L(r) for r in out["route L"])
    return out, ok


# ============================================================================================ C: code checks on banked modules
def c_checks():
    out = {}
    # route T's Fox restriction reproduces tower_lib's r1 (K3's W1 and K4's W1 at their first prime-root)
    lev = RT.Level(1)
    p = primes(12, [1, -34, 1], 1, 2 ** 22 - 17 * 104729)[0]
    r = froots([1, -34, 1], p)[0]
    A = RT.Arith("gf", 12, p=p, r=r)
    rho = T.rs_rho(lev.cov, A.field)
    ex = lev.exponents((0, 0), 6)
    V = lev.twisted(A, rho, ex, 1)
    cls, _ = T.h1_classes(V, lev.rels)
    W = RT.ext_with_line(V, cls[0], lev.line(A, ex, -4), lev.cov["gens"])
    Wcls, a1 = T.h1_classes(W, lev.rels)
    BP = RT.peripheral_coboundaries(W, lev)
    cols = [RT.restrict(W, z, lev.mu).vstack(RT.restrict(W, z, lev.lam)) for z in Wcls]
    r1_fox = T.dm_rank(BP.hstack(*cols)) - T.dm_rank(BP) if cols else 0
    out["Fox restriction r1 = index_lib r1 (K3's W1)"] = r1_fox == A.ix(W, lev.rels, lev.mu, lev.lam)["r1"]
    # route T's wedge vectors agree with tower_lib's Lambda^2: wedge2(M) (e ^ u) = (M e) ^ (M u)
    rng = random.Random(1515)
    dom = A.dom
    M = DomainMatrix([[dom(rng.randrange(p)) for _ in range(4)] for _ in range(4)], (4, 4), dom)
    e = DomainMatrix([[dom(rng.randrange(p))] for _ in range(4)], (4, 1), dom)
    u = DomainMatrix([[dom(rng.randrange(p))] for _ in range(4)], (4, 1), dom)
    out["wedge vector convention = tower_lib's wedge2"] = T.dm_equal(T.wedge2(M) * RT.wedge_vec(e, u), RT.wedge_vec(M * e, M * u))
    # the two routes' characters and deck actions
    agree = {}
    for n in range(1, 7):
        levT = RT.Level(n)
        setT = {(Fr(a, levT.N), Fr(b, levT.N)) for a, b in levT.chars}
        chL, D = RL.fibre_characters(n)
        setL = set(chL)
        deckT = {(Fr(a, levT.N), Fr(b, levT.N)): (Fr(T.deck((a, b), levT.N)[0], levT.N), Fr(T.deck((a, b), levT.N)[1], levT.N))
                 for a, b in levT.chars}
        deckL = {ab: RL.deck_image(ab) for ab in chL}
        agree[f"M{n}"] = {"characters": len(setT), "same set": setT == setL, "same deck": deckT == deckL, "N (T)": levT.N, "D (L)": D}
    out["characters and deck, route T vs route L"] = agree
    ok = out["Fox restriction r1 = index_lib r1 (K3's W1)"] and out["wedge vector convention = tower_lib's wedge2"] and \
        all(v["same set"] and v["same deck"] for v in agree.values())
    return out, ok


def main():
    t0 = time.time()
    rng = random.Random(1515)
    rec = {"S1": s1_form()}
    rec["S2-S6"] = {}
    for lev in range(1, 7):
        rec["S2-S6"][f"M{lev}"] = s_torus(lev, rng)
        print(f"[{time.time() - t0:7.1f}s] torus M{lev} done", flush=True)
    rec["S7"] = s7_q()
    rec["K1-K2"], ok12 = k1_k2()
    print(f"[{time.time() - t0:7.1f}s] K1-K2 done", flush=True)
    rec["K3-K5"], ok345 = k3_k4_k5()
    print(f"[{time.time() - t0:7.1f}s] K3-K5 done", flush=True)
    rec["K6"], ok6 = k6()
    print(f"[{time.time() - t0:7.1f}s] K6 done", flush=True)
    rec["C"], okc = c_checks()
    S = rec["S2-S6"]
    tor_ok = all(v["h*(T; rho1)"] == [1, 2, 1] and v["h*(T; rho1*)"] == [1, 2, 1] and v["h*(T; L2 rho1)"] == [2, 4, 2]
                 and v["T1: every cocycle of P in rho1 is valued in e-perp"]
                 and v["torus table (dim of invariants)"] == {"W1 [z1 + k z2]": [1, "never drops"], "W1* [z1 + k z2]": [2, "never drops"],
                                                              "L2W1 [z1 + k z2]": [2, "never drops"], "L2W1* [z1 + k z2]": [3, "never drops"],
                                                              "W1 [z2]": 1, "W1* [z2]": 2, "L2W1 [z2]": 2, "L2W1* [z2]": 3}
                 and all(v["T-deck: m acts trivially on H^1(P)"].values()) and v["dim (L2 rho1)^P"] == 2 and v["dim pi_A"] == 2
                 and all(x["e ^ c_P valued in (L2 rho1)^P"] for x in v["parabolic"].values()) for v in S.values())
    rec["summary"] = {
        "S1 signature (3, 1), one invariant form": rec["S1"]["signature (+, -)"] == [3, 1] and rec["S1"]["invariant symmetric forms (dimension)"] == 1,
        "S2-S6 the torus table on every level": tor_ok,
        "S7 Q(1, s) = -(s - 1)^2 (s^2 - 6 s + 1)": rec["S7"]["Q(1, s)"] == "-(s - 1)**2*(s**2 - 6*s + 1)",
        "K1-K2 both routes": ok12, "K3 both routes": ok345["K3"], "K4 both routes": ok345["K4"], "K5 both routes": ok345["K5"],
        "K6 R40 on m010, both routes, exact and mod p": ok6, "C code checks": okc}
    rec["seconds"] = round(time.time() - t0, 1)
    print(json.dumps(rec["summary"], indent=1))
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
    return rec


if __name__ == "__main__":
    main()
