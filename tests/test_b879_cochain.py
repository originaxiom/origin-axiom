"""Locks B879 -- the cc3 selection-cochain harvest."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B879_selection_cochain"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_v1_enumeration_exact():
    assert RES["V1_counts"] == [1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335]
    assert RES["V1_total"] == 745


def test_c1_collapse():
    assert RES["C1_unitdet_iff_tr3"] is True
    assert RES["C1_trace3_classes"] == ["LR"]


def test_c2_strata():
    assert RES["V4_amphichiral_count"] == 53
    assert RES["V4_prime_d_set"] == [5, 13, 17, 29, 37, 53, 173, 229]
    assert RES["V4_prime_d_amph_joint"] == 11


def test_c4_c5():
    assert RES["C4_entangled_amphichiral"] == [["LLRR", 2]]
    assert RES["C5_d5_count"] == 16 and RES["C5_includes_R4L4_tr18"] is True


def test_c3_corroboration_scope():
    assert RES["V3_value_counts"] == [188, 153, 249, 147, 8]
    assert RES["V3_sample_worst_dev"] < 1e-12
    assert abs(RES["V3_silver"][0] - 1.0) < 1e-9
    assert "not a new law, not a pointwise-formula verification" in _F


def test_c6_the_headline():
    assert RES["V2_matches_rerun"] is True
    assert RES["V2_primary"] == [2, 0, 0, 6] and RES["V2_alt"] == [5, 6, 10, 17]
    assert "one line" in RES["V2_nogo_lemma"]
    assert "structurally unreachable" in _F


def test_provenance_and_carried():
    assert (_D / "packet" / "HANDOFF_CC_SELECTION_COCHAIN.md").exists()
    assert "the addendum's self-downgrades are accurate" in _F
    assert "not silently applied tonight" in _F
