"""B14 — the half-step square root, verified exactly (added 2026-09-17, B1424/S17).

B14 was banked PROVED in the repository's first week and carried NO script and NO test lock. It was
the one record of the paper's ninety-five without a primary lock, and it is the arithmetic under the
paper's MOST EXPENSIVE axiom: the squaring that buys orientation and, by the paper's own §chirality,
costs the chirality bit. An outside referee found the asymmetry in one query on the manifest.

Four checks, each able to fail:

  (1) F = LP is an integer square root of A = LR = [[2,1],[1,1]], and it is orientation-REVERSING.
  (2) It is the ONLY one up to sign, proved rather than searched: for X in GL(2,Z) with X^2 = A,
      Cayley-Hamilton gives X^2 = tr(X) X - det(X) I.
        * det X = +1 forces tr(X) X = A + I = [[3,1],[1,2]], whose determinant is 5, so
          det X = tr(X)^2 * 1 = 5 -- impossible for an integer trace with det +1.
        * det X = -1 forces tr(X) X = A - I = [[1,1],[1,0]] = F, with det(A - I) = -1 = tr(X)^2 * (-1),
          so tr(X) = +-1 and X = +-F.
      A brute-force enumeration over a box is run as an INDEPENDENT control on the same statement.
  (3) B(a,b) = L_a R_b = [[1+ab, a],[b, 1]] has an orientation-reversing integer square root IFF a = b:
      X = (B - I)/t with t = tr(X), det X = -ab/t^2 = -1 so t^2 = ab, and integrality forces t | a and
      t | b; writing a = t a', b = t b' gives a' b' = 1, hence a = b. Conversely (L_k P)^2 = B(k,k).
  (4) CONTROLS so the criterion can fail: a != b cases are checked to have NO such root, over a grid,
      by enumeration; and A itself is confirmed to have no orientation-PRESERVING square root at all.

Run: python3 square_root.py        (pure Python, no dependencies)
"""

L = ((1, 1), (0, 1))
R = ((1, 0), (1, 1))
P = ((0, 1), (1, 0))          # the record swap


def mul(X, Y):
    return ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]),
            (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))


def det(X):
    return X[0][0] * X[1][1] - X[0][1] * X[1][0]


def tr(X):
    return X[0][0] + X[1][1]


def neg(X):
    return tuple(tuple(-v for v in row) for row in X)


def B(a, b):
    return ((1 + a * b, a), (b, 1))


def square_roots_by_search(T, box):
    """every integer X with |entries| <= box and X^2 == T -- the independent control on the proof"""
    out = []
    for x00 in range(-box, box + 1):
        for x01 in range(-box, box + 1):
            for x10 in range(-box, box + 1):
                for x11 in range(-box, box + 1):
                    X = ((x00, x01), (x10, x11))
                    if abs(det(X)) == 1 and mul(X, X) == T:
                        out.append(X)
    return sorted(out)


def has_orientation_reversing_root(a, b, box=12):
    return any(det(X) == -1 for X in square_roots_by_search(B(a, b), box))


if __name__ == "__main__":
    A = mul(L, R)
    F = mul(L, P)
    print("A  = LR =", A, " det", det(A))
    print("F  = LP =", F, " det", det(F), " tr", tr(F))
    print("(1) F^2 == A :", mul(F, F) == A, " and F is orientation-reversing :", det(F) == -1)

    roots = square_roots_by_search(A, 6)
    print("(2) integer square roots of A with |entries| <= 6 :", roots)
    print("    they are exactly {F, -F} :", roots == sorted([F, neg(F)]))
    print("    none is orientation-preserving :", all(det(X) == -1 for X in roots))

    eq = [(k, has_orientation_reversing_root(k, k)) for k in range(1, 5)]
    ne = [((a, b), has_orientation_reversing_root(a, b))
          for a in range(1, 5) for b in range(1, 5) if a != b]
    print("(3) a == b has an orientation-reversing root :", eq)
    print("    and (L_k P)^2 == B(k,k) :",
          all(mul(mul(((1, k), (0, 1)), P), mul(((1, k), (0, 1)), P)) == B(k, k) for k in range(1, 5)))
    print("(4) CONTROL a != b has none :", all(not v for _, v in ne), " over", len(ne), "pairs")
    print("    CONTROL A has no orientation-preserving square root :",
          not any(det(X) == 1 for X in square_roots_by_search(A, 6)))
    ok = (mul(F, F) == A and det(F) == -1 and roots == sorted([F, neg(F)])
          and all(v for _, v in eq) and all(not v for _, v in ne))
    print("B14 VERIFIED:", ok)
