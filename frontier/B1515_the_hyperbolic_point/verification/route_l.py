"""B1515 -- THE HYPERBOLIC POINT: route L, the interior index from one joint linear system.  Library; nothing sealed is computed on
import.

The independent route the owner's rule requires (WORKING_RULES, NO NEGATIVE FROM A BUG).  It shares no code with route T
(route_t.py), B1511's tower_lib.py or B1374's index_lib.py.  From B1513's independent_audit.py it takes only the two arithmetic
backends (exact: sympy's AlgebraicField; GF(p): that file's own numpy elimination), m004's words and its build of Ballas' matrices.
The presentations, cochain maps, character enumeration, symmetric cube and interior dimension below are new.

The method.  Let E be a module of a group G with peripheral subgroup P = <mu, lam>.  A class [z] in H^1(G; E) is interior iff
z|_P = delta_P v for some v in E.  So the interior classes are the image in H^1(G; E) of
    K = {(z, v) in C^1(G; E) x E :  d^1 z = 0,  z(mu) = (E(mu) - 1) v,  z(lam) = (E(lam) - 1) v}.
The kernel of K -> H^1 is {(delta w, w + u) : w in E, u in E^P}, of dimension d + t0 - a0 (t0 = dim E^P, a0 = dim E^G).  Hence
    n(E) = dim K - (d + t0 - a0),
read from the nullity of one stacked matrix.  Route T instead takes the rank of the restriction map modulo the peripheral
coboundaries.  The index is I(E) = n(E) - n(E*).  Poincare-Lefschetz duality gives a self-check, asserted at every reading:
n(E*) = h^1(E) - a0 + b0 - s0, with b0 = dim (E*)^G and s0 = dim (E*)^P.

The cochains.  A 1-cochain is the column (z(g_1); ...; z(g_k)).  For a word w, z(w) is a linear function of z.  It is read off by
composing affine pairs (A, X)(B, Y) = (AB, AY + X), letter by letter; d^1 stacks these maps over the relators.  The interior index
uses only H^0 and H^1, which any presentation of the group computes."""
import importlib.util
from fractions import Fraction
from math import gcd
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location(
    "b1513_independent_audit", ROOT / "frontier/B1513_the_triplets_higgs_sector/verification/independent_audit.py")
IA = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(IA)

Exact, ModP = IA.Exact, IA.ModP
K12 = sp.QQ.algebraic_field(sp.sqrt(-3), sp.I)           # Q(zeta_12): the exact levels 1 and 3, and m010's Q(sqrt -3)


# ============================================================================================ scalars
def lcm(a, b):
    return a * b // gcd(a, b)


