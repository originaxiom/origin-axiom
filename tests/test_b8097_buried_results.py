"""B8097 — the buried-results census. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8097_buried_results", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_twelve_admitted_representation_debts(r):
    assert r["catalogue_1_representation_debts"]["count"] == 12

def test_six_over_wide_closures_plus_one_falsified(r):
    c = r["catalogue_2_over_wide_closures"]
    assert c["count"] == 6 and c["falsified"]["lead"] == "L73"

def test_L1_touches_the_objects_own_selection(r):
    """The most load-bearing row: the object's selection banked wider than proved."""
    l1 = [x for x in r["catalogue_2_over_wide_closures"]["ranked"] if x["lead"] == "L1"][0]
    assert "CANNOT DISCRIMINATE" in l1["why_worst"] and "TIES with m003" in l1["why_worst"]

def test_the_meta_finding_is_that_noticing_was_treated_as_discharging(r):
    assert "NOTICING HAS BEEN TREATED AS DISCHARGING" in r["meta_finding"]

def test_no_suppressed_positive_is_claimed(r):
    assert r["no_suppressed_positive"] is True
    assert r["mechanism_is_not_gate5"] is True
