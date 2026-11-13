#!/usr/bin/env python3
"""C14, patch 3 (main's M20): the main goal's living lines and the knowledge index speak plainly

A diff of this change would carry, in its removed lines, words that are treated as the owner's.  So the change is given
as the blocks that come in: each block that goes is named by its file, the line it starts at and the sha256 of its text,
and no line of it is written here.

    python3 <this file> <a clean checkout>

It stops and writes nothing if a block that goes is not, byte for byte, the block this seat replaced.  It stages what
it changes and prints the tree, and says whether it is the tree this seat built.  It commits nothing: the message is the file beside this one.
"""
import hashlib, json, pathlib, subprocess, sys

root = pathlib.Path(sys.argv[1]).resolve()
EXPECTED = '87081fd98b65c528a754535d3b4bdbc570774712'
AFTER = ''
OPS = json.loads(r'''[
[
"docs/MAIN_GOAL.md",
2,
3,
"98214bd0032af8e99afd7409c222efc1848d3822ad30b610c67ee7aafa32e972",
[
"*(Set as the main goal on 2026-09-06, with no drift from it until the Standard Model is derived in full; it binds",
"all work. It refines `docs/STRATEGY_2026-09-05.md` §4, whose items 3–5 stay live and resume when a join blocks. [Reworded",
"2026-11-13: this line gave the decision as a quotation; it is in plain words, and what stood is not kept here.])*"
]
],
[
"docs/MAIN_GOAL.md",
9,
1,
"7810918e75de1a6aff60e28033edf82900bea1749f6c3f3243dedbc128c76554",
[
"> - THE FINAL ATTACK's order was chosen on 2026-10-30 (P-495): explaining as compression with a null, and one"
]
],
[
"knowledge/INDEX.md",
42,
1,
"c87c3acf6aa6ee16f10ae5c14447321cd080e3f695aeb175b3cb0e9e9b9f7100",
[
"| **K024** ✓ | [The forcing map: the object's anatomy, and what can escape it](K024_the_forcing_map.md) | Built 2026-07-08, to measure the object's whole body and its self-triggering structure rather than ask it to be the SM. The unified map: **nodes** = the object's facets (its coordinates/angles), **edges** = the FORCINGS (which triggers which), each marked PROVEN / KNOWN / OPEN. Answers three questions: is it doable, can anything escape, do we already have the objects. Nodes span `σ` (the substitution a → ab, `K021`), `φ / λ_m` (golden & metallic eigenvalues, `K002`), `A_m` (metallic matrices, `K002`/B471), `X_m` (the det −1 half / breath root, B469), `4₁` & the census (`K004`), the trace map / character variety (`K001`), the Ruelle spectrum (escape rate γ, B451), the level-15 seam / Weil master theorem (B472/B474), and the Fibonacci anyon / SU(2)₃ TQFT (B483) | B451, B469, B471, B472/B474, B483; `K001`,`K002`,`K004`,`K021` |"
]
],
[
"scripts/gates/gates.py",
3194,
2,
"dec9b38fd114df5d01c6e9c170fed4cd2c4dea2488b5b91f036b9e4ff65faa3a",
[
"    'docs/MAIN_GOAL.md': {'lane': 1, 'main': 1, 'owner': 4, 'ruled': 1, 'seat': 10},",
"    # knowledge/INDEX.md: at zero since C14's third patch (2026-11-13)"
]
]
]''')

texts = {}
for path, start, count, digest, new in OPS:
    lines = texts.setdefault(path, (root / path).read_text(encoding="utf-8").split("\n"))
by_file = {}
for op in OPS:
    by_file.setdefault(op[0], []).append(op)
for path, ops in by_file.items():
    lines = texts[path]
    for _p, start, count, digest, new in ops:
        if hashlib.sha256("\n".join(lines[start:start + count]).encode("utf-8")).hexdigest() != digest:
            sys.exit("STOPPED, nothing written: in %s the %d line(s) from line %d are not the ones this change replaces" % (path, count, start + 1))
    for _p, start, count, digest, new in sorted(ops, key=lambda o: -o[1]):
        lines[start:start + count] = new
for path, lines in texts.items():
    (root / path).write_text("\n".join(lines), encoding="utf-8")
if AFTER:
    r = subprocess.run(AFTER, cwd=str(root), shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("the files are edited and THE STEP AFTER THEM FAILED (%s):\n" % AFTER + (r.stdout + r.stderr)[-1500:])
subprocess.run(["git", "add", "-A"], cwd=str(root), check=True)
tree = subprocess.run(["git", "write-tree"], cwd=str(root), capture_output=True, text=True).stdout.strip()
changed = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=str(root), capture_output=True, text=True).stdout.split()
print("staged: %d files" % len(changed)); print("\n".join("  " + c for c in changed))
print("the tree: %s" % tree)
if EXPECTED:
    print("it is the tree the builder made" if tree == EXPECTED else "it is NOT the tree the builder made (%s): the base differs, or something else is staged" % EXPECTED)