def gf_root_of_unity(p, K):
    """a primitive K-th root of unity in GF(p) (route L's own search)"""
    assert (p - 1) % K == 0
    for g in range(2, p):
        z = pow(g, (p - 1) // K, p)
        if all(pow(z, K // r, p) != 1 for r in sp.primefactors(K)):
            return z
    raise ValueError("no primitive root")


class Units:
    """exp(2 pi i f) for rational f, in one backend: over GF(p) as powers of one primitive K-th root (so every value is one embedding
    of Q(zeta_K)); exactly in Q(zeta_12) when the denominator divides 12"""

    def __init__(self, F, K=12):
        self.F, self.K = F, K
        if isinstance(F, ModP):
            self.z = gf_root_of_unity(F.p, K)

    def __call__(self, f):
        f = Fraction(f) % 1
        F = self.F
        if isinstance(F, ModP):
            assert (f * self.K).denominator == 1, ("denominator does not divide K", f, self.K)
            return pow(self.z, int(f * self.K), F.p)
        assert 12 % f.denominator == 0, ("exact values only for denominators dividing 12", f)
        ang = 2 * sp.pi * sp.Rational(f.numerator, f.denominator)
        return F.s(sp.nsimplify(sp.cos(ang)) + sp.I * sp.nsimplify(sp.sin(ang)))


def spow(F, x, k):
    if k < 0:
        x, k = F.sinv(x), -k
    out = F.c(1)
    for _ in range(k):
        out = out * x
    return out % F.p if isinstance(F, ModP) else out


# ============================================================================================ representations of a presentation
class GRep:
    """matrices (and inverses) on named generators (lower case; upper case is the inverse), with relators and two peripheral words"""

    def __init__(self, F, gens, rels, peri, mats):
        self.F, self.gens, self.rels, self.peri = F, tuple(gens), tuple(rels), tuple(peri)
        self.d = mats[self.gens[0]].shape[0]
        self.g = {k: (mats[k], F.inv(mats[k])) for k in self.gens}

    def w(self, word):
        return IA.word(self.F, self.g, word, self.d)

    def holds(self):
        F, I = self.F, self.F.eye(self.d)
        a, b = self.w(self.peri[0]), self.w(self.peri[1])
        return all(F.is_zero(F.sub(self.w(r), I)) for r in self.rels) and F.is_zero(F.sub(F.mul(a, b), F.mul(b, a)))

    def remake(self, mats):
        return GRep(self.F, self.gens, self.rels, self.peri, mats)

    def dual(self):
        return self.remake({k: self.F.T(self.g[k][1]) for k in self.gens})

    def wedge2(self):
        return self.remake({k: IA.compound2(self.F, self.g[k][0]) for k in self.gens})

    def scaled(self, vals):
        """E (x) chi, chi given by its scalar values on the generators"""
        return self.remake({k: self.F.smul(vals[k], self.g[k][0]) for k in self.gens})


def line(F, gens, rels, peri, vals):
    return GRep(F, gens, rels, peri, {k: F.mat([[vals[k]]]) for k in gens})


def direct_sum(A, B):
    F = A.F
    mats = {}
    for k in A.gens:
        top = F.hstack([A.g[k][0], F.zeros(A.d, B.d)])
        bot = F.hstack([F.zeros(B.d, A.d), B.g[k][0]])
        mats[k] = F.vstack([top, bot])
    return A.remake(mats)


def ext_line(V, c, L):
    """W = [[V, c L], [0, L]] for a cocycle c of V (x) L^-1 (L of rank one): the extension of L by V with class c"""
    F, d = V.F, V.d
    mats = {}
    for i, k in enumerate(V.gens):
        ck = F.sub_block(c, i * d, (i + 1) * d, 0, 1)
        Lk = L.g[k][0]
        mats[k] = F.vstack([F.hstack([V.g[k][0], F.mul(ck, Lk)]), F.hstack([F.zeros(1, d), Lk])])
    return V.remake(mats)


# ============================================================================================ cochains
def word_map(rep, word):
    """(E(word), X) with z(word) = X z for every 1-cochain z"""
    F, d, k = rep.F, rep.d, len(rep.gens)
    sel = {}
    for i, g in enumerate(rep.gens):
        blocks = [F.zeros(d, d) for _ in rep.gens]
        blocks[i] = F.eye(d)
        sel[g] = F.hstack(blocks)
    A, X = F.eye(d), F.zeros(d, k * d)
    for ch in word:
        g = ch.lower()
        if ch.islower():
            B, Y = rep.g[g][0], sel[g]
        else:
            B = rep.g[g][1]
            Y = F.smul(-1, F.mul(B, sel[g]))
        A, X = F.mul(A, B), F.add(F.mul(A, Y), X)
    return A, X


def d0(rep):
    F, I = rep.F, rep.F.eye(rep.d)
    return F.vstack([F.sub(rep.g[k][0], I) for k in rep.gens])


def d1(rep):
    F = rep.F
    rows = []
    for r in rep.rels:
        A, X = word_map(rep, r)
        assert F.is_zero(F.sub(A, F.eye(rep.d))), "a relator fails in the module"
        rows.append(X)
    return F.vstack(rows)


def dims(rep):
    """a0 = dim E^G, h1 = dim H^1(G; E), t0 = dim E^P, n = the interior dimension (the joint system K)"""
    F, d, k = rep.F, rep.d, len(rep.gens)
    D0, D1 = d0(rep), d1(rep)
    assert F.is_zero(F.mul(D1, D0)), "d1 d0 != 0"
    r0 = F.rank(D0)
    a0, h1 = d - r0, k * d - F.rank(D1) - r0
    I = F.eye(d)
    Am, Xm = word_map(rep, rep.peri[0])
    Al, Xl = word_map(rep, rep.peri[1])
    t0 = d - F.rank(F.vstack([F.sub(Am, I), F.sub(Al, I)]))
    J = F.vstack([F.hstack([D1, F.zeros(D1.shape[0], d)]),
                  F.hstack([Xm, F.smul(-1, F.sub(Am, I))]),
                  F.hstack([Xl, F.smul(-1, F.sub(Al, I))])])
    n = (k * d + d - F.rank(J)) - (d + t0 - a0)
    assert 0 <= n <= h1, ("interior dimension out of range", n, h1)
    return {"a0": a0, "h1": h1, "t0": t0, "n": n}


def index(rep):
    """I(E) = n(E) - n(E*), with the duality self-check n(E*) = h^1(E) - a0 + b0 - s0"""
    E, Ed = dims(rep), dims(rep.dual())
    assert Ed["n"] == E["h1"] - E["a0"] + Ed["a0"] - Ed["t0"], ("duality self-check", E, Ed)
    return {"I": E["n"] - Ed["n"], "E": E, "E*": Ed}


def prop_e_range(ix):
    """B1509's Proposition E: over every end condition W in H^1(T; E), N_W = dim W - t0 + a0 - b0, dim W in [0, t0 + s0]"""
    a0, b0, t0, s0 = ix["E"]["a0"], ix["E*"]["a0"], ix["E"]["t0"], ix["E*"]["t0"]
    return [a0 - b0 - t0, a0 - b0 + s0]


def h1_basis(rep):
    """cocycles completing B^1 to Z^1 (route L's own greedy completion)"""
    F = rep.F
    D0, D1 = d0(rep), d1(rep)
    cur, rk, out = D0, F.rank(D0), []
    for z in F.nullspace(D1):
        nxt = F.hstack([cur, z])
        rn = F.rank(nxt)
        if rn > rk:
            out.append(z)
            cur, rk = nxt, rn
    return out


# ============================================================================================ m004's levels at q = 1
def level_presentation(n):
    """G_n = <x, y, t | t g t^-1 = phi^n(g)>; the cusp P = <t, ell>, ell = y x^-1 y^-1 x"""
    return ("x", "y", "t"), tuple(IA.relators(n)), ("t", IA.ELL)


def rho_at(F, n, q):
    """Ballas' rho_q on G_n at the backend scalar q: x = n m^-1, y = m n m^-2, t = m^n (B1513's own build of the matrices)"""
    mn = IA.mn_mats(F, q)
    words = {"x": IA.FIBRE_MN["x"], "y": IA.FIBRE_MN["y"], "t": "m" * n}
    gens, rels, peri = level_presentation(n)
    return GRep(F, gens, rels, peri, {k: IA.word(F, mn, words[k], 4) for k in gens})


def rho1(F, n):
    """the hyperbolic point q = 1"""
    return rho_at(F, n, F.c(1))


def exponent_sums(w):
    return (sum((ch == "x") - (ch == "X") for ch in w), sum((ch == "y") - (ch == "Y") for ch in w))


def fibre_characters(n):
    """every character of T_n = coker(Phi^n - 1) as (a, b) in (Q/Z)^2: nu(x) = exp(2 pi i a), nu(y) = exp(2 pi i b).
    Phi^n is read from the exponent sums of phi^n(x), phi^n(y); the characters are the (a, b) mod D = |T_n| with
    nu o phi^n = nu."""
    img = IA.phi_n(n)
    cx, cy = exponent_sums(img["x"]), exponent_sums(img["y"])
    M = [[cx[0] - 1, cy[0]], [cx[1], cy[1] - 1]]
    D = abs(M[0][0] * M[1][1] - M[0][1] * M[1][0])
    out = []
    for a in range(D):
        for b in range(D):
            if (a * M[0][0] + b * M[1][0]) % D == 0 and (a * M[0][1] + b * M[1][1]) % D == 0:
                out.append((Fraction(a, D), Fraction(b, D)))
    assert len(out) == D
    return out, D


def deck_image(ab):
    """nu -> nu o phi, from the exponent sums of phi(x), phi(y)"""
    a, b = ab
    ex, ey = exponent_sums(IA.PHI["x"]), exponent_sums(IA.PHI["y"])
    return ((a * ex[0] + b * ex[1]) % 1, (a * ey[0] + b * ey[1]) % 1)


def character_values(U, ab, lam, power=1):
    """nu^power on x, y, t as backend scalars"""
    return {"x": U(power * ab[0]), "y": U(power * ab[1]), "t": U(power * lam)}


# ============================================================================================ one member, read completely
def trials(F, basis):
    """the classes read: each basis class; for h^1 >= 2 also c1 + c2 and the fixed combination sum_k (k + 1) c_k"""
    out = [(f"c{k + 1}", c) for k, c in enumerate(basis)]
    if len(basis) >= 2:
        out.append(("c1+c2", F.add(basis[0], basis[1])))
        comb = basis[0]
        for k, c in enumerate(basis[1:], start=2):
            comb = F.add(comb, F.smul(k, c))
        out.append(("generic", comb))
    return out


def summary(ix):
    return {"I": ix["I"], "E(a0,h1,t0,n)": [ix["E"][k] for k in ("a0", "h1", "t0", "n")],
            "E*(b0,h1,s0,n)": [ix["E*"][k] for k in ("a0", "h1", "t0", "n")], "prop E range": prop_e_range(ix)}


def read_member(F, U, n, rho, ab, lam, full=True):
    """the member nu = (ab, lam) at q = 1 on G_n.  If full is False only h^1(V_eta) is read (the member test off lam = 1)."""
    gens, rels, peri = rho.gens, rho.rels, rho.peri
    V = rho.scaled(character_values(U, ab, lam, 1))
    Veta = rho.scaled(character_values(U, ab, lam, 5))
    cE = h1_basis(Veta)
    row = {"h1(V_eta)": len(cE)}
    if not full or not cE:
        return row
    L = line(F, gens, rels, peri, character_values(U, ab, lam, -4))
    Linv = line(F, gens, rels, peri, character_values(U, ab, lam, 4))
    VL = rho.scaled(character_values(U, ab, lam, -3))
    L2V = V.wedge2()
    assert all(m.holds() for m in (V, Veta, L, VL))
    row["pieces"] = {name: summary(index(m)) for name, m in (("V", V), ("L", L), ("V_eta", Veta), ("V(x)L", VL), ("L2V", L2V))}
    row["h1"] = {name: row["pieces"][name]["E(a0,h1,t0,n)"][1] for name in row["pieces"]}
    row["case"] = "a" if F.is_zero(F.sub(L.g["x"][0], F.eye(1))) and F.is_zero(F.sub(L.g["y"][0], F.eye(1))) \
        and F.is_zero(F.sub(L.g["t"][0], F.eye(1))) else "b"
    row["W1"] = {}
    for name, c in trials(F, cE):
        W1 = ext_line(V, c, L)
        assert W1.holds()
        row["W1"][name] = {"W1": summary(index(W1)), "L2W1": summary(index(W1.wedge2()))}
    Vd = V.dual()
    cEd = h1_basis(Veta.dual())
    row["h1(V_eta*)"] = len(cEd)
    row["W2"] = {}
    for name, c in trials(F, cEd):
        W2s = ext_line(Vd, c, Linv)
        assert W2s.holds()
        i1, i2 = index(W2s), index(W2s.wedge2())
        row["W2"][name] = {"I(W2)": -i1["I"], "I(L2W2)": -i2["I"]}
    return row


# ============================================================================================ the positive control: R40 on m010
M010 = {"gens": ("a", "b"), "rels": ("aabaBaaBab",), "peri": ("AbAA", "babA")}


def sym3(F, M):
    """Sym^3 of a 2 x 2 matrix on e1^3, e1^2 e2, e1 e2^2, e2^3 (M e1 = M11 e1 + M21 e2): column j holds the coefficients of
    (M e1)^(3 - j) (M e2)^j, expanded by hand"""
    (m11, m12), (m21, m22) = F.tolist(M)
    f, g = [m11, m21], [m12, m22]

    def mul(p, q):
        out = [F.c(0)] * (len(p) + len(q) - 1)
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                out[i + j] = out[i + j] + x * y
        return out
    cols = []
    for j in range(4):
        poly = [F.c(1)]
        for _ in range(3 - j):
            poly = mul(poly, f)
        for _ in range(j):
            poly = mul(poly, g)
        cols.append(poly)
    rows = [[cols[j][i] for j in range(4)] for i in range(4)]
    return F.mat([[v % F.p if isinstance(F, ModP) else v for v in r] for r in rows])


def m010_modules(F, u):
    """R27/R40 (the audit lane's FINITE_TWIST and COEFFICIENT_PARENT): u^2 - u + 1 = 0, rho(a) = [[0, 1], [-1, 1]],
    rho(b) = [[0, u^2], [u, -2]], chi(a) = u, chi(b) = -1; V = Sym^3(rho) (x) chi, L = chi^2, W = V + L"""
    g, r, pe = M010["gens"], M010["rels"], M010["peri"]
    A = F.mat([[0, 1], [-1, 1]])
    B = F.mat([[F.c(0), u * u], [u, F.c(-2)]])
    if isinstance(F, ModP):
        B = B % F.p
    chi = {"a": u, "b": F.c(-1)}
    V = GRep(F, g, r, pe, {"a": F.smul(chi["a"], sym3(F, A)), "b": F.smul(chi["b"], sym3(F, B))})
    L = line(F, g, r, pe, {"a": spow(F, u, 2), "b": F.c(1)})
    W = direct_sum(V, L)
    assert V.holds() and L.holds() and W.holds()
    return {"V": V, "L2V": V.wedge2(), "W": W, "L2W": W.wedge2()}
