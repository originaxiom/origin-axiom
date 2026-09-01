#!/usr/bin/env python3
"""
R26 (A) -- blind recomputation of the B1080 global-form kernels, written BEFORE
opening any B1080 script (b1080_results.json was grepped only for the DEFINITION
of the six Weyl realizations / row 4).

Setting.  E6 simply connected, Bourbaki numbering (chain 1-3-4-5-6, node 2 on 4).
For a Levi subalgebra l = s + z (s semisimple, z = centre, dim z = 6 - |L|) given by
a node subset L, the group generated inside E6 is (S x Z^0)/Gamma with
S simply connected, Z^0 the connected centre torus, and

    Gamma = Z(S)  intersect  Z^0      (computed inside the common maximal torus T).

Because the 27 is a faithful E6 rep, this is exactly "the elements of Z(S) x U(1)^k
acting trivially on the 27" -- the arc's definition -- with ALL centre u(1)'s allowed
(the arc's 'only one u(1) needed' is then the statement that Gamma is cyclic and
sits in a circle; that is automatic for any cyclic torsion subgroup of a torus).

Two independent instruments:

 ROUTE 1 (root datum, exact):  Gamma ~ dual of  P_L / K  with K = P  cap  span_R(Phi_L)
   (saturation of the Levi root lattice inside the E6 weight lattice P).  Coordinates
   of kappa in P_L are just its E6 fundamental-weight coordinates restricted to L, so
   Gamma's invariant factors = Smith normal form of the K-basis matrix restricted to
   the L columns.  |Gamma| = |Z(S)| / [K : Q_L].

 ROUTE 2 (the 27's weights, SNF congruence solve):  build the 27 weights as the Weyl
   orbit of omega_1; for each z in Z(S) ask whether some s in Z^0 makes z*s act
   trivially on every weight.  With v_Z = sum_{j not in L} t_j omega_j^vee this is
   C t == b (mod Z^27) with C = 3 * (root-basis coords of the weights, columns j not
   in L), solvable iff w.b in Z for every integer w in the integer left kernel of C
   (Z-basis via SNF).  Kernel elements collected and closure-checked.

Also: exhaustive sweep over EVERY node subset (all Levis), a planted control where
Gamma is strictly smaller than Z(S) (must exist for the instrument to be non-vacuous).
"""
from fractions import Fraction as Fr
from itertools import product, combinations
import sys

# ---------------------------------------------------------------- Cartan matrix
NODES = [1, 2, 3, 4, 5, 6]
EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]
A = [[0] * 6 for _ in range(6)]
for i in range(6):
    A[i][i] = 2
for a, b in EDGES:
    A[a - 1][b - 1] = A[b - 1][a - 1] = -1

# ---------------------------------------------------------------- exact linear algebra
def mat_inv(M):
    n = len(M)
    aug = [[Fr(x) for x in row] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if aug[r][c] != 0)
        aug[c], aug[p] = aug[p], aug[c]
        pv = aug[c][c]
        aug[c] = [x / pv for x in aug[c]]
        for r in range(n):
            if r != c and aug[r][c] != 0:
                f = aug[r][c]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[c])]
    return [row[n:] for row in aug]

def det(M):
    n = len(M)
    M = [[Fr(x) for x in row] for row in M]
    d = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            M[c], M[p] = M[p], M[c]; d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return d

