"""B1218 -- the open-claim sweep must keep its bite, in both directions.

MB12: an instrument that can only fire is worth nothing. These lock BOTH halves --
it finds the known locks, AND it stays silent on text the corpus never discussed.
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "checks" / "open_claim_sweep.py"


def _selftest():
    return subprocess.run([sys.executable, str(SCRIPT), "--selftest"],
                          capture_output=True, text=True, cwd=str(ROOT))


def test_bite_control_passes_both_directions():
    r = _selftest()
    assert r.returncode == 0, r.stdout + r.stderr
    assert "positive 5/5" in r.stdout, r.stdout
    assert "negative PASS" in r.stdout, r.stdout


def test_negative_control_can_actually_fail():
    """The MB12 check on the check: the nonsense control must score ~0, not merely
    'below bar'. A control that passes because the bar is loose is decorative."""
    r = _selftest()
    line = [l for l in r.stdout.splitlines() if "off-corpus text" in l][0]
    score = float(line.split("=")[1].split("(")[0].strip())
    assert score < 1.0, f"negative control scored {score}; bar is doing the work, not the instrument"


def test_self_exclusion_is_present():
    """The instrument must exclude its own arc -- it quotes every lock it reports."""
    src = SCRIPT.read_text(encoding="utf-8")
    assert 'SELF = "B1218_open_claim_sweep"' in src
    assert "if name == SELF:" in src


def test_tautology_exclusion_is_present():
    """VERDICT_LEDGER is a generated index OF arcs; including it measures nothing."""
    src = SCRIPT.read_text(encoding="utf-8")
    assert "VERDICT_LEDGER" in src and "not in p.name" in src
