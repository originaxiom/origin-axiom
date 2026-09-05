"""Classifier controls; object-matrix verification has a separate sealed runner."""
import json

import sympy as sp

from reports.physical_bridge_2026_09_05 import upstream_second_check as check


def test_polynomial_square_has_even_degree_negative_and_coefficient_controls():
    x, y = sp.symbols("x y")
    assert check.polynomial_square(sp.Rational(25, 4)*(x+y)**4, [x, y])
    assert check.polynomial_square(sp.Integer(0), [x, y])
    assert not check.polynomial_square(x*x+1, [x, y])
    assert not check.polynomial_square(-x*x, [x, y])
    assert not check.polynomial_square(2*x*x, [x, y])


def test_named_laws_survive_but_classifier_and_stratum_scope_need_correction():
    result = check.dynamics_controls()
    assert set(result["exact_named_identity_remainders"].values()) == {"0"}
    assert result["square_predicate_controls"][-1] == {
        "polynomial": "x**2 + 1", "upstream": True, "factorization": False}
    assert result["decimation_to_undefined_class"]["kappa_after"] == "2"
    assert not result["determinant_one_not_Aut_witness"]["matrix_images_commute"]
    assert result["rational_Thue_Morse_class_change"]["square_class_ratio"] == "-4"
    assert json.loads(json.dumps(result)) == result
