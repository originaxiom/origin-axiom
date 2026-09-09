#!/usr/bin/env python3
"""B1354 -- THE MAXIMAL PERSISTENCE: can any formal branch tangent to V10 keep a cusp-fixed vector beyond order 4?  Exactly, modulo two primes.

A formal branch rho_t = exp(X(t)) rho_0, X = t Y + t^2 X_2 + t^3 X_3 + ..., is determined order by order by the relator up to Z^1 at each
order: X_k = part(-R_k^low) + sum_i lam^(k)_i Z_i (Z_i the eight exact block classes; coboundaries are gauge and dropped).  lam^(k) is
constrained by the relator at order k+1: R_{k+1}^low(lam^(k)) in im d1 (affine in lam^(k), through the polarisation B(Y, Z_i)).
A cusp-fixed vector v_0 of rho_0 persists through order m along the branch iff the obstruction classes o_1, ..., o_m vanish, where
o_m = Q_T (sum_{j=1..m} T_j v_{m-j}) in coker T_0 (30-dimensional), T(t) = [mu(t) - I; lambda(t) - I], v_j = part_T(-sum ...) + kappa_j.
lam^(m) enters o_m only through T_m v_0 = ... + sum_i lam^(m)_i z(Z_i) v_0, whose class vanishes for the classes that keep v_0 to
first order (stage C of B1352) -- so the newest non-keeping components can cancel an obstruction, and the whole question is a
polynomial system: o_2 affine in lam^(2); o_3 affine in (lam^(2), lam^(3)); o_4 quadratic in lam^(2), affine in lam^(3), lam^(4),
plus the relator conditions (affine in the newest lam, quadratic below), plus the bilinear kappa-terms when another fixed vector is
lost earlier along the branch.  The system is built EXACTLY by polynomial interpolation of the black-box pipeline (checked at random
points), the linear unknowns are eliminated, and the remaining equations in lam^(2) (and kappa) are decided by a Groebner basis over
GF(p).  Output per direction and target vector: 'no branch keeps v_0 through order 4' (basis {1}) or an explicit branch (then
continued and checked by the Toeplitz kernel dimensions of stage D).
Usage: python3 persistence_tower.py [prime ...]"""
from __future__ import annotations
import os, sys, time, random, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1350_the_v10_direction', 'verification'))
import obstruction_higher as OH
O, E, S = OH.O, OH.E, OH.S
t0 = time.time()
PR = [int(x) for x in sys.argv[1:]] or [67108819, 67108837]
n = 27
zero = np.zeros((n, n), dtype=np.int64)
I27 = np.eye(n, dtype=np.int64)

# ------------------------------------------------------------------ mod-p linear algebra
class Solver:
    """RREF of A (m x n) mod p with fixed pivots: particular solutions (linear in b on im A), the cokernel projector Q (rows spanning
    the left null space), the kernel basis."""
    def __init__(self, A, p):
        self.p = p; A = np.array(A, dtype=np.int64) % p
        m, nn = A.shape; self.m, self.n = m, nn
        # augment with identity to track row operations: [A | I]
        M = np.hstack([A, np.eye(m, dtype=np.int64)])
        r = 0; piv = []
        for c in range(nn):
            nz = np.nonzero(M[r:, c])[0]
            if nz.size == 0: continue
            k = r + nz[0]
            if k != r: M[[r, k]] = M[[k, r]]
            inv = pow(int(M[r, c]), -1, p); M[r] = (M[r] * inv) % p
            rows = np.nonzero(M[:, c])[0]; rows = rows[rows != r]
            if rows.size: M[rows] = (M[rows] - np.outer(M[rows, c], M[r])) % p
            piv.append(c); r += 1
            if r == m: break
        self.rank = r; self.piv = piv
        self.R = M[:, :nn]; self.Tm = M[:, nn:]          # Tm @ A = R (mod p)
        self.Q = self.Tm[r:]                               # rows r.. of Tm annihilate A: the cokernel projector (m - r rows)
        free = [c for c in range(nn) if c not in piv]
        K = []
        for f in free:
            v = np.zeros(nn, dtype=np.int64); v[f] = 1
            for i, c in enumerate(piv): v[c] = (-self.R[i, f]) % p
            K.append(v)
        self.kernel = np.array(K, dtype=np.int64).reshape(len(K), nn)
    def coker(self, b):
        return (self.Q @ (np.asarray(b, dtype=np.int64) % self.p)) % self.p
    def part_any(self, b):
        """the pivot-based particular part (linear in b; a solution exactly when b is in im A)"""
        y = (self.Tm @ (np.asarray(b, dtype=np.int64) % self.p)) % self.p
        x = np.zeros(self.n, dtype=np.int64)
        for i, c in enumerate(self.piv): x[c] = y[i]
        return x
    def part(self, b):
        """x with A x = b, or None if b is not in im A"""
        y = (self.Tm @ (np.asarray(b, dtype=np.int64) % self.p)) % self.p
        if np.any(y[self.rank:] % self.p): return None
        x = np.zeros(self.n, dtype=np.int64)
        for i, c in enumerate(self.piv): x[c] = y[i]
        return x

