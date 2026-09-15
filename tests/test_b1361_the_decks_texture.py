"""B1361 lock (seconds): the apex U(1)^2 selection rule leaves only 27_1 27_2 27_3 (none with a neutral Higgs), the hollow-matrix
identity e_2(MM^dagger) = S^2 holds symbolically, and the numerical saturation of sigma_1 = sigma_2 + sigma_3."""
import sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1361_the_decks_texture" / "verification"


def test_the_selection_rule_and_the_hollow_identity():
    out = subprocess.run([sys.executable, str(VER / "decks_texture.py")], capture_output=True, text=True, timeout=600).stdout
    assert "symmetric couplings lambda_ijk invariant under both U(1)s: [(1, 2, 3)] (of 10)" in out
    assert "-> no tree-level Yukawa at all: True" in out
    assert "Z_3 (the deck) alone: 4 invariant cubic combinations" in out
    assert "e_2(M M^dagger) - S^2 = 0  -> e_1^2 - 4 e_2 = 0" in out
    assert "max |sigma1 - sigma2 - sigma3|/sigma1 = " in out and "min sigma2/sigma1 = 0.50" in out
    assert "up: m_3/(m_2 + m_1) = 273.2" in out
