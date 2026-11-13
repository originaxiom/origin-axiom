"""B1909's lock. It loads each of the three scripts (their writes are under a main guard, so loading writes nothing),
requires every check each one makes to hold, its planted cases among them, and holds the page's table to the counts. It
writes nothing."""
import importlib.util, io, contextlib, json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
PAGE = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
LINE = json.loads((HERE.parent / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
WORDS = {1: "one", 2: "two", 3: "three"}

def _checks(name):
    before = sorted(p.name for p in HERE.iterdir())
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    with contextlib.redirect_stdout(io.StringIO()):
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    assert sorted(p.name for p in HERE.iterdir()) == before
    return m.CHECKS

def test_every_check_holds_and_the_page_counts_them():
    total = planted_total = 0
    for name, step in (("the_transition_matrices", "step 2, step 3's arithmetic, step 7"), ("the_pole_constant", "step 1"),
                       ("the_brackets_at_root_level", "step 5 at the level of roots")):
        C = _checks(name)
        assert C and all(c["holds"] for c in C), [c["check"] for c in C if not c["holds"]]
        planted = sum("plant" in c["check"] for c in C)
        assert planted >= 1
        row = "| `%s.py` | %s | %d, none failing | %s |" % (name, step, len(C), WORDS[planted])
        assert row in PAGE, row
        total += len(C); planted_total += planted
    assert "%d checks, none failing, %s of them planted cases" % (total, {6: "six"}[planted_total]) in LINE

def test_the_constant_is_seven_halves_on_the_grade_minus_two_plane():
    C = _checks("the_pole_constant")
    assert any("7/2" in c["check"] and c["holds"] for c in C)