def word_series(M, Mi, X, p, deg, word):
    def letter(L):
        g = abs(L)
        Xg = [x % p for x in X[g]] + [zero] * (deg + 1 - len(X[g]))
        if L > 0:
            ex = OH.ser_exp(Xg[:deg + 1], p, deg); return [(e @ M[g]) % p for e in ex]
        ex = OH.ser_exp([(-x) % p for x in Xg[:deg + 1]], p, deg); return [(Mi[g] @ e) % p for e in ex]
    cur = [I27] + [zero] * deg
    for L in word: cur = OH.ser_mul(cur, letter(L), p, deg)
    return cur

# ------------------------------------------------------------------ the setting per prime
class Setting:
    def __init__(self, p):
        self.p = p
        red, w = O.make_red(p); self.red = red
        self.M = {g: O.red_mat(O.rho0.M[g], red, p) for g in (1, 2)}
        self.Mi = {g: O.red_mat(O.rho0.I[g], red, p) for g in (1, 2)}
        self.REP = [np.array([[int(O.F(x).numerator) * pow(int(O.F(x).denominator), -1, p) % p for x in row] for row in E.REP[k].tolist()], dtype=np.int64) for k in range(78)]
        def e6mat(Z):
            acc = zero.copy()
            for k in range(78):
                c = red(Z[k])
                if c: acc = (acc + c * self.REP[k]) % p
            return acc
        self.Zs = [{1: e6mat(Za), 2: e6mat(Zb)} for _, Za, Zb in O.COC]
        self.labels = [f"V{w_}" + ("#2" if i == 5 else "") for i, (w_, _, _) in enumerate(O.COC)]
        # d1: 729 x 156
        cols = []
        for g in (1, 2):
            for k in range(78):
                X = {1: [zero, zero], 2: [zero, zero]}; X[g] = [zero, self.REP[k]]
                cols.append(OH.rel_series(self.M, self.Mi, X, p, 1)[1].reshape(-1))
        self.D = np.array(cols, dtype=np.int64).T % p
        self.d1 = Solver(self.D, p); assert self.d1.rank == 70, self.d1.rank
        # T0 and its solver
        lam0 = word_series(self.M, self.Mi, {1: [zero], 2: [zero]}, p, 0, S.LONG)[0]
        self.T0 = np.vstack([(self.M[1] - I27) % p, (lam0 - I27) % p])
        self.tsol = Solver(self.T0, p); assert self.tsol.rank == 24
        self.K = self.tsol.kernel                          # 3 x 27: the cusp-fixed vectors of rho_0
        # z(Z_i) v for the eight classes: the first-order variation of T applied to v
        self.zT = []
        for Z in self.Zs:
            mu1 = word_series(self.M, self.Mi, {g: [zero, Z[g]] for g in (1, 2)}, p, 1, [1])[1]
            la1 = word_series(self.M, self.Mi, {g: [zero, Z[g]] for g in (1, 2)}, p, 1, S.LONG)[1]
            self.zT.append(np.vstack([mu1, la1]) % p)     # 54 x 27
    def unflat(self, x):
        p = self.p
        return {1: sum(((int(x[k]) * self.REP[k]) % p for k in range(78)), zero.copy()) % p, 2: sum(((int(x[78 + k]) * self.REP[k]) % p for k in range(78)), zero.copy()) % p}
    def direction(self, coeffs):
        p = self.p
        return {g: sum(((int(c) * self.Zs[i][g]) % p for i, c in enumerate(coeffs) if c), zero.copy()) % p for g in (1, 2)}
    # -------------------------------------------------------------- the branch to order K with prescribed class additions
    def branch(self, Y, lams, K):
        """X = [0, Y, X2, ..., XK]; lams[k] in F^8 for k = 2..K (the class added at order k).  Returns (X, order_failed or None)."""
        p = self.p
        X = {g: [zero, Y[g]] for g in (1, 2)}
        for k in range(2, K + 1):
            Xk = {g: X[g] + [zero] for g in (1, 2)}
            R = OH.rel_series(self.M, self.Mi, Xk, p, k)
            b = [(-int(v)) % p for v in R[k].reshape(-1)]
            x = self.d1.part(b)
            if x is None: return X, k
            corr = self.unflat(x)
            add = self.direction(lams.get(k, [0] * 8))
            for g in (1, 2): Xk[g][k] = (corr[g] + add[g]) % p
            X = Xk
        return X, None
    def T_series(self, X, K):
        p = self.p
        mu = word_series(self.M, self.Mi, X, p, K, [1]); la = word_series(self.M, self.Mi, X, p, K, S.LONG)
        return [np.vstack([(mu[j] - (I27 if j == 0 else 0)) % p, (la[j] - (I27 if j == 0 else 0)) % p]) for j in range(K + 1)]
    def obstructions(self, T, v0, K, kappas=None):
        """o_1..o_K for the vector v0 (kappas[j] added to v_j); returns the list of 30-vectors (zero = persists)."""
        p = self.p; vs = [np.asarray(v0, dtype=np.int64) % p]; out = []
        for m in range(1, K + 1):
            rhs = sum(((T[j] @ vs[m - j]) % p for j in range(1, m + 1)), np.zeros(54, dtype=np.int64)) % p
            out.append(self.tsol.coker(rhs))
            vm = self.tsol.part_any((-rhs) % p)                        # the pivot-based particular part: linear in rhs, a solution exactly when o_m = 0
            if kappas and m in kappas: vm = (vm + kappas[m]) % p
            vs.append(vm % p)
        return out
    def toeplitz_kd(self, T, K):
        p = self.p; kd = [0]
        for m in range(1, K + 2):
            big = np.zeros((54 * m, 27 * m), dtype=np.int64)
            for i in range(m):
                for j in range(i + 1):
                    big[54 * i:54 * (i + 1), 27 * j:27 * (j + 1)] = T[i - j]
            kd.append(27 * m - Solver(big, p).rank)
        return kd[1:]

