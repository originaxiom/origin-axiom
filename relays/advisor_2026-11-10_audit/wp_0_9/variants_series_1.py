#!/usr/bin/env python3
"""WP-0.9, series 1: this seat's own variants on its own mend, before it is sent.

The series: the grade of a verdict is held to the evidence it names (patch 1); the front page counts the verdicts by grade
(patch 2).  Main verifies with cases this seat has not seen.  These are other shapes of the same, on main's real arcs, in a
scratch clone.

    python3 variants_series_1.py --src CLONE --work DIR      (CLONE: a clone holding the patches at its HEAD)

Nothing is written into CLONE.  DIR is emptied and used for the scratch clone.

EXPECTATIONS, written before the first run.  "red" = the gate arc-data returns False.  Four of them are PASSES: each is a
limit of the mend, stated in its patch, and the variant pins where the limit lies.
    y1   the candidate (B1841) is graded a theorem and names a lock that names it
         and is not its own (tests/test_seal_immutable.py)                           red
    y2   the candidate is graded an exact computation, naming one of its scripts      red: it has no lock of its own
    y3   one of the fourteen (B1612) is graded a theorem and names the lock of
         another of the fourteen (B1637)                                             red
    y4   a verdict file gives its grade as a list of one word                         red
    y5   a verdict file gives the word with a capital letter                          red: the five words are exact
    y6   a grade names a folder as its evidence                                       red
    y7   the candidate is graded a numerical estimate, naming one of its scripts
         and one committed output                                                     PASSES: the gate reads a form
    y8   the candidate is graded sealed cells held, naming its sealed file, with a
         count this script makes up (1 of 1)                                          PASSES: the count is the arc's word
    y9   an arc that is not an instrument and is PROVED is graded a process           PASSES: what PROVED may rest on is
                                                                                      main's and the owner's; it is printed
    y10  B1612 is graded a theorem with its own lock; the views are generated         PASSES; the gate says one of the named
                                                                                      carries a grade now; the front page
                                                                                      reads 1 theorem and 1099 with no grade,
                                                                                      and the gate on the views passes

  THE FIRST RUN (variants_series_1_first_run_out.txt) stopped at y3, and y1 and y2 held.  The harness looked for an arc's lock
  in the arc's own folder; B1612 and B1637 keep theirs in tests/, under their number.  No expectation is changed: the harness
  now finds a lock where the gate itself looks for one.
"""
import sys, os, re, json, glob, shutil, subprocess

src = os.path.abspath(sys.argv[sys.argv.index("--src") + 1])
work = os.path.abspath(sys.argv[sys.argv.index("--work") + 1])
WHO = ["-c", "user.name=originaxiom", "-c", "user.email=planted@example.invalid"]
RUN = r'''
import sys, json, importlib.util
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("gates_under_variants", "scripts/gates/gates.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
out = {}
for name in sys.argv[1].split(","):
    try:
        r = g.GATES[name](); d = r[1] if isinstance(r[1], str) else " | ".join(map(str, r[1]))
        out[name] = [bool(r[0]), d[:900]]
    except Exception as e:
        out[name] = [None, "RAISED %s: %s" % (type(e).__name__, str(e)[:200])]
print(json.dumps(out))
'''
PLAIN = {k: v for k, v in os.environ.items() if not k.startswith(("OA_", "GIT_", "PYTEST_"))}
PLAIN["PYTHONDONTWRITEBYTECODE"] = "1"


def sh(args, cwd=None, check=True):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, env=PLAIN)
    if check and r.returncode != 0:
        sys.exit("failed: %s\n%s" % (" ".join(map(str, args))[:200], r.stderr[:400]))
    return r


if os.path.exists(work):
    shutil.rmtree(work)
os.makedirs(work)
clone = os.path.join(work, "clone")
sh(["git", "clone", "-q", "file://" + src, clone])
tip = sh(["git", "-C", clone, "rev-parse", "HEAD"]).stdout.strip()
print("variants on the patches at %s" % tip[:9])
path = lambda rel: os.path.join(clone, rel)


def reset():
    sh(["git", "-C", clone, "reset", "-q", "--hard", tip]); sh(["git", "-C", clone, "clean", "-q", "-fd"])


def commit(text):
    sh(["git", "-C", clone, "add", "-A"]); sh(["git", "-C", clone, *WHO, "commit", "-q", "-m", text])


def gate(name="arc-data"):
    r = subprocess.run([sys.executable, "-B", "-c", RUN, name], cwd=clone, capture_output=True, text=True, env=PLAIN)
    try:
        return json.loads(r.stdout.strip().split("\n")[-1])[name]
    except Exception:
        sys.exit("the gate %s did not run: %s" % (name, (r.stdout + r.stderr)[-400:]))


