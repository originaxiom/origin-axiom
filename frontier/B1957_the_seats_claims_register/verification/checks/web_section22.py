"""The web seat's status page, section 22 (its branch at 3e3b143fe): what it says of main's record at 57cc5d5fe, each
statement held against main's files there.  Nothing of the seat's is run."""
import json, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "57cc5d5fe"; V = "frontier/B1957_the_seats_claims_register/verification/"
rec = lambda r: json.loads(git("show", "%s:%srecords/%s.json" % (AT, V, r)))
ch = sorted(l.split("\t")[-1].split("/")[-1][:-5] for l in git("diff", "--name-status", "cdf78dd95", AT, "--", V + "records/").split("\n") if l and "/web-" in l)
print("D1: the lane's records new or changed between cdf78dd95 and %s: %d" % (AT, len(ch)))
s2 = rec("web-st17-02"); s3 = rec("web-st17-03"); s3b = rec("web-st17-03b")
print("D2: web-st17-03 at %s holds %d units, kept for its ground: %s; web-st17-03b %s with %d unit; web-st17-02's note names line 1715 on H4: %s"
      % (AT, len(s3["units"]), "no statement under it" in s3["note"], s3b["verdict"], len(s3b["units"]), "line 1715" in s2["note"] and "H4" in s2["note"]))
s14 = rec("web-st14-04"); w5 = rec("web-wa2-05v")
print("D3: line 116's brackets: web-st14-04 %s, web-wa2-05v %s" % ("section 20.4, item 2" in s14["how"], "section 20.4, item 2" in w5["note"]))
F = git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md").split("\n"); L = git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n")
r1930 = next(l for l in L if l.startswith("| 1930 |")); s18 = rec("web-st18-01")
print("D4: the three wrong statements named at %s in FINDINGS: %s; in row 1930's bracket: %s; in web-st18-01's ground and note: %s, %s"
      % (AT, [i + 1 for i, l in enumerate(F) if "that the records of section 17 stated it rightly" in l][:2], "that the records of section 17 stated it rightly" in r1930, "section 20.4, item 3" in s18["how"], "the three statements of the first version that did not hold" in s18["note"]))
r1935 = next(l for l in L if l.startswith("| 1935 |")); s20 = rec("web-st20-01"); s203 = rec("web-st20-03")
print("D5: section 20's withdrawal recorded at %s: row 1935 %s, web-st20-03 %s; web-st20-01 holds the first version's 1961 or 1990: %s"
      % (AT, "withdrew the word again" in r1935, "was withdrawn by the seat" in s203["note"], any(u.endswith((":1961", ":1990")) for u in s20["units"])))
w = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]; t2 = git("show", AT + ":" + V + "checks/third_reading_web_run.txt").strip().split("\n")[-1]
n2 = git("show", AT + ":" + V + "checks/grounds_cite_records_that_exist_run.txt").strip().split("\n")[-1]
print("D6: the lane at %s: %s; N2 %s; %s" % (AT, {k: w[k] for k in ("files", "read", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}, n2[n2.index("each saying"):], t2))
b2 = rec("web-st19b-02"); r3n = rec("web-wf17-04-r3n")
print("D7: still open at %s: web-st19b-02's ground says 'four': %s; web-wf17-04-r3n's ground lists line 139: %s; its history is E3 of web_section23.py" % (AT, "four of the receiving records" in b2["how"], "139" in r3n["how"]))
# D8 to D10 (added 2026-11-18 at the seat's corrected sections 21 and 22, eb545d286)
s20b = rec("web-st20-02"); M = git("show", AT + ":docs/seats/chat1.md"); P = git("show", AT + ":docs/POINT_REGISTER.md").split("\n")
p865 = next(l for l in P if l.startswith("| P-865 |")); lock = git("show", AT + ":" + V + "test_b1957_register.py")
print("D8: web-st20-02 at %s: its ground names 1968, 2002 and 2010: %s; it holds %d lines; its note empty: %s" % (AT, all(n in s20b["how"] for n in ("1968", "2002", "2010")), len(s20b["units"]), not s20b.get("note")))
print("D9: M61 at %s says of W-F17's line 139 'That line is PARTIAL': %s; web-wf17-04-r3c holds line 139 as %s" % (AT, "and none of their lines. That line is PARTIAL." in M, rec("web-wf17-04-r3c")["verdict"]))
print("D10: P-865's entry for section 18's first version says every statement held: %s, with the three named beside it: %s; the one-by-one lock exempts web-st20b and web-st17-03b: %s"
      % ("every statement it makes about main's record holds (checks/web_section18.py)" in p865, "that the records of section 17 stated it rightly" in p865, '"web-st20b-"' in lock and '"web-st17-03b"' in lock))
c18 = git("show", "cdf78dd95:" + V + "records/web-st20-01.json"); c20 = json.loads(git("show", "cdf78dd95:" + V + "records/web-st20-02.json"))
print("D11: at cdf78dd95 web-st20-01 held the first version's lines 1961 and 1990: %s; web-st20-02 held line 1968: %s" % (all("web:STATUS_CHAT1:%d" % n in json.loads(c18)["units"] for n in (1961, 1990)), "web:STATUS_CHAT1:1968" in c20["units"]))
# D12 (added 2026-11-18): every record of the lane at 57cc5d5fe that still gives the old reason for W-A2's line 116, and whether
# each carries the dated bracket beside it; the generated recovery view's line 67 and the pages naming d3ecf1dea (E2 of
# web_section23.py): which pages record the withdrawal without naming a commit.
import re
hits = []
for l in git("ls-tree", "--name-only", AT, V + "records/").split("\n"):
    if "/web-" not in l: continue
    d = json.loads(git("show", AT + ":" + l)); t = d["how"] + " " + d.get("note", "")
    for m in re.finditer(r"not (?:being )?read out", t):
        ctx = t[max(0, m.start() - 160): m.end() + 80]; hits.append((d["id"], "corrected 2026-11-18 at the seat's corrected section 20.4, item 2" in ctx or "this read" in ctx))
cr = git("show", AT + ":docs/views/CONTEXT_RECOVERY.md").split("\n")[66]; cs = git("show", AT + ":docs/CAMPAIGN_STATUS.md").split("\n")[4]
print("D12: records of the lane at %s still giving 'not read out': %s; each with its dated bracket: %s; the recovery view's line 67 records the withdrawal: %s, names d3ecf1dea: %s; CAMPAIGN_STATUS line 5 records it: %s, names d3ecf1dea: %s"
      % (AT, [h[0] for h in hits], all(h[1] for h in hits), "WITHDREW HARVEST COMPLETE" in cr, "d3ecf1dea" in cr, "WITHDREW HARVEST COMPLETE" in cs or "withdrew" in cs.lower(), "d3ecf1dea" in cs))
