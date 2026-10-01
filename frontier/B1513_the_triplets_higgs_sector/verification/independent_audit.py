"""B1513 -- INDEPENDENT AUDIT of the banked NEGATIVE (post-bank, 2026-10-01).

The owner's rule: no negative may stand on a bug.  This script re-derives every zero B1513 banked, with code that shares nothing
with the arc's instrument (higgs_lib.py), B1511's tower_lib.py or B1509's extension_index.py, and by a different method.

What is re-derived.
  Z1  the coupling form B(a, a') = Y(h, a, a') vanishes on all of H^1(W*), at every member of both populations (P4's NO, post-run (b));
  Z2  the mu-type pairing <h u e u hbar> vanishes at both populations (post-run (c));
  Z3  no invariant form joins two different members (P5);
  Z4  the Higgs sector's dimensions (P3), and the computational inputs of T-HIGGS-BULK-ACYCLIC.
Positive controls (two-sided, WORKING_RULES E52):
  C1  at B1510's four +-i points the same code finds B != 0 and <h u e u hbar> != 0 (B1513 post-run (a): -lam_h kappa and lam_h kappa);
  C2  the same classes pulled back to the level-3 group G_3 stay non-zero (population I runs on G_3);
  C3  B is symmetric where it is non-zero (graded commutativity of the wedge cup); a coboundary in either slot changes nothing; a
      non-cocycle is caught; a random corner is caught; the wedge form is found as the invariant form at i = j = k.

The method.  For 1-cocycles a in Z^1(G; A), b in Z^1(G; B) and an equivariant bilinear map mu: A (x) B -> C, the class
[mu(a u b)] in H^2(G; C) vanishes iff
    R(g) = [[C(g), N(g), beta(g)], [0, B(g), b(g)], [0, 0, 1]],      N(g) v = mu(a(g) (x) B(g) v),
is a homomorphism of G for some cochain beta.  (The (1,2) block is a cocycle because mu is equivariant.  The corner of R(g)R(k) is
beta(g) + g beta(k) + mu(a(g) (x) g b(k)), so beta exists iff delta beta = -mu(a u b).)  On a relator r the corner of R(r) is
Q_r + L_r(beta): Q is the corner at beta = 0, and L is the coboundary d^1 of C, read off the same way from [[C, beta], [0, 1]].
So the class is zero iff Q lies in the image of L.  G_n's presentation complex is the mapping torus of a rose, hence aspherical, so
these are the cohomology groups of M_n.  Only products of block matrices along relator words are used: no bar chains, no fundamental
class, no relative lift, no triple-product formula, no Fox calculus.

Why this decides the banked claims.  Lambda^2 W is acyclic on the cusp (checked below), so Poincare-Lefschetz duality pairs
H^1(M; Lambda^2 W) = H^1(M, dM; Lambda^2 W) perfectly with H^2(M; Lambda^2 W*), and Y(h, a, b) is that pairing applied to h and the
class of a ^ b.  Hence B = 0 on H^1(W*) iff [a ^ b] = 0 in H^2(M; Lambda^2 W*) for all a, b; and <h u e u hbar> = 0 iff
[hbar u e] = 0 there.

Arithmetic.  Route E is exact, over the number fields Q(q) (sympy's AlgebraicField, not the instrument's FiniteExtension); one
computation per population covers every conjugate point.  Route P works over GF(p) for several primes and every root, with this
file's own numpy elimination.  Route E decides the zero claims, and route P must agree everywhere.  For the invariant forms (Z3)
route P is rigorous on its own: invariants can only gain dimension mod p, and the wedge form is invariant over Q."""
import json
import random
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
RECORD = HERE / "independent_audit_run.txt"
Qs = sp.Symbol("q")

# ============================================================================================ words
FIBRE_MN = {"x": "nM", "y": "mnMM"}          # x = n m^-1, y = m n m^-2
PHI = {"x": "y", "y": "yXyy"}                 # phi(g) = m g m^-1 on the fibre
RELATOR_MN = "mnMNmNMnmN"                     # pi_1(m004) = <m, n | mnm^-1n^-1 m n^-1m^-1 n m n^-1>
LONGITUDE_MN = "nMNmmNMn"
ELL = "yXYx"                                  # the fibre's boundary word


def inv(w):
    return "".join(c.swapcase() for c in reversed(w))


