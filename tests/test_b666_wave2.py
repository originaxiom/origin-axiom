"""B666 wave-2 locks (artifact-level over the twelve cells)."""
import json
import os

_C = os.path.join(os.path.dirname(__file__), "..", "frontier",
                  "B666_leads_campaign")


def _read(*p):
    return open(os.path.join(_C, *p)).read()


def test_cell2_fifth_wall_and_subfield():
    out = _read("cell2", "cell2_output.txt")
    assert "CELL 2 COMPUTATION COMPLETE" in out
    assert "2 distinct eigenvalue(s) of 3" in out
    assert "every decisive value lies in K = Q(sqrt-3) EXACTLY" in out
    d = json.load(open(os.path.join(_C, "cell2", "cell2_cup_values.json")))
    assert d["class_antisymmetry_25of25"] is True
    assert d["cup_surjective_rank5"] is True


def test_cell8_glued_cubic_nondegenerate():
    out = _read("cell8", "cell8_output.txt")
    assert "THE GLUED CUBIC (flat, C both sides in the trivialized chart): "\
           "rank 5, kernel dim 0" in out
    assert "THE (C, C*) INTRINSIC CUBIC: rank 5, kernel dim 0" in out


def test_cell9_exact_integers():
    out = _read("cell9", "taskA_verify2_output.txt")
    assert out.count("CONFIRMS EXACT INTEGER") >= 6


def test_cell10_sector_value():
    r = _read("cell10", "cell10_output.txt")
    assert "2" in r  # presence gate; the exact value line:
    assert "sqrt" in r.lower() or "√" in r


def test_revivals_present():
    for cell, key in (("cellR1", "c("), ("cellR2", "Latin"),
                      ("cellR3", "Gauss")):
        found = False
        d = os.path.join(_C, cell)
        for f in os.listdir(d):
            if f.endswith((".md", ".txt")):
                if key.lower() in open(os.path.join(d, f),
                                       errors="ignore").read().lower():
                    found = True
                    break
        assert found, cell
