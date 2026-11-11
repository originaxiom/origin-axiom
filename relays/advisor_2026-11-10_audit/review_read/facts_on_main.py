#!/usr/bin/env python3
"""The facts behind this seat's read of main's page on the periodic review (card C3), measured on a clone of main.

    python3 facts_on_main.py --repo CLONE        (CLONE: a clean checkout of main at the commit to be read)

It writes nothing in CLONE: what it plants, it plants in memory, by handing a gate another text to read.
Each block prints what was measured and the line of main's code it rests on.  Label, in the protocol's words:
computed once.
"""
import importlib.util, json, os, re, subprocess, sys

repo = os.path.abspath(sys.argv[sys.argv.index("--repo") + 1])


def git(*a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True).stdout


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(repo, rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


sys.dont_write_bytecode = True
g = load("gates_read", "scripts/gates/gates.py")
rt = load("review_tools_read", "scripts/review/review_tools.py")
head = git("rev-parse", "--short=9", "HEAD").strip()
anchor = rt.last_anchor()
print("main at %s; the last review's anchor: %s; dirty files in the clone: %d\n" % (head, anchor, len(git("status", "--porcelain").splitlines())))

# ---- F1: what the window's pool holds, and what it does not
ns = git("diff", "--name-status", "-M", anchor, "HEAD").splitlines()
arc = lambda p: re.match(r"frontier/(B\d{1,4})_[^/]*/arc_verdict\.json$", p)
num = lambda b: int(b[1:])
added = sorted({arc(l.split("\t")[-1]).group(1) for l in ns if l[0] == "A" and arc(l.split("\t")[-1])}, key=num)
changed = sorted({arc(l.split("\t")[-1]).group(1) for l in ns if l[0] == "M" and arc(l.split("\t")[-1])}, key=num)
flips = []
for l in ns:
    p = l.split("\t")[-1]
    if l[0] == "M" and arc(p):
        try:
            old, new = json.loads(git("show", "%s:%s" % (anchor, p))), json.load(open(os.path.join(repo, p), encoding="utf-8"))
            if old.get("verdict") != new.get("verdict"):
                flips.append("%s %s -> %s" % (arc(p).group(1), old.get("verdict"), new.get("verdict")))
        except Exception as exc:
            flips.append("%s (unreadable: %s)" % (arc(p).group(1), str(exc)[:40]))
fp = git("log", "--first-parent", "--format=%h", anchor + "..HEAD").split()
print("F1  the window %s..%s: %d commits on the first-parent line" % (anchor, head, len(fp)))
print("    arcs whose verdict file was ADDED (the review's pool; review_tools.py, gather: --diff-filter=A): %d  %s" % (len(added), " ".join(added)))
print("    arcs whose verdict file was CHANGED, and are not in the pool: %d  %s" % (len(changed), " ".join(changed)))
print("    of them, the verdict word itself changed: %s" % ("; ".join(flips) or "none"))

# ---- F2: the draw
n = max(5, len(added) // 6)
print("\nF2  the draw (review_tools.py, sample_draw(arcs, anchor, max(5, len(arcs) // 6))): %s" % " ".join(rt.sample_draw(added, anchor, n)))
print("    its seed is the last review's anchor, known since that review was banked; the pool is the arcs so far.")
more = "B%d" % (num(added[-1]) + 1) if added else "B1"
print("    with one more arc in the pool (%s): %s" % (more, " ".join(rt.sample_draw(added + [more], anchor, max(5, (len(added) + 1) // 6)))))

# ---- F3, F4: what else is in the window
touched = set(git("diff", "--name-only", anchor, "HEAD").split("\n"))
inst = sorted(p for p in touched if p.startswith(("scripts/gates/", "scripts/checks/", "scripts/review/", "scripts/hooks/", "scripts/seats/")) or p in ("GOVERNANCE.md", "WORKING_RULES.md"))
print("\nF3  instruments and governing pages changed in the window: %d\n    %s" % (len(inst), "  ".join(inst)))
light = 0
for h in fp:
    files = [f for f in git("show", "--name-only", "--format=", h).split("\n") if f]
    if files and all(f.startswith(("docs/views/", "docs/seats/", "scripts/atlas/")) or f == "README.md" for f in files):
        light += 1
print("F4  of the %d commits, %d touch nothing but generated views, the atlas, the front page's state block or a session's page" % (len(fp), light))
other = [l for l in ns if l[0] in "DR"]
print("    files deleted or renamed in the window: %d (the review's script lists added files only)" % len(other))

# ---- F5: the environment
RUN = ("import sys, json; sys.dont_write_bytecode = True; sys.path.insert(0, 'scripts/gates'); import gates as g\n"
       "print(json.dumps({n: [bool(g.GATES[n]()[0]), str(g.GATES[n]()[1])[:110]] for n in sys.argv[1].split(',')}))\n")


def three(env):
    r = subprocess.run([sys.executable, "-B", "-c", RUN, "review-fires,point-debt,retraction-debt"], cwd=repo, capture_output=True, text=True,
                       env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", **env))
    return json.loads(r.stdout.strip().split("\n")[-1])


empty = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a_page_with_no_row.md")
base = three({})
print("\nF5  three gates as they stand: " + "; ".join("%s %s" % (k, "PASS" if v[0] else "FAIL") for k, v in base.items()))
for label, env, gate in (("OA_REVIEW_MERGES=0", {"OA_REVIEW_MERGES": "0"}, "review-fires"),
                         ("OA_POINT_REGISTER=<a page with no row>", {"OA_POINT_REGISTER": empty}, "point-debt"),
                         ("OA_RETRACTIONS_LEDGER=<a page with no row>", {"OA_RETRACTIONS_LEDGER": empty}, "retraction-debt")):
    got = three(env)[gate]
    print("    with %s: %s %s -- %s%s" % (label, gate, "PASS" if got[0] else "FAIL", got[1][:95], "   [its line changed]" if got != base[gate] else "   [unchanged]"))
print("    (gates.py, gate_review_fires: 'OA_REVIEW_MERGES overrides the count for the failing-path test')")

# ---- F6: a sentence moves the anchor
real = g._read(g.REVIEWS)
before = g.review_status()
planted = real + "\n\nA note, not a review: the gates were run at **anchor-commit: `%s`** today.\n" % head
orig = g._read
g._read = lambda rel: planted if rel == g.REVIEWS else orig(rel)
after = (g.review_status(), g.gate_review_fires(), g.gate_review_core()[0], g.GATES["review-actions"]()[0], g.GATES["carry-age"]()[0])
g._read = orig
print("\nF6  the count of landings since the last review, as it stands: %s" % (before,))
print("    with one sentence at the end of docs/progress/REVIEWS.md that names the head as an anchor (planted in memory):")
print("    count %s; review-fires %s; review-core %s; review-actions %s; carry-age %s" % (after[0], after[1], "PASS" if after[2] else "FAIL", "PASS" if after[3] else "FAIL", "PASS" if after[4] else "FAIL"))
print("    (gates.py, review_status, and review_tools.py, last_anchor: the last 'anchor-commit:' anywhere in the file)")

# ---- F7: an anchor git does not know
bad = "0123456789abcdef"
log = [l for l in rt.git("log", "--format=%h", bad + "..HEAD").splitlines() if l]
add = [p for p in rt.git("diff", "--name-only", "--diff-filter=A", bad, "HEAD").splitlines() if p]
print("\nF7  the window from an anchor git does not know: %d commits, %d added files, and no refusal" % (len(log), len(add)))
print("    (review_tools.py, git(): it returns what git printed and not whether git failed)")

# ---- F8: the reach of the provenance scan
src = open(os.path.join(repo, "scripts/review/review_tools.py"), encoding="utf-8").read()
print("\nF8  the review's scan for phrases that pretend outside verification reads the added lines of: %s" % re.findall(r'git\("diff", anchor, "HEAD", "--", ("[^"]+")\)\.splitlines', src))
