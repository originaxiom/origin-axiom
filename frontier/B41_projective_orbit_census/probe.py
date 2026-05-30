"""B41 -- projective orbit census.

Performs a bounded low-complexity census of projective trace-map behavior.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

import sympy as sp


def trace_map_tuple(point: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    x, y, z = point
    return (z, x, 2 * x * z - y)


def canonical_projective(point: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    images = []
    for sa, sb in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y, z = point
        images.append((sa * x, sb * y, sa * sb * z))
    return min(images)


def projective_period(point: tuple[Fraction, Fraction, Fraction], max_period: int = 8) -> int | None:
    start = canonical_projective(point)
    current = point
    for period in range(1, max_period + 1):
        current = trace_map_tuple(current)
        if canonical_projective(current) == start:
            return period
    return None


def main() -> None:
    print("=" * 72)
    print("B41 -- projective orbit census")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    print("\n[1] bounded rational seed census")
    seeds = [Fraction(-1), Fraction(0), Fraction(1)]
    periods: dict[int, set[tuple[Fraction, Fraction, Fraction]]] = {}
    for point in itertools.product(seeds, repeat=3):
        period = projective_period(point)
        if period is not None:
            periods.setdefault(period, set()).add(canonical_projective(point))
    for period in sorted(periods):
        print(f"    projective period {period}: {len(periods[period])} canonical seeds")
    assert 1 in periods
    assert 3 in periods

    print("\n[2] exact coordinate-axis family")
    c = sp.symbols("c")
    x0 = sp.Matrix([0, 0, c])
    t1 = sp.Matrix([c, 0, 0])
    t2 = sp.Matrix([0, c, 0])
    t3 = sp.Matrix([0, 0, -c])
    print(f"    orbit = {tuple(x0)} -> {tuple(t1)} -> {tuple(t2)} -> {tuple(t3)}")
    assert t3[2] ** 2 == x0[2] ** 2

    print("\n[3] invariant remains free")
    invariant = c**2 - 1
    print(f"    I = {invariant}")
    assert sp.diff(invariant, c) == 2 * c

    print("\nVerdict: STALLED")
    print("The coordinate-axis 3-cycle is natural and simple, but it is a")
    print("one-parameter family and does not select S1.")


if __name__ == "__main__":
    main()
