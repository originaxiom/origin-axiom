"""B1529 -- route T: the fibre's four-term sequence.  Library; nothing sealed is computed on import.

A word state's group Gamma = F x| <t> (sm:B1527 family_lib.word_group; F = <a, b> free) has the cusp <l, t'> with l = abAB and
t' = t (sign +) or abt (sign -); t' fixes l exactly, and t' g t'^-1 = phi'(g) is a word in a, b (phi' = phi for +, and
ab phi(g) BA for -).  A module V = nu (x) W with nu a character: nu|F = nu0 (a torsion character of F fixed by phi), nu(t') = kappa.

Route T reads everything from the fibre, in four spaces with one operator (PREREGISTRATION section 3, Lemma F):
    0 -> A -> B -> C -> D -> 0,   A = W^l,  B = H^1(F, dF; nu0 (x) W),  C = H^1(F; nu0 (x) W),  D = W_l,
the long exact sequence of the pair (F, dF), dF the circle <l>; exact when H^0(F; nu0 (x) W) = 0 = H^0(F; (nu0 (x) W)*).
The operator is S0, the stable letter t' without its character:
    (S0 z)(g) = W(t')^-1 z(phi'(g))   on cocycles z of F (no nu(t')); on A and D it is W(t')^-1.
Then, with g(X; k) the dimension of the k-eigenspace of S0 on X:
    h^1(Gamma; V) = g(C; kappa),  h^1(Gamma; V*) = g(B; kappa) = g(C'; 1/kappa)  (C' the same space for nu^-1 (x) W*),
    t0 = g(A; kappa),  s0 = g(D; kappa),  a0 = b0 = 0,
    I(V) = [g(B; kappa) - g(A; kappa)] - [g(C; kappa) - g(D; kappa)]   (Lemma E of sm:B1527),
and I(V) != 0 only if kappa is a root of the interior polynomial chi_K = chi_C / chi_D (= chi_B / chi_A).

C is computed as the d x d matrix T_C of S0 on Z^1/B^1 in the basis of cocycles vanishing on b (or on a, whichever slot is
better conditioned):  Z^1 = W^2 (the values on a, b), B^1 = {(X v, Y v)}, X = nu0(a) W(a) - 1, Y = nu0(b) W(b) - 1,
    T_C = S_aa - X Y^-1 S_ba   (slot b),    T_C = S_bb - Y X^-1 S_ab   (slot a),    S_gh = W(t')^-1 d phi'(g) / d h,
with the Fox derivatives in the left convention of sm:B1527's cusp_lib (z(gh) = z(g) + g.z(h)).  The Fox derivatives depend on
the character only through nu0(prefix) = zeta^(i e_a + j e_b) (u = (i/D, j/D), zeta = e^{2 pi i / D}, (e_a, e_b) the prefix's
exponent sums), so each derivative is precomputed once per module as a sum over residue classes of (e_a, e_b) mod D, and a
character costs one small product (python-flint's acb_mat, at PREC bits).

Decisions: eigenvalue multiplicities (am) from the Taylor coefficients of chi_C at kappa (the order of vanishing, with the margin
between the largest coefficient read as zero and the first read as non-zero, both relative to the largest); eigenspace
dimensions (g) by singular values at mp.dps = 60 (mpmath), with REL_TOL and margins as sm:B1527's cusp_lib.

This is new code for B1529.  It shares the presentation (family_lib.word_group) and the hyperbolic point (family_lib) with
sm:B1527, and no linear algebra with cusp_lib's Fox route or wang_lib's route W."""
import importlib.util
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
from flint import acb, acb_mat, acb_poly, ctx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1527 = ROOT / "frontier" / "B1527_the_cusp_decides" / "verification"

PREC = 320                                   # python-flint working precision, bits (about 96 digits)
DPS = 60                                     # mpmath precision for the singular values
REL_TOL = mp.mpf(10) ** -30                  # a singular value below REL_TOL * (largest) is zero (as cusp_lib)
AM_ZERO = mp.mpf(10) ** -30                  # a Taylor coefficient below AM_ZERO * (largest) is zero
SLOT_MIN = mp.mpf(10) ** -6                  # below this a slot matrix is not used (the orthogonal complement instead)


