"""Locks for B397 M5 -- the last census facts."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier",
                    "B397_last_census_facts")


def test_stabilizer_no_local_relabel():
    R = json.load(open(os.path.join(HERE, "relabel_search.json")))
    assert all(v["relabels"] == [] for v in R.values())


def test_defect_intra_model_correction():
    D = json.load(open(os.path.join(HERE, "defect_traceless.json")))
    assert D["slot"]["flip"] == ["0", "0", "0", "0"]
    assert D["3block"]["flip"] == ["0", "0", "-1/24", "-1/24"]
    assert D["raw_cells_differ"] is True
