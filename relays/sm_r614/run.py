#!/usr/bin/env python3
"""SM-R614 (register row P-614, main's page M53): the discrete symmetry surviving 27 -> SM, on main's own 27 weights,
in GENESIS's U1-eta normalisation. Data-free; exact (Fractions, integer lattices, sympy's Smith form only).

Usage:  python3 relays/sm_r614/run.py <main checkout>            (the run; writes r614_results.json beside this file)
        python3 relays/sm_r614/run.py <main checkout> --smoke    (toy inputs only: SU(3), SU(5), U(1) lattices)

Inputs from main's checkout: B299's `_weights_27` and `E6_CARTAN` (frontier/B299_trinification_triality/), imported.
From the record, as constants: B1303's table of the 27 (states, colour, weak dimension, Y, psi, chi) and its
gamma = -5 psi/12 + chi/4, which B1365/B1415 identify with the eta direction GENESIS v1.12 calls U1-eta.

Conventions. A weight mu is a vector of Dynkin labels; a Cartan element x is a vector of simple-coroot coordinates; the
pairing is mu . x. E6 is simply connected and its 27 is faithful, so exp(2 pi i x) = 1 on E6 iff x is in Z^6.
A torus element fixes a vev weight w iff w . x is an integer.

Blocks:  A  the SM embedding found on main's weights, checked against B1303's table;
         B  the eta direction (GENESIS's U1-eta), its checks;
         E  E6-level vevs (the cloud memos' setting): N, nu^c, both in one 27, both in two 27s;
            compact stabiliser dimension and rank, SM inside it, torus component group, matter-parity search,
            the memo-72/76 GF(2) census redone and each survivor tested for lying in the SM torus;
         G  GENESIS's setting: the rank-5 group SM x U1-eta (torus V_SM + R eta), broken by a singlet vev;
            component group modulo the SM, its action, matter parity, nu^c nu^c;
         M  Majorana-shaped terms in 27^3;
         P  plants: a wrong vev, wrong directions for eta, the naive Z_|q| rule, an impossible parity (must fail),
            and two positive controls (must fire).
"""
import sys, os, json, random, importlib.util
from fractions import Fraction as Fr
from itertools import combinations_with_replacement
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

HERE = os.path.dirname(os.path.abspath(__file__))


