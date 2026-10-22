"""B1706 -- GENESIS v1.52. The amendment reproduces the root file from the hash-pinned v1.51 (--check bites); every
status cell as it was; the lifted and scoped tags, FK10's sentence and the log entry in place above an unrewritten v1.51
entry."""
import importlib.util, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1706_genesis_v1_52"


def _m():
    spec = importlib.util.spec_from_file_location("am52", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_amendment_reproduces_the_root_file():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.52 · 2026-10-22 · canonical.**" in g:
        assert _m().build() == g


def test_the_changes():
    src = (A / "received" / "GENESIS_v1_51_main.md").read_text(encoding="utf-8"); out = _m().build()
    cells = lambda t: re.findall(r"^\| (GM\d\w?|PF\d|FK\d+|SE\d) \|[^|]*\| \*{0,2}([A-Z][A-Z ,]+)", t, re.M)
    assert cells(src) == cells(out)
    assert src.count("; v1.51]") == 20 and out.count("; v1.51]") == 13
    assert out.count("verified on main since, B1689") >= 4 and "The Higgs's end data are this unit (B1700)." in out
    assert out.count("of R57 only its quotient") == 5
    i52, i51 = out.find("- **v1.52 · 2026-10-22 · main B1706.**"), out.find("- **v1.51 · 2026-10-21 · main B1685.**")
    assert 0 < i52 < i51
