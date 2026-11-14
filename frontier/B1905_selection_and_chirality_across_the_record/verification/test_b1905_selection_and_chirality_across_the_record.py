"""B1905 -- the record read for selection and chirality: the lock.

The page, the verdict line, the rows and the script are main's.  The classes in the rows are the readers', one reader an
arc, and are not checked here or anywhere.  What this lock holds:

  1. the rows and the lists of arcs are the files main gave, by their digests;
  2. the tables are what main's script makes of the rows, and the kept table and the kept run say the same;
  3. every number on the page and in the verdict line is stated in a SENTENCE that is built here from the rows, and that
     sentence stands on the page or in the line (a number held as a digit alone is held nowhere: Review 80's lesson);
  4. every quotation is found at the commit the readers read.  Where that commit is not in the clone the test is skipped
     ALOUD, and a test that does not need the commit holds that the kept table was made with it;
  5. two plants fail: a quotation changed, and a class changed;
  6. the rule that came with the arc stands in the working rules, in main's words.

Main's script writes its kept table at every run.  This lock runs none of it as a process: it reads the script and calls
its functions, so that a test leaves the checkout as it found it."""
import copy
import hashlib
import json
import pathlib
import re
import subprocess
import types

import pytest

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = HERE.parents[2]
# main's fourth hand-over folder of 2026-11-12 left the tree with this arc (docs/REORGANIZATIONS.md); git has it at the
# last commit that held the folders between sessions, and the lock reads main's copies there
HANDED_OVER_AT = "9c8a50887de1288e2c6667a80c0f480f358f88bb"
HANDED_OVER = "docs/handoffs/MAIN_TO_BUILDER_2026-11-12_D/"


def _as_handed_over(path):
    r = subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s%s" % (HANDED_OVER_AT, HANDED_OVER, path)], capture_output=True)
    assert r.returncode == 0, "git has no %s%s at %s" % (HANDED_OVER, path, HANDED_OVER_AT)
    return r.stdout

ROWS_AS_MAIN_GAVE_THEM = "610863d00cb3b0abe3aa7109c35e4a6ae3ea88e17c4d2ce4076e6b5dc6e811a8"
LISTS_AS_MAIN_GAVE_THEM = "9f3221621707023c8d810282a278a511a32aacdc7f7ec4de8b067070462db860"
THE_RULE_AS_MAIN_GAVE_IT = "7b30300d734133ee30f00b80d095b61e5c77fa05385eb05fa14c176b4685cdf8"


def _mains():
    """main's script, read and compiled without an import, so that no compiled file is left beside it"""
    p = HERE / "sweep_tables.py"
    m = types.ModuleType("b1905_sweep_tables")
    m.__file__ = str(p)
    exec(compile(p.read_text(encoding="utf-8"), str(p), "exec"), m.__dict__)
    return m


ST = _mains()
ROWS = ST.load()
T = ST.tables(ROWS)
KEPT = json.loads((HERE / "sweep_tables.json").read_text(encoding="utf-8"))
PAGE = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
VERDICT = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
flat = lambda s: " ".join(s.split())
commas = lambda n: format(n, ",")

# the page's own names for the walls it tabulates and for the kinds of principle (the script's codes are W1.. and A..K)
WALLS_ON_THE_PAGE = (("W1", "the mirror pair not split"), ("W2", "one member of a family not picked"), ("W3", "a value or modulus not picked"),
                     ("W4", "a count not forced"), ("W7", "a construction not canonical"))
WALLS_NOT_ON_THE_PAGE = ("W5", "W6", "W8")
KINDS_ON_THE_PAGE = (("D", "uniqueness theorem"), ("C", "symmetry"), ("H", "what a read-out can see"), ("B", "census of all that is allowed"), ("F", "arithmetic"),
                     ("A", "extremum"), ("E", "consistency"), ("G", "dynamics, flow, rate"), ("I", "declared choice"), ("J", "measure, typicality"))
KINDS_IN_THE_LINE = (("D", "uniqueness"), ("C", "symmetry"), ("H", "a read-out"), ("B", "census"), ("F", "arithmetic"), ("A", "an extremum"), ("E", "consistency"),
                     ("G", "dynamics"), ("I", "a declared choice"), ("J", "a measure"))
