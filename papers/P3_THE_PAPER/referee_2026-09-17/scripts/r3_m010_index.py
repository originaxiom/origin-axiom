"""Independent referee verification of R27(b) / the paper's SS7 m010 witness.

Claim under test (B1413, from the audit lane's R27):
  m010 = <a,b | aabaBaaBab>, mu = AbAA, lam = babA
  A = [[0,1],[-1,1]], B = [[0,u^2],[u,-2]],  u^2 - u + 1 = 0   (u a primitive 6th root, Q(u)=Q(sqrt-3))
  chi(a) = u, chi(b) = -1
  V = Sym^3(rho) (x) chi  ->  a0=0, a1=1, t0=1, t1=2, r1=0, n=1
  V*                      ->  a1=2, r1=2, n=0
  I(V) = n(V) - n(V*) = +1
  rho is reducible non-split, invariant line (1,u), eigenvalues u and -1.
  Its semisimplification: a0=1, a1=4, t0=4, r1=4, n=0 both sides -> I = 0
  and it has the SAME TRACE ON EVERY WORD as rho.

Nothing here is read from the lane's or main's scripts: the field, Fox calculus,
cohomology and restriction are implemented from the definitions.
"""
from fractions import Fraction as Fr
import itertools, random

# ---------------------------------------------------------------- Q(u), u^2 = u - 1
class K:
    __slots__ = ("p", "q")                      # p + q*u
    def __init__(s, p=0, q=0): s.p, s.q = Fr(p), Fr(q)
    def __add__(s, o): o = mk(o); return K(s.p + o.p, s.q + o.q)
    __radd__ = __add__
    def __neg__(s): return K(-s.p, -s.q)
    def __sub__(s, o): return s + (-mk(o))
    def __rsub__(s, o): return mk(o) + (-s)
    def __mul__(s, o):
        o = mk(o)
        # (p1+q1 u)(p2+q2 u) = p1p2 + (p1q2+q1p2) u + q1q2 u^2 , u^2 = u - 1
        a, b, c, d = s.p, s.q, o.p, o.q
        return K(a * c - b * d, a * d + b * c + b * d)
    __rmul__ = __mul__
    def inv(s):
        # norm of p+qu with u^2=u-1 : (p+qu)(p+q ubar), ubar = 1-u ; N = p^2+pq+q^2
        n = s.p * s.p + s.p * s.q + s.q * s.q
        if n == 0: raise ZeroDivisionError
        # conjugate is p + q*(1-u) = (p+q) - q u
        return K((s.p + s.q) / n, -s.q / n)
    def __truediv__(s, o): return s * mk(o).inv()
    def __eq__(s, o): o = mk(o); return s.p == o.p and s.q == o.q
    def is0(s): return s.p == 0 and s.q == 0
    def __repr__(s): return f"({s.p}+{s.q}u)"

def mk(x): return x if isinstance(x, K) else K(x)
ZERO, ONE, U = K(0), K(1), K(0, 1)
assert (U * U - U + ONE).is0(), "u^2 - u + 1 = 0 must hold"
assert (U * U * U + ONE).is0(), "u^3 = -1"
assert (U * U * U * U * U * U - ONE).is0(), "u^6 = 1"

# ---------------------------------------------------------------- matrices over K
def mat(rows): return [[mk(x) for x in r] for r in rows]
def eye(n): return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
def mmul(X, Y):
    n, m, p = len(X), len(Y), len(Y[0])
    return [[sum((X[i][k] * Y[k][j] for k in range(m)), ZERO) for j in range(p)] for i in range(n)]
