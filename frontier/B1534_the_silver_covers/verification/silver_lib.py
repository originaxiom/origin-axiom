#!/usr/bin/env python3
"""B1534 -- route E for the silver covers: sm:B1515's frame on m135 = -LLRR and m136 = +LLRR at the hyperbolic point, the
twisted terms T(nu, chi, c) = (I(W1(c) (x) chi), I(Lambda^2 W1(c) (x) chi)) and the pencils that locate the special classes.
Exact over Q(zeta_24) with sm:B1530's exact_lib (banked; it asserts B1297's identity, the annihilator identity and Lemma E at
every index).  Nothing sealed is computed on import.

- The states: sm:B1527's family_lib presentation <a, b, t> with its cusp <abAB, t'>, t' = t (+) or abt (-), through sm:B1530's
  exact_states; the exact holonomy in PGL(2, Q(i)) read by sm:B1529's reader (sign - for m135; sign + for m136, as sm:B1530's
  post_run_e136.m136_sl2); the four is H -> g H g* / |det g|.
- A member is nu = (u, kappa), u a fibre character fixed by phi and kappa = nu(t'), with h^1(V_eta) >= 1, V_eta = nu^5 (x) rho.
  V = nu (x) rho, L = nu^-4, W1(c) = [[V, c L], [0, L]].
- The contributing characters of a member (Lemma Z'): chi = (w, k) with w a fibre character fixed by phi and chi(t') = k in
  {kappa^-1, kappa^4, kappa^-2, kappa^3}, the values at which a composition factor of W1 (x) chi or Lambda^2 W1 (x) chi is
  unipotent on P.  Every other chi leaves the cusp acyclic for both, and its term is (0, 0).
- The pencil (Lemma J, sm:B1532): for a member with h^1(V_eta) = 2 and an interior line <c_int>, the classes are c_int and
  c_s = c_b + s c_int.  Each of the four modules M in {E, E*, Lambda^2 E, (Lambda^2 E)*}, E = W1(c) (x) chi, is an extension
  0 -> S -> M -> Q -> 0 whose off-diagonal block is linear in c, and its h^1 changes with s only through
  delta^1_c : H^1(Q) -> H^2(S), [y] -> [the S-part of the Fox coboundary of the lift (0, y)].  delta^1_{c_s} = P_b + s P_int.
  The special classes are the s where the pencil's rank drops: rational in K, or a conjugate pair over K, read through the
  restriction of scalars R(E) (I(R(E)) = 2 I(E))."""
import itertools
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1530V = ROOT / "frontier" / "B1530_the_interior_extensions" / "verification"
if str(B1530V) not in sys.path:
    sys.path.insert(0, str(B1530V))
import exact_lib as E  # noqa: E402
import exact_states as S  # noqa: E402

STATES = {"-LLRR": ("-", "LLRR", "m135"), "+LLRR": ("+", "LLRR", "m136")}
KAPPA_TURNS = (Fraction(0), Fraction(1, 2), Fraction(1, 4), Fraction(3, 4), Fraction(1, 3), Fraction(2, 3))


# ============================================================================================ the states
def holonomy(state):
    sign, word, _ = STATES[state]
    if state == "-LLRR":
        return S.m135_sl2()
    P = S.load(B1530V, "post_run_e136", "b1530_post_run_e136")
    return P.m136_sl2()[0]


def setup(state):
    sign, word, name = STATES[state]
    G, img, chars, D = S.group(sign, word)
    rho = S.four_module(holonomy(state))
    assert rho.check(G.rels), "the four does not satisfy the relators"
    return {"state": state, "sign": sign, "word": word, "name": name, "G": G, "img": img, "chars": chars, "D": D,
            "rho": rho}


def char(st, w, k):
    """the character with fibre part w and value e^{2 pi i k} at t'"""
    return S.nu(st["sign"], (Fraction(w[0]), Fraction(w[1])), Fraction(k))


def mul(ch1, ch2):
    return {g: ch1[g] * ch2[g] for g in ch1}


def is_trivial(ch):
    return all(v == E.ONE for v in ch.values())


def member_modules(st, u, k):
    ch = char(st, u, k)
    V = st["rho"].twist(ch)
    Lc = S.power_char(ch, -4)
    L = None if is_trivial(Lc) else E.line(st["G"].gens, Lc)
    Veta = st["rho"].twist(S.power_char(ch, 5))
    return ch, V, L, Veta


