"""B1378 lock -- THE M6 DECK TRIPLET.  A single seed non-split background on Y6 (m004's degree-6 cyclic cover) sits in a
genuine order-3 deck orbit; each of the three orbit members has six-Standard-Model-sector index (-1)^6, and their rank-6
direct sum has EXACT index (-3)^6, confirmed over three primes and exactly over Q(zeta_8) -- reproducing (with an
independently-built Reidemeister-Schreier presentation and this branch's own index_lib.py/exact_lib.py, not a copy of the
source's script) a result reported by an external seat's audit package.  Y6's identity with H1 = Z/8 (+) Z/40 (+) Z is
cross-checked against the classical fibration-monodromy computation, independent of any group presentation.  The arc
had reported an error in the source's word-level deck map; that report is WITHDRAWN (2026-10-01, main's B1432, recomputed
exactly here): the source's TAU2 is conjugation by a^2, and this seat's substitute is not.  The index never used the map."""
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


def test_the_web_seats_deck_map_is_right():
    """2026-10-01 correction (main's B1432): over Q(sqrt-3) the web seat's TAU2 is conjugation by a^2 on all seven cover
    generators; the substitute this arc had proposed fails on generators 5 and 7"""
    out = run(str(VER / "deck_map_web_seat.py"), timeout=300)
    assert "web seat's TAU2 = conjugation by a^2 on every cover generator: True" in out
    assert "B1378's substitute = conjugation by a^2: False" in out and "5: False" in out and "7: False" in out
    assert "DONE" in out
