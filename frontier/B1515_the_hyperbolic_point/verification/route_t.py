"""B1515 -- THE HYPERBOLIC POINT: route T, B1511's instrument at q = 1.  Library; nothing sealed is computed on import.

Route T is B1511's projective tower read at the hyperbolic point q = 1 (t = 1/2 in Ballas' family):
- tower_lib.py: the Reidemeister-Schreier presentation of each level M_n, its characters, the twisted modules and Fox calculus;
- the index (a0, a1, t0, t1, r1) / (b0, b1, s0, q1), with r1 the rank of the restriction H^1(M; E) -> H^1(T; E):
  - exactly by tower_lib.index over Q(zeta_12)[q]/(q - 1) at levels 1 and 3 (it asserts the annihilator identity r1 + q1 = t1 = s1
    and the B1297 identity);
  - over GF(p) by B1374's index_lib (tower_lib.index_gf) at every level.
Every root of unity is a power of one primitive K-th root, K = lcm(N, 12), so every reading is one embedding of Q(zeta_K).

The mechanism (PREREGISTRATION Lemma 8) is read here too, at every member with h^1(V) = h^1(V_eta) = h^1(V (x) L) = 1 and lam = 1:
  rho  = [v|_P is not a multiple of c|_P in H^1(T; rho_1)]  (v spans H^1(V));
  bit  = [e ^ c|_P lies in the image of H^1(Lambda^2 V) in H^1(T; Lambda^2 V)]  (e spans V^P);
and Lemma 8 says I(W1) = 1 - b0 - rho and I(Lambda^2 W1) = bit there.  Remark 9's two checks are read with it: e ^ c|_P lies in
the parabolic part pi_A (the classes of cocycles valued in (Lambda^2 V)^P), and the image Lambda_A of H^1(Lambda^2 V) meets pi_A
only in 0.  Together they force bit = 0."""
import importlib.util
from math import gcd
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location("b1511_tower_lib", ROOT / "frontier/B1511_the_projective_tower/verification/tower_lib.py")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)
IL = T.IL
Q = T.Q
LAMBDAS = [(0, "1"), (6, "-1"), (3, "i"), (9, "-i"), (4, "w"), (8, "w^2")]   # lam = zeta_12^k: mu_4 and mu_3, the only lam with a
                                                                             # possible non-zero index (Lemma 5)


def lcm(a, b):
    return a * b // gcd(a, b)


