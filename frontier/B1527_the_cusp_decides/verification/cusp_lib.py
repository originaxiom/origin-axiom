"""B1527 -- THE CUSP DECIDES: the library.  Nothing sealed is computed on import.

Main's class index (B1297) for a finite-dimensional complex representation V of a finitely presented group Gamma with one
peripheral subgroup Delta = <p1, p2> = Z^2:
    n(V) = dim ker(H^1(Gamma; V) -> H^1(Delta; V)),      I(V) = n(V) - n(V*),
with the B1297 identity I = (a0 - b0) + s0 - r1 checked on every reading (a0 = h^0(Gamma; V), b0 = h^0(Gamma; V*),
s0 = h^0(Delta; V*), r1 = rank of the restriction), the annihilator identity r1 + q1 = h^1(Delta; V) = t0 + s0, and
Lemma E (B1527 PREREGISTRATION section 3) I = h^1(V*) - h^1(V) + 2 (a0 - b0) + s0 - t0.

Cohomology by Fox calculus with left cocycles, z(gh) = z(g) + g.z(h): Z^1 is the kernel of the Fox matrix of the relators,
B^1 the image of v -> ((g - 1)v)_g.  Ranks by singular values at mp.dps = 60, with every decision's margin kept: the smallest
singular value kept and the largest dropped, relative to the largest.

This is new code for B1527.  It shares nothing with sm:B1374's index_lib or sm:B1511's tower_lib (exact and modular routes);
its controls are banked numbers of the record (sm:B1509's I(W1) = -1 and I(W2) = +1 on m004; B1509 T1's longitude
spectrum)."""
import mpmath as mp

mp.mp.dps = 60
REL_TOL = mp.mpf(10) ** -30          # a singular value below REL_TOL * (largest) is zero


# ============================================================================================ words
def inv_word(w):
    return "".join(c.swapcase() for c in reversed(w))


