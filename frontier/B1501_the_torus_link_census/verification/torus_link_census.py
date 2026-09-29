"""B1501 -- THE TORUS-LINK CENSUS, run as sealed (PREREGISTRATION.md, sha256 51b6730b...; SEAL_LEDGER 2026-09-29).

Which cones over the four homogeneous nearly Kaehler 6-manifolds, modulo finite groups of their listed automorphisms, have an ADE
locus that is a cone over a torus, of what ADE type and of what shape?

The links, as coset spaces Y = G/K with the normal metric (-1/2 Re tr on G's defining representation) and the canonical J of the
3-symmetric space, J = (2 theta + 1)/sqrt 3 on m = k-perp, theta = Ad of an order-3 element whose centraliser is K:
  S6    = G2 / SU(3)              (G2 = Aut(octonions) on Im O; K = the stabiliser of e1)
  S3xS3 = SU(2)^3 / diag SU(2)    (theta = the cyclic permutation of the factors)
  CP3   = Sp(2) / (U(1) x Sp(1))  (Sp(2) in U(4); K = the stabiliser of the complex line C e1)
  F12   = SU(3) / T^2             (the flag manifold)
The automorphisms used are the sealed list: left translations; for S3xS3 the cyclic permutations sigma, sigma^2; for F12 the right
action of the 3-cycle P and P^2.  Excluded (checked to reverse J): S6's antipodal map, CP3's real structure, the transpositions.

The census (sealed): every conjugacy class of automorphisms gamma of order <= 12 that is a left translation by an element of a
maximal torus (up to the Weyl group, the ineffective centre and the listed outer part), or such a translation composed with a listed
outer element.  For each: the fixed set by damped Newton from 400 random seeds on G; components decided by minimising the distance over
C(gamma)^0 (threshold 1e-6); dimension = dim ker(d gamma - 1) at three points; topology from the C(gamma)^0 orbit; for a torus, the
period lattice, its Gram matrix in the normal metric and the reduced shape tau (hexagonal: |tau - e^{i pi/3}| < 1e-9 up to
reflection); H_F, the full pointwise stabiliser, fixing three generic points and checked on 20; its action on the normal space in Y's J.

The banked identity is run first and must pass before any census number is read (see main()).
"""
import hashlib
import itertools
import json
import sys
import time
from fractions import Fraction
from math import gcd
from pathlib import Path

import numpy as np
import sympy
from sympy.matrices.normalforms import hermite_normal_form

HERE = Path(__file__).resolve().parent
SEALED_SHA256 = "51b6730bd362e34656d3dfb2697e46af91a9f6c95739986bb7885997e5ac345d"
N_SEEDS = 400                 # sealed
COMP_TOL = 1e-6               # sealed: one component when the distance minimised over C(gamma)^0 is below this
HEX_TOL = 1e-9                # sealed
CONV_TOL = 1e-11              # a Newton seed counts as a fixed point when its residual is below this
N_CLUSTER_STARTS = 16         # random starts on C(gamma)^0 per distance minimisation
N_HF_SEEDS = 200              # seeds for the discrete part of H_F
MAX_ORDER = 12                # sealed
OMEGA = np.exp(2j * np.pi / 3)
SQ3 = np.sqrt(3.0)


# ---------------------------------------------------------------------------------------------------------------- linear algebra
def dag(g):
    return np.conj(np.swapaxes(g, -1, -2))


def ip(X, Y):
    """the normal inner product -1/2 Re tr(XY) on the Lie algebra (batched over leading axes)"""
    return -0.5 * np.real(np.trace(X @ Y, axis1=-2, axis2=-1))


def orthonormal(mats, tol=1e-9):
    out = []
    for M in mats:
        V = np.array(M, dtype=complex)
        for _ in range(2):
            for B in out:
                V = V - ip(B, V) * B
        nrm = np.sqrt(max(ip(V, V), 0.0))
        if nrm > tol:
            out.append(V / nrm)
    return out


def coords(X, basis):
    return np.stack([ip(B, X) for B in basis], axis=-1)


def from_coords(c, basis):
    c = np.asarray(c)
    return np.tensordot(c, np.array(basis), axes=([-1], [0]))


def expm_skew(X):
    """exp of skew-Hermitian (or real skew) matrices, batched, via the Hermitian eigendecomposition of iX"""
    H = 1j * X
    H = 0.5 * (H + dag(H))
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * w)[..., None, :]) @ dag(V)


def null_space(M, tol=1e-9):
    """orthonormal basis (columns) of the null space of M, with a relative tolerance"""
    M = np.atleast_2d(M)
    if M.shape[0] == 0:
        return np.eye(M.shape[1])
    u, s, vh = np.linalg.svd(M)
    scale = max(s[0] if len(s) else 0.0, 1.0)
    rank = int(np.sum(s > tol * scale))
    return vh[rank:].conj().T


def rank_of(M, tol=1e-8):
    M = np.atleast_2d(M)
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * max(s[0], 1.0)))


# ------------------------------------------------------------------------------------------------------------------- the links
class Link:
    """Y = G/K. Subclasses set: name, n (matrix size), g_basis, k_basis, m_basis, the torus (r, torus(q), H), Weyl generators on q,
    Z0 (ineffective centre, as q-vectors), outer_q (the listed outer part acting on torus classes), the embedding and its derivative,
    theta_elem (the order-3 element whose Ad is the 3-symmetry, or None when theta is an outer automorphism), outer elements."""

    def finish(self):
        self.g_basis = orthonormal(self.g_basis)
        self.k_basis = orthonormal(self.k_basis)
        # m = k-perp inside g
        comp = []
        for B in self.g_basis:
            comp.append(B - from_coords(coords(B, self.k_basis), self.k_basis))
        self.m_basis = orthonormal(comp)
        assert len(self.m_basis) == 6 and len(self.k_basis) + 6 == len(self.g_basis), (self.name, len(self.m_basis))
        self.G = np.array(self.g_basis)
        self.Mb = np.array(self.m_basis)
        self.Kb = np.array(self.k_basis)
        self.J = self.canonical_J()

    # ---- group elements
    def random_elements(self, rng, size, basis=None, spread=2.5):
        basis = self.g_basis if basis is None else basis
        B = np.array(basis)
        g = np.broadcast_to(np.eye(self.n, dtype=complex), (size, self.n, self.n)).copy()
        for _ in range(3):
            c = rng.normal(0, spread, (size, len(basis)))
            g = g @ expm_skew(np.tensordot(c, B, axes=([1], [0])))
        return g

    def Ad_matrix(self, g, basis_from, basis_to=None):
        """matrix of X -> g X g^-1 from basis_from coordinates to basis_to coordinates"""
        basis_to = basis_from if basis_to is None else basis_to
        imgs = [g @ B @ dag(g) for B in basis_from]
        return np.array([[ip(Bt, Xi) for Xi in imgs] for Bt in basis_to])

    def canonical_J(self):
        """J = (2 theta + 1)/sqrt 3 on m, theta the 3-symmetry"""
        Th = np.array([[ip(Bt, self.theta_lie(B)) for B in self.m_basis] for Bt in self.m_basis])
        return (2 * Th + np.eye(6)) / SQ3

    # ---- automorphisms: ('left', a) / ('aut', a, sigma) / ('right', a, n)
    def act(self, gam, g):
        kind = gam[0]
        a = gam[1]
        if kind == "left":
            return a @ g
        if kind == "aut":
            return a @ gam[2]["group"](g)
        if kind == "right":
            return a @ g @ gam[2]
        raise ValueError(kind)

    def transport(self, gam, X):
        """the Lie-algebra map carrying a right perturbation of g to one of act(gam, g)"""
        kind = gam[0]
        if kind == "left":
            return X
        if kind == "aut":
            return gam[2]["lie"](X)
        n = gam[2]
        return dag(n) @ X @ n

    def gamma_on_g(self, gam, X):
        """the conjugation action of gam on left translations: L_c -> L_{gam(c)}, on the Lie algebra"""
        kind = gam[0]
        a = gam[1]
        if kind == "aut":
            X = gam[2]["lie"](X)
        return a @ X @ dag(a)

    def centraliser_basis(self, gam):
        M = np.array([[ip(Bt, self.gamma_on_g(gam, B)) for B in self.g_basis] for Bt in self.g_basis]) - np.eye(len(self.g_basis))
        N = null_space(M, 1e-9)
        return orthonormal([from_coords(N[:, j].real, self.g_basis) for j in range(N.shape[1])])

    def differential(self, gam, g):
        """d gamma at a fixed point gK, as a 6x6 matrix on m (coordinates in m_basis)"""
        k = dag(g) @ self.act(gam, g)
        imgs = [k @ self.transport(gam, B) @ dag(k) for B in self.m_basis]
        return np.array([[ip(Bt, Xi) for Xi in imgs] for Bt in self.m_basis])

    # ---- the fixed-point equation
    def residual(self, gam, g):
        return self.embed(self.act(gam, g)) - self.embed(g)

    def jacobian(self, gam, g):
        gp = self.act(gam, g)
        cols = [self.dembed(gp, self.transport(gam, B)) - self.dembed(g, B) for B in self.m_basis]
        return np.stack(cols, axis=-1)


