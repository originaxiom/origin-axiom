"""B8103 — the specialist register revisited. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8103_specialist_revisit", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_thesis_is_that_gates_have_dates(r):
    assert "HAS A DATE" in r["thesis"]

def test_two_of_seven_are_literature_gates(r):
    assert r["register_items"] == 7
    assert len(r["not_actually_specialist_gates"]) == 2

def test_no_E6_character_variety_work_exists(r):
    assert r["E6_work_found"] is False
    assert r["exceptional_group_character_variety_work_found"] is False
    assert r["novelty_claim_survives"] is True

def test_the_gate_is_substantially_discharged(r):
    assert "SUBSTANTIALLY DISCHARGED" in r["gate_status"]
    assert "not a specialist wall" in r["gate_status"]

def test_the_other_rows_are_NOT_claimed_expired(r):
    """B391 untested; four are genuine walls."""
    assert any("B391" in n for n in r["not_claimed"])
    assert r["next_revisit"].startswith("B391")
