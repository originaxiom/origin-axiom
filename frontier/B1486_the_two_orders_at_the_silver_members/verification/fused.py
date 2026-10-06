#!/usr/bin/env python3
"""B1486 (draft, NOT RUN on the sealed objects): the two orders at a silver member -- do they fuse?

The SM seat's second ask of 2026-10-03, and main's B1466 C3b carried from m004's counted point to m135's member:
S = V (+) 1 (V = nu (x) four), c1 the interior class of H^1(V) (the order W1), c2 its image in H^1(V*) under the
Lorentz form (the order W2).  (1) Is the mixed first-order direction c1 + c2 obstructed at second order?  The relators
are expanded to order eps^2 along rho_eps(g) = (1 + eps u_g + eps^2 w_g) S(g); unobstructed iff the quadratic term lies
in the image of the linear one.  (2) If not obstructed: Gauss-Newton on the relators from the second-order seed to an
exact flat module at finite eps; is it irreducible (commutant dimension 1; no invariant line, no invariant
hyperplane); what is its class index.

Numerical, mpmath at 50 digits; ranks by SVD with a stated tolerance.  Presentation with any number of generators and
relators.  Imports B1485's second_route for the exact objects (the four, the cocycles) and embeds them."""
import sys, json, pathlib
import mpmath as mp
mp.mp.dps = 50
TOL = mp.mpf(10) ** -30
HERE = pathlib.Path(__file__).resolve().parent


def inv(M): return mp.inverse(M)
def word(w, G):
    """product along a word; G maps a letter (lower = generator, upper = inverse) to a matrix"""
    n = G[w[0].lower()].rows; R = mp.eye(n)
    for ch in w: R = R * (G[ch] if ch.islower() else inv(G[ch.lower()]))
    return R


def series_word(w, S, A, B):
    """the relator along P_g = S_g + eps A_g + eps^2 B_g, to order eps^2: returns (R0, R1, R2)"""
    n = next(iter(S.values())).rows; R = [mp.eye(n), mp.zeros(n), mp.zeros(n)]
    for ch in w:
        g = ch.lower()
        if ch.islower(): P = [S[g], A[g], B[g]]
        else:
            Si = inv(S[g]); P = [Si, -Si * A[g] * Si, Si * A[g] * Si * A[g] * Si - Si * B[g] * Si]
        R = [R[0] * P[0], R[0] * P[1] + R[1] * P[0], R[0] * P[2] + R[1] * P[1] + R[2] * P[0]]
    return R


def vec(M): return [M[i, j] for i in range(M.rows) for j in range(M.cols)]


def linear_map(gens, rels, S):
    """L : (w_g) -> (second-order term of each relator with u = 0), as a matrix (|rels| n^2) x (|gens| n^2)"""
    n = S[gens[0]].rows; Z = {g: mp.zeros(n) for g in gens}; cols = []
    for g in gens:
        for i in range(n):
            for j in range(n):
                E = mp.zeros(n); E[i, j] = 1; B = dict(Z); B[g] = E * S[g]
                cols.append(sum((vec(series_word(r, S, Z, B)[2]) for r in rels), []))
    L = mp.matrix(len(cols[0]), len(cols))
    for j, c in enumerate(cols):
        for i in range(len(c)): L[i, j] = c[i]
    return L


def lstsq_min_norm(J, r):
    U, s, Vh = mp.svd_c(J); top = max(1, abs(s[0])); k = sum(1 for i in range(len(s)) if abs(s[i]) > TOL * top)
    x = mp.zeros(J.cols, 1)
    for i in range(k): x += (U[:, i].H * r)[0] / s[i] * Vh[i, :].H
    return x, k


def obstruction(gens, rels, S, u):
    """the class of the second-order term: residual of  L w = -Q(u)  and the solution w"""
    n = S[gens[0]].rows; Z = {g: mp.zeros(n) for g in gens}; A = {g: u[g] * S[g] for g in gens}
    R = [series_word(r, S, A, Z) for r in rels]
    first = max(mp.norm(x[1]) for x in R)                       # must vanish: u is a cocycle
    Q = mp.matrix(sum((vec(x[2]) for x in R), [])); L = linear_map(gens, rels, S)
    x, k = lstsq_min_norm(L, -Q); res = mp.norm(L * x + Q)
    w = {g: mp.matrix(n, n) for g in gens}
    for a, g in enumerate(gens):
        for i in range(n):
            for j in range(n): w[g][i, j] = x[a * n * n + i * n + j]
    return dict(first_order_residual=first, norm_Q=mp.norm(Q), rank_L=k, residual=res, w=w)


