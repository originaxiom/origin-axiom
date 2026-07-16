"""B652 locks — GATE B's table and verdict integrity."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B652 = os.path.join(HERE, "..", "frontier", "B652_gate_b")


def test_table_and_verdict():
    t = open(os.path.join(B652, "GRAMMAR_TABLE.md")).read()
    v = open(os.path.join(B652, "GATE_B_VERDICT.md")).read()
    # the one freedom, stated identically in both
    assert "orbit size 2" in t and "orbit size 2" in v
    assert "N = 1, discrete" in v
    # the quotient cites proven identities
    assert "disc(A₁) = 5" in t and "B644" in t and "B651 P1/P2" in t
    # the residues are named
    assert "A3" in v and "A4" in v and "BOUNDED" in v
    # the verdict
    assert "PASS, with the two residues" in v
    assert "PAUSES HERE FOR THE OWNER" in v
    # no SM quantities anywhere in the gate documents
    for bad in ("PMNS value", "mass ratio =", "GeV", "eV"):
        assert bad not in t and bad not in v


def test_no_row_overclaims_strength():
    t = open(os.path.join(B652, "GRAMMAR_TABLE.md")).read()
    # the core-ratio row must NOT be labeled FORCED (gauge adjudication)
    import re
    row = [ln for ln in t.splitlines() if "24ζ₆" in ln]
    assert row and "CONVENTION" in row[0]
    lit = [ln for ln in t.splitlines() if "lit/silent class" in ln]
    assert lit and "COMPUTED" in lit[0]
