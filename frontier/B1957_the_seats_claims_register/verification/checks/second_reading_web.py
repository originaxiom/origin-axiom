"""B1957: the second reading of the web lane's verified statements (2026-11-18), held against the records as they stand.
second_reading/web.json lists every statement a read-only sorter marked as possibly not covered by its record's ground,
with the sorter's class and reason and main's decision.  This script checks that the records say what that list says, and
counts.  Data-free; it reads the register's own files."""
import json, pathlib, collections
V = pathlib.Path(__file__).resolve().parent.parent
L = json.loads((V / "second_reading" / "web.json").read_text()); units = {u[0] for u in json.loads((V / "UNITS.json").read_text())["units"]}
owner = {}
for q in (V / "records").glob("*.json"):
    d = json.loads(q.read_text())
    for u in d.get("units", []): owner.setdefault(u, []).append((d["id"], d["verdict"]))
want = {"K": "VERIFIED", "N": "NOTED", "C": "CONDITIONAL", "P": "PARTIAL", "S": "SUPERSEDED"}; bad = []; twice = [u for u, o in owner.items() if len(o) > 1]      # S added 2026-11-18: a kept line the seat itself later withdrew
for x in L["units"]:
    o = owner.get(x["unit"], [])
    if x["unit"] not in units or len(o) != 1 or o[0][1] != want[x["decision"]]: bad.append((x["unit"], x["decision"], o))
    elif x["decision"] != "K" and not o[0][0].startswith(x["record"] + "-r2"): bad.append((x["unit"], "not in the parent's companion", o))
    elif x["decision"] == "K" and o[0][0] != x["record"]: bad.append((x["unit"], "kept, but not in its parent", o))
by = collections.Counter(x["decision"] for x in L["units"]); cls = collections.Counter((x["class"], x["decision"]) for x in L["units"])
print("S1: candidates listed: %d (of %d verified statements the sorters read); decisions: kept verified %d, partial %d, noted %d, conditional %d" % (len(L["units"]), L["sorted"], by["K"], by["P"], by["N"], by["C"]))
print("S2: by the sorters' class: %s" % {c: {d: cls[(c, d)] for d in "KPNC" if cls[(c, d)]} for c in "abcdet"})
print("S3: listed statements whose record does not carry the decision's verdict, or that sit in two records: %d and %d" % (len(bad), len(twice)))
web = [o[0] for u, o in owner.items() if u.startswith("web:")]; v = collections.Counter(x[1] for x in web)
print("S4: the web lane's units by verdict now: %s; companions of the second reading: %d records" % (dict(sorted(v.items())), len({o[0][0] for o in owner.values() if o[0][0].endswith(("-r2n", "-r2c", "-r2p"))})))
