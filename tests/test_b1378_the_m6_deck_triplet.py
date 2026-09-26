"""B1378 lock -- THE M6 DECK TRIPLET.  A single seed non-split background on Y6 (m004's degree-6 cyclic cover) sits in a
genuine order-3 deck orbit; each of the three orbit members has six-Standard-Model-sector index (-1)^6, and their rank-6
direct sum has EXACT index (-3)^6, confirmed over three primes and exactly over Q(zeta_8) -- reproducing (with an
independently-built Reidemeister-Schreier presentation and this branch's own index_lib.py/exact_lib.py, not a copy of the
source's script) a result reported by an external seat's audit package.  Y6's identity with H1 = Z/8 (+) Z/40 (+) Z is
cross-checked against the classical fibration-monodromy computation, independent of any group presentation.  One error
was found in the source's own account of the deck square's word-level automorphism (does not touch the index; see
verification/rs_presentation.py's TAU2 comment and FINDINGS.md Sec. 3)."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1378_the_m6_deck_triplet" / "verification"


def run(*args, timeout):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True, timeout=timeout, cwd=str(VER)).stdout


def test_the_presentation_and_the_classical_cross_check():
    out = run(str(VER / "rs_presentation.py"), timeout=120)
    assert "torsion [8, 40], free rank 1" in out
    assert "(TAU2)^3 = I: True; TAU2 != I: True" in out
    assert "invariant factors [8, 40], order of M on it: 6" in out
    assert "ALL STRUCTURAL CHECKS PASSED" in out


def test_the_deck_triplet_index():
    out = run(str(VER / "deck_triplet.py"), timeout=180)
    assert out.count("members [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1]]") == 4
    assert "orbit-sum I per sector [-3, -3, -3, -3, -3, -3]" in out and out.count("orbit-sum I per sector [-3, -3, -3, -3, -3, -3]") == 3
    assert "V dims (a0,a1,t0,r1) = (0, 6, 3, 6), V* dims = (0, 3, 3, 0)" in out
    assert out.count("V dims (a0,a1,t0,r1) = (0, 6, 3, 6), V* dims = (0, 3, 3, 0)") == 6
    assert "cross-check passed: True" in out
    assert "h^1(pi; chi_j^2) = [1, 1, 1]" in out
    assert "index with the cocycle set to 0 (all six sectors): [0, 0, 0, 0, 0, 0]" in out
    assert "DONE" in out
