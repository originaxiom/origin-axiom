#!/usr/bin/env python3
"""WP-0.7, series 4, patches 4 to 8: this seat's own variants on its own mends, before they are sent.

The five patches: a test of a lock is not switched off without a recorded act; the old lines of the member-scope gate are
held by name; the gate that reads a lock's own paths reads them however they are written; a lock does not compare, as text,
a float that a process printed; a test run leaves the tracked files as it found them.  Main verifies with cases this seat
has not seen.  These are other shapes of the same, on the real pages and the real locks, in a scratch clone.

    python3 variants_series_4_part_2.py --src CLONE --work DIR      (CLONE: a clone holding the patches at its HEAD)

Nothing is written into CLONE.  DIR is emptied and used for the scratch clone.

EXPECTATIONS, written before the first run.  "red" = the named gate returns False; for the run check, the run of the tests
ends with a status that is not 0.  Nine of them are PASSES: each is a limit of a mend, stated in its patch, and the variant
pins where the limit lies.
  a test of a lock is switched off (test-vacuity)
    w1   a real lock of tests/ is given a module-wide skip mark                  red, names the lock
    w2   the first test of an arc's own lock skips by a call in its body         red
    w3   one test function is deleted from a real lock, the others stay          red, names the test
    w4   a real lock is moved to another name and one of its tests is marked     red: the lock is followed where it went
    w5   a function of the lock's file decides the skip, and a test calls it     PASSES: a skip that a helper decides
                                                                                 is not read
    w6   a test's body is rewritten to assert something else                     PASSES: what a test asserts is not held
  the old lines of the member-scope gate (member-scope)
    w7   a new NEGATIVE that says it in another of the gate's phrases,
         nothing reworded                                                        red, names the new arc's folder
    w8   the folder of one of the eight old arcs is renamed, its line as it was  red: a line is held by its arc's folder
    w9   a new NEGATIVE about one thread that avoids every phrase                PASSES: the gate reads a wording
  a lock's own paths (tracked-deps)
    w10  the lock of B1671 as it is on main, with one of its three logs
         taken out of the commit and left on disk                                red, names the log
    w11  the same, the log also gone from disk, as in a clean checkout           red, and says that git ignores the path
    w12  a lock names a file inside a folder that .gitignore names (audit/)      red
    w13  a lock goes up from its folder and down again to an ignored file        red
    w14  a lock keeps the folder in an attribute of a class                      PASSES: an attribute is not read
    w15  a lock builds the file's name with an f-string                          PASSES, and the gate's count of paths
                                                                                 with a computed part is one more
  a float that a process printed, compared as text (test-vacuity)
    w16  a new test, added to a lock that holds one of the fourteen named        red, names the new test: the fourteen
                                                                                 are held by test and not by file
    w17  a lock reads what os.popen gave                                         red
    w18  one of the fourteen named tests is given a second pin                   PASSES: a named test is held whole
    w19  a lock formats the float inside its own process                         PASSES: not a process
    w20  the process is started in a module beside the lock                      PASSES: another module is not read
  a test run and the tracked files (the run's status)
    w21  an arc's own lock, run alone by its path, rewrites a tracked file       the run fails and names the file
    w22  main's own test that rewrites the census, run alone                     the run passes, and says that the file
                                                                                 is held by name as found
    w23  a test changes the mode of a tracked file and not its content           the run fails and names the file
    w24  a parallel run in which one test rewrites a tracked file                the run fails, and says so once
    w25  a test leaves a new file that is not tracked                            PASSES: a file that is not tracked is
                                                                                 not the check's
"""
import sys, os, re, json, shutil, subprocess

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
read = lambda rel: open(path(rel), encoding="utf-8").read()


def write(rel, text):
    os.makedirs(os.path.dirname(path(rel)), exist_ok=True)
    with open(path(rel), "w", encoding="utf-8") as fh:
        fh.write(text)


def reset():
    sh(["git", "-C", clone, "reset", "-q", "--hard", tip]); sh(["git", "-C", clone, "clean", "-q", "-fd"])


def commit(text):
    sh(["git", "-C", clone, "add", "-A"]); sh(["git", "-C", clone, *WHO, "commit", "-q", "-m", text])


def gate(name):
    r = subprocess.run([sys.executable, "-B", "-c", RUN, name], cwd=clone, capture_output=True, text=True, env=PLAIN)
    try:
        return json.loads(r.stdout.strip().split("\n")[-1])[name]
    except Exception:
        sys.exit("the gate %s did not run: %s" % (name, (r.stdout + r.stderr)[-400:]))


