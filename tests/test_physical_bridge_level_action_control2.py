"""R69 separately sealed normalization controls; originals retained."""
import importlib.util
from pathlib import Path

import pytest

PATH = Path(__file__).resolve().parents[1]/"reports/physical_bridge_2026_09_05/level_action_control2.py"
SPEC = importlib.util.spec_from_file_location("level_action_control2_r69", PATH)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)


def test_exact_descended_candidates_and_split_control():
    result = C.exact_controls()
    assert all(v for n,v in result["checks"].items() if "candidate_index" in n or "split_control" in n)
    assert result["checks"]["nonsplit_cocycle"]
    assert result["checks"]["cochain_dimension"]


def test_actual_induction_and_distinct_pullback_populations():
    result = C.exact_controls()
    assert all(v for n,v in result["checks"].items() if "level_counts" in n or "root_index" in n or "doublet_pullback" in n)
    assert all(row["coefficient_rank"] == 6 for row in result["rows"].values())


def test_peripheral_holonomy_not_filled_meridian():
    result = C.exact_controls()
    assert result["checks"]["last_generator"]
    assert all(v for n,v in result["checks"].items() if "peripheral_cube" in n or "unipotent_meridian" in n)


def test_independent_Fox_and_rational_rank_controls():
    result = C.exact_controls()
    assert all(v for n,v in result["checks"].items() if "Fox_affine" in n)
    assert result["checks"]["cocycle_relations"] and result["checks"]["exponent_relations"]


def test_distinct_deck_characters_are_not_one_tensor_vacuum():
    result = C.exact_controls()
    assert result["checks"]["three_distinct_extension_characters"]
    assert result["checks"]["order_four_ratio"]


def test_received_selected_candidate_is_the_exact_fixture():
    assert all(C.source_controls()["checks"].values())


def test_actual_sheetwise_products_metric_and_nonzero_cubic():
    result = C.action_controls()
    assert all(result["checks"].values())
    assert (result["sheet_algebra_dimension"],result["enlarged_algebra_dimension"]) == (12,36)
    assert result["nonzero_cubic"] != 0


def test_all_scoped_controls_and_invalid_population():
    result = C.run()
    assert set(result["groups"]) == {"exact","source","action","normalization","equality"}
    assert len(result["checks"]) == 46
    assert result["all_checks_pass"]
    with pytest.raises(ValueError):
        C.cover(7)