def grade(folder, **fields):
    reset()
    p = path("frontier/%s/arc_verdict.json" % folder)
    d = json.loads(open(p, encoding="utf-8").read()); d.update(fields)
    open(p, "w", encoding="utf-8").write(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
    commit("planted: a grade on " + folder)
    return gate()


def lock_of(folder):
    """the arc's own lock: in its folder, or in tests/ under its number"""
    found = sorted(glob.glob(path("frontier/%s/verification/test_*.py" % folder)) + glob.glob(path("tests/test_%s_*.py" % folder.split("_")[0].lower())))
    assert found, folder
    return os.path.relpath(found[0], clone)


def own(folder, pattern):
    found = sorted(glob.glob(path("frontier/%s/%s" % (folder, pattern)), recursive=True))
    assert found, (folder, pattern)
    return os.path.relpath(found[0], clone)


results = []


def line(tag, ok, text):
    results.append(bool(ok)); print("%-4s %-6s %s" % (tag, "HOLDS" if ok else "FAILS", text), flush=True)


control = gate()
assert control[0] is True, "arc-data must pass before any variant: " + control[1]
CAND, A, B = "B1841_the_principled_ends_card", "B1612_the_mixing_patterns_the_weave_fixes", "B1637_fits_on_the_ruled_branch"

r = grade(CAND, grade="theorem", grade_evidence=["tests/test_seal_immutable.py"])
line("y1", r[0] is False and CAND in r[1], "the candidate graded a theorem, naming a lock that is not its own: %s" % r[1][:170])
r = grade(CAND, grade="exact computation", grade_evidence=[own(CAND, "**/*.py")])
line("y2", r[0] is False and CAND in r[1], "the candidate graded an exact computation, naming one of its scripts: %s" % r[1][:170])
r = grade(A, grade="theorem", grade_evidence=[lock_of(B)])
line("y3", r[0] is False and A in r[1], "B1612 graded a theorem, naming B1637's lock: %s" % r[1][:170])
r = grade(A, grade=["theorem"], grade_evidence=[lock_of(A)])
line("y4", r[0] is False and A in r[1], "a grade given as a list of one word: %s" % r[1][:150])
r = grade(A, grade="Theorem", grade_evidence=[lock_of(A)])
line("y5", r[0] is False and A in r[1], "the word with a capital letter: %s" % r[1][:150])
r = grade(A, grade="theorem", grade_evidence=["frontier/%s/verification" % A])
line("y6", r[0] is False and A in r[1], "a folder named as evidence: %s" % r[1][:150])
outputs = [p for p in sorted(glob.glob(path("frontier/%s/**/*" % CAND), recursive=True)) if re.search(r"(_run\.txt|_out\.txt|\.jsonl?)$", p) and not p.endswith("arc_verdict.json")]
r = grade(CAND, grade="numerical estimate", grade_evidence=[own(CAND, "**/*.py"), os.path.relpath(outputs[0], clone)])
line("y7", r[0] is True, "the candidate graded a numerical estimate, naming a script and an output: the gate passes (a limit)" if r[0] else "the gate says: " + r[1][:170])
r = grade(CAND, grade="sealed cells held", grade_evidence=["frontier/%s/PREREGISTRATION.md" % CAND], grade_cells=[1, 1])
line("y8", r[0] is True, "the candidate graded sealed cells held with a made-up count: the gate passes (a limit)" if r[0] else "the gate says: " + r[1][:170])
r = grade(A, grade="process")
line("y9", r[0] is True and "1 process" in r[1], "a PROVED arc that is not an instrument graded a process: the gate passes and prints it (a limit) -- %s" % re.search(r"\d+ carry a grade[^;]*", r[1]).group(0) if r[0] else "the gate says: " + r[1][:170])

r = grade(A, grade="theorem", grade_evidence=[lock_of(A)])
said = "1 of the named carry one now: shorten the list" in r[1] and "13 of the 14" in r[1]
sh([sys.executable, "-B", "scripts/views/generate.py"], cwd=clone); sh([sys.executable, "-B", "scripts/views/spine.py"], cwd=clone)
front = [l for l in open(path("README.md"), encoding="utf-8").read().splitlines() if l.startswith("| the PROVED, by the grade")]
commit("planted: the views generated")
views = gate("views-generated")
line("y10", r[0] is True and said and len(front) == 1 and "1 theorem; 1099 carry no grade" in front[0] and views[0] is True,
     "B1612 graded a theorem with its own lock: the gate %s; the front page reads: %s; the gate on the views %s" % (
         "passes and says one of the named carries a grade" if (r[0] and said) else "says: " + r[1][-200:], front[0] if front else "NO SUCH ROW", "passes" if views[0] else "FAILS: " + views[1][:120]))

reset()
print("\n%d of %d expectations hold" % (sum(results), len(results)))
