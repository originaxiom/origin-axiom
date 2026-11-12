#!/usr/bin/env python3
"""The twenty pages of the move (main's M12): what names each of them, in a file that is not a page.

    python3 what_names_the_twenty.py <a checkout before the move>

Main asked to be told of a page among the twenty that a script, a test or a gate reads.  Every tracked file that is not
a page (not .md, .tex or .txt) is read as text, and each of the twenty is looked for by its path and by its file name
standing as a name of its own.  A file that names a page is listed with its kind: a script, a test, or a file of data.
Whether a script that names a page READS it is then looked at by hand, and said in the note.  Nothing is written."""
import collections
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(sys.argv[1])
TWENTY = """AUDIT_REPORT.md docs/RECONTEXT_AUDIT_AND_MASTERPLAN_2026-07.md docs/SESSION3_SYNTHESIS.md docs/RECOGNITION.md docs/AUDIT_2026-07-05.md
docs/CLOSURE_2026-07-11.md docs/CODEX_AUDIT_RESPONSE_2026-07-12.md docs/CRYSTALLIZATION_2026-07-09.md docs/REBASE_2026-07-12.md docs/CLOSURE_PROGRAM.md
docs/PHASE1_WRAP.md docs/COMMS_PROTOCOL.md docs/ROADMAP_TOE.md docs/THE_PATTERN_MEDITATION.md docs/PARAMETER_CLOSURE_MASTERPLAN.md docs/PUBLICATION_CAMPAIGN.md
docs/THE_PATTERN_MEDITATION_2.md docs/CLOSURE_2026-07-05.md docs/THE_ROLES_ACCOUNTING.md docs/SUBMISSION_CAMPAIGN.md""".split()

tracked = [f for f in subprocess.run(["git", "-C", ROOT, "ls-files"], capture_output=True, text=True).stdout.split("\n") if f]
missing = [p for p in TWENTY if p not in tracked]
print("the head read: " + subprocess.run(["git", "-C", ROOT, "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip())
print("of the twenty, tracked at this head: %d%s" % (len(TWENTY) - len(missing), "; NOT THERE: " + ", ".join(missing) if missing else ""))
others = [f for f in tracked if not f.endswith((".md", ".tex", ".txt"))]
print("tracked files that are not pages, each read as text: %d" % len(others))


def kind(f):
    base = os.path.basename(f)
    if base.startswith("test_") and f.endswith(".py"):
        return "a test"
    if f.endswith((".py", ".sh")):
        return "a script"
    return "data"


names = collections.defaultdict(list)
for f in others:
    try:
        text = open(os.path.join(ROOT, f), encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    for p in TWENTY:
        if re.search(r"(?<![\w/.-])" + re.escape(os.path.basename(p)) + r"(?![\w-])", text) or p in text:
            names[p].append(f)
print()
for p in TWENTY:
    hits = names.get(p, [])
    by_kind = collections.Counter(kind(f) for f in hits)
    print("%-48s %s" % (p, ", ".join("%d %s" % (n, k) for k, n in sorted(by_kind.items())) if hits else "named by no file that is not a page"))
    for f in hits:
        if kind(f) != "data":
            print("      %s: %s" % (kind(f), f))
tests = sorted({f for hits in names.values() for f in hits if kind(f) == "a test"})
scripts = sorted({f for hits in names.values() for f in hits if kind(f) == "a script"})
data = sorted({f for hits in names.values() for f in hits if kind(f) == "data"})
print("\ntests that name one of the twenty: %d" % len(tests))
print("scripts that name one of the twenty: %d %s" % (len(scripts), scripts))
print("files of data that name one of the twenty: %d" % len(data))
for f in data:
    print("      " + f)
