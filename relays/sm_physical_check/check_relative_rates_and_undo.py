#!/usr/bin/env python3
"""The SM seat's check of the physical lane's RELATIVE_RATES_AND_THE_ROLE_OF_A_MOVE.md and
INTERNAL_REGISTRATION_AND_FULL_UNDO.md (audit/physical-bridge-2026-09-05 at 798281903): every finite, algebraic or
numerically checkable claim, plus planted countercontrols that must fail, on this seat's own code.
    python3 check_relative_rates_and_undo.py
Composition is right to left: (g h)(s) = g(h(s)). Pullbacks act on column functions: (G f)(s) = f(g(s))."""
import itertools
import json
import pathlib

import numpy as np
import sympy as sp
from scipy.linalg import expm

out = {}
plants = {}


def rec(key, ok, detail=""):
    out[key] = {"holds": bool(ok), "detail": detail}


def plant(key, ok, detail=""):
    # a countercontrol: it is expected to FAIL (ok is False)
    plants[key] = {"fails_as_expected": not bool(ok), "detail": detail}


# ------------------------------------------------------------------ generic finite-group tools
def states(m, d=2):
    return list(itertools.product(range(m), repeat=d))


def as_perm(g, S):
    idx = {s: i for i, s in enumerate(S)}
    return tuple(idx[g(s)] for s in S)


def compose(p, q):  # (p q)(i) = p(q(i))
    return tuple(p[q[i]] for i in range(len(q)))


def inverse(p):
    inv = [0] * len(p)
    for i, j in enumerate(p):
        inv[j] = i
    return tuple(inv)


def closure(gens):
    e = tuple(range(len(gens[0])))
    G, frontier = {e}, [e]
    while frontier:
        new = []
        for h in frontier:
            for g in gens:
                k = compose(g, h)
                if k not in G:
                    G.add(k); new.append(k)
        frontier = new
    return G


def order(p):
    e, k, q = tuple(range(len(p))), 1, p
    while q != e:
        q = compose(p, q); k += 1
    return k


def pullback(p):  # matrix G with (G f)(i) = f(p(i))
    n = len(p); M = sp.zeros(n, n)
    for i in range(n):
        M[i, p[i]] = 1
    return M


# ================================================================== RELATIVE RATES
S2 = states(2)
fx = lambda s: ((s[0] + 1) % 2, s[1])
fr = lambda s: (s[0], (s[1] + 1) % 2)
Um2 = lambda s: (s[0], (s[1] + s[0]) % 2)
Vm2 = lambda s: ((s[0] + 1) % 2, s[1])
Jm2 = lambda s: (s[1], s[0])
Fx, Fr = pullback(as_perm(fx, S2)), pullback(as_perm(fr, S2))
Fb = pullback(as_perm(lambda s: fx(fr(s)), S2))
I4 = sp.eye(4); Pi = sp.ones(4, 4) / 4
rec("RR s2: F_x, F_r commute, square to I, product flips both",
    Fx * Fr == Fr * Fx and Fx ** 2 == I4 and Fr ** 2 == I4 and Fx * Fr == Fb)
a, b, c, t, s = sp.symbols("a b c t s", positive=True)
L = a * (Fx + Fr - 2 * I4) + b * (Fx * Fr - I4) + c * (Pi - I4)
offdiag = [sp.simplify(L[i, j]) for i in range(4) for j in range(4) if i != j]
rec("RR (1): off-diagonals of L nonnegative, rows and columns sum 0, L symmetric",
    all(sp.simplify(e).is_nonnegative for e in offdiag)
    and all(sp.simplify(sum(L.row(i))) == 0 for i in range(4))
    and all(sp.simplify(sum(L.col(i))) == 0 for i in range(4)) and L == L.T,
    "off-diagonal entries: " + str(sorted(set(str(e) for e in offdiag))))
# (2) exp[t(F - I)] for an involution F
dev2 = max(float(np.max(np.abs(expm(tt * np.array((F - I4).tolist(), float))
                               - np.array((((1 + sp.exp(-2 * tt)) / 2) * I4 + ((1 - sp.exp(-2 * tt)) / 2) * F)
                                          .evalf().tolist(), float))))
           for F in (Fx, Fr, Fb) for tt in (0.1, 0.7, 2.3))