def tests(*args):
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *args], cwd=clone, capture_output=True, text=True, env=PLAIN)
    return r.returncode, r.stdout + r.stderr


results = []


def line(tag, ok, text):
    results.append(bool(ok)); print("%-4s %-6s %s" % (tag, "HOLDS" if ok else "FAILS", text), flush=True)


def first_test(text):
    m = re.search(r"^def (test_\w+)\([^)]*\):\n", text, re.M)
    return m.group(1), m.end()


for name in ("test-vacuity", "member-scope", "tracked-deps"):
    control = gate(name)
    assert control[0] is True, "%s must pass before any variant: %s" % (name, control[1])
clean_deps = gate("tracked-deps")[1]

# ---- a test of a lock is switched off
LOCK = "tests/test_derived_potential.py"
reset(); write(LOCK, read(LOCK) + "\n\nimport pytest as _planted\npytestmark = _planted.mark.skip(reason='planted')\n"); commit("planted: a module-wide skip mark")
r = gate("test-vacuity"); line("w1", r[0] is False and LOCK in r[1], "a module-wide skip mark on a real lock: %s" % r[1][:150])

reset(); ARC_LOCK = "frontier/B1857_the_read_out_by_a_state_checked/verification/test_b1857_the_read_out_by_a_state_checked.py"
t = read(ARC_LOCK); name, at = first_test(t)
write(ARC_LOCK, t[:at] + "    import pytest; pytest.skip('planted')\n" + t[at:]); commit("planted: a skip called in a test's body")
r = gate("test-vacuity"); line("w2", r[0] is False and "test_b1857" in r[1], "a skip called in the body of %s, in an arc's own lock: %s" % (name, r[1][:140]))

reset(); t = read(LOCK); m = re.search(r"^def (test_gradient_flow_relation)\(.*?(?=^def )", t, re.M | re.S)
write(LOCK, t[:m.start()] + t[m.end():]); commit("planted: one test function deleted")
r = gate("test-vacuity"); line("w3", r[0] is False and LOCK + "::test_gradient_flow_relation" in r[1], "one test function deleted from a real lock: %s" % r[1][:150])

reset(); t = read(LOCK); name, at = first_test(t); moved = LOCK.replace(".py", "_moved.py")
sh(["git", "-C", clone, "mv", LOCK, moved])
write(moved, t[:t.index("def " + name)] + "import pytest as _planted\n\n\n@_planted.mark.skip(reason='planted')\n" + t[t.index("def " + name):]); commit("planted: a lock moved, and one of its tests marked")
r = gate("test-vacuity"); line("w4", r[0] is False and name in r[1], "a lock moved to another name with one test marked: %s" % r[1][:150])

reset(); t = read(LOCK); name, at = first_test(t)
write(LOCK, t[:t.index("def " + name)] + "def _only_here():\n    import pytest\n    pytest.skip('planted')\n\n\n" + t[t.index("def " + name):at] + "    _only_here()\n" + t[at:])
commit("planted: a helper that skips, called by a test")
r = gate("test-vacuity"); line("w5", r[0] is True, "a function of the lock's file decides the skip: the gate passes (a limit) -- %s" % r[1][:60])

reset(); t = read(LOCK); m = re.search(r"^def (test_gradient_flow_relation)\([^)]*\):\n.*?(?=^def )", t, re.M | re.S)
write(LOCK, t[:m.start()] + "def test_gradient_flow_relation():\n    assert sp is not None\n\n\n" + t[m.end():]); commit("planted: a test's body rewritten")
r = gate("test-vacuity"); line("w6", r[0] is True, "a test's body rewritten to assert something else: the gate passes (a limit) -- %s" % r[1][:60])

# ---- the old lines of the member-scope gate
def negative(folder, claim):
    write("frontier/%s/arc_verdict.json" % folder, json.dumps({"id": folder.split("_")[0], "verdict": "NEGATIVE", "depends_on": [], "claim_one_line": claim}, indent=1) + "\n")

reset(); negative("B9010_a_planted_negative", "PLANTED: on one thread it is impossible on the object to carry a third generation."); commit("planted: another of the gate's phrases")
r = gate("member-scope"); line("w7", r[0] is False and "B9010_a_planted_negative" in r[1], "a new NEGATIVE in another of the gate's phrases: %s" % r[1][:150])