def snf(M):
    """Smith normal form over Z with transforms: returns (D, U, V) with U*M*V = D,
    U,V unimodular; D diagonal (nonneg, divisibility chain)."""
    m, n = len(M), len(M[0]) if M else 0
    D = [[int(x) for x in row] for row in M]
    U = [[int(i == j) for j in range(m)] for i in range(m)]
    V = [[int(i == j) for j in range(n)] for i in range(n)]
    def swap_rows(X, i, j): X[i], X[j] = X[j], X[i]
    def swap_cols(X, i, j):
        for row in X: row[i], row[j] = row[j], row[i]
    def add_row(X, i, j, f):  # row i += f*row j
        X[i] = [a + f * b for a, b in zip(X[i], X[j])]
    def add_col(X, i, j, f):  # col i += f*col j
        for row in X: row[i] += f * row[j]
    t = 0
    while t < min(m, n):
        # pivot: nonzero entry of minimal abs in submatrix
        best = None
        for i in range(t, m):
            for j in range(t, n):
                if D[i][j] != 0 and (best is None or abs(D[i][j]) < abs(D[best[0]][best[1]])):
                    best = (i, j)
        if best is None:
            break
        i, j = best
        swap_rows(D, t, i); swap_rows(U, t, i)
        swap_cols(D, t, j); swap_cols(V, t, j)
        while True:
            changed = False
            for i in range(t + 1, m):
                if D[i][t] != 0:
                    q = D[i][t] // D[t][t]
                    add_row(D, i, t, -q); add_row(U, i, t, -q)
                    if D[i][t] != 0:
                        swap_rows(D, t, i); swap_rows(U, t, i); changed = True
            for j in range(t + 1, n):
                if D[t][j] != 0:
                    q = D[t][j] // D[t][t]
                    add_col(D, j, t, -q); add_col(V, j, t, -q)
                    if D[t][j] != 0:
                        swap_cols(D, t, j); swap_cols(V, t, j); changed = True
            if not changed:
                # divisibility fix
                bad = None
                for i in range(t + 1, m):
                    for j in range(t + 1, n):
                        if D[i][j] % D[t][t] != 0:
                            bad = i; break
                    if bad is not None: break
                if bad is None:
                    break
                add_row(D, t, bad, 1); add_row(U, t, bad, 1)
        if D[t][t] < 0:
            D[t] = [-x for x in D[t]]; U[t] = [-x for x in U[t]]
        t += 1
    return D, U, V

def elementary_divisors(M):
    D, _, _ = snf(M)
    return [D[i][i] for i in range(min(len(D), len(D[0]))) if D[i][i] != 0]

def matmul(X, Y):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*Y)] for row in X]

# ---------------------------------------------------------------- root data
AINV = mat_inv(A)                                   # symmetric
def sub(M, rows, cols): return [[M[i][j] for j in cols] for i in rows]

# weights of the 27 = W-orbit of omega_1 (minuscule), fundamental-weight coordinates
def weyl_orbit(hw):
    seen = {tuple(hw)}; frontier = [tuple(hw)]
    while frontier:
        new = []
        for lam in frontier:
            for i in range(6):
                if lam[i] != 0:
                    mu = tuple(lam[j] - lam[i] * A[i][j] for j in range(6))
                    if mu not in seen:
                        seen.add(mu); new.append(mu)
        frontier = new
    return sorted(seen)
W27 = weyl_orbit([1, 0, 0, 0, 0, 0])
assert len(W27) == 27, len(W27)
# root-basis coordinates of each weight: lam (omega-coords) = c A  =>  c = lam A^-1
def root_coords(lam): return [sum(Fr(lam[i]) * AINV[i][j] for i in range(6)) for j in range(6)]
W27_root = [root_coords(l) for l in W27]
assert all(3 * x == int(3 * x) for c in W27_root for x in c)   # P/Q = Z3

def levi_type(L):
    """Dynkin type of the node subset L (connected components as A_n chains / D / E)."""
    L = sorted(L); comps = []; left = set(L)
    while left:
        s = left.pop(); comp = {s}; stack = [s]
        while stack:
            x = stack.pop()
            for a, b in EDGES:
                for u, v in ((a, b), (b, a)):
                    if u == x and v in left:
                        left.remove(v); comp.add(v); stack.append(v)
        comps.append(sorted(comp))
    names = []
    for c in comps:
        k = len(c)
        if 4 in c and 2 in c and 3 in c and 5 in c:
            names.append({4: 'D4', 5: 'D5' if 1 in c or 6 in c else 'D4?', 6: 'E6'}[k] if k in (4, 5, 6) else '?')
        else:
            names.append(f'A{k}')
    return '+'.join(sorted(names)), comps

