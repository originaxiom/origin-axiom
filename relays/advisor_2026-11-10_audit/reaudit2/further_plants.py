#!/usr/bin/env python3
"""Re-audit 2: further planted violations against main's rewritten append-only gate and its new seal gates.
Each case is planted in a scratch clone of main, committed there, the named gates are run from that clone, and the
clone is reset. Usage: plants.py CLONE_DIR"""
import sys, os, re, json, glob, subprocess, importlib.util
C = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("pv", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "planted_violations.py"))
pv = importlib.util.module_from_spec(spec); spec.loader.exec_module(pv)
sh, read, write, run_gates, WHO = pv.sh, pv.read, pv.write, pv.run_gates, pv.WHO
base = sh(["git", "rev-parse", "HEAD"], C).stdout.strip()
def reset():
    sh(["git", "checkout", "-q", "--detach", base], C); sh(["git", "reset", "-q", "--hard", base], C); sh(["git", "clean", "-fdq"], C)
def commit(msg="a planted violation"):
    sh(["git", "add", "-A"], C); r = sh(["git"] + WHO + ["commit", "-q", "-m", msg], C)
    return sh(["git", "rev-parse", "HEAD"], C).stdout.strip()
def show(tag, what, gates, expect):
    res = run_gates(C, gates)
    caught = [g for g, r in res.items() if r[0] is False]
    print("%-4s %-11s %s" % (tag, "CAUGHT" if caught else "NOT CAUGHT", what))
    for g, r in res.items(): print("       %-22s %-5s %s" % (g, "FAIL" if r[0] is False else "PASS", r[1][:150]))
    print("       expected by the seat before running: %s" % expect)
