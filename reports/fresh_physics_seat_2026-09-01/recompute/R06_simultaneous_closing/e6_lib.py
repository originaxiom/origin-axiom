"""R06 independent E6 Chevalley machinery. Written BLIND (before reading the arc's
verification scripts). Everything built from the Cartan matrix + a Frenkel-Kac
bimultiplicative cocycle; the basis is then VALIDATED (full Jacobi, Chevalley
properties) rather than trusted.

Basis order: indices 0..5 = Cartan coroots h_1..h_6 (Bourbaki E6 numbering),
indices 6..77 = root vectors e_alpha, alpha in ROOTS (list of 72 coefficient
tuples w.r.t. simple roots).
"""
import numpy as np
from fractions import Fraction
from itertools import combinations

# ---------------- Cartan matrix, Bourbaki E6: chain 1-3-4-5-6, node 2 on 4 ----
N = 6
EDGES = [(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)]  # 0-indexed Bourbaki
A = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in EDGES:
    A[i][j] = A[j][i] = -1
A = np.array(A, dtype=np.int64)

def ip(a, b):
    """(alpha,beta) with all roots length^2 = 2; a,b coefficient tuples."""
    va, vb = np.array(a, dtype=np.int64), np.array(b, dtype=np.int64)
    return int(va @ A @ vb)

# ---------------- roots: closure under simple reflections ----------------
def build_roots():
    simple = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
    roots = set(simple)
    frontier = set(simple)
    while frontier:
        new = set()
        for r in frontier:
            for i in range(N):
                c = ip(r, simple[i])
                s = tuple(r[k] - c * simple[i][k] for k in range(N))
                if s not in roots:
                    new.add(s)
        roots |= new
        frontier = new
    return sorted(roots), simple

ROOTS, SIMPLE = build_roots()
assert len(ROOTS) == 72, len(ROOTS)
RIDX = {r: i for i, r in enumerate(ROOTS)}
NEG = {r: tuple(-x for x in r) for r in ROOTS}
POS = [r for r in ROOTS if r > NEG[r]]  # one representative per +- pair... use height
def height(r):
    return sum(r)
POSITIVE = [r for r in ROOTS if height(r) > 0]
assert len(POSITIVE) == 36

# ---------------- Frenkel-Kac cocycle ----------------
# eps(alpha_i,alpha_j) = -1 if i==j; for i<j: -1 iff adjacent; +1 otherwise.
L = np.zeros((N, N), dtype=np.int64)  # eps = (-1)^{c^T L d}
for i in range(N):
    L[i][i] = 1
for i, j in EDGES:
    a, b = min(i, j), max(i, j)
    L[a][b] = 1

def eps(a, b):
    va, vb = np.array(a, dtype=np.int64), np.array(b, dtype=np.int64)
    return -1 if (va @ L @ vb) % 2 else 1

# sign normalisation n(alpha) so that [e_a, e_{-a}] = +h_a for ALL roots:
# raw Frenkel-Kac gives [e_a, e_{-a}] = -h_a; rescale e_a -> -e_a on negative roots.
def nsign(r):
    return -1 if height(r) < 0 else 1

def eps2(a, b):
    """structure sign for the rescaled basis: [e_a,e_b] = eps2(a,b) e_{a+b}."""
    s = tuple(a[k] + b[k] for k in range(N))
    return eps(a, b) * nsign(a) * nsign(b) * nsign(s)

# ---------------- structure tensor C[i,j,k]: [b_i,b_j] = sum_k C[i,j,k] b_k ----
D = 78
C = np.zeros((D, D, D), dtype=np.int64)
for i in range(N):
    for r in ROOTS:
        c = ip(SIMPLE[i], r)
        C[i, 6 + RIDX[r], 6 + RIDX[r]] = c
        C[6 + RIDX[r], i, 6 + RIDX[r]] = -c
for a in ROOTS:
    for b in ROOTS:
        if b == NEG[a]:
            # [e_a, e_{-a}] = h_a = sum c_i h_i (coroot = root, simply laced)
            for k in range(N):
                C[6 + RIDX[a], 6 + RIDX[b], k] = a[k]
        else:
            s = tuple(a[k] + b[k] for k in range(N))
            if s in RIDX:
                C[6 + RIDX[a], 6 + RIDX[b], 6 + RIDX[s]] = eps2(a, b)

