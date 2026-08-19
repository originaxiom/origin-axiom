"""B8087 — the neutrino selector is a condition, not a point. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8087_neutrino_selector", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_algebra_is_so10_on_the_16(r):
    assert r["dim_so10"] == 45 and r["rank_so10"] == 5 and r["dim_16"] == 16

def test_purity_is_the_unique_rank_four_condition(r):
    """The load-bearing fact: pure gives rank 4, generic destroys the rank outright."""
    assert r["pure"]["rank_after_breaking"] == 4
    assert r["generic"]["rank_after_breaking"] == 0
    assert r["purity_is_the_unique_rank4_condition"] is True

def test_the_pure_stabiliser_is_sl5_semidirect_lambda2(r):
    assert r["pure"]["stab_dim"] == 34 == 24 + 10
    assert r["pure"]["orbit_dim"] == 11

def test_spin10_is_transitive_on_the_pure_cone(r):
    """Orbit dim equals the cone dim (spinor variety S_10 is 10-dim projectively)."""
    assert r["orbit_equals_cone_dim"] is True
    assert r["pure"]["orbit_dim"] == 10 + 1

def test_the_generic_spinor_is_a_real_negative_control(r):
    assert r["generic"]["stab_dim"] != r["pure"]["stab_dim"]
    assert r["generic"]["orbit_dim"] == 16

def test_the_second_vev_is_a_free_choice_not_forced(r):
    assert r["second_vev_is_a_free_choice"] is True

def test_scope_names_the_pair_reading(r):
    assert "PAIRS" in r["scope"] and "Gate 5 untouched" in r["scope"]