rec("RR (2): exp[t(F-I)] = ((1+e^-2t)/2) I + ((1-e^-2t)/2) F", dev2 < 1e-12, "max deviation %.1e" % dev2)
rec("RR (3) premise: Pi commutes with F_x, F_r, F_xF_r and Pi^2 = Pi",
    all(Pi * F == F * Pi for F in (Fx, Fr, Fb)) and Pi ** 2 == Pi)
rng = np.random.default_rng(11)
dev3 = 0.0; minpos = 1.0; dev3prod = 0.0
nFx, nFr, nFb, nPi, nI = (np.array(M.tolist(), float) for M in (Fx, Fr, Fb, Pi, I4))
for _ in range(50):
    A, B, Cc = rng.random(3) * 3 + 0.01
    ss = rng.random() * 3 + 0.01
    nL = A * (nFx + nFr - 2 * nI) + B * (nFx @ nFr - nI) + Cc * (nPi - nI)
    L0 = A * (nFx + nFr - 2 * nI) + B * (nFx @ nFr - nI)
    P, P0 = expm(ss * nL), expm(ss * L0)
    prod = expm(ss * A * (nFx - nI)) @ expm(ss * A * (nFr - nI)) @ expm(ss * B * (nFb - nI))
    dev3 = max(dev3, np.max(np.abs(P - (np.exp(-Cc * ss) * P0 + (1 - np.exp(-Cc * ss)) * nPi))))
    dev3prod = max(dev3prod, np.max(np.abs(P0 - prod)))
    minpos = min(minpos, P.min())
rec("RR (3): P_s = e^-cs P0_s + (1 - e^-cs) Pi (50 random a,b,c,s)", dev3 < 1e-12, "max deviation %.1e" % dev3)
rec("RR s2: P0_s is the product of the three stochastic factors (2)", dev3prod < 1e-12, "%.1e" % dev3prod)
rec("RR s2: every entry of P_s strictly positive for s > 0", minpos > 0, "min entry over trials %.3e" % minpos)
# U, V, J generate S4; average of the 24 pullbacks is Pi; c(Pi - I) = (c/24) sum_g (G - I)
G2 = closure([as_perm(g, S2) for g in (Um2, Vm2, Jm2)])
avg = sum((pullback(g) for g in G2), sp.zeros(4, 4)) / len(G2)
rec("RR s2: U, V, J generate all 24 permutations of S_2 (S4)", len(G2) == 24)
rec("RR s2: the average of the 24 permutation pullbacks is Pi", avg == Pi)
rec("RR s2: c(Pi - I) = (c/24) sum_g (G - I), every g (incl. U, J) at rate c/24",
    sp.simplify(c * (Pi - I4) - sum((pullback(g) - I4 for g in G2), sp.zeros(4, 4)) * c / 24) == sp.zeros(4, 4))
# (4) eigenfunctions
f1 = sp.Matrix([1, 1, 1, 1])
fX = sp.Matrix([(-1) ** x for x, r in S2]); fR = sp.Matrix([(-1) ** r for x, r in S2])
fP = sp.Matrix([(-1) ** (x + r) for x, r in S2])
lx, lp = 2 * (a + b) + c, 4 * a + c
rec("RR (4): L1 = 0, L f_x = -(2(a+b)+c) f_x, L f_r = same, L f_p = -(4a+c) f_p",
    sp.simplify(L * f1) == sp.zeros(4, 1) and sp.simplify(L * fX + lx * fX) == sp.zeros(4, 1)
    and sp.simplify(L * fR + lx * fR) == sp.zeros(4, 1) and sp.simplify(L * fP + lp * fP) == sp.zeros(4, 1))
rec("RR s3: 1, f_x, f_r, f_p are a basis; the last three have zero mean",
    sp.Matrix.hstack(f1, fX, fR, fP).rank() == 4 and sum(fX) == sum(fR) == sum(fP) == 0)
