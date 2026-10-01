"""B1513 -- THE TRIPLET'S HIGGS SECTOR: main's B1443 question (does each member of a deck orbit couple to its own Higgs class?) asked of
B1511's projective triplet in the harmonic frame.  Library; no sealed quantity is computed on import.

The frame (B1509): E8 > SU(5)' x SU(5)_perp with B1509's rank-five flat bundle W in SU(5)_perp.
  - the 10' zero modes are the interior part of H^1(W*) (B1511: N(10') = -I(W));
  - the 5'_H classes are H^1(Lambda^2 W); the up-type Yukawa 10'.10'.5'_H uses the invariant form W* (x) W* (x) Lambda^2 W -> C;
  - the 5bar'_H classes are H^1(Lambda^2 W*).
The triplet (B1511 Part A): s961 = M_3, the fibre characters nu_k = (2,0), (0,2), (2,2) mod 4 with lam3 = nu(z) = -1, at q^6 - 34 q^3 + 1 = 0.
V_k = nu_k (x) rho_q has h^1 = 1 (class c_k), W_k = [[V_k, c_k], [0, 1]] and I(W_k) = -1.  Everything is defined over Q(q).

The fibred presentation of pi_n:  G_n = <x, y, t | t g t^-1 = phi^n(g), g = x, y>,  t = m^n,  x = nM,  y = mnMM,  phi(x) = y,  phi(y) = yXyy.
The fibre's boundary is ELL = yXYx: the longitude nMNmmNMn written in x, y (checked as matrices).  phi fixes it as a reduced word, so
<t, ELL> = Z^2 is the peripheral subgroup on every level.

The relative triple product (derived here; main's B1435 relcup built the same pairing on <x, y, t> with the boundary word [x, y]):
  - a relative 1-cocycle is (h, e): h in Z^1(G; H), e in H with h(p) = p e - e on P (the relative lift);
  - (h, e) u a u b = (h u a u b, e u a u b), and <(Omega, E), (C, z)> = Omega(C) - E(z);
  - so Y(h, a, b; T) = sum_C T(h(g1), g1 a(g2), g1 g2 b(g3)) - sum_z T(e, a(p), p b(q));
  - z = [t | ELL] - [ELL | t] is the cusp torus.  C = prism(sigma) + K(Phi_* sigma - sigma) with d sigma = -[ELL]:
    sigma = sum_j [w_1..w_j | w_(j+1)] - sum over inverse letters h^-1 of [h | h^-1], for any word w in the commutator subgroup;
    the prism h satisfies dh + hd = 1 - c_t, and K fills 2-cycles of the free fibre group from Fox terms.  So dC = z (asserted as an
    identity of integer chains).
Conventions: cocycles f(gk) = f(g) + g f(k); d[g|k] = [k] - [gk] + [g]; d[g|k|l] = [k|l] - [gk|l] + [g|kl] - [g|k] (trivial coefficients,
normalised: cells containing the identity are dropped).  Elements of G_n are pairs (f, k) = f t^k, f a reduced word in x, y."""
import importlib.util
import sys
from fractions import Fraction
from collections import defaultdict
from pathlib import Path

import flint
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1511 = ROOT / "frontier/B1511_the_projective_tower/verification"
sys.path.insert(0, str(B1511))
import tower_lib as T  # noqa: E402

