#!/usr/bin/env python3
"""Re-audit 6, the finding E2: planted cases against main's rewritten lock, tests/test_b734_m004_congruence.py.

The lock says it fails "if any page states the old level for this group with no correction in the same file".  Each case
below plants one thing in a SCRATCH CLONE of main (never in the working tree), runs the lock there, and reports whether
the lock turned red.  The clone is reset between cases.

    python3 e2_plants.py --repo REPO --ref origin/main --work DIR        (DIR outside the repository)

EXPECTATIONS, written before the first run.  "caught" = the lock fails.
  c0   nothing planted                                                                  the lock passes (control)
  p1   a new page under docs/: "The figure-eight knot group m004 is congruence at level (8)."        caught
  p2   the same statement over two lines                                                not caught
  p3   "m004 is a congruence subgroup of level 8."  (no brackets)                       not caught
  p4   "m004 first becomes congruence at Γ((8))."                                       not caught
  p5   p1's sentence in a new .tex file under papers/                                   not caught
  p6   p1's sentence appended to the README at the root                                 not caught
  p7   the correction removed from a page that carries it (B733's FINDINGS)             caught
  p8   the lock's own generator B replaced by [[1,0],[1,1]] (another group)             caught  (the lock can fail)
  p9   the correction removed from B734's verdict line                                  caught
  p10  a new arc_verdict.json whose claim line is p1's sentence                         not caught
  p11  p1's sentence added to docs/LAW_MAP.md, which carries the correction elsewhere   not caught (main's rule: a
       correction in the same file excuses the file)
  s1   SEEN BEFORE THIS SCRIPT WAS WRITTEN, so not a blind expectation: at main's head the generated page
       docs/views/THE_SPINE.md has a line for B734 that states "(2)³=(8)" and holds no correction    true
"""
import sys, os, re, json, shutil, subprocess

repo = os.path.abspath(sys.argv[sys.argv.index("--repo") + 1])
ref = sys.argv[sys.argv.index("--ref") + 1]
work = os.path.abspath(sys.argv[sys.argv.index("--work") + 1])
LOCK = "tests/test_b734_m004_congruence.py"
MARK = "the congruence level is (4)"
SENTENCE = "The figure-eight knot group m004 is congruence at level (8).\n"


def sh(args, cwd=None, check=True):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.exit("failed: %s\n%s" % (" ".join(args)[:160], r.stderr[:300]))
    return r


if os.path.exists(work):
    shutil.rmtree(work)
sh(["git", "clone", "-q", "--no-checkout", "file://" + repo, work])
sha = sh(["git", "-C", repo, "rev-parse", ref]).stdout.strip()
sh(["git", "-C", work, "fetch", "-q", "file://" + repo, sha])
sh(["git", "-C", work, "checkout", "-q", "--detach", sha])
print("planted cases against %s at main %s" % (LOCK, sha[:9]))


def reset():
    sh(["git", "-C", work, "checkout", "-q", "--", "."]); sh(["git", "-C", work, "clean", "-q", "-fd"])


def run_lock():
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", LOCK], cwd=work, capture_output=True, text=True, env=env)
    failed = sorted(set(re.findall(r"^FAILED \S+::(\S+)", r.stdout, re.M)))
    return r.returncode != 0, failed


def path(rel):
    return os.path.join(work, rel)


def write(rel, text, mode="w"):
    os.makedirs(os.path.dirname(path(rel)), exist_ok=True)
    with open(path(rel), mode, encoding="utf-8") as fh:
        fh.write(text)


def read(rel):
    return open(path(rel), encoding="utf-8").read()


def p7():
    rel = "frontier/B733_observer_space/FINDINGS.md"
    text = read(rel); assert MARK in text
    write(rel, "\n".join(l for l in text.splitlines() if MARK not in l) + "\n")


def p8():
    text = read(LOCK); old = "B = (E, Z, sub(Z, add(E, w)), E)"
    assert text.count(old) == 1
    write(LOCK, text.replace(old, "B = (E, Z, E, E)"))


def p9():
    rel = "frontier/B734_m004_is_congruence/arc_verdict.json"
    j = json.loads(read(rel)); assert MARK in j["claim_one_line"]
    j["claim_one_line"] = re.sub(r"\s*\[CORRECTED 2026-11-11.*", "", j["claim_one_line"], flags=re.S)
    assert MARK not in j["claim_one_line"]
    write(rel, json.dumps(j, ensure_ascii=False, indent=1) + "\n")


def p11():
    assert MARK in read("docs/LAW_MAP.md")
    write("docs/LAW_MAP.md", "\n" + SENTENCE, "a")


CASES = [
    ("c0", "nothing planted", lambda: None, False),
    ("p1", "a new page under docs/ states level (8) for m004", lambda: write("docs/PLANTED_PAGE.md", "# A planted page\n\n" + SENTENCE), True),
    ("p2", "the same statement over two lines", lambda: write("docs/PLANTED_PAGE.md", "# A planted page\n\nThe figure-eight knot group m004 is congruence\nat level (8).\n"), False),
    ("p3", "\"a congruence subgroup of level 8\", no brackets", lambda: write("docs/PLANTED_PAGE.md", "# A planted page\n\nm004 is a congruence subgroup of level 8.\n"), False),
    ("p4", "\"first becomes congruence at Γ((8))\"", lambda: write("docs/PLANTED_PAGE.md", "# A planted page\n\nm004 first becomes congruence at Γ((8)).\n"), False),
    ("p5", "p1's sentence in a new .tex file under papers/", lambda: write("papers/planted/planted.tex", "\\section{Planted}\n" + SENTENCE), False),
    ("p6", "p1's sentence appended to the root README", lambda: write("README.md", "\n" + SENTENCE, "a"), False),
    ("p7", "the correction removed from B733's FINDINGS", p7, True),
    ("p8", "the lock's generator B replaced by [[1,0],[1,1]]", p8, True),
    ("p9", "the correction removed from B734's verdict line", p9, True),
    ("p10", "a new arc_verdict.json whose claim line states level (8)", lambda: write("frontier/B99998_planted/arc_verdict.json", json.dumps({"id": "B99998", "verdict": "PROVED", "claim_one_line": SENTENCE.strip()}) + "\n"), False),
    ("p11", "p1's sentence added to docs/LAW_MAP.md, which carries the correction elsewhere", p11, False),
]
held = 0
for tag, what, plant, expect_caught in CASES:
    reset(); plant()
    caught, failed = run_lock()
    ok = caught == expect_caught; held += ok
    print("%-4s %-11s expected %-11s %s  %s%s" % (tag, "CAUGHT" if caught else "NOT CAUGHT", "caught" if expect_caught else "not caught",
                                                "HOLDS" if ok else "FAILS", what, ("  [red: " + ", ".join(failed) + "]") if failed else ""))
reset()
spine = [l for l in read("docs/views/THE_SPINE.md").splitlines() if "**B734**" in l]
s1 = len(spine) == 1 and "(2)³=(8)" in spine[0] and MARK not in spine[0] and "(4)" not in spine[0]
print("s1   %s  the generated spine's line for B734 states the old level and holds no correction: %s" % ("TRUE " if s1 else "FALSE", spine[0] if spine else "(no line)"))
print()
print("expectations that hold: %d of %d (and s1 is %s)" % (held, len(CASES), "true" if s1 else "false"))
