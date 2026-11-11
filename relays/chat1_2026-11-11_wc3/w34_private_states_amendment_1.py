"""
W-C3, item W34 (arc B1675): the private states at the common point, computed by this seat's own route.

AMENDMENT 1, committed before its run.  The sealed script w34_private_states.py (batch 2, sha256 b4279fa4...) stopped
at its first computation with a shape error: rho_word began every product with the 2 x 2 identity, also when it was
called on a block's matrices (dim V), so it printed nothing.  Its output (empty) and its error are committed as they
are.  This file is that script with one line changed: rho_word starts from the identity of the size of the matrices
it is given.  Nothing else is changed: the rule, the expectations, the control and the code are the sealed ones.

SOURCE OF THE DEFINITIONS.  The SM seat's W34_RULE.md as main received it (B1675's verification/received/) and main's
B1675 FINDINGS, read through the mask.  Neither the seat's scripts nor main's checking script is run or opened.
  - The common point rho_Q: a -> i, b -> j (in SU(2)); the puncture c = [a, b] = a b a^-1 b^-1 goes to -1.
  - The blocks V = Sym^{2k} rho_Q, k = 1, 2, 3.  H^1(F2; V) = Z^1 / B^1 with Z^1 = V + V (the values on a and b) and
    B^1 the coboundaries.  The restriction to the puncture is z -> z(c) in H^1(<c>; V) = V (rho(c) acts as 1 on an
    even block).  The private states are its kernel.
  - A move phi acts by (phi^* z)(x) = g^-1 z(phi(x)), where g rho_Q(x) g^-1 = rho_Q(phi(x)), with the unnormalised
    lift divided by det(g)^k on Sym^{2k}.
  - The moves: L: a -> a, b -> ab; R: a -> ab, b -> b; the mirror P: a <-> b; -I: a -> a^-1, b -> b^-1.
  - The threads: every primitive cyclic word in L and R with both letters, of length 2 to 12, up to rotation and the
    swap L <-> R (379), each with both signs (the - thread composed with -I): 758 states.  A thread acts as the
    composite of its letters; both orders of composition are run.
  - "Kept" means fixed: a class z with phi^* z = z in H^1.  Rank three is the blocks k = 1, 2 together; rank four
    k = 1, 2, 3.

WHAT IS COMPUTED, AND WHAT WOULD COUNT AS NOT REPRODUCING (written before the run)
  T   (dim V, dim H^1, rank of the restriction, private) = (3, 3, 3, 0), (5, 7, 3, 4), (7, 8, 6, 2) for k = 1, 2, 3,
      computed exactly (sympy, Gaussian rationals).
  J   the joint action of L and R keeps no private class and no class of H^1 in any block; with P and -I added, none.
  S   at rank three, L keeps one private class, R one, P two; at rank four, P three.  (L and R at rank four reported.)
  N   no thread of the 758 keeps a private class, in any block, in either order of composition (double precision,
      singular values; the gap between the kept and the dropped values reported).
  Any of T, J, S, N coming out otherwise is NOT REPRODUCED.
  REPORTED  the number of the 758 states that keep a class of all of H^1, per block (main's finding has 718 of 758 in
      the first block); the count 379.

CONTROL (must come out as stated, or the code is broken)
  K1  at a random irreducible pair in SL(2, C) (no finite image), every block has dim H^1 = dim V, restriction rank 1
      and private states dim V - 1 (the boundary sees only the trace of the puncture).
  AMENDMENT TO THE CARD, disclosed: the card's control for W34 said the private states "must be zero" at a generic
      irreducible representation.  That is wrong for the free group: they are dim V - 1, which K1 now states.  The
      card's sentence was written before this script and is corrected here, before any run.

DISCLOSED.  The seat's and main's numbers are known to this seat; this is a check, not a blind test.
"""
import itertools
import json
import sys

import numpy as np
import sympy as sp

I = sp.I


