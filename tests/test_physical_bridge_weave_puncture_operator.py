"""Local mathematical locks, not certification of a physical compactification."""
import importlib.util
from fractions import Fraction
from pathlib import Path

import pytest
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "reports/physical_bridge_2026_09_05/weave_puncture_operator_2026_10_08"


def load(name):
    spec = importlib.util.spec_from_file_location("weave_benchmark_"+name, PACKET/(name+".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def result():
    return load("probe").run()


def test_native_and_separate_reference_agree(result):
    reference = load("reference").run()
    for key in ("sheaf_indices", "pole_norms", "weyl_residual_squared"):
        assert result[key] == reference[key]
    assert all(result["facts"].values())
    assert all(reference["predicates"].values())


@pytest.mark.parametrize("d", range(7))
def test_every_local_coefficient_rank_and_sheaf_index(d):
    native = load("probe")
    p = sp.diag(*([1]*d+[0]*(6-d)))
    assert native.coefficient_domain(p) == {
        "plus_rank": d, "total_rank": 6, "green_zero": True, "grading_kept": True}
    assert native.sheaf_index(6, (Fraction(1, 2),)*6, d) == d-3


def test_wrong_degree_and_nonprojector_rejected():
    native = load("probe")
    with pytest.raises(ValueError):
        native.sheaf_index(1, (Fraction(1, 2),), 0)
    with pytest.raises(ValueError):
        native.coefficient_domain(sp.Matrix([[1, 1], [0, 0]]))


def test_norm_positive_and_negative_controls():
    native = load("probe")
    assert native.radial_class(Fraction(-1, 2), "one_form") == "finite"
    assert native.radial_class(Fraction(-1, 2), "cusp_spin") == "divergent"
    assert native.radial_class(Fraction(1, 2), "cusp_spin") == "finite"


def test_no_automatic_physical_or_global_pde_promotion(result):
    assert not result["hodge_triplet_refuted"]
    assert not result["physical_chiral_SM_derived"]
    assert not result["finite_distance_global_graph_index_certified"]
    assert not result["generated_action_or_domain_selected"]
