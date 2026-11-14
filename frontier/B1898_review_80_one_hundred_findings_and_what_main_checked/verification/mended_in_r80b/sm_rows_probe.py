#!/usr/bin/env python3
"""Review 80: main's own recount of the rows of the SM seat's file that are counts, dates or the presence of a sentence.
Everything is read from git at c40446392 (what the seat read).  The owner's words are never printed: where a row is about
a quotation of him, only the line's number and its length are given."""
# NOTE OF THE MEND, 2026-11-12 (R80b, part 6; sent back by the builder with R80a, and main's fault by its word in M16).
# Main's script stands as main wrote it in ../checks/, held there by its hash.  This copy differs in four places.  Each is
# marked: the lines main wrote stand after "#| ", the lines that replace them follow, to "# END OF THE MEND".  With each
# marked block put back, and this note taken out, the file is main's, byte for byte: the arc's lock holds that.
#   0. two modules more are imported, for the mends below;
#   1. the three times of SM-04 were printed in the zone of the machine that ran the script, so the kept file read one
#      hour apart on two machines.  They are printed in UTC, and say so;
#   2. SM-16 asked whether f6e89032a is a commit in the repository.  It is an object in main's repository, where it was a
#      scratch commit on no branch, and in no clone; so the row read "not held" on main's machine, against main's own
#      table, and "held" in every clone.  It asks now whether the commit is on a branch or a tag, which is the same in
#      main's repository and in a clone;
#   3. the output was written to a folder of main's own working tree.  It is written beside this script.
# END OF THE NOTE
# MENDED (0).  Main wrote:
#| import subprocess, json, re, math, ast
import os, pathlib, subprocess, json, re, math, ast
# END OF THE MEND
AT = "c40446392"
def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True); return r.stdout if r.returncode == 0 else None
def show(p, rev=AT): return git("show", "%s:%s" % (rev, p))
def ls(prefix, rev=AT): return [p for p in git("ls-tree", "-r", "--name-only", rev).split("\n") if p.startswith(prefix)]
OUT = {}
def say(row, what, held):
    OUT[row] = {"main finds": what, "held": bool(held)}; print("%-10s %-5s %s" % (row, "HELD" if held else "NOT", str(what)[:330]))

# ---- SM-04: was anything landed between the last message to the readers and the entry?
# MENDED (1).  Main wrote:
#| t = lambda c: git("log", "-1", "--format=%cd", "--date=format-local:%Y-%m-%d %H:%M:%S", c).strip()
t = lambda c: subprocess.run(["git", "log", "-1", "--format=%cd", "--date=format-local:%Y-%m-%d %H:%M:%S UTC", c],
                             capture_output=True, text=True, env=dict(os.environ, TZ="UTC")).stdout.strip()
# END OF THE MEND
between = git("log", "--format=%h", "f8b5e6769..84baf38fb", "--first-parent").split()
files = git("show", "--stat", "--format=", "c66c8ccae").strip().split("\n")
touched = [l.split("|")[0].strip() for l in files if "|" in l]
say("SM-04", {"last message": t("f8b5e6769"), "c66c8ccae": t("c66c8ccae"), "entry": t("84baf38fb"), "commits between": len(between), "c66c8ccae touches": [p for p in touched if p in ("CHANGELOG.md", "PROGRESS_LOG.md", "docs/CAMPAIGN_STATUS.md", "docs/POINT_REGISTER.md") or "SEAL" in p.upper()]},
    "c66c8ccae" in " ".join(between) and "CHANGELOG.md" in touched)

# ---- SM-07: the answers' own sentence on what the rule counts
ans = show(next(p for p in ls("frontier/B1892_") if p.endswith("ANSWERS.md")))
i = ans.find("which the rule does not count"); seg = " ".join(ans[max(0, i - 500):i + 220].split())
say("SM-07", {"the sentence says the rule does not count a pair and then gives 88 and ten": ("does not count" in seg and "88 distinct" in seg and "ten were found twice" in seg)}, "does not count" in seg and "88 distinct" in seg)

