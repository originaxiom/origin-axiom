"""B1297 / D2 engine: exact twisted cohomology of a one-cusped 3-manifold group presentation.

Field  K = Q(zeta_12) = Q[x]/(x^4 - x^2 + 1)  (contains i = z^3, omega = z^4, sqrt(-3) = 2*omega+1).
Words  SnapPy strings (uppercase = inverse) for the base group; explicit (gen, +-1) lists otherwise.
Ranks  exact Gaussian elimination over K; the caller cross-checks with float SVD.
"""
from fractions import Fraction as Fr
import cmath

# ---------------------------------------------------------------- the field Q(zeta_12)
class K:
    __slots__ = ("c",)
    def __init__(self, c=(0, 0, 0, 0)):
        if isinstance(c, (int, Fr)): c = (Fr(c), 0, 0, 0)
        c = list(Fr(x) for x in c)
        while len(c) < 4: c.append(Fr(0))
        while len(c) > 4:
            top = c.pop(); c[-2] += top; c[-4] -= top
        self.c = tuple(c)
    def __add__(s, o): o = K.lift(o); return K(tuple(a + b for a, b in zip(s.c, o.c)))
    __radd__ = __add__
    def __neg__(s): return K(tuple(-a for a in s.c))
    def __sub__(s, o): return s + (-K.lift(o))
    def __rsub__(s, o): return K.lift(o) - s
    def __mul__(s, o):
        o = K.lift(o); r = [Fr(0)] * 7
        for i, a in enumerate(s.c):
            if a == 0: continue
            for j, b in enumerate(o.c):
                if b != 0: r[i + j] += a * b
        for n in (6, 5, 4):
            t = r[n]; r[n] = Fr(0)
            if t: r[n - 2] += t; r[n - 4] -= t
        return K(tuple(r[:4]))
    __rmul__ = __mul__
    def __eq__(s, o): return s.c == K.lift(o).c
    def __hash__(s): return hash(s.c)
    def is_zero(s): return all(x == 0 for x in s.c)
    def inv(s):
        M = [[Fr(0)] * 4 for _ in range(4)]
        for j in range(4):
            e = [Fr(0)] * 4; e[j] = Fr(1)
            col = (s * K(tuple(e))).c
            for i in range(4): M[i][j] = col[i]
        A = [row[:] + [Fr(1) if i == 0 else Fr(0)] for i, row in enumerate(M)]
        for c in range(4):
            p = next(r for r in range(c, 4) if A[r][c] != 0)
            A[c], A[p] = A[p], A[c]
            pv = A[c][c]; A[c] = [x / pv for x in A[c]]
            for r in range(4):
                if r != c and A[r][c] != 0:
                    f = A[r][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
        return K(tuple(A[i][4] for i in range(4)))
    def __truediv__(s, o): return s * K.lift(o).inv()
    def conj(s):
        zinv = K((0, 1, 0, -1))          # z^-1 = z - z^3
        r = K(0); p = K(1)
        for a in s.c:
            r = r + K(a) * p; p = p * zinv
        return r
    def cx(s):
        z = cmath.exp(1j * cmath.pi / 6)
        return sum(float(a) * z ** k for k, a in enumerate(s.c))
    def __repr__(s):
        names = ["", "z", "z^2", "z^3"]
        terms = [(f"{a}" if k == 0 else (f"{a}*{names[k]}" if a != 1 else names[k])) for k, a in enumerate(s.c) if a != 0]
        return "(" + (" + ".join(terms) if terms else "0") + ")"
    @staticmethod
    def lift(o): return o if isinstance(o, K) else K(o)

Z12 = K((0, 1, 0, 0))
I_ = Z12 * Z12 * Z12
OMEGA = I_ * Z12
SQRTM3 = OMEGA * 2 + 1
ONE, ZERO = K(1), K(0)
assert (I_ * I_) == K(-1) and (OMEGA * OMEGA * OMEGA) == ONE and (OMEGA * OMEGA + OMEGA + 1).is_zero()
assert (SQRTM3 * SQRTM3) == K(-3)

# ---------------------------------------------------------------- matrices over K
def mat(rows): return [[K.lift(x) for x in r] for r in rows]
def eye(n): return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
def zeros(n, m): return [[ZERO] * m for _ in range(n)]
def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0]); C = zeros(n, m)
    for i in range(n):
        for t in range(k):
            a = A[i][t]
            if a.is_zero(): continue
            for j in range(m):
                b = B[t][j]
                if not b.is_zero(): C[i][j] = C[i][j] + a * b
    return C
