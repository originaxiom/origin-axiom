"""B1957: main's own reading of the physical lane's verified statements (2026-11-18). The lane read every record of its own
lane itself, so no sorter read it at the second reading; main read all 1,390 statements that stood verified, one by one,
each against its record's full ground. The list second_reading/physical_unmarked.json names every line read and every line
narrowed, with main's reason. This script checks the list against the records.
 P1  each narrowed line sits in one record, the parent's -r3 companion, with the listed verdict; each other line read is
     verified now.
 P2  every statement of the lane that is verified now was read by main one by one: in this list, or in a record written
     since from main's own reading of the lane's later packages."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; V = HERE.parent
L = json.loads((V / "second_reading" / "physical_unmarked.json").read_text())
owner = collections.defaultdict(list)
for q in (V / "records").glob("physical-*.json"):
    d = json.loads(q.read_text())
    for u in d.get("units", []): owner[u].append((d["id"], d["verdict"]))
want = {"P": "PARTIAL", "N": "NOTED", "C": "CONDITIONAL"}; bad = []
for x in L["units"]:
    o = owner.get(x["unit"], [])
    if len(o) != 1 or o[0] != ("%s-r3%s" % (x["record"], x["decision"].lower()), want[x["decision"]]): bad.append((x["unit"], o))
narrowed = {x["unit"] for x in L["units"]}; kept = [u for u in L["read_units"] if u not in narrowed]
later = [u for u in kept if not (len(owner.get(u, [])) == 1 and owner[u][0][1] == "VERIFIED")]
print("P1: lines read: %d; narrowed: %d (%s); kept verified: %d; narrowed lines not where the list says: %d; kept lines not under a verified record now: %d"
      % (L["read"], len(L["units"]), ", ".join("%s %d" % (want[k].lower(), v) for k, v in sorted(L["decisions"].items())), len(kept), len(bad), len(later)))
ver = {u: o[0][0] for u, o in owner.items() if o[0][1] == "VERIFIED"}
since = ("physical-m16b-", "physical-c3i-", "physical-pr-", "physical-nr-")      # records written after the reading from main's own reading of the lane's later packages (2026-11-18, later)
cover = collections.Counter("read here" if u in set(kept) else "in a record written since from main's reading" if ver[u].startswith(since) and since else "NOT READ ONE BY ONE" for u in ver)
print("P2: the lane's verified statements now: %d; %s" % (len(ver), "; ".join("%s: %d" % kv for kv in sorted(cover.items()))))
print("P2: verified statements main has not read one by one against the record's ground: %d" % cover.get("NOT READ ONE BY ONE", 0))
