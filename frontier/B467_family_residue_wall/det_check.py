#!/usr/bin/env python3
"""B467 registry-R2 verification: exact determinants of the seam operators (F_p)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B465_monodromy_intake"))
from exact_engine import build, matmul


def detmod(M, p):
    M = [row[:] for row in M]
    n = len(M)
    d = 1
    for c in range(n):
        piv = next((i for i in range(c, n) if M[i][c] % p), None)
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            d = -d
        d = (d * M[c][c]) % p
        inv = pow(M[c][c], p - 2, p)
        for i in range(c + 1, n):
            f = (M[i][c] * inv) % p
            M[i] = [(a - f * b) % p for a, b in zip(M[i], M[c])]
    return d % p


def main():
    ok = True
    for p in (61, 421):
        z, i4, W1, W2, Par = build(p, c=1)
        dW1, dW2, dPar = detmod(W1, p), detmod(W2, p), detmod(Par, p)
        dM = detmod(matmul(matmul(Par, W1, p), W2, p), p)
        good = dW1 == 1 and dW2 == 1 and dPar == p - 1 and dM == p - 1
        ok &= good
        print(f"p={p}: det(W1)={dW1} det(W2)={dW2} det(Par)={dPar} det(ParW1W2)={dM} "
              f"-> {'PASS' if good else 'FAIL'}")
    print("ALL CHECKS PASS" if ok else "CHECK FAILURE")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
