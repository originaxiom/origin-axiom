"""B1473 -- the three kinds cover a third at most: the census re-combined from the readers' tables, the population and
the quotes re-verified, and the FACE-ONLY discriminator asserted on the kill graph itself."""
import json, os, subprocess, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1473_the_three_kinds_cover_a_third_at_most", "verification")


def test_census_recomputed_from_the_readers_tables():
    for s in ("aggregate.py", "combine.py"):
        r = subprocess.run([sys.executable, os.path.join(V, s)], capture_output=True, text=True, cwd=V); assert r.returncode == 0, r.stderr[-400:]
    c = json.load(open(os.path.join(V, "census.json"))); f = json.load(open(os.path.join(V, "census_final.json")))
    assert c["entries"] == 460 and c["verified"] == 460 and c["discarded"] == []
    assert c["by_kind"] == {"OTHER": 306, "PAIRING": 24, "NON-UNIQUENESS": 98, "FLATNESS": 32}
    assert f["population"] == 460 and f["three_kinds_first"] == 154 and f["core"] == 84 and f["core_plus_fitted"] == 103
    assert f["adversarial_confirmed"] == {"PAIRING": 16, "NON-UNIQUENESS": 51, "FLATNESS": 17}


def test_face_only_records_are_not_kills():
    kg = json.load(open(os.path.join(ROOT, "frontier", "B738_pathfinder_compiler", "kill_graph.json")))
    empty = [e for e in kg if not e.get("claim_killed")]
    # the discriminator holds on the live graph (later kills may be added; FACE-ONLY records carry no claim text)
    assert all(e.get("priority") == "FACE-ONLY" for e in empty) and all(e.get("priority") != "FACE-ONLY" for e in kg if e.get("claim_killed"))
    assert len(empty) >= 343 and len(kg) - len(empty) >= 460
    # the census population is the snapshot the readers read (frozen in the arc)
    snap = sum(1 for i in range(8) for e in json.load(open(os.path.join(V, "readers", "batch_%d.json" % i))) if e["claim_killed"])
    assert snap == 460
