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
    # ADDED 2026-11-12 (Review 80; the SM seat's finding 34, which main recounted).  A bracket of the first section said "two at
    # other levels".  Most levels have none: counted here, and the page's correction is held to the count.  BUILT AGAIN
    # 2026-11-13 on main's b1bcc7f50: main corrected the bracket itself (B1923, at agy-002's reading); the lock holds main's words.
    others = [counts[n] for n in range(2, 201) if n != 5]
    assert (len(others), others.count(0), others.count(2), others.count(1)) == (198, 173, 25, 0)
    assert "and two at other levels. [CORRECTED 2026-11-13 (" in f and "two at 25 other levels to 200" in f and "none at the other 173" in f


def test_the_column_convention_is_the_swap_of_the_coordinates_and_not_a_transpose():
    """Added 2026-11-12, from a second reading of a mend of Review 79's second round.  That mend named the column convention the
    transpose of the rows.  The row ground is symmetric, so its transpose is itself; the column ground is the row ground conjugated
    by the swap of the two coordinates, and so are the letters and the tick.  Fails if the ground were not symmetric, or if the
    script's label, its run or the page still called the columns a transpose without the correction."""
    swap = lambda g: m.mul(m.mul(m.SW, g), m.SW)
    tr = lambda g: (g[0], g[2], g[1], g[3])
    assert tr(m.LR) == m.LR and swap(m.LR) == (2, 1, 1, 1) and swap(m.LR) != tr(m.LR)
    assert swap(m.L) == (1, 1, 0, 1) == m.R and swap(m.R) == (1, 0, 1, 1) == m.L and swap(m.F) == (1, 1, 1, 0)
    assert m.mul(swap(m.F), swap(m.F)) == swap(m.LR)
    col = lambda g, v: ((g[0] * v[0] + g[1] * v[1]) % 5, (g[2] * v[0] + g[3] * v[1]) % 5)
    # the marks, computed from the script's own objects and not typed: the four rows the row ground keeps up to sign, the columns
    # they all annihilate, and the four columns the swapped ground keeps up to sign.  The swap carries the second set to the third.
    marks = m.kept_up_to_sign(m.LR, 5)
    annihilated = [u for u in m.primitive(5) if all((v[0] * u[0] + v[1] * u[1]) % 5 == 0 for v in marks)]
    kept_columns = [u for u in m.primitive(5) if col(swap(m.LR), u) in (u, ((-u[0]) % 5, (-u[1]) % 5))]
    assert len(marks) == len(annihilated) == len(kept_columns) == 4 and (1, 3) in marks and (1, 2) in kept_columns
    assert sorted(annihilated) == sorted(marks)                                           # the mark's line is its own annihilator
    assert sorted(col(m.SW, u) for u in annihilated) == sorted(kept_columns)
    assert sorted(kept_columns) != sorted(marks)                                          # and the columns kept are another line
    keys = [k for k in RES if k.startswith("G5 ")]
    assert len(keys) == 1 and "the row convention with every matrix conjugated by the swap of the coordinates" in keys[0] and RES[keys[0]] is True
    run = (HERE / "ground_level_on_main_run.txt").read_text(encoding="utf-8")
    assert "transpose" not in keys[0] and "the transpose of B1872's rows" not in run
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    para = [b_ for b_ in f.split("\n\n") if "the columns are the transpose that B1881 used" in b_]
    assert len(para) == 1 and "the columns are not the transpose" in para[0] and "conjugated by the swap" in para[0]
    src = (HERE / "ground_level_on_main.py").read_text(encoding="utf-8")
    assert "CORRECTED AGAIN the same day" in src and src.count("the transpose of B1872's rows") == 1          # once, in the note that says what it read


def _names_the_column_convention_as_mains_own(claim):
    """the places where a verdict line calls the column convention main's own and does not take it back within 120 characters"""
    out, at = [], claim.find("main's own convention")
    while at != -1:
        if "it is not main's own" not in claim[at:at + 120]:
            out.append(at)
        at = claim.find("main's own convention", at + 1)
    return out


