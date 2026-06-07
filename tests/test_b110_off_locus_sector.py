"""B110 -- locking tests for the off-locus sector of 4_1 at SL(3) (Task 3 / S011).
The figure-eight SL(3) variety has exactly 3 irreducible components (HMP arXiv:1505.04451 = B71's V0,W1,W2),
each ON the forced locus (x1=x4 or x2=x5), so the off-locus sector (x1!=x4 AND x2!=x5) is EMPTY for 4_1 at SL(3).
Honest scope: the higher-rank / other-manifold S011 fork stays OPEN. NO physics; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b110", _ROOT / "frontier" / "B110_off_locus_sector" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_all_irreducible_components_on_forced_locus():
    comp = B.components_on_forced_locus()
    assert all(v["on_locus_all_samples"] for v in comp.values())   # V0, W1, W2 all on the locus


def test_off_locus_sector_empty_for_figure_eight_sl3():
    s = B.off_locus_search()
    assert s["off_locus_empty"] is True                            # no x1!=x4 AND x2!=x5 point
    assert s["off_locus_points_found"] == 0
    v = B.verdict()
    assert v["off_locus_empty_for_figure_eight_SL3"] is True
    assert "OPEN" in v["scope"]                                     # the broader fork stays open