q, s = T.Q, T.S_
G0 = q ** 6 - 34 * q ** 3 + 1                      # B1511's triplet locus at lam3 = -1 (w^3 - 3w = 34, w = q + 1/q)
TRIPLET = [(0, 2), (2, 2), (2, 0)]                  # the deck orbit, in order: (a, b) -> (b, 3b - a) mod 4
PHI_INV = {"x": "xxYx", "y": "x"}
ELL = "yXYx"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ============================================================================================ the group G_n and its chains
class FibredGroup:
    def __init__(self, n):
        self.n = n
        self.Phi = T.phi_power(n)
        assert T.apply(self.Phi, ELL) == ELL, "phi^n must fix the boundary word"
        self.gens = ["x", "y", "t"]
        self.rels = ["tx" + "T" + T.inv(self.Phi["x"]), "ty" + "T" + T.inv(self.Phi["y"])]
        self.mu, self.lam = "t", ELL
        self.ID = ("", 0)
        self.t = ("", 1)
        self.ell = (ELL, 0)
        self._pk = {}

    # ---- elements
    def phik(self, w, k):
        """Phi^k on a fibre word (k >= 0)"""
        key = (w, k)
        if key not in self._pk:
            out = w
            for _ in range(k):
                out = T.apply(self.Phi, out)
            self._pk[key] = out
        return self._pk[key]

    def mul(self, a, b):
        (f, k), (g, l) = a, b
        assert k >= 0 and l >= 0
        return (T.red(f + self.phik(g, k)), k + l)

    @staticmethod
    def word(el):
        f, k = el
        return f + "t" * k

    # ---- chains: dicts {tuple of elements: integer}
    def norm(self, c):
        out = defaultdict(int)
        for cell, k in c.items():
            if k and all(g != self.ID for g in cell):
                out[cell] += k
        return {cell: k for cell, k in out.items() if k}

    def add(self, *chains):
        out = defaultdict(int)
        for c in chains:
            for cell, k in c.items():
                out[cell] += k
        return self.norm(out)

    @staticmethod
    def scale(c, a):
        return {cell: a * k for cell, k in c.items()}

    def boundary(self, c):
        out = defaultdict(int)
        for cell, k in c.items():
            n = len(cell)
            out[cell[1:]] += k
            for i in range(n - 1):
                out[cell[:i] + (self.mul(cell[i], cell[i + 1]),) + cell[i + 2:]] += k * (-1) ** (i + 1)
            out[cell[:-1]] += k * (-1) ** n
        return self.norm({cl: v for cl, v in out.items() if len(cl) > 0})

    def conj_t(self, g):
        f, k = g
        assert k == 0
        return (self.phik(f, 1), 0)

    def prism(self, c):
        """h on 1- and 2-chains of the fibre: dh + hd = 1 - c_t, c_t = conjugation by t (= Phi on the fibre)"""
        out = defaultdict(int)
        t = self.t
        for cell, k in c.items():
            if len(cell) == 1:
                (g,) = cell
                out[(t, g)] += k
                out[(self.conj_t(g), t)] -= k
            else:
                g, r = cell
                g1, r1 = self.conj_t(g), self.conj_t(r)
                out[(t, g, r)] += k
                out[(g1, t, r)] -= k
                out[(g1, r1, t)] += k
        return self.norm(out)

    @staticmethod
    def fox_terms(w):
        """(sign, prefix, generator) per letter: a positive letter at prefix u gives (+1, u, g); an inverse letter gives (-1, u g^-1, g)"""
        out, pre = [], ""
        for ch in w:
            if ch.islower():
                out.append((1, pre, ch))
                pre = T.red(pre + ch)
            else:
                pre = T.red(pre + ch)
                out.append((-1, pre, ch.lower()))
        return out

    def fill(self, c):
        """K on 2-chains of the fibre: dK(w) = w for a 2-cycle w (asserted by the caller)"""
        out = defaultdict(int)
        for (g, r), k in c.items():
            assert g[1] == 0 and r[1] == 0
            for (sg, u, gen) in self.fox_terms(r[0]):
                out[(g, (u, 0), (gen, 0))] += k * sg
        return self.norm(out)

    def push(self, c):
        out = defaultdict(int)
        for cell, k in c.items():
            out[tuple(self.conj_t(g) for g in cell)] += k
        return self.norm(out)

    def sigma(self, w=ELL):
        """a 2-chain of the fibre with d sigma = -[w] (w in the commutator subgroup, reduced)"""
        out = defaultdict(int)
        for j in range(1, len(w)):
            out[((T.red(w[:j]), 0), (w[j], 0))] += 1
        for ch in w:
            if ch.isupper():
                out[((ch.lower(), 0), (ch, 0))] -= 1
        return self.norm(out)

    def fundamental(self):
        """(C, z, checks): the relative fundamental class of (M_n, dM_n) in the bar complex, every identity asserted"""
        sg = self.sigma()
        ok = {"d sigma = -[ell]": self.boundary(sg) == {(self.ell,): -1}}
        w = self.add(self.push(sg), self.scale(sg, -1))
        ok["Phi_* sigma - sigma is a cycle"] = self.boundary(w) == {}
        E = self.fill(w)
        ok["dK(w) = w"] = self.boundary(E) == w
        C = self.add(self.prism(sg), E)
        z = self.norm({(self.t, self.ell): 1, (self.ell, self.t): -1})
        ok["dz = 0"] = self.boundary(z) == {}
        ok["dC = z"] = self.boundary(C) == z
        assert all(ok.values()), ok
        return C, z, ok


