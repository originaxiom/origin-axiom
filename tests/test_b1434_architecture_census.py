"""B1434 lock -- the architecture census.

Sealed before any index was computed off the root. These assertions pin the outcomes of the seven predictions on the
recorded census, and recompute live the two states that carry a generation-shaped background at their own level --
with a control (the root, which cannot) and the bite that the own-level count is not a constant of the code.
"""
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1434_the_architecture_census" / "verification"
sys.path.insert(0, str(V))


def _rows():
    return json.loads((V / "architecture_census.json").read_text())


def test_the_seal_is_the_file_that_was_sealed():
    import hashlib
    h = hashlib.sha256((V.parent / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert h in (V.parent / "ARTIFACT_HASHES.txt").read_text()
    s = hashlib.sha256((V / "architecture_census.py").read_bytes()).hexdigest()
    assert s in (V.parent / "ARTIFACT_HASHES.txt").read_text(), "the instrument changed after the seal"


def test_population_and_agreement_across_primes():
    r = _rows()
    assert len(r) == 68 and sum(o["candidates"] for o in r) == 942268
    assert sum(o["differing_at_other_primes"] for o in r) == 0
    assert all(o["index_deck_invariant"] and o["background_orbits_closed"] for o in r)


def test_p1_p2_p6_one_count_per_background_everywhere():
    r = _rows()
    absI, h1 = Counter(), Counter()
    for o in r:
        for k, v in o["abs_counts"].items():
            absI[int(k)] += v
        for k, v in o["h1_multiset"].items():
            h1[int(k)] += v
    assert dict(absI) == {1: 8800} and dict(h1) == {1: 5156}
    assert all(len(set(o["signs"].values())) == 1 for o in r if o["generation_backgrounds"])


def test_p3_two_states_fire_at_their_own_level_recorded():
    own = {o["state"]: (o["generation_backgrounds"], o["lifted"]) for o in _rows() if o["k"] == 1 and o["generation_backgrounds"]}
    assert own == {"-LLRLR": (8, 0), "-LLLRLR": (16, 16)}


def test_p3_live_with_control_and_bite():
    """m369 and s639 recomputed; the root gives none; the neighbour (+, LLRLR) gives none -- the count is measured"""
    import architecture_census as ac
    got = {}
    for eps, w in ((-1, "LLRLR"), (-1, "LLLRLR"), (+1, "LR"), (+1, "LLRLR")):
        o = ac.census(eps, w, 1)
        got[o["state"]] = (o["torsion"], o["firing"], o["generation_backgrounds"], o["lifted"])
    assert got["-LLRLR"] == (12, 40, 8, 0)
    assert got["-LLLRLR"] == (15, 72, 16, 16)
    assert got["+LR"] == (1, 0, 0, 0)
    assert got["+LLRLR"] == (8, 12, 0, 0)


def test_p3_exact_and_second_presentation_recorded():
    d = json.loads((V / "own_level_checks.json").read_text())
    ex = {e["state"]: e for e in d["exact"]}
    assert ex["-LLRLR"]["identical_to_prime_field_table"] and ex["-LLRLR"]["firing_exact"] == 40
    assert ex["-LLLRLR"]["identical_to_prime_field_table"] and ex["-LLLRLR"]["firing_exact"] == 72
    sn = {e["manifold"]: e for e in d["snappy"]}
    assert (sn["m369"]["generation_backgrounds"], sn["m369"]["lifted"]) == (8, 0)
    assert (sn["s639"]["generation_backgrounds"], sn["s639"]["lifted"]) == (16, 16)
    assert sn["m004"]["generation_backgrounds"] == 0 and sn["m003"]["generation_backgrounds"] == 0


def test_p4_p5_three_fold_levels():
    k3 = {o["state"]: (o["generation_backgrounds"], o["lifted"], o["backgrounds_by_orbit_size"]) for o in _rows() if o["k"] == 3}
    assert len(k3) == 12
    assert {s for s, v in k3.items() if v[0] == 0} == {"-LLR", "+LLRR"}                     # P4 NO: ten of twelve
    assert all(set(v[2]) == {"3"} for v in k3.values() if v[0])                            # every one an orbit of three
    assert k3["+LR"] == (48, 0, {"3": 48}) and k3["-LR"] == (96, 0, {"3": 96})
    assert {s for s, v in k3.items() if v[1]} == {"+LLR", "-LLRR", "+LLLLR", "-LLLLR", "+LLLLLR"}   # P5 NO


def test_p7_size_one_orbits_are_the_own_level_pullbacks():
    r = _rows()
    one = {(o["state"], o["k"]) for o in r if o["k"] > 1 and "1" in o["backgrounds_by_orbit_size"]}
    assert one == {("-LLRLR", 2), ("-LLLRLR", 2)}
    assert all(o["k"] % int(s) == 0 for o in r for s in o["backgrounds_by_orbit_size"])


def test_one_manifold_two_decks():
    r = {(o["state"], o["k"]): o for o in _rows()}
    assert r[("+LR", 6)]["backgrounds_by_orbit_size"] == {"6": 2112, "3": 48}
    assert r[("-LR", 6)]["backgrounds_by_orbit_size"] == {"6": 2064, "3": 96}
    assert r[("+LR", 6)]["generation_backgrounds"] == r[("-LR", 6)]["generation_backgrounds"] == 2160
