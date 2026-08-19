"""B8091 — the first step's two losses. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8091_first_step_losses", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_monodromy_is_the_square_of_the_substitution_matrix(r):
    assert r["M"] == [[1, 1], [1, 0]] and r["M2"] == [[2, 1], [1, 1]]
    assert r["monodromy_is_the_square"] is True and r["trace_M2"] == 3

def test_order_is_invisible_to_the_incidence_matrix(r):
    """a->ab and a->ba are different rules with the same matrix."""
    assert r["order_is_invisible"] is True and r["M"] == r["M_mirror"]

def test_the_order_blindness_is_not_vacuous(r):
    assert r["bite_nonvacuous"] is True

def test_squaring_erases_the_sign_and_is_forced(r):
    assert r["det_M"] == -1 and r["det_M2"] == 1
    assert r["squaring_forced_by_orientability"] is True

def test_the_identification_is_marked_unproved(r):
    """The mechanism is proved; which loss carries which bit is not."""
    assert "UNPROVED" in r["losses"]["order"] and "UNPROVED" in r["losses"]["sign"]
    assert "Does NOT prove the IDENTIFICATION" in r["scope"]
