"""B273 locks -- the e6 bracket-coupled cup-product obstruction H^1 x H^1 -> H^2(e6) vanishes identically at
rho_prin (exact mod 99991 & 100003; all 6 directions + generic combination). Resolves the B272-flagged residual:
the {4,8} E6 deformations integrate to 2nd order. FIREWALLED; nothing to CLAIMS.md.
(Heavy computation reproduced by sage-python e6_obstruction_modp.py.)"""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B273_e6_obstruction" / "e6_obstruction.py"
_spec = importlib.util.spec_from_file_location("b273", _PATH)
b273 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b273)


def test_cup_product_identically_zero():
    assert b273.cup_product_identically_zero()


def test_two_primes_agree_h2_dim_6():
    assert b273.PRIMES == [99991, 100003]
    for p in b273.PRIMES:
        assert b273.RESULT[p]["H2dim"] == 6
        # non-vacuous: the obstruction cochain q is nonzero yet a coboundary
        assert b273.RESULT[p]["generic_nonvacuous"] is True


def test_all_six_exponent_directions_vanish():
    for p in b273.PRIMES:
        assert all(b273.RESULT[p][f"exp{m}"] for m in b273.EXPONENTS)
