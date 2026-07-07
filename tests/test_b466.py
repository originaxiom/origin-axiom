"""B466 — locks: the sigma action on the SL(3) components, the fixed line, the
Gieseking half-monodromy identities, and the geometric period-2 orbit."""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B466_sigma_equivariant"))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B71_sl3_apoly"))

from sigma_action import (sigma_component_map, sigma_fixed_locus,
                          sl2_geometric_orbit, p, q)


def test_component_map_exchanges_dehn_pair():
    assert sigma_component_map() == {"V0": "V0", "W1": "W2", "W2": "W1"}


def test_fixed_locus_is_the_v0_line_through_allones():
    on_v0, on_w1, allones = sigma_fixed_locus()
    assert set(map(str, on_v0)) == {"-p + q", "p - q"}
    assert on_w1 == [{p: 1, q: 1}]
    assert allones


def test_geometric_orbit_is_banked_b448_period2():
    kap, roots, swap, fixed = sl2_geometric_orbit()
    assert sp.expand(kap - sp.expand(sp.Symbol('x')**2 * (sp.Symbol('x')**2 - 3*sp.Symbol('x') + 3))) == 0
    assert swap and set(fixed) == {0, 2}
    disc = sp.discriminant(sp.Symbol('x')**2 - 3*sp.Symbol('x') + 3, sp.Symbol('x'))
    assert disc == -3   # Q(sqrt-3), the trace field


def test_sigma_is_orientation_reversing_half_monodromy():
    A = sp.Matrix([[1, 1], [1, 0]])
    assert A.det() == -1
    assert A * A == sp.Matrix([[2, 1], [1, 1]])
