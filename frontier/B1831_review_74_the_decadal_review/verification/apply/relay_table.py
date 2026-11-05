"""Review 74: the two relay readers' proposals as one table {ledger line: (disposition, evidence)}."""
import re, json, pathlib
R = pathlib.Path(__file__).resolve().parents[1] / "relays"
rows = {}
old = (R / "OLDER_HALF.md").read_text(encoding="utf-8")
for m in re.finditer(r"\*\*(\d+)\. `([^`]+)`[^\n]*?— lines? (\d+)[^\n]*?\*\*(.*?)(?=\n\*\*\d+\. `|\n## |\Z)", old, re.S):
    body = m.group(4); p = re.search(r"- Proposed:\s*(.*?)(?:\n- |\n\n|\Z)", body, re.S)
    if not p: p = re.search(r"(\*\*(?:BANKED|DECLINED)[^*]*\*\*[^\n]*)", body)
    rows[int(m.group(3))] = dict(name=m.group(2), proposed=" ".join(p.group(1).split()) if p else "?", half="older", body=" ".join(body.split())[:900])
new = (R / "NEWER_HALF.md").read_text(encoding="utf-8")
for b in re.split(r"\n### ", new)[1:]:
    m = re.match(r"(\d+) `([^`]+)`", b); p = re.search(r"Proposed disposition:\s*(.*)", b)
    if m: rows[int(m.group(1))] = dict(name=m.group(2), proposed=p.group(1).strip() if p else "?", half="newer")
for k in sorted(rows):
    d = rows[k]; disp = "BANKED" if "BANKED" in d["proposed"][:40] else "DECLINED" if "DECLINED" in d["proposed"][:40] else "OPEN" if "OPEN" in d["proposed"][:40] else "?"
    d["disp"] = disp
json.dump(rows, open(pathlib.Path(__file__).with_name("relay_table.json"), "w"), ensure_ascii=False, indent=1)
import collections
print(len(rows), collections.Counter(d["disp"] for d in rows.values()))
for k in sorted(rows):
    if rows[k]["disp"] in ("?", "OPEN", "DECLINED"): print(k, rows[k]["disp"], rows[k]["name"][:60], "|", rows[k]["proposed"][:150])
