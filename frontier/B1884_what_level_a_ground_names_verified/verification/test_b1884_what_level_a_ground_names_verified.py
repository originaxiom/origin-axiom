"""B1884 lock -- the web seat's card on what level a ground names, verified on main.

What could fail: a check of the sealed run not holding; the identity for odd histories failing on a matrix; a second level with
exactly one line kept; the arc saying that the tick has a line of its own."""
import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
spec = importlib.util.spec_from_file_location("ground_level_on_main_lock", HERE / "ground_level_on_main.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
RES = json.loads((HERE / "ground_level_on_main.json").read_text(encoding="utf-8"))


def test_every_check_of_the_sealed_run_holds():
    checks = {k: v for k, v in RES.items() if isinstance(v, bool)}
    assert len(checks) == 17 and all(checks.values())
    assert "CHECKS: 17, FAILING: 0" in (HERE / "ground_level_on_main_run.txt").read_text(encoding="utf-8")


def test_the_tick_keeps_no_vector_and_its_square_keeps_four_at_five_recomputed():
    assert m.F == (0, 1, 1, 1) and m.mul(m.F, m.F) == m.LR == (1, 1, 1, 2)
    for n in range(2, 61):
        assert m.kept_up_to_sign(m.F, n) == []
        assert len(m.kept_up_to_sign(m.LR, n)) == (4 if n == 5 else 0)


def test_exactly_one_line_is_kept_at_five_and_nowhere_else_recomputed():
    one = [n for n in range(2, 121) if m.lines_kept(m.LR, n) == 1]
    assert one == [5] and [n for n in range(2, 121) if m.lines_kept(m.F, n) == 1] == [5]
    assert m.lines_kept(m.LR, 11) == m.lines_kept(m.LR, 19) == 2 and m.lines_kept(m.LR, 25) == 0 and m.lines_kept(m.LR, 7) == 0
    assert RES["numbers"]["levels_with_a_line_kept"][:8] == [5, 11, 19, 29, 31, 41, 55, 59]


def test_among_odd_histories_only_trace_one_has_no_own_line():
    import itertools
    mats = [g for g in itertools.product(range(9), repeat=4) if m.det(g) == -1]
    assert len(mats) == 87 == RES["numbers"]["matrices_det_minus_one"]
    d = lambda g, s: m.det((g[0] + s, g[1], g[2], g[3] + s))
    assert all(d(g, -1) == -(g[0] + g[3]) and d(g, 1) == g[0] + g[3] for g in mats)
    assert sorted(g for g in mats if g[0] + g[3] == 1) == sorted([m.F, m.F2])


def test_the_arc_says_which_reading_gives_the_level():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The tick has its level by one reading only, the discriminant", "that rule gives the tick none", "Nothing leaves the budget",
              "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1884" and v["claim_one_line"].endswith("0 of 19.") and "thread" in v["weave_or_thread"]
