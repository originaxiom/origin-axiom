#!/usr/bin/env python3
"""Independent cold-read verification of rebuilt builder series R80b Parts 4 and 5
(relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_4/ and part_5/, at the builder's ef5f59c8f).

Applies Part 1 + rebuilt Parts 2, 3 onto main's bf76e5ab1, then Part 4 (six patches), then Part 5 (patches 1 and 2 by git am,
patch 3 by its script and message).  Checks scope and attribution, runs the changed tests, main's own sweep of asserts that end
in a constant (or_true_sweep, from a staged copy), the foundation's P-796 hygiene for patch 3 (no removed passage of GENESIS.md
in any file the patch adds, compared by six-word slices held in memory and never printed), the locks of B1886, B1891, B1904,
and all gates, and puts unseen plants to the mended listener and atlas query.
COI (said in the card): Part 5 patch 2, B1862's tripwire, answers agy-002's own rows 10 and 11, and is left aside on substance:
only that it applies and that its lock passes is recorded.
"""
import ast
import importlib.util
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]
BASE, P1, SENT = "bf76e5ab1", "112e73d67", "bc71f9373"
HEAD = subprocess.check_output(["git", "-C", str(REPO), "rev-parse", "--short=9", "origin/cld/cool-hamilton-k9eqvo"], text=True).strip()
D = "relays/advisor_2026-11-10_audit/r80b"
R = D + "/on_mains_bf76e5ab1"
ENV = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", PYTHONDONTWRITEBYTECODE="1")
UNCHECKED_P4 = {2: "SM-37", 3: "SM-38", 5: "SM-39", 6: "SM-40"}


def blob(spec):
    return subprocess.check_output(["git", "-C", str(REPO), "show", spec])


def ls(rev, path):
    return sorted(p.split("/")[-1] for p in subprocess.check_output(["git", "-C", str(REPO), "ls-tree", "--name-only", rev, path + "/"], text=True).split())


def git(wt, *a, check=True):
    return subprocess.run(["git", "-C", str(wt), *a], capture_output=True, text=True, env=ENV, check=check)


