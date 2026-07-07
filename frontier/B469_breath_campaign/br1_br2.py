#!/usr/bin/env python3
"""B469 BR1 + BR2 — the two-register breath law and the family Gieseking theorem.

BR1: at levels N in {15, 45, 75, 225}: (a) quantum det(Par@N) — the negation
permutation matrix determinant = its permutation sign = (-1)^{#transpositions}
= (-1)^{(N-1)/2} for odd N; computed exactly as a permutation sign; (b) the
classical sign of sigma_ab = [[1,1],[1,0]] acting on (Z/N)^2 — the prereg's
prediction: both equal (-1)^((N-1)/2), the level's class mod 4, at every level.

BR2: X_m = [[m,1],[1,0]] squares to A_m = [[m^2+1, m],[m,1]] with det = -1,
for ALL m symbolically — every metallic bundle orientation-double-covers a
non-orientable punctured-torus bundle (m=1: the Gieseking manifold).
"""
import sys
from itertools import product

import sympy as sp


def perm_sign_of_map(f, domain):
    idx = {x: i for i, x in enumerate(domain)}
    seen = [False] * len(domain)
    sign = 1
    for i, x in enumerate(domain):
        if seen[i]:
            continue
        length = 0
        j = i
        while not seen[j]:
            seen[j] = True
            j = idx[f(domain[j])]
            length += 1
        if length % 2 == 0:
            sign = -sign
    return sign


def br1():
    print("== BR1: the two-register breath law ==")
    ok = True
    for N in (15, 45, 75, 225):
        pred = (-1) ** ((N - 1) // 2)
        # quantum register: det(Par@N) = sign of the negation permutation on Z/N
        par_sign = perm_sign_of_map(lambda j: (-j) % N, list(range(N)))
        # classical register: sign of sigma on (Z/N)^2 (sample-free exact walk)
        dom = list(product(range(N), repeat=2))
        sig_sign = perm_sign_of_map(lambda v: ((v[0] + v[1]) % N, v[0]), dom)
        hit = par_sign == pred == sig_sign
        ok &= hit
        print(f"  N={N:4d} (N mod 4 = {N % 4}): det(Par) = {par_sign:+d}, "
              f"sign(sigma on (Z/N)^2) = {sig_sign:+d}, "
              f"prediction (-1)^((N-1)/2) = {pred:+d}  -> {'PASS' if hit else 'FAIL'}")
    print(f"  BR1: the two registers breathe together at every level: {'YES' if ok else 'NO'}")
    return ok


def br2():
    print("\n== BR2: the family Gieseking theorem (symbolic, all m) ==")
    m = sp.Symbol('m', integer=True)
    X = sp.Matrix([[m, 1], [1, 0]])
    A = sp.Matrix([[m * m + 1, m], [m, 1]])
    sq_ok = sp.simplify(X * X - A) == sp.zeros(2, 2)
    det_ok = sp.simplify(X.det()) == -1
    print(f"  X_m^2 = A_m symbolically: {sq_ok};  det X_m = -1: {det_ok}")
    print("  => EVERY metallic bundle (monodromy A_m) is the orientation double cover")
    print("     of the non-orientable bundle with monodromy X_m (m=1: the Gieseking manifold).")
    print("     Lit-gate recorded: Gieseking-type quotients are standard-shaped; cited not claimed.")
    return bool(sq_ok and det_ok)


if __name__ == '__main__':
    ok = br1() and br2()
    print("\nALL CHECKS PASS" if ok else "\nCHECK FAILURE")
    sys.exit(0 if ok else 1)
