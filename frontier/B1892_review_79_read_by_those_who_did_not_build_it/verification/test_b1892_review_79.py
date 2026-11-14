"""B1892 lock -- Review 79's evidence.

What could fail: a finding in the table with no row in the count, or twice; a quotation of a reader's file that is not in the file it
names at the commit read; the planted suite's output not saying what the page says; the entry's anchor not being the commit the
readers read; a number on the page that is not the evidence's."""
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
    rows = re.findall(r"^\| ((?:W|SM-|A|X)\d+) \|", (ARC / "ANSWERS.md").read_text(encoding="utf-8"), re.M)
    assert rows == A["ids"] and len(rows) == len(set(rows)) == A["findings"] == sum(A["by reader"].values())
    assert sum(1 for r in rows if r.startswith("W")) == A["by reader"]["the web seat"]
    assert sum(1 for r in rows if r.startswith("SM-")) == A["by reader"]["the SM seat"]
    assert sum(1 for r in rows if re.fullmatch(r"A\d+", r)) == A["by reader"]["agy-002"]
    assert sum(1 for r in rows if re.fullmatch(r"X\d+", r)) == A["by reader"]["agy-exp"]
    assert len(A["by reader"]) == 4
    twice = {x for group in A["reported by two readers"] for x in group}
    assert twice <= set(rows) and A["distinct faults"] == A["findings"] - sum(len(g) - 1 for g in A["reported by two readers"]) + 1          # one finding of the second reader, A6, stands in two groups
    assert set(A["sent on to the builder of the enforcement package"]) <= set(rows) and set(A["not mended"]) <= set(rows)
    assert "%d findings, and all %d held" % (A["findings"], A["held"]) in F and "%d distinct faults" % A["distinct faults"] in F


def test_every_quotation_was_found_and_the_check_can_fail():
    q = json.loads((HERE / "quote_check.json").read_text(encoding="utf-8"))
    assert set(q) == {"the SM seat", "the web seat", "agy-002", "agy-exp"}
    assert all(v["quotations"] == v["found"] > 0 for v in q.values())
    assert q["the SM seat"]["control: the first quotation altered by one character is reported missing"] is True
    total = sum(v["quotations"] for v in q.values())
    assert "%d of %d" % (total, total) in F
    # where the readers' commits are in this clone, the check is run again and must give the committed result
    spec = importlib.util.spec_from_file_location("b1892_quote_check", HERE / "quote_check.py"); qc = importlib.util.module_from_spec(spec); spec.loader.exec_module(qc)
    again = qc.build()
    for reader, r in again.items():
        assert r is None or r == q[reader], reader
    # [ADDED 2026-11-12 (Review 80).  A session that built none of this planted five cases against the script and this lock, and
    #  all five passed.  What is held now: each quotation is placed strictly; an empty quotation is not found; a quotation set
    #  under the wrong file is not placed in it; the rows the script does not read are counted and are what they were found to
    #  be; and where no reader's commit is in the clone this test says that it did not run, and does not pass in silence.]
    placed = {k: (v["in the file the finding names"], v["in the arc's own folder, no file being named"], v["on a wide page only"], v["placed nowhere"]) for k, v in q.items()}
    assert placed == {"the SM seat": (0, 45, 14, 0), "the web seat": (11, 0, 0, 0), "agy-002": (26, 0, 0, 0), "agy-exp": (15, 0, 0, 0)}
    assert all(sum(placed[k]) == q[k]["quotations"] for k in q)
    assert [(q[k]["rows with more cells than their table's header"], q[k]["lines that begin as a row and give fewer than four cells"]) for k in ("the SM seat", "the web seat", "agy-002", "agy-exp")] \
        == [(0, 0), (0, 6), (0, 0), (0, 0)]            # the six are rows of the web seat's table of what it read, of three cells: no finding
    if all(r is None for r in again.values()):
        import pytest
        pytest.skip("no reader's commit is in this clone: the quotations were not looked for again here")
    read = ("0dda7b472",)
    named = "frontier/B1892_review_79_read_by_those_who_did_not_build_it/FINDINGS.md"
    assert qc.found("", "B1892", named, read) is False and qc.placed("", "B1892", named, read) is None
    words = qc.text("0dda7b472", "WORKING_RULES.md").split()
    theirs = " ".join(words[40:58])                                             # eighteen words of the working rules
    assert theirs not in qc.text("0dda7b472", "frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md")
    assert qc.found(theirs, "B1881", "frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md", read) is True      # the wide rule: found, in a wide page
    assert qc.placed(theirs, "B1881", "frontier/B1881_the_whole_and_the_value_verified/FINDINGS.md", read) == "wide"   # the strict one: not in the file named
    table = "| arc | file | quoted | wrong |\n|---|---|---|---|\n| B1 | `a.md` | one half | the other half | wrong |\n|B1|`a.md`|compact|wrong|\n"
    assert qc.rows_not_read("agy-002", table) == (1, 1)


