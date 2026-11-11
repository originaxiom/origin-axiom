#!/usr/bin/env python3
"""WP-0.7, series 1: this seat's own variants on its own mends, before the series is sent.

Series 1 mends the three planted cases in which a gate was not a function of the commit: PV9 (an export), PV22 (a
shallow clone), PV15 (the wall clock), and adds one rule of the seat's own (a commit dated before its parent).  Main
verifies the series with cases this seat has not seen.  These are cases this seat had not run either when it wrote the
mends: each is another shape of the same violation.

    python3 variants_series_1.py --src CLONE --work DIR      (CLONE: a clone holding the series at its HEAD)

Nothing is written into CLONE.  DIR is emptied and used for scratch trees.

EXPECTATIONS, written before the first run.  "Passes" below means a gate of the table READS_GIT returning ok.

  no git (the mend of PV9): in each tree, NO gate of READS_GIT passes
    e1  the tree copied with its .git folder left out
    e2  the export unpacked inside another repository
    e3  the clone itself, with git taken off the PATH
    e4  the copy of e1 with an empty .git folder put in
    e5  the copy of e1 with a .git FILE that points at a repository that is not there

  a cut history (the mend of PV22): in each clone, EVERY gate of READS_HISTORY is refused and says shallow, and no gate of
  READS_TRACKED is refused
    s1  depth 1
    s2  depth 500
    s3  cut by date (--shallow-since 2026-11-01)
    s4  a full clone, then cut to depth 5 by a fetch

  the day (the mends of PV15 and the seat's own rule): on a full clone
    d1  the four seams set to a word that is no date: the four debt gates answer as they do with no seam set
    d2  one more commit, dated sixty days back: the four debt gates are refused, naming it
    d3  after d2, one more commit dated rightly: still refused, naming the commit of d2
    d4  (no expectation; a read-out) one more commit on a fresh clone, dated sixty days ON: what the four gates then say
"""
import sys, os, json, shutil, subprocess, datetime

src = os.path.abspath(sys.argv[sys.argv.index("--src") + 1])
work = os.path.abspath(sys.argv[sys.argv.index("--work") + 1])
HERE = os.path.dirname(os.path.abspath(__file__))
RUN = r'''
import sys, os, json, importlib.util
root = os.path.abspath(sys.argv[1]); only = sys.argv[2].split(",")
spec = importlib.util.spec_from_file_location("gates_under_variants", os.path.join(root, "scripts", "gates", "gates.py"))
g = importlib.util.module_from_spec(spec); sys.dont_write_bytecode = True; spec.loader.exec_module(g)
names = {"GIT": sorted(g.READS_GIT), "HISTORY": sorted(g.READS_HISTORY), "TRACKED": sorted(g.READS_TRACKED)}
out = {}
for name in (names.get(only[0]) or only):
    try: r = g.GATES[name](); out[name] = [bool(r[0]), str(r[1])[:200]]
    except Exception as e: out[name] = [None, "RAISED %s: %s" % (type(e).__name__, str(e)[:150])]
print(json.dumps({"names": names, "out": out}))
'''


def sh(args, cwd=None, env=None, check=True, inp=None):
    r = subprocess.run(args, cwd=cwd, env=env, capture_output=True, input=inp)
    if check and r.returncode != 0: sys.exit("failed: %s\n%s" % (" ".join(map(str, args))[:200], r.stderr.decode("utf-8", "replace")[:400]))
    return r


def gates(tree, which, env=None):
    e = dict(os.environ, PYTHONDONTWRITEBYTECODE="1"); e.update(env or {})
    r = subprocess.run([sys.executable, "-B", "-c", RUN, tree, which], capture_output=True, text=True, env=e, cwd=tree)
    try: return json.loads(r.stdout.strip().split("\n")[-1])
    except Exception: sys.exit("the gates did not run in %s: %s" % (tree, (r.stdout + r.stderr)[-400:]))


def line(tag, ok, text): print("%-3s %-9s %s" % (tag, "HOLDS" if ok else "FAILS", text)); return ok


if os.path.exists(work): shutil.rmtree(work)
os.makedirs(work)
tip = sh(["git", "-C", src, "rev-parse", "--short=9", "HEAD"]).stdout.decode().strip()
print("variants on the series at %s" % tip)
results = []

# ---- no git
tar = sh(["git", "-C", src, "archive", "HEAD"]).stdout
copy = os.path.join(work, "copy"); os.makedirs(copy); sh(["tar", "-x", "-C", copy], inp=tar)


def no_git(tag, what, tree, env=None):
    d = gates(tree, "GIT", env)
    passing = sorted(n for n, r in d["out"].items() if r[0])
    refused = sum(1 for r in d["out"].values() if r[0] is False and "refused" in r[1])
    results.append(line(tag, not passing, "%s: %d gates of READS_GIT, %d refused in plain words, %d pass%s" % (
        what, len(d["out"]), refused, len(passing), (" (" + ", ".join(passing) + ")") if passing else "")))


