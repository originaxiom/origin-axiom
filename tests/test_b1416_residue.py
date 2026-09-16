"""B1416 lock: the class counts of primitive indefinite binary quadratic forms of discriminant m^2 + 4 -- the banked GL(2,Z) table
(1,1,1,1,1,2,1,1,2,2,1) for m = 1..11 and, at m = 12 (D = 148), 3 proper / 2 improper classes (B1240's R42; cc3's B8148 said 3/3)."""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1416_the_relay_residue_closed", "verification")

def test_class_numbers_m2_plus_4():
    r = subprocess.run([sys.executable, os.path.join(V, "class_numbers_m2plus4.py")], capture_output=True, text=True, timeout=300)
    assert r.returncode == 0, r.stderr[-500:]
    assert "GL table m=1..11: [1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1]" in r.stdout
    assert "m=12 D= 148  SL(2,Z) classes 3  GL(2,Z) classes 2" in r.stdout
