"""Locks B874 -- the measurement ladder."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B874_measurement_ladder"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_census_is_a_two_value_cliff():
    c = RES["census"]
    assert len(c) == 15
    soft = {"x8", "x16", "x8+x16"}
    for k, v in c.items():
        assert v == (30 if k in soft else 12), (k, v)


def test_the_ladder_values():
    assert RES["ladder"] == [30, 12]


def test_cent_c_structure():
    assert RES["cent_dim"] == 12 and RES["closure_ok"] is True
    assert RES["derived_dim"] == 8 and RES["center_dim"] == 4


def test_derived_is_a2_su21_by_nondegenerate_killing_and_signature():
    assert RES["killing_rank"] == 8
    assert RES["killing_signature"] == [4, 4, 4]
    assert RES["derived_type"].startswith("A2")
    assert "su(2,1)" in RES["derived_real_form"]


def test_full_measurement_is_not_the_sm_stated_plainly():
    assert RES["full_measurement_is_sm"] is False
    assert 'the "full measurement = sm" reading is dead' in _F


def test_no_dictionary_asserted_and_step2_question_stays_open():
    assert "no dictionary to color is asserted" in _F
    assert "remains open" in _F


JOINT = json.loads((_D / "joint_results.json").read_text(encoding="utf-8"))


def test_addendum_enhancement_confirmed_at_13x_roots():
    """kern(s1) = 46 at every 13x-scaled banked root -- the normalization fact
    reconfirmed at the source."""
    assert JOINT["enhancement_confirmed_at_13x"] is True
    assert all(r["kern_s1"] == 46 for r in JOINT["rows"]) and len(JOINT["rows"]) == 3


def test_addendum_no_26_stratum_step2_not_retired():
    assert JOINT["no_26_stratum"] is True
    assert all(r["joint_x14"] == 12 and r["joint_x22"] == 12 for r in JOINT["rows"])
    assert "closes negatively for the object's 2t-charge system" in _F
    assert "the ranking is not retired by charge measurement" in _F
