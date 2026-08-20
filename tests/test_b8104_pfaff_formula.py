"""B8104 — the cusped formula exists. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8104_pfaff_formula", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_it_retracts_this_seats_own_label(r):
    assert "B8102" in r["retracts"] and r["label_lifetime_hours"] == 2

def test_the_formula_has_the_three_terms(r):
    f = r["source"]["formula"]
    assert "kappa(X)" in f and "vol(X)" in f and "R(k,sigma_k)" in f
    assert r["three_term_structure_matches_B8101"] is True

def test_kappa_is_the_cusp_count_and_ours_is_one(r):
    assert "number of cusps" in r["source"]["kappa_is"]
    assert r["our_ingredients"]["kappa"] == 1

def test_every_ingredient_is_available(r):
    assert r["nothing_unavailable"] is True
    assert abs(r["our_ingredients"]["volume"] - 2.029883212819307) < 1e-12

def test_the_remaining_gap_is_one_identification(r):
    assert "ONE IDENTIFICATION" in r["remaining_gap"]
    assert "dictionary entry, not a theorem" in r["remaining_gap"]

def test_the_error_is_owned(r):
    assert any("SECOND HIT" in n for n in r["not_claimed"])
