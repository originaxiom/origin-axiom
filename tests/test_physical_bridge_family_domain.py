"""All eight sealed R11 mathematical locks, with a separate domain adapter."""
import importlib.util
from pathlib import Path

import pytest
import sympy as sp

from reports.physical_bridge_2026_09_05 import family_action as f
from reports.physical_bridge_2026_09_05 import family_action_domain as d

spec = importlib.util.spec_from_file_location("r11_sealed_locks", Path(__file__).with_name("test_physical_bridge_family_action.py"))
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)
LOCKS = sorted(name for name in vars(original) if name.startswith("test_"))


def original_lock_passes(name, answer):
    """Run the unchanged sealed assertion body and expose a fallible predicate.

    Only a failed assertion becomes False. Missing locks, bad keys and other
    execution errors still propagate instead of being reported as a pass.
    """
    try:
        getattr(original, name)(answer)
    except AssertionError:
        return False
    return True


@pytest.fixture(scope="module")
def result():
    before = f.integerize
    answer = d.run()
    assert f.integerize is before and len(LOCKS) == 8
    return answer


@pytest.mark.parametrize("name", LOCKS)
def test_original_mathematical_lock_with_exact_domain(name, result):
    assert original_lock_passes(name, result), name


@pytest.mark.parametrize("name,section,key,value", [
    ("test_lattice_integrality_and_a_corrupt_root_are_checked",
     "lattice", "denominator", 2),
    ("test_marked_map_verifies_all_products_and_rejects_bad_assignment",
     "marked_isomorphism", "all_product_checks", 0),
])
def test_delegated_sealed_lock_rejects_changed_computed_result(name, section, key, value, result):
    changed = dict(result)
    changed[section] = dict(result[section])
    changed[section][key] = value
    assert not original_lock_passes(name, changed)


def test_domain_conversion_preserves_exact_entries():
    matrix = sp.Matrix([[sp.Rational(1, 4), sp.Rational(-3, 4)]])
    converted, den = d.integerize(matrix)
    assert den == 4 and converted == sp.Matrix([[1, -3]])
    assert converted.to_DM().domain == sp.ZZ


def test_domain_adapter_still_rejects_truncation():
    with pytest.raises(ValueError, match="truncation forbidden"):
        d.integerize(sp.Matrix([[sp.Rational(1, 4)]]), 2)


def test_context_restores_original_binding_on_failure():
    before = f.integerize
    with pytest.raises(RuntimeError, match="planted"):
        with d.exact_domain():
            assert f.integerize is d.integerize
            raise RuntimeError("planted")
    assert f.integerize is before
