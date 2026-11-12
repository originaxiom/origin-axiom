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


def test_mains_files_are_as_main_wrote_them():
    """the two tables and every check, by hash.  The hashes are of main's own files in its folder of 2026-11-12."""
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


def _run_a_check(name, tmp_path):
    """one of main's checks, run as main wrote it: from a folder that is not the repository, with git told where the
    repository is, so that what the script writes beside itself or under audit/ lands in the temporary folder"""
    work = tmp_path / name
    (work / "audit" / "review80").mkdir(parents=True)
    env = {k: v for k, v in __import__("os").environ.items() if not k.startswith("GIT_")}
    git_dir = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--absolute-git-dir"], capture_output=True, text=True).stdout.strip()
    env["GIT_DIR"] = git_dir
    r = subprocess.run([sys.executable, "-B", str(HERE / "checks" / (name + ".py"))], cwd=str(work), capture_output=True, text=True, env=env, timeout=600)
    return r, work


def test_three_of_the_four_checks_of_quotations_run_again_give_what_main_kept(tmp_path):
    if not _have(READ):
        pytest.skip("the commit the readers read, %s, is not in this clone: the quotations were not looked for again here" % READ)
    r, _ = _run_a_check("quote_check_chat1", tmp_path)
    assert r.returncode == 0, r.stderr[-600:]
    web = json.loads(r.stdout)
    assert (web["found"], web["of"], web["the control, one word changed, is found"]) == (7, 7, False)
    ran = ["the web seat"]
    for name, source in (("quote_check_agy002", "origin/agy-002/verify"), ("quote_check_agyexp", "42ac86532")):
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