PAIRS_ON_THE_PAGE = (("B+C", "symmetry with census"), ("C+F", "symmetry with arithmetic"), ("C+H", "symmetry with a read-out"), ("B+F", "census with arithmetic"),
                     ("C+D", "symmetry with uniqueness"), ("B+E", "census with consistency"), ("D+F", "uniqueness with arithmetic"))
share = lambda c: round(100 * c[0] / sum(c)) if sum(c) else 0


def _arcs_at_the_commit_read():
    """how many arcs main held at the commit the readers read, or None where that commit is not in the clone"""
    import subprocess
    if not ST.have(ST.READ):
        return None
    r = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "-d", "--name-only", ST.READ, "frontier/"], capture_output=True, text=True)
    return len([l for l in r.stdout.split("\n") if l.strip()])


def _the_sentences(rows, tables, lists, of_arcs):
    """(where, sentence) for each sentence that states a number: built from the rows, the tables and the lists"""
    w, k, pr = tables["wall by outcome"], tables["kind of principle by outcome, all walls"], tables["pairs of kinds used together"]
    by_wall = tables["kind of principle by outcome, wall by wall"]
    words = tables["settled or partly, by the words of the outcome"]
    asked = [r for r in rows if not (r["topic"] == "neither" and r["quote"] in ("n/a", ""))]
    n, live, neither = len(rows), tables["about selection or chirality"], tables["neither on reading"]
    S = []
    S.append(("page", "%d of %s arcs have selection or chirality in their verdict line or title; %d are about one of them on reading." % (n, commas(of_arcs), live)))
    S.append(("page", "%d arcs on selection, %d on chirality, %d in the union." % (len(lists["selection"]), len(lists["chirality"]), len(lists["union"]))))
    S.append(("page", "Six readers, %d arcs each," % (n // 6)))
    S.append(("page", "%d rows, every one with its 13 keys; %d are \"neither\" on reading. %d rows carry a quotation (the %d, and %d of the \"neither\" rows):"
              % (n, neither, len(asked), live, len(asked) - live)))
    S.append(("page", "## 3. The tables (%d arcs)" % live))
    for code, name in WALLS_ON_THE_PAGE:
        S.append(("page", "| %s | %d | %s |" % (name, sum(w[code]), " | ".join(str(x) for x in w[code]))))
    for code, name in KINDS_ON_THE_PAGE:
        S.append(("page", "| %s | %d | %s | %d%% |" % (name, sum(k[code]), " | ".join(str(x) for x in k[code]), share(k[code]))))
    S.append(("page", "**The mirror pair (%d settled or partly).** %d say that the route does not split the pair; %d say something is fixed,"
              % (w["W1"][0] + w["W1"][1], words["W1"].get("does not pick", 0), words["W1"].get("picks", 0))))
    S.append(("page", "**One member of a family (%d settled or partly).**" % (w["W2"][0] + w["W2"][1])))
    S.append(("page", "A measure: %d settled of %d. An extremum: %d settled of %d, %d corrected."
              % (by_wall["W2"]["J"][0], sum(by_wall["W2"]["J"]), by_wall["W2"]["A"][0], sum(by_wall["W2"]["A"]), by_wall["W2"]["A"][4])))
    S.append(("page", "**A value (%d settled or partly).**" % (w["W3"][0] + w["W3"][1])))
    S.append(("page", ", ".join("%s %d" % (name, pr[code]) for code, name in PAIRS_ON_THE_PAGE) + "."))
    S.append(("line", "%d of %s arcs name either subject in their verdict line or title; %d are about one of them on reading" % (n, commas(of_arcs), live)))
    S.append(("line", "%d of %d quotations found by machine at the commit read" % (len(asked), len(asked))))
    S.append(("line", "The walls: the mirror pair not split, %d arcs; one member of a family not picked, %d; a value not picked, %d; a count not forced, %d."
              % (sum(w["W1"]), sum(w["W2"]), sum(w["W3"]), sum(w["W4"]))))
    S.append(("line", ", ".join("%s %d%%" % (name, share(k[code])) for code, name in KINDS_IN_THE_LINE) + "."))
    S.append(("scope", "the %d arcs whose verdict line or title the topic sweep matched for the words of selection or of chirality, of %s" % (n, commas(of_arcs))))
    return S


def _what_is_not_said(rows, tables, lists, of_arcs, page=None, verdict=None):
    """the sentences, built from the rows, that the page, the verdict line or the scope does not hold"""
    page = PAGE if page is None else page
    verdict = VERDICT if verdict is None else verdict
    text = {"page": flat(page), "line": flat(verdict["claim_one_line"]), "scope": flat(verdict["scope"]["object"])}
    return [(where, s) for where, s in _the_sentences(rows, tables, lists, of_arcs) if flat(s) not in text[where]]


LISTS = json.loads((HERE / "arcs_by_title.json").read_text(encoding="utf-8"))
OF_ARCS = 1644                                              # the arcs at the commit read; counted by test_the_count_of_arcs... where the commit is in the clone


def test_the_rows_and_the_lists_are_the_files_main_gave():
    assert hashlib.sha256((HERE / "rows.json.txt").read_bytes()).hexdigest() == ROWS_AS_MAIN_GAVE_THEM
    assert hashlib.sha256((HERE / "arcs_by_title.json").read_bytes()).hexdigest() == LISTS_AS_MAIN_GAVE_THEM
    assert len(ROWS) == len({r["arc"] for r in ROWS}) == len(LISTS["union"]) and {r["arc"] for r in ROWS} == set(LISTS["union"])
    assert set(LISTS["selection"]) | set(LISTS["chirality"]) == set(LISTS["union"])
    assert all(sorted(r) == sorted(ST.KEYS) for r in ROWS)
    # the two files are also in the folder main handed over, and are the same files there (the folder is in git's
    # history since it left the tree with this arc)
    for name in ("rows.json.txt", "arcs_by_title.json", "sweep_tables.py"):
        assert _as_handed_over("b1905_selection_and_chirality/verification/" + name) == (HERE / name).read_bytes(), name
    assert not (ROOT / HANDED_OVER).exists(), "the hand-over folder left the tree with this arc"


def test_the_tables_are_what_mains_script_makes_of_the_rows():
    assert json.loads(json.dumps(T, ensure_ascii=False)) == KEPT["the tables"]
    # every row that is about either subject is in exactly one of the eight walls, and the walls sum to them
    assert sum(sum(c) for c in T["wall by outcome"].values()) == T["about selection or chirality"] == len(ROWS) - T["neither on reading"]
    assert set(T["wall by outcome"]) == {c for c, _ in WALLS_ON_THE_PAGE} | set(WALLS_NOT_ON_THE_PAGE)


def test_the_kept_run_gives_the_numbers_of_the_tables():
    run = (HERE / "sweep_tables_run.txt").read_text(encoding="utf-8")
    assert run.split("\n")[0] == "rows %d; about selection or chirality %d; neither on reading %d" % (T["rows"], T["about selection or chirality"], T["neither on reading"])
    assert json.loads(run.split("\n")[1][len("quotations: "):]) == KEPT["the quotations"]
    for code, c in T["wall by outcome"].items():
        m = re.search(r"^  %s .*?(\d+)((?:\s+\d+){5})\s*$" % code, run, re.M)
        assert m and [int(m.group(1))] + [int(x) for x in m.group(2).split()] == [sum(c)] + c, code
    head = run[run.index("KIND OF PRINCIPLE, all walls"):run.index("\nW1, ")]
    for code, c in T["kind of principle by outcome, all walls"].items():
        m = re.search(r"^  %s \S+\s+(\d+)((?:\s+\d+){5})\s+(\d+)%%\s*$" % code, head, re.M)
        assert m and [int(m.group(1))] + [int(x) for x in m.group(2).split()] + [int(m.group(3))] == [sum(c)] + c + [share(c)], code


def test_every_number_of_the_page_and_of_the_verdict_line_stands_in_a_sentence_built_from_the_rows():
    assert _what_is_not_said(ROWS, T, LISTS, OF_ARCS) == []
    # the verdict file is the arc's: its verdict, and what it rests on
    assert VERDICT["id"] == "B1905" and VERDICT["verdict"] == "PROVED" and VERDICT["depends_on"] == ["B1204", "B1225"]
    assert "The classes are the readers' and are not independently checked." in VERDICT["claim_one_line"]
    assert "The classes are the readers' and are not independently checked." in flat(PAGE)


def test_the_count_of_arcs_is_the_count_at_the_commit_read():
    n = _arcs_at_the_commit_read()
    if n is None:
        pytest.skip("the commit the readers read, %s, is not in this clone: the arcs at that commit are not counted" % ST.READ)
    assert n == OF_ARCS


def test_the_kept_table_was_made_with_the_commit_in_the_clone():
    q = KEPT["the quotations"]
    assert "NOT RUN" not in q and q["the commit read"] == ST.READ
    asked = [r for r in ROWS if not (r["topic"] == "neither" and r["quote"] in ("n/a", ""))]
    assert q["quotations"] == q["found on one line of the file named, at the commit read"] == len(asked) and q["not found"] == [] and q["controls found"] == 0


def test_every_quotation_is_found_at_the_commit_the_readers_read():
    if not ST.have(ST.READ):
        pytest.skip("the commit the readers read, %s, is not in this clone: NO QUOTATION IS LOOKED FOR HERE" % ST.READ)
    assert ST.quotes(ROWS) == KEPT["the quotations"]


def test_a_changed_quotation_fails():
    """main's first plant.  The digest sees it without the commit; with the commit the script names the arc."""
    rows = copy.deepcopy(ROWS)
    i = next(i for i, r in enumerate(rows) if r["topic"] != "neither" and len(r["quote"].split()) > 3)
    words = rows[i]["quote"].split(" ")
    rows[i]["quote"] = " ".join(words[:1] + ["never"] + words[1:])
    planted = "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n"
    assert hashlib.sha256(planted.encode("utf-8")).hexdigest() != ROWS_AS_MAIN_GAVE_THEM
    if not ST.have(ST.READ):
        pytest.skip("the commit the readers read, %s, is not in this clone: the plant is seen by the digest alone" % ST.READ)
    q = ST.quotes(rows)
    assert q["not found"] == [rows[i]["arc"]] and q["found on one line of the file named, at the commit read"] == q["quotations"] - 1


def test_a_changed_class_fails():
    """main's second plant: one arc moved from one wall to another.  Three things see it."""
    rows = copy.deepcopy(ROWS)
    i = next(i for i, r in enumerate(rows) if r["wall"].startswith("W1"))
    rows[i]["wall"] = "W2 one member of a family not picked (thread, root, object)"
    planted = "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n"
    assert hashlib.sha256(planted.encode("utf-8")).hexdigest() != ROWS_AS_MAIN_GAVE_THEM                    # the digest
    t = ST.tables(rows)
    assert json.loads(json.dumps(t, ensure_ascii=False)) != KEPT["the tables"]                              # the tables
    lack = _what_is_not_said(rows, t, LISTS, OF_ARCS)                                                       # the sentences
    assert ("page", "| the mirror pair not split | %d | %s |" % (sum(t["wall by outcome"]["W1"]), " | ".join(str(x) for x in t["wall by outcome"]["W1"]))) in lack
    assert any(where == "line" and s.startswith("The walls: the mirror pair not split, ") for where, s in lack)
    # the twin: the rows as they are say everything
    assert _what_is_not_said(ROWS, T, LISTS, OF_ARCS) == []
    # and a number changed on the page, with the rows as they are, is seen as well
    assert _what_is_not_said(ROWS, T, LISTS, OF_ARCS, page=PAGE.replace("| the mirror pair not split | 149 |", "| the mirror pair not split | 150 |")) != []
    line = dict(VERDICT, claim_one_line=VERDICT["claim_one_line"].replace("a measure 0%", "a measure 4%"))
    assert [w for w, _ in _what_is_not_said(ROWS, T, LISTS, OF_ARCS, verdict=line)] == ["line"]


def test_the_rule_that_came_with_the_arc_stands_in_the_working_rules_in_mains_words():
    rules = (ROOT / "WORKING_RULES.md").read_text(encoding="utf-8")
    head = "## Rule (2026-11-12, after the owner's question on selection and his point on the record's walls — adopted): BEFORE A SELECTION OR A HAND IS CLAIMED"
    assert rules.count(head) == 1
    section = rules[rules.index(head):]
    section = section[:section.index("\n## ", 5)] if "\n## " in section[5:] else section
    assert hashlib.sha256(flat(section).encode("utf-8")).hexdigest() == THE_RULE_AS_MAIN_GAVE_IT
    # the same words stand in main's folder, as a quoted block
    card = _as_handed_over("README.md").decode("utf-8")
    block = "\n".join(l[4:] if l.startswith("   > ") else l[3:].lstrip("> ").rstrip() if l.strip() == ">" else l for l in card.split("\n") if l.startswith("   >"))
    assert flat(block) == flat(section)
    assert "the rule in `WORKING_RULES.md`, \"BEFORE A SELECTION OR A HAND IS CLAIMED\"" in flat(PAGE)
