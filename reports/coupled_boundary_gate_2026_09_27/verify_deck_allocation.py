"""Boundary/deck comparators, not a global representation calculation."""
import json
from itertools import product

import sympy as s

from verify_boundary_gate import boundary_models, fixed, inputs, wedge2


def allocations(bounds, target, equal_nontrivial=False):
    return [x for x in product(*(range(-b, b + 1) for b in bounds))
            if sum(x) == target and (not equal_nontrivial or x[1] == x[2])]


def twisted_pair_fixed(u, w, phase):
    omega = s.Matrix([[0, -1], [1, -1]])
    count = fixed(s.kronecker_product(u, omega ** (phase % 3)),
                  s.kronecker_product(w, s.eye(2)))
    assert count % 2 == 0
    return count // 2


def transfer_comparator(u, w):
    p = s.Matrix(inputs()["permutation"])
    n = u.rows
    # The regular factor is first; deck and holonomy are different maps.
    deck = s.kronecker_product(p, s.eye(n))
    mu = s.kronecker_product(p, u)
    longitude = s.kronecker_product(s.eye(3), w)
    return {
        "twisted_pair_fixed": [twisted_pair_fixed(u, w, k) for k in range(3)],
        "pushforward_pair_fixed": fixed(mu, longitude),
        "invariant_pair_fixed": fixed(mu, longitude, deck),
        "upstairs_pair_fixed": fixed(u**3, w),
        "deck_order_three": deck**3 == s.eye(3*n),
        "holonomy_cube_is_identity": mu**3 == s.eye(3*n),
    }


def main():
    u, _, w = boundary_models()
    fundamental = transfer_comparator(u, w)
    exterior = transfer_comparator(wedge2(u), wedge2(w))
    assert fundamental["twisted_pair_fixed"] == [2, 1, 1]
    assert exterior["twisted_pair_fixed"] == [3, 2, 2]
    for row, total, invariant in [(fundamental, 4, 2), (exterior, 7, 3)]:
        assert row["pushforward_pair_fixed"] == row["upstairs_pair_fixed"] == total
        assert sum(row["twisted_pair_fixed"]) == total
        assert row["invariant_pair_fixed"] == invariant
        assert row["deck_order_three"] and not row["holonomy_cube_is_identity"]
    possibilities = allocations((2, 1, 1), 3)
    assert possibilities == [(1, 1, 1), (2, 0, 1), (2, 1, 0)]
    assert allocations((2, 1, 1), 3, True) == [(1, 1, 1)]
    print(json.dumps({
        "E_boundary_comparator": fundamental,
        "wedge2E_boundary_comparator": exterior,
        "necessary_E_index_triples_for_plus_three": possibilities,
        "if_Galois_hypothesis_holds": allocations((2, 1, 1), 3, True),
        "global_index_computed": False, "physical_chirality_derived": False,
    }, indent=2))
    print("PASS: exact local transfer and necessary deck-allocation constraints")


if __name__ == "__main__":
    main()