def madd(A, B): return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]
def msub(A, B): return [[a - b for a, b in zip(r, s)] for r, s in zip(A, B)]
def mneg(A): return [[-a for a in r] for r in A]
def mscale(A, c): return [[a * c for a in r] for r in A]
def transpose(A): return [list(r) for r in zip(*A)]
def det2(A): return A[0][0] * A[1][1] - A[0][1] * A[1][0]
def inv2(A):
    d = det2(A); assert d == ONE, "not in SL2"
    return [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
def tr(A): return sum((A[i][i] for i in range(len(A))), K(0))
def meq(A, B): return all((a - b).is_zero() for r, s in zip(A, B) for a, b in zip(r, s))
def kron_block(blocks):
    rows = []
    for br in blocks:
        for i in range(len(br[0])):
            rows.append([x for blk in br for x in blk[i]])
    return rows
def mconj(A): return [[a.conj() for a in r] for r in A]
def to_cx(A): return [[a.cx() for a in r] for r in A]
def general_inv(M):
    n = len(M); A = [r[:] + [ONE if i == j else ZERO for j in range(n)] for i, r in enumerate(M)]
    for c in range(n):
        p = next(i for i in range(c, n) if not A[i][c].is_zero())
        A[c], A[p] = A[p], A[c]
        pv = A[c][c].inv(); A[c] = [x * pv for x in A[c]]
        for i in range(n):
            if i != c and not A[i][c].is_zero():
                f = A[i][c]; A[i] = [x - f * y for x, y in zip(A[i], A[c])]
    return [r[n:] for r in A]

def rref_rank_null(A):
    """exact row reduction; returns (rank, nullspace basis as column vectors)"""
    if not A or not A[0]: return 0, []
    n, m = len(A), len(A[0])
    M = [r[:] for r in A]; piv = []; r = 0
    for c in range(m):
        p = next((i for i in range(r, n) if not M[i][c].is_zero()), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c].inv(); M[r] = [x * pv for x in M[r]]
        for i in range(n):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]; M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == n: break
    free = [c for c in range(m) if c not in piv]
    null = []
    for f in free:
        v = [ZERO] * m; v[f] = ONE
        for i, pc in enumerate(piv): v[pc] = -M[i][f]
        null.append(v)
    return r, null
def rank(A): return rref_rank_null(A)[0]
def hstack(A, B):
    if not A: return [r[:] for r in B]
    if not B: return [r[:] for r in A]
    return [ra + rb for ra, rb in zip(A, B)]
def cols_from_vectors(vs, n):
    if not vs: return [[] for _ in range(n)]
    return [[v[i] for v in vs] for i in range(n)]

# ---------------------------------------------------------------- symmetric powers of 2x2 matrices
def sym_power(g, k):
    """Sym^k acting on X^(k-j) Y^j with g.X = p X + r Y, g.Y = q X + s Y (a homomorphism; checked in controls)."""
    if k == 0: return [[ONE]]
    p, q = g[0][0], g[0][1]; r, s = g[1][0], g[1][1]
    def pmul(P, Q):
        R = {}
        for (a, b), c in P.items():
            for (d, e), f in Q.items():
                R[(a + d, b + e)] = R.get((a + d, b + e), ZERO) + c * f
        return R
    gX = {(1, 0): p, (0, 1): r}; gY = {(1, 0): q, (0, 1): s}
    cols = []
    for j in range(k + 1):
        P = {(0, 0): ONE}
        for _ in range(k - j): P = pmul(P, gX)
        for _ in range(j): P = pmul(P, gY)
        cols.append([P.get((k - jj, jj), ZERO) for jj in range(k + 1)])
    return transpose(cols)

# ---------------------------------------------------------------- words and representations
def inv_word(w): return [(g, -e) for g, e in reversed(w)]
def word_from_snappy(s): return [(ch.lower(), 1 if ch.islower() else -1) for ch in s]
def word_to_snappy(w): return "".join(g if e == 1 else g.upper() for g, e in w)
def free_reduce(w):
    out = []
    for g, e in w:
        if out and out[-1][0] == g and out[-1][1] == -e: out.pop()
        else: out.append((g, e))
    return out

