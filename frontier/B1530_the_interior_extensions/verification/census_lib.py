#!/usr/bin/env python3
"""B1530 -- route G: Fox calculus on the bundle group itself, the derivatives grouped by the class of the prefix.  Library;
nothing sealed is computed on import.

Gamma = <a, b, t | t a T phi(a)^-1, t b T phi(b)^-1> (sm:B1527 family_lib.word_group), with the cusp <abAB, t'>.  Take a module
rho (no character) and a character nu with nu(a) = zeta_D^i, nu(b) = zeta_D^j, nu(t) = lam.  The left Fox derivative of a word
w by a generator g, evaluated in nu (x) rho, is the sum over the occurrences of g^(+-1) in w of +- nu(prefix) rho(prefix).
nu(prefix) = zeta_D^(i e_a + j e_b) lam^(e_t) depends only on the class (e_a mod D, e_b mod D, e_t) of the prefix.  So each
derivative is precomputed once per module as a sum over classes (python-flint acb_mat at PREC bits), and a character costs one
weighted sum per block.  Ranks are read by singular values at mp.dps = 60, with every decision's margin kept (REL_TOL = 10^-30,
as sm:B1527's cusp_lib).

What it reads:
  - h1(nu (x) rho) = dim Z^1 - dim B^1 at any character (Part B: population B at kappa in {-1, +-i, omega, omega^2});
  - Part C, for Lambda^2 rho at a character chi with chi|P = 1: Lambda_A (the restriction image of H^1(Gamma; chi (x)
    Lambda^2 rho) in H^1(P; Lambda^2 rho)) and pi_A (the classes of the cocycles valued in the P-fixed vectors), with
    dim(Lambda_A meet pi_A) read two ways:
      (rank) 2 + 2 - dim(Lambda_A + pi_A) modulo B^1(P);
      (pairing) 2 - rank of the torus cup-product pairing between the restricted cocycles and the pi_A cocycles, with the
      coefficient pairing alpha ^ beta on Lambda^2 C^4 (Lambda_A is Lagrangian and pi_A isotropic, both checked, so the
      pairing's rank is 2 - dim(Lambda_A meet pi_A)).

New code for B1530.  It shares the presentation and the hyperbolic point with sm:B1527 and sm:B1529.  It shares no linear
algebra with sm:B1529's fibre_lib (route T: the fibre's four-term sequence), sm:B1527's cusp_lib and wang_lib, or exact_lib."""
import mpmath as mp
from flint import acb, acb_mat, ctx

PREC = 320
DPS = 60
REL_TOL = mp.mpf(10) ** -30


def to_acb(x):
    x = mp.mpc(x)
    return acb(mp.nstr(mp.re(x), DPS + 5, strip_zeros=False), mp.nstr(mp.im(x), DPS + 5, strip_zeros=False))


