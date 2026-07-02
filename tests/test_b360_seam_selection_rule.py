"""B360 -- the selection rule tested: both parity readings refuted; silver-selectivity survives."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B360_seam_selection_rule'))
from seam_predict import load_banked


def test_prediction_verdicts():
    r = load_banked()
    assert r["3,5"]["seam"] == 0 and r["3,5"]["nonzero"] == 15      # dark, as predicted
    assert r["1,4"]["seam"] == 0 and r["1,4"]["nonzero"] == 31      # DARK -- refutes "contains an even seed"
    assert r["2,4"]["seam"] == 36 and r["2,4"]["nonzero"] == 49     # BRIGHT -- refutes "opposite parity"


def test_2_4_svalues_subset_of_1_2():
    r = load_banked()
    assert set(r["2,4"]["svals"]) == {"-1/120", "-1/240", "-1/480", "1/120", "1/240", "1/480"}


def test_silver_selectivity_across_all_six_pairs():
    r = load_banked()
    bright = {k for k, v in r.items() if v["seam"] > 0}
    assert bright == {"2,4"}                                         # of this run's three; (1,2),(2,3) banked in B358/B359
    # the six-pair statement is documented in FINDINGS; this lock covers the new three.


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1", reason="full exact regeneration ~10 min")
def test_full_regeneration_slow():
    import json
    import seam_predict as spd
    spd.main()
    assert load_banked()["1,4"]["seam"] == 0
