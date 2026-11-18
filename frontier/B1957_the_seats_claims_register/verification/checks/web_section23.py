"""The web seat's status page at eb545d286: its section 21 and 22 as corrected after their referee reads, and its section
23. What they say of main's record, each held against main's files at the commit the seat read (section 21: cdf78dd95;
section 22: 57cc5d5fe; section 23: f1efc59dd).  Nothing of the seat's is run.
 E1  section 21 at cdf78dd95: FINDINGS line 726; row 1932 names all three wrong statements of section 18's first version;
     the pin row says three were wrong and points to rows; what the first section 21's item 4 said (9dccd2062).
 E2  section 22 at 57cc5d5fe: which pages name d3ecf1dea; web-st20-02's lines; web-st20-03 holds line 2006; P-865's later
     entry; check B4's subject.
 E3  web-wf17-04-r3n and -r3c over their history: which W-F17 lines each held at each commit that changed them.
 E4  section 23 at f1efc59dd: the lane's records changed since 57cc5d5fe; the cut; web-st20-01's note; the pin row;
     web-st21-01 to -03; web-st-log and web-st7-06; the lane's counts; N2 and the one-by-one lock.
 E5  section 23.2: M63 and row 1938 say every statement held; web-st21-01 held the four lines at f1efc59dd; the rows of
     sections 18, 20 and 21 each recorded "every statement holds" of a version the seat's referee read corrected."""
import json, re, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
V = "frontier/B1957_the_seats_claims_register/verification/"; ST = "web:STATUS_CHAT1:"
rec = lambda at, r: json.loads(git("show", "%s:%srecords/%s.json" % (at, V, r)))
row = lambda at, n: next(l for l in git("show", at + ":docs/HARVEST_LEDGER.md").split("\n") if l.startswith("| %d |" % n))
pin = lambda at: next(l for l in git("show", at + ":docs/HARVEST_LEDGER.md").split("\n") if l.startswith("| chat1 | `origin/chat1/web-seat`"))
THREE = ("web-wa3-04's ground named", "the read-out computed", "the records of section 17 stat")
AT = "cdf78dd95"; F = git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md").split("\n")
first21 = git("show", "9dccd2062:relays/STATUS_CHAT1.md"); it4 = [l for l in first21.split("\n") if l.startswith("4. **§ 20's first version's word")]
print("E1: at %s FINDINGS line 726 says every statement held: %s; row 1932 names the three: %s; the pin row names them: %s, says three were wrong: %s, rows it points to: %s; the first section 21's item 4 (9dccd2062) names the four places: %s"
      % (AT, "Every statement it makes there about main's record holds" in F[725], [k in row(AT, 1932) for k in THREE], [k in pin(AT) for k in THREE], "three of the statements held were wrong" in pin(AT), re.findall(r"\d{4}", re.search(r"three of the statements held were wrong; ([^\]]*)\]", pin(AT)).group(1)), [("four places" in l) for l in it4]))
AT = "57cc5d5fe"; L = git("show", AT + ":docs/HARVEST_LEDGER.md"); P = git("show", AT + ":docs/POINT_REGISTER.md").split("\n"); p865 = next(l for l in P if l.startswith("| P-865 |"))
pages = {"FINDINGS": git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md"), "CAMPAIGN_STATUS": git("show", AT + ":docs/CAMPAIGN_STATUS.md").split("\n\n")[1] if False else git("show", AT + ":docs/CAMPAIGN_STATUS.md")[:6000],
         "row 1935": row(AT, 1935), "the pin row": pin(AT), "P-865": p865, "M61": git("show", AT + ":docs/seats/chat1.md"), "web-st20-03": json.dumps(rec(AT, "web-st20-03"))}
s202 = rec(AT, "web-st20-02"); b4 = re.search(r"\n B4 [^\n]*", git("show", AT + ":" + V + "checks/web_section20b.py"))
print("E2: at %s the pages naming d3ecf1dea: %s; web-st20-02 holds lines %s; P-865 says 'three withdrawn lines main had held verified': %s; check B4's line: %s"
      % (AT, {k: ("d3ecf1dea" in v) for k, v in pages.items()}, [u.rsplit(":", 1)[1] for u in s202["units"]], "three withdrawn lines main had held verified" in p865, b4.group(0).strip()[:120] if b4 else None))
s203 = rec("cdf78dd95", "web-st20-03"); print("E2: at cdf78dd95 web-st20-03 (%s) holds the first version's line 2006: %s" % (s203["verdict"], ST + "2006" in s203["units"]))
W17 = "web:CHAT1_TO_CC_2026-11-14_W-F17_SECOND_COMPUTATIONS_FOR_COMPUTED_NOWHERE:"
for r in ("web-wf17-04-r3n", "web-wf17-04-r3c"):
    hist = []
    for c in git("log", "--format=%h", "--reverse", "f1efc59dd", "--", V + "records/%s.json" % r).split():
        d = rec(c, r); hist.append((c, d["verdict"], sorted(int(u.rsplit(":", 1)[1]) for u in d["units"] if u.startswith(W17))))
    print("E3: %s over its history (commit, verdict, W-F17 lines held): %s" % (r, hist))
