"""B1372 lock (seconds): the Standard-Model weights of the 27 and the 78 with their SL(2)_beta spin and gamma (the frame theorem and
the unique both-doublet assignment: the 10 from the 78 at gamma = 1, the 5bar from the 27 at gamma = 1/3); Theorem B (no simultaneous
cusp-fixedness at a non-unitary peripheral eigenvalue: 0 of 32 sign patterns); Theorem C (a unitary eigenvalue must be a fourth root
of unity); Theorem C' (no uniform eigenvector choice at order 4); m004's four order-4 representations, all unitary."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1372_the_doublet_halves" / "verification"


def test_the_mixed_frame_is_closed_by_charge_arithmetic_at_the_cusp():
    out = subprocess.run([sys.executable, str(VER / "doublet_halves.py")], capture_output=True, text=True, timeout=1500).stdout
    assert "the only both-doublet assignment: the 10 from the 78's doublets, gamma = [Fraction(1, 1)]; the 5bar from the 27's doublets, gamma = [Fraction(1, 3)]" in out
    assert "(Y, gamma) types: the 10 in the 78 [('-2/3', '1'), ('1/6', '1'), ('1', '1')]; the 5bar in the 27 [('-1/2', '1/3'), ('1/3', '1/3')]" in out
    assert "sign patterns (which eigenvector each of the five types fixes) admitting (Im s, Im t) with L != 0: 0 of 32" in out
    assert "the 10 (three Y-types, gamma = 1): consistent (Im s, Im t) = [('0', '-L'), ('0', 'L')]" in out
    assert "theta mod 1 admitting a solution, over all 32 patterns: [0, 1/4, 1/2, 3/4]" in out
    assert "patterns with a solution at theta = +-1/4: 4:" in out
    assert "patterns with all fifteen weights on the same eigenvector: 0" in out
    assert "order-4 representations: 4; with rho(lambda) fixing a vector (a cusp-fixed doublet sector possible): 4; of them unitary: 4" in out
    assert "DONE" in out
