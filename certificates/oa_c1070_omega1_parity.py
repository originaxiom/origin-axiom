#!/usr/bin/env python3
"""OA-C1070 / outside campaign A5: the omega_1 parity clause.

This is a small, dependency-free check of the locked C-P1 result.  It does
not re-enumerate nilpotent orbits (that is the scope of the locked
cp1_strata.py certificate); it records every one of its 20 accepted rows and
recomputes the 27 weights, H=A^{-1}c, and projectivity test from the lattice
formula.  The final assertions separate the positive 20-row result from the
general lattice implication.
"""
from fractions import Fraction as F
from itertools import product


# The simple-root order is the order printed by cp1_strata.py.
A = (
    (2, 0, -1, 0, 0, 0),
    (0, 2, 0, -1, 0, 0),
    (-1, 0, 2, -1, 0, 0),
    (0, -1, -1, 2, -1, 0),
    (0, 0, 0, -1, 2, -1),
    (0, 0, 0, 0, -1, 2),
)


def inverse(M):
    n = len(M)
    z = [[F(M[i][j]) for j in range(n)] + [F(i == j) for j in range(n)]
         for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if z[i][col])
        z[col], z[pivot] = z[pivot], z[col]
        q = z[col][col]
        z[col] = [x / q for x in z[col]]
        for i in range(n):
            if i != col and z[i][col]:
                q = z[i][col]
                z[i] = [x - q * y for x, y in zip(z[i], z[col])]
    return tuple(tuple(row[n:]) for row in z)


Ainv = inverse(A)

# Exact accepted census printed by the locked source.  Fields are
# (weighted-Dynkin labels, orbit dimension, Levi/distinguished, projective).
ROWS = (
    ((0, 0, 0, 1, 0, 0), 40, "LEVI-REGULAR", False),
    ((0, 0, 0, 2, 0, 0), 58, "DISTINGUISHED", True),
    ((0, 0, 1, 0, 1, 0), 50, "LEVI-REGULAR", False),
    ((0, 1, 0, 0, 0, 0), 22, "LEVI-REGULAR", False),
    ((0, 1, 1, 0, 1, 0), 56, "LEVI-REGULAR", False),
    ((0, 2, 0, 0, 0, 0), 42, "LEVI-REGULAR", True),
    ((0, 2, 0, 2, 0, 0), 60, "LEVI-REGULAR", True),
    ((1, 0, 0, 0, 0, 1), 32, "LEVI-REGULAR", False),
    ((1, 0, 0, 1, 0, 1), 54, "LEVI-REGULAR", False),
    ((1, 1, 0, 0, 0, 1), 46, "LEVI-REGULAR", False),
    ((1, 1, 1, 0, 1, 1), 62, "LEVI-REGULAR", False),
    ((1, 2, 0, 0, 0, 1), 52, "LEVI-REGULAR", False),
    ((1, 2, 1, 0, 1, 1), 64, "DISTINGUISHED", False),
    ((2, 0, 0, 0, 0, 2), 48, "LEVI-REGULAR", True),
    ((2, 0, 0, 2, 0, 2), 66, "DISTINGUISHED", True),
    ((2, 1, 1, 0, 1, 2), 64, "LEVI-REGULAR", False),
    ((2, 2, 0, 0, 0, 2), 60, "LEVI-REGULAR", True),
    ((2, 2, 0, 2, 0, 2), 68, "LEVI-REGULAR", True),
    ((2, 2, 2, 0, 2, 2), 70, "DISTINGUISHED", True),
    ((2, 2, 2, 2, 2, 2), 72, "LEVI-REGULAR", True),
)


def pair(weight, j):
    """<weight, alpha_j^vee>, for a weight in simple-root coordinates."""
    return sum(weight[i] * A[i][j] for i in range(6))


