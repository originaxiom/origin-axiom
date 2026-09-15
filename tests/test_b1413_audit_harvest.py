"""B1413 lock: main's exact recomputation of R27's positive re-runs live (sympy over Q(u)) and reproduces I(V) = +1, I(V^ss) = 0."""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1413_the_audit_lanes_r21_r31", "verification")

def test_r27_exact_positive_live():
    r = subprocess.run([sys.executable, os.path.join(V, "main_r27_exact_lift.py")], capture_output=True, text=True, timeout=900)
    out = r.stdout
    assert r.returncode == 0, out[-800:] + r.stderr[-800:]
    assert "I(V) = n(V) - n(V*) = 1" in out and "I(V^ss) = 0" in out, out[-600:]
    assert "relator -> [[1, 0], [0, 1]]" in out and "chi on relator, mu, lambda: 1 1 1" in out
