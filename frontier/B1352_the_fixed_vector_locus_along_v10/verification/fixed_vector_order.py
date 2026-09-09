#!/usr/bin/env python3
"""B1352 stage D -- THE ORDER AT WHICH THE CUSP-FIXED VECTORS ARE LOST ALONG THE FORMAL V10 BRANCHES, exactly modulo two primes.

Stage C showed that every V10 class keeps all three cusp-fixed vectors of rho_0 to first order; B1350's genuine V10 points
carry none (2000-bit read: the cusp-fixed matrix [mu - I; lambda - I] has full rank 27, its three smallest pivots ~1e-30,
1e-36, 1e-38 at a step of 0.02/|Y|).  Here the formal branch rho_t(g) = exp(X_g(t)) rho_0(g) of obstruction_higher.py
(integrable through order KMAX for every V10 class) is used to compute T(t) = [mu(t) - I; lambda(t) - I] as a 54x27 matrix
over F_p[t]/(t^(KMAX+1)), and the Smith exponents of its three non-unit invariant factors t^e1, t^e2, t^e3 from the
F_p-dimensions kd(m) = sum_i min(e_i, m) of ker(T mod t^m): #{i : e_i >= m} = kd(m) - kd(m-1).  e_i is the order at
which the i-th cusp-fixed vector is lost (persists modulo t^e_i, not modulo t^(e_i+1)); e_i > KMAX prints as '> KMAX'.
Three formal branches per direction: the greedy one of obstruction_higher.py, a randomised one (a random combination of
the eight classes added at every order >= 2 before solving) and a randomised one within the five classes that keep all
three cusp-fixed vectors to first order (V2, V6, V10, V10#2, V14; stage C), to see how the exponents depend on the branch.
The V8 control is integrated only as far as the greedy method goes (order 4).
Usage: python3 fixed_vector_order.py [KMAX] [prime ...]"""
from __future__ import annotations
import os, sys, time, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1350_the_v10_direction', 'verification'))
import obstruction_higher as OH
O, E, S = OH.O, OH.E, OH.S
t0 = time.time()
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10
PR = [int(x) for x in sys.argv[2:]] or [67108819, 67108837]
n = 27
zero = np.zeros((n, n), dtype=np.int64)
KEEP = (0, 2, 4, 5, 6)      # the classes that keep all three cusp-fixed vectors to first order (stage C): V2, V6, V10, V10#2, V14

def word_series(M, Mi, X, p, deg, word):
    """rho_t(word) to order deg for rho_t(g) = exp(X_g(t)) rho_0(g), X = {g: [0, X1, X2, ...]} (mod p)."""
    def letter(L):
        g = abs(L)
        Xg = [x % p for x in X[g]] + [zero] * (deg + 1 - len(X[g]))
        if L > 0:
            ex = OH.ser_exp(Xg[:deg + 1], p, deg)
            return [(e @ M[g]) % p for e in ex]
        ex = OH.ser_exp([(-x) % p for x in Xg[:deg + 1]], p, deg)
        return [(Mi[g] @ e) % p for e in ex]
    cur = [np.eye(n, dtype=np.int64)] + [zero] * deg
    for L in word:
        cur = OH.ser_mul(cur, letter(L), p, deg)
    return cur

def rank_mod_np(A, p):
    """rank over F_p of an int64 numpy matrix (entries reduced mod p; p < 2^31 so products fit in int64)."""
    A = A.copy() % p
    nrow, ncol = A.shape
    r = 0
    for c in range(ncol):
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0: continue
        piv = r + nz[0]
        if piv != r: A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), -1, p)
        A[r] = (A[r] * inv) % p
        rows = np.nonzero(A[:, c])[0]
        rows = rows[rows != r]
        if rows.size:
            A[rows] = (A[rows] - np.outer(A[rows, c], A[r])) % p
        r += 1
        if r == nrow: break
    return r

def smith_exponents(T, p, K):
    """T = [T_0, ..., T_K] (54x27 mod p).  kd(m) = dim_Fp ker(T mod t^m) for m = 1..K+1, then #{e_i >= m}."""
    kd = [0]
    for m in range(1, K + 2):
        big = np.zeros((54 * m, 27 * m), dtype=np.int64)
        for i in range(m):
            for j in range(i + 1):
                big[54 * i:54 * (i + 1), 27 * j:27 * (j + 1)] = T[i - j]
        kd.append(27 * m - rank_mod_np(big, p))
    counts = [kd[m] - kd[m - 1] for m in range(1, K + 2)]      # counts[m-1] = #{i : e_i >= m}
    exps = []
    for m in range(1, K + 2):
        c_here = counts[m - 1] - (counts[m] if m <= K else 0)   # #{i : e_i = m} for m <= K
        if m <= K: exps += [m] * c_here
    beyond = counts[K]                                           # #{i : e_i >= K+1}
    return kd[1:], exps, beyond

