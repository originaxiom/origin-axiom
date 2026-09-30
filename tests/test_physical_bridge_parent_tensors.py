"""R59 parent/tensor admission; not a physical spectrum certificate."""
import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/parent_tensors.py'
spec = importlib.util.spec_from_file_location('parent_tensors_r59', path)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


def test_complete_instrument():
    result = p.run()
    assert result['passed'] == 18


def test_branching_needs_duality_and_Cartans():
    assert p.actual() == p.branching()
    assert sum(p.branching(True).values()) == 248
    assert p.branching(True) != p.actual()


def test_up_tensor_matches_every_root_triple():
    result = p.cubic_support()['up']
    assert result['exact_support'] and result['nonzero_bracket']
    assert result['actual_count'] == 300
    assert result['compared'] == 61250


def test_down_tensor_matches_every_root_triple():
    result = p.cubic_support()['down']
    assert result['exact_support'] and result['nonzero_bracket']
    assert result['actual_count'] == 300
    assert result['compared'] == 61250


def test_allowed_and_forbidden_are_not_dimension_tests():
    assert p.up_tensor(((0, 1), 0), ((2, 3), 1), (4, (0, 1))) == 1
    assert p.up_tensor(((0, 1), 0), ((2, 3), 1), (4, (0, 2))) == 0
    assert p.down_tensor(((0, 1), 0), (0, (1, 2)), (1, (3, 4))) == 1
    assert p.down_tensor(((0, 1), 0), (0, (1, 2)), (1, (2, 4))) == 0


def test_actual_Higgs_slots_are_not_claimed_modes():
    assert p.charged_fibre((0, 0, 1, 3)) == p.dual(p.exterior(2))
    assert p.charged_fibre((0, 0, 1, -3)) == p.exterior(2)


def test_tensor_exchange_with_internal_form_wedge():
    args = (((0, 1), 0), ((2, 3), 1), (4, (0, 1)))
    value = p.up_tensor(*args)
    exchanged = p.up_tensor(args[1], args[0], args[2])
    assert value == -exchanged != 0
    assert value == (-1) * exchanged  # swap two internal one-forms too
