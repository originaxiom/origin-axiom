"""B666 wave 0+1 + cell S locks (artifact-level; the heavy re-runs
live in the cell scripts)."""
import os

_C = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B666_leads_campaign")


def _read(*p):
    return open(os.path.join(_C, *p)).read()


def test_cell_t_triage_table():
    t = _read("cellT", "TRIAGE_TABLE.md")
    assert "SUPERSEDED" in t and "REVIVAL" in t.upper()


def test_cell_1_group_side_verdict():
    t = _read("cell1", "b666c1_shadow_log.txt")
    assert "order 384" in t and "2O as quotient: True" in t
    assert "2O as subgroup: False" in t


def test_cell_3_e6_landscape():
    t = _read("cell3", "cell3_output.txt")
    assert "ALL GATES PASS" in t or "GATES PASS" in t.upper()


def test_cell_4_proof_note():
    t = _read("cell4", "PROOF_NOTE.md")
    assert "square" in t.lower()
    out = _read("cell4", "cell4_output.txt")
    assert "FAIL" not in out


def test_cell_6_tickets():
    t = _read("cell6", "cell6_output.txt")
    assert "610/610" in t
    assert "0.16" in t          # the corrected value discussed


def test_cell_s_rigidity():
    t = _read("cellS", "cellS_output.txt")
    assert "51840" in t and "FAIL" not in t
    n = _read("cellS", "PROOF_NOTE.md")
    assert "torsor" in n.lower()
