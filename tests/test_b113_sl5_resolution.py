"""B113 -- locking tests: the B112-proved closed form resolves the SL(5) sign sectors + localizes degree=rank.
Heights 2,3,4 of the SL(5) tower match the proved closed form exactly (incl. B62's char(M^2)^2.char(-M^2), the
2 gauge-corrupted modes); degree=rank is confined to height-1 + char(M^5); the promotion is n-dependent (open).
NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b113", _ROOT / "frontier" / "B113_sl5_resolution" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_closed_form_matches_sl5_above_height1():
    rows = B.closed_form_vs_sl5()
    assert rows[2]["match"] and rows[3]["match"] and rows[4]["match"]   # heights 2,3,4 exact
    assert not rows[1]["match"]                                          # height 1 differs (the promotion)


def test_resolves_b62_gauge_corrupted_modes():
    b = B.b62_modes_resolved()
    assert b["predicts_second_char_M2"] is True                         # char(M^2)^2 . char(-M^2)
    assert b["closed_form_h2"] == (2, 1)


def test_degree_rank_localized_and_promotion_nonuniform():
    d = B.degree_rank_localization()
    assert d["heights_2_to_nminus1_pure_bulk_theta"] is True            # heights 2..n-1 = pure bulk theta
    assert d["height1_differs"] is True
    assert d["top_power_present_in_tower"] is True                      # char(M^5) = the longitude
    assert d["promotion_is_uniform"] is False                          # n-dependent (open power half)
