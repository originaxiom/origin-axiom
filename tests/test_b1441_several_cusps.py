"""B1441 lock -- the class index of rank-two non-split modules on manifolds with several cusps.

Sealed before any such index was computed. Recorded: the population, the seven predictions as read by the sealed
reader, the seventeen carriers of |I| = 2 and their exact confirmation. Live: one carrier recomputed with B1333's
code and exactly over Q, one root cover that stays at one, and the one-cusp control.
"""
import hashlib
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1441_the_several_cusped_levels"
V = ARC / "verification"
sys.path.insert(0, str(V))
snappy = pytest.importorskip("snappy")


def _rows():
    out = []
    for i in range(6):
        out += json.loads((V / f"several_cusps_{i}.json").read_text())
    return out


def test_the_seal_is_the_file_that_was_sealed():
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text()
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() in hashes
    for name in ("several_cusps.py", "read_several.py"):
        assert hashlib.sha256((V / name).read_bytes()).hexdigest() in hashes, f"{name} changed after the seal"


def test_the_population_and_the_identities():
    r = _rows()
    assert len(r) == 79 and len({o["tag"] for o in r}) == 79
    run = [o for o in r if "skipped" not in o]
    assert len(run) == 76 and sum(o["modules"] for o in run) == 564742
    assert sum(o["rechecks_differing"] for o in run) == 0


def test_the_predictions_as_read_by_the_sealed_reader():
    import read_several
    s = read_several.read(str(V))
    assert s["predictions"] == dict(M1=True, M2=False, M3=True, M4=False, M5=False, M6=True, M7=True)
    assert s["max_abs_I"] == 2
    assert json.loads(json.dumps(s)) == json.loads((ARC / "several_cusps_summary.json").read_text())
    assert read_several.read(str(V)) == s                                  # the reader can be run twice


def test_seventeen_carriers_all_exact_and_none_on_the_roots_covers():
    run = [o for o in _rows() if "skipped" not in o]
    car = [o for o in run if o["max_abs_I"] >= 2]
    assert len(car) == 17 and {o["root"] for o in car} == {"m009", "m010"}
    assert max(o["max_abs_I"] for o in run if o["root"] in ("m004", "m003")) == 1
    assert sum(v for o in run for k, v in o["I_hist"].items() if k in ("2", "-2")) == 344
    ex = json.loads((ARC / "exact_several.json").read_text())
    assert len(ex) == 17 and all(o["exact_max_abs_I"] == 2 for o in ex)
    assert {o["tag"] for o in ex} == {o["tag"] for o in car}


def test_the_named_manifolds():
    named = {o["tag"]: o for o in _rows() if o["degree"] is None}
    for tag in ("m202", "m202 N=12", "s959", "s959 N=12", "m125", "m125 N=12"):
        assert named[tag]["max_abs_I"] == 0, tag
    assert named["m129 N=12"]["I_hist"] == {"-1": 16, "0": 3092, "1": 16}
    assert named["o10_150726 N=12"]["max_abs_I"] == 1


def test_one_carrier_live_and_exact():
    """m009 deg 6 #21, three cusps, sign characters: I = 2 by B1333's code and exactly over Q"""
    import several_cusps as sc
    import exact_mc as ex
    C = sc.get("m009", 6, 21)
    assert C.num_cusps() == 3
    r = sc.census(C)
    assert r["N"] == 2 and r["max_abs_I"] == 2 and r["I_hist"]["2"] == r["I_hist"]["-2"] == 11
    w = [x for x in r["witnesses"] if x["l"] == [0, 0, 0, 1] and x["alpha"] == [0, 1, 0, 0]][:1]
    assert w and w[0]["I"] == 2
    out = ex.verify("m009 deg 6 #21", "m009", 6, 21, None, w, limit=1)
    assert [e["I"] for e in out[0]["exact"]] == [2, 2, 2, 2, 2]


def test_a_cover_of_the_root_stays_at_one_and_the_one_cusp_control():
    import several_cusps as sc
    r = sc.census(sc.get("m004", 5, 2))                                    # three cusps
    assert r["cusps"] == 3 and r["max_abs_I"] == 1
    c = sc.census(snappy.Manifold("m004").covers(3, cover_type="cyclic")[0])
    assert c["cusps"] == 1 and c["I_hist"] == {"-1": 36, "0": 858, "1": 36}   # the banked 72 of s961; B1440's one
