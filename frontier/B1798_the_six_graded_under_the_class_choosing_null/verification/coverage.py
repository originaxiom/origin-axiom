import json, pathlib, sys
D = pathlib.Path(__file__).resolve().parent / "b1753_all266"
keys = set()
for p in (D / "census_ext.jsonl", D / "census_ext_tail.jsonl"):
    if not p.exists(): continue
    for l in p.read_text(encoding="utf-8").splitlines():
        try: r = json.loads(l)
        except json.JSONDecodeError: continue
        keys.add((r["apex"], r["line"]))
print(len(keys))
