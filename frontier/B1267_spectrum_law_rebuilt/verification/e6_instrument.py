#!/usr/bin/env python3
"""The 27-instrument, rebuilt from the repository's own exact data.

Loads B883's `rep27.json` (78 exact integer 27x27 matrices, B854 basis order) and rebuilds,
with its own code and no reference to the outside-bench certificate:

  * the e6 bracket (B854's Chevalley cocycle) and the check that rep27 IS a representation;
  * the principal sl2 (e, h, f) and the block decomposition 27 = 17 + 9 + 1;
  * the six highest-weight vectors hv_{2m} spanning the centralizer of e (the dial slots);
  * the theta-parity of the slots by bracket closure: <sl2, hv> = e6 (78) for m in {4, 8},
    = f4 (52) for m in {5, 7, 11} -- B265/B576's dichotomy, recomputed;
  * the subregular sl2 E6(a1) (weighted Dynkin (2,2,2,0,2,2)) and 27 = 13 + 9 + 5;
  * exact group elements exp(x) on the 27 for nilpotent x (polynomials, no floats);
  * the Q(omega) pair arithmetic used by the Fox-calculus layer.

Everything exact (python Fractions); floats appear only in diagnostics.
"""
from __future__ import annotations
import json, os, itertools, random
from fractions import Fraction as F
import numpy as np

ROOT = os.environ.get('OA_ROOT') or os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
REP27 = os.path.join(ROOT, 'frontier', 'B883_the_27', 'rep27.json')

# ------------------------------------------------------------------ e6 roots, B854 order
C = [[2, 0, -1, 0, 0, 0],
     [0, 2, 0, -1, 0, 0],
     [-1, 0, 2, -1, 0, 0],
     [0, -1, -1, 2, -1, 0],
     [0, 0, 0, -1, 2, -1],
     [0, 0, 0, 0, -1, 2]]
N = 6


def ip(a, b):
    return sum(a[i] * b[j] * C[i][j] for i in range(N) for j in range(N))


POS = [tuple(a) for a in itertools.product(range(4), repeat=N) if any(a) and ip(a, a) == 2]
ROOTS = POS + [tuple(-x for x in a) for a in POS]
IDX = {r: k for k, r in enumerate(ROOTS)}
DIM = N + len(ROOTS)
assert len(POS) == 36 and DIM == 78

E0 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        E0[i][j] = -1 if i == j else ((-1) ** C[i][j] if i < j else 1)


def eps(a, b):
    s = 1
    for i in range(N):
        if a[i] == 0:
            continue
        for j in range(N):
            if b[j] == 0:
                continue
            if E0[i][j] == -1 and (a[i] * b[j]) % 2:
                s = -s
    return s


def bracket_basis(p, q):
    """[b_p, b_q] as a dict {index: coefficient} in the 78-dim basis."""
    out = {}
    if p < N and q < N:
        return out
    if p < N:
        b = ROOTS[q - N]
        c = sum(b[j] * C[p][j] for j in range(N))
        if c:
            out[q] = F(c)
        return out
    if q < N:
        a = ROOTS[p - N]
        c = -sum(a[j] * C[q][j] for j in range(N))
        if c:
            out[p] = F(c)
        return out
    a, b = ROOTS[p - N], ROOTS[q - N]
    s = tuple(a[i] + b[i] for i in range(N))
    if all(v == 0 for v in s):
        sgn = eps(a, tuple(-v for v in a))
        for i in range(N):
            if a[i]:
                out[i] = F(sgn * a[i])
        return out
    if s in IDX:
        out[N + IDX[s]] = F(eps(a, b))
    return out


BB = [[bracket_basis(p, q) for q in range(DIM)] for p in range(DIM)]


def br(u, v):
    """Bracket of two coefficient vectors (lists of Fractions, length 78)."""
    out = [F(0)] * DIM
    for p, up in enumerate(u):
        if up == 0:
            continue
        for q, vq in enumerate(v):
            if vq == 0:
                continue
            c = up * vq
            for k, rk in BB[p][q].items():
                out[k] += c * rk
    return out


def vec(i, c=F(1)):
    v = [F(0)] * DIM
    v[i] = c
    return v


def add(u, v):
    return [a + b for a, b in zip(u, v)]


def smul(c, u):
    return [c * a for a in u]


def nz(u):
    return any(a != 0 for a in u)