def msub(X, Y): return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
def smul(c, X): return [[mk(c) * X[i][j] for j in range(len(X[0]))] for i in range(len(X))]
def madd(X, Y): return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
def zeros(n, m): return [[ZERO] * m for _ in range(n)]
def det2(X): return X[0][0] * X[1][1] - X[0][1] * X[1][0]
def trace(X): return sum((X[i][i] for i in range(len(X))), ZERO)
def minv(X):
    """inverse by Gauss-Jordan over K"""
    n = len(X); Aug = [row[:] + eye(n)[i][:] for i, row in enumerate(X)]
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, n) if not Aug[i][c].is0()), None)
        if piv is None: raise ValueError("singular")
        Aug[r], Aug[piv] = Aug[piv], Aug[r]
        iv = Aug[r][c].inv()
        Aug[r] = [x * iv for x in Aug[r]]
        for i in range(n):
            if i != r and not Aug[i][c].is0():
                f = Aug[i][c]
                Aug[i] = [Aug[i][j] - f * Aug[r][j] for j in range(2 * n)]
        r += 1
    return [row[n:] for row in Aug]
def rank(X):
    if not X or not X[0]: return 0
    M = [row[:] for row in X]; n, m = len(M), len(M[0]); r = 0
    for c in range(m):
        piv = next((i for i in range(r, n) if not M[i][c].is0()), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        iv = M[r][c].inv(); M[r] = [x * iv for x in M[r]]
        for i in range(n):
            if i != r and not M[i][c].is0():
                f = M[i][c]; M[i] = [M[i][j] - f * M[r][j] for j in range(m)]
        r += 1
        if r == n: break
    return r
def nullity(X, ncols): return ncols - rank(X)
def stack_h(*blocks):
    return [sum((b[i] for b in blocks), []) for i in range(len(blocks[0]))]

# ---------------------------------------------------------------- Sym^m
def sym(X, m):
    """matrix of Sym^m(X) on the basis x^m, x^(m-1)y, ..., y^m"""
    a, b, c, d = X[0][0], X[0][1], X[1][0], X[1][1]   # x->a x + c y ; y-> b x + d y  (column convention)
    n = m + 1
    out = zeros(n, n)
    for j in range(n):          # image of basis vector x^(m-j) y^j
        # (a x + c y)^(m-j) * (b x + d y)^j  -> collect coefficient of x^(m-i) y^i
        poly = {0: ONE}
        for _ in range(m - j):
            new = {}
            for k, v in poly.items():
                new[k] = new.get(k, ZERO) + v * a
                new[k + 1] = new.get(k + 1, ZERO) + v * c
            poly = new
        for _ in range(j):
            new = {}
            for k, v in poly.items():
                new[k] = new.get(k, ZERO) + v * b
                new[k + 1] = new.get(k + 1, ZERO) + v * d
            poly = new
        for i, v in poly.items():
            out[i][j] = v
    return out

# ---------------------------------------------------------------- the group
REL = "aabaBaaBab"
MU, LAM = "AbAA", "babA"

def word_eval(w, rho):
    M = eye(len(rho['a']))
    for ch in w:
        M = mmul(M, rho[ch.lower()] if ch.islower() else rho[ch.lower() + "i"])
    return M

def make_rho(A, B, chi_a=None, chi_b=None, m=None):
    """Sym^m of (A,B), optionally twisted by the character chi"""
    Am, Bm = (sym(A, m), sym(B, m)) if m is not None else (A, B)
    if chi_a is not None:
        Am, Bm = smul(chi_a, Am), smul(chi_b, Bm)
    return {'a': Am, 'b': Bm, 'ai': minv(Am), 'bi': minv(Bm)}

def dual(rho):
    def T(X): return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    return {'a': T(minv(rho['a'])), 'b': T(minv(rho['b'])),
            'ai': T(rho['a']), 'bi': T(rho['b'])}

def fox(w, rho):
    """(d w/d a, d w/d b) evaluated under rho"""
    n = len(rho['a']); P = eye(n); Da, Db = zeros(n, n), zeros(n, n)
    for ch in w:
        g = ch.lower(); inv = ch.isupper()
        if not inv:
            if g == 'a': Da = madd(Da, P)
            else:        Db = madd(Db, P)
            P = mmul(P, rho[g])
        else:
            P = mmul(P, rho[g + "i"])
            if g == 'a': Da = msub(Da, P)
            else:        Db = msub(Db, P)
    return Da, Db

def cocycle_value(w, rho, xa, xb):
    """value at w of the cocycle determined by u(a)=xa, u(b)=xb"""
    n = len(rho['a']); P = eye(n); val = [ZERO] * n
    def addv(M, x):
        return [val[i] + sum((M[i][k] * x[k] for k in range(n)), ZERO) for i in range(n)]
    for ch in w:
        g = ch.lower(); inv = ch.isupper(); x = xa if g == 'a' else xb
        if not inv:
            val = addv(P, x); P = mmul(P, rho[g])
        else:
            P = mmul(P, rho[g + "i"])
            val = addv(smul(-1, P), x)
    return val

def cohomology(rho, label=""):
    n = len(rho['a'])
    I = eye(n)
    # a0 = dim H^0(pi;V)
    Mbig = [msub(rho['a'], I)[i] + [] for i in range(n)] + [msub(rho['b'], I)[i] + [] for i in range(n)]
    a0 = nullity(Mbig, n)
    # Z^1: (x,y) with Da x + Db y = 0
    Da, Db = fox(REL, rho)
    Zmat = stack_h(Da, Db)                      # n x 2n
    dimZ = 2 * n - rank(Zmat)
    dimB = n - a0
    a1 = dimZ - dimB
    # cusp
    Mu, La = word_eval(MU, rho), word_eval(LAM, rho)
    Tbig = [msub(Mu, I)[i] + [] for i in range(n)] + [msub(La, I)[i] + [] for i in range(n)]
    t0 = nullity(Tbig, n)
    # Z^1(Z^2): (p,q) with (Mu-1)q = (La-1)p
    C = stack_h(smul(-1, msub(La, I)), msub(Mu, I))     # [-(La-1) | (Mu-1)] acting on (p,q)
    dimZT = 2 * n - rank(C)
    dimBT = n - t0
    t1 = dimZT - dimBT
    return dict(n=n, a0=a0, a1=a1, t0=t0, t1=t1, Da=Da, Db=Db, Mu=Mu, La=La,
                dimZ=dimZ, dimB=dimB, dimZT=dimZT, dimBT=dimBT)

def basis_of_kernel(X, ncols):
    """basis of the nullspace of X (list of vectors of length ncols)"""
    M = [row[:] for row in X] if X else [[ZERO] * ncols]
    nrows = len(M)
    piv_cols, r = [], 0
    for c in range(ncols):
        piv = next((i for i in range(r, nrows) if not M[i][c].is0()), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        iv = M[r][c].inv(); M[r] = [x * iv for x in M[r]]
        for i in range(nrows):
            if i != r and not M[i][c].is0():
                f = M[i][c]; M[i] = [M[i][j] - f * M[r][j] for j in range(ncols)]
        piv_cols.append(c); r += 1
    free = [c for c in range(ncols) if c not in piv_cols]
    out = []
    for fc in free:
        v = [ZERO] * ncols; v[fc] = ONE
        for i, pc in enumerate(piv_cols): v[pc] = -M[i][fc]
        out.append(v)
    return out

def restriction_rank(rho, co):
    """r1 = rank of H^1(pi;V) -> H^1(T;V)"""
    n = co['n']
    Z = basis_of_kernel(stack_h(co['Da'], co['Db']), 2 * n)   # cocycles (xa,xb)
    I = eye(n)
    # image vectors in Z^1(T) = (u(mu), u(lam)) in K^{2n}
    imgs = []
    for z in Z:
        xa, xb = z[:n], z[n:]
        imgs.append(cocycle_value(MU, rho, xa, xb) + cocycle_value(LAM, rho, xa, xb))
    # B^1(T) = {((Mu-1)v, (La-1)v)}
    Bt = []
    for k in range(n):
        v = [ZERO] * n; v[k] = ONE
        Mu1 = msub(co['Mu'], I); La1 = msub(co['La'], I)
        Bt.append([sum((Mu1[i][j] * v[j] for j in range(n)), ZERO) for i in range(n)] +
                  [sum((La1[i][j] * v[j] for j in range(n)), ZERO) for i in range(n)])
    rB = rank(Bt) if Bt else 0
    rAll = rank(Bt + imgs) if (Bt or imgs) else 0
    return rAll - rB

def report(name, rho):
    co = cohomology(rho)
    r1 = restriction_rank(rho, co)
    nV = co['a1'] - r1
    print(f"  {name:28s} a0={co['a0']} a1={co['a1']} t0={co['t0']} t1={co['t1']} r1={r1}  n={nV}")
    return co, r1, nV

# ---------------------------------------------------------------- run
A = mat([[0, 1], [-1, 1]])
B = [[ZERO, U * U], [U, K(-2)]]
print("=== base data ===")
print("  det A =", det2(A), "  det B =", det2(B), "  (both must be 1)")
rho2 = {'a': A, 'b': B, 'ai': minv(A), 'bi': minv(B)}
print("  relator aabaBaaBab = I ?", all(word_eval(REL, rho2)[i][j] == eye(2)[i][j]
                                        for i in range(2) for j in range(2)))
v = [ONE, U]
Av = [sum((A[i][k] * v[k] for k in range(2)), ZERO) for i in range(2)]
Bv = [sum((B[i][k] * v[k] for k in range(2)), ZERO) for i in range(2)]
print("  A*(1,u) = u*(1,u) ?", Av[0] == U * v[0] and Av[1] == U * v[1])
print("  B*(1,u) = -1*(1,u) ?", Bv[0] == -v[0] and Bv[1] == -v[1])

# character: chi(a)=u, chi(b)=-1
def chi_word(w):
    z = ONE
    for ch in w:
        g = ch.lower(); c = U if g == 'a' else K(-1)
        z = z * (c if ch.islower() else c.inv())
    return z
print("  chi(relator) =", chi_word(REL), " chi(mu) =", chi_word(MU), " chi(lam) =", chi_word(LAM),
      " (all must be 1)")

# semisimplification: diag(u, 1-u) and diag(-1,-1)
Ass = [[U, ZERO], [ZERO, ONE - U]]
Bss = [[K(-1), ZERO], [ZERO, K(-1)]]
rho2ss = {'a': Ass, 'b': Bss, 'ai': minv(Ass), 'bi': minv(Bss)}
print("  det Ass =", det2(Ass), " det Bss =", det2(Bss))
print("  ss relator = I ?", all(word_eval(REL, rho2ss)[i][j] == eye(2)[i][j]
                                for i in range(2) for j in range(2)))
random.seed(0)
same = True
for _ in range(400):
    w = "".join(random.choice("abAB") for _ in range(random.randint(1, 14)))
    if not (trace(word_eval(w, rho2)) == trace(word_eval(w, rho2ss))): same = False; break
print("  same trace on 400 random words ?", same)

print("\n=== V = Sym^3(rho) (x) chi ===")
V   = make_rho(A, B, U, K(-1), m=3)
coV, r1V, nV = report("V", V)
coD, r1D, nD = report("V*", dual(V))
print(f"  ==> I(V) = n(V) - n(V*) = {nV} - {nD} = {nV - nD}     [lane/paper: +1]")
print(f"  ==> t0 - r1 = {coV['t0']} - {r1V} = {coV['t0'] - r1V}  [paper's stated form]")

print("\n=== semisimplification: Sym^3(rho_ss) (x) chi ===")
W   = make_rho(Ass, Bss, U, K(-1), m=3)
coW, r1W, nW = report("ss", W)
coWD, r1WD, nWD = report("ss*", dual(W))
print(f"  ==> I(ss) = {nW} - {nWD} = {nW - nWD}     [lane/paper: 0]")
