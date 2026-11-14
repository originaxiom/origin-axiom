"""B1898 lock -- Review 80's evidence: main's two tables, its checks, and the counts made from them.

What could fail: a row of either table deleted or added; a row's check or state changed (a finding that only its reader
looked at written as checked; a finding that waits written as mended); a file of main's changed in this arc; an output
main kept changed; a count on the arc's page, on its verdict line or in the review's entry that is not the recount's; a
quotation of a reader's file that is no longer found at the commit read; the entry's anchor not being that commit.

What it runs, and what it only holds.  It runs the recount, and three of main's four checks of quotations, which take
under a second together.  The fourth takes about a minute and is held with every other check of main's: by the hash of
the script and of the output main kept.  A check that needs a commit this clone does not hold says aloud that it did not
run; it does not pass in silence."""
import hashlib
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = ARC.parents[1]
R = json.loads((HERE / "recount.json").read_text(encoding="utf-8"))
T, K, G = R["the two tables"], R["the outputs main kept"], R["git"]
HELD = json.loads((HERE / "as_main_wrote_them.json").read_text(encoding="utf-8"))
F = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
V = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
READ = R["the commits"]["the readers read"]


def _recount():
    spec = importlib.util.spec_from_file_location("b1898_recount", HERE / "recount.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _have(commit):
    return subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", commit + "^{commit}"], capture_output=True).returncode == 0


_THE_FIRST_TABLE_AS_MAIN_WROTE_IT = "3f695c3045d46fe4a9cb31ba381b8bfede178282aac8958f26bed51a60d7eb22"
_THE_NOTE_AT_ITS_HEAD = "*[CORRECTED 2026-11-12, after it was written (Review 80; the web seat's finding 11 of its second addition, checked\nby main)."


def _under_its_note(text):
    """the first table without the dated note at its head: the title, then everything after the note's paragraph"""
    title = "# Review 80: every finding of the readers, and what main did with it\n\n"
    if not text.startswith(title + _THE_NOTE_AT_ITS_HEAD):
        return text
    rest = text[len(title):]
    return title + rest[rest.index("]*\n\n") + len("]*\n\n"):]


def test_the_first_table_is_as_main_wrote_it_under_one_dated_note():
    """Added 2026-11-12 (Review 80; the web seat's finding 11 of its second addition, checked by main).  The first table said
    "reproduced" for main's own checks and was headed as a draft with two of four files in.  A dated note at its head says so
    and changes no word below it.  Held here: without that note the file is main's, by the hash of main's own file; and the
    note says the two things.  Planted: a word changed under the note, and a second paragraph slipped in after the note."""
    text = (ARC / "ANSWERS_the_first_43.md").read_text(encoding="utf-8")
    sha = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()
    assert text.count(_THE_NOTE_AT_ITS_HEAD) == 1 and sha(_under_its_note(text)) == _THE_FIRST_TABLE_AS_MAIN_WROTE_IT
    note = text[text.index(_THE_NOTE_AT_ITS_HEAD):text.index("]*\n\n") + 2]
    assert "all four were in when the file was committed" in note and "They are not the label \"reproduced\" of the protocol's § 12" in note
    changed = text.replace("| W1 |", "| W1 [changed] |", 1)
    assert changed != text and sha(_under_its_note(changed)) != _THE_FIRST_TABLE_AS_MAIN_WROTE_IT
    slipped = text.replace("]*\n\n", "]*\n\nA second paragraph, not main's.\n\n", 1)
    assert sha(_under_its_note(slipped)) != _THE_FIRST_TABLE_AS_MAIN_WROTE_IT


def test_mains_files_are_as_main_wrote_them():
    """the two tables and every check, by hash.  The hashes are of main's own files in its folder of 2026-11-12.
    CHANGED 2026-11-12 (Review 80): the first table has one dated note at its head since that day, in the folder and here;
    its hash is of the file with the note, and the test above holds that under the note it is the file main wrote."""
    names = ["ANSWERS_the_first_43.md", "STATUS_OF_THE_57.md"] + sorted("verification/checks/" + p.name for p in (HERE / "checks").iterdir())
    assert names == sorted(HELD, key=lambda n: (not n.endswith(".md"), n)) and len(names) == 26
    for name in names:
        assert hashlib.sha256((ARC / name).read_bytes()).hexdigest() == HELD[name], name + " is not the file main wrote"
    # while main's folder stands in the tree, each file is the folder's, byte for byte
    folder = ROOT / "docs" / "handoffs" / "MAIN_TO_BUILDER_2026-11-12" / "review80"
    for name in names:
        theirs = folder / name.replace("verification/", "")
        if theirs.is_file():
            assert theirs.read_bytes() == (ARC / name).read_bytes(), name


def _with_its_mends_put_back(text):
    """a mended script as main wrote it: the note taken out, and each marked block replaced by the lines after '#| '"""
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        if lines[i].startswith("# NOTE OF THE MEND"):
            while not lines[i].startswith("# END OF THE NOTE"):
                i += 1
            i += 1
            continue
        if lines[i].startswith("# MENDED ("):
            i += 1
            while lines[i].startswith("#| "):
                out.append(lines[i][3:])
                i += 1
            while not lines[i].startswith("# END OF THE MEND"):
                i += 1
            i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def test_three_probes_of_mains_are_mended_beside_the_files_main_wrote():
    """ADDED 2026-11-12 (R80b, part 6; three things the builder sent back with R80a, main's faults by its word): a recount
    that changed with the machine's zone and with a commit that is in main's repository alone; a probe that ended in an
    error; a kept output with no script.  Main's files in checks/ stand as main wrote them (the test above).  The mended
    ones stand beside them, and this holds what they are."""
    import datetime
    M = HERE / "mended_in_r80b"
    sha = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()
    # 1. the two mended scripts are main's but for their marked blocks
    # (2026-11-12, the next patch of the same part: three more, for what main's third folder owes in its section 6, item 4)
    for name, blocks in (("sm_rows_probe.py", 4), ("builder_rows_probe.py", 2), ("plants_agy002.py", 5), ("plants_b1881_third.py", 2), ("quote_check_agy002.py", 1)):
        text = (M / name).read_text(encoding="utf-8")
        assert text.count("\n# MENDED (") == text.count("\n# END OF THE MEND") == blocks and text.count("# NOTE OF THE MEND") == 1, name
        assert sha(_with_its_mends_put_back(text)) == HELD["verification/checks/" + name], name + ": with its mends put back it is not main's file"
        assert sha(_with_its_mends_put_back("#| x".join(text.rsplit("#| ", 1)))) != HELD["verification/checks/" + name]      # and this can fail
    # 2. the recount of the SM seat's rows no longer changes with the machine: two rows differ from the file main kept
    kept = json.loads((HERE / "checks" / "sm_rows_probe.json").read_text(encoding="utf-8"))
    mended = json.loads((M / "sm_rows_probe.json").read_text(encoding="utf-8"))
    assert sorted(k for k in kept if kept[k] != mended.get(k)) == ["SM-04", "SM-16"] and list(kept) == list(mended) and len(mended) == 15
    assert kept["SM-16"]["held"] is False and mended["SM-16"]["held"] is True          # main's table gives the row as held
    assert all(v["held"] for v in mended.values()) and sum(v["held"] for v in kept.values()) == 14
    assert "| 16 |" in (ARC / "STATUS_OF_THE_57.md").read_text(encoding="utf-8")
    was, now = kept["SM-04"]["main finds"], mended["SM-04"]["main finds"]
    hours = set()
    for k in ("last message", "c66c8ccae", "entry"):
        assert now[k].endswith(" UTC") and not was[k].endswith("UTC"), k
        a = datetime.datetime.strptime(was[k], "%Y-%m-%d %H:%M:%S")
        b = datetime.datetime.strptime(now[k][:-4], "%Y-%m-%d %H:%M:%S")
        hours.add((a - b).total_seconds() / 3600)
    assert len(hours) == 1 and next(iter(hours)) == int(next(iter(hours))), hours      # the same three instants, one zone apart
    assert {k: v for k, v in was.items() if not isinstance(v, str)} == {k: v for k, v in now.items() if not isinstance(v, str)}
    assert "f6e89032a is on a branch or a tag of this repository" in mended["SM-16"]["main finds"]
    # 3. the first probe of the package's rows runs to its end
    out = (M / "builder_rows_probe_out.txt").read_text(encoding="utf-8")
    assert "Traceback" not in out and "rows probed: ['41', '42', '43', '44', '45'] | cases: 33 | reproduced: 29" in out
    assert len(json.loads((M / "builder_rows_probe.json").read_text(encoding="utf-8"))) == 33
    # 4. the second probe, written again: a case for each of main's fourteen kept lines, and each case gave main's answer
    lines = json.loads((HERE / "checks" / "builder_rows_probe2.json").read_text(encoding="utf-8"))
    again = json.loads((M / "builder_rows_probe2.json").read_text(encoding="utf-8"))
    assert [(o["row"], o["case"], o["answer"]) for o in again] == [(k["row"], k["case"], k["answer"]) for k in lines] and len(lines) == 14
    assert all(o["the same as main kept"] and o["main kept"] == o["answer"] for o in again) and all(k["reproduced"] for k in lines)
    assert not (HERE / "checks" / "builder_rows_probe2.py").exists()                    # main's own script is still not in its folder
    # 5. (the next patch of the same part) main's plants for agy-002's rows, each plant in fact made: two answers differ from
    #    the file main kept, and they are the two plants that had changed nothing
    was = json.loads((HERE / "checks" / "plants_agy002.json").read_text(encoding="utf-8"))
    now = json.loads((M / "plants_agy002.json").read_text(encoding="utf-8"))
    assert [(r["arc"], r["plant"]) for r in was] == [(r["arc"], r["plant"]) for r in now] and len(now) == 21
    differ = [(a["arc"], a["plant"], a["the lock"], b["the lock"]) for a, b in zip(was, now) if a["the lock"] != b["the lock"]]
    assert differ == [("B1893", "'still passes' turned into 'IS REFUSED' on the page", "PLANT NOT MADE", "passes"),
                      ("B1885", "the note on the grid's 18 digits taken out of the verdict line", "passes", "FAILS")], differ
    assert not any(r["the lock"] == "PLANT NOT MADE" for r in now)
    assert [r["the lock"] for r in now if r["plant"] == "nothing planted"] == ["passes"] * 5
    # 6. main's five plants against B1881's lock, each made through the guard: the controls behave and none of the five passes
    third = json.loads((M / "plants_b1881_third.json").read_text(encoding="utf-8"))
    assert [r["the lock"] for r in third] == ["PASSES"] + ["CATCHES IT"] * 6 and len(third) == 7
    # 7. the check that named a branch names the commit that the arc's verdict file gives for that reader
    check = (M / "quote_check_agy002.py").read_text(encoding="utf-8")
    assert 'SRC = ("4ae026d99", "relays/REVIEW_80_AGY-002.md")' in check and "@ 4ae026d99" in " ".join(V["cites_seat"])
    assert sum(1 for l in check.split("\n") if "origin/" in l and not l.startswith("#")) == 0
    page = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "verification/mended_in_r80b/" in page


def test_the_counts_are_the_tables():
    again = _recount().the_tables()
    assert again == T, "the recount kept in this arc is not what the two tables give now"
    assert T["findings in all"] == 100 == T["the first table: findings"] + T["the second table: findings"]
    assert T["the first table: findings, by reader"] == {"the web seat": 7, "agy-002": 36}
    assert T["the second table: findings, by reader"] == {"the SM seat": 41, "agy-exp": 14, "the web seat's addition": 2}
    unchecked, part = T["the second table: main's check is 'not checked'"], T["the second table: 'not checked' for a part of the row"]
    assert (len(unchecked), len(part), T["the second table: checked by main in full"]) == (17, 3, 37)
    assert T["checked by main in full, both tables"] == 80 and 80 + 3 + 17 == 100
    waits, mended, noted = (T["the second table: the state says 'to build'"], T["the second table: 'mended', and nothing to build"],
                            T["the second table: 'noted', and nothing to build"])
    assert (len(waits), len(mended), len(noted)) == (41, 9, 7) and T["the second table: none of the three"] == []
    assert not set(waits) & set(mended) and not set(waits) & set(noted)
    # a finding that only its reader looked at is not among those written as mended or noted
    assert not set(unchecked) & (set(mended) | set(noted)), "a row given as not checked is given as mended"
    assert T["the first table: findings sent to the builder, whole rows"] == 16


def test_the_page_the_verdict_line_and_the_entry_say_the_recounts_numbers():
    said = ("100 findings", "80 of them main checked in full", "3 in part", "17 nobody but their reader has looked at",
            "41 of the 57 wait to be built", "26 commits")
    for s in said:
        assert s in F, "the page does not say: " + s
    line = " ".join(V["claim_one_line"].split())
    for s in ("100 FINDINGS", "80", "17", "41"):
        assert s in line, "the verdict line does not say: " + s
    assert V["id"] == "B1898" and V["verdict"] == "PROVED" and V["creates_law"] is False and V["instrument"] is False
    reviews = (ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8")
    start = reviews.index("\n# Review 80 ")
    entry = " ".join(reviews[start:].split())
    for s in ("100 findings", "80", "17", "41", "26 commits", "anchor-commit: `%s`" % READ):
        assert s in entry, "Review 80's entry does not say: " + s
    assert G["commits in the window"] == 26 == G["of them on main's own line"]
    assert G["arcs added in the window"] == ["B189%d" % n for n in range(1, 8)]
    assert G["the law map: lines of its tables less the rules, at the two ends"] == [329, 329]
    assert G["the theorem registry: lines of its tables less the rules, at the two ends"] == [229, 229]


# ADDED 2026-11-12 at the landing, by main.  A cold reading of this series on another family of model planted four
# rewrites and all four passed the test above: it asked for "80", "17" and "41" as digits, and "80" is in "REVIEW 80".
# The verdict line, the entry and the register's row are held here by their SENTENCES, the marks on Review 79's items and
# the items of this review by count, and the seventeen rows nobody but their reader looked at by name.
LINE_SAYS = ["REVIEW 80: 100 FINDINGS ON MAIN'S WORK SINCE REVIEW 79, in four readers' files and one dated addition, every quotation but the addition's two found by machine at the commit read (7 of 7, 36 of 36, 50 of 50, 14 of 14).", 'MAIN CHECKED 80 OF THEM IN FULL AND EVERY ONE HELD; it checked 3 more in part; 17 have been looked at by nobody but their reader.', 'The first 43 are mended on main or with the builder of the enforcement package (16 whole rows). Of the other 57, 16 are mended or noted on main and 41 WAIT TO BE BUILT.', 'The window is 26 commits and 7 added arcs; the law map and the theorem registry have the rows they had. No reader was tested against planted faults. 0 of 19.']
ENTRY_SAYS = ["**100 findings** on main's work since Review 79, in four readers' files and one dated addition.", '**Main checked 80 of them in full, and all 80 held.** It checked 3 more in part. **17 have been looked at by nobody but their reader.**', "16 of the 43 are in the enforcement package's files and went whole to its builder. Of the other 57, 16 are mended or noted on main.", '**41 of the 57 wait to be built,** with five things owed from the first 43.', "Review 79's eighteen items: none resolved, eighteen carried", "And 17 findings stand on their reader's word alone: eleven of the SM seat's, four of agy-exp's, and the web seat's two of its addition."]
REGISTER_SAYS = ['100 findings; main checked 80 in full and all 80 held, and 3 in part; 17 have been looked at by nobody but their reader.']


def test_the_numbers_are_held_as_sentences_and_not_as_digits():
    line = " ".join(V["claim_one_line"].split())
    for s in LINE_SAYS:
        assert s in line, "the verdict line does not say: " + s
    reviews = (ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8")
    entry = " ".join(reviews[reviews.index("\n# Review 80 "):].split())
    for s in ENTRY_SAYS:
        assert s in entry, "Review 80's entry does not say: " + s
    items = re.findall(r"^- \[.\] R80-(\d+):", reviews, re.M)
    assert items == [str(n) for n in range(1, 23)], "Review 80's action items are not R80-1 to R80-22, once each and in order"
    before = reviews[:reviews.index("\n# Review 80 ")]
    carried = re.findall(r"^- \[>\] R79-(\d+):", before, re.M)
    assert sorted(carried, key=int) == [str(n) for n in range(1, 19)], "Review 79's eighteen items are not all marked as carried"
    row = [l for l in (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8").split("\n") if l.startswith("| P-834 |")]
    assert len(row) == 1 and all(s in row[0] for s in REGISTER_SAYS), "register row P-834 does not say what the entry says"
    # the page's own counts, against the recount and not against digits found anywhere
    page = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    sec = lambda n: " ".join(page[page.index("\n## %d. " % n):page.index("\n## %d. " % (n + 1))].split())
    assert T["findings in all"] == 100 == T["checked by main in full, both tables"] + 20
    assert "**80 of them main checked in full, and every one held.** Main checked 3 in part. **17 nobody but their reader has looked at.**" in sec(1)
    alone = T["the second table: main's check is 'not checked'"]
    assert len(alone) == 17 and T["the second table: 'not checked' for a part of the row"] == ["F6", "F7", "F10"]
    named = "17 (the SM seat's 22, 25, 26, 30, 32, 33 and 37 to 41; agy-exp's F9, F11, F13 and F14; the web seat's W8 and W9)"
    assert alone == ["22", "25", "26", "30", "32", "33", "37", "38", "39", "40", "41", "F9", "F11", "F13", "F14", "W8", "W9"], "the recount's seventeen are not the ones the page names"
    assert named in sec(5), "section 5 does not name the seventeen rows that only their reader looked at"
    assert "26 commits" in sec(3) and G["commits in the window"] == 26


def test_the_outputs_main_kept_say_what_the_tables_say():
    again = _recount().the_kept_outputs()
    assert again == K
    assert K["agy-002: quotations found, of"] == [36, 36] and K["the SM seat: quotations placed, of, in findings"] == [50, 50, 41]
    assert K["agy-exp: quotations found, of"] == [14, 14] and K["controls found, in the three"] == [0, 0, 0]
    status = (ARC / "STATUS_OF_THE_57.md").read_text(encoding="utf-8")
    assert "7 of 7, 36 of 36, 50 of 50" in status and "14 of 14" in status
    strict = K["Review 79's quotations checked again strictly"]
    assert (strict["quotations"], strict["in the file the finding names"], strict["in the arc's own folder (no file named)"],
            strict["in a wide page only"], strict["found nowhere, strictly"]) == (111, 52, 45, 14, 0)
    answers = (ARC / "ANSWERS_the_first_43.md").read_text(encoding="utf-8")
    assert "The 111 quotations checked again: 52 in the file named, 45 in the arc's folder where no file is named, 14 on a wide page, none nowhere" in answers
    b = K["main's computation on B1895"]
    assert b["sequences"] == 1332 == b["on which the second word, built, is the first conjugated by the swap"] and "1,332 of 1,332" in status
    plants = dict(K["main's plants against B1881's lock: the plant and the lock's answer"])
    five = [k for k in plants if re.match(r"F[1-5]:", k)]
    assert len(five) == 5 and all(plants[k] == "PASSES" for k in five) and plants["nothing planted"] == "PASSES"
    assert [v for k, v in plants.items() if k.startswith("the control")] == ["CATCHES IT"]
    # one plant of main's own still passes the lock it was written against, and the page says so: it is not written as held
    assert K["main's plants for agy-002's rows that the lock passes, a plant being made"] == [["B1885", "the note on the grid's 18 digits taken out of the verdict line"]]
    assert "One plant of main's own passes" in F
    # CORRECTED 2026-11-12 at the landing, by main: that plant changed nothing.  The page, the verdict line and the entry
    # say so, and main's own run of the plant made properly is held: 178 characters taken out, and the lock fails
    made = json.loads((HERE / "main_at_the_landing" / "the_plant_on_b1885_made_properly.json").read_text(encoding="utf-8"))
    assert [(m["plant"], m["characters taken out"], m["the lock"]) for m in made] == [
        ("nothing planted", 0, "passes"), ("main's pattern as it was written", 0, "passes"), ("the note in fact taken out", 178, "FAILS")]
    assert "THAT PLANT CHANGED NOTHING" in F and "THAT PLANT CHANGED NOTHING" in " ".join(V["claim_one_line"].split())
    assert "| the note in fact taken out | 178 | **fails**, 1 of 8 |" in (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    reviews = " ".join((ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8").split())
    assert reviews.count("THAT PLANT CHANGED NOTHING") == 1 and "[ANSWERED 2026-11-12 at the landing: the plant changed nothing" in reviews


def test_the_planted_suites_output_says_what_the_page_and_the_entry_say():
    suite = (HERE / "planted_suite_on_main_c40446392_out.txt").read_text(encoding="utf-8")
    assert suite.startswith("planted-violation suite at %s" % READ)
    controls = re.findall(r"^CTL\d+\s+\S+\s+(NOT CAUGHT|CAUGHT)", suite, re.M)
    cases = re.findall(r"^(PV\d+)\s+(?!twin)\S+\s+(NOT CAUGHT|CAUGHT)", suite, re.M)                # a twin is the honest form of a case, not a case
    twins = dict(re.findall(r"^(PV\d+)\s+twin\s+(\S+)", suite, re.M))
    assert controls == ["CAUGHT"] * 5 and len(cases) == len({c for c, _ in cases}) == 38
    unread = sorted(c for c, answer in twins.items() if answer != "PASSES")
    assert unread == ["PV38"] and len(twins) == 12, "a case whose twin does not pass is not to be read"
    read = [(c, answer) for c, answer in cases if c not in unread]
    caught = sum(1 for _c, answer in read if answer == "CAUGHT")
    assert (caught, len(read)) == (24, 37)
    assert "24 of 37" in F and "Of 38 planted cases 25 are caught and 13 are not" in F
    reviews = (ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8")
    entry = " ".join(reviews[reviews.index("\n# Review 80 "):].split())
    assert "Main's gates catch 24 of 37 planted faults" in entry and "24 of 37, by the enforcement package's suite" in entry


# ADDED 2026-11-12 at the landing, by main.  One of main's checks names a session's BRANCH where it should name the commit
# main read, and the branch has moved since: its file has 49 rows now and had 36.  The lock as it was sent ran the script
# as written and so compared 49 with the 36 main kept; it passed where the branch had not moved and failed on main.  The
# script is held as main wrote it (by hash); it is RUN with the one name replaced by the commit, and the lock says so.
READ_AT = {"quote_check_agy002": ('"origin/agy-002/verify"', '"4ae026d99"')}


def _run_a_check(name, tmp_path):
    """one of main's checks, run as main wrote it but for the name in READ_AT: from a folder that is not the repository,
    with git told where the repository is, so that what the script writes beside itself or under audit/ lands in the
    temporary folder"""
    work = tmp_path / name
    (work / "audit" / "review80").mkdir(parents=True)
    script = HERE / "checks" / (name + ".py")
    if name in READ_AT:
        branch, commit = READ_AT[name]
        text = script.read_text(encoding="utf-8")
        assert text.count(branch) == 1, name + ": the branch's name is not in the script exactly once"
        script = work / (name + ".py")
        script.write_text(text.replace(branch, commit), encoding="utf-8")
    env = {k: v for k, v in __import__("os").environ.items() if not k.startswith("GIT_")}
    git_dir = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--absolute-git-dir"], capture_output=True, text=True).stdout.strip()
    env["GIT_DIR"] = git_dir
    r = subprocess.run([sys.executable, "-B", str(script)], cwd=str(work), capture_output=True, text=True, env=env, timeout=600)
    return r, work


def test_three_of_the_four_checks_of_quotations_run_again_give_what_main_kept(tmp_path):
    if not _have(READ):
        pytest.skip("the commit the readers read, %s, is not in this clone: the quotations were not looked for again here" % READ)
    r, _ = _run_a_check("quote_check_chat1", tmp_path)
    assert r.returncode == 0, r.stderr[-600:]
    web = json.loads(r.stdout)
    assert (web["found"], web["of"], web["the control, one word changed, is found"]) == (7, 7, False)
    ran = ["the web seat"]
    for name, source in (("quote_check_agy002", "4ae026d99"), ("quote_check_agyexp", "42ac86532")):
        if not _have(source):
            continue                                                  # that session's commit is not in this clone
        r, work = _run_a_check(name, tmp_path)
        assert r.returncode == 0, (name, r.stderr[-600:])
        made = json.loads((work / "audit" / "review80" / (name + ".json")).read_text(encoding="utf-8"))
        kept = json.loads((HERE / "checks" / (name + ".json")).read_text(encoding="utf-8"))
        assert made["summary"] == kept["summary"], name + ": made again, the counts are not the ones main kept"
        ran.append(name)
    if len(ran) < 3:
        pytest.skip("run again here: %s; the other sessions' commits are not in this clone, and their checks are held by hash only" % ", ".join(ran))


def test_two_rows_of_the_register_point_at_what_was_found_since():
    """ADDED 2026-11-12 (R80b, part 6; a reader's check of main's answers at this review, its row A18 and its note on A2).  Row
    P-805 said that every arc of the window was read in full, with no pointer to the row that says otherwise; and the
    retractions index sent the reading of five reviews' corrections to row P-823, which named two."""
    register = (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    row = lambda p: next(l for l in register.split("\n") if l.startswith("| %s |" % p))
    r805, r823, r830 = row("P-805"), row("P-823"), row("P-830")
    assert "every arc of the window read in full, all but one by two sessions" in r805                  # what the row said is kept
    assert "Ten older arcs that changed in the window were on no reader's card" in r805 and "they are named in P-830" in r805
    assert "Ten of the 25 were on no card" in r830
    assert "Five landed in the window, 75 to 79" in r823 and "the corrections of Reviews 75, 76 and 77 are owed their rows under this row" in r823
    index = " ".join((ROOT / "docs" / "RETRACTIONS.md").read_text(encoding="utf-8").split())
    assert "Five reviews landed in this window, 75 to 79, and not two" in index
    assert "the corrections of Reviews 75, 76 and 77 are owed their rows (P-823)" in index
    for r in (r805, r823):
        assert r.rstrip().endswith("| 2026-11-12 |") and r.count(" | ") == r805.count(" | ")           # each is still one row of the register's shape


def test_mains_probe_of_b1895_is_mended_beside_the_file_main_wrote_and_gives_what_main_kept():
    """ADDED 2026-11-13 (C16; main's word in M22, on a cold reader's finding that main checked).  Main's two check files
    `plants_b1881_third.py` and `b1895_probes.py` set their root to the folder above their own, which is not the repository's
    root, and run in place they stop at their first search.  The first was mended beside main's file in R80b's part 6 (the
    test above holds it).  The second is mended here, the same way: main's file stands in checks/ as main wrote it; the mended
    copy stands in mended_in_r80b/, differs from it in one marked block, and run in place gives the json main kept."""
    M = HERE / "mended_in_r80b"
    sha = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()
    text = (M / "b1895_probes.py").read_text(encoding="utf-8")
    assert text.count("\n# MENDED (") == text.count("\n# END OF THE MEND") == 1 and text.count("# NOTE OF THE MEND") == 1
    assert sha(_with_its_mends_put_back(text)) == HELD["verification/checks/b1895_probes.py"]
    assert sha(_with_its_mends_put_back("#| x".join(text.rsplit("#| ", 1)))) != HELD["verification/checks/b1895_probes.py"]
    # both mended copies count the root from the repository and not from their own folder
    for name in ("b1895_probes.py", "plants_b1881_third.py"):
        t = (M / name).read_text(encoding="utf-8")
        assert "ROOT = next(p for p in HERE.parents if (p / \"scripts\" / \"gates\" / \"gates.py\").is_file())" in t, name
        assert "#| HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]" in t, name
    # run in place, the mended probe gives what main kept, and its run is kept beside it
    assert json.loads((M / "b1895_probes.json").read_text(encoding="utf-8")) == json.loads((HERE / "checks" / "b1895_probes.json").read_text(encoding="utf-8"))
    assert "(4) 3378 primitive cyclic sequences" in (M / "b1895_probes_out.txt").read_text(encoding="utf-8")

