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


def test_the_join_the_extendable_class_is_the_geometric_one():
    """m004's meridian is a^2 in pi_1(m000); squaring can never give order 6 in 2T."""
    H = _mod()
    G, I, mul = H.G, H.I, H.mul
    REL000 = "aabbAB"
    surj = [(A, B) for A in G for B in G
            if H.ev(REL000, A, B) == I and len(H.T.generated([A, B])) == 24]
    assert len(surj) == 48, len(surj)                       # codex R037's count
    orders_a = {H.order(A) for A, B in surj}
    assert orders_a == {3, 6}, orders_a                     # control: both occur
    orders_a2 = {H.order(mul(A, A)) for A, B in surj}
    assert orders_a2 == {3}, orders_a2                      # but the square is always 3
    assert 6 not in {H.order(mul(g, g)) for g in G}         # squaring never gives 6 in 2T
