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
    # the closure nodes, each with members and at least one duty blocked
    xs = [n for n in NODES if n["kind"] == "closure"]
    assert len(xs) == 11 and all(n["members"] and n["duties_blocked"] for n in xs)
    assert by["V:0OF19"]["grade"] == "RECORD" and by["V:SIX"]["grade"] == "READING"
    # DERIVED means proved outright (Review 77, the reader): it requires only DERIVED nodes; the tube's real part is conditional
    for e in EDGES:
        if e["kind"] == "requires" and by[e["src"]]["grade"] == "DERIVED":
            assert by[e["dst"]]["grade"] == "DERIVED", (e["src"], e["dst"])
    assert by["T:RE"]["grade"] == "CONDITIONAL" and by["SC:UNIT"]["grade"] == "NEGATIVE"
    bm.S.EDGES.append(dict(src="W:T", kind="requires", dst="G:GM1", grade="DERIVED", note="planted"))
    try:
        fails = bm.build()[3]
    finally:
        bm.S.EDGES.pop()
    assert any("a DERIVED node requires a node that is not DERIVED" in f for f in fails)


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


def test_weave_or_thread_is_labelled_and_kept_apart():
    """THE WEAVE's test: every node of the spine says what it is stated about, and no weave result rests on a thread."""
    by = {n["id"]: n for n in NODES}
    assert all(n.get("weave_or_thread") in ("weave", "thread", "list", "record", "n/a") for n in NODES)
    assert by["G:ROOT"]["weave_or_thread"] == "thread" and by["MC:Z6"]["weave_or_thread"] == "thread"
    assert by["W:MIRROR-EVEN"]["weave_or_thread"] == "list" and by["W:ONE-END"]["weave_or_thread"] == "list"
    assert by["W:T"]["weave_or_thread"] == "weave" and by["V:SIX"]["weave_or_thread"] == "thread"
    for e in EDGES:
        if e["kind"] == "requires" and by[e["src"]]["weave_or_thread"] == "weave" and by[e["src"]]["grade"] in ("DERIVED", "CONDITIONAL", "NEGATIVE"):
            assert by[e["dst"]]["weave_or_thread"] not in ("thread", "list"), (e["src"], e["dst"])
    # MB12: the check can fail -- a weave result made to rest on a thread is refused
    bm.S.EDGES.append(dict(src="W:T", kind="requires", dst="G:SE2", grade="DERIVED", note="planted"))
    try:
        fails = bm.build()[3]
    finally:
        bm.S.EDGES.pop()
    assert any("a weave result rests on a thread" in f for f in fails)


def test_a_conditional_result_names_its_premise():
    """Found building the closure programme (B1861, 2026-11-10): eight CONDITIONAL nodes named no premise."""
    has = {e["src"] for e in EDGES if e["kind"] in ("requires", "applies-under")}
    cond = [n["id"] for n in NODES if n["grade"] in ("CONDITIONAL", "READING")]
    assert len(cond) >= 19 and all(c in has for c in cond)
    # MB12: the check can fail -- take one conditional node's only premise edge away
    i = next(k for k, e in enumerate(bm.S.EDGES) if e["src"] == "FA:F2" and e["kind"] == "requires")
    saved = bm.S.EDGES.pop(i)
    try:
        fails = bm.build()[3]
    finally:
        bm.S.EDGES.insert(i, saved)
    assert any("a conditional result names no premise: FA:F2" in f for f in fails)
    assert bm.build()[3] == []


