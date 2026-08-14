"""B1041 locks -- the theta-leg: the obstruction, the L rows, the 8/8, the seal."""
import pathlib, hashlib, subprocess, sys

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1041_theta_leg"


def test_seal_hash_unchanged():
    h = hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h.startswith("165d8ef5"), h


def test_compute_reproduces():
    out = subprocess.run([sys.executable, str(ARC / "b1041_cells.py")],
                         capture_output=True, text=True, timeout=60).stdout
    assert "coordinate-permutation dictionaries intertwining Phi: 0 of 6" in out
    assert "L(e_T4)=(1, 0, 1)  L(e_T6)=(0, 0, 1)  L(e_T3)=(0, 1, 0)" in out
    assert "L is INVERTIBLE over F2 (rank 3)" in out
    assert "affine matches passing the full 3x8 equivariance table: 8 of 8" in out


def test_findings_phrases():
    f = " ".join((ARC / "FINDINGS.md").read_text().split())
    assert "0 of 6" in f
    assert "theta" in f.lower() or "θ" in (ARC / "FINDINGS.md").read_text()
    assert "PROVED" in f
    # the honesty fence: bare existence is torsor-generic, not the banked content
    assert "torsor generality, zero bits" in f
    # the diagonal is the banked new structure
    assert "DIAGONAL" in f
