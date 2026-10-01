"""B1511 -- THE PROJECTIVE TOWER: the audit lane's harmonic family (Ballas' rho_q) on the cyclic covers M_n of m004, twisted by
characters of the fibre torsion, with B1509's rank-five extensions on every level.  Library (no sealed quantity is computed on import).

Conventions (B1509's wang_monodromy.py, B1374's index_lib, B1506's the_level.py):
  pi = <m, n | mnMNmNMnmN>, meridian m, longitude nMNmmNMn; epsilon(m) = epsilon(n) = 1.
  Fibre F = ker(epsilon) = <x, y>, free, with x = u0 = n m^-1 and y = u1 = m n m^-2 (u_k = m^k n m^-(k+1), m u_k m^-1 = u_{k+1}).
  phi(g) = m g m^-1:  phi(x) = y,  phi(y) = y x^-1 y y;  abelianised Phi = [[0, -1], [1, 3]] (columns are the images of x, y).
  M_n = the n-fold cyclic cover, pi_n = F x| <z>, z = m^n acting by phi^n; T_n = coker(Phi^n - 1), the torsion of H_1(M_n).
  A character nu of pi_n is (nu_F, lam): nu_F a character of F^ab with nu_F o phi^n = nu_F (a character of T_n), lam = nu(z).
  Exponent form: nu_F(x) = zeta_N^a, nu_F(y) = zeta_N^b; the deck tau (conjugation by m) acts by (a, b) -> (b, 3b - a), lam fixed.
  The twisted background V = nu (x) rho_q:  V(g) = nu_F(g) rho_q(g) on F,  V(z) = lam rho_q(m)^n.

The one-step monodromy.  For ANY character nu_F of F^ab, (S c)(g) = rho_q(m)^-1 c(phi(g)) maps the nu_F-twisted cocycles
Z^1(F; nu_F (x) rho_q) to the (nu_F o phi)-twisted ones (V_{nu o phi}(g) = rho(m)^-1 V_nu(phi g) rho(m)), and maps the coboundary
delta v to delta(rho_q(m)^-1 v).  In the coordinates (c(x), c(y)) in C^8 it is an 8 x 8 matrix S_nu.  Around a level:
S^(n)_nu = S_{nu o phi^(n-1)} ... S_{nu o phi} S_nu = rho_q(m)^-n c(phi^n(.)), an endomorphism of Z^1(F; nu_F (x) rho_q) when
nu_F o phi^n = nu_F; on B^1 it is rho_q(m)^-n (unipotent).  Wang: if H^0(F; nu_F (x) rho_q) = 0, then
H^1(M_n; V) = ker(lam^-1 S^(n) - 1) and H^2(M_n; V) = coker(lam^-1 S^(n) - 1) on H^1(F; nu_F (x) rho_q) = Z^1 / B^1 (dimension 4),
and cup with the fibration class is the natural map ker -> coker.

Arithmetic: sympy DomainMatrix over Q(q) or Q(i)(q) (symbolic), over Q(i)[q]/(g) (FiniteExtension: exact at an algebraic q), or
B1374's index_lib over GF(p)."""
import importlib.util
import itertools
import math
from functools import reduce
from pathlib import Path

import sympy as sp
from sympy.polys.agca.extensions import FiniteExtension
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location("b1374_index_lib", ROOT / "frontier/B1374_the_class_index_in_the_sm_frame/verification/index_lib.py")
IL = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(IL)

Q = sp.Symbol("q")
S_ = sp.Symbol("s")
Q12 = sp.QQ.algebraic_field(sp.sqrt(-3), sp.I)          # Q(zeta_12) = Q(sqrt -3, i)
WORD_R = "mnMNmNMnmN"
WORD_L = "nMNmmNMn"
FIBRE = {"x": "nM", "y": "mnMM"}
PHI = {"x": "y", "y": "yXyy"}
PHI_AB = sp.Matrix([[0, -1], [1, 3]])
Q_MONIC = sp.expand((-Q * S_ ** 4 + 8 * Q * S_ ** 3 + (Q ** 2 - 16 * Q + 1) * S_ ** 2 + 8 * Q * S_ - Q) / (-Q))   # B1509 T3


# ============================================================================================ words
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


def apply(phi, w):
    return red("".join(phi[c] if c.islower() else inv(phi[c.lower()]) for c in w))


def phi_power(k):
    img = {"x": "x", "y": "y"}
    for _ in range(k):
        img = {g: apply(PHI, img[g]) for g in "xy"}
    return img


