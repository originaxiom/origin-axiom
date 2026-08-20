"""B8095 — the related-work armor. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8095_related_work_armor", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_five_differentiators(r):
    assert r["n"] == 5 and len(r["differentiators"]) == 5

def test_every_row_ends_in_a_not_claim(r):
    """cc's specified deliverable shape."""
    assert r["every_row_has_a_not_claim"] is True

def test_the_lisi_row_rests_on_the_accounting_not_the_algebra(r):
    row = [d for d in r["differentiators"] if "Lisi" in d["programme"]][0]
    assert "0905.2658" in row["killer"]
    assert "PRICED INPUT" in row["our_difference"]

def test_the_connes_row_admits_the_limitation(r):
    """We are not vulnerable there because we do not reach there."""
    row = [d for d in r["differentiators"] if "Connes" in d["programme"]][0]
    assert "do NOT claim their successes" in row["we_do_not_claim"]

def test_scope_admits_the_primary_papers_were_not_read(r):
    assert r["primary_papers_read_in_full"] is False
    assert "STANDING PUBLISHED criticisms" in r["scope"]