ADM = np.transpose(C, (0, 2, 1)).copy()  # ADM[i] = matrix of ad(b_i): ADM[i][k,j]=C[i,j,k]

def validate_algebra():
    out = {}
    # antisymmetry
    out["antisym"] = bool(np.all(C + np.transpose(C, (1, 0, 2)) == 0))
    # full Jacobi via representation property ad([x,y]) = [ad x, ad y] on all 3003 pairs
    bad = 0
    for i in range(D):
        for j in range(i + 1, D):
            lhs = np.tensordot(C[i, j, :], ADM, axes=(0, 0))
            rhs = ADM[i] @ ADM[j] - ADM[j] @ ADM[i]
            if not np.array_equal(lhs, rhs):
                bad += 1
    out["jacobi_pair_failures"] = bad
    # Chevalley properties
    out["ef_h_ok"] = all(
        np.array_equal(C[6 + RIDX[a], 6 + RIDX[NEG[a]], :6], np.array(a, dtype=np.int64))
        for a in ROOTS)
    ns = [abs(int(C[6 + RIDX[a], 6 + RIDX[b], 6 + RIDX[tuple(x + y for x, y in zip(a, b))]]))
          for a in ROOTS for b in ROOTS
          if b != NEG[a] and tuple(x + y for x, y in zip(a, b)) in RIDX]
    out["all_N_pm1"] = (set(ns) == {1})
    return out

# ---------------- Killing form ----------------
def killing():
    B = np.einsum("iab,jba->ij", ADM, ADM)
    return B

# ---------------- exact signature of a symmetric integer/Fraction matrix ------
def exact_signature(G):
    """Congruence diagonalisation over Q. G: list-of-lists / np array (symmetric).
    Returns (n_pos, n_neg, n_zero)."""
    n = len(G)
    M = [[Fraction(int(G[i][j])) if not isinstance(G[i][j], Fraction) else G[i][j]
          for j in range(n)] for i in range(n)]
    pos = neg = zero = 0
    idx = 0
    size = n
    while size > 0:
        # find nonzero diagonal pivot
        p = next((k for k in range(size) if M[k][k] != 0), None)
        if p is None:
            # find off-diagonal nonzero
            q = None
            for a in range(size):
                for b in range(a + 1, size):
                    if M[a][b] != 0:
                        q = (a, b)
                        break
                if q:
                    break
            if q is None:
                zero += size
                break
            a, b = q
            # row/col op: add row b to row a (and col) -> diagonal becomes 2*M[a][b]
            for j in range(size):
                M[a][j] += M[b][j]
            for i2 in range(size):
                M[i2][a] += M[i2][b]
            p = a
        # move pivot to front
        if p != 0:
            M[0], M[p] = M[p], M[0]
            for row in M:
                row[0], row[p] = row[p], row[0]
        d = M[0][0]
        if d > 0:
            pos += 1
        else:
            neg += 1
        # eliminate
        newM = [[M[i2][j2] - M[i2][0] * M[0][j2] / d
                 for j2 in range(1, size)] for i2 in range(1, size)]
        M = newM
        size -= 1
    return pos, neg, zero

def column_space_basis(Mint):
    """Exact column-space basis (as integer-ish Fraction column list) of an integer matrix."""
    from fractions import Fraction as F
    rows = len(Mint)
    cols = len(Mint[0])
    W = [[F(int(Mint[i][j])) for j in range(cols)] for i in range(rows)]
    # column reduce: gaussian elim on transpose
    T = [[W[i][j] for i in range(rows)] for j in range(cols)]  # cols x rows
    basis = []
    pivots = []
    for row in T:
        r = row[:]
        for b, p in zip(basis, pivots):
            if r[p] != 0:
                f = r[p] / b[p]
                r = [x - f * y for x, y in zip(r, b)]
        p = next((k for k in range(rows) if r[k] != 0), None)
        if p is not None:
            basis.append(r)
            pivots.append(p)
    return basis  # list of length-rows Fraction vectors