def fibre_word_in_mn(w):
    """a word in x, y as a word in m, n"""
    return red("".join(FIBRE[c] if c.islower() else inv(FIBRE[c.lower()]) for c in w))


# ============================================================================================ the family
def ballas(qq):
    t = sp.sympify(qq) / 2
    m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
    n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return m, n


def word_matrix(mats, w):
    d = mats["m"].shape[0]
    X = sp.eye(d)
    for ch in w:
        X = X * (mats[ch] if ch.islower() else mats[ch.lower()].inv())
    return X


def symbolic_mats(dual=False):
    m, n = ballas(Q)
    if dual:
        m, n = m.inv().T, n.inv().T
    return {"m": m.applyfunc(sp.cancel), "n": n.applyfunc(sp.cancel)}


# ============================================================================================ fields
class Field:
    """a target field for the entries: 'sym' (Q(i)(q) or Q(q)), 'ext' (Q(i)[q]/(g)), or 'gf' (GF(p) with q = r, i = iota)."""

    def __init__(self, kind, g=None, p=None, r=None, iota=None, gaussian=True, base=None):
        self.kind = kind
        self.base = base or ("QI" if gaussian else "Q")
        if kind in ("sym", "ext"):
            bdom = {"Q": sp.QQ, "QI": sp.QQ_I, "Q12": Q12}[self.base]
        if kind == "sym":
            self.dom = bdom.frac_field(Q)
        elif kind == "ext":
            self.g = sp.Poly(g, Q, domain=bdom)
            self.dom = FiniteExtension(self.g)
        elif kind == "gf":
            self.p, self.r, self.iota = p, r % p, (iota % p if iota is not None else None)
            self.dom = sp.GF(p)
        else:
            raise ValueError(kind)

    def conv(self, e):
        """a rational function of q with Gaussian-rational coefficients -> the field"""
        e = sp.sympify(e)
        if self.kind == "sym":
            return self.dom.from_sympy(sp.cancel(e))
        num, den = sp.fraction(sp.cancel(sp.together(e)))
        if self.kind == "ext":
            return self.dom.convert(sp.expand(num)) * self.dom.convert(sp.expand(den)) ** -1
        p = self.p
        nv = self._gf_eval(sp.expand(num))
        dv = self._gf_eval(sp.expand(den))
        assert dv % p, ("denominator vanishes mod p", e, p)
        return self.dom(nv * pow(dv, p - 2, p) % p)

    def _gf_eval(self, poly_expr):
        p = self.p
        P = sp.Poly(poly_expr, Q, sp.I) if poly_expr.has(sp.I) else sp.Poly(poly_expr, Q)
        tot = 0
        for monom, coeff in P.terms():
            c = int(sp.Rational(coeff).p) * pow(int(sp.Rational(coeff).q), p - 2, p) % p
            v = pow(self.r, monom[0], p)
            if len(monom) > 1 and monom[1]:
                assert self.iota is not None
                v = v * pow(self.iota, monom[1], p) % p
            tot = (tot + c * v) % p
        return tot

    def unit(self, k, N):
        """zeta_N^k, for N | 4 exactly (values in Q(i)); other N only over GF(p)"""
        k %= N
        if self.kind == "gf":
            if N == 1:
                return self.dom(1)
            z = IL.GF(self.p).root_of_unity(N)
            if N == 4:
                z = self.iota
            return self.dom(pow(z, k, self.p))
        if self.base == "Q12":
            assert 12 % N == 0, ("Q(zeta12) carries only the twelfth roots of unity", N)
            return self.conv(sp.nsimplify(sp.cos(2 * sp.pi * k / N)) + sp.I * sp.nsimplify(sp.sin(2 * sp.pi * k / N)))
        assert 4 % N == 0, ("this exact field carries only the fourth roots of unity", N)
        return self.conv(sp.I ** (4 // N * k))

    def mat(self, M):
        rows = [[self.conv(M[i, j]) for j in range(M.shape[1])] for i in range(M.shape[0])]
        return DomainMatrix(rows, M.shape, self.dom)


def gf_root_of_unity(p, N, iota=None):
    if N == 4 and iota is not None:
        return iota % p
    return IL.GF(p).root_of_unity(N)


# ============================================================================================ the twisted fibre monodromy
def char_value_exponent(ab, w):
    """the exponent of nu_F on a word in x, y, for nu_F(x) = zeta^a, nu_F(y) = zeta^b"""
    a, b = ab
    e = 0
    for ch in w:
        s = 1 if ch.islower() else -1
        e += s * (a if ch.lower() == "x" else b)
    return e


def deck(ab, N):
    """nu_F -> nu_F o phi in exponent form"""
    a, b = ab
    return (b % N, (3 * b - a) % N)


class FibreMonodromy:
    """rho_q (or its dual) on the fibre over a Field, and the one-step twisted monodromy S_nu"""

    def __init__(self, field, dual=False, mats=None):
        self.F = field
        mats = mats or symbolic_mats(dual)
        self.rx = field.mat(word_matrix(mats, FIBRE["x"]))
        self.ry = field.mat(word_matrix(mats, FIBRE["y"]))
        self.mm = field.mat(mats["m"])
        self.minv = field.mat(mats["m"].inv().applyfunc(sp.cancel))
        self.d = 4
        self.I = DomainMatrix.eye(4, field.dom)

    def V(self, ab, N):
        return {"x": self.rx * self.F.unit(ab[0], N), "y": self.ry * self.F.unit(ab[1], N)}

    def cocycle_value(self, word, g, z):
        d, dom = self.d, self.F.dom
        val = DomainMatrix.zeros((d, 1), dom)
        pre = DomainMatrix.eye(d, dom)
        for ch in word:
            if ch.islower():
                val = val + pre * z[ch]
                pre = pre * g[ch]
            else:
                ginv = dm_inv(g[ch.lower()])
                val = val - pre * ginv * z[ch.lower()]
                pre = pre * ginv
        return val

    def one_step(self, ab, N):
        """S_nu: Z^1(F; nu) -> Z^1(F; nu o phi), 8 x 8 in the coordinates (c(x), c(y))"""
        d, dom = self.d, self.F.dom
        g = self.V(ab, N)
        cols = []
        for j in range(2 * d):
            e = [DomainMatrix.zeros((d, 1), dom), DomainMatrix.zeros((d, 1), dom)]
            e[j // d] = DomainMatrix([[dom.one if i == j % d else dom.zero] for i in range(d)], (d, 1), dom)
            z = {"x": e[0], "y": e[1]}
            top = self.minv * self.cocycle_value(PHI["x"], g, z)
            bot = self.minv * self.cocycle_value(PHI["y"], g, z)
            cols.append(top.vstack(bot))
        return cols[0].hstack(*cols[1:])

    def coboundary(self, ab, N):
        g = self.V(ab, N)
        return (g["x"] - self.I).vstack(g["y"] - self.I)

    def level(self, ab, N, n):
        """S^(n)_nu as the product of n one-step matrices (nu_F o phi^n = nu_F is asserted), and B for nu"""
        cur = tuple(x % N for x in ab)
        S = DomainMatrix.eye(8, self.F.dom)
        for _ in range(n):
            S = self.one_step(cur, N) * S
            cur = deck(cur, N)
        assert cur == tuple(x % N for x in ab), ("the character is not fixed by phi^n", ab, N, n)
        return S, self.coboundary(ab, N)

    def level_by_words(self, ab, N, n):
        """the same S^(n) computed directly from the words phi^n(x), phi^n(y) (a check of the factorisation)"""
        d, dom = self.d, self.F.dom
        g = self.V(ab, N)
        img = phi_power(n)
        mninv = DomainMatrix.eye(d, dom)
        for _ in range(n):
            mninv = mninv * self.minv
        cols = []
        for j in range(2 * d):
            e = [DomainMatrix.zeros((d, 1), dom), DomainMatrix.zeros((d, 1), dom)]
            e[j // d] = DomainMatrix([[dom.one if i == j % d else dom.zero] for i in range(d)], (d, 1), dom)
            z = {"x": e[0], "y": e[1]}
            cols.append((mninv * self.cocycle_value(img["x"], g, z)).vstack(mninv * self.cocycle_value(img["y"], g, z)))
        return cols[0].hstack(*cols[1:])


def dm_equal(A, B):
    """equality of DomainMatrices regardless of their internal (dense or sparse) format"""
    return A.shape == B.shape and (A - B).is_zero_matrix


# ---- linear algebra over the exact fields.  sympy's fraction-free elimination needs exact division in the representing ring, which
# Q(i)[q]/(g) (FiniteExtension) does not provide; plain Gauss-Jordan with field inverses is used there and over GF(p).
def _own_ge(dom):
    return isinstance(dom, FiniteExtension) or getattr(dom, "is_FiniteField", False)


def _rref(rows, ncols, dom):
    A = [list(r) for r in rows]
    piv, r = [], 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(A)) if A[i][c] != dom.zero), None)
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        inv_ = dom.one / A[r][c]
        A[r] = [x * inv_ for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != dom.zero:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        if r == len(A):
            break
    return A, piv


def dm_rank(M):
    if M.shape[0] == 0 or M.shape[1] == 0:
        return 0
    if not _own_ge(M.domain):
        return M.rank()
    return len(_rref(M.to_list(), M.shape[1], M.domain)[1])


def dm_nullspace(M):
    """a basis of {x : M x = 0} as a list of column DomainMatrices"""
    dom, n = M.domain, M.shape[1]
    if not _own_ge(dom):
        N = M.nullspace()
        return [N[i:i + 1, :].transpose() for i in range(N.shape[0])] if N.shape[0] else []
    A, piv = _rref(M.to_list(), n, dom)
    free = [c for c in range(n) if c not in piv]
    out = []
    for f in free:
        v = [dom.zero] * n
        v[f] = dom.one
        for i, pc in enumerate(piv):
            v[pc] = -A[i][f]
        out.append(DomainMatrix([[x] for x in v], (n, 1), dom))
    return out


def dm_inv(M):
    dom, n = M.domain, M.shape[0]
    if not _own_ge(dom):
        return M.inv()
    rows = [list(r) + [dom.one if i == j else dom.zero for j in range(n)] for i, r in enumerate(M.to_list())]
    A, piv = _rref(rows, n, dom)
    assert piv == list(range(n)), "singular"
    return DomainMatrix([r[n:] for r in A], (n, n), dom)


def charpoly_on_H1(S):
    """the characteristic polynomial of S on Z^1 / B^1, as a sympy expression in s: charpoly(S on Z^1) / (s - 1)^4 (B^1 part
    unipotent), with the division asserted exact"""
    dom = S.domain
    coeffs = [dom.to_sympy(c) for c in S.charpoly()]
    full = sp.Poly(coeffs, S_)
    quo, rem = sp.div(full, sp.Poly((S_ - 1) ** 4, S_))
    assert rem.is_zero, "the B^1 part is not (s - 1)^4"
    return quo.as_expr()


def kernel_dims_on_H1(S, B, lam, maxpow=4):
    """dim ker (S - lam)^j on H^1 = Z^1/B^1 for j = 1..maxpow: 8 - rank[(S - lam)^j | B]"""
    dom = S.domain
    N = S - DomainMatrix.eye(8, dom) * lam
    out = []
    P = DomainMatrix.eye(8, dom)
    for _ in range(maxpow):
        P = P * N
        out.append(8 - dm_rank(P.hstack(B)))
    return out


# ============================================================================================ torsion and characters
def torsion(n):
    A = PHI_AB ** n - sp.eye(2)
    from sympy.matrices.normalforms import smith_normal_form
    D = smith_normal_form(A, domain=sp.ZZ)
    inv_f = [abs(int(D[i, i])) for i in range(2) if abs(int(D[i, i])) != 1]
    return inv_f, abs(int(A.det()))


def characters(n):
    """all characters of T_n in exponent form (a, b) mod N, N = the exponent of T_n (lcm of the invariant factors)"""
    inv_f, order = torsion(n)
    N = reduce(lambda u, v: u * v // math.gcd(u, v), inv_f, 1)
    A = PHI_AB ** n - sp.eye(2)
    out = []
    for a, b in itertools.product(range(N), repeat=2):
        row = sp.Matrix([[a, b]]) * A
        if all(int(x) % N == 0 for x in row):
            out.append((a, b))
    assert len(out) == order, (n, len(out), order)
    return out, N


def orbits(chars, N):
    seen, out = set(), []
    for c in chars:
        if c in seen:
            continue
        orb = [c]
        cur = deck(c, N)
        while cur != c:
            orb.append(cur)
            cur = deck(cur, N)
        for x in orb:
            seen.add(x)
        out.append(orb)
    return out


def order_of(ab, N):
    return N // math.gcd(N, math.gcd(ab[0], ab[1]))


# ============================================================================================ the Reidemeister-Schreier covers
LETTERS = "z" + "".join(f"{k}" for k in range(10))


def rs_cover(n):
    """pi_1(M_n) on the transversal m^k: generators z = m^n and y_k = m^k n m^-(k+1) (k < n-1), y_{n-1} = m^(n-1) n.
    Generator names: 'z' and 'a', 'b', ... (y_0, y_1, ...); upper case is the inverse."""
    names = ["z"] + [chr(ord("a") + k) for k in range(n)]
    words = {"z": "m" * n}
    for k in range(n):
        words[names[k + 1]] = "m" * k + "n" + ("M" * (k + 1) if k < n - 1 else "")

    def rewrite(w, k=0):
        out = []
        for ch in w:
            if ch == "m":
                if k == n - 1:
                    out.append("z")
                k = (k + 1) % n
            elif ch == "M":
                if k == 0:
                    out.append("Z")
                k = (k - 1) % n
            elif ch == "n":
                out.append(names[k + 1])
                k = (k + 1) % n
            elif ch == "N":
                k = (k - 1) % n
                out.append(names[k + 1].upper())
        return "".join(out), k

    rels = []
    for k in range(n):
        r, kk = rewrite(WORD_R, k)
        assert kk == k
        rels.append(r)
    lam, k2 = rewrite(WORD_L)
    assert k2 == 0
    return {"gens": names, "words": words, "rels": rels, "mu": "z", "lam": lam, "rewrite": rewrite, "n": n}


def rs_character_exponents(cov, ab, N, lam_exp, Nl):
    """exponents of nu on the RS generators, as (exponent of zeta_N, exponent of zeta_Nl): nu(z) = lam,
    nu(y_k) = nu_F(u_k) (k < n-1), nu(y_{n-1}) = nu_F(u_{n-1}) lam; u_k = phi^k(x)"""
    n = cov["n"]
    out = {"z": (0, lam_exp)}
    for k in range(n):
        uk = phi_power(k)["x"]
        e = char_value_exponent(ab, uk) % N
        out[cov["gens"][k + 1]] = (e, lam_exp if k == n - 1 else 0)
    return out


def rs_deck(cov):
    """tau = conjugation by m on the RS generators, rewritten from coset 0"""
    out = {}
    for g in cov["gens"]:
        w, k = cov["rewrite"]("m" + cov["words"][g] + "M")
        assert k == 0
        out[g] = red(w)
    return out


# ============================================================================================ modules on a presentation
def rs_rho(cov, field, mats=None):
    mats = mats or symbolic_mats()
    return {g: field.mat(word_matrix(mats, cov["words"][g])) for g in cov["gens"]}


def twisted_rep(cov, field, ab, N, lam_k, Nl, rho=None):
    """V = nu (x) rho_q on the RS generators, nu given by (a, b) mod N on the fibre and lam = zeta_Nl^lam_k"""
    rho = rho or rs_rho(cov, field)
    ex = rs_character_exponents(cov, ab, N, lam_k, Nl)
    out = {}
    for g in cov["gens"]:
        e1, e2 = ex[g]
        out[g] = rho[g] * (field.unit(e1, N) * field.unit(e2, Nl))
    return out


class DMRep:
    """a representation by DomainMatrices on named generators (upper case = inverse), with Fox calculus"""

    def __init__(self, gens, mats):
        self.gens = list(gens)
        self.M = dict(mats)
        self.d = mats[gens[0]].shape[0]
        self.dom = mats[gens[0]].domain
        for g in self.gens:
            self.M[g.upper()] = dm_inv(mats[g])

    def word(self, w):
        X = DomainMatrix.eye(self.d, self.dom)
        for ch in w:
            X = X * self.M[ch]
        return X

    def fox(self, w):
        D = {g: DomainMatrix.zeros((self.d, self.d), self.dom) for g in self.gens}
        pre = DomainMatrix.eye(self.d, self.dom)
        for ch in w:
            g = ch.lower()
            D[g] = D[g] + pre if ch.islower() else D[g] - pre * self.M[ch]
            pre = pre * self.M[ch]
        return D

    def dual(self):
        return DMRep(self.gens, {g: dm_inv(self.M[g]).transpose() for g in self.gens})

    def check(self, rels):
        I = DomainMatrix.eye(self.d, self.dom)
        return all(dm_equal(self.word(r), I) for r in rels)


def cocycle_space(rep, rels):
    """(Z^1 basis as columns of length #gens*d, B^1 matrix): Z^1 = ker of the Fox Jacobian of the relators"""
    gens, d = rep.gens, rep.d
    rows = [rep.fox(r) for r in rels]
    J = None
    for D in rows:
        blk = D[gens[0]].hstack(*[D[g] for g in gens[1:]])
        J = blk if J is None else J.vstack(blk)
    Z = dm_nullspace(J)
    I = DomainMatrix.eye(d, rep.dom)
    B = None
    for g in gens:
        blk = rep.M[g] - I
        B = blk if B is None else B.vstack(blk)
    return Z, B


def h1_classes(rep, rels):
    """a basis of H^1 as cocycles (column vectors), chosen from the Z^1 basis greedily modulo B^1"""
    Z, B = cocycle_space(rep, rels)
    rb = dm_rank(B)
    chosen, cur = [], B
    for z in Z:
        trial = cur.hstack(z)
        if dm_rank(trial) > dm_rank(cur):
            chosen.append(z)
            cur = trial
    return chosen, len(Z) - rb


def extension_rep(rep, coc, line=None):
    """W = [[V, c], [0, L]] on the generators (L = 1 unless a dict of 1 x 1 values is given): c(g) = the cocycle's block on g"""
    gens, d, dom = rep.gens, rep.d, rep.dom
    out = {}
    for i, g in enumerate(gens):
        cg = coc[i * d:(i + 1) * d, :]
        Lg = line[g] if line is not None else DomainMatrix([[dom.one]], (1, 1), dom)
        top = rep.M[g].hstack(cg)
        bot = DomainMatrix.zeros((1, d), dom).hstack(Lg)
        out[g] = top.vstack(bot)
    return DMRep(gens, out)


def wedge2(M):
    """Lambda^2 of a square DomainMatrix in the basis e_i ^ e_j, i < j"""
    d, dom = M.shape[0], M.domain
    pairs = [(i, j) for i in range(d) for j in range(i + 1, d)]
    rows = [[M[i, k].element * M[j, l].element - M[i, l].element * M[j, k].element for (k, l) in pairs] for (i, j) in pairs]
    return DomainMatrix(rows, (len(pairs), len(pairs)), dom)


def wedge2_rep(rep):
    return DMRep(rep.gens, {g: wedge2(rep.M[g]) for g in rep.gens})


def cohomology_data(rep, rels, mu, lam):
    """(a0, a1, t0, t1, r1) exactly over rep's field (index_lib's conventions, any presentation)"""
    d, gens, dom = rep.d, rep.gens, rep.dom
    I = DomainMatrix.eye(d, dom)
    d0 = None
    for g in gens:
        blk = rep.M[g] - I
        d0 = blk if d0 is None else d0.vstack(blk)
    rk0 = dm_rank(d0)
    a0 = d - rk0
    Z, _ = cocycle_space(rep, rels)
    a1 = len(Z) - rk0
    Wm, Wl = rep.word(mu), rep.word(lam)
    Am, Al = Wm - I, Wl - I
    BT = Am.vstack(Al)
    rkBT = dm_rank(BT)
    t0 = d - rkBT
    ZT = (Al * dom.convert(-1)).hstack(Am)
    t1 = 2 * d - dm_rank(ZT) - rkBT
    Dm, Dl = rep.fox(mu), rep.fox(lam)
    Rm = Dm[gens[0]].hstack(*[Dm[g] for g in gens[1:]])
    Rl = Dl[gens[0]].hstack(*[Dl[g] for g in gens[1:]])
    Res = Rm.vstack(Rl)
    if Z:
        cols = Res * (Z[0].hstack(*Z[1:]) if len(Z) > 1 else Z[0])
        r1 = dm_rank(cols.hstack(BT)) - rkBT
    else:
        r1 = 0
    return a0, a1, t0, t1, r1


def index(rep, rels, mu, lam):
    a0, a1, t0, t1, r1 = cohomology_data(rep, rels, mu, lam)
    b0, b1, s0, s1, q1 = cohomology_data(rep.dual(), rels, mu, lam)
    I = (a1 - r1) - (b1 - q1)
    assert r1 + q1 == t1 == s1, ("annihilator identity", r1, q1, t1, s1)
    assert I == (a0 - b0) + s0 - r1, ("B1297 identity", I, a0, b0, s0, r1)
    return {"I": I, "a0": a0, "a1": a1, "t0": t0, "t1": t1, "r1": r1, "b0": b0, "b1": b1, "s0": s0, "q1": q1}


# ============================================================================================ GF(p) through index_lib
def to_il(rep, p):
    """a DMRep over GF(p) -> index_lib's Rep (lists of ints)"""
    F = IL.GF(p)
    mats = {g: [[int(rep.M[g][i, j].element) % p for j in range(rep.d)] for i in range(rep.d)] for g in rep.gens}
    return IL.Rep(F, rep.gens, mats)


def index_gf(rep, rels, mu, lam, p):
    r = to_il(rep, p)
    assert r.check_relators(rels)
    I, (a0, a1, t0, r1), (b0, b1, s0, q1) = IL.index(r, rels, mu, lam)
    return {"I": I, "a0": a0, "a1": a1, "t0": t0, "r1": r1, "b0": b0, "b1": b1, "s0": s0, "q1": q1}


def gf_roots(poly_expr, p, iota=None):
    """roots in GF(p) of a polynomial in q with Gaussian-rational coefficients (i -> iota)"""
    P = sp.Poly(sp.expand(poly_expr), Q, sp.I) if sp.sympify(poly_expr).has(sp.I) else sp.Poly(sp.expand(poly_expr), Q)
    coeffs = {}
    for monom, c in P.terms():
        c = sp.Rational(c)
        v = int(c.p) * pow(int(c.q), p - 2, p) % p
        if len(monom) > 1 and monom[1]:
            v = v * pow(iota, monom[1], p) % p
        coeffs[monom[0]] = (coeffs.get(monom[0], 0) + v) % p
    deg = max(coeffs)
    return [r for r in range(p) if sum(c * pow(r, e, p) for e, c in coeffs.items()) % p == 0]


# ============================================================================================ the closed form of the one-step matrix
# With M = rho(m)^-1, R_x = rho(u0), R_y = rho(u1) and nu_F(x) = X, nu_F(y) = Y, phi(y) = y x^-1 y y gives
#   (S c)(x) = M c_y,   (S c)(y) = M (c_y - V_y V_x^-1 c_x + V_y V_x^-1 c_y + V_y V_x^-1 V_y c_y),
# so S_nu = [[0, A1], [-alpha A2, A1 + alpha A2 + beta A3]] with A1 = M, A2 = M R_y R_x^-1, A3 = M R_y R_x^-1 R_y, alpha = Y/X and
# beta = Y^2/X.  Every entry of A1, A2, A3 is a Laurent polynomial in q with exponents in [-2, 2] (controls), so the entries of
# S^(n) lie in [-2n, 2n] and the coefficients of its characteristic polynomial (and of P on H^1) in [-16n, 16n].
LAURENT_STEP = (-2, 2)


def block_mats(dual=False):
    mats = symbolic_mats(dual)
    Rx = word_matrix(mats, FIBRE["x"]).applyfunc(sp.cancel)
    Ry = word_matrix(mats, FIBRE["y"]).applyfunc(sp.cancel)
    M = mats["m"].inv().applyfunc(sp.cancel)
    A2 = (M * Ry * Rx.inv()).applyfunc(sp.cancel)
    A3 = (M * Ry * Rx.inv() * Ry).applyfunc(sp.cancel)
    return M, A2, A3


def one_step_closed(field, blocks, ab, N):
    """S_nu from the closed form, over a Field (blocks = field.mat of A1, A2, A3)"""
    A1, A2, A3 = blocks
    a, b = ab
    alpha = field.unit(b - a, N)
    beta = field.unit(2 * b - a, N)
    Z = DomainMatrix.zeros((4, 4), field.dom)
    top = Z.hstack(A1)
    bot = (A2 * (-alpha)).hstack(A1 + A2 * alpha + A3 * beta)
    return top.vstack(bot)


# ============================================================================================ GF(p): the twisted polynomials by interpolation
class ModP:
    """the fibre data of rho_q over GF(p) at many q, in plain integer arithmetic; zeta_N and i chosen once per prime"""

    def __init__(self, p, N, dual=False):
        assert (p - 1) % N == 0 and (p - 1) % 4 == 0, (p, N)
        self.p, self.N = p, N
        self.zeta = IL.GF(p).root_of_unity(N)
        self.iota = IL.GF(p).root_of_unity(4)
        A1, A2, A3 = block_mats(dual)
        self.blocks = []
        for A in (A1, A2, A3):
            ent = []
            for i in range(4):
                row = []
                for j in range(4):
                    num, den = sp.fraction(sp.cancel(A[i, j]))
                    row.append((sp.Poly(num, Q).all_coeffs()[::-1], sp.Poly(den, Q).all_coeffs()[::-1]))
                ent.append(row)
            self.blocks.append(ent)

    def _ev(self, coeffs, r):
        p = self.p
        tot = 0
        for e, c in enumerate(coeffs):
            c = sp.Rational(c)
            tot = (tot + int(c.p) * pow(int(c.q), p - 2, p) * pow(r, e, p)) % p
        return tot

    def blocks_at(self, r):
        p = self.p
        out = []
        for ent in self.blocks:
            M = [[0] * 4 for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    nc, dc = ent[i][j]
                    dv = self._ev(dc, r)
                    assert dv, ("pole", r)
                    M[i][j] = self._ev(nc, r) * pow(dv, p - 2, p) % p
            out.append(M)
        return out

    def unit(self, k):
        return pow(self.zeta, k % self.N, self.p)

    def one_step(self, B, ab):
        p = self.p
        A1, A2, A3 = B
        a, b = ab
        al, be = self.unit(b - a), self.unit(2 * b - a)
        S = [[0] * 8 for _ in range(8)]
        for i in range(4):
            for j in range(4):
                S[i][4 + j] = A1[i][j]
                S[4 + i][j] = (-al * A2[i][j]) % p
                S[4 + i][4 + j] = (A1[i][j] + al * A2[i][j] + be * A3[i][j]) % p
        return S

    def level(self, B, ab, n):
        p, N = self.p, self.N
        cur = (ab[0] % N, ab[1] % N)
        S = [[int(i == j) for j in range(8)] for i in range(8)]
        for _ in range(n):
            T1 = self.one_step(B, cur)
            S = [[sum(T1[i][k] * S[k][j] for k in range(8)) % p for j in range(8)] for i in range(8)]
            cur = deck(cur, N)
        assert cur == (ab[0] % N, ab[1] % N)
        return S

    def charpoly_H1(self, S):
        """coefficients (constant first) of the characteristic polynomial on H^1: charpoly(S) / (s - 1)^4 (Faddeev-LeVerrier)"""
        p, n = self.p, 8
        c = [0] * (n + 1)
        c[n] = 1
        Mk = [[0] * n for _ in range(n)]
        for k in range(1, n + 1):
            # M_k = S M_{k-1} + c_{n-k+1} I ; c_{n-k} = -tr(S M_k) / k
            SM = [[sum(S[i][l] * Mk[l][j] for l in range(n)) % p for j in range(n)] for i in range(n)]
            Mk = [[(SM[i][j] + (c[n - k + 1] if i == j else 0)) % p for j in range(n)] for i in range(n)]
            tr = sum(sum(S[i][l] * Mk[l][i] for l in range(n)) for i in range(n)) % p
            c[n - k] = (-tr * pow(k, p - 2, p)) % p
        poly = c[:]
        for _ in range(4):                       # divide by (s - 1)
            deg = len(poly) - 1
            quo = [0] * deg
            carry = 0
            for e in range(deg, 0, -1):
                carry = (poly[e] + carry) % p
                quo[e - 1] = carry
            assert (poly[0] + carry) % p == 0, "not divisible by (s - 1)"
            poly = quo
        return poly                               # length 5, monic

    def f_values(self, ab, n, lams, points):
        """for each q0 in points: q0^(16 n) P_nu(q0, lam) for each lam (lam as exponents of i)"""
        p = self.p
        out = {l: [] for l in lams}
        for r in points:
            B = self.blocks_at(r)
            P = self.charpoly_H1(self.level(B, ab, n))
            sh = pow(r, 16 * n, p)
            for l in lams:
                lv = pow(self.iota, l, p)
                out[l].append(sh * sum(P[e] * pow(lv, e, p) for e in range(5)) % p)
        return out


def interpolate_modp(xs, ys, p):
    """Newton interpolation over GF(p): coefficients (constant first)"""
    n = len(xs)
    coef = list(ys)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) * pow((xs[i] - xs[i - j]) % p, p - 2, p) % p
    poly = [0]
    for i in range(n - 1, -1, -1):
        # poly = poly * (x - xs[i]) + coef[i]
        new = [0] * (len(poly) + 1)
        for e, c in enumerate(poly):
            new[e + 1] = (new[e + 1] + c) % p
            new[e] = (new[e] - c * xs[i]) % p
        new[0] = (new[0] + coef[i]) % p
        poly = new
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def f_polys_modp(mp, ab, n, lams):
    """the polynomials q^(16 n) P_nu(q, lam) over GF(p) (degree <= 32 n), by interpolation at 32 n + 1 points"""
    D = 32 * n
    pts = list(range(1, D + 2))
    vals = mp.f_values(ab, n, lams, pts)
    return {l: interpolate_modp(pts, vals[l], mp.p) for l in lams}
