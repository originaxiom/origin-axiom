"""B1443 lock -- the coupling tensor of a deck orbit: one Higgs class per member.

Live: the root's three-fold cover, orbit by orbit; a level where one Higgs character serves all three members (the
check can fail); and the direct functional check that a background couples to exactly one character. Recorded: the
census of all 18 788 orbits.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1443_the_orbits_coupling_tensor"
V = ARC / "verification"
sys.path.insert(0, str(V))


def test_the_roots_three_fold_cover_live():
    import orbit_tensor as ot
    r, orbs = ot.orbits(1, "LR", 3)
    assert r["generation_backgrounds"] == 48 and len(orbs) == 16
    for o in orbs:
        assert o["size"] == 3 and o["distinct_l"] == 3
        for name in ("up", "down", "lepton", "neutrino"):
            assert o[name] == dict(distinct_higgs=3, nonzero=True), (name, o[name])


def test_the_number_can_be_less_than_the_orbit_size():
    """the bite: on the three-fold cover of -LR half the orbits have ONE Higgs character for all three members"""
    import orbit_tensor as ot
    r, orbs = ot.orbits(-1, "LR", 3)
    ups = sorted(o["up"]["distinct_higgs"] for o in orbs)
    assert len(orbs) == 32 and ups == [1] * 16 + [3] * 16


def test_a_background_couples_to_exactly_one_character_live():
    import one_higgs_per_member as oh
    r = oh.run(1, "LR", 3)
    t = r["table"]
    assert t["Q.uc | own Higgs character | functionals 1 | couples"] == 48
    assert t["Q.dc | own Higgs character | functionals 1 | couples"] == 48
    assert not any("another character" in k and k.endswith("| couples") for k in t)
    assert sum(v for k, v in t.items() if "another character" in k) == 2 * 48 * 15


def test_the_census_of_orbits_recorded():
    rows = json.loads((V / "orbit_tensor.json").read_text())
    assert len(rows) == 142 and sum(r["orbits"] for r in rows) == 18788
    three = full = one_for_all = 0
    for r in rows:
        for x in r["table"]:
            if x["size"] == 3:
                three += x["orbits"]
                full += x["orbits"] * (x["up_distinct"] == 3 and x["down_distinct"] == 3)
                one_for_all += x["orbits"] * (x["up_distinct"] == 1 or x["down_distinct"] == 1)
    assert (three, full, one_for_all) == (4904, 4464, 440)
    complete = [r["state"] for r in rows if r["k"] == 3 and all(
        x["size"] == 3 and x["up_distinct"] == 3 and x["up_nonzero"] and x["down_distinct"] == 3 and x["down_nonzero"]
        and x["neutrino_distinct"] == 3 for x in r["table"])]
    assert sorted(complete) == ["+LR", "-LLLR"]


def test_the_mass_matrix_statements():
    """pure linear algebra: y diag(v) -- equal v degenerate, one v rank one, ratios = ratios of v"""
    import numpy as np
    y = 1.5
    sv = lambda v: sorted(np.linalg.svd(y * np.diag(v), compute_uv=False))
    assert np.allclose(sv([1, 1, 1]), [1.5, 1.5, 1.5])
    assert np.allclose(sv([0, 0, 2]), [0, 0, 3.0])
    s = sv([1, 10, 100])
    assert np.allclose([s[1] / s[0], s[2] / s[1]], [10, 10])
    assert np.allclose(sv([2, 2, 2]), sorted(np.linalg.svd(y * 2 * np.eye(3), compute_uv=False)))   # one Higgs for all: degenerate


def test_no_invariant_tells_members_apart_and_the_higgs_product():
    """checked at the owner's instruction: slopes are constant along orbits; on the root's cover the product of an
    orbit's Higgs characters is trivial (a cubic joining them is character-allowed); on -LR's it is not (the bite)"""
    import higgs_product as hp
    r = hp.check(1, "LR", 3)
    assert r["slopes_along_orbit"] == {"constant": 16} and r["deck_fixed_nontrivial_characters"] == 0
    assert r["higgs_product"] == {"size 3, down: product trivial": 16, "size 3, neutrino: product trivial": 16, "size 3, up: product trivial": 16}
    q = hp.check(-1, "LR", 3)
    assert q["higgs_product"]["size 3, up: product not trivial"] == 32
    rec = json.loads((V / "higgs_product.json").read_text())
    assert all(set(o["slopes_along_orbit"]) == {"constant"} for o in rec)
    assert all("not trivial" not in k for o in rec if o["state"] == "+LR" for k in o["higgs_product"])
