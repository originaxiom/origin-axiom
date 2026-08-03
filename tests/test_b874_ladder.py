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
