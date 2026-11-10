#!/usr/bin/env python3
"""The computational chain of an arc: which other arcs' files its scripts load, followed recursively.
A static reading of the scripts (frontier/B<n>_* paths and folder names named in the source); read-only.
    python3 relays/advisor_2026-11-10_audit/dry_run/code_chain.py [ARC]"""
import glob, os, re, sys, collections, json
ROOT_ARC = sys.argv[1] if len(sys.argv) > 1 else "B1841"
dirs = {}
for d in sorted(glob.glob("frontier/B*_*")):
    m = re.match(r"frontier/(B\d+)_", d)
    if m and os.path.isdir(d): dirs.setdefault(m.group(1), d)
byname = {os.path.basename(d): k for k, d in dirs.items()}
def refs(arc):
    out = collections.defaultdict(set)
    for f in glob.glob(dirs[arc] + "/**/*.py", recursive=True):
        if "/referee/" in f or os.path.basename(f).startswith("test_"): continue
        src = open(f, encoding="utf-8", errors="replace").read()
        for name in set(re.findall(r"B\d{2,4}_[A-Za-z0-9_]+", src)):
            k = byname.get(name)
            if k and k != arc:
                # which files of that arc are named near the folder name
                files = set(re.findall(re.escape(name) + r"[\"'/, ]+(?:[\"']?verification[\"']?[\"'/, ]+)?[\"']?([A-Za-z0-9_]+\.(?:py|json|npz|npy|jsonl|txt|gz))", src))
                out[k] |= files or {"(folder named)"}
    return out
seen, order, edges = {}, [ROOT_ARC], {}
seen[ROOT_ARC] = 0
i = 0
while i < len(order):
    a = order[i]; i += 1
    r = refs(a); edges[a] = {k: sorted(v) for k, v in r.items()}
    for k in sorted(r, key=lambda s: int(s[1:])):
        if k not in seen: seen[k] = seen[a] + 1; order.append(k)
print("computational chain of", ROOT_ARC, ":", len(order), "arcs")
for a in order:
    print("  " * seen[a] + a, os.path.basename(dirs[a])[len(a) + 1:][:46], "<-", {k: v[:4] for k, v in edges[a].items()} if edges[a] else "(loads no other arc)")
json.dump(dict(root=ROOT_ARC, depth=seen, edges=edges), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "code_chain_%s.json" % ROOT_ARC), "w"), indent=1)
