"""B1957: the web seat's sections 14 (corrected version, 4d7721e2e) and 15 (its check of main's message M54, f3ac59295), held
against main's own register (data-free).  The register's files are read from the commits the seat read (84fcf1e57 for
section 14, dbd7c24e3 for section 15) and from the working tree.  No script of the seat's is run; one committed output of
the seat's is read as text (Y3).
 Y1  the lane's totals and unit counts at both commits, against the seat's figures.
 Y2  section 14.1 at 84fcf1e57: the records and lines it names.
 Y3  section 15.1 at dbd7c24e3: the records and lines it names, and its four exceptions.
 Y4  section 15.2: each unit it says is still under a verified record, at dbd7c24e3 and now.
 Y5  15.2 item 1: what main's read-out tested then and tests now.   Y6  item 3: main's script has no test of E0.
 Y7  15.2 item 7: main's least singular values against the seat's, class by class.
 Y8  the first version of section 14 as registered at dbd7c24e3."""
import json, pathlib, subprocess, re
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()); V = HERE.parent
REL = "frontier/B1957_the_seats_claims_register/verification/"
git = lambda *a: subprocess.run(["git"] + list(a), capture_output=True, text=True, cwd=ROOT).stdout
def state(commit):
    """the web lane's units and records at a commit (None: the working tree): (unit ids, owner of each unit, records by id)"""
    if commit is None:
        units = json.loads((V / "UNITS.json").read_text())["units"]; recs = {q.stem: json.loads(q.read_text()) for q in (V / "records").glob("web-*.json")}
    else:
        units = json.loads(git("show", "%s:%sUNITS.json" % (commit, REL)))["units"]
        names = [n for n in git("ls-tree", "--name-only", commit, REL + "records/").split("\n") if n.rsplit("/", 1)[-1].startswith("web-")]
        blob = subprocess.run(["git", "cat-file", "--batch"], input="\n".join("%s:%s" % (commit, n) for n in names) + "\n", capture_output=True, text=True, cwd=ROOT).stdout
        recs = {}; pos = 0
        for n in names:
            head_end = blob.index("\n", pos); size = int(blob[pos:head_end].split()[2]); raw = blob.encode()[len(blob[:head_end + 1].encode()):][:size].decode()
            recs[n.rsplit("/", 1)[-1][:-5]] = json.loads(raw); pos = len((blob.encode()[:len(blob[:head_end + 1].encode()) + size + 1]).decode())
    allw = [u[0] for u in units if u[0].startswith("web:")]; ids = allw; owner = {}
    for rid, d in recs.items():
        for u in d.get("units", []): owner[u] = (rid, d["verdict"])
    return ids, allw, owner, recs
def at(st, stem, lines):
    ids, _, owner, _ = st; out = {}
    for i in ids:
        head, _, ln = i.rpartition(":")
        if stem in head and ln.isdigit() and int(ln) in lines: out[int(ln)] = owner.get(i, ("-", "PENDING"))
    return out
