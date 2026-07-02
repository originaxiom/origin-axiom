"""B347 -- the E6 character-variety tangent of the figure-eight and its two Z/2 gradings. mpmath-only."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B347_e6_tangent_gradings'))
import mpmath as mp
from e6_tangent_gradings import (
    EXPONENTS, geometric_rep_residual, symrep_homomorphism_residual,
    H1_dim, e6_tangent_total, amphichiral_indicator, hyperelliptic_sign, run_all,
)


def test_geometric_rep_and_symrep_are_valid():
    assert geometric_rep_residual() < mp.mpf(10) ** -50        # rho(relator) = I
    assert symrep_homomorphism_residual() < mp.mpf(10) ** -50   # Sym^d is a genuine homomorphism


def test_sl2_anchor_is_one():
    assert H1_dim(1) == 1                                       # dim H^1(4_1, Sym^2) = the A-poly curve tangent


def test_e6_tangent_is_six_one_per_exponent():
    assert all(H1_dim(m) == 1 for m in EXPONENTS)               # uniform: one direction per exponent
    assert e6_tangent_total() == 6                              # = rank E6 (refutes the degenerate-cascade reading)


def test_amphichirality_acts_uniformly():
    assert all(amphichiral_indicator(m) == 1 for m in EXPONENTS)  # J^2 = +1 real structure everywhere, no split


def test_hyperelliptic_grades_onto_the_e6_f4_split():
    signs = {m: hyperelliptic_sign(m) for m in EXPONENTS}
    assert signs == {m: (-1) ** (m + 1) for m in EXPONENTS}     # ε_m = (-1)^{m+1}
    minus = [m for m in EXPONENTS if signs[m] < 0]
    assert minus == [4, 8]                                      # (-1)-eigenspace = e6/f4 coset (B265 escape sector)
    plus = [m for m in EXPONENTS if signs[m] > 0]
    assert plus == [1, 5, 7, 11]                                # (+1)-eigenspace = F4 exponents


def test_run_all_shape():
    r = run_all()
    assert r["total"] == 6 and r["minus_eigenspace"] == [4, 8]
