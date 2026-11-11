#!/usr/bin/env python3
"""Re-audit 3: planted violations against main's gate for the scripts a seal hashed (B1874), its mended waivers, and
the four refusals added to the programme's builder (B1873).

Each case is planted in a scratch clone of main, committed there, the gate or the builder is run from that clone on
the clean tree, and the clone is reset. The seat's expectation of each case is written here before the run.
    python3 -B plants.py CLONE_DIR"""
import sys, os, re, json, glob, subprocess, importlib.util, hashlib

C = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("pv", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "planted_violations.py"))
pv = importlib.util.module_from_spec(spec); spec.loader.exec_module(pv)
sh, read, write, WHO = pv.sh, pv.read, pv.write, pv.WHO
base = sh(["git", "rev-parse", "HEAD"], C).stdout.strip()
print("re-audit 3: plants at", base[:9], "\n")

def reset():
    sh(["git", "checkout", "-q", "--detach", base], C); sh(["git", "reset", "-q", "--hard", base], C); sh(["git", "clean", "-fdq"], C)
def commit(msg="a planted violation"):
    sh(["git", "add", "-A"], C); sh(["git"] + WHO + ["commit", "-q", "-m", msg], C)
    return sh(["git", "rev-parse", "HEAD"], C).stdout.strip()
def gate(name, cwd=None):
    code = ("import sys, json; sys.path.insert(0, 'scripts/gates'); import gates\n"
            "try:\n    r = gates.GATES[%r](); out = [bool(r[0]), str(r[1])]\n"
            "except Exception as exc:\n    out = [False, 'EXCEPTION ' + repr(exc)]\n"
            "print('@@' + json.dumps(out))\n" % name)
    r = sh([sys.executable, "-B", "-c", code], cwd or C)
    m = re.search(r"@@(\[.*\])", r.stdout)
    return json.loads(m.group(1)) if m else [None, "no output: " + (r.stderr or r.stdout)[-300:]]
def show(tag, what, gates_, expect, want_text=None):
    res = {g: gate(g) for g in gates_}
    caught = [g for g, r in res.items() if r[0] is False]
    print("%-4s %-11s %s" % (tag, "CAUGHT" if caught else "NOT CAUGHT", what))
    for g, r in res.items():
        print("       %-18s %-5s %s" % (g, "FAIL" if r[0] is False else "PASS", r[1][:230]))
        if want_text:
            for t in want_text: print("       the gate's sentence names %r: %s" % (t[:30], t in r[1]))
    print("       expected by the seat before running: %s" % expect)
    return res

AH = ["artifact-hashes"]
arc = glob.glob(os.path.join(C, "frontier/B1841_*"))[0]; arel = os.path.relpath(arc, C)
lst = arel + "/ARTIFACT_HASHES.txt"

# ---------------------------------------------------------------- the scripts a seal hashed
reset(); t = arel + "/verification/census.py"
write(C, t, read(C, t) + "\n# a line added to a sealed instrument after the seal\n"); commit()
show("t1", "the second re-audit's case again: one line added to the candidate's hashed census.py", AH, "caught")

reset(); write(C, t, read(C, t) + "\n# a line added to a sealed instrument after the seal\n")
new = hashlib.sha256(open(os.path.join(C, t), "rb").read()).hexdigest()
L = read(C, lst).splitlines(True); L = [(new + l[64:]) if l.rstrip().endswith("verification/census.py") and not l.startswith("#") and "frontier/" not in l else l for l in L]
write(C, lst, "".join(L)); commit()
show("t2", "the same, with the list rewritten to the new hash in the same commit", AH, "caught, by the list's history")

reset(); real = "frontier/B1838_the_end/verification/exact_end_web_seat.py"; orig = read(C, real)
for holder in (arel, os.path.relpath(glob.glob(os.path.join(C, "frontier/B1839_*"))[0], C)):
    write(C, holder + "/" + real, orig)                      # a copy with the sealed content, where the gate looks first
write(C, real, orig + "\n# the real instrument, changed after the seal; a copy with the old content stands where the gate looks first\n"); commit()
r3 = show("t3", "a decoy: copies of a hashed instrument (%s) placed beside the two lists that name it from the root, then the real file changed" % os.path.basename(real), AH + ["seal-immutable", "tracked-forbidden", "arc-data", "path-refs"],
          "NOT caught by any of the five: the gate looks for a name beside its list before it looks from the root, and takes the first it finds")

