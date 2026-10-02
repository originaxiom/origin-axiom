"""B1514 -- THE DECOUPLING LAW: route L, the lifting criterion.  Library; no sealed quantity is computed on import.

The independent route the owner's rule requires (WORKING_RULES, NO NEGATIVE FROM A BUG).  It shares no code with route T
(law_lib.py), B1513's higgs_lib.py or B1511's tower_lib.py.  It is built only on B1513's independent_audit.py: own words, own
build of Ballas' matrices, own modular elimination, sympy's AlgebraicField for exact work.  It reads the banked populations as data
(the JSON records of B1511 and B1512), never their code.

The method (B1513 FINDINGS Section 9).  For 1-cocycles a, b and an equivariant bilinear map mu: A (x) B -> C, the class
[mu(a u b)] in H^2(G; C) vanishes iff the block map [[C, N_a, beta], [0, B, b], [0, 0, 1]], N_a(g) v = mu(a(g) (x) g v), is a
homomorphism for some beta; on the relators that is "the corners at beta = 0 lie in the image of d^1".  By duality (the Higgs
modules are acyclic on the cusp) a coupling <h u a u b> vanishes for every Higgs class h iff [a ^ b] = 0 in H^2 of the dual module."""
import importlib.util
import json
from math import gcd
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location(
    "b1513_independent_audit", ROOT / "frontier/B1513_the_triplets_higgs_sector/verification/independent_audit.py")
IA = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(IA)

GENS = IA.GENS
Qs = IA.Qs
B1512_RUN = ROOT / "frontier/B1512_the_self_coincident_orbits/verification/census_run.txt"
B1511_RUN = ROOT / "frontier/B1511_the_projective_tower/verification/tower_census_run.txt"


# ============================================================================================ scalars
def spow(F, x, k):
    if k < 0:
        x, k = F.sinv(x), -k
    out = F.c(1)
    for _ in range(k):
        out = out * x
    return out % F.p if isinstance(F, IA.ModP) else out