# ------------------------------------------------------------------ the 27 (B883, exact)
_rep = json.load(open(REP27))['rep']
REP = [np.array(_rep[str(k)], dtype=object) for k in range(DIM)]   # 27x27, entries python ints
for k in range(DIM):
    REP[k] = np.array([[F(int(x)) for x in row] for row in REP[k].tolist()], dtype=object)


def rho(u):
    """The 27x27 matrix of the e6 element with coefficient vector u (exact)."""
    M = np.zeros((27, 27), dtype=object)
    M[:] = F(0)
    for k, c in enumerate(u):
        if c != 0:
            M = M + REP[k] * c
    return M


def mm(A, B):
    return A.dot(B)


def comm(A, B):
    return A.dot(B) - B.dot(A)


def zeros27():
    M = np.zeros((27, 27), dtype=object)
    M[:] = F(0)
    return M


def eye27():
    M = zeros27()
    for i in range(27):
        M[i, i] = F(1)
    return M


def is_zero(M):
    return all(x == 0 for x in M.flatten())


def check_representation(trials=400, seed=3):
    rng = random.Random(seed)
    bad = 0
    for _ in range(trials):
        p, q = rng.sample(range(DIM), 2)
        lhs = rho(dict_to_vec(BB[p][q]))
        rhs = comm(REP[p], REP[q])
        if not is_zero(lhs - rhs):
            bad += 1
    return bad


def dict_to_vec(d):
    v = [F(0)] * DIM
    for k, c in d.items():
        v[k] = c
    return v


# ------------------------------------------------------------------ principal sl2
def principal_sl2():
    import sympy as sp
    Cm = sp.Matrix(C)
    cvec = Cm.inv() * sp.Matrix([2] * N)
    h = [F(int(sp.Rational(cvec[i]).p), int(sp.Rational(cvec[i]).q)) for i in range(N)] + [F(0)] * len(ROOTS)
    e = [F(0)] * DIM
    for i in range(N):
        u = [0] * N
        u[i] = 1
        e[N + IDX[tuple(u)]] = F(1)
    # [e_ai, e_-ai] = eps(ai,-ai) * h_ai ; want sum d_i eps_i h_i = h  => d_i = c_i / eps_i
    f = [F(0)] * DIM
    for i in range(N):
        u = [0] * N
        u[i] = 1
        sgn = eps(tuple(u), tuple(-x for x in u))
        u[i] = -1
        f[N + IDX[tuple(u)]] = h[i] / sgn
    assert br(e, f) == h and br(h, e) == smul(F(2), e) and br(h, f) == smul(F(-2), f)
    return e, h, f


# ------------------------------------------------------------------ ad matrices, kernels
def ad_matrix(x):
    """78x78 exact matrix of ad(x): column j = [x, b_j]."""
    import sympy as sp
    cols = []
    for j in range(DIM):
        cols.append([sp.Rational(c.numerator, c.denominator) for c in br(x, vec(j))])
    return sp.Matrix(cols).T


def height(r):
    return sum(r)


def hw_vectors(e):
    """Highest-weight vectors of the principal sl2 blocks: ker ad(e) on each weight space."""
    import sympy as sp
    ht = {r: height(r) for r in POS}
    out = {}
    for m in (1, 4, 5, 7, 8, 11):
        basis = [r for r in POS if ht[r] == m]
        A = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in br(e, vec(N + IDX[r]))]
                       for r in basis]).T
        ns = A.nullspace()
        assert len(ns) == 1, (m, len(ns))
        coef = ns[0]
        from math import lcm as _lcm
        lcm = 1
        for c in coef:
            lcm = _lcm(lcm, int(sp.Rational(c).q))
        v = [F(0)] * DIM
        for i, r in enumerate(basis):
            q = sp.Rational(coef[i] * lcm)
            if q != 0:
                v[N + IDX[r]] = F(int(q.p), int(q.q))
        out[2 * m] = v
    return out


def closure_dim(gens, cap=78):
    """Dimension of the Lie algebra generated by `gens` (bracket closure, exact rank)."""
    import sympy as sp
    span = [g for g in gens]

    def rank_of(vs):
        return sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in v] for v in vs]).rank()

    r = rank_of(span)
    while True:
        new = []
        for i in range(len(span)):
            for j in range(i + 1, len(span)):
                w = br(span[i], span[j])
                if nz(w):
                    new.append(w)
        cand = span + new
        r2 = rank_of(cand)
        if r2 == r:
            return r
        # reduce to a basis to keep it small
        M = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in v] for v in cand])
        rref, piv = M.T.rref()
        span = [cand[k] for k in piv]
        r = r2
        if r >= cap:
            return r