reset()
code = ("import sys, json; sys.path.insert(0, 'scripts/gates'); import gates\n"
        "st = gates.artifact_hash_state()\n"
        "print('@@' + json.dumps([[k, l, n, s] for (k, l, n, s) in st if s == 'MISMATCH' and k in gates.ARTIFACT_HASHES_BROKEN and str(n).endswith('.py')]))\n")
frozen = json.loads(re.search(r"@@(\[.*\])", sh([sys.executable, "-B", "-c", code], C).stdout).group(1))
print("\n(frozen entries that are scripts whose hash does not verify: %d; planting on: %s)" % (len(frozen), frozen[0][2] if frozen else None))
if frozen:
    fz = frozen[0][2]; write(C, fz, read(C, fz) + "\n# changed again, after the gate froze this entry as it was found\n"); commit()
    show("t4", "a script whose entry is one of the 63 frozen as found: changed again", AH, "NOT caught: the freeze is of a key, and a key does not hold the file's present content")

reset(); sh(["git", "rm", "-q", t], C); commit()
show("t5", "the candidate's hashed census.py deleted", AH, "caught")

reset(); write(C, t, read(C, t) + "\n# changed, and a second list written beside the first with the new hash\n")
new = hashlib.sha256(open(os.path.join(C, t), "rb").read()).hexdigest()
write(C, arel + "/ARTIFACT_HASHES_2.txt", "# an amendment nobody named in the gate\n%s  verification/census.py\n" % new); commit()
show("t6", "the script changed and a second list added beside the first, the old entry's key named nowhere", AH, "caught: the old entry no longer verifies")

reset(); d = "frontier/B9003_planted_seal_under_another_name/"
write(C, d + "verification/run.py", "print('the instrument as sealed')\n")
h = hashlib.sha256(open(os.path.join(C, d + "verification/run.py"), "rb").read()).hexdigest()
write(C, d + "SEAL_SHA256.txt", "%s  verification/run.py\n" % h); write(C, d + "PREREGISTRATION.md", "# PREREGISTRATION\nThe rule. The instrument's hash is in SEAL_SHA256.txt.\n"); commit("the seal")
write(C, d + "verification/run.py", "print('the instrument, changed after the seal')\n"); commit("the change")
show("t7", "a new arc whose list of hashed files is named SEAL_SHA256.txt; its instrument changed after the seal", AH + ["seal-immutable"], "NOT caught: the gate reads lists named ARTIFACT_HASHES*.txt only")

reset()
tracked = sh(["git", "ls-files"], C).stdout.split("\n")
other = []
for f in tracked:
    b = os.path.basename(f)
    if re.match(r"ARTIFACT_HASHES.*\.txt$", b) or not re.search(r"\.(txt|md|sha256|sums)$", b, re.I): continue
    if not re.search(r"sha|hash|seal|digest|checksum|manifest", b, re.I): continue
    try: s = read(C, f)
    except Exception: continue
    n = len(re.findall(r"(?m)^\s*[0-9a-f]{64}\s+\S+\.\w+", s))
    if n: other.append((f, n))
print("\n(tracked files that hold lines of the form '<sha256>  <file name>' under a name the gate does not read: %d files, %d lines)" % (len(other), sum(n for _, n in other)))
for f, n in sorted(other, key=lambda x: -x[1])[:8]: print("       %4d  %s" % (n, f))

d3 = os.path.join(os.path.dirname(C), "shallow3")
sh(["rm", "-rf", d3], os.path.dirname(C)); sh(["git", "clone", "-q", "--depth", "3", "file://" + C, d3], os.path.dirname(C)); sh(["git", "checkout", "-q", "--detach", base], d3)
r = gate("artifact-hashes", d3)
print("\nt9   %-11s the gate on a clone of depth 3 (the rule's first commit is not in it)" % ("CAUGHT" if r[0] is False else "NOT CAUGHT"))
print("       artifact-hashes    %-5s %s" % ("FAIL" if r[0] is False else "PASS", r[1][:200])); print("       expected by the seat before running: fails closed, and says why")
sh(["rm", "-rf", d3], os.path.dirname(C))

