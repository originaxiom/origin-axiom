"""The web seat's status page, section 26 (its branch at 19685b3ce, the read version): what it says of main's record at
d18e3c30c, each statement held against main's files there.  Nothing of the seat's is run.
 G1  (a) the sweep's figures under the seat's three ledger keys; unit 2582's record.
 G2  (b) 'dated' and 'overturned' in web-st24-01's ground and in harvest row 1945, and whether a bracket stands beside them.
 G3  (c) '320' in FINDINGS and in the point register's line 53.
 G4  (d) the web lane's cut at each main commit that changed extract.py; whether eb545d286 was ever one; web-st22-02's unit 2240.
 G5  (e) see web_section25.py K2b: the record's history, which K2 (first presence) does not show.
 G6  (f) names shared by several registered files at d18e3c30c.
 G7  (g) unit 2546's two parts; unit 2606's mathematics: V^-1 V^T for V = [[1, -1], [0, -1]], and the form on Z/5 from V + V^T."""
import json, re, subprocess, collections
from fractions import Fraction as Fr
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
AT = "d18e3c30c"; V = "frontier/B1957_the_seats_claims_register/verification/"
rec = lambda r, at=AT: json.loads(git("show", "%s:%srecords/%s.json" % (at, V, r)))
o = json.loads(git("show", AT + ":" + V + "checks/older_rows.json"))
keys = ("chat1 (owner-relayed, 2026-09-15)", "web seat (chat1)", "the web seat (chat1)")
print("G1: at %s the seat's three keys: rows %s, naming no file %s, files %s; the key 'web seat (chat1)' alone: rows %d, naming no file %d; unit 2582 in web-st25-01 (%s): %s"
      % (AT, [len(o[k]["rows"]) for k in keys], [len(o[k]["rows_no_file"]) for k in keys], [len(o[k]["files"]) for k in keys], len(o[keys[1]]["rows"]), len(o[keys[1]]["rows_no_file"]), rec("web-st25-01")["verdict"], "web:STATUS_CHAT1:2582" in rec("web-st25-01")["units"]))
s24 = rec("web-st24-01"); L = git("show", AT + ":docs/HARVEST_LEDGER.md").split("\n"); r1945 = next(l for l in L if l.startswith("| 1945 |"))
br = lambda t: " ".join(re.findall(r"\[(?:corrected|CORRECTED)[^\]]*\]", t))
print("G2: at %s web-st24-01's ground says 'placed and dated': %s, 'overturned': %s; its note brackets either: %s; row 1945 says 'placed and dated': %s, 'overturned': %s; a bracket in row 1945 on either: %s"
      % (AT, "placed and dated" in s24["how"], "overturned" in s24["how"], "dated" in s24.get("note", "") or "overturned" in s24.get("note", ""), "placed and dated" in r1945, "overturned" in r1945, any(w in br(r1945) for w in ("dated", "overturned"))))
F = git("show", AT + ":frontier/B1957_the_seats_claims_register/FINDINGS.md").split("\n"); P = git("show", AT + ":docs/POINT_REGISTER.md").split("\n")
print("G3: at %s FINDINGS' lines giving 320: %s; giving 283: %s; the point register's line 53 gives 320: %s"
      % (AT, [i + 1 for i, l in enumerate(F) if re.search(r"\b320 are on a branch", l)], [i + 1 for i, l in enumerate(F) if "283" in l], "320 files outside" in P[52]))
cuts = collections.OrderedDict()
for cm in git("log", "--format=%h", "--reverse", AT, "--", V + "extract.py").split():
    m = re.search(r'"origin/chat1/web-seat", "[0-9a-f]+", "([0-9a-f]+)"', git("show", "%s:%sextract.py" % (cm, V)))
    if m: cuts.setdefault(m.group(1), cm)