def test_the_planted_suites_output_says_what_the_page_says():
    out = (HERE / "planted_suite_on_main_0dda7b472_out.txt").read_text(encoding="utf-8")
    cases = [l for l in out.split("\n") if re.match(r"^PV\d+\s+\S+\s+(NOT CAUGHT|CAUGHT)", l)]
    caught = [l for l in cases if not re.match(r"^PV\d+\s+\S+\s+NOT CAUGHT", l)]
    controls = [l for l in out.split("\n") if l.startswith("CTL")]
    assert "planted-violation suite at origin/main (0dda7b472)" in out and "controls not reported CAUGHT: 0" in out
    assert (len(caught), len(cases), len(controls)) == (14, 32, 5)
    assert "14 of 32 planted cases caught" in F and "controls 5 of 5" in F


def test_the_entry_is_anchored_on_the_commit_the_readers_read():
    r = (ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8")
    k = r.index("# Review 79 (")
    entry = r[k:]
    assert "### Action items (Review 79)" in entry and re.search(r"\*\*anchor-commit: `0dda7b472`\*\*", entry)
    assert "- [ ] R78-" not in r                                   # the last review's block is closed or carried, item by item
    assert "B1892" in entry and "%d findings" % A["findings"] in entry and "%d distinct faults" % A["distinct faults"] in entry


def test_the_arc_says_what_it_did_not_do():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The fourth reader delivered last", "No reader was tested against planted faults", "Read once only", "What main got wrong in running this review",
              "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1892" and set(v["scope"]) == {"frame", "object", "reach", "hypotheses"} and v["claim_one_line"].endswith("0 of 19.")


def _what_two_readers_found(page):
    """the table of section 5, counted: (rows, the first reader's findings, the second's, those found by both)"""
    section = page[page.index("## 5. What two readers found in common"):]
    section = section[:section.index("\n## ", 5)]
    rows = [[c.strip() for c in l.strip().strip("|").split(" | ")] for l in section.split("\n") if l.startswith("| ") and not l.startswith("| what")]
    rows = [r for r in rows if len(r) == 4]
    leading = lambda cell: int(re.match(r"\d+", cell).group(0))
    return (len(rows),) + tuple(sum(leading(r[k]) for r in rows) for k in (1, 2, 3))


def test_the_table_of_what_two_readers_found_and_the_sentences_that_count_it():
    """ADDED 2026-11-12 (Review 80; a reader's check of main's answers, its row A1, held by main).  The table of section 5 was
    corrected to sum to 53 and 43, and a note added to the page in the same commit said 52 for the first reader; nothing
    counted the table.  It is counted here, and the page and the verdict line are held to the count."""
    page = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    rows, first, second, both = _what_two_readers_found(page)
    assert (rows, first, second, both) == (16, 53, 43, 9)
    together = first + second - both
    assert together == 87 and 2 * first > together and 2 * second < together       # by the table: the first reading more than half, the second just under
    # Built again on main's 663a902ff (2026-11-13): main corrected the page itself at Review 81 (the web seat's finding 4):
    # its bracket gives 53, as the table sums, and says the conclusion holds.  The page and the verdict line are main's and
    # are not held here to this seat's sentences; that the second reading's 43 of 87 is under half is sent back to main.
    assert "the first reader has 52 findings" in F and "53, as § 5's table sums after its own correction" in F
    assert F.index("the first reader has 52 findings") < F.index("53, as § 5's table sums after its own correction")
    # that the count can fail: one number of one row changed
    changed = page.replace("| B1879 | 10 | 0 | 0 |", "| B1879 | 9 | 0 | 0 |")
    assert changed != page and _what_two_readers_found(changed) == (16, 52, 43, 9)