def sym_power(g, n):
    """Sym^n of a 2x2 matrix (sympy), acting on the basis x^(n-r) y^r, r = 0..n, by (x, y) -> (x, y) g."""
    x, y = sp.symbols('x y')
    a, b = g[0, 0], g[0, 1]
    c, d = g[1, 0], g[1, 1]
    X = a * x + c * y
    Y = b * x + d * y
    M = sp.zeros(n + 1, n + 1)
    for r in range(n + 1):
        p = sp.expand(X ** (n - r) * Y ** r)
        P = sp.Poly(p, x, y)
        for s in range(n + 1):
            M[s, r] = P.coeff_monomial(x ** (n - s) * y ** s)
    return M


QI = sp.Matrix([[I, 0], [0, -I]])
QJ = sp.Matrix([[0, 1], [-1, 0]])

# automorphisms of F2 as images of a, b; words as lists of (generator, exponent)
MOVES = {
    'L': {'a': [('a', 1)], 'b': [('a', 1), ('b', 1)]},
    'R': {'a': [('a', 1), ('b', 1)], 'b': [('b', 1)]},
    'P': {'a': [('b', 1)], 'b': [('a', 1)]},
    '-I': {'a': [('a', -1)], 'b': [('b', -1)]},
}


def rho_word(rho, w):
    M = sp.eye(next(iter(rho.values())).shape[0])
    for g, e in w:
        M = M * (rho[g] if e == 1 else rho[g].inv())
    return M


def lift(rho, phi):
    """g with g rho(x) = rho(phi(x)) g for x = a, b (a null vector of a linear system); unnormalised."""
    gs = sp.symbols('g0:4')
    G = sp.Matrix([[gs[0], gs[1]], [gs[2], gs[3]]])
    eqs = []
    for x in ('a', 'b'):
        E = G * rho[x] - rho_word(rho, phi[x]) * G
        eqs += list(E)
    A, _ = sp.linear_eq_to_matrix(eqs, gs)
    ns = A.nullspace()
    assert len(ns) == 1, len(ns)
    v = ns[0]
    v = v / [t for t in v if t != 0][0]
    return sp.Matrix([[v[0], v[1]], [v[2], v[3]]])


def cocycle_value(rhoV, z, w):
    """z(w) for a cocycle given by z['a'], z['b'] (column vectors), rhoV the block's matrices, w a word."""
    val = sp.zeros(z['a'].shape[0], 1)
    M = sp.eye(z['a'].shape[0])
    for g, e in w:
        if e == 1:
            val = val + M * z[g]
            M = M * rhoV[g]
        else:
            Minv = rhoV[g].inv()
            val = val + M * (-Minv * z[g])
            M = M * Minv
    return val


def action_matrix(rho, rhoV, phi, k, dimV):
    """The matrix of phi^* on Z^1 = V + V (coordinates z_a then z_b)."""
    g = lift(rho, phi)
    gV = sym_power(g, 2 * k) / (g.det() ** k)
    gVinv = gV.inv()
    cols = []
    for idx in range(2 * dimV):
        e = sp.zeros(2 * dimV, 1)
        e[idx] = 1
        z = {'a': e[:dimV, :], 'b': e[dimV:, :]}
        za = gVinv * cocycle_value(rhoV, z, phi['a'])
        zb = gVinv * cocycle_value(rhoV, z, phi['b'])
        cols.append(sp.Matrix.vstack(za, zb))
    return sp.Matrix.hstack(*cols)


def block_data(rho, k):
    dimV = 2 * k + 1
    rhoV = {x: sym_power(rho[x], 2 * k) for x in ('a', 'b')}
    Id = sp.eye(dimV)
    B = sp.Matrix.vstack(rhoV['a'] - Id, rhoV['b'] - Id)          # columns span B^1 in Z^1
    c_word = [('a', 1), ('b', 1), ('a', -1), ('b', -1)]
    res_cols = []
    for idx in range(2 * dimV):
        e = sp.zeros(2 * dimV, 1)
        e[idx] = 1
        z = {'a': e[:dimV, :], 'b': e[dimV:, :]}
        res_cols.append(cocycle_value(rhoV, z, c_word))
    Res = sp.Matrix.hstack(*res_cols)
    rhoc = rho_word({x: rhoV[x] for x in ('a', 'b')}, c_word)
    return dimV, rhoV, B, Res, rhoc


