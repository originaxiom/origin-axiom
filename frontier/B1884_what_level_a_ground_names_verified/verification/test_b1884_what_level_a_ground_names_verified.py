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


def test_two_and_no_more_holds_to_200_and_not_beyond():
    """Added 2026-11-12 (Review 79), from a second derivation on another family of model: the page said "Two at 11, 19, ... and
    on; none elsewhere", which is true of the range computed and false nine levels later.  Counted here by brute force."""
    rho = lambda n: sum(1 for x in range(n) if (x * x - x - 1) % n == 0)
    counts = {n: rho(n) for n in range(2, 1001)}
    assert max(counts[n] for n in range(2, 201)) == 2                                   # to 200: none, one or two
    assert min(n for n, c in counts.items() if c > 2) == 209 and counts[209] == 4      # 11 x 19: the first with four
    assert [x for x in range(209) if (x * x - x - 1) % 209 == 0] == [15, 81, 129, 195]
    assert [n for n, c in counts.items() if c == 1] == [5] and counts[25] == 0          # exactly one: at 5 and at no other level to 1000
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "four at 209 = 11 × 19" in f and "holds to 200, the range computed" in f


import os as _os

import pytest as _pytest


@_pytest.mark.skipif(not _os.environ.get("OA_SLOW"), reason="OA_SLOW=1: runs the arc's script again (four and a half minutes on main's machine)")
def test_the_script_is_run_again_and_every_check_holds():
    """Added 2026-11-12 (Review 79).  The first test reads the seventeen checks from the committed file and reruns nothing; a
    reader planted a change in one check, the script reported it failing and this lock passed.  Here the script is run.
    IN THE SLOW LANE ONLY, because of its time: so in the default lane a change to the script that is not rerun still
    passes this lock, and the three recomputing tests above are what stands against it.  Said, not hidden."""
    import subprocess
    import sys
    r = subprocess.run([sys.executable, "-B", str(HERE / "ground_level_on_main.py")], capture_output=True, text=True, timeout=1800)
    assert r.returncode == 0, (r.stdout[-500:], r.stderr[-500:])
    assert "FAILING: 0" in r.stdout and "every coprime factorisation of the 139 levels" in r.stdout

