"""B1247 — the proxies replaced by reporters, and E58 gains its time-indexed clause."""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "scripts" / "checks" / "coverage_candidates.py"

def _run(*a):
    return subprocess.run([sys.executable, str(TOOL), *a], capture_output=True, text=True,
                          cwd=str(ROOT), env={"OA_ROOT": str(ROOT), "PATH": "/usr/bin:/bin"})

def test_the_reporter_selftests_both_directions():
    r = _run("--selftest")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "controls pass" in r.stdout

def test_it_RUNS_on_the_live_corpus_and_separates_the_queue_from_the_periphery():
    r = _run("--unrepresented")
    assert r.returncode == 0, r.stdout + r.stderr
    m = re.search(r"the real queue: (\d+)", r.stdout)
    assert m, r.stdout
    queue = int(m.group(1))
    total = int(re.search(r"UNREPRESENTED \(no synthesis surface\): (\d+)", r.stdout).group(1))
    # the whole point: in-degree separates load-bearing from peripheral
    assert queue < total / 5, f"the queue ({queue}) should be a small fraction of {total}"

def test_the_chain_gap_direction_runs_and_refuses_to_be_a_defect_list():
    r = _run("--chain-gap")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "NOT a defect list" in r.stdout, "the reporter must state that absence is the normal case"
    assert "CHAIN_COVERAGE.json" in r.stdout, "it must name where a promotion gets pinned"

def test_the_rejected_alternative_is_recorded_not_silently_dropped():
    """in-degree as a SCREEN was tried and failed; the docstring must say so."""
    src = TOOL.read_text(encoding="utf-8")
    assert "rejected" in src.lower() and "in-degree 1-2" in src, \
        "the failed design must be recorded in the instrument, per the B1240/B1243 practice"

def test_representation_sweep_declares_its_floor_a_gate_threshold():
    src = (ROOT / "scripts" / "checks" / "representation_sweep.py").read_text(encoding="utf-8")
    assert "NOT A MEASURE OF SUBSTANTIALITY" in src
    assert "coverage_candidates.py" in src, "it must point at what covers its blind spot"
    assert "CLAIM_FLOOR = 500" in src, "the floor is KEPT so the gate does not regress"

def test_chain_coverage_carries_a_criterion_not_just_a_list():
    cov = json.loads((ROOT / "docs" / "CHAIN_COVERAGE.json").read_text(encoding="utf-8"))
    assert "_criterion" in cov, "a hand-maintained pin list without a feeder is what R54-2 was about"
    assert "coverage_candidates.py" in cov["_criterion"]
    assert cov["must_appear_in_chain"], "the pins themselves must survive"

def test_E58_carries_the_time_indexed_clause():
    el = (ROOT / "docs" / "ERROR_LEDGER.md").read_text(encoding="utf-8")
    assert "A CLAIM ABOUT A FILE IS" in el and "TIME-INDEXED" in el
    assert "quote the SHA or timestamp you read" in el
    assert "neither party's error" in el, "the resolving case must be recorded"
    assert "E60" not in el, "filed as a clause, not a new class"
