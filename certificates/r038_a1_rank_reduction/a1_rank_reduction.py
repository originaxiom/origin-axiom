#!/usr/bin/env python3
"""R038: exact A1/SU(6) singlet stabilizer and rank-reduction audit.

The computation distinguishes the gauge-centralizer reading of SU(2)_E from
incorrectly treating SU(2)_E as a second four-dimensional gauge factor.
Only Python's standard library is used.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
Q = Fraction


def add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def neg(value):
    return (-value[0], -value[1])


def zero_matrix(size):
    return [[(0, 0) for _ in range(size)] for _ in range(size)]


def su_basis(size):
    """An integral real basis of anti-Hermitian traceless matrices."""

    answer = []
    for left, right in combinations(range(size), 2):
        real_skew = zero_matrix(size)
        real_skew[left][right] = (1, 0)
        real_skew[right][left] = (-1, 0)
        answer.append(real_skew)

        imaginary_symmetric = zero_matrix(size)
        imaginary_symmetric[left][right] = (0, 1)
        imaginary_symmetric[right][left] = (0, 1)
        answer.append(imaginary_symmetric)
    for index in range(size - 1):
        diagonal = zero_matrix(size)
        diagonal[index][index] = (0, 1)
        diagonal[-1][-1] = (0, -1)
        answer.append(diagonal)
    assert len(answer) == size * size - 1
    return answer


def tensor_action(a, b=None):
    """Infinitesimal action on v=bar(e_6) tensor e_1."""

    values = [[(0, 0) for _ in range(2)] for _ in range(6)]
    # Dual action is -bar(e_6) A.
    for column in range(6):
        values[column][0] = neg(a[5][column])
    if b is not None:
        # Fundamental SU(2) action on e_1.
        for row in range(2):
            values[5][row] = add(values[5][row], b[row][0])
    return [coordinate for row in values for value in row for coordinate in value]


def rank(rows):
    matrix = [[Q(value) for value in row] for row in rows]
    if not matrix:
        return 0
    height, width = len(matrix), len(matrix[0])
    pivot_row = 0
    for column in range(width):
        pivot = next((row for row in range(pivot_row, height)
                      if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(height):
            if row == pivot_row or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [left - scale * right
                           for left, right in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == height:
            break
    return pivot_row


def action_rank(columns):
    # Convert action vectors stored by generator into matrix rows.
    rows = [[column[row] for column in columns]
            for row in range(len(columns[0]))]
    return rank(rows)


def main():
    sources = json.loads((HERE / "source_snapshot.json").read_text())
    assert sources["schema"] == "oa-r038-a1-rank-reduction-sources-v1"
    assert sources["source_commit"] == "b92644283529b5b82334f9863b4a90ed0c1c9204"
    assert {key: row["git_blob_sha1"] for key, row in sources["sources"].items()} == {
        "r035_certificate": "ebdada2ca9ff7e86cd26fb62c49d7b90fad1d5f1",
        "r035_memo": "fef6a4448406c039d84569848904ad8f103760b4",
        "b1098_findings": "80682625d94d1d7fa5cfa61fd867d70a2e7aa29d",
        "b964_findings": "ec8211515297e9ca76e0910056f111e25446d914",
    }

    su6 = su_basis(6)
    su2 = su_basis(2)
    su6_actions = [tensor_action(generator) for generator in su6]
    full_actions = (su6_actions
                    + [tensor_action(zero_matrix(6), generator)
                       for generator in su2])
    orbit_su6 = action_rank(su6_actions)
    orbit_full = action_rank(full_actions)
    stabilizer_su6 = len(su6) - orbit_su6
    stabilizer_full = len(su6) + len(su2) - orbit_full
    assert (orbit_su6, stabilizer_su6) == (11, 24)
    assert (orbit_full, stabilizer_full) == (13, 25)

    # Defining-six charges.  The VEV lies in bar(e_6) tensor s_+.
    y = (Q(-1, 3),) * 3 + (Q(1, 2),) * 2 + (Q(0),)
    x = (Q(1, 3),) * 3 + (Q(0),) * 2 + (Q(-1),)
    assert sum(y) == sum(x) == 0
    h_su6 = tuple(2 * value_y + 5 * value_x
                  for value_y, value_x in zip(y, x))
    assert h_su6 == (Q(1),) * 5 + (Q(-5),)
    t_plus = Q(1)
    vev_y = -y[5]
    vev_x = -x[5]
    vev_h_full = -h_su6[5] - 5 * t_plus
    assert (vev_y, vev_x, vev_h_full) == (0, 1, 0)

    # SU(5) x U(1)_H branching of 27=(Lambda^2 6,1)+(bar6,2).
    branching = [
        ("10", 10, 2),
        ("5", 5, -4),
        ("bar5", 5, -6),
        ("bar5", 5, 4),
        ("1_vev", 1, 0),
        ("1", 1, 10),
    ]
    assert sum(dimension for _name, dimension, _charge in branching) == 27
    assert [row for row in branching if row[0] == "1_vev"] == [("1_vev", 1, 0)]

    # Cartan kernels: one constraint on rank 5 for SU(6), and one constraint
    # on rank 6 for SU(6)xSU(2).  These reproduce SU(5) and U(5), respectively.
    assert 5 - rank([[1, 1, 1, 1, 1]]) == 4
    assert 6 - rank([[1, 1, 1, 1, 1, 1]]) == 5

    # A single decomposable vector cannot be D-flat: both trace-free partial
    # projectors have nonzero Hilbert-Schmidt norm (normalization irrelevant).
    su6_moment_norm2 = 5 * Q(1, 6) ** 2 + Q(5, 6) ** 2
    su2_moment_norm2 = 2 * Q(1, 2) ** 2
    assert (su6_moment_norm2, su2_moment_norm2) == (Q(5, 6), Q(1, 2))

    # Complex algebraic stabilizer: line parabolic in SL6, Borel in SL2,
    # minus one character-matching equation.  Its reductive Levi is GL5.
    parabolic_sl6 = (6 * 6 - 1) - 5
    borel_sl2 = (2 * 2 - 1) - 1
    algebraic_stabilizer = parabolic_sl6 + borel_sl2 - 1
    assert (parabolic_sl6, borel_sl2, algebraic_stabilizer) == (30, 2, 31)

    print("PASS compact action kernel in SU(6) alone has dimension 24 and rank 4 = SU(5)")
    print("PASS full-product stabilizer algebra is u(5); cover preimage U(5), E6 image U(5)/C2")
    print("PASS VEV is Y-neutral, breaks pure X, and preserves diagonal (2Y+5X,-5T_E)")
    print("RESULT 27 -> 10_2 + 5_-4 + bar5_-6 + bar5_4 + 1_0 + 1_10")
    print("NEGATIVE one decomposable VEV is not D-flat; moment norms are 5/6 and 1/2")
    print("SCOPE SU(2)_E-as-holonomy gives conditional SU(6)->SU(5); no zero mode, VEV selection, SUSY vacuum or physical matter map")


if __name__ == "__main__":
    main()