kerdims = [len((L.subs({a: A_, b: B_, c: C_})).nullspace()) for A_, B_, C_ in [(1, 1, 1), (1, 2, 1), (3, 1, 2)]]
rec("RR s3: zero eigenvalue is simple (unique stationary uniform law), uniform is stationary",
    kerdims == [1, 1, 1] and sp.simplify(sp.ones(1, 4) * L) == sp.zeros(1, 4), "kernel dims %s" % kerdims)
rec("RR s3: detailed balance with the uniform law (diag(pi) L symmetric)",
    sp.simplify(sp.eye(4) / 4 * L - (sp.eye(4) / 4 * L).T) == sp.zeros(4, 4))
# (5) stationary correlations, (6) the ratio, C_p = C_x^R
devc = 0.0; devpow = 0.0
for (A, B, Cc) in [(1, 1, 1), (1, 2, 1), (0.3, 1.7, 0.2)]:
    nL = A * (nFx + nFr - 2 * nI) + B * (nFx @ nFr - nI) + Cc * (nPi - nI)
    lxn, lpn = 2 * (A + B) + Cc, 4 * A + Cc
    for ss in (0.05, 0.4, 1.3):
        P = expm(ss * nL); mu = np.full(4, 0.25)
        Cx = mu @ (np.array(fX.tolist(), float).ravel() * (P @ np.array(fX.tolist(), float).ravel()))
        Cp = mu @ (np.array(fP.tolist(), float).ravel() * (P @ np.array(fP.tolist(), float).ravel()))
        devc = max(devc, abs(Cx - np.exp(-lxn * ss)), abs(Cp - np.exp(-lpn * ss)))
        devpow = max(devpow, abs(Cp - Cx ** (lpn / lxn)))
rec("RR (5): E[f_x f_x(s)] = e^-lambda_x s, E[f_p f_p(s)] = e^-lambda_p s", devc < 1e-12, "%.1e" % devc)
Rf = lambda A, B, Cc: sp.Rational(4 * A + Cc, 2 * (A + B) + Cc)
rec("RR (6): R(1,1,1) = 1 and R(1,2,1) = 5/7", Rf(1, 1, 1) == 1 and Rf(1, 2, 1) == sp.Rational(5, 7),
    "R(1,1,1) = %s, R(1,2,1) = %s" % (Rf(1, 1, 1), Rf(1, 2, 1)))
rec("RR s3: eliminating s gives C_p = C_x^R", devpow < 1e-12, "%.1e" % devpow)
ev1 = sorted(L.subs({a: 1, b: 1, c: 1}).eigenvals().items())
ev2 = sorted(L.subs({a: 1, b: 2, c: 1}).eigenvals().items())
L1n = np.array(L.subs({a: 1, b: 1, c: 1}).tolist(), float); L2n = np.array(L.subs({a: 1, b: 2, c: 1}).tolist(), float)
ident = False
for p in itertools.permutations(range(4)):
    Cm = np.eye(4)[list(p)]; M = Cm @ L1n @ Cm.T
    k = np.sum(M * L2n) / np.sum(M * M)
    ident |= np.allclose(k * M, L2n)
rec("RR s3: spectra {0, -5^3} vs {0, -7^2, -5}; no state permutation with a clock scaling identifies them",
    not ident and [m for _, m in ev1] == [3, 1] and sorted(m for _, m in ev2) == [1, 1, 2], "%s vs %s" % (ev1, ev2))
# section 4: symmetries of the law
transl = [as_perm(fx, S2), as_perm(fr, S2)]
rec("RR s4: L invariant under both coordinate translations and J",
    all(sp.simplify(pullback(g) * L * pullback(g).inv() - L) == sp.zeros(4, 4) for g in transl + [as_perm(Jm2, S2)]))
Up = pullback(as_perm(Um2, S2))
rec("RR s4: conjugation by U fixes F_r and Pi and exchanges F_x with F_xF_r",
    Up * Fr * Up.inv() == Fr and Up * Fx * Up.inv() == Fb and Up * Fb * Up.inv() == Fx and Up * Pi * Up.inv() == Pi)
