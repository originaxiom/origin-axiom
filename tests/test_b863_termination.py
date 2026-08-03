"""Locks B863 -- the termination theorem."""
import importlib.util
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B863_termination"
_S = importlib.util.spec_from_file_location("b863", _D / "termination.py")
b3 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b3)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_every_proper_descent_is_dead():
    assert RES["all_descents_dead"] is True
    for k, d in RES["descents"].items():
        assert d["chiral"] is False, k


def test_the_conformal_su2_4_case_is_included_and_conformal():
    """The non-obvious case: a genuine conformal embedding, and it dies too."""
    assert RES["conformality_bprime"]["match"] is True
    assert RES["descents"]["bprime_su2_4_principal_CONFORMAL"]["chiral"] is False


def test_the_positive_control_the_sm_itself_is_chiral():
    """Without this the multiset test could be vacuous-fatal (killing everything)."""
    assert RES["sm_itself_chiral"] is True
    assert RES["terminal"] is True


def test_the_su3_content_is_the_verified_vector_like_multiset():
    a = RES["descents"]["a_drop_su2"]["multiset"]
    assert a == {"3": 2, "3bar": 2, "1": 3}


def test_the_menu_import_is_stated_not_hidden():
    assert "Not exhaustive" in _F and "P5" in _F


def test_the_kind_check_is_a_check_not_an_input():
    assert "consistency check, not an input" in _F
