"""The web seat's status page, section 28 (its branch at 61a0684e0, the read version): what it says of main's record at
996638890 and of its own older files, held against main's files and the seat's branch.  Nothing of the seat's is run.
 J1  28.1: M69's mends at 996638890 (42 relay rows BANKED; P-876's closing note; companion_grounds.py; web-st26-02 holds 2706, 2723).
 J2  28.3: the lane's counts at 996638890.
 J3  28.4: B1957's FINDINGS at 996638890 records 51 rows taken in by the recount rule; the seven rows of (a) and their dispositions.
 J4  28.4 (b): the pin history's line on the first background; row 899's location cell; row 1088; P-356's clause on
     inverse_sm_all; the commit 6ce5dcc82 on the seat's branch; the attack note's section 2.5 names inverse_sm_all.
 J5  28.4 (a) 5: the P-327 relay at 5d4e3b11d and at 0cc73b1e6: where e19 appears.
 J6  28.4 (c): B1832 on the kernel lemma (P-524) and the exponent law (P-559); B1906 on the zero law (P-337)."""
import json, re, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "996638890"; V = "frontier/B1957_the_seats_claims_register/verification/"
RL = git("show", AT + ":docs/RELAY_LEDGER.md").split("\n"); L = git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n"); P = git("show", AT + ":docs/POINT_REGISTER.md").split("\n")
row = lambda n: next(l for l in L if l.startswith("| %d |" % n)); rec = lambda r: json.loads(git("show", "%s:%srecords/%s.json" % (AT, V, r)))
open_own = [l for l in RL if re.match(r"\| `CHAT1_TO_CC_", l) and " | OPEN | " in l]; banked_stale = sum(1 for l in RL if re.match(r"\| `CHAT1_TO_CC_", l) and "OPEN was stale" in l)
p876 = next(l for l in P if l.startswith("| P-876 |")); cg = git("show", AT + ":" + V + "checks/companion_grounds.py")
print("J1: at %s the seat's relays still OPEN: %d (all W-P1: %s); rows BANKED as stale: %d; P-876 closes its part: %s; companion_grounds names the move: %s; web-st26-02 holds 2706 and 2723: %s"
      % (AT, len(open_own), all("W-P1" in l for l in open_own), banked_stale, "the web seat's part of this point is closed" in p876, "names the line's move" in cg and "unnamed" in cg, all("web:STATUS_CHAT1:%d" % n in rec("web-st26-02")["units"] for n in (2706, 2723))))
sm = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]; U = json.loads(git("show", AT + ":" + V + "UNITS.json"))["units"]
print("J2: the lane at %s: %s, units %d" % (AT, {k: sm[k] for k in ("files", "read", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}, sum(1 for u in U if u[0].startswith("web:"))))
F = git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md").split("\n")
print("J3: FINDINGS' lines 287 to 295 at %s name 51 rows: %s; the dispositions of rows 1201, 1250, 1291, 1332, 1337, 1404, 1513: %s"
      % (AT, "51" in " ".join(F[286:295]), [re.sub(r"\*", "", row(n).split(" | ")[5])[:40] for n in (1201, 1250, 1291, 1332, 1337, 1404, 1513)]))
p356 = next(l for l in P if l.startswith("| P-356 |")); br = git("ls-tree", "-r", "--name-only", "6ce5dcc82")
print("J4: the pin history's line names the first background read at d40c1ab6e: %s; row 899's location cell: %s; row 1088: %s; P-356 says inverse_sm_all has no committed output: %s; 6ce5dcc82 on the seat's branch: %s, with inverse_sm_all_two_higgs.json: %s; the attack note's section 2.5 names inverse_sm_all: %s"
      % ("at `d40c1ab6`" in L[29] and "the first-background relay and its FINDINGS read at this head (row 899), nothing re-run" in L[29], row(899).split(" | ")[4][:80], row(1088).split(" | ")[5][:50], "inverse_sm_all has no committed output" in p356,
         subprocess.run(["git", "merge-base", "--is-ancestor", "6ce5dcc82", "origin/chat1/web-seat"]).returncode == 0, any(f.endswith("inverse_sm_all_two_higgs.json") for f in br.split("\n")), "inverse_sm_all" in git("show", "61a0684e0:relays/chat1_2026-10-23_attack/THE_NEXT_ATTACK.md")))
r1 = git("show", "5d4e3b11d:relays/CHAT1_TO_CC_AND_SM_2026-10-24_P327_THE_CUSPS_OF_THE_FIT_LINES.md"); r2 = git("show", "0cc73b1e6:relays/CHAT1_TO_CC_AND_SM_2026-10-24_P327_THE_CUSPS_OF_THE_FIT_LINES.md")
print("J5: the P-327 relay names e19 at 5d4e3b11d: %s; at 0cc73b1e6: %s" % ("e19" in r1, "e19" in r2))
b1832 = open(next(iter(__import__("glob").glob("frontier/B1832_*/FINDINGS.md")))).read(); b1906 = open(next(iter(__import__("glob").glob("frontier/B1906_*/FINDINGS.md")))).read()
print("J6: B1832 states the kernel lemma (T-KERNEL-SUM-TWIST, P-524) with a hostile referee owed: %s, and the exponent law of P-559: %s; B1906 states the zero law on every line (P-337): %s"
      % ("T-KERNEL-SUM-TWIST" in b1832 and "hostile referee" in b1832, "P-559's exponent law" in b1832, "the zero law on every line (P-337)" in b1906))
