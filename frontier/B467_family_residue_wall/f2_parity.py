#!/usr/bin/env python3
"""B467 F2 — the parity residue, determinate version (exact).

Signs of the classical actions as permutations of the discrete phase-space torus
(Z/15)^2. The parity of a permutation is exact; for linear maps on finite tori it is
classical arithmetic (Jacobi-symbol-shaped) — the adjudication is derivability.
Chat-1's per-point sum over the 240 dual-torus points requires their unshared loop
construction — recorded as awaiting-construction in the FINDINGS.
"""
import sys
from itertools import product

N = 15


def perm_sign_of_map(f, domain):
    idx = {x: i for i, x in enumerate(domain)}
    seen = [False] * len(domain)
    sign = 1
    for i, x in enumerate(domain):
        if seen[i]:
            continue
        # walk the cycle
        length = 0
        j = i
        while not seen[j]:
            seen[j] = True
            j = idx[f(domain[j])]
            length += 1
        if length % 2 == 0:
            sign = -sign
    return sign


def linmap(M):
    return lambda v: ((M[0][0] * v[0] + M[0][1] * v[1]) % N,
                      (M[1][0] * v[0] + M[1][1] * v[1]) % N)


def mm(A, B):
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % N, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % N],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % N, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % N]]


def main():
    dom = list(product(range(N), repeat=2))
    A1 = [[2, 1], [1, 1]]
    A2 = [[5, 2], [2, 1]]
    SIG = [[1, 1], [1, 0]]            # sigma_ab, det -1
    NEG = [[N - 1, 0], [0, N - 1]]    # -I
    table = {
        'A1 (golden monodromy)': A1,
        'A2 (silver)': A2,
        'A1*A2 (the two-generator word)': mm(A1, A2),
        '-I (Par)': NEG,
        '-A1*A2 (the B465 shadow)': mm(NEG, mm(A1, A2)),
        'sigma [[1,1],[1,0]] (Gieseking half-monodromy)': SIG,
    }
    print("== exact permutation signs on (Z/15)^2 ==")
    signs = {}
    for name, M in table.items():
        s = perm_sign_of_map(linmap(M), dom)
        signs[name] = s
        print(f"  sign({name}) = {s:+d}")
    print("\n== the Galois scalings x -> c x ==")
    for c in [1, 2, 4, 7, 8, 11, 13, 14]:
        s = perm_sign_of_map(lambda v, c=c: ((c * v[0]) % N, (c * v[1]) % N), dom)
        print(f"  sign(x -> {c:2d}x) = {s:+d}")
    # every SL(2,Z/15) element: sign should be constant on the group if the sign
    # character is trivial on SL2; the table tests it on our generators
    print("\nresidue verdict inputs:", signs)
    sys.exit(0)


if __name__ == '__main__':
    main()
