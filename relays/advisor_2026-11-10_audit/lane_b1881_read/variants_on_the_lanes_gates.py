#!/usr/bin/env python3
"""Variants of the seat's planted cases, written after reading the agy lane's branch (agy/stage4-sync-2026-11-11 at
b4ddb600b) and not published before it.  The lane's gates refuse the seat's published cases t3, t4, t7 and j4.  A gate
can be fitted to the cases it was shown, so each is tried here in a form the lane was not shown.

Each case is planted in a scratch clone at the lane's tip, committed there, the gate is run from that clone on the
clean tree, and the clone is reset.  The seat's expectation of each case is written here before the run.
    python3 -B variants_on_the_lanes_gates.py CLONE_AT_THE_LANES_TIP"""
import sys, os, re, json, hashlib, importlib.util

C = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("pv", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "planted_violations.py"))
pv = importlib.util.module_from_spec(spec); spec.loader.exec_module(pv)
sh, read, write, WHO = pv.sh, pv.read, pv.write, pv.WHO
base = sh(["git", "rev-parse", "HEAD"], C).stdout.strip()
print("variants on the lane's gates: plants at", base[:9], "\n")
GATES = ["artifact-hashes", "seal-immutable", "seal-digests", "seal-ledger-current"]


def reset():
    sh(["git", "checkout", "-q", "--detach", base], C); sh(["git", "reset", "-q", "--hard", base], C); sh(["git", "clean", "-fdq"], C)
def commit(msg="a planted violation"):
    sh(["git", "add", "-A"], C); sh(["git"] + WHO + ["commit", "-q", "-m", msg], C)
def gate(name):
    code = ("import sys, json; sys.path.insert(0, 'scripts/gates'); import gates\n"
            "try:\n    r = gates.GATES[%r](); out = [bool(r[0]), str(r[1])]\n"
            "except Exception as exc:\n    out = [False, 'EXCEPTION ' + repr(exc)]\n"
            "print('@@' + json.dumps(out))\n" % name)
    r = sh([sys.executable, "-B", "-c", code], C)
    m = re.search(r"@@(\[.*\])", r.stdout)
    return json.loads(m.group(1)) if m else [None, "no output: " + (r.stderr or r.stdout)[-300:]]
def show(tag, what, expect):
    res = {g: gate(g) for g in GATES}
    caught = [g for g, r in res.items() if r[0] is False]
    print("%-5s %-11s %s" % (tag, "CAUGHT" if caught else "NOT CAUGHT", what))
    for g in caught: print("        %-20s FAIL  %s" % (g, res[g][1][:230]))
    print("        expected by the seat before running: %s" % expect)
def sha(text): return hashlib.sha256(text.encode("utf-8")).hexdigest()
CODE = "THRESHOLD = 5\nprint('the count is at most', THRESHOLD)\n"
LOOSE = CODE.replace("THRESHOLD = 5", "THRESHOLD = 50")

reset()
for g in GATES:
    r = gate(g); print("clean tree: %-20s %-5s %s" % (g, "FAIL" if r[0] is False else "PASS", r[1][:150]))
print()

# ---- t4, in a form not shown: a frozen entry whose file is NOT a script, changed again
code = ("import sys, json; sys.path.insert(0, 'scripts/gates'); import gates\n"
        "st = gates.artifact_hash_state()\n"
        "print('@@' + json.dumps(sorted({n for (k, l, n, s) in st if k in gates.ARTIFACT_HASHES_BROKEN and s == 'MISMATCH' and not n.endswith('.py')})))\n")
frozen = json.loads(re.search(r"@@(\[.*\])", sh([sys.executable, "-B", "-c", code], C).stdout).group(1))
for kind in (".json", ".md"):
    f = next(x for x in frozen if x.endswith(kind))
    reset(); write(C, f, read(C, f) + "\n"); commit()
    show("t4b" if kind == ".json" else "t4c", "a frozen entry that is not a script (%s), changed again by one line" % f, "caught: the lane's table holds 41 entries, of every kind of file")

# ---- t7, in forms not shown: a list of hashed files under a name the lane's pattern does not know, and one outside its two folders
def seal_then_loosen(tag, arc, list_name, expect):
    reset()
    write(C, arc + "/verification/tool.py", CODE); write(C, arc + "/" + list_name, "# sealed before the run: sha256 of the instrument\n%s  verification/tool.py\n" % sha(CODE)); commit("a seal")
    write(C, arc + "/verification/tool.py", LOOSE); commit("the instrument loosened after the seal")
    show(tag, "a new arc (%s) whose list of hashed files is named %s; its instrument changed after the seal" % (arc, list_name), expect)
seal_then_loosen("t7a", "frontier/B9003_a_sealed_run", "SEAL_SHA256.txt", "caught: the seat's published case, as a control")
seal_then_loosen("t7b", "frontier/B9003_a_sealed_run", "MANIFEST.txt", "NOT caught: the lane recognises a list by its file name, and this name is not in its pattern")
seal_then_loosen("t7c", "frontier/B9003_a_sealed_run", "PINS.md", "NOT caught, for the same reason")
seal_then_loosen("t7d", "papers/P99_a_sealed_note", "SEAL_SHA256.txt", "NOT caught: the lane reads such lists under frontier/ and outside_bench/ only")

# ---- t3, in a form not shown: the decoy in the list's verification folder, for a name the list gives from the root
code = ("import sys, json, os; sys.path.insert(0, 'scripts/gates'); import gates\n"
        "st = gates.artifact_hash_state()\n"
        "c = [(l, n) for (k, l, n, s) in st if s == 'VERIFIES' and n.startswith('frontier/') and not n.startswith(os.path.dirname(l) + '/') and n.endswith('.py')]\n"
        "print('@@' + json.dumps(c[:1]))\n")
lst, name = json.loads(re.search(r"@@(\[.*\])", sh([sys.executable, "-B", "-c", code], C).stdout).group(1))[0]
reset(); sealed = read(C, name)
write(C, os.path.join(os.path.dirname(lst), "verification", name), sealed); write(C, name, sealed + "\n# changed after the seal\n"); commit()
show("t3b", "a decoy in the list's verification folder (%s names %s from the root), then the real file changed" % (lst, name), "caught: the lane reads a name that starts with frontier/ from the root, and refuses a second candidate")
reset(); print("\nclone reset to", sh(["git", "rev-parse", "--short", "HEAD"], C).stdout.strip(), "| clean:", sh(["git", "status", "--short"], C).stdout.strip() == "")