diffU = sp.simplify(Up * L * Up.inv() - L)
rec("RR s4: U L U^-1 = L exactly when a = b", diffU.subs(b, a) == sp.zeros(4, 4) and diffU != sp.zeros(4, 4),
    "U L U^-1 - L = (a-b)(F_xF_r - F_x) check: %s" % (sp.simplify(diffU - (a - b) * (Fb - Fx)) == sp.zeros(4, 4)))
rec("RR s4: I, F_x, F_r, F_xF_r linearly independent",
    sp.Matrix.hstack(*[M.reshape(16, 1) for M in (I4, Fx, Fr, Fb)]).rank() == 4)
rec("RR (7): I + F_x + F_r + F_xF_r = 4 Pi; at a = b, L = (4a+c)(Pi - I) and R = 1",
    I4 + Fx + Fr + Fb == 4 * Pi and sp.simplify(L.subs(b, a) - (4 * a + c) * (Pi - I4)) == sp.zeros(4, 4)
    and sp.simplify(lp / lx.subs(b, a)) == 1)
okpass = True
for p in itertools.permutations(range(4)):
    Cm = sp.Matrix(np.eye(4)[list(p)].astype(int)); Ln = L.subs({a: 1, b: 2, c: 1})
    Lp = Cm * Ln * Cm.inv(); f = sp.Matrix([1, 5, -2, 3]); mu0 = sp.Matrix([[1, 2, 3, 4]]) / 10
    P1 = (s * Ln).exp().subs(s, sp.Rational(1, 3)); P1p = Cm * P1 * Cm.inv()
    okpass &= sp.simplify((mu0 * Cm.inv()) * (Cm * f) - mu0 * f) == sp.zeros(1, 1)
    okpass &= sp.simplify((mu0 * Cm.inv()) * P1p * (Cm * f) - mu0 * P1 * f) == sp.zeros(1, 1)
rec("RR s4: passive transport L' = C L C^-1, f' = C f, mu' = mu C^-1 preserves mu f and mu P f (all 24 C)", okpass)

# ================================================================== INTERNAL REGISTRATION AND FULL UNDO
def maps(m):
    return dict(V=lambda s: ((s[0] + 1) % m, s[1]), U=lambda s: (s[0], (s[1] + s[0]) % m), J=lambda s: (s[1], s[0]),
                Vi=lambda s: ((s[0] - 1) % m, s[1]), Ui=lambda s: (s[0], (s[1] - s[0]) % m))


ok_inv = ok4 = ok5 = ok6 = ok7 = okW = True; fixed_counts = {}
for m in range(2, 8):
    fixed = 0
    M = maps(m); V, U, J, Vi, Ui = M["V"], M["U"], M["J"], M["Vi"], M["Ui"]
    for st in states(m):
        ok_inv &= Vi(V(st)) == st == V(Vi(st)) and Ui(U(st)) == st == U(Ui(st)) and J(J(st)) == st
        x, r = st
        ok4 &= J(U(J(st))) == ((x + r) % m, r)
        ok5 &= U(V(st)) == ((x + 1) % m, (r + x + 1) % m) and V(U(st)) == ((x + 1) % m, (r + x) % m)
        W = Vi(U(V(st))); Wi = Vi(Ui(V(st)))
        ok6 &= W == (x, (r + x + 1) % m)
        ok7 &= Wi == (x, (r - x - 1) % m) and Vi(Ui(V(W))) == st and Vi(U(V(Wi))) == st
        fixed += W == st
    okW &= fixed < m * m; fixed_counts[m] = fixed
rec("IR (1)-(3): V^-1, U^-1, J^-1 = J are two-sided inverses on S_m (m = 2..7)", ok_inv)
rec("IR (1): R(U^-1 U s) = R(s) for every s (any R): U^-1 U = id on S_m", ok_inv)
rec("IR (4): J U J(x,r) = (x+r, r) (m = 2..7)", ok4)
rec("IR (5): U V(x,r) = (x+1, r+x+1), V U(x,r) = (x+1, r+x) (m = 2..7)", ok5)
rec("IR (6): W = V^-1 U V, W(x,r) = (x, r+x+1), W != id_S (m = 2..7)",
    ok6 and okW and all(v == k for k, v in fixed_counts.items()),
    "W fixes exactly the m states with x = -1 mod m; it is not the identity map")
