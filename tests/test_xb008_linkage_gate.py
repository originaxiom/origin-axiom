"""xB008 — the lock on the linkage-kill gate.

E82's standing rule is A KILL NEEDS THE SAME MAP A PROMOTION NEEDS. These assert the
MATHEMATICS OF THE INSTRUMENT (WORKING_RULES §7 — locks assert facts, not transcripts):
that it catches the error it was built from, clears that error's repair, clears the
record's own sound forms, and ratchets.
"""
import importlib.util
import json
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHECK = ROOT / "scripts" / "checks" / "linkage_kills.py"
BASELINE = ROOT / "docs" / "LINKAGE_BASELINE.json"


def _mod():
    spec = importlib.util.spec_from_file_location("_lk", CHECK)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


LK = _mod()


def test_the_error_it_was_built_from_is_caught():
    """THE cell. xB005's Q3 as it ORIGINALLY stood must be classed C. If this ever goes
    green the gate is theatre: it would not catch the single error it was designed from."""
    assert LK.adjudicate(LK.Q3_ORIGINAL)[1] == "C"


def test_the_repair_is_recognised():
    """...and the CORRECTED Q3 must NOT be C, or the gate cannot tell a defect from its fix
    and would punish the correction."""
    assert LK.adjudicate(LK.Q3_CORRECTED)[1] != "C"


def test_selftest_passes_both_directions():
    assert LK.selftest_quiet() == []


@pytest.mark.parametrize("blob,want", [
    (LK.PLANT_BAD, "C"),          # a planted E82 kill
    (LK.PLANT_OK_THM, "A"),       # a named theorem does the work
    (LK.PLANT_OK_RATE, "R"),      # a computed base rate: sound, different argument
])
def test_planted_controls(blob, want):
    assert LK.adjudicate(blob)[1] == want


def test_b727_the_records_own_sound_form_is_not_flagged():
    """B727 is the SOUND form of the same pattern ('forced by one ADE classification, so the
    recurrence is generic not evidence'). If the gate flags it, it is miscalibrated and
    xB006's S1 criterion is violated."""
    f = ROOT / "frontier" / "B727_base_rate_the_structure" / "FINDINGS.md"
    if not f.exists():
        pytest.skip("B727 absent")
    hits, k, _ = LK.adjudicate(f.read_text(encoding="utf-8", errors="replace"))
    assert hits, "B727 does not trip the lexicon at all -- too narrow"
    assert k != "C"


def test_lexicon_excludes_by_construction():
    """'by construction' is descriptive prose (B425's 'golden BY CONSTRUCTION'), was never in
    xB006's sealed lexicon, and drove 27 of an initial 46 candidates on its own. Its return
    would silently triple the false-positive rate."""
    assert not LK.LINKAGE.search("the torsion is golden BY CONSTRUCTION and therefore expected")


def test_baseline_is_frozen_and_adjudicated():
    d = json.loads(BASELINE.read_text(encoding="utf-8"))
    frozen = d["frozen"]
    adj = d["adjudication"]
    assert frozen and set(frozen) == set(adj), "every frozen entry must carry an adjudication"
    assert all(v.get("xB006_class") for v in adj.values())
    assert "A KILL NEEDS THE SAME MAP A PROMOTION NEEDS." in d["_standing_rule"]
    assert "REDUCES the class" in d["_recall"], "the bounded-recall statement must survive"


def test_the_tree_is_green_and_the_ratchet_ratchets():
    novel, hits, frozen = LK.check()
    assert not novel, f"the present tree reds: {novel}"
    assert set(frozen) == set(n for n, _ in hits), "baseline and scan disagree"
    # G5: a NEW unexhibited linkage kill must red.  Simulate by unfreezing one.
    real = LK.baseline
    try:
        LK.baseline = lambda: set(list(frozen)[1:])
        novel2, _, _ = LK.check()
        assert novel2, "removing an entry from the baseline did not red: no ratchet"
    finally:
        LK.baseline = real
    assert not LK.check()[0], "the ratchet did not restore"
