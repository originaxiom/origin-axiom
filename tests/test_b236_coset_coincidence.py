"""B236 locks -- Path A: the ordinary/super coset coincidence at SU(2)_3 (closes the H21 gate). Pure
central-charge arithmetic, fully pyenv-testable. Firewall: dimensionless CFT data; nothing to CLAIMS.md."""
import importlib.util
import pathlib
from fractions import Fraction as Fr

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B236_coset_coincidence_pathA" / "coset_coincidence.py"
_spec = importlib.util.spec_from_file_location("b236_coset", _PATH)
b236 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b236)


def test_coset_charges_match_minimal_model_formulas():
    for m in range(3, 8):
        assert b236.c_ordinary(m) == Fr(1) - Fr(6, m * (m + 1))
    for k in range(1, 6):
        assert b236.c_super(k) == Fr(3, 2) * (Fr(1) - Fr(8, (k + 2) * (k + 4)))


def test_tci_is_the_same_coset_ordinary_and_super():
    assert b236.ordinary_coset_data(4) == b236.super_coset_data(1) == ((1, 2), 3)
    assert b236.c_ordinary(4) == b236.c_super(1) == Fr(7, 10)


def test_coset_coincidence_is_unique_at_tci():
    assert b236.coincidences(60) == [(4, 1, Fr(7, 10))]


def test_e7_appears_in_tci_as_coset_algebra():
    """(E7)_1 (+) (E7)_1 / (E7)_2 has c=7/10 -- E7 in the TCI itself (distinct from the excluded McKay 2O)."""
    assert b236.c_e7_tci_coset() == Fr(7, 10)