# ------------------------------------------------------------------ the polynomial model of the pipeline
def evaluate(st, Y, u, v0, nvar2, blocks, kap_blocks):
    """the full equation vector E(u) for unknowns u = (lam2 [8], lam3 [8], lam4 [8], kappa-coordinates...):
    E = (coker_d1 R3^low, coker_d1 R4^low, o2, o3, o4) with the branch built through order 4 (R4 is checked while building X4).
    If the branch cannot be built (R3 or R4 not solvable) the corresponding coker entries record the defect: we build the branch
    with the *particular part only where solvable*; to keep E polynomial we compute the defects directly."""
    p = st.p
    lam2 = [int(x) for x in u[0:8]]; lam3 = [int(x) for x in u[8:16]]; lam4 = [int(x) for x in u[16:24]]
    X = {g: [zero, Y[g]] for g in (1, 2)}
    E = []
    for k, lam in ((2, lam2), (3, lam3), (4, lam4)):
        Xk = {g: X[g] + [zero] for g in (1, 2)}
        R = OH.rel_series(st.M, st.Mi, Xk, p, k)
        b = [(-int(v)) % p for v in R[k].reshape(-1)]
        if k >= 3: E.append(st.d1.coker(b))                          # the relator defect at order k (must vanish): 659 entries
        y = (st.d1.Tm @ (np.asarray(b) % p)) % p; x = np.zeros(156, dtype=np.int64)
        for i, c in enumerate(st.d1.piv): x[c] = y[i]                # the particular part (exact when the defect vanishes)
        corr = st.unflat(x); add = st.direction(lam)
        for g in (1, 2): Xk[g][k] = (corr[g] + add[g]) % p
        X = Xk
    T = st.T_series(X, 4)
    kappas = {}
    off = 24
    for m, basis in kap_blocks.items():                              # kappa_m = sum c_i basis_i
        cs = [int(x) for x in u[off:off + len(basis)]]; off += len(basis)
        kappas[m] = sum(((c * bvec) % p for c, bvec in zip(cs, basis)), np.zeros(n, dtype=np.int64)) % p
    o = st.obstructions(T, v0, 4, kappas)
    E += [o[1], o[2], o[3]]                                           # o2, o3, o4 (o1 = 0 for V10 directions)
    return np.concatenate(E) % p

