"""B1751 -- GENESIS v1.56.  The amendment reproduces the root file from the hash-pinned v1.55 (--check bites); every status
cell as it was; FK9's joint-looks sentence and F-MC's ladder rule in place; the log entry above an unrewritten v1.55
entry; the look ledger, the ladder's rule and the glossary present."""
import importlib.util, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1751_genesis_v1_56"


def _m():
    spec = importlib.util.spec_from_file_location("am56", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_amendment_reproduces_the_root_file():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.56 · 2026-10-24 · canonical.**" in g:
        assert _m().build() == g


def test_the_changes():
    src = (A / "received" / "GENESIS_v1_55_main.md").read_text(encoding="utf-8"); out = _m().build()
    cells = lambda t: re.findall(r"^\| (GM\d\w?|PF\d|FK\d+|SE\d) \|[^|]*\| \*{0,2}([A-Z][A-Z ,]+)", t, re.M)
    assert cells(src) == cells(out)
    assert "The looks are counted jointly across seats" in out and "The ladder's rule R1" in out
    i56, i55 = out.find("- **v1.56 · 2026-10-24 · main B1751.**"), out.find("- **v1.55 · 2026-10-24 · main B1750.**")
    assert 0 < i56 < i55


def test_the_companions():
    assert "every seat's search of the same frame against the same data is one look" in (ROOT / "docs" / "LOOK_LEDGER.md").read_text(encoding="utf-8")
    assert "## The ladder's rule (adopted 2026-10-24): R1, every finite rung at once" in (ROOT / "docs" / "THE_WEAVE.md").read_text(encoding="utf-8")
    assert "Classical names — the referee lane's concordance" in (ROOT / "TERMINOLOGY.md").read_text(encoding="utf-8")
