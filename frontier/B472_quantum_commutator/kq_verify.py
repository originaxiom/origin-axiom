#!/usr/bin/env python3
"""B472 — the quantum commutator kappa_q: the exact table, the (2,3) closure
theorem, and the Q8/SL(2,5) CRT mechanism. Third independent lift (the B465
engine), agreeing with seat-2's two lifts on all 25 entries."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B465_monodromy_intake"))
from exact_engine import build, matmul

EXPECTED = {1: [-1, 3, -5, 3, -1], 2: [3, 3, 15, 3, 3], 3: [-1, 3, -5, 3, -1],
            4: [3, 3, 15, 3, 3], 5: [-5, 15, -5, 15, -5]}


def matinv(M, p):
    n = len(M)
    A = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        piv = next(i for i in range(c, n) if A[i][c] % p)
        A[c], A[piv] = A[piv], A[c]
        inv = pow(A[c][c], p - 2, p)
        A[c] = [(x * inv) % p for x in A[c]]
        for i in range(n):
            if i != c and A[i][c]:
                f = A[i][c]
                A[i] = [(a - f * b) % p for a, b in zip(A[i], A[c])]
    return [row[n:] for row in A]


def matpow(M, k, p):
    n = len(M)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while k:
        if k & 1: R = matmul(R, M, p)
        M = matmul(M, M, p); k >>= 1
    return R


def main():
    ok = True
    for p in (61, 421):
        z, i4, W1, W2, Par = build(p, c=1)
        for j in range(1, 6):
            for l in range(1, 6):
                A = matpow(W1, j, p); B = matpow(W2, l, p)
                C = matmul(matmul(A, B, p), matmul(matinv(A, p), matinv(B, p), p), p)
                t = sum(C[i][i] for i in range(15)) % p
                ts = t if t <= p // 2 else t - p
                ok &= ts == EXPECTED[j][l - 1]
        A = matpow(W1, 2, p); B = matpow(W2, 3, p)
        C = matmul(matmul(A, B, p), matmul(matinv(A, p), matinv(B, p), p), p)
        ok &= all(C[i][jj] % p == (1 if i == jj else 0) for i in range(15) for jj in range(15))
        print(f"p={p}: table 25/25 + closure [W1^2,W2^3] = I: {ok}")
    # CRT mechanism (classical)
    def mm(A, B, m):
        return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0]) % m, (A[0][0]*B[0][1]+A[0][1]*B[1][1]) % m],
                [(A[1][0]*B[0][0]+A[1][1]*B[1][0]) % m, (A[1][0]*B[0][1]+A[1][1]*B[1][1]) % m]]
    def inv2(M, m):
        d = (M[0][0]*M[1][1]-M[0][1]*M[1][0]) % m; di = pow(d, -1, m)
        return [[(M[1][1]*di) % m, (-M[0][1]*di) % m], [(-M[1][0]*di) % m, (M[0][0]*di) % m]]
    A1 = [[2, 1], [1, 1]]; A2 = [[5, 2], [2, 1]]
    a3 = [[x % 3 for x in r] for r in A1]; b3 = [[x % 3 for x in r] for r in A2]
    negI3 = [[2, 0], [0, 2]]
    ok &= mm(a3, a3, 3) == negI3 and mm(b3, b3, 3) == negI3
    ok &= mm(mm(a3, b3, 3), mm(inv2(a3, 3), inv2(b3, 3), 3), 3) == negI3     # Q8
    a5 = [[x % 5 for x in r] for r in A1]; b5 = [[x % 5 for x in r] for r in A2]
    seen = {((1, 0), (0, 1))}
    frontier = [[[1, 0], [0, 1]]]
    while frontier:
        new = []
        for g in frontier:
            for h in (a5, b5, inv2(a5, 5), inv2(b5, 5)):
                x = mm(g, h, 5); k = tuple(map(tuple, x))
                if k not in seen:
                    seen.add(k); new.append(x)
        frontier = new
    ok &= len(seen) == 120                                                   # SL(2,5)
    print(f"CRT mechanism: Q8 mod 3 + SL(2,5) mod 5 (order {len(seen)}): {ok}")
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
