"""B1359 lock (seconds): the Burnside count of 2T-orbit types from per-order fixed-point numbers returns B1357's torus census once
the origin is required, and exactly Xiao's two K3 configurations for T24 (E6 + D4 + A5 + 2A2 and 2E6 + A3 + 2A2) from Nikulin's numbers."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1359_the_k3_alternative" / "verification"


def test_the_fixed_point_count_reproduces_the_torus_census_and_xiaos_two_k3_types():
    out = subprocess.run([sys.executable, str(VER / "k3_alternative.py")], capture_output=True, text=True, timeout=600).stdout
    assert "the counts agree for every element of the same order (both order-3 and both order-6 classes): True" in out
    assert "T^4: 2 solutions of the counts, 1 with a 2T-fixed point (B1357's census E6 + D4 + A1 + 4A2: True)" in out
    assert "K3: 2 solutions of the counts: E6 + D4 + A5 + 2A2; 2E6 + A3 + 2A2" in out
    assert out.count("chi(quotient) = 5; chi(resolution) = 24") == 5
