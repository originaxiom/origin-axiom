#!/usr/bin/env python3
"""R035: exact A1/SU6 branching against the full joint SM-shaped 27.

Convention:
    27 | SU6 x SU2_E = (Lambda^2 6, 1) + (bar(6), 2_E).

The SU2_E factor is the minimal A1 used by the holonomy; the unbroken gauge
algebra is its SU6 centralizer.  The main positive test therefore embeds
SU3_color x SU2_weak x U1 inside SU6 and forgets only the SU2_E multiplicity.
All arithmetic is exact Fraction arithmetic.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
COLOR_DIM = {"1": 1, "3": 3, "3bar": 3}


def add(result, color, weak_dim, charge, copies=1):
    result[(color, int(weak_dim), F(charge))] += int(copies)


def dimension(branch):
    return sum(COLOR_DIM[color] * weak_dim * copies
               for (color, weak_dim, _charge), copies in branch.items())


def charge_histogram(branch):
    answer = Counter()
    for (color, weak_dim, charge), copies in branch.items():
        answer[charge] += COLOR_DIM[color] * weak_dim * copies
    return answer


def internal_weak_branch(a, b, c):
    """6=(3,1)_a +(1,2)_b +(1,1)_c; physical weak lies in SU6."""

    a, b, c = map(F, (a, b, c))
    assert 3 * a + 2 * b + c == 0
    answer = Counter()

    # (15,1_E) = Lambda^2(6)
    add(answer, "3bar", 1, 2 * a)       # Lambda^2(3)
    add(answer, "3", 2, a + b)          # 3 tensor 2
    add(answer, "3", 1, a + c)          # 3 tensor 1
    add(answer, "1", 1, 2 * b)          # Lambda^2(2)
    add(answer, "1", 2, b + c)          # 2 tensor 1

    # (bar(6),2_E); SU2_E gives two copies after restriction to the centralizer.
    add(answer, "3bar", 1, -a, copies=2)
    add(answer, "1", 2, -b, copies=2)
    add(answer, "1", 1, -c, copies=2)
    assert dimension(answer) == 27
    return answer


def external_weak_branch(a, b, c, d):
    """Abstract control: take SU2_E itself as weak; this is not unbroken gauge."""

    a, b, c, d = map(F, (a, b, c, d))
    assert 3 * a + b + c + d == 0
    answer = Counter()

    # Here the defining color block is bar(3), plus three singlets.
    add(answer, "3", 1, 2 * a)          # Lambda^2(bar3)
    for value in (b, c, d):
        add(answer, "3bar", 1, a + value)
    for left, right in ((b, c), (b, d), (c, d)):
        add(answer, "1", 1, left + right)

    # bar(6) tensor 2_E: now 2_E is being read as the weak doublet.
    add(answer, "3", 2, -a)
    for value in (b, c, d):
        add(answer, "1", 2, -value)
    assert dimension(answer) == 27
    return answer


TARGET = Counter({
    ("3", 2, F(1, 6)): 1,       # Q
    ("3bar", 1, F(-2, 3)): 1,   # u^c
    ("3bar", 1, F(1, 3)): 2,    # d^c and exotic Dbar
    ("3", 1, F(-1, 3)): 1,      # exotic D
    ("1", 2, F(-1, 2)): 2,      # L and H_d
    ("1", 2, F(1, 2)): 1,       # H_u
    ("1", 1, F(1)): 1,          # e^c
    ("1", 1, F(0)): 2,          # nu^c and S
})


def matrix_commutator(left, right):
    def mul(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(2))
                 for j in range(2)] for i in range(2)]
    lr, rl = mul(left, right), mul(right, left)
    return [[lr[i][j] - rl[i][j] for j in range(2)] for i in range(2)]


def su2_tensor_dimensions(left_dim, right_dim):
    """Dimensions in the Clebsch--Gordan product V_m tensor V_n."""

    low = abs(int(left_dim) - int(right_dim)) + 1
    high = int(left_dim) + int(right_dim) - 1
    return set(range(low, high + 1, 2))


def main() -> None:
    sources = json.loads((HERE / "source_snapshot.json").read_text())
    assert sources["schema"] == "oa-r035-a1-su6-sm-branching-sources-v1"
    assert sources["source_commit"] == "864c6b758e2bbd0e0921f5e36af47df68b3c99ca"
    assert {key: item["git_blob_sha1"] for key, item in sources["sources"].items()} == {
        "b254": "975cd957c678f4d6ca99c989b4a18de424d0a1a0",
        "b1098": "80682625d94d1d7fa5cfa61fd867d70a2e7aa29d",
        "b1102": "16df38b29a6d560b3c10c9af20388dfef5a068df",
        "b1109": "347288f3039fbb455f48878b612aa1d77bf6058d",
        "b1112": "390fbb4c033e78dffdde843ecfcdf75e4fd51275",
        "b1139": "74d05d28fbd364c636bd8cdb04116a77e8843659",
        "b1145": "bbfc235ced367c9294c02e72907506abd6039c24",
    }

    assert dimension(TARGET) == 27
    assert sorted(charge_histogram(TARGET).values(), reverse=True) == [6, 6, 4, 3, 3, 2, 2, 1]

    # The exact centralizer-compatible solution.
    y6 = (F(-1, 3), F(1, 2), F(0))
    exact = internal_weak_branch(*y6)
    assert exact == TARGET

    # Exhaust the only block charges compatible with the target labels.  The
    # bar(6),2_E term forces -a into target (bar3,1) charges, -b into target
    # (1,2) charges, and -c into target singlet charges.
    a_values = sorted({-charge for color, weak, charge in TARGET
                       if color == "3bar" and weak == 1})
    b_values = sorted({-charge for color, weak, charge in TARGET
                       if color == "1" and weak == 2})
    c_values = sorted({-charge for color, weak, charge in TARGET
                       if color == "1" and weak == 1})
    trace_compatible = [(a, b, c) for a, b, c in product(a_values, b_values, c_values)
                        if 3 * a + 2 * b + c == 0]
    joint_hits = [values for values in trace_compatible
                  if internal_weak_branch(*values) == TARGET]
    assert trace_compatible == [
        (F(-1, 3), F(1, 2), F(0)),
        (F(2, 3), F(-1, 2), F(-1)),
    ]
    assert joint_hits == [y6]

    # Bite: charge multiplicities alone admit a false positive.  The mixed
    # dual signs are load-bearing: 27=(15,1)+(bar6,2), not an all-plus model.
    charge_only_false_positive = (F(-1, 6), F(1, 2), F(-1, 2))
    assert charge_histogram(internal_weak_branch(*charge_only_false_positive)) == charge_histogram(TARGET)
    assert internal_weak_branch(*charge_only_false_positive) != TARGET

    # A second abstract match exists if SU2_E itself is called weak, but SU2_E
    # is the holonomy A1, not part of its SU6 centralizer.  A nonabelian group
    # does not commute with its own dense image (elementary bite below).
    external = external_weak_branch(F(-1, 6), F(1, 2), F(1, 2), F(-1, 2))
    assert external == TARGET
    e = [[0, 1], [0, 0]]
    f = [[0, 0], [1, 0]]
    assert matrix_commutator(e, f) == [[1, 0], [0, -1]]

    # Nor can a diagonal weak identification hide the type error: the exact
    # internal branch contains (2_W,2_E), which restricts diagonally as 1+3.
    assert set(weak for _color, weak, _charge in TARGET) == {1, 2}
    diagonal_weak_dimensions = su2_tensor_dimensions(2, 2)
    assert exact[("1", 2, F(-1, 2))] == 2  # one (2_W,2_E), dimension(E)=2
    assert 3 in diagonal_weak_dimensions and 3 not in {
        weak for _color, weak, _charge in TARGET
    }

    # S(U3 x U2 x U1) has two commuting block-scalar directions.  Y is one;
    # an independent traceless X demonstrates the extra U1 remains.
    extra_x = (F(1, 3), F(0), F(-1))
    assert 3 * y6[0] + 2 * y6[1] + y6[2] == 0
    assert 3 * extra_x[0] + 2 * extra_x[1] + extra_x[2] == 0
    assert y6[0] * extra_x[1] - y6[1] * extra_x[0] != 0

    print("PASS mixed-dual 27=(15,1)+(bar6,2_E) has dimension 27")
    print("PASS unique internal-SU6 joint match Y6 = (-1/3,-1/3,-1/3,1/2,1/2,0)")
    print("CONTROL charge histogram alone admits a false positive rejected by joint reps")
    print("CONTROL external-SU2_E abstract match is not an unbroken centralizer gauge factor")
    print("CONTROL diagonal weak contains a triplet absent from the target")
    print("RESULT A1/SU6 branch reproduces the full joint SM-shaped E6 27 exactly")
    print("DATA commuting block-scalar rank = 2: hypercharge plus one extra U1")
    print("SCOPE compatibility theorem; A1 selection, extra-U1 breaking, physical matter/spin, chirality, generations, dynamics and values remain open")


if __name__ == "__main__":
    main()
