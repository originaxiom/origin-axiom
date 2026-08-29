#!/usr/bin/env python3
"""Exact chart/frame transport for the height-308 toric evaluator.

The existing Sage unit-ideal calculation stores four-variable polynomials in
the affine coordinates determined by ``tuple(sorted(cone))``.  Those raw
polynomials are not common Laurent functions: every line-bundle section also
carries a chart monomial q_(D,sigma), and the ordered ray matrix contributes a
local orientation.  This dependency-free certificate pins those data on all
36 charts of dP6 x dP6.

It does not serialize Phi_308, construct characteristic-zero Bezout
coefficients, or evaluate a residue.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Vector = tuple[int, ...]
RationalVector = tuple[Fraction, ...]
Matrix = tuple[tuple[int, ...], ...]
RationalMatrix = tuple[tuple[Fraction, ...], ...]

UNIT_HEXAGON = (
    (1, 0),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (0, -1),
    (1, -1),
)
DUAL_HEXAGON = (
    (-1, -1),
    (-1, 0),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1),
)
FAN_RAYS = tuple(ray + (0, 0) for ray in UNIT_HEXAGON) + tuple(
    (0, 0) + ray for ray in UNIT_HEXAGON
)
POLYTOPE_POINTS = tuple(left + right for left, right in product(DUAL_HEXAGON, repeat=2))

ZETA_N: Matrix = (
    (0, 0, 0, -1),
    (0, 0, 1, 1),
    (1, 0, 0, 0),
    (0, 1, 0, 0),
)
EXPECTED_A_M: Matrix = (
    (0, 0, 1, -1),
    (0, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 0),
)
EXPECTED_RAY_PERMUTATION = (6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 0)


def dot(left: Vector | RationalVector, right: Vector | RationalVector) -> Fraction:
    return sum((Fraction(a) * Fraction(b) for a, b in zip(left, right)), Fraction(0))


def matvec(matrix: Matrix | RationalMatrix, vector: Vector | RationalVector) -> RationalVector:
    return tuple(dot(row, vector) for row in matrix)


def matmul(
    left: Matrix | RationalMatrix,
    right: Matrix | RationalMatrix,
) -> RationalMatrix:
    right_columns = tuple(zip(*right))
    return tuple(tuple(dot(row, column) for column in right_columns) for row in left)


def identity(size: int) -> RationalMatrix:
    return tuple(tuple(Fraction(row == column) for column in range(size)) for row in range(size))


def inverse(matrix: Matrix | RationalMatrix) -> RationalMatrix:
    size = len(matrix)
    rows = [
        [Fraction(value) for value in row]
        + [Fraction(row_index == column) for column in range(size)]
        for row_index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if rows[row][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = rows[column][column]
        rows[column] = [value / scale for value in rows[column]]
        for row in range(size):
            if row == column or not rows[row][column]:
                continue
            scale = rows[row][column]
            rows[row] = [left - scale * right for left, right in zip(rows[row], rows[column])]
    return tuple(tuple(row[size:]) for row in rows)


def determinant(matrix: Matrix | RationalMatrix) -> Fraction:
    rows = [[Fraction(value) for value in row] for row in matrix]
    result = Fraction(1)
    for column in range(len(rows)):
        pivot = next((row for row in range(column, len(rows)) if rows[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            result = -result
        pivot_value = rows[column][column]
        result *= pivot_value
        for row in range(column + 1, len(rows)):
            if not rows[row][column]:
                continue
            scale = rows[row][column] / pivot_value
            rows[row] = [left - scale * right for left, right in zip(rows[row], rows[column])]
    return result


def transpose(matrix: Matrix | RationalMatrix) -> RationalMatrix:
    return tuple(tuple(Fraction(value) for value in row) for row in zip(*matrix))


def integral(matrix: RationalMatrix) -> Matrix:
    assert all(value.denominator == 1 for row in matrix for value in row)
    return tuple(tuple(value.numerator for value in row) for row in matrix)


def add(left: Vector | RationalVector, right: Vector | RationalVector) -> RationalVector:
    return tuple(Fraction(a) + Fraction(b) for a, b in zip(left, right))


def scale_sum(coefficients: tuple[int, ...], vectors: RationalMatrix) -> RationalVector:
    answer = tuple(Fraction(0) for _ in range(4))
    for coefficient, vector in zip(coefficients, vectors):
        answer = add(answer, tuple(Fraction(coefficient) * value for value in vector))
    return answer


def chart_ray_ids(left_start: int, right_start: int) -> tuple[int, ...]:
    cone = (
        left_start,
        (left_start + 1) % 6,
        6 + right_start,
        6 + ((right_start + 1) % 6),
    )
    # This exactly reproduces ``tuple(sorted(cone))`` in the Sage file, where
    # cone contains ray vectors rather than their global integer labels.
    return tuple(sorted(cone, key=lambda ray: FAN_RAYS[ray]))


def ray_matrix(ray_ids: tuple[int, ...]) -> Matrix:
    return tuple(tuple(FAN_RAYS[ray][coordinate] for ray in ray_ids) for coordinate in range(4))


def chart_data(left_start: int, right_start: int) -> tuple[tuple[int, ...], Matrix, Matrix, int]:
    ray_ids = chart_ray_ids(left_start, right_start)
    matrix = ray_matrix(ray_ids)
    dual = integral(inverse(matrix))
    sign = int(determinant(matrix))
    assert sign in (-1, 1)
    return ray_ids, matrix, dual, sign


def ray_image(ray: Vector) -> Vector:
    image = matvec(ZETA_N, ray)
    assert all(value.denominator == 1 for value in image)
    return tuple(value.numerator for value in image)


def chart_action(chart: tuple[int, int]) -> tuple[int, int]:
    image_rays = {EXPECTED_RAY_PERMUTATION[ray] for ray in chart_ray_ids(*chart)}
    matches = [
        candidate
        for candidate in product(range(6), repeat=2)
        if set(chart_ray_ids(*candidate)) == image_rays
    ]
    assert len(matches) == 1
    return matches[0]


def orbit(seed: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    answer = []
    cursor = seed
    while cursor not in answer:
        answer.append(cursor)
        cursor = chart_action(cursor)
    assert cursor == seed
    return tuple(answer)


def q_exponent(dual: Matrix, ray_ids: tuple[int, ...], omitted_ray: int | None = None) -> RationalVector:
    coefficients = tuple(0 if ray == omitted_ray else 1 for ray in ray_ids)
    return scale_sum(coefficients, tuple(tuple(Fraction(value) for value in row) for row in dual))


def raw_exponents(point: Vector, ray_ids: tuple[int, ...], omitted_ray: int | None = None) -> tuple[int, ...]:
    answer = []
    for ray in ray_ids:
        exponent = int(dot(point, FAN_RAYS[ray])) + 1 - int(ray == omitted_ray)
        assert exponent >= 0
        answer.append(exponent)
    return tuple(answer)


def assert_lattice_action() -> tuple[Matrix, tuple[int, ...]]:
    zeta_inverse = inverse(ZETA_N)
    a_m = integral(transpose(zeta_inverse))
    assert a_m == EXPECTED_A_M
    assert matmul(ZETA_N, matmul(ZETA_N, matmul(ZETA_N, ZETA_N))) != identity(4)
    zeta_power = identity(4)
    for _ in range(12):
        zeta_power = matmul(zeta_power, ZETA_N)
    assert zeta_power == identity(4)

    ray_index = {ray: index for index, ray in enumerate(FAN_RAYS)}
    permutation = tuple(ray_index[ray_image(ray)] for ray in FAN_RAYS)
    assert permutation == EXPECTED_RAY_PERMUTATION

    for point in POLYTOPE_POINTS:
        for ray in FAN_RAYS:
            # A_M is the contragredient monomial action.
            assert dot(matvec(a_m, point), matvec(ZETA_N, ray)) == dot(point, ray)
    planted_failure = any(
        dot(matvec(ZETA_N, point), matvec(ZETA_N, ray)) != dot(point, ray)
        for point in POLYTOPE_POINTS
        for ray in FAN_RAYS
    )
    assert planted_failure
    return a_m, permutation


def assert_chart_frames() -> tuple[dict[int, int], tuple[int, ...], tuple[tuple[int, ...], ...]]:
    signs: dict[int, int] = {}
    dual_frames = []
    for left, right in product(range(6), repeat=2):
        chart_number = 6 * left + right
        ray_ids, matrix, dual, sign = chart_data(left, right)
        signs[chart_number] = sign
        dual_frames.append(dual)
        assert matmul(dual, matrix) == identity(4)
        assert all(dot(dual[row], FAN_RAYS[ray_ids[column]]) == (row == column)
                   for row in range(4) for column in range(4))
        assert sign == (1 if ((left < 3) == (right < 3)) else -1)

        q_h = q_exponent(dual, ray_ids)
        for point in POLYTOPE_POINTS:
            exponents = raw_exponents(point, ray_ids)
            common = scale_sum(exponents, tuple(tuple(Fraction(v) for v in row) for row in dual))
            assert common == add(point, q_h)

        for component, ray in enumerate(FAN_RAYS):
            component_points = tuple(point for point in POLYTOPE_POINTS if dot(point, ray) >= 0)
            assert len(component_points) == 35
            q_component = q_exponent(dual, ray_ids, component)
            for point in component_points:
                exponents = raw_exponents(point, ray_ids, component)
                common = scale_sum(exponents, tuple(tuple(Fraction(v) for v in row) for row in dual))
                assert common == add(point, q_component)

    sign_counts = {sign: tuple(signs.values()).count(sign) for sign in (-1, 1)}
    assert sign_counts == {-1: 18, 1: 18}

    # The old unordered representative choice is replaced by the minimum
    # chart number in each exact orbit.
    unseen = set(product(range(6), repeat=2))
    chart_orbits = []
    while unseen:
        selected = min(unseen, key=lambda chart: 6 * chart[0] + chart[1])
        selected_orbit = orbit(selected)
        chart_orbits.append(selected_orbit)
        unseen.difference_update(selected_orbit)
    assert sorted(len(value) for value in chart_orbits) == [12, 12, 12]
    representatives = tuple(min(6 * left + right for left, right in value) for value in chart_orbits)
    assert representatives == (0, 1, 2)

    expected_representative_duals = (
        ((0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0)),
        ((0, 0, -1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (1, 0, 0, 0)),
        ((0, 0, -1, -1), (0, 0, 0, 1), (0, 1, 0, 0), (1, 0, 0, 0)),
    )
    actual_representative_duals = tuple(
        chart_data(number // 6, number % 6)[2] for number in representatives
    )
    assert actual_representative_duals == expected_representative_duals

    # Sorting global ray IDs instead of ray vectors gives a different affine
    # coordinate frame even on chart zero; this planted convention error must
    # be visible.
    correct_dual = chart_data(0, 0)[2]
    wrong_dual = integral(inverse(ray_matrix(tuple(sorted((0, 1, 6, 7))))))
    assert wrong_dual != correct_dual

    # A raw anticanonical chart monomial is q_H*t^u, not t^u.  Dividing by
    # q_H is an essential frame conversion rather than a cosmetic rewrite.
    ray_ids, _, dual, _ = chart_data(0, 1)
    point = (1, 0, 1, 1)
    raw_common = scale_sum(raw_exponents(point, ray_ids), tuple(
        tuple(Fraction(value) for value in row) for row in dual
    ))
    assert raw_common != tuple(map(Fraction, point))
    assert tuple(a - b for a, b in zip(raw_common, q_exponent(dual, ray_ids))) == tuple(
        map(Fraction, point)
    )
    return sign_counts, representatives, actual_representative_duals


def assert_chart_action() -> tuple[tuple[int, int], ...]:
    assert all(chart_action((left, right)) == ((right + 1) % 6, left)
               for left, right in product(range(6), repeat=2))
    sample_orbit = orbit((0, 0))
    assert len(sample_orbit) == 12
    return sample_orbit


def main() -> None:
    a_m, permutation = assert_lattice_action()
    sign_counts, representatives, representative_duals = assert_chart_frames()
    sample_orbit = assert_chart_action()
    print("DATA exact monomial action A_M =", a_m)
    print("RESULT exact ray permutation =", permutation)
    print("RESULT induced chart action is (i,j) -> (j+1 mod 6,i), of order 12")
    print("DATA chart-0 orbit =", tuple(6 * left + right for left, right in sample_orbit))
    print("RESULT deterministic chart-orbit representatives =", representatives)
    print("DATA representative y-to-t exponent rows =", representative_duals)
    print("RESULT ordered-ray orientation counts =", sign_counts)
    print("RESULT all 49 anticanonical and 12x35 component monomials satisfy raw = q_D * t^u on every chart")
    print("RESULT Cartier/rational frames are ell_(D,sigma)=q_(D,sigma)^(-1); raw chart coefficients require division by q_D in common Laurent coordinates")
    print("RESULT planted wrong ray ordering, all-positive orientation and omitted-q_D conventions are rejected")
    print("SCOPE Phi_308 coefficients and characteristic-zero Bezout multipliers are not serialized or evaluated here")


if __name__ == "__main__":
    main()
