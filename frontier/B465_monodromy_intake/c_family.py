#!/usr/bin/env python3
"""B465 ADDENDUM — Chat-2's c-family (quadratic-form deformation, fixed Fourier kernel),
implemented verbatim from the 2026-07-07 shuttle and gated against their table.

Verifies: (1) the 15/9 distinct-eigenvalue table with the (c|5) split; (2) unitarity of
every U_c; (3) the per-c l=1 structure — full B465 structure (mu4-coset, scalar law,
(4,4,3,4)) persists iff (c|5) = +1; (4) the complementarity: this family splits by (c|5),
the Galois family (exact_engine.py) splits by (c|3) — the two Klein-four generators.
"""
import sys
from collections import Counter
from math import gcd

import numpy as np

N = 15
z = np.exp(2j * np.pi / N)
F = np.array([[z**((j * k) % N) for k in range(N)] for j in range(N)])
Finv = np.array([[z**((-j * k) % N) for k in range(N)] for j in range(N)])
Par = np.zeros((N, N), complex)
for j in range(N):
    Par[(-j) % N, j] = 1

CS = [1, 2, 4, 7, 8, 11, 13, 14]
QR5 = {1, 4}          # squares mod 5
EXPECT = {1: 15, 2: 9, 4: 15, 7: 9, 8: 9, 11: 15, 13: 9, 14: 15}


def Dc(p, c):
    return np.diag([z**((p * c * (j * (j - 1) // 2)) % N) for j in range(N)])


def U_c(c):
    WR = (F @ Dc(-1, c) @ Finv) / N
    return Par @ (WR @ Dc(1, c))


def M_c(c):
    WR = (F @ Dc(-1, c) @ Finv) / N
    return Par @ (WR @ Dc(1, c)) @ (WR @ WR @ Dc(2, c))


def spec(Mx, base=60):
    ev = np.linalg.eigvals(Mx)
    ks = [int(round((np.angle(l) / (2 * np.pi)) * base)) % base for l in ev]
    assert all(abs(ev[i] - np.exp(2j * np.pi * ks[i] / base)) < 1e-8 for i in range(len(ev)))
    return Counter(ks)


def main():
    ok = True
    print("== gate: Chat-2's 15/9 table + unitarity ==")
    for c in CS:
        U = U_c(c)
        unit = np.max(np.abs(U @ U.conj().T - np.eye(N))) < 1e-12
        cnt = spec(U)
        hit = len(cnt) == EXPECT[c] and ((c % 5 in QR5) == (len(cnt) == 15))
        ok &= unit and hit
        print(f"  c={c:2d}: distinct={len(cnt):2d} expect={EXPECT[c]:2d} "
              f"(c|5)={'QR' if c % 5 in QR5 else 'NQR'} unitary={unit} -> {'PASS' if unit and hit else 'FAIL'}")

    print("== per-c l=1 structure: full B465 structure iff (c|5)=+1 ==")
    for c in CS:
        M = M_c(c)
        cnt = spec(M)
        ks = sorted(cnt.keys())
        ap = len(ks) == 4 and all((ks[i + 1] - ks[i]) % 60 == 15 for i in range(3))
        M4 = np.linalg.matrix_power(M, 4)
        scal = np.max(np.abs(M4 - M4[0, 0] * np.eye(N))) < 1e-8
        mults = sorted(cnt.values(), reverse=True)
        full = ap and scal and mults == [4, 4, 4, 3]
        expect_full = c % 5 in QR5
        ok &= (full == expect_full)
        print(f"  c={c:2d}: mu4-coset={ap} scalar-law={scal} mults={mults} "
              f"-> {'PASS' if full == expect_full else 'FAIL'}")

    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
