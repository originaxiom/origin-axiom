"""B1375 locks.  Fast (about a minute): the cyclic covers Y_2, Y_3, Y_4 of m004 on their own presentations, torsion-complete and
T5-restricted -- Y_2 and Y_3 carry no generation-shaped background, Y_4 carries 12 800 on 64 loci with count +-1 (the census numbers
of B1374 on t12839 reproduced from the cover's own presentation).  Slow: Y_5 and Y_6, and the exact check over Q(zeta_132) of a Y_5
background."""
import sys, subprocess
import pytest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1375_the_towers_generation_count" / "verification"


def run(*args, timeout):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True, timeout=timeout, cwd=str(VER)).stdout


def test_levels_two_to_four_and_the_presentation_independence_of_y4():
    out = run(str(VER / "tower_generations.py"), "2", "3", "4", timeout=1500)
    assert "Y_2  = Z/5 + Z                    N =  60 primes [421, 541, 601]: |Hom| =    300, non-split loci    9" in out
    assert "firing 16 (re-checked 16, differing 0); GENERATION-SHAPED backgrounds 0 on 0 loci" in out
    assert "Y_3  = Z/4 + Z/4 + Z              N =  12 primes [409, 421, 433]: |Hom| =    192, non-split loci   31" in out
    assert "firing 0 (re-checked 0, differing 0); GENERATION-SHAPED backgrounds 0 on 0 loci" in out
    assert "Y_4  = Z/3 + Z/15 + Z             N =  60 primes [421, 541, 601]: |Hom| =   2700, non-split loci   89 (spurious [0, 0, 0]; h1(chi^2) {1: 89})" in out
    assert "T5-candidate doublet modules 4005, firing 976 (re-checked 976, differing 0); GENERATION-SHAPED backgrounds 12800 on 64 loci, signs {1: 6400, -1: 6400}, |count| {1: 12800}" in out
    assert "psi_Y orders {1: 512, 5: 12288}" in out
    assert "DONE" in out


@pytest.mark.slow
def test_levels_five_and_six_and_the_exact_y5_background():
    out = run(str(VER / "tower_generations.py"), "5", "6", timeout=3000)
    assert "Y_5  = Z/11 + Z/11 + Z            N = 132 primes [661, 1321, 1453]: |Hom| =  15972, non-split loci  241" in out
    assert "firing 4400 (re-checked 4400, differing 0); GENERATION-SHAPED backgrounds 800 on 200 loci, signs {-1: 400, 1: 400}, |count| {1: 800}" in out
    assert "Y_6  = Z/8 + Z/40 + Z             N = 120 primes [601, 1201, 1321]: |Hom| =  38400, non-split loci  639" in out
    assert "firing 10816 (re-checked 10816, differing 0); GENERATION-SHAPED backgrounds 67200 on 576 loci, signs {1: 33600, -1: 33600}, |count| {1: 67200}" in out
    out2 = run(str(VER / "exact_check_cover.py"), "5", "(0,6,120)", "(0,0,0)", "(24,90,96)", timeout=3000)
    assert "h^1(pi; chi^2) = 1 exactly" in out2 and "EXACT counts (Q, u^c, e^c, d^c, L, nu^c) = (1, 1, 1, 1, 1, 0)" in out2
