"""B1797 -- GENESIS v1.59.  The amendment reproduces the root file from the hash-pinned v1.58 (--check bites); every status
cell as it was; FK10's v1.59 sentence names the four links as not derived and keeps B1700's reading tag and FK11; FK15's
pointer is to its existence half only; the log entry above an unrewritten v1.58 entry."""
import importlib.util, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1797_genesis_v1_59"


def _m():
    spec = importlib.util.spec_from_file_location("am59", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_amendment_reproduces_the_root_file():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.59 · 2026-10-28 · canonical.**" in g:
        assert _m().build() == g


def test_the_changes():
    src = (A / "received" / "GENESIS_v1_58_main.md").read_text(encoding="utf-8"); out = _m().build()
    cells = lambda t: re.findall(r"^\| (GM\d\w?|PF\d|FK\d+|SE\d) \|[^|]*\| \*{0,2}([A-Z][A-Z ,]+)", t, re.M)
    assert cells(src) == cells(out)
    fk10 = [l for l in out.splitlines() if l.startswith("| FK10 ")][0]
    assert "The unit reduced to the field's existence and three further links, none derived on the record" in fk10
    assert "B1700's reading, not a claim" in fk10 and "That the three are generations is FK11's" in fk10
    assert "this is a reduction of the postulate, not a derivation" in fk10 and "At a Fuchsian point of the fibre" in fk10
    assert len(fk10.split(" | ")) == len([l for l in src.splitlines() if l.startswith("| FK10 ")][0].split(" | "))
    fk15 = [l for l in out.splitlines() if l.startswith("| FK15 ")][0]
    assert "follows from this fork's existence half" in fk15 and "not B1654's (0, 1) typing above" in fk15
    i59, i58 = out.find("- **v1.59 · 2026-10-28 · main B1797.**"), out.find("- **v1.58 · 2026-10-24 · main B1754.**")
    assert 0 < i59 < i58


def test_the_companions_b1797():
    reg = (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    assert "| P-288 | 2026-10-22 | OW |" in reg
    cm = (ROOT / "docs" / "THE_COMPLETION_MAP.md").read_text(encoding="utf-8")
    assert "four open links" in cm
