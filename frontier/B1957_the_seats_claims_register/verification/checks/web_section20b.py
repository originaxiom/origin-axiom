"""The web seat's section 20 as corrected (its branch at d3ecf1dea): its statements about main's record at 57e0b3d63 that
the first version's check (web_section20.py) did not cover, each held against main's files there.  Nothing run."""
import json, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "57e0b3d63"; V = "frontier/B1957_the_seats_claims_register/verification/"
rec = lambda r: json.loads(git("show", "%s:%srecords/%s.json" % (AT, V, r)))
s3 = rec("web-st17-03"); s14 = rec("web-st14-04"); w5 = rec("web-wa2-05v"); s18 = rec("web-st18-01")
F = git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md").split("\n"); L = git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n")
r1930 = next(l for l in L if l.startswith("| 1930 |")); pin = next(l for l in L if l.startswith("| chat1 | `origin/chat1/web-seat`"))
print("B1: web-st17-03 at %s: %s with %d units; its ground names H1 to H3 as main's side: %s" % (AT, s3["verdict"], len(s3["units"]), "H1 to H3" in s3["how"]))
print("B2: line 116's reason: in web-st14-04's ground 'its level 8 not being read out': %s; in web-wa2-05v's note 'the level 8 of line 116 are not read out by main': %s" % ("its level 8 not being read out" in s14["how"], "the level 8 of line 116 are not read out by main" in w5["note"]))
print("B3: FINDINGS line 725 says every statement held: %s; row 1930's head says so: %s; its bracket names only the withdrawal: %s; web-st18-01's ground still lists web-wa3-04's ground as naming part D: %s"
      % ("Every statement it makes there about main's record holds" in F[724], "EVERY STATEMENT ABOUT MAIN'S RECORD HOLDS" in r1930, "three of the statements" not in r1930.split("[corrected")[1] if "[corrected" in r1930 else None, "web-wa3-04's ground names wa3_on_main.py, part D" in s18["how"]))
print("B4: the pin row at %s records the withdrawal: %s; FINDINGS lines 716 to 718 name the channels' eighth: %s" % (AT, "withdrawn" in pin.split("—")[0] + pin[:400], any("channels'" in F[i] for i in range(715, 718))))
