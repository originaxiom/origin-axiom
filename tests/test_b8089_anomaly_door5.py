"""B8089 — the anomaly layer over the derived content is identically zero. Reads results.json."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8089_anomaly_door5", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_second_route_is_independent(r):
    """All 16 hypercharges re-derived from su(5) alone; no SM table is load-bearing."""
    assert r["route2_reproduces_route1"] is True and r["n_states"] == 16

def test_every_gauge_anomaly_vanishes_over_the_derived_16(r):
    assert all(v == "0" for v in r["gauge_anomalies_16"].values())

def test_the_instrument_can_detect_an_anomaly(r):
    """A cancellation check that cannot detect an anomaly is not a check."""
    assert set(r["bite_control_nonzero"]) == {"U(1)^3", "U(1)-grav"}

def test_nu_c_is_exactly_what_cancels_B_minus_L(r):
    assert r["BL_anomaly_free_over_16"] is True
    assert r["BL_anomalous_over_15"] is True
    assert r["BL_15"]["U(1)^3"] == "-1" and r["BL_15"]["U(1)-grav"] == "-1"

def test_the_z6_congruence_has_a_unique_solution(r):
    assert r["z6_consistent"] is True and r["z6_solutions"] == [[4, 3]]

def test_the_layer_is_identically_zero_so_no_ratio_exists(r):
    """The load-bearing negative: door 5's ask is structurally unanswerable."""
    assert r["n_nonvanishing_invariants"] == 0
    assert r["anomaly_layer_identically_zero"] is True
    assert r["outcome"] == "B"

def test_scope_keeps_the_scale_lane_closed(r):
    assert "scale lane" in r["scope"] and "NO value compared" in r["scope"]
