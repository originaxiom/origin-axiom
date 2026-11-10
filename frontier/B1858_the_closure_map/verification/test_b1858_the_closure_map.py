"""B1858 -- the closure map is what its builder generates from the record, and every pin checks.

The builder reads main's files in this checkout and, where this clone holds them, the seat branches' pinned revisions.
A fresh clone without the seat branches still checks every pin on main and the map's own consistency; the seat pins are
then counted as unavailable, not passed."""
import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
spec = importlib.util.spec_from_file_location("b1858_build_map", HERE / "build_map.py")
bm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bm)
NODES, EDGES, STATS, FAILS, NOTES, ROWS = bm.build()


def test_every_pin_checks_and_the_map_is_consistent():
    assert FAILS == [], FAILS[:5]
    assert STATS["pins_checked_on_main"] >= 240
    assert STATS["pins_checked_on_seat_branches"] + STATS["seat_pins_unavailable_in_this_clone"] == 39
    if STATS["seat_pins_unavailable_in_this_clone"] == 0:
        assert STATS["pins_checked_on_seat_branches"] == 39


def test_the_committed_files_are_the_builders_output():
    assert json.loads((ARC / "NODES.json").read_text(encoding="utf-8")) == json.loads(json.dumps(NODES, ensure_ascii=False))
    assert json.loads((ARC / "EDGES.json").read_text(encoding="utf-8")) == json.loads(json.dumps(EDGES, ensure_ascii=False))
    assert (ARC / "MAP.md").read_text(encoding="utf-8") == bm.render_map(NODES, EDGES, STATS)
    assert (ARC / "CLOSURE_QUEUE.md").read_text(encoding="utf-8") == bm.render_queue(NODES, EDGES, STATS, ROWS)


def test_the_grades_are_kept_apart():
    by = {n["id"]: n for n in NODES}
    # a seat's result is never graded as proved on main, and nothing proved on main rests on a seat's word alone
    for n in NODES:
        if any(len(p) == 3 for p in n["pins"]) and all(len(p) == 3 for p in n["pins"]):
            assert n["grade"] in ("LANE-INPUT", "LANE-PROPOSED", "LANE-REVIEWED", "OPEN", "DUTY", "RECORD"), n["id"]
    for e in EDGES:
        if e["kind"] == "requires" and by[e["src"]]["grade"] == "DERIVED":
            assert not by[e["dst"]]["grade"].startswith("LANE"), (e["src"], e["dst"])
    # the ten closure nodes, each with members and at least one duty blocked
    xs = [n for n in NODES if n["kind"] == "closure"]
    assert len(xs) == 10 and all(n["members"] and n["duties_blocked"] for n in xs)
    assert by["V:0OF19"]["grade"] == "RECORD" and by["V:SIX"]["grade"] == "READING"


def test_a_planted_error_is_caught():
    """MB12: the pin check must be able to fail. A quote that is not in the file is reported."""
    saved = bm.S.NODES[0]["pins"]
    bm.S.NODES[0]["pins"] = [["GENESIS.md", "this sentence is not in the foundation document"]]
    try:
        fails = bm.build()[3]
    finally:
        bm.S.NODES[0]["pins"] = saved
    assert any("quote not found" in f for f in fails)
    assert bm.build()[3] == []
