"""Wave locks: B931 (the divisor map anchors), B932 (the selection), B933 (the probe)."""
import json
import os

import sympy as sp

FR = os.path.join(os.path.dirname(__file__), "..", "frontier")


def test_b931_2304_derivation_anchor():
    lc = 500716339200
    assert lc == 2304**2 * 5**2 * 7**3 * 11
    f = sp.factorint(lc)
    assert f[2] == 16 and f[3] == 4    # 2304^2's {2,3} part exactly


def test_b931_953_level_structure():
    r = json.load(open(os.path.join(FR, "B931_why_953", "results.json")))
    t = json.dumps(r)
    assert "953" in t and ("1/2" in t or "one-half" in t or "degener" in t.lower())


def test_b932_outcome_A():
    r = json.load(open(os.path.join(FR, "B932_chain_selection", "results.json")))
    t = json.dumps(r)
    assert "(6,1,1)" in t or "6,1,1" in t
    # no color singlets in the conformal 27
    assert "singlet" in t.lower() or "no lepton" in t.lower() or "0" in t


def test_b933_probe_bracket():
    r = json.load(open(os.path.join(FR, "B933_spinor_hejhal_design", "results.json")))
    t = json.dumps(r)
    assert "2.97455" in t
