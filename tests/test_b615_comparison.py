"""B615 lock: the Branch-3 comparison — the raw table and verdict pinned."""
import os
import subprocess
import sys

_SCRIPT = os.path.join(os.path.dirname(__file__), "..", "frontier",
                       "B615_comparison", "b615_comparison.py")


def test_b615_comparison():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=1200)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert "design hash: 9a189f49" in out
    # the three G2 matches at tier 1e-2, none at 1e-3
    assert "A5 (4/7)sin^2(4pi/7) vs sin^2th23" in out
    assert out.count("MATCH@1e-2") == 4          # 3 in G2 + 1 in G4
    assert "observed 3, expected 0.57" in out
    assert "Sidak-corrected best-grid p, tier 0.01: 0.0775" in out
    assert "VERDICT (per the locked table): AMBIGUOUS" in out
