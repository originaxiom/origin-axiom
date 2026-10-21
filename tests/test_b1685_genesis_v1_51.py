"""B1685 -- GENESIS v1.51. The amendment reproduces the root file from the hash-pinned v1.50 (the bite: --check fails if
the root differs); the tags are in place, no status cell changed, FK11 reads W45 and W46 as verified, GM1's tie to PF1 is
read as circular through kappa, and the log carries the v1.51 entry above an unrewritten v1.50 entry."""
import importlib.util, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1685_genesis_v1_51_reliance_tagged"


def _m():
    spec = importlib.util.spec_from_file_location("am", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_amendment_reproduces_the_root_file():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.51 · 2026-10-21 · canonical.**" in g:          # later amendments keep this arc's text, not its version
        assert _m().build() == g


def test_the_tags_and_no_status_changed():
    m = _m(); src = (A / "received" / "GENESIS_v1_50_main.md").read_text(encoding="utf-8"); out = m.build()
    assert src.count("the seat's, unverified on main") == 0
    assert out.count("; v1.51]") == 20 and out.count("the seat's, unverified on main") == 22   # twenty sites, the §5 note, the log
    cells = lambda t: re.findall(r"^\| (GM\d\w?|PF\d|FK\d+|SE\d) \|[^|]*\| \*{0,2}([A-Z][A-Z ,]+)", t, re.M)
    assert cells(src) == cells(out)                                 # every status cell as it was
    assert "both verified on main since, B1632 and B1641" in out and "Joined through κ the tie is circular" in out
    i51, i50 = out.find("- **v1.51 · 2026-10-21 · main B1685.**"), out.find("- **v1.50 · 2026-10-21 · main B1683.**")
    assert 0 < i51 < i50
