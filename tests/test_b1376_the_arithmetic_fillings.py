"""B1376 lock.  The cocompact arithmeticity criterion, own instrument without Sage, on seven controls -- the Weeks manifold,
the Meyerhoff manifold m004(5,1), m004(6,1), m004(8,1) arithmetic; m004(7,1), m004(4,3), m004(1,2) not, each with its reason.
An exhaustive |p|<=8, 1<=q<=8 grid re-check was attempted (verification/arithmetic_fillings.py grid) and abandoned: it reproduced
these same six slopes on 46 of 87 cases and then stalled on a high-degree non-integral field the algdep/lindep route cannot
resolve without Sage in reasonable time; the exhaustive census is B718's own (dual-method), cited rather than re-derived here,
so no lock depends on the grid finishing."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1376_the_arithmetic_fillings" / "verification"


def run(*args, timeout):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True, timeout=timeout, cwd=str(VER)).stdout


def test_the_meyerhoff_manifold_and_the_controls():
    out = run(str(VER / "arithmetic_fillings.py"), "controls", timeout=1500)
    assert "m003(-3,1)     ARITHMETIC" in out and "k: degree 3, signature (1,1), squarefree part of the discriminant -23," in out
    assert "m004(5,1)      ARITHMETIC" in out and "k: degree 4, signature (2,1), squarefree part of the discriminant -283," in out and "ramified at the real places [True, True], vol 0.98137, H1 Z/5" in out
    assert "m004(6,1)      ARITHMETIC" in out and "squarefree part of the discriminant -59," in out
    assert "m004(8,1)      ARITHMETIC" in out and "squarefree part of the discriminant -31," in out
    assert "m004(7,1)      NON-ARITHMETIC (2 complex places)" in out and "signature (2,2)" in out
    assert "m004(4,3)      NON-ARITHMETIC (the quaternion algebra splits at a real place)" in out and "ramified at the real places [True, True, False]" in out
    assert "m004(1,2)      NON-ARITHMETIC (the quaternion algebra splits at a real place)" in out and "signature (5,1)" in out
    assert out.count("ARITHMETIC  ") == 4 and "DONE" in out