A, B, NOW = state("84fcf1e57"), state("dbd7c24e3"), state(None)
tot = lambda c: json.loads(git("show", "%s:%sSUMMARY.json" % (c, REL)))["lanes"]["web"]
keys = ("files", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")
s14 = dict(zip(keys, (137, 6826, 1901, 2, 15, 429, 54, 4425, 0))); s15 = dict(zip(keys, (137, 6956, 1961, 2, 15, 457, 55, 4466, 0)))
print("Y1: the web lane at 84fcf1e57 as section 14.1 gives it: %s (units of every kind there: %d; the seat: 7,531); at dbd7c24e3 as section 15.1 gives it: %s (units: %d; the seat: 7,668)"
      % (all(tot("84fcf1e57")[k] == v for k, v in s14.items()), len(A[1]), all(tot("dbd7c24e3")[k] == v for k, v in s15.items()), len(B[1])))
ST, WF17, WZ1, WA2, WA3, WB2, P783, WC3, WC2, WF1, SR = "STATUS_CHAT1", "W-F17_SECOND", "W-Z1", "W-A2_", "W-A3_", "2026-11-15_W-B2_FRAME_D1S", "P-783_THE_GOLDEN", "W-C3_THE_SM_SEATS", "W-C2_THE_AGY-EXP", "W-F1_", "2026-09-08_SESSION_RELAY"
def holds(st, stem, lines, rid, verdict): got = at(st, stem, lines); return len(got) == len(lines) and all(v == (rid, verdict) for v in got.values())
y2 = [("W-F17's lines 244 and 278 NOTED in web-wf17-04r", holds(A, WF17, {244, 278}, "web-wf17-04r", "NOTED")), ("its lines 263, 266, 91, 264 PARTIAL in web-wf17-04p", holds(A, WF17, {263, 266, 91, 264}, "web-wf17-04p", "PARTIAL")),
      ("W-Z1's lines 59 and 106 PARTIAL in web-wz1-04p", holds(A, WZ1, {59, 106}, "web-wz1-04p", "PARTIAL")), ("W-A2's lines 112, 114, 187 PARTIAL in web-wa2-05r", holds(A, WA2, {112, 114, 187}, "web-wa2-05r", "PARTIAL")),
      ("unit 883 still VERIFIED in web-st9-03", holds(A, ST, {883}, "web-st9-03", "VERIFIED")), ("W-A3's line 145 PARTIAL in web-wa3-07r", holds(A, WA3, {145}, "web-wa3-07r", "PARTIAL")),
      ("units 1052 and 1124 VERIFIED in web-st12b-01", holds(A, ST, {1052, 1124}, "web-st12b-01", "VERIFIED")), ("web-st12-01's ground says 'four mends'", "four mends" in A[3]["web-st12-01"]["how"]), ("web-st12b-01's says five", "five" in A[3]["web-st12b-01"]["how"])]
print("Y2: section 14.1 at 84fcf1e57: " + "; ".join("%s: %s" % x for x in y2))
print("Y2: its line on unit 883, the other clauses, at 84fcf1e57: web-st8-07 is %s; records split from web-r2-01: %s"
      % (A[3]["web-st8-07"]["verdict"], {r: (d["verdict"], len(d["units"])) for r, d in A[3].items() if r.startswith("web-r2-01") and r != "web-r2-01"}))
pp = lambda st, stem, lines: sorted({v for v in at(st, stem, lines).values()})
y3 = [("W-F17's rows 98 to 101, 103 and lines 121, 247, 265, 277 PARTIAL in web-wf17-04p", holds(B, WF17, {98, 99, 100, 101, 103, 121, 247, 265, 277}, "web-wf17-04p", "PARTIAL")),
      ("lines 102, 211, 244, 278 NOTED in web-wf17-04r", holds(B, WF17, {102, 211, 244, 278}, "web-wf17-04r", "NOTED")), ("W-Z1's 53, 59, 106 PARTIAL in web-wz1-04p", holds(B, WZ1, {53, 59, 106}, "web-wz1-04p", "PARTIAL")),
      ("W-A2's 110, 112, 114, 116, 187 VERIFIED in web-wa2-05v", holds(B, WA2, {110, 112, 114, 116, 187}, "web-wa2-05v", "VERIFIED")), ("unit 883 SUPERSEDED in web-st9-03s", holds(B, ST, {883}, "web-st9-03s", "SUPERSEDED")),
      ("W-F1's 50, 52, 55 PARTIAL in web-wf1-01r", holds(B, WF1, {50, 52, 55}, "web-wf1-01r", "PARTIAL")), ("the session relay's 133 PARTIAL in web-sr-02p", holds(B, SR, {133}, "web-sr-02p", "PARTIAL")),
      ("web-st12-01 no longer says 'four mends'", "four mends" not in B[3]["web-st12-01"]["how"]), ("web-st13-02 records section 13.6", "13.6" in B[3]["web-st13-02"]["how"])]
print("Y3: section 15.1 at dbd7c24e3: " + "; ".join("%s: %s" % x for x in y3))
for name, stem, lines in (("W-A3's 27, 167", WA3, {27, 167}), ("the first W-B2 note's 48, 51, 64", WB2, {48, 51, 64}), ("P-783's 80, 81, 90, 94, 95", P783, {80, 81, 90, 94, 95}), ("W-C3's 48, 55, 85, 88, 99, 104, 105", WC3, {48, 55, 85, 88, 99, 104, 105}), ("W-C2's 23, 101", WC2, {23, 101})):
    got = pp(B, stem, lines); print("Y3: %s at dbd7c24e3: %s; all PARTIAL in records ending in p: %s" % (name, got, all(v == "PARTIAL" and r.endswith("p") for r, v in got)))
print("Y3: its exceptions at dbd7c24e3: W-F17's line 261 %s; W-C3's line 91 %s" % (pp(B, WF17, {261}), pp(B, WC3, {91})))
named = [("item 1, W-A2's lines 110 and 187", WA2, {110, 187}), ("item 2, units 1052 and 1124", ST, {1052, 1124}), ("item 3, W-F17's lines 226, 232, 251, 261", WF17, {226, 232, 251, 261}), ("item 4, W-C3's line 91", WC3, {91}),
         ("item 5, units 1231 and 1267", ST, {1231, 1267}), ("item 6, units 1324 and 1328", ST, {1324, 1328})]
left = 0
for name, stem, lines in named:
    then, now = at(B, stem, lines), at(NOW, stem, lines); left += sum(v[1] == "VERIFIED" for v in now.values())
    print("Y4: %s: at dbd7c24e3 all under a verified record: %s (%s); now: %s" % (name, all(v[1] == "VERIFIED" for v in then.values()) and len(then) == len(lines), sorted({v[0] for v in then.values()}), {l: "%s %s" % v for l, v in sorted(now.items())}))
print("Y4: of the units its 15.2 names, still under a verified record now: %d (W-A2's line 187 is one, by design: see Y5)" % left)
old = git("show", "dbd7c24e3:%schecks/web_wa2_readout.py" % REL); new = (HERE / "web_wa2_readout.py").read_text(); run = (HERE / "web_wa2_readout_run.txt").read_text()
print("Y5: main's read-out at dbd7c24e3 took its reality test from U_L(T) alone: %s; it now tests U_L(S) too: %s; its run says U_L(S) is a real signed permutation up to one phase in all eight cases: %s; and the constant under T it prints: %s"
      % ("ph = UT[np.abs(UT) > 0.5]" in old and "US[np.abs" not in old and "realise" not in old, "realise(l[\"UL\"])" in new, "U_L(S) a real signed permutation up to one phase: True" in run, re.search(r"reading S (\[[^\]]*\]), reading St (\[[^\]]*\])", run).groups()))
wf = (HERE / "web_wf17_on_main.py").read_text()
print("Y6: main's script for W-F17 names E0 or a Chebyshev polynomial: %s (so line 251's check is the seat's alone)" % bool(re.search(r"E0|[Cc]hebyshev", wf)))
mrun = (HERE / "web_p783_spectrum_run.txt").read_text(); mine = {}
for val, body in re.findall(r"P4: at the lane's value ([0-9.]+) the least scaled singular value, by class \(the smallest of the three heights\): (.*)", mrun):
    mine[val] = {tuple(int(x) for x in m.group(1).split(",")): float(m.group(2)) for m in re.finditer(r"\((-?1, -?1)\) ([0-9.e+-]+)", body)}
sout = git("show", "ab3b69517:relays/chat1_2026-11-11_p783/p783_spectrum_out.txt"); theirs = {}
for val, body in re.findall(r"REPORTED  the lane's value ([0-9.]+): (\{.*\})", sout):
    d = json.loads(body.replace("'", '"')); theirs[val] = {tuple(int(x) for x in k.strip("()").split(",")): v["smallest_scaled_singular"] for k, v in d.items()}
ratios = {(val, c): theirs[val][c] / mine[val][c] for val in mine for c in mine[val]}
print("Y7: the seat's least scaled singular value over main's, class by class: %s" % "; ".join("%s %s: %.2g" % (v, c, r) for (v, c), r in sorted(ratios.items())))
print("Y7: cells where main's is smaller by ten or more: %d of 8; smaller by less than ten: %s; LARGER than the seat's: %s (so 'smaller by a factor of ten or more', main's note in web-p783-06p, was wrong in two cells, as the seat says)"
      % (sum(r >= 10 for r in ratios.values()), ["%s %s: %.1f" % (v, c, r) for (v, c), r in ratios.items() if 1 <= r < 10], ["%s %s: main's is %.1f times the seat's" % (v, c, 1 / r) for (v, c), r in ratios.items() if r < 1]))
r14 = B[3]["web-st14-01"]; lines14 = {int(u.rpartition(":")[2]) for u in r14["units"]}
print("Y8: web-st14-01 at dbd7c24e3: %s, %d units; it holds the units 1363, 1368, 1371, 1380, 1381, 1383 (claims the corrected version lists as wrong): %s; and 1373, 1385 to 1390: %s; its ground says the eight records 'stand as it lists them': %s; verified statements of the lane then, less these: %d (the second reading's count was 1,942)"
      % (r14["verdict"], len(r14["units"]), {1363, 1368, 1371, 1380, 1381, 1383} <= lines14, ({1373} | set(range(1385, 1391))) & lines14 == ({1373} | set(range(1385, 1391))) & {int(i.rpartition(":")[2]) for i in B[0] if ST in i}, "stand as it lists them" in r14["how"], tot("dbd7c24e3")["VERIFIED"] - len(r14["units"])))
print("Y8: its ground also says 'main has since read the move under S and the reality of the signs' (15.2, item 1): %s" % ("main has since read the move under S and the reality of the signs" in r14["how"]))
