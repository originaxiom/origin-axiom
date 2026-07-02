"""P5 — exact word-ensemble thermodynamics: Z_count = 2^N, Z_trace = 3^N + 1.

Hardened 2026-07-01 (audit): the partitions are now recomputed by brute-force
enumeration over the actual word ensemble (all length-N words in {L, R}), not
just compared to their own closed forms, and the thresholds beta_c^count =
log 2, beta_c^trace = log 3 are asserted as the exact free-energy growth rates
they are, not merely ordered.
"""

from itertools import product

import sympy as sp

from origin_axiom.algebra import L, R
from origin_axiom.statistics import z_count, z_trace


def test_word_count_partition_is_two_to_the_N():
    for N in range(1, 13):
        assert z_count(N) == 2**N


def test_word_count_partition_matches_brute_force_enumeration():
    # Enumerate the actual ensemble: distinct length-N words over {L, R}.
    for N in range(1, 9):
        words = list(product("LR", repeat=N))
        assert len(set(words)) == z_count(N)


def test_trace_partition_is_three_to_the_N_plus_one():
    for N in range(1, 13):
        assert z_trace(N) == 3**N + 1


def test_trace_partition_matches_brute_force_word_sum():
    # Z_N^trace = sum over all 2^N words w of Tr(M_w), computed word by word —
    # the ensemble definition, independent of the Tr((L+R)^N) shortcut.
    gens = {"L": L, "R": R}
    for N in range(1, 8):
        total = 0
        for word in product("LR", repeat=N):
            M = sp.eye(2)
            for letter in word:
                M = M * gens[letter]
            total += sp.trace(M)
        assert total == z_trace(N) == 3**N + 1


def test_thermodynamic_thresholds():
    # beta_c^count = log 2 and beta_c^trace = log 3 are the exact exponential
    # growth rates (free energy per letter) of the two partitions:
    #   (1/N) log Z_N^count = log 2 exactly for every N;
    #   (1/N) log Z_N^trace -> log 3 (limit, since Z = 3^N + 1).
    N = sp.symbols("N", positive=True)
    assert sp.simplify(sp.log(2**N) / N - sp.log(2)) == 0
    assert sp.limit(sp.log(3**N + 1) / N, N, sp.oo) == sp.log(3)
    # and the thresholds are distinct (the two ensembles differ):
    assert sp.log(2) < sp.log(3)
