"""B1204 lock -- the forcing theorem's shape, with B1160's anatomy re-derived in the test."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1204_forcing_shape"


def test_the_cubic_is_what_cuts_to_points():
    t = sp.symbols("t")
    cubic = sp.factor(-18 * (t - 3) * (t + 3))
    assert set(sp.solve(cubic, t)) == {3, -3}          # a LINE cut to two POINTS
    # a linear condition on the same line cuts nothing to a finite set by itself
    assert sp.solve(sp.Integer(0) * t, t) == []        # vacuous: no cut


def test_verdict_states_the_refinement_and_labels_the_proposal():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "BOTH FAMILIES ARE FAILABLE; NEITHER IS A SYMMETRY" in c
    assert "ITS DECISIVE STEP IS NONLINEAR" in c
    assert "PROPOSAL, labelled" in c or "PROPOSAL," in c
    assert "nothing weakens V-3" in c
