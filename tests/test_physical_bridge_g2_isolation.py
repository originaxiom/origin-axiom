"""Locks on actual fixed spaces, not on the wording of a physical verdict."""
import json

import sympy as sp

from reports.physical_bridge_2026_09_05 import g2_isolation_audit as g


def test_positive_form_and_actual_compact_G2_group():
    result = g.exact_example()
    assert sp.Matrix(result["metric"]) == sp.eye(7)
    assert len(result["group"]) == 8
    assert all(g.preserves_form(sp.Matrix(m), g.PHI) for m in result["group"])


def test_all_elements_fix_but_group_does_not():
    result = g.exact_example()
    assert result["nonidentity_fixed_dimensions"] == [3]*7
    assert result["common_fixed_dimension"] == 0
    # The mutation that replaces a common-fixed-space test by an element test loses.
    assert min(result["nonidentity_fixed_dimensions"]) != result["common_fixed_dimension"]
    assert result["single_generator_fixed_dimension"] == 3


def test_every_subgroup_and_independent_Reynolds_projector():
    result = g.exact_example()
    assert len(result["subgroups"]) == 16
    expected = {1: 7, 2: 3, 4: 1, 8: 0}
    for row in result["subgroups"]:
        projector = sp.Matrix(row["Reynolds_projector"])
        assert projector**2 == projector
        assert projector.rank() == row["fixed_dimension"] == expected[row["order"]]


def test_isotropy_stratum_is_not_the_entire_singular_set_or_a_chiral_index():
    result = g.exact_example()
    assert result["point_isotropy_orders"] == {"plane": 2, "axis": 4, "free": 1, "apex": 8}
    assert result["isolated_maximal_isotropy_stratum"]
    assert not result["isolated_point_of_total_singular_set"]
    assert not result["physical_chiral_index_computed"]


def test_wrong_SO7_form_control_is_rejected():
    wrong = sp.diag(-1, -1, 1, 1, 1, 1, 1)
    assert wrong.det() == 1 and wrong.T*wrong == sp.eye(7)
    assert not g.preserves_form(wrong, g.PHI)


def test_actual_old_group_keeps_lines_and_has_a_distinct_apex_stratum():
    result = g.original_group()
    assert result["group_order"] == 96
    assert result["nonidentity_element_census"] == {3: 53, 1: 42}
    assert result["exact_common_fixed_dimension"] == result["full_96_action_float_common_fixed_dimension"] == 0
    assert result["A1_E6_intersection_dimensions"] == [1]*30
    assert result["A1_orbit_sizes"] == [6, 12, 12]
    assert result["axis_stabilizer_orders"] == [48, 48, 48]


def test_upstream_element_test_can_pass_without_testing_the_inference():
    result = g.analyze()
    assert result["upstream_B1259_selftest"]["returncode"] == 0
    assert result["exact_G2_counterexample"]["common_fixed_dimension"] == 0
    assert not result["actual_B1084_group"]["physical_chiral_index_computed"]
    assert json.loads(json.dumps(result, allow_nan=False))["upstream_B1259_selftest"]["commit"] == g.UPSTREAM
