#!/usr/bin/env python3
"""SM-R81's own recounts, read from git objects only.
(a) rows of docs/RETRACTIONS.md by the rule of tests/test_b1425_determinism.py, at the ends of Review 79's window
    (38d2a36dc, 0dda7b472) and on either side of 738be0e5f;
(b) the exponent of P-670's bound in docs/POINT_REGISTER.md at 78edf8694 and at 7d7ab1dfa.
The planted control counts with the header filter dropped and must disagree with (a)."""
import json, pathlib, re, subprocess
HERE = pathlib.Path(__file__).resolve().parent
show = lambda c, p: subprocess.run(["git", "show", f"{c}:{p}"], capture_output=True, text=True).stdout
def rows(c, plant=False):
    idx = show(c, "docs/RETRACTIONS.md")
    return len([l for l in idx.split("\n") if l.startswith("| ") and not l.startswith("|---")
                and (plant or "what was asserted" not in l)])
out = {"retraction rows": {c: rows(c) for c in ["38d2a36dc", "0dda7b472", "738be0e5f~1", "738be0e5f", "c40446392"]}}
out["control (header filter dropped) at 0dda7b472"] = rows("0dda7b472", plant=True)
out["control disagrees"] = out["control (header filter dropped) at 0dda7b472"] != out["retraction rows"]["0dda7b472"]
def bound(c):
    row = next(l for l in show(c, "docs/POINT_REGISTER.md").split("\n") if l.startswith("| P-670"))
    return re.findall(r"5\.8 × 10(\S+)", row)
out["P-670 bound"] = {c: bound(c) for c in ["78edf8694", "7d7ab1dfa"]}
(HERE / "r81_recounts.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(out, ensure_ascii=False))
