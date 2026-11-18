"""The web seat's status page, section 25 as corrected after its referee read (its branch at 614bff48d): what it says of main's
record at 23cd5a5ca, each statement held against main's files there.  Nothing of the seat's is run.
 K1  the companion survey at 23cd5a5ca (companion_grounds.py's rule): companions, silent notes, placed lines; of the placed lines,
     how many have a date (2026-) within 200 characters of the line's mention in the receiving record's ground or note.
 K2  web-r79b-01's REVIEW_79B lines 20, 22, 29: VERIFIED at 23cd5a5ca; the first commit at which each came into the record.
 K3  units 2240, 2437, 2456 at 23cd5a5ca: held VERIFIED in web-st24-01; web-st24-02 holds 2243, 2444, 2450; web-st22-02's units
     and whether its note names the line it lost.
 K4  the lane's counts at 23cd5a5ca; the lock's exemptions."""
import json, re, subprocess, importlib.util, pathlib
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "23cd5a5ca"; V = "frontier/B1957_the_seats_claims_register/verification/"; HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "companion_grounds.py").read_text(); g = {}; exec(src[:src.index("for at, lab in")], g)
recs = g["load"](AT); c, s, n, p, a, u = g["survey"](recs, "web-")
owner = {x: k for k, r in recs.items() for x in r.get("units", [])}
dated = 0; total = 0
for k, r in recs.items():
    if not k.startswith("web-") or not re.search(r"-r[23][pncs]$", k): continue
    h = r.get("how", ""); nums = set()
    for m in re.finditer(r"Lines?: ([\d, ]+)", h): nums |= set(re.findall(r"\d+", m.group(1)))
    nums |= set(re.findall(r"\bline (\d+):", h)); i = h.find("by line")
    if i >= 0: nums |= set(re.findall(r"(?:\): |; )(\d+): ", h[i:]))
    held = {x.rsplit(":", 1)[1] for x in r.get("units", [])}
    parent = re.sub(r"-r[23][pncs]$", "", k); tags = set()
    for cc in recs:
        if cc == k or cc == parent or cc.startswith(parent + "-r"): tags |= {x.split(":")[1] for x in recs[cc].get("units", [])}
    for num in nums - held:
        cand = [x for x in owner if x.rsplit(":", 1)[1] == num and x.split(":")[1] in tags and owner[x] != k]
        if len(cand) != 1: continue
        total += 1; txt = recs[owner[cand[0]]].get("note", "") + " " + recs[owner[cand[0]]].get("how", "")
        dated += any("2026-" in txt[max(0, m.start() - 200): m.end() + 200] for m in re.finditer(r"\b%s\b" % num, txt))
print("K1: at %s: companions %d, silent %d, placed %d (%s); of the placed lines, with a date within 200 characters of the line's mention: %d of %d" % (AT, c, s, n, p, dated, total))
R79 = "web:REVIEW_79B_CHAT1:"
w = json.loads(git("show", "%s:%srecords/web-r79b-01.json" % (AT, V)))
first = {}
for cm in git("log", "--format=%h", "--reverse", AT, "--", V + "records/web-r79b-01.json").split():
    d = json.loads(git("show", "%s:%srecords/web-r79b-01.json" % (cm, V)))
    for ln in (20, 22, 29):
        if R79 + str(ln) in d["units"] and ln not in first: first[ln] = cm
print("K2: web-r79b-01 at %s %s holds lines 20, 22, 29: %s; the first commit at which each came in: %s" % (AT, w["verdict"], [R79 + str(x) in w["units"] for x in (20, 22, 29)], first))
# K2b (added 2026-11-18, later, at the seat's section 26.2 (e)): K2 prints each line's FIRST presence, which does not show when the
# lines came back; the record's history does: at each commit that changed it, which of the three lines it holds.
hist = []
for cm in git("log", "--format=%h", "--reverse", AT, "--", V + "records/web-r79b-01.json").split():
    d = json.loads(git("show", "%s:%srecords/web-r79b-01.json" % (cm, V))); hist.append("%s %s" % (cm, [ln for ln in (20, 22, 29) if R79 + str(ln) in d["units"]]))
print("K2b: web-r79b-01's history up to %s, the lines 20, 22, 29 it holds at each commit that changed it: %s" % (AT, "; ".join(hist)))
rec = lambda r: json.loads(git("show", "%s:%srecords/%s.json" % (AT, V, r)))
s1, s2, s22 = rec("web-st24-01"), rec("web-st24-02"), rec("web-st22-02")
print("K3: at %s web-st24-01 (%s) holds 2240, 2437, 2456: %s; web-st24-02 holds %s; web-st22-02 holds %s, its note names a lost line: %s"
      % (AT, s1["verdict"], ["web:STATUS_CHAT1:%d" % x in s1["units"] for x in (2240, 2437, 2456)], [x.rsplit(":", 1)[1] for x in s2["units"]], [x.rsplit(":", 1)[1] for x in s22["units"]], "lost" in s22.get("note", "") or "left" in s22.get("note", "")))
wl = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]; lock = git("show", AT + ":" + V + "test_b1957_register.py")
print("K4: the lane at %s: %s; the lock exempts web-st24 and web-st24j: %s" % (AT, {k: wl[k] for k in ("files", "read", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}, '"web-st24-"' in lock and '"web-st24j-"' in lock))
