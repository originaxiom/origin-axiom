"""B213 -- the Higgs-side period data of the figure-eight character variety (Act I, S039). Firewalled;
nothing to CLAIMS.md. Load-bearing locks (the firewall-holds-a-4th-time verdict):
 - every special-geometry datum is O(1) (no forced tiny number / no hierarchy);
 - the null test: L(E,1)/Omega is a generic simple BSD rational (1/2 is NOT special);
 - the structural arithmetic: the conductor 40=2^3*5 sees the golden monodromy prime 5, not hyperbolic 3.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B213_higgs_side_periods"))
from higgs_periods import (E40A1, NULL_L_OVER_OMEGA, structural_arithmetic,  # noqa: E402
                           is_simple_rational)


def test_higgs_handle_all_O1_no_hierarchy():
    # the decisive firewall test: NO forced tiny number -- every datum is O(1)
    for key in ("real_period", "L_at_1", "L_over_Omega", "regulator", "mahler_Phi", "vol_over_2pi"):
        assert 0.1 < E40A1[key] < 2.0, (key, E40A1[key])
    assert E40A1["rank"] == 0 and E40A1["sha"] == 1 and E40A1["cm"] is False


def test_L_over_Omega_is_exactly_half_BSD():
    # L(E,1)/Omega = 1/2 exactly (BSD: Sha * prod c_p / |T|^2, with Sha=1, |T|=4, prod c_p = 8)
    assert E40A1["L_over_Omega"] == 0.5
    ok, frac = is_simple_rational(E40A1["L_over_Omega"])
    assert ok and frac.numerator == 1 and frac.denominator == 2


def test_null_test_kills_the_half():
    # HELD rule: 1/2 is NOT special -- EVERY rank-0 curve gives a simple BSD rational L/Omega
    n_simple = sum(is_simple_rational(v)[0] for v in NULL_L_OVER_OMEGA.values())
    assert n_simple == len(NULL_L_OVER_OMEGA)            # all simple rationals
    # and the values are spread (1/5, 1/6, 1/4, 1/3, 1/2, 2/3, 1) -- 1/2 is one generic point
    distinct = {is_simple_rational(v)[1] for v in NULL_L_OVER_OMEGA.values()}
    assert len(distinct) >= 5


def test_mahler_geometry_rhyme_is_O1():
    # m(Phi) ~ Omega/2 ~ L(E,1): a Deninger-type arithmetic<->geometry rhyme, all O(1) (no scale)
    assert abs(E40A1["mahler_Phi"] - E40A1["real_period"] / 2) < 0.01
    assert abs(E40A1["mahler_Phi"] - E40A1["L_at_1"]) < 0.01


def test_structural_conductor_sees_golden_not_hyperbolic_prime():
    # the firewall-clean structural find: conductor 40=2^3*5 -> sees the monodromy prime 5, not the
    # hyperbolic prime 3 (the variety is a Betti object; its arithmetic tracks the Betti/monodromy side)
    s = structural_arithmetic()
    assert s["sees_golden_prime_5"] is True
    assert s["sees_hyperbolic_prime_3"] is False
    assert E40A1["bad_primes"] == [2, 5]


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