plant("PLANT IR (6), stronger than the text: W moves every state", all(v == 0 for v in fixed_counts.values()),
      "fixed points per m: %s" % fixed_counts)
rec("IR (7): W^-1 = V^-1 U^-1 V = (x, r-x-1), a two-sided inverse of W (m = 2..7)", ok7)
M3 = maps(3); trace = [(0, 0)]
for g in ("V", "U", "Vi"):
    trace.append(M3[g](trace[-1]))
rec("IR s3 table: (0,0) -> V (1,0) -> U (1,1) -> V^-1 (0,1)", trace == [(0, 0), (1, 0), (1, 1), (0, 1)], str(trace))
rec("IR s1: e(h) = id does not force h = empty: h = V^-1 V is a length-2 word with identity evaluation",
    all(maps(3)["Vi"](maps(3)["V"](st)) == st for st in states(3)))
# integers, on a finite window
box = range(-6, 7); okZ = True
for x, r in itertools.product(box, box):
    u = (x, r + x); okZ &= (u[0], u[1] - u[0]) == (x, r)  # U^-1 U = id on Z
    pos = (0, 0)
    for _ in range(abs(x)):
        pos = (pos[0] + (1 if x > 0 else -1), pos[1])
    for _ in range(abs(r)):
        pos = (pos[0], pos[1] + (1 if r > 0 else -1))  # J V^{+-1} J(x,r) = (x, r +- 1)
    okZ &= pos == (x, r)
rec("IR s2 (Z): V and J V J reach every integer pair (window [-6,6]^2); U has total inverse on Z", okZ)
# d components
okd = {}
for m_, d in [(2, 2), (2, 3), (3, 2), (3, 3)]:
    S = states(m_, d); gens = []
    for i in range(d):
        gens.append(as_perm(lambda st, i=i: tuple((v + (k == i)) % m_ for k, v in enumerate(st)), S))
        for j in range(d):
            if i != j:
                gens.append(as_perm(lambda st, i=i, j=j: tuple((v + st[i] * (k == j)) % m_
                                                              for k, v in enumerate(st)), S))
    for pm in itertools.permutations(range(d)):
        gens.append(as_perm(lambda st, pm=pm: tuple(st[pm[k]] for k in range(d)), S))
    G = closure(gens)
    trans = len({g[0] for g in G}) == len(S)
    sep = len({tuple(st[pm[0]] for pm in itertools.permutations(range(d))) for st in S}) == len(S)
    okd["m=%d,d=%d" % (m_, d)] = dict(states=len(S), group=len(G), transitive=trans, separate=sep)
rec("IR s2: d components: outputs after permutations separate states; transitive; 4 and 8 states at m = 2",
    all(v["transitive"] and v["separate"] for v in okd.values())
    and okd["m=2,d=2"]["states"] == 4 and okd["m=2,d=3"]["states"] == 8, okd)
# section 4: quotient q(x,r) = x
ok8 = True; desc_J = True; indep = True; sepJ = True
for m in (2, 3, 5):
    M = maps(m)
    ok8 &= all(M["J"](st)[0] == st[1] for st in states(m))
    desc_J &= all(M["J"]((x, r1))[0] == M["J"]((x, r2))[0] for x in range(m) for r1 in range(m) for r2 in range(m))
    H = closure([as_perm(M[g], states(m)) for g in ("V", "U")])
    S = states(m)
    indep &= all(S[h[S.index((x, r1))]][0] == S[h[S.index((x, r2))]][0]
                 for h in H for x in range(m) for r1 in range(m) for r2 in range(m))
    sepJ &= len({(st[0], M["J"](st)[0]) for st in S}) == m * m