class Rep:
    def __init__(self, images):
        self.im = {(g, 1): M for g, M in images.items()}
        self.dim = len(next(iter(images.values())))
    def letter(self, g, e):
        if e == 1: return self.im[(g, 1)]
        if (g, -1) not in self.im:
            M = self.im[(g, 1)]
            self.im[(g, -1)] = inv2(M) if (len(M) == 2 and det2(M) == ONE) else general_inv(M)
        return self.im[(g, -1)]
    def __call__(self, w):
        M = eye(self.dim)
        for g, e in w: M = mmul(M, self.letter(g, e))
        return M

def fox(rep, word, gens):
    """left Fox derivatives evaluated in rep: f(w) = sum_g D_g f(g)"""
    n = rep.dim; D = {g: zeros(n, n) for g in gens}; P = eye(n)
    for g, e in word:
        if e == 1:
            D[g] = madd(D[g], P); P = mmul(P, rep.letter(g, 1))
        else:
            P = mmul(P, rep.letter(g, -1)); D[g] = msub(D[g], P)
    return D

def dual_rep(rep_matrices): return {g: transpose(general_inv(M)) for g, M in rep_matrices.items()}

# ---------------------------------------------------------------- cohomology of a presentation
class Presentation:
    def __init__(self, gens, rels):
        self.gens = list(gens); self.rels = [free_reduce(r) for r in rels]

def cochain_maps(pres, rep):
    n = rep.dim
    d0 = kron_block([[msub(rep.letter(g, 1), eye(n))] for g in pres.gens])
    blocks = []
    for R in pres.rels:
        D = fox(rep, R, pres.gens); blocks.append([D[g] for g in pres.gens])
    d1 = kron_block(blocks) if blocks else None
    return d0, d1

def cohomology_dims(pres, rep):
    n = rep.dim; d0, d1 = cochain_maps(pres, rep)
    r0 = rank(d0)
    if d1 is None: r1, kerd1 = 0, n * len(pres.gens)
    else:
        r1, _ = rref_rank_null(d1); kerd1 = n * len(pres.gens) - r1
    return dict(h0=n - r0, h1=kerd1 - r0, h2=(n * len(pres.rels) - r1) if d1 is not None else 0,
                rank_d0=r0, rank_d1=r1, d0=d0, d1=d1)

def restriction_rank(pres, rep, cusp_words, cusp_pres):
    """(a_k, t_k, r1) for the pair (pres, cusp) where the cusp generators are the given words."""
    n = rep.dim; N = n * len(pres.gens)
    coh = cohomology_dims(pres, rep); d1 = coh["d1"]
    if d1 is None: Z1 = [[ONE if i == j else ZERO for i in range(N)] for j in range(N)]
    else: _, Z1 = rref_rank_null(d1)
    blocks = []
    for w in cusp_words:
        D = fox(rep, w, pres.gens); blocks.append([D[g] for g in pres.gens])
    Res = kron_block(blocks)
    cusp_rep = Rep({cg: rep(w) for cg, w in zip(cusp_pres.gens, cusp_words)})
    cd0, cd1 = cochain_maps(cusp_pres, cusp_rep)
    ResZ = mmul(Res, cols_from_vectors(Z1, N)) if Z1 else []
    rB = rank(cd0)
    r1 = rank(hstack(ResZ, cd0) if ResZ else cd0) - rB
    tc = cohomology_dims(cusp_pres, cusp_rep)
    return dict(r1=r1, t0=tc["h0"], t1=tc["h1"], t2=tc["h2"], a0=coh["h0"], a1=coh["h1"], a2=coh["h2"])

def index_data(pres, rep_mats, cusp_words, cusp_pres):
    V = Rep(rep_mats); Vd = Rep(dual_rep(rep_mats))
    A = restriction_rank(pres, V, cusp_words, cusp_pres)
    B = restriction_rank(pres, Vd, cusp_words, cusp_pres)
    I = (A["a0"] - B["a0"]) + B["t0"] - A["r1"]
    F = A["a1"] - B["a1"]
    Fpred = (A["a0"] - B["a0"]) + A["r1"] - A["t0"]
    Istar = (B["a0"] - A["a0"]) + A["t0"] - B["r1"]
    checks = dict(annihilator=(A["r1"] + B["r1"] == A["t1"]), t1_split=(A["t1"] == A["t0"] + B["t0"]),
                  F_formula=(F == Fpred), antisym=(I == -Istar),
                  euler_M=(A["a0"] - A["a1"] + A["a2"] == 0), euler_T=(A["t0"] - A["t1"] + A["t2"] == 0))
    return dict(V=A, Vstar=B, I=I, F=F, Istar=Istar, Cc=I + (A["t0"] - B["t0"]) - (A["a0"] - B["a0"]), checks=checks)

