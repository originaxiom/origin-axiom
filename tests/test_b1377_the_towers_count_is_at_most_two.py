"""B1377 lock.  Fast (seconds): on Y_2, Y_3, Y_4 every rank-one character into mu_N has h^1 <= 1 (the hypothesis of the |I| <= 2
bound), and B1375's record shows every firing doublet module with (a_1, r_1) = (1, 0) against (2, 2).  Slow: Y_5 and Y_6."""
import sys, subprocess
import pytest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1377_the_towers_count_is_at_most_two" / "verification"
REC = ROOT / "frontier" / "B1375_the_towers_generation_count" / "verification" / "tower_generations_run.txt"


def run(*args, timeout):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True, timeout=timeout, cwd=str(VER)).stdout


def test_rank_one_h1_at_most_one_on_levels_two_to_four_and_the_firing_dimensions():
    out = run(str(VER / "rank_one_bound.py"), "2", "3", "4", timeout=900)
    assert "Y_2: H1 = Z/5 + Z, N = 60" in out and "a_1 = h^1 distribution {0: 295, 1: 5}" in out and "max a_1 = 1" in out
    assert "Y_3: H1 = Z/4 + Z/4 + Z, N = 12" in out and "{0: 176, 1: 16}" in out
    assert "Y_4: H1 = Z/3 + Z/15 + Z, N = 60" in out and "{0: 2655, 1: 45}" in out
    assert out.count("max a_1 = 1") == 3 and "DONE" in out
    rec = REC.read_text()
    assert "firing modules' (a_1, r_1, a_1*, r_1*): {(1, 0, 2, 2): 488, (2, 2, 1, 0): 488}" in rec        # Y_4
    assert "firing modules' (a_1, r_1, a_1*, r_1*): {(2, 2, 1, 0): 2200, (1, 0, 2, 2): 2200}" in rec      # Y_5
    assert "firing modules' (a_1, r_1, a_1*, r_1*): {(2, 2, 1, 0): 5408, (1, 0, 2, 2): 5408}" in rec      # Y_6


@pytest.mark.slow
def test_rank_one_h1_at_most_one_on_levels_five_and_six():
    out = run(str(VER / "rank_one_bound.py"), "5", "6", timeout=1800)
    assert "Y_5: H1 = Z/11 + Z/11 + Z, N = 132" in out and "{0: 15849, 1: 123}" in out and "max a_1 = 1" in out
    assert "Y_6: H1 = Z/8 + Z/40 + Z, N = 120" in out and "{0: 38080, 1: 320}" in out
    assert out.count("max a_1 = 1") == 2