print("G4: the web lane's cuts on main up to %s (cut: first main commit): %s; eb545d286 among them: %s; web-st22-02 holds unit 2240 at 7d3776b67 (cut %s): %s, at 23cd5a5ca (cut %s): %s"
      % (AT, dict(cuts), any(c.startswith("eb545d2") for c in cuts), re.search(r'"origin/chat1/web-seat", "[0-9a-f]+", "([0-9a-f]+)"', git("show", "7d3776b67:" + V + "extract.py")).group(1), "web:STATUS_CHAT1:2240" in rec("web-st22-02", "7d3776b67")["units"],
         re.search(r'"origin/chat1/web-seat", "[0-9a-f]+", "([0-9a-f]+)"', git("show", "23cd5a5ca:" + V + "extract.py")).group(1), "web:STATUS_CHAT1:2240" in rec("web-st22-02", "23cd5a5ca")["units"]))
U = json.loads(git("show", AT + ":" + V + "UNITS.json"))["units"]; nm = collections.defaultdict(set)
for u in U: lane, path = u[0].split(":")[0], u[0].split(":")[1]; nm[path.split("/")[-1]].add((lane, path))
print("G6: at %s names shared by several registered files: %d: %s" % (AT, sum(1 for v in nm.values() if len(v) > 1), sorted(k for k, v in nm.items() if len(v) > 1)))
F23 = git("show", "23cd5a5ca:frontier/B1957_the_seats_claims_register/FINDINGS.md").split("\n"); M = git("show", "23cd5a5ca:docs/seats/chat1.md")
pg = git("show", "614bff48d:relays/STATUS_CHAT1.md").split("\n")
m65 = M[M.index("### M65"):M.index("### M64")]
print("G7: 2546: at 23cd5a5ca FINDINGS' lines 734 and 735 say all three companions' reasons were overturned by the corrected section 17: %s; M65 says the same: %s; the seat's section 24.5 at 614bff48d puts 20 and 22 at rows 339 and 340, before the corrected section 17, corrected in place: %s"
      % ("Three companions whose reasons the seat's corrected section 17" in F23[733] and "overturned" in F23[734], "The three companions whose reasons your corrected section 17 overturned" in m65,
         "rows 339 and 340" in " ".join(pg[2466:2469]) and "before it (corrected in place" in " ".join(pg[2467:2469])))
