#!/usr/bin/env python3
"""Review 79's eleven findings in the enforcement package's files (main's P-812): which the unlanded series close.

    python3 which_of_the_eleven_the_series_close.py <a checkout at main's head> <a checkout with series 3 and 4 applied>

Three things are done, on both trees.
  1. THE QUOTED LINE.  Each finding quotes a line of a gate or a checker.  Does that line still stand?
  2. THE PLANTS for the findings the series are said to close: the two variables that moved a debt gate, and a
     repository that holds no commit.
  3. THE PLANTS for the arrival gate and for the runner's line, which the series do not touch: shown still open.
Every plant is made in a folder of its own, outside both checkouts.  Nothing is written into either."""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile

MAIN, SERIES = (os.path.abspath(p) for p in sys.argv[1:3])
TREES = (("main's head", MAIN), ("the series", SERIES))

# the finding -> (the file, the line it quotes).  R79-SM-nn are the first reader's; row nn is a row of the second reader's table.
QUOTED = (
    ("R79-SM-44; row 25", "scripts/gates/gates.py", 'if _ARRIVAL_NEG_RE.search(" " + own[-160:] + " "): continue'),
    ("R79-SM-45", "scripts/gates/gates.py", 'ARRIVAL_PHRASES = ("the standard model is derived", "the standard model has been derived"'),
    ("R79-SM-46; row 20 (a)", "scripts/checks/harvest_debt.py", 'os.environ.get("OA_HARVEST_PIN_OVERRIDE", "")'),
    ("R79-SM-46; row 21", "scripts/checks/point_debt.py", 'path = pathlib.Path(os.environ.get("OA_POINT_REGISTER", REGISTER))'),
    ("R79-SM-47", "scripts/checks/relay_debt.py", "It moves with every commit, so it cannot"),
    ("row 10 (a)", "scripts/gates/gates.py", "int(t) < int(pt)"),
    ("row 20 (b)", "scripts/checks/harvest_debt.py", "time.time()"),
    ("row 20 (c)", "scripts/checks/harvest_debt.py", "datetime.date.fromtimestamp("),
    ("row 22", "scripts/checks/harvest_debt.py", "sorted(hits, key=len)[0]"),
    ("row 23", "scripts/gates/gates.py", 'before = git("show", f"{c}^:{path}")'),
    ("row 24", "scripts/gates/gates.py", "on_disk = any(os.path.exists(os.path.join(repo, c)) for c in every)"),
)

RUN = ("import sys, json, importlib.util\n"
       "sys.dont_write_bytecode = True\n"
       "s = importlib.util.spec_from_file_location('gates_read', sys.argv[1] + '/scripts/gates/gates.py')\n"
       "g = importlib.util.module_from_spec(s); s.loader.exec_module(g)\n"
       "out = {}\n"
       "for name in (sys.argv[2].split(',') if sys.argv[2] else list(g.GATES)):\n"
       "    try:\n"
       "        r = g.GATES[name](); out[name] = [bool(r[0]), r[1] if isinstance(r[1], str) else ' | '.join(map(str, r[1]))]\n"
       "    except Exception as e:\n"
       "        out[name] = [None, 'raised ' + type(e).__name__]\n"
       "print(json.dumps(out))\n")


def gates_of(tree, names="", env=None):
    r = subprocess.run([sys.executable, "-B", "-c", RUN, tree, names], capture_output=True, text=True, env=env)
    assert r.returncode == 0, r.stderr[-600:]
    return json.loads(r.stdout.strip().splitlines()[-1])


def module_of(tree):
    spec = importlib.util.spec_from_file_location("gates_of_" + str(abs(hash(tree))), os.path.join(tree, "scripts", "gates", "gates.py"))
    g = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(g)
    return g


