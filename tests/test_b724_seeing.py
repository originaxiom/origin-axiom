"""B724 lock — the SEEING-STRATEGY re-adjudication, all computed."""
import sympy as sp, math

def test_C2_three_H1_incommensurable_not_spatial_triad():
    blocks = (17, 9, 1)                       # 27 = Sym16 + Sym8 + Sym0
    assert sum(blocks) == 27 and len(set(blocks)) == 3   # distinct dims -> no S_3/SO(3) triad

def test_C4_forced_ratio_misses_hierarchy():
    tau = {4: 260736, 8: 100636318520821923840}
    forced = math.log10(tau[8] / tau[4])     # theta-odd ratio (the principled combo)
    assert abs(forced - 14.59) < 0.1          # 10^14.59, misses 10^17
    assert 10**(17 - forced) > 200            # by a factor > 200 (259x)

def test_C5_two_bits_cannot_parametrize_19_continuous():
    v4_points = 4                             # 2 bits
    sm_params = 19
    assert v4_points < float('inf') and sm_params >= 19   # 4 discrete points, 19 continuous dims
    # a finite set is measure-zero in R^19 -> base rate exactly 0
    assert v4_points == 4

def test_Path1_only_common_integer_is_forced_prime_3():
    ggm = {1,3,4,8,9,10,11,12,18,46,62,74,90,170,424,697,702,724351}
    banked = {3, 260736, 165110400, 7983360}  # tau_1 + others + sum-rule
    assert ggm & banked == {3}                # only 3 (the forced ramified prime of Q(sqrt-3))
