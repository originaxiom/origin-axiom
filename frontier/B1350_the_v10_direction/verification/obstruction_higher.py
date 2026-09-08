#!/usr/bin/env python3
"""B1350 stage (5c): FORMAL INTEGRABILITY of the V10 classes to higher order, exactly modulo two primes.

Stage (5b) found every block class -- the two V10's included -- unobstructed at second order, so the Newton stall of stage (4)
is not a second-order obstruction.  Here the deformation rho_eps(g) = exp(X_g(eps)) rho_0(g), X_g = eps Y_g + eps^2 W_g + eps^3 V_g + ...,
is continued order by order: at order k the relator's coefficient R_k must lie in im d1 up to the freedom of adding cocycles at
order k-1 (which changes R_k by the polarised second-order form B(Y, Z)); solvable => continue; unsolvable => OBSTRUCTED at
order k.  THE METHOD IS ONE-SIDED: 'integrable to order k' exhibits a formal solution and is exact; 'obstructed at order k'
uses only the cocycle freedom at order k-1 (whose effect on order k is the linear term B(Y, Z)) and NOT the freedom at orders
<= k-2, whose effect on order k is non-linear -- so an 'obstructed' verdict here is a failure of this greedy continuation, not
a theorem.  The V8 control shows exactly that: the greedy continuation stops at order 5, while B1268's Newton search
converged (residual 1e-63) to a genuine theta-odd representation along V8.  Run for the two V10 classes, their sum and
difference, and the V8 control."""
from __future__ import annotations
import sys, time
import numpy as np
import obstruction as O
E, S, Qw = O.E, O.S, O.Qw
t0 = time.time()
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
PR = [int(x) for x in sys.argv[2:]] or [67108819, 67108837]

def ser_mul(P, Q, p, deg):
    n = P[0].shape[0]
    out = [np.zeros((n, n), dtype=np.int64) for _ in range(deg + 1)]
    for i, Pi in enumerate(P):
        if i > deg or not Pi.any(): continue
        for j, Qj in enumerate(Q):
            if i + j > deg: break
            if not Qj.any(): continue
            out[i + j] = (out[i + j] + (Pi @ Qj) % p) % p
    return out

def ser_exp(X, p, deg):
    """exp of a series with X[0] = 0, truncated at deg."""
    n = X[0].shape[0]
    I = np.eye(n, dtype=np.int64)
    out = [I] + [np.zeros((n, n), dtype=np.int64) for _ in range(deg)]
    term = [I] + [np.zeros((n, n), dtype=np.int64) for _ in range(deg)]
    fact = 1
    for j in range(1, deg + 1):
        term = ser_mul(term, X, p, deg)
        fact = fact * j % p
        inv = pow(fact, -1, p)
        out = [(o + t * inv) % p for o, t in zip(out, term)]
    return out

def rel_series(M, Mi, X, p, deg):
    """rho_eps(REL) to order deg for rho_eps(g) = exp(X_g) rho_0(g); X = {g: [0, X1, X2, ...]} (mod p)."""
    n = 27
    def letter(L):
        g = abs(L)
        Xg = [x % p for x in X[g]] + [np.zeros((n, n), dtype=np.int64)] * (deg + 1 - len(X[g]))
        if L > 0:
            ex = ser_exp(Xg[:deg + 1], p, deg)
            return [(e @ M[g]) % p for e in ex]
        ex = ser_exp([(-x) % p for x in Xg[:deg + 1]], p, deg)
        return [(Mi[g] @ e) % p for e in ex]
    cur = [np.eye(n, dtype=np.int64)] + [np.zeros((n, n), dtype=np.int64)] * deg
    for L in S.REL:
        cur = ser_mul(cur, letter(L), p, deg)
    return cur

def solve_mod(cols, b, p):
    """particular solution x of sum_j x_j cols[j] = b over F_p, or None."""
    m = len(cols); nrow = len(b)
    A = [[cols[j][i] for j in range(m)] + [b[i] % p] for i in range(nrow)]
    r = 0; pivots = []
    for c in range(m):
        piv = next((i for i in range(r, nrow) if A[i][c] % p), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], -1, p); A[r] = [(x * inv) % p for x in A[r]]
        for i in range(nrow):
            if i != r and A[i][c] % p:
                f = A[i][c]; A[i] = [(x - f * y) % p for x, y in zip(A[i], A[r])]
        pivots.append(c); r += 1
        if r == nrow: break
    for i in range(r, nrow):
        if A[i][m] % p:
            return None
    x = [0] * m
    for i, c in enumerate(pivots):
        x[c] = A[i][m]
    return x

