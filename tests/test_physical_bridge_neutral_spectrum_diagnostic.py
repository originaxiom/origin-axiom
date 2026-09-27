"""R49 post-failure rational polynomial/rank controls, not physical modes."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

PATH = Path(__file__).resolve().parents[1]/"reports/physical_bridge_2026_09_05/neutral_spectrum_diagnostic.py"
SPEC = importlib.util.spec_from_file_location("r49_spectrum_diagnostic", PATH)
d = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(d)


@pytest.mark.parametrize("restricted,multiplicities", [(False,(1,3,11)), (True,(1,3,5))])
def test_rational_spectra_and_projectors(restricted, multiplicities):
    matrix = d.r.zero_weight_restriction()[1] if restricted else d.r.operators()[5]
    result = d.analyze(matrix, multiplicities)
    assert all(result["checks"].values())
    assert sum(result["kernel_dimensions"]) == matrix.rows


def test_expression_variables_must_not_be_merged_by_name():
    a = s.Symbol("same_name", real=True)
    b = s.Symbol("same_name")
    assert str(a) == str(b)
    assert a != b
    assert not d.r.zero(a-b)
    poly = s.diag(2,6).charpoly(a)
    assert d.qq_coefficients(poly) == (1,-8,12)
    assert d.r.zero(poly.as_expr()-(poly.gen-2)*(poly.gen-6))


def test_two_sided_controls():
    assert all(d.controls().values())


def test_symbolic_coefficient_is_not_silently_renamed():
    x,y = s.symbols("x y")
    with pytest.raises(ValueError, match="exact rational coefficients"):
        d.qq_coefficients(s.Poly(x+y,x))


def test_corrected_polynomial_keeps_all_six_extra_channels():
    full = d.r.operators()[5]
    small = d.r.zero_weight_restriction()[1]
    x = s.Symbol("comparison_variable")
    pfull = s.Poly.from_list(d.qq_coefficients(full.charpoly()),x,domain=s.QQ)
    psmall = s.Poly.from_list(d.qq_coefficients(small.charpoly()),x,domain=s.QQ)
    quotient,remainder = s.div(pfull,psmall)
    assert remainder.is_zero
    assert quotient == s.Poly((x-6)**6,x,domain=s.QQ)
