"""B798 — locks on the algebraicity falsifier's power box (R32-4/R32-5).

The falsifier said "50+ digits with adequate power". Unspecified power is repairable after
the fact, which makes it not a falsifier (E32). These locks fix the arithmetic.
"""
import math


def _H_excluded(N, d):
    """PSLQ at N digits excludes degree-d relations up to height H ~ 10**(N/(1.43 d))."""
    return N / (1.43 * d)


def test_eight_digits_has_essentially_no_power():
    """B797's refusal to claim Test 3 in either direction at 8 digits was correct."""
    assert _H_excluded(8, 2) < 3.0            # d=2 reaches only ~10^2.8
    assert _H_excluded(8, 10) < 1.0           # d=10 reaches under 10^1


def test_fifty_digits_is_under_specified_for_BSV_parity():
    """The headline finding: BSV parity (d<=10, H<=1e7) needs 100 digits, not 50."""
    assert _H_excluded(50, 10) < 4.0          # 50 digits buys only H <= ~10^3.5 at d=10
    need = 1.43 * 10 * 7                      # d=10, log10(H)=7
    assert 99 <= need <= 101                  # => N >= 100
    assert _H_excluded(100, 10) >= 6.9        # 100 digits reaches 10^7


def test_cost_is_orders_of_magnitude_not_a_refinement():
    """Modes ~ linear in precision; dense solve cubic; arbitrary precision adds 10-100x."""
    for N, lo, hi in ((50, 3.0, 4.5), (100, 4.0, 5.5)):
        modes = 900 * (N / 8)
        solve = (modes / 900) ** 3
        assert lo <= math.log10(solve * 10) <= hi
        assert math.log10(solve * 100) <= hi + 1.1
    # the 100-digit run is ~8x the 50-digit run
    assert 7.5 <= ((900 * 100 / 8) / 900) ** 3 / (((900 * 50 / 8) / 900) ** 3) <= 8.5