def red(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def phi(w):
    return red("".join(PHI[c] if c.islower() else inv(PHI[c.lower()]) for c in w))


def phi_n(n):
    img = {"x": "x", "y": "y"}
    for _ in range(n):
        img = {g: phi(img[g]) for g in img}
    return img


def relators(n):
    """G_n = <x, y, t | t g t^-1 = phi^n(g)>"""
    P = phi_n(n)
    return ["txT" + inv(P["x"]), "tyT" + inv(P["y"])]


GENS = ("x", "y", "t")


# ============================================================================================ two arithmetic backends
class Exact:
    """a number field, sympy's AlgebraicField (dense ANP arithmetic)"""

    def __init__(self, K, label):
        self.K, self.label = K, label

    def s(self, expr):
        return self.K.from_sympy(sp.nsimplify(expr) if isinstance(expr, float) else sp.sympify(expr))

    def c(self, k):
        return self.K.convert(sp.Rational(k))

    def sinv(self, x):
        return self.K.exquo(self.K.one, x)

    def mat(self, rows):
        return DomainMatrix([[self.K.convert(v) for v in r] for r in rows], (len(rows), len(rows[0])), self.K)

    def eye(self, d):
        return DomainMatrix.eye(d, self.K)

    def zeros(self, r, c):
        return DomainMatrix.zeros((r, c), self.K)

    def mul(self, A, B):
        return A * B

    def add(self, A, B):
        return A + B

    def sub(self, A, B):
        return A - B

    def smul(self, a, A):
        return A * self.K.convert(a)

    def inv(self, A):
        return A.inv()

    def T(self, A):
        return A.transpose()

    def hstack(self, Ms):
        return Ms[0].hstack(*Ms[1:]) if len(Ms) > 1 else Ms[0]

    def vstack(self, Ms):
        return Ms[0].vstack(*Ms[1:]) if len(Ms) > 1 else Ms[0]

    def sub_block(self, A, r0, r1, c0, c1):
        return A[r0:r1, c0:c1]

    def tolist(self, A):
        return A.to_list()

    def rank(self, A):
        return A.rank()

    def nullspace(self, A):
        """a basis of {v : A v = 0} as column matrices"""
        N = A.nullspace()
        return [N[i:i + 1, :].transpose() for i in range(N.shape[0])]

    def is_zero(self, A):
        return A.is_zero_matrix

    def zero_scalar(self, x):
        return x == self.K.zero

    def show(self, x):
        return str(self.K.to_sympy(x))


class ModP:
    """GF(p), p < 2^23 so that int64 products of residues and their short sums never overflow"""

    def __init__(self, p, label):
        assert p < 2 ** 23
        self.p, self.label = p, label

    def s(self, expr):
        r = sp.Rational(expr)
        return int(r.p) % self.p * pow(int(r.q) % self.p, -1, self.p) % self.p

    def c(self, k):
        return self.s(k)

    def sinv(self, x):
        return pow(int(x) % self.p, -1, self.p)

    def mat(self, rows):
        return np.array([[int(v) % self.p for v in r] for r in rows], dtype=np.int64)

    def eye(self, d):
        return np.eye(d, dtype=np.int64)

    def zeros(self, r, c):
        return np.zeros((r, c), dtype=np.int64)

    def mul(self, A, B):
        assert A.shape[1] < 2 ** 16
        return (A @ B) % self.p

    def add(self, A, B):
        return (A + B) % self.p

    def sub(self, A, B):
        return (A - B) % self.p

    def smul(self, a, A):
        return (int(a) % self.p * A) % self.p

    def rref(self, A):
        A = A.copy() % self.p
        rows, cols = A.shape
        piv, r = [], 0
        for c in range(cols):
            if r == rows:
                break
            nz = np.nonzero(A[r:, c])[0]
            if len(nz) == 0:
                continue
            k = r + int(nz[0])
            if k != r:
                A[[r, k]] = A[[k, r]]
            A[r] = (A[r] * pow(int(A[r, c]), -1, self.p)) % self.p
            others = np.nonzero(A[:, c])[0]
            others = others[others != r]
            if len(others):
                A[others] = (A[others] - np.outer(A[others, c], A[r]) % self.p) % self.p
            piv.append(c)
            r += 1
        return A, piv

    def inv(self, A):
        d = A.shape[0]
        R, piv = self.rref(np.hstack([A % self.p, np.eye(d, dtype=np.int64)]))
        assert piv[:d] == list(range(d)), "singular matrix"
        return R[:, d:]

    def T(self, A):
        return A.T.copy()

    def hstack(self, Ms):
        return np.hstack(Ms)

    def vstack(self, Ms):
        return np.vstack(Ms)

    def sub_block(self, A, r0, r1, c0, c1):
        return A[r0:r1, c0:c1].copy()

    def tolist(self, A):
        return A.tolist()

    def rank(self, A):
        return len(self.rref(A)[1])

    def nullspace(self, A):
        R, piv = self.rref(A)
        cols = A.shape[1]
        out = []
        for f in [c for c in range(cols) if c not in piv]:
            v = np.zeros((cols, 1), dtype=np.int64)
            v[f, 0] = 1
            for i, pc in enumerate(piv):
                v[pc, 0] = (-R[i, f]) % self.p
            out.append(v)
        return out

    def is_zero(self, A):
        return not np.any(A % self.p)

    def zero_scalar(self, x):
        return int(x) % self.p == 0

    def show(self, x):
        return int(x) % self.p


# ============================================================================================ Ballas' family, from its definition
def ballas_sym():
    """rho_q(m), rho_q(n) with t = q/2 (the audit lane's harmonic family; B1509 FINDINGS)"""
    t = Qs / 2
    m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
    n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return m, n


def rf_at(F, expr, q):
    """a rational function of q, evaluated at the backend scalar q"""
    num, den = sp.fraction(sp.cancel(sp.sympify(expr)))

    def poly_at(e):
        P = sp.Poly(e, Qs)
        acc = F.c(0)
        for cf in P.all_coeffs():
            acc = acc * q + F.s(cf)
        return acc
    return poly_at(num) * F.sinv(poly_at(den))


def mn_mats(F, q):
    m, n = ballas_sym()
    M = F.mat([[rf_at(F, e, q) for e in m.row(i)] for i in range(4)])
    N = F.mat([[rf_at(F, e, q) for e in n.row(i)] for i in range(4)])
    return {"m": (M, F.inv(M)), "n": (N, F.inv(N))}


def word(F, gens, w, d):
    X = F.eye(d)
    for ch in w:
        X = F.mul(X, gens[ch][0] if ch.islower() else gens[ch.lower()][1])
    return X


class Rep:
    """a representation of G_n on x, y, t (matrix and inverse per generator)"""

    def __init__(self, F, n, mats):
        self.F, self.n = F, n
        self.d = mats["x"].shape[0]
        self.g = {k: (mats[k], F.inv(mats[k])) for k in GENS}
        self.rels = relators(n)

    def w(self, word_):
        return word(self.F, self.g, word_, self.d)

    def relators_hold(self):
        I = self.F.eye(self.d)
        return all(self.F.is_zero(self.F.sub(self.w(r), I)) for r in self.rels)

    def dual(self):
        return Rep(self.F, self.n, {k: self.F.T(self.g[k][1]) for k in GENS})

    def wedge2(self):
        return Rep(self.F, self.n, {k: compound2(self.F, self.g[k][0]) for k in GENS})


def pairs(d):
    return [(i, j) for i in range(d) for j in range(i + 1, d)]


def compound2(F, A):
    a = F.tolist(A)
    P = pairs(len(a))
    return F.mat([[a[i][k] * a[j][l] - a[i][l] * a[j][k] for (k, l) in P] for (i, j) in P])


def wedge_vec(F, u, w):
    """u ^ w in the basis e_i ^ e_j (i < j): components u_i w_j - u_j w_i"""
    uu, ww = [r[0] for r in F.tolist(u)], [r[0] for r in F.tolist(w)]
    return F.mat([[uu[i] * ww[j] - uu[j] * ww[i]] for (i, j) in pairs(len(uu))])


def level_rep(F, mn, n, twist):
    """nu (x) rho_q on G_n:  x = n m^-1, y = m n m^-2, t = m^n; twist = (nu(x), nu(y), nu(t)) as backend scalars"""
    words = {"x": FIBRE_MN["x"], "y": FIBRE_MN["y"], "t": "m" * n}
    return Rep(F, n, {k: F.smul(tw, word(F, mn, words[k], 4)) for k, tw in zip(GENS, twist)})


# ============================================================================================ cochains by block products along words
def coboundary_0(rep):
    F, I = rep.F, rep.F.eye(rep.d)
    return F.vstack([F.sub(rep.g[k][0], I) for k in GENS])


def coboundary_1(rep):
    """d^1: the relators' corners of [[C, beta], [0, 1]] as linear maps of beta = (beta_x; beta_y; beta_t); (A, X) pairs compose as
    (A, X)(B, Y) = (AB, AY + X), which is the block product with the identity block dropped"""
    F, d = rep.F, rep.d
    E = {}
    for i, k in enumerate(GENS):
        blocks = [F.zeros(d, d) for _ in GENS]
        blocks[i] = F.eye(d)
        E[k] = F.hstack(blocks)
    rows = []
    for r in rep.rels:
        A, X = F.eye(d), F.zeros(d, 3 * d)
        for ch in r:
            k = ch.lower()
            if ch.islower():
                B, Y = rep.g[k][0], E[k]
            else:
                B = rep.g[k][1]
                Y = F.smul(-1, F.mul(B, E[k]))
            A, X = F.mul(A, B), F.add(F.mul(A, Y), X)
        assert F.is_zero(F.sub(A, F.eye(d))), "a relator fails in the module"
        rows.append(X)
    return F.vstack(rows)


def cohomology(rep):
    F, d = rep.F, rep.d
    D0, D1 = coboundary_0(rep), coboundary_1(rep)
    assert F.is_zero(F.mul(D1, D0)), "d^1 d^0 != 0"
    r0, r1 = F.rank(D0), F.rank(D1)
    out = {"h0": d - r0, "h1": 3 * d - r1 - r0, "h2": 2 * d - r1}
    return out, D0, D1


def h1_basis(rep, D0, D1):
    """cocycles (columns of length 3d) completing a basis of B^1 to one of Z^1"""
    F = rep.F
    Z = F.nullspace(D1)
    cur = D0
    rk = F.rank(cur)
    out = []
    for z in Z:
        nxt = F.hstack([cur, z])
        rn = F.rank(nxt)
        if rn > rk:
            out.append(z)
            cur, rk = nxt, rn
    return out


def values(F, col, d):
    return {k: F.sub_block(col, i * d, (i + 1) * d, 0, 1) for i, k in enumerate(GENS)}


def extension(rep, cvals):
    """W = [[V, c], [0, 1]]"""
    F, d = rep.F, rep.d
    mats = {}
    for k in GENS:
        top = F.hstack([rep.g[k][0], cvals[k]])
        bot = F.hstack([F.zeros(1, d), F.eye(1)])
        mats[k] = F.vstack([top, bot])
    return Rep(F, rep.n, mats)


def coker_functionals(F, D1):
    """row vectors y with y D1 = 0 (a basis of H^2's dual)"""
    return [F.T(v) for v in F.nullspace(F.T(D1))]


def cup_corner(C, B, Nfun, avals, bvals):
    """Q = the relators' corners of R(g) = [[C, N, 0], [0, B, b], [0, 0, 1]], N(g) = Nfun(a(g), B(g)); every other block of R(r)
    is checked to be the identity's (so a and b are cocycles and N is one too)"""
    F = C.F
    dc, db = C.d, B.d
    D = dc + db + 1
    R = {}
    for k in GENS:
        N = Nfun(avals[k], B.g[k][0])
        top = F.hstack([C.g[k][0], N, F.zeros(dc, 1)])
        mid = F.hstack([F.zeros(db, dc), B.g[k][0], bvals[k]])
        bot = F.hstack([F.zeros(1, dc + db), F.eye(1)])
        M = F.vstack([top, mid, bot])
        R[k] = (M, F.inv(M))
    Qs_, ok = [], True
    for r in C.rels:
        P = word(F, R, r, D)
        corner = F.sub_block(P, 0, dc, D - 1, D)
        rest = F.sub(P, F.eye(D))
        rest_wo = F.hstack([F.sub_block(rest, 0, D, 0, D - 1), F.vstack([F.zeros(dc, 1), F.sub_block(rest, dc, D, D - 1, D)])])
        ok = ok and F.is_zero(rest_wo)
        Qs_.append(corner)
    return F.vstack(Qs_), ok


def class_values(F, ys, Q):
    return [F.tolist(F.mul(y, Q))[0][0] for y in ys]


def N_wedge(F):
    def Nfun(a, Bg):
        cols = [wedge_vec(F, a, F.sub_block(Bg, 0, Bg.shape[0], k, k + 1)) for k in range(Bg.shape[1])]
        return F.hstack(cols)
    return Nfun


def N_scalar(F):
    def Nfun(a, Bg):
        return a                                    # mu(eta (x) s) = s eta, B trivial of rank one
    return Nfun


def trivial_rep(F, n):
    one = F.eye(1)
    return Rep(F, n, {k: one for k in GENS})


def fibration_class(F):
    return {"x": F.zeros(1, 1), "y": F.zeros(1, 1), "t": F.eye(1)}


# ============================================================================================ one member, read completely
def member(F, mn, n, twist, label, extra=None):
    """the Higgs sector and the couplings of W = [[V, c], [0, 1]] for V = twist (x) rho_q on G_n"""
    t0 = time.time()
    out = {"member": label}
    V = level_rep(F, mn, n, twist)
    out["relators hold on V"] = V.relators_hold()
    hV, D0V, D1V = cohomology(V)
    out["h(V)"] = hV
    cV = h1_basis(V, D0V, D1V)
    assert len(cV) == 1, (label, hV)
    W = extension(V, values(F, cV[0], 4))
    out["relators hold on W"] = W.relators_hold()
    Wd, L2W = W.dual(), W.wedge2()
    L2Wd = Wd.wedge2()
    L2V = V.wedge2()
    dims = {}
    for name, rep in (("V*", V.dual()), ("W", W), ("W*", Wd), ("Lambda2 V", L2V), ("Lambda2 W", L2W), ("Lambda2 W*", L2Wd)):
        dims[name] = cohomology(rep)[0]
    out["h"] = dims
    # the cusp: Lambda^2 W and Lambda^2 W* have no eigenvalue 1 on the longitude (so H*(cusp) = 0 and duality applies)
    I10 = F.eye(10)
    out["Lambda2 W, Lambda2 W* acyclic on the cusp (det(ell - 1) != 0)"] = [
        F.rank(F.sub(rep.w(ELL), I10)) == 10 for rep in (L2W, L2Wd)]
    out["ell commutes with t on W"] = F.is_zero(F.sub(F.mul(W.w(ELL), W.g["t"][0]), F.mul(W.g["t"][0], W.w(ELL))))
    # H^1(W*) and H^2(Lambda^2 W*)
    _, D0d, D1d = cohomology(Wd)
    A = h1_basis(Wd, D0d, D1d)
    _, D0c, D1c = cohomology(L2Wd)
    ys = coker_functionals(F, D1c)
    out["dim H^1(W*), dim H^2(Lambda2 W*)"] = [len(A), len(ys)]
    Nw = N_wedge(F)
    # f0 = the invariant line of W*, e f0 its class
    f0 = F.vstack([F.zeros(4, 1), F.eye(1)])
    ef0 = {"x": F.zeros(5, 1), "y": F.zeros(5, 1), "t": f0}
    ef0_col = F.vstack([ef0[k] for k in GENS])
    out["e f0 is a cocycle"] = F.is_zero(F.mul(D1d, ef0_col))
    out["e f0 non-zero in H^1(W*)"] = F.rank(F.hstack([D0d, ef0_col])) > F.rank(D0d)
    # Z1: the class of a_i ^ a_j for a basis of H^1(W*)
    table, all_ok = [], True
    for i, ai in enumerate(A):
        row = []
        for j, aj in enumerate(A):
            Q, ok = cup_corner(L2Wd, Wd, Nw, values(F, ai, 5), values(F, aj, 5))
            all_ok = all_ok and ok
            row.append(class_values(F, ys, Q))
        table.append(row)
    out["blocks check (cocycles and N)"] = all_ok
    out["[a_i ^ a_j] in H^2(Lambda2 W*)"] = [[[F.show(v) for v in cell] for cell in row] for row in table]
    out["B == 0 on H^1(W*)"] = all(F.zero_scalar(v) for row in table for cell in row for v in cell)
    # the symmetry of B (C3)
    out["B symmetric"] = all(all(F.zero_scalar(u - v) for u, v in zip(table[i][j], table[j][i]))
                             for i in range(len(A)) for j in range(len(A)))
    # the class against e f0 for each basis element (Lemma 6's cross term)
    cross = []
    for ai in A:
        Q, ok = cup_corner(L2Wd, Wd, Nw, values(F, ai, 5), ef0)
        cross.append([F.show(v) for v in class_values(F, ys, Q)])
    out["[a_i ^ e f0]"] = cross
    # coboundary invariance (C3): a_0 + delta v in the first slot, a_1 + delta v' in the second
    rnd = random.Random(1513)
    v = F.mat([[rnd.randrange(1, 97)] for _ in range(5)])
    shift = F.mul(D0d, v)
    Qs1, _ = cup_corner(L2Wd, Wd, Nw, values(F, F.add(A[0], shift), 5), values(F, A[-1], 5))
    Qs2, _ = cup_corner(L2Wd, Wd, Nw, values(F, A[0], 5), values(F, F.add(A[-1], shift), 5))
    out["coboundary in either slot changes nothing"] = (
        all(F.zero_scalar(u - w) for u, w in zip(class_values(F, ys, Qs1), table[0][-1])) and
        all(F.zero_scalar(u - w) for u, w in zip(class_values(F, ys, Qs2), table[0][-1])))
    # a non-cocycle is caught (C3)
    bad = values(F, A[0], 5)
    bad = dict(bad, x=F.add(bad["x"], F.mat([[1], [0], [0], [0], [0]])))
    _, ok_bad = cup_corner(L2Wd, Wd, Nw, bad, values(F, A[-1], 5))
    out["a non-cocycle is caught"] = not ok_bad
    # a random corner is caught (C3): H^2 != 0, so a random vector is not in the image of d^1
    Rq = F.mat([[rnd.randrange(1, 10 ** 6)] for _ in range(20)])
    out["a random corner is caught"] = any(not F.zero_scalar(v) for v in class_values(F, ys, Rq))
    # Z2: the mu-type pairing, [hbar u e] in H^2(Lambda^2 W*)
    Hb = h1_basis(L2Wd, D0c, D1c)
    mus = []
    for hb in Hb:
        Q, ok = cup_corner(L2Wd, trivial_rep(F, n), N_scalar(F), values(F, hb, 10), fibration_class(F))
        all_ok = all_ok and ok
        mus.append(class_values(F, ys, Q))
    out["dim H^1(Lambda2 W*) (the 5bar'_H classes)"] = len(Hb)
    out["[hbar u e] in H^2(Lambda2 W*)"] = [[F.show(v) for v in row] for row in mus]
    out["mu-type pairing == 0"] = all(F.zero_scalar(v) for row in mus for v in row)
    out["blocks check (all products)"] = all_ok
    if extra is not None:
        extra(out, V, W, Wd, L2Wd, A, ef0, ys)
    out["seconds"] = round(time.time() - t0, 1)
    return out, W


# ============================================================================================ C2: pull a +-i point back to G_3
def pullback3(rep):
    """the restriction to G_3 = <x, y, t^3>"""
    F = rep.F
    return Rep(F, 3, {"x": rep.g["x"][0], "y": rep.g["y"][0], "t": F.mul(F.mul(rep.g["t"][0], rep.g["t"][0]), rep.g["t"][0])})


def pullback3_cocycle(rep, vals):
    """a(t^3) = corner of [[rho(t), a_t], [0, 1]]^3"""
    F, d = rep.F, rep.d
    M = F.vstack([F.hstack([rep.g["t"][0], vals["t"]]), F.hstack([F.zeros(1, d), F.eye(1)])])
    M3 = F.mul(F.mul(M, M), M)
    return {"x": vals["x"], "y": vals["y"], "t": F.sub_block(M3, 0, d, d, d + 1)}


def control_level3(out, V, W, Wd, L2Wd, A, ef0, ys):
    F = W.F
    Wd3, L2Wd3 = pullback3(Wd), pullback3(L2Wd)
    _, _, D1c3 = cohomology(L2Wd3)
    ys3 = coker_functionals(F, D1c3)
    Nw = N_wedge(F)
    vals = []
    for ai in A:
        Q, ok = cup_corner(L2Wd3, Wd3, Nw, pullback3_cocycle(Wd, values(F, ai, 5)), pullback3_cocycle(Wd, ef0))
        assert ok
        vals.append(class_values(F, ys3, Q))
    out["C2: dim H^2(M_3; Lambda2 W*)"] = len(ys3)
    out["C2: [a_i ^ e f0] pulled back to G_3 non-zero for some i"] = any(not F.zero_scalar(v) for row in vals for v in row)


# ============================================================================================ Z3: invariant forms (route P)
def invariant_forms(F, Ws):
    """dim of invariant forms on Lambda^2 W_k (x) W_i* (x) W_j*: rows T with T (R(g) - 1) = 0"""
    out = {}
    L2 = [W.wedge2() for W in Ws]
    Wd = [W.dual() for W in Ws]
    T0 = np.zeros((1, 250), dtype=np.int64)
    for a_, (i, j) in enumerate(pairs(5)):
        for k in range(5):
            for l in range(5):
                if (k, l) == (i, j):
                    T0[0, a_ * 25 + k * 5 + l] += 1
                if (k, l) == (j, i):
                    T0[0, a_ * 25 + k * 5 + l] -= 1
    T0 %= F.p
    wedge_found = True
    for k in range(len(Ws)):
        for i in range(len(Ws)):
            for j in range(len(Ws)):
                blocks = []
                for g in GENS:
                    R = np.kron(np.kron(L2[k].g[g][0], Wd[i].g[g][0]) % F.p, Wd[j].g[g][0]) % F.p
                    D = (R - np.eye(250, dtype=np.int64)) % F.p
                    blocks.append(D.T.copy())
                    if i == j == k:
                        wedge_found = wedge_found and not np.any((T0 @ D) % F.p)
                out[(k, i, j)] = 250 - F.rank(np.vstack(blocks))
    return out, wedge_found


# ============================================================================================ Z4: the bulk theorem's inputs
P_LAMBDA = None


def p_lambda(q, s):
    w = q + 1 / q
    return s ** 6 - 12 * s ** 5 + 48 * s ** 4 - (w ** 2 - w + 72) * s ** 3 + 48 * s ** 2 - 12 * s + 1


def bulk_checks(primes):
    out = {}
    s_, u = sp.symbols("s u")
    w = Qs + 1 / Qs
    f = u ** 3 - 12 * u ** 2 + 45 * u - 48
    out["s^-3 P = f(s + 1/s) - (w^2 - w)"] = sp.simplify(p_lambda(Qs, s_) / s_ ** 3 - (f.subs(u, s_ + 1 / s_) - (w ** 2 - w))) == 0
    out["f' = 3(u - 3)(u - 5), f(2) = 2, w^2 - w - 2 = (q - 1)^2 (q^2 + q + 1) / q^2"] = [
        sp.expand(sp.diff(f, u) - 3 * (u - 3) * (u - 5)) == 0, f.subs(u, 2) == 2,
        sp.simplify(w ** 2 - w - 2 - (Qs - 1) ** 2 * (Qs ** 2 + Qs + 1) / Qs ** 2) == 0]
    # H^0(F; Lambda^2 rho_q) = 0 for q > 0: gcd of 6 x 6 minors of 4q (Lambda^2 x - 1; Lambda^2 y - 1)
    m, n = ballas_sym()
    X = n * m.inv()
    Y = m * n * m.inv() * m.inv()

    def c2(A):
        P = pairs(4)
        return sp.Matrix([[A[i, k] * A[j, l] - A[i, l] * A[j, k] for (k, l) in P] for (i, j) in P])
    Bm = (4 * Qs * (c2(X) - sp.eye(6))).col_join(4 * Qs * (c2(Y) - sp.eye(6))).applyfunc(sp.cancel)
    assert all(sp.fraction(sp.cancel(e))[1].is_number for e in Bm), "4q B must be polynomial"
    rnd = random.Random(6)
    g = None
    tried = 0
    while tried < 40:
        rows = sorted(rnd.sample(range(12), 6))
        d = sp.factor(Bm.extract(rows, list(range(6))).det(method="berkowitz"))
        tried += 1
        if d == 0:
            continue
        g = d if g is None else sp.gcd(g, d)
    out["gcd of 40 random 6x6 minors of 4q B"] = str(sp.factor(g))
    out["no positive real root"] = all(not (r.is_real and r > 0) for r in sp.roots(sp.Poly(g, Qs)).keys()) if sp.Poly(g, Qs).degree() > 0 else True
    # P_Lambda is the polynomial whose roots are exactly the twists with cohomology: mod p, h^1(G_1; s (x) Lambda^2 rho_q) at the
    # roots s of P_Lambda(q, .) and at random non-roots
    rows = []
    for p in primes:
        F = ModP(p, f"GF({p})")
        rnd = random.Random(p)
        found = 0
        while found < 2:
            qv = rnd.randrange(2, p - 1)
            iq = pow(qv, -1, p)
            wv = (qv + iq) % p
            coeffs = [1, -12, 48, -((wv * wv - wv + 72) % p), 48, -12, 1]
            S = np.arange(p, dtype=np.int64)
            acc = np.zeros(p, dtype=np.int64)
            for cf in coeffs:
                acc = (acc * S + cf) % p
            roots = [int(r) for r in np.nonzero(acc == 0)[0] if r != 0]
            if not roots:
                continue
            found += 1
            mn = mn_mats(F, qv)
            Lam = level_rep(F, mn, 1, (1, 1, 1)).wedge2()
            res = {"q": qv, "roots": roots, "h1 at roots": [], "h1 at 5 non-roots": []}
            for sv in roots:
                rep = Rep(F, 1, {"x": Lam.g["x"][0], "y": Lam.g["y"][0], "t": F.smul(sv, Lam.g["t"][0])})
                res["h1 at roots"].append(cohomology(rep)[0]["h1"])
            for _ in range(5):
                sv = rnd.randrange(2, p - 1)
                if sv in roots:
                    continue
                rep = Rep(F, 1, {"x": Lam.g["x"][0], "y": Lam.g["y"][0], "t": F.smul(sv, Lam.g["t"][0])})
                res["h1 at 5 non-roots"].append(cohomology(rep)[0]["h1"])
            rows.append(res)
    out["P_Lambda's roots are the twists with cohomology (mod p)"] = rows
    out["P_Lambda verdict"] = all(all(h >= 1 for h in r["h1 at roots"]) and all(h == 0 for h in r["h1 at 5 non-roots"]) for r in rows)
    # acyclic covers at rational q > 0 (mod p acyclic implies acyclic over Q)
    cov = []
    F = ModP(primes[0], "cov")
    for qq in (sp.Rational(2), sp.Rational(3), sp.Rational(5, 2), sp.Rational(1, 3), sp.Rational(7, 4)):
        mn = mn_mats(F, F.s(qq))
        for nlev in range(1, 7):
            h = cohomology(level_rep(F, mn, nlev, (1, 1, 1)).wedge2())[0]
            cov.append({"q": str(qq), "n": nlev, **h})
    out["Lambda^2 rho_q on M_1..M_6 at five rational q (mod p)"] = {
        "all acyclic": all(r["h0"] == r["h1"] == r["h2"] == 0 for r in cov), "cases": len(cov)}
    return out


# ============================================================================================ the family's identity
def family_checks():
    out = {}
    m, n = ballas_sym()
    mats = {"m": (m, m.inv()), "n": (n, n.inv())}

    def W_(w):
        X = sp.eye(4)
        for ch in w:
            X = X * (mats[ch][0] if ch.islower() else mats[ch.lower()][1])
        return X.applyfunc(sp.cancel)
    out["m004 relator holds over Q(q)"] = W_(RELATOR_MN) == sp.eye(4)
    out["phi is conjugation by m (x, y)"] = [
        (W_("m" + FIBRE_MN[g] + "M") - W_("".join(FIBRE_MN[c] if c.islower() else inv(FIBRE_MN[c.lower()]) for c in PHI[g]))).applyfunc(sp.cancel) == sp.zeros(4)
        for g in "xy"]
    ell_mn = "".join(FIBRE_MN[c] if c.islower() else inv(FIBRE_MN[c.lower()]) for c in ELL)
    out["ell = yXYx is the longitude nMNmmNMn"] = (W_(ell_mn) - W_(LONGITUDE_MN)).applyfunc(sp.cancel) == sp.zeros(4)
    lam = sp.Symbol("lam")
    cp = sp.factor((W_(LONGITUDE_MN) - lam * sp.eye(4)).det())
    out["charpoly of the longitude"] = str(cp)
    out["longitude eigenvalues q, q, q, q^-3"] = sp.simplify(cp - (lam - Qs) ** 3 * (lam - Qs ** -3)) == 0
    out["meridian and longitude commute"] = (W_("m" + LONGITUDE_MN) - W_(LONGITUDE_MN + "m")).applyfunc(sp.cancel) == sp.zeros(4)
    # at q = 1 the family is the complete hyperbolic structure: an invariant form of signature (3, 1)
    m1, n1 = m.subs(Qs, 1), n.subs(Qs, 1)
    Js = sp.symbols("j0:10")
    J = sp.Matrix(4, 4, lambda i, j: Js[min(i, j) * 4 - min(i, j) * (min(i, j) - 1) // 2 + abs(i - j)])
    eqs = list((m1.T * J * m1 - J)) + list((n1.T * J * n1 - J))
    sol = sp.linsolve(eqs, Js)
    (vec,) = list(sol)
    free = sorted(set().union(*[sp.sympify(e).free_symbols for e in vec]), key=str)
    Jsol = J.subs(dict(zip(Js, vec)))
    out["q = 1: invariant symmetric forms (dimension)"] = len(free)
    if len(free) == 1:
        J1 = Jsol.subs(free[0], 1)
        ev = [sp.re(sp.N(e)) for e in J1.eigenvals(multiple=True)]
        sig = (sum(1 for e in ev if e > 0), sum(1 for e in ev if e < 0))
        out["q = 1: signature"] = sorted(sig, reverse=True)
    return out


# ============================================================================================ the run
TRIPLET = [(0, 2), (2, 2), (2, 0)]


def gf_roots(poly, p):
    P = [int(c) % p for c in sp.Poly(poly, Qs).all_coeffs()]
    S = np.arange(p, dtype=np.int64)
    acc = np.zeros(p, dtype=np.int64)
    for cf in P:
        acc = (acc * S + cf) % p
    return [int(r) for r in np.nonzero(acc == 0)[0]]


def sqrt_m1(p):
    for a in range(2, p):
        r = pow(a, (p - 1) // 4, p)
        if r * r % p == p - 1:
            return r
    raise ValueError


def find_primes(poly, need_i, count, start):
    deg = sp.Poly(poly, Qs).degree()
    out, p = [], start
    while len(out) < count:
        p = int(sp.prevprime(p))
        if need_i and p % 4 != 1:
            continue
        if len(gf_roots(poly, p)) == deg:
            out.append(p)
    return out


def main():
    t_all = time.time()
    rec = {"what": "B1513 independent audit: the banked zeros re-derived by the obstruction method, with positive controls",
           "shares code with the instrument": False}
    print("family checks ...", flush=True)
    rec["family"] = family_checks()
    print(json.dumps(rec["family"]), flush=True)

    # ---------------------------------------------------------------- route E (exact)
    print("route E ...", flush=True)
    E = {}
    # population I: Q(q), q^6 - 34 q^3 + 1 = 0
    K6 = sp.QQ.algebraic_field(sp.cbrt(17 + 12 * sp.sqrt(2)))
    F = Exact(K6, "Q(q), q^6 - 34q^3 + 1 = 0")
    assert K6.mod.to_list() == [1, 0, 0, -34, 0, 0, 1]
    q6 = K6.from_sympy(sp.cbrt(17 + 12 * sp.sqrt(2)))
    mn = mn_mats(F, q6)
    one, mone = F.c(1), F.c(-1)
    rows, Ws = [], []
    for (a, b) in TRIPLET:
        tw = (one if a % 4 == 0 else mone, one if b % 4 == 0 else mone, mone)
        r, W = member(F, mn, 3, tw, f"I: nu = ({a}, {b}), lam3 = -1")
        rows.append(r)
        Ws.append(W)
        print(json.dumps(r, default=str), flush=True)
    E["population I"] = rows
    # population II: Q(sqrt 2), q = 17 - 12 sqrt 2, mu = -1, G_1
    K2 = sp.QQ.algebraic_field(sp.sqrt(2))
    F2 = Exact(K2, "Q(sqrt 2)")
    mn2 = mn_mats(F2, K2.from_sympy(17 - 12 * sp.sqrt(2)))
    r, _ = member(F2, mn2, 1, (F2.c(1), F2.c(1), F2.c(-1)), "II: q = 17 - 12 sqrt 2, mu = -1")
    E["population II"] = r
    print(json.dumps(r, default=str), flush=True)
    # C1 and C2: B1510's +-i points (all four conjugate over Q(sqrt 3, i)); one computation, plus its pull-back to G_3
    K12 = sp.QQ.algebraic_field(sp.sqrt(3), sp.I)
    F12 = Exact(K12, "Q(sqrt 3, i)")
    mn12 = mn_mats(F12, K12.from_sympy(7 - 4 * sp.sqrt(3)))
    r, _ = member(F12, mn12, 1, (F12.c(1), F12.c(1), K12.from_sympy(sp.I)), "C1: q = 7 - 4 sqrt 3, mu = i", extra=control_level3)
    E["positive control (+-i)"] = r
    print(json.dumps(r, default=str), flush=True)
    rec["route E"] = E

    # ---------------------------------------------------------------- route P (mod p, every root)
    print("route P ...", flush=True)
    P = {"I": [], "II": [], "C1": [], "invariant forms": []}
    g6 = Qs ** 6 - 34 * Qs ** 3 + 1
    for p in find_primes(g6, False, 3, 2 ** 23):
        F = ModP(p, f"GF({p})")
        for qv in gf_roots(g6, p):
            mn = mn_mats(F, qv)
            Ws_p = []
            for (a, b) in TRIPLET:
                tw = (1 if a % 4 == 0 else p - 1, 1 if b % 4 == 0 else p - 1, p - 1)
                r, W = member(F, mn, 3, tw, f"I: p = {p}, q = {qv}, nu = ({a}, {b})")
                P["I"].append({k: r[k] for k in ("member", "h", "dim H^1(W*), dim H^2(Lambda2 W*)", "B == 0 on H^1(W*)",
                                                   "mu-type pairing == 0", "blocks check (all products)", "B symmetric")})
                Ws_p.append(W)
            if len(P["invariant forms"]) < 4:
                dims, wedge_found = invariant_forms(F, Ws_p)
                P["invariant forms"].append({"p": p, "q": qv, "one form iff i = j = k": all(v == (1 if k == i == j else 0)
                                                                                         for (k, i, j), v in dims.items()),
                                             "the wedge form is invariant at i = j = k": wedge_found,
                                             "dims": {str(key): v for key, v in dims.items()}})
        print(f"  I done at p = {p}", flush=True)
    g2 = Qs ** 2 - 34 * Qs + 1
    for p in find_primes(g2, False, 3, 2 ** 23 - 10 ** 5):
        F = ModP(p, f"GF({p})")
        for qv in gf_roots(g2, p):
            r, _ = member(F, mn_mats(F, qv), 1, (1, 1, p - 1), f"II: p = {p}, q = {qv}")
            P["II"].append({k: r[k] for k in ("member", "h", "B == 0 on H^1(W*)", "mu-type pairing == 0", "blocks check (all products)")})
    g14 = Qs ** 2 - 14 * Qs + 1
    for p in find_primes(g14, True, 3, 2 ** 23 - 2 * 10 ** 5):
        F = ModP(p, f"GF({p})")
        i_ = sqrt_m1(p)
        for qv in gf_roots(g14, p):
            for mu in (i_, p - i_):
                r, _ = member(F, mn_mats(F, qv), 1, (1, 1, mu), f"C1: p = {p}, q = {qv}, mu = {mu}", extra=control_level3)
                P["C1"].append({k: r[k] for k in ("member", "h", "B == 0 on H^1(W*)", "mu-type pairing == 0", "B symmetric",
                                                  "C2: [a_i ^ e f0] pulled back to G_3 non-zero for some i")})
    rec["route P"] = P
    print("bulk checks ...", flush=True)
    rec["bulk (T-HIGGS-BULK-ACYCLIC inputs)"] = bulk_checks(find_primes(g2, False, 2, 2 ** 22))

    # ---------------------------------------------------------------- verdicts
    eI, eII, eC = E["population I"], E["population II"], E["positive control (+-i)"]
    V = {}
    V["Z1 exact: B == 0 at every member of I and at II"] = all(r["B == 0 on H^1(W*)"] for r in eI) and eII["B == 0 on H^1(W*)"]
    V["Z2 exact: mu-type pairing == 0 at I and II"] = all(r["mu-type pairing == 0"] for r in eI) and eII["mu-type pairing == 0"]
    V["Z4 exact: h1(V) = h1(V*) = 1, h1(W*) = 2, h1(L2W) = h1(L2W*) = 1, L2V acyclic"] = all(
        r["h(V)"]["h1"] == 1 and r["h"]["V*"]["h1"] == 1 and r["h"]["W*"]["h1"] == 2 and r["h"]["Lambda2 W"]["h1"] == 1
        and r["h"]["Lambda2 W*"]["h1"] == 1 and r["h"]["Lambda2 V"] == {"h0": 0, "h1": 0, "h2": 0} for r in eI + [eII])
    V["cusp acyclic and blocks consistent everywhere (route E)"] = all(
        all(r["Lambda2 W, Lambda2 W* acyclic on the cusp (det(ell - 1) != 0)"]) and r["blocks check (all products)"]
        and r["relators hold on V"] and r["relators hold on W"] and r["ell commutes with t on W"] for r in eI + [eII, eC])
    V["C1 exact: B != 0 and mu-type pairing != 0 at the +-i points"] = (not eC["B == 0 on H^1(W*)"]) and (not eC["mu-type pairing == 0"])
    V["C2 exact: non-zero after pull-back to G_3"] = eC["C2: [a_i ^ e f0] pulled back to G_3 non-zero for some i"]
    V["C3 exact: symmetric, coboundary-blind, catches a non-cocycle and a random corner"] = all(
        r["B symmetric"] and r["coboundary in either slot changes nothing"] and r["a non-cocycle is caught"]
        and r["a random corner is caught"] for r in eI + [eII, eC])
    V["route P agrees: Z1, Z2 at every prime and root"] = all(r["B == 0 on H^1(W*)"] and r["mu-type pairing == 0"]
                                                              for r in P["I"] + P["II"])
    V["route P agrees: C1, C2 at every prime, root and sign of i"] = all(
        (not r["B == 0 on H^1(W*)"]) and (not r["mu-type pairing == 0"]) and r["B symmetric"]
        and r["C2: [a_i ^ e f0] pulled back to G_3 non-zero for some i"] for r in P["C1"])
    V["Z3 (route P, rigorous): one invariant form iff i = j = k, the wedge form"] = all(
        r["one form iff i = j = k"] and r["the wedge form is invariant at i = j = k"] for r in P["invariant forms"])
    fam = rec["family"]
    V["family: relator, phi, longitude, eigenvalues, hyperbolic at q = 1"] = (
        fam["m004 relator holds over Q(q)"] and all(fam["phi is conjugation by m (x, y)"]) and fam["ell = yXYx is the longitude nMNmmNMn"]
        and fam["longitude eigenvalues q, q, q, q^-3"] and fam["meridian and longitude commute"]
        and fam.get("q = 1: signature") == [3, 1])
    bk = rec["bulk (T-HIGGS-BULK-ACYCLIC inputs)"]
    V["Z4 bulk theorem inputs"] = (bk["s^-3 P = f(s + 1/s) - (w^2 - w)"] and all(bk["f' = 3(u - 3)(u - 5), f(2) = 2, w^2 - w - 2 = (q - 1)^2 (q^2 + q + 1) / q^2"])
                                   and bk["no positive real root"] and bk["P_Lambda verdict"]
                                   and bk["Lambda^2 rho_q on M_1..M_6 at five rational q (mod p)"]["all acyclic"])
    rec["verdicts"] = V
    rec["AUDIT PASSES (the negative is not a bug)"] = all(V.values())
    rec["seconds"] = round(time.time() - t_all, 1)
    return rec


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    RECORD.write_text(txt + "\n", encoding="utf-8")
    print(json.dumps(res["verdicts"], indent=1))
    print("AUDIT PASSES:", res["AUDIT PASSES (the negative is not a bug)"], f"({res['seconds']} s)")
    sys.exit(0 if res["AUDIT PASSES (the negative is not a bug)"] else 1)