# ============================================================ exact linear algebra over Q and Z
def rref(M):
    """Row-reduce a list of rows of Fractions/ints; return (rows, pivot columns)."""
    A = [[Fr(x) for x in r] for r in M]
    if not A:
        return A, []
    m, n = len(A), len(A[0]); piv = []; r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = 1 / A[r][c]; A[r] = [x * inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
        if r == m:
            break
    return A, piv


def rank(M):
    return len(rref(M)[1]) if M else 0


def nullspace(M, n):
    """Basis of {c in Q^n : M c = 0}; M a list of rows of length n (possibly empty)."""
    if not M:
        return [[Fr(int(i == j)) for i in range(n)] for j in range(n)]
    R, piv = rref(M); free = [j for j in range(n) if j not in piv]; out = []
    for f in free:
        v = [Fr(0)] * n; v[f] = Fr(1)
        for i, p in enumerate(piv):
            v[p] = -R[i][f]
        out.append(v)
    return out


def solve(cols, y):
    """Some t with sum_k t_k cols[k] = y (rational), or None."""
    n = len(cols); m = len(y)
    aug = [[cols[k][i] for k in range(n)] + [y[i]] for i in range(m)]
    R, piv = rref(aug)
    if n in piv:
        return None
    t = [Fr(0)] * n
    for i, p in enumerate(piv):
        t[p] = R[i][n]
    return t


def to_int_rows(rows):
    out = []
    for r in rows:
        den = 1
        for x in r:
            den = den * Fr(x).denominator // __import__('math').gcd(den, Fr(x).denominator)
        out.append([int(Fr(x) * den) for x in r])
    return out


def col_echelon(M, n):
    """Unimodular column reduction of an integer k x n matrix (list of rows). Returns (E, U) with E = M U,
    E in column echelon form; the nonzero columns of E come first."""
    E = [list(r) for r in M]; k = len(E)
    U = [[int(i == j) for j in range(n)] for i in range(n)]
    def colop(a, b, q):          # col_a -= q * col_b
        for r in E: r[a] -= q * r[b]
        for r in U: r[a] -= q * r[b]
    def swap(a, b):
        for r in E: r[a], r[b] = r[b], r[a]
        for r in U: r[a], r[b] = r[b], r[a]
    pc = 0
    for row in range(k):
        if pc >= n:
            break
        while True:
            nz = [c for c in range(pc, n) if E[row][c] != 0]
            if not nz:
                break
            cmin = min(nz, key=lambda c: abs(E[row][c])); swap(pc, cmin)
            done = True
            for c in range(pc + 1, n):
                if E[row][c] != 0:
                    colop(c, pc, E[row][c] // E[row][pc]); done = done and E[row][c] == 0
            if done and all(E[row][c] == 0 for c in range(pc + 1, n)):
                break
        if any(E[row][c] != 0 for c in range(pc, n)):
            pc += 1
    return E, U, pc


def zkernel(M, n):
    """Z-basis of {z in Z^n : M z = 0}, M a list of integer rows."""
    if not M:
        return [[int(i == j) for i in range(n)] for j in range(n)]
    E, U, r = col_echelon(M, n)
    return [[U[i][j] for i in range(n)] for j in range(r, n)]


def lattice_basis(vecs, n):
    """Z-basis (as vectors) of the lattice generated by integer vectors in Z^n."""
    if not vecs:
        return []
    M = [[v[i] for v in vecs] for i in range(n)]
    E, U, r = col_echelon(M, len(vecs))
    return [[E[i][j] for i in range(n)] for j in range(r)]


def saturate(vecs, n):
    """Z-basis of span_Q(vecs) intersected with Z^n."""
    if not vecs or rank(vecs) == 0:
        return []
    comp = nullspace([list(v) for v in vecs], n)          # vectors orthogonal to the span
    if not comp:
        return [[int(i == j) for i in range(n)] for j in range(n)]
    return zkernel(to_int_rows(comp), n)


def int_coords(y, basis):
    t = solve(basis, [Fr(x) for x in y])
    if t is None or any(x.denominator != 1 for x in t):
        return None
    return [int(x) for x in t]


def dot(a, b):
    return sum(Fr(x) * Fr(y) for x, y in zip(a, b))


def in_span_plus_Z(x, Vb):
    """Is x in span(Vb) + Z^6 ?  (exp(2 pi i x) lies in the torus exp(span Vb))"""
    F = nullspace([list(v) for v in Vb], len(x))          # linear forms vanishing on span(Vb)
    if not F:
        return True
    gens = [[dot(f, [int(i == j) for i in range(len(x))]) for f in F] for j in range(len(x))]
    tgt = [dot(f, x) for f in F]
    den = 1
    for v in gens + [tgt]:
        for q in v:
            den = den * q.denominator // __import__('math').gcd(den, q.denominator)
    L = lattice_basis([[int(q * den) for q in v] for v in gens], len(F))
    return int_coords([int(q * den) for q in tgt], L) is not None


# ============================================================ the torus engine
def component_group(Vbasis, vevs):
    """Stab = {x in V : w.x in Z for every vev w}; return the group Stab / (K + V cap Z^6), K = V cap ker(vevs),
    as invariant factors, with dim K and an explicit generator x for each cyclic factor (found by search)."""
    d = len(Vbasis); n = len(Vbasis[0])
    A = [[dot(w, b) for b in Vbasis] for w in vevs]                    # m x d
    dimK = d - rank(A)
    if not vevs or rank(A) == 0:
        return dict(dimK=dimK, invariants=[], order=1, gens=[])
    m = len(vevs)
    L1 = saturate([[A[i][k] for i in range(m)] for k in range(d)], m)  # im(A) cap Z^m
    VZ = saturate(Vbasis, n)                                           # V cap Z^n
    L0gen = [[int(dot(w, z)) for w in vevs] for z in VZ]
    L0 = lattice_basis(L0gen, m)
    co = [int_coords(y, L1) for y in L0]
    assert all(c is not None for c in co)
    snf = smith_normal_form(Matrix(co), domain=ZZ)
    diag = [abs(int(snf[i, i])) for i in range(min(snf.shape))]
    inv = [e for e in diag if e > 1]
    order = 1
    for e in inv: order *= e
    gens = []
    if inv and len(L1) <= 3:                                           # explicit generators by a bounded search
        def in_L0(y): return int_coords(y, L0) is not None
        def ordr(y):
            for k in range(1, order + 1):
                if in_L0([k * c for c in y]): return k
            return None
        import itertools
        for ks in itertools.product(range(order), repeat=len(L1)):
            y = [sum(k * b[i] for k, b in zip(ks, L1)) for i in range(m)]
            if ordr(y) == max(inv):
                t = solve([[A[i][k] for i in range(m)] for k in range(d)], [Fr(v) for v in y])
                x = [sum(t[k] * Vbasis[k][i] for k in range(d)) for i in range(n)]
                gens.append(x); break
    return dict(dimK=dimK, invariants=inv, order=order, gens=gens)


def parity_search(Vbasis, constraints):
    """constraints: list of (weight-or-root lambda, bit). Is there x in V with lambda.x = bit/2 mod 1 for all?
    Returns (found, gf2 dimension of the image of the map x -> (2 lambda.x mod 2), witness x or None)."""
    d = len(Vbasis); J = len(constraints)
    Ap = [[2 * dot(lam, b) for b in Vbasis] for lam, _ in constraints]
    L1 = saturate([[Ap[j][k] for j in range(J)] for k in range(d)], J)
    rows = [[c % 2 for c in y] for y in L1]
    target = [bit % 2 for _, bit in constraints]
    # GF(2) elimination with combination tracking
    basis = []   # (vector, combination over L1 indices)
    for i, r in enumerate(rows):
        v = list(r); comb = [int(k == i) for k in range(len(rows))]
        for bv, bc in basis:
            p = next(j for j in range(J) if bv[j])
            if v[p]:
                v = [(a + b) % 2 for a, b in zip(v, bv)]; comb = [(a + b) % 2 for a, b in zip(comb, bc)]
        if any(v):
            basis.append((v, comb))
    v = list(target); comb = [0] * len(rows)
    for bv, bc in basis:
        p = next(j for j in range(J) if bv[j])
        if v[p]:
            v = [(a + b) % 2 for a, b in zip(v, bv)]; comb = [(a + b) % 2 for a, b in zip(comb, bc)]
    found = not any(v); wit = None
    if found:
        y = [sum(c * L1[k][j] for k, c in enumerate(comb)) for j in range(J)]
        t = solve([[Ap[j][k] for j in range(J)] for k in range(d)], [Fr(c) for c in y])
        wit = [sum(t[k] * Vbasis[k][i] for k in range(d)) for i in range(len(Vbasis[0]))]
    return found, len(basis), wit


# ============================================================ minuscule representations and their Lie algebra
def minuscule_weights(C, hw):
    r = len(C); seen = {tuple(hw)}; q = [tuple(hw)]
    while q:
        mu = q.pop(0)
        for i in range(r):
            if mu[i] == 1:
                nu = tuple(mu[j] - C[i][j] for j in range(r))
                if nu not in seen: seen.add(nu); q.append(nu)
    return sorted(seen, reverse=True)


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n) if A[i][k]) for j in range(n)] for i in range(n)]


