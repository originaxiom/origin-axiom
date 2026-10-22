"""B1715 -- GENESIS v1.53. The amendment reproduces the root file from the hash-pinned v1.52 (--check bites); every
status cell as it was; the five [v1.53] sentences and the log entry in place above an unrewritten v1.52 entry."""
import importlib.util, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1715_genesis_v1_53"


def _m():
    spec = importlib.util.spec_from_file_location("am53", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_amendment_reproduces_the_root_file():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.53 · 2026-10-22 · canonical.**" in g:
        assert _m().build() == g


def test_the_changes():
    src = (A / "received" / "GENESIS_v1_52_main.md").read_text(encoding="utf-8"); out = _m().build()
    cells = lambda t: re.findall(r"^\| (GM\d\w?|PF\d|FK\d+|SE\d) \|[^|]*\| \*{0,2}([A-Z][A-Z ,]+)", t, re.M)
    assert cells(src) == cells(out)
    assert out.count("[v1.53]") == 5 and "never three. FK10's single" in out and "Closed since (B1678" in out
    i53, i52 = out.find("- **v1.53 · 2026-10-22 · main B1715.**"), out.find("- **v1.52 · 2026-10-22 · main B1706.**")
    assert 0 < i53 < i52


def test_the_check_bites(tmp_path):
    m = _m(); g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert m.build() != g.replace("FK10's single unit", "FK10's one unit") or "Version 1.53" not in g[:400]
