"""B8092 — the design audit. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8092_design_audit", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_no_intentional_bias_and_the_arithmetic_was_clean(r):
    """The headline both ways: no bias found, recomputations reproduced."""
    assert r["intentional_bias_found"] is False
    assert r["arithmetic_recomputations_clean"] is True

def test_three_findings_each_one_directional(r):
    assert len(r["findings"]) == 3
    assert all(f["can_only"] == "remove candidates" for f in r["findings"])

def test_the_headline_finding_was_not_named_by_cc(r):
    f = [x for x in r["findings"] if x.get("headline")][0]
    assert f["id"] == 1 and f["named_by_cc"] is False
    assert "Re h" in f["condition_disqualifies"]
    assert "any coupling-channel quantity" in f["prompt_disqualifies"]

def test_ccs_third_probe_is_confirmed_sound(r):
    assert r["cc_probe_iii_gate5_classes_only"].startswith("SOUND")

def test_the_audit_does_not_claim_the_negatives_are_wrong(r):
    """The distinction the finding rests on."""
    assert r["shows_negatives_are_wrong"] is False
    assert r["shows_design_could_not_have_found_a_positive"] is True

def test_scope_disclaims_the_arithmetic(r):
    assert "NOT a re-audit of the arithmetic" in r["scope"]
