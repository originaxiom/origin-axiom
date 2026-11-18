"""The web seat's status page, section 24 as corrected after its referee read (its branch at e9279d8eb): what it says of main's
record at 7d3776b67, each statement held against main's files there.  Nothing of the seat's is run.
 H1  the lane's records new or changed between f1efc59dd and 7d3776b67; the cut in extract.py there; the lane's counts; N2;
     the one-by-one lock and its exemptions; every unit the lane's records hold is in UNITS.json at the cut.
 H2  section 22.4's items as M64 mended them: the notes of web-st20-01, -02, -03; web-st19b-02's 'five'; M61's bracket;
     P-865; web-wf17-04-r3n; web-st21-01's units and note; M63's and row 1938's clauses; the item numbers its brackets cite.
 H3  the counts M64 and row 1940 give for the lane, against SUMMARY.json at the same commit."""
import json, re, subprocess
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "7d3776b67"; V = "frontier/B1957_the_seats_claims_register/verification/"; ST = "web:STATUS_CHAT1:"
rec = lambda r, at=AT: json.loads(git("show", "%s:%srecords/%s.json" % (at, V, r)))
ch = sorted(l.split("\t")[-1].split("/")[-1][:-5] for l in git("diff", "--name-status", "f1efc59dd", AT, "--", V + "records/").split("\n") if l and "/web-" in l)
head = re.search(r'"origin/chat1/web-seat", "[0-9a-f]+", "([0-9a-f]+)"', git("show", AT + ":" + V + "extract.py")).group(1)
w = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]; lock = git("show", AT + ":" + V + "test_b1957_register.py")
n2 = git("show", AT + ":" + V + "checks/grounds_cite_records_that_exist_run.txt").strip().split("\n")[-1]; t2 = git("show", AT + ":" + V + "checks/third_reading_web_run.txt").strip().split("\n")[-1]
units = {u[0] for u in json.loads(git("show", AT + ":" + V + "UNITS.json"))["units"]}
allheld = set()
for f in git("ls-tree", "--name-only", AT, V + "records/").split():
    if "/web-" in f: allheld |= set(json.loads(git("show", AT + ":" + f)).get("units", []))
print("H1: at %s the lane's records new or changed since f1efc59dd: %d %s; cut at %s; counts %s; N2 %s; %s; the lock exempts web-st21b, web-st22, web-st23: %s; every unit held is in UNITS.json: %s"
      % (AT, len(ch), ch, head, {k: w[k] for k in ("files", "read", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")}, n2[n2.index("each saying"):], t2, all(x in lock for x in ('"web-st21b-"', '"web-st22-"', '"web-st23-"')), allheld <= units))
s201, s202, s203 = rec("web-st20-01"), rec("web-st20-02"), rec("web-st20-03"); b2 = rec("web-st19b-02"); r3n = rec("web-wf17-04-r3n"); s21 = rec("web-st21-01")
M = git("show", AT + ":docs/seats/chat1.md"); L = git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n"); row = lambda n: next(l for l in L if l.startswith("| %d |" % n))
p865 = next(l for l in git("show", AT + ":docs/POINT_REGISTER.md").split("\n") if l.startswith("| P-865 |"))
m63 = M[M.index("### M63"):]; m63 = m63[:m63.index("\n### ", 5)]; m61 = M[M.index("### M61"):]; m61 = m61[:m61.index("\n### ", 5)]
print("H2: web-st20-01's note names 1961 and 1990: %s; web-st20-02's note names 1968 and its lines %s: %s; web-st20-03's note names 2006: %s; web-st19b-02 reads 'five': %s; M61's bracket names line 1913: %s; P-865 names the three: %s; web-wf17-04-r3n's note: %s"
      % ("1961" in s201["note"] and "1990" in s201["note"], [u.rsplit(":", 1)[1] for u in s202["units"]], "1968" in s202["note"], "2006" in s203["note"], "five of the receiving records" in b2["how"], "line 1913" in m61, "the records of section 17 stated it rightly" in p865, "never held it" in r3n["note"]))
first = git("show", "9dccd2062:relays/STATUS_CHAT1.md").split("\n"); now = git("show", "fdc3008e0:relays/STATUS_CHAT1.md").split("\n")
gone = [n for n in (2100, 2141, 2125, 2110, 2147) if ST + str(n) in s21["units"] and now[n - 1] == first[n - 1]]
print("H2: web-st21-01 at %s holds a first-version line of the five under its own text: %s; its note names the five: %s; web-st21b-01 %s; M63's clause says five: %s; row 1938's: %s"
      % (AT, gone, all(x in s21["note"] for x in ("2100", "2141", "2125", "2110", "2147")) or all(x in s21["note"] for x in ("one contradicted line", "P-865 was a third", "'four'", "named none of the three", "four places")), rec("web-st21b-01")["verdict"], "Five of the" in m63, "five of the lines it calls holding" in row(1938)))
print("H2: the item numbers the brackets cite: web-st19b-02's bracket %s; web-wf17-04-r3n's note %s"
      % (re.findall(r"section 22\.4, item (\d)", b2["how"]), re.findall(r"section 22\.4, item (\d)", r3n["note"])))
m64 = M[M.index("### M64"):]; m64 = m64[:m64.index("\n### ", 5)]
print("H3: M64 gives the lane as %s; row 1940 as %s; SUMMARY.json at %s: %d verified, %d noted, %d pending"
      % (re.findall(r"Your lane now:\*\* ([^.]*)", m64), re.findall(r"The web lane: ([^|]*)", row(1940)), AT, w["VERIFIED"], w["NOTED"], w["PENDING"]))