# ============================================================================================ modules and cocycles on G_n
class Module:
    """matrices for x, y, t (DomainMatrices over one domain), with cached values on words"""

    def __init__(self, G, mats):
        self.G = G
        self.rep = T.DMRep(G.gens, mats)
        self.d, self.dom = self.rep.d, self.rep.dom
        self._rho = {"": DomainMatrix.eye(self.d, self.dom)}

    def rho(self, w):
        if w in self._rho:
            return self._rho[w]
        i = len(w)
        while w[:i] not in self._rho:
            i -= 1
        P = self._rho[w[:i]]
        for j in range(i, len(w)):
            P = P * self.rep.M[w[j]]
            self._rho[w[:j + 1]] = P
        return P

    def check(self):
        return self.rep.check(self.G.rels)

    def dual(self):
        return Module(self.G, {g: T.dm_inv(self.rep.M[g]).transpose() for g in self.G.gens})

    def wedge2(self):
        return Module(self.G, {g: T.wedge2(self.rep.M[g]) for g in self.G.gens})

    def extension(self, coc):
        """W = [[V, c], [0, 1]] for a cocycle given as a stacked column (values on x, y, t)"""
        return Module(self.G, {g: m for g, m in T.extension_rep(self.rep, coc).M.items() if g in self.G.gens})


class Cocycle:
    """a 1-cocycle given by its values on x, y, t (column DomainMatrices), evaluated on words by Fox calculus"""

    def __init__(self, mod, vals):
        self.mod = mod
        self.v = {g: vals[g] for g in mod.G.gens}
        self._val = {"": DomainMatrix.zeros((mod.d, 1), mod.dom)}

    @classmethod
    def from_column(cls, mod, col):
        d = mod.d
        return cls(mod, {g: col[i * d:(i + 1) * d, :] for i, g in enumerate(mod.G.gens)})

    def column(self):
        return self.v["x"].vstack(self.v["y"], self.v["t"])

    def __call__(self, w):
        if w in self._val:
            return self._val[w]
        i = len(w)
        while w[:i] not in self._val:
            i -= 1
        val = self._val[w[:i]]
        for j in range(i, len(w)):
            ch = w[j]
            if ch.islower():
                val = val + self.mod.rho(w[:j]) * self.v[ch]
            else:
                val = val - self.mod.rho(w[:j + 1]) * self.v[ch.lower()]
            self._val[w[:j + 1]] = val
        return val

    def is_cocycle(self):
        """the relators evaluate to zero"""
        return all(self(r).is_zero_matrix for r in self.mod.G.rels)

    def plus_coboundary(self, u):
        I = DomainMatrix.eye(self.mod.d, self.mod.dom)
        return Cocycle(self.mod, {g: self.v[g] + (self.mod.rep.M[g] - I) * u for g in self.mod.G.gens})

    def scaled(self, a):
        return Cocycle(self.mod, {g: self.v[g] * a for g in self.mod.G.gens})


def solve(A, b):
    """one solution x of A x = b over A's domain, or None"""
    dom, n = A.domain, A.shape[1]
    rows = [r + [bb[0]] for r, bb in zip(A.to_list(), b.to_list())]
    R, piv = T._rref(rows, n + 1, dom)
    if n in piv:
        return None
    x = [dom.zero] * n
    for i, pc in enumerate(piv):
        x[pc] = R[i][n]
    return DomainMatrix([[v] for v in x], (n, 1), dom)


def peripheral_coboundaries(mod):
    I = DomainMatrix.eye(mod.d, mod.dom)
    return (mod.rho("t") - I).vstack(mod.rho(ELL) - I)


def relative_lift(coc):
    """e with coc(t) = (t - 1) e and coc(ELL) = (ELL - 1) e, or None"""
    return solve(peripheral_coboundaries(coc.mod), coc("t").vstack(coc(ELL)))