def run(p, rng_seed):
    red, w = O.make_red(p)
    print(f"=== stage D modulo p = {p} (omega -> {w}), branches to order {KMAX} ===")
    M = {g: O.red_mat(O.rho0.M[g], red, p) for g in (1, 2)}
    Mi = {g: O.red_mat(O.rho0.I[g], red, p) for g in (1, 2)}
    REP = [np.array([[int(O.F(x).numerator) * pow(int(O.F(x).denominator), -1, p) % p for x in row] for row in E.REP[k].tolist()], dtype=np.int64) for k in range(78)]
    def e6mat(Z):
        acc = zero.copy()
        for k in range(78):
            c = red(Z[k])
            if c: acc = (acc + c * REP[k]) % p
        return acc
    def unflat(x):
        return {1: sum(((x[k] * REP[k]) % p for k in range(78)), zero.copy()) % p, 2: sum(((x[78 + k] * REP[k]) % p for k in range(78)), zero.copy()) % p}
    cols = []
    for g in (1, 2):
        for k in range(78):
            X = {1: [zero, zero], 2: [zero, zero]}; X[g] = [zero, REP[k]]
            ser = OH.rel_series(M, Mi, X, p, 1)
            cols.append([int(v) for v in ser[1].reshape(-1)])
    Ys = [{1: e6mat(Za), 2: e6mat(Zb)} for _, Za, Zb in O.COC]
    labels = [f"V{w_}" + ("#2" if i == 5 else "") for i, (w_, _, _) in enumerate(O.COC)]
    def polar(Y, Z):
        def Q(A):
            ser = OH.rel_series(M, Mi, {g: [zero, A[g]] for g in (1, 2)}, p, 2)
            assert not ser[1].any()
            return [int(v) for v in ser[2].reshape(-1)]
        qy, qz = Q(Y), Q(Z); qyz = Q({g: (Y[g] + Z[g]) % p for g in (1, 2)})
        return [(a - b - c) % p for a, b, c in zip(qyz, qy, qz)]
    def integrate(Y, name, kmax, rng=None, keep=None):
        """the formal branch to order kmax (greedy, as obstruction_higher.py; rng: a random class combination added at
        every order >= 2 before solving, restricted to the classes in `keep` when given).  Returns (X, reached_order)."""
        Bs = [polar(Y, Z) for Z in Ys]
        X = {g: [zero, Y[g]] for g in (1, 2)}
        for k in range(2, kmax + 1):
            Xk = {g: X[g] + [zero] for g in (1, 2)}
            if rng is not None and k >= 3:
                lam = [rng.randrange(p) if (keep is None or i in keep) else 0 for i in range(8)]
                for g in (1, 2):
                    Xk[g][k - 1] = (Xk[g][k - 1] + sum(((lam[i] * Ys[i][g]) % p for i in range(8)), zero.copy())) % p
            R = OH.rel_series(M, Mi, Xk, p, k)
            for j in range(1, k):
                assert not R[j].any(), (name, k, j)
            b = [(-int(v)) % p for v in R[k].reshape(-1)]
            x = OH.solve_mod(cols, b, p)
            if x is None and k >= 3:
                x2 = OH.solve_mod(cols + Bs, b, p)
                if x2 is not None:
                    lam = x2[156:]; x = x2[:156]
                    for g in (1, 2):
                        Xk[g][k - 1] = (Xk[g][k - 1] + sum(((lam[i] * Ys[i][g]) % p for i in range(8)), zero.copy())) % p
            if x is None:
                return X, k - 1
            corr = unflat(x)
            for g in (1, 2):
                Xk[g][k] = corr[g]
            X = Xk
            chk = OH.rel_series(M, Mi, X, p, k)
            assert all(not chk[j].any() for j in range(1, k + 1)), (name, k)
        return X, kmax
    out = {}
    T0 = np.vstack([(M[1] - np.eye(n, dtype=np.int64)) % p, (word_series(M, Mi, {1: [zero], 2: [zero]}, p, 0, S.LONG)[0] - np.eye(n, dtype=np.int64)) % p])
    print(f"    at rho_0: rank of [mu - I; lambda - I] = {rank_mod_np(T0, p)} (cusp-fixed vectors: {27 - rank_mod_np(T0, p)})")
    dirs = [(labels[4], Ys[4]), (labels[5], Ys[5]),
            ("V10 + V10#2", {g: (Ys[4][g] + Ys[5][g]) % p for g in (1, 2)}), ("V10 - V10#2", {g: (Ys[4][g] - Ys[5][g]) % p for g in (1, 2)}),
            (labels[3], Ys[3])]
    for name, Y in dirs:
        for branch, rng, keep in (("greedy", None, None), ("random", random.Random(rng_seed), None), ("random-keep", random.Random(rng_seed + 1), KEEP)):
            kmax = KMAX if name != "V8" else 4
            X, K = integrate(Y, f"{name} [{branch}]", kmax, rng, keep)
            mu = word_series(M, Mi, X, p, K, [1])
            lam = word_series(M, Mi, X, p, K, S.LONG)
            T = [np.vstack([(mu[i] - (np.eye(n, dtype=np.int64) if i == 0 else 0)) % p, (lam[i] - (np.eye(n, dtype=np.int64) if i == 0 else 0)) % p]) for i in range(K + 1)]
            kd, exps, beyond = smith_exponents(T, p, K)
            out[(name, branch)] = (K, tuple(exps), beyond)
            print(f"    {name:12s} [{branch:6s}] branch to order {K}: kd(m) = {kd}; loss orders {exps}{'; ' + str(beyond) + ' vector(s) persist beyond order ' + str(K) if beyond else ''}   ({time.time() - t0:.0f} s)")
    return out

if __name__ == "__main__":
    res = [run(p, 12345 + i) for i, p in enumerate(PR)]
    print("\n=== summary: the orders at which the three cusp-fixed vectors are lost along each formal branch ===")
    for key in res[0]:
        K, exps, beyond = res[0][key]
        print(f"    {key[0]:12s} [{key[1]:6s}]: {exps}{' + ' + str(beyond) + ' beyond order ' + str(K) if beyond else ''}   agreement between primes: {all(r[key] == res[0][key] for r in res)}")
    print(f"[{time.time() - t0:.0f} s]")
