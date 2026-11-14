#!/usr/bin/env python3
"""C18, the move, as a diff and a script.

The diff `0001_the_scripts_the_readers_the_log_and_the_foundations_new_arc.patch` holds the new files (the move's script,
the foundation's version 1.68 as the arc B1930, the move's lock), the edits of the gates, the seal ledger's script, the
tests and arcs' scripts that read a moved file, the attribution baseline and the log of moves. This script then makes, in
the checkout: the move and the removals and the living pages' paths (by the move's own script), the foundation at 1.68 (by
B1930's own script), and the generated pages (by their generators). No moved or removed file's text, and no line of the
foundation, stands in the diff.

The spine reads each lock's birth from git, and a lock not yet committed has none: so, to count the move's new lock as
the spine will once the move is committed, the script makes one temporary commit of what it staged, runs the spine,
and takes the temporary commit back (`git reset --soft`), leaving everything staged and nothing committed.

    python3 0001_the_historical_folders_move.py <a clean checkout of the chain's last entry>

It stages what it changes and prints the tree, and says whether it is the tree this seat built. It commits nothing: the
message is 0001_message.txt, beside this file."""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
EXPECTED = "e2558cf6be3391a3e1ff4c836a86a20c1dded121"
root = pathlib.Path(sys.argv[1]).resolve()


def run(*a):
    r = subprocess.run(list(a), cwd=str(root), capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("STOPPED at %s:\n%s" % (" ".join(a), (r.stdout + r.stderr)[-1500:]))
    return r.stdout


if run("git", "status", "--porcelain").strip():
    sys.exit("STOPPED, nothing written: the checkout is not clean")
run("git", "apply", "--index", str(HERE / "0001_the_scripts_the_readers_the_log_and_the_foundations_new_arc.patch"))
print(run(sys.executable, "-B", "scripts/reorganize/history_2026_11_13.py").strip())
print(run(sys.executable, "-B", "frontier/B1930_the_foundation_at_version_1_68/verification/write_version_1_68.py", "--write").strip().split("\n")[-1])
for step in (["scripts/atlas/atlas.py"], ["frontier/B1883_where_we_stand/verification/build_where_we_stand.py", "--write"],
             ["scripts/views/generate.py"],
             ["frontier/B1861_the_closure_programme/verification/build_programme.py", "--write"]):
    run(sys.executable, "-B", *step)
run("git", "add", "-A")
run("git", "-c", "user.name=c18-temporary", "-c", "user.email=c18-temporary@localhost", "commit", "-q", "--no-verify",
    "-m", "C18, temporary: taken back below")
try:
    run(sys.executable, "-B", "scripts/views/spine.py")
finally:
    run("git", "reset", "-q", "--soft", "HEAD~1")
run("git", "add", "-A")
tree = run("git", "write-tree").strip()
print("the tree: %s" % tree)
print("it is the tree the builder made" if tree == EXPECTED else "it is NOT the tree the builder made (%s): the base differs, or something else is staged" % EXPECTED)
