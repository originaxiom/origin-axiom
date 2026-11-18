"""B1957: agy-exp's Review 83 reading (20 findings on main's own window, relays/REVIEW_83_AGY-EXP.md at 48a4054aa), each
finding's items tested by main on main's present files, with its state: a plant (absent on main), mended (B1950, or since,
by a dated correction beside the text or a changed line), or standing (true on main's head; action item R83-1).
Nothing of the seat's is run; its quotations were checked at the reading commit by B1950's quote_check.py."""
import json, math, pathlib, re, subprocess, sys
import sympy as sp
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
A = lambda pat: next((ROOT / "frontier").glob(pat)); T = lambda p: pathlib.Path(p).read_text()
has = lambda p, s: s in T(p); OUT = []
def row(n, basis, state): OUT.append((n, bool(basis), state))

if __name__ == "__main__":
    from sympy.matrices.normalforms import smith_normal_form
    b = {x: A("B19%s_*" % x) for x in ("28", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45")}
    sb = T(ROOT / "docs/TOTAL_INPUTS_SCOREBOARD.md"); gen = T(ROOT / "scripts/checks/inputs_scoreboard.py")
    # the six plants: main's files carry the right figures
    row("01", has(b["38"] / "FINDINGS.md", "max |z| 6.4") and not has(b["38"] / "FINDINGS.md", "max |z| 2.4"), "plant")
    row("02", not has(b["40"] / "FINDINGS.md", "0.086 in ln"), "plant"); row("03", not has(b["41"] / "FINDINGS.md", "+1.83"), "plant")
    row("04", not has(b["42"] / "FINDINGS.md", "each hit six times") and 15 ** 2 - 5 ** 2 - 3 ** 2 + 1 == 192 and 192 // 24 == 8, "plant")
    LR = sp.Matrix([[2, 1], [1, 1]]); sm = lambda M: [abs(x) for x in smith_normal_form(M, domain=sp.ZZ).diagonal()]
    row("05", has(b["43"] / "FINDINGS.md", "Smith(LR + I) = (1, 5)") and sm(LR + sp.eye(2)) == [1, 5], "plant"); row("06", not has(b["44"] / "FINDINGS.md", "| 1.21 | 7.6 |"), "plant")
    # 07: m003 = -LR has torsion of order 5; the board no longer lists it under SE1
    carried = [str(q) for d in (ROOT / "docs", A("B1858_*"), A("B1861_*")) for q in d.rglob("*") if q.is_file() and q.suffix in (".md", ".json") and "selects the class of LR (m004, m003)" in q.read_text(errors="ignore")]
    row("07", sm(-LR - sp.eye(2)) == [1, 5] and "(m004, m003)" not in sb and not carried and not (ROOT / "docs/atlas/MAP.md").exists(), "mended (no page carries the sentence; the atlas path the finding names for its travel does not exist)")
    # 08: the threshold literal; the lock's two frames; the truncated cells
    t34 = T(A("B1834_*") / "verification/test_b1834_the_total_inputs_scoreboard.py")
    row("08.1", "against 22.0" not in sb and "against 22.0" not in T(ROOT / "docs/total_inputs_scoreboard.json"), "mended since (2026-11-18)")
    row("08.2", "6 rows claimed, 14 borrowed joints" in t34 and "7 rows claimed, 12 borrowed" not in t34 and "both frames stand on it" in sb and 'other = "A" if key == "B" else "B"' in gen, "standing")
    row("08.3", "[:300]" in gen and any(l.startswith("| C02") and l.rstrip().endswith("of one |") for l in sb.splitlines()), "standing")
    # 09: the unused variable; the three figures; the later output file and no dated note
    l32 = T(b["32"] / "verification/test_b1932_values_and_seal.py"); f32 = T(b["32"] / "FINDINGS.md")
    row("09.1", "a = json.loads(" in l32 and re.search(r"\ba\[", l32) is None, "standing")
    e = json.loads(T(b["32"] / "verification/ergodic_t90.json")); v = json.loads(T(b["32"] / "verification/BIG_RUN_VALUES.json"))["options"]; q2 = T(b["32"] / "verification/pairs/q2_run.txt")
    sh = [abs(d) / (s / r) for d, s, r in zip(e["dln"], e["se_truncated"], e["R_truncated"])]; spr = [abs(math.log(y / x)) for x, y in zip(v["W+|a (move count)"]["values"], v["W+|b (area)"]["values"])]
    row("09.2", "each shift 5 to 11 times" in f32 and min(sh) < 5 and "differ** by 0.10 to 0.58 in ln on the seven values" in f32 and min(spr) < 0.08 and "mirror-symmetric to 8e-11" in f32 and "canon L_2: max |log| 2.48e-05" in q2, "standing")
    row("09.3", (b["32"] / "verification/big_run_output.json").exists() and "B1940" not in f32 and json.loads(T(b["32"] / "arc_verdict.json")).get("superseded_by") is None, "standing")
    # 10: the lock's S has no Weil phase; with the true quadratic T the group it generates has order 240, with -S 120
    sys.path.insert(0, str(b["34"] / "verification")); import numpy as np, level_five_structure as L
    S = np.array([[L.W ** (x * y) for y in range(L.P)] for x in range(L.P)]) / np.sqrt(L.P); Tq = np.diag([L.W ** (x * x) for x in range(L.P)])
    o1, o2 = len(L.generate([S, Tq])), len(L.generate([-S, Tq]))
    row("10", (o1, o2) == (240, 120) and "S = np.array([[L.W ** (x * y) for y in range(L.P)] for x in range(L.P)]) / np.sqrt(L.P)" in T(b["34"] / "verification/test_b1934_level_five_structure.py"), "standing")
    row("11", has(b["35"] / "FINDINGS.md", "agy-exp's F-R83-11"), "mended")
    # 12: the conjugate of the degree-0 singlet; the sign of the (0, 4, 1) trilinear; 15 components listed for 16
    v36 = json.loads(T(b["36"] / "arc_verdict.json"))["claim_one_line"]
    row("12", has(b["36"] / "FINDINGS.md", "every conjugate at 5 − k") and "(kc == (5 - expect[f]) % 5)" in T(b["36"] / "verification/degrees.py") and (5 - 0) % 5 == 0 and (-1) ** (0 + 4 + 1) == -1 and "16 of 32" in v36 and "Q, u, e at 2, d, L at 4" in v36 and "neutrino" not in v36, "standing")
    f37 = T(b["37"] / "FINDINGS.md"); rule = T(b["37"] / "verification/BIG_RUN_RULE_v2.md"); a7 = rule.split("**A7.")[1].split("**A8.")[0]
    row("13.1", len(re.findall(r"^def test_", T(b["37"] / "verification/test_b1937_rule_v2.py"), re.M)) == 10 and "nine tests" in f37, "standing")
    row("13.2", "A1 to A12" in f37 and "A15" in rule and "nine joints" in rule, "standing")
    row("13.3", "S10" in a7 and "X_1(5)" not in a7 and "four cusps" not in a7, "standing")
    row("13.4", all('"a": (-2.0, 0.3)' in T(p) for p in (b["37"] / "verification/big_run_windows.py", b["40"] / "verification/big_run_windows_v3.py")) and 10 ** 0.3 > 1.99, "standing")
    f38 = T(b["38"] / "FINDINGS.md")
    row("14", "max(diffs) < 1e-12" not in T(b["38"] / "verification/test_b1938_coupling_and_gauge_class.py") and "No figure here uses" in f38 and "(0.6 + .5, 0.2)" in T(b["38"] / "verification/residue_as_determinants.py"), "mended (the lock); standing (the sentence on unreduced twists)")
    f39 = T(b["39"] / "FINDINGS.md"); v39 = json.loads(T(b["39"] / "arc_verdict.json")); hl = T(ROOT / "docs/HARVEST_LEDGER.md")
    row("15.1", "Those are V's, the conjugate" in f39 and "The weave triplet V" in f39, "standing")
    row("15.2", "for every once-punctured torus bundle" in f39, "standing")
    row("15.3", 'v.count("CAUGHT") >= 3 and "MISSED" not in v' in T(b["39"] / "verification/test_b1939_five_claims.py"), "standing")
    row("15.4", "THE AGY SEATS" in v39["claim_one_line"] and all(re.search(r"^\| %s \|.*OWED" % r, hl, re.M) for r in ("1676", "1677", "1678", "1696", "1710", "1815")), "standing")
    # 16: the verdict file; the W+ cusp limit, recomputed; the lock and the extended-precision file
    v40 = json.loads(T(b["40"] / "arc_verdict.json")); row("16.1", bool(v40.get("cites_seat")) and "Review 83" in v40["claim_one_line"] and "second computation owed" in v40["claim_one_line"], "mended in part (the seat is cited and the line carries a dated note; the words 'second computation owed' still stand in it)")
    sys.path.insert(0, str(b["45"] / "verification")); import determinant_law as DL, cusp_mixing as CM
    mp = DL.mp; counts = {}; tie = None
    for y in (30.0, 45.0, 85.0):
        c = {"12": 0, "23": 0, "13": 0, "m12": 0, "m23": 0, "m13": 0}
        for i in range(5):
            for j in range(5):
                if (i, j) == (0, 0): continue
                _, _, Yu, *_ = DL.parts("0.13", y, Fr(i, 5), Fr(j, 5), "up"); _, _, Yd, *_ = DL.parts("0.13", y, Fr(i, 5), Fr(j, 5), "down")
                V = CM.U_of(Yu["S"]).H * CM.U_of(Yd["St"]); W = CM.U_of(Yu["St"]).H * CM.U_of(Yd["S"])
                for k, (r, cc) in (("12", (0, 1)), ("23", (1, 2)), ("13", (0, 2))):
                    c[k] += round(float(abs(V[r, cc]))); c["m" + k] += round(float(abs(W[r, cc])))
                if y == 30.0 and (i, j) == (0, 1): s = sorted(abs(x) for x in mp.svd_c(Yd["St"], compute_uv=False)); tie = float(s[1] / s[0])
        counts[y] = c
    plus = lambda y: (counts[y]["12"], counts[y]["23"], counts[y]["13"]); minus = lambda y: (counts[y]["m12"], counts[y]["m23"], counts[y]["m13"])
    row("16.2", plus(45.0) == plus(85.0) == (14, 14, 10) and minus(45.0) == minus(85.0) == (10, 10, 14) and plus(30.0) == (12, 14, 10) and has(b["40"] / "FINDINGS.md", "agy-exp's F-R83-16"), "mended since (2026-11-18, dated notes on B1940, B1945 and the open-leads entry)")
    row("16.3", "area_measure_mp.json" not in T(b["40"] / "verification/test_b1940_corrected_values_and_v3.py"), "standing")
    v44 = json.loads(T(b["44"] / "arc_verdict.json")); f44 = T(b["44"] / "FINDINGS.md")
    row("17.1", any("SM-C15" in s for s in v44["cites_seat"]) and "SM-C15" in v44["claim_one_line"], "mended in part (the card is cited; the line still names it)")
    row("17.2", not any(k in f44 for k in ("worst_factor_six", "worst_factor_nine", "worst_factor_seven")) and "wall teaches" not in T(ROOT / "docs/OPEN_LEADS.md"), "standing")
    row("17.3", "reads only those three files" in f44 and "L.targets(" in T(b["44"] / "verification/read_the_look.py"), "standing")
    v33 = json.loads(T(b["33"] / "arc_verdict.json"))["claim_one_line"]; t30 = T(next((b["30"] / "verification").glob("test_b1930*.py")))
    row("18.1", "the SM seat" in v33 and "agy-exp's X-NEVER" in v33, "standing")
    row("18.2", "# a seventh path into a moved folder" in t30 and 'W.ARCHIVE + W.PATHS[0]' in t30, "standing")
    row("18.3", not list(b["31"].rglob("test_*.py")) and has(b["31"] / "FINDINGS.md", "the first review read by the other family"), "standing")
    row("18.4", T(b["28"] / "FINDINGS.md").splitlines()[2].startswith("**Verdict: OPEN** *[UPGRADED") and json.loads(T(b["28"] / "arc_verdict.json"))["verdict"] == "PROVED", "the header says OPEN with a dated note of the upgrade beside it")
    sw = T(ROOT / "docs/THE_SWEEP_OF_2026-11-14.md")
    row("19.1", "are marked offrecord_origin=true" in sw and sw.count("offrecord_origin=true") == 1, "standing")
    row("19.2", "forced given SE1" in T(ROOT / "docs/THE_PAIRS_PROGRAMME.md"), "standing")
    row("19.3", "cld-advisor.md M40" in sw and "The codex audit seat" in sw, "standing")
    row("20.1", "assert all(a in written for a in anchors if a), anchors" in T(ROOT / "tests/test_review_waiver_names_its_anchor.py"), "standing")
    sys.path.insert(0, str(ROOT / "scripts/gates")); import gates
    row("20.2", gates.selection_claims_in("The census selects (B1906) m004.") == [] and gates.selection_claims_in("The census selects m004.") != [] and gates.selection_claims_in("No rule (B1204) selects one member.") != [] and gates.selection_claims_in("No rule selects one member.") == [], "standing")
    # 19.4: the item's three statements against the commit read (b35eac607) and main's present files
    show = lambda path: subprocess.run(["git", "show", "b35eac607:" + path], capture_output=True, text=True, cwd=ROOT).stdout
    stale = show("docs/THE_STALE_OPEN_VERDICTS_O1_TO_O10.md").splitlines(); b1716 = show(str(A("B1716_*").relative_to(ROOT)) + "/FINDINGS.md"); reg = show("docs/POINT_REGISTER.md").splitlines()
    f194 = {"the ranked list put P-853 first at the commit read": reg[49].startswith("1. P-853"), "P-776 says R1 to R4 met": any(l.startswith("| P-776") and "R1 to R4 and R8 met" in l for l in reg),
            "the cited lines of the stale-verdicts page name B44": any("B44" in l for l in stale[154:159] + stale[196:199]), "B1716's page reaches line 256 or says 'met in part'": len(b1716.splitlines()) >= 256 or "met in part" in b1716}
    row("19.4", f194["the ranked list put P-853 first at the commit read"] and f194["P-776 says R1 to R4 met"] and not f194["the cited lines of the stale-verdicts page name B44"] and not f194["B1716's page reaches line 256 or says 'met in part'"], "two of its statements found, two of its citations not found at the commit read")
    # 20.3: curly quotes change no count; a new inner word on a line already entered in the errata is not reported
    phrase = " as the owner's lane ruled"; q0, q1 = dict(gates.public_face_words(phrase)), dict(gates.public_face_words("“" + phrase + "”"))
    rows_ = [[x.strip() for x in l.strip().strip("|").split(" | ")] for l in gates._read(gates.PUBLIC_FACE_ERRATA).split("\n")]
    rel, n = next((c[0].strip("`"), int(c[1])) for c in rows_ if len(c) == 4 and c[0].startswith("`") and c[1].isdigit())
    def patched(r):
        t = gates._read(r)
        if r != rel: return t
        ls = t.split("\n"); ls[n - 1] += phrase; return "\n".join(ls)
    row("20.3", q0 and q0 == q1 and gates.public_face_unentered(reader=patched) == gates.public_face_unentered(), "standing")
    lock = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", str(A("B1834_*") / "verification/test_b1834_the_total_inputs_scoreboard.py")], capture_output=True, text=True, cwd=ROOT)
    for n, basis, state in OUT: print("F-R83-%-4s: the facts the item rests on hold on main's files: %-5s  state: %s" % (n, basis, state))
    print("the group generated by the lock's S and the quadratic T: order %d; by -S and the same T: %d" % (o1, o2))
    print("the pair (S up, S~ down), points with |V12|, |V23|, |V13| = 1 at heights 30, 45, 85: %s, %s, %s; the pair (S~ up, S down): %s, %s, %s; at height 30 and the point (0, 1/5) the down sector's two light singular values are in the ratio %.3f"
          % (plus(30.0), plus(45.0), plus(85.0), minus(30.0), minus(45.0), minus(85.0), tie))
    print("B1834's lock on the present files: %s" % lock.stdout.strip().splitlines()[-1])
    print("items whose facts hold: %d of %d; plants %d; mended or answered %d; standing on main's head %d; item 19.4 in detail: %s"
          % (sum(x for _, x, _ in OUT), len(OUT), sum(s == "plant" for *_, s in OUT), sum(s.startswith(("mended", "the header", "two of")) for *_, s in OUT), sum(s == "standing" for *_, s in OUT), f194))