def test_a_node_that_no_edge_joins_is_held_by_name_or_refused():
    """2026-11-12 (R80b, part 6; a reader's supplement on the arcs main changed at Review 80, its finding 11; not checked by
    main).  Three nodes were added with no edge and nothing said so.  The page lists every such node, and the builder refuses
    one that the source does not hold by name."""
    others, debts = bm.joined_to_nothing(NODES, EDGES)
    ends = {e["src"] for e in EDGES} | {e["dst"] for e in EDGES}
    assert sorted(n["id"] for n in others) == sorted(n["id"] for n in NODES if n["kind"] != "debt" and n["id"] not in ends)
    assert sorted(n["id"] for n in others) == sorted(bm.S.JOINED_TO_NOTHING_AS_FOUND)
    assert {"G:SE3", "G:PF2", "G:FK12"} <= {n["id"] for n in others}                     # the three the finding names
    page = (ARC / "MAP.md").read_text(encoding="utf-8")
    listed = page[page.index("## The nodes that no edge joins"):]
    assert all("| %s | " % n["id"] in listed for n in others)
    assert listed.split("\n")[2].startswith("%d of the %d nodes that are not debts, and %d of the %d debts." % (
        len(others), len([n for n in NODES if n["kind"] != "debt"]), len(debts), len([n for n in NODES if n["kind"] == "debt"])))
    saved = bm.S.JOINED_TO_NOTHING_AS_FOUND
    try:
        # a node with no edge that the table does not name: as the map stood when the three were added
        bm.S.JOINED_TO_NOTHING_AS_FOUND = tuple(i for i in saved if i != "G:SE3")
        assert [f for f in bm.build()[3]] == ["G:SE3 is joined to nothing and is not held by name"]
        # a name in the table that an edge joins, and one that is no node
        joined = sorted(ends)[0]
        bm.S.JOINED_TO_NOTHING_AS_FOUND = saved + (joined,)
        assert bm.build()[3] == ["%s is held by name as joined to nothing, and an edge joins it" % joined]
        bm.S.JOINED_TO_NOTHING_AS_FOUND = saved + ("G:NO-SUCH-NODE",)
        assert bm.build()[3] == ["G:NO-SUCH-NODE is held by name as joined to nothing, and it is not a node"]
    finally:
        bm.S.JOINED_TO_NOTHING_AS_FOUND = saved
    assert bm.build()[3] == []


def test_a_debt_under_a_heading_of_another_day_is_held_by_name_or_refused():
    """The same finding: debts of a later day stood under a heading of an earlier one, and the map printed that heading as
    their class.  Main mended the list (P-828); this holds the mend."""
    import re
    reg = (bm.ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    found = bm.debts_under_a_heading_of_another_day(reg)
    assert [(p, own) for p, own, _ in found] == sorted(bm.S.A_DEBT_WHOSE_ROW_IS_OF_ANOTHER_DAY_THAN_ITS_HEADING.items())
    # the list as it stood before main's mend, made again on a small register: two debts of the 12th under a heading of the 10th
    small = "\n".join([
        "## The debts, by load (worked in this order)", "",
        "*added at a session (a seat's re-audit, 2026-11-10):*", "",
        "1. P-901 — a debt of the day the heading names.",
        "2. P-902 — a debt of two days later.",
        "3. P-903 — another of two days later.", "",
        "*added at a session, with no day named:*", "",
        "4. P-904 — a debt under a heading that names no day.", "",
        "## The rows", "",
        "| P-901 | 2026-11-10 | SE | A | QUEUED | - |",
        "| P-902 | 2026-11-12 | SE | B | QUEUED | - |",
        "| P-903 | 2026-11-12 | SE | C | QUEUED | - |",
        "| P-904 | 2026-11-12 | SE | D | QUEUED | - |", ""])
    assert bm.debts_under_a_heading_of_another_day(small) == [("P-902", "2026-11-12", "2026-11-10"), ("P-903", "2026-11-12", "2026-11-10")]
    # the twin: the same two under a heading of their own day
    mended = small.replace("3. P-903", "*added on 2026-11-12:*\n\n3. P-903").replace("2. P-902 — a debt of two days later.\n", "") \
                  .replace("3. P-903 —", "2. P-902 — a debt of two days later.\n3. P-903 —")
    assert bm.debts_under_a_heading_of_another_day(mended) == []
    # a debt whose row is not in the register at all is reported with no day
    assert bm.debts_under_a_heading_of_another_day(small.replace("| P-901 | 2026-11-10 |", "| P-911 | 2026-11-10 |")) [0] == ("P-901", None, "2026-11-10")
    # on the live register: the name taken out of the table is refused by the builder
    saved = dict(bm.S.A_DEBT_WHOSE_ROW_IS_OF_ANOTHER_DAY_THAN_ITS_HEADING)
    try:
        bm.S.A_DEBT_WHOSE_ROW_IS_OF_ANOTHER_DAY_THAN_ITS_HEADING.clear()
        fails = bm.build()[3]
        assert len(fails) == len(saved) and all(re.match(r"P-\d+ is a debt under a heading that names \d{4}-\d\d-\d\d, and its row is of ", f) for f in fails)
    finally:
        bm.S.A_DEBT_WHOSE_ROW_IS_OF_ANOTHER_DAY_THAN_ITS_HEADING.update(saved)
    assert bm.build()[3] == []
