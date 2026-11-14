"""B1894 lock -- Review 79's second round.

What could fail: a finding in the table with no row in the count, or twice; a quotation of a reader's file that is not in the
file it names at the commit read; a number on the page that is not the data's; the sign the round corrected standing again in
one of the four places; a mend the table names being undone."""
import importlib.util
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = ARC.parents[1]
A = json.loads((HERE / "answers.json").read_text(encoding="utf-8"))
F = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())


def test_the_table_and_the_count_are_one():
    rows = re.findall(r"^\| (2(?:W|SM-|A|X)\d+) \|", (ARC / "ANSWERS.md").read_text(encoding="utf-8"), re.M)
    assert rows == A["ids"] and len(rows) == len(set(rows)) == A["findings"] == sum(A["by reader"].values())
    for prefix, reader in (("2W", "the web seat"), ("2SM-", "the SM seat"), ("2A", "agy-002"), ("2X", "agy-exp")):
        assert sum(1 for r in rows if re.fullmatch(re.escape(prefix) + r"\d+", r)) == A["by reader"][reader], reader
    assert A["held in full"] + len(A["reproduced in part"]) == A["findings"]
    groups = A["found by more than one reader"]
    assert {x for g in groups for x in g} <= set(rows) and A["distinct faults"] == A["findings"] - sum(len(g) - 1 for g in groups)
    assert set(A["a correction that did not travel"]) <= set(rows)
    assert "%d findings on main's mends, and all held" % A["findings"] in F and "%d distinct faults" % A["distinct faults"] in F
    n = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
    assert "%s of the %d" % (n[len(A["a correction that did not travel"])].capitalize(), A["findings"]) in F


def test_the_readers_check_of_the_ninety_nine_adds_up_and_is_what_the_page_says():
    c = A["the readers' check of main's 99 answers"]
    total = {k: sum(v.get(k, 0) for v in c.values()) for k in ("checked", "right and complete", "not complete", "not mended, as main had said", "with the builder")}
    assert total["checked"] == 99 == sum(total[k] for k in total if k != "checked")
    assert "They report %d right and complete, %d not complete" % (total["right and complete"], total["not complete"]) in F
    assert "and %d still with the builder" % total["with the builder"] in F
    t = A["the tripwire against planted errors, by the SM seat"]
    assert "| the first round's planted errors, against the lock as it was then | %d of %d that were faults |" % (t["caught at the first round"], t["the first round's errors that were faults"]) in F
    assert "| the same errors, against the lock as mended at Review 79 | %d of %d |" % (t["caught after Review 79's mend"], t["the first round's errors that were faults"]) in F
    assert "| %d new errors, against the lock as mended at Review 79 | %d |" % (t["new errors"], t["new errors caught"]) in F


def test_every_quotation_was_found_and_the_check_can_fail():
    q = json.loads((HERE / "quote_check.json").read_text(encoding="utf-8"))
    assert set(q) == {"the SM seat", "the web seat", "agy-002", "agy-exp"}
    sm = q["the SM seat"]
    assert sm["found"] + sm["of its own first file, found there"] == sm["quotations"] and sm["found nowhere"] == 0
    assert all(v["quotations"] == v["found"] > 0 for k, v in q.items() if k != "the SM seat")
    assert sm["control: the first quotation altered by one character is reported missing"] is True
    in_main = sum(v["found"] for v in q.values())
    assert "%d of %d in main's files" % (in_main, in_main) in F
    spec = importlib.util.spec_from_file_location("b1894_quote_check", HERE / "quote_check.py"); qc = importlib.util.module_from_spec(spec); spec.loader.exec_module(qc)
    # ADDED 2026-11-12 (Review 80; a reader's finding F7).  Where each quotation stands, strictly, as B1892's checker says since
    # that day: of the 38 found in main's files, 26 stand in the file their finding names; the SM seat's findings name
    # neither an arc nor a file, and its 12 are placed in the pages swept (11) and on a wide page (1).  None is placed nowhere
    # but the two of the SM seat's own first file.  No line of a reader's table goes unread.
    placing = {k: sum(v[k] for v in q.values()) for k in ("in the file the finding names", "in the arc's own folder, no file being named",
                                                         "in the pages swept, neither an arc nor a file being named", "on a wide page only", "placed nowhere")}
    assert list(placing.values()) == [26, 0, 11, 1, 2] and sum(list(placing.values())[:4]) == in_main
    assert q["the SM seat"]["placed nowhere"] == q["the SM seat"]["of its own first file, found there"] == 2
    assert all(v["rows with more cells than their table's header"] == v["lines that begin as a row and give fewer than four cells"] == 0 for v in q.values())
    assert "26 stand in the file their finding names" in F and "11 in the pages the checker sweeps" in F
    # an empty quotation is a quotation of nothing; a quotation that names a file is not placed by standing in another
    assert qc.found("", "B1894", None) is False and qc.placed("", "B1894", None) is None
    other = "No item is added and no status cell changes."                       # a sentence of the foundation, a wide page
    assert qc.found(other, "B1894", "frontier/B1894_review_79_the_second_round/FINDINGS.md") is True       # the pool finds it
    assert qc.placed(other, "B1894", "frontier/B1894_review_79_the_second_round/FINDINGS.md") == "wide"    # the strict placing says where
    built = qc.build()
    if all(r is None for r in built.values()):
        # CHANGED 2026-11-12 (Review 80; the same finding): with no reader's commit in the clone every result is None and the
        # loop below passed without a word.  It says so aloud, as B1892's lock does.
        import pytest
        pytest.skip("no reader's commit is in this clone: the quotations were not looked for again here")
    for reader, r in built.items():
        assert r is None or r == q[reader], reader


