"""B8098 — two selection criteria are blind. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8098_L1_verified", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_object_and_its_sister_are_isovolumetric(r):
    assert r["isovolumetric"] is True and r["volume_diff"] == 0.0

def test_criterion_1_cannot_discriminate(r):
    assert r["criterion_1_can_discriminate"] is False

def test_criterion_3_cannot_discriminate_by_theorem(r):
    assert r["criterion_3_can_discriminate"] is False
    assert "commensurability invariant" in r["criterion_3_reason"]

def test_L73_falsification_confirmed(r):
    """m004 torsion-free; m003 carries Z/5 at the hearing prime."""
    assert r["m004_torsion_free"] is True and r["m003_has_Z5"] is True

def test_scope_does_not_claim_the_object_is_unselected(r):
    assert "does NOT show the object is unselected" in r["scope"] or \
           "Says nothing about the other three" in r["scope"]
