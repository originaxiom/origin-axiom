"""B1895 lock -- the mends of B1881 read by a session that did not write them, and what the arc's second convention is.

What could fail here: a check of the arc's run not holding, or the run not being what its script gives today (the statements are
computed again below, by code that shares only the imported functions of B1881's script); a number on the page that differs from
the run; a quotation of the reader not found at the commit it read; a planted reversion of a mend that the lock of B1881 passes;
the corrected word standing uncorrected anywhere on main."""
import importlib.util
import itertools
import json
import pathlib
import subprocess

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = HERE.parents[2]
RES = json.loads((HERE / "second_convention_and_least_apex.json").read_text(encoding="utf-8"))
RUN = (HERE / "second_convention_and_least_apex_run.txt").read_text(encoding="utf-8")
PAGE = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
B1881 = ROOT / "frontier" / "B1881_the_whole_and_the_value_verified"
B1884 = ROOT / "frontier" / "B1884_what_level_a_ground_names_verified"


def _b1881_script():
    spec = importlib.util.spec_from_file_location("b1881_script_for_b1895", B1881 / "verification" / "whole_and_value_on_main.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _mul(A, B):
    return ((A[0] * B[0] + A[1] * B[2]) % 5, (A[0] * B[1] + A[1] * B[3]) % 5, (A[2] * B[0] + A[3] * B[2]) % 5, (A[2] * B[1] + A[3] * B[3]) % 5)


def _group():
    I = (1, 0, 0, 1)
    grp, todo = {I}, [I]
    while todo:
        g = todo.pop()
        for h in (_mul(g, (0, 4, 1, 0)), _mul(g, (1, 1, 0, 1))):
            if h not in grp:
                grp.add(h); todo.append(h)
    return grp


def test_every_check_of_the_run_holds_and_the_page_gives_its_numbers():
    checks = {k: v for k, v in RES.items() if isinstance(v, bool)}
    assert len(checks) == 16 and all(checks.values()), [k for k, v in checks.items() if not v]
    assert "CHECKS: 16, FAILING: 0" in RUN and "[FAILS]" not in RUN
    a, b = RES["A_numbers"], RES["B_numbers"]
    for s in ("the 1,332 run sequences of length 2 and 4 with runs to 6, which reach all 120 matrices" if (a["sequences"], a["matrices"]) == (1332, 120) else None,
              "differs from the transposed word on %d of the 1,332, and the two tests they give differ on %d" % (a["swapped_word_differs_from_transposed"], a["tests_differ"]),
              "they agree on %d of the 120" % min(a["controls"].values()),
              "**Checked** on {:,} sequences".format(b["sequences"]),
              "the {:,} others above 4/3; the {:,} with a run of 3 or more above 3/2".format(b["others"], b["with_a_run_of_three_or_more"])):
        assert s and s in PAGE, s
    assert set(a["controls"].values()) == {88} and len(a["controls"]) == 4 and a["row_test_equals_column_test_on_swapped"] == 120
    assert b["at"] == [2, 2] and b["least_among_the_others"].startswith("1.41421356")


def test_the_two_tests_are_one_test_recomputed_with_the_lines_that_s_keeps():
    """Recomputed here apart from the arc's script: on the whole group, for the mark of B1881's script."""
    S = _b1881_script()
    G = _group()
    assert len(G) == 120
    J = (0, 1, 1, 0)
    swap = lambda g: _mul(_mul(J, g), J)
    row = lambda v, g: ((v[0] * g[0] + v[1] * g[2]) % 5, (v[0] * g[1] + v[1] * g[3]) % 5)
    col = lambda g, v: ((g[0] * v[0] + g[1] * v[1]) % 5, (g[2] * v[0] + g[3] * v[1]) % 5)
    line = lambda w: min(((k * w[0]) % 5, (k * w[1]) % 5) for k in (1, 2, 3, 4))
    vecs = [(x, y) for x in range(5) for y in range(5) if (x, y) != (0, 0)]
    lines = sorted({line(w) for w in vecs})
    ann = lambda v: {line(u) for u in vecs if (v[0] * u[0] + v[1] * u[1]) % 5 == 0}
    own = [v for v in lines if ann(v) == {v}]
    kept_by_s = [v for v in lines if line(row(v, (0, 4, 1, 0))) == v]
    assert own == kept_by_s and line(S.V) in own and len(own) == 2                 # the lines that annihilate themselves are the lines S keeps
    second = [v for v in own if v != line(S.V)][0]
    assert second == line(col(J, line(S.V))) == (1, 2)
    agree = sum((line(row(S.V, g)) == line(S.V)) == (line(col(swap(g), second)) == second) for g in G)
    assert agree == 120 == RES["A_numbers"]["row_test_equals_column_test_on_swapped"]
    for c in lines:
        n = sum((line(row(c, g)) == c) == (line(col(swap(g), line(col(J, c)))) == line(col(J, c))) for g in G)
        assert n == (120 if c in own else RES["A_numbers"]["controls"][str(c)]) and (c in own or n < 120), c


def test_the_bound_on_the_least_reading_recomputed():
    """The ingredient and the three statements, on sequences the arc's script did not try: length 2 with runs to 12, length 4 with
    runs to 4, and the all-twos and one-two sequences to length 10."""
    S = _b1881_script()
    mp.mp.dps = 40
    s5 = mp.sqrt(5) / 2
    seqs = [q for q in itertools.product(range(1, 13), repeat=2)] + [q for q in itertools.product(range(1, 5), repeat=4)]
    seqs += [(2,) * n for n in (2, 4, 6, 8, 10)] + [(2,) + (1,) * (n - 1) for n in (2, 4, 6, 8, 10)] + [(1,) * n for n in (2, 4, 6, 8, 10)]
    seen_ground = seen_other = 0
    for q in seqs:
        n = len(q)
        for i in range(n):
            a = q[(i + 1) % n]
            x = 1 / S.cf_value([q[(i + 1 + k) % n] for k in range(n)])
            assert mp.mpf(1) / (a + 1) < x < mp.mpf(1) / a, q
        top = max(S.heights(list(q)))
        if set(q) == {1}:
            seen_ground += 1
            assert abs(top - s5) < mp.mpf(10) ** -35, q
        else:
            seen_other += 1
            assert top > (mp.mpf(3) / 2 if max(q) >= 3 else mp.mpf(4) / 3), q
    assert seen_ground >= 5 and seen_other >= 300 and s5 < mp.mpf(4) / 3
    assert "every run sequence that is not all ones reads above 4/3" in PAGE and "Whether √2 is the second least\n  reading over every sequence is not shown" in PAGE


def test_the_quotations_and_the_planted_reversions():
    q = json.loads((HERE / "quote_check.json").read_text(encoding="utf-8"))
    assert q["quotations"] == q["found"] == 4 and q["control: the first quotation altered by one character is reported missing"] is True
    assert q["the commit of main read"] == "87bfa1f05" and "4 of 4 found at `87bfa1f05`" in PAGE
    p = json.loads((HERE / "planted_reversions.json").read_text(encoding="utf-8"))
    assert p["control passes"] is True and p["plants"][0]["tests failing"] == [] and p["plants"][0]["plant"].startswith("control")
    assert p["of"] == len(p["plants"]) - 1 == 18 and p["caught"] == sum(1 for x in p["plants"][1:] if x["tests failing"]) == 18
    assert "**18 of 18 caught.**" in PAGE and "tested against 18 planted reversions" in PAGE
    # the lock that was tested is the lock as it stands: every test named in the result exists in it today
    lock = (B1881 / "verification" / "test_b1881_the_whole_and_the_value_verified.py").read_text(encoding="utf-8")
    named = {t for x in p["plants"] for t in x["tests failing"]}
    assert len(named) == 5 and all("def %s(" % t in lock for t in named), named
    # ten on the day of this arc.  The lock was planted against again the same day and has more since (B1897): the number of its
    # tests is not held here, only that it has not fewer and that the page says what it had then
    assert lock.count("\ndef test_") >= 10 and "B1881's lock had five tests. It has ten." in PAGE


def test_the_fourth_finding_is_reproduced_on_the_lock_as_it_stood():
    """The committed result of the_old_lock_with_the_mends_undone.py: at the commit read, the seven mends the lock did not hold
    could be undone, in five ways, with every test passing; what it did hold is caught.  The run needs that commit and a few
    seconds, and is made again by the script; here its record is read and held to the page."""
    o = json.loads((HERE / "the_old_lock_with_the_mends_undone.json").read_text(encoding="utf-8"))
    assert o["the commit read"] == "87bfa1f05" and o["tests in the lock at that commit"] == 5
    assert o["the lock as it stood passes"] is True and o["plants"][0]["tests failing"] == []
    middle = o["plants"][1:-1]
    assert len(middle) == o["of"] == 5 and o["undone with every test passing"] == sum(1 for x in middle if not x["tests failing"]) == 5
    named = {m.strip() for x in middle for m in x["the mends it belongs to"].split(",")}
    assert {"SM-11", "SM-12", "SM-13", "X7", "SM-14", "SM-16", "SM-17"} <= named                    # the seven the reader named
    assert o["what it did hold is caught"] is True and o["plants"][-1]["tests failing"] == ["test_the_two_quotients_recomputed"]
    assert "undid the other seven mends there, in five ways. Every test passed each time" in PAGE


def test_the_old_word_stands_nowhere_on_main_without_its_correction():
    """The wrong sentence was written in two arcs and was sent to one session.  A paragraph that calls the columns a transpose
    must carry the correction, in itself or in the paragraph after it.  The files are found by git over frontier/ and docs/ where
    git can list them; the places this arc names are read in any case, so the test never skips."""
    olds = ("is its transpose and is this arc's own", "the columns are the transpose that B1881 used", "the transpose of B1872's rows", "the second one compared here is the transpose",
            "the columns are named as the transpose", "the transpose, which B1881 used")
    marks = ("not the transpose", "CORRECTED AGAIN", "CORRECTED 2026-11-12, a second time", "this label read")
    known = ["frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md", "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json",
             "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md", "frontier/B1884_what_level_a_ground_names_verified/verification/ground_level_on_main.py",
             "docs/seats/agy-exp.md"]
    cmd = ["git", "-C", str(ROOT), "grep", "-l", "-F"] + [x for o in olds for x in ("-e", o)] + ["--", "frontier", "docs"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    listed = [f for f in r.stdout.split("\n") if f] if r.returncode in (0, 1) else []
    files = sorted({f for f in known + listed if not f.startswith(("docs/views/", "frontier/B1895_"))})
    hits, carrying = [], 0
    for f in files:
        text = (ROOT / f).read_text(encoding="utf-8")
        blocks = [text] if f.endswith(".json") else text.split("\n\n")
        for i, blk in enumerate(blocks):
            if any(o in blk for o in olds):
                carrying += 1
                near = blk + ("\n\n" + blocks[i + 1] if i + 1 < len(blocks) else "")
                if not any(m_ in near for m_ in marks):
                    hits.append(f)
    assert hits == [], hits
    assert carrying >= 5 and all(any(o in (ROOT / f).read_text(encoding="utf-8") for o in olds) for f in known), carrying     # the old words are kept, each with its correction


def test_the_arc_says_what_it_is_and_what_it_is_not():
    for s in ("## Seen first", "## Disclosed", "## Reproduce", "0 of 19", "No result of B1881 changes", "Everything in § 3 and § 4 is computed once",
              "These mends have been read by nobody but main", "The identity is computed modulo 5", "It places nothing", "The bound of § 4 is the reader's",
              "It is the fourth time at this review that a correction main wrote held\n  an error of its own"):
        assert s in PAGE, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1895" and v["verdict"] == "PROVED" and v["claim_one_line"].endswith("0 of 19.") and set(v["scope"]) == {"frame", "object", "reach", "hypotheses"}
    assert v["scope"]["reach"] in ("single", "class", "general") and "level 5" in v["scope"]["hypotheses"]
    led = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
    assert "c67f84c1" in led and "B1895" in led
