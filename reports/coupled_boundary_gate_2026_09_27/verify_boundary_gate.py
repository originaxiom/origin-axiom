"""Exact boundary-only comparators. Do not import before local Git seal."""
import json
from itertools import combinations
from pathlib import Path

import sympy as s


def inputs():
    return json.loads(Path(__file__).with_name("INPUTS.json").read_text())


def nilpotent(partition):
    blocks = []
    for size in partition:
        block = s.zeros(size)
        for j in range(size - 1):
            block[j, j + 1] = 1
        blocks.append(block)
    return s.diag(*blocks)


def unipotent(partition):
    n = nilpotent(partition)
    return sum((n**k / s.factorial(k) for k in range(1, n.rows)), s.eye(n.rows))


def wedge2(a):
    pairs = list(combinations(range(a.rows), 2))
    return s.Matrix([
        [a[i, k] * a[j, l] - a[i, l] * a[j, k] for k, l in pairs]
        for i, j in pairs
    ])


def dual(a):
    return a.inv().T


def fixed(*matrices):
    size = matrices[0].rows
    equations = s.Matrix.vstack(*(a - s.eye(size) for a in matrices))
    return size - equations.rank()


def cubic_fixed(a, phase):
    omega = s.Matrix([[0, -1], [1, -1]])
    lifted = s.kronecker_product(a, omega ** (phase % 3))
    nullity = fixed(lifted)
    assert nullity % 2 == 0
    return nullity // 2


def jordan_wedge_count(partition):
    return sum(n // 2 for n in partition) + sum(
        min(a, b) for a, b in combinations(partition, 2)
    )


def boundary_models():
    data = inputs()
    a = s.eye(2)
    a[0, 1] = s.Rational(*data["meridian_shear"])
    p = s.Matrix(data["permutation"])
    w = s.eye(5)
    w[0, 1] = data["toy_longitude_shear"]
    down = s.diag(a, p)
    up = down ** data["cover_degree"]
    return down, up, w


def mixed(a):
    # vec(A X B^-1) = (B^-T tensor A) vec(X).
    return s.kronecker_product(dual(a[2:, 2:]), a[:2, :2])


def index_interval(t0, t0_dual, a0, a0_dual):
    assert 0 <= a0 <= t0 and 0 <= a0_dual <= t0_dual
    delta = a0 - a0_dual
    return delta - t0, delta + t0_dual


def universal_interval(t0, t0_dual):
    bounds = [index_interval(t0, t0_dual, a, b)
              for a in range(t0 + 1) for b in range(t0_dual + 1)]
    return min(lo for lo, _ in bounds), max(hi for _, hi in bounds)


def main():
    data = inputs()
    rows = []
    for partition, predicted in zip(data["partitions"], data["expected_partition_wedge_dimensions"]):
        u = unipotent(partition)
        v = wedge2(u)
        assert u.det() == v.det() == 1
        assert fixed(u) == len(partition)
        assert fixed(v) == jordan_wedge_count(partition) == predicted
        assert fixed(dual(u)) == fixed(u)
        assert fixed(dual(v)) == fixed(v)
        rows.append({"partition": partition, "E": fixed(u), "wedge2E": fixed(v)})
    down, up, w = boundary_models()
    assert up == s.diag(s.Matrix([[1, 1], [0, 1]]), s.eye(3))
    models = {}
    for name, u, expected in [("quotient_meridian", down, [2, 3, 1]),
                              ("cubed_cover_meridian", up, [4, 7, 3])]:
        assert u.det() == w.det() == 1 and u * w == w * u
        coefficients = [u, wedge2(u), mixed(u)]
        longitudes = [w, wedge2(w), mixed(w)]
        counts = [fixed(a) for a in coefficients]
        assert counts == expected
        assert [fixed(a, b) for a, b in zip(coefficients, longitudes)] == counts
        assert [fixed(dual(a), dual(b)) for a, b in zip(coefficients, longitudes)] == counts
        models[name] = {
            "meridian_bounds_E_wedge_mixed": counts,
            "toy_pair_attains_bounds": True,
            "E_balanced_H0_interval": list(index_interval(counts[0], counts[0], 0, 0)),
            "E_unconditional_interval": list(universal_interval(counts[0], counts[0])),
            "cubic_twist_E": [cubic_fixed(u, k) for k in range(3)],
            "cubic_twist_wedge2E": [cubic_fixed(wedge2(u), k) for k in range(3)],
        }
    assert models["quotient_meridian"]["cubic_twist_E"] == [2, 1, 1]
    assert models["quotient_meridian"]["cubic_twist_wedge2E"] == [3, 2, 2]
    assert models["cubed_cover_meridian"]["cubic_twist_E"] == [4, 0, 0]
    assert models["cubed_cover_meridian"]["cubic_twist_wedge2E"] == [7, 0, 0]
    print(json.dumps({
        "scope": data["scope"], "partition_comparators": rows, "boundary_models": models,
        "principal_E_unconditional_interval": list(universal_interval(1, 1)),
        "principal_E_balanced_interval": list(index_interval(1, 1, 0, 0)),
        "global_representation_constructed": False,
        "physical_chirality_derived": False,
    }, indent=2))
    print("PASS: exact boundary comparators; no global or physical existence claim")


if __name__ == "__main__":
    main()
