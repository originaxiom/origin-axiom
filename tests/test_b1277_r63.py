"""B1277 — fc's R63 recomputed: three claims confirmed, one premise corrected."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1277_leak_closure" / "verification" / "r63_check.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import r63_check as R
    return R


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_subregular_lies_in_no_F4():
    """27|F4 = 26+1, so an sl2 inside F4 must leave a trivial summand in the 27."""
    R = _mod()
    WT, Cinv, roots = R.setup()
    assert 1 in R.d27(R.PRIN, WT, Cinv)          # principal can lie in F4
    assert 1 not in R.d27(R.SUB, WT, Cinv)       # subregular cannot


def test_the_spin2_premise_does_not_hold_for_the_principal():
    """fc's 'both have exactly one spin-2 summand' — the principal has ZERO."""
    R = _mod()
    WT, Cinv, roots = R.setup()
    assert R.d27(R.PRIN, WT, Cinv).count(5) == 0
    assert R.d78(R.PRIN, roots).count(5) == 0
    assert R.d27(R.SUB, WT, Cinv).count(5) == 1
