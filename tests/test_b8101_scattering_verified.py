"""B8101 — the scattering determinant verified. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8101_scattering_verified", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_completion_is_right(r):
    assert r["functional_equation_worst_err"] < 1e-25

def test_the_H3_unitarity_condition_holds(r):
    """phi(s)phi(2-s)=1 -- the THREE-dimensional condition, not the 2d one."""
    assert r["unitarity_worst_err"] < 1e-25
    assert "s(2-s)" in r["unitarity_condition"]

def test_phi_at_the_symmetric_point_is_minus_one(r):
    assert r["phi_at_symmetric_point"] == -1.0
    assert r["one_minus_phi1"] == 2.0

def test_the_integrand_is_real_on_the_critical_line(r):
    assert r["integrand_real_on_critical_line"] is True

def test_five_of_seven_in_hand(r):
    assert r["n_in_hand"] == 5 and r["n_total"] == 7

def test_the_gap_is_one_named_function(r):
    assert "test function h(r)" in r["what_is_missing"] or "h(r)" in r["what_is_missing"]
