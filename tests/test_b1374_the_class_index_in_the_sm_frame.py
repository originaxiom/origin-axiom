"""B1374 locks.  Fast (about two minutes): main's B1418 modules on m004, s958 and t12839 recomputed with the seat's own prime-field
index (3 339 modules identical on all three primes), and the Standard-Model-frame census at mu_12 on the same three members (rank-one
sectors zero; at mu_12 no generation-shaped pattern).  Slow: the full cells (19 253 modules), the torsion-complete census (t12839:
12 800 generation-shaped, anomaly-free pairs; the other twelve members 0), the pair extraction and the three exact backgrounds."""
import sys, subprocess
import pytest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1374_the_class_index_in_the_sm_frame" / "verification"


def run(*args, timeout):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True, timeout=timeout, cwd=str(VER)).stdout


def test_main_b1418_verified_on_three_members_and_the_sm_frame_census_at_mu12():
    out = run(str(VER / "class_index_sm_frame.py"), "all", "m004", "s958", "t12839", timeout=1500)
    assert "m004        H1 = Z                      loci (ours, mu_12)   1: modules compared   135, identical on all three primes   135, differing 0" in out
    assert "s958        H1 = Z/3 + Z                loci (ours, mu_12)  13: modules compared   819, identical on all three primes   819, differing 0" in out
    assert "t12839      H1 = Z/3 + Z/15 + Z         loci (ours, mu_12)  17: modules compared  2385, identical on all three primes  2385, differing 0" in out
    assert "TOTAL modules compared: 3339; I and all four dimensions of V and V* identical over the three primes: 3339; differing: 0" in out
    assert "m = 0 modules 12 with I != 0: 0; doublet modules (m = 1) with I != 0: 0" in out          # m004: nothing fires
    assert "m = 0 modules 468 with I != 0: 0; doublet modules (m = 1) with I != 0: 8; adjoint (m = 2) with I != 0: 8" in out
    assert "m = 0 modules 1836 with I != 0: 0; doublet modules (m = 1) with I != 0: 64; adjoint (m = 2) with I != 0: 64" in out
    assert "pairs (psi_Y, psi_gamma) with some net count non-zero: 1160 of 16848; generation-shaped (Q = u^c = e^c = d^c = L != 0): 0; anomaly-free with a non-zero charged count: 0" in out
    assert "pairs (psi_Y, psi_gamma) with some net count non-zero: 28928 of 198288; generation-shaped (Q = u^c = e^c = d^c = L != 0): 0; anomaly-free with a non-zero charged count: 0" in out
    assert "(Q, u^c, e^c, d^c, L, nu^c) = (1, -1, 0, 1, -1, -1)" in out
    assert out.count("generation-shaped (Q = u^c = e^c = d^c = L != 0): 0") == 3
    assert "DONE" in out


@pytest.mark.slow
def test_every_module_main_ran_the_torsion_complete_census_and_the_generation_on_the_tower():
    out = run(str(VER / "class_index_sm_frame.py"), "all", timeout=3000)
    assert "TOTAL modules compared: 19253; I and all four dimensions of V and V* identical over the three primes: 19253; differing: 0" in out
    assert out.count("generation-shaped (Q = u^c = e^c = d^c = L != 0): 0; anomaly-free with a non-zero charged count: 0") == 13
    assert "m = 0 modules 3960 with I != 0: 0" in out
    out2 = run(str(VER / "torsion_complete.py"), timeout=3000)
    assert out2.count("generation-shaped 0; anomaly-free non-zero 0") == 12
    assert "o10_150697  H1 = Z/5 + Z              N = 60 p = 421: |Hom(H1, mu_N)| =   300, non-split loci   13" in out2 and "with I != 0:    16" in out2
    assert "t12839      H1 = Z/3 + Z/15 + Z       N = 60 p = 421: |Hom(H1, mu_N)| =  2700, non-split loci   89" in out2
    assert "generation-shaped 12800; anomaly-free non-zero 12800" in out2
    out3 = run(str(VER / "generation_pairs.py"), "t12839", "60", timeout=3000)
    assert "generation-shaped pairs (from the table): 12800" in out3
    assert "recomputed sector by sector over (421, 541, 601): differing 0 of 12800" in out3
    assert "loci carrying a generation-shaped pair: 64 of 89; sign of the count: {-1: 6400, 1: 6400}; orders of psi_Y: {1: 512, 5: 12288}" in out3
    for psiG, counts in (("(14,12,44)", "(1, 1, 1, 1, 1, 0)"), ("(6,8,56)", "(-1, -1, -1, -1, -1, 0)")):
        out4 = run(str(VER / "exact_check.py"), "t12839", "60", "2", "(0,0,0)", psiG, timeout=1500)
        assert "h^1(pi; chi^2) = 1 exactly" in out4 and f"EXACT counts (Q, u^c, e^c, d^c, L, nu^c) = {counts}" in out4
