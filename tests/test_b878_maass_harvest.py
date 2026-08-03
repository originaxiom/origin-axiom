"""Locks B878 -- the cc3 Wave-1 Maass harvest."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B878_maass_upper_window"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_the_claim_arithmetic_closes():
    assert RES["claims_check"] == {"claim_43": True, "claim_72": True,
                                   "stability_26_26": True}
    assert RES["combined_distinct"] == 43 and RES["combined_mult"] == 72
    assert (RES["lower_distinct"], RES["lower_mult"]) == (17, 27)
    assert (RES["upper_distinct"], RES["upper_mult"]) == (26, 45)


def test_all_four_parents_present():
    assert RES["parents_all_present"] is True


def test_the_two_flagged_entries_are_in_the_data():
    assert len(RES["noted_entries"]) == 2
    assert any("restored" in n for n in RES["noted_entries"])


def test_provenance_and_the_never_merge_rule():
    assert "never merged" in RES["provenance"]
    assert "integrate-don't-merge" in _F
    assert (_D / "RELAY_AS_RECEIVED.md").exists()
    for f in ("branch_scanE_refined.json", "branch_hejhal_m004.py",
              "branch_cell9_rung1_v2.py", "branch_FINDINGS.md"):
        assert (_D / f).exists() and (_D / f).stat().st_size > 0


def test_honest_boundaries():
    assert "the arb certification of the 26 upper values is the branch's" in _F
    assert "no completeness claim for the 43" in _F
    assert "not a re-run of the certification" in _F