rec("IR (8): q(J(x,r)) = r (m = 2,3,5)", ok8)
rec("IR s4: with V, U and inverses only, every future x output is independent of r", indep)
rec("IR s4: o_x and o_x J separate all of S_m", sepJ)
plant("PLANT IR s4: J descends through q(x,r) = x", desc_J)
# section 5: Heisenberg
okH = {}
for m in (2, 3, 4, 5):
    M = maps(m); S = states(m)
    T = lambda A, B, Cc, m=m: (lambda st: ((st[0] + A) % m, (st[1] + B * st[0] + Cc) % m))
    Tp = {(A, B, Cc): as_perm(T(A, B, Cc), S) for A in range(m) for B in range(m) for Cc in range(m)}
    H = closure([as_perm(M["U"], S), as_perm(M["V"], S)])
    Up_, Vp_ = as_perm(M["U"], S), as_perm(M["V"], S)
    Cp = compose(compose(Up_, Vp_), compose(inverse(Up_), inverse(Vp_)))
    Cmap = as_perm(lambda st: (st[0], (st[1] + 1) % m), S)
    law = all(compose(Tp[k1], Tp[k2]) == Tp[((k1[0] + k2[0]) % m, (k1[1] + k2[1]) % m,
                                             (k1[2] + k2[2] + k1[1] * k2[0]) % m)] for k1 in Tp for k2 in Tp)
    wrong = all(compose(Tp[k1], Tp[k2]) == Tp[((k1[0] + k2[0]) % m, (k1[1] + k2[1]) % m,
                                               (k1[2] + k2[2] + k1[0] * k2[1]) % m)] for k1 in Tp for k2 in Tp)
    invs = all(inverse(Tp[(A, B, Cc)]) == Tp[((-A) % m, (-B) % m, (B * A - Cc) % m)] for (A, B, Cc) in Tp)
    def pw(p, k):
        q = tuple(range(len(p)))
        for _ in range(k):
            q = compose(p, q)
        return q
    words = all(compose(compose(pw(Vp_, A), pw(Up_, B)), pw(Cmap, Cc)) == Tp[(A, B, Cc)] for (A, B, Cc) in Tp)
    other = compose(compose(Vp_, Up_), compose(inverse(Vp_), inverse(Up_)))
    okH[m] = dict(order=len(H), equals_T_set=set(H) == set(Tp.values()), distinct=len(set(Tp.values())) == m ** 3,
                  law10=law, inverse=invs, commutator_is_C=Cp == Cmap,
                  C_central=compose(Cmap, Up_) == compose(Up_, Cmap) and compose(Cmap, Vp_) == compose(Vp_, Cmap),
                  eq12=words, plant_ab_law=wrong, VUViUi_is_C=other == Cmap)
rec("IR (9): <U,V> = {T(a,b,c)} with m^3 distinct elements (m = 2..5)",
    all(v["order"] == k ** 3 and v["equals_T_set"] and v["distinct"] for k, v in okH.items()))
rec("IR (10): T(a,b,c) T(a',b',c') = T(a+a', b+b', c+c'+b a')", all(v["law10"] for v in okH.values()))
rec("IR s5: T(a,b,c)^-1 = T(-a, -b, ba - c)", all(v["inverse"] for v in okH.values()))
rec("IR (11): [U,V] = U V U^-1 V^-1 = C, C(x,r) = (x, r+1); C commutes with U and V",
    all(v["commutator_is_C"] and v["C_central"] for v in okH.values()))
rec("IR (12): V^a U^b C^c = T(a,b,c) for every triple", all(v["eq12"] for v in okH.values()))
plant("PLANT IR (10): the transposed cocycle c+c'+a b' (m = 2..5, any m)",
      any(v["plant_ab_law"] for v in okH.values()), "holds at m: %s" % [k for k, v in okH.items() if v["plant_ab_law"]])
out["note: the other commutator convention V U V^-1 U^-1 equals C only at m = 2 (it is C^-1)"] = {
    k: v["VUViUi_is_C"] for k, v in okH.items()}
