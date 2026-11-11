#!/usr/bin/env python3
"""What weighs in the repository, and what a first reader meets: the numbers behind section 15 of the opinion page.

    python3 measure.py --repo CLONE        (CLONE: a clean checkout of main at the commit to be read)

Read-only.  Label, in the protocol's words: computed once.
"""
import collections, os, re, subprocess, sys

repo = os.path.abspath(sys.argv[sys.argv.index("--repo") + 1])
git = lambda *a: subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True).stdout
files = [f for f in git("ls-files").split("\n") if f]
size = {f: os.path.getsize(os.path.join(repo, f)) for f in files if os.path.isfile(os.path.join(repo, f))}
total = sum(size.values())
print("main at %s: %d tracked files, %.0f MB in the working tree" % (git("rev-parse", "--short=9", "HEAD").strip(), len(size), total / 1e6))
big = sorted(((s, f) for f, s in size.items() if s > 5_000_000), reverse=True)
print("files above 5 MB: %d, %.0f MB, %.0f%% of the tree; between 1 and 5 MB: %d files, %.0f MB\n" % (
    len(big), sum(s for s, f in big) / 1e6, 100 * sum(s for s, f in big) / total,
    sum(1 for s in size.values() if 1_000_000 < s <= 5_000_000), sum(s for s in size.values() if 1_000_000 < s <= 5_000_000) / 1e6))
listed = set()
for f in files:
    b = os.path.basename(f)
    if b.startswith("ARTIFACT_HASHES") and b.endswith(".txt"):
        for line in open(os.path.join(repo, f), encoding="utf-8", errors="replace"):
            for tok in line.split():
                tok = tok.strip("`*")
                if "." in tok:
                    listed.add(os.path.normpath(os.path.join(os.path.dirname(f), tok))); listed.add((os.path.dirname(f).split("/")[1] if f.startswith("frontier/") else "", os.path.basename(tok)))
py = {f: open(os.path.join(repo, f), encoding="utf-8", errors="replace").read() for f in files if f.endswith(".py")}
print("%-6s %-10s %-9s %-7s %-7s %s" % ("MB", "added", "in a hash", "its own", "other", "file"))
print("%-6s %-10s %-9s %-7s %-7s" % ("", "", "list", "scripts", "arcs'"))
for s, f in big:
    arc = f.split("/")[1] if f.startswith("frontier/") else ""
    base = os.path.basename(f)
    sealed = f in listed or (arc, base) in listed
    own = sum(1 for p, t in py.items() if base in t and p.split("/")[:2] == f.split("/")[:2])
    other = sum(1 for p, t in py.items() if base in t and arc.split("_")[0] in t and p.split("/")[:2] != f.split("/")[:2])
    first = git("log", "--diff-filter=A", "--format=%cs", "--", f).split()
    print("%-6.0f %-10s %-9s %-7d %-7d %s" % (s / 1e6, first[-1] if first else "?", "yes" if sealed else "no", own, other, f))
md = [f for f in files if f.endswith(".md")]
top = collections.Counter(f.split("/")[0] if "/" in f else "(root)" for f in md)
front = [f for f in md if "/" not in f or (f.startswith("docs/") and f.count("/") == 1)]
marked = [f for f in front if re.search(r"doc-currency:\s*[a-z-]+", open(os.path.join(repo, f), encoding="utf-8", errors="replace").read(1500))]
print("\n.md pages: %d  %s" % (len(md), dict(top.most_common(12))))
print("at the root and directly under docs/: %d; of them with a mark in their first lines that says current or frozen: %d" % (len(front), len(marked)))
names = sorted(f for f in front if re.search(r"STATUS|MASTERPLAN|WHERE_WE|STATE|ROADMAP|PLAN|README|CLAIM|GENESIS", os.path.basename(f).upper()))
print("of them, named as a status, a plan, a claim or a start: %d" % len(names))
for f in names:
    print("   %-52s last changed %s" % (f, git("log", "-1", "--format=%cs", "--", f).strip()))
