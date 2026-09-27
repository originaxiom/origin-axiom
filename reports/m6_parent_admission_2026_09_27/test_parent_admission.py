import importlib.util
from pathlib import Path
import pytest

spec = importlib.util.spec_from_file_location("m6_parent_admission",
    Path(__file__).with_name("verify_parent_admission.py"))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def test_entire_prespecified_instrument():
    v.run()


def test_full_characters_not_just_dimension():
    actual = v.actual_branching()
    wrong = v.expected_branching(wrong_conjugation=True)
    assert sum(actual.values()) == sum(wrong.values()) == 248
    assert actual != wrong
    assert actual != v.actual_branching(include_cartan=False)


@pytest.mark.parametrize("name", list(v.SECTOR_LABELS))
def test_charged_bundle_and_its_dual(name):
    actual = v.actual_branching()
    label = v.SECTOR_LABELS[name]
    expect = v.exterior(1 if name in ("Q","u","e") else 2)
    assert v.fibre(actual,label) == expect
    assert v.fibre(actual,tuple(-x for x in label)) == v.dual(expect)


@pytest.mark.parametrize("name", ["Q","u","e","d","L","nu"])
def test_actual_pairing_obstruction_survives_relabeling(name):
    profiles,n = v.character_profiles()
    rows = profiles[name]
    assert v.oriented_grid_count(rows,n) == 0
    assert v.oriented_grid_count(list(reversed(rows)),n) == 0
    shifted = [tuple((x+11*(i+1)) % n for i,x in enumerate(r)) for r in rows]
    sheared = [tuple([r[0],(r[1]+r[2]) % n]+list(r[2:])) for r in rows]
    assert v.oriented_grid_count(shifted,n) == 0
    assert v.oriented_grid_count(sheared,n) == 0


def test_nontrivial_tensor_control_passes_under_same_changes():
    rows,n = v.synthetic_grid(),120
    count = v.oriented_grid_count(rows,n)
    assert count > 0
    assert v.oriented_grid_count(rows[2:]+rows[:2],n) == count
    shifted = [tuple((x+11*(i+1)) % n for i,x in enumerate(r)) for r in rows]
    sheared = [tuple([r[0],(r[1]+r[2]) % n]+list(r[2:])) for r in rows]
    assert v.oriented_grid_count(shifted,n) == count
    assert v.oriented_grid_count(sheared,n) == count


def test_rank_is_not_a_zero_mode_count():
    # Multiplying a list of fibre weights by one formal line preserves its length.
    for k in (1,2):
        weights = list(v.exterior(k).elements())
        shifted = [(w, 7) for w in weights]
        assert len(shifted) == (5 if k == 1 else 10)
    # No assertion bounds global cohomology dimension by these fibre ranks.
