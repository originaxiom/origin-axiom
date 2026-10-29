"""P-418's graded vector, second row: FR-FIB's two-Higgs branch (the web seat's TWO_HIGGS, verified on main as B1742).
Print it from FR_FIB_TWO_HIGGS_ENTRY.json, recompute every menu count that can be recomputed, and check every other
typed item by quoting its source.  Main's files are read with git show at the entry's as_of_main, this branch's at its
as_of_seat; nothing is written to either.  Data-free: no measured number is read.  The web seat, 2026-10-29.  0 of 19.

Recomputed: the ten lines and the grid (TWO_HIGGS's own definitions), the 266 lines (B1726's lines(), run alone), the
Higgs menu from its stated rule, the 27 sector assignments and the nine searched, the horocycles, c's scan (B1798),
the readings (B1741's COV), the unused UNEARNED rows, the union-find's sources, the bits.  Quoted: every label's
evidence and every reduction.  Typed: the end's scale as a binary; the weight's count of seven, as in the first row.

Checks: K1 citations exist; K2 menus equal their recomputation; K3 quotes in their own source; K4 the identification
rows (UNEARNED, reductions quoted, sources as expected, every UNEARNED row accounted for); K5 the bits.
"""
import ast, functools, itertools, json, math, pathlib, re, subprocess, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
E = json.loads((HERE / "FR_FIB_TWO_HIGGS_ENTRY.json").read_text(encoding="utf-8"))
MREV, SREV = E["as_of_main"], E["as_of_seat"]
FAILS = []


def show(rev, path):
    return subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (rev, path)], check=True,
                          capture_output=True).stdout.decode("utf-8")


ARCS = {}
for p in subprocess.run(["git", "-C", str(ROOT), "ls-tree", "--name-only", MREV, "frontier/"], check=True,
                        capture_output=True).stdout.decode("utf-8").split():
    m = re.match(r"frontier/(B\d+)_", p)
    if m: ARCS.setdefault(m.group(1), []).append(p)


def arc(b, name="FINDINGS.md"):
    assert len(ARCS[b]) == 1, (b, ARCS[b])
    return show(MREV, ARCS[b][0] + "/" + name)


def seat(path): return show(SREV, path)


def check(tag, ok, detail=""):
    print("%-4s %-5s %s" % (tag, "PASS" if ok else "FAIL", detail))
    if not ok: FAILS.append((tag, detail))


REG = show(MREV, "docs/POINT_REGISTER.md")
IDL = show(MREV, "docs/IDENTIFICATION_LEDGER.md")
REG_ROWS = {m.group(1): m.group(0) for m in re.finditer(r"^\| (P-\d+) \|.*$", REG, flags=re.M)}
ID_ROWS = {m.group(1): m.group(0) for m in re.finditer(r"^\| (I-\d+) \|.*$", IDL, flags=re.M)}
TH = "relays/chat1_2026-10-23_two_higgs/"
ZF = "relays/chat1_2026-10-23_zero_free_frame/ZERO_FREE_FRAME_EXPLORATION.md"