def ranks_exact(rho, k):
    dimV, rhoV, B, Res, rhoc = block_data(rho, k)
    rB = B.rank()
    h1 = 2 * dimV - rB
    # H^1(<c>; V) = V / (rho(c) - 1) V; the restriction's rank on H^1 is the rank of Res modulo im(rho(c) - 1)
    Q = (rhoc - sp.eye(dimV))
    rQ = Q.rank()
    rank_res = sp.Matrix.hstack(Res, Q).rank() - rQ
    return dimV, h1, rank_res, h1 - rank_res


def fixed_dims(Phi_list, Bmat, Priv):
    """dim of {z in span(Priv) : phi z - z in B^1 for all phi} / B^1, and the same on all of Z^1 (exact)."""
    n = Bmat.shape[0]
    out = {}
    for label, S in (('private', Priv), ('all', sp.eye(n))):
        blocks = []
        for Phi in Phi_list:
            blocks.append(((Phi - sp.eye(n)) * S))
        # unknowns: alpha (coeffs on S), beta_phi (coeffs on B for each phi)
        rows = []
        m = S.shape[1]
        nb = Bmat.shape[1]
        big = sp.zeros(n * len(Phi_list), m + nb * len(Phi_list))
        for t, blk in enumerate(blocks):
            big[t * n:(t + 1) * n, :m] = blk
            big[t * n:(t + 1) * n, m + t * nb:m + (t + 1) * nb] = -Bmat
        ns = big.nullspace()
        alphas = [v[:m, :] for v in ns]
        if alphas:
            A = sp.Matrix.hstack(*[S * a for a in alphas])
            dim_sol = sp.Matrix.hstack(A, Bmat).rank()
        else:
            dim_sol = Bmat.rank()
        out[label] = dim_sol - Bmat.rank()
    return out


def lyndon(n, alphabet):
    k = len(alphabet)
    out = []
    w = [-1]
    while w:
        w[-1] += 1
        m = len(w)
        if m == n:
            out.append(''.join(alphabet[i] for i in w))
        while len(w) < n:
            w.append(w[len(w) - m])
        while w and w[-1] == k - 1:
            w.pop()
    return out


