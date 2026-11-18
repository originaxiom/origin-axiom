"""The web seat's status page, section 20 (its branch at 5322929cd): what it says of main's record at 57e0b3d63, each
statement held against main's files at that commit.  Nothing of the seat's is run.
A1  H4 in the read-out's run: its case count and the two constants; the dated notes that name H4 (web-st17-02,
    web-wa2-05v-r2s), B1957's FINDINGS and P-873.
A2  the three notes' corrections, the outcome of M56's question, line 116's bracket, web-wa2-05-r3p's note, N2,
    web-read-44, web-wa3-04's ground.
A3  web-st18-01's units and note, web-st18-03's note, web-st18b and web-st19 verdicts; the generated recovery view and
    row 1930 on the withdrawal.
A4  the lane's records changed between 0ffa123c8 and 57e0b3d63, and the lane's counts there.
A5  web-wtau-03-r3p's lines there and the ten lines its ground lists."""
import json, re, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "57e0b3d63"; V = "frontier/B1957_the_seats_claims_register/verification/"
rec = lambda r: json.loads(git("show", "%s:%srecords/%s.json" % (AT, V, r)))
run = git("show", AT + ":" + V + "checks/web_wa2_readout_run.txt")
m = re.search(r"H4: .* over (\d+) cases .*worst residual ([0-9.e+-]+); c = (\[[^\]]*\]) of a turn in S and (\[[^\]]*\]) in S-tilde with Q; (\[[^\]]*\]) and (\[[^\]]*\]) with -Q", run)
fnd = git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md").split("\n"); p873 = next(l for l in git("show", AT + ":docs/POINT_REGISTER.md").split("\n") if l.startswith("| P-873 |"))
print("A1: H4 at %s: %s cases, residual %s, c %s %s with Q and %s %s with -Q; H4 named in web-st17-02's note %s, web-wa2-05v-r2s's %s; FINDINGS lines naming H4: %s; P-873's row-1928 note cites H1 to H3: %s"
      % (AT, m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6), "H4" in rec("web-st17-02")["note"], "H4" in rec("web-wa2-05v-r2s")["note"], [i + 1 for i, l in enumerate(fnd) if "H4" in l], "H1 to H3" in p873))
n2 = git("show", AT + ":" + V + "checks/grounds_cite_records_that_exist_run.txt").strip().split("\n")[-1]
print("A2: web-wa2-05v corrected %s; web-wtau-03 corrected %s; web-wa2-05v-r2p outcome %s and line 116's bracket %s; web-wa2-05-r3p 'returned' %s; %s; web-read-44 %s; web-wa3-04's ground names part D %s"
      % ("CORRECTED 2026-11-18 at the web seat's section 18.2" in rec("web-wa2-05v")["note"], "CORRECTED 2026-11-18 at the web seat's section 18.2" in rec("web-wtau-03")["note"], "OUTCOME 2026-11-18" in rec("web-wa2-05v-r2p")["note"],
         "[corrected 2026-11-18 at the web seat's section 18.2, item 3" in rec("web-wa2-05v-r2p")["how"], "returned to it" in rec("web-wa2-05-r3p")["note"], n2[n2.index("each saying"):], rec("web-read-44")["verdict"], "wa3_on_main.py, part D" in rec("web-wa3-04")["how"]))
s18 = rec("web-st18-01"); cr = git("show", AT + ":docs/views/CONTEXT_RECOVERY.md").split("\n"); row1930 = next(l for l in git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n") if l.startswith("| 1930 |"))
# CORRECTED 2026-11-18 at the seat's section 22.4, item 1: A3 tested only that web-st18-01's note carried a dated
# correction, not that it named all three wrong statements of section 18's first version (it named two at 57e0b3d63);
# the same kind of fault as Y4's. The three are now tested one by one.
three = [("web-wa3-04", "web-wa3-04's ground"), ("the read-out comput", "the read-out"), ("the records of section 17 stat", "section 17's records")]
print("A3b: web-st18-01's note at %s names each wrong statement of section 18's first version: %s" % (AT, {lab: (k in s18["note"]) for k, lab in three}))
F20 = git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md"); r1930 = next(l for l in git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n") if l.startswith("| 1930 |"))
import re as _re
br1930 = " ".join(_re.findall(r"\[corrected[^\]]*\]", r1930)); three_c = [("web-wa3-04's ground named", "web-wa3-04's ground")] + three[1:]
print("A3c: at %s row 1930's brackets name each: %s; B1957's FINDINGS names each: %s (added at the seat's corrected section 22.4, item 1: A3 had tested only that the bracket recorded the withdrawal, and not FINDINGS)" % (AT, {lab: (k in br1930) for k, lab in three_c}, {lab: (k in F20) for k, lab in three_c}))
print("A3: web-st18-01 holds %d units, its note corrected %s; web-st18-03's note says withdrawn %s; verdicts %s; the recovery view's lines naming the withdrawal %s; row 1930's bracket %s"
      % (len(s18["units"]), "CORRECTED 2026-11-18" in s18["note"], "withdrawn" in rec("web-st18-03")["note"], {r: rec(r)["verdict"] for r in ("web-st18b-01", "web-st18b-02", "web-st18b-03", "web-st19-01", "web-st19-02", "web-st19-03")},
         [i + 1 for i, l in enumerate(cr) if "WITHDREW" in l or "withdrew" in l][:3], "the seat withdrew HARVEST COMPLETE at 10c488d71" in row1930))
ch = sorted(l.split("\t")[-1].split("/")[-1][:-5] for l in git("diff", "--name-status", "0ffa123c8", AT, "--", V + "records/").split("\n") if l and "/web-" in l)
w = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]
print("A4: the lane's records new or changed between 0ffa123c8 and %s: %d; the lane there: %s" % (AT, len(ch), {k: w[k] for k in ("files", "read", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}))
u3 = rec("web-wtau-03-r3p")
print("A5: web-wtau-03-r3p at %s holds lines %s; its ground lists as narrowed lines %s" % (AT, sorted(int(x.rsplit(":", 1)[1]) for x in u3["units"]), sorted({int(x) for x in re.findall(r"line (\d+):", u3["how"])})))
