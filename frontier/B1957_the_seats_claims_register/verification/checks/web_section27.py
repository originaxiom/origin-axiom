"""The web seat's status page, section 27 (its branch at e46bbc14c, the read version): what it says of main's record at
1a70d5dbe, each statement held against main's files there.  Nothing of the seat's is run.
 H1  27.1: the records and brackets M68 names; N2's last line; FINDINGS' line 765.
 H2  27.1 (f): the sweep's figures under the seat's four keys; I26_DECISION_TABLE.md's class; harvest row 530's location cell.
 H3  27.2: web-st26-01 to -04's sizes; lines 2706 and 2723 in web-st26-01.
 H4  27.3: the lane's counts; the third reading's last line; the exemption of web-st26-.
 H5  27.4 (a): the relay ledger's rows of the seat's own relays marked OPEN; which are in the register with nothing pending.
 H6  27.4 (b): P-876 and the point register's line 53; the seat's map of its 13 rows naming no file, against the rows' cells
     and the register.
 H7  27.4 (c): companion_grounds.py's docstring and printed label.
 H8  27.5: the relay ledger's row for card W-P1; web-wp1-01 to -04; web-st24-02's ground."""
import json, re, subprocess, collections
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "1a70d5dbe"; V = "frontier/B1957_the_seats_claims_register/verification/"
rec = lambda r: json.loads(git("show", "%s:%srecords/%s.json" % (AT, V, r)))
F = git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md").split("\n"); P = git("show", AT + ":docs/POINT_REGISTER.md").split("\n")
L = git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n"); RL = git("show", AT + ":docs/RELAY_LEDGER.md").split("\n")
row = lambda n: next(l for l in L if l.startswith("| %d |" % n))
n2 = git("show", AT + ":" + V + "checks/grounds_cite_records_that_exist_run.txt").strip().split("\n")[-1]
print("H1: web-st25-04 %s holds 2582: %s; row 1951 bracketed at (a): %s; web-st24-01's note says 'placed and named': %s; web-st22-02 names e9279d8eb: %s; FINDINGS' line 765 carries the corrected count: %s; N2 ends: %s"
      % (rec("web-st25-04")["verdict"], "web:STATUS_CHAT1:2582" in rec("web-st25-04")["units"], "does not stand for its line 2582" in row(1951), "placed and named" in rec("web-st24-01")["note"], "e9279d8eb" in rec("web-st22-02")["note"], "337 outside" in F[764], n2[-40:]))
o = json.loads(git("show", AT + ":" + V + "checks/older_rows.json")); keys = ("chat1 (owner-relayed, 2026-09-15)", "web seat (chat1)", "the web seat (chat1)", "chat1")
cls = collections.Counter(st for k in keys for st in o[k]["files"].values())
print("H2: at %s the four keys: rows %d, naming no file %d, files %d: %s; I26_DECISION_TABLE.md: %s; row 530's location cell names the folder: %s"
      % (AT, sum(len(o[k]["rows"]) for k in keys), sum(len(o[k]["rows_no_file"]) for k in keys), sum(len(o[k]["files"]) for k in keys), dict(cls), o[keys[0]]["files"].get("I26_DECISION_TABLE.md"), "chat1_i26_decision_table_2026-09-15/" in row(530).split(" | ")[4]))
