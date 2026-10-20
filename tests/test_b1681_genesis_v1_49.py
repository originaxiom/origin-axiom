"""B1681 -- GENESIS v1.49. The amendment reproduces the root file from the hash-pinned v1.48 (the bite: --check fails if
the root differs), GM1 reads DERIVED given one input, and the log carries the v1.49 entry."""
import importlib.util, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1681_genesis_v1_49_two_records_derived"


def test_the_amendment_reproduces_the_root_file():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    spec = importlib.util.spec_from_file_location("am", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    assert m.build() == (ROOT / "GENESIS.md").read_text(encoding="utf-8")


def test_gm1_and_the_log():
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert "**Version 1.49 · 2026-10-20 · canonical.**" in g
    assert "| GM1 | Two records: updates act on a pair of integer counts, ℤ² | **DERIVED given one input [v1.49]**" in g
    assert "- **v1.49 · 2026-10-20 · main B1681.**" in g and "the principle's form is the family of wordings" in g.lower() or "The principle's form is the family" in g
