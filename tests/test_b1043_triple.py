"""B1043 locks -- the triple: the gate, the numbers, the fingerprint, the decoy."""
import pathlib, hashlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1043_triple_assembly"


def test_seal_hash_unchanged():
    h = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h.startswith("575ad81b"), h


def test_output_log_numbers():
    out = (ARC / "b1043_output.txt").read_text()
    assert "h0(M;27) = 1   h0(T^2;27) = 3" in out
    assert "h1(double;27) = 5" in out and "GATE PASS" in out
    assert "h1(triple;27) = 10" in out
    assert "9 - 2 = 7" in out and "bulk = h1 - connecting = 3" in out
    assert "F3 (>= 6, pinned pre-arc): connecting = 7 -> PASS" in out
    assert "DECOY D (>= 12, deliberately unbanked): -> FAIL" in out
    assert "R44-12 discharged" in out
    assert "HALT-VOID" in out


def test_findings_phrases():
    f = " ".join((ARC / "FINDINGS.md").read_text().split())
    assert "10 = 7 + 3" in f or "10 = 7 connecting + 3 bulk" in f.replace("h¹ = 10 = 7 + 3", "10 = 7 + 3")
    assert "SUPERLINEAR" in f
    assert "invariant line" in f
    assert "DISCHARGED" in f
    assert "closed mirror-double OF the 3-fold cyclic cover" in f
    assert "PROVED" in f
