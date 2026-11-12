#!/usr/bin/env python3
"""The tenth patch of series 4 mends two locks, and its two tests stand in those same locks.

So its tests cannot be run "on the commit before" in the usual form: the lock as the patch leaves it holds the mend, and
no gate or checker is changed.  This script makes the form that shows the fault.  It takes each lock as it stood on the
commit before, adds the patch's new tests and the names they need, adds nothing else of the patch, and runs the two new
tests there.

    python3 the_tenth_patchs_two_tests_on_the_locks_as_they_stood.py <a checkout that holds both commits> <the commit before> <the patch's commit>

It works in a worktree of its own, which it removes.  It changes no file of the checkout."""
import ast
import os
import subprocess
import sys
import tempfile

repo, before, patch = sys.argv[1:4]

# the lock -> the top-level names of the patch that are its new test and what that test needs.  The mend is not among them:
# it is the function that adds a record (_record_in_the_gate) and the lines of one test that now do the same.
LOCKS = {
    "tests/test_nothing_leaves_a_ledger.py": ("_the_statement_that_binds", "_AS_MAIN_WOULD_WRITE_IT", "_gates_in_which_acts_are_recorded",
                                              "test_the_tests_that_record_an_act_run_whatever_the_tables_already_hold"),
    "tests/test_a_gate_reads_all_it_is_about.py": ("_the_statement_that_binds",
                                                   "test_the_record_of_a_control_that_left_is_planted_whatever_the_table_already_holds"),
}


def git(*a, cwd=repo):
    r = subprocess.run(["git", "-C", cwd, *a], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout


def name_of(node):
    if isinstance(node, ast.FunctionDef):
        return node.name
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
        return node.targets[0].id
    return None


before, patch = git("rev-parse", before).strip(), git("rev-parse", patch).strip()
assert git("rev-parse", patch + "^").strip() == before, "the first commit is not the parent of the second"
print("the commit before: %s    the patch: %s" % (before[:9], patch[:9]))
print("files the patch changes: " + ", ".join(git("show", "--name-only", "--format=", patch).split()))

with tempfile.TemporaryDirectory() as tmp:
    wt = os.path.join(tmp, "as_they_stood")
    git("worktree", "add", "-q", "--detach", wt, before)
    try:
        ids = []
        for lock, names in LOCKS.items():
            old, new = git("show", before + ":" + lock), git("show", patch + ":" + lock)
            stood = {name_of(n) for n in ast.parse(old).body}
            comes = {name_of(n): n for n in ast.parse(new).body}
            assert not (set(names) & stood), "a name of the patch already stands in %s on the commit before" % lock
            assert old.count("import importlib.util\n") == 1
            text = old.replace("import importlib.util\n", "import ast\nimport importlib.util\n", 1).rstrip("\n")
            text += "".join("\n\n\n" + ast.get_source_segment(new, comes[n]) for n in names) + "\n"
            with open(os.path.join(wt, lock), "w", encoding="utf-8") as f:
                f.write(text)
            ids += [lock + "::" + n for n in names if n.startswith("test_")]
            print("%s: as it stood, with %d name(s) of the patch added: %s" % (lock, len(names), ", ".join(names)))
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "-rA", "--tb=short", *ids],
                           cwd=wt, capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
        print()
        for line in r.stdout.splitlines():
            if line.startswith(("E   ", "PASSED", "FAILED", "ERROR")) or " passed" in line or " failed" in line:
                print(line.replace(tmp, "<the worktree>")[:900])
    finally:
        git("worktree", "remove", "--force", wt)
