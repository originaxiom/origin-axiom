#!/usr/bin/env python3
"""Re-audit 6, the finding E5: planted cases against main's lock, tests/test_b892_walls_on_the_line.py.

Each case plants one thing in a SCRATCH CLONE of main (never in the working tree), runs the lock there, and reports
whether it turned red.  The clone is reset between cases.  The lock has two lanes: the default one, and a slow one
(OA_SLOW=1) that runs the computation again.

    python3 e5_plants.py --repo REPO --ref origin/main --work DIR        (DIR outside the repository)

EXPECTATIONS, written before the first run.  "caught" = the lock fails.
  c0   nothing planted, default lane                                                          passes (control)
  c1   nothing planted, slow lane                                                             passes (control)
  q1   one wall value changed in the committed result (0.0515261607 to 0.0515261707)          caught
  q2   the correction removed from B892's findings (the quoted block under the scan's sentence)   caught
  q3   the instrument broken (t1 = 12 x the root, not 13), the committed run left as it is:
         default lane                                                                         NOT caught
         slow lane                                                                            caught
  q4   the instrument broken as in q3 and run, so that the committed result is its output     caught (default lane)
  q5   the correction removed from B892's verdict line                                        caught
  q6   the old scan's script mended in silence (its refinement made unconditional)            caught (the lock pins the
       script as it was run)
  q7   a new page under docs/ states the old claim ("the 120-point real-line scan shows that no real nullity-14 point
       exists: a fact") with no correction                                                    NOT caught (no sweep)
"""
import sys, os, re, json, shutil, subprocess

repo = os.path.abspath(sys.argv[sys.argv.index("--repo") + 1])
ref = sys.argv[sys.argv.index("--ref") + 1]
work = os.path.abspath(sys.argv[sys.argv.index("--work") + 1])
LOCK = "tests/test_b892_walls_on_the_line.py"
ARC = "frontier/B892_second_measurement"
TOOL = ARC + "/verification/walls_on_the_line.py"


def sh(args, cwd=None, check=True, env=None):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        sys.exit("failed: %s\n%s" % (" ".join(args)[:160], r.stderr[:300]))
    return r


if os.path.exists(work):
    shutil.rmtree(work)
sh(["git", "clone", "-q", "--no-checkout", "file://" + repo, work])
sha = sh(["git", "-C", repo, "rev-parse", ref]).stdout.strip()
sh(["git", "-C", work, "fetch", "-q", "file://" + repo, sha])
sh(["git", "-C", work, "checkout", "-q", "--detach", sha])
print("planted cases against %s at main %s" % (LOCK, sha[:9]), flush=True)


def reset():
    sh(["git", "-C", work, "checkout", "-q", "--", "."]); sh(["git", "-C", work, "clean", "-q", "-fd"])


def run_lock(slow=False):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("OA_SLOW", None)
    if slow:
        env["OA_SLOW"] = "1"
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", LOCK], cwd=work, capture_output=True, text=True, env=env)
    failed = sorted(set(re.findall(r"^FAILED \S+::(\S+)", r.stdout, re.M)))
    tail = [l for l in r.stdout.strip().splitlines() if " passed" in l or " failed" in l or " skipped" in l][-1:]
    return r.returncode != 0, failed, (tail[0].strip() if tail else "")


def path(rel):
    return os.path.join(work, rel)


def read(rel):
    return open(path(rel), encoding="utf-8").read()


def write(rel, text):
    os.makedirs(os.path.dirname(path(rel)), exist_ok=True)
    with open(path(rel), "w", encoding="utf-8") as fh:
        fh.write(text)


def q1():
    rel = ARC + "/verification/walls_on_the_line.json"
    text = read(rel); j = json.loads(text)
    walls = j["numbers"]["walls"]; hit = [w for w in walls if abs(w[0] - 0.0515261607) < 1e-9]
    assert len(hit) == 1
    hit[0][0] += 1e-8
    write(rel, json.dumps(j, indent=1) + "\n")


def q2():
    rel = ARC + "/FINDINGS.md"
    lines = read(rel).splitlines()
    start = next(i for i, l in enumerate(lines) if "CORRECTED 2026-11-11 (the audit's finding E5" in l)
    end = start
    while end < len(lines) and lines[end].lstrip().startswith(">"):
        end += 1
    assert end > start
    write(rel, "\n".join(lines[:start] + lines[end:]) + "\n")


def break_tool():
    text = read(TOOL); old = "t1 = 13 * min("
    assert text.count(old) == 1
    write(TOOL, text.replace(old, "t1 = 12 * min("))


def q4():
    break_tool()
    subprocess.run([sys.executable, "-B", path(TOOL)], cwd=work, capture_output=True, text=True)


def q5():
    rel = ARC + "/arc_verdict.json"
    j = json.loads(read(rel)); assert "CORRECTED 2026-11-11 (the audit's finding E5)" in j["claim_one_line"]
    j["claim_one_line"] = re.sub(r"\s*\[CORRECTED 2026-11-11 \(the audit's finding E5\).*", "", j["claim_one_line"], flags=re.S)
    write(rel, json.dumps(j, ensure_ascii=False, indent=1) + "\n")


def q6():
    rel = ARC + "/wall_search.py"
    text = read(rel); assert text.count("if not found:") == 1
    write(rel, text.replace("if not found:", "if True:"))


def q7():
    write("docs/PLANTED_PAGE.md", "# A planted page\n\nB892: the 120-point real-line scan shows that no real nullity-14 point exists on the line of the second measurement: a fact.\n")


CASES = [
    ("c0", "nothing planted, default lane", lambda: None, False, False),
    ("c1", "nothing planted, slow lane", lambda: None, True, False),
    ("q1", "one wall value changed in the committed result", q1, False, True),
    ("q2", "the correction removed from B892's findings", q2, False, True),
    ("q3a", "the instrument broken, the committed run left; default lane", break_tool, False, False),
    ("q3b", "the instrument broken, the committed run left; slow lane", break_tool, True, True),
    ("q4", "the instrument broken and run, so the committed result is its output", q4, False, True),
    ("q5", "the correction removed from B892's verdict line", q5, False, True),
    ("q6", "the old scan's script mended in silence", q6, False, True),
    ("q7", "a new page states the old claim with no correction", q7, False, False),
]
held = 0
for tag, what, plant, slow, expect_caught in CASES:
    reset(); plant()
    caught, failed, tail = run_lock(slow)
    ok = caught == expect_caught; held += ok
    print("%-4s %-11s expected %-11s %s  %s  [%s]%s" % (tag, "CAUGHT" if caught else "NOT CAUGHT", "caught" if expect_caught else "not caught", "HOLDS" if ok else "FAILS", what, tail,
                                                      ("  [red: " + ", ".join(failed) + "]") if failed else ""), flush=True)
reset()
print()
print("expectations that hold: %d of %d" % (held, len(CASES)))
