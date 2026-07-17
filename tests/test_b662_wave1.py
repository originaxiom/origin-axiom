"""B662 wave-1 locks (campaign prereg 41f8d5ec; cells A, C, D, E).

Fast locks: artifact-level assertions + this seat's independent
re-derivations (the cellC real-structure identity from the persisted
JSON alone; the cellD checkerboard parity from the banked silver
letters). Heavy re-runs live in the cell dirs' scripts.
"""
import json
import os
from fractions import Fraction as Fr

_C = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B662_successor_campaign")


def test_cell_a_l101_output():
    out = open(os.path.join(_C, "cellA", "cellA_output.txt")).read()
    assert out.count("PASS") >= 30 and "FAIL" not in out
    note = open(os.path.join(_C, "cellA", "PROOF_NOTE.md")).read()
    assert "i" in note and "Lemma" in note


def test_cell_c_real_structure_from_json_alone():
    d = json.load(open(os.path.join(_C, "cellC",
                                    "sigma_matrix_golden.json")))
    M = d["matrix"]
    n = len(M)

    def mul(a, b):
        return (a[0] * b[0] - 3 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])

    for i in range(n):
        for j in range(n):
            s0, s1 = Fr(0), Fr(0)
            for k in range(n):
                a = (Fr(M[i][k][0]), -Fr(M[i][k][1]))   # conj
                b = (Fr(M[k][j][0]), Fr(M[k][j][1]))
                p = mul(a, b)
                s0 += p[0]
                s1 += p[1]
            assert (s0, s1) == ((Fr(1) if i == j else Fr(0)), Fr(0))


def test_cell_d_checkerboard_parity_banked_letters():
    p = os.path.join(os.path.dirname(__file__), "..", "frontier",
                     "B649_silver_holonomy", "entries_L.json")
    d = json.load(open(p))

    def degs(entry):
        out = set()
        for grp in entry:
            for deg, c in enumerate(grp):
                if Fr(c) != 0:
                    out.add(deg % 2)
        return out

    for g, want_diag in (("a", {1}), ("b", {0}), ("c", {1})):
        for pos in ("00", "11"):
            assert degs(d[g + pos]) <= want_diag
        for pos in ("01", "10"):
            assert degs(d[g + pos]) <= (want_diag ^ {0, 1})


def test_cell_e_l102_verdict():
    v = json.load(open(os.path.join(_C, "cellE", "cellE_verdict.json")))
    assert v["golden_control_pass"] is True
    assert v["silver_block_diagonal_canonical"] is True
    assert "BLOCK-DIAGONAL" in v["verdict"]


def test_cell_b_qblock_78():
    d = json.load(open(os.path.join(_C, "cellB", "qblock_78.json")))
    assert d["verdict"] == "CONFIRMED-(0,6)"
    f = d["fox"]
    assert (f["h0"], f["h1"]) == (0, 6)
    per = d.get("per_block", d.get("blocks", []))
    if per:
        assert all(b["h1"] == 1 and b["h0"] == 0 for b in per)
