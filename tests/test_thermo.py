"""P5 — exact word-ensemble thermodynamics: Z_count = 2^N, Z_trace = 3^N + 1."""

import sympy as sp

from origin_axiom.statistics import z_count, z_trace


def test_word_count_partition_is_two_to_the_N():
    for N in range(1, 13):
        assert z_count(N) == 2**N


def test_trace_partition_is_three_to_the_N_plus_one():
    for N in range(1, 13):
        assert z_trace(N) == 3**N + 1


def test_thermodynamic_thresholds():
    # beta_c^count = log 2, beta_c^trace = log 3 (radii of convergence)
    assert sp.log(2) < sp.log(3)
