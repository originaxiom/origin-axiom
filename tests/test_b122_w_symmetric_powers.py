"""B122 -- locking test: the tower is symmetric powers of the external monodromy fundamental W=V(+)1 (unifies B121).
A genuine GL(2)-module iso (symbolic in general (x,y), det-independent, n<=8) -- NOT vacuous; W is B121's external
det=-1 fundamental (Fricke=Sym^2V is the internal det=+1 one, explaining Chat-2's Fricke kill). Honest: a
repackaging + canonical W, NOT a wall-bypass. NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b122", _ROOT / "frontier" / "B122_W_symmetric_powers" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_character_identity_matches_two_sequence():
    c = B.w_identity_character(11)
    assert c["all_match"] is True and c["mismatches"] == []   # rho_n = Sym^n(W)+Sym^{n-3}(W)-1-V == mu_d, n<=11


def test_genuine_gl2_module_iso():
    g = B.w_identity_is_gl2_module_iso(8)
    assert g["all_zero_general_xy"] is True      # holds symbolically in general (x,y) => genuine GL(2)-module iso
    assert g["det_independent"] is True           # det-independent (not metallic-only)


def test_W_is_external_fundamental_unifies_b121():
    w = B.W_is_external_fundamental()
    assert w["W_external_det_minus_1"] is True     # det(W=V(+)1) = -1 (B121 external parity)
    assert w["fricke_internal_det_plus_1"] is True  # det(Fricke=Sym^2V) = +1 (internal/Kostant) -> the Fricke kill


def test_a7a_sym4_unique_saturation():
    a = B.a7a_corollaries()
    assert a["unique_at_4"] is True               # Sym^4(3-space)=15=sl(4), unique saturating order
    assert a["band_offset_eq_dimW"] == 3


def test_honest_not_a_wall_bypass():
    nb = B.not_a_wall_bypass()
    assert nb["wall_bypassed"] is False           # repackaging + canonical W, NOT a proof route


# --- Chat-2 interlude extensions (det layers + void-specificity) ---

def test_fig8_is_golden_squared():
    fg = B.fig8_is_golden_squared()
    assert fg["M1sq"] == [[2, 1], [1, 1]] and fg["det_is_plus_one"] is True   # fig-8 = golden^2, det +1


def test_magnitude_layer_det_independent_through_n14():
    md = B.magnitude_layer_det_independent(14)
    assert md["all_match"] is True and md["det_independent"] is True   # W-identity holds det=+/-1, n<=14


def test_sign_layer_is_det_minus_one():
    sl = B.sign_layer_is_det_minus_one()
    assert sl["inversion_holds_det_minus_1"] is True       # char(M^-1)=char(-M) at det=-1
    assert sl["inversion_fails_det_plus_1"] is True         # ... fails at det=+1 (the sign layer is metallic)


def test_sym_tower_is_void_specific_order_6():
    vs = B.sym_tower_is_void_specific()
    assert vs["void_charpoly_is_Sym2M"] is True             # void (2,2,2) = Sym^2(M)
    assert vs["zero_charpoly_is_lam3_plus_1"] is True        # (0,0,0) char poly lambda^3+1 = 6th roots
    assert vs["order_is_6_not_3"] is True                    # the order-6 correction (NOT cube roots / order 3)