# This is the same formula used by twisted_double.py: start at omega_1 and
# walk lambda -> lambda-alpha_j whenever <lambda,alpha_j^vee>=1.
omega1 = tuple(Ainv[i][0] for i in range(6))
weights = [omega1]
seen = {omega1}
todo = [omega1]
while todo:
    lam = todo.pop()
    for j in range(6):
        if pair(lam, j) == 1:
            nxt = tuple(x - (i == j) for i, x in enumerate(lam))
            if nxt not in seen:
                seen.add(nxt)
                weights.append(nxt)
                todo.append(nxt)
assert len(weights) == 27


def h_coefficients(c):
    # H_c=sum_j t_j alpha_j^vee, with A*t=c.
    return tuple(sum(Ainv[i][j] * c[j] for j in range(6)) for i in range(6))


def spectrum(c):
    t = h_coefficients(c)
    # lambda(H_c)=sum_j t_j <lambda,alpha_j^vee>.
    return tuple(sum(pair(lam, j) * t[j] for j in range(6)) for lam in weights)


def main():
    assert len(ROWS) == 20 and len({row[0] for row in ROWS}) == 20
    assert all(all(x in (0, 1, 2) for x in c) for c, *_ in ROWS)
    print("accepted rows: 20 (copied exactly from locked C-P1 output)")
    print("c | dim O | type | t=A^-1 c | omega_1 parity | projective")
    for c, dim, typ, expected_projective in ROWS:
        t = h_coefficients(c)
        vals = spectrum(c)
        # Accepted weighted-Dynkin characteristics are cocharacters, hence
        # integral in the simple-coroot basis.  Check that input fact here;
        # it is the hypothesis needed by the general lattice proof below.
        assert all(x.denominator == 1 for x in t)
        actual = all(x.denominator == 1 and x.numerator % 2 == 0 for x in vals)
        assert actual == expected_projective
        print(c, "|", dim, "|", typ, "|", tuple(int(x) for x in t),
              "|", "even" if actual else "odd", "|", actual)

    projective = sum(expected for _, _, _, expected in ROWS)
    assert projective == 9
    assert all(all(x % 2 == 0 for x in c) for c, _, _, p in ROWS if p)
    assert sum(all(x % 2 == 0 for x in c) for c, *_ in ROWS) == 9
    print("projective rows: 9/20; every projective row has all labels even")

    # General implication in the integral coroot lattice.  det(A)=3, so A is
    # nonsingular mod 2.  Thus A*t even and integral t imply t even, and then
    # every integral weight (in particular every omega_1 weight) evaluates
    # evenly on H.  Check this over all integral c=2d for which A^-1 c is
    # integral; this is broader than the nilpotent 20-row census.
    det = 3
    assert det % 2 == 1
    integral_even = []
    for d in product((0, 1), repeat=6):
        c = tuple(2 * x for x in d)
        t = h_coefficients(c)
        if all(x.denominator == 1 for x in t):
            integral_even.append((c, t))
            assert all(x.numerator % 2 == 0 for x in t)
            assert all(x.numerator % 2 == 0 for x in spectrum(c))
    assert len(integral_even) == 24  # includes c=0; not an orbit census
    print("integral even-label test: 24/64 label vectors pass; all give even t and 27-spectrum")

    # The inverse-Cartan denominators matter if the lattice hypothesis is
    # dropped.  c=(2,0,0,0,0,0) has even labels but t_1=8/3, so it is not an
    # integral weighted-Dynkin characteristic and is outside the theorem.
    bad = (2, 0, 0, 0, 0, 0)
    assert h_coefficients(bad)[0] == F(8, 3)
    assert spectrum(bad)[0] == F(8, 3)  # highest weight omega_1
    print("scope fence: c=(2,0,0,0,0,0) is even but t_1=8/3; arbitrary even labels are not enough")
    print("OA-C1070: PASS — among weighted-Dynkin characteristics, omega_1 parity is redundant")


if __name__ == "__main__":
    main()
