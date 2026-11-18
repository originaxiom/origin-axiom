"""The web seat's status page, section 21 (its branch at 9dccd2062): what it says of main's record at cdf78dd95, each
statement held against main's files there.  Nothing of the seat's is run."""
import json, re, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "cdf78dd95"; V = "frontier/B1957_the_seats_claims_register/verification/"
rec = lambda r: json.loads(git("show", "%s:%srecords/%s.json" % (AT, V, r)))
dt = int(git("show", "-s", "--format=%ct", "d3ecf1dea").strip()) - int(git("show", "-s", "--format=%ct", AT).strip())
F = git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md").split("\n"); CS = git("show", AT + ":docs/CAMPAIGN_STATUS.md").split("\n")
L = git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n"); P = git("show", AT + ":docs/POINT_REGISTER.md").split("\n"); RV = git("show", AT + ":docs/views/CONTEXT_RECOVERY.md").split("\n")
row = lambda n: next(l for l in L if l.startswith("| %d |" % n)); pin = next(l for l in L if l.startswith("| chat1 | `origin/chat1/web-seat`"))
p865 = next(l for l in P if l.startswith("| P-865 |")); p873 = next(l for l in P if l.startswith("| P-873 |"))
print("C1: main committed %s %d seconds before the seat's withdrawal at d3ecf1dea; the word announced at %s in FINDINGS: %s, CAMPAIGN_STATUS line 5: %s, row 1935: %s, the pin row: %s, P-865: %s, the recovery view: %s"
      % (AT, dt, AT, any("HARVEST COMPLETE AGAIN" in l for l in F), "HARVEST COMPLETE AGAIN" in CS[4], "HARVEST COMPLETE, WRITTEN AGAIN" in row(1935), "written again" in pin, "WROTE HARVEST COMPLETE AGAIN" in p865, any("AGAIN" in l and "HARVEST COMPLETE" in l for l in RV)))
s20 = rec("web-st20-01"); first = git("show", "5322929cd:relays/STATUS_CHAT1.md").split("\n")
print("C2: web-st20-01 at %s holds the first version's line 1990: %s; it reads: %s" % (AT, "web:STATUS_CHAT1:1990" in s20["units"], first[1989][:90]))
s18 = rec("web-st18-01"); y4 = git("show", AT + ":" + V + "checks/web_section18_run.txt").strip().split("\n")[-1]
print("C3: web-st18-01's note names the three statements: %s; Y4 at %s: %s; the pin row and row 1932 carry the account: %s, %s; M59's correction: %s"
      % ("that the records of section 17 stated it rightly" in s18["note"] and "that web-wa3-04's ground named" in s18["note"] and "that the read-out computed" in s18["note"], AT, y4[y4.index("in its ground"):y4.index(";")], "three of the statements held were wrong" in pin, "web-st18-01 held VERIFIED three lines" in row(1932), "Three of the statements it calls holding were wrong" in git("show", AT + ":docs/seats/chat1.md")))
own = {}
for l in git("ls-tree", "--name-only", AT, V + "records/").split("\n"):
    if "/web-" in l and l.endswith(".json"):
        d = json.loads(git("show", AT + ":" + l))
        for u in d.get("units", []): own[u] = d["id"]
want = {"web-wa2-02": [25, 35, 37, 42], "web-wa3-02": [49, 165], "web-wa3-05-r3c": [116], "web-wf16-01-r3p": [19], "web-wf17-04": [236]}
files = {"web-wa2-02": "W-A2_POSTULATE_D_FROM_THE_GROUND", "web-wa3-02": "W-A3_THE_COVER_THE_CLASS_AND_THE_UP_SECTOR", "web-wa3-05-r3c": "W-A3_THE_COVER_THE_CLASS_AND_THE_UP_SECTOR", "web-wf16-01-r3p": "W-F16_THE_TWO_WAY_CHOICES_SETTLE_EACH_OTHER", "web-wf17-04": "W-F17_SECOND_COMPUTATIONS_FOR_COMPUTED_NOWHERE"}
ok = all(own.get(next(u for u in own if files[r] in u and u.endswith(":%d" % n)), None) == r for r, ns in want.items() for n in ns)
print("C4: the five records' lines sit in the receivers named, at %s: %s; web-wf17-04-r3c holds W-F17's line 139: %s; P-873 names H4: %s; FINDINGS lines naming H4: %s"
      % (AT, ok, own.get(next(u for u in own if "W-F17_SECOND" in u and u.endswith(":139"))) == "web-wf17-04-r3c", "H4" in p873, [i + 1 for i, l in enumerate(F) if "H4" in l][:4]))
w = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]; n2 = git("show", AT + ":" + V + "checks/grounds_cite_records_that_exist_run.txt").strip().split("\n")[-1]
t2 = git("show", AT + ":" + V + "checks/third_reading_web_run.txt").strip().split("\n")[-1]; lock = git("show", AT + ":" + V + "test_b1957_register.py")
print("C5: the lane at %s: %s; N2 %s; the lock exempts web-st19b and web-st20 by name: %s; %s"
      % (AT, {k: w[k] for k in ("files", "read", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}, n2[n2.index("each saying"):], '"web-st19b-"' in lock and '"web-st20-"' in lock, t2))
s3 = rec("web-st17-03"); s14 = rec("web-st14-04"); r1930 = row(1930)
print("C6: still open at %s: web-st17-03 %s with %d units; web-st14-04's false reason present: %s; web-wa2-05v's: %s; row 1930's bracket names the three: %s"
      % (AT, s3["verdict"], len(s3["units"]), "its level 8 not being read out" in s14["how"], "the level 8 of line 116 are not read out by main." in rec("web-wa2-05v")["note"], "three of the statements" in r1930))