def test_the_sign_stands_corrected_in_the_four_places():
    old = "the index is their sum above its value at no unit, so a unit on one line gives one"
    for rel in ("docs/THEOREM_REGISTRY.md", "docs/LAW_MAP.md", "frontier/B1641_w46_on_main_and_the_two_objects/arc_verdict.json"):
        t = (ROOT / rel).read_text(encoding="utf-8")
        assert t.count(old) == 1, rel                                   # kept once, inside the bracket that corrects it
        i = t.index(old)
        assert "This bracket first read" in t[i - 60:i] and "minus the sum of the units: -3 for the uniform unit" in t[i - 700:i], rel
    note = (ROOT / "frontier" / "B1641_w46_on_main_and_the_two_objects" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "CORRECTED 2026-11-12, a second time" in note and "gives the index −3, and a unit on" in note
    table = json.loads((ROOT / "frontier" / "B1641_w46_on_main_and_the_two_objects" / "verification" / "w46_on_main.json").read_text(encoding="utf-8"))["W3"]
    assert all(round(ident["table"]["0,n=1"][0]) == -3 and round(ident["table"]["0,n=-1"][0]) == 3 for ident in table.values())


# ---- Review 80 (2026-11-12; the SM seat's finding 27, checked by main by a search).  The test above looks for the old sentence
# in one exact wording.  The old sign stood in two more wordings, on four pages, and neither was seen.
_OLD_SIGN = ("a unit on one line gives index one",
             "the index it cites is for a unit that is the same on the cusp's three lines; a unit on one line gives one")
_THE_SIGN = ("-1 for a unit on one line", "−1 for a unit on one line")
_SIGN_WITHIN = 700


def _old_sign_uncorrected(text):
    """The places where a text gives the index of a unit on one line as one and does not give its sign: within 700 characters
    after the words, or, for a message under a heading of its own, in the first 700 characters under that heading, where a
    note at the head of a message stands."""
    out = []
    for section in text.split("\n### "):
        flat = " ".join(section.split())
        for old in _OLD_SIGN:
            at = flat.find(old)
            while at != -1:
                if not any(s in flat[at:at + len(old) + _SIGN_WITHIN] or s in flat[:_SIGN_WITHIN] for s in _THE_SIGN):
                    out.append(old)
                at = flat.find(old, at + 1)
    return out


def test_the_old_sign_stands_corrected_in_its_other_wordings():
    """Four pages gave the index of a unit on one line as one, in words the test above does not look for: the changelog's
    entry of 2026-11-11, the harvest ledger's row 1709, the law map's currency read, and main's fourth message to the
    session whose finding it was.  Each carries the correction beside it now.  Planted: each page with its correction taken
    out, which is the page as it stood; the test above passes on all four."""
    pages = {"CHANGELOG.md": 1, "docs/HARVEST_LEDGER.md": 1, "docs/LAW_MAP.md": 1, "docs/seats/agy-002.md": 2}
    for rel, n in pages.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        flat = " ".join(text.split())
        assert sum(flat.count(o) for o in _OLD_SIGN) == n, rel       # the old words are kept: once on each page, and once more in the message's own note
        assert _old_sign_uncorrected(text) == [], rel
        # the page as it stood: every correction of Review 80 taken out again
        stood = text
        for mark in ("[CORRECTED 2026-11-12 (Review 80; a reader's finding, checked by main by a search):", "[CORRECTED 2026-11-12, in the entry of Review 80's mends:",
                     "*[NOTE 2026-11-12 (Review 80; a reader's finding, checked by main by a search), added at the head"):
            while mark in stood:
                i = stood.index(mark)
                stood = stood[:i] + stood[stood.index("]", i) + 1:]
        assert stood != text and len(_old_sign_uncorrected(stood)) == 1, rel


def test_the_arc_says_what_it_did_not_do():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("were not run against the tripwire's new form", "have been read by nobody but main", "What main got wrong in this round", "Not closed, and asserted as open",
              "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1894" and set(v["scope"]) == {"frame", "object", "reach", "hypotheses"} and v["scope"]["reach"] in ("single", "class", "general")
    assert v["claim_one_line"].endswith("0 of 19.")