def test_the_verdict_line_does_not_leave_the_column_convention_as_mains_own():
    """Added 2026-11-12 (Review 80; the SM seat's finding 35, checked by main).  The page and the script were corrected at Review
    79's second round; the verdict line still said "The same counts hold in main's own convention", gave the agreement as a
    result, and no test read it.  Planted: the line as it stood, and the correction moved to the end of the line."""
    claim = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert claim.count("main's own convention") == 1 and _names_the_column_convention_as_mains_own(claim) == []
    assert "the row convention with every matrix conjugated by the swap of the two coordinates" in claim and "an instance of an identity" in claim
    start = claim.index(" [CORRECTED 2026-11-12 (Review 80): it is not main's own.")
    end = claim.index("].", start) + 1
    as_it_stood = claim[:start] + claim[end:]
    assert "The same counts hold in main's own convention. Nothing leaves the budget" in as_it_stood
    assert len(_names_the_column_convention_as_mains_own(as_it_stood)) == 1
    moved = as_it_stood[:-len("0 of 19.")] + claim[start + 1:end] + " 0 of 19."
    assert len(_names_the_column_convention_as_mains_own(moved)) == 1


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



def test_the_lines_the_ground_keeps_are_the_roots_of_its_own_quadratic():
    """ADDED 2026-11-12 (Review 80; a reader's supplement on the arcs main changed, its first finding, computed by main).  A
    bracket main wrote at this review said that LR keeps one point at N = 5 and two at other levels.  The lines LR keeps are
    the roots of x^2 - 3x + 1 modulo N: counted here by brute force, both ways, and the page's sentence is held to it."""
    roots = lambda n: sum(1 for x in range(n) if (x * x - 3 * x + 1) % n == 0)
    assert all(m.lines_kept(m.LR, n) == roots(n) for n in range(2, 201))                # lines and roots agree at every level
    to_60 = {n: roots(n) for n in range(2, 61)}
    assert sum(1 for c in to_60.values() if c == 0) == 51 and [n for n, c in to_60.items() if c == 1] == [5]
    assert [n for n, c in to_60.items() if c == 2] == [11, 19, 29, 31, 41, 55, 59] and max(to_60.values()) == 2
    five_is_a_square = lambda n: any((x * x - 5) % n == 0 for x in range(n))
    assert all(roots(n) == 0 for n in range(2, 201) if not five_is_a_square(n))          # none wherever 5 is not a square
    assert five_is_a_square(2) and roots(2) == 0                                         # and not only there: at 2, 5 is a square and no line is kept
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    # BUILT AGAIN 2026-11-13 on main's b1bcc7f50: main wrote the correction on the page itself (B1923, at the same reader's
    # finding); the page's sentence held here is main's, and the counts above are its counts to 60
    assert "LR keeps exactly one point at N = 5, and two at other levels. [CORRECTED 2026-11-13 (" in f   # what was written is kept
    assert "Lines kept as a set number one at N = 5, two at 25 other levels to 200 (11, 19, 29, 31, 41, 55, " in f
    assert "and none at the other 173" in f


def test_the_arcs_corrections_of_review_79_and_80_are_held_and_the_script_says_what_the_page_says():
    """ADDED 2026-11-12 (the same supplement, its second finding, not checked by main): the page was corrected to say
    "computed once" and the script's own heading still said that its expectations were written before the run; and the
    lock held one of main's four mends of this arc."""
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    for s in ("is main's own check and not a prediction of the card",
              "it now tries every one",
              "stood unscoped in five places; each carries the correction now",
              "By the protocol's labels this is computed once, and not \"expectations committed first\""):
        assert s in f, s
    script = (HERE / "ground_level_on_main.py").read_text(encoding="utf-8")
    assert "EXPECTATIONS, WRITTEN BEFORE THE RUN (each says how it could fail)\n[CORRECTED 2026-11-12 (Review 80;" in script
    assert "By the protocol's labels this is computed once" in " ".join(script.split())
