"""B497 locks — the endomorphism monoid Phase 0 (four strata, two universal laws).

Guards: the stratum-2 trace maps (decimation + period-doubling), the exact per-verb
kappa multipliers, U1 (kappa=2 invariance), U2 (toral classical floor), the injectivity/
kernel witnesses, the Fibonacci degree ledger, and the F_p guard.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B497_endomorphism_monoid"))
import verify_monoid as V


def test_stratum2_trace_maps():
    assert V.check_stratum2_maps(n=8)


def test_kappa_multipliers_exact():
    assert V.check_kappa_multipliers()


def test_U1_classicality_conserved():
    assert V.check_U1(trials=12)


def test_U2_toral_floor():
    assert V.check_U2()


def test_witnesses():
    assert V.check_witnesses()


def test_fibonacci_degree_ledger():
    assert V.degree_ledger() == [2, 3, 5, 8, 13, 21, 34, 55]


def test_Fp_guard():
    assert V.check_Fp(primes=(101,), n=80)
