"""B1341 - already_banked must show a FINDINGS-surface hit's VERDICT, not just its heading.

The failure this locks out, measured on this bench: the sweep for the object's phase space returned
B448 as its TOP hit at 6 of 7 terms, and printed B448's FINDINGS heading -- "the heartbeat
adjudication: two handoffs, one exact orbit-field tower" -- which contains no matched term. B448's
claim_one_line says "the cusp locus kappa=-2 (the Markov surface)" in its FIRST SENTENCE. The reader
scanned the printed line and rediscovered a banked identification.

B1338 measured where the instrument is blind. This is the complementary defect: the instrument saw
it and did not SHOW it.
"""
import subprocess
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "checks" / "already_banked.py"


def _run(query):
    r = subprocess.run([sys.executable, str(SCRIPT), query], capture_output=True, text=True,
                       cwd=str(ROOT), timeout=600)
    return r.stdout


def test_the_exact_miss_is_now_visible():
    """the query that missed B448 must now print B448's Markov sentence."""
    out = _run("Markov surface trace map leaf phase space")
    assert "B448_heartbeat_adjudication" in out, "B448 must still be found"
    b448 = [ln for ln in out.splitlines() if "heartbeat adjudication" in ln]
    assert b448, "B448's row went missing"
    assert any("Markov surface" in ln for ln in b448), (
        "B448's row must carry its own 'the Markov surface' phrase, not only its heading")


def test_findings_rows_carry_a_verdict_marker():
    out = _run("Markov surface trace map leaf phase space")
    rows = [ln for ln in out.splitlines() if "heartbeat adjudication" in ln]
    assert all("VERDICT:" in ln for ln in rows), (
        "every FINDINGS-surface row inside an arc must print its claim_one_line")


def test_default_behaviour_is_unchanged():
    """B1202's reproduce.sh depends on the default surfaces; the fix must not widen the scan."""
    out = _run("kappa")
    assert "already-banked: terms" in out
    assert "--wide" not in out, "the wide surfaces must stay opt-in"
