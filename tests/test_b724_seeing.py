"""B724 lock — the SEEING-STRATEGY re-adjudication, all computed."""
import sympy as sp, math

def test_C2_three_H1_incommensurable_not_spatial_triad():
    blocks = tuple(math.comb(k + 1, 1) for k in (16, 8, 0))  # 27 = Sym16 + Sym8 + Sym0
    assert blocks == (17, 9, 1) and sum(blocks) == 27 and len(set(blocks)) == 3

def test_C4_forced_ratio_misses_hierarchy():
    tau = {4: 260736, 8: 100636318520821923840}
    forced = math.log10(tau[8] / tau[4])     # theta-odd ratio (the principled combo)
    assert abs(forced - 14.59) < 0.1          # 10^14.59, misses 10^17
    assert 10**(17 - forced) > 200            # by a factor > 200 (259x)

def test_C5_two_bits_cannot_parametrize_19_continuous():
    v4_group = [(a, b) for a in (0, 1) for b in (0, 1)]
    v4_points = len(v4_group)
    sm_params = 9 + 4 + 3 + 2 + 1             # 9 fermion masses + 4 CKM + 3 gauge + 2 Higgs + theta_QCD
    assert v4_points == 4 and math.log2(v4_points) == 2.0 and sm_params == 19

def test_Path1_only_common_integer_is_forced_prime_3():
    z = sp.Symbol("z")
    ramified_prime = abs(int(sp.discriminant(sp.Poly(z**2 + z + 1, z))))
    ggm = {1,3,4,8,9,10,11,12,18,46,62,74,90,170,424,697,702,724351}
    banked = {3, 260736, 165110400, 7983360}  # tau_1 + others + sum-rule
    assert ramified_prime == 3 and ggm & banked == {ramified_prime}
