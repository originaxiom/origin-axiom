"""B1219 -- the reverse sweep must keep its bite AND reproduce across processes.

Two properties, both of which failed at some point during this arc's construction:
  (1) planted bite controls, in both directions;
  (2) DETERMINISM across separate processes -- the first version returned 45 and 46 on
      identical input, because a top-N truncation over a set is PYTHONHASHSEED-dependent.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "checks" / "reverse_sweep.py"


def _run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args],
                          capture_output=True, text=True, cwd=str(ROOT))


def test_planted_controls_pass_both_directions():
    r = _run("--selftest")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CONTROLS PASS" in r.stdout, r.stdout


def test_planted_off_surface_target_actually_flags():
    """MB12: the instrument must be able to FIRE. A control that only ever clears is decorative."""
    out = _run("--selftest").stdout
    a = float(re.search(r"PLANT A.*cover=([0-9.]+)", out).group(1))
    b = float(re.search(r"PLANT B.*cover=([0-9.]+)", out).group(1))
    assert a < 0.55 <= b, f"controls do not separate: A={a} B={b}"


def test_deterministic_across_processes():
    """The defect this lock exists for: separate processes must agree exactly."""
    lines = {_run().stdout.splitlines()[1] for _ in range(3)}
    assert len(lines) == 1, f"non-deterministic across processes: {lines}"


def test_tautology_and_self_exclusions_present():
    """Generated per-arc indexes are not surfaces; the arc must not surface itself."""
    src = SCRIPT.read_text(encoding="utf-8")
    assert "_GENERATED" in src and "VERDICT_LEDGER" in src
    assert 'SELF = "B1219"' in src and "m.group(1) == SELF" in src