def acb_of_mp(M):
    return acb_mat([[to_acb(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])


def mp_of_acb(M):
    out = mp.matrix(M.nrows(), M.ncols())
    for i, row in enumerate(M.tolist()):
        for j, z in enumerate(row):
            out[i, j] = mp.mpc(mp.mpf(z.real.mid().str(DPS + 10, radius=False)),
                               mp.mpf(z.imag.mid().str(DPS + 10, radius=False)))
    return out


def unit(k, D):
    if D == 1 or k % D == 0:
        return acb(1)
    return (acb.pi() * acb(0, 2 * (k % D)) / D).exp()


def eye_acb(d):
    return acb_mat(d, d, [1 if i == j else 0 for i in range(d) for j in range(d)])


class Margins:
    def __init__(self):
        self.kept, self.dropped = mp.mpf(1), mp.mpf(0)

    def note(self, s, r):
        if not s or s[0] == 0:
            return
        if r > 0:
            self.kept = min(self.kept, s[r - 1] / s[0])
        if r < len(s):
            self.dropped = max(self.dropped, s[r] / s[0])

    def as_dict(self):
        return {"smallest kept": mp.nstr(self.kept, 3), "largest dropped": mp.nstr(self.dropped, 3)}


def svd_rank(A, mg, scale=None):
    """(rank, U, s, Vh) by singular values; with scale, a matrix below REL_TOL * scale is zero"""
    with mp.workdps(DPS):
        if A.rows == 0 or A.cols == 0:
            return 0, None, [], None
        U, S, Vh = mp.svd_c(A, full_matrices=True)
        s = [abs(S[k]) for k in range(min(A.rows, A.cols))]
        top = max(s) if s else mp.mpf(0)
        if top == 0 or (scale is not None and top <= REL_TOL * scale):
            return 0, U, s, Vh
        r = sum(1 for x in s if x > REL_TOL * top)
        mg.note(sorted(s, reverse=True), r)
        return r, U, s, Vh


def null_basis(A, mg):
    """columns spanning ker A (right singular vectors)"""
    r, U, s, Vh = svd_rank(A, mg)
    n = A.cols
    K = mp.matrix(n, n - r)
    for k in range(r, n):
        for i in range(n):
            K[i, k - r] = mp.conj(Vh[k, i])
    return K


def vstack(*mats):
    cols = mats[0].cols
    out = mp.matrix(sum(M.rows for M in mats), cols)
    r = 0
    for M in mats:
        for i in range(M.rows):
            for j in range(cols):
                out[r + i, j] = M[i, j]
        r += M.rows
    return out


def hstack(*mats):
    rows = mats[0].rows
    out = mp.matrix(rows, sum(M.cols for M in mats))
    c = 0
    for M in mats:
        for i in range(rows):
            for j in range(M.cols):
                out[i, c + j] = M[i, j]
        c += M.cols
    return out


class GroupedFox:
    """the Fox blocks of the relators and of the cusp words for rho, grouped by the class of the prefix"""

    def __init__(self, G, mats, D):
        ctx.prec = PREC
        self.G, self.D = G, D
        self.gens = list(G.gens)
        self.d = mats[self.gens[0]].rows
        self.M = {g: acb_of_mp(mats[g]) for g in self.gens}
        self.Mi = {g: acb_of_mp(mp.inverse(mats[g])) for g in self.gens}
        self.rel_blocks = [self._blocks(r) for r in G.rels]
        self.cusp_blocks = [self._blocks(p) for p in G.cusp]
        self.cusp_words = [self._word_class(p) for p in G.cusp]
        self.gen_class = {g: self._word_class(g) for g in self.gens}

    def _cls(self, ea, eb, et):
        return (ea % self.D, eb % self.D, et)

    def _blocks(self, w):
        d = self.d
        P = eye_acb(d)
        ea = eb = et = 0
        out = {g: {} for g in self.gens}

        def add(g, key, X, sgn):
            cur = out[g].get(key)
            if cur is None:
                out[g][key] = X if sgn > 0 else -X
            else:
                out[g][key] = (cur + X if sgn > 0 else cur - X).mid()
        for c in w:
            g = c.lower()
            if c.islower():
                add(g, self._cls(ea, eb, et), P, +1)
                P = (P * self.M[g]).mid()
                ea, eb, et = ea + (g == "a"), eb + (g == "b"), et + (g == "t")
            else:
                P = (P * self.Mi[g]).mid()
                ea, eb, et = ea - (g == "a"), eb - (g == "b"), et - (g == "t")
                add(g, self._cls(ea, eb, et), P, -1)
        return out

    def _word_class(self, w):
        d = self.d
        P = eye_acb(d)
        ea = eb = et = 0
        for c in w:
            g = c.lower()
            if c.islower():
                P = (P * self.M[g]).mid()
                ea, eb, et = ea + (g == "a"), eb + (g == "b"), et + (g == "t")
            else:
                P = (P * self.Mi[g]).mid()
                ea, eb, et = ea - (g == "a"), eb - (g == "b"), et - (g == "t")
        return self._cls(ea, eb, et), P

    def _chi(self, key, i, j, lam):
        ea, eb, et = key
        v = unit(i * ea + j * eb, self.D)
        if et:
            v = v * (lam ** et if et > 0 else (1 / lam) ** (-et))
        return v

    def _eval(self, blocks, i, j, lam):
        d = self.d
        S = acb_mat(d, d)
        for key, X in blocks.items():
            S = (S + self._chi(key, i, j, lam) * X).mid()
        return S

    def fox(self, i, j, lam):
        """the Fox matrix of the relators (rows) on (z(a), z(b), z(t)) (columns), at nu = (zeta^i, zeta^j, lam)"""
        rows = []
        for bl in self.rel_blocks:
            rows.append(hstack(*[mp_of_acb(self._eval(bl[g], i, j, lam)) for g in self.gens]))
        return vstack(*rows)

    def restriction(self, i, j, lam):
        rows = []
        for bl in self.cusp_blocks:
            rows.append(hstack(*[mp_of_acb(self._eval(bl[g], i, j, lam)) for g in self.gens]))
        return vstack(*rows)

    def gen_matrix(self, g, i, j, lam):
        key, P = self.gen_class[g]
        return mp_of_acb((self._chi(key, i, j, lam) * P).mid())

    def cusp_matrix(self, k, i, j, lam):
        key, P = self.cusp_words[k]
        return mp_of_acb((self._chi(key, i, j, lam) * P).mid())


def lam_of(sign, i, j, D, kappa):
    """nu(t) for nu|F = (zeta^i, zeta^j) and nu(t') = kappa (acb): kappa for +, kappa zeta^-(i+j) for - (t' = abt)"""
    return kappa if sign == "+" else kappa * unit(-(i + j), D)


def h1(gf, i, j, lam):
    """(h1, t0, margins) of nu (x) rho"""
    mg = Margins()
    d = gf.d
    J = gf.fox(i, j, lam)
    rJ = svd_rank(J, mg)[0]
    B = vstack(*[gf.gen_matrix(g, i, j, lam) - mp.eye(d) for g in gf.gens])
    rB = svd_rank(B, mg, scale=mp.mpf(1))[0]
    C = vstack(*[gf.cusp_matrix(k, i, j, lam) - mp.eye(d) for k in range(2)])
    t0 = d - svd_rank(C, mg, scale=mp.mpf(1))[0]
    return (3 * d - rJ) - rB, t0, mg


# ============================================================================================ Part C
def omega_matrix():
    """alpha ^ beta on Lambda^2 C^4 in the basis e_ij (i < j), against e_0 ^ e_1 ^ e_2 ^ e_3"""
    idx = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    W = mp.matrix(6, 6)
    for a, (i, j) in enumerate(idx):
        for b, (k, m) in enumerate(idx):
            perm = (i, j, k, m)
            if len(set(perm)) == 4:
                inv = sum(1 for x in range(4) for y in range(x + 1, 4) if perm[x] > perm[y])
                W[a, b] = -1 if inv % 2 else 1
    return W


OMEGA = omega_matrix()


def torus_pairing(z, w, P1, P2, d):
    """the cup product of two 1-cocycles of P = <p1, p2> (values (z(p1), z(p2)) stacked) on [p1|p2] - [p2|p1]"""
    z1, z2 = z[:d, 0], z[d:, 0]
    w1, w2 = w[:d, 0], w[d:, 0]
    a = (z1.T * OMEGA * (P1 * w2))[0, 0]
    b = (z2.T * OMEGA * (P2 * w1))[0, 0]
    return a - b


def lambda_meet_pi(gf2, i, j, lam):
    """Part C at the character (zeta^i, zeta^j, lam) for Lambda^2 rho (gf2: GroupedFox of Lambda^2 rho); the character must be
    trivial on P"""
    mg = Margins()
    d = gf2.d
    assert d == 6
    J = gf2.fox(i, j, lam)
    Z = null_basis(J, mg)
    R = gf2.restriction(i, j, lam)
    RZ = R * Z
    P1, P2 = gf2.cusp_matrix(0, i, j, lam), gf2.cusp_matrix(1, i, j, lam)
    I6 = mp.eye(d)
    triv = max(mp.mnorm(P1 - gf2.cusp_matrix(0, 0, 0, mp.mpc(1)), 1), mp.mnorm(P2 - gf2.cusp_matrix(1, 0, 0, mp.mpc(1)), 1))
    BD = vstack(P1 - I6, P2 - I6)
    rBD = svd_rank(BD, mg, scale=mp.mpf(1))[0]
    F = null_basis(vstack(P1 - I6, P2 - I6), mg)                       # the P-fixed vectors (2-dim)
    pis = []
    for k in range(F.cols):
        f = F[:, k]
        zero = mp.matrix(d, 1)
        pis.append(vstack(f, zero))
        pis.append(vstack(zero, f))
    Pi = hstack(*pis)
    dimLam = svd_rank(hstack(BD, RZ), mg)[0] - rBD
    dimPi = svd_rank(hstack(BD, Pi), mg)[0] - rBD
    dimSum = svd_rank(hstack(BD, RZ, Pi), mg)[0] - rBD
    meet_rank = dimLam + dimPi - dimSum
    # the pairing
    scale = max(mp.mpf(1), mp.mnorm(RZ, 1)) * max(mp.mpf(1), mp.mnorm(Pi, 1))
    Gm = mp.matrix(RZ.cols, Pi.cols)
    for a in range(RZ.cols):
        for b in range(Pi.cols):
            Gm[a, b] = torus_pairing(RZ[:, a], Pi[:, b], P1, P2, d)
    rG = svd_rank(Gm, mg, scale=scale)[0]
    # isotropy checks
    iso_lam = max((abs(torus_pairing(RZ[:, a], RZ[:, b], P1, P2, d)) for a in range(RZ.cols) for b in range(RZ.cols)),
                  default=mp.mpf(0)) / scale
    iso_pi = max((abs(torus_pairing(Pi[:, a], Pi[:, b], P1, P2, d)) for a in range(Pi.cols) for b in range(Pi.cols)),
                 default=mp.mpf(0)) / scale
    return {"h1": Z.cols - (svd_rank(vstack(*[gf2.gen_matrix(g, i, j, lam) - I6 for g in gf2.gens]), mg,
                                     scale=mp.mpf(1))[0]),
            "dim Lambda_A": dimLam, "dim pi_A": dimPi, "dim(Lambda_A meet pi_A) by rank": meet_rank,
            "pairing rank": rG, "dim(Lambda_A meet pi_A) by pairing": dimPi - rG if dimPi == 2 else None,
            "Lambda_A isotropic (rel)": mp.nstr(iso_lam, 3), "pi_A isotropic (rel)": mp.nstr(iso_pi, 3),
            "character on P (deviation)": mp.nstr(triv, 3), "margins": mg.as_dict()}