def reduce_char(ab, N):
    g = gcd(gcd(ab[0] % N, ab[1] % N), N)
    return (ab[0] % N // g, ab[1] % N // g), N // g


def scal_rep(F, n, vals):
    return IA.Rep(F, n, {k: F.mat([[v]]) for k, v in zip(GENS, vals)})


# ============================================================================================ the member
class Member:
    """a case-(b) member nu = (a, b mod N, lam) on G_n: V = nu rho, L = nu^-4, V_eta = nu^5 rho, V (x) L = nu^-3 rho, c, x, W1"""

    def __init__(self, F, mn, n, ab, N, lam, zeta, c_coeffs=None):
        (a, b), Nr = reduce_char(ab, N)
        self.F, self.n, self.char = F, n, ((a, b), Nr)
        nu = (spow(F, zeta, a), spow(F, zeta, b), lam)
        self.nu = nu
        self.V = IA.level_rep(F, mn, n, nu)
        self.L = scal_rep(F, n, tuple(spow(F, v, -4) for v in nu))
        self.Veta = IA.level_rep(F, mn, n, tuple(spow(F, v, 5) for v in nu))
        self.VL = IA.level_rep(F, mn, n, tuple(spow(F, v, -3) for v in nu))
        _, D0E, D1E = IA.cohomology(self.Veta)
        _, D0L, D1L = IA.cohomology(self.L)
        self.c_basis = IA.h1_basis(self.Veta, D0E, D1E)
        self.x_basis = IA.h1_basis(self.L, D0L, D1L)
        if c_coeffs is None:
            self.c = self.c_basis[0]
        else:
            self.c = F.add(F.smul(c_coeffs[0], self.c_basis[0]), F.smul(c_coeffs[1], self.c_basis[1]))
        self.x = self.x_basis[0]
        cv = IA.values(F, self.c, 4)
        mats = {}
        for k in GENS:
            Lg = self.L.g[k][0]
            top = F.hstack([self.V.g[k][0], F.mul(cv[k], Lg)])
            bot = F.hstack([F.zeros(1, 4), Lg])
            mats[k] = F.vstack([top, bot])
        self.W1 = IA.Rep(F, n, mats)
        self.W1d = self.W1.dual()
        self.L2W = self.W1.wedge2()
        self.L2Wd = self.W1d.wedge2()
        self.L2V = self.V.wedge2()


def h_data(rep):
    return IA.cohomology(rep)[0]


def cusp_acyclic(rep):
    F = rep.F
    return F.rank(F.sub(rep.w(IA.ELL), F.eye(rep.d))) == rep.d


# ============================================================================================ classes and their products
def basis(rep):
    _, D0, D1 = IA.cohomology(rep)
    return IA.h1_basis(rep, D0, D1)


def class_test(C, B, Nfun, avals, bvals):
    """the class of mu(a u b) in H^2(C): (block checks, values against a basis of H^2's dual)"""
    F = C.F
    _, _, D1 = IA.cohomology(C)
    ys = IA.coker_functionals(F, D1)
    Q, ok = IA.cup_corner(C, B, Nfun, avals, bvals)
    return ok, IA.class_values(F, ys, Q), len(ys)


def wedge_table(target, slot):
    """[a_i ^ a_j] in H^2(target) for a basis of H^1(slot), target = Lambda^2 of slot's module"""
    F = target.F
    As = basis(slot)
    Nw = IA.N_wedge(F)
    tab, ok_all, h2 = [], True, None
    for ai in As:
        row = []
        for aj in As:
            ok, vals, h2 = class_test(target, slot, Nw, IA.values(F, ai, slot.d), IA.values(F, aj, slot.d))
            ok_all = ok_all and ok
            row.append(vals)
        tab.append(row)
    zero = all(F.zero_scalar(v) for row in tab for cell in row for v in cell)
    sym = all(all(F.zero_scalar(u - w) for u, w in zip(tab[i][j], tab[j][i])) for i in range(len(As)) for j in range(len(As)))
    return {"dim H^1(slot)": len(As), "dim H^2(target)": h2 if As else None, "zero": zero, "symmetric": sym, "blocks ok": ok_all,
            "table": [[[F.show(v) for v in cell] for cell in row] for row in tab]}


def x_cup_c(mem):
    """the positive control: [x u c] in H^2(V), mu(s (x) w) = s w on L (x) V_eta -> V"""
    F = mem.F

    def Nfun(a, Bg):
        return F.smul(F.tolist(a)[0][0], Bg)
    ok, vals, h2 = class_test(mem.V, mem.Veta, Nfun, IA.values(F, mem.x, 1), IA.values(F, mem.c, 4))
    return {"blocks ok": ok, "non-zero": any(not F.zero_scalar(v) for v in vals), "dim H^2(V)": h2}


def cocycle_on_word(rep, avals, word):
    """a(word) from the corner of [[rho, a], [0, 1]] along the word"""
    F, d = rep.F, rep.d
    R = {}
    for k in GENS:
        M = F.vstack([F.hstack([rep.g[k][0], avals[k]]), F.hstack([F.zeros(1, d), F.eye(1)])])
        R[k] = (M, F.inv(M))
    P = IA.word(F, R, word, d + 1)
    return F.sub_block(P, 0, d, d, d + 1)


def interior_dimension(rep):
    """dim ker(H^1(G; rep) -> H^1(P; rep)), P = <t, ell>: a class is interior iff its (a(t), a(ell)) is a peripheral coboundary"""
    F, d = rep.F, rep.d
    As = basis(rep)
    if not As:
        return 0
    I = F.eye(d)
    Bt = F.sub(rep.g["t"][0], I)
    Bl = F.sub(rep.w(IA.ELL), I)
    BP = F.vstack([Bt, Bl])
    cols = []
    for a in As:
        av = IA.values(F, a, d)
        cols.append(F.vstack([av["t"], cocycle_on_word(rep, av, IA.ELL)]))
    r_all = F.rank(F.hstack([BP] + cols))
    r_b = F.rank(BP)
    return len(As) - (r_all - r_b)


# ============================================================================================ joining forms (GF(p), numpy)
def form_space(Wk, Wi, Wj):
    """invariant forms on Lambda^2 Wk* (x) Wi (x) Wj = invariant vectors of Lambda^2 Wk (x) Wi* (x) Wj*; (dimension, basis)"""
    F = Wk.F
    p = F.p
    L2 = Wk.wedge2()
    rows = []
    for k in GENS:
        A = L2.g[k][0]
        Bi = Wi.g[k][1].T.copy()
        Bj = Wj.g[k][1].T.copy()
        K = np.kron(np.kron(A, Bi) % p, Bj) % p
        rows.append((K - np.eye(K.shape[0], dtype=np.int64)) % p)
    S = np.vstack(rows)
    N = F.nullspace(S)
    return len(N), [v[:, 0].tolist() for v in N]


def form_map_N(F, vec, Wj):
    """N(g) for mu(u (x) v)_P = sum_{i,j} vec[(P, i, j)] u_i v_j : Wi (x) Wj -> Lambda^2 Wk"""
    T3 = np.array(vec, dtype=np.int64).reshape(10, 5, 5) % F.p

    def Nfun(a, Bg):
        u = a[:, 0] % F.p
        out = np.zeros((10, 5), dtype=np.int64)
        for c in range(5):
            v = Bg[:, c] % F.p
            tmp = (T3 @ v) % F.p                      # contract j first: entries < 5 p^2 < 2^49
            out[:, c] = (tmp @ u) % F.p               # then i
        return out % F.p
    return Nfun


def cross_coupling(Wk, Wi, Wj, vec):
    """[mu(a u b)] in H^2(Lambda^2 Wk) for a, b running over bases of H^1(Wi), H^1(Wj)"""
    F = Wk.F
    L2 = Wk.wedge2()
    Ai, Aj = basis(Wi), basis(Wj)
    Nfun = form_map_N(F, vec, Wj)
    zero, ok_all = True, True
    for ai in Ai:
        for aj in Aj:
            ok, vals, _ = class_test(L2, Wj, Nfun, IA.values(F, ai, 5), IA.values(F, aj, 5))
            ok_all = ok_all and ok
            zero = zero and all(F.zero_scalar(v) for v in vals)
    return {"zero": zero, "blocks ok": ok_all, "pairs": len(Ai) * len(Aj)}


# ============================================================================================ the populations (banked data)
def populations():
    out = []
    r11 = json.loads(B1511_RUN.read_text(encoding="utf-8"))
    for orb in r11["C1"]["4"]:
        if orb["lam"] == "1" and any(f["factor"] == "q**2 - 7*q + 1" for f in orb["factors"]):
            out.append({"level": 4, "label": f"M4 orbit {orb['orbit'][0]}", "orbits": {str(orb["orbit"][0]): [tuple(m) for m in orb["orbit"]]},
                        "N": 15, "lam": "1", "factor": "q**2 - 7*q + 1"})
    r12 = json.loads(B1512_RUN.read_text(encoding="utf-8"))
    classes = {}
    for lev in ("level_5", "level_6"):
        for cl in r12["A"]["classes"][lev]["classes"]:
            classes[(int(lev[-1]), tuple(cl["orbits"]))] = ({str(m["orbit_index"]): [tuple(x) for x in m["orbit"]] for m in cl["members"]},
                                                             r12["A"]["classes"][lev]["N"])
    for d in r12["D"]:
        key = (int(d["level"]), tuple(d["class_orbits"]))
        orbits, N = classes[key]
        out.append({"level": int(d["level"]), "label": f"M{d['level']} {list(key[1])} lam = {d['lam']}", "orbits": orbits, "N": N,
                    "lam": d["lam"], "factor": d["factor"], "banked_h1": d["h1 (L, V_nu, V_eta, V_eta*) values"]})
    return out


def root_of_unity(p, N):
    for g in range(2, p):
        z = pow(g, (p - 1) // N, p)
        if all(pow(z, N // r, p) != 1 for r in sp.primefactors(N)):
            return z
    raise ValueError("no primitive root of unity")


def primes_for(factor_expr, orders, count, start):
    """`count` primes below `start`, = 1 mod every order in `orders`, at which the factor has a root; with all its roots"""
    poly = sp.sympify(factor_expr, locals={"q": Qs})
    out, p = [], start
    while len(out) < count:
        p = int(sp.prevprime(p))
        if any(p % m != 1 for m in orders):
            continue
        r = IA.gf_roots(poly, p)
        if r:
            out.append((p, r))
    return out
