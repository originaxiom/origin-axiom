"""B1263 — I-6's side A: 48 surjections, 2 quotients up to Aut, no mirror pairing."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1263_i6_side_a_verified" / "verification" / "two_2T_quotients.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import two_2T_quotients as T
    return T


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_side_A_is_real():
    T = _mod()
    assert len(T.G) == 24
    assert len(T.surjections()) == 48


def test_exactly_two_quotients_up_to_Aut():
    T = _mod()
    S = T.surjections()
    auts = T.automorphisms(*S[0])
    assert len(auts) == 24
    seen, n = set(), 0
    for A, B in S:
        if (A, B) in seen:
            continue
        n += 1
        for h in auts:
            seen.add((h[A], h[B]))
    assert n == 2


def test_fibonacci_part_runs_and_cross_checks():
    """Part 2: monodromy = Fibonacci^2, and the fiber picture gives the same 2 classes."""
    script = ROOT / "frontier" / "B1263_i6_side_a_verified" / "verification" / "fibonacci_and_the_two.py"
    r = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout
    assert "monodromy-invariant CLASSES: 2" in r.stdout
    assert "swapped 0, fixed 24" in r.stdout
