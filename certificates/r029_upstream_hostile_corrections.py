#!/usr/bin/env python3
"""Exact hostile checks for the 2026-08-30 upstream Gate C/D claims.

Stdlib only.  The field is Q(w), w^2-w+1=0, where w is a primitive
sixth root.  No floating point or repository input is used.

The certificate checks two discriminating facts.

1.  The three commensurator-labelled Riley representations in B324 are
    related by explicit invertible intertwiners on ONE two-dimensional
    carrier.  Their character-variety orbit therefore has size one; after
    any functorial principal map the carrier is one 27, not 3 x 27.

2.  In the full-trace Fibonacci convention, I(E-lambda,E,2)=lambda^2+2.
    An object branch kappa=1+w therefore fixes lambda only up to sign.
    Moreover each finite polynomial approximant used by outside memo 156 is
    nonconstant.  By the fundamental theorem of algebra it has a zero, so
    {|x_n(E)|<2} contains an open neighbourhood.  Thus the finite mask has
    nonempty interior and planar box dimension 2, not the reported ~0.8.
    This does not decide the limiting non-self-adjoint spectrum.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("FAIL: " + message)


@dataclass(frozen=True)
class QW:
    """a+b*w in Q[w]/(w^2-w+1)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __init__(self, a=0, b=0):
        object.__setattr__(self, "a", Fraction(a))
        object.__setattr__(self, "b", Fraction(b))

    def __add__(self, other):
        other = q(other)
        return QW(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return QW(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-q(other))

    def __rsub__(self, other):
        return q(other) - self

    def __mul__(self, other):
        other = q(other)
        # w^2 = w-1
        return QW(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    __rmul__ = __mul__

    def __pow__(self, exponent: int):
        require(exponent >= 0, "negative QW exponent")
        answer, base = QW(1), self
        while exponent:
            if exponent & 1:
                answer = answer * base
            base = base * base
            exponent //= 2
        return answer

    def __str__(self):
        return f"({self.a})+({self.b})w"


def q(value) -> QW:
    return value if isinstance(value, QW) else QW(value)


ZERO, ONE, TWO = QW(0), QW(1), QW(2)
W = QW(0, 1)
U = W - 1  # primitive cube root, U^2+U+1=0

# Audit-target metadata for the finite masks.  These are the literal parameters
# externally checked in outside commit 941b60e0..., gate_d_numerics.py git blob
# c35cf7f3fad3c637d5c38019409ed08083e4faa0.  This self-contained certificate
# reconstructs the recurrence independently; it records but does not fetch or
# hash that upstream blob.  The limiting question is not identified with these
# three finite levels.
UPSTREAM_GATE_D_BLOB = "c35cf7f3fad3c637d5c38019409ed08083e4faa0"
UPSTREAM_MASK_LEVELS = (6, 8, 10)
UPSTREAM_WINDOW = (-6, 6, -6, 6)


def mmul(left, right):
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(2)), ZERO)
              for j in range(2))
        for i in range(2)
    )


ID = ((ONE, ZERO), (ZERO, ONE))


def mpow(matrix, exponent: int):
    require(exponent >= 0, "negative matrix exponent")
    answer, base = ID, matrix
    while exponent:
        if exponent & 1:
            answer = mmul(answer, base)
        base = mmul(base, base)
        exponent //= 2
    return answer


def minv2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    require(det == ONE, "matrix determinant is not one")
    return ((matrix[1][1], -matrix[0][1]),
            (-matrix[1][0], matrix[0][0]))


def trace(matrix):
    return matrix[0][0] + matrix[1][1]


def gate_c() -> None:
    g = ((ZERO, -ONE), (ONE, -ONE))
    a0 = ((ONE, ONE), (ZERO, ONE))
    b0 = ((ONE, ZERO), (U, ONE))
    require(mpow(g, 3) == ID and mpow(g, 1) != ID, "g has order three")

    aa, bb = [], []
    for i in range(3):
        gi = mpow(g, i)
        gii = mpow(g, (-i) % 3)
        aa.append(mmul(mmul(gi, a0), gii))
        bb.append(mmul(mmul(gi, b0), gii))

    # One exact intertwiner relates every adjacent pair on both generators.
    for i in range(3):
        j = (i + 1) % 3
        require(mmul(aa[j], g) == mmul(g, aa[i]), "a intertwiner")
        require(mmul(bb[j], g) == mmul(g, bb[i]), "b intertwiner")

    # Representative character coordinates agree exactly.  The intertwiner
    # identities above imply agreement for every group word, not only these.
    chars = []
    for i in range(3):
        chars.append((trace(aa[i]), trace(bb[i]),
                      trace(mmul(aa[i], minv2(bb[i])))))
    require(chars[0] == chars[1] == chars[2], "characters agree")

    # MB12: deleting conjugation from one labelled representative is detected.
    bad_b = ((bb[1][0][0] + ONE, bb[1][0][1]), bb[1][1])
    require(mmul(bad_b, g) != mmul(g, bb[0]), "planted non-intertwiner fires")

    print("GATE_C order_three_intertwiner PASS")
    print("GATE_C character_orbit_size=1 PASS")
    print("GATE_C actual_carrier_dimension=2 required_three_copy_dimension=6")
    print("GATE_C functorial_principal_carrier=27 required_three_copy_carrier=81")