# ------------------------------------------------------------------ subregular sl2 E6(a1)
def subregular_sl2(seed=7):
    """Weighted Dynkin (2,2,2,0,2,2): h_sub; e_sub generic in g_2; f_sub solved in g_-2."""
    import sympy as sp
    c = [2, 2, 2, 0, 2, 2]
    Cm = sp.Matrix(C)
    hv = Cm.inv() * sp.Matrix(c)
    h = [F(int(sp.Rational(hv[i]).p), int(sp.Rational(hv[i]).q)) for i in range(N)] + [F(0)] * len(ROOTS)
    g2 = [r for r in POS if sum(r[i] * c[i] for i in range(N)) == 2]
    gm2 = [tuple(-x for x in r) for r in g2]
    rng = random.Random(seed)
    e = [F(0)] * DIM
    for r in g2:
        e[N + IDX[r]] = F(rng.choice([1, 2, 3, -1, -2, 5]))
    # solve [e, f] = h with f in g_-2
    ds = sp.symbols('d0:%d' % len(gm2))
    acc = [sp.Integer(0)] * DIM
    for k, r in enumerate(gm2):
        w = br(e, vec(N + IDX[r]))
        for i, ci in enumerate(w):
            if ci:
                acc[i] += ds[k] * sp.Rational(ci.numerator, ci.denominator)
    eqs = [sp.Eq(acc[i], sp.Rational(h[i].numerator, h[i].denominator)) for i in range(DIM)]
    sol = sp.solve(eqs, ds, dict=True)
    assert sol, "no f in g_-2 with [e,f] = h"
    sol = sol[0]
    f = [F(0)] * DIM
    for k, r in enumerate(gm2):
        val = sp.Rational(sol.get(ds[k], 0))
        f[N + IDX[r]] = F(int(val.p), int(val.q))
    assert br(e, f) == h and br(h, e) == smul(F(2), e) and br(h, f) == smul(F(-2), f)
    return e, h, f, g2


def centralizer_dim(x):
    return DIM - ad_matrix(x).rank()


# ------------------------------------------------------------------ exact exponentials on the 27
def expm_nilpotent(Xm):
    """exp of an exactly nilpotent 27x27 matrix over a field of characteristic 0."""
    I = eye27()
    out = I.copy()
    term = I.copy()
    k = 1
    while True:
        term = term.dot(Xm) * F(1, k)
        if is_zero(term):
            return out
        out = out + term
        k += 1
        assert k < 60, "not nilpotent"


# ------------------------------------------------------------------ Q(omega) pairs
class Qw:
    """Elements x + y*omega of Q(omega), omega^2 = -1 - omega (omega = e^{2 pi i/3})."""
    __slots__ = ('x', 'y')

    def __init__(self, x, y=F(0)):
        self.x = F(x)
        self.y = F(y)

    def __add__(self, o):
        o = o if isinstance(o, Qw) else Qw(o)
        return Qw(self.x + o.x, self.y + o.y)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Qw) else Qw(o)
        return Qw(self.x - o.x, self.y - o.y)

    def __rsub__(self, o):
        return Qw(o) - self

    def __neg__(self):
        return Qw(-self.x, -self.y)

    def __mul__(self, o):
        o = o if isinstance(o, Qw) else Qw(o)
        # (x1 + y1 w)(x2 + y2 w) = x1x2 + (x1y2 + y1x2) w + y1y2 (-1 - w)
        return Qw(self.x * o.x - self.y * o.y, self.x * o.y + self.y * o.x - self.y * o.y)

    __rmul__ = __mul__

    def __eq__(self, o):
        o = o if isinstance(o, Qw) else Qw(o)
        return self.x == o.x and self.y == o.y

    def __ne__(self, o):
        return not self.__eq__(o)

    def __hash__(self):
        return hash((self.x, self.y))

    def is_zero(self):
        return self.x == 0 and self.y == 0

    def conj(self):
        # complex conjugation: omega -> omega^2 = -1 - omega
        return Qw(self.x - self.y, -self.y)

    def norm(self):
        return self.x * self.x - self.x * self.y + self.y * self.y

    def inv(self):
        n = self.norm()
        c = self.conj()
        return Qw(c.x / n, c.y / n)

    def to_complex(self):
        w = complex(-0.5, 3 ** 0.5 / 2)
        return complex(float(self.x)) + float(self.y) * w

    def __repr__(self):
        return f"({self.x}+{self.y}w)"


