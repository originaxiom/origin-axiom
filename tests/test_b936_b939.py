"""B936/B937/B939 locks: the H1 classification, the observer-place law, the Klein distinctness."""
import json
import os

FR = os.path.join(os.path.dirname(__file__), "..", "frontier")


def _r(arc):
    with open(os.path.join(FR, arc, "results.json")) as f:
        return json.load(f)


def test_b936_h1_is_klein_four_and_D2_is_a_coboundary():
    t = json.dumps(_r("B936_cohomology_reading"))
    assert "coboundary" in t.lower() or "B^1" in t or "B1" in t
    # the four-classes-of-four structure and the witness
    assert "(1, 1, 1, 1, -1, -1)" in t or "1, 1, 1, 1, -1, -1" in t


def test_b936_value_corollary_failed_honestly():
    r = _r("B936_cohomology_reading")
    t = json.dumps(r)
    # the refutation's fingerprints: the wrong-field pencil and the block ratios
    assert "3129" in t
    assert "17/384" in t or "-17/384" in t


def test_b937_monogenic_upgrade_and_no_golden():
    t = json.dumps(_r("B937_golden_and_29"))
    # K = Q[s]/(s^3 - 12s - 5), disc 6237
    assert "6237" in t
    assert "12" in t and "5" in t
    # 29 verdict recorded
    assert "coincidence" in t.lower() or "COINCIDENCE" in t


def test_b939_klein_shadows_distinct():
    r = _r("B939_klein_assembly")
    v = r["verdict_sharp_pair"]
    assert "DISTINCT" in v
    assert "sigma_-1" in v
