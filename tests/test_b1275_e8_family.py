"""B1275 — the E8 > E6 x A2 family mechanism, rebuilt and verified."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1275_e8_family_verified" / "verification" / "e8_family.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import e8_family as E
    return E


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_the_branching_closes():
    E = _mod()
    roots, R, a, b, A2, E6, rest = E.decompose()
    assert len(roots) == 240 and len(A2) == 6 and len(E6) == 72 and len(rest) == 162
    assert 162 == 6 * 27


def test_six_classes_of_27():
    E = _mod()
    _, _, a, b, _, _, rest = E.decompose()
    byc = {}
    for r in rest:
        byc.setdefault((E.dot(r, a), E.dot(r, b)), []).append(r)
    assert len(byc) == 6 and {len(v) for v in byc.values()} == {27}
