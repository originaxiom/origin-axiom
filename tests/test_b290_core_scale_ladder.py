"""B290 lock -- the core-geodesic SCALE LADDER and the n-vs-k question. The (1,n) core length is
ell_C = 2*pi*i/n + (pi/sqrt(3))/n^2 + ... (NZ, cusp-shape-controlled; |ell_C| ~ 2*pi/n, confirming B286). The filling
coefficient n is a topological surgery integer, NOT the WRT quantum level k (B204) -- independent axes. The
core=(G*Lambda)/3 link under k=n is HELD (122-order gap). FIREWALLED; nothing to CLAIMS.md.
(SnapPy reproducer: sage-python frontier/B290_core_scale_ladder/core_scale_ladder.py.)"""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B290_core_scale_ladder" / "verdict.py"
_spec = importlib.util.spec_from_file_location("b290", _PATH)
b290 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b290)


def test_correction_coeff_is_2pi_over_cusp_shape():
    coeff = b290.correction_coeff_from_cusp_shape()
    assert sp.simplify(coeff - sp.pi / sp.sqrt(3)) == 0               # = 2*pi/|tau_cusp|, tau = 2 sqrt(3) i
    assert abs(float(coeff) - b290.CORRECTION_COEFF_MEASURED) < 2e-3  # cusp-shape prediction vs SnapPy measurement


def test_leading_ladder_confirms_b286():
    assert b290.LEADING_IS_2pi_over_n                                 # |ell_C| ~ 2*pi/n
    assert b290.NZ_CUSP_SHAPE_CONTROLLED


def test_filling_n_is_not_the_wrt_level_k():
    assert b290.FILLING_N_IS_TOPOLOGICAL
    assert b290.WRT_LEVEL_K_IS_QUANTUM
    assert b290.N_EQUALS_K is False                                  # independent axes


def test_glambda_link_held_firewall():
    assert "HELD" in b290.CORE_EQUALS_GLAMBDA_OVER_3_UNDER_kn        # 122-order gap, not banked
    assert b290.DERIVES_SM_VALUES is False
    assert b290.verdict()
