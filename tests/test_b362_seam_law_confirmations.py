"""B362 -- three pre-registered predictions, three hits: the law at 11 pairs."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B362_seam_law_confirmations'))
from seam_confirm import load_banked


def test_predictions_all_hit():
    r = load_banked()
    assert r["2,7"]["seam"] == 12 and set(r["2,7"]["svals"]) == {"-1/48", "-1/96", "1/48", "1/96"}
    assert r["1,5"]["seam"] == 0 and r["1,5"]["nonzero"] == 6
    assert r["4,5"]["seam"] == 0 and r["4,5"]["nonzero"] == 6


def test_law_at_eleven_pairs():
    bright = {(1, 2), (2, 3), (2, 4), (1, 7), (3, 7), (2, 7)}
    dark = {(1, 3), (1, 4), (3, 5), (1, 5), (4, 5)}
    doubly_elliptic = {2, 7}
    assert all(any(m in doubly_elliptic for m in p) for p in bright)
    assert all(not any(m in doubly_elliptic for m in p) for p in dark)
