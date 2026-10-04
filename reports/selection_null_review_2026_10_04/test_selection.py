import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("selection_contract", Path(__file__).with_name("verify_selection.py"))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_independent_positive_control():
    assert v.independent_control()["actual_union"] == "19/100"


def test_valid_dependent_null_can_cross_threshold():
    assert v.dependent_control()["decision_can_differ"]


def test_scan_needs_sampling_law():
    assert v.finite_scan_control()["without_replacement"] == "2/5"


def test_union_bound_exhaustive():
    assert v.arbitrary_dependence_bound()["pairs_checked"] == 1024