def interpolate_quadratic(f, nvar, p, rng, checks=3):
    """exact quadratic model of f: F^nvar -> F^N from evaluations at 0, e_i, 2e_i, e_i + e_j; verified at random points."""
    f0 = f(np.zeros(nvar, dtype=np.int64))
    N = f0.shape[0]
    lin = np.zeros((N, nvar), dtype=np.int64); quad = {}
    inv2 = pow(2, -1, p)
    fe = []
    for i in range(nvar):
        e = np.zeros(nvar, dtype=np.int64); e[i] = 1; f1 = f(e); e[i] = 2; f2 = f(e)
        # f(e) = f0 + l + q, f(2e) = f0 + 2l + 4q  ->  q = (f2 - 2 f1 + f0)/2, l = f1 - f0 - q
        q = ((f2 - 2 * f1 + f0) % p * inv2) % p; l = (f1 - f0 - q) % p
        lin[:, i] = l; quad[(i, i)] = q; fe.append(f1)
    for i in range(nvar):
        for j in range(i + 1, nvar):
            e = np.zeros(nvar, dtype=np.int64); e[i] = 1; e[j] = 1; fij = f(e)
            quad[(i, j)] = (fij - fe[i] - fe[j] + f0) % p
    def model(u):
        u = np.asarray(u, dtype=np.int64) % p
        val = (f0 + lin @ u) % p
        for (i, j), q in quad.items():
            c = int(u[i]) * int(u[j]) % p
            if c: val = (val + c * q) % p
        return val
    ok = True
    for _ in range(checks):
        u = np.array([rng.randrange(p) for _ in range(nvar)], dtype=np.int64)
        if np.any((model(u) - f(u)) % p): ok = False
    return f0, lin, quad, model, ok

def groebner_decide(quads_coeffs, nvar, p, names):
    """quads_coeffs: list of dicts monomial-tuple -> coefficient; returns (basis_is_one, basis)"""
    import sympy as sp
    xs = sp.symbols(names[:nvar])
    polys = []
    for cf in quads_coeffs:
        expr = 0
        for mono, c in cf.items():
            c = int(c) % p
            if c == 0: continue
            if c > p // 2: c -= p
            term = sp.Integer(c)
            for i in mono: term = term * xs[i]
            expr += term
        if expr != 0: polys.append(sp.Poly(expr, *xs, modulus=p))
    if not polys: return False, []
    G = sp.groebner(polys, *xs, modulus=p, order='grevlex')
    return (len(G.exprs) == 1 and G.exprs[0].is_number and G.exprs[0] != 0), G