mul = lambda A, B: [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
Vm = [[1, -1], [0, -1]]; det = Vm[0][0] * Vm[1][1] - Vm[0][1] * Vm[1][0]; Vi = [[Fr(Vm[1][1], det), Fr(-Vm[0][1], det)], [Fr(-Vm[1][0], det), Fr(Vm[0][0], det)]]
VT = [[Vm[j][i] for j in range(2)] for i in range(2)]; S = [[Vm[i][j] + VT[i][j] for j in range(2)] for i in range(2)]; dS = S[0][0] * S[1][1] - S[0][1] * S[1][0]
Si = [[Fr(S[1][1], dS), Fr(-S[0][1], dS)], [Fr(-S[1][0], dS), Fr(S[0][0], dS)]]
lam = Si[0][0] % 1; q = (lam * pow(2, -1, 5)) % 1 if lam.denominator == 5 else None
squares = sorted({(x * x) % 5 for x in range(1, 5)})
print("G7: 2539: the seat's section 24.5 at 614bff48d: 'dated' corrected in place at line 2459: %s; 'dated' still in its remedy, lines 2473 and 2474: %s" % ("corrected in place, 2026-11-18: this read \"a dated move\"" in " ".join(pg[2458:2460]), "dated" in " ".join(pg[2472:2474])))
print("G7: 2606: V^-1 V^T = %s (gamma = [[2, 1], [1, 1]]: %s); V + V^T = %s, det %d, so H_1 = Z/5 generated by e1 (e2 = 2 e1); the linking form lambda(e1, e1) = (V + V^T)^-1 [0][0] mod 1 = %s; its quadratic refinement q = lambda / 2 = %s, i.e. x^2/5; lambda's class 2x^2/5 and q's class x^2/5, the squares mod 5 being %s"
      % ([[int(x) for x in r] for r in mul(Vi, VT)], mul(Vi, VT) == [[2, 1], [1, 1]], S, dS, lam, Fr(int(q * 5), 5) if q is not None else None, squares))
# G8 (section 26.1, 26.4 and the lane): the seat's other statements about main's record at d18e3c30c
F18 = F; M18 = git("show", AT + ":docs/seats/chat1.md"); lock = git("show", AT + ":" + V + "test_b1957_register.py")
m65 = M18[M18.index("### M65"):M18.index("### M64")]
print("G8: 26.1.1: FINDINGS' lines 744 to 747 say 'named': %s; M65's bracket does: %s; the lock's docstring: %s"
      % ("named" in " ".join(F18[743:747]), "each placed and named" in m65, "the lock tests\n    that the move is named" in lock or "that the move is named" in lock))
k1 = git("show", AT + ":" + V + "checks/web_section25_run.txt").split("\n")[0]
print("G8: 26.1.1: K1 at %s: %s" % (AT, k1[k1.index("of the placed"):][:120]))
src = git("show", AT + ":" + V + "checks/companion_grounds.py"); src_now = open(V + "checks/companion_grounds.py").read()
g = {"__name__": "cg"}; exec(src_now[:src_now.index("for at, lab in")], g)
c_, s_, n_, p_, a_, u_ = g["survey"](g["load"](AT), "web-")
print("G8: 26.1.1: at %s the %d placed lines sit in %d receiving records; web-st25-02 %s holds line 2535 (this seat's count): %s"
      % (AT, n_, len(g["RECEIVERS"]), rec("web-st25-02")["verdict"], "web:STATUS_CHAT1:2535" in rec("web-st25-02")["units"]))
r2p = rec("web-r79b-01-r2p")["note"]
print("G8: 26.1.2: FINDINGS' lines 750 and 751 name rows 339 and 340 at 364ce101e and put line 29 at the corrected section 17 (6f337047b): %s; web-r79b-01-r2p's note names 339, 340, 364ce101e and 6f337047b: %s; FINDINGS cites K2: %s, the note: %s"
      % (all(w in " ".join(F18[748:752]) for w in ("339", "340", "364ce101e", "only line 29 at the corrected section 17")), all(w in r2p for w in ("339", "340", "364ce101e", "6f337047b")), "K2" in " ".join(F18[748:752]), "K2" in r2p))
own = collections.defaultdict(list)
for l in git("ls-tree", "--name-only", AT, V + "records/").split("\n"):
    if "/web-" in l and l.endswith(".json"):
        d = json.loads(git("show", AT + ":" + l))
        for u in d.get("units", []): own[u].append((d["id"], d["verdict"]))
print("G8: 26.1.3: units 2240, 2437, 2456 held by: %s" % [own["web:STATUS_CHAT1:%d" % n] for n in (2240, 2437, 2456)])
a23 = set(rec("web-st24-01", "23cd5a5ca")["units"]); a18 = set(rec("web-st24-01")["units"]); left = a23 - a18; ids18 = {u[0] for u in U}
st25 = set(rec("web-st25-01")["units"]); s245 = {u for u in st25 if 2454 <= int(u.rsplit(":", 1)[1]) <= 2491}
print("G8: 26.1.3: web-st24-01 holds %d; of its %d units at 23cd5a5ca, %d left: to web-st24j-02 %d, to web-st25-01 %d, ids that no longer exist %d; new ids %d; web-st25-01 holds %d of section 24.5's lines (2454 to 2491)"
      % (len(a18), len(a23), len(left), len(left & set(rec("web-st24j-02")["units"])), len(left & st25), len(left - ids18), len(a18 - a23), len(s245)))
web59 = {k: v for k, v in o.items() if k in keys}; webstems = {u[0].split(":")[1].split("/")[-1] for u in U if u[0].startswith("web:")}
print("G8: 26.1.4: at %s the seat's 59 files all read 'in the register': %s; each has a file of that name in the web lane: %s"
      % (AT, all(st == "in the register" for v in web59.values() for st in v["files"].values()), all(f in webstems for v in web59.values() for f in v["files"])))
ex = git("show", AT + ":" + V + "extract.py")
print("G8: 26.1.5: EXCLUDE_PATTERNS at %s keeps W-P1's card, its steps' conditions and the three step relays, with the reason: %s; the status page in the lane: %s"
      % (AT, all(w in ex for w in ('"relays/cards/CHAT1_W-P1_*"', "W-P1A", "W-P1B", "W-P1C")) and "section 25.5" in ex, any(u[0].startswith("web:STATUS_CHAT1:") for u in U)))
sm = json.loads(git("show", AT + ":" + V + "SUMMARY.json"))["lanes"]["web"]; t3 = git("show", AT + ":" + V + "checks/third_reading_web_run.txt").strip().split("\n")[-1]
print("G8: the lane at %s: %s, units %d; the third reading's last line: %s; the lock exempts web-st25- and web-wp1-: %s; web-st25-01 %s holds %d"
      % (AT, {k: sm[k] for k in ("files", "read", "statements", "PENDING")}, sum(1 for u in U if u[0].startswith("web:")), t3[-90:], '"web-st25-"' in lock and '"web-wp1-"' in lock, rec("web-st25-01")["verdict"], len(rec("web-st25-01")["units"])))
n2 = git("show", AT + ":" + V + "checks/grounds_cite_records_that_exist_run.txt").strip().split("\n")[-1]
empty = []
for l in git("ls-tree", "--name-only", AT, V + "records/").split("\n"):
    if l.endswith(".json"):
        d = json.loads(git("show", AT + ":" + l))
        if d.get("verdict") != "READ" and not d.get("units") and "no statement under it" not in d.get("note", ""): empty.append(d["id"])
print("G8: N2 at %s ends: %s; the records kept empty without the note: %s" % (AT, n2[-40:], empty))
shared = {k for k, v in nm.items() if len(v) > 1}
oth = [(k, f) for k, v in o.items() if k not in keys for f, st in v["files"].items() if st == "in the register" and f in shared]
print("G8: 26.2 (f): at %s, files under other seats' keys reading 'in the register' through a shared name: %d: %s" % (AT, len(oth), oth))
L18 = L
print("G8: 26.4: row 1950 names 3f4fccbcf: %s; row 1949 answers W-P1's Higgs-orbit question: %s; rows 1956 and 1957 say received before their reads: %s; P-874 enters W-P1: %s"
      % ("3f4fccbc" in next(l for l in L18 if l.startswith("| 1950 |")), "ITS ANSWER TO W-P1" in next(l for l in L18 if l.startswith("| 1949 |")) and "W_P1_PROCESS_ORBIT_RESPONSE" in next(l for l in L18 if l.startswith("| 1949 |")),
         [("RECEIVED" in next(l for l in L18 if l.startswith("| %d |" % n))) for n in (1956, 1957)], "W-P1" in next(l for l in P if l.startswith("| P-874 |"))))
# G9: the last of section 26's statements that main's files can settle
on = lambda c: git("merge-base", "--is-ancestor", c, "origin/chat1/web-seat") == "" and subprocess.run(["git", "merge-base", "--is-ancestor", c, "origin/chat1/web-seat"]).returncode == 0
wp = {r: rec(r)["verdict"] for r in ("web-wp1-01", "web-wp1-02", "web-wp1-03", "web-wp1-04")}
m67 = M18[M18.index("### M67"):M18.index("### M66")]; r1951 = next(l for l in L if l.startswith("| 1951 |")); p874 = next(l for l in P if l.startswith("| P-874 |"))
print("G9: the seat's page at 614bff48d, lines 2243 and 2244 say 'dated': %s; 2f2e490e1 and 35373bd43 on its branch: %s; web-wp1's records at %s: %s; P-874 names W-P1's tasks: %s; K2 cited in M67: %s, in row 1951: %s, in web-st25-01's ground (K1 to K4): %s"
      % ("dated" in " ".join(pg[2242:2244]), [on(c) for c in ("2f2e490e1", "35373bd43")], AT, wp, "task" in p874[p874.index("W-P1"):], "K2" in m67, "K2" in r1951, "K1 to K4" in rec("web-st25-01")["how"]))
