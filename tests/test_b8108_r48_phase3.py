"""B8108 — R48 phase 3. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8108_r48_phase3", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_candidate_list_is_bounded(r):
    assert r["candidates_in"] == 36
    assert r["correctly_handled_banner"] == 13
    assert r["genuinely_untriaged"] == 21

def test_the_worst_lags_are_correctly_handled(r):
    """The four biggest lags carry banners -- not defects."""
    assert "ARCHITECTURE.md" in r["handled_paths"]
    assert "docs/ROADMAP_TOE.md" in r["handled_paths"]

def test_the_remedy_is_a_banner_not_a_rewrite(r):
    assert "BANNER, not a rewrite" in r["general_remedy"]

def test_the_instrument_declares_its_own_false_positives(r):
    """The discriminator is itself a candidate-generator."""
    assert "BANKING_PROTOCOL" in r["caveat_on_own_instrument"]
    assert "candidate-generator too" in r["caveat_on_own_instrument"]

def test_the_review_reports_and_does_not_repair(r):
    assert r["no_document_edited"] is True
