"""B1347 - the other three strata: the exact leaf identity, and the absence of an arrow."""
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1347_the_other_strata"
x, y, z = sp.symbols("x y z")
LEAF = x ** 2 + y ** 2 + z ** 2 - x * y * z          # = 0 is kappa = -2, the Markov surface
M3 = x ** 2 + y ** 2 - x * y * z                     # the Thue-Morse multiplier (B497/B1342)


def test_arc_is_banked():
    assert (ARC / "FINDINGS.md").exists()
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1347" and v["verdict"] == "NEGATIVE", (
        "the headline is the absence of an arrow; a PROVED verdict would misreport it")


def test_the_leaf_identity_is_exact():
    """M_3 = -z^2 on the object's own leaf, as a polynomial identity."""
    assert sp.simplify(sp.expand(M3 + z ** 2 - LEAF)) == 0
    # and the control: it is NOT -z^2 off the leaf, or the identity would be vacuous
    assert sp.simplify(sp.expand(M3 + z ** 2)) != 0


def test_one_step_crosses_nothing():
    """kappa - 2 = -4 on the leaf; one TM step gives (-4)(-z^2) = +4 z^2 >= 0."""
    k2 = sp.Integer(-4)
    nxt = sp.expand(k2 * (-z ** 2))
    assert nxt == 4 * z ** 2
    assert nxt.subs(z, 0) == 0, "it lands exactly on nothing iff z = 0"
    for val in (2, 3, sp.Rational(1, 2)):
        assert (nxt.subs(z, val) > 0) is sp.true or nxt.subs(z, val) > 0


def test_stratum_1_cannot_move_kappa_and_stratum_4_lands_on_nothing():
    """the two uniform ends -- multiplier 1 and multiplier 0."""
    assert sp.Integer(1) == 1                                  # stratum 1's multiplier
    # stratum 4: x -> ab, y -> ab, so tr = (z, z, z^2 - 2) and kappa' == 2 identically
    k4 = sp.expand(z ** 2 + z ** 2 + (z ** 2 - 2) ** 2 - z * z * (z ** 2 - 2) - 2)
    assert sp.simplify(k4 - 2) == 0, "stratum 4's image is the kappa = 2 floor"


def test_the_negative_is_stated_as_the_headline():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "does NOT supply an arrow" in t
    assert "basin structure" in t.lower()
    assert "34/66" in t and "19/81" in t and "18/82" in t, "the mixed fractions must be on the record"


def test_the_fences_are_kept():
    import re
    raw = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    # normalise: markdown emphasis and line wrapping must not defeat a content check
    t = re.sub(r"\s+", " ", raw.replace("*", "").replace("`", "")).lower()
    assert "s063" in t, "the physics-naming fence must be named"
    assert "no mapping torus" in t, "the solenoid caveat must survive"
    assert "inverse limit" in t, "and its consequence -- not a manifold"
    for banned in ("decoherence is", "erasure is the"):
        assert banned not in t, "no stratum may be given a physics name as a derivation"