no_git("e1", "the tree copied without its .git", copy)
outer = os.path.join(work, "outer"); os.makedirs(os.path.join(outer, "inside"))
sh(["git", "init", "-q", outer]); sh(["tar", "-x", "-C", os.path.join(outer, "inside")], inp=tar)
sh(["git", "-C", outer, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "add", "-A"])
sh(["git", "-C", outer, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-q", "-m", "an outer repository that tracks the export"])
no_git("e2", "the export inside another repository that tracks it", os.path.join(outer, "inside"))
shutil.rmtree(outer)
full = os.path.join(work, "full"); sh(["git", "clone", "-q", "file://" + src, full])
nogit_path = os.path.join(work, "bin_without_git"); os.makedirs(nogit_path)
no_git("e3", "a clone, with git off the PATH", full, {"PATH": nogit_path})
os.makedirs(os.path.join(copy, ".git"))
no_git("e4", "the copy with an empty .git folder", copy)
shutil.rmtree(os.path.join(copy, ".git")); open(os.path.join(copy, ".git"), "w").write("gitdir: /no/such/repository\n")
no_git("e5", "the copy with a .git file pointing nowhere", copy)
shutil.rmtree(copy)

# ---- a cut history
base_tracked = gates(full, "TRACKED")["out"]


def cut(tag, what, tree):
    h, t = gates(tree, "HISTORY")["out"], gates(tree, "TRACKED")["out"]
    not_refused = sorted(n for n, r in h.items() if not (r[0] is False and "refused" in r[1] and "shallow" in r[1]))
    wrongly = sorted(n for n, r in t.items() if "refused" in r[1])
    results.append(line(tag, not not_refused and not wrongly, "%s: %d of %d history gates refused as shallow%s; %d of %d tracked-file gates refused%s" % (
        what, len(h) - len(not_refused), len(h), (" (not: " + ", ".join(not_refused) + ")") if not_refused else "", len(wrongly), len(t),
        (" (" + ", ".join(wrongly) + ")") if wrongly else "")))


for tag, what, extra in (("s1", "depth 1", ["--depth", "1"]), ("s2", "depth 500", ["--depth", "500"]), ("s3", "cut by date", ["--shallow-since", "2026-11-01"])):
    d = os.path.join(work, tag); sh(["git", "clone", "-q", *extra, "file://" + src, d]); cut(tag, what, d); shutil.rmtree(d)
d = os.path.join(work, "s4"); sh(["git", "clone", "-q", "file://" + src, d]); sh(["git", "-C", d, "fetch", "-q", "--depth", "5", "origin"]); cut("s4", "a full clone cut to depth 5 by a fetch", d); shutil.rmtree(d)

# ---- the day
DATED = ["lead-debt", "point-debt", "relay-debt", "harvest-debt"]
SEAMS = {"OA_LEAD_TODAY": "tomorrow", "OA_POINT_TODAY": "tomorrow", "OA_RELAY_TODAY": "tomorrow", "OA_HARVEST_TODAY": "tomorrow"}
plain = gates(full, ",".join(DATED))["out"]; seamed = gates(full, ",".join(DATED), SEAMS)["out"]
results.append(line("d1", plain == seamed, "the four seams set to a word that is no date: %d of 4 gates answer as with no seam" % sum(plain[n] == seamed[n] for n in DATED)))
now = int(sh(["git", "-C", full, "log", "-1", "--format=%ct", "HEAD"]).stdout.decode().strip())


def commit(tree, when, text):
    with open(os.path.join(tree, "docs", "planted_variant.txt"), "a") as fh: fh.write(text + "\n")
    e = dict(os.environ, GIT_COMMITTER_DATE="%d +0000" % when, GIT_AUTHOR_DATE="%d +0000" % when)
    sh(["git", "-C", tree, "add", "docs/planted_variant.txt"])
    sh(["git", "-C", tree, "-c", "user.name=originaxiom", "-c", "user.email=planted@example.invalid", "commit", "-q", "-m", text], env=e)
    return sh(["git", "-C", tree, "rev-parse", "--short=9", "HEAD"]).stdout.decode().strip()


back = commit(full, now - 60 * 86400, "a planted commit, dated sixty days back")
r = gates(full, ",".join(DATED))["out"]
results.append(line("d2", all(r[n][0] is False and back in r[n][1] for n in DATED), "a commit dated sixty days back (%s): %d of 4 debt gates refused, naming it" % (back, sum(r[n][0] is False and back in r[n][1] for n in DATED))))
commit(full, now + 3600, "a planted commit, dated rightly, on top")
r = gates(full, ",".join(DATED))["out"]
results.append(line("d3", all(r[n][0] is False and back in r[n][1] for n in DATED), "a rightly dated commit on top: %d of 4 still refused, naming %s" % (sum(r[n][0] is False and back in r[n][1] for n in DATED), back)))
shutil.rmtree(full)
ahead = os.path.join(work, "ahead"); sh(["git", "clone", "-q", "file://" + src, ahead])
commit(ahead, now + 60 * 86400, "a planted commit, dated sixty days on")
r = gates(ahead, ",".join(DATED))["out"]
print("d4  read-out  a commit dated sixty days on: " + "; ".join("%s %s" % (n, "passes" if r[n][0] else "fails (" + r[n][1][:70] + ")") for n in DATED))
shutil.rmtree(ahead)
print()
print("expectations that hold: %d of %d" % (sum(results), len(results)))
