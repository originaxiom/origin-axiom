#!/usr/bin/env python3
"""WP-0.7, series 2: this seat's own variants on its own mends, before the series is sent.

Series 2 mends the five planted cases in which something deleted or emptied still passed, or a ceiling rose in the commit
it was meant to stop (PV10, PV11, PV12, PV13, PV19), by one rule read from history: nothing leaves a ledger, and no
ceiling rises, without a recorded act.  Main verifies with cases this seat has not seen.  These are other shapes of the
same violations, run on the real pages in a scratch clone, where the series' own lock uses small pages of its own.

    python3 variants_series_2.py --src CLONE --work DIR      (CLONE: a clone holding the series at its HEAD)

Nothing is written into CLONE.  DIR is emptied and used for the scratch clone.

EXPECTATIONS, written before the first run.  "red" = the named gate returns False.
  the registry of retracted phrases
    t1   every second phrase row removed                                        retraction-sweep red, and it says how many left
    t2   the registry replaced by an empty file                                 retraction-sweep red
  the law map and the chain
    t3   ten rows cut from the middle of the law map                            law-map-provenance red: 10 laws left
    t4   one link of the chain renumbered, C9 to C99                            chain-locks red, naming C9
    t5   a law cut in one commit and put back in the next                       law-map-provenance passes: it holds what it held
    t6   a law cut and named in LEFT_BY_NAME in the same commit                 law-map-provenance passes, its sentence says
                                                                                "left by name", and the runner prints it whole
  the identification baseline
    t7   one more unearned row and the count raised by one, no record           identification-register red: the baseline rose
    t8   the same, with the raise recorded in the file's own list               identification-register passes and says so
  the locks
    t9   one arc's own lock deleted                                             test-vacuity red, naming it
    t10  a lock in tests/ renamed with git mv                                   test-vacuity passes
  the attribution baseline
    t11  a new page holding one vendor token, and a new entry for it in the
         baseline, in one commit                                                attribution red: a ceiling rose
  what the rule does not bound, and what holds it
    t12  a law cut in one commit, and the anchor moved to that commit in the
         next: the GATE                                                         law-map-provenance PASSES (the hole)
    t13  the same: the LOCK that pins the anchor                                the lock FAILS (what holds it)
  a cut history
    t14  a clone of depth 1                                                     all six gates refused as shallow
"""
import sys, os, re, json, shutil, subprocess, base64

src = os.path.abspath(sys.argv[sys.argv.index("--src") + 1])
work = os.path.abspath(sys.argv[sys.argv.index("--work") + 1])
WHO = ["-c", "user.name=originaxiom", "-c", "user.email=planted@example.invalid"]
SIX = ["retraction-sweep", "law-map-provenance", "chain-locks", "identification-register", "test-vacuity", "attribution"]
RUN = r'''
import sys, json, importlib.util
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("gates_under_variants", "scripts/gates/gates.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
out = {}
for name in sys.argv[1].split(","):
    try:
        r = g.GATES[name](); d = r[1] if isinstance(r[1], str) else " | ".join(map(str, r[1]))
        out[name] = [bool(r[0]), d[:400], g.result_line(name, bool(r[0]), d).strip()[:400]]
    except Exception as e:
        out[name] = [None, "RAISED %s: %s" % (type(e).__name__, str(e)[:200]), ""]
print(json.dumps(out))
'''


def sh(args, cwd=None, check=True, env=None):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        sys.exit("failed: %s\n%s" % (" ".join(map(str, args))[:200], r.stderr[:400]))
    return r


