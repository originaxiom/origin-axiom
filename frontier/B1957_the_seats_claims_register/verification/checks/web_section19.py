"""The web seat's status page, section 19 (its branch at b7d2b8b7e): what it says of main's record at 0ffa123c8, each
statement held against main's files at that commit.  Nothing of the seat's is run.
Z1  its lane's counts in the register at 0ffa123c8; Z2  the lane's records new or changed between 6f337047b and 0ffa123c8;
Z3  the N2 line of grounds_cite_records_that_exist at 0ffa123c8; Z4  that web-st18-03 there records HARVEST COMPLETE at
6f337047b, and that web-wa2-05-r3p there says it holds no statement while holding W-A2's line 113."""
import json, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "0ffa123c8"; V = "frontier/B1957_the_seats_claims_register/verification/"
w = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]
print("Z1: the web lane at %s: %s" % (AT, {k: w[k] for k in ("files", "read", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}))
ch = sorted(l.split("\t")[1].split("/")[-1][:-5] for l in git("diff", "--name-status", "6f337047b", AT, "--", V + "records/").split("\n") if l and "/web-" in l)
print("Z2: the lane's records new or changed between 6f337047b and %s: %d: %s" % (AT, len(ch), ch))
print("Z3: %s" % git("show", AT + ":" + V + "checks/grounds_cite_records_that_exist_run.txt").strip().split("\n")[-1])
r18 = json.loads(git("show", AT + ":" + V + "records/web-st18-03.json")); r3p = json.loads(git("show", AT + ":" + V + "records/web-wa2-05-r3p.json"))
print("Z4: web-st18-03 at %s names HARVEST COMPLETE at 6f337047b: %s; web-wa2-05-r3p says 'no statement under it': %s and holds W-A2's line 113: %s"
      % (AT, "HARVEST COMPLETE, written by the seat at main's 6f337047b" in r18["how"], "no statement under it" in r3p["note"], "web:CHAT1_TO_CC_2026-11-17_W-A2_POSTULATE_D_FROM_THE_GROUND:113" in r3p["units"]))
# Z5 to Z7 (added 2026-11-18, at the seat's corrected section 19, 04a72b04a)
t_main = int(git("show", "-s", "--format=%ct", AT).strip()); t_seat = int(git("show", "-s", "--format=%ct", "10c488d71").strip())
print("Z5: main committed %s %d seconds before the seat's withdrawal at 10c488d71" % (AT, t_seat - t_main))
s18 = json.loads(git("show", AT + ":" + V + "records/web-st18-01.json"))["units"]; first = git("show", "8bb9a1fcc:relays/STATUS_CHAT1.md").split("\n")
print("Z6: web-st18-01 at %s held the first version's lines 1830, 1831 and 1835: %s; they read: %s" % (AT, all("web:STATUS_CHAT1:%d" % n in s18 for n in (1830, 1831, 1835)), [first[n - 1][:60] for n in (1830, 1831, 1835)]))
empty = [l.split("/")[-1][:-5] for l in git("ls-tree", "--name-only", AT, V + "records/").split("\n") if l.endswith(".json")]
recs = {e: json.loads(git("show", "%s:%srecords/%s.json" % (AT, V, e))) for e in empty}
kept = [e for e, d in recs.items() if d.get("verdict") != "READ" and not d.get("units")]
print("Z7: records kept for their ground with no statement at %s: %d, of them the web lane's: %d" % (AT, len(kept), sum(1 for e in kept if e.startswith("web-"))))