def realflat(M, k):
    """flatten the last k axes of a complex array and split real and imaginary parts"""
    M = np.asarray(M)
    f = M.reshape(M.shape[:M.ndim - k] + (-1,))
    return np.concatenate([f.real, f.imag], axis=-1)


# ---------------------------------------------------------------------------------------------------------------------- S^6
TRIPLES = [(1, 2, 3), (1, 4, 5), (1, 7, 6), (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 6, 5)]
CROSS = np.zeros((7, 7, 7))
for (_a, _b, _c) in TRIPLES:
    for (_x, _y, _z) in [(_a, _b, _c), (_b, _c, _a), (_c, _a, _b)]:
        CROSS[_x - 1, _y - 1, _z - 1] = 1.0
        CROSS[_y - 1, _x - 1, _z - 1] = -1.0


def cross(u, v):
    return np.einsum("...i,...j,ijk->...k", u, v, CROSS)


class S6(Link):
    name = "S6"
    n = 7
    r = 2

    def __init__(self):
        so7 = []
        for i, j in itertools.combinations(range(7), 2):
            E = np.zeros((7, 7))
            E[i, j], E[j, i] = 1.0, -1.0
            so7.append(E)
        # derivations of the cross product: D(u x v) = Du x v + u x Dv
        rows = []
        for E in so7:
            d = np.einsum("lk,ijk->ijl", E, CROSS) - np.einsum("mi,mjl->ijl", E, CROSS) - np.einsum("mj,iml->ijl", E, CROSS)
            rows.append(d.reshape(-1))
        N = null_space(np.array(rows).T, 1e-10)
        assert N.shape[1] == 14, N.shape
        self.g_basis = [sum(N[a, j] * so7[a] for a in range(21)).astype(complex) for j in range(14)]
        e1 = np.zeros(7)
        e1[0] = 1.0
        C = np.array([(B @ e1).real for B in orthonormal(self.g_basis)])
        Nk = null_space(C.T, 1e-10)
        gb = orthonormal(self.g_basis)
        self.k_basis = [sum(Nk[a, j] * gb[a] for a in range(14)) for j in range(Nk.shape[1])]
        assert len(self.k_basis) == 8
        # the J1-unitary frame of e1-perp: f1 = e2 (J f1 = e3), f2 = e4 (J f2 = e5), f3 = e7 (J f3 = e6)
        self.frame = [(1, 2), (3, 4), (6, 5)]
        self.H = []
        for s in range(2):
            Hm = np.zeros((7, 7))
            for j, sign in ((s, 1.0), (2, -1.0)):
                a, b = self.frame[j]
                Hm[b, a] += sign           # f -> J f
                Hm[a, b] -= sign
            self.H.append(Hm.astype(complex))
        self.weyl = self._weyl()
        self.Z0 = [(Fraction(0), Fraction(0))]
        self.outer_q = []
        self.z3 = self.torus((Fraction(1, 3), Fraction(1, 3)))
        self.outer = {}
        self.finish()
        # the antipodal element: exp(pi X), X in m with |X e1| = 1
        X = self.m_basis[0]
        X = X / np.linalg.norm((X @ e1))
        self.antipodal = expm_skew(np.pi * X)
        self.excluded = {"antipodal map (right N(SU(3))/SU(3))": ("right", self.antipodal)}

    def torus(self, q):
        q1, q2 = (float(x) for x in q)
        ang = [2 * np.pi * q1, 2 * np.pi * q2, -2 * np.pi * (q1 + q2)]
        t = np.eye(7, dtype=complex)
        for (a, b), phi in zip(self.frame, ang):
            c, s = np.cos(phi), np.sin(phi)
            t[a, a], t[b, b], t[b, a], t[a, b] = c, c, s, -s
        return t

    def _weyl(self):
        # q -> (q1, q2), q3 = -q1 - q2; S3 permutations and the sign
        def perm(p):
            def f(q):
                full = (q[0], q[1], -q[0] - q[1])
                return (full[p[0]], full[p[1]])
            return f
        gens = [perm(p) for p in itertools.permutations(range(3))]
        return gens + [lambda q, f=f: tuple(-x for x in f(q)) for f in gens]

    def theta_lie(self, X):
        return self.z3 @ X @ dag(self.z3)

    def embed(self, g):
        v = g[..., :, 0]
        return np.concatenate([v.real, v.imag], axis=-1)

    def dembed(self, g, Y):
        v = (g @ Y)[..., :, 0]
        return np.concatenate([v.real, v.imag], axis=-1)


# ------------------------------------------------------------------------------------------------------------------- S3 x S3
PAULI = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]


def blockdiag3(a, b, c):
    Z = np.zeros(a.shape[:-2] + (6, 6), dtype=complex)
    Z[..., 0:2, 0:2], Z[..., 2:4, 2:4], Z[..., 4:6, 4:6] = a, b, c
    return Z


def blocks(g):
    return g[..., 0:2, 0:2], g[..., 2:4, 2:4], g[..., 4:6, 4:6]


def perm_blocks(g, p):
    """(g_{p(0)}, g_{p(1)}, g_{p(2)}) as a block matrix"""
    b = blocks(g)
    return blockdiag3(b[p[0]], b[p[1]], b[p[2]])


class S3xS3(Link):
    name = "S3xS3"
    n = 6
    r = 3

    def __init__(self):
        Z2 = np.zeros((2, 2), dtype=complex)
        self.g_basis = []
        for j in range(3):
            for s in PAULI:
                parts = [Z2, Z2, Z2]
                parts[j] = 1j * s
                self.g_basis.append(blockdiag3(*parts))
        self.k_basis = [blockdiag3(1j * s, 1j * s, 1j * s) for s in PAULI]
        sig = {"group": lambda g: perm_blocks(g, (2, 0, 1)), "lie": lambda X: perm_blocks(X, (2, 0, 1))}     # (g3, g1, g2)
        sig2 = {"group": lambda g: perm_blocks(g, (1, 2, 0)), "lie": lambda X: perm_blocks(X, (1, 2, 0))}
        self.outer = {"sigma": sig, "sigma^2": sig2}
        self.excluded = {"transposition (12)": ("aut", np.eye(6, dtype=complex),
                                                {"group": lambda g: perm_blocks(g, (1, 0, 2)),
                                                 "lie": lambda X: perm_blocks(X, (1, 0, 2))}),
                         "transposition (23)": ("aut", np.eye(6, dtype=complex),
                                                {"group": lambda g: perm_blocks(g, (0, 2, 1)),
                                                 "lie": lambda X: perm_blocks(X, (0, 2, 1))})}
        self.H = [blockdiag3(*[(np.diag([1j, -1j]) if i == j else Z2) for i in range(3)]) for j in range(3)]
        self.weyl = [lambda q, s=s: tuple(x * e for x, e in zip(q, s)) for s in itertools.product((1, -1), repeat=3)]
        self.Z0 = [(Fraction(0),) * 3, (Fraction(1, 2),) * 3]
        self.outer_q = [lambda q: (q[2], q[0], q[1]), lambda q: (q[1], q[2], q[0])]     # conjugation by sigma^{+-1}
        self.finish()

    def torus(self, q):
        d = [np.diag([np.exp(2j * np.pi * float(x)), np.exp(-2j * np.pi * float(x))]) for x in q]
        return blockdiag3(*d)

    def theta_lie(self, X):
        return self.outer["sigma"]["lie"](X)

    def embed(self, g):
        g1, g2, g3 = blocks(g)
        A, B = g1 @ dag(g2), g2 @ dag(g3)
        f = np.concatenate([A.reshape(A.shape[:-2] + (4,)), B.reshape(B.shape[:-2] + (4,))], axis=-1)
        return np.concatenate([f.real, f.imag], axis=-1)

    def dembed(self, g, Y):
        g1, g2, g3 = blocks(g)
        Y1, Y2, Y3 = blocks(np.broadcast_to(Y, g.shape))
        A, B = g1 @ (Y1 - Y2) @ dag(g2), g2 @ (Y2 - Y3) @ dag(g3)
        f = np.concatenate([A.reshape(A.shape[:-2] + (4,)), B.reshape(B.shape[:-2] + (4,))], axis=-1)
        return np.concatenate([f.real, f.imag], axis=-1)


# ---------------------------------------------------------------------------------------------------------------------- CP^3
OMEGA4 = np.block([[np.zeros((2, 2)), np.eye(2)], [-np.eye(2), np.zeros((2, 2))]]).astype(complex)


