"""B1123 lock -- the forcedness census: 39 of 43 links forced, C6..C17 axiom-free,
regenerated from docs/THEOREM_LEDGER.md by a checker that FAILS on drift (non-vacuous)."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts/checks/forcedness_census.py"


def test_census_holds_on_current_ledger():
    p = subprocess.run([sys.executable, str(CHECKER)], capture_output=True, text=True,
                       cwd=str(ROOT), timeout=60)
    assert p.returncode == 0, p.stdout + p.stderr
    assert "FORCED (non-axiom): 39 of 43" in p.stdout
    assert "axioms in C6..C17 (the knot -> the algebra): NONE" in p.stdout
    assert "PASS" in p.stdout


def test_checker_fails_on_drift(tmp_path):
    """MB12 vacuity: relabelling an in-stretch THEOREM to AXIOM must be caught."""
    led = (ROOT / "docs/THEOREM_LEDGER.md").read_text(encoding="utf-8")
    mut = re.sub(r'(\*\*C1[0-7] \[)THEOREM', r'\1AXIOM', led, count=1)
    assert mut != led, "test setup: expected an in-stretch THEOREM link to flip"
    d = tmp_path / "ledger_drift.md"
    d.write_text(mut, encoding="utf-8")
    p = subprocess.run([sys.executable, str(CHECKER), str(d)], capture_output=True,
                       text=True, cwd=str(ROOT), timeout=60)
    assert p.returncode == 1
    assert "AXIOM-FREE STRETCH BROKEN" in p.stdout


def test_checker_fails_on_unparseable(tmp_path):
    bad = tmp_path / "not_a_ledger.md"
    bad.write_text("# no C-links here\n", encoding="utf-8")
    p = subprocess.run([sys.executable, str(CHECKER), str(bad)], capture_output=True,
                       text=True, cwd=str(ROOT), timeout=60)
    assert p.returncode == 1 and "FAIL" in p.stdout
