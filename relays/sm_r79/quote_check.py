#!/usr/bin/env python3
"""SM-R79: every quotation in this seat's Review 79 findings, checked by machine against the file at main's commit.

Usage: quote_check.py FINDINGS.json OUT.json [REPO]

FINDINGS.json is a list of {"id", "arc", "file", "quote"[, "commit"]}. Each quote must occur verbatim in
`git show COMMIT:file`, COMMIT being the row's own commit where it names one (M4's rows: main at 0dda7b472).
Control: a copy of the first quote with one character changed must be reported missing, or the check is broken."""
import json
import subprocess
import sys
from pathlib import Path

COMMIT = "323f923278181ffbe69f8c3124182549ab0e3163"
rows = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
repo = sys.argv[3] if len(sys.argv) > 3 else "."
cache = {}


def text(path, commit=COMMIT):
    if (commit, path) not in cache:
        r = subprocess.run(["git", "-C", repo, "show", f"{commit}:{path}"], capture_output=True)
        cache[(commit, path)] = r.stdout.decode("utf-8") if r.returncode == 0 else None
    return cache[(commit, path)]


out = {"commit": COMMIT, "rows": []}
for r in rows:
    t = text(r["file"], r.get("commit", COMMIT))
    found = t is not None and r["quote"] in t
    out["rows"].append({"id": r["id"], "commit": r.get("commit", COMMIT)[:9], "file": r["file"], "file_exists": t is not None, "quote_found": found,
                        "occurrences": t.count(r["quote"]) if t else 0})
first = rows[0]
q = first["quote"]
k = len(q) // 2
altered = q[:k] + ("X" if q[k] != "X" else "Y") + q[k + 1:]
t = text(first["file"])
out["control_altered_quote_reported_missing"] = t is not None and altered not in t
out["all_found"] = all(x["quote_found"] for x in out["rows"])
out["ok"] = out["all_found"] and out["control_altered_quote_reported_missing"]
Path(sys.argv[2]).write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=1))
for x in out["rows"]:
    if not x["quote_found"]:
        print("MISSING:", x["id"], x["file"])