def free_reduce(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def substitute(w, img):
    """the image of w under the endomorphism with images img[g] for the lower-case generators g"""
    return free_reduce("".join(img[c] if c.islower() else inv_word(img[c.lower()]) for c in w))


# ============================================================================================ modules
class Module:
    """matrices M[g] (mp.matrix, d x d) for the generators; words evaluated left to right"""

    def __init__(self, mats):
        self.M = dict(mats)
        self.d = next(iter(mats.values())).rows
        for g in list(mats):
            self.M[g.upper()] = mp.inverse(mats[g])

    def word(self, w):
        X = mp.eye(self.d)
        for c in w:
            X = X * self.M[c]
        return X

    def dual(self):
        return Module({g: mp.inverse(self.M[g]).T for g in self.M if g.islower()})

    def gens(self):
        return [g for g in self.M if g.islower()]


def scaled(mod, chi):
    """chi (x) V, chi a character given by its values on the generators"""
    return Module({g: chi[g] * mod.M[g] for g in mod.gens()})


def wedge2(M):
    n = M.rows
    idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
    W = mp.matrix(len(idx), len(idx))
    for a, (i, j) in enumerate(idx):
        for b, (k, l) in enumerate(idx):
            W[a, b] = M[i, k] * M[j, l] - M[i, l] * M[j, k]
    return W


def wedge2_module(mod):
    return Module({g: wedge2(mod.M[g]) for g in mod.gens()})


# ============================================================================================ linear algebra with margins
class Margins:
    """every rank decision's (smallest kept, largest dropped) singular value, relative to the largest"""

    def __init__(self):
        self.kept, self.dropped = mp.mpf(1), mp.mpf(0)

    def note(self, s, r):
        if not s:
            return
        top = max(s)
        if top == 0:
            return
        rel = [x / top for x in s]
        if r > 0:
            self.kept = min(self.kept, rel[r - 1])
        if r < len(rel):
            self.dropped = max(self.dropped, rel[r])

    def as_dict(self):
        return {"smallest kept": mp.nstr(self.kept, 3), "largest dropped": mp.nstr(self.dropped, 3)}


def svals(A):
    if A.rows == 0 or A.cols == 0:
        return []
    S = mp.svd_c(A, compute_uv=False)
    return sorted([abs(S[i]) for i in range(min(A.rows, A.cols))], reverse=True)


def rank(A, mg):
    s = svals(A)
    if not s or s[0] == 0:
        return 0
    r = sum(1 for x in s if x > REL_TOL * s[0])
    mg.note(s, r)
    return r


def kernel(A, mg):
    """an orthonormal basis of the kernel (columns), with the rank decision recorded"""
    n = A.cols
    if A.rows == 0:
        return mp.eye(n)
    U, S, V = mp.svd_c(A, full_matrices=True)
    s = [abs(S[i]) for i in range(min(A.rows, A.cols))]
    top = max(s) if s else mp.mpf(0)
    r = sum(1 for x in s if top > 0 and x > REL_TOL * top)
    mg.note(sorted(s, reverse=True), r)
    Vh = V                                   # rows of V are the right singular vectors (conjugated)
    K = mp.matrix(n, n - r)
    for k in range(r, n):
        for i in range(n):
            K[i, k - r] = mp.conj(Vh[k, i])
    return K


def hstack(*mats):
    mats = [M for M in mats if M is not None and M.cols > 0]
    if not mats:
        return None
    rows = mats[0].rows
    out = mp.matrix(rows, sum(M.cols for M in mats))
    c = 0
    for M in mats:
        for i in range(rows):
            for j in range(M.cols):
                out[i, c + j] = M[i, j]
        c += M.cols
    return out


def vstack(*mats):
    mats = [M for M in mats if M is not None and M.rows > 0]
    cols = mats[0].cols
    out = mp.matrix(sum(M.rows for M in mats), cols)
    r = 0
    for M in mats:
        for i in range(M.rows):
            for j in range(cols):
                out[r + i, j] = M[i, j]
        r += M.rows
    return out


# ============================================================================================ Fox calculus and cohomology
def fox(word, mod, gens):
    """the Fox derivatives d word / d g, evaluated in mod: a dict g -> d x d matrix (left convention)"""
    d = mod.d
    out = {g: mp.matrix(d, d) for g in gens}
    P = mp.eye(d)
    for c in word:
        if c.islower():
            out[c] += P
            P = P * mod.M[c]
        else:
            P = P * mod.M[c]
            out[c.lower()] -= P
    return out


def fox_row(word, mod, gens):
    """the d x (d * #gens) block row z -> z(word)"""
    F = fox(word, mod, gens)
    return hstack(*[F[g] for g in gens])


class Group:
    def __init__(self, gens, rels, cusp, name=""):
        self.gens, self.rels, self.cusp, self.name = list(gens), list(rels), tuple(cusp), name


def relator_residual(G, mod):
    return max(mp.mnorm(mod.word(r) - mp.eye(mod.d), 1) for r in G.rels)


def cusp_commutator_residual(G, mod):
    P1, P2 = mod.word(G.cusp[0]), mod.word(G.cusp[1])
    return mp.mnorm(P1 * P2 - P2 * P1, 1)


def half_index(G, mod, mg):
    """(a0, h1, t0, r1, n) for one module"""
    d, gens = mod.d, G.gens
    I = mp.eye(d)
    # H^0(Gamma)
    Hg = vstack(*[mod.M[g] - I for g in gens])
    a0 = d - rank(Hg, mg)
    # Z^1(Gamma): kernel of the Fox matrix
    J = vstack(*[fox_row(r, mod, gens) for r in G.rels])
    Z = kernel(J, mg)
    B = vstack(*[mod.M[g] - I for g in gens])                       # columns v -> ((g - 1) v)_g
    dimB = rank(B, mg)
    h1 = Z.cols - dimB
    # the peripheral torus
    P1, P2 = mod.word(G.cusp[0]), mod.word(G.cusp[1])
    t0 = d - rank(vstack(P1 - I, P2 - I), mg)
    R = vstack(fox_row(G.cusp[0], mod, gens), fox_row(G.cusp[1], mod, gens))   # z -> (z(p1), z(p2))
    BD = vstack(P1 - I, P2 - I)
    rB = rank(BD, mg)
    rZ = rank(hstack(R * Z, BD), mg)
    r1 = rZ - rB
    # Z^1(Delta) and H^1(Delta), directly, for the identity check
    ZD = kernel(hstack(-(P2 - I), P1 - I), mg)                       # (u1, u2) with (P1 - 1) u2 = (P2 - 1) u1
    h1D = ZD.cols - rB
    return {"a0": a0, "h1": h1, "t0": t0, "r1": r1, "n": h1 - r1, "h1(Delta)": h1D}


def class_index(G, mod):
    mg = Margins()
    V = half_index(G, mod, mg)
    Vs = half_index(G, mod.dual(), mg)
    I = V["n"] - Vs["n"]
    checks = {
        "B1297 identity I = (a0 - b0) + s0 - r1": I == (V["a0"] - Vs["a0"]) + Vs["t0"] - V["r1"],
        "r1 + q1 = h1(Delta) = t0 + s0": V["r1"] + Vs["r1"] == V["h1(Delta)"] == V["t0"] + Vs["t0"] == Vs["h1(Delta)"],
        "Lemma E I = h1(V*) - h1(V) + 2(a0 - b0) + s0 - t0":
            I == Vs["h1"] - V["h1"] + 2 * (V["a0"] - Vs["a0"]) + Vs["t0"] - V["t0"],
    }
    return {"I": I, "V": V, "V*": Vs, "checks": checks, "margins": mg.as_dict(),
            "relator residual": mp.nstr(relator_residual(G, mod), 3),
            "cusp commutator residual": mp.nstr(cusp_commutator_residual(G, mod), 3)}


# ============================================================================================ extensions (the positive control)
def cocycle_generator(G, mod):
    """a cocycle z (dict g -> column vector) whose class spans H^1(Gamma; V) when h^1 = 1: the kernel vector of the Fox matrix
    orthogonal to the coboundaries"""
    mg = Margins()
    d, gens = mod.d, G.gens
    J = vstack(*[fox_row(r, mod, gens) for r in G.rels])
    Z = kernel(J, mg)
    B = vstack(*[mod.M[g] - mp.eye(d) for g in gens])
    # project the kernel onto the orthogonal complement of the coboundaries
    QB = kernel(B.H, mg)                    # vectors orthogonal to im B
    best, bestn = None, mp.mpf(0)
    for k in range(Z.cols):
        z = Z[:, k]
        pr = QB * (QB.H * z)
        nz = mp.norm(pr)
        if nz > bestn:
            best, bestn = z, nz
    return {g: best[i * d:(i + 1) * d, 0] for i, g in enumerate(gens)}, bestn


def extension(mod, z):
    """W = [[V, z], [0, 1]] (rank d + 1, the trivial line as quotient)"""
    d = mod.d
    mats = {}
    for g in mod.gens():
        W = mp.matrix(d + 1, d + 1)
        for i in range(d):
            for j in range(d):
                W[i, j] = mod.M[g][i, j]
            W[i, d] = z[g][i]
        W[d, d] = 1
        mats[g] = W
    return Module(mats)


# ============================================================================================ m004 in Ballas' presentation (control)
BALLAS = Group(["m", "n"], ["mnMNmNMnmN"], ("m", "nMNmmNMn"), "m004 (Ballas' presentation)")


def ballas(q):
    """Ballas' family at q (t = q/2), as in sm:B1509 and sm:B1520"""
    t = mp.mpf(q) / 2
    m = mp.matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + mp.mpf(1) / 2], [0, 0, 0, 1]])
    n = mp.matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return Module({"m": m, "n": n})


# ============================================================================================ SL(2, C) -> SO(3, 1) in the paraboloid frame
def hermitian_paraboloid(g):
    """H -> g H g^* on Hermitian H = [[p, w], [conj w, r]], in the coordinates (p/2, Re w, Im w, r): a real 4 x 4 matrix.
    The parabolic [[1, z], [0, 1]] maps to exp(x(E12 + E24) + y(E13 + E34)), z = x + i y (Ballas' type-0 normal form)."""
    basis = [mp.matrix([[2, 0], [0, 0]]), mp.matrix([[0, 1], [1, 0]]), mp.matrix([[0, 1j], [-1j, 0]]), mp.matrix([[0, 0], [0, 1]])]

    def coords(H):
        return [mp.re(H[0, 0]) / 2, mp.re(H[0, 1]), mp.im(H[0, 1]), mp.re(H[1, 1])]
    out = mp.matrix(4, 4)
    for j, E in enumerate(basis):
        c = coords(g * E * g.H)
        for i in range(4):
            out[i, j] = c[i]
    return out