def canon_rot(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def main():
    out = {}
    rho = {'a': QI, 'b': QJ}
    # T
    table = []
    for k in (1, 2, 3):
        table.append(ranks_exact(rho, k))
    print('T   (dim V, dim H1, restriction rank, private) for k = 1, 2, 3:', table)
    out['T'] = table

    # K1: a random irreducible pair
    rng = np.random.default_rng(5)
    def rnd():
        a = sp.Rational(int(rng.integers(2, 9)), int(rng.integers(2, 9)))
        b = sp.Rational(int(rng.integers(1, 9)), int(rng.integers(2, 9)))
        c = sp.Rational(int(rng.integers(1, 9)), int(rng.integers(2, 9)))
        return sp.Matrix([[a, b], [c, (1 + b * c) / a]])
    rho_g = {'a': rnd(), 'b': rnd()}
    k1 = [ranks_exact(rho_g, k) for k in (1, 2, 3)]
    print('K1  random pair:', k1)
    out['K1'] = k1

    # exact actions of the moves on Z^1, per block, and the private bases
    acts = {}
    data = {}
    for k in (1, 2, 3):
        dimV, rhoV, B, Res, rhoc = block_data(rho, k)
        Q = rhoc - sp.eye(dimV)
        nsp = sp.Matrix.hstack(Res, -Q).nullspace()
        Pcols = sp.Matrix.hstack(*[v[:2 * dimV, :] for v in nsp])
        Priv = sp.Matrix.hstack(*Pcols.columnspace())
        Bsp = sp.Matrix.hstack(*B.columnspace())
        data[k] = (dimV, Bsp, Priv)
        acts[k] = {name: action_matrix(rho, rhoV, phi, k, dimV) for name, phi in MOVES.items()}
        # sanity: each action preserves B^1
        for name, Phi in acts[k].items():
            assert sp.Matrix.hstack(Bsp, Phi * Bsp).rank() == Bsp.rank(), (k, name)

    # J and S
    J = {}
    for k in (1, 2, 3):
        dimV, Bsp, Priv = data[k]
        A = acts[k]
        J[k] = dict(
            L_and_R=fixed_dims([A['L'], A['R']], Bsp, Priv),
            L_R_P_minusI=fixed_dims([A['L'], A['R'], A['P'], A['-I']], Bsp, Priv),
            L=fixed_dims([A['L']], Bsp, Priv), R=fixed_dims([A['R']], Bsp, Priv), P=fixed_dims([A['P']], Bsp, Priv),
            minusI=fixed_dims([A['-I']], Bsp, Priv))
        print('J/S k = %d:' % k, J[k])
    out['J_S_per_block'] = {str(k): v for k, v in J.items()}
    for rank, ks in (('three', (1, 2)), ('four', (1, 2, 3))):
        s = {m: sum(J[k][m]['private'] for k in ks) for m in ('L', 'R', 'P', 'L_and_R', 'L_R_P_minusI')}
        print('S   rank %s, private classes kept:' % rank, s)
        out['S_rank_' + rank] = s

    # N: the threads, numerically
    words = []
    for n in range(2, 13):
        words += lyndon(n, 'LR')
    up_to_swap = set()
    for w in words:
        sw = w.translate(str.maketrans('LR', 'RL'))
        up_to_swap.add(min(canon_rot(w), canon_rot(sw)))
    reps = sorted(up_to_swap, key=lambda s: (len(s), s))
    print('N   words to length 12 up to rotation: %d; up to rotation and the swap: %d' % (len(words), len(reps)))
    out['words'] = len(words)
    out['up_to_swap'] = len(reps)
    numA = {k: {m: np.array(acts[k][m].evalf(), dtype=complex) for m in acts[k]} for k in (1, 2, 3)}
    numB = {k: np.array(data[k][1].evalf(), dtype=complex) for k in (1, 2, 3)}
    numP = {k: np.array(data[k][2].evalf(), dtype=complex) for k in (1, 2, 3)}

    def fixed_num(Phi, Bm, S):
        n = Bm.shape[0]
        big = np.hstack([(Phi - np.eye(n)) @ S, -Bm])
        sv = np.linalg.svd(big, compute_uv=False)
        # nullity of big, then subtract the part that is B^1 itself (dim B^1, independent columns)
        nul = big.shape[1] - int(np.sum(sv > 1e-8 * sv[0]))
        # B^1 inside span(S) contributes rank(B) solutions; B is a subspace of the private space
        res = nul - np.linalg.matrix_rank(Bm, tol=1e-8)
        small_kept = sv[sv > 1e-8 * sv[0]].min() / sv[0]
        dropped = sv[sv <= 1e-8 * sv[0]]
        return res, float(small_kept), float(dropped.max() / sv[0]) if len(dropped) else 0.0

    counts = {}
    gap = [1.0, 0.0]
    for order in ('first letter applied last', 'first letter applied first'):
        keep_priv = {1: 0, 2: 0, 3: 0}
        keep_all = {1: 0, 2: 0, 3: 0}
        for w in reps:
            for sign in (1, -1):
                for k in (1, 2, 3):
                    A = numA[k]
                    n = numB[k].shape[0]
                    # (phi psi)^* = psi^* phi^*: the composite phi = x1 o x2 o ... o xm has pullback xm^* ... x1^*
                    M = np.eye(n, dtype=complex)
                    seq = list(w)
                    for ch in (seq if order == 'first letter applied last' else reversed(seq)):
                        M = A[ch] @ M
                    if sign == -1:
                        M = A['-I'] @ M
                    fp, sk, dr = fixed_num(M, numB[k], numP[k])
                    fa, sk2, dr2 = fixed_num(M, numB[k], np.eye(n, dtype=complex))
                    gap[0] = min(gap[0], sk, sk2)
                    gap[1] = max(gap[1], dr, dr2)
                    if fp > 0:
                        keep_priv[k] += 1
                    if fa > 0:
                        keep_all[k] += 1
        counts[order] = dict(states=2 * len(reps), keep_a_private_class=keep_priv, keep_a_class_of_H1=keep_all)
        print('N   %s:' % order, counts[order])
    print('N   smallest kept singular value (relative): %.3g; largest dropped: %.3g' % (gap[0], gap[1]))
    out['N'] = counts
    out['N_gap'] = gap
    json.dump(out, open(sys.argv[1], 'w'), indent=1, default=str)
    return 0


if __name__ == '__main__':
    sys.exit(main())