# ---------------------------------------------------------------- K1
cited = set()
def walk(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ("evidence", "route", "source", "arcs"): cited.update(v)
            walk(v)
    elif isinstance(x, list):
        for v in x: walk(v)
walk(E)
I = E["identifications"]
for r in I["rows"] + I["not_used"]: cited.add(r["id"])
cited.update(I["not_entered"]["rows"])
missing = [c for c in sorted(cited) if not (
    (re.fullmatch(r"B\d+", c) and c in ARCS) or (re.fullmatch(r"P-\d+", c) and c in REG_ROWS) or
    (re.fullmatch(r"I-\d+", c) and c in ID_ROWS) or (c == "GENESIS" and show(MREV, "GENESIS.md")))]
check("K1", not missing, "%d citations, missing: %s" % (len(cited), missing or "none"))

# ---------------------------------------------------------------- K2: the menus, recomputed
test = seat(TH + "two_higgs_test.py")
defs = {}
for node in ast.parse(test).body:
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and node.targets[0].id in (
            "MENU", "PAIRS", "LINES", "RES", "IMS"):
        defs[node.targets[0].id] = node
ns = {"Fr": Fr, "range": range, "round": round}
for name in ("MENU", "PAIRS", "LINES", "RES", "IMS"):
    exec(compile(ast.Module(body=[defs[name]], type_ignores=[]), name, "exec"), ns)
MENU, PAIRS, LINES, RES, IMS = (ns[k] for k in ("MENU", "PAIRS", "LINES", "RES", "IMS"))
menu_a = sorted(int(m.split("_")[1]) for m in MENU)
cen = arc("B1726", "verification/census.py")
fn = next(n for n in ast.parse(cen).body if isinstance(n, ast.FunctionDef) and n.name == "lines")
ns2 = {"math": math, "Fr": Fr, "functools": functools}
exec(compile(ast.Module(body=[fn], type_ignores=[]), "lines", "exec"), ns2)
L266 = ns2["lines"]()
rbs = seat("relays/chat1_2026-10-23_route_b/route_b_scan.py")
hors = ast.literal_eval(re.search(r"^HORS = (\[.*\])", rbs, flags=re.M).group(1))
f98 = arc("B1798")
cs = next(s for s in re.findall(r"c ∈ \{([^}]*)\}", f98) if s.startswith("1/3, 1/2, 2/3"))
cvals = [Fr(x.strip()) for x in cs.split(",")]
cmp41 = arc("B1741", "verification/compare.py")
cov = eval(re.search(r"^COV = (tuple\(.*\))\s*$", cmp41, flags=re.M).group(1), {"tuple": tuple, "range": range})
assign27 = list(itertools.product(MENU, repeat=3))                        # (up, down, lepton)
typeII = [x for x in assign27 if x[1] == x[2]]
check("K2", len(LINES) == 10 and all(a == Fr(2, 5) for a, _ in LINES) and set(LINES) <= set(L266) and len(L266) == 266,
      "lines: the test's %d lines are (2/5, k/10), all among B1713's %d" % (len(LINES), len(L266)))
check("K2", len(RES) == 8 and len(IMS) == 16 and len(LINES) * len(RES) * len(IMS) == 1280 and min(IMS) == 2.0 and max(IMS) == 3.5,
      "grid: %d Re tau (%.4f-%.4f) x %d Im tau (%.1f-%.1f) x %d lines = %d points" % (
          len(RES), min(RES), max(RES), len(IMS), min(IMS), max(IMS), len(LINES), len(LINES) * len(RES) * len(IMS)))
check("K2", (0.5625 in RES) and (2.6 in IMS) and (Fr(2, 5), Fr(1, 10)) in LINES, "the best row 0.5625 + 2.6i on (2/5, 1/10) is a grid point")
mr = E["menu_rule"]
zf = seat(ZF)
mline = re.search(r"With one unit of end data the members are a = (.*?)\n", zf).group(1)
mline = re.sub(r"\(r = \d+\)", "", mline)
members = [int(t.replace("−", "-")) for t in re.findall(r"[−-]?\d+", mline)]
rule_ok = all(a % 4 == 2 for a in members) and sorted({(2 * a) % 24 for a in members}) == [4, 12, 20]
eps = {a: 1j ** ((a + 2) // 2) for a in members}                        # eps = i^((a+2)/2), the stated rule
derived = sorted(a for a in members if (2 * a) % 24 in mr["r_three_generations"] and abs(eps[a] - 1) < 1e-12)
check("K2", rule_ok and derived == sorted(mr["menu"]) == menu_a,
      "the menu from its rule: of %d members (a = 2 mod 4, r = 2a mod 24 in {4, 12, 20}), r in %s and eps = +1 (a = 6 mod 8) "
      "leave %s; the test's MENU is %s" % (len(members), mr["r_three_generations"], derived, menu_a))
COUNT = {"line": ("open", len(L266)), "higgs_assignment": (len(assign27), len(PAIRS)), "reading": (len(set(cov)), 4),                                   # four readings seen: quoted in K3
         "c": ("open", len(cvals)), "horocycle": (len(hors), len(hors)), "end_scale": (2, None), "weight": ("open", None)}
check("K2", sorted(PAIRS) == sorted((u, d) for u, d, e in typeII) and len(PAIRS) == 9,
      "assignments: %d in all; the %d with down = leptons are the test's PAIRS" % (len(assign27), len(typeII)))
for d in E["discrete"]:
    o, s = COUNT[d["id"]]
    check("K2", o == d["options"] and s == d["searched"], "%s: options %s (entry %s), searched %s (entry %s)" % (
        d["id"], o, d["options"], s, d["searched"]))
check("K2", E["discrete"][0]["searched_in_test"] == len(LINES), "the line: %d searched in the test" % len(LINES))

# ---------------------------------------------------------------- K3: quotes, each in its own source
RULE, RES_ = seat(TH + "TWO_HIGGS_RULE.md"), seat(TH + "TWO_HIGGS_RESULT.md")
Q = [
    ("B1742", arc("B1742"), "best six-row (F₆ ∣ F₂₂, 0.5625 + 2.6i, (2/5, 1/10), L₂)"),
    ("B1742", arc("B1742"), "| χ²_six (σ² = rel² + 0.10², B1720's) | 1.19 | 1.1884 |"),
    ("B1742", arc("B1742"), "| rows below 16.75 | 14, all F₆ ∣ F₂₂, Im τ 2.6, L₂"),
    ("B1742", arc("B1742"), "χ²_six 1.04–3.43"),
    ("B1742", arc("B1742"), "the pair is chosen by the data out of six"),
    ("B1742", arc("B1742"), "F₂₂'s QI component is θ₂²²/θ₃²² ≈ 10⁻¹³"),
    ("B1742", arc("B1742"), "| with c = 1 at that row | worst six 3.20 | 3.198 |"),
    ("B1742", arc("B1742"), "| the full grid (15 360 off-diagonal rows): min χ²_six; min χ²_nine | 1.19; 154.1 | 1.1884; 154.14 |"),
    ("B1809", arc("B1809"), "outside H-cov's proofs"),
    ("B1750", arc("B1750"), "free (set by hand)"),
    ("B1740 census.py", arc("B1740", "verification/census.py"), "L read at Im tau from its Re tau = 1/4 column"),
    ("P-355", REG_ROWS["P-355"], "excludes at 14σ"),
    ("P-351", REG_ROWS["P-351"], "A READING (the pair chosen by the data"),
    ("P-365", REG_ROWS["P-365"], "the comparison at M_Z is a choice"),
    ("TWO_HIGGS_RULE", RULE, "This restriction is a choice made after those results"),
    ("TWO_HIGGS_RULE", RULE, "both read S (holomorphic)"),
    ("TWO_HIGGS_RULE", RULE, "H_u for the up quarks and H_d for the down quarks and the leptons"),
    ("TWO_HIGGS_RESULT", RES_, "With c = 1 the six is 3.20: the hand-set factor is essential."),
    ("TWO_HIGGS_RESULT", RES_, "PF1-W is a reading; holomorphy applies to the Higgs factor only."),
    ("TWO_HIGGS_RESULT", RES_, "the menu (fixed after the zero-free census)"),
    ("TWO_HIGGS_RESULT", RES_, "the two-doublet idea itself, which came from the framing read-outs"),
    ("TWO_HIGGS_RESULT", RES_, "0.15% of random four-target sets"),
    ("TWO_HIGGS_RESULT", RES_, "The two lepton ratios miss by 230σ and 54σ"),
    ("TWO_HIGGS_RESULT", RES_, "\"If S stands for the Higgs doublet\" is a reading"),
    ("TWO_HIGGS_RESULT", RES_, "χ²_six at this row is 5.8"),
    ("TWO_HIGGS_RESULT", RES_, "at 2 × 10¹⁶ GeV in the SM m_c/m_t moves to 4.8σ"),
    ("TWO_HIGGS_RESULT", RES_, "every pair with F_−2 misses (25–167)"),
    ("ZERO_FREE_FRAME_EXPLORATION", seat(ZF), "With one unit of end data the members are a = −10, 2, 14, 26 (r = 4); −6, 6, 18 (r = 12); and −2, 10, 22"),
    ("ZERO_FREE_FRAME_EXPLORATION", seat(ZF), "W127 counts three generations at r = 12 and 20"),
    ("ZERO_FREE_FRAME_EXPLORATION", seat(ZF), "that leaves F_6, F_−2 and F_22, and F_−2 fails"),
    ("ZERO_FREE_FRAME_EXPLORATION", seat(ZF), "a ≡ 2 (mod 4), ε = i^{(a+2)/2} and r ≡ 2a (mod 24)"),
    ("THE EXACT END", seat("relays/CHAT1_TO_CC_AND_SM_2026-10-28_THE_EXACT_END_THE_SELECTOR_AND_THE_AUDIT.md"),
     "at L₂ the exact norms of the frame's twisted kernels agree with 2πL₂ + c_s to 0.6%"),
    ("route_b_scan.py", rbs, "return v[0] * B.QI + v[1] * B.QJ + v[2] * B.QK"),
    ("B1753", arc("B1753"), "10.75 (1.6σ) at the χ²-best row"),
    ("B1753", arc("B1753"), "10.48–11.32 over the rows below the bar"),
    ("B1753", arc("B1753"), "nine fail (χ²_nine 183"),
    ("B1726", arc("B1726"), "35–38% below it, and with them the six fail near the four families' rows"),
    ("B1730", arc("B1730"), "IS ZERO-FREE ONLY IF r ≡ 4 MOD 8"),
    ("B1790", arc("B1790"), "the MSSM's H_u, H_d"),
    ("P-094", REG_ROWS["P-094"], "10.58 ± 0.11"),
    ("P-377", REG_ROWS["P-377"], "reaches χ²_nine 47 at best"),
    ("P-421", REG_ROWS["P-421"], "or the scale is an input"),
    ("P-287", REG_ROWS["P-287"], "the fits put Im τ near 2.7 at the second horocycle and near 3.1 at the first"),
    ("TWO_HIGGS_RULE", RULE, "Im τ ∈ {2.0, 2.1, …, 3.5} (16 values)"),
    ("TWO_HIGGS_RULE", RULE, "the readings S, S̃ and the two mixed ones"),
    ("TWO_HIGGS_RESULT", RES_, "depends on tan β"),
    ("ZERO_FREE_FRAME_EXPLORATION", seat(ZF), "only the ε = +1 lines with a ≥ 6 reach"),
    ("ZERO_FREE_FRAME_EXPLORATION", seat(ZF), "Main's frame is outside PF1-W as written"),
    ("ZERO_FREE_FRAME_EXPLORATION", seat(ZF), "Where χ_η^r is absorbed (the fermions' twists or a counterterm) is not tested"),
    ("I-32", ID_ROWS["I-32"], "the weave's Higgs line as the electroweak Higgs"),
    ("I-33", ID_ROWS["I-33"], "T-NORM by hand, B1654"),
]
for src, t, q in Q:
    check("K3", q in t, "%s: '%s'" % (src, q[:96]))

# ---------------------------------------------------------------- K4
def covers(row, b):
    n = int(b[1:])
    return bool(re.search(r"\b%s\b" % b, row)) or any(int(x) <= n <= int(y) for x, y in re.findall(r"B(\d+)[–-]B(\d+)", row))
def status(i): return re.search(r"\*\*(EARNED|REFUTED|UNEARNED)\*\*", ID_ROWS[i]).group(1)
par = {}
def find(x):
    par.setdefault(x, x)
    while par[x] != x: x = par[x]
    return x
used = I["rows"]
for r in used:
    row = ID_ROWS[r["id"]]
    q_ok = (r["quote"] is None or r["quote"] in row) and (r["reduces_to"] is None or r["reduces_to"] in (r["quote"] or ""))
    a_ok = all(covers(row, b) for b in r["arcs"])
    check("K4", status(r["id"]) == "UNEARNED" and q_ok and a_ok, "%s %s; reduction quote %s; arcs %s %s" % (
        r["id"], status(r["id"]), "found" if q_ok else "MISSING", r["arcs"], "cited" if a_ok else "NOT ALL CITED"))
    find(r["id"])
    if r["reduces_to"]:
        assert status(r["reduces_to"]) == "UNEARNED", r
        par[find(r["id"])] = find(r["reduces_to"])
groups = {}
for r in used: groups.setdefault(find(r["id"]), []).append(r["id"])
check("K4", len(groups) == I["expected_sources"], "union-find: %d rows -> %d sources (entry expects %d): %s" % (
    len(used), len(groups), I["expected_sources"], "; ".join("[%s] %s" % (k, ", ".join(v)) for k, v in sorted(groups.items()))))
unearned = {i for i in ID_ROWS if status(i) == "UNEARNED"}
listed = [r["id"] for r in used] + [r["id"] for r in I["not_used"]] + I["not_entered"]["rows"]
check("K4", set(listed) == unearned and len(listed) == len(set(listed)), "the ledger's %d UNEARNED rows = %d used + %d not used + %d not entered" % (
    len(unearned), len(used), len(I["not_used"]), len(I["not_entered"]["rows"])))

# ---------------------------------------------------------------- K5: the bits
on_data = by_hand = 0.0
out = []
for d in E["discrete"]:
    o, s = COUNT[d["id"]]
    bm = math.log2(o) if isinstance(o, int) else None
    bs = math.log2(s) if s else None
    if "on the data" in d["label"]:
        on_data += bs
        if bm is not None: by_hand += bm - bs
    else:
        by_hand += bm if bm is not None else math.log2(7)
    out.append("    %-17s %-40s %-62s options %-5s bits %-5s searched %-4s bits %-5s" % (
        d["id"], d["value"][:40], d["label"][:62], o, "%.2f" % bm if bm is not None else "open", s if s else "-",
        "%.2f" % bs if bs is not None else "-"))
check("K5", all(("on the data" in d["label"]) == (d["searched"] is not None) for d in E["discrete"]),
      "every item chosen on the data has a search count and no item chosen by hand has one")

print()
print("THE VECTOR — FR-FIB's two-Higgs branch on the six, at main %s and seat %s" % (MREV, SREV))
fc, cc = E["fitted_continuous"], E["chosen_continuous"]
print("  fitted continuous (%d): %s" % (len(fc), ", ".join("%s = %s" % (p["name"], p["value"].split(" (")[0]) for p in fc)))
print("  continuous, set by hand (%d): %s" % (len(cc), ", ".join("%s = %s" % (p["name"], p["value"]) for p in cc)))
print("  discrete (%d; %d chosen on the data, %d by hand):" % (len(E["discrete"]),
      sum("on the data" in d["label"] for d in E["discrete"]), sum("on the data" not in d["label"] for d in E["discrete"])))
print("\n".join(out))
print("  bits (a heuristic, not a bound): %.2f searched on the data, %.2f set by hand; %.2f in all" % (on_data, by_hand, on_data + by_hand))
print("  identifications: %d rows -> %d irreducible sources: %s; not used: %s; not entered: %d" % (
    len(used), len(groups), "; ".join("[%s] %s" % (k, ", ".join(v)) for k, v in sorted(groups.items())),
    ", ".join(r["id"] for r in I["not_used"]), len(I["not_entered"]["rows"])))
print("  tagged hypotheses (listed, not counted): %s" % ", ".join(h["id"] for h in E["hypotheses"]))
print("  unpriced looks (searches with the data in view that no bits here price): %d" % len(E["unpriced_looks"]))
print("  bought: %s" % E["reach"]["bought"])
print()
print("RESULT: %s" % ("ALL CHECKS PASS" if not FAILS else "%d FAIL: %s" % (len(FAILS), FAILS)))
sys.exit(1 if FAILS else 0)
