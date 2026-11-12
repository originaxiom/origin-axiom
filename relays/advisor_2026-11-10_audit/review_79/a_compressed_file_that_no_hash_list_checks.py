#!/usr/bin/env python3
"""Main's M9, one more finding in the enforcement package's files: a compressed file that no hash list checks in the form
it is tracked in.

    python3 a_compressed_file_that_no_hash_list_checks.py <a checkout at main's head> [<a checkout with the series applied>]

1. THE MEASURE, on the first checkout: of the entries of the hash lists that name no tracked file, how many name a file
   whose compressed form is tracked beside the name; and for each, whether the listed hash is the hash of what the
   compressed file holds.
2. THE PLANT, on each checkout: in a worktree of its own, the content of the census file of B1786 is replaced and
   committed, and the gate on the hash lists is run.  The worktree is removed.  Nothing is written into the checkout."""
import bz2
import gzip
import hashlib
import importlib.util
import lzma
import os
import subprocess
import sys
import tempfile

TREES = [os.path.abspath(p) for p in sys.argv[1:3]]
OPEN = {".gz": gzip.open, ".bz2": bz2.open, ".xz": lzma.open}
CENSUS = "frontier/B1786_the_slope_principle_out_of_sample/verification/census.jsonl.gz"


def gates_of(tree, name):
    spec = importlib.util.spec_from_file_location("gates_" + name, os.path.join(tree, "scripts", "gates", "gates.py"))
    g = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(g)
    return g


def git(repo, *a):
    r = subprocess.run(["git", "-C", repo, "-c", "user.name=originaxiom", "-c", "user.email=originaxiom@users.noreply.github.com", *a],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-400:]
    return r.stdout.strip()


main = TREES[0]
g = gates_of(main, "main")
tracked = set(git(main, "ls-files").split("\n"))
state = g.hash_list_state(main)
no_file = [e for e in state if e[3] in ("ABSENT", "NOT TRACKED")]
print("main's head: %s" % git(main, "rev-parse", "--short=9", "HEAD"))
print("\n1. THE MEASURE")
print("   entries of the hash lists: %d;   that name no tracked file: %d" % (len(state), len(no_file)))
found = []
for key, lst, name, st, sig in no_file:
    d = os.path.dirname(lst)
    for base in (os.path.normpath(os.path.join(d, name)), os.path.normpath(os.path.join(d, "verification", name)), os.path.normpath(name)):
        for suffix, opener in OPEN.items():
            if base + suffix in tracked:
                found.append((lst, name, base + suffix, opener))
print("   of those, entries whose named file is tracked in a compressed form (.gz, .bz2, .xz): %d" % len(found))
for lst, name, packed, opener in found:
    listed = [l.split()[0] for l in open(os.path.join(main, lst), encoding="utf-8", errors="replace").read().split("\n") if l.strip().endswith(name) and l.split()]
    try:
        with opener(os.path.join(main, packed), "rb") as fh:
            inner = hashlib.sha256(fh.read()).hexdigest()
    except Exception as e:
        inner = "cannot be opened (%s)" % type(e).__name__
    print("      %s names %s; tracked: %s" % (lst, name, packed))
    print("         the listed hash is the hash of what the compressed file holds: %s" % ("YES" if inner in listed else "NO"))

print("\n2. THE PLANT: the content of %s is replaced, and committed" % CENSUS)
for n, tree in enumerate(TREES):
    name = "main's head" if n == 0 else "the series"
    with tempfile.TemporaryDirectory() as tmp:
        wt = os.path.join(tmp, "wt")
        git(tree, "worktree", "add", "-q", "--detach", wt, "HEAD")
        try:
            gg = gates_of(wt, "plant_%d" % n)
            before = gg.GATES["artifact-hashes"]()
            with gzip.open(os.path.join(wt, CENSUS), "wb") as fh:
                fh.write(b'{"a census": "that is not the census"}\n')
            git(wt, "add", "-A")
            git(wt, "commit", "-q", "-m", "the census replaced")
            after = gg.GATES["artifact-hashes"]()
            print("   %-12s before: %s;   after: %s   -> %s" % (name, "passes" if before[0] else "FAILS", "passes" if after[0] else "FAILS",
                                                               "NOT CAUGHT" if after[0] else "CAUGHT"))
            if not after[0]:
                print("        " + str(after[1])[:200].replace(tmp, "<the plant>"))
        finally:
            git(tree, "worktree", "remove", "--force", wt)
