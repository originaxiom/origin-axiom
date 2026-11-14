"""The ledger of walls (main's card C13, 2026-11-12): a generated view whose whole content is the rows of B1905.

The classes in the rows are the readers', one reader an arc, and are not checked here.  What is held: the page is what the
generator makes of the rows; its counts are the counts of B1905's own tables; "first met" and "settled without a pick" are
what the page says they are; the page prints no quotation and no outcome's text; and a row added, a class changed or a
word of the outcome changed moves the page."""
import copy
import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1905_selection_and_chirality_across_the_record"


def _generator():
    sys.dont_write_bytecode, was = True, sys.dont_write_bytecode
    try:
        spec = importlib.util.spec_from_file_location("views_generate_for_the_walls", ROOT / "scripts" / "views" / "generate.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
    finally:
        sys.dont_write_bytecode = was
    return m


G = _generator()
ST = G._walls_source()
ROWS = ST.load()
LEDGER = G.walls_ledger()
PAGE = (ROOT / "docs" / "views" / G.WALLS_VIEW).read_text(encoding="utf-8")
num = lambda a: int(a[1:])


def test_the_page_is_what_the_generator_makes_of_the_rows():
    assert PAGE == G.view_walls()
    assert G.view_walls(G.walls_ledger(ROWS, ST)) == PAGE
    assert G.WALLS_ARC == ARC.relative_to(ROOT).as_posix() and (ARC / "verification" / "rows.json.txt").is_file()


def test_the_counts_are_those_of_b1905s_own_tables():
    T = ST.tables(ROWS)
    assert (LEDGER["rows"], LEDGER["about"], LEDGER["neither"]) == (T["rows"], T["about selection or chirality"], T["neither on reading"])
    assert [w["code"] for w in LEDGER["walls"]] == list(ST.WALLS) and len(LEDGER["walls"]) == 8
    for w in LEDGER["walls"]:
        assert w["by_outcome"] == T["wall by outcome"][w["code"]] and w["arcs"] == sum(w["by_outcome"]), w["code"]
        assert len(w["question_was_wrong"]) == w["by_outcome"][3] and len(w["later_corrected"]) == w["by_outcome"][4], w["code"]
    # the four walls for which B1905's script tabulates the kinds: the ledger's table is that table, without its empty rows
    for code, tab in T["kind of principle by outcome, wall by wall"].items():
        mine = next(w for w in LEDGER["walls"] if w["code"] == code)["kinds"]
        assert mine == {k: c for k, c in tab.items() if sum(c)}, code
    assert sum(w["arcs"] for w in LEDGER["walls"]) == LEDGER["about"]
    assert sorted(a for w in LEDGER["walls"] for a in w["question_was_wrong"]) == sorted(T["arcs whose question was found to be wrong"])
    # and each count stands on the page, in the row of its wall
    for w in LEDGER["walls"]:
        assert "| %s, %s | %d | %s | %s |" % (w["code"], w["name"], w["arcs"], w["first"], " | ".join(str(x) for x in w["by_outcome"])) in PAGE


def test_first_met_and_settled_without_a_pick_are_what_the_page_says_they_are():
    live = [r for r in ROWS if r["topic"] != "neither"]
    by = {r["arc"]: r for r in live}
    for w in LEDGER["walls"]:
        mine = [r for r in live if r["wall"].startswith(w["code"])]
        assert w["first"] == min((r["arc"] for r in mine), key=num), w["code"]
        for a in w["settled_without_a_pick"]:
            r = by[a]
            assert r["wall"].startswith(w["code"]) and r["settled"] == "yes" and ST.NEG.search(r["outcome"]) and not ST.POS.search(r["outcome"]), a
        assert w["settled_without_a_pick"] == sorted(w["settled_without_a_pick"], key=num)
    assert "the arc of the wall with the lowest number" in PAGE and "It is not a judgement of the arc." in PAGE
    assert "They are not independently checked." in PAGE


def test_the_page_prints_no_quotation_and_no_outcome():
    for r in ROWS:
        for field in ("quote", "outcome", "why", "question", "principle_note"):
            text = r[field].strip()
            assert len(text) < 25 or text not in PAGE, (r["arc"], field)


def test_a_row_added_a_class_changed_and_a_word_of_the_outcome_changed_each_move_the_page():
    # a row added: an arc with a lower number than any of its wall is now where the wall was first met
    rows = copy.deepcopy(ROWS)
    w5 = next(r for r in rows if r["wall"].startswith("W5") and r["topic"] != "neither")
    rows.append(dict(w5, arc="B1", settled="no"))
    L = G.walls_ledger(rows, ST)
    five = next(w for w in L["walls"] if w["code"] == "W5")
    was = next(w for w in LEDGER["walls"] if w["code"] == "W5")
    assert five["first"] == "B1" != was["first"] and five["arcs"] == was["arcs"] + 1 and G.view_walls(L) != PAGE
    # a class changed: one arc moved from the first wall to the second
    rows = copy.deepcopy(ROWS)
    i = next(i for i, r in enumerate(rows) if r["wall"].startswith("W1"))
    rows[i]["wall"] = "W2 one member of a family not picked (thread, root, object)"
    L = G.walls_ledger(rows, ST)
    assert [w["arcs"] for w in L["walls"]][:2] == [LEDGER["walls"][0]["arcs"] - 1, LEDGER["walls"][1]["arcs"] + 1] and G.view_walls(L) != PAGE
    # a word of the outcome changed: an arc listed as settled without a pick, whose outcome now says that something is picked, leaves the list
    listed = LEDGER["walls"][0]["settled_without_a_pick"][0]
    rows = copy.deepcopy(ROWS)
    r = next(r for r in rows if r["arc"] == listed)
    r["outcome"] = "The rule selects one member."
    assert ST.POS.search(r["outcome"]) and not ST.NEG.search(r["outcome"])
    L = G.walls_ledger(rows, ST)
    assert listed not in L["walls"][0]["settled_without_a_pick"] and G.view_walls(L) != PAGE
    # the twin: the same rows in another order make the same page
    assert G.view_walls(G.walls_ledger(list(reversed(copy.deepcopy(ROWS))), ST)) == PAGE


def test_the_generator_leaves_nothing_beside_b1905s_script():
    G._walls_source()
    assert not (ARC / "verification" / "__pycache__").exists()