# ---------------------------------------------------------------- ROUTE 1
def route1(L):
    L = sorted(L); Lc = [j for j in NODES if j not in L]
    li = [i - 1 for i in L]
    A_L = sub(A, li, li)
    zS = int(abs(det(A_L)))                          # |Z(S)| = |P_L/Q_L| = det A_L
    zS_struct = elementary_divisors(A_L)
    # K = P cap span_R(Phi_L): saturation of the row lattice of Levi simple roots in Z^6.
    # Levi simple roots in omega-coords are the rows A[i], i in L.  Saturation of a rank-r
    # row lattice R in Z^n: K = Z^n cap Q R.  Via SNF: U R V = D  => rows of (D^{-1}_r U R)
    # ... simpler: K basis = rows of  (first r rows of V^{-1}) ... we instead compute
    # [K:Q_L] = prod of elementary divisors of R, and K explicitly as
    #   K = { x in Z^6 : x in span }  = solve via: x = c R, c in Q^r, x integer.
    R = [A[i] for i in li]
    r = len(li)
    D, U, V = snf(R)
    divs = [D[i][i] for i in range(r)]
    index_K_over_QL = 1
    for d in divs: index_K_over_QL *= d
    # Explicit K basis: U R V = D  => R = U^-1 D V^-1; row lattice of R = row lattice of
    # D V^-1 (U unimodular). Saturation = row lattice of  [I_r 0] V^-1  (divide out D).
    Vinv = [[int(x) for x in row] for row in mat_inv(V)]
    Kbasis = [Vinv[i] for i in range(r)]
    # sanity: Kbasis rows lie in span(R): check each row satisfies the same linear
    # constraints as R -- i.e. pairs to zero with fundamental coweights of j not in L,
    # i.e. root-basis coordinates vanish outside L.
    for k in Kbasis:
        rc = root_coords(k)
        assert all(rc[j - 1] == 0 for j in Lc), (L, k, rc)
    # Gamma ~ dual of P_L / K ; coordinates of K in P_L = restriction to L columns
    KL = [[k[i] for i in li] for k in Kbasis]
    gamma_divs = [d for d in elementary_divisors(KL) if d != 1]
    order = 1
    for d in elementary_divisors(KL): order *= d
    assert order * index_K_over_QL == zS, (order, index_K_over_QL, zS)
    return dict(zS=zS, zS_struct=[d for d in zS_struct if d != 1], index_K_QL=index_K_over_QL,
                gamma_order=order, gamma_divs=gamma_divs)

# ---------------------------------------------------------------- ROUTE 2
def integer_left_kernel(C):
    """Z-basis of {w in Z^m : w C = 0}: rows of U beyond the rank, where U C V = D."""
    D, U, V = snf(C)
    m, n = len(C), len(C[0])
    rank = sum(1 for i in range(min(m, n)) if D[i][i] != 0)
    return [U[i] for i in range(rank, m)]

def route2(L, verbose=False):
    L = sorted(L); Lc = [j for j in NODES if j not in L]
    li = [i - 1 for i in L]; lci = [j - 1 for j in Lc]
    A_L = sub(A, li, li); A_L_inv = mat_inv(A_L)
    N = int(abs(det(A_L)))
    # Z(S) elements: v_S = sum_{i in L} n_i omega_i^{vee,L};  <lam, v_S> = sum_i n_i (A_L^-1 lam_L)_i
    # coroot-basis coords of v_S: A_L^-1 n (mod Z^L) -- dedupe mod Q_L^vee
    elems = {}
    for n in product(range(N), repeat=len(L)):
        coords = tuple((sum(A_L_inv[i][k] * n[k] for k in range(len(L)))) % 1 for i in range(len(L)))
        if coords not in elems:
            elems[coords] = n
    assert len(elems) == N, (len(elems), N)
    # charge matrix of Z^0: C = 3 * root-coords of weights on columns j not in L (integer)
    C = [[int(3 * W27_root[w][j]) for j in lci] for w in range(27)]
    LK = integer_left_kernel(C) if lci else [[int(i == j) for j in range(27)] for i in range(27)]
    kernel = []
    for coords, n in elems.items():
        # b_w = -<lam_w, v_S>  (mod 1); with u = t/3, C u == b (mod Z)
        b = [-(sum(Fr(coords[i]) * W27[w][li[i]] for i in range(len(L)))) for w in range(27)]
        ok = all((sum(Fr(wv) * bv for wv, bv in zip(wrow, b))) % 1 == 0 for wrow in LK)
        if ok:
            kernel.append(coords)
    # closure check (group law = addition of coroot coords mod 1)
    ks = set(kernel)
    for x in kernel:
        for y in kernel:
            s = tuple((a + b) % 1 for a, b in zip(x, y))
            assert s in ks, "kernel not closed"
    # structure: element orders
    def order_of(x):
        k = 1; y = x
        while any(c != 0 for c in y):
            y = tuple((a + b) % 1 for a, b in zip(y, x)); k += 1
        return k
    orders = sorted(order_of(x) for x in kernel)
    return dict(size=len(kernel), orders=orders, cyclic=(max(orders) == len(kernel)), kernel=kernel)

