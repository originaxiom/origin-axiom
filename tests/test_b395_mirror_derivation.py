"""Locks for B395 M3 -- the emergent-mirror kill."""
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier",
                    "B395_mirror_derivation")


def test_cell_law_killed():
    R = json.load(open(os.path.join(HERE, "mirror_derivation.json")))
    assert R["lift"] is None


def test_passing_set_not_pm_I_mod3():
    D = json.load(open(os.path.join(HERE, "passing_domain.json")))
    assert D["passing"] == 100 and D["match_pm"] is False
