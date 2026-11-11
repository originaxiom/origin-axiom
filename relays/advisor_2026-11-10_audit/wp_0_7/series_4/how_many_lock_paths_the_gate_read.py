#!/usr/bin/env python3
"""How many of the paths that locks name beside themselves did the tracked-deps gate read before series 4's patch 6?

    python3 how_many_lock_paths_the_gate_read.py CHECKOUT GATES_FILE

CHECKOUT is a checkout of the commit to measure (main's head).  GATES_FILE is the gates' file WITH the patch, which holds
both readers: the one that reads the syntax tree, and the pattern reader that was the gate's only reader before.  Each lock of
CHECKOUT is read by both.  Nothing is written.  Standard library only."""
import collections, importlib.util, os, subprocess, sys

root, gates_file = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
spec = importlib.util.spec_from_file_location("gates_with_the_patch", gates_file)
g = importlib.util.module_from_spec(spec); sys.dont_write_bytecode = True; spec.loader.exec_module(g)
tracked = set(subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True).stdout.split("\n"))
locks = [f for f in sorted(tracked) if f.startswith(("tests/", "frontier/")) and os.path.basename(f).startswith("test_") and f.endswith(".py")]
n_tree = n_both = computed = unparsed = 0
only_pattern = []
for rel in locks:
    txt = open(os.path.join(root, rel), encoding="utf-8", errors="replace").read()
    by_tree, c, parsed = g._own_paths(rel, txt)
    by_pattern = g._file_relative_refs_by_pattern(rel, txt)
    n_tree += len(by_tree); n_both += len(by_tree & by_pattern); computed += c; unparsed += not parsed
    only_pattern += [(rel, p) for p in sorted(by_pattern - by_tree)]
head = subprocess.run(["git", "-C", root, "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
print("at %s: %d locks; %d do not parse" % (head, len(locks), unparsed))
print("paths of files that the locks name beside themselves, read from the syntax tree: %d" % n_tree)
print("of them read by the pattern reader, the gate's only reader before the patch:     %d (%d in 100)" % (n_both, round(100.0 * n_both / max(n_tree, 1))))
print("with a part that is computed, read by neither:                                   %d" % computed)
kinds = collections.Counter("a folder" if os.path.isdir(os.path.join(root, p)) else "a pattern" if any(ch in p for ch in "*?[") else "another path"
                            for _, p in only_pattern)
print("read by the pattern reader alone: %d -- %s" % (len(only_pattern), ", ".join("%d %s" % (v, k) for k, v in sorted(kinds.items()))))
for rel, p in only_pattern:
    if not os.path.isdir(os.path.join(root, p)) and not any(ch in p for ch in "*?["):
        print("    ", p, "<-", rel)
absent = sorted({(p, rel) for rel in locks for p in g._own_paths(rel, open(os.path.join(root, rel), encoding="utf-8", errors="replace").read())[0]
                 if p not in tracked and not os.path.isdir(os.path.join(root, p))})
ignored = set(subprocess.run(["git", "-C", root, "check-ignore", "--no-index", "--stdin"], input="\n".join(p for p, _ in absent) + "\n",
                             capture_output=True, text=True).stdout.split("\n")) - {""}
print("paths read from the tree that the commit does not hold: %d; of them git would ignore: %d" % (len(absent), len(ignored)))
for p, rel in absent:
    print("    ", "IGNORED" if p in ignored else "absent ", p, "<-", rel)
