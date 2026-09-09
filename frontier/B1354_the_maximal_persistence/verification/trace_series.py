#!/usr/bin/env python3
"""B1354 stage 2' -- WHAT KIND OF BRANCH IS IT?  Along a formal branch rho_t = exp(X(t)) rho_0 the traces tr rho_t(w) are power series
in t.  A branch whose traces are all constant is a deformation inside the fibre of the character map over chi(rho_0) -- at the
reducible subregular point (27 = 13 + 9 + 5) such deformations exist (extensions of the summands; non-semisimple representations
with the same character as rho_0) and are invisible to the character variety, hence to the physics.  A branch whose traces move
is a genuine curve of characters.  Test, exactly modulo p, through order K: (a) the tuned branch of continuation.py (all three
cusp-fixed vectors kept through order K); (b) the greedy branch of obstruction_higher.py (fixed vectors lost at order 4; the
Newton curve's model).  For each: the first order at which any of the traces tr rho_t(w), w in {a, b, ab, a^2 b, [a,b], b a^2,
longitude, a b^-1}, moves; and the self-duality defects tr rho_t(w) - tr rho_t(w^-1) by order.
Usage: python3 trace_series.py [KMAX] [prime]"""
from __future__ import annotations
import os, sys, time, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import persistence_tower as PT
import continuation as C
from persistence_tower import zero, I27, n, OH, S
t0 = time.time()
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
p = int(sys.argv[2]) if len(sys.argv) > 2 else 67108819
st = PT.Setting(p); rng = random.Random(77)
Yc = [0, 0, 0, 0, 1, 0, 0, 0]; Y = st.direction(Yc)

def greedy_branch(K):
    """obstruction_higher.py's greedy continuation: at each order solve d1 X_k = -R_k, using the class freedom at order k-1 when needed"""
    def polar(Z):
        def Q(A):
            ser = OH.rel_series(st.M, st.Mi, {g: [zero, A[g]] for g in (1, 2)}, p, 2); return ser[2].reshape(-1)
        qy, qz = Q(Y), Q(Z); qyz = Q({g: (Y[g] + Z[g]) % p for g in (1, 2)}); return (qyz - qy - qz) % p
    Bs = [polar(Z) for Z in st.Zs]
    X = {g: [zero, Y[g]] for g in (1, 2)}
    for k in range(2, K + 1):
        Xk = {g: X[g] + [zero] for g in (1, 2)}
        R = OH.rel_series(st.M, st.Mi, Xk, p, k); b = (-R[k].reshape(-1)) % p
        x = st.d1.part(b)
        if x is None:
            cols = [[int(v) for v in c] for c in st.D.T] + [[int(v) for v in B] for B in Bs]
            x2 = OH.solve_mod(cols, [int(v) for v in b], p); assert x2 is not None, k
            lam = x2[156:]; x = np.array(x2[:156], dtype=np.int64)
            for g in (1, 2): Xk[g][k - 1] = (Xk[g][k - 1] + sum(((lam[i] * st.Zs[i][g]) % p for i in range(8)), zero.copy())) % p
        corr = st.unflat(x)
        for g in (1, 2): Xk[g][k] = corr[g] % p
        X = Xk
        chk = OH.rel_series(st.M, st.Mi, X, p, k); assert all(not chk[j].any() for j in range(1, k + 1)), k
    return X

def tuned_branch(K):
    fam = (np.zeros(8, dtype=np.int64), np.eye(8, dtype=np.int64)); lams_fixed = {}
    ok, lam_fixed, fam_next, L = C.solve_step(st, Y, lams_fixed, 4, fam, rng, "lam2 symbolic"); assert ok
    lams_fixed[2] = lam_fixed; fam = fam_next
    for k in range(5, K + 1):
        ok, lam_fixed, fam_next, L = C.solve_step(st, Y, lams_fixed, k, fam, rng, f"lam{k-2} symbolic"); assert ok
        lams_fixed[k - 2] = lam_fixed; fam = fam_next
    full = dict(lams_fixed); full[K - 1] = L[K - 1]; full[K] = L[K]
    Ev, X, T = C.equations(st, Y, full, K); assert not np.any(Ev)
    return X, T

WORDS = {"a": [1], "b": [2], "ab": [1, 2], "a^2 b": [1, 1, 2], "[a,b]": [1, 2, -1, -2], "b a^2": [2, 1, 1], "longitude": S.LONG, "a b^-1": [1, -2]}
def inv(w): return [-x for x in reversed(w)]
def report(label, X, K):
    print(f"=== {label} ===")
    first_move = None
    for name, w in WORDS.items():
        ser = PT.word_series(st.M, st.Mi, X, p, K, w); tr = [int(np.trace(s) % p) for s in ser]
        seri = PT.word_series(st.M, st.Mi, X, p, K, inv(w)); tri = [int(np.trace(s) % p) for s in seri]
        moves = [k for k in range(1, K + 1) if tr[k]]; defects = [k for k in range(1, K + 1) if (tr[k] - tri[k]) % p]
        print(f"    tr rho_t({name:9s}): non-zero coefficients at orders {moves if moves else 'none'};  self-duality defect at orders {defects if defects else 'none'}")
        if moves and (first_move is None or moves[0] < first_move): first_move = moves[0]
    print(f"    ==> the character {'is constant through order ' + str(K) + ' (a deformation inside the fibre of the character map)' if first_move is None else 'moves first at order ' + str(first_move)}")

Xg = greedy_branch(KMAX)
Tg = st.T_series(Xg, KMAX)
print(f"greedy branch: Toeplitz kd = {st.toeplitz_kd(Tg, KMAX)}   ({time.time() - t0:.0f} s)")
report("the greedy branch (fixed vectors lost at order 4)", Xg, KMAX)
Xt, Tt = tuned_branch(KMAX)
print(f"tuned branch: Toeplitz kd = {st.toeplitz_kd(Tt, KMAX)}   ({time.time() - t0:.0f} s)")
report("the tuned branch (all three fixed vectors kept)", Xt, KMAX)
print(f"[{time.time() - t0:.0f} s]")
