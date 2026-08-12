"""B1044 locks -- the Gamma-ledger: the counts, the closure, the fence, the seal."""
import pathlib, hashlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1044_gamma_ledger"


def test_seal_hash_unchanged():
    h = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h.startswith("0d8776d2"), h


def test_ledger_counts():
    led = " ".join((ARC / "b1044_ledger.md").read_text().split())
    assert "Γ: 0 of 20 rows" in led
    assert "ALGEBRA: 18" in led
    assert "CLASS: 1 (B727" in led
    assert "UNDECIDABLE: 0" in led


def test_findings_closure_and_fence():
    f = " ".join((ARC / "FINDINGS.md").read_text().split())
    assert "the Γ-column is EMPTY" in f
    assert "B803's open address CLOSES EMPTY" in f
    assert "EXIST" in f and "ENTER" in f          # the entry fence
    assert "CONFIRMED by enumeration" in f        # B993's re-verification
    assert "PROVED" in f
