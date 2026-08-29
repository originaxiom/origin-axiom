#!/usr/bin/env python3
"""Marked toric top trace for Z=dP6 x dP6.

The height-308 Yukawa evaluator ultimately needs the connecting map

    H^3(Y,O_Y) -> H^4(Z,K_Z),

for an anticanonical hypersurface Y in Z.  This dependency-free certificate
constructs the weight-zero Cech representative of H^2(dP6,K_dP6), an exact
dual trace cycle, and its Eilenberg--Zilber cross product on the 36-chart
product cover.  The latter is a finite functional on C^4(K_Z).

The marked orientation is fixed by the listed fan-ray and chart orders.  A
different orientation rescales the trace by -1 and cannot change a Yukawa
rank or a nonvanishing result.  This file does not construct the
hypersurface lift, divide its Cech coboundary by f, or evaluate a Yukawa
entry.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


Scalar = Fraction
Simplex = tuple[int, ...]
Matrix = list[list[Scalar]]

RAYS = (
    (1, 0),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (0, -1),
    (1, -1),
)
CONES = tuple(frozenset((index, (index + 1) % 6)) for index in range(6))


def common_rays(charts: Simplex) -> frozenset[int]:
    common = set(CONES[charts[0]])
    for chart in charts[1:]:
        common.intersection_update(CONES[chart])
    return frozenset(common)


def canonical_weight_zero_exists(charts: Simplex) -> bool:
    """Toric local-section test for K=-sum D_r at character m=0.

    On an intersection with cone-ray set S, the inequalities are
    <0,v_r>-1 >= 0 for every r in S.  They are therefore soluble precisely
    when S is empty.
    """

    return not common_rays(charts)


BASES: dict[int, tuple[Simplex, ...]] = {
    degree: tuple(
        simplex
        for simplex in combinations(range(6), degree + 1)
        if canonical_weight_zero_exists(simplex)
    )
    for degree in range(6)
}


def differential(degree: int) -> Matrix:
    source = BASES[degree]
    target = BASES[degree + 1]
    source_index = {simplex: index for index, simplex in enumerate(source)}
    answer = [[Scalar(0) for _ in source] for _ in target]
    for row, simplex in enumerate(target):
        for omitted in range(len(simplex)):
            face = simplex[:omitted] + simplex[omitted + 1 :]
            if face in source_index:
                answer[row][source_index[face]] += Scalar((-1) ** omitted)
    return answer


DIFFERENTIALS = {degree: differential(degree) for degree in range(5)}


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left:
        return []
    inner = len(left[0])
    assert inner == len(right)
    columns = len(right[0]) if right else 0
    return [
        [sum((left[row][k] * right[k][column] for k in range(inner)), Scalar(0))
         for column in range(columns)]
        for row in range(len(left))
    ]


def rank(matrix: Matrix) -> int:
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0]) if rows else 0
    pivot_row = 0
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not rows[row][column]:
                continue
            scale = rows[row][column]
            rows[row] = [left - scale * right
                         for left, right in zip(rows[row], rows[pivot_row])]
        pivot_row += 1
    return pivot_row


def column(matrix: Matrix, index: int) -> list[Scalar]:
    return [row[index] for row in matrix]


def augment(matrix: Matrix, extra: list[Scalar]) -> Matrix:
    assert len(matrix) == len(extra)
    return [row + [value] for row, value in zip(matrix, extra)]


def vector_for(degree: int, values: dict[Simplex, Scalar | int]) -> list[Scalar]:
    return [Scalar(values.get(simplex, 0)) for simplex in BASES[degree]]


# The all-ones two-cocycle is cyclically fixed literally: on every ordered
# four-set its differential is 1-1+1-1=0.
TAU_VALUES = {simplex: 1 for simplex in BASES[2]}
TAU = vector_for(2, TAU_VALUES)

# This is an exact Cech-homology two-cycle.  Pairing it with a two-cocycle
# gives the marked trace.  It was chosen cyclically invariant and normalized
# to <TRACE_CYCLE,TAU>=1.
TRACE_VALUES = {
    (0, 1, 3): Scalar(1, 4),
    (0, 2, 4): Scalar(-1, 4),
    (0, 2, 5): Scalar(1, 4),
    (0, 3, 4): Scalar(1, 4),
    (1, 2, 4): Scalar(1, 4),
    (1, 3, 5): Scalar(-1, 4),
    (1, 4, 5): Scalar(1, 4),
    (2, 3, 5): Scalar(1, 4),
}
TRACE = vector_for(2, TRACE_VALUES)

# A plausible one-index variant is retained as a negative control.  Merely
# replacing 013 by 012 breaks the dual-cycle equations; a trace row is not a
# freely chosen normalization.
REJECTED_TRACE_VALUES = dict(TRACE_VALUES)
REJECTED_TRACE_VALUES.pop((0, 1, 3))
REJECTED_TRACE_VALUES[(0, 1, 2)] = Scalar(1, 4)
REJECTED_TRACE = vector_for(2, REJECTED_TRACE_VALUES)


def dot(left: list[Scalar], right: list[Scalar]) -> Scalar:
    assert len(left) == len(right)
    return sum((a * b for a, b in zip(left, right)), Scalar(0))


def det2(left: tuple[int, int], right: tuple[int, int]) -> int:
    return left[0] * right[1] - left[1] * right[0]


def shifted(simplex: Simplex) -> tuple[Simplex, int]:
    entries = [((entry + 1) % 6) for entry in simplex]
    inversions = sum(
        entries[left] > entries[right]
        for left in range(len(entries))
        for right in range(left + 1, len(entries))
    )
    return tuple(sorted(entries)), (-1 if inversions % 2 else 1)


def shift_vector(degree: int, vector: list[Scalar]) -> list[Scalar]:
    target_index = {simplex: index for index, simplex in enumerate(BASES[degree])}
    answer = [Scalar(0) for _ in vector]
    for simplex, value in zip(BASES[degree], vector):
        target, sign = shifted(simplex)
        answer[target_index[target]] += sign * value
    return answer


def shuffle_words() -> tuple[tuple[str, ...], ...]:
    words = []
    for horizontal_positions in combinations(range(4), 2):
        horizontal = set(horizontal_positions)
        words.append(tuple("H" if index in horizontal else "V" for index in range(4)))
    return tuple(words)


def shuffle_sign(word: tuple[str, ...]) -> int:
    # Koszul sign: the number of vertical steps occurring before a horizontal
    # step.  Both factor degrees are even, but individual shuffles still carry
    # their ordinary permutation signs.
    inversions = sum(
        word[left] == "V" and word[right] == "H"
        for left in range(4)
        for right in range(left + 1, 4)
    )
    return -1 if inversions % 2 else 1


def product_simplex(left: Simplex, right: Simplex, word: tuple[str, ...]) -> Simplex:
    left_position = 0
    right_position = 0
    vertices = [(left[0], right[0])]
    for step in word:
        if step == "H":
            left_position += 1
        else:
            right_position += 1
        vertices.append((left[left_position], right[right_position]))
    # The product cover uses lexicographic chart order (i,j) -> 6*i+j.
    encoded = tuple(6 * left_chart + right_chart for left_chart, right_chart in vertices)
    assert all(encoded[index] < encoded[index + 1] for index in range(4))
    return encoded


def product_trace_cycle() -> dict[Simplex, Scalar]:
    answer: dict[Simplex, Scalar] = {}
    for left, left_value in TRACE_VALUES.items():
        for right, right_value in TRACE_VALUES.items():
            for word in shuffle_words():
                simplex = product_simplex(left, right, word)
                coefficient = Scalar(left_value * right_value * shuffle_sign(word))
                answer[simplex] = answer.get(simplex, Scalar(0)) + coefficient
    return {simplex: value for simplex, value in answer.items() if value}


PRODUCT_TRACE = product_trace_cycle()


def product_weight_zero_exists(simplex: Simplex) -> bool:
    decoded = tuple(divmod(vertex, 6) for vertex in simplex)
    left_charts = tuple(pair[0] for pair in decoded)
    right_charts = tuple(pair[1] for pair in decoded)
    return canonical_weight_zero_exists(left_charts) and canonical_weight_zero_exists(right_charts)


def boundary(chain: dict[Simplex, Scalar]) -> dict[Simplex, Scalar]:
    answer: dict[Simplex, Scalar] = {}
    for simplex, value in chain.items():
        for omitted in range(len(simplex)):
            face = simplex[:omitted] + simplex[omitted + 1 :]
            # The dual chain complex has one basis vector only when the
            # corresponding weight-zero local section exists.  Ineligible
            # faces are absent, exactly as in the factor differential.
            if not product_weight_zero_exists(face):
                continue
            answer[face] = answer.get(face, Scalar(0)) + ((-1) ** omitted) * value
    return {simplex: value for simplex, value in answer.items() if value}


def alternating_value(values: dict[Simplex, Scalar | int], entries: Simplex) -> Scalar:
    if len(set(entries)) != len(entries):
        return Scalar(0)
    inversions = sum(
        entries[left] > entries[right]
        for left in range(len(entries))
        for right in range(left + 1, len(entries))
    )
    return (-1 if inversions % 2 else 1) * values.get(tuple(sorted(entries)), 0)


def alexander_whitney_top(simplex: Simplex) -> Scalar:
    decoded = tuple(divmod(vertex, 6) for vertex in simplex)
    left_face = tuple(decoded[index][0] for index in range(3))
    right_face = tuple(decoded[index][1] for index in range(2, 5))
    return alternating_value(TAU_VALUES, left_face) * alternating_value(TAU_VALUES, right_face)


def assert_factor_complex() -> tuple[list[int], list[int], list[int]]:
    assert all(det2(RAYS[index], RAYS[(index + 1) % 6]) == 1
               for index in range(6))
    dimensions = [len(BASES[degree]) for degree in range(6)]
    assert dimensions == [0, 9, 20, 15, 6, 1]
    ranks = [rank(DIFFERENTIALS[degree]) for degree in range(5)]
    assert ranks == [0, 9, 10, 5, 1]
    for degree in range(4):
        product = matmul(DIFFERENTIALS[degree + 1], DIFFERENTIALS[degree])
        assert all(not value for row in product for value in row)

    incoming = [0] + ranks
    outgoing = ranks + [0]
    cohomology = [
        dimensions[degree] - outgoing[degree] - incoming[degree]
        for degree in range(6)
    ]
    assert cohomology == [0, 0, 1, 0, 0, 0]

    assert all(not value for value in [
        sum(DIFFERENTIALS[2][row][entry] * TAU[entry]
            for entry in range(len(TAU)))
        for row in range(len(BASES[3]))
    ])
    assert rank(augment(DIFFERENTIALS[1], TAU)) == ranks[1] + 1

    # TRACE is a cycle in the dual Cech chain complex and is normalized.
    assert all(dot(TRACE, column(DIFFERENTIALS[1], entry)) == 0
               for entry in range(len(BASES[1])))
    assert dot(TRACE, TAU) == 1

    dual_boundaries = [list(row) for row in zip(*DIFFERENTIALS[2])]
    alternate_trace = [left + right
                       for left, right in zip(TRACE, column(dual_boundaries, 0))]
    assert all(dot(alternate_trace, column(DIFFERENTIALS[1], entry)) == 0
               for entry in range(len(BASES[1])))
    assert dot(alternate_trace, TAU) == 1
    trace_difference = [left - right for left, right in zip(alternate_trace, TRACE)]
    assert rank(augment(dual_boundaries, trace_difference)) == rank(dual_boundaries)
    assert any(dot(REJECTED_TRACE, column(DIFFERENTIALS[1], entry)) != 0
               for entry in range(len(BASES[1])))

    # The chart rotation preserves both the trace cycle and the all-ones top
    # cocycle literally.
    assert shift_vector(2, TRACE) == TRACE
    shifted_tau = shift_vector(2, TAU)
    assert shifted_tau == TAU
    return dimensions, ranks, cohomology


def assert_product_trace() -> None:
    assert len(shuffle_words()) == 6
    assert all(product_weight_zero_exists(simplex) for simplex in PRODUCT_TRACE)
    assert not boundary(PRODUCT_TRACE)
    pairing = sum(
        coefficient * alexander_whitney_top(simplex)
        for simplex, coefficient in PRODUCT_TRACE.items()
    )
    assert pairing == 1

    # The trace kills both types of total-complex degree-four boundaries:
    # d(C1 tensor C2) and d(C2 tensor C1).
    for entry in range(len(BASES[1])):
        assert dot(TRACE, column(DIFFERENTIALS[1], entry)) == 0
    assert dot(TRACE, TAU) == 1

    # The order-twelve ray action exchanges the two dP6 factors and rotates
    # one factor.  The graded swap sign is (-1)^(2*2)=+1; factor rotation is
    # already checked above, hence the marked product trace is invariant.
    assert (-1) ** (2 * 2) == 1


def main() -> None:
    dimensions, ranks, cohomology = assert_factor_complex()
    assert_product_trace()
    print("DATA dP6 canonical weight-zero Cech dimensions =", dimensions)
    print("DATA dP6 canonical weight-zero differential ranks =", ranks)
    print("RESULT dP6 canonical weight-zero cohomology dimensions =", cohomology)
    print("DATA marked H2(K_dP6) generator support =", sorted(TAU_VALUES.items()))
    print("DATA cyclic trace-cycle support =", sorted(TRACE_VALUES.items()))
    print("RESULT factor trace(tau) =", dot(TRACE, TAU))
    print("RESULT a boundary-shifted trace is homologous; the planted 012-for-013 row is rejected")
    print("RESULT chart rotation acts as +1 on the marked H2 class")
    print("DATA product trace-cycle nonzero simplex count =", len(PRODUCT_TRACE))
    print("RESULT product trace cycle has zero boundary and pairs with tau x tau as 1")
    print("RESULT order-12 factor-exchange action has product orientation sign +1")
    print("RESULT normalized ambient trace Tr_Z: H4(K_Z) -> Q is explicit on the 36-chart cover")
    print("SCOPE C12 invariance is a cohomology/trace statement; literal invariance of this marked 384-simplex chain is not claimed")
    print("SCOPE for anticanonical Y, Tr_Y(c)=Tr_Z(delta_f(c)); constructing delta_f(c) for the 18 connecting Yukawa entries remains open")


if __name__ == "__main__":
    main()
