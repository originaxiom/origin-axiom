"""B1255 — the generation index: right Galois type, wrong commutator.

Pins the ARITHMETIC tier (runs anywhere) and the register consequence. The object
tier needs B923's step-1 invariants cache and is exercised on-bench, not in CI.
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1255_generation_type"
SCRIPT = ARC / "verification" / "generation_type.py"


def test_the_script_runs_and_selftests():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    assert "SELFTEST: PASS" in r.stdout, r.stdout[-500:]


def test_both_cubics_are_totally_real_S3_in_the_sqrt77_family():
    """The load-bearing arithmetic: the RIGHT type, which Q(sqrt-3) cannot supply."""
    sys.path.insert(0, str(SCRIPT.parent))
    import generation_type as G
    for coeffs in (G.MU13, G.HIER_COEFFS):
        irred, kern, grp, nreal, _ = G.cubic_type(coeffs)
        assert irred and kern == [7, 11] and grp == "S3" and nreal == 3


def test_the_S3_verdict_can_fail():
    """MB12: a cyclic cubic must type as C3, or the test is a tautology."""
    sys.path.insert(0, str(SCRIPT.parent))
    import generation_type as G
    assert G.cubic_type([1, -3, 0, 1])[2] == "C3"


def test_the_dimension_count_that_closes_the_single_27_route():
    """27 = 16+10+1 carries the 16 with multiplicity one; 3 copies need 48 > 27."""
    assert 16 + 10 + 1 == 27 and 3 * 16 > 27


def _ledger_rows():
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    return [l for l in led.splitlines() if re.match(r"\|\s*I-\d+\s*\|", l)]


def test_I24_is_registered_REFUTED_and_did_not_enter_the_unearned_set():
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    row = next(l for l in led.splitlines() if l.startswith("| I-24 |"))
    assert "**REFUTED**" in row, row[:200]
    assert "B1255" in row
    b = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8"))
    # THE INVARIANT, not a snapshot: a REFUTED row must never appear as a ratchet RAISE
    # and must never sit in the UNEARNED set. Pinning the literal count here would go red
    # on any unrelated later raise (it did, at B1256's I-25) and teach the wrong lesson.
    assert "I-24" not in b["rows"], "I-24 is REFUTED; it must not be in the unearned set"
    for r in b["_baseline_raises"]:
        assert r.get("row") != "I-24", "a REFUTED row must not be recorded as a raise"
    assert b["total_rows"] == len(_ledger_rows())
