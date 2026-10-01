"""B1439 lock -- the census by slope, every signed word state to length twelve.

Sealed before any slope was computed on a new level. Recorded: the population, the eight predictions as read by the
sealed reader, the fourteen complete own-level states. Live: the control on small old levels, the shortest complete
state recomputed, and the reader re-run on the records.
"""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1439_the_census_by_slope"
V = ARC / "verification"
sys.path.insert(0, str(V))


def _rows():
    out = []
    for i in range(4):
        out += json.loads((V / f"census_by_slope_{i}.json").read_text())
    return out


def test_the_seal_is_the_file_that_was_sealed():
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text()
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() in hashes
    for name in ("census_by_slope.py", "read_census.py"):
        assert hashlib.sha256((V / name).read_bytes()).hexdigest() in hashes, f"{name} changed after the seal"
    s = ROOT / "frontier" / "B1438_the_slope_law" / "verification" / "slope_census.py"
    assert hashlib.sha256(s.read_bytes()).hexdigest() in hashes, "the slope census changed after the seal"


def test_the_population():
    r = _rows()
    assert len(r) == 988 and len({(o["state"], o["k"]) for o in r}) == 988
    assert sum(1 for o in r if o["k"] == 1) == 758
    assert sum(o["generation_backgrounds"] for o in r) == 61648
    assert sum((o["slope_coincidences_at_one_prime_only"] or 0) for o in r) == 0
    assert all(o["abs_counts"] in ({}, {"1": o["generation_backgrounds"]}) for o in r)     # one count per background


def test_the_predictions_as_read_by_the_sealed_reader():
    import read_census
    r = read_census.read(str(V))
    assert r["predictions"] == dict(E1=True, E2=True, E3=False, E4=False, E5=True, E6=False, E7=False, E8=True)
    assert r["new_levels"] == 920 and r["new_own_levels"] == 734 and r["new_own_levels_firing"] == 93
    assert r["control_levels"] == 68
    assert json.loads(json.dumps(r)) == json.loads((ARC / "census_summary.json").read_text())


def test_the_own_level_in_numbers():
    own = [o for o in _rows() if o["k"] == 1]
    fire = [o for o in own if o["generation_backgrounds"]]
    assert len(fire) == 95
    assert sum(1 for o in fire if o["state"][0] == "+") == 49
    assert sum(o["generation_backgrounds"] for o in fire) == 9376
    full = {o["state"]: c for o in fire for y, c in o["yukawa_type"].items() if json.loads(y) == [True, True, True, True]}
    assert len(full) == 14 and sum(full.values()) == 256
    assert min(full, key=lambda s: (len(s), s)) == "+LLRLRRLR"
    assert sum(1 for o in fire if o["torsion"] % 3 == 0) == 71          # E6's guess: false


def test_the_shortest_complete_state_live():
    """+LLRLRRLR at its own level: sixteen backgrounds, none lifting, every one with all four couplings"""
    import census_by_slope as cb
    r = cb.census(1, "LLRLRRLR", 1)
    assert r["torsion"] == 36 and r["N"] == 6
    assert r["generation_backgrounds"] == 16 and r["lifted"] == 0
    assert r["yukawa_type"] == {"[true, true, true, true]": 16}
    assert r["backgrounds_by_orbit_size"] == {"1": 16}


def test_the_control_live_on_small_levels():
    """the instrument returns B1434's record where B1434 computed an index"""
    import census_by_slope as cb
    rec = {(o["state"], o["k"]): o for o in json.loads((ROOT / "frontier" / "B1434_the_architecture_census" / "verification" / "architecture_census.json").read_text()) if "candidates" in o}
    for (st, k) in [("+LR", 3), ("-LLRLR", 1), ("-LLLRLR", 1), ("+LR", 1), ("-LLR", 3)]:
        r = cb.census(1 if st[0] == "+" else -1, st[1:], k)
        o = rec[(st, k)]
        assert r["generation_backgrounds"] == o["generation_backgrounds"] and r["firing"] == o["firing"] and r["lifted"] == o["lifted"]
    assert cb.census(1, "LR", 1)["generation_backgrounds"] == 0          # the root cannot, at its own level