AT = "f1efc59dd"
ch = sorted(l.split("\t")[-1].split("/")[-1][:-5] for l in git("diff", "--name-status", "57cc5d5fe", AT, "--", V + "records/").split("\n") if l and "/web-" in l)
head = re.search(r'"origin/chat1/web-seat", "[0-9a-f]+", "([0-9a-f]+)"', git("show", AT + ":" + V + "extract.py")).group(1)
n201 = rec(AT, "web-st20-01")["note"]; t21 = {r: (rec(AT, r)["verdict"], len(rec(AT, r)["units"])) for r in ("web-st21-01", "web-st21-02", "web-st21-03")}
only_ids = {}
for r in ("web-st-log", "web-st7-06"):
    a, b = rec("57cc5d5fe", r), rec(AT, r); only_ids[r] = all(a[k] == b[k] for k in a if k != "units") and len(a["units"]) == len(b["units"])
w = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]
n2 = git("show", AT + ":" + V + "checks/grounds_cite_records_that_exist_run.txt").strip().split("\n")[-1]; t2 = git("show", AT + ":" + V + "checks/third_reading_web_run.txt").strip().split("\n")[-1]
print("E4: at %s the lane's records new or changed since 57cc5d5fe: %d %s; the lane cut at %s; web-st20-01's note names line 1990: %s, names 1961, 1968 or 2006: %s; the pin row records the withdrawal at d3ecf1dea: %s; web-st21: %s; web-st-log and web-st7-06 changed only their unit ids: %s"
      % (AT, len(ch), ch, head, "1990" in n201, any(x in n201 for x in ("1961", "1968", "2006")), "withdrawn at d3ecf1dea" in pin(AT) or "d3ecf1dea" in pin(AT), t21, only_ids))
print("E4: the lane at %s: %s; N2 %s; %s" % (AT, {k: w[k] for k in ("files", "read", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}, n2[n2.index("each saying"):], t2))
m63 = git("show", AT + ":docs/seats/chat1.md"); m63 = m63[m63.index("### M63"):]; m63 = m63[:m63.index("\n### ", 5)]
s21 = rec(AT, "web-st21-01")["units"]; old = {2100: "web-st20-01 holds one line", 2110: "pin row", 2125: "records of § 19", 2147: "4. **§ 20's first version's word"}
first_lines = first21.split("\n")
print("E5: at %s M63 says every statement holds: %s; row 1938: %s; web-st21-01 holds the first section 21's lines 2100, 2110, 2125, 2147 VERIFIED: %s; their texts there: %s"
      % (AT, "holds" in m63 and "every statement" in m63.lower(), "every statement about main's record holds" in row(AT, 1938).lower(), [ST + str(n) in s21 for n in (2100, 2110, 2125, 2147)], [first_lines[n - 1][:70] for n in (2100, 2110, 2125, 2147)]))
corrected = git("show", "eb545d286:relays/STATUS_CHAT1.md").split("\n")
print("E5: those four texts on the corrected page (eb545d286): %s" % [first_lines[n - 1] in corrected for n in (2100, 2110, 2125, 2147)])
print("E5: rows that recorded every statement holding of a version the seat later corrected: 1930 %s, 1935 %s, 1938 %s"
      % ("every statement it makes there about main's record holds" in row(AT, 1930).lower() or "every statement" in row(AT, 1930).lower(), "every statement" in row(AT, 1935).lower(), "every statement" in row(AT, 1938).lower()))
# E6 (added 2026-11-18 at the seat's corrected sections 21 to 23, fdc3008e0)
def entry1935(at):
    m = re.search(r"row 1935 \(its section 20[^—]*", pin(at)); return m.group(0) if m else ""
h57 = pin("57cc5d5fe").split(" — before")[0]
print("E6: the pin row's head at 57cc5d5fe records the withdrawal: %s; its history entry for row 1935 carries the withdrawal at 57cc5d5fe: %s, at f1efc59dd: %s"
      % ("withdr" in h57.lower(), "withdr" in entry1935("57cc5d5fe").lower(), "withdr" in entry1935("f1efc59dd").lower()))
lock = git("show", "f1efc59dd:" + V + "test_b1957_register.py")
print("E6: the one-by-one lock at f1efc59dd exempts web-st21 by name: %s; at 57cc5d5fe: %s" % ('"web-st21-"' in lock, '"web-st21-"' in git("show", "57cc5d5fe:" + V + "test_b1957_register.py")))
p8 = next(l for l in git("show", "cdf78dd95:docs/POINT_REGISTER.md").split("\n") if l.startswith("| P-865 |")); s21 = rec("f1efc59dd", "web-st21-01")["units"]
print("E6: web-st21-01 at f1efc59dd holds the first section 21's line 2141 VERIFIED: %s, which reads: %s; P-865 at cdf78dd95 said every statement of section 18's first version held: %s"
      % (ST + "2141" in s21, first_lines[2140][:110], "every statement it makes about main's record holds (checks/web_section18.py)" in p8))
print("E6: the first section 21's line 2141 on the page at fdc3008e0: %s" % (first_lines[2140] in git("show", "fdc3008e0:relays/STATUS_CHAT1.md").split("\n")))
print("E6: the first section 21's lines 2100, 2110, 2125, 2147 on the page at fdc3008e0: %s; M63 at f1efc59dd takes the word only from a version carrying the referee read's corrections: %s"
      % ([first_lines[n - 1] in git("show", "fdc3008e0:relays/STATUS_CHAT1.md").split("\n") for n in (2100, 2110, 2125, 2147)], "carries its referee read" in m63 or "carries the read's corrections" in m63 or "referee read's corrections" in m63))
