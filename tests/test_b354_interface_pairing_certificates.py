"""B354 -- the metallic interface pairing: exact certificates + divisibility law + parity legs. sympy-only."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B354_interface_pairing_certificates'))
from interface_certificates import (
    strong_channel_is_universal_only, pair_12_intersection,
    pair_13_certificate, pair_23_certificate, no_quadratic_subfield,
    divisibility_law, divisibility_examples, parity_exact_legs,
)


def test_strong_channel_kill_is_exact_and_universal():
    # Fix(T_i) cap Fix(T_j) = {(0,0,0),(2,2,2)} for (1,2) and (1,3), = Fix(Ta) cap Fix(Tb) (Groebner)
    assert strong_channel_is_universal_only()


def test_pair_12_intersection_reproduces_banked_b131_fork():
    m2, fork = pair_12_intersection()
    assert m2 == [2, 4] and fork == [-4, -2]            # = B131/V120 exact fork


def test_pair_13_and_23_exact_certificates():
    # irreducible odd-degree minpolys whose kappa-images match B131's banked numeric forks (all 8 values)
    assert pair_13_certificate()
    assert pair_23_certificate()


def test_classical_seam_null():
    assert no_quadratic_subfield()                       # degrees 5,3 => no quadratic subfield => no sqrt(-15)


def test_divisibility_law():
    assert divisibility_law()                            # R^m L^m == I mod p <=> p | m (exact)
    assert divisibility_examples()                       # golden !=I mod 2; silver ==I mod 2; bronze ==I mod 3


def test_parity_texture_exact_legs():
    assert parity_exact_legs()                           # golden l=-2 fiber {1,4}; silver {4} only
