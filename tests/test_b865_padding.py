"""Locks B865 -- the padding lemma and the full-27 rerun."""
import importlib.util
import json
from collections import Counter
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B865_padding_lemma"
_S = importlib.util.spec_from_file_location("b865", _D / "padding.py")
b5 = importlib.util.module_from_spec(_S)
_S.loader.exec_module(b5)
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_the_lemma_verifies_on_random_multisets():
    assert RES["padding_lemma_verified"] is True
    assert b5.padding_lemma_verify(trials=500, seed=123) is True


def test_the_lemma_direction_that_could_fail():
    """Non-vacuity: padding with NON-self-conjugate content CAN flip a verdict."""
    m = Counter({"(3,2)": 1})                       # chiral
    bad_pad = Counter({"(3bar,2)": 1})              # NOT self-conjugate
    assert b5.chiral(m) is True
    assert b5.chiral(m + bad_pad) is False, "the conjugate pad kills chirality -- the test bites"


def test_full27_rerun_preserves_every_verdict():
    assert RES["verdicts_unchanged"] is True
    f = RES["full27"]
    assert f["step2_SU5xU1"]["chiral"] is True
    assert f["step2_PatiSalam"]["chiral"] is True
    assert f["step3_SM"]["chiral"] is True
    assert f["step3_SU4xU1"]["chiral"] is False


def test_the_singlet_counts_are_not_collapsed():
    """The first-draft defect: duplicate dict keys silently collapsing counts."""
    sm = RES["full27"]["step3_SM"]["multiset"]
    assert sm.get("(1,1)") == 4, sm      # 1 from the generation + 3 descended singlets
    assert sm.get("(1,2)") == 3, sm      # 1 from the generation + 2 from the 5+5bar
    src = (_D / "padding.py").read_text(encoding="utf-8")
    assert "DUPLICATE KEYS" in src, "the defect must stay documented where the fix lives"


def test_the_singlets_fate_is_recorded():
    assert "anomaly ballast" in _F
    assert "right-handed-neutrino slot" in _F


def test_scope_what_it_does_not_derive():
    # markdown bold splits the phrase ("does **not** derive"); strip asterisks before matching
    assert "does not derive" in _F.lower().replace("*", "")
