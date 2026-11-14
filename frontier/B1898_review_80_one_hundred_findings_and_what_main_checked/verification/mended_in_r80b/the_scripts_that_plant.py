#!/usr/bin/env python3
"""Which tracked scripts plant a change against a lock or a gate, and what each does when a plant changes nothing.

A script is counted where it is tracked, is not a test file and not under relays/ or legacy/, and its text (1) says "plant",
(2) changes a text (a replace, a substitution, a write) and (3) runs something on the result (a process, pytest, a gate).
What this search can miss: a script that plants and never uses the word; one that changes a file by another call than
these; and a planting test (a test file is not counted: its plants are asserts of the suite).

For each script it prints: the lines that make a plant by replacing a text, and whether the script, anywhere, compares a
planted text with the text it came from and stops (an assert, a raise, an exit) where they are the same.

    python3 the_scripts_of_mains_that_plant.py <repository>
"""
import pathlib, re, subprocess, sys
root = pathlib.Path(sys.argv[1]).resolve()
names = subprocess.run(["git", "-C", str(root), "ls-files", "*.py"], capture_output=True, text=True).stdout.split("\n")
SAYS = re.compile(r"plant", re.I)
CHANGES = re.compile(r"\.replace\(|re\.sub\(|\.write_text\(|\.write\(")
RUNS = re.compile(r"subprocess\.|pytest|GATES\[|gates\.")
STOPS = re.compile(r"(assert|raise|sys\.exit|exit)\b[^\n]*(!=|==|is not|not in| in )[^\n]*|changed nothing|changes nothing|no change|unchanged", re.I)
out = []
for rel in names:
    if not rel or rel.startswith(("relays/", "legacy/", "tests/")) or pathlib.PurePosixPath(rel).name.startswith("test_"):
        continue
    try:
        text = (root / rel).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        continue
    if SAYS.search(text) and CHANGES.search(text) and RUNS.search(text):
        plants = [n for n, l in enumerate(text.split("\n"), 1) if ".replace(" in l or "re.sub(" in l]
        guards = [n for n, l in enumerate(text.split("\n"), 1) if re.search(r"changed nothing|changes nothing|plant[^\n]*(!=|==)|(!=|==)[^\n]*plant|assert [a-z_]+ != [a-z_]+\b", l, re.I)]
        out.append((rel, len(plants), guards))
print("tracked scripts that say they plant, change a text and run something on it: %d" % len(out))
for rel, n, guards in out:
    print("%-118s replacements: %2d; lines that compare a plant with its source: %s" % (rel[:118], n, guards[:6] or "none"))