class CP3(Link):
    name = "CP3"
    n = 4
    r = 2

    def __init__(self):
        u4 = []
        for i in range(4):
            E = np.zeros((4, 4), dtype=complex)
            E[i, i] = 1j
            u4.append(E)
        for i, j in itertools.combinations(range(4), 2):
            E = np.zeros((4, 4), dtype=complex)
            E[i, j], E[j, i] = 1, -1
            u4.append(E)
            F = np.zeros((4, 4), dtype=complex)
            F[i, j], F[j, i] = 1j, 1j
            u4.append(F)
        rows = [realflat(E.T @ OMEGA4 + OMEGA4 @ E, 2) for E in u4]
        N = null_space(np.array(rows).T, 1e-10)
        assert N.shape[1] == 10
        self.g_basis = [sum(N[a, j] * u4[a] for a in range(16)) for j in range(10)]
        gb = orthonormal(self.g_basis)
        C = np.array([realflat((B @ np.eye(4)[:, 0])[1:], 1) for B in gb])
        Nk = null_space(C.T, 1e-10)
        self.k_basis = [sum(Nk[a, j] * gb[a] for a in range(10)) for j in range(Nk.shape[1])]
        assert len(self.k_basis) == 4, len(self.k_basis)
        self.P0 = np.zeros((4, 4), dtype=complex)
        self.P0[0, 0] = 1
        self.H = [np.diag([1j, 0, -1j, 0]), np.diag([0, 1j, 0, -1j])]
        self.weyl = [lambda q, p=p, s=s: tuple(q[p[i]] * s[i] for i in range(2))
                     for p in itertools.permutations(range(2)) for s in itertools.product((1, -1), repeat=2)]
        self.Z0 = [(Fraction(0),) * 2, (Fraction(1, 2),) * 2]
        self.outer_q = []
        self.outer = {}
        self.z3 = self.torus((Fraction(1, 3), Fraction(0)))
        self.finish()
        n = np.zeros((4, 4), dtype=complex)
        n[0, 2], n[1, 1], n[2, 0], n[3, 3] = -1, 1, 1, 1
        self.realstr = n
        self.excluded = {"real structure (right N(K)/K)": ("right", n)}

    def torus(self, q):
        a, b = (2 * np.pi * float(x) for x in q)
        return np.diag([np.exp(1j * a), np.exp(1j * b), np.exp(-1j * a), np.exp(-1j * b)])

    def theta_lie(self, X):
        return self.z3 @ X @ dag(self.z3)

    def embed(self, g):
        return realflat(g @ self.P0 @ dag(g), 2)

    def dembed(self, g, Y):
        Y = np.broadcast_to(Y, g.shape)
        return realflat(g @ (Y @ self.P0 - self.P0 @ Y) @ dag(g), 2)


# ---------------------------------------------------------------------------------------------------------------------- F_{1,2}
class F12(Link):
    name = "F12"
    n = 3
    r = 2

    def __init__(self):
        su3 = []
        for i in range(2):
            E = np.zeros((3, 3), dtype=complex)
            E[i, i], E[i + 1, i + 1] = 1j, -1j
            su3.append(E)
        off = []
        for i, j in itertools.combinations(range(3), 2):
            E = np.zeros((3, 3), dtype=complex)
            E[i, j], E[j, i] = 1, -1
            F = np.zeros((3, 3), dtype=complex)
            F[i, j], F[j, i] = 1j, 1j
            off += [E, F]
        self.g_basis = su3 + off
        self.k_basis = su3
        self.H0 = np.diag([1.0, 0.0, -1.0]).astype(complex)
        self.H = [np.diag([1j, 0, -1j]), np.diag([0, 1j, -1j])]
        self.weyl = []
        for p in itertools.permutations(range(3)):
            def f(q, p=p):
                full = (q[0], q[1], -q[0] - q[1])
                return (full[p[0]], full[p[1]])
            self.weyl.append(f)
        self.Z0 = [(Fraction(0), Fraction(0)), (Fraction(1, 3), Fraction(1, 3)), (Fraction(2, 3), Fraction(2, 3))]
        self.outer_q = []
        P = np.zeros((3, 3), dtype=complex)
        P[1, 0], P[2, 1], P[0, 2] = 1, 1, 1                                   # e1 -> e2 -> e3 -> e1, det +1
        self.P = P
        self.outer = {"R_P": P, "R_P^2": P @ P}
        s = np.zeros((3, 3), dtype=complex)
        s[0, 1], s[1, 0], s[2, 2] = 1, 1, -1                                  # the transposition (12), det +1
        self.excluded = {"right transposition (12)": ("right", s), "right transposition (23)": ("right", P @ s @ dag(P))}
        self.z3 = self.torus((Fraction(0), Fraction(1, 3)))
        self.finish()

    def torus(self, q):
        a, b = (2 * np.pi * float(x) for x in q)
        return np.diag([np.exp(1j * a), np.exp(1j * b), np.exp(-1j * (a + b))])

    def theta_lie(self, X):
        return self.z3 @ X @ dag(self.z3)

    def embed(self, g):
        return realflat(g @ self.H0 @ dag(g), 2)

    def dembed(self, g, Y):
        Y = np.broadcast_to(Y, g.shape)
        return realflat(g @ (Y @ self.H0 - self.H0 @ Y) @ dag(g), 2)


# ------------------------------------------------------------------------------------------------------------- automorphisms
def gamma_of(link, cls):
    """the automorphism of a census class: ('left', t) or a twisted one"""
    t = link.torus(cls["q"])
    if cls["outer"] is None:
        return ("left", t)
    if link.name == "S3xS3":
        return ("aut", t, link.outer[cls["outer"]])
    if link.name == "F12":
        return ("right", t, link.outer[cls["outer"]])
    raise ValueError(cls)


