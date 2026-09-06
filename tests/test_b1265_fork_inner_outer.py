"""B1265 — D2's signature derives E6(-14); E6(-26) is outer-only."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1265_the_fork_is_inner_vs_outer" / "verification" / "fork_inner_outer.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import fork_inner_outer as F
    return F


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_D2_signature_is_minus_14_and_selects_one_form():
    F = _mod()
    k, p = F.d2_signature()
    assert (k, p) == (46, 32) and k + p == 78
    sig = p - k
    assert sig == -14
    match = [f for f in F.FORMS if 78 - 2 * f[2] == sig]
    assert len(match) == 1 and match[0][0] == "E6(-14)"


def test_E6_minus_26_is_outer_so_no_torus_element_reaches_it():
    F = _mod()
    by = {f[0]: f[3] for f in F.FORMS}
    assert by["E6(-14)"] == F.RANK_E6          # inner
    assert by["E6(-26)"] != F.RANK_E6          # outer — the rank obstruction