# ---- SM-11: the run file's own line on patch 6
run = show(next(p for p in ls("frontier/B1893_") if p.endswith("each_patchs_lock_on_the_commit_before_run.txt")))
say("SM-11", {"the run file says patch 6 was not run by main": "not run by main" in run, "the page says each patch's lock fails on the commit before it": "Each patch's lock fails on the commit before it" in show(next(p for p in ls("frontier/B1893_") if p.endswith("FINDINGS.md")))}, "not run by main" in run)

# ---- SM-16: is f6e89032a a commit here?
# MENDED (2).  Main wrote:
#| say("SM-16", {"f6e89032a is a commit in this repository": git("cat-file", "-t", "f6e89032a") is not None}, git("cat-file", "-t", "f6e89032a") is None)
on_a_ref = [l for l in (git("for-each-ref", "--contains", "f6e89032a", "--format=%(refname)") or "").split("\n") if l]
say("SM-16", {"f6e89032a is on a branch or a tag of this repository": bool(on_a_ref)}, not on_a_ref)
# END OF THE MEND

# ---- SM-18: test files in tests/ at the series' anchor (the page's own anchor is named in its text)
f93 = show(next(p for p in ls("frontier/B1893_") if p.endswith("FINDINGS.md")))
anchor = re.search(r"anchor[^`]*`([0-9a-f]{7,10})`", f93)
anc = anchor.group(1) if anchor else None
if anc and git("cat-file", "-t", anc):
    tests = [p for p in git("ls-tree", "-r", "--name-only", anc, "tests/").split("\n") if re.match(r"tests/test_[^/]*\.py$", p)]
    say("SM-18", {"anchor": anc, "tests/test_*.py": len(tests), "of them test_b*.py": sum(1 for p in tests if re.match(r"tests/test_b[^/]*\.py$", p))}, len(tests) != 1407)
else:
    say("SM-18", {"anchor not read from the page": anc}, False)

# ---- SM-19: the tests of B1881's lock, now and along its history
lockp = next(p for p in ls("frontier/B1881_") if "/test_b1881" in p)
def ntests(rev):
    s = show(lockp, rev); return None if s is None else sum(1 for n in ast.walk(ast.parse(s)) if isinstance(n, ast.FunctionDef) and n.name.startswith("test_"))
hist = git("log", "--format=%h", AT, "--", lockp).split()
say("SM-19", {"tests at the commit read": ntests(AT), "along the lock's history (oldest first)": [ntests(c) for c in reversed(hist)],
             "B1895 still says fourteen": "the lock has fourteen tests now" in show(next(p for p in ls("frontier/B1895_") if p.endswith("FINDINGS.md"))),
             "the lock's comment says four": "The four tests below hold the six." in show(lockp)}, ntests(AT) == 15)

# ---- SM-27: the old sign of the index for a unit on one line, where it still stands
hits = [l for l in (git("grep", "-n", "-F", "-e", "a unit on one line gives index one", "-e", "a unit on one line gives one", AT, "--", "*.md", "*.py") or "").split("\n") if l]
say("SM-27", {"places": sorted({l.split(":")[1] for l in hits}), "lines": len(hits)}, len(hits) >= 2)

# ---- SM-28 and SM-29: a block quotation of the owner on the plan (the words are not printed)
prog = show("frontier/B1861_the_closure_programme/PROGRAMME.md").split("\n")
src = show("frontier/B1861_the_closure_programme/verification/programme_source.py"); bld = show("frontier/B1861_the_closure_programme/verification/build_programme.py")
m = re.search(r"CONFIRMATION\s*=\s*\(", src)
conf = ast.literal_eval(re.search(r"CONFIRMATION\s*=\s*(\(.*?\))\n", src, re.S).group(1)) if m else None
quoted = [k + 1 for k, l in enumerate(prog) if conf and l.strip() == '> "%s"' % conf[1]]
say("SM-28", {"the plan's page holds the confirmation as a block quotation at line": quoted, "its length in characters": (len(conf[1]) if conf else None),
             "the builder emits it": '"> \\"%s\\"" % S.CONFIRMATION[1]' in bld, "the builder refuses to build without it": "rulings are marked confirmed with no date or no words of the owner" in bld}, bool(quoted))