SEAL = ["seal-immutable", "seal-digests", "seal-ledger-current", "seal-provenance", "seal-order-unshown"]
# ---------------- G1
reset(); arch = sorted(glob.glob(os.path.join(C, "docs/progress/*.md")))[0]; rel = os.path.relpath(arch, C)
L = read(C, rel).splitlines(True); L[len(L)//2] = "THIS LINE OF THE ARCHIVE WAS REWRITTEN AFTER THE FACT.\n"; write(C, rel, "".join(L)); commit()
show("a1", "rewrite one line inside an archive of the log (%s), commit" % rel, ["append-only"], "not caught")
reset(); L = read(C, "PROGRESS_LOG.md").splitlines(True); write(C, "PROGRESS_LOG.md", "".join(L[:199] + L[400:])); bad = commit()
g = read(C, "scripts/gates/gates.py"); g = g.replace("APPEND_ONLY_WAIVED = {}", 'APPEND_ONLY_WAIVED = {"%s": "waived"}' % bad, 1); write(C, "scripts/gates/gates.py", g); commit("waive it")
show("a2", "delete 200 lines of the log, then in the next commit add that commit to the gate's own waiver list", ["append-only"], "not caught, and the passing message does not mention the waiver")
reset(); sh(["git", "checkout", "-q", "-b", "side"], C); L = read(C, "PROGRESS_LOG.md").splitlines(True); write(C, "PROGRESS_LOG.md", "".join(L[:199] + L[400:])); commit("on a side branch")
sh(["git", "checkout", "-q", "--detach", base], C); write(C, "docs/zz_note.txt", "main moves on\n"); commit("main moves on")
sh(["git"] + WHO + ["merge", "-q", "--no-ff", "-m", "merge the side branch", "side"], C)
show("a4", "the deletion made on a side branch and merged into the first-parent line", ["append-only"], "caught")
sh(["git", "branch", "-D", "side"], C)
# ---------------- G2
reset(); arc = glob.glob(os.path.join(C, "frontier/B1841_*"))[0]; arel = os.path.relpath(arc, C)
hashed = [l.split()[-1] for l in read(C, arel + "/ARTIFACT_HASHES.txt").splitlines() if re.match(r"^[0-9a-f]{64}\s", l)]
target = next((h for h in hashed if h.endswith(".py")), None)
print("\n(B1841's ARTIFACT_HASHES.txt lists %d files; the instrument planted on: %s)" % (len(hashed), target))
tp = target if target.startswith("frontier/") else arel + "/" + target.lstrip("./")
write(C, tp, read(C, tp) + "\n# a line added to a sealed instrument after the seal\n"); commit()
show("s1", "edit a script that the candidate's seal hashed (%s), commit" % os.path.basename(tp), SEAL, "not caught")
reset(); write(C, arel + "/PRE_RUN_NOTE.md", read(C, arel + "/PRE_RUN_NOTE.md") + "\nThe joint rule is changed here, after the look.\n"); commit()
show("s2", "edit the candidate's PRE_RUN_NOTE.md, which holds the rule its two looks are read by, commit", SEAL, "not caught")
reset(); deep = "frontier/B1296_the_charge_locus_parity_lock/verification/DESIGN.md"
write(C, deep, read(C, deep) + "\nA sentence added to a sealed design kept one folder down.\n"); commit()
show("s3", "edit a sealed-style file one folder below its arc's top level (%s), commit" % deep, SEAL, "not caught")
reset(); d = "frontier/B9002_planted_rule_after_record/"
v = json.loads(read(C, os.path.relpath(glob.glob(os.path.join(C, "frontier/B1857_*/arc_verdict.json"))[0], C))); v.update(id="B9002", depends_on=[], claim_one_line="PLANTED: the record first, the rule afterwards.")
write(C, d + "FINDINGS.md", "# FINDINGS\nThe result. Sweep: literature and repo, none.\n"); write(C, d + "arc_verdict.json", json.dumps(v, indent=1)); commit("the record")
write(C, d + "PREREGISTRATION.md", "# PREREGISTRATION\nThe criterion, written after the result was committed.\n"); commit("the rule, afterwards")
show("s4", "a new arc whose results are committed first and whose PREREGISTRATION.md is committed afterwards", ["seal-order-unshown", "seal-immutable"], "not caught")
reset(); rel = arel + "/PREREGISTRATION.md"; write(C, rel, read(C, rel) + "\nP9 (added after the seal): pass.\n"); bad = commit()
g = read(C, "scripts/gates/gates.py"); g = g.replace("SEAL_IMMUTABLE_WAIVED = {}", 'SEAL_IMMUTABLE_WAIVED = {("%s", "%s"): "waived"}' % (bad, rel), 1); write(C, "scripts/gates/gates.py", g); commit("waive it")
show("s5", "append a criterion to the candidate's sealed file, then in the next commit add a waiver for it to the gate's own list", ["seal-immutable"], "not caught, and the passing message does not mention the waiver")
# ---------------- PV25 again, three ways
reset(); vd = glob.glob(os.path.join(C, "frontier/B1857_*/verification"))[0]; vrel = os.path.relpath(vd, C)
write(C, vrel + "/test_b1857_planted_a.py", 'from pathlib import Path\nHERE = Path(__file__).parent\ndef test_a():\n    assert "ok" in (HERE / "driver_k1.log").read_text()\n'); commit()
show("p1", "a lock that reads HERE / 'driver_k1.log', a file git ignores", ["tracked-deps"], "caught (main says this form is now refused)")
reset(); write(C, vrel + "/test_b1857_planted_b.py", 'from pathlib import Path\nHERE = Path(__file__).parent\nRUNS = HERE / "runs"\ndef test_b():\n    name = "driver_k1" + ".log"\n    assert "ok" in (RUNS / name).read_text()\n'); commit()
show("p2", "the same, with the ignored name built in two steps", ["tracked-deps"], "not caught")
reset(); write(C, vrel + "/test_b1857_planted_c.py", 'import glob, os\nHERE = os.path.dirname(__file__)\ndef test_c():\n    logs = glob.glob(os.path.join(HERE, "*.log"))\n    assert all("ok" in open(f).read() for f in logs)\n'); commit()
show("p3", "a lock that reads every *.log beside it by a glob (and passes when there is none)", ["tracked-deps", "test-vacuity"], "not caught")
reset(); print("\nclone reset to", sh(["git", "rev-parse", "--short", "HEAD"], C).stdout.strip(), "| clean:", sh(["git", "status", "--short"], C).stdout.strip() == "")