s26 = {r: rec(r) for r in ("web-st26-01", "web-st26-02", "web-st26-03", "web-st26-04")}
print("H3: web-st26-01 to -04 hold %s; 2706 and 2723 in web-st26-01: %s" % ([len(d["units"]) for d in s26.values()], ["web:STATUS_CHAT1:%d" % n in s26["web-st26-01"]["units"] for n in (2706, 2723)]))
sm = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]; U = json.loads(git("show", AT + ":" + V + "UNITS.json"))["units"]
t3 = git("show", AT + ":" + V + "checks/third_reading_web_run.txt").strip().split("\n")[-1]; lock = git("show", AT + ":" + V + "test_b1957_register.py")
print("H4: the lane at %s: %s, units %d; the third reading: %s; web-st26- exempt in the lock and the third reading: %s, %s"
      % (AT, {k: sm[k] for k in ("files", "read", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}, sum(1 for u in U if u[0].startswith("web:")), t3[-3:], '"web-st26-"' in lock, '"web-st26-"' in git("show", AT + ":" + V + "checks/third_reading_web.py")))
regfiles = collections.Counter(); pend = collections.Counter(); held = set()
for l in git("ls-tree", "--name-only", AT, V + "records/").split("\n"):
    if l.endswith(".json"): held |= set(json.loads(git("show", AT + ":" + l)).get("units", []))
SU = json.loads(git("show", AT + ":" + V + "UNITS.json"))["units"]
for u in SU:
    if u[0].startswith("web:"): f = u[0].split(":")[1].split("/")[-1]; regfiles[f] += 1; pend[f] += (u[2] == "s" and u[0] not in held)
own = [(i + 1, re.search(r"`([^`]+)`", l).group(1)) for i, l in enumerate(RL) if l.startswith("| `") and " | OPEN | " in l and re.search(r"`(CHAT1_TO_CC_[^`]+)`", l)]
reg = [(n, f) for n, f in own if f[:-3] in regfiles]; unreg = [(n, f) for n, f in own if f[:-3] not in regfiles]
print("H5: at %s the relay ledger marks %d of the seat's own relays OPEN; %d in the register (statements pending under them: %d); not in it: %s"
      % (AT, len(own), len(reg), sum(pend[f[:-3]] for _, f in reg), [(n, f[:60]) for n, f in unreg]))
p876 = next(l for l in P if l.startswith("| P-876 |"))
print("H6: P-876 at %s queues the seat's 13 rows: %s; line 53 says the harvest is not complete while it is open: %s" % (AT, "its 13 rows that name no file" in p876, "not complete while it is open" in P[52]))
regpaths = {u[0].split(":")[1] for u in SU if u[0].startswith("web:")}
has = lambda s: any(s in p for p in regpaths)
mp = {1143: has("chat1_2026-10-14_the_first_row/FINDINGS"), 1304: has("THREADS_WITH_INGREDIENTS"), 1317: has("ZERO_FREE_FRAME_EXPLORATION"), 1322: has("ZERO_FREE_HOLOMORPHIC_RULE"), 1323: has("TICK_LINE_HIGGS_RULE"),
      1338: "read in full and registered" in row(1338), 1340: "read in full and registered" in row(1340), 1342: "read in full and registered" in row(1342),
      1642: row(1652).split(" | ")[5].startswith("**VERIFIED") and "B1868" in row(1652), 1686: "ROW 1691" in row(1686), 1822: has("W-F17_SECOND_COMPUTATIONS") and "Addendum 2" in git("show", "e46bbc14c:relays/CHAT1_TO_CC_2026-11-14_W-F17_SECOND_COMPUTATIONS_FOR_COMPUTED_NOWHERE.md"),
      1833: has("W-F24_WHERE_FRAME") and has("CHAT1_W-F24_"), 1848: "READ AT ITS SOURCE" in row(1848)}
print("H6: the seat's map, row by row, held at main's files: %s; row 1143's relay CHAT1_TO_CC_2026-10-14_THE_FIRST_ROW.md is in the register: %s (its row: read in full in its day: %s)"
      % (mp, has("CHAT1_TO_CC_2026-10-14_THE_FIRST_ROW"), "read in full" in row(1143)))
cg = git("show", AT + ":" + V + "checks/companion_grounds.py"); cgr = git("show", AT + ":" + V + "checks/companion_grounds_run.txt")
print("H7: at %s companion_grounds.py says 'dated move': %s; its run prints 'placed without a dated move named': %s" % (AT, "dated move" in cg, "placed without a dated move named" in cgr))
w1386 = next(l for l in RL if l.startswith("| `CHAT1_TO_CC_2026-11-18_W-P1_THE_PROCESS_READING.md`"))
T = {u[0]: u for u in SU}
pg = git("show", "e46bbc14c:relays/STATUS_CHAT1.md").split("\n")
print("H8: the relay ledger's row for card W-P1: BANKED %s, names web-wp1-01 to -04: %s; those records hold %s statements; web-st24-02 (%s) holds line 2243: %s, which reads 'the move is dated': %s; its note says so: %s"
      % (" | BANKED | " in w1386, "web-wp1-01 to -04" in w1386, [len(rec("web-wp1-0%d" % i)["units"]) for i in range(1, 5)], rec("web-st24-02")["verdict"], "web:STATUS_CHAT1:2243" in rec("web-st24-02")["units"], "the move is dated" in pg[2242], "dated" in rec("web-st24-02").get("note", "")))
print("H5b: the seat's count: 41 in the register + line 1241 + three W-P1 step relays = %d OPEN, where section 27.4 (a) says 44" % (41 + 1 + 3))
# H9: 27.4 (a)'s sub-lines and 27.5's line on its own page
win = [n for n, f in reg if "not in B1957's window" in RL[n - 1] or "not in B1957" in RL[n - 1]]
same = {c: sum(1 for l in git("show", c + ":docs/RELAY_LEDGER.md").split("\n") if l.startswith("| `CHAT1_TO_CC_") and " | OPEN | " in l) for c in ("23cd5a5ca", "d18e3c30c", AT)}
pg = git("show", "e46bbc14c:relays/STATUS_CHAT1.md").split("\n")
own2503 = [(json.loads(git("show", AT + ":" + l))["id"], json.loads(git("show", AT + ":" + l))["verdict"]) for l in git("ls-tree", "--name-only", AT, V + "records/").split("\n") if l.endswith(".json") and "/web-st2" in l and "web:STATUS_CHAT1:2502" in json.loads(git("show", AT + ":" + l)).get("units", [])]
print("H9: of the 41 registered OPEN rows, %d say 'not in B1957's window' (lines %s to %s); the seat's OPEN relay rows at 23cd5a5ca, d18e3c30c, %s: %s; its page's line 2503 (the unit starting at 2502) says 'the three records whose reasons' and 'overturned': %s, held by %s"
      % (len(win), min(win), max(win), AT, same, "the three records whose reasons" in " ".join(pg[2501:2504]) and "overturned" in " ".join(pg[2501:2504]), own2503))
