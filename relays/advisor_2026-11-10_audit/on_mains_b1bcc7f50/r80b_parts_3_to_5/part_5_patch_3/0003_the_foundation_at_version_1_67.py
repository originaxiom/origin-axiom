#!/usr/bin/env python3
"""R80b, part 5, patch 3, as a script and not as one diff.

A diff of the foundation's own page would carry, in its removed lines, the seven passages in which the owner was quoted.
So the patch is given in two steps, and no file here holds a passage:

  1. everything the patch changes but GENESIS.md, as a diff: 0003_all_of_the_patch_but_the_foundations_own_page.patch;
  2. GENESIS.md, written by the arc's own script, which that diff adds
     (frontier/B1904_the_foundation_at_version_1_67/verification/write_version_1_67.py).  It loads main's seven pairs from
     main's file in the arc B1898 and prints each passage's number.

    python3 0003_the_foundation_at_version_1_67.py <a clean checkout>

It applies the diff to the index and the working tree, runs the arc's script, stages GENESIS.md and prints the tree.  On
main's b1bcc7f50 with R80b's parts 3 and 4 and the first two patches of part 5, as rebuilt there, the tree is
4054bc3d204daf67bd98becdae0e656560199e05; the script says whether it is.  It commits nothing: the message is 0003_message.txt, beside this file.
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
root = pathlib.Path(sys.argv[1]).resolve()
EXPECTED = "4054bc3d204daf67bd98becdae0e656560199e05"


def run(*args):
    return subprocess.run(list(args), cwd=str(root), capture_output=True, text=True)


if run("git", "status", "--porcelain").stdout.strip():
    sys.exit("STOPPED, nothing written: the checkout is not clean")
r = run("git", "apply", "--index", str(HERE / "0003_all_of_the_patch_but_the_foundations_own_page.patch"))
if r.returncode != 0:
    sys.exit("STOPPED, nothing written: the diff does not apply\n" + r.stderr[-1500:])
r = run(sys.executable, "-B", "frontier/B1904_the_foundation_at_version_1_67/verification/write_version_1_67.py", "--write")
if r.returncode != 0 or not r.stdout.rstrip().endswith("written"):
    sys.exit("the diff is applied and THE FOUNDATION IS NOT WRITTEN:\n" + (r.stdout + r.stderr)[-1500:])
print(r.stdout.rstrip())
subprocess.run(["git", "add", "GENESIS.md"], cwd=str(root), check=True)
tree = run("git", "write-tree").stdout.strip()
changed = run("git", "diff", "--cached", "--name-only").stdout.split()
print("staged: %d files" % len(changed))
print("the tree: %s" % tree)
print("it is the tree the builder made" if tree == EXPECTED else
      "it is NOT the tree the builder made (%s): main's head has moved, or something else is staged" % EXPECTED)