def triple(G, C, z, h, a, b, form, e=None):
    """Y = <(h, e) u a u b, (C, z)> through the trilinear form(u, v, w) -> domain element; e = h's relative lift (computed if None)"""
    if e is None:
        e = relative_lift(h)
        assert e is not None, "the first class does not restrict to a coboundary on the cusp"
    dom = h.mod.dom
    tot = dom.zero
    for (g1, g2, g3), k in C.items():
        w1 = G.word(g1)
        w12 = G.word(G.mul(g1, g2))
        tot += dom.convert(k) * form(h(w1), a.mod.rho(w1) * a(G.word(g2)), b.mod.rho(w12) * b(G.word(g3)))
    for (p1, p2), k in z.items():
        w1 = G.word(p1)
        tot -= dom.convert(k) * form(e, a(w1), b.mod.rho(w1) * b(G.word(p2)))
    return tot


# ---- the invariant forms
def pairs(d):
    return [(i, j) for i in range(d) for j in range(i + 1, d)]


def form_wedge(dW):
    """Lambda^2 W (x) W* (x) W* -> C:  (omega, f, g) -> (f ^ g)(omega) = sum_{i<j} omega_ij (f_i g_j - f_j g_i)"""
    P = pairs(dW)

    def F(om, f, g):
        o, ff, gg = om.to_list(), f.to_list(), g.to_list()
        tot = o[0][0] - o[0][0]
        for k, (i, j) in enumerate(P):
            tot += o[k][0] * (ff[i][0] * gg[j][0] - ff[j][0] * gg[i][0])
        return tot
    return F


def form_permuted(form, perm):
    """the same form with its arguments read in another order: perm = positions of (omega, f, g) among the new arguments"""
    def F(*args):
        return form(*(args[i] for i in perm))
    return F


def form_line_pairing():
    """V (x) C (x) V* -> C:  (v, s, f) -> s <f, v>"""
    def F(v, s1, f):
        vv, ff = v.to_list(), f.to_list()
        tot = vv[0][0] - vv[0][0]
        for i in range(len(vv)):
            tot += ff[i][0] * vv[i][0]
        return tot * s1.to_list()[0][0]
    return F


# ============================================================================================ Ballas' family on G_n
def rho_mats(G, field, mats=None):
    """rho_q on x = nM, y = mnMM, t = m^n, as DomainMatrices over a tower_lib Field"""
    mats = mats or T.symbolic_mats()
    words = {"x": T.FIBRE["x"], "y": T.FIBRE["y"], "t": "m" * G.n}
    return {g: field.mat(T.word_matrix(mats, w).applyfunc(sp.cancel)) for g, w in words.items()}