def members(st, kappa_turns=KAPPA_TURNS):
    """every (u, kappa) with h^1(V_eta) >= 1: its h^1, interior dimension and classes"""
    out = []
    for u in st["chars"]:
        for k in kappa_turns:
            ch, V, L, Veta = member_modules(st, u, k)
            C = E.Cohomology(st["G"], Veta)
            if C.h1 == 0:
                continue
            m = {"u": (Fraction(u[0]), Fraction(u[1])), "kappa": Fraction(k), "case": "(a)" if L is None else "(b)",
                 "h1": C.h1, "n": C.n, "V": V, "L": L, "C": C}
            ints = C.interior()
            if C.h1 == 1:
                m["classes"] = {"the class": C.reps[0]}
                m["the class is interior"] = C.n == 1
            else:
                assert C.h1 == 2 and C.n == 1, ("a member outside the two shapes this arc reads", C.h1, C.n)
                c_int = C.combine(ints[0])
                c_b = next(z for z in C.reps if E.rank_vectors(C.Bvecs + [c_int, z], C.d * C.ng) == C.dimB + 2)
                m["c_int"], m["c_b"] = c_int, c_b
            out.append(m)
    return out


def contributing(st, m):
    """Lemma Z': the characters whose twist can leave a factor of W1 or Lambda^2 W1 unipotent on P"""
    k = m["kappa"]
    ks = sorted({(-k) % 1, (4 * k) % 1, (-2 * k) % 1, (3 * k) % 1})
    return [((Fraction(w[0]), Fraction(w[1])), kk) for w in st["chars"] for kk in ks]


def non_contributing_sample(st, m, n=3):
    """characters outside the contributing set (Lemma Z' control): kappa' = i, omega and their products"""
    out = []
    k = m["kappa"]
    bad = {(-k) % 1, (4 * k) % 1, (-2 * k) % 1, (3 * k) % 1}
    for kk in (Fraction(1, 4), Fraction(1, 3), Fraction(3, 4), Fraction(2, 3), Fraction(1, 6)):
        if kk in bad:
            continue
        for w in st["chars"][:2]:
            out.append(((Fraction(w[0]), Fraction(w[1])), kk))
    return out[:n]


# ============================================================================================ the terms
def lin(c1, c2, a, b):
    """a c1 + b c2, a and b in K"""
    return [a * x + b * y for x, y in zip(c1, c2)]


def term(st, m, c, chi):
    G = st["G"]
    W1 = E.extension(m["V"], c, m["L"])
    assert W1.check(G.rels)
    a = E.class_index(G, W1.twist(chi))
    b = E.class_index(G, W1.wedge2().twist(chi))
    return (a["I"], b["I"]), {"W": a, "L2W": b}


# ---------------------------------------------------------------------------- the restriction of scalars (conjugate pairs)
def _restrict(X, Y, d):
    """the K-matrix of X + sqrt(d) Y on K(sqrt d)^n: [[X, d Y], [Y, X]]"""
    n = len(X)
    R = E.zeros(2 * n, 2 * n)
    for i in range(n):
        for j in range(n):
            R[i][j] = X[i][j]
            R[i][n + j] = d * Y[i][j]
            R[n + i][j] = Y[i][j]
            R[n + i][n + j] = X[i][j]
    return R


