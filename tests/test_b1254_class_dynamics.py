"""B1254 — the orientation class under B497's four strata.

Pins the join: eps = squarefree(2 - kappa) is preserved by strata 1-2 and movable only by
stratum 3, with the stratum-3 argument resting on PARITY OF DEGREE, not a search.
"""
import importlib.util
import pathlib

import sympy as sp

_SRC = (pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1254_class_dynamics"
        / "verification" / "class_dynamics.py")
_s = importlib.util.spec_from_file_location("b1254", _SRC)
cd = importlib.util.module_from_spec(_s)
_s.loader.exec_module(cd)

_ACT = cd.class_action()


def test_selftest_passes():
    assert cd.selftest(verbose=False) == []


def test_stratum1_and_2_preserve_the_class():
    assert _ACT["1 Aut/metallic"][2] == "PRESERVED"
    assert _ACT["2 A->A^2,B->B^2"][2] == "PRESERVED"


def test_stratum2_is_the_sharp_case():
    """Its kappa-law is non-trivial, yet (xy)^2 is a perfect square so the class survives."""
    F, is_sq, verdict = _ACT["2 A->A^2,B->B^2"]
    assert F != 1, "the kappa-law must be non-trivial or the case is vacuous"
    assert is_sq and verdict == "PRESERVED"


def test_stratum3_moves_the_class_BY_PARITY_not_by_search():
    x, y, z = sp.symbols('x y z')
    F = cd.STRATA["3 Thue-Morse"]
    assert sp.Poly(sp.expand(F), x, y, z).total_degree() % 2 == 1, "odd degree is the whole proof"
    assert not cd.is_perfect_square(F)
    assert _ACT["3 Thue-Morse"][2] == "CAN CHANGE"


def test_the_classifier_discriminates_both_ways():
    """MB12: if every stratum came back the same, the result would say nothing."""
    assert {v[2] for v in _ACT.values()} == {"PRESERVED", "CAN CHANGE"}


def test_stratum4_lands_where_the_class_is_undefined():
    d = cd.stratum4_lands_on_the_degenerate_locus()
    assert d["2_minus_kappa"] == 0 and d["eps"] == "undefined"
