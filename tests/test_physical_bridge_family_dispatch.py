"""Two-sided controls of the exact delegating function flagged by the AST gate."""
import copy
import importlib.util
from pathlib import Path

import pytest

from reports.physical_bridge_2026_09_05 import family_action_domain as d

spec = importlib.util.spec_from_file_location("r11_domain_locks_controlled", Path(__file__).with_name("test_physical_bridge_family_domain.py"))
delegation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(delegation)

NAMES = (
    "test_lattice_integrality_and_a_corrupt_root_are_checked",
    "test_marked_map_verifies_all_products_and_rejects_bad_assignment",
    "test_root_space_actions_are_not_identified_from_orbit_counts",
    "test_commuting_split_reconstructs_literal_action_exactly",
    "test_six_classes_have_the_same_cycles_but_distinct_internal_actions",
    "test_map_is_equivariant_and_orientation_is_not_silently_fixed",
    "test_family_lift_has_order_three_and_lie_centralizer_control",
    "test_exact_arithmetic_and_input_provenance_are_retained",
)


@pytest.fixture(scope="module")
def result():
    return d.run()


def corrupt(result, case):
    broken = copy.deepcopy(result)
    detail = next(r for r in broken["all_twenty_actions"] if "matrices" in r)
    if case == 0:
        broken["lattice"]["gram_determinant"] = 2
    elif case == 1:
        broken["marked_isomorphism"]["all_product_checks"] = 1
    elif case == 2:
        broken["all_twenty_actions"][0]["root_space_fixed_dimensions"]["L"] = 6
    elif case == 3:
        detail["matrices"]["U"][0][0] += 1
    elif case == 4:
        detail["E6_root_cycles"]["L"] = {1: 72}
    elif case == 5:
        broken["unit_conjugation_covariance_checks"] = 2399
    elif case == 6:
        broken["SU3_order_three_representative"][0][0] = 1
    elif case == 7:
        broken["source_receipts"][0]["sha256"] = "bad"
    else:
        raise ValueError("unknown mutation")
    return broken


@pytest.mark.parametrize("case,name", list(enumerate(NAMES)))
def test_actual_dispatch_accepts_true_and_rejects_false(case, name, result):
    assert name in delegation.LOCKS
    delegation.test_original_mathematical_lock_with_exact_domain(name, result)
    with pytest.raises(AssertionError):
        delegation.test_original_mathematical_lock_with_exact_domain(name, corrupt(result, case))