def analyse(st, Yc, ylabel, v0, vlabel, kap_blocks, rng):
    p = st.p
    Y = st.direction(Yc)
    nk = sum(len(b) for b in kap_blocks.values())
    nvar = 24 + nk
    f = lambda u: evaluate(st, Y, u, v0, 8, None, kap_blocks)
    t1 = time.time()
    f0, lin, quad, model, ok = interpolate_quadratic(f, nvar, p, rng)
    N = f0.shape[0]
    # which quadratic terms are actually present?
    qpairs = sorted(k for k, q in quad.items() if q.any())
    inv = lambda i: ("lam2" if i < 8 else "lam3" if i < 16 else "lam4" if i < 24 else "kappa") + f"[{i if i < 24 else i - 24}]"
    print(f"    {ylabel}, target {vlabel}: {N} equations in {nvar} unknowns; quadratic model exact at random points: {ok}; "
          f"quadratic terms among blocks: {sorted(set((inv(i)[:4], inv(j)[:4]) for i, j in qpairs))}   ({time.time() - t1:.0f} s)")
    # the greedy/feasible check: is u = 0 feasible? (no: the relator forces lam's) -- solve the LINEAR part for the affine unknowns
    # unknowns entering only linearly: those i with no quadratic term
    quad_vars = sorted(set(i for (i, j) in qpairs for i in (i, j)))
    lin_vars = [i for i in range(nvar) if i not in quad_vars]
    A_lin = lin[:, lin_vars]
    sol = Solver(A_lin, p)
    Qp = sol.Q                                                       # projector killing the linear unknowns' contributions
    # remaining system: Qp (f0 + lin[:, quad_vars] u_q + quad(u_q)) = 0 in the quadratic unknowns u_q
    Rl = (Qp @ lin[:, quad_vars]) % p; R0 = (Qp @ f0) % p
    eqs = []
    for r in range(Qp.shape[0]):
        cf = {}
        if R0[r]: cf[()] = int(R0[r])
        for a, i in enumerate(quad_vars):
            if Rl[r, a]: cf[(a,)] = int(Rl[r, a])
        for (i, j), q in quad.items():
            if i in quad_vars and j in quad_vars:
                c = int((Qp[r] @ q) % p)
                if c: cf[(quad_vars.index(i), quad_vars.index(j))] = c
        if cf: eqs.append(cf)
    # reduce to a basis of the span of the equations (as vectors over the monomials)
    monos = sorted(set(m for cf in eqs for m in cf))
    Mat = np.array([[cf.get(m, 0) for m in monos] for cf in eqs], dtype=np.int64) % p if eqs else np.zeros((0, 0), dtype=np.int64)
    if eqs:
        srow = Solver(Mat.T, p)                                     # rank of the equation span
        # take the pivot rows of a row-reduction of Mat: use Solver on Mat.T: pivots index independent rows
        basis_rows = srow.piv
        eqs_b = [eqs[i] for i in basis_rows]
    else: eqs_b = []
    # is the constant equation present (inconsistent already at linear level)?
    print(f"        after eliminating the {len(lin_vars)} linear unknowns: {len(eqs)} equations, {len(eqs_b)} independent, in the {len(quad_vars)} quadratic unknowns {[inv(i) for i in quad_vars]}")
    if any(set(cf) == {()} for cf in eqs_b):
        print(f"        ==> INCONSISTENT at the linear level (a non-zero constant equation): no branch keeps {vlabel} through order 4")
        return "none"
    if not eqs_b:
        print(f"        ==> no remaining equations: branches keeping {vlabel} through order 4 EXIST (an affine family)")
        return "exists"
    names = [inv(i).replace("[", "_").replace("]", "") for i in quad_vars]
    t2 = time.time()
    one, G = groebner_decide(eqs_b, len(quad_vars), p, names)
    if one:
        print(f"        ==> Groebner basis {{1}}: NO branch tangent to {ylabel} keeps {vlabel} through order 4   ({time.time() - t2:.0f} s)")
        return "none"
    print(f"        ==> Groebner basis has {len(G.exprs)} elements (not {{1}}): candidate branches keeping {vlabel} through order 4 exist; first elements: {[str(g)[:80] for g in G.exprs[:4]]}   ({time.time() - t2:.0f} s)")
    return "candidate"

def affine_rows(st, Yc, v0, rng):
    """the affine model (constant, linear part over lam2, lam3) of coker R3, o2(v0), o3(v0) -- Pass A unknowns, orders <= 3 only"""
    p = st.p; Y = st.direction(Yc)
    def f(u16):
        u = np.concatenate([u16, np.zeros(8, dtype=np.int64)])
        Ev = evaluate(st, Y, u, v0, 8, None, {})
        return np.concatenate([Ev[0:659], Ev[1318:1348], Ev[1348:1378]])          # coker R3 | o2 | o3
    f0 = f(np.zeros(16, dtype=np.int64)); lin = np.zeros((f0.shape[0], 16), dtype=np.int64)
    for i in range(16):
        e = np.zeros(16, dtype=np.int64); e[i] = 1; lin[:, i] = (f(e) - f0) % p
    u = np.array([rng.randrange(p) for _ in range(16)], dtype=np.int64)
    assert not np.any((f0 + lin @ u - f(u)) % p), "the orders <= 3 system is not affine in (lam2, lam3)"
    return f0, lin

