"""B8090 — the banked 'character' is not one. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8090_cold_audit_f1", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_sign_lambda_sq_is_minus_one_at_the_identity(r):
    assert r["sign_lambda_sq"]["I"] == -1

def test_and_therefore_is_not_a_character(r):
    """A character sends e to +1; this fails multiplicativity on every product."""
    assert r["sign_is_homomorphism"] is False
    assert r["n_failed_products"] == 16

def test_the_corrected_object_IS_a_character(r):
    assert r["correct_is_homomorphism"] is True
    assert r["correct_character"] == {"I": 1, "chi_a": 1, "chi_b": -1, "D2": -1}

def test_the_banked_polarity_is_inverted(r):
    assert r["banked_polarity_matches_character"] is False

def test_the_defect_is_summary_layer_only(r):
    assert "summary-layer only" in r["defect"]
    assert set(r["surfaces_affected"]) == {"FINDINGS.md", "arc_verdict.json", "CHANGELOG.md"}
