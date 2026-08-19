"""B8085 — Route A: the arithmetic obstruction is absent. Reads results.json, never prose."""
import json, os, pytest
RES=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","frontier",
                 "B8085_integral_orbits","results.json")

@pytest.fixture(scope="module")
def r():
    with open(RES) as fh: return json.load(fh)

def test_the_field_is_the_charge_field(r):
    """A class group of the wrong field is worthless."""
    assert r["disc"]==6237 and r["signature"].replace(" ","")=="[3,0]"

def test_every_candidate_counter_is_trivial(r):
    """The point of computing all four: the conclusion must not depend on which governs."""
    assert r["all_counters_trivial"] is True
    assert all(v==1 for v in r["candidate_counters"].values())

def test_the_narrow_class_number_is_the_new_part(r):
    """h=1 was already banked; h+ is what this arc computed."""
    assert r["h_narrow"]==1 and r["h_narrow_independent"]==1

def test_two_engines_agree(r):
    assert r["h_narrow"]==r["h_narrow_independent"]

def test_the_mechanism_is_signature_surjectivity(r):
    """h+ = h*2^r1/|image|; surjectivity is why it collapses to 1."""
    assert r["signature_surjective"] is True and r["signature_rank_F2"]==3

def test_the_prior_is_recorded_as_not_held(r):
    """B990's prior was UNFAVOURABLE. Recording that it failed is the finding."""
    assert "UNFAVOURABLE" in r["prior"]
    assert r["prior_held"] is False

def test_scope_does_not_overclaim(r):
    """The arc must not claim the orbit count IS 1, nor h=1 as its own finding."""
    s=r["scope"]
    assert "owed" in s and "does NOT claim" in s
