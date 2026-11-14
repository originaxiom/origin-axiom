"""The topic sweep prints the ledger's row of a wall before its own list (main's card C13, item 4; WORKING_RULES, the rule of
2026-11-12, step 1: a question of a known shape is met with its history first).

Held here: what the sweep reads from the page is what the generator put there; a sweep whose expression matches a wall's name
or words prints that wall's row, and prints it before the first arc; a sweep that matches no wall prints none; a sweep on a
checkout without the page says so and goes on; and the words are the generator's, printed on the page."""
import contextlib
import importlib.util
import io
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name, rel):
    sys.dont_write_bytecode, was = True, sys.dont_write_bytecode
    try:
        spec = importlib.util.spec_from_file_location(name, ROOT / rel)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
    finally:
        sys.dont_write_bytecode = was
    return m


TS = _load("topic_sweep_for_the_walls", "scripts/checks/topic_sweep.py")
G = _load("views_generate_for_the_sweep", "scripts/views/generate.py")
LEDGER = G.walls_ledger()


def _run(*argv):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = TS.main(list(argv))
    return code, out.getvalue().split("\n")


def test_what_the_sweep_reads_from_the_page_is_what_the_generator_put_there():
    rows = TS.walls()
    assert rows is not None and [w["code"] for w in rows] == [w["code"] for w in LEDGER["walls"]]
    for mine, theirs in zip(rows, LEDGER["walls"]):
        assert (mine["name"], mine["arcs"], mine["first"], mine["outcomes"]) == (theirs["name"], theirs["arcs"], theirs["first"], theirs["by_outcome"])
        assert mine["words"] == list(G.WALL_WORDS[mine["code"]])


def test_a_sweep_that_matches_a_wall_prints_its_row_before_its_first_arc():
    code, lines = _run("chiral")
    assert code == 0
    walls = [i for i, l in enumerate(lines) if l.startswith("  WALL ")]
    arcs = [i for i, l in enumerate(lines) if l.startswith("  B")]
    w1 = next(w for w in TS.walls() if w["code"] == "W1")
    assert [lines[i] for i in walls] == [TS.wall_line(w1)] and arcs and max(walls) < min(arcs)
    assert lines[-2].startswith("VERDICT topic-sweep /chiral/")                 # the verdict line is as it was: its readers are not changed
    # by its name, and by a word of another wall
    assert [l for l in _run("mirror pair")[1] if l.startswith("  WALL ")] == [TS.wall_line(w1)]
    assert [l.split(",")[0] for l in _run("canonical")[1] if l.startswith("  WALL ")] == ["  WALL W7"]


def test_a_sweep_that_matches_no_wall_prints_none():
    assert not [l for l in _run("painlev")[1] if l.startswith("  WALL ")]
    assert not [l for l in _run("zzzz-not-there")[1] if l.startswith("  WALL ")]


def test_a_checkout_without_the_page_says_so_and_goes_on(tmp_path, monkeypatch):
    monkeypatch.setattr(TS, "WALLS_PAGE", "docs/views/NO_SUCH_PAGE.md")
    code, lines = _run("chiral")
    assert code == 0 and "the ledger of walls (docs/views/NO_SUCH_PAGE.md) is not on this checkout: no wall is printed" in lines[0]
    assert lines[-2].startswith("VERDICT topic-sweep /chiral/")


def test_the_sweep_reads_the_page_and_not_the_rows(tmp_path):
    """planted: the page with one count changed.  The sweep prints the changed count (it reads the page), and the ledger's own
    lock is what refuses such a page (tests/test_ledger_of_walls.py, the page is what the generator makes)."""
    page = (ROOT / TS.WALLS_PAGE).read_text(encoding="utf-8")
    w1 = next(w for w in TS.walls() if w["code"] == "W1")
    row = "| W1, %s | %d |" % (w1["name"], w1["arcs"])
    assert page.count(row) == 1
    (tmp_path / "docs" / "views").mkdir(parents=True)
    (tmp_path / TS.WALLS_PAGE).write_text(page.replace(row, "| W1, %s | %d |" % (w1["name"], w1["arcs"] + 1)), encoding="utf-8")
    planted = TS.walls(str(tmp_path))
    assert next(w for w in planted if w["code"] == "W1")["arcs"] == w1["arcs"] + 1
    assert planted != TS.walls() and page != (tmp_path / TS.WALLS_PAGE).read_text(encoding="utf-8")
    # the twin: the page copied as it is reads the same
    shutil.copy(ROOT / TS.WALLS_PAGE, tmp_path / TS.WALLS_PAGE)
    assert TS.walls(str(tmp_path)) == TS.walls()


def test_the_selftest_holds_its_planted_walls():
    code, lines = _run("--selftest")
    assert code == 0 and lines[0].startswith("selftest: PASS")
