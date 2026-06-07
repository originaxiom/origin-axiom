"""B111 -- locking tests for the tower's sign structure + the degree=rank exponent constraints.
PART 0: the SL(3) sign rule + the corrected (t - det N) parity. The opposition-involution closed form
(matches B62 height-2). PATH B/C: Tower(n) = closed form with one char(M^1) promoted to char(M^n) (n=3,4).
ADDITION 1: M^4 scalar on the SL(4) secondary -> k=4 impossible (proved); k=4 allowed on the principal.
ADDITION 2: cusp orders {n-1,n+1,2n}; ord-1 formula TESTED-NEGATIVE. s_n<->c DEAD. NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("b111", _ROOT / "frontier" / "B111_sign_structure" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


# --- PART 0: the SL(3) sign rule + the corrected parity ----------------------
def test_sl3_sign_rule_parity_t_minus_detN():
    r = B.sl3_sign_rule()
    assert r["metallic_m_stable_det_minus1"] is True
    for name, v in r["components"].items():
        assert v["parity_divides"] is True               # parity (t-1)(t - det N) divides char(J)
    # the corrected rule: det=-1 -> (t-1)(t+1); det=+1 -> (t-1)^2
    assert "(t - 1)*(t + 1)" in r["components"]["metallic_m1"]["parity_predicted"]
    assert "(t - 1)**2" in r["components"]["figure_eight"]["parity_predicted"]


# --- the opposition-involution closed form ----------------------------------
def test_closed_form_matches_b62_height2():
    m = B.closed_form_matches_b62((3, 4, 5))
    assert all(m[n]["match"] for n in (3, 4, 5))         # (1,0),(1,1),(2,1)
    for n in (3, 4, 5, 6):
        assert B.excess_plus_over_minus(n)["matches"]     # (+)-excess = floor(n/2)


# --- PATH B/C: the degree=rank promotion ------------------------------------
def test_tower_is_closed_form_plus_degree_rank_promotion():
    for n in (3, 4):
        r = B.tower_vs_closed_form(n)
        assert r["tower_equals_closed_plus_promotion"] is True   # one char(M) -> char(M^n)


# --- ADDITION 1: the M^4-scalar impossibility -------------------------------
def test_addition1_secondary_k4_impossible_principal_allowed():
    mp = B.mpower_scalar_table()
    assert mp["secondary_k4_impossible"] is True          # M^4 = -1 scalar on the secondary -> k=4 impossible
    assert mp["principal_k4_allowed"] is True             # M^4 non-scalar on the principal -> k=4 allowed
    # each component's degree=rank exponent is a non-scalar power
    for name, v in mp["per_component"].items():
        assert v["exponent_is_nonscalar"] is True


# --- ADDITION 2: cusp orders {n-1,n+1,2n}; ord-1 TESTED-NEGATIVE -------------
def test_addition2_cusp_orders_and_ord_minus_1_negative():
    co = B.cusp_order_pattern()
    assert co["pattern_is_nm1_np1_2n"] is True            # orders are {n-1, n+1, 2n}
    assert co["ord_minus_1_formula_passes_hinge"] is False  # ord-1 fails the all-four hinge


# --- s_n <-> c DEAD ----------------------------------------------------------
def test_s_n_to_c_bridge_dead():
    assert B.s_n_to_c_bridge_dead()["bridge_dead"] is True