# ============================================================================================ fields and units
class Arith:
    """the field of one reading: exact Q(zeta_12)[q]/(q - 1), or GF(p) with q = 1; units zeta_K^k from one primitive root"""

    def __init__(self, kind, K, p=None, r=1, g=None):
        """q = 1 unless a control asks for another point: r (a root mod p) or g (its polynomial, exactly)"""
        self.kind, self.K, self.p = kind, K, p
        if kind == "exact":
            assert 12 % K == 0
            self.field = T.Field("ext", g=(Q - 1) if g is None else g, base="Q12")
            self.q1 = g is None
        else:
            assert (p - 1) % K == 0
            self.field = T.Field("gf", p=p, r=r)
            self.q1 = r % p == 1
            self.z = IL.GF(p).root_of_unity(K)
        self.dom = self.field.dom

    def unit(self, k):
        k %= self.K
        if self.kind == "exact":
            return self.field.unit(k * (12 // self.K), 12)
        return self.dom(pow(self.z, k, self.p))

    def ix(self, rep, rels, mu, lam):
        if self.kind == "exact":
            return T.index(rep, rels, mu, lam)
        d = T.index_gf(rep, rels, mu, lam, self.p)
        d["t1"] = d["t0"] + d["s0"]
        return d


# ============================================================================================ modules on a level
class Level:
    def __init__(self, n):
        self.n = n
        self.cov = T.rs_cover(n)
        self.chars, self.N = T.characters(n)
        self.K = lcm(self.N, 12)
        self.rels, self.mu, self.lam = self.cov["rels"], self.cov["mu"], self.cov["lam"]

    def exponents(self, ab, lk):
        """nu on the RS generators as exponents of zeta_K: nu_F = (a, b) mod N, lam = zeta_12^lk"""
        ex = T.rs_character_exponents(self.cov, ab, self.N, lk, 12)
        return {g: (e1 * (self.K // self.N) + e2 * (self.K // 12)) for g, (e1, e2) in ex.items()}

    def twisted(self, A, rho, ex, power):
        return T.DMRep(self.cov["gens"], {g: rho[g] * A.unit(power * ex[g]) for g in self.cov["gens"]})

    def line(self, A, ex, power):
        return T.DMRep(self.cov["gens"], {g: DomainMatrix([[A.unit(power * ex[g])]], (1, 1), A.dom) for g in self.cov["gens"]})


def ext_with_line(V, coc, L, gens):
    """W = [[V, c L], [0, L]] with c a cocycle of V (x) L^-1 (B1511's construction)"""
    d, dom = V.d, V.dom
    out = {}
    for i, g in enumerate(gens):
        lv = L.M[g][0, 0].element
        cg = coc[i * d:(i + 1) * d, :] * lv
        out[g] = V.M[g].hstack(cg).vstack(DomainMatrix.zeros((1, d), dom).hstack(L.M[g]))
    return T.DMRep(gens, out)


def class_trials(cls):
    out = [(f"c{k + 1}", c) for k, c in enumerate(cls)]
    if len(cls) >= 2:
        out.append(("c1+c2", cls[0] + cls[1]))
        comb = cls[0]
        for k, c in enumerate(cls[1:], start=2):
            comb = comb + c * c.domain.convert(k)
        out.append(("generic", comb))
    return out


def brief(d):
    return {"I": d["I"], "E(a0,a1,t0,r1)": [d["a0"], d["a1"], d["t0"], d["r1"]],
            "E*(b0,b1,s0,q1)": [d["b0"], d["b1"], d["s0"], d["q1"]],
            "prop E range": [d["a0"] - d["b0"] - d["t0"], d["a0"] - d["b0"] + d["s0"]]}


# ============================================================================================ the mechanism (Lemma 8)
def restrict(rep, coc, word):
    """z(word) by Fox calculus"""
    D = rep.fox(word)
    R = D[rep.gens[0]].hstack(*[D[g] for g in rep.gens[1:]])
    return R * coc


def peripheral_coboundaries(rep, lev):
    I = DomainMatrix.eye(rep.d, rep.dom)
    return (rep.word(lev.mu) - I).vstack(rep.word(lev.lam) - I)


def wedge_vec(e, u):
    d = e.shape[0]
    rows = []
    for i in range(d):
        for j in range(i + 1, d):
            rows.append([e[i, 0].element * u[j, 0].element - e[j, 0].element * u[i, 0].element])
    return DomainMatrix(rows, (len(rows), 1), e.domain)


def mechanism(lev, V, Veta, c, L2V):
    """(rho, bit) of Lemma 8 at a lam = 1 member"""
    gens, rels = lev.cov["gens"], lev.rels
    vcls, hv = T.h1_classes(V, rels)
    assert hv == 1
    BP = peripheral_coboundaries(V, lev)
    BPeta = peripheral_coboundaries(Veta, lev)
    assert T.dm_equal(BP, BPeta), "V and V_eta differ on P (lam must be 1)"
    vP = restrict(V, vcls[0], lev.mu).vstack(restrict(V, vcls[0], lev.lam))
    cP = restrict(Veta, c, lev.mu).vstack(restrict(Veta, c, lev.lam))
    rho = T.dm_rank(BP.hstack(cP, vP)) - T.dm_rank(BP.hstack(cP))
    # e spans V^P; e ^ c|_P in Lambda^2 V coordinates (pairs i < j, as tower_lib.wedge2)
    I = DomainMatrix.eye(V.d, V.dom)
    eP = T.dm_nullspace((V.word(lev.mu) - I).vstack(V.word(lev.lam) - I))
    assert len(eP) == 1
    e = eP[0]
    cm, cl = restrict(Veta, c, lev.mu), restrict(Veta, c, lev.lam)
    delta = wedge_vec(e, cm).vstack(wedge_vec(e, cl))
    acls, ha = T.h1_classes(L2V, rels)
    BA = peripheral_coboundaries(L2V, lev)
    cols = [restrict(L2V, a, lev.mu).vstack(restrict(L2V, a, lev.lam)) for a in acls]
    base = BA.hstack(*cols) if cols else BA
    bit = int(T.dm_rank(base.hstack(delta)) == T.dm_rank(base))
    # the parabolic part pi_A: classes of cocycles with values in the P-invariants of Lambda^2 V (Remark 9)
    IA_ = DomainMatrix.eye(L2V.d, L2V.dom)
    inv = T.dm_nullspace((L2V.word(lev.mu) - IA_).vstack(L2V.word(lev.lam) - IA_))
    Z = DomainMatrix.zeros((L2V.d, 1), L2V.dom)
    pcols = [w.vstack(Z) for w in inv] + [Z.vstack(w) for w in inv]
    rB, rBL, rBP = T.dm_rank(BA), T.dm_rank(base), T.dm_rank(BA.hstack(*pcols))
    return {"rho": rho, "bit": bit, "h1(L2V)": ha, "dim (L2V)^P": len(inv), "dim pi_A": rBP - rB, "dim Lambda_A": rBL - rB,
            "e ^ c|P in pi_A": T.dm_rank(BA.hstack(*pcols, delta)) == rBP,
            "Lambda_A meets pi_A in 0": T.dm_rank(base.hstack(*pcols)) == rBL + rBP - rB}


# ============================================================================================ one member, read completely
def read_member(lev, A, rho, ab, lk, full=True):
    gens, rels, mu, lam = lev.cov["gens"], lev.rels, lev.mu, lev.lam
    ex = lev.exponents(ab, lk)
    V = lev.twisted(A, rho, ex, 1)
    Veta = lev.twisted(A, rho, ex, 5)
    assert V.check(rels) and Veta.check(rels)
    clsE, h1E = T.h1_classes(Veta, rels)
    row = {"h1(V_eta)": h1E}
    if not full or h1E == 0:
        return row
    L = lev.line(A, ex, -4)
    Linv = lev.line(A, ex, 4)
    Lrep = L
    VL = lev.twisted(A, rho, ex, -3)
    L2V = T.wedge2_rep(V)
    pieces = {"V": V, "L": Lrep, "V_eta": Veta, "V(x)L": VL, "L2V": L2V}
    row["pieces"] = {k: brief(A.ix(m, rels, mu, lam)) for k, m in pieces.items()}
    row["h1"] = {k: v["E(a0,a1,t0,r1)"][1] for k, v in row["pieces"].items()}
    one = DomainMatrix([[A.dom.one]], (1, 1), A.dom)
    row["case"] = "a" if all(T.dm_equal(L.M[g], one) for g in gens) else "b"
    simple = A.q1 and lk == 0 and all(T.h1_classes(m, rels)[1] == 1 for m in (V, Veta, VL))
    row["simple"] = simple
    row["W1"] = {}
    for name, c in class_trials(clsE):
        W1 = ext_with_line(V, c, L, gens)
        assert W1.check(rels)
        r = {"W1": brief(A.ix(W1, rels, mu, lam)), "L2W1": brief(A.ix(T.wedge2_rep(W1), rels, mu, lam))}
        if simple:
            m = mechanism(lev, V, Veta, c, L2V)
            b0 = r["W1"]["E*(b0,b1,s0,q1)"][0]
            r["mechanism"] = dict(m, **{"Lemma 8 I(W1) = 1 - b0 - rho": r["W1"]["I"] == 1 - b0 - m["rho"],
                                        "Lemma 8 I(L2W1) = bit": r["L2W1"]["I"] == m["bit"]})
        row["W1"][name] = r
    Vd = V.dual()
    clsEd, h1Ed = T.h1_classes(Veta.dual(), rels)
    row["h1(V_eta*)"] = h1Ed
    row["W2"] = {}
    for name, c in class_trials(clsEd):
        W2s = ext_with_line(Vd, c, Linv, gens)
        assert W2s.check(rels)
        row["W2"][name] = {"I(W2)": -A.ix(W2s, rels, mu, lam)["I"], "I(L2W2)": -A.ix(T.wedge2_rep(W2s), rels, mu, lam)["I"]}
    return row


# ============================================================================================ the positive control: R40 on m010
M010 = {"gens": ["a", "b"], "rels": ["aabaBaaBab"], "mu": "AbAA", "lam": "babA"}


def sym3_matrix(M):
    """Sym^3 of a 2 x 2 sympy matrix, by substitution into the cubic monomials (route T's own construction)"""
    X, Y = sp.symbols("X Y")
    mons = [X ** 3, X ** 2 * Y, X * Y ** 2, Y ** 3]
    # M acts on column vectors; on polynomials in the coordinates of e1, e2 it sends e1 -> M[0,0] e1 + M[1,0] e2, e2 -> M[0,1] e1 + M[1,1] e2
    sub = {X: M[0, 0] * X + M[1, 0] * Y, Y: M[0, 1] * X + M[1, 1] * Y}
    cols = []
    for mono in mons:
        img = sp.Poly(sp.expand(mono.subs(sub, simultaneous=True)), X, Y)
        cols.append([img.coeff_monomial(m) for m in mons])
    return sp.Matrix(4, 4, lambda i, j: cols[j][i])


def m010_reps(A, u):
    """R27/R40: V = Sym^3(rho) (x) chi, L = chi^2, W = V + L, over route T's field (u a sympy number or a GF(p) residue)"""
    uu = sp.Symbol("u")
    Am = sp.Matrix([[0, 1], [-1, 1]])
    Bm = sp.Matrix([[0, uu ** 2], [uu, -2]])
    S3 = {"a": sym3_matrix(Am) * uu, "b": sym3_matrix(Bm) * (-1)}
    Lv = {"a": uu ** 2, "b": sp.Integer(1)}

    def ev(e):
        e = sp.expand(sp.sympify(e))
        if A.kind == "exact":
            return A.field.conv(e.subs(uu, u))
        P = sp.Poly(e, uu)
        tot = 0
        for (k,), cf in P.terms():
            cf = sp.Rational(cf)
            tot += int(cf.p) * pow(int(cf.q), -1, A.p) * pow(int(u), k, A.p)
        return A.dom(tot % A.p)
    V = T.DMRep(M010["gens"], {g: DomainMatrix([[ev(S3[g][i, j]) for j in range(4)] for i in range(4)], (4, 4), A.dom)
                               for g in M010["gens"]})
    L = T.DMRep(M010["gens"], {g: DomainMatrix([[ev(Lv[g])]], (1, 1), A.dom) for g in M010["gens"]})
    W = T.DMRep(M010["gens"], {g: V.M[g].hstack(DomainMatrix.zeros((4, 1), A.dom)).vstack(
        DomainMatrix.zeros((1, 4), A.dom).hstack(L.M[g])) for g in M010["gens"]})
    for R in (V, L, W):
        assert R.check(M010["rels"])
    return {"V": V, "L2V": T.wedge2_rep(V), "W": W, "L2W": T.wedge2_rep(W)}


def m010_indices(A, u):
    reps = m010_reps(A, u)
    return {k: brief(A.ix(R, M010["rels"], M010["mu"], M010["lam"])) for k, R in reps.items()}
