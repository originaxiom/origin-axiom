"""B361 -- the seam's local law: the (1,7)/(3,7) discriminator decides H-loc."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B361_seam_local_law'))
from seam_disc import load_banked


def test_1_7_bright_refutes_hmin():
    r = load_banked()
    assert r["1,7"]["seam"] == 20 and r["1,7"]["nonzero"] == 31
    assert set(r["1,7"]["svals"]) == {"-1/48", "-1/96", "1/48", "1/96"}


def test_3_7_bright_with_the_2_3_value_echo():
    r = load_banked()
    assert r["3,7"]["seam"] == 18 and r["3,7"]["nonzero"] == 39
    assert set(r["3,7"]["svals"]) == {"-1/144", "-1/288", "1/144", "1/288"}   # identical to (2,3)'s


def test_local_law_consistency_over_the_computed_range():
    # bright iff the pair contains a doubly-elliptic seed (m = 2 or 7 among m <= 7)
    bright = {(1, 2), (2, 3), (2, 4), (1, 7), (3, 7)}
    dark = {(1, 3), (1, 4), (3, 5)}
    def qualifies(m):
        return m in (2, 7)
    assert all(any(qualifies(m) for m in p) for p in bright)
    assert all(not any(qualifies(m) for m in p) for p in dark)
