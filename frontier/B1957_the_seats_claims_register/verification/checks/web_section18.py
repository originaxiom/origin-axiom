"""The web seat's status page, section 18 (its branch at 8bb9a1fcc): what it says of main's record at 6f337047b, each
statement held against main's files at that commit.  Nothing of the seat's is run.

Y1  its lane in the register: 138 files, 7,581 statements: 1,690 verified, 2 refuted, 162 conditional, 744 partial,
    59 superseded, 4,924 noted, none pending; 8,327 units; the lane cut at bf3b06b14.
Y2  the lane's records new or changed between 364ce101e and 6f337047b: 8 new, 22 changed, none gone.
Y3  the verdict of each unit it lists, read from the records at 6f337047b.
Y4  web-wa3-04's ground names wa3_on_main.py for the trace signature; web.json's decision for line 110 is S.
"""
import json, re, subprocess, collections
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "6f337047b"; V = "frontier/B1957_the_seats_claims_register/verification/"
summ = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]
units = json.loads(git("show", AT + ":" + V + "UNITS.json")); webu = [u for u in units["units"] if u[0].startswith("web:")]
ext = git("show", AT + ":" + V + "extract.py"); head = re.search(r'"origin/chat1/web-seat", "[0-9a-f]+", "([0-9a-f]+)"', ext).group(1)
print("Y1: the web lane at %s: %s; units %d; cut at %s" % (AT, {k: summ[k] for k in ("files", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}, len(webu), head))
ch = collections.Counter(l.split("\t")[0][0] for l in git("diff", "--name-status", "364ce101e", AT, "--", V + "records/").split("\n") if l and "/web-" in l)
print("Y2: the lane's records between 364ce101e and %s: new %d, changed %d, gone %d" % (AT, ch["A"], ch["M"], ch["D"]))
owner = {}
for l in git("ls-tree", "--name-only", AT, V + "records/").split("\n"):
    if "/web-" not in l: continue
    d = json.loads(git("show", AT + ":" + l))
    for u in d.get("units", []): owner[u] = (d["id"], d["verdict"])
F = {"W-A2": "web:CHAT1_TO_CC_2026-11-17_W-A2_POSTULATE_D_FROM_THE_GROUND", "weave": "web:CHAT1_TO_CC_2026-11-10_THE_WEAVES_OWN_ACTION_ON_TAU",
     "W-F16": "web:CHAT1_TO_CC_2026-11-14_W-F16_THE_TWO_WAY_CHOICES_SETTLE_EACH_OTHER", "W-A3": "web:CHAT1_TO_CC_2026-11-17_W-A3_THE_COVER_THE_CLASS_AND_THE_UP_SECTOR",
     "W-F17": "web:CHAT1_TO_CC_2026-11-14_W-F17_SECOND_COMPUTATIONS_FOR_COMPUTED_NOWHERE", "R79B": "web:REVIEW_79B_CHAT1", "P-783": "web:CHAT1_TO_CC_2026-11-11_P-783_THE_GOLDEN_STATE_IS_THE_LOWEST_AND_SIMPLE",
     "W-C2": "web:CHAT1_TO_CC_2026-11-11_W-C2_THE_AGY-EXP_SEATS_FOUR_THEOREMS", "STATUS": "web:STATUS_CHAT1", "W-F24": "web:CHAT1_TO_CC_2026-11-15_W-F24_WHERE_FRAME_CS_READ_OUT_LOSES_THE_HIERARCHY"}
wb2 = sorted({u.rsplit(":", 1)[0] for u, o in owner.items() if o[0] == "web-wb2-d1-05"})
claims = [("W-A2", 110, "SUPERSEDED"), ("W-A2", 113, "PARTIAL"), ("W-A2", 116, "PARTIAL"), ("W-A2", 28, "PARTIAL"), ("W-A2", 35, "VERIFIED"), ("W-A2", 181, "CONDITIONAL")]
claims += [("weave", n, "VERIFIED") for n in (55, 60, 61, 68, 70, 90, 99, 100, 132, 136)] + [("weave", 65, "PARTIAL")]
claims += [("W-F16", 19, "PARTIAL"), ("W-A3", 116, "CONDITIONAL"), ("W-F17", 236, "VERIFIED"), ("R79B", 29, "VERIFIED"), ("P-783", 54, "PARTIAL"),
           ("W-C2", 114, "NOTED"), ("STATUS", 174, "NOTED"), ("STATUS", 175, "NOTED"), ("W-A3", 165, "VERIFIED"), ("W-F24", 86, "VERIFIED")]
bad = [(f, n, owner.get("%s:%d" % (F[f], n)), want) for f, n, want in claims if owner.get("%s:%d" % (F[f], n), (None, None))[1] != want]
wb2bad = [(n, owner.get("%s:%d" % (w, n))) for w in wb2 for n in (126, 127) if owner.get("%s:%d" % (w, n), (None, None))[1] != "VERIFIED"]
print("Y3: %d units it names, read from the records at %s: not with the verdict it says: %d %s; the corrected W-B2 note's lines 126 and 127 (file %s): not verified: %s"
      % (len(claims) + 2, AT, len(bad), bad, [w.split(":")[1][:40] for w in wb2], wb2bad))
how = json.loads(git("show", AT + ":" + V + "records/web-wa3-04.json"))["how"] + " " + json.loads(git("show", AT + ":" + V + "records/web-wa3-04.json")).get("note", "")
wj = json.loads(git("show", AT + ":" + V + "second_reading/web.json")); d110 = [x["decision"] for x in wj["units"] if x["unit"] == F["W-A2"] + ":110"]
print("Y4: web-wa3-04 names wa3_on_main.py, part D, for the trace signature: %s; web.json's decision for W-A2's line 110: %s" % ("wa3_on_main.py, part D" in how, d110))