lock61 = show(next(p for p in ls("frontier/B1861_") if "/test_b1861" in p))
say("SM-29", {"the lock's assertion looks for one phrase and forbids one spelling": 'assert "the option the owner chose, in main\'s label" in page and "NOT CONFIRMED: the owner, \\"" not in page' in lock61}, 'NOT CONFIRMED: the owner, \\"' in lock61)

# ---- SM-31: the lock's docstring against its assertion
l81 = show(lockp)
say("SM-31", {"docstring says two planted lines": "with two planted lines the scan must report" in l81, "an assertion of three lines": "[2, 3, 4]" in l81}, "with two planted lines the scan must report" in l81 and "[2, 3, 4]" in l81)

# ---- SM-34: the roots of x^2 - x - 1 at each level
roots = {N: sum(1 for x in range(N) if (x * x - x - 1) % N == 0) for N in range(2, 211)}
c = {k: sum(1 for N, v in roots.items() if N <= 200 and N != 5 and v == k) for k in (0, 1, 2, 4)}
say("SM-34", {"levels 2..200 other than 5: with no root": c[0], "with one": c[1], "with two": c[2], "with four": c[4], "at 5": roots[5], "at 209": roots[209],
             "the page's bracket": "LR keeps exactly one point at N = 5, and two at other levels.]" in show(next(p for p in ls("frontier/B1884_") if p.endswith("FINDINGS.md")))}, c[0] == 173 and c[2] == 25 and roots[209] == 4)

# ---- SM-35: the verdict line's words
v84 = json.loads(show(next(p for p in ls("frontier/B1884_") if p.endswith("arc_verdict.json"))))
say("SM-35", {"the verdict line says main's own convention": "The same counts hold in main's own convention." in v84["claim_one_line"]}, "main's own convention" in v84["claim_one_line"])

# ---- SM-21: is the sentence B1897 attributes to B1895 in any file of B1895?
phr = ["the count that matters is the reader's", "count that matters"]
in95 = [p for p in ls("frontier/B1895_") if any(x in (show(p) or "") for x in phr)]
say("SM-21", {"files of B1895 that hold the sentence": in95, "B1897 says B1895 said it": "It said that the count that matters is the reader's." in show(next(p for p in ls("frontier/B1897_") if p.endswith("FINDINGS.md")))}, not in95)

# ---- SM-20: B1895's sentences left as they were after the reader ran its plants
f95 = show(next(p for p in ls("frontier/B1895_") if p.endswith("FINDINGS.md"))); v95 = json.loads(show(next(p for p in ls("frontier/B1895_") if p.endswith("arc_verdict.json"))))
say("SM-20", {"§ 5 still says the reader's plants were not run": "The reader's planted errors were not run" in f95, "the verdict line still says ten tests": "now ten tests" in v95["claim_one_line"], "the page names 17 of 23 somewhere": "17 of 23" in f95}, "The reader's planted errors were not run" in f95 and "now ten tests" in v95["claim_one_line"])

# ---- SM-15: which series is 'the series after it'
say("SM-15", {"the page says the cases that pass are for the series after it": "pass are for the series after it." in f93, "and names the fourth series for one of them": "fourth patch of its fourth series" in f93}, "pass are for the series after it." in f93 and "fourth patch of its fourth series" in f93)

# MENDED (3).  Main wrote:
#| json.dump(OUT, open("audit/review80/sm_rows_probe.json", "w"), indent=1)
json.dump(OUT, open(pathlib.Path(__file__).with_name("sm_rows_probe.json"), "w"), indent=1)
# END OF THE MEND
print("\nrows probed: %d; held: %d" % (len(OUT), sum(v["held"] for v in OUT.values())))
