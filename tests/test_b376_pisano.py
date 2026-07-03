"""Lock for B376 — the Pisano identity (recomputed live; integer-fast)."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..",
                                "frontier", "B376_cat_map_recognition"))
from pisano_identity import pisano, ord_cat, MEASURED


def test_pisano_identity_five_levels():
    for N, measured in MEASURED.items():
        assert pisano(N) // 2 == ord_cat(N) == measured


def test_registered_predictions():
    assert pisano(375) // 2 == ord_cat(375) == 500
    assert pisano(405) // 2 == ord_cat(405) == 540
    assert pisano(675) // 2 == ord_cat(675) == 900