def run(p):
    red, w = O.make_red(p)
    print(f"=== (5c) formal integrability modulo p = {p} (omega -> {w}), orders 2 .. {KMAX} ===")
    M = {g: O.red_mat(O.rho0.M[g], red, p) for g in (1, 2)}
    Mi = {g: O.red_mat(O.rho0.I[g], red, p) for g in (1, 2)}
    REP = [np.array([[int(O.F(x).numerator) * pow(int(O.F(x).denominator), -1, p) % p for x in row] for row in E.REP[k].tolist()], dtype=np.int64) for k in range(78)]
    zero = np.zeros((27, 27), dtype=np.int64)
    def e6mat(Z):
        acc = zero.copy()
        for k in range(78):
            c = red(Z[k])
            if c: acc = (acc + c * REP[k]) % p
        return acc
    def unflat(x):
        return {1: sum(((x[k] * REP[k]) % p for k in range(78)), zero.copy()) % p, 2: sum(((x[78 + k] * REP[k]) % p for k in range(78)), zero.copy()) % p}
    # d1 columns (first-order relator coefficient of a basis element in one slot)
    cols = []
    for g in (1, 2):
        for k in range(78):
            X = {1: [zero, zero], 2: [zero, zero]}; X[g] = [zero, REP[k]]
            ser = rel_series(M, Mi, X, p, 1)
            cols.append([int(v) for v in ser[1].reshape(-1)])
    rk = O.rank_mod(cols, p); assert rk == 70, rk
    Ys = [{1: e6mat(Za), 2: e6mat(Zb)} for _, Za, Zb in O.COC]
    labels = [f"V{w_}" + ("#2" if i == 5 else "") for i, (w_, _, _) in enumerate(O.COC)]
    def polar(Y, Z):
        def Q(A):
            ser = rel_series(M, Mi, {g: [zero, A[g]] for g in (1, 2)}, p, 2)
            assert not ser[1].any()
            return [int(v) for v in ser[2].reshape(-1)]
        qy, qz = Q(Y), Q(Z); qyz = Q({g: (Y[g] + Z[g]) % p for g in (1, 2)})
        return [(a - b - c) % p for a, b, c in zip(qyz, qy, qz)]
    def integrate(Y, name):
        # the ambiguity columns at each order: B(Y, Z_i), i over the 8 classes
        Bs = [polar(Y, Z) for Z in Ys]
        rkB = O.rank_mod(cols + Bs, p)
        X = {g: [zero, Y[g]] for g in (1, 2)}
        for k in range(2, KMAX + 1):
            Xk = {g: X[g] + [zero] for g in (1, 2)}
            R = rel_series(M, Mi, Xk, p, k)
            for j in range(1, k):
                assert not R[j].any(), (name, k, j)
            b = [(-int(v)) % p for v in R[k].reshape(-1)]
            x = solve_mod(cols, b, p)
            used_amb = False
            if x is None and k >= 3:
                x2 = solve_mod(cols + Bs, b, p)
                if x2 is not None:
                    lam = x2[156:]; x = x2[:156]; used_amb = True
                    # add sum lam_i Z_i at order k-1
                    for g in (1, 2):
                        Xk[g][k - 1] = (Xk[g][k - 1] + sum(((lam[i] * Ys[i][g]) % p for i in range(8)), zero.copy())) % p
            if x is None:
                r_now = O.rank_mod(cols + Bs + [[(-v) % p for v in b]], p)
                print(f"    {name}: the greedy continuation STOPS at order {k} -- R_{k} is not in im d1 + span B(Y, Z_i) (rank {rkB} -> {r_now}); not a proof of obstruction (see the docstring)")
                return k
            corr = unflat(x)
            for g in (1, 2):
                Xk[g][k] = corr[g]
            X = Xk
            # verify
            chk = rel_series(M, Mi, X, p, k)
            assert all(not chk[j].any() for j in range(1, k + 1)), (name, k)
            print(f"    {name}: integrable to order {k}{' (using the cocycle freedom at order ' + str(k - 1) + ')' if used_amb else ''}")
        return None
    out = {}
    for i in (3, 4, 5):
        out[labels[i]] = integrate(Ys[i], labels[i])
    Yp = {g: (Ys[4][g] + Ys[5][g]) % p for g in (1, 2)}; Ym = {g: (Ys[4][g] - Ys[5][g]) % p for g in (1, 2)}
    out["V10+V10#2"] = integrate(Yp, "V10 + V10#2")
    out["V10-V10#2"] = integrate(Ym, "V10 - V10#2")
    print(f"    ({time.time() - t0:.0f} s)")
    return out

if __name__ == "__main__":
    res = [run(p) for p in PR]
    print("\n=== summary (order of the first obstruction; None = integrable through order", KMAX, ") ===")
    for k in res[0]:
        print(f"    {k:12s}: {res[0][k]}   agreement between primes: {all(r[k] == res[0][k] for r in res)}")
    print(f"[{time.time() - t0:.0f} s]")