reset(); sh(["git", "-C", clone, "mv", "frontier/B429_bosonic_rigidity", "frontier/B429_bosonic_rigidity_renamed"]); commit("planted: an old arc's folder renamed")
r = gate("member-scope"); line("w8", r[0] is False and "B429_bosonic_rigidity_renamed" in r[1], "an old arc's folder renamed, its line as it was: %s" % r[1][:150])

reset(); negative("B9010_a_planted_negative", "PLANTED: on one thread the manifold admits no third generation."); commit("planted: a negative that avoids every phrase")
r = gate("member-scope"); line("w9", r[0] is True, "a new NEGATIVE about one thread that avoids every phrase: the gate passes (a limit) -- %s" % r[1][:70])

# ---- a lock's own paths
LOG = "frontier/B1671_the_dedekind_phase_verified/verification/my_verify4.log"
reset(); sh(["git", "-C", clone, "rm", "-q", "--cached", LOG]); commit("planted: one of B1671's logs taken out of the commit")
on_disk = os.path.isfile(path(LOG))
r = gate("tracked-deps"); line("w10", on_disk and r[0] is False and "my_verify4.log" in r[1], "B1671's lock as it is, one log out of the commit and on disk: %s" % r[1][:170])
os.remove(path(LOG))
r = gate("tracked-deps"); line("w11", r[0] is False and "my_verify4.log" in r[1] and "git ignores this path" in r[1], "the same, the log gone from disk: %s" % r[1][:200])

D = "frontier/B9011_a_planted_arc/verification/"
HERE = "import pathlib\nHERE = pathlib.Path(__file__).resolve().parent\n\n\n"
def lock(body, extra=None):
    reset(); write(D + "test_b9011_a_planted_arc.py", body)
    for rel, text in (extra or {}).items(): write(rel, text)
    commit("planted: a lock")

lock(HERE + 'def test_it():\n    assert (HERE / "audit" / "notes.txt").read_text()\n')
r = gate("tracked-deps"); line("w12", r[0] is False and "audit/notes.txt" in r[1], "a file inside a folder that .gitignore names: %s" % r[1][:170])

lock(HERE + 'def test_it():\n    assert (HERE.parent / "verification" / "run.log").read_text()\n')
r = gate("tracked-deps"); line("w13", r[0] is False and "run.log" in r[1], "up from the folder and down again to an ignored file: %s" % r[1][:170])

lock(HERE + 'class TestIt:\n    V = HERE / "runs"\n\n    def test_it(self):\n        assert (self.V / "run.log").read_text()\n')
r = gate("tracked-deps"); line("w14", r[0] is True, "the folder kept in an attribute of a class: the gate passes (a limit)")

lock(HERE + 'def test_it():\n    k = 3\n    assert not (HERE / f"run_{k}.log").exists()\n')
r = gate("tracked-deps")
count = lambda s: int(re.search(r"(\d+) more have a part that is computed", s).group(1))
line("w15", r[0] is True and count(r[1]) == count(clean_deps) + 1, "the file's name built with an f-string: the gate passes, and counts %d with a computed part where it counted %d" % (count(r[1]), count(clean_deps)))

# ---- a float that a process printed, compared as text
HELD = "tests/test_b610_m136_weld.py"
reset(); write(HELD, read(HELD) + "\n\ndef test_a_planted_second_test():\n    import subprocess, sys\n"
               "    out = subprocess.run([sys.executable, '-c', 'print(1 / 3)'], capture_output=True, text=True).stdout\n    assert '0.3333333333333333' in out\n")
commit("planted: a new test in a lock that holds a named one")
r = gate("test-vacuity"); line("w16", r[0] is False and HELD + "::test_a_planted_second_test" in r[1], "a new test beside a named one, pinning a printed float: %s" % r[1][:170])

lock("import os, pathlib\nHERE = pathlib.Path(__file__).resolve().parent\n\n\ndef test_it():\n    out = os.popen('python3 ' + str(HERE / 'third.py')).read()\n"
     "    assert 'one third = 0.33333333333333331' in out\n", {D + "third.py": "print('one third = %.17f' % (1 / 3))\n"})
r = gate("test-vacuity"); line("w17", r[0] is False and "test_b9011_a_planted_arc.py::test_it" in r[1], "what os.popen gave, compared with a literal: %s" % r[1][:150])

reset(); t = read(HELD); pin = '    assert "     5   -0.500000000   +0.866025404" in out'
assert t.count(pin) == 1
write(HELD, t.replace(pin, pin + '\n    assert "+0.866025404" in out')); commit("planted: a second pin in a named test")
r = gate("test-vacuity"); line("w18", r[0] is True, "a second pin in one of the fourteen named tests: the gate passes (a limit)")

