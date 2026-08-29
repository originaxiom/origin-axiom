"""B1211 — the declaration gap. The registry gate reads a field the seat fills in; these are the
counter-checks on the declaration itself.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1211_declaration_gap"
REGISTRY = ROOT / "docs" / "THEOREM_REGISTRY.md"
BAND = 1180          # forward-only, per the lane-0 rule: history is never flipped

THEOREM_WORDS = [r"\bTHE [A-Z][A-Z' -]{4,40}THEOREM\b", r"\bTHEOREM\b", r"\bwe prove\b",
                 r"\bPROVED (?:EXACTLY|ALL-|IN GENERAL)", r"\bis a THEOREM\b",
                 r"\bIMPOSSIBLE\b", r"\bCANNOT (?:BE|EXIST)", r"\bEXHAUSTIVE\b", r"\bUNIQUE\b"]
DISOWN = [r"not a theorem", r"an interpretation joining", r"process arc", r"no mathematics",
          r"bookkeep", r"NOT PROVED"]


def _arcs():
    for p in ROOT.glob("frontier/*/arc_verdict.json"):
        try: v = json.loads(p.read_text(encoding="utf-8"))
        except Exception: continue
        if isinstance(v.get("id"), str): yield v


def test_the_six_corrected_arcs_declare_and_register():
    """The repair itself: each flipped arc declares creates_law and has its registry row."""
    reg = REGISTRY.read_text(encoding="utf-8")
    for a in ("B1182", "B1183", "B1184", "B1192", "B1196", "B1200"):
        v = next(x for x in _arcs() if x["id"] == a)
        assert v["creates_law"] is True, a
        assert "creates_law_corrected" in v, f"{a}: the correction must be dated, not silent"
        assert v["creates_law_corrected"]["was"] is False
        assert a in reg, f"{a} declares creates_law but has no registry row"


def test_b1203_stays_false_as_the_control():
    """A review that flipped everything it looked at would be a sweep, not a judgement. B1203
    disowns theorem status in its own words and must keep its declaration."""
    v = next(x for x in _arcs() if x["id"] == "B1203")
    assert v["creates_law"] is False
    assert "creates_law_reviewed" in v, "the arc must record that it WAS reviewed and kept"


def test_no_undeclared_theorem_in_the_current_band():
    """THE COUNTER-CHECK the registry gate cannot perform. gate_theorem_registry catches
    OVER-declaration (declared true, no row). This catches UNDER-declaration: an arc whose claim
    talks like a theorem while its flag says otherwise. Forward-only from B1180 — history is never
    flipped, and the older band is recorded in the arc's results instead."""
    bad = []
    for v in _arcs():
        n = int(re.match(r"B(\d+)", v["id"]).group(1) or 0)
        if n < BAND or v.get("verdict") not in ("PROVED", "NEGATIVE"): continue
        if v.get("creates_law") is True or v.get("instrument"): continue
        # A recorded, dated decision to keep the flag false is a valid disposition. What this lock
        # forbids is SILENCE -- an arc that talks like a theorem and never says why it is not one.
        if v.get("creates_law_reviewed"): continue
        c = v.get("claim_one_line", "")
        if any(re.search(d, c[:400], re.I) for d in DISOWN): continue
        if sum(1 for w in THEOREM_WORDS if re.search(w, c)) >= 2:
            bad.append(v["id"])
    assert not bad, (f"arcs in the current band talking like theorems while declaring otherwise: "
                     f"{bad} -- declare and register them, or state the self-limit in the claim")


def test_the_detectors_own_scope_correction_is_recorded():
    """The instrument's first pass lost B1183 -- THE ONE-CLASS THEOREM -- because the arc FENCES a
    borrowed computation with 'cited, not re-run', which a global disown-list read as a disclaimer.
    Third scope failure of the same species in one session; recorded so the pattern is nameable."""
    r = json.loads((ARC / "b1211_results.json").read_text(encoding="utf-8"))
    sc = r["instrument_corrections"]
    assert sc["first_pass_lost"], "the false negatives must be named"
    assert "B1183" in sc["first_pass_lost"]
    assert "headline" in sc["fix"].lower()


def test_the_registration_gap_that_motivated_the_arc_is_recorded():
    r = json.loads((ARC / "b1211_results.json").read_text(encoding="utf-8"))
    g = r["registration_gap"]
    assert g["observer_arcs_on_no_registered_surface"] >= 7
    assert g["registry_last_row_before"] == "B1145"