def git(repo, *a):
    r = subprocess.run(["git", "-C", repo, "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


print("main's head: %s      the series: %s" % (git(MAIN, "rev-parse", "--short=9", "HEAD"), git(SERIES, "rev-parse", "--short=9", "HEAD")))

print("\n1. THE QUOTED LINE: does it still stand?\n")
print("   %-24s %-34s %-12s %-12s" % ("finding", "file", "main's head", "the series"))
for finding, rel, line in QUOTED:
    stands = ["stands" if line in open(os.path.join(t, rel), encoding="utf-8").read() else "gone" for _, t in TREES]
    print("   %-24s %-34s %-12s %-12s" % (finding, rel, *stands))
for name, tree in TREES:
    g = open(os.path.join(tree, "scripts", "gates", "gates.py"), encoding="utf-8").read()
    def body(fn):
        at = g.index("def %s(" % fn)
        return g[at:g.index("\ndef ", at + 1)]
    print("   %-12s --first-parent in: commit_day_problems %s; hash_lists_immutable_problems %s; hash_lists_by_content_problems %s.  "
          "attribution_history_problems reads the author's name (%%an) %s, and the committer or an address (%%cn, %%ae, %%ce) %s"
          % (name, *("yes" if "--first-parent" in body(f) else "no" for f in ("commit_day_problems", "hash_lists_immutable_problems", "hash_lists_by_content_problems")),
             "yes" if "%an" in body("attribution_history_problems") else "no",
             "yes" if any(x in body("attribution_history_problems") for x in ("%cn", "%ae", "%ce")) else "no"))

with tempfile.TemporaryDirectory() as tmp:
    print("\n2. THE PLANTS FOR WHAT THE SERIES CLOSE\n")
    print("   (a) R79-SM-46, rows 20 (a) and 21: a variable of the environment moves a debt gate")
    register = os.path.join(tmp, "a_planted_register.md")
    lines = open(os.path.join(MAIN, "docs", "POINT_REGISTER.md"), encoding="utf-8").read().splitlines(keepends=True)
    open(register, "w", encoding="utf-8").write("".join(lines[:-150]))                       # the register, without its last 150 lines
    seat_head = subprocess.run(["git", "-C", MAIN, "rev-parse", "--verify", "--quiet", "origin/agy-002/verify"], capture_output=True, text=True).stdout.strip()
    planted = dict(os.environ, OA_POINT_REGISTER=register, OA_HARVEST_PIN_OVERRIDE="agy002=" + seat_head)
    print("       OA_POINT_REGISTER: the register without its last 150 lines.   OA_HARVEST_PIN_OVERRIDE: agy002=%s"
          % (seat_head[:9] or "(this clone has no origin/agy-002/verify: the second variable could not be planted)"))
    for name, tree in TREES:
        plain, moved = gates_of(tree, "point-debt,harvest-debt"), gates_of(tree, "point-debt,harvest-debt", planted)
        for gate in ("point-debt", "harvest-debt"):
            print("       %-12s %-13s %s" % (name, gate, "MOVED BY THE VARIABLE" if plain[gate] != moved[gate] else "the same sentence with and without the variable"))
            if plain[gate] != moved[gate]:
                print("            without: %s %s" % (plain[gate][0], plain[gate][1][:150]))
                print("            with:    %s %s" % (moved[gate][0], moved[gate][1][:150]))

    print("\n   (b) row 10, its third part: a repository that holds no commit")
    for name, tree in TREES:
        repo = os.path.join(tmp, "no_commit_" + name.replace(" ", "_").replace("'", ""))
        for part in ("gates", "checks"):
            shutil.copytree(os.path.join(tree, "scripts", part), os.path.join(repo, "scripts", part), ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        git(repo, "init", "-q")
        out = gates_of(repo)
        says = sum(1 for ok, d in out.values() if ok is False and "holds no commit" in d)
        print("       %-12s %d of %d gates say that the repository holds no commit.  A debt gate, which asks the commit's day, says:" % (name, says, len(out)))
        print("            %s" % out["point-debt"][1][:170].replace(tmp, "<the plant>"))

    print("\n3. THE PLANTS FOR WHAT THE SERIES DO NOT TOUCH\n")
    print("   (a) R79-SM-44, R79-SM-45 and row 25: a sentence of arrival, as each reader planted it")
    def fill(n):
        """n characters of plain words, each after one space"""
        words = {0: "", 1: " ", 2: " a", 3: " so", 4: " and", 5: " then", 6: " again", 7: " indeed", 8: " so then", 9: " and then",
                 10: " again and", 11: " again then", 12: " again again", 13: " indeed again"}
        return " indeed" * ((n - n % 7) // 7 - 1) + words[n % 7 + 7] if n >= 14 else words[n]

    def cut(extra):
        """one sentence in which the gate's 160 characters start inside the word "claim": at its "aim" (extra 0), or one later"""
        head = " with care, after long work in every sector and at every scale, for each field and each coupling,"
        between = head + fill(157 + extra - len(head) - len(" that ")) + " that "
        assert len(between) == 157 + extra
        return "We claim" + between + "the Standard Model is derived."
    sentences = (("the control: the bare sentence", "The Standard Model is derived."),
                 ("R79-SM-44", "Without a single free parameter, the Standard Model is derived."),
                 ("R79-SM-44", "No longer a hope: the Standard Model is derived."),
                 ("R79-SM-44", "Not only the gauge group: the standard model is derived."),
                 ("R79-SM-45, a word inside", "As of this arc the Standard Model is now derived."),
                 ("R79-SM-45, a line break inside", "As of this arc the Standard Model\nis derived."),
                 ("row 25", "Without question, the Standard Model is derived."),
                 ("row 25", "There is no doubt: all nineteen are derived."),
                 ("row 25", "After years of aimless search, the Standard Model is derived."),
                 ("row 25, \"claim\" cut to \"aim\" at the 160th", cut(0)),
                 ("the same sentence, one letter longer", cut(1)))
    for name, tree in TREES:
        g = module_of(tree)
        print("       %s" % name)
        for n, (what, text) in enumerate(sentences):
            repo = os.path.join(tmp, "arrival_%s_%d" % (name.replace(" ", "_").replace("'", ""), n))
            os.makedirs(os.path.join(repo, "docs"))
            open(os.path.join(repo, "docs", "A_PAGE.md"), "w", encoding="utf-8").write("# A page\n\n" + text + "\n")
            git(repo, "init", "-q"); git(repo, "add", "-A"); git(repo, "commit", "-q", "-m", "a page")
            hits = g.arrival_hits(repo)
            print("            %-12s %-42s %s" % ("CAUGHT" if hits else "passes", what, text.replace("\n", "<line break>")[-66:]))

    print("\n   (b) row 24, its third part: a passing sentence that holds the word \"skipped\"")
    for name, tree in TREES:
        g = module_of(tree)
        line = g.result_line("closure-generated", True, "every generated page compared with its builder; skipped in part: no seat's branch in this clone")
        print("       %-12s the runner prints: %s" % (name, line.strip()[:110]))
