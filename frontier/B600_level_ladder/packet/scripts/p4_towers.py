"""P4 — L76: the two towers, exact.

Tower 1 (cover torsion / P8): t_n = |det(A1^n - I)|, A1 = [[2,1],[1,1]], n = 1..24 exact.
Tower 2 (escalator charge / B556): e_n = det(I - M_n), M_1 = T(F), T(M) = [[M,M],[M^2,M]],
F = [[0,1],[1,1]]; sizes 2^(n+1).
  - exact (fraction-free Bareiss, python ints) for n = 1..6 (sizes 4..128);
  - mod-p (numpy F_p elimination) for n = 1..12 at p = 11 and n = 1..10 for all
    primes 3 <= p <= 79 (extends the banked "only 11 divides any e_n" scan);
  - mod-p validated against the exact values on n <= 6.

Preregistered tests:
  (i)  11-loci: 11 | t_n <=> n ≡ 0 (mod 5)  vs banked  11 | e_n <=> n ≡ 1 (mod 3);
       first predicted DOUBLE point n = 10 — decided here.
  (ii) gcd(t_n, e_n) table on the exact range.
  (iii) norm-form data readout (no fit).
Banked cross-checks: e_1 = -11; e_4 = -(11^2 * 1459 * 597049 * 2169349081).
"""
import numpy as np
from math import gcd

import sympy as sp


# ---------- tower 1 ----------
def torsion_tower(nmax=24):
    A = [[2, 1], [1, 1]]

    def matmul2(X, Y):
        return [[X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]],
                [X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]]]

    out, P = {}, [[1, 0], [0, 1]]
    for n in range(1, nmax + 1):
        P = matmul2(P, A)
        d = (P[0][0] - 1) * (P[1][1] - 1) - P[0][1] * P[1][0]
        out[n] = abs(d)
    return out


# ---------- tower 2, exact ----------
def matmul_big(X, Y):
    n, m, k = len(X), len(Y[0]), len(Y)
    Yt = list(zip(*Y))
    return [[sum(X[i][t] * Yt[j][t] for t in range(k)) for j in range(m)] for i in range(n)]


def T_step(M):
    M2 = matmul_big(M, M)
    n = len(M)
    top = [M[i] + M[i] for i in range(n)]
    bot = [M2[i] + M[i] for i in range(n)]
    return top + bot


def bareiss_det(A):
    """Fraction-free Bareiss determinant on python ints (destructive on a copy)."""
    A = [row[:] for row in A]
    n = len(A)
    sign, prev = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if piv is None:
                return 0
            A[k], A[piv] = A[piv], A[k]
            sign = -sign
        for i in range(k + 1, n):
            Aik = A[i][k]
            Akk = A[k][k]
            rowk = A[k]
            rowi = A[i]
            for j in range(k + 1, n):
                rowi[j] = (Akk * rowi[j] - Aik * rowk[j]) // prev
            rowi[k] = 0
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def charge_tower_exact(nmax=6):
    F = [[0, 1], [1, 1]]
    out, M = {}, F
    for n in range(1, nmax + 1):
        M = T_step(M)
        n_dim = len(M)
        ImM = [[(1 if i == j else 0) - M[i][j] for j in range(n_dim)] for i in range(n_dim)]
        out[n] = bareiss_det(ImM)
    return out


# ---------- tower 2, mod p ----------
def det_mod_p(A, p):
    A = A.astype(np.int64) % p
    n = A.shape[0]
    det = 1
    for i in range(n):
        piv = np.nonzero(A[i:, i])[0]
        if piv.size == 0:
            return 0
        j = i + int(piv[0])
        if j != i:
            A[[i, j]] = A[[j, i]]
            det = (-det) % p
        inv = pow(int(A[i, i]), p - 2, p)
        det = (det * int(A[i, i])) % p
        if i + 1 < n:
            f = (A[i + 1:, i] * inv) % p
            A[i + 1:, i:] = (A[i + 1:, i:] - np.outer(f, A[i, i:])) % p
    return det


def charge_tower_mod_p(p, nmax):
    F = np.array([[0, 1], [1, 1]], dtype=np.int64) % p
    out, M = {}, F
    for n in range(1, nmax + 1):
        M2 = (M @ M) % p
        M = np.block([[M, M], [M2, M]]) % p
        ImM = (np.eye(M.shape[0], dtype=np.int64) - M) % p
        out[n] = det_mod_p(ImM, p)
    return out


def main():
    print("=== tower 1: t_n = |det(A1^n - I)|, n = 1..24 ===")
    t = torsion_tower(24)
    for n in range(1, 25):
        print(f"  t_{n} = {t[n]}" + ("   [11 | t]" if t[n] % 11 == 0 else ""))
    pat_t = [n for n in t if t[n] % 11 == 0]
    print(f"11-locus of t: {pat_t}  (prediction: multiples of 5)")
    assert pat_t == [n for n in range(1, 25) if n % 5 == 0]

    print("\n=== tower 2 exact: e_n = det(I - M_n), n = 1..6 ===")
    e = charge_tower_exact(6)
    for n, v in e.items():
        print(f"  e_{n} = {v}" + ("   [11 | e]" if v % 11 == 0 else ""))
    assert e[1] == -11, "banked e_1 = -11 FAILED"
    banked_e4 = -(11 ** 2 * 1459 * 597049 * 2169349081)
    print(f"banked e_4 cross-check: e_4 == -(11^2*1459*597049*2169349081) : {e[4] == banked_e4}")

    print("\n=== tower 2 mod 11, n = 1..12 ===")
    e11 = charge_tower_mod_p(11, 12)
    for n in range(1, 13):
        ok = "" if n > 6 else f"  (exact check: {'OK' if e11[n] == e[n] % 11 else 'MISMATCH'})"
        print(f"  e_{n} mod 11 = {e11[n]}" + ("   [11 | e]" if e11[n] == 0 else "") + ok)
    loc_e = [n for n in range(1, 13) if e11[n] == 0]
    print(f"11-locus of e (n <= 12): {loc_e}  (banked law predicts n ≡ 1 mod 3: "
          f"{[n for n in range(1, 13) if n % 3 == 1]})")

    print("\n=== test (i): the interlock at n = 10 ===")
    both = (t[10] % 11 == 0) and (e11[10] == 0)
    print(f"n = 10: 11|t_10 = {t[10] % 11 == 0}, 11|e_10 = {e11[10] == 0}  -> DOUBLE POINT: {both}")

    print("\n=== test (ii): gcd(t_n, e_n), exact range ===")
    for n in range(1, 7):
        print(f"  gcd(t_{n}, e_{n}) = {gcd(t[n], abs(e[n]))}")

    print("\n=== the wide prime scan: p in 3..79, n <= 10 (extends the banked 'only 11') ===")
    hits = {}
    for p in [3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]:
        ep = charge_tower_mod_p(p, 10)
        zz = [n for n, v in ep.items() if v == 0]
        if zz:
            hits[p] = zz
        print(f"  p = {p}: e_n ≡ 0 at n = {zz if zz else 'none'}")
    print(f"\nprimes 3..79 dividing some e_n (n <= 10): {sorted(set(hits) | {11})}")

    print("\n=== test (iii): norm-form data readout ===")
    # t_n = |N_{Q(sqrt5)}(phi^{2n} - 1)| = |L_{2n} - 2|; print L-form alongside e_n
    for n in range(1, 7):
        print(f"  n={n}: t_n = L_{2*n}-2-form = {t[n]}, e_n = {e[n]}, "
              f"e_n/t_n = {sp.Rational(e[n], t[n])}")


if __name__ == '__main__':
    main()