def frac_mod1(x):
    x = Fraction(x)
    return x - (x.numerator // x.denominator)


def canon_q(q):
    return tuple(frac_mod1(x) for x in q)


def left_order(link, q):
    for m in range(1, 1000):
        mq = canon_q(tuple(m * x for x in q))
        if any(mq == canon_q(z) for z in link.Z0):
            return m
    raise ValueError(q)


def class_key(link, q):
    """canonical representative of a torus element under W, the ineffective centre and the listed outer part"""
    best = None
    frontier = [canon_q(q)]
    seen = set(frontier)
    while frontier:
        new = []
        for x in frontier:
            imgs = [canon_q(w(x)) for w in link.weyl] + [canon_q(o(x)) for o in link.outer_q]
            imgs += [canon_q(tuple(a + b for a, b in zip(x, z))) for z in link.Z0]
            for y in imgs:
                if y not in seen:
                    seen.add(y)
                    new.append(y)
        frontier = new
    best = min(seen)
    return best


def enumerate_classes(link):
    """the sealed element list for one link"""
    left = {}
    for m in range(1, MAX_ORDER + 1):
        for z in link.Z0:
            for nvec in itertools.product(range(m), repeat=len(z)):
                q = canon_q(tuple(Fraction(zz + nn, m) for zz, nn in zip(z, nvec)))
                o = left_order(link, q)
                if o > MAX_ORDER:
                    continue
                key = class_key(link, q)
                left.setdefault(key, o)
    classes = []
    for key, o in sorted(left.items(), key=lambda kv: (kv[1], kv[0])):
        if o == 1:
            continue
        classes.append({"link": link.name, "q": key, "outer": None, "order": o})
    if link.name == "S3xS3":
        seen = set()
        for j in range(24):
            kappa = Fraction(j, 24)
            m2 = left_order_scalar(2 * kappa)
            order = 3 * m2
            if order > MAX_ORDER:
                continue
            c = frac_mod1(kappa) % Fraction(1, 2)
            c = min(c, Fraction(1, 2) - c)
            if c in seen:
                continue
            seen.add(c)
            for o in ("sigma", "sigma^2"):
                classes.append({"link": link.name, "q": (Fraction(0), Fraction(0), c), "outer": o, "order": order})
    if link.name == "F12":
        for key, o in sorted(left.items(), key=lambda kv: (kv[1], kv[0])):
            order = o * 3 // gcd(o, 3)
            if order > MAX_ORDER:
                continue
            for oo in ("R_P", "R_P^2"):
                classes.append({"link": link.name, "q": key, "outer": oo, "order": order})
    return classes


def left_order_scalar(x):
    x = frac_mod1(x)
    return x.denominator


def class_label(cls):
    q = ",".join(str(x) for x in cls["q"])
    return "%s L(%s)%s" % (cls["link"], q, "" if cls["outer"] is None else " o " + cls["outer"])


def label_seed(label):
    return int(hashlib.sha256(label.encode()).hexdigest()[:8], 16)


# ------------------------------------------------------------------------------------------------ the structures (banked identity)
def transport_on_m(link, elem):
    """the 6x6 matrix on m of an automorphism type that fixes the base point: ('aut', 1, sigma) -> d sigma, ('right', n) -> Ad n^-1"""
    kind = elem[0]
    if kind == "aut":
        f = elem[2]["lie"]
    else:
        n = elem[1]
        f = lambda X: dag(n) @ X @ n                                          # noqa: E731
    return np.array([[ip(Bt, f(B)) for B in link.m_basis] for Bt in link.m_basis])


def structure_checks(link, rng):
    """J^2 = -1 and J orthogonal; J Ad(K)-invariant (every left translation preserves J); the listed outer elements preserve J (and the
    metric, hence omega); the excluded ones reverse J.  Returns a record; asserts."""
    J = link.J
    rec = {"J^2+1": float(np.abs(J @ J + np.eye(6)).max()), "J orthogonal": float(np.abs(J.T @ J - np.eye(6)).max())}
    worst = 0.0
    for k in link.random_elements(rng, 20, basis=link.k_basis):
        A = link.Ad_matrix(k, link.m_basis)
        worst = max(worst, np.abs(A @ J - J @ A).max(), np.abs(A.T @ A - np.eye(6)).max())
    rec["Ad(K) commutes with J"] = float(worst)
    rec["theta order 3 on m"] = float(np.abs(np.linalg.matrix_power((SQ3 * J - np.eye(6)) / 2, 3) - np.eye(6)).max())
    listed, excluded = {}, {}
    for name, o in link.outer.items():
        elem = ("aut", None, o) if isinstance(o, dict) else ("right", o)
        D = transport_on_m(link, elem)
        listed[name] = {"D J - J D": float(np.abs(D @ J - J @ D).max()), "orthogonal": float(np.abs(D.T @ D - np.eye(6)).max())}
        assert listed[name]["D J - J D"] < 1e-12 and listed[name]["orthogonal"] < 1e-12, (link.name, name, listed[name])
    for name, e in link.excluded.items():
        elem = ("aut", None, e[2]) if e[0] == "aut" else ("right", e[1])
        if e[0] == "right":
            n = e[1]
            # n normalises K
            worst_n = max(np.abs(coords(n @ B @ dag(n), link.m_basis)).max() for B in link.k_basis)
            assert worst_n < 1e-12, (link.name, name, worst_n)
        D = transport_on_m(link, elem)
        excluded[name] = {"D J + J D": float(np.abs(D @ J + J @ D).max())}
        assert excluded[name]["D J + J D"] < 1e-12, (link.name, name, excluded[name])
    rec["listed outer elements preserve J"] = listed
    rec["excluded elements reverse J"] = excluded
    assert rec["J^2+1"] < 1e-12 and rec["J orthogonal"] < 1e-12 and rec["Ad(K) commutes with J"] < 1e-12, (link.name, rec)
    assert rec["theta order 3 on m"] < 1e-12
    # the torus generators: exp(2 pi sum q_i H_i) = torus(q), in G and with the lattice Z^r
    for _ in range(5):
        q = rng.uniform(-1, 1, link.r)
        X = 2 * np.pi * sum(qi * Hi for qi, Hi in zip(q, link.H))
        assert np.abs(expm_skew(X) - link.torus(q)).max() < 1e-12
        assert np.abs(coords(X, link.g_basis) @ np.array([B for B in link.g_basis]).reshape(len(link.g_basis), -1)
                      - X.reshape(-1)).max() < 1e-12                                      # H in Lie(G)
    return rec


def s6_cross_product_check(link, rng):
    """the coset J against J_x(v) = x cross v, and G2 = the automorphisms of the cross product"""
    e1 = np.zeros(7)
    e1[0] = 1
    worst_aut, worst_J, sign = 0.0, 0.0, None
    for g in link.random_elements(rng, 30):
        g = g.real
        u, v = rng.normal(size=7), rng.normal(size=7)
        worst_aut = max(worst_aut, np.abs(g @ cross(u, v) - cross(g @ u, g @ v)).max())
        x = g @ e1
        for B, JB in zip(link.m_basis, from_coords(link.J.T, link.m_basis)):
            tang = (g @ B.real @ e1)
            Jtang = (g @ JB.real @ e1)
            c = cross(x, tang)
            if sign is None:
                sign = 1.0 if np.dot(c, Jtang) > 0 else -1.0
            worst_J = max(worst_J, np.abs(sign * c - Jtang).max())
    for q in [(0.1, 0.27), (1 / 3, 1 / 3)]:
        t = link.torus(q).real
        u, v = rng.normal(size=7), rng.normal(size=7)
        worst_aut = max(worst_aut, np.abs(t @ cross(u, v) - cross(t @ u, t @ v)).max())
    assert worst_aut < 1e-12 and worst_J < 1e-12, (worst_aut, worst_J)
    return {"G2 preserves the cross product": float(worst_aut), "coset J = %+d x (x cross .)" % sign: float(worst_J)}


# ----------------------------------------------------------------------------------------------------------------- the solver
def newton_fixed(link, gam, g, iters=80):
    """damped Gauss-Newton (minimum-norm steps) for gamma(gK) = gK from a batch of seeds; returns (g, residual norms)"""
    g = g.copy()
    R = link.residual(gam, g)
    res = np.linalg.norm(R, axis=-1)
    for _ in range(iters):
        active = res > 1e-14
        if not active.any():
            break
        Jm = link.jacobian(gam, g[active])
        step = -np.einsum("bij,bj->bi", np.linalg.pinv(Jm, rcond=1e-10), R[active])
        X = from_coords(step, link.m_basis)
        alpha = np.ones(active.sum())
        g_act, r_act = g[active], res[active]
        new_g = g_act @ expm_skew(X)
        new_res = np.linalg.norm(link.residual(gam, new_g), axis=-1)
        for _h in range(12):
            bad = new_res >= r_act
            if not bad.any():
                break
            alpha[bad] *= 0.5
            new_g[bad] = g_act[bad] @ expm_skew(alpha[bad][:, None, None] * X[bad])
            new_res[bad] = np.linalg.norm(link.residual(gam, new_g[bad]), axis=-1)
        keep = new_res < r_act
        idx = np.where(active)[0]
        g[idx[keep]] = new_g[keep]
        res[idx[keep]] = new_res[keep]
        R = link.residual(gam, g)
        res = np.linalg.norm(R, axis=-1)
        if not keep.any():
            break
    return g, res


def c_orbit_distance(link, cbasis, rep, others, rng, starts=N_CLUSTER_STARTS, iters=40):
    """min over c in C(gamma)^0 of |Phi(c rep) - Phi(other)|, for a batch of others (each from several random starts)"""
    m = len(others)
    target = link.embed(others)
    if len(cbasis) == 0:
        return np.linalg.norm(link.embed(rep) - target, axis=-1)
    Cb = np.array(cbasis)
    B = m * starts
    c = link.random_elements(rng, B, basis=cbasis, spread=3.0)
    tgt = np.repeat(target, starts, axis=0)
    for _ in range(iters):
        x = c @ rep
        R = link.embed(x) - tgt
        cols = [link.dembed(x, dag(x) @ Z @ x) for Z in cbasis]
        Jm = np.stack(cols, axis=-1)
        step = -np.einsum("bij,bj->bi", np.linalg.pinv(Jm, rcond=1e-10), R)
        c = expm_skew(np.tensordot(step, Cb, axes=([1], [0]))) @ c
    d = np.linalg.norm(link.embed(c @ rep) - tgt, axis=-1).reshape(m, starts)
    return d.min(axis=1)


def cluster_components(link, gam, sols, rng):
    cbasis = link.centraliser_basis(gam)
    unassigned = list(range(len(sols)))
    comps = []
    while unassigned:
        r = unassigned[0]
        rest = unassigned[1:]
        members = [r]
        if rest:
            d = c_orbit_distance(link, cbasis, sols[r], sols[rest], rng)
            members += [i for i, di in zip(rest, d) if di < COMP_TOL]
        comps.append(members)
        unassigned = [i for i in unassigned if i not in set(members)]
    return comps, cbasis


# -------------------------------------------------------------------------------------------------------- component analysis
def lie_structure(link, cbasis):
    """dim, rank, dim of the derived algebra of c; and bracket coordinates"""
    d = len(cbasis)
    if d == 0:
        return {"dim": 0, "rank": 0, "derived": 0}
    br = np.array([[coords(A @ B - B @ A, cbasis) for B in cbasis] for A in cbasis])     # d x d x d
    derived = rank_of(br.reshape(d * d, d))
    x = np.random.default_rng(7).normal(size=d)
    adx = np.einsum("a,abc->bc", x, br).T                                                  # (ad x) in c-coordinates
    rank = d - rank_of(adx)
    return {"dim": d, "rank": rank, "derived": derived}


def centraliser_name(s):
    table = {(0, 0, 0): "trivial", (1, 1, 0): "U(1)", (2, 2, 0): "T2", (3, 3, 0): "T3", (3, 1, 3): "SU(2)",
             (4, 2, 3): "U(2)", (5, 3, 3): "SU(2) x T2", (6, 2, 6): "SU(2) x SU(2)", (7, 3, 6): "SU(2)^2 x U(1)",
             (8, 2, 8): "SU(3)", (9, 3, 9): "SU(2)^3", (10, 2, 10): "Sp(2)", (14, 2, 14): "G2"}
    return table.get((s["dim"], s["rank"], s["derived"]), "dim %d rank %d derived %d" % (s["dim"], s["rank"], s["derived"]))


def orbit_map(link, g, basis):
    """X -> the m-coordinates of the vector field of X at gK"""
    return np.array([coords(dag(g) @ X @ g, link.m_basis) for X in basis]).T                  # 6 x len(basis)


def largest_ideal(cb, s_coords):
    """the largest ideal of c inside the subspace s (given by coordinate columns in c)"""
    d = cb.shape[0]
    S = s_coords
    while S.shape[1] > 0:
        # X in S with [Z_a, X] in S for all a
        P = np.eye(d) - S @ np.linalg.pinv(S)
        rows = []
        for a in range(d):
            ad_a = cb[a].T                                                                # column j: [Z_a, Z_j] in c-coordinates
            rows.append(P @ ad_a @ S)
        N = null_space(np.vstack(rows), 1e-9)
        if N.shape[1] == S.shape[1]:
            return S
        S = S @ N
    return S


def topology(link, g, cbasis):
    d = len(cbasis)
    A = orbit_map(link, g, cbasis) if d else np.zeros((6, 0))
    odim = rank_of(A) if d else 0
    if d == 0:
        return {"orbit_dim": 0, "type": "point"}
    S = null_space(A, 1e-9)                                                                 # stabiliser algebra in c-coordinates
    br = np.array([[coords(X @ Y - Y @ X, cbasis) for Y in cbasis] for X in cbasis])
    I = largest_ideal(br, S)
    eff, eff_stab = d - I.shape[1], S.shape[1] - I.shape[1]
    Pc = np.eye(d) - (I @ np.linalg.pinv(I) if I.shape[1] else 0)
    brq = np.einsum("ij,abj->abi", Pc, br)                                                  # brackets modulo the ideal
    derived_eff = rank_of(brq.reshape(d * d, d))
    abelian = derived_eff == 0
    if odim == 0:
        typ = "point"
    elif odim == 2 and abelian and eff == 2 and eff_stab == 0:
        typ = "torus"
    elif odim == 2 and eff == 3 and derived_eff == 3 and eff_stab == 1:
        typ = "sphere"
    else:
        typ = "other"
    return {"orbit_dim": odim, "effective_dim": eff, "effective_stabiliser_dim": eff_stab, "effective_derived": derived_eff,
            "type": typ}


def rationalise(x, maxden=720, tol=1e-9):
    f = Fraction(float(x)).limit_denominator(maxden)
    assert abs(float(f) - x) < tol, (x, f)
    return f


def torus_q_subspace(link, gam):
    """Q_c = {q : sum q_i H_i in c(gamma)} as an integer basis (columns), from the (integer) action of gamma on Lie(T)"""
    r = link.r
    M = np.zeros((len(link.g_basis), r))
    for i, Hi in enumerate(link.H):
        M[:, i] = coords(link.gamma_on_g(gam, Hi) - Hi, link.g_basis)
    # express the image back in H-coordinates when it lies in Lie(T); otherwise use the g-coordinates directly
    Mq = sympy.Matrix([[rationalise(v, 60, 1e-9) for v in row] for row in M])
    ns = Mq.nullspace()
    cols = []
    for v in ns:
        den = sympy.ilcm(*[sympy.fraction(sympy.nsimplify(x))[1] for x in v]) if len(v) else 1
        w = [int(sympy.nsimplify(x) * den) for x in v]
        g0 = 0
        for x in w:
            g0 = gcd(g0, abs(x))
        cols.append([x // g0 for x in w])
    return np.array(cols, dtype=int).T if cols else np.zeros((r, 0), dtype=int)


def hnf_2d(vectors):
    """a basis of the lattice generated by rational 2-vectors (Fractions)"""
    vecs = [tuple(Fraction(x) for x in v) for v in vectors if any(x != 0 for x in v)]
    den = 1
    for v in vecs:
        for x in v:
            den = den * x.denominator // gcd(den, x.denominator)
    M = sympy.Matrix([[int(x * den) for x in v] for v in vecs]).T                               # 2 x n integer
    H = hermite_normal_form(M)
    basis = [[Fraction(int(H[i, j]), den) for i in range(2)] for j in range(H.shape[1])]
    assert len(basis) == 2, basis
    return basis


def gauss_reduce(b1, b2, G):
    """Gauss (Lagrange) reduction of a 2d lattice basis in the metric G (on coefficient vectors)"""
    def n2(v):
        return float(np.array(v, dtype=float) @ G @ np.array(v, dtype=float))

    def dot(u, v):
        return float(np.array(u, dtype=float) @ G @ np.array(v, dtype=float))
    b1, b2 = list(b1), list(b2)
    for _ in range(200):
        if n2(b2) < n2(b1):
            b1, b2 = b2, b1
        mu = round(dot(b1, b2) / n2(b1))
        if mu == 0:
            break
        b2 = [x - mu * y for x, y in zip(b2, b1)]
    if dot(b1, b2) > 0:
        b2 = [-x for x in b2]
    return b1, b2


def torus_shape(link, gam, g, cbasis, rng):
    """the period lattice of the orbit T_c . gK, its Gram matrix in the normal metric (units (2 pi)^2) and the reduced shape"""
    Qc = torus_q_subspace(link, gam)                                                         # r x d integer
    d = Qc.shape[1]

    def vf(q):                                                                              # m-coordinates of the vector field of q
        X = 2 * np.pi * sum(float(qi) * Hi for qi, Hi in zip(q, link.H))
        return coords(dag(g) @ X @ g, link.m_basis)
    W = np.array([vf(Qc[:, j]) for j in range(d)]).T                                         # 6 x d
    assert rank_of(W) == 2, W
    # rational coordinates of the images in a basis of two of them
    for i, j in itertools.combinations(range(d), 2):
        if rank_of(W[:, [i, j]]) == 2:
            base = (i, j)
            break
    Bm = W[:, list(base)]
    coef = np.linalg.lstsq(Bm, W, rcond=None)[0]                                             # 2 x d
    assert np.abs(Bm @ coef - W).max() < 1e-9
    gens = [[rationalise(coef[0, j], 60), rationalise(coef[1, j], 60)] for j in range(d)]
    L0 = hnf_2d(gens)                                                                        # basis of the image of the integral lattice
    q_of = lambda c: float(c[0]) * Qc[:, base[0]] + float(c[1]) * Qc[:, base[1]]              # noqa: E731
    phi0 = link.embed(g)
    # every point of the full period lattice in the fundamental domain of L0: rational points up to denominator 60, and a Newton grid
    found = set()
    for N in range(1, 61):
        for a in range(N):
            for b in range(N):
                if gcd(gcd(a, b), N) != 1:
                    continue
                c = [Fraction(a, N) * L0[0][k] + Fraction(b, N) * L0[1][k] for k in range(2)]
                t = link.torus(q_of(c))
                if np.linalg.norm(link.embed(t @ g) - phi0) < 1e-9:
                    found.add((Fraction(a, N), Fraction(b, N)))
    grid = set()
    uu = np.linspace(0, 1, 41)[:-1]
    for u0 in uu:
        for v0 in uu:
            u = np.array([u0, v0], dtype=float)
            for _ in range(30):
                c = u[0] * np.array(L0[0], dtype=float) + u[1] * np.array(L0[1], dtype=float)
                q = c[0] * Qc[:, base[0]] + c[1] * Qc[:, base[1]]
                t = link.torus(q)
                R = link.embed(t @ g) - phi0
                cols = []
                for k in range(2):
                    dq = float(L0[k][0]) * Qc[:, base[0]] + float(L0[k][1]) * Qc[:, base[1]]
                    X = 2 * np.pi * sum(float(x) * Hi for x, Hi in zip(dq, link.H))
                    cols.append(link.dembed(t @ g, dag(t @ g) @ X @ (t @ g)))
                Jm = np.stack(cols, axis=-1)
                u = u - np.linalg.lstsq(Jm, R, rcond=None)[0]
            if np.linalg.norm(R) < 1e-10:
                w = u % 1.0
                w[np.abs(w - 1) < 1e-9] = 0.0
                grid.add((rationalise(w[0], 240, 1e-7), rationalise(w[1], 240, 1e-7)))
    grid = {(frac_mod1(a), frac_mod1(b)) for a, b in grid}
    assert grid == found, (sorted(found), sorted(grid))
    gens = [L0[0], L0[1]] + [[a * L0[0][k] + b * L0[1][k] for k in range(2)] for a, b in found]
    Lfull = hnf_2d(gens)
    # the metric on coefficient vectors (in the basis Bm of the tangent plane)
    Gm = Bm.T @ Bm / (2 * np.pi) ** 2
    b1, b2 = gauss_reduce(Lfull[0], Lfull[1], Gm)
    V = np.array([np.array(b1, dtype=float), np.array(b2, dtype=float)])
    Gram = V @ Gm @ V.T
    a2, b2n, ab = Gram[0, 0], Gram[1, 1], Gram[0, 1]
    tau = complex(ab / a2, np.sqrt(a2 * b2n - ab * ab) / a2)
    hexa = min(abs(tau - np.exp(1j * np.pi / 3)), abs(tau - np.exp(2j * np.pi / 3))) < HEX_TOL
    qb = [[str(x) for x in (float(bb[0]) * Qc[:, base[0]] + float(bb[1]) * Qc[:, base[1]])] for bb in (b1, b2)]
    return {"torus_q_subspace (integer basis, columns)": Qc.tolist(),
            "index of the integral image in the period lattice": len(found),
            "period lattice basis (q-coordinates)": [[str(rationalise(float(x), 720)) for x in
                                                      (float(bb[0]) * Qc[:, base[0]] + float(bb[1]) * Qc[:, base[1]])]
                                                     for bb in (b1, b2)],
            "Gram (units (2 pi)^2)": Gram.round(15).tolist(), "tau": [tau.real, tau.imag],
            "hexagonal": bool(hexa), "dist to e^{i pi/3} up to reflection": float(min(abs(tau - np.exp(1j * np.pi / 3)),
                                                                                         abs(tau - np.exp(2j * np.pi / 3))))}


# --------------------------------------------------------------------------------------------------------- H_F and its normal type
def rho_of(link, typ):
    """(kind, rho) for an automorphism type: 'left', or a listed outer element name"""
    if typ == "left":
        return ("left", None)
    o = link.outer[typ]
    return ("aut", o) if isinstance(o, dict) else ("right", o)


def make_gamma(kind, a, rho):
    return ("left", a) if kind == "left" else (kind, a, rho)


def rho_apply(kind, rho, g):
    if kind == "left":
        return g
    if kind == "aut":
        return rho["group"](g)
    return g @ rho


def fixers_of(link, typ, g1, others, rng, seeds=N_HF_SEEDS, iters=60):
    """automorphisms L_a rho (rho of type typ) fixing g1 K and every point in others: Newton over k in K with a = g1 k rho(g1)^-1"""
    kind, rho = rho_of(link, typ)
    R1 = rho_apply(kind, rho, g1)
    Binv = R1                                          # a(k) = g1 k R1^-1, so a(k exp Z) = a(k) exp(R1^-1 ... ) : W = R1 Z R1^-1 ... see below
    k = link.random_elements(rng, seeds, basis=link.k_basis, spread=3.0)
    Kb = np.array(link.k_basis)
    rho_o = [rho_apply(kind, rho, y) for y in others]

    def a_of(kk):
        return g1 @ kk @ dag(R1)

    def resid(kk):
        a = a_of(kk)
        return np.concatenate([link.embed(a @ ry) - link.embed(y) for ry, y in zip(rho_o, others)], axis=-1)
    R = resid(k)
    for _ in range(iters):
        a = a_of(k)
        cols = []
        for Z in link.k_basis:
            W = R1 @ Z @ dag(R1)                           # a(k exp Z) = a(k) exp(W)
            cols.append(np.concatenate([link.dembed(a @ ry, dag(ry) @ W @ ry) for ry in rho_o], axis=-1))
        Jm = np.stack(cols, axis=-1)
        step = -np.einsum("bij,bj->bi", np.linalg.pinv(Jm, rcond=1e-10), R)
        k_new = k @ expm_skew(np.tensordot(step, Kb, axes=([1], [0])))
        R_new = resid(k_new)
        better = np.linalg.norm(R_new, axis=-1) < np.linalg.norm(R, axis=-1)
        k[better], R[better] = k_new[better], R_new[better]
        if not better.any():
            break
    res = np.linalg.norm(R, axis=-1)
    ok = res < CONV_TOL
    return [a_of(kk) for kk in k[ok]], kind, rho, int(ok.sum()), float(res.min())


def same_automorphism(link, kind, rho, a1, a2, hbasis, tests, rng):
    """is L_{a1} rho = L_{a2} rho L_h for some h in H_F^0 ?  (distance of the actions on test points, minimised over h)"""
    def act(a, ys):
        return np.stack([link.embed(a @ rho_apply(kind, rho, y)) for y in ys])
    target = act(a1, tests)
    if not hbasis:
        return float(np.linalg.norm(act(a2, tests) - target)) < COMP_TOL
    Hb = np.array(hbasis)
    best = np.inf
    for _ in range(12):
        h = link.random_elements(rng, 1, basis=hbasis, spread=3.0)[0]
        for _it in range(40):
            ys = [h @ y for y in tests]
            R = (act(a2, ys) - target).reshape(-1)
            cols = []
            for Z in hbasis:
                col = []
                for y in ys:
                    x = a2 @ rho_apply(kind, rho, y)
                    ry = rho_apply(kind, rho, y)
                    # d/ds a2 rho(exp(sZ) y): for aut, rho(exp(sZ) y) = exp(s drho Z) rho(y); for right/left, exp(sZ) y rho-part
                    if kind == "aut":
                        Zr = rho["lie"](Z)
                    else:
                        Zr = Z
                    col.append(link.dembed(x, dag(x) @ (a2 @ Zr @ dag(a2)) @ x))
                cols.append(np.concatenate(col))
            Jm = np.stack(cols, axis=-1)
            step = -np.linalg.pinv(Jm, rcond=1e-10) @ R
            h = expm_skew(np.tensordot(step, Hb, axes=([0], [0]))) @ h
        ys = [h @ y for y in tests]
        best = min(best, float(np.linalg.norm(act(a2, ys) - target)))
        if best < COMP_TOL:
            return True
    return False


def complex_frame(J, N):
    """a J-complex orthonormal basis (n1, n2) of the J-invariant subspace spanned by the columns of N"""
    v1 = N[:, 0] / np.linalg.norm(N[:, 0])
    rest = N - np.outer(v1, v1 @ N) - np.outer(J @ v1, (J @ v1) @ N)
    u, s, vh = np.linalg.svd(rest)
    v2 = u[:, 0] / np.linalg.norm(u[:, 0])
    return v1, v2


def complex_matrix(D, J, v1, v2):
    """D restricted to the complex 2-plane spanned by (v1, v2) (complex structure J), as a 2x2 complex matrix"""
    frame = [v1, v2]
    M = np.zeros((2, 2), dtype=complex)
    for j, v in enumerate(frame):
        w = D @ v
        for i, u in enumerate(frame):
            M[i, j] = (u @ w) + 1j * ((J @ u) @ w)
    return M


def unitary_order(M, maxm=720):
    P = np.eye(M.shape[0], dtype=complex)
    for m in range(1, maxm + 1):
        P = P @ M
        if np.abs(P - np.eye(M.shape[0])).max() < 1e-8:
            return m
    return None


def pointwise_stabiliser(link, gam, g, rng):
    """H_F for the torus component through gK: fixes three generic points, checked on 20; identity component, the discrete part
    (left translations and each listed outer type), the action on the normal space in Y's J"""
    Qc = torus_q_subspace(link, gam)
    pts = [link.torus(Qc @ rng.uniform(0, 1, Qc.shape[1])) @ g for _ in range(23)]
    P3, P20 = pts[:3], pts[3:]
    A = np.vstack([orbit_map(link, p, link.g_basis) for p in P3])
    Nh = null_space(A, 1e-9)
    hbasis = orthonormal([from_coords(Nh[:, j].real, link.g_basis) for j in range(Nh.shape[1])])
    worst_h20 = max(float(np.abs(orbit_map(link, p, hbasis)).max()) for p in P20) if hbasis else 0.0
    # the tangent and normal spaces at p1, and J there (J is left-invariant: the same matrix in the m-trivialisation)
    g1 = P3[0]
    T = orbit_map(link, g1, [2 * np.pi * sum(float(x) * Hi for x, Hi in zip(Qc[:, j], link.H)) for j in range(Qc.shape[1])])
    u, s, vh = np.linalg.svd(T)
    Tb = u[:, :2]
    Nb = u[:, 2:]
    J = link.J
    assert np.abs(Nb.T @ J @ Tb).max() < 1e-9, "the tangent plane of F is not J-complex"
    v1, v2 = complex_frame(J, Nb)
    tests = [link.random_elements(rng, 1)[0] for _ in range(6)]
    comps = []
    types = ["left"] + list(link.outer.keys())
    record_types = {}
    for typ in types:
        found, kind, rho, nconv, rmin = fixers_of(link, typ, g1, P3[1:], rng)
        reps = []
        for a in found:
            if not any(same_automorphism(link, kind, rho, a, b, hbasis, tests, rng) for b in reps):
                reps.append(a)
        record_types[typ] = {"converged seeds": nconv, "components": len(reps)}
        for a in reps:
            phi = make_gamma(kind, a, rho)
            worst20 = max(float(np.linalg.norm(link.residual(phi, p))) for p in P20)
            D = link.differential(phi, g1)
            tang = float(np.abs(D @ Tb - Tb).max())
            commJ = float(np.abs(D @ J - J @ D).max())
            M = complex_matrix(D, J, v1, v2)
            comps.append({"type": typ, "fixes the 20 points (worst residual)": worst20, "d phi = 1 on T F": tang,
                          "d phi J - J d phi": commJ, "normal matrix": M, "normal eigenvalues": np.linalg.eigvals(M),
                          "det": complex(np.linalg.det(M)), "order": unitary_order(M) if not hbasis else None})
    # the identity component's generator(s) on the normal space
    gens = []
    for X in hbasis:
        kX = dag(g1) @ X @ g1
        adk = np.array([[ip(Bt, kX @ B - B @ kX) for B in link.m_basis] for Bt in link.m_basis])
        M = complex_matrix(adk, J, v1, v2)
        gens.append({"normal matrix": M, "eigenvalues": np.linalg.eigvals(M), "trace": complex(np.trace(M)),
                     "tangent": float(np.abs(adk @ Tb).max())})
    h0 = len(hbasis)
    ncomp = len(comps)
    su2_type = all(abs(c["det"] - 1) < 1e-9 and c["d phi = 1 on T F"] < 1e-9 for c in comps) and \
        all(abs(gg["trace"]) < 1e-9 and gg["tangent"] < 1e-9 for gg in gens)
    if h0 == 0:
        orders = [c["order"] for c in comps]
        cyclic = max(orders) == ncomp
        kind_str = "finite, order %d" % ncomp
        all_cyclic = cyclic
        ade = ("A%d" % (ncomp - 1)) if cyclic and ncomp >= 2 else ("trivial" if ncomp == 1 else "non-cyclic: see orders")
    elif h0 == 1:
        kind_str = "continuous: U(1)" if ncomp == 1 else "continuous: U(1) with %d components" % ncomp
        all_cyclic = ncomp == 1
        ade = "A (every finite subgroup cyclic)" if all_cyclic else "D possible (a component outside U(1))"
    else:
        kind_str = "continuous, identity component of dimension %d" % h0
        all_cyclic = False
        ade = "non-abelian identity component"
    return {"identity component dim": h0, "discrete part by type": record_types, "H_F": kind_str,
            "every finite subgroup cyclic": bool(all_cyclic), "ADE": ade, "SU(2)-type on the normal space": bool(su2_type),
            "identity component checked on 20 points (worst vector field)": worst_h20,
            "elements": [{k: (v.round(12).tolist() if isinstance(v, np.ndarray) and v.dtype != complex else
                              ([[str(np.round(z, 12)) for z in row] for row in v] if isinstance(v, np.ndarray) and v.ndim == 2 else
                               ([str(np.round(z, 12)) for z in v] if isinstance(v, np.ndarray) else
                                (str(np.round(v, 12)) if isinstance(v, complex) else v))))
                          for k, v in c.items()} for c in comps],
            "generators": [{"eigenvalues": [str(np.round(z, 12)) for z in gg["eigenvalues"]], "trace": str(np.round(gg["trace"], 12)),
                            "tangent": gg["tangent"]} for gg in gens]}


# ------------------------------------------------------------------------------------------------------------- one census class
LINKS = {"S6": S6, "S3xS3": S3xS3, "CP3": CP3, "F12": F12}


def jsonable(x):
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, complex):
        return [x.real, x.imag]
    if isinstance(x, np.ndarray):
        return jsonable(x.tolist())
    return x


def run_class(link, cls, full=True):
    label = class_label(cls)
    rng = np.random.default_rng(label_seed(label))
    t0 = time.time()
    gam = gamma_of(link, cls)
    cbasis = link.centraliser_basis(gam)
    cstruct = lie_structure(link, cbasis)
    g, res = newton_fixed(link, gam, link.random_elements(rng, N_SEEDS))
    conv = res < CONV_TOL
    rec = {"label": label, "link": link.name, "q": [str(x) for x in cls["q"]], "outer": cls["outer"], "order": cls["order"],
           "C(gamma)^0": centraliser_name(cstruct), "C(gamma)^0 structure": cstruct,
           "seeds": N_SEEDS, "converged": int(conv.sum()),
           "smallest residual of the other seeds": float(res[~conv].min()) if (~conv).any() else None, "components": []}
    sols = g[conv]
    if len(sols):
        comps, _ = cluster_components(link, gam, sols, rng)
        for members in comps:
            rep = sols[members[0]]
            pts = [sols[i] for i in members[:3]]
            while len(pts) < 3:
                c = link.random_elements(rng, 1, basis=cbasis, spread=3.0)[0] if cbasis else np.eye(link.n, dtype=complex)
                pts.append(c @ rep)
            dims = [6 - rank_of(link.differential(gam, p) - np.eye(6), 1e-8) for p in pts]
            top = topology(link, rep, cbasis)
            crec = {"seeds": len(members), "dims at three points": dims, "dim": dims[0] if len(set(dims)) == 1 else None,
                    "topology": top, "residual at the three points": float(max(np.linalg.norm(link.residual(gam, p)) for p in pts))}
            if top["type"] == "torus" and full:
                crec["shape"] = torus_shape(link, gam, rep, cbasis, rng)
                crec["H_F"] = pointwise_stabiliser(link, gam, rep, rng)
            if top["type"] == "point":
                crec["point (embedding)"] = [round(float(x), 9) for x in link.embed(rep)]
            rec["components"].append(crec)
    rec["seconds"] = round(time.time() - t0, 1)
    return jsonable(rec)


def s6_direct(cls):
    """the fixed set of a G2 torus element on S6, from its fixed subspace on R^7 (1 + 2 x the number of trivial eigenvalue pairs)"""
    q1, q2 = cls["q"]
    qs = [frac_mod1(q1), frac_mod1(q2), frac_mod1(-q1 - q2)]
    triv = sum(1 for x in qs if x == 0)
    dim = 1 + 2 * triv
    return {1: "two antipodal points", 3: "a great 2-sphere"}.get(dim, "dim %d" % dim)


def s6_agrees(rec, cls):
    expect = s6_direct(cls)
    comps = rec["components"]
    if expect == "two antipodal points":
        ok = len(comps) == 2 and all(c["dim"] == 0 and c["topology"]["type"] == "point" for c in comps)
        if ok:
            p, q = (np.array(c["point (embedding)"]) for c in comps)
            ok = np.abs(p + q).max() < 1e-8                                                  # antipodal
    else:
        ok = len(comps) == 1 and comps[0]["dim"] == 2 and comps[0]["topology"]["type"] == "sphere"
    return expect, bool(ok)


# --------------------------------------------------------------------------------------------------------------------- the run
_WORKER_LINKS = {}


def _worker(cls):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    name = cls["link"]
    if name not in _WORKER_LINKS:
        _WORKER_LINKS[name] = LINKS[name]()
    return run_class(_WORKER_LINKS[name], cls)


def banked_identity(links, log):
    """must pass before any census number is read"""
    rng = np.random.default_rng(1501)
    out = {}
    log("BANKED IDENTITY")
    # the structures
    for name, link in links.items():
        rec = structure_checks(link, rng)
        out["structures " + name] = rec
        log("  %-6s J^2 = -1 to %.1e, J orthogonal to %.1e, Ad(K) commutes with J to %.1e; listed outer elements preserve J: %s; "
            "excluded reverse J: %s" % (name, rec["J^2+1"], rec["J orthogonal"], rec["Ad(K) commutes with J"],
                                        sorted(rec["listed outer elements preserve J"]) or "none listed",
                                        sorted(rec["excluded elements reverse J"])))
    rec = s6_cross_product_check(links["S6"], rng)
    out["S6 cross product"] = rec
    log("  S6: G2 preserves the octonion cross product to %.1e; %s" % tuple(list(rec.values())[:1] + ["; ".join(
        "%s to %.1e" % kv for kv in list(rec.items())[1:])]))
    # S6: torus elements against the direct fixed subspace (non-census controls of order 13)
    for q in [(Fraction(1, 13), Fraction(3, 13)), (Fraction(1, 13), Fraction(12, 13)), (Fraction(2, 13), Fraction(5, 13))]:
        cls = {"link": "S6", "q": q, "outer": None, "order": 13}
        r = run_class(links["S6"], cls)
        expect, ok = s6_agrees(r, cls)
        out["S6 control " + r["label"]] = {"expected": expect, "agrees": ok,
                                           "components": [(c["seeds"], c["dim"], c["topology"]["type"]) for c in r["components"]]}
        log("  S6 control %s (order 13, not in the census): %s; census pipeline %s" % (r["label"], expect, "agrees" if ok else "DISAGREES"))
        assert ok, r
    # S3 x S3: the diagonal-conjugation torus (B1500 section 5), on a non-census control of order 13
    link = links["S3xS3"]
    cls = {"link": "S3xS3", "q": (Fraction(1, 13),) * 3, "outer": None, "order": 13}
    r = run_class(link, cls)
    tori = [c for c in r["components"] if c["topology"]["type"] == "torus"]
    assert len(r["components"]) == 1 and len(tori) == 1, r
    G = np.array(tori[0]["shape"]["Gram (units (2 pi)^2)"])
    gram_ok = np.abs(G - np.array([[2, -1], [-1, 2]]) / 3).max() < 1e-12 and tori[0]["shape"]["hexagonal"]
    # the diagonal U(1) fixes the torus pointwise: its vector field vanishes along F
    gam = gamma_of(link, cls)
    g, res = newton_fixed(link, gam, link.random_elements(np.random.default_rng(13), 20))
    diag = blockdiag3(*[np.diag([1j, -1j])] * 3)
    worst = 0.0
    for gg in g[res < CONV_TOL]:
        for _ in range(5):
            p = link.torus(np.random.default_rng(3).uniform(0, 1, 3)) @ gg
            worst = max(worst, float(np.abs(orbit_map(link, p, [diag])).max()))
    hf = tori[0]["H_F"]
    u1_ok = worst < 1e-12 and hf["identity component dim"] >= 1
    out["S3xS3 diagonal torus"] = {"Gram": G.tolist(), "hexagonal": tori[0]["shape"]["hexagonal"],
                                   "diagonal U(1) vector field along F (worst)": worst, "H_F": hf["H_F"]}
    log("  S3xS3 diagonal-conjugation torus (order-13 control): Gram %s (2 pi)^2, hexagonal %s; the diagonal U(1) fixes it pointwise "
        "(vector field %.1e); H_F %s" % (np.round(G, 12).tolist(), tori[0]["shape"]["hexagonal"], worst, hf["H_F"]))
    assert gram_ok and u1_ok, out["S3xS3 diagonal torus"]
    log("  banked identity: PASS")
    return out


def main(workers=4):
    t0 = time.time()
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)
    digest = hashlib.sha256((HERE.parent / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert digest == SEALED_SHA256, digest
    log("B1501 THE TORUS-LINK CENSUS, run as sealed. PREREGISTRATION sha256 %s (matches SEAL_LEDGER)" % digest)
    links = {name: L() for name, L in LINKS.items()}
    identity = banked_identity(links, log)
    # the census
    classes = []
    for name, link in links.items():
        cl = enumerate_classes(link)
        classes += cl
        log("census %s: %d classes of order <= %d (%s)" % (name, len(cl), MAX_ORDER, ", ".join(
            "%s %d" % (k, v) for k, v in sorted(Counter_((c["outer"] or "left") for c in cl).items()))))
    import multiprocessing as mp
    ctx = mp.get_context("fork")
    with ctx.Pool(workers) as pool:
        records = list(pool.imap(_worker, classes, chunksize=1))
    log("census computed in %.0f s" % (time.time() - t0))
    # checks that must pass
    lemma_fail = [r["label"] for r in records if r["outer"] is None and r["link"] in ("S6", "CP3", "F12")
                  and any(c["topology"]["type"] == "torus" for c in r["components"])]
    log("THE LEMMA (left translations on S6, CP3, F12 give no torus): %s" % ("PASS" if not lemma_fail else "FAIL %s" % lemma_fail))
    assert not lemma_fail
    s6_bad = [r["label"] for r, c in zip(records, classes) if r["link"] == "S6" and not s6_agrees(r, c)[1]]
    log("S6 census against the direct fixed subspace: %s" % ("all %d agree" % sum(1 for r in records if r["link"] == "S6")
                                                            if not s6_bad else "DISAGREE %s" % s6_bad))
    assert not s6_bad
    flags = []
    for r in records:
        for c in r["components"]:
            if c["dim"] is None:
                flags.append((r["label"], "dimensions disagree at the three points", c["dims at three points"]))
            elif c["dim"] != c["topology"]["orbit_dim"]:
                flags.append((r["label"], "component not a single C(gamma)^0 orbit", c["dim"], c["topology"]["orbit_dim"]))
            if c["topology"]["type"] == "other":
                flags.append((r["label"], "topology other", c["topology"]))
        s = r["smallest residual of the other seeds"]
        if s is not None and s < 1e-6:
            flags.append((r["label"], "a non-converged seed has a small residual", s))
    log("internal flags: %d %s" % (len(flags), flags[:10]))
    summary = readout(records, log)
    out = {"sealed sha256": digest, "banked identity": identity, "classes": len(records), "flags": flags, "summary": summary,
           "records": records}
    (HERE / "census.json").write_text(json.dumps(jsonable(out), indent=1))
    log("wrote census.json; %.0f s in all" % (time.time() - t0))
    (HERE / "census_run.txt").write_text("\n".join(lines) + "\n")
    return out


def Counter_(it):
    from collections import Counter
    return Counter(it)


def readout(records, log):
    summary = {}
    for name in LINKS:
        rs = [r for r in records if r["link"] == name]
        comp_types = Counter_(c["topology"]["type"] for r in rs for c in r["components"])
        with_fix = sum(1 for r in rs if r["components"])
        cent = Counter_(r["C(gamma)^0"] for r in rs)
        tori = [(r["label"], r["order"], c) for r in rs for c in r["components"] if c["topology"]["type"] == "torus"]
        summary[name] = {"classes": len(rs), "with fixed points": with_fix, "components by type": dict(comp_types),
                         "centraliser types met": dict(cent), "torus classes": len(set(t[0] for t in tori))}
        log("%s: %d classes, %d with fixed points; components %s; centraliser types met %s" % (
            name, len(rs), with_fix, dict(comp_types), dict(cent)))
        for lab, order, c in tori:
            h = c["H_F"]
            log("   torus: %s (order %d): tau = %.12f + %.12f i, hexagonal %s, lattice %s, Gram %s; H_F %s, every finite subgroup "
                "cyclic %s, %s, normal SU(2)-type %s" % (lab, order, c["shape"]["tau"][0], c["shape"]["tau"][1], c["shape"]["hexagonal"],
                                                         c["shape"]["period lattice basis (q-coordinates)"],
                                                         np.round(np.array(c["shape"]["Gram (units (2 pi)^2)"]), 12).tolist(),
                                                         h["H_F"], h["every finite subgroup cyclic"], h["ADE"],
                                                         h["SU(2)-type on the normal space"]))
    all_tori = [(r, c) for r in records for c in r["components"] if c["topology"]["type"] == "torus"]
    p1 = all(c["H_F"]["every finite subgroup cyclic"] and c["H_F"]["SU(2)-type on the normal space"] for r, c in all_tori)
    p2 = all(c["shape"]["hexagonal"] for r, c in all_tori)
    links_with = sorted(set(r["link"] for r, c in all_tori))
    f12 = any(r["link"] == "F12" for r, c in all_tori)
    summary["P1 every torus locus A-type (all finite subgroups of H_F cyclic)"] = "YES" if p1 and all_tori else ("NO" if all_tori else "no torus")
    summary["P2 every torus hexagonal"] = "YES" if p2 and all_tori else ("NO" if all_tori else "no torus")
    summary["P3 links carrying torus loci"] = links_with
    summary["P3 F12 carries a torus locus"] = f12
    summary["torus components"] = len(all_tori)
    log("P1 (every torus locus A-type, all finite subgroups of H_F cyclic): %s" % summary["P1 every torus locus A-type (all finite subgroups of H_F cyclic)"])
    log("P2 (every torus hexagonal): %s" % summary["P2 every torus hexagonal"])
    log("P3: links carrying torus loci %s; F12 carries one: %s; %d torus components in %d classes" % (
        links_with, f12, len(all_tori), len(set(r["label"] for r, c in all_tori))))
    return summary


if __name__ == "__main__":
    main()