# ---------------------------------------------------------------- the mended waivers
reset(); L = read(C, "PROGRESS_LOG.md").splitlines(True); write(C, "PROGRESS_LOG.md", "".join(L[:199] + L[400:])); bad = commit()
g = read(C, "scripts/gates/gates.py"); assert "APPEND_ONLY_WAIVED = {}" in g
write(C, "scripts/gates/gates.py", g.replace("APPEND_ONLY_WAIVED = {}", 'APPEND_ONLY_WAIVED = {"%s": "a reason typed by whoever deleted the lines"}' % bad, 1)); commit("waive it")
show("w1", "200 lines of the log deleted, then waived by name in the next commit", ["append-only"], "passes, and now the gate's sentence names the commit and the reason", want_text=[bad[:9], "a reason typed"])
cli = sh([sys.executable, "-B", "scripts/gates/gates.py", "append-only"], C)
print("       the runner's own printed line names the waiver: %s | %s" % (bad[:9] in cli.stdout, [l for l in cli.stdout.splitlines() if "append-only" in l][:1]))

reset(); rel = arel + "/PREREGISTRATION.md"; write(C, rel, read(C, rel) + "\nP9 (added after the seal): pass.\n"); bad = commit()
g = read(C, "scripts/gates/gates.py"); assert "SEAL_IMMUTABLE_WAIVED = {}" in g
write(C, "scripts/gates/gates.py", g.replace("SEAL_IMMUTABLE_WAIVED = {}", 'SEAL_IMMUTABLE_WAIVED = {("%s", "%s"): "a reason typed by whoever edited the seal"}' % (bad, rel), 1)); commit("waive it")
show("w2", "a criterion appended to the candidate's sealed file, then waived by name in the next commit", ["seal-immutable"], "passes, and now the sentence names the commit, the file and the reason", want_text=[bad[:9], "a reason typed"])

# ---------------------------------------------------------------- the programme's builder
PS = "frontier/B1861_the_closure_programme/verification/programme_source.py"
BP = "frontier/B1861_the_closure_programme/verification/build_programme.py"
def build(tag, what, addition, expect):
    reset(); write(C, PS, read(C, PS) + "\n# a planted change\n" + addition + "\n"); commit()
    r = sh([sys.executable, "-B", BP], C)
    fails = [l.strip() for l in (r.stdout + r.stderr).splitlines() if re.search(r"REFUSED|refus|^\s*- |FAIL", l)][:4]
    print("%-4s %-11s %s" % (tag, "REFUSED" if r.returncode != 0 else "BUILT", what))
    for l in fails[:3]: print("       %s" % l[:230])
    print("       expected by the seat before running: %s" % expect)
print()
build("j1", "a finding's 'bears on' line removed (E3)", 'del BEARS_ON["E3"]', "refused (rule 16)")
build("j2", "a package marked started under a need that has not started (WP-2.3 under WP-2.1)", '[w for w in WP if w["id"] == "WP-2.3"][0]["status"] = "STARTED"', "refused (rule 18)")
build("j3", "a finding the re-audit did not accept marked FIXED (E3)", 'FINDINGS["E3"]["state"] = "FIXED"', "refused (rule 19)")
build("j4", "the same, with the re-audit's verdict retyped as 'accepted' in main's own file", 'FINDINGS["E3"]["state"] = "FIXED"\nACCEPTED["E3"] = "accepted"',
      "BUILT: the verdict is main's transcription, and nothing checks it against the seat's file")
build("j5", "the sealed card made not to wait on the suite (WP-0.5 dropped from every need of the card)",
      'for _w in WP:\n    if _w["id"] in ("WP-5.3", "WP-5.2", "WP-5.1"):\n        _w["needs"] = [n for n in _w["needs"] if n not in ("WP-0.5", "@C0")]', "refused (rule 17)")
reset(); print("\nclone reset to", sh(["git", "rev-parse", "--short", "HEAD"], C).stdout.strip(), "| clean:", sh(["git", "status", "--short"], C).stdout.strip() == "")
