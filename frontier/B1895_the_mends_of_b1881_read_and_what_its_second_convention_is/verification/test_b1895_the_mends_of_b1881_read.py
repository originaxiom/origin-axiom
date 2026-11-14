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
    runs to 4, and the all-twos and one-two sequences to length 10.

    CORRECTED 2026-11-12 (Review 80; a reader's finding, not checked by main; counted here, below): most of these sequences the
    arc's script did try.  Of the 409 distinct sequences of this test, 295 are among the script's 2,061 (length 2 and 4 with runs
    to 6, length 6 with runs to 3): every one of length 4, the 36 of length 2 with runs to 6, and three of length 6.  114 are
    new: the 108 of length 2 with a run of 7 to 12, and six of length 8 and 10.  The first sentence stays as it was written."""
    S = _b1881_script()
    mp.mp.dps = 40
    s5 = mp.sqrt(5) / 2
    seqs = [q for q in itertools.product(range(1, 13), repeat=2)] + [q for q in itertools.product(range(1, 5), repeat=4)]
    seqs += [(2,) * n for n in (2, 4, 6, 8, 10)] + [(2,) + (1,) * (n - 1) for n in (2, 4, 6, 8, 10)] + [(1,) * n for n in (2, 4, 6, 8, 10)]
    tried_by_the_script = {q for n, top in ((2, 6), (4, 6), (6, 3)) for q in itertools.product(range(1, top + 1), repeat=n)}
    distinct = set(seqs)
    assert len(tried_by_the_script) == RES["B_numbers"]["sequences"] == 2061
    assert (len(distinct), len(distinct & tried_by_the_script), len(distinct - tried_by_the_script)) == (409, 295, 114)
    assert sum(1 for q in distinct - tried_by_the_script if len(q) == 2 and max(q) >= 7) == 108
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


# ---- Review 80 (2026-11-12).  Four things the readers' files say of this arc, each computed by main with code of its own (the
# arc B1898 keeps it: verification/checks/b1895_probes.py, with its output).  They are computed again here, by that code
# placed in the lock, so that the notes of that day on the page are held to a computation.
def _word(seq, a, b):
    """the word of a run sequence over the integers: the first letter for runs at even places, the second for the others"""
    mul = lambda A, B: (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])
    W = (1, 0, 0, 1)
    for k, r in enumerate(seq):
        for _ in range(r):
            W = mul(W, a if k % 2 == 0 else b)
    return W


_SEAT = ((1, 0, 1, 1), (1, 1, 0, 1))          # the seat's letters, on rows
_SECOND = ((1, 1, 0, 1), (1, 0, 1, 1))        # the second convention's letters, on columns
_SEQS = [seq for n in (2, 4) for seq in itertools.product(range(1, 7), repeat=n)]
_LINE = lambda w: min(((k * w[0]) % 5, (k * w[1]) % 5) for k in (1, 2, 3, 4))
_LINES = sorted({_LINE((a, b)) for a in range(5) for b in range(5) if (a, b) != (0, 0)})
_OWN = lambda v: (v[0] * v[0] + v[1] * v[1]) % 5 == 0                            # the mark annihilates its own line


def test_the_second_conventions_word_is_built_and_is_the_seats_conjugated_by_the_swap():
    """Row A1 of the page says that every word of the second convention is the seat's word conjugated by the swap.  The arc's
    script and this lock compared the outcome of the two tests, and built no word of the second convention.  Here it is built,
    letter by letter over the integers, on the 1,332 sequences of the row.  A control: with the letters of the second
    convention exchanged the two words differ, so the comparison can fail."""
    mul = lambda A, B: (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])
    J = (0, 1, 1, 0)
    conj = lambda W: mul(mul(J, W), J)
    assert len(_SEQS) == 1332 == RES["A_numbers"]["sequences"]
    assert sum(1 for seq in _SEQS if _word(seq, *_SECOND) == conj(_word(seq, *_SEAT))) == 1332
    assert sum(1 for seq in _SEQS if _word(seq, _SECOND[1], _SECOND[0]) == conj(_word(seq, *_SEAT))) < 1332        # the control
    assert "it equals the seat's word conjugated by the swap on 1,332 of the 1,332 sequences" in PAGE


def test_the_allowed_set_is_not_closed_under_reversal_for_a_mark_that_does_not_annihilate_its_own_line():
    """Section 7 left this as not computed.  It is: for each mark, the sequences that are allowed differently from their
    reversal.  None for the two marks that annihilate their own line; 358 or 362 of the 1,332 for each of the other four."""
    m5 = lambda A: tuple(x % 5 for x in A)
    row = lambda v, g: ((v[0] * g[0] + v[1] * g[2]) % 5, (v[0] * g[1] + v[1] * g[3]) % 5)
    kept = lambda v, g: _LINE(row(v, g)) == _LINE(v)
    differ = {v: sum(1 for seq in _SEQS if kept(v, m5(_word(seq, *_SEAT))) != kept(v, m5(_word(tuple(reversed(seq)), *_SEAT)))) for v in _LINES}
    assert [v for v in _LINES if _OWN(v)] == [(1, 2), (1, 3)]
    assert differ == {(0, 1): 358, (1, 0): 358, (1, 1): 362, (1, 2): 0, (1, 3): 0, (1, 4): 362}
    assert "358 or 362 of the 1,332 run sequences" in PAGE and "for the two that do, none" in PAGE


def test_the_second_least_reading_is_the_all_twos_over_the_cyclic_sequences_that_were_read():
    """Section 4 says that whether the all-twos' reading is the second least over every sequence is not shown.  A reader gave an
    argument by cases, which main read; that argument is not written in this arc and is not what this test holds.  What it
    holds is main's computation: over the primitive cyclic run sequences of length 1 to 10 and 12, with the runs each length
    is given below, the least reading is the all-ones', the second least the all-twos', and every other reads above 17/12."""
    S = _b1881_script()
    mp.mp.dps = 50
    canon = lambda seq: min(tuple(seq[i:] + seq[:i]) for i in range(len(seq)))
    cyc = set()
    for n, top in ((1, 9), (2, 9), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 3), (9, 2), (10, 2), (12, 2)):
        for seq in itertools.product(range(1, top + 1), repeat=n):
            cyc.add(canon(seq))
    primitive = lambda seq: not any(len(seq) % d == 0 and seq == seq[:d] * (len(seq) // d) for d in range(1, len(seq)))
    prim = sorted(c for c in cyc if primitive(c))
    read = {c: max(S.heights(list(c) if len(c) % 2 == 0 else list(c) * 2)) for c in prim}       # the reading takes an even length
    assert len(prim) == 3378
    assert abs(read[(1,)] - mp.sqrt(5) / 2) < mp.mpf(10) ** -40 and abs(read[(2,)] - mp.sqrt(2)) < mp.mpf(10) ** -40
    others = {c: h for c, h in read.items() if c not in ((1,), (2,))}
    low = min(others.values())
    assert low > mp.mpf(17) / 12 > mp.sqrt(2) and [c for c, h in others.items() if h == low] == [(1, 1, 2, 2)]
    assert mp.nstr(low, 5) == "1.4866"
    flat = " ".join(PAGE.split())                                              # the page's sentences, whatever line they break on
    assert "over 3,378 primitive cyclic run sequences" in flat and "the least of them 1.4866 at (1, 1, 2, 2)" in flat


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


_OLDS = ("is its transpose and is this arc's own", "the columns are the transpose that B1881 used", "the transpose of B1872's rows", "the second one compared here is the transpose",
         "the columns are named as the transpose", "the transpose, which B1881 used")
_MARKS = ("not the transpose", "CORRECTED AGAIN", "CORRECTED 2026-11-12, a second time", "this label read")
_WITHIN = 400      # characters after the old words, in one text of a verdict file, in which their correction must stand


def _texts_of(value):
    """every text a json value holds, at any depth"""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from _texts_of(v)
    elif isinstance(value, (list, tuple)):
        for v in value:
            yield from _texts_of(v)


def _carriers(name, text):
    """Each place where the old words stand in a file, as the words that may excuse it.
    On a page: a paragraph, with the paragraph after it.  In a verdict file: a text of the file, from the old words to 400
    characters after them.  CHANGED 2026-11-12 (Review 80; a reader's finding F9, not checked by main, made again here): a
    verdict file was read as one block, so one correction anywhere in it excused the old words anywhere else in it, in the
    same line or in another field."""
    if name.endswith(".json"):
        for leaf in _texts_of(json.loads(text)):
            for o in _OLDS:
                at = leaf.find(o)
                while at != -1:
                    yield leaf[at:at + len(o) + _WITHIN]
                    at = leaf.find(o, at + 1)
        return
    blocks = text.split("\n\n")
    for i, blk in enumerate(blocks):
        if any(o in blk for o in _OLDS):
            yield blk + ("\n\n" + blocks[i + 1] if i + 1 < len(blocks) else "")


def _uncorrected(name, text):
    """how many places in the file hold the old words with no correction beside them, and how many hold them at all"""
    near = list(_carriers(name, text))
    return sum(1 for n in near if not any(m_ in n for m_ in _MARKS)), len(near)


def test_a_correction_in_a_verdict_file_excuses_only_the_words_it_stands_with():
    """Planted: B1881's verdict file, which holds the old words once with their correction, given the old words a second time
    with none: in another field, and at the end of the same line.  Read as one block, as this lock read it, each passes."""
    name = "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json"
    text = (ROOT / name).read_text(encoding="utf-8")
    as_one_block = lambda t: any(o in t for o in _OLDS) and not any(m_ in t for m_ in _MARKS)      # True where it was reported
    assert _uncorrected(name, text) == (0, 1) and not as_one_block(text)
    v = json.loads(text)
    in_another_field = dict(v, scope=dict(v["scope"], hypotheses=v["scope"]["hypotheses"] + "; the columns are the transpose that B1881 used"))
    at_the_end = dict(v, claim_one_line=v["claim_one_line"] + " " * _WITHIN + "The second ground is the transpose, which B1881 used.")
    for what, planted in (("in another field", in_another_field), ("at the end of the same line", at_the_end)):
        planted = json.dumps(planted, indent=1, ensure_ascii=False)
        assert not as_one_block(planted), what                                  # the lock as it was does not report it
        assert _uncorrected(name, planted) == (1, 2), what
    # a twin: the old words a second time with their correction beside them are not reported
    twin = json.dumps(dict(v, claim_one_line=v["claim_one_line"] + " " * _WITHIN + "the transpose, which B1881 used [it is not the transpose]"), indent=1, ensure_ascii=False)
    assert _uncorrected(name, twin) == (0, 2)


def test_the_old_word_stands_nowhere_on_main_without_its_correction():
    """The wrong sentence was written in two arcs and was sent to one session.  A paragraph that calls the columns a transpose
    must carry the correction, in itself or in the paragraph after it.  The files are found by git over frontier/ and docs/ where
    git can list them; the places this arc names are read in any case, so the test never skips.

    CHANGED 2026-11-12 (Review 80; a reader's finding F9): what may excuse the old words is `_carriers`, above; a verdict file
    is no longer one block.  The four lines that read a file as blocks stand in that function, for a page as they were."""
    olds, marks = _OLDS, _MARKS
    known = ["frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md", "frontier/B1881_the_whole_and_the_value_verified/arc_verdict.json",
             "frontier/B1884_what_level_a_ground_names_verified/FINDINGS.md", "frontier/B1884_what_level_a_ground_names_verified/verification/ground_level_on_main.py",
             "docs/seats/agy-exp.md"]
    cmd = ["git", "-C", str(ROOT), "grep", "-l", "-F"] + [x for o in olds for x in ("-e", o)] + ["--", "frontier", "docs"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    listed = [f for f in r.stdout.split("\n") if f] if r.returncode in (0, 1) else []
    files = sorted({f for f in known + listed if not f.startswith(("docs/views/", "frontier/B1895_"))})
    hits, carrying = [], 0
    for f in files:
        bad, held = _uncorrected(f, (ROOT / f).read_text(encoding="utf-8"))
        carrying += held
        hits += [f] * bad
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
    # ADDED 2026-11-12 (Review 80; a reader's finding F8): the verdict line is published on the verdict ledger and names no
    # session; the file's citation of the seat says who read, and so does the page
    assert "agy-" not in v["claim_one_line"] and "by a session that did not write them" in v["claim_one_line"]
    assert any(c.startswith("agy-002: ") for c in v["cites_seat"]) and "**The verdict line does not name the reader.**" in PAGE
    led = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
    assert "c67f84c1" in led and "B1895" in led


def test_a_plant_that_changes_nothing_stops_the_run():
    """ADDED 2026-11-12 (Review 80; owed by main's word in its third folder for the builder, section 6, item 4).  One of
    main's plants at Review 80, against another lock, changed nothing, and that lock's passing was read as a finding.  The
    runner of this arc's plants, which the arc B1897 and main's plants of Review 80 also use, reads its scratch copy before
    a plant and after it, and ends the run where the copy is as it was."""
    import importlib.util, shutil
    import pytest
    spec = importlib.util.spec_from_file_location("planted_reversions_for_its_guard", HERE / "planted_reversions.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    try:
        arc = m.fresh()
        m.made("the control", m.p_nothing, arc)                                   # plants nothing, changes nothing: passes
        with pytest.raises(SystemExit) as stopped:
            m.made("a plant whose pattern matches nothing", lambda a: None, arc)
        assert "changed nothing in the copy" in str(stopped.value)
        with pytest.raises(SystemExit):                                           # a file written back as it was is no plant either
            m.made("a file written back as it was", lambda a: (a / "FINDINGS.md").write_text((a / "FINDINGS.md").read_text(encoding="utf-8"), encoding="utf-8"), arc)
        m.made("a plant that adds one character", lambda a: (a / "FINDINGS.md").write_text((a / "FINDINGS.md").read_text(encoding="utf-8") + "x", encoding="utf-8"), arc)
        def a_control_that_changes(a):
            (a / "a_new_file.txt").write_text("x", encoding="utf-8")
        keep = m.p_nothing
        m.p_nothing = a_control_that_changes
        try:
            with pytest.raises(SystemExit) as stopped:
                m.made("the control", m.p_nothing, m.fresh())
            assert "plants nothing, and the copy is not as it was" in str(stopped.value)
        finally:
            m.p_nothing = keep
        # each of the arc's eighteen plants changes its copy (no lock is run here: the copy is read, and that is all)
        for name, fn in m.PLANTS[1:]:
            m.made(name, fn, m.fresh())
        assert len(m.PLANTS) == 19
    finally:
        shutil.rmtree(m.WORK.parent, ignore_errors=True)
