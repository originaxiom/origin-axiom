#!/usr/bin/env python3
"""SM-R79b: the foundation's status cells at versions 1.64, 1.65 and 1.66, read by this seat's own parser (B1886's and B1891's
claims: none gone and none changed at 1.65; no item added and no status cell changed at 1.66).  Usage: status_cells_check.py OUT.json"""
import json, re, subprocess, sys
VERS = {"v1.64": "8f0b03814", "v1.65": "9ace774f4", "v1.66": "896cae025"}
ID = re.compile(r"^(PF\d|GM\d[a-d]?|SE\d|T-ROOT|FK\d+)\b")


def cells_of(line):
    # split on | that is not escaped and not inside backticks
    out, cur, tick = [], "", False
    s = line.strip()
    for i, ch in enumerate(s):
        if ch == "`":
            tick = not tick
        if ch == "|" and not tick and (i == 0 or s[i - 1] != "\\"):
            out.append(cur); cur = ""
        else:
            cur += ch
    out.append(cur)
    return [c.strip() for c in out[1:-1]]


def read(commit):
    t = subprocess.run(["git", "show", commit + ":GENESIS.md"], capture_output=True, text=True, check=True).stdout
    lines = t.split("\n")
    tables, i = [], 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and re.fullmatch(r"\s*\|[\s:|-]+\|?\s*", lines[i + 1]):
            head = cells_of(lines[i]); rows = []; j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append(cells_of(lines[j])); j += 1
            tables.append((head, rows)); i = j
        else:
            i += 1
    status = {}
    ident = {}
    for head, rows in tables:
        low = [h.lower().strip("* ") for h in head]
        si = low.index("status") if "status" in low else None
        for r in rows:
            if si is not None and si < len(r):
                status[" | ".join(head) + " :: " + r[0]] = r[si]
            m = ID.match(r[0].strip("* ")) if r else None
            if m and m.group(1) not in ident:
                ident[m.group(1)] = r
    return {"tables": len(tables), "status_rows": status, "identifier_rows": {k: v for k, v in ident.items()}}


R = {v: read(c) for v, c in VERS.items()}
sc = lambda k, row: row[3] if k.startswith("PF") else row[2]     # the status column: the fourth for PF rows, the third otherwise
out = {"versions": VERS}
for v in R:
    out[v] = {"tables": R[v]["tables"], "status_rows": len(R[v]["status_rows"]), "identifier_rows": len(R[v]["identifier_rows"])}
for a, b in (("v1.64", "v1.65"), ("v1.65", "v1.66")):
    A, B = R[a]["status_rows"], R[b]["status_rows"]
    out[f"{a}->{b}"] = {"status_rows_gone": sorted(set(A) - set(B)), "status_rows_new": sorted(set(B) - set(A)),
                        "status_changed": sorted(k for k in set(A) & set(B) if A[k] != B[k]),
                        "identifier_status_changed": sorted(k for k in set(R[a]["identifier_rows"]) & set(R[b]["identifier_rows"])
                                                            if sc(k, R[a]["identifier_rows"][k]) != sc(k, R[b]["identifier_rows"][k])),
                        "identifiers_gone": sorted(set(R[a]["identifier_rows"]) - set(R[b]["identifier_rows"])),
                        "identifiers_new": sorted(set(R[b]["identifier_rows"]) - set(R[a]["identifier_rows"]))}
json.dump(out, open(sys.argv[1], "w"), indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False)[:3000])