# m = 2: dihedral, not Q8
M = maps(2); S = states(2); Up_, Vp_ = as_perm(M["U"], S), as_perm(M["V"], S)
D = closure([Up_, Vp_]); e = tuple(range(4))
inv2 = sum(1 for g in D if order(g) == 2)
UV = compose(Up_, Vp_)
rec("IR s5 m=2: 8 elements, U != V nonidentity involutions, (UV)^2 = C != id, UV of order 4",
    len(D) == 8 and Up_ != Vp_ and order(Up_) == order(Vp_) == 2 and compose(UV, UV) == as_perm(
        lambda st: (st[0], (st[1] + 1) % 2), S) and order(UV) == 4)
# Q8 as left multiplication on itself
def qmul(p, r):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = r
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)
Q8 = [tuple(sg * (k == i) for k in range(4)) for i in range(4) for sg in (1, -1)]
Q8p = [tuple(Q8.index(qmul(g, h)) for h in Q8) for g in Q8]
invQ = sum(1 for g in Q8p if order(g) == 2)
rec("IR s5 m=2: dihedral of order 8 (5 involutions, a 4-cycle), not Q8 (1 involution)",
    inv2 == 5 and invQ == 1 and len(closure(Q8p)) == 8, "involutions: D %d, Q8 %d" % (inv2, invQ))
plant("PLANT IR s5: <U,V> at m = 2 is isomorphic to Q8 (same involution count)", inv2 == invQ)
# m = 2, full group with J
Jp = as_perm(M["J"], S); G24 = closure([Up_, Vp_, Jp]); i0 = S.index((0, 0))
stab = [g for g in G24 if g[i0] == i0]
rec("IR s5 m=2: U, J fix (0,0); U swaps (1,0),(1,1); J swaps (1,0),(0,1); transitive; |stab| = 6; group = S4",
    M["U"]((0, 0)) == (0, 0) == M["J"]((0, 0)) and M["U"]((1, 0)) == (1, 1) and M["U"]((1, 1)) == (1, 0)
    and M["J"]((1, 0)) == (0, 1) and len({g[i0] for g in G24}) == 4 and len(stab) == 6 and len(G24) == 24
    and len(closure([as_perm(M["U"], S), Jp])) == 6)
# section 6: contextual quotient H/~ is G
def quotient_test(H, pi):
    Hl = sorted(H); e = tuple(range(len(Hl[0])))
    R = {h: int(pi(h) != pi(e)) for h in Hl}
    sig = {h: tuple(R[compose(compose(u, h), v)] for u in Hl for v in Hl) for h in Hl}
    classes = len(set(sig.values()))
    fibres_match = all((sig[h] == sig[k]) == (pi(h) == pi(k)) for h in Hl for k in Hl)
    return classes, len({pi(h) for h in Hl}), fibres_match
res6 = {}
# S4 -> S3: action of S4 on the three pairings of S_2 = {0,1,2,3}
pairings = [frozenset([frozenset([0, 1]), frozenset([2, 3])]), frozenset([frozenset([0, 2]), frozenset([1, 3])]),
            frozenset([frozenset([0, 3]), frozenset([1, 2])])]
pi_s3 = lambda g: tuple(pairings.index(frozenset(frozenset(g[i] for i in pr) for pr in P)) for P in pairings)
res6["S4 -> S3"] = quotient_test(G24, pi_s3)
S3_ = states(3); H3 = closure([as_perm(maps(3)["U"], S3_), as_perm(maps(3)["V"], S3_)])
pi_ab = lambda g: (S3_[g[S3_.index((0, 0))]][0], (S3_[g[S3_.index((1, 0))]][1] - S3_[g[S3_.index((0, 0))]][1]) % 3)
res6["Heis(3) -> Z3 x Z3"] = quotient_test(H3, pi_ab)
res6["D4 -> Z2 (x-shift parity)"] = quotient_test(D, lambda g: S[g[S.index((0, 0))]][0])
rec("IR (13): H/~ has exactly |G| classes, and h ~ k iff pi(h) = pi(k); a binary test separates 6 and 9 classes",
    all(cl == ng and fm for cl, ng, fm in res6.values()),
    {k: dict(classes=v[0], image=v[1], fibres=v[2]) for k, v in res6.items()})
