"""B123 -- locking test: m=1 arithmeticity, a third independent selection criterion (SUPPORTED).
COMPUTED in-house: the fig-8 cyclotomic shape (z^2-z+1=Phi_6, z0=e^{i pi/3}) + the order-6 echo at the geometric
cusp (kappa=-2). CITED (Reid 1991): the fig-8 is the unique arithmetic knot; m>=2 are non-arithmetic. The m>=2
trace-field non-arithmeticity is SnapPy-gated (the named confirmation step) -- banked SUPPORTED, NOT TESTED-POSITIVE.
The order-6 echo is an OBSERVATION, not a connection. NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b123", _ROOT / "frontier" / "B123_arithmeticity_m1" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_figure_eight_shape_is_cyclotomic():
    sh = B.figure_eight_shape_is_cyclotomic()
    assert sh["is_cyclotomic_Phi6"] is True        # z^2-z+1 = Phi_6 (the 6th cyclotomic)
    assert sh["z0_satisfies_shape"] is True and sh["z0_primitive_6th_root"] is True   # z0 = e^{i pi/3}


def test_order6_echo_at_geometric_cusp_is_observation():
    ec = B.order6_echo_at_geometric_cusp()
    assert ec["zero_jacobian_6th_roots"] is True and ec["order_is_6"] is True   # (0,0,0) = 6th roots
    assert ec["kappa_at_zero"] == -2 and ec["is_geometric_cusp"] is True         # at the geometric cusp
    assert "OBSERVATION" in ec["status"]                                          # not a banked connection


def test_third_criterion_supported_not_tested_positive():
    tc = B.third_selection_criterion()
    assert tc["shape_computed"] is True
    assert tc["banked_as"] == "SUPPORTED (not TESTED-POSITIVE)"   # honest scope (trace field SnapPy-gated)
    assert "SnapPy" in tc["m_ge_2_nonarith_status"]               # the named confirmation step


def test_det_minus_one_is_b121_crossref():
    db = B.det_minus_one_is_b121()
    assert db["is_b121_restated"] is True          # cross-ref B121, NOT a new finding