def member_mats(G, field, ab, lam_sign, rho=None):
    """V = nu (x) rho_q for an order-2 fibre character nu = (a, b) mod 4 (a, b even) and nu(t) = lam_sign = +-1: rational over Q(q)"""
    a, b = ab
    assert a % 2 == 0 and b % 2 == 0
    rho = rho or rho_mats(G, field)
    sx, sy = (-1) ** (a // 2), (-1) ** (b // 2)
    dom = field.dom
    return {"x": rho["x"] * dom.convert(sx), "y": rho["y"] * dom.convert(sy), "t": rho["t"] * dom.convert(lam_sign)}


def trivial_module(G, dom):
    one = DomainMatrix([[dom.one]], (1, 1), dom)
    return Module(G, {g: one for g in G.gens})


def fibration_class(G, dom):
    """e(x) = e(y) = 0, e(t) = 1 in the trivial module"""
    M = trivial_module(G, dom)
    z0 = DomainMatrix([[dom.zero]], (1, 1), dom)
    return Cocycle(M, {"x": z0, "y": z0, "t": DomainMatrix([[dom.one]], (1, 1), dom)})


# ============================================================================================ cohomology on G_n
def h1_basis(mod):
    cls, h1 = T.h1_classes(mod.rep, mod.G.rels)
    return [Cocycle.from_column(mod, c) for c in cls], h1


def coboundary_matrix(mod):
    I = DomainMatrix.eye(mod.d, mod.dom)
    return (mod.rep.M["x"] - I).vstack(mod.rep.M["y"] - I, mod.rep.M["t"] - I)


def rank_mod_coboundaries(mod, cocs):
    """the dimension of the span of the given cocycles in H^1"""
    B = coboundary_matrix(mod)
    rb = T.dm_rank(B)
    if not cocs:
        return 0
    return T.dm_rank(B.hstack(*[c.column() for c in cocs])) - rb


def cohomology_data(mod):
    return T.cohomology_data(mod.rep, mod.G.rels, mod.G.mu, mod.G.lam)


def index(mod):
    return T.index(mod.rep, mod.G.rels, mod.G.mu, mod.G.lam)


def interior_classes(mod):
    """a basis of the kernel of H^1(G) -> H^1(P) as (cocycle, relative lift) pairs"""
    basis, h1 = h1_basis(mod)
    if not basis:
        return []
    dom = mod.dom
    BP = peripheral_coboundaries(mod)
    R = [c("t").vstack(c(ELL)) for c in basis]
    A = R[0].hstack(*R[1:], BP * dom.convert(-1)) if len(R) > 1 else R[0].hstack(BP * dom.convert(-1))
    ns = T.dm_nullspace(A)
    k = len(basis)
    out, span = [], []
    for v in ns:
        coeffs = [v[i, 0].element for i in range(k)]
        if all(cf == dom.zero for cf in coeffs):
            continue                                   # an invariant of P, not a class
        coc = None
        for cf, c in zip(coeffs, basis):
            term = c.scaled(cf)
            coc = term if coc is None else Cocycle(mod, {g: coc.v[g] + term.v[g] for g in mod.G.gens})
        if rank_mod_coboundaries(mod, span + [coc]) > len(span):
            span.append(coc)
            out.append((coc, v[k:, :]))
    return out


def quotient_to_V(wmod_wedge, coc, dW):
    """Lambda^2 W -> V (the e_i ^ e_last components, i < last) applied to a cocycle of Lambda^2 W"""
    P = pairs(dW)
    idx = [P.index((i, dW - 1)) for i in range(dW - 1)]
    return {g: DomainMatrix([[coc.v[g][i, 0].element] for i in idx], (dW - 1, 1), wmod_wedge.dom) for g in wmod_wedge.G.gens}


def include_Vstar(wedge_dual_mod, cstar, dW):
    """V* -> Lambda^2 W*, f -> f ^ e*_last (the (i, last) components), applied to a cocycle of V*"""
    P = pairs(dW)
    dom = wedge_dual_mod.dom
    vals = {}
    for g in wedge_dual_mod.G.gens:
        col = [dom.zero] * len(P)
        for i in range(dW - 1):
            col[P.index((i, dW - 1))] = cstar.v[g][i, 0].element
        vals[g] = DomainMatrix([[x] for x in col], (len(P), 1), dom)
    return Cocycle(wedge_dual_mod, vals)


# ============================================================================================ the fibre polynomial of an arbitrary module of pi
def fox_on_fibre(mats_xy, w):
    """Fox derivatives of a word in x, y evaluated in a representation of the fibre (sympy matrices): {g: matrix}"""
    d = mats_xy["x"].shape[0]
    D = {g: sp.zeros(d) for g in "xy"}
    pre = sp.eye(d)
    inv = {g: mats_xy[g].inv() for g in "xy"}
    for ch in w:
        g = ch.lower()
        if ch.islower():
            D[g] += pre
            pre = pre * mats_xy[g]
        else:
            pre = pre * inv[g]
            D[g] -= pre
    return D


def fibre_monodromy(E):
    """for a representation E of pi on m, n (sympy matrices): the matrix S on Z^1(F; E) = E^2 (coordinates (c(x), c(y))),
    (S c)(g) = E(m)^-1 c(phi(g)), and the coboundary matrix B (columns v -> (E(x) v - v, E(y) v - v))"""
    Ex = T.word_matrix(E, T.FIBRE["x"])
    Ey = T.word_matrix(E, T.FIBRE["y"])
    Mi = E["m"].inv()
    d = Ex.shape[0]
    D = fox_on_fibre({"x": Ex, "y": Ey}, T.PHI["y"])
    S = sp.zeros(2 * d)
    S[:d, d:] = Mi                                 # (S c)(x) = E(m)^-1 c(y)
    S[d:, :d] = Mi * D["x"]                         # (S c)(y) = E(m)^-1 (D_x c(x) + D_y c(y))
    S[d:, d:] = Mi * D["y"]
    B = (Ex - sp.eye(d)).col_join(Ey - sp.eye(d))
    return S.applyfunc(sp.cancel), B.applyfunc(sp.cancel)


def wedge2_sym(M):
    d = M.shape[0]
    P = pairs(d)
    return sp.Matrix([[M[i, k] * M[j, l] - M[i, l] * M[j, k] for (k, l) in P] for (i, j) in P])


# ============================================================================================ the fibre polynomial over Q(q)
def laurent_range(M):
    lo, hi = 0, 0
    for e in M:
        num, den = sp.fraction(sp.cancel(e))
        if num == 0:
            continue
        dp = sp.Poly(den, q)
        assert len(dp.terms()) == 1, ("denominator not a monomial", den)
        dk = dp.degree()
        npl = sp.Poly(num, q)
        mons = [m[0] for m in npl.monoms()]
        lo, hi = min(lo, min(mons) - dk), max(hi, max(mons) - dk)
    return lo, hi


def fmpq_mat_at(M, qv):
    rows = [[sp.Rational(M[i, j].subs(q, qv)) for j in range(M.shape[1])] for i in range(M.shape[0])]
    return flint.fmpq_mat(M.shape[0], M.shape[1], [flint.fmpq(int(x.p), int(x.q)) for r in rows for x in r])


def interpolate(xs, ys):
    """the polynomial of degree < len(xs) through the points (exact: Newton's divided differences in Fractions)"""
    X = [Fraction(int(x)) for x in xs]
    c = [Fraction(int(sp.Rational(y).p), int(sp.Rational(y).q)) for y in ys]
    n = len(X)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            c[i] = (c[i] - c[i - 1]) / (X[i] - X[i - j])
    poly = [Fraction(0)] * n                      # coefficients low to high
    for i in range(n - 1, -1, -1):                # Horner on the Newton form
        new = [Fraction(0)] * n
        for k in range(n - 1):
            new[k + 1] += poly[k]
        for k in range(n):
            new[k] -= X[i] * poly[k]
        new[0] += c[i]
        poly = new
    return sp.expand(sum(sp.Rational(a.numerator, a.denominator) * q ** k for k, a in enumerate(poly)))


def fibre_polynomial(E):
    """P(q, s) = det(s - S on H^1(F; E)) over Q(q), with S's charpoly on Z^1 divided by the coboundary part, asserted"""
    S, B = fibre_monodromy(E)
    n = S.shape[0]
    d = n // 2
    lo, hi = laurent_range(S)
    npts = n * (hi - lo) + 4
    xs = list(range(2, 2 + npts))
    vals = [fmpq_mat_at(S, x).charpoly() for x in xs]          # fmpq_poly, monic of degree n, coefficients low to high
    coeffs = []
    for j in range(1, n + 1):                                   # coefficient of s^(n - j): Laurent in [j lo, j hi]
        ys = [sp.Rational(int(v[n - j].p), int(v[n - j].q)) * sp.Integer(x) ** (-j * lo) for v, x in zip(vals, xs)]
        poly = interpolate(xs[:j * (hi - lo) + 1], ys[:j * (hi - lo) + 1])
        for x, y in zip(xs[j * (hi - lo) + 1:j * (hi - lo) + 4], ys[j * (hi - lo) + 1:j * (hi - lo) + 4]):
            assert poly.subs(q, x) == y, "interpolation check failed"
        coeffs.append(sp.expand(poly * q ** (j * lo)))
    full = sp.expand(s ** n + sum(c * s ** (n - j) for j, c in enumerate(coeffs, start=1)))
    # the coboundary part: S acts on B^1 as E(m)^-1
    Pb = sp.expand((s * sp.eye(d) - E["m"].inv()).det())
    quo, rem = sp.div(sp.Poly(full, s), sp.Poly(Pb, s))
    assert rem.is_zero, "the coboundary part does not divide"
    P = sp.expand(quo.as_expr())
    # fresh points: exact charpoly at q = 1/3, 5/7
    for qv in (sp.Rational(1, 3), sp.Rational(5, 7)):
        cp = fmpq_mat_at(S, qv).charpoly()
        direct = sp.expand(sum(sp.Rational(int(cp[k].p), int(cp[k].q)) * s ** k for k in range(n + 1)))
        assert sp.expand(full.subs(q, qv) - direct) == 0, "fresh point disagrees"
    rank_B = T.dm_rank(DomainMatrix.from_Matrix(B.subs(q, sp.Rational(7, 3))).convert_to(sp.QQ))
    return {"P": P, "deg_s": sp.Poly(P, s).degree(), "laurent_range_S": (lo, hi), "points": npts, "rank_B_at_q=7/3": rank_B,
            "Pb": Pb}
