"""B1681 -- GENESIS v1.49. The amendment reproduces v1.49 from the hash-pinned v1.48: the root file while it was at
v1.49, and B1683's received copy since (2026-10-21: GENESIS moved to v1.50, so the check reads the pinned copy, as
B1662's reads its own log entry). In v1.49 GM1 read DERIVED given one input; the log keeps the v1.49 entry."""
import hashlib, importlib.util, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1681_genesis_v1_49_two_records_derived"
V149 = ROOT / "frontier" / "B1683_genesis_v1_50_gm1_characterised" / "received" / "GENESIS_v1_49_main.md"


def test_the_amendment_reproduces_v1_49():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    spec = importlib.util.spec_from_file_location("am", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    v = V149.read_text(encoding="utf-8")
    assert hashlib.sha256(v.encode("utf-8")).hexdigest() == "347ea2d24d63687c3b9fab3cbac4ba98c09237c1721939ea51b413d1760506f4"
    assert m.build() == v


def test_gm1_in_v1_49_and_the_log():
    v = V149.read_text(encoding="utf-8")
    assert "**Version 1.49 · 2026-10-20 · canonical.**" in v
    assert "| GM1 | Two records: updates act on a pair of integer counts, ℤ² | **DERIVED given one input [v1.49]**" in v
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert "- **v1.49 · 2026-10-20 · main B1681.**" in g and "The principle's form is the family" in g
