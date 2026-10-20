"""B1683 -- GENESIS v1.50. The amendment reproduces the root file from the hash-pinned v1.49 (the bite: --check fails if
the root differs), GM1 reads POSTULATED in an equivalent form with the extension of the moves named, GM5b's "only" is
scoped while its status stays ADOPTED, and the log carries the v1.50 entry above an unrewritten v1.49 entry."""
import importlib.util, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1683_genesis_v1_50_gm1_characterised"


def test_the_amendment_reproduces_the_root_file():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    spec = importlib.util.spec_from_file_location("am", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.50 · 2026-10-21 · canonical.**" in g:          # later amendments keep this arc's text, not its version
        assert m.build() == g


def test_gm1_gm5b_and_the_log():
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert "| GM1 | Two records: updates act on a pair of integer counts, ℤ² | **POSTULATED, in an equivalent form [v1.50]**" in g
    assert "**[v1.50] Answered: equivalent, not weaker" in g and "the moves extend beyond two records democratically" in g
    assert "| GM5b | Inverse moves are legal | **ADOPTED [v1.48]**" in g
    assert "of the two readings B1662 compared, only this one never settles" in g and "at equal strength only this reading never settles" not in g
    i50, i49 = g.find("- **v1.50 · 2026-10-21 · main B1683.**"), g.find("- **v1.49 · 2026-10-20 · main B1681.** GM1 derived given one input")
    assert 0 < i50 < i49
