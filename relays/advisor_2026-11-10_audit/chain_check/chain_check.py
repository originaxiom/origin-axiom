#!/usr/bin/env python3
"""Was this repository's commit chain broken after it was started?  The checks, in one file.

The owner asked it on 2026-11-11: he remembered a "distilled" repository and an interrupted chain, and thought the agy
lane had pointed it out.  This seat first ran each check by hand; this file is the same checks, so that main or anyone
can run them again.  WRITTEN AFTER THE ANSWERS WERE SEEN: it is a record of what was checked, not a blind test.

    python3 chain_check.py [--ref origin/main]        (run inside a full clone with every branch and tag fetched)

What a git history can and cannot show.  It shows every commit that is there and what each rests on.  It cannot show a
commit that was once pushed and then replaced: a rewrite leaves no mark in the graph.  What can be asked instead is whether
the things that were named at the time -- tags, and commit ids typed into the logs -- are still there.  If the line had
been rewritten, the old ids would be gone.
"""
import subprocess, sys, re, collections

ref = sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else "origin/main"


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, errors="replace")


def out(*a):
    return git(*a).stdout.strip()


print("checked at %s = %s" % (ref, out("rev-parse", "--short=9", ref)))
print("1. a full clone: %s" % ("yes" if out("rev-parse", "--is-shallow-repository") == "false" else "NO, shallow: the rest is not to be read"))
roots = out("rev-list", "--max-parents=0", ref).split()
print("2. commits: %s; on main's own line: %s; first commits (no parent): %d -- %s" % (
    out("rev-list", "--count", ref), out("rev-list", "--count", "--first-parent", ref), len(roots),
    "; ".join(out("log", "-1", "--format=%h %cs %s", r)[:90] for r in roots)))
merges = out("rev-list", "--merges", ref).split()
unrelated = [m for m in merges if git("merge-base", m + "^1", m + "^2").returncode != 0]
print("3. merges: %d; of them joining two histories with no common ancestor: %d" % (len(merges), len(unrelated)))
stamps = [int(x) for x in out("log", "--first-parent", "--format=%ct", ref).split()]
back = sum(1 for newer, older in zip(stamps, stamps[1:]) if newer < older)
gap, at = max((newer - older, i) for i, (newer, older) in enumerate(zip(stamps, stamps[1:])))
days = out("log", "--first-parent", "--format=%cs", ref).split()
print("4. commits on main's own line dated before their parent: %d; the longest pause: %.1f days, from %s to %s" % (back, gap / 86400, days[at + 1], days[at]))
window = collections.Counter(d for d in days if "2026-08-29" <= d <= "2026-09-08")
print("5. main's own line around the distilled repository's dates (its head is dated 2026-09-03): " + ", ".join("%s: %d" % (d[5:], window[d]) for d in sorted(window)))
tags = out("tag").split()
on, off = [], []
for t in sorted(tags):
    (on if git("merge-base", "--is-ancestor", t + "^{commit}", ref).returncode == 0 else off).append(t)
kept = [t for t in off if t.startswith(("archive/", "retired/"))]
print("6. tags: %d.  Marking a commit that is in main's history: %d, dated %s to %s.  Not in it: %d, of which %d are named archive/ or retired/ (seats' branches kept as tags); others: %s" % (
    len(tags), len(on), min(out("log", "-1", "--format=%cs", t + "^{commit}") for t in on), max(out("log", "-1", "--format=%cs", t + "^{commit}") for t in on),
    len(off), len(kept), ", ".join(sorted(set(off) - set(kept))) or "none"))
files = ["PROGRESS_LOG.md", "CHANGELOG.md"] + [l for l in out("ls-tree", "-r", "--name-only", ref, "docs/progress").splitlines() if l.endswith(".md")]
pat = re.compile(r"(?:@\s?|\bcommit\s+|\bcommits?\s+`|\bHEAD\s*(?:=|at|is)\s*|\bmerged?\s+(?:at\s+|in\s+)?|\bpinned\s+at\s+|\bat\s+`)`?([0-9a-f]{7,12})\b")
cited = collections.OrderedDict()
for f in files:
    for n, line in enumerate(git("show", ref + ":" + f).stdout.splitlines(), 1):
        for m in pat.finditer(line):
            tok = m.group(1)
            if re.search(r"[a-f]", tok) and re.search(r"\d", tok):
                cited.setdefault(tok, "%s:%d" % (f, n))
res = collections.Counter(); gone = []
for tok, where in cited.items():
    r = git("rev-parse", "--verify", "--quiet", tok + "^{commit}")
    if r.returncode != 0:
        res["not found"] += 1; gone.append("%s (%s)" % (tok, where))
    elif git("merge-base", "--is-ancestor", r.stdout.strip(), ref).returncode == 0:
        res["in main's history"] += 1
    else:
        res["in the repository, on a seat's branch or tag"] += 1
print("7. commit ids typed into the two logs and the progress pages at the time (%d pages, %d ids): %s" % (len(files), len(cited), "; ".join("%s: %d" % kv for kv in res.most_common())))
print("   not found: " + ("; ".join(gone) if gone else "none"))
print("8. the distilled repository's head, 1002235a8, in this repository: %s; refs on any remote that name 'distill': %d" % (
    "yes" if git("cat-file", "-e", "1002235a8^{commit}").returncode == 0 else "no", sum(1 for l in out("for-each-ref", "--format=%(refname)").splitlines() if "distill" in l.lower())))
