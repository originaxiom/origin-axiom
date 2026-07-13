"""B565 H1(iv) lock — the triality match: B299's (theta,phi) Z3xZ3 acts on the E6
27 as the cyclic triality (9 free orbits of size 3, each hitting all three
trinification blocks exactly once). Runs the full reproducer."""
import pathlib
import subprocess
import sys

def test_triality_reproducer_verdicts():
    script = (pathlib.Path(__file__).resolve().parent.parent
              / "frontier" / "B565_gauge_behavior_campaign" / "verify_h1_triality.py")
    out = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, timeout=300)
    assert out.returncode == 0, out.stderr[-500:]
    for gen in ("theta", "phi"):
        assert f"{gen}: 9 orbits, sizes {{3: 9}}" in out.stdout            # 9 free orbits of size 3
        assert f"{gen}: every orbit hits all 3 blocks exactly once (multiset == [0,1,2]): True" in out.stdout