def term_quadratic(st, m, alpha, beta, d, chi):
    """the term at c_s, s = alpha + beta sqrt(d) (sqrt d not in K), through R: I(R(M)) = 2 I(M)"""
    G = st["G"]
    gens = G.gens
    Xc = E.extension(m["V"], lin(m["c_b"], m["c_int"], E.ONE, alpha), m["L"])
    Yc = E.extension(m["V"], lin(m["c_b"], m["c_int"], E.ZERO, beta), m["L"])
    zero = E.extension(m["V"], [E.ZERO] * len(m["c_b"]), m["L"])
    RW, RL = {}, {}
    for g in gens:
        X = Xc.M[g]
        Y = E.madd(Yc.M[g], zero.M[g], -1)               # only the off-diagonal column: beta c_int L
        RW[g] = E.scal(_restrict(X, Y, d), chi[g])
        A2 = E.wedge2(X)
        B2 = E.madd(E.wedge2(E.madd(X, Y)), A2, -1)      # Lambda^2 (X + t Y) = Lambda^2 X + t B2 (Lambda^2 Y = 0)
        RL[g] = E.scal(_restrict(A2, B2, d), chi[g])
    MW, ML = E.Module(gens, RW), E.Module(gens, RL)
    assert MW.check(G.rels) and ML.check(G.rels)
    a, b = E.class_index(G, MW), E.class_index(G, ML)
    assert a["I"] % 2 == 0 and b["I"] % 2 == 0, ("an odd index on a restriction of scalars", a["I"], b["I"])
    return (a["I"] // 2, b["I"] // 2), {"W (R)": a, "L2W (R)": b}


# ============================================================================================ the pencils
def _permuted(mod, order):
    return E.Module(mod.gens, {g: [[mod.M[g][i][j] for j in order] for i in order] for g in mod.gens})


def four_modules(m, c, chi):
    """the four extensions of Lemma J at the class c, each permuted so that its submodule S comes first: (name, module, dS)"""
    W1 = E.extension(m["V"], c, m["L"])
    Ew = W1.twist(chi)
    L2 = W1.wedge2().twist(chi)
    n = E.wedge_index(5)
    sub2 = [a for a, (i, j) in enumerate(n) if j < 4]
    quo2 = [a for a, (i, j) in enumerate(n) if j == 4]
    return [("E", Ew, 4),
            ("E*", _permuted(Ew.dual(), [4, 0, 1, 2, 3]), 1),
            ("L2E", _permuted(L2, sub2 + quo2), 6),
            ("(L2E)*", _permuted(L2.dual(), quo2 + sub2), 4)]


def _blocks(mod, dS):
    d = mod.d
    for g in mod.gens:
        for i in range(dS, d):
            for j in range(dS):
                assert mod.M[g][i][j].is_zero(), "not block upper-triangular"
    A = E.Module(mod.gens, {g: [row[:dS] for row in mod.M[g][:dS]] for g in mod.gens})
    B = E.Module(mod.gens, {g: [row[dS:] for row in mod.M[g][dS:]] for g in mod.gens})
    return A, B


def _fox_all(G, mod):
    return [E.fox_blocks(mod, r)[0] for r in G.rels]


def _phi(G, mod, dS, y, fox=None):
    """the S-part of the Fox coboundary of the lift (0, y) of a Q-cocycle y, over every relator"""
    d, dQ = mod.d, mod.d - dS
    out = []
    for Kb in (fox if fox is not None else _fox_all(G, mod)):
        acc = [E.ZERO] * dS
        for gi, g in enumerate(G.gens):
            yg = y[gi * dQ:(gi + 1) * dQ]
            for i in range(dS):
                s = E.ZERO
                for j in range(dQ):
                    if not yg[j].is_zero():
                        s = s + Kb[g][i][dS + j] * yg[j]
                acc[i] = acc[i] + s
        out += acc
    return out


def _annihilator(G, Smod):
    """rows f with f . d^1_S = 0: coordinates on H^2(S) = C^2(S) / im d^1_S"""
    dS = Smod.d
    fox = _fox_all(G, Smod)
    cols = []
    for g in G.gens:
        for k in range(dS):
            col = []
            for Kb in fox:
                col += [Kb[g][i][k] for i in range(dS)]
            cols.append(col)
    nrow = dS * len(G.rels)
    F = E.nullspace(cols, nrow) if cols else []      # f with <col, f> = 0 for every column
    return F


def pencil(st, m, chi, which):
    """(P_b, P_int, h^1(Q), h^2(S)) for one of the four modules: delta^1_{c_b + s c_int} = P_b + s P_int"""
    G = st["G"]
    mods_b = {n: (M, dS) for n, M, dS in four_modules(m, m["c_b"], chi)}
    mods_i = {n: (M, dS) for n, M, dS in four_modules(m, m["c_int"], chi)}
    Mb, dS = mods_b[which]
    Mi, _ = mods_i[which]
    Smod, Qmod = _blocks(Mb, dS)
    CQ = E.Cohomology(G, Qmod)
    CS = E.Cohomology(G, Smod)
    F = _annihilator(G, Smod)
    h2S = len(F)
    assert h2S == CS.h1 - CS.a0, ("Euler characteristic", h2S, CS.h1, CS.a0)
    Pb = [[E.ZERO] * CQ.h1 for _ in range(h2S)]
    Pi = [[E.ZERO] * CQ.h1 for _ in range(h2S)]
    fb, fi = _fox_all(G, Mb), _fox_all(G, Mi)
    for j, y in enumerate(CQ.reps):
        vb, vi = _phi(G, Mb, dS, y, fb), _phi(G, Mi, dS, y, fi)
        for a, f in enumerate(F):
            Pb[a][j] = sum((x * z for x, z in zip(f, vb)), E.ZERO)
            Pi[a][j] = sum((x * z for x, z in zip(f, vi)), E.ZERO)
    # linearity in c (Lemma J): the pencil at c_b + c_int is P_b + P_int
    Ms, _ = {n: (M, dS) for n, M, dS in four_modules(m, lin(m["c_b"], m["c_int"], E.ONE, E.ONE), chi)}[which]
    fs = _fox_all(G, Ms)
    for j, y in enumerate(CQ.reps):
        vs = _phi(G, Ms, dS, y, fs)
        for a, f in enumerate(F):
            assert sum((x * z for x, z in zip(f, vs)), E.ZERO) == Pb[a][j] + Pi[a][j], "the pencil is not linear in c"
    return Pb, Pi, CQ.h1, h2S


# ---------------------------------------------------------------------------- polynomials over K (lists, lowest degree first)
def _ptrim(p):
    p = list(p)
    while p and p[-1].is_zero():
        p.pop()
    return p


def _pmul(p, q):
    if not p or not q:
        return []
    out = [E.ZERO] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = out[i + j] + x * y
    return _ptrim(out)


def _psub(p, q):
    n = max(len(p), len(q))
    return _ptrim([(p[i] if i < len(p) else E.ZERO) - (q[i] if i < len(q) else E.ZERO) for i in range(n)])


def _pmod(p, q):
    p, q = _ptrim(p), _ptrim(q)
    while len(p) >= len(q) and p:
        c = p[-1] / q[-1]
        sh = len(p) - len(q)
        p = _psub(p, [E.ZERO] * sh + [c * x for x in q])
    return p


def _pgcd(p, q):
    p, q = _ptrim(p), _ptrim(q)
    while q:
        p, q = q, _pmod(p, q)
    if p:
        p = [x / p[-1] for x in p]
    return p


def _det_poly(M):
    """the determinant of a square matrix of polynomials"""
    n = len(M)
    if n == 1:
        return M[0][0]
    out = []
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        t = _pmul(M[0][j], _det_poly(minor))
        out = _psub(out, t) if j % 2 else _psub(out, _psub([], t))
    return _ptrim(out)


def _rank_at(Pb, Pi, s):
    rows = [[b + s * i for b, i in zip(rb, ri)] for rb, ri in zip(Pb, Pi)]
    if not rows or not rows[0]:
        return 0
    return E.rank(rows, len(rows[0]))


GENERIC_S = (Fraction(7, 3), Fraction(-5, 11), Fraction(13, 2), Fraction(-17, 7))


def special_points(Pb, Pi):
    """the s in K where rank(P_b + s P_int) drops below its generic rank, and the irreducible quadratics over K whose roots do
    (as (c0, c1, c2), lowest first); with the generic rank"""
    if not Pb or not Pb[0]:
        return {"generic rank": 0, "rational": [], "quadratic": [], "gcd degree": 0}
    rg = max(_rank_at(Pb, Pi, E.K.of(s)) for s in GENERIC_S)
    if rg == 0:
        return {"generic rank": 0, "rational": [], "quadratic": [], "gcd degree": 0}
    nr, nc = len(Pb), len(Pb[0])
    g = None
    for rows in itertools.combinations(range(nr), rg):
        for cols in itertools.combinations(range(nc), rg):
            Mp = [[_ptrim([Pb[i][j], Pi[i][j]]) for j in cols] for i in rows]
            d = _det_poly(Mp)
            if d:
                g = d if g is None else _pgcd(g, d)
    assert g is not None
    g = _ptrim(g)
    deg = len(g) - 1
    out = {"generic rank": rg, "rational": [], "quadratic": [], "gcd degree": deg}
    if deg <= 0:
        return out
    if deg == 1:
        out["rational"].append(-g[0] / g[1])
    elif deg == 2:
        roots = _quadratic_roots_in_K(g)
        if roots is None:
            out["quadratic"].append(tuple(g))
        else:
            out["rational"] += roots
    else:
        raise AssertionError(("a special-point polynomial of degree > 2", deg))
    for s in out["rational"]:
        assert _rank_at(Pb, Pi, s) < rg
    return out


# ---------------------------------------------------------------------------- is a quadratic over K split?  (sympy, exactly)
def _to_sympy(x):
    import sympy as sp
    z = (sp.sqrt(6) + sp.sqrt(2)) / 4 + sp.I * (sp.sqrt(6) - sp.sqrt(2)) / 4         # e^{i pi / 12}
    return sp.nsimplify(sum((sp.Rational(int(c), int(x.d)) * z ** k for k, c in enumerate(x.c)), sp.Integer(0)))


def _from_sympy(e):
    """an element of Q(i, sqrt 2, sqrt 3) as an element of K"""
    import sympy as sp
    e = sp.expand(e)
    if e.is_Rational:
        return E.K.of(Fraction(int(e.p), int(e.q)))
    if e == sp.I:
        return E.I_UNIT
    if e.is_Add:
        out = E.ZERO
        for a in e.args:
            out = out + _from_sympy(a)
        return out
    if e.is_Mul:
        out = E.ONE
        for a in e.args:
            out = out * _from_sympy(a)
        return out
    if e.is_Pow and e.exp == sp.Rational(1, 2) and e.base.is_Rational:
        return E.sqrt_rational(Fraction(int(e.base.p), int(e.base.q)))
    if e.is_Pow and e.exp.is_Integer:
        b = _from_sympy(e.base)
        n = int(e.exp)
        out = E.ONE
        for _ in range(abs(n)):
            out = out * b
        return out if n >= 0 else E.ONE / out
    raise ValueError(("not read into K", e))


def _quadratic_roots_in_K(g):
    """the two roots in K of g = c0 + c1 s + c2 s^2, or None if g is irreducible over K = Q(i, sqrt 2, sqrt 3)"""
    import sympy as sp
    s = sp.Symbol("s")
    c0, c1, c2 = (_to_sympy(x) for x in g)
    poly = sp.expand(c2 * s ** 2 + c1 * s + c0)
    fac = sp.factor_list(poly, s, extension=[sp.I, sp.sqrt(2), sp.sqrt(3)])
    lins = [f for f, k in fac[1] for _ in range(k) if sp.degree(f, s) == 1]
    if not lins:
        return None
    roots = []
    for f in lins:
        a, b = sp.Poly(f, s).all_coeffs()
        r = _from_sympy(sp.nsimplify(-b / a))
        assert (g[0] + g[1] * r + g[2] * r * r).is_zero(), "a root read into K does not vanish"
        roots.append(r)
    return roots


# ============================================================================================ the subgroups and the counts
def _add(x, y):
    return (((x[0][0] + y[0][0]) % 1, (x[0][1] + y[0][1]) % 1), (x[1] + y[1]) % 1)


def closure(gens_):
    zero = ((Fraction(0), Fraction(0)), Fraction(0))
    H = {zero}
    frontier = [zero]
    while frontier:
        new = []
        for h in frontier:
            for g in gens_:
                x = _add(h, g)
                if x not in H:
                    H.add(x)
                    new.append(x)
        frontier = new
    return frozenset(H)


def subgroups(C):
    """every subgroup of the finite abelian group C (closed under addition), by closures of at most three elements"""
    C = [((Fraction(w[0]) % 1, Fraction(w[1]) % 1), Fraction(k) % 1) for w, k in C]
    Cs = set(C)
    out = set()
    for r in range(0, 4):
        for gs in itertools.combinations(C, r):
            H = closure(gs)
            assert H <= Cs, "the contributing characters are not closed under the group law"
            out.add(H)
    return sorted(out, key=lambda H: (len(H), sorted(H)))


def key(chi_wk):
    w, k = chi_wk
    return f"({w[0]}, {w[1]}; {k})"
