#!/usr/bin/env python3
"""Minimum-support normalized toric trace for the height-308 evaluator.

R027 fixes a cyclic eight-triangle dual trace on the six-chart dP6 cover.
This certificate exhausts every smaller support, constructs a normalized
four-triangle trace, proves it homologous to R027's marked trace, and forms
its 96-simplex product trace on dP6 x dP6.  It changes no normalization; it
only makes the pending residue contraction four times smaller.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
R027 = runpy.run_path(str(
    ROOT / "certificates" / "r027_toric_top_trace" / "toric_top_trace.py"
))


def solve_affine(rows: list[list[Fraction]], variables: int) -> list[Fraction] | None:
    """Return one exact solution of an augmented system, or None."""

    matrix = [[Fraction(value) for value in row] for row in rows]
    pivot_row = 0
    pivots: list[int] = []
    for column in range(variables):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                left - scale * right
                for left, right in zip(matrix[row], matrix[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1

    if any(
        all(not value for value in row[:variables]) and row[-1]
        for row in matrix
    ):
        return None

    answer = [Fraction(0) for _ in range(variables)]
    for row, pivot in reversed(list(enumerate(pivots))):
        answer[pivot] = matrix[row][-1] - sum(
            matrix[row][column] * answer[column]
            for column in range(variables)
            if column != pivot
        )
    assert all(
        sum(row[column] * answer[column] for column in range(variables))
        == row[-1]
        for row in rows
    )
    return answer


def normalized_trace_on_support(support: tuple[int, ...]) -> list[Fraction] | None:
    d1 = R027["DIFFERENTIALS"][1]
    equations = [
        [d1[index][column] for index in support] + [Fraction(0)]
        for column in range(len(d1[0]))
    ]
    # TAU is one on every eligible triangle.
    equations.append([Fraction(1) for _ in support] + [Fraction(1)])
    return solve_affine(equations, len(support))


def minimum_trace() -> tuple[dict[tuple[int, ...], Fraction], tuple[int, ...]]:
    triangles = R027["BASES"][2]
    rejected_counts = []
    for size in range(1, len(triangles) + 1):
        rejected = 0
        for support in combinations(range(len(triangles)), size):
            solution = normalized_trace_on_support(support)
            if solution is None:
                rejected += 1
                continue
            values = {
                triangles[index]: value
                for index, value in zip(support, solution)
                if value
            }
            # Since all smaller supports were exhausted, the first solution
            # cannot hide a zero coefficient.
            assert len(values) == size
            assert size == 4
            assert tuple(rejected_counts) == (20, 190, 1140)
            return values, tuple(rejected_counts)
        rejected_counts.append(rejected)
    raise AssertionError("no normalized trace")


def product_trace(values: dict[tuple[int, ...], Fraction]) -> dict[tuple[int, ...], Fraction]:
    answer: dict[tuple[int, ...], Fraction] = {}
    for left, left_value in values.items():
        for right, right_value in values.items():
            for word in R027["shuffle_words"]():
                simplex = R027["product_simplex"](left, right, word)
                coefficient = left_value * right_value * R027["shuffle_sign"](word)
                answer[simplex] = answer.get(simplex, Fraction(0)) + coefficient
    return {simplex: value for simplex, value in answer.items() if value}


def assert_homologous(trace: list[Fraction]) -> list[Fraction]:
    difference = [
        left - right for left, right in zip(trace, R027["TRACE"])
    ]
    d2 = R027["DIFFERENTIALS"][2]
    # A dual degree-two boundary is in im(d_2^T).
    transpose = [list(row) for row in zip(*d2)]
    equations = [row + [target] for row, target in zip(transpose, difference)]
    witness = solve_affine(equations, len(transpose[0]))
    assert witness is not None
    reconstructed = [
        sum(transpose[row][column] * witness[column]
            for column in range(len(witness)))
        for row in range(len(transpose))
    ]
    assert reconstructed == difference
    return witness


def main() -> None:
    # Re-run the complete dependency before refining its representative.
    R027["assert_factor_complex"]()
    R027["assert_product_trace"]()

    values, rejected_counts = minimum_trace()
    expected = {
        (0, 1, 2): Fraction(1, 4),
        (0, 2, 3): Fraction(1, 4),
        (0, 3, 4): Fraction(1, 4),
        (0, 4, 5): Fraction(1, 4),
    }
    assert values == expected
    trace = R027["vector_for"](2, values)
    d1 = R027["DIFFERENTIALS"][1]
    assert all(
        R027["dot"](trace, R027["column"](d1, entry)) == 0
        for entry in range(len(d1[0]))
    )
    assert R027["dot"](trace, R027["TAU"]) == 1
    witness = assert_homologous(trace)

    product = product_trace(values)
    assert len(product) == 96
    assert not R027["boundary"](product)
    pairing = sum(
        coefficient * R027["alexander_whitney_top"](simplex)
        for simplex, coefficient in product.items()
    )
    assert pairing == 1

    planted = dict(values)
    planted.pop((0, 2, 3))
    planted_trace = R027["vector_for"](2, planted)
    assert (
        any(
            R027["dot"](planted_trace, R027["column"](d1, entry)) != 0
            for entry in range(len(d1[0]))
        )
        or R027["dot"](planted_trace, R027["TAU"]) != 1
    )

    print("DATA exhaustive rejected support counts for sizes 1,2,3 =", rejected_counts)
    print("RESULT minimum normalized dP6 trace support = 4")
    print("DATA sparse factor trace =", sorted(values.items()))
    print("RESULT sparse trace is an exact dual cycle and pairs with tau as 1")
    print("RESULT sparse trace differs from R027 cyclic trace by an exact dual boundary")
    print("DATA factor homology witness =", [
        (simplex, value)
        for simplex, value in zip(R027["BASES"][3], witness)
        if value
    ])
    print("RESULT sparse product trace support =", len(product))
    print("RESULT sparse product trace has zero boundary and pairs with tau x tau as 1")
    print("CONTROL deleting one sparse triangle breaks the cycle or normalization")
    print("SCOPE computation shrinks 384 trace simplices to 96; no Yukawa entry or rank is evaluated")


if __name__ == "__main__":
    main()