# ---------------------------------------------------------------- sweeps
def report(L, tag=''):
    ty, comps = levi_type(L)
    r1 = route1(L); r2 = route2(L)
    assert r1['gamma_order'] == r2['size'], (L, r1, r2)
    print(f"L={L!s:<22} type={ty:<9} |Z(S)|={r1['zS']:<3} Z(S)={r1['zS_struct']!s:<10} "
          f"[K:Q_L]={r1['index_K_QL']:<3} |Gamma|={r1['gamma_order']:<3} invariants={r1['gamma_divs']!s:<10} "
          f"route2: size={r2['size']} cyclic={r2['cyclic']} orders={r2['orders']} {tag}")
    return r1, r2

if __name__ == '__main__':
    print("=== cascade terminus A2+A1 Levis (ALL node subsets of that type; superset of the six) ===")
    a2a1 = []
    for L in combinations(NODES, 3):
        ty, _ = levi_type(L)
        if ty == 'A1+A2':
            a2a1.append(L)
    print(f"count of A2+A1 node subsets: {len(a2a1)}")
    res = [report(L) for L in a2a1]
    print("uniform |Gamma| =", sorted({r[0]['gamma_order'] for r in res}),
          "invariants =", sorted({tuple(r[0]['gamma_divs']) for r in res}),
          "all cyclic:", all(r[1]['cyclic'] for r in res))
    # the six named by the arc: su(3) on {1,3} or {2,4}, su(2) on {2,5,6} / {1,6}
    six = [(1, 3, 2), (1, 3, 5), (1, 3, 6), (2, 4, 1), (2, 4, 6), (2, 4, 5)]  # (2,4,5) is NOT a valid A2+A1 (5 adj 4) -- listed to test
    print("arc-named su(3)/su(2) pairs, validity as Levi of type A2+A1:",
          [(s, levi_type(sorted(s))[0]) for s in six])

    print("\n=== row 1: A2+A1+A1 Levis (full centre) ===")
    r1s = []
    for L in combinations(NODES, 4):
        if levi_type(L)[0] == 'A1+A1+A2':
            r1s.append(L)
    print(f"count of A2+2A1 node subsets: {len(r1s)}  (arc/B1079 say 5)")
    res1 = [report(L) for L in r1s]
    print("uniform |Gamma| =", sorted({r[0]['gamma_order'] for r in res1}),
          "invariants =", sorted({tuple(r[0]['gamma_divs']) for r in res1}))

    print("\n=== row 4: A4 Levis (su(5)+u(1)^2) ===")
    r4s = [L for L in combinations(NODES, 4) if levi_type(L)[0] == 'A4']
    print(f"count of A4 node subsets: {len(r4s)}  (arc says four su(5)-embeddings)")
    res4 = [report(L) for L in r4s]
    print("uniform |Gamma| =", sorted({r[0]['gamma_order'] for r in res4}),
          "invariants =", sorted({tuple(r[0]['gamma_divs']) for r in res4}))

    print("\n=== exhaustive: every Levi (node subset), to expose where Gamma != Z(S) [planted controls] ===")
    strict = []
    for k in range(1, 7):
        for L in combinations(NODES, k):
            r1, r2 = report(L)
            if r1['gamma_order'] != r1['zS']:
                strict.append((L, levi_type(L)[0], r1['zS'], r1['gamma_order']))
    print("\nLevis with Gamma STRICTLY SMALLER than Z(S) (instrument can say 'no'):")
    for s in strict: print("   ", s)
