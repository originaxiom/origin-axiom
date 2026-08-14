"""B1042 locks -- the trit morphism: the chain's computed links, the control, the seal."""
import pathlib, hashlib, subprocess, sys

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1042_trit_morphism"


def test_seal_hash_unchanged():
    h = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h.startswith("b8544786"), h


def test_compute_reproduces():
    out = subprocess.run([sys.executable, str(ARC / "b1042_cells.py")],
                         capture_output=True, text=True, timeout=600).stdout
    assert "conjugacy classes: 7 with sizes [1, 1, 4, 4, 4, 4, 6]" in out
    assert "character orthogonality over Q(omega), all 49 pairs exact: PASS" in out
    assert "graph IS affine E6 (center deg 3, middles deg 2, tips deg 1): PASS" in out
    assert "order-3 automorphism of the McKay graph fixing the center: PASS" in out
    assert "the rotation permutes the three A2 components in one 3-cycle" in out
    assert "PERFECT: the golden end admits NO nontrivial 1-dim characters" in out


def test_findings_fences_and_verdict():
    f = " ".join((ARC / "FINDINGS.md").read_text().split())
    assert "JOINED" in f and "PROVED" in f
    # the sV4 fence: the counting-floor pair stays untouched
    assert "UNTOUCHED for its own pair" in f
    # the control refutes (not avoids) the B757 shape
    assert "REFUTED, not" in f.replace("refuted, not merely avoided", "REFUTED, not")
    # the promotion is row-scoped
    assert "for that row only" in f