def gates(tree, names):
    r = subprocess.run([sys.executable, "-B", "-c", RUN, ",".join(names)], cwd=tree, capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    try:
        return json.loads(r.stdout.strip().split("\n")[-1])
    except Exception:
        sys.exit("the gates did not run in %s: %s" % (tree, (r.stdout + r.stderr)[-400:]))


if os.path.exists(work):
    shutil.rmtree(work)
os.makedirs(work)
clone = os.path.join(work, "clone")
sh(["git", "clone", "-q", "file://" + src, clone])
tip = sh(["git", "-C", clone, "rev-parse", "HEAD"]).stdout.strip()
print("variants on the series at %s" % tip[:9])
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
    return sh(["git", "-C", clone, "rev-parse", "HEAD"]).stdout.strip()


results = []


def line(tag, ok, text):
    results.append(bool(ok)); print("%-4s %-6s %s" % (tag, "HOLDS" if ok else "FAILS", text), flush=True)


control = gates(clone, SIX)
assert all(v[0] for v in control.values()), "the six gates must be green before any variant: %s" % {k: v[1][:80] for k, v in control.items() if not v[0]}
print("control: the six gates pass on the series as it stands")

# ---- the registry
reset(); t = read("docs/RETRACTED_PHRASES.md").split("\n")
rows = [i for i, l in enumerate(t) if re.match(r'\|\s*(\d+\s*\|\s*`|["“])', l)]
cut = set(rows[::2]); write("docs/RETRACTED_PHRASES.md", "\n".join(l for i, l in enumerate(t) if i not in cut)); commit("planted: every second phrase row removed")
r = gates(clone, ["retraction-sweep"])["retraction-sweep"]
line("t1", r[0] is False and "retracted phrase(s) left" in r[1], "%d of %d phrase rows removed: %s" % (len(cut), len(rows), r[1][:110]))
reset(); write("docs/RETRACTED_PHRASES.md", ""); commit("planted: the registry emptied to nothing")
r = gates(clone, ["retraction-sweep"])["retraction-sweep"]
line("t2", r[0] is False, "the registry an empty file: %s" % r[1][:110])

# ---- the law map and the chain
reset(); t = read("docs/LAW_MAP.md").split("\n")
rows = [i for i, l in enumerate(t) if l.startswith("| **")]
cut = set(rows[len(rows) // 2: len(rows) // 2 + 10]); cut_law = t[rows[len(rows) // 2]]
write("docs/LAW_MAP.md", "\n".join(l for i, l in enumerate(t) if i not in cut)); commit("planted: ten laws cut from the middle")
r = gates(clone, ["law-map-provenance"])["law-map-provenance"]
line("t3", r[0] is False and "10 law(s) left" in r[1], "ten rows cut: %s" % r[1][:120])
reset(); c = read("docs/THEOREM_LEDGER.md"); assert c.count("**C9 [") == 1
write("docs/THEOREM_LEDGER.md", c.replace("**C9 [", "**C99 [")); commit("planted: a link renumbered")
r = gates(clone, ["chain-locks"])["chain-locks"]
line("t4", r[0] is False and re.search(r"\bC9\b", r[1]) is not None, "C9 renumbered C99: %s" % r[1][:120])
reset(); whole = read("docs/LAW_MAP.md"); one = [l for l in whole.split("\n") if l.startswith("| **")][3]
write("docs/LAW_MAP.md", whole.replace(one + "\n", "")); commit("planted: one law cut")
mid = gates(clone, ["law-map-provenance"])["law-map-provenance"]
write("docs/LAW_MAP.md", whole); commit("planted: and put back")
r = gates(clone, ["law-map-provenance"])["law-map-provenance"]
line("t5", mid[0] is False and r[0] is True, "a law cut (the gate then: %s) and put back (now: %s)" % ("red" if mid[0] is False else "passes", "passes" if r[0] else "red"))
reset(); title = re.search(r"\*\*(.+?)\*\*", one.split("|")[1]).group(1)
write("docs/LAW_MAP.md", whole.replace(one + "\n", ""))
gsrc = read("scripts/gates/gates.py"); assert gsrc.count("LEFT_BY_NAME = {}") == 1
write("scripts/gates/gates.py", gsrc.replace("LEFT_BY_NAME = {}", "LEFT_BY_NAME = {%r: {%r: %r}}" % ("docs/LAW_MAP.md", re.sub(r"\s+", " ", title).strip(), "2026-11-11 -- planted: merged into the row above")))
commit("planted: a law cut and named in the same commit")
r = gates(clone, ["law-map-provenance"])["law-map-provenance"]
line("t6", r[0] is True and "1 law(s) left by name" in r[1] and "left by name" in r[2] and r[2].startswith("PASS"), "cut and named: %s" % r[2][-150:])

# ---- the identification baseline
reset(); led = read("docs/IDENTIFICATION_LEDGER.md"); base = json.loads(read("docs/IDENTIFICATION_BASELINE.json"))
last = [l for l in led.split("\n") if re.match(r"\|\s*I-\d+\s*\|", l)][-1]
n = max(int(x) for x in re.findall(r"^\|\s*I-(\d+)\s*\|", led, re.M)) + 1
new_row = "| I-%d | planted | A | B | ✘ | ✘ | **UNEARNED** | planted | planted |" % n
write("docs/IDENTIFICATION_LEDGER.md", led.replace(last, last + "\n" + new_row))
b0 = base["unearned"]; base["unearned"] = b0 + 1
write("docs/IDENTIFICATION_BASELINE.json", json.dumps(base, indent=1, ensure_ascii=False) + "\n"); commit("planted: one more unearned row, and the count moved to fit it")
r = gates(clone, ["identification-register"])["identification-register"]
line("t7", r[0] is False and "the baseline rose %d -> %d" % (b0, b0 + 1) in r[1], "one row, the count raised, no record: %s" % r[1][:130])
base.setdefault("_baseline_raises", []).append({"date": "2026-11-11", "from": b0, "to": b0 + 1, "row": "I-%d" % n, "reason": "planted: registered unearned, with what would earn it"})
write("docs/IDENTIFICATION_BASELINE.json", json.dumps(base, indent=1, ensure_ascii=False) + "\n"); commit("planted: the raise recorded")
r = gates(clone, ["identification-register"])["identification-register"]
line("t8", r[0] is True and "raised 1 time(s) by name" in r[1], "the raise recorded in the file's own list: %s" % r[1][:130])

# ---- the locks
reset(); locks = sh(["git", "-C", clone, "ls-files", "--", ":(glob)frontier/**/test_*.py"]).stdout.split()
victim = locks[len(locks) // 2]; os.remove(path(victim)); commit("planted: an arc's own lock deleted")
r = gates(clone, ["test-vacuity"])["test-vacuity"]
line("t9", r[0] is False and victim in r[1], "one of %d arcs' own locks deleted: %s" % (len(locks), r[1][:150]))
reset(); mover = sh(["git", "-C", clone, "ls-files", "--", "tests/test_b9*.py"]).stdout.split()[0]
sh(["git", "-C", clone, "mv", mover, mover.replace(".py", "_renamed.py")]); commit("planted: a lock renamed")
r = gates(clone, ["test-vacuity"])["test-vacuity"]
line("t10", r[0] is True, "%s renamed: %s" % (mover, r[1][:90]))

# ---- the attribution baseline
reset(); token = base64.b64decode(b"Q2xhdWRl").decode()            # a vendor's name, not typed in this file
write("docs/PLANTED_PAGE.md", "# A planted page\n\nWritten with %s.\n" % token)
ab = json.loads(read("docs/ATTRIBUTION_BASELINE.json")); ab["frozen"]["docs/PLANTED_PAGE.md"] = 1
write("docs/ATTRIBUTION_BASELINE.json", json.dumps(ab, indent=1, ensure_ascii=False) + "\n"); commit("planted: a new page with a token, and a baseline entry for it")
r = gates(clone, ["attribution"])["attribution"]
line("t11", r[0] is False and "ceiling(s) in docs/ATTRIBUTION_BASELINE.json rose" in r[1] and "docs/PLANTED_PAGE.md 0 -> 1" in r[1], "a new page and its new entry: %s" % r[1][:150])

# ---- what the rule does not bound
reset(); write("docs/LAW_MAP.md", whole.replace(one + "\n", "")); x = commit("planted: one law cut")
gsrc = read("scripts/gates/gates.py"); old = re.search(r'NOTHING_LEAVES_FROM = "([0-9a-f]{40})"', gsrc).group(1)
write("scripts/gates/gates.py", gsrc.replace('NOTHING_LEAVES_FROM = "%s"' % old, 'NOTHING_LEAVES_FROM = "%s"' % x)); commit("planted: and the anchor moved to that commit")
r = gates(clone, ["law-map-provenance"])["law-map-provenance"]
line("t12", r[0] is True, "a law cut, then the anchor moved past the cut -- the gate: %s" % ("PASSES" if r[0] else "red: " + r[1][:100]))
lock = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests/test_nothing_leaves_a_ledger.py::test_the_rule_reads_main_from_its_anchor_and_nothing_is_named_yet"],
                      cwd=clone, capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
line("t13", lock.returncode != 0, "the same -- the lock that pins the anchor: %s" % ("FAILS" if lock.returncode != 0 else "passes"))

# ---- a cut history
shallow = os.path.join(work, "shallow"); sh(["git", "clone", "-q", "--depth", "1", "file://" + src, shallow])
r = gates(shallow, SIX)
refused = [k for k, v in r.items() if v[0] is False and "refused" in v[1] and "shallow" in v[1]]
line("t14", sorted(refused) == sorted(SIX), "a clone of depth 1: %d of 6 refused as shallow%s" % (len(refused), "" if len(refused) == 6 else " (not: %s)" % ", ".join(sorted(set(SIX) - set(refused)))))
shutil.rmtree(shallow); reset()
print()
print("expectations that hold: %d of %d" % (sum(results), len(results)))
