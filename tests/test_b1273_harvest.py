"""B1273 — the seat harvest: codex R037's central twist reproduced on main's data."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1273_seat_harvest" / "verification" / "harvest.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import harvest as H
    return H


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_centre_is_C2_as_codex_reports():
    H = _mod()
    assert len(H.centre()) == 2


def test_the_central_twist_swaps_the_two_classes_completely():
    """codex R037: the nonextendable class is the unique central H^1 twist of the extendable."""
    H = _mod()
    S, lab, k = H.orbits()
    minus = [z for z in H.centre() if z != H.I][0]
    moved = sum(1 for (A, B) in S if lab[(H.mul(A, minus), H.mul(B, minus))] != lab[(A, B)])
    assert moved == len(S) == 48


def test_twisting_one_generator_is_not_a_homomorphism():
    """The error that was caught: the character must negate BOTH meridians."""
    H = _mod()
    S, lab, _ = H.orbits()
    minus = [z for z in H.centre() if z != H.I][0]
    valid = sum(1 for (A, B) in S if (H.mul(A, minus), B) in lab)
    assert valid == 0