ONE = Qw(1)
ZERO = Qw(0)
OMEGA = Qw(0, 1)
U_RILEY = Qw(1, 1)          # u = 1 + omega = e^{i pi/3}, the Riley root of u^2 - u + 1


def qw_matrix(M):
    """Lift an exact Fraction matrix to a Qw matrix."""
    out = np.empty(M.shape, dtype=object)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            out[i, j] = Qw(M[i, j])
    return out


def qw_zeros(n, m=None):
    m = n if m is None else m
    out = np.empty((n, m), dtype=object)
    for i in range(n):
        for j in range(m):
            out[i, j] = ZERO
    return out


def qw_eye(n):
    out = qw_zeros(n)
    for i in range(n):
        out[i, i] = ONE
    return out


def qw_is_zero(M):
    return all(x.is_zero() for x in M.flatten())


def qw_expm_nilpotent(Xm):
    I = qw_eye(Xm.shape[0])
    out = I.copy()
    term = I.copy()
    k = 1
    while True:
        term = term.dot(Xm)
        term = np.array([[t * Qw(F(1, k)) for t in row] for row in term.tolist()], dtype=object)
        if qw_is_zero(term):
            return out
        out = out + term
        k += 1
        assert k < 60


def qw_transpose(M):
    return M.T.copy()


def qw_conj_matrix(M):
    return np.array([[x.conj() for x in row] for row in M.tolist()], dtype=object)


# ------------------------------------------------------------------ modular rank (two primes)
def _cube_root_mod(p):
    for g in range(2, p):
        r = pow(g, (p - 1) // 3, p)
        if r != 1 and (r * r + r + 1) % p == 0:
            return r
    raise ValueError(p)


def rank_mod_p(M, p, w=None):
    """Rank over F_p of a Qw (or Fraction) matrix, omega -> a cube root of unity mod p."""
    if w is None:
        w = _cube_root_mod(p)
    n, m = M.shape
    A = np.zeros((n, m), dtype=np.int64)
    for i in range(n):
        for j in range(m):
            x = M[i, j]
            if isinstance(x, Qw):
                a = (x.x.numerator * pow(x.x.denominator, -1, p)) % p
                b = (x.y.numerator * pow(x.y.denominator, -1, p)) % p
                A[i, j] = (a + b * w) % p
            else:
                x = F(x)
                A[i, j] = (x.numerator * pow(x.denominator, -1, p)) % p
    # Gaussian elimination mod p
    r = 0
    for c in range(m):
        piv = None
        for i in range(r, n):
            if A[i, c] % p:
                piv = i
                break
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), -1, p)
        A[r] = (A[r] * inv) % p
        for i in range(n):
            if i != r and A[i, c] % p:
                A[i] = (A[i] - A[i, c] * A[r]) % p
        r += 1
        if r == n:
            break
    return r


PRIMES = (1000003, 1000033)   # both prime and = 1 mod 3 (checked with sympy)


def rank_qw(M):
    rs = [rank_mod_p(M, p) for p in PRIMES]
    assert rs[0] == rs[1], f"modular ranks disagree {rs}"
    return rs[0]


if __name__ == '__main__':
    print("e6: positive roots", len(POS), "dim", DIM)
    print("rep27 is a representation: bad pairs =", check_representation())
    e, h, f = principal_sl2()
    Re, Rh, Rf = rho(e), rho(h), rho(f)
    assert is_zero(comm(Re, Rf) - Rh)
    eig = sorted(int(Rh[i, i]) for i in range(27))
    from collections import Counter
    print("principal h on the 27:", dict(sorted(Counter(eig).items())))
    HV = hw_vectors(e)
    print("hv slots:", sorted(HV))
    for m in (4, 5, 7, 8, 11):
        print(f"  closure <sl2, hv{2*m}> dim = {closure_dim([e, h, f, HV[2*m]])}")
    es, hs, fs, g2 = subregular_sl2()
    print("subregular: |g_2| =", len(g2), " dim C(e_sub) =", centralizer_dim(es), " (orbit dim", DIM - centralizer_dim(es), ")")
    Rhs = rho(hs)
    eig2 = sorted(int(Rhs[i, i]) for i in range(27))
    print("subregular h on the 27:", dict(sorted(Counter(eig2).items())))
