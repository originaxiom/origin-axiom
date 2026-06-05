"""B69 (P3, V49) -- the m=2 trace-map framing yields the m136 A-polynomial exactly."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b69_meridian", _ROOT / "frontier" / "B69_metallic_apoly_family" / "metallic_meridian.py")
mm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mm)


def test_m2_trace_identity():
    """kappa = tr(t)^2 - 6 (the m=2 meridian<->longitude identity); resultant = 16 (P^2-S-6)^4."""
    res, check = mm.trace_identity()
    assert check == 0
    P, S = sp.symbols("P S")
    assert sp.simplify(res / (P**2 - S - 6)**4).is_number


def test_m2_apolynomial_is_m136():
    """The squarefree (M,L) eliminant equals the established m136 A-polynomial exactly."""
    derived = mm.derived_apolynomial()
    assert sp.expand(derived - mm.A_M136) == 0
