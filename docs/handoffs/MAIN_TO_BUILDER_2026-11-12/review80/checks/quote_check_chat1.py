#!/usr/bin/env python3
"""Review 80, the web seat's file: each quotation of its section 1 looked for, by machine, in the file it names at the
commit the seat read.  A quotation that is not there word for word is reported.  The control: a quotation changed by
one word must not be found."""
import subprocess, json, sys
AT = "c40446392"
Q = [("scripts/checks/check_test_vacuity.py", "Find test functions that pass unconditionally -- locks that cannot fail."),
     ("scripts/checks/retraction_sweep.py", "A line is a MENTION (allowed) if it carries any of these near the phrase."),
     ("docs/RETRACTED_PHRASES.md", "that line is held by name in the sweep's own table, by its file and its phrase"),
     ("scripts/gates/gates.py", "(1) the control is not skipped: no skip or xfail mark on it or on its module, and no call that skips in its body;"),
     ("scripts/gates/gates.py", "healed = len(CANNOT_FAIL_AS_FOUND) - len(held) if held else 0"),
     ("frontier/B1891_the_foundation_at_version_1_66/verification/test_b1891_the_foundation_at_version_1_66.py", "one of the four corrected sentences standing in its old"),
     ("frontier/B1894_review_79_the_second_round/FINDINGS.md", "is a living page and quotes nothing he said")]
def text(path):
    return subprocess.run(["git", "show", "%s:%s" % (AT, path)], capture_output=True, text=True, check=True).stdout
def flat(s):
    return " ".join(s.split())
out = []
for path, q in Q:
    t = text(path)
    out.append({"file": path, "found": q in t, "found when the lines are joined": flat(q) in flat(t)})
control = flat(Q[0][1].replace("unconditionally", "conditionally")) in flat(text(Q[0][0]))
res = {"at": AT, "quotations": out, "found": sum(o["found"] or o["found when the lines are joined"] for o in out), "of": len(out), "the control, one word changed, is found": control}
print(json.dumps(res, indent=1))
