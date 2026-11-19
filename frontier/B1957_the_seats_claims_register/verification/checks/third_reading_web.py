"""B1957: main's own reading of the web lane's verified statements that no sorter had marked (2026-11-18, at the web seat's
section 15.3: every verified statement held against its record's ground, none skipped).  The list second_reading/web_unmarked.json
names every line main read (990) and every line it narrowed, with the reason.  This script checks the list against the records,
and counts what the two readings together cover.
 T1  each narrowed line sits in one record with the listed verdict; each other line read is verified now.
 T2  every statement of the lane that is verified now was read by main one by one: in the second reading's list of marked
     lines (kept), in this list, or in a record written since from main's own reading of the seat's page."""
import json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; V = HERE.parent
L = json.loads((V / "second_reading" / "web_unmarked.json").read_text()); M = json.loads((V / "second_reading" / "web.json").read_text())
owner = collections.defaultdict(list); rec = {}
for q in (V / "records").glob("web-*.json"):
    d = json.loads(q.read_text()); rec[d["id"]] = d
    for u in d.get("units", []): owner[u].append((d["id"], d["verdict"]))
want = {"P": "PARTIAL", "N": "NOTED", "C": "CONDITIONAL"}; bad = []
for x in L["units"]:
    o = owner.get(x["unit"], [])
    home = x["record"] if x.get("whole_record") else "%s-r3%s" % (x["record"], x["decision"].lower())
    if len(o) != 1 or o[0] != (home, want[x["decision"]]): bad.append((x["unit"], o))
narrowed = {x["unit"] for x in L["units"]}; kept = [u for u in L["read_units"] if u not in narrowed]
later = [u for u in kept if not (len(owner.get(u, [])) == 1 and owner[u][0][1] == "VERIFIED")]
print("T1: lines read: %d; narrowed: %d (%s); kept verified: %d; narrowed lines not where the list says: %d; kept lines not under a verified record now: %d"
      % (L["read"], len(L["units"]), ", ".join("%s %d" % (want[k].lower(), v) for k, v in sorted(L["decisions"].items())), len(kept), len(bad), len(later)))
ver = {u: o[0][0] for u, o in owner.items() if o[0][1] == "VERIFIED"}
marked_kept = {x["unit"] for x in M["units"] if x["decision"] == "K"} | {e["unit"] for e in json.loads((V / "second_reading" / "web_rv55.json").read_text())["entries"] if e["main"] == "V"}; since = {u for u, r in ver.items() if r.startswith(("web-st14-", "web-st15-", "web-st16-", "web-st17-", "web-st18-", "web-st18b-", "web-st19-", "web-st19b-", "web-st20-", "web-st20b-", "web-st21-", "web-st22-", "web-st21b-", "web-st23-", "web-st24-", "web-st24j-", "web-wp1-", "web-st25-", "web-st26-", "web-st27-", "web-old-", "web-st28-", "web-lbl-", "web-st29-33-", "web-st17-03b", "web-rv55-"))}      # restored at the seat's own reading (rv55), each row read by main
cover = collections.Counter("marked at the second reading and kept, or restored at the seat's own reading" if u in marked_kept else "read here" if u in set(kept) else "in a record written from main's reading of the seat's sections 14 to 16 and its rv55 findings" if u in since else "NOT READ ONE BY ONE" for u in ver)
print("T2: the lane's verified statements now: %d; %s" % (len(ver), "; ".join("%s: %d" % kv for kv in sorted(cover.items()))))
print("T2: verified statements main has not read one by one against the record's ground: %d" % cover.get("NOT READ ONE BY ONE", 0))
