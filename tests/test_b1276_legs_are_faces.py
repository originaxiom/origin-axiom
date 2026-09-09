"""B1276 — the three forced faces are one V4; the parity law puts the bit on the being face."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1276_legs_are_faces" / "verification" / "legs_are_faces.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import legs_are_faces as L
    return L


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_the_V4_group_law_closes():
    L = _mod()
    assert L.FACES["being"] * L.FACES["hearing"] == L.FACES["meeting"]


def test_the_parity_law_puts_the_bit_on_being():
    L = _mod()
    assert L.c_moves(-3) and not L.c_moves(5) and L.c_moves(-15)


def test_face_is_registered_as_overloaded():
    t = (ROOT / "TERMINOLOGY.md").read_text(encoding="utf-8")
    assert "overloaded-symbol registry" in t
    assert "most overloaded word" in t and "being · hearing = meeting" in t