def others_persist_on_the_feasible_set(st, Yc, a, rng):
    """do the other two cusp-fixed vectors persist through order 3 on every branch in F3' = {coker R3 = 0, o2(e_a) = 0, o3(e_a) = 0}?
    (then the kappa-terms vanish identically there and Pass A is complete for e_a).  Linear test: the affine functionals o2(e_b), o3(e_b)
    lie in the affine row space of the defining system."""
    p = st.p
    f0, lin = affine_rows(st, Yc, st.K[a], rng)
    A = np.hstack([lin, f0.reshape(-1, 1)]) % p                      # rows: (coefficients, constant)
    base = Solver(A.T, p).rank
    ok = True
    for b in range(3):
        if b == a: continue
        g0, glin = affine_rows(st, Yc, st.K[b], rng)
        Ob = np.hstack([glin[659:], g0[659:].reshape(-1, 1)]) % p     # o2(e_b), o3(e_b) rows
        if Solver(np.vstack([A, Ob]).T, p).rank != base: ok = False
    return ok

if __name__ == "__main__":
    results = {}
    for ip, p in enumerate(PR):
        st = Setting(p); rng = random.Random(1000 + ip)
        print(f"=== prime p = {p}: rank d1 = {st.d1.rank}, dim coker T0 = {st.tsol.Q.shape[0]}, cusp-fixed vectors of rho_0: {st.K.shape[0]}   ({time.time() - t0:.0f} s)")
        keep = [[not np.any(st.tsol.coker(st.zT[i] @ st.K[a])) for i in range(8)] for a in range(3)]
        for a in range(3): print(f"    fixed vector {a}: kept to first order by {[st.labels[i] for i in range(8) if keep[a][i]]}")
        dirs = {"V10": [0, 0, 0, 0, 1, 0, 0, 0], "V10#2": [0, 0, 0, 0, 0, 1, 0, 0], "V10 + V10#2": [0, 0, 0, 0, 1, 1, 0, 0], "V10 - V10#2": [0, 0, 0, 0, 1, p - 1, 0, 0]}
        for ylabel, Yc in dirs.items():
            Y = st.direction(Yc)
            X, failed = st.branch(Y, {}, 4)
            Bs = []
            for Z in st.Zs:
                def Q(A):
                    ser = OH.rel_series(st.M, st.Mi, {g: [zero, A[g]] for g in (1, 2)}, p, 2); return ser[2].reshape(-1)
                qy, qz = Q(Y), Q(Z); qyz = Q({g: (Y[g] + Z[g]) % p for g in (1, 2)})
                Bs.append((qyz - qy - qz) % p)
            rB = Solver(np.array([st.d1.coker(b) for b in Bs]).T % p, p).rank
            print(f"    {ylabel}: the branch with no class additions builds to order {failed - 1 if failed else 4}" + (f" (the relator at order {failed} needs a class at order {failed - 1})" if failed else "") + f"; the relator constrains {rB} of the 8 class directions at each order ({8 - rB} free, the direction itself among them)")
        rv = np.array([rng.randrange(p) for _ in range(3)], dtype=np.int64); vr = (rv @ st.K) % p
        for ylabel, Yc in dirs.items():
            print(f"  -- direction {ylabel}: Pass A (no kappa-terms)")
            for a in range(3):
                results[(p, ylabel, f"e{a}", "A")] = analyse(st, Yc, ylabel, st.K[a], f"e{a}", {}, rng)
            results[(p, ylabel, "random v0", "A")] = analyse(st, Yc, ylabel, vr, "random v0", {}, rng)
            print(f"  -- direction {ylabel}: do the other fixed vectors persist through order 3 on every branch allowed for e_a? (then Pass A is complete)")
            for a in range(3):
                ok = others_persist_on_the_feasible_set(st, Yc, a, rng)
                print(f"        e{a}: {'yes -- Pass A complete' if ok else 'NO -- kappa-terms needed: Pass C'}")
                results[(p, ylabel, f"e{a}", "others")] = ok
                if not ok:
                    lost = [b for b in range(3) if b != a]
                    kb = {1: [st.K[b] for b in lost], 2: [st.K[b] for b in lost]}
                    results[(p, ylabel, f"e{a}", "C")] = analyse(st, Yc, ylabel, st.K[a], f"e{a} (with kappa)", kb, rng)
        print(f"    ({time.time() - t0:.0f} s)")
    print("\n=== summary ===")
    for key, val in results.items(): print(f"    p = {key[0]}, {key[1]:12s}, {key[2]:10s}, pass {key[3]}: {val}")
    print(f"[{time.time() - t0:.0f} s]")