# ---------------------------------------------------------------- Reidemeister-Schreier for a cyclic quotient
def rs_cyclic(base_gens, base_rels, phi, n):
    """kernel of phi: gens -> Z/n; transversal t^j (t = the generator with phi = 1);
    kernel generators x_{g,j} = t^j g t^-j (g != t) and z = t^n."""
    t = next(g for g in base_gens if phi[g] % n == 1)
    others = [g for g in base_gens if g != t]
    gens = [f"{g}{j}" for g in others for j in range(n)] + ["z"]
    def rewrite(word):
        out = []; j = 0
        for g, e in word:
            if g == t:
                if e == 1:
                    if j == n - 1: out.append(("z", 1))
                    j = (j + 1) % n
                else:
                    if j == 0: out.append(("z", -1))
                    j = (j - 1) % n
            else: out.append((f"{g}{j}", e))
        assert j == 0, "word not in kernel"
        return free_reduce(out)
    rels = [rewrite([(t, 1)] * j + list(R) + [(t, -1)] * j) for j in range(n) for R in base_rels]
    return gens, rels, rewrite, t, others

def abelianize(gens, rels):
    M = []
    for R in rels:
        row = [0] * len(gens)
        for g, e in R: row[gens.index(g)] += e
        M.append(row)
    return M

def smith(Mrows, ncols):
    """Smith normal form with transforms: U*A*V = D (integers, U, V unimodular)."""
    A = [r[:] for r in Mrows]; m = len(A); n = ncols
    U = [[int(i == j) for j in range(m)] for i in range(m)]
    V = [[int(i == j) for j in range(n)] for i in range(n)]
    def swap_rows(X, i, j): X[i], X[j] = X[j], X[i]
    def add_row(X, i, j, c): X[i] = [a + c * b for a, b in zip(X[i], X[j])]
    def swap_cols(X, i, j):
        for r in X: r[i], r[j] = r[j], r[i]
    def add_col(X, i, j, c):
        for r in X: r[i] += c * r[j]
    t = 0
    while t < min(m, n):
        piv = None
        for i in range(t, m):
            for j in range(t, n):
                if A[i][j] != 0 and (piv is None or abs(A[i][j]) < abs(A[piv[0]][piv[1]])): piv = (i, j)
        if piv is None: break
        i, j = piv
        swap_rows(A, t, i); swap_rows(U, t, i); swap_cols(A, t, j); swap_cols(V, t, j)
        done = False
        while not done:
            done = True
            for i in range(t + 1, m):
                if A[i][t] != 0:
                    q = A[i][t] // A[t][t]; add_row(A, i, t, -q); add_row(U, i, t, -q)
                    if A[i][t] != 0: swap_rows(A, t, i); swap_rows(U, t, i); done = False
            for j in range(t + 1, n):
                if A[t][j] != 0:
                    q = A[t][j] // A[t][t]; add_col(A, j, t, -q); add_col(V, j, t, -q)
                    if A[t][j] != 0: swap_cols(A, t, j); swap_cols(V, t, j); done = False
            if done:
                bad = None
                for i in range(t + 1, m):
                    for j in range(t + 1, n):
                        if A[i][j] % A[t][t] != 0: bad = (i, j)
                if bad is not None: add_row(A, t, bad[0], 1); add_row(U, t, bad[0], 1); done = False
        if A[t][t] < 0: A[t] = [-x for x in A[t]]; U[t] = [-x for x in U[t]]
        t += 1
    return A, U, V

def h1_coordinates(gens, rels):
    """H1 of the presentation: (invariants d_i != 1, class(word) -> coords mod d_i, V, D, kept indices)"""
    A = abelianize(gens, rels); n = len(gens)
    D, U, V = smith(A, n)
    diag = [D[i][i] if i < len(D) else 0 for i in range(n)]
    def reduce(vec): return tuple((x % d) if d != 0 else x for x, d in zip(vec, diag))
    def cls(word):
        v = [0] * n
        for g, e in word:
            k = gens.index(g)
            for i in range(n): v[i] += e * V[k][i]
        return reduce(v)
    keep = [i for i, d in enumerate(diag) if d != 1]
    def cls_k(word): return tuple(cls(word)[i] for i in keep)
    return [diag[i] for i in keep], cls_k, V, D, keep