lock("def test_it():\n    assert '%.17f' % (1 / 3) == '0.33333333333333331'\n")
r = gate("test-vacuity"); line("w19", r[0] is True, "the float formatted inside the lock's own process: the gate passes (a limit)")

lock("import runner_beside_the_lock\n\n\ndef test_it():\n    assert 'one third = 0.33333333333333331' in runner_beside_the_lock.printed()\n",
     {D + "runner_beside_the_lock.py": "import pathlib, subprocess, sys\n\n\ndef printed():\n    return subprocess.run([sys.executable, str(pathlib.Path(__file__).with_name('third.py'))], capture_output=True, text=True).stdout\n",
      D + "third.py": "print('one third = %.17f' % (1 / 3))\n"})
r = gate("test-vacuity"); line("w20", r[0] is True, "the process started in a module beside the lock: the gate passes (a limit)")

# ---- a test run and the tracked files
WRITES = "import pathlib\nROOT = pathlib.Path(__file__).resolve().parents[%d]\n\n\ndef test_it(tmp_path):\n%s"
changed = lambda: sh(["git", "-C", clone, "status", "--porcelain", "--untracked-files=no"]).stdout.split()

reset(); P = "frontier/B9012_a_planted_arc/verification/test_b9012_a_planted_arc.py"
write(P, WRITES % (3, "    (ROOT / 'CHANGELOG.md').write_text('written by a test\\n')\n    assert (ROOT / 'CHANGELOG.md').read_text()\n")); commit("planted: an arc's own lock that rewrites a tracked file")
rc, out = tests(P)
line("w21", rc != 0 and "1 passed" in out and "CHANGELOG.md" in out and "CHANGELOG.md" in changed(), "an arc's own lock, run alone, rewrites CHANGELOG.md: the run ends with status %d and %s the file" % (rc, "names" if "CHANGELOG.md" in out else "DOES NOT NAME"))

reset(); rc, out = tests("tests/test_b1464_aged_items.py")
said = [l for l in out.splitlines() if "held by name as found" in l]
line("w22", rc == 0 and len(said) == 1 and "seal_census.json" in said[0] and any("seal_census.json" in c for c in changed()),
     "main's test that rewrites the census, run alone: the run ends with status %d and says: %s" % (rc, (said[0][:150] if said else "NOTHING of it; " + out.strip().splitlines()[-1][:100])))

reset(); write("tests/test_zz_planted_mode.py", WRITES % (1, "    import os\n    os.chmod(ROOT / 'CHANGELOG.md', 0o755)\n    assert os.access(ROOT / 'CHANGELOG.md', os.X_OK)\n")); commit("planted: a test that changes a mode")
rc, out = tests("tests/test_zz_planted_mode.py")
line("w23", rc != 0 and "CHANGELOG.md" in out, "a test changes the mode of a tracked file: the run ends with status %d and %s the file" % (rc, "names" if "CHANGELOG.md" in out else "DOES NOT NAME"))

reset(); write("tests/test_zz_planted_writes.py", WRITES % (1, "    (ROOT / 'CHANGELOG.md').write_text('written by a test\\n')\n    assert (ROOT / 'CHANGELOG.md').read_text()\n")); commit("planted: a test that rewrites a tracked file")
rc, out = tests("-n", "2", "tests/test_zz_planted_writes.py", "tests/test_claims_baseline.py" if os.path.isfile(path("tests/test_claims_baseline.py")) else LOCK)
line("w24", rc != 0 and out.count("CHANGED 1 TRACKED FILE(S)") == 1, "a parallel run in which one test rewrites CHANGELOG.md: status %d; the run says so %d time(s)" % (rc, out.count("CHANGED 1 TRACKED FILE(S)")))

reset(); write("tests/test_zz_planted_new_file.py", WRITES % (1, "    (ROOT / 'a_new_file_left_by_a_test.txt').write_text('left by a test\\n')\n    assert (ROOT / 'a_new_file_left_by_a_test.txt').is_file()\n")); commit("planted: a test that leaves a new file")
rc, out = tests("tests/test_zz_planted_new_file.py")
line("w25", rc == 0 and os.path.isfile(path("a_new_file_left_by_a_test.txt")), "a test leaves a new file that is not tracked: the run ends with status %d (a limit)" % rc)

reset()
print("\n%d of %d expectations hold" % (sum(results), len(results)))
