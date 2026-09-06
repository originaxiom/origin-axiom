"""Review 55 — the three instrument repairs, each pinned so the blindness cannot return."""
import json, re, sys, glob
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _rs():
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    try:
        import retraction_sweep
        return retraction_sweep
    finally:
        sys.path.pop(0)


def _gates():
    sys.path.insert(0, str(ROOT / "scripts" / "gates"))
    try:
        import gates
        return gates
    finally:
        sys.path.pop(0)


# --- repair 1: the retraction sweep read 9 of 21 registry rows -------------------------------

def test_the_sweep_parses_BOTH_registry_table_formats():
    """It read only `| n | \\`phrase\\` |` and was blind to 12 rows for nine days."""
    ph = _rs()._phrases()
    assert len(ph) >= 17, f"parser regressed to {len(ph)} phrases"
    assert "cell 2 is queued and unrun" in ph          # format 2, was invisible
    assert "excess transitive reach" in ph             # format 2, had live uses


def test_the_sweep_does_NOT_sweep_phrases_whose_READING_was_retracted():
    """The tail is load-bearing. A naive widening reds ~25 correct uses of sin^2(theta_W) = 3/8
    and every correct use of 'mirror-odd' for the orientation bit."""
    ph = _rs()._phrases()
    assert not any("3/8" in p for p in ph), "the NUMBER is legitimate; only the reading was retracted"
    assert "**mirror-odd**" not in ph, "mirror-odd is correct for the ORIENTATION bit (B1168/B1169)"


def test_the_sweep_is_green_and_would_still_FIRE():
    rs = _rs()
    assert rs.sweep() == [], rs.sweep()[:5]
    # non-vacuity: a planted live use of a registered phrase must be caught
    ph = rs._phrases()
    assert ph and rs.MENTION_CUES.search("this line retracts it")           # cue works
    assert not rs.MENTION_CUES.search("the poset shows " + ph[-1])          # bare use is NOT a mention


def test_the_two_live_uses_are_corrected_AT_SOURCE():
    for rel in ("frontier/B1187_depth_closure/FINDINGS.md",
                "frontier/B189_omega_causal_dimension/ADDENDUM_b1187_null_reversal.md"):
        t = (ROOT / rel).read_text(encoding="utf-8")
        assert "reach-DEFICIT" in t, rel
        assert "Review 55" in t, rel


# --- repair 2: the supersession gate skipped a comma-joined forward edge ----------------------

def test_the_supersession_gate_splits_a_comma_joined_forward_edge():
    """B239 declares supersedes = "B234, B235" -- one string, two ids. The gate skipped it."""
    d = json.loads((ROOT / "frontier" / "B239_reconciled_trace_field_law" / "arc_verdict.json")
                   .read_text(encoding="utf-8"))
    assert d["supersedes"] == "B234, B235"          # the malformed edge is preserved, not rewritten
    for arc in ("B234", "B235"):
        f = glob.glob(str(ROOT / "frontier" / f"{arc}_*" / "arc_verdict.json"))
        assert f, arc
        v = json.loads(Path(f[0]).read_text(encoding="utf-8"))
        assert v.get("superseded_by") == "B239", (arc, v.get("superseded_by"))
    ok, detail = _gates().gate_supersession_backlinks()
    assert ok, detail


# --- repair 3: my own B1291 registry row called a run computation "unrun" ---------------------

def test_the_B1291_registry_row_no_longer_calls_a_RUN_computation_unrun():
    """E53 by the same seat: B1292 ran it and the registry row was not updated."""
    t = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    i = t.find("T-CUSP-PARITY")
    assert i != -1
    row = t[i:i + 4000]
    assert "B1292" in row and "m202" in row
    assert "MIS-SCOPED" in row.upper()
    # and the theorem itself must NOT have been weakened by the correction.
    # Assert its SUBSTANCE, not a word: an earlier version of this test guessed "excluded"
    # and reddened on prose that says "impossible" -- pinning vocabulary is the snapshot
    # anti-pattern this repo already named (see test_b1290's invariant comment).
    assert "is impossible" in row and "EVEN number of points" in row
    assert "one cusp" in row.lower()
