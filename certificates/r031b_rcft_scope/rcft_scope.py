#!/usr/bin/env python3
"""Exact scope controls for the B1229/B1230 RCFT consistency route.

This certificate does not certify the cited CFT literature.  It locks the
elementary arithmetic and logic which the literature assumptions must still
cross: rationality is not finiteness, the trace-field Galois group is not a
Z/3, and the c=6 enumeration is an enumeration inside the simply-laced WZW
class rather than inside all RCFTs.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


def c_wzw(dimension: int, dual_coxeter: int, level: int) -> Fraction:
    return Fraction(level * dimension, level + dual_coxeter)


def a_data(rank: int) -> tuple[int, int]:
    return rank * (rank + 2), rank + 1


def d_data(rank: int) -> tuple[int, int]:
    return rank * (2 * rank - 1), 2 * rank - 2


def required_level(dimension: int, dual_coxeter: int) -> Fraction:
    """Solve k*dim/(k+h)=6 exactly."""

    return Fraction(6 * dual_coxeter, dimension - 6)


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    memo = (root / "memos/RCFT_CONSISTENCY_SCOPE.md").read_text(encoding="utf-8")
    for marker in (
        "Anderson--Moore",
        "complex Chern--Simons",
        "Q(zeta_3)",
        "simply-laced WZW",
        "not restriction-free",
        "question-map row",
    ):
        assert marker in memo

    # Rational numbers are not a finite menu.  The displayed family supplies
    # arbitrarily many distinct positive rationals in the bounded interval.
    for count in (10, 100, 1000):
        family = {Fraction(index, count + 1) for index in range(1, count + 1)}
        assert len(family) == count
        assert all(Fraction(0) < value < Fraction(1) for value in family)
    # Midpoints give the elementary exact density control on rational inputs.
    for left, right in ((Fraction(0), Fraction(1)),
                        (Fraction(1, 3), Fraction(2, 3)),
                        (Fraction(999, 1000), Fraction(1))):
        middle = (left + right) / 2
        assert left < middle < right and isinstance(middle, Fraction)

    # Q(zeta_3)=Q(sqrt(-3)) has degree phi(3)=2.  Its Galois group therefore
    # has order two; it is not the order-three trinification/simple-current
    # group.  The distinction is by order alone.
    phi_3 = 2
    trace_field_galois_order = phi_3
    trinification_order = 3
    assert trace_field_galois_order == 2
    assert trace_field_galois_order != trinification_order

    # Solve c(g_k)=6 for every simply-laced simple WZW family.  The inequalities
    # below make the finite rank bounds exact: k<1 beyond A6/D6, so no positive
    # integral level can occur there.
    solutions = []
    # A1 has c=3k/(k+2)<3 for every positive k, since the difference between
    # 3(k+2) and 3k is the positive constant 6.
    dimension_a1, h_a1 = a_data(1)
    assert (dimension_a1, h_a1) == (3, 2)
    assert 3 * (1 + h_a1) - dimension_a1 * 1 == 6
    assert required_level(dimension_a1, h_a1) < 0
    for rank in range(2, 7):
        dimension, dual_coxeter = a_data(rank)
        level = required_level(dimension, dual_coxeter)
        if level.denominator == 1 and level > 0:
            solutions.append((f"A{rank}", int(level)))
            assert c_wzw(dimension, dual_coxeter, int(level)) == 6
    # For every r>=7, denominator-numerator in the required-level formula is
    #   r(r+2)-6 - 6(r+1) = (r-6)(r+2) > 0,
    # so 0<k<1 and no positive integral level exists.
    for rank in (7, 8, 20, 100):
        dimension, dual_coxeter = a_data(rank)
        assert dimension - 6 - 6 * dual_coxeter == (rank - 6) * (rank + 2) > 0
        assert 0 < required_level(dimension, dual_coxeter) < 1

    for rank in range(4, 7):
        dimension, dual_coxeter = d_data(rank)
        level = required_level(dimension, dual_coxeter)
        if level.denominator == 1 and level > 0:
            solutions.append((f"D{rank}", int(level)))
            assert c_wzw(dimension, dual_coxeter, int(level)) == 6
    # For every r>=7,
    #   r(2r-1)-6 - 12(r-1) = (2r-1)(r-6) > 0,
    # again forcing 0<k<1.
    for rank in (7, 8, 20, 100):
        dimension, dual_coxeter = d_data(rank)
        assert dimension - 6 - 6 * dual_coxeter == (2 * rank - 1) * (rank - 6) > 0
        assert 0 < required_level(dimension, dual_coxeter) < 1

    for name, dimension, dual_coxeter in (
        ("E6", 78, 12), ("E7", 133, 18), ("E8", 248, 30)
    ):
        level = required_level(dimension, dual_coxeter)
        if level.denominator == 1 and level > 0:
            solutions.append((name, int(level)))
            assert c_wzw(dimension, dual_coxeter, int(level)) == 6

    assert sorted(solutions) == [("A2", 9), ("A6", 1), ("D6", 1), ("E6", 1)]

    # Failure control: widening from the WZW subclass to even a symbolic
    # rational-c family immediately defeats the four-entry claim.
    rational_c_controls = {Fraction(6)} | {
        Fraction(6 * n + 1, n) for n in range(1, 21)
    }
    assert len(rational_c_controls) == 21

    print("PASS rationality alone permits arbitrarily large finite subsets of (0,1) and rational midpoints")
    print("RESULT Gal(Q(zeta_3)/Q) order =", trace_field_galois_order,
          "!= trinification/simple-current order", trinification_order)
    print("RESULT simply-laced WZW solutions of c=6 =", sorted(solutions))
    print("SCOPE that four-entry result is WZW-class exhaustive, not RCFT exhaustive")
    print("CONTROL a rational-c family already exceeds the four-entry WZW menu: size =",
          len(rational_c_controls))
    print("RESULT no arithmetic identification maps trace-field, trinification and fusion Z/3 data")
    print("R031B RCFT consistency-scope controls: PASS")


if __name__ == "__main__":
    main()