def trim(poly):
    values = list(poly)
    while len(values) > 1 and values[-1] == ZERO:
        values.pop()
    return tuple(values)


def padd(left, right):
    n = max(len(left), len(right))
    return trim(tuple((left[i] if i < len(left) else ZERO) +
                      (right[i] if i < len(right) else ZERO)
                      for i in range(n)))


def pneg(poly):
    return tuple(-value for value in poly)


def psub(left, right):
    return padd(left, pneg(right))


def pmul(left, right):
    values = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            values[i + j] = values[i + j] + a * b
    return trim(values)


def pconst(value):
    return (q(value),)


def pdegree(poly):
    return len(trim(poly)) - 1


def peval(poly, value):
    answer = ZERO
    for coefficient in reversed(poly):
        answer = answer * value + coefficient
    return answer


def qwnorm2(value):
    """Complex |a+b*w|^2=a^2+ab+b^2 for w=exp(i*pi/3)."""
    return value.a * value.a + value.a * value.b + value.b * value.b


def in_sample_square(value):
    real = value.a + value.b / 2
    imag_squared = Fraction(3, 4) * value.b * value.b
    return -6 < real < 6 and imag_squared < 36


def invariant(x, y, z):
    return psub(
        padd(padd(pmul(x, x), pmul(y, y)), pmul(z, z)),
        padd(pmul(pmul(x, y), z), pconst(2)),
    )


def gate_d() -> None:
    require(UPSTREAM_MASK_LEVELS == (6, 8, 10), "upstream mask-level binding")
    require(UPSTREAM_WINDOW == (-6, 6, -6, 6), "upstream window binding")
    E = (ZERO, ONE)
    x, y, z = psub(E, pconst(W)), E, pconst(2)
    kappa_plus = ONE + W
    expected = pconst(kappa_plus)
    require(invariant(x, y, z) == expected, "I(E-w,E,2)=1+w")

    # The invariant fixes a square, not a preferred square root.
    require(W * W == kappa_plus - 2, "+w solves lambda^2=kappa-2")
    require((-W) * (-W) == kappa_plus - 2, "-w also solves")
    require(W != -W, "the two signs are distinct")

    # Conjugate object branch and its two roots.
    wbar = ONE - W
    kappa_minus = TWO - W
    require(wbar * wbar == kappa_minus - 2, "conjugate root")
    require((-wbar) * (-wbar) == kappa_minus - 2, "negative conjugate root")

    degrees = {}
    approximants = {}
    for n in range(1, 11):
        x, y, z = psub(pmul(x, y), z), x, y
        require(invariant(x, y, z) == expected, f"exact invariant at n={n}")
        if n in UPSTREAM_MASK_LEVELS:
            degrees[n] = pdegree(x)
            require(degrees[n] > 0, f"finite approximant n={n} nonconstant")
            approximants[n] = x

    # Exact dyadic Q(w) witnesses, located independently and then certified
    # without floating point.  Each lies strictly inside the upstream square
    # and strictly inside |x_n(E)|<2, so the sampled-window intersection itself
    # (not merely the global lemniscate) has nonempty interior.
    witnesses = {
        6: QW(Fraction(75, 128), Fraction(115, 256)),
        8: QW(Fraction(-227, 256), Fraction(55, 128)),
        10: QW(Fraction(-371, 256), Fraction(121, 256)),
    }
    for n in UPSTREAM_MASK_LEVELS:
        witness = witnesses[n]
        require(in_sample_square(witness), f"n={n} witness inside [-6,6]^2")
        require(qwnorm2(peval(approximants[n], witness)) < 4,
                f"n={n} exact witness satisfies |x_n|<2")

    # MB12: the theorem gate correctly rejects a constant detector polynomial.
    require(pdegree(pconst(7)) == 0, "constant-polynomial control")

    print("GATE_D exact_full_trace_identity=lambda^2+2 PASS")
    print("GATE_D allowed_lambda_on_chosen_branch={+w,-w} SIGN_NOT_SELECTED")
    print("GATE_D both_kappa_branches_allowed_lambda={+w,-w,+wbar,-wbar}")
    print("GATE_D externally_checked_upstream_blob=" + UPSTREAM_GATE_D_BLOB)
    print("GATE_D upstream_levels=(6,8,10) upstream_window=[-6,6]^2")
    print("GATE_D finite_approximant_degrees", degrees)
    print("GATE_D exact_in_window_interior_witnesses=(6,8,10) PASS")
    print("GATE_D finite_sigma_has_nonempty_interior_by_FTA_and_continuity")
    print("GATE_D finite_sigma_planar_box_dimension=2")
    print("GATE_D reported_sub2_dimension_is_UNDER_RESOLUTION_NOT_A_THEOREM")


def main() -> None:
    require(W * W - W + ONE == ZERO, "field relation")
    require(U * U + U + ONE == ZERO, "cube-root relation")
    gate_c()
    gate_d()
    print("VERDICT GATE_C_ROUTE_REFUTED; GATE_D_EXACT_CORE_NARROWED; LIMIT_OPEN")


if __name__ == "__main__":
    main()