def gauss_newton(gens, rels, X, steps=40):
    """minimal-norm Newton steps on the relators from the seed X; returns (X, residual history)"""
    n = X[gens[0]].rows; hist = []
    for _ in range(steps):
        F = mp.matrix(sum((vec(word(r, X) - mp.eye(n)) for r in rels), [])); hist.append(mp.norm(F))
        if hist[-1] < mp.mpf(10) ** -45: break
        Z = {g: mp.zeros(n) for g in gens}; cols = []
        for g in gens:
            for i in range(n):
                for j in range(n):
                    E = mp.zeros(n); E[i, j] = 1; A = dict(Z); A[g] = E
                    cols.append(sum((vec(series_word(r, X, A, Z)[1]) for r in rels), []))
        J = mp.matrix(len(cols[0]), len(cols))
        for j, c in enumerate(cols):
            for i in range(len(c)): J[i, j] = c[i]
        dx, _ = lstsq_min_norm(J, -F)
        for a, g in enumerate(gens):
            for i in range(n):
                for j in range(n): X[g][i, j] += dx[a * n * n + i * n + j]
    return X, hist


def num_rank(M):
    if M.rows == 0 or M.cols == 0: return 0, None
    s = mp.svd_c(M, compute_uv=False); top = max(1, abs(s[0])); k = sum(1 for i in range(len(s)) if abs(s[i]) > TOL * top)
    gap = (abs(s[k - 1]) / abs(s[k])) if 0 < k < len(s) and abs(s[k]) > 0 else None
    return k, gap


def commutant_dim(gens, X):
    """dim {T : T X_g = X_g T for all g}"""
    n = X[gens[0]].rows; rows = []
    for g in gens:
        for i in range(n):
            for j in range(n):
                row = [0] * (n * n)
                for k in range(n):
                    row[k * n + j] += X[g][i, k]        # (X T)_{ij} = sum_k X_ik T_kj
                    row[i * n + k] -= X[g][k, j]        # (T X)_{ij} = sum_k T_ik X_kj
                rows.append(row)
    r, gap = num_rank(mp.matrix(rows)); return n * n - r, gap


def invariants(gens, X):
    """dimension of the common fixed vectors of X and of its dual"""
    n = X[gens[0]].rows
    def fixed(Y):
        M = mp.matrix(len(gens) * n, n)
        for a, g in enumerate(gens):
            D = Y[g] - mp.eye(n)
            for i in range(n):
                for j in range(n): M[a * n + i, j] = D[i, j]
        return n - num_rank(M)[0]
    return fixed(X), fixed({g: inv(X[g]).T for g in gens})


def fox(w, X, gens):
    n = X[gens[0]].rows; val = mp.eye(n); dd = {g: mp.zeros(n) for g in gens}
    for ch in w:
        g = ch.lower()
        if ch.islower(): dd[g] += val; val = val * X[g]
        else: val = val * inv(X[g]); dd[g] -= val
    return dd


def counts(gens, rels, cusp, X):
    """(a0, a1, t0, r1, n) of a numerical module, the instrument's block ranks by SVD"""
    n = X[gens[0]].rows; Id = mp.eye(n); mu, lam = cusp
    def stack(blocks):
        M = mp.matrix(sum(b.rows for b in blocks), blocks[0].cols); r = 0
        for b in blocks:
            M[r:r + b.rows, :] = b; r += b.rows
        return M
    def hcat(blocks):
        M = mp.matrix(blocks[0].rows, sum(b.cols for b in blocks)); c = 0
        for b in blocks:
            M[:, c:c + b.cols] = b; c += b.cols
        return M
    d0 = stack([X[g] - Id for g in gens]); d1 = stack([hcat([fox(r, X, gens)[g] for g in gens]) for r in rels])
    R = stack([hcat([fox(w, X, gens)[g] for g in gens]) for w in (mu, lam)]); BT = stack([word(mu, X) - Id, word(lam, X) - Id])
    r0, rd1, rBT = num_rank(d0)[0], num_rank(d1)[0], num_rank(BT)[0]
    block = mp.zeros(d1.rows + R.rows, d1.cols + BT.cols); block[:d1.rows, :d1.cols] = d1; block[d1.rows:, :d1.cols] = R; block[d1.rows:, d1.cols:] = BT
    r1 = num_rank(block)[0] - rd1 - rBT; a0 = n - r0; a1 = len(gens) * n - rd1 - r0
    return dict(a0=a0, a1=a1, t0=n - rBT, r1=r1, n=a1 - r1)


def relator_residual(gens, rels, X):
    n = X[gens[0]].rows; return max(abs(word(r, X)[i, j] - (1 if i == j else 0)) for r in rels for i in range(n) for j in range(n))


def index(gens, rels, cusp, X):
    assert relator_residual(gens, rels, X) < mp.mpf(10) ** -25, "not a representation"   # added after the sealed run: the twin now refuses a non-representation
    A = counts(gens, rels, cusp, X); B = counts(gens, rels, cusp, {g: inv(X[g]).T for g in gens})
    return dict(I=A["n"] - B["n"], E=A, Edual=B)
