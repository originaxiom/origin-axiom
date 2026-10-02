#!/usr/bin/env python3
"""B1520 -- the gauge lift in E8 (PREREGISTRATION section 2, Lemma G): two facts checked with own integer arithmetic.

E1. The longest element w0 of the Weyl group of E8 is -1 on the root lattice. Computed by walking a regular dominant vector
    (rho) to the antidominant chamber with simple reflections (120 = number of positive roots steps); the product is w0.
    Hence the Chevalley involution of e8 (-1 on a Cartan h, e_a -> -e_-a) is realised by an element of the adjoint group that
    normalises h (it is inner in any case, since E8's Dynkin diagram has no symmetries).
E2. A4 + A4 is a regular (maximal-rank) subsystem: removing the node of mark 5 from the extended Dynkin diagram leaves two A4
    chains. Checked on the Gram matrix of the eight roots {alpha0 = -theta, alpha8, alpha7, alpha6} and {alpha1, alpha3, alpha4,
    alpha2} (Bourbaki labels). The Chevalley involution of e8 relative to the shared Cartan restricts to the Chevalley
    involution of each sl5, X -> -X^T, i.e. g -> g^-T: duality on both SL(5) factors at once.
Usage: python3 lift_e8.py   (writes lift_e8.json)"""
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4)]     # Bourbaki numbering of E8


def cartan():
    C = [[2 if i == j else 0 for j in range(8)] for i in range(8)]
    for a, b in EDGES:
        C[a - 1][b - 1] = C[b - 1][a - 1] = -1
    return C


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def inverse(M):
    n = len(M)
    A = [[F(x) for x in row] + [F(1 if i == j else 0) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        piv = A[c][c]
        A[c] = [x / piv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def reflection(C, i):
    """s_i on simple-root coordinates: v -> v - <v, alpha_i^vee> alpha_i, <v, alpha_i^vee> = (C v)_i (simply laced)"""
    n = len(C)
    S = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
    for c in range(n):
        S[i][c] -= C[i][c]
    return S


def longest_element(C):
    n = len(C)
    Cinv = inverse(C)
    rho = [sum(Cinv[i][j] for j in range(n)) for i in range(n)]       # <rho, alpha_i^vee> = 1 for all i
    assert all(x.denominator == 1 for x in rho)
    rho = [int(x) for x in rho]
    W = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
    v = list(rho)
    steps = 0
    while True:
        pair = matvec(C, v)
        i = next((k for k in range(n) if pair[k] > 0), None)
        if i is None:
            break
        S = reflection(C, i)
        W = matmul(S, W)
        v = matvec(S, v)
        steps += 1
    return W, steps, rho


def highest_root():
    return [2, 3, 4, 6, 5, 4, 3, 2]          # theta in simple-root coordinates (Bourbaki, E8)


def main():
    C = cartan()
    W0, steps, rho = longest_element(C)
    minus_one = [[-1 if r == c else 0 for c in range(8)] for r in range(8)]
    theta = highest_root()
    # theta is a root of norm 2 and pairs to zero with every simple root but alpha8 (it is the highest root)
    norm_theta = sum(theta[i] * matvec(C, theta)[i] for i in range(8))
    pair_theta = matvec(C, theta)
    roots = {0: [-x for x in theta]}
    for k in range(1, 9):
        roots[k] = [1 if j == k - 1 else 0 for j in range(8)]
    def ip(a, b):
        return sum(a[i] * matvec(C, b)[i] for i in range(8))
    blocks = ([0, 8, 7, 6], [1, 3, 4, 2])
    gram = {str(b): [[ip(roots[x], roots[y]) for y in b] for x in b] for b in blocks}
    a4 = [[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]]
    cross = [[ip(roots[x], roots[y]) for y in blocks[1]] for x in blocks[0]]
    out = {"E1 steps (= number of positive roots)": steps, "E1 rho in simple-root coordinates": rho,
           "E1 w0 = -1": W0 == minus_one,
           "E2 theta norm": norm_theta, "E2 theta pairings": pair_theta,
           "E2 Gram matrices": gram, "E2 cross pairings": cross,
           "E2 both blocks A4, orthogonal": all(gram[str(b)] == a4 for b in blocks) and all(x == 0 for r in cross for x in r)}
    out["passed"] = (steps == 120 and out["E1 w0 = -1"] and norm_theta == 2 and pair_theta == [0, 0, 0, 0, 0, 0, 0, 1]
                     and out["E2 both blocks A4, orthogonal"])
    (HERE / "lift_e8.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