# section 7: P_t on N states
okP = True; tt, nn = sp.symbols("t n", positive=True)
for N in range(2, 6):
    IN, PiN = sp.eye(N), sp.ones(N, N) / N; Pt = PiN + tt * (IN - PiN)
    okP &= sp.simplify(Pt - (tt * IN + (1 - tt) * PiN)) == sp.zeros(N, N)
    okP &= all(sp.simplify(sum(Pt.row(i)) - 1) == 0 and sp.simplify(sum(Pt.col(i)) - 1) == 0 for i in range(N))
    okP &= all(sp.simplify(e_.subs(tt, tv)) > 0 for e_ in Pt for tv in (sp.Rational(1, 100), sp.Rational(99, 100)))
    for p in itertools.permutations(range(N)):
        Cm = sp.Matrix(np.eye(N, dtype=int)[list(p)]); okP &= sp.simplify(Cm * Pt - Pt * Cm) == sp.zeros(N, N)
    okP &= PiN ** 2 == PiN and PiN * (IN - PiN) == sp.zeros(N, N)
    for k in range(1, 6):
        okP &= sp.simplify(Pt ** k - (PiN + tt ** k * (IN - PiN))) == sp.zeros(N, N)
    for tv in (sp.Rational(1, 3), sp.Rational(4, 5)):
        okP &= len((Pt.subs(tt, tv).T - IN).nullspace()) == 1
        f = sp.Matrix([sp.Integer(i * i) for i in range(N)]); f = f - sp.ones(N, 1) * sum(f) / N
        for k in range(1, 5):
            corr = sum(f[i] * (Pt.subs(tt, tv) ** k * f)[i] for i in range(N)) / N
            okP &= sp.simplify(corr - tv ** k * sum(fi ** 2 for fi in f) / N) == 0
rec("IR (14)-(16): P_t > 0, doubly stochastic, S_N-commuting, unique stationary; P_t^n, E[f f_n] (N = 2..5)",
    okP)
cnt = {(i, j): sum(1 for g in G24 if g[i] == j) for i in range(4) for j in range(4)}
rec("IR s7: over S4, exactly 6 of 24 permutations take any input to any output", set(cnt.values()) == {6})
wts = {g: (1 - tt) / 24 + (tt if g == e else 0) for g in G24}
rec("IR s7: P_t = sum_g w_g G with w_g = (1-t)/24 + t [g = id] > 0",
    sp.simplify(sum((w * pullback(g) for g, w in wts.items()), sp.zeros(4, 4)) - (tt * I4 + (1 - tt) * Pi))
    == sp.zeros(4, 4))
# countercontrols on the rate example
Ln = lambda A, B, Cc: L.subs({a: A, b: B, c: Cc})
plant("PLANT RR s4: U L U^-1 = L at (a,b,c) = (1,2,1)",
      sp.simplify(Up * Ln(1, 2, 1) * Up.inv() - Ln(1, 2, 1)) == sp.zeros(4, 4))
plant("PLANT RR (6): R(1,2,1) = 1", Rf(1, 2, 1) == 1)
plant("PLANT IR (6): W = V^-1 U V is the identity on S_3", all(maps(3)["Vi"](maps(3)["U"](maps(3)["V"](st))) == st
                                                                for st in states(3)))
plant("PLANT RR (4): f_p has the same eigenvalue as f_x for (a,b,c) = (1,2,1)",
      sp.simplify(Ln(1, 2, 1) * fP + 7 * fP) == sp.zeros(4, 1))

summary = dict(claims=len(out) - 1, claims_holding=sum(1 for v in out.values() if v.get("holds") is True),
               plants=len(plants), plants_failing_as_expected=sum(1 for v in plants.values() if v["fails_as_expected"]))
res = dict(summary=summary, claims=out, countercontrols=plants)
print(json.dumps(res, indent=1, default=str))
pathlib.Path(__file__).with_name("check_relative_rates_and_undo.json").write_text(
    json.dumps(res, indent=1, default=str))
