"""B1274 — I-25's four candidates collapse to one; two selectors agree."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1274_the_second_collapse" / "verification" / "second_collapse.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import second_collapse as S
    return S


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_both_selectors_pick_the_subregular():
    S = _mod()
    br, _ = S.selector_brieskorn()
    cand, free = S.selector_psl()
    assert br == free == [(2, 2, 2, 0, 2, 2)]


def test_the_agreement_is_not_vacuous():
    """Selector 2 must start from FOUR candidates, or agreeing means nothing."""
    S = _mod()
    cand, free = S.selector_psl()
    assert len(cand) == 4 and len(free) == 1
