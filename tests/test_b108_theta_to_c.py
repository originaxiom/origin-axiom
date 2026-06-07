"""B108 -- locking tests for the theta=-w0 -> c derivation (Task 1).
1a/1b: theta is the contragredient involution (P^2=I) and COMMUTES with the trivial-point Jacobian J(m) -- a
tower symmetry organizing the Dickson parity (B62 height-2 split). 1c: at the Dehn-filling reps theta acts as
the contragredient, c -> c^{-1}. 1d (the HINGE): theta fixes c iff c^2=1, so it predicts W1/W2 (order 1),
principal (order 2), but NOT the secondary (c=i, order 4 > order 2 of theta). The hinge fails -- a clean
structural negative with a precise obstruction. NO physics; proven core P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("b108", _ROOT / "frontier" / "B108_theta_to_c" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


# --- 1a / 1b: theta is a tower symmetry --------------------------------------
def test_theta_is_contragredient_involution_commuting_with_tower():
    r = B.theta_is_tower_symmetry()
    assert r["P_is_involution"] is True              # P^2 = I
    assert r["commutes_with_Jm"] is True             # [P, J(m)] = 0 (symbolic, SL(3))
    assert r["height2_split_n345"] == {3: (1, 0), 4: (1, 1), 5: (2, 1)}


# --- 1c: contragredient sends c -> c^{-1} on every realization (>=2 seeds) ---
def test_contragredient_sends_c_to_c_inverse():
    for comp in ("W1", "W2", "principal", "secondary"):
        for seed in (0, 1):
            r = B.contragredient_c(comp, seed)
            assert abs(r["c_times_cdual"] - 1) < 1e-3    # c * c_dual = 1, i.e. c_dual = c^{-1}, every realization


# --- 1d: THE HINGE TEST -- fails on the order-4 secondary (B106-canonical) ---
def test_hinge_theta_does_not_predict_order4_secondary():
    h = B.hinge_test()
    rows = h["rows"]
    assert all(rows[c]["is_root_of_unity"] for c in rows)
    # canonical (B106/D4 seed=0) orders: W1/W2 = 1, principal = 2, secondary = 4
    assert rows["W1"]["order"] == 1 and rows["W2"]["order"] == 1
    assert rows["principal"]["order"] == 2
    assert rows["secondary"]["order"] == 4
    # theta (order 2) fixes c iff c^2 = 1: W1/W2/principal yes, secondary (c=i) no
    assert rows["W1"]["theta_fixes"] and rows["W2"]["theta_fixes"] and rows["principal"]["theta_fixes"]
    assert rows["secondary"]["theta_fixes"] is False
    # the hinge requires ALL FOUR -- it fails, with the order-4 obstruction recorded
    assert h["predicted_by_theta"] == {"W1": True, "W2": True, "principal": True, "secondary": False}
    assert h["hinge_all_four_passed"] is False
    assert h["obstruction"] is not None and "order 4" in h["obstruction"]