def bracket(A, B):
    P, Q = matmul(A, B), matmul(B, A)
    return [[P[i][j] - Q[i][j] for j in range(len(A))] for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def lie_algebra(C, W):
    """Chevalley basis on a minuscule rep: E_i v_mu = v_{mu+alpha_i} when mu_i = -1. Returns
    (basis matrices, positive roots in simple-root coordinates, their E matrices, index of weights)."""
    r = len(C); n = len(W); idx = {w: i for i, w in enumerate(W)}
    Es = []
    for i in range(r):
        M = [[0] * n for _ in range(n)]
        for mu in W:
            if mu[i] == -1:
                nu = tuple(mu[j] + C[i][j] for j in range(r)); M[idx[nu]][idx[mu]] = 1
        Es.append(M)
    Hs = [[[W[a][i] if a == b else 0 for b in range(n)] for a in range(n)] for i in range(r)]
    pos = {tuple(int(i == j) for j in range(r)): Es[i] for i in range(r)}
    frontier = list(pos)
    while frontier:
        new = []
        for k in frontier:
            for i in range(r):
                kk = list(k); kk[i] += 1; kk = tuple(kk)
                if kk in pos: continue
                M = bracket(Es[i], pos[k])
                if any(any(x for x in row) for row in M):
                    pos[kk] = M; new.append(kk)
        frontier = new
    roots = sorted(pos, key=lambda k: (sum(k), k))
    basis = Hs + [pos[k] for k in roots] + [transpose(pos[k]) for k in roots]
    return basis, roots, pos, idx


def flat(M):
    return [x for row in M for x in row]


def stabiliser(basis, vecs):
    """Complexified compact stabiliser: coefficient vectors c with sum c_k M_k v = 0 and sum c_k M_k^T v = 0."""
    n = len(basis[0]); rows = []
    for v in vecs:
        for T in (False, True):
            cols = []
            for M in basis:
                MM = transpose(M) if T else M
                cols.append([sum(MM[i][j] * v[j] for j in range(n)) for i in range(n)])
            for i in range(n):
                rows.append([c[i] for c in cols])
    return nullspace(rows, len(basis))


def combo(basis, c):
    n = len(basis[0])
    return [[sum(ck * M[i][j] for ck, M in zip(c, basis) if ck) for j in range(n)] for i in range(n)]


def reductive_rank(mats, seeds=(1, 2)):
    """min over seeds of dim of the centraliser of a random element inside span(mats) (= rank, generically)."""
    best = None
    for s in seeds:
        rng = random.Random(s)
        X0 = combo(mats, [rng.randint(-9, 9) for _ in mats])
        cols = [flat(bracket(X0, S)) for S in mats]
        rows = [[c[i] for c in cols] for i in range(len(cols[0]))]
        rows = [r for r in rows if any(r)]
        k = len(mats) - rank(rows)
        best = k if best is None else min(best, k)
    return best


def in_stab(M, vecs):
    MT = transpose(M); n = len(M)
    return all(all(sum(A[i][j] * v[j] for j in range(n)) == 0 for i in range(n)) for v in vecs for A in (M, MT))


# ============================================================ smoke tests (toy inputs, outside the test population)
def smoke():
    A2 = [[2, -1], [-1, 2]]; W3 = minuscule_weights(A2, (1, 0)); assert len(W3) == 3
    b, roots, _, _ = lie_algebra(A2, W3); assert len(b) == 8 and rank([flat(M) for M in b]) == 8
    e = lambda i, n: [int(j == i) for j in range(n)]
    st = stabiliser(b, [e(0, 3)]); assert len(st) == 3                          # SU(2) in SU(3)
    assert reductive_rank([combo(b, c) for c in st]) == 1
    A4 = [[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]]
    W5 = minuscule_weights(A4, (1, 0, 0, 0)); b5, _, _, _ = lie_algebra(A4, W5); assert len(b5) == 24
    assert len(stabiliser(b5, [e(0, 5)])) == 15 and len(stabiliser(b5, [e(0, 5), e(1, 5)])) == 8
    v = [1, 2, 0, 0, 0]; assert len(stabiliser(b5, [v])) == 15                  # a rotated vector: still SU(4)
    # torus engine: U(1) (V = R, lattice Z) with a vev of charge 5 -> Z/5; charge 1 -> trivial
    assert component_group([[Fr(1)]], [[5]])['invariants'] == [5]
    assert component_group([[Fr(1)]], [[1]])['invariants'] == []
    # U(1)^2 with vev weight (2, 4): kernel dim 1, quotient Z/2
    g = component_group([[Fr(1), Fr(0)], [Fr(0), Fr(1)]], [[2, 4]]); assert g['dimK'] == 1 and g['invariants'] == [2]
    # a U(1) sitting diagonally: V = R(1,1) in R^2, vev (1, 2) -> charge 3 on the generator (1,1) -> Z/3
    assert component_group([[Fr(1), Fr(1)]], [[1, 2]])['invariants'] == [3]
    # parity search on U(1), charges: matter 1, higgs 2, vev 4 -> x = 1/2 works
    f, dm, w = parity_search([[Fr(1)]], [([1], 1), ([2], 0), ([4], 0)]); assert f and w == [Fr(1, 2)]
    f, _, _ = parity_search([[Fr(1)]], [([1], 1), ([2], 0), ([3], 0)]); assert not f   # 1 odd, 3 even: impossible
    assert in_span_plus_Z([Fr(1, 2), Fr(1, 2)], [[1, -1]]) and not in_span_plus_Z([Fr(1, 2), Fr(0)], [[1, 1]])
    assert zkernel([[2, 4, 6]], 3) and all(2 * a + 4 * b + 6 * c == 0 for a, b, c in zkernel([[2, 4, 6]], 3))
    assert sorted(map(tuple, saturate([[Fr(2), Fr(2)]], 2))) in ([(1, 1)], [(-1, -1)])
    return True


# ============================================================ the record's constants
B1303 = {  # name: (states, colour (3 / -3 / 1), su2 dim, Y, psi, chi)   -- main's B1303 verification, as stated there
    'Q': (6, 3, 2, Fr(1, 6), 1, -1), 'u^c': (3, -3, 1, Fr(-2, 3), 1, -1), 'e^c': (1, 1, 1, Fr(1), 1, -1),
    'd^c': (3, -3, 1, Fr(1, 3), 1, 3), 'L': (2, 1, 2, Fr(-1, 2), 1, 3), 'nu^c': (1, 1, 1, Fr(0), 1, -5),
    'H_u': (2, 1, 2, Fr(1, 2), -2, 2), 'D': (3, 3, 1, Fr(-1, 3), -2, 2),
    'H_d': (2, 1, 2, Fr(-1, 2), -2, -2), 'Dbar': (3, -3, 1, Fr(1, 3), -2, -2), 'N': (1, 1, 1, Fr(0), 4, 0)}
MATTER = ['Q', 'u^c', 'd^c', 'L', 'e^c']
HIGGS = ['H_u', 'H_d']


def load_main(main):
    p = os.path.join(main, 'frontier', 'B299_trinification_triality', 'trinification_triality.py')
    spec = importlib.util.spec_from_file_location('b299', p); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    C = [[int(mod.E6_CARTAN[i, j]) for j in range(6)] for i in range(6)]
    W = sorted((tuple(int(x) for x in w) for w in mod._weights_27()), reverse=True)
    assert len(W) == 27 and len(set(W)) == 27
    return C, W


def cartan_inverse(C):
    Ci = Matrix(C).inv()
    return [[Fr(int(Ci[i, j].p), int(Ci[i, j].q)) for j in range(6)] for i in range(6)]


# ============================================================ the run
def run(main):
    out = {}; lines = []
    def say(s=''):
        print(s); lines.append(s)
    C, W = load_main(main); Ci = cartan_inverse(C); n = 6
    basis, posroots, Epos, idx = lie_algebra(C, W)
    say(f"[A0] main's 27: {len(W)} weights; Lie algebra on it: {len(basis)} matrices, "
        f"rank {rank([flat(M) for M in basis])}, positive roots {len(posroots)}")
    root_dyn = {k: tuple(sum(k[i] * C[i][j] for i in range(6)) for j in range(6)) for k in posroots}
    all_roots = set(root_dyn.values()) | {tuple(-x for x in v) for v in root_dyn.values()}
    out['A0'] = dict(weights=len(W), algebra_dim=len(basis), positive_roots=len(posroots))

    # ---------------- A: the SM embedding on main's weights, matched to B1303's table
    coroot = lambda i: [Fr(int(j == i)) for j in range(6)]
    psi = [3 * Ci[j][0] for j in range(6)]             # 3 x the fundamental coweight of node 0 (the 27's top node)
    assert sorted({dot(w, psi) for w in W}) == [-2, 1, 4]
    ps = {w: dot(w, psi) for w in W}
    D5 = [1, 2, 3, 4, 5]                               # node 2 is trivalent; 1 and 5 are D5's spinor nodes
    e_ = lambda j: [Fr(int(i == j)) for i in range(6)]
    candidates = []
    for removed in (1, 5):
        su5 = [i for i in D5 if i != removed]
        adj = {i: [j for j in su5 if j != i and C[i][j] == -1] for i in su5}
        chain = [next(i for i in su5 if len(adj[i]) == 1)]
        while len(chain) < 4:
            chain.append(next(j for j in adj[chain[-1]] if j not in chain))
        # chi: in the span of the D5 coroots, killing the SU(5) roots
        chi = nullspace([C[i] for i in su5] + [e_(0)], 6)
        assert len(chi) == 1
        for (su3, su2) in ((chain[0:2], [chain[3]]), (chain[2:4], [chain[0]])):
            # Y: in the span of the SU(5) coroots, killing the SU(3) and SU(2) roots
            Ysp = nullspace([C[i] for i in su3 + su2] + [e_(j) for j in range(6) if j not in su5], 6)
            assert len(Ysp) == 1
            candidates.append(dict(removed=removed, su3=su3, su2=su2, chi=chi[0], Y=Ysp[0]))
    matches = []
    target16 = sorted([-1] * 10 + [3] * 5 + [-5])
    for cand in candidates:
        su3, su2 = cand['su3'], cand['su2']
        def colour(mu):
            s = (dot(mu, coroot(su3[0])), dot(mu, coroot(su3[1])))
            return 3 if s in ((1, 0), (-1, 1), (0, -1)) else (-3 if s in ((-1, 0), (1, -1), (0, 1)) else 1)
        s16 = [dot(w, cand['chi']) for w in W if ps[w] == 1]
        scale = next((sc for sc in sorted({Fr(t) / x for t in (-1, 3, -5) for x in s16 if x != 0})
                      if sorted(x * sc for x in s16) == target16), None)
        if scale is None:
            continue
        chi = [x * scale for x in cand['chi']]
        qset = [w for w in W if ps[w] == 1 and dot(w, chi) == -1 and colour(w) != 1 and dot(w, coroot(su2[0])) != 0]
        if not qset or dot(qset[0], cand['Y']) == 0:
            continue
        Y = [x * Fr(1, 6) / dot(qset[0], cand['Y']) for x in cand['Y']]
        flipc = colour(qset[0]) == -3
        lab = {}
        for w in W:
            col = colour(w) * (-1 if flipc else 1); wk = 2 if dot(w, coroot(su2[0])) != 0 else 1
            key = (col, wk, dot(w, Y), ps[w], dot(w, chi))
            lab[w] = next((nm for nm, v in B1303.items() if (v[1], v[2], v[3], v[4], v[5]) == key), None)
        ok = all(lab[w] is not None for w in W) and \
            all(sum(1 for w in W if lab[w] == nm) == B1303[nm][0] for nm in B1303)
        if ok:
            matches.append(dict(cand, chi=chi, Y=Y, psi=psi, lab=lab))
    say(f"[A1] SM embeddings tried: {len(candidates)}; matching B1303's table on all 27 weights: {len(matches)}")
    out['A1'] = dict(tried=len(candidates), matched=len(matches))
    assert matches, "no SM embedding on main's weights reproduces B1303's table"
    S = matches[0]; lab = S['lab']; psi = S['psi']; chi = S['chi']; Y = S['Y']
    sm_nodes = S['su3'] + S['su2']
    sm_roots = [k for k in posroots if all(k[i] == 0 for i in range(6) if i not in sm_nodes)]
    V_SM = [coroot(i) for i in sm_nodes] + [Y]
    st = {nm: [w for w in W if lab[w] == nm] for nm in B1303}
    nu, Nw = st['nu^c'][0], st['N'][0]

    # ---------------- B: eta, GENESIS's U1-eta
    gamma = [Fr(-5, 12) * p + Fr(1, 4) * c for p, c in zip(psi, chi)]
    eta = [3 * g for g in gamma]                        # the primitive integer form (3 chi - 5 psi)/4
    beta = tuple(a - b for a, b in zip(Nw, nu))
    Kill = lambda x, y: sum(x[i] * C[i][j] * y[j] for i in range(6) for j in range(6))
    q_eta = {nm: dot(st[nm][0], eta) for nm in B1303}
    constant = all(len({dot(w, eta) for w in st[nm]}) == 1 for nm in B1303)
    chk = dict(
        eta_per_multiplet={nm: str(v) for nm, v in q_eta.items()},
        gamma_matches_B1303=all(dot(st[nm][0], gamma) == Fr(-5 * B1303[nm][4], 12) + Fr(B1303[nm][5], 4)
                                for nm in B1303),
        constant_on_multiplets=constant,
        equal_on_the_two_singlets=q_eta['nu^c'] == q_eta['N'],
        orthogonal_to_SM_roots=all(dot(root_dyn[k], eta) == 0 for k in sm_roots),
        killing_orthogonal_to_Y=Kill(eta, Y) == 0,
        beta_is_root=beta in all_roots, beta_dot_eta=str(dot(beta, eta)),
        trace=str(sum(dot(w, eta) for w in W)), cubic_trace=str(sum(dot(w, eta) ** 3 for w in W)),
        eta_in_coroot_lattice=all(x.denominator == 1 for x in eta), eta_coords=[str(x) for x in eta])
    say(f"[B] eta (U1-eta, integer form) on the 11 multiplets: {chk['eta_per_multiplet']}")
    for k_, v_ in chk.items():
        if k_ != 'eta_per_multiplet': say(f"    {k_}: {v_}")
    out['B'] = chk
    V5 = V_SM + [eta]
    say(f"    V_SM + R eta = ker(beta)?  dim {rank(V5)}, all annihilated by beta: {all(dot(beta, v) == 0 for v in V5)}")
    out['B']['V5_is_ker_beta'] = rank(V5) == 5 and all(dot(beta, v) == 0 for v in V5)
    # -1 in SU(2)_beta is in the torus of V5: beta^vee/2 + z in V5 for some integer z
    bk = next(k for k in posroots if root_dyn[k] in (beta, tuple(-x for x in beta)))
    half = [Fr(x, 2) for x in bk]
    bh = dot(beta, half)                                # = +-1 for a root; a consistency fact, it cannot fail
    j1 = next(j for j in range(6) if abs(beta[j]) == 1)
    zsol = [int(i == j1) * beta[j1] * int(bh) for i in range(6)]
    out['B']['minus_one_of_SU2_beta_in_T5'] = dot(beta, [h - z for h, z in zip(half, zsol)]) == 0

    def to_sm_central(x):
        """subtract the SU(3) x SU(2) Cartan part so that x pairs to zero with the SM simple roots"""
        Csm = [[C[i][j] for j in sm_nodes[:3]] for i in sm_nodes[:3]]
        c = solve([[Csm[i][j] for i in range(3)] for j in range(3)], [dot(C[i], x) for i in sm_nodes[:3]])
        return [x[k] - sum(c[j] * (k == sm_nodes[j]) for j in range(3)) for k in range(6)]

    def multiplet_phases(x):
        return {nm: str(dot(st[nm][0], x) % 1) for nm in B1303 if len({dot(w, x) % 1 for w in st[nm]}) == 1}

    def parity(Vb, vevs, nu_odd=None, extra=None):
        cons = [(root_dyn[k], 0) for k in sm_roots] + [(w, 0) for w in vevs]
        cons += [(w, 1) for nm in MATTER for w in st[nm]] + [(w, 0) for nm in HIGGS for w in st[nm]]
        if nu_odd is not None:
            cons += [(w, int(nu_odd)) for w in st['nu^c']]
        if extra: cons += extra
        f, dm, wit = parity_search(Vb, cons)
        return dict(found=f, gf2_image_dim=dm, witness_phases=multiplet_phases(wit) if wit else None)

    E = lambda w: [int(v == w) for v in W]
    # ---------------- E: E6-level vevs (the cloud memos' setting)
    R6 = [coroot(i) for i in range(6)]
    scen = {'E1 N only': [E(Nw)], 'E2 nu^c only': [E(nu)],
            'E3 nu^c + N in one 27': [[a + b for a, b in zip(E(nu), E(Nw))]],
            'E3b nu^c + 2N in one 27': [[a + 2 * b for a, b in zip(E(nu), E(Nw))]],
            'E4 nu^c, N in two 27s': [E(nu), E(Nw)]}
    sm_mats = [Epos[k] for k in sm_roots] + [transpose(Epos[k]) for k in sm_roots] + \
              [[[dot(W[a], h) if a == b else 0 for b in range(27)] for a in range(27)] for h in V_SM]
    out['E'] = {}
    for name, vecs in scen.items():
        stb = stabiliser(basis, vecs); mats = [combo(basis, c) for c in stb]
        rk = reductive_rank(mats) if mats else 0
        smin = all(in_stab(M, vecs) for M in sm_mats)
        wts = [W[i] for v in vecs for i in range(27) if v[i]]
        cg = component_group(R6, wts)
        par = parity(R6, wts)
        par_nu = parity(R6, wts, nu_odd=True) if nu not in wts else None
        rec = dict(stab_dim=len(stb), stab_rank=rk, SM_inside=smin, torus_identity_dim=cg['dimK'],
                   torus_component_group=cg['invariants'], matter_parity=par, matter_parity_nu_odd=par_nu)
        out['E'][name] = rec
        say(f"[{name}] stabiliser dim {len(stb)}, rank {rk}, SM inside {smin}; torus: identity dim {cg['dimK']}, "
            f"components {cg['invariants'] or 'trivial'}; matter parity {par['found']}"
            + (f" (nu^c odd too: {par_nu['found']})" if par_nu else ''))
    # memo 72/76 census redone: h in Z^6 mod 2, even on both doors
    import itertools
    doors = [nu, Nw]; K = nullspace([list(w) for w in doors], 6)
    census = []
    for h in itertools.product((0, 1), repeat=6):
        if any(dot(w, h) % 2 for w in doors): continue
        if not any(h): continue
        x = [Fr(c, 2) for c in h]
        odd = {nm: sum(1 for w in st[nm] if dot(w, h) % 2) for nm in B1303}
        sm_central = all(dot(root_dyn[k], h) % 2 == 0 for k in sm_roots)
        census.append(dict(h=list(h), odd_on_15=sum(odd[nm] for nm in MATTER),
                           odd_on_higgs=sum(odd[nm] for nm in HIGGS),
                           odd_on_exotics=odd['D'] + odd['Dbar'], sm_central=sm_central,
                           in_SM_torus=in_span_plus_Z(x, V_SM)))
    say(f"[E5] memo-72 census redone: {len(census)} nontrivial gradings even on both doors; "
        f"odd on all 15: {sum(c['odd_on_15'] == 15 for c in census)}; odd-on-15 counts "
        f"{sorted({c['odd_on_15'] for c in census})}; SM-central: {sum(c['sm_central'] for c in census)}; "
        f"in the SM torus: {sum(c['in_SM_torus'] for c in census)}; kernel of the doors = V_SM: {rank(K + V_SM) == 4}")
    out['E5_census'] = census

    # ---------------- G: GENESIS's setting, SM x U1-eta broken by a singlet vev
    out['G'] = {}
    for name, wts in {'G1 nu^c': [nu], 'G2 N': [Nw], 'G3 nu^c and N': [nu, Nw]}.items():
        cg = component_group(V5, wts)
        gens = [multiplet_phases(to_sm_central(x)) for x in cg['gens']]
        par = parity(V5, wts); par_nu = parity(V5, wts, nu_odd=True) if nu not in wts else None
        maj = all(Fr(2) * dot(nu, x) % 1 == 0 for x in cg['gens'])
        out['G'][name] = dict(identity_dim=cg['dimK'], identity_is_SM=cg['dimK'] == 4,
                              component_group_mod_SM=cg['invariants'], generator_phases=gens, matter_parity=par,
                              matter_parity_nu_odd=par_nu, nu_nu_allowed_by_every_generator=maj)
        say(f"[{name}] identity dim {cg['dimK']}; residual mod SM {cg['invariants'] or 'trivial'}; "
            f"matter parity {par['found']}; nu^c nu^c allowed by the residual: {maj}")
    # where Z/5 inside U1-eta goes: is exp(2 pi i eta/5) an SM element?
    out['G']['eta_over_5_is_SM_element'] = in_span_plus_Z([x / 5 for x in eta], V_SM)
    say(f"[G4] exp(2 pi i eta/5) (the naive Z/5) lies in the SM group: {out['G']['eta_over_5_is_SM_element']}")

    # ---------------- M: Majorana-shaped terms in 27^3
    Wset = set(W); trip = []
    for a, b, c in combinations_with_replacement(range(27), 3):
        if all(W[a][i] + W[b][i] + W[c][i] == 0 for i in range(6)): trip.append((a, b, c))
    sing = {idx[nu], idx[Nw]}
    two_singlets = [t for t in trip if sum(1 for i in t if i in sing) >= 2]
    neg2 = tuple(-2 * x for x in nu) in Wset or tuple(-2 * x for x in Nw) in Wset
    out['M'] = dict(zero_sum_triples=len(trip), triples_with_two_singlets=len(two_singlets),
                    minus_twice_a_singlet_is_a_weight=neg2,
                    all_triples_eta_neutral=all(sum(dot(W[i], eta) for i in t) == 0 for t in trip),
                    singlet_triples=[[lab[W[i]] for i in t] for t in trip if any(i in sing for i in t)])
    say(f"[M] zero-sum triples in 27^3: {len(trip)}; with two SM singlets: {len(two_singlets)}; "
        f"-2 x singlet a weight: {neg2}; all eta-neutral: {out['M']['all_triples_eta_neutral']}")

    # ---------------- P: plants
    out['P'] = {}
    Hu = st['H_u'][0]
    stb = stabiliser(basis, [E(Hu)])
    out['P']['P1_wrong_vev_Hu_SM_inside'] = all(in_stab(M, [E(Hu)]) for M in sm_mats)
    out['P']['P1_wrong_vev_Hu_torus_contains_V_SM'] = all(dot(Hu, v) == 0 for v in V_SM)
    out['P']['P2_psi_equal_on_singlets'] = dot(nu, psi) == dot(Nw, psi)
    out['P']['P2_chi_equal_on_singlets'] = dot(nu, chi) == dot(Nw, chi)
    naive = {nm: abs(dot(nu, [k * x for x in eta])) for nm, k in (('eta', 1), ('2eta', 2), ('gamma', Fr(1, 3)))}
    lat = {nm: component_group(V_SM + [[k * x for x in eta]], [nu])['invariants']
           for nm, k in (('eta', 1), ('2eta', 2), ('gamma', Fr(1, 3)))}
    out['P']['P3_naive_Zq'] = {k: str(v) for k, v in naive.items()}
    out['P']['P3_lattice'] = lat
    imp = parity(V5, [nu], extra=[(w, 1) for w in st['H_u']])
    out['P']['P4_impossible_parity_found'] = imp['found']
    out['P']['C1_positive_E1_parity_found'] = out['E']['E1 N only']['matter_parity']['found']
    twice = tuple(2 * x for x in nu)
    cg2 = component_group(V5, [twice]); par2 = parity(V5, [twice])
    out['P']['C2_positive_twice_nu_vev'] = dict(component_group=cg2['invariants'], matter_parity=par2['found'],
                                               phases=[multiplet_phases(to_sm_central(x)) for x in cg2['gens']])
    for k_, v_ in out['P'].items():
        say(f"[P] {k_}: {v_}")
    return out, lines


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if '--smoke' in sys.argv:
        load_main(sys.argv[1]); smoke(); print('smoke: ok'); sys.exit(0)
    res, lines = run(sys.argv[1])
    with open(os.path.join(HERE, 'r614_results.json'), 'w') as f:
        json.dump(res, f, indent=1, default=str)