def pytest(wt, *paths):
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *map(str, paths)], cwd=str(wt), capture_output=True, text=True, env=ENV)
    return r.returncode, (r.stdout.strip().splitlines() or [""])[-1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def staged_run(wt, src, *args):
    """main's kept check scripts read the repository from the working directory; run a byte-identical copy outside the tree"""
    d = pathlib.Path(tempfile.mkdtemp(prefix="agy002_chk_"))
    try:
        (d / src.name).write_bytes(src.read_bytes())
        return subprocess.run([sys.executable, "-B", str(d / src.name), *args], cwd=str(wt), capture_output=True, text=True, env=ENV)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def gates(wt):
    r = subprocess.run([sys.executable, "-B", str(wt / "scripts/gates/gates.py")], cwd=str(wt), capture_output=True, text=True, env=ENV)
    return r.returncode, [l.strip() for l in r.stdout.splitlines() if l.lstrip().startswith("FAIL")]


def main():
    print("=== A2-S-R80b-p4p5 cold read: rebuilt Parts 4 and 5 at the builder's %s, on bf76e5ab1 + Parts 1 to 3 ===" % HEAD)
    p2 = [n for n in ls(SENT, R + "/part_2") if n.endswith(".patch")]
    p3 = [n for n in ls(SENT, R + "/part_3") if n.endswith(".patch")]
    p4 = [n for n in ls(HEAD, R + "/part_4") if n.endswith(".patch")]
    p5 = ls(HEAD, R + "/part_5")
    assert len(p4) == 6 and len(p2) == 12 and len(p3) == 18
    for n in p4 + [x for x in p5 if x.endswith(".patch") and x.startswith(("0001", "0002"))]:
        folder = "part_4" if n in p4 else "part_5"
        assert blob("%s:%s/%s/%s" % (SENT, R, folder, n)) == blob("%s:%s/%s/%s" % (HEAD, R, folder, n)), n
    print("[SENT] Part 4 and Part 5's first two patches are byte for byte the same at bc71f9373 and at %s; Part 5 patch 3 is only at %s" % (HEAD, HEAD))

    # attribution
    for i, n in enumerate(p4, 1):
        subj = " ".join(blob("%s:%s/part_4/%s" % (HEAD, R, n)).decode("utf-8").split("\n\n", 1)[0].split())
        if i in UNCHECKED_P4:
            assert "NOT CHECKED" in subj, (i, n)
        else:
            assert "checked by main" in subj, (i, n)
    msg3 = blob("%s:%s/part_5/0003_message.txt" % (HEAD, R)).decode("utf-8")
    print("[ATTR] Part 4: the four rows main has not checked (SM-37 to SM-40) are said to be not checked; SM-36 and F12 are said to be checked by main")
    print("[ATTR] Part 5 patch 3 message says W7 was 'checked by main': %s" % ("checked by main" in " ".join(msg3.split())))

    tmp = pathlib.Path(tempfile.mkdtemp(prefix="agy002_r80b_p45_"))
    wt = tmp / "wt"
    pd = tmp / "p"; pd.mkdir()
    try:
        for n in ("0001_message.txt", "0001_the_plans_page_gives_the_owners_answer_in_plain_words.py",
                  "0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch",
                  "0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch"):
            (pd / ("p1_" + n)).write_bytes(blob("%s:%s/part_1/%s" % (P1, D, n)))
        for part, names, rev in (("part_2", p2, SENT), ("part_3", p3, SENT), ("part_4", p4, HEAD), ("part_5", p5, HEAD)):
            for n in names:
                (pd / (part + "_" + n)).write_bytes(blob("%s:%s/%s/%s" % (rev, R, part, n)))
        p53 = tmp / "part_5_as_sent"; p53.mkdir()                       # the script of patch 3 finds its diff beside itself, by name
        for n in p5:
            if n.startswith("0003_"):
                (p53 / n).write_bytes(blob("%s:%s/part_5/%s" % (HEAD, R, n)))
        git(REPO, "worktree", "add", "--detach", str(wt), BASE)
        subprocess.run([sys.executable, "-B", str(pd / "p1_0001_the_plans_page_gives_the_owners_answer_in_plain_words.py"), str(wt)], check=True, capture_output=True, env=ENV)
        git(wt, "commit", "-qF", str(pd / "p1_0001_message.txt"))
        git(wt, "am", "-q", str(pd / "p1_0002_the_lock_asks_that_the_plans_page_quote_nothing_of_the_owner.patch"), str(pd / "p1_0003_a_text_that_opens_with_punctuation_is_not_cut_to_the_mark_alone.patch"))
        git(wt, "am", "-q", *[str(pd / ("part_2_" + n)) for n in p2])
        git(wt, "am", "-q", *[str(pd / ("part_3_" + n)) for n in p3])

        sweep = wt / "docs/handoffs/MAIN_TO_BUILDER_2026-11-12/review80/checks/or_true_sweep.py"
        before_sweep = staged_run(wt, sweep).stdout.strip().splitlines()
        before4 = git(wt, "rev-parse", "HEAD").stdout.strip()

        # ---------------- PART 4 ----------------
        print("\n=================== PART 4 ===================")
        git(wt, "am", "-q", *[str(pd / ("part_4_" + n)) for n in p4])
        ch4 = git(wt, "diff", "--name-only", before4, "HEAD").stdout.split()
        print("[SCOPE] Part 4 changes: %s" % ", ".join(ch4))
        rc, last = pytest(wt, wt / "tests/test_seat_listener.py", wt / "tests/test_atlas.py")
        print("[TESTS] tests/test_seat_listener.py and tests/test_atlas.py on Part 4's last patch: rc=%d, %s" % (rc, last))
        # each new test against the code of the commit before Part 4
        for f, test in (("scripts/seats/listen.py", "tests/test_seat_listener.py"), ("scripts/atlas/query.py", "tests/test_atlas.py")):
            now = (wt / f).read_bytes()
            (wt / f).write_bytes(git(wt, "show", "%s:%s" % (before4, f)).stdout.encode("utf-8"))
            rcb, lastb = pytest(wt, wt / test)
            (wt / f).write_bytes(now)
            print("[BEFORE/AFTER] %s with %s of the commit before Part 4: rc=%d, %s" % (test, f, rcb, lastb))
        rcg, fails = gates(wt)
        print("[GATES] on Part 4's last patch: rc=%d; failing: %s" % (rcg, fails or "none"))

        print("--- unseen plants against Part 4 ---")
        L = load("agy002_listen", wt / "scripts/seats/listen.py")
        page = ("## Messages from main (newest first)\n\n### M2 — a day — two\n\ntext two\n\n   ### What stands between, indented three spaces\n\nnot a message\n\n"
                "### M1 — a day — one\n\ntext one\n")
        ms = L.messages(page)
        print("  P4-A (a heading of three marks indented by three spaces, which Markdown renders as a heading, between two messages): "
              "taken into M2: %s" % ("not a message" in ms[2]))
        dup = "## Messages\n\n### M2 — a day — first text of two\n\nA\n\n### M2 — a day — a second message under the same number\n\nB\n\n### M1 — x — one\n\nC\n"
        md = L.messages(dup)
        print("  P4-B (two messages under one number; not a row of Part 4, seen on the way): both kept: %s; M2 holds %r" % ("A" in md[2] and "B" in md[2], md[2].split("\n")[0]))
        Q = load("agy002_query", wt / "scripts/atlas/query.py")
        planted = wt / "frontier" / "B58_planted_by_agy002"
        planted.mkdir()
        (planted / "arc_verdict.json").write_text(json.dumps({"verdict": "PROVED", "claim_one_line": "planted. 0 of 19."}), encoding="utf-8")
        card = Q.arc_card("B58")
        rc4, last4 = pytest(wt, wt / "tests/test_atlas.py")
        shutil.rmtree(planted)
        print("  P4-C (a fourth folder for B58 planted): the card shows it: %s; tests/test_atlas.py rc=%d (%s)" % ("B58_planted_by_agy002" in card["text"], rc4, last4))
        bare = wt / "frontier" / "B57"
        bare.mkdir()
        (bare / "arc_verdict.json").write_text(json.dumps({"verdict": "RETRACTED", "claim_one_line": "planted. 0 of 19."}), encoding="utf-8")
        card57 = Q.arc_card("B57")
        shutil.rmtree(bare)
        print("  P4-D (a folder named B57 with no slug, carrying a RETRACTED verdict file): the card shows it: %s" % ("RETRACTED" in card57["text"]))

        # ---------------- PART 5 ----------------
        print("\n=================== PART 5 ===================")
        before5 = git(wt, "rev-parse", "HEAD").stdout.strip()
        git(wt, "am", "-q", str(pd / "part_5_0001_four_of_mains_five_asserts_that_ended_in_a_constant.patch"))
        ch51 = git(wt, "diff", "--name-only", before5, "HEAD").stdout.split()
        after_sweep = staged_run(wt, sweep).stdout.strip().splitlines()
        print("[P5-1 SCOPE] %s" % ", ".join(ch51))
        print("[P5-1 SWEEP] main's or_true_sweep before: %s" % before_sweep[-1])
        print("              after:  %s" % after_sweep[-1])
        print("              still reported after patch 1: " + "; ".join(l.split("  ")[0] for l in after_sweep[:-1]))
        src1832 = (wt / "frontier/B1832_the_agy_lanes_digested/verification/apply/apply_b1832.py").read_text(encoding="utf-8")
        tree = ast.parse(src1832)
        rows_node = next(n for n in ast.walk(tree) if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "rows" for t in n.targets))
        rows = [eval(compile(ast.Expression(e), "rows", "eval"), {"LOCK": "the lock"}) for e in rows_node.value.elts]
        print("[P5-1 B1832] the mended assert, evaluated by agy-002 on the %d rows the script names: %s" % (len(rows), all("|" not in r.strip("| ").replace(" | ", "") for r in rows)))
        for rel in ("frontier/B1103_being_gate/b1103_exact_engine.py", "frontier/B1306_the_older_debt/verification/sliceC/c_su3_level2.py"):
            try:
                r = subprocess.run([sys.executable, "-B", str(wt / rel)], cwd=str(wt), capture_output=True, text=True, env=ENV, timeout=900)
                print("[P5-1 RUN] %s: rc=%d; last line of output %r; last line of errors %r" % (rel, r.returncode, (r.stdout.strip().splitlines() or [""])[-1][:140], (r.stderr.strip().splitlines() or [""])[-1][:200]))
            except subprocess.TimeoutExpired:
                print("[P5-1 RUN] %s: did not finish within 900 seconds" % rel)
        git(wt, "checkout", "--", ".")
        git(wt, "clean", "-fdq", "frontier/B1103_being_gate", "frontier/B1306_the_older_debt")

        before52 = git(wt, "rev-parse", "HEAD").stdout.strip()
        git(wt, "am", "-q", str(pd / "part_5_0002_b1862s_tripwire_is_widened_in_five_ways.patch"))
        ch52 = git(wt, "diff", "--name-only", before52, "HEAD").stdout.split()
        lock1862 = next(wt.glob("frontier/B1862_*/verification/test_*.py"))
        rc, last = pytest(wt, lock1862)
        print("[P5-2, COI: left aside on substance] applies; changes %s; B1862's lock rc=%d, %s" % (", ".join(ch52), rc, last))

        dirty = git(wt, "status", "--porcelain").stdout.strip()
        print("[P5-3] untracked or changed files left by the runs above, removed before the script: %s" % (dirty.replace("\n", "; ") or "none"))
        git(wt, "checkout", "--", "."); git(wt, "clean", "-fdq")
        old_genesis = (wt / "GENESIS.md").read_text(encoding="utf-8")
        r = subprocess.run([sys.executable, "-B", str(p53 / "0003_the_foundation_at_version_1_67.py"), str(wt)], capture_output=True, text=True, env=ENV)
        print("[P5-3] the script: rc=%d; %s %s" % (r.returncode, " | ".join(r.stdout.strip().splitlines()[-2:]), r.stderr.strip()[-300:]))
        git(wt, "commit", "-qF", str(pd / "part_5_0003_message.txt"))
        new_genesis = (wt / "GENESIS.md").read_text(encoding="utf-8")
        gone = [l for l in old_genesis.split("\n") if l.strip() and l not in new_genesis.split("\n")]
        words = lambda s: " ".join(s.lower().split()).split()
        slices = {" ".join(w[i:i + 6]) for l in gone for w in [words(l)] for i in range(max(0, len(w) - 5))}
        common = {" ".join(w[i:i + 6]) for l in new_genesis.split("\n") for w in [words(l)] for i in range(max(0, len(w) - 5))}
        slices -= common                                                # words that still stand in the new page are not the passages
        ch53 = git(wt, "diff", "--name-only", "HEAD~1", "HEAD").stdout.split()
        added_files = [pd / "part_5_0003_all_of_the_patch_but_the_foundations_own_page.patch", pd / "part_5_0003_the_foundation_at_version_1_67.py",
                       pd / "part_5_0003_message.txt", pd / "part_5_0003_what_was_run_out.txt"] + [wt / f for f in ch53 if f != "GENESIS.md" and (wt / f).is_file()]
        leaks = [str(f.name) for f in added_files if any(s in " ".join(f.read_text(encoding="utf-8", errors="ignore").lower().split()) for s in slices)]
        print("[P5-3 P-796] %d lines of GENESIS.md removed; %d six-word slices of them that stand nowhere in the new page (held in memory, not printed)" % (len(gone), len(slices)))
        print("[P5-3 P-796] files of the patch (its diff, script, message, run record, and every file it adds or changes but GENESIS.md) holding any such slice: %s" % (leaks or "none"))
        print("[P5-3 SCOPE] %s" % ", ".join(ch53))
        hunks = [h for h in git(wt, "diff", "-U0", "HEAD~1", "HEAD", "--", "GENESIS.md").stdout.split("\n") if h.startswith("@@")]
        print("[P5-3 GENESIS] hunks in GENESIS.md: %d" % len(hunks))
        locks = [next(wt.glob("frontier/%s_*/verification/test_*.py" % a)) for a in ("B1886", "B1891", "B1904", "B1898")]
        for _ in (1, 2):
            rc, last = pytest(wt, *locks)
            print("[P5-3 LOCKS] B1886, B1891, B1904, B1898 in one run: rc=%d, %s" % (rc, last))
        rcg, fails = gates(wt)
        print("[GATES] on Part 5's last patch: rc=%d; failing: %s" % (rcg, fails or "none"))
        print("[TREE] after Part 5 patch 3: %s (builder's: 4ec0c47a3b3bb0d5c3dd2c267e79d73df55ac302)" % git(wt, "write-tree").stdout.strip())
    finally:
        git(REPO, "worktree", "remove", "--force", str(wt), check=False)
        shutil.rmtree(tmp, ignore_errors=True)
    print("\n=== A2-S-R80b-p4p5 VERIFICATION COMPLETE (EXIT 0) ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