def load_b1527(name):
    """sm:B1527's modules, by path (they import each other by bare name, so their directory goes on sys.path)"""
    if str(B1527) not in sys.path:
        sys.path.insert(0, str(B1527))
    spec = importlib.util.spec_from_file_location(name, B1527 / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return sys.modules[name]


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


def tprime(sign):
    return "t" if sign == "+" else "abt"


def phi_prime(sign, img):
    """t' g t'^-1 as a word in a, b"""
    if sign == "+":
        return dict(img)
    return {g: free_reduce("ab" + img[g] + "BA") for g in "ab"}


# ============================================================================================ conversions
def to_acb(x):
    x = mp.mpc(x)
    return acb(mp.nstr(mp.re(x), mp.mp.dps + 5, strip_zeros=False), mp.nstr(mp.im(x), mp.mp.dps + 5, strip_zeros=False))


def acb_of_mp(M):
    return acb_mat([[to_acb(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])


def mp_of_acb(M):
    out = mp.matrix(M.nrows(), M.ncols())
    for i, row in enumerate(M.tolist()):
        for j, z in enumerate(row):
            out[i, j] = mp.mpc(mp.mpf(z.real.mid().str(DPS + 10, radius=False)), mp.mpf(z.imag.mid().str(DPS + 10, radius=False)))
    return out


def mp_of_acb_scalar(z):
    return mp.mpc(mp.mpf(z.real.mid().str(DPS + 10, radius=False)), mp.mpf(z.imag.mid().str(DPS + 10, radius=False)))


def root_of_unity(k, D):
    """e^{2 pi i k / D} as an acb"""
    if D == 1 or k % D == 0:
        return acb(1)
    return (acb.pi() * acb(0, 2 * (k % D)) / D).exp()


# ============================================================================================ the module on the fibre
class FibreModule:
    """W on Gamma's generators (mpmath matrices for a, b, t), with the Fox derivatives of phi'(a), phi'(b) precomputed by
    residue class of the prefix's exponent sums mod D."""

    def __init__(self, sign, img, mats, D):
        ctx.prec = PREC
        self.sign, self.D = sign, D
        self.d = mats["a"].rows
        self.phi = phi_prime(sign, img)
        M = {g: acb_of_mp(mats[g]) for g in "abt"}
        Mi = {g: acb_of_mp(mp.inverse(mats[g])) for g in "abt"}
        self.M, self.Mi = M, Mi
        self.Wt = self.word(tprime(sign))                                              # W(t')
        self.Wti = acb_of_mp(mp.inverse(mp_of_acb(self.Wt)))
        # the Fox derivatives d phi'(g) / d h, h = a, b, by residue class of (e_a, e_b) mod D
        self.fox = {}
        for g in "ab":
            for h in "ab":
                self.fox[(g, h)] = self._fox_classes(self.phi[g], h)

    def word(self, w):
        X = acb_mat(self.d, self.d, [1 if i == j else 0 for i in range(self.d) for j in range(self.d)])
        for c in w:
            X = (X * (self.M[c] if c.islower() else self.Mi[c.lower()])).mid()
        return X

    def _fox_classes(self, w, h):
        d, D = self.d, self.D
        P = acb_mat(d, d, [1 if i == j else 0 for i in range(d) for j in range(d)])
        ea = eb = 0
        out = {}

        def add(key, X, sgn):
            if key in out:
                out[key] = (out[key] + X if sgn > 0 else out[key] - X).mid()
            else:
                out[key] = X if sgn > 0 else -X
        for c in w:
            if c.islower():
                if c == h:
                    add((ea % D, eb % D), P, +1)
                P = (P * self.M[c]).mid()
                ea, eb = ea + (c == "a"), eb + (c == "b")
            else:
                P = (P * self.Mi[c.lower()]).mid()
                ea, eb = ea - (c == "A"), eb - (c == "B")
                if c.lower() == h:
                    add((ea % D, eb % D), P, -1)
        return out

    def fox_at(self, g, h, i, j):
        """d phi'(g) / d h evaluated in nu0 (x) W, nu0 = (zeta^i, zeta^j)"""
        d, D = self.d, self.D
        S = acb_mat(d, d)
        for (ea, eb), X in self.fox[(g, h)].items():
            S = (S + root_of_unity(i * ea + j * eb, D).mid() * X).mid()
        return S

    def T_C(self, i, j):
        """S0 on C = H^1(F; nu0 (x) W) as a d x d matrix: (T, slot, conditioning).  The basis is the cocycles vanishing on b
        (slot "b": T = S_aa - X Y^-1 S_ba) or on a (slot "a": T = S_bb - Y X^-1 S_ab), whichever slot matrix is better
        conditioned (|det| over the product of its column norms); when both are below SLOT_MIN (a module with a trivial
        subquotient on a generator), the orthogonal complement of B^1 in W^2 (slot "perp": T = Q^H S0 Q, Q an orthonormal basis
        of im(d)^perp by singular vectors)."""
        d = self.d
        Id = acb_mat(d, d, [1 if r == c else 0 for r in range(d) for c in range(d)])
        X = (root_of_unity(i, self.D).mid() * self.M["a"] - Id).mid()
        Y = (root_of_unity(j, self.D).mid() * self.M["b"] - Id).mid()
        cond = {}
        for name, Z in (("b", Y), ("a", X)):
            Zm = mp_of_acb(Z)
            cn = mp.mpf(1)
            for c in range(d):
                cn *= mp.norm(Zm[:, c])
            cond[name] = abs(mp.det(Zm)) / cn if cn else mp.mpf(0)
        slot = "b" if cond["b"] >= cond["a"] else "a"
        if cond[slot] >= SLOT_MIN:
            if slot == "b":
                S_aa = (self.Wti * self.fox_at("a", "a", i, j)).mid()
                S_ba = (self.Wti * self.fox_at("b", "a", i, j)).mid()
                Yi = acb_of_mp(mp.inverse(mp_of_acb(Y)))
                return (S_aa - ((X * Yi).mid() * S_ba).mid()).mid(), slot, cond[slot]
            S_bb = (self.Wti * self.fox_at("b", "b", i, j)).mid()
            S_ab = (self.Wti * self.fox_at("a", "b", i, j)).mid()
            Xi = acb_of_mp(mp.inverse(mp_of_acb(X)))
            return (S_bb - ((Y * Xi).mid() * S_ab).mid()).mid(), slot, cond[slot]
        # the orthogonal complement of B^1 = im [X; Y]
        with mp.workdps(DPS + 20):
            Bm = vstack_mp(mp_of_acb(X), mp_of_acb(Y))
            U, Sv, V = mp.svd_c(Bm, full_matrices=True)
            sv = [abs(Sv[k]) for k in range(d)]
            Q = mp.matrix(2 * d, d)
            for k in range(d):
                for r in range(2 * d):
                    Q[r, k] = U[r, d + k]
            S0 = mp.matrix(2 * d, 2 * d)
            for bi, g in enumerate("ab"):
                for bj, h in enumerate("ab"):
                    Bk = mp_of_acb((self.Wti * self.fox_at(g, h, i, j)).mid())
                    for r in range(d):
                        for c in range(d):
                            S0[bi * d + r, bj * d + c] = Bk[r, c]
            Tm = Q.H * S0 * Q
            return acb_of_mp(Tm), "perp", min(sv) / max(sv)

    def fibre_invariants(self, i, j):
        """dim H^0(F; nu0 (x) W) (must be 0 for route T), with its margin"""
        d = self.d
        Id = mp.eye(d)
        A = mp_of_acb(self.M["a"]) * mp.mpc(mp_of_acb_scalar(root_of_unity(i, self.D))) - Id
        B = mp_of_acb(self.M["b"]) * mp.mpc(mp_of_acb_scalar(root_of_unity(j, self.D))) - Id
        return d - rank_mp(vstack_mp(A, B))[0]


# ============================================================================================ decisions
def svals(A):
    S = mp.svd_c(A, compute_uv=False)
    return sorted([abs(S[i]) for i in range(min(A.rows, A.cols))], reverse=True)


def rank_mp(A, scale=None):
    """(rank, smallest kept / largest, largest dropped / largest).  With scale, a matrix whose largest singular value is below
    REL_TOL * scale is the zero matrix (a relative threshold alone would read rounding noise as full rank)."""
    with mp.workdps(DPS):
        s = svals(A)
        if not s or s[0] == 0 or (scale is not None and s[0] <= REL_TOL * scale):
            return 0, None, (s[0] / scale if s and scale else None)
        r = sum(1 for x in s if x > REL_TOL * s[0])
        kept = s[r - 1] / s[0] if r > 0 else None
        dropped = s[r] / s[0] if r < len(s) else None
        return r, kept, dropped


def vstack_mp(*mats):
    cols = mats[0].cols
    out = mp.matrix(sum(M.rows for M in mats), cols)
    r = 0
    for M in mats:
        for i in range(M.rows):
            for j in range(cols):
                out[r + i, j] = M[i, j]
        r += M.rows
    return out


def g_at(T, kappa):
    """dim ker(T - kappa) for an acb_mat T and an acb (or mp) kappa, by singular values: (g, kept, dropped)"""
    with mp.workdps(DPS):
        Tm = mp_of_acb(T)
        k = kappa if isinstance(kappa, (mp.mpc, mp.mpf)) else mp_of_acb_scalar(kappa)
        scale = max(mp.mpf(1), abs(k), mp.mnorm(Tm, 1))
        r, kept, dropped = rank_mp(Tm - k * mp.eye(Tm.rows), scale)
        return Tm.rows - r, kept, dropped


def taylor(p, kappa):
    """the Taylor coefficients of the polynomial p at kappa: p(kappa + y) = sum c_k y^k"""
    return (p(acb_poly([kappa, acb(1)]))).coeffs()


def order_at(p, kappa):
    """the order of vanishing of p at kappa, read from its Taylor coefficients: (order, largest read as zero, first read as
    non-zero), both relative to the largest coefficient"""
    c = [abs(mp_of_acb_scalar(x)) for x in taylor(p, kappa)]
    top = max(c)
    k = 0
    while k < len(c) and c[k] <= AM_ZERO * top:
        k += 1
    zero = max(c[:k]) / top if k > 0 else None
    nonzero = c[k] / top if k < len(c) else None
    return k, zero, nonzero


def charpoly(T):
    return T.charpoly()


# ============================================================================================ the cusp's two ends of the sequence
def cusp_ends(Wl, Wt):
    """A = W^l and D = W_l with W(t')^-1 acting (mpmath matrices in, mpmath matrices out): (T_A, T_D, e, margins).
    A: an orthonormal basis K of ker(W(l) - 1), T_A = K^H W(t')^-1 K.  D: an orthonormal basis Q of im(W(l) - 1)^perp,
    T_D = Q^H W(t')^-1 Q (the image is W(t')-invariant, so the orthogonal projection is the projection along it)."""
    with mp.workdps(DPS):
        d = Wl.rows
        N = Wl - mp.eye(d)
        U, S, V = mp.svd_c(N, full_matrices=True)
        s = [abs(S[i]) for i in range(d)]
        top = max(s)
        r = sum(1 for x in s if x > REL_TOL * top)
        e = d - r
        Wti = mp.inverse(Wt)
        K = mp.matrix(d, e)
        Q = mp.matrix(d, e)
        for k in range(e):
            for i in range(d):
                K[i, k] = mp.conj(V[r + k, i])
                Q[i, k] = U[i, r + k]
        TA = K.H * Wti * K if e else mp.matrix(0, 0)
        TD = Q.H * Wti * Q if e else mp.matrix(0, 0)
        margins = {"kept": s[r - 1] / top if r else None, "dropped": s[r] / top if r < d else None}
        return TA, TD, e, margins


def g_mp(T, kappa):
    if T.rows == 0:
        return 0
    with mp.workdps(DPS):
        scale = max(mp.mpf(1), abs(kappa), mp.mnorm(T, 1))
        return T.rows - rank_mp(T - kappa * mp.eye(T.rows), scale)[0]


def interior_value(chiC, TD, kappa):
    """chi_K(kappa) = (chi_C / chi_D)(kappa), with the division's remainder (relative), and |chi_K(kappa)| relative to
    chi_K's largest coefficient"""
    if TD.rows == 0:
        chiD = acb_poly([acb(1)])
    else:
        chiD = acb_of_mp(TD).charpoly()
    q, r = divmod(chiC, chiD)
    rc = [abs(mp_of_acb_scalar(x)) for x in r.coeffs()] or [mp.mpf(0)]
    cc = [abs(mp_of_acb_scalar(x)) for x in chiC.coeffs()]
    qc = [abs(mp_of_acb_scalar(x)) for x in q.coeffs()]
    val = abs(mp_of_acb_scalar(q(kappa if isinstance(kappa, acb) else to_acb(kappa))))
    return {"chi_K(kappa) rel": val / max(qc), "remainder rel": max(rc) / max(cc), "deg chi_K": q.degree()}


# ============================================================================================ a state's modules (shared by the instruments)
def dual_mats(mats):
    return {g: mp.inverse(mats[g]).T for g in mats}


def wedge_mats(mats):
    L = load_b1527("cusp_lib")
    return {g: L.wedge2(mats[g]) for g in mats}


def int_char(u, D):
    return int(u[0] * D), int(u[1] * D)


def kappa_of(sign, i, j, D, lam):
    """nu(t') for nu = (zeta^i, zeta^j, lam): lam for +, zeta^(i+j) lam for - (t' = abt)"""
    if sign == "+":
        return mp.mpc(lam)
    return mp.expjpi(2 * mp.mpf(i + j) / D) * lam


def hyperbolic_mats(sign, word):
    """the hyperbolic point in Ballas' paraboloid frame (sm:B1527 family_lib, route F seeded), at the ambient precision"""
    FL = load_b1527("family_lib")
    A2, B2, T2, sh = FL.hyperbolic_sl2(sign, word)
    M2 = FL.to_cusp_frame(A2, B2, T2, sign, 0)
    rho = FL.paraboloid_module(M2)
    return {g: rho.M[g] for g in "abt"}


class StateModules:
    """route T's data for one representation of one word state: the four and Lambda^2, each with its dual, and the cusp ends"""

    def __init__(self, sign, img, mats, D):
        L = load_b1527("cusp_lib")
        self.sign, self.D = sign, D
        self.mods = {}
        for name, M in (("4", mats), ("L2", wedge_mats(mats))):
            Md = dual_mats(M)
            W = L.Module(M)
            TA, TD, e, mg = cusp_ends(W.word("abAB"), W.word(tprime(sign)))
            self.mods[name] = {"V": FibreModule(sign, img, M, D), "V*": FibreModule(sign, img, Md, D),
                               "TA": TA, "TD": TD, "e": e, "cusp margins": mg}
        self.cache = {}

    def TC(self, name, which, i, j):
        key = (name, which, i % self.D, j % self.D)
        if key not in self.cache:
            fm = self.mods[name][which]
            self.cache[key] = (fm.T_C(i, j), fm.fibre_invariants(i, j))
        return self.cache[key]

    def row(self, name, i, j, kappa):
        """route T's (h1, h1*, t0, s0, I) for nu (x) W, nu|F = (zeta^i, zeta^j), nu(t') = kappa"""
        (TC, slot, cond), f0 = self.TC(name, "V", i, j)
        (TCd, slotd, condd), f0d = self.TC(name, "V*", -i, -j)
        h1, k1, d1 = g_at(TC, kappa)
        h1s, k2, d2 = g_at(TCd, 1 / kappa)
        m = self.mods[name]
        t0, s0 = g_mp(m["TA"], kappa), g_mp(m["TD"], kappa)
        I = (h1s - t0) - (h1 - s0)
        kept = [x for x in (k1, k2) if x is not None]
        dropped = [x for x in (d1, d2) if x is not None]
        return {"h1": h1, "h1*": h1s, "t0": t0, "s0": s0, "I": I, "H0(F; V), H0(F; V*)": [f0, f0d],
                "slot conditioning": min(cond, condd), "kept": min(kept) if kept else None,
                "dropped": max(dropped) if dropped else None}
