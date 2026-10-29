"""P-418's graded vector for FR-FIB: print it from FR_FIB_ENTRY.json, recompute from main's committed files every menu
count that can be recomputed, and check every other typed item by quoting its source (read with git show at the
entry's pinned revision; nothing on main is written).  Data-free: no measured number is read.  The web seat,
2026-10-29.  0 of 19.

What is recomputed and what is only quoted:
  recomputed  the readings (B1741's SEAT and COV), the lines (B1726's lines(), executed alone), the apexes and their
              band (B1753's census), the horocycles (the census's keys), c's scan (B1798 sec. 4's set), the UNEARNED
              rows the entry does not use (the ledger minus the entry's lists), the union-find's sources, the bits;
  quoted      B1691's seven weights (its text), every label's evidence, every reduction between identification rows;
  typed       the end's scale and the shared section as binaries (by definition), the since-B1750 tally (read from
              B1750 sec. 2 by hand; its 'none removed' basis is quoted).

Checks (each prints PASS or FAIL; the exit code is 1 if any fails):
  K1  every arc (B####), register row (P-###) and identification row (I-##) the entry cites exists at the revision;
  K2  each menu count in the entry equals its recomputed value;
  K3  each quoted sentence occurs in its source; a register quote is searched in the cited row only, a ledger quote
      in the cited row only;
  K4  each identification row used is UNEARNED, its reduction is quoted from its own row, the union-find over the
      rows used gives the entry's expected number of sources, and every other UNEARNED row is listed as not used or
      not entered;
  K5  the bits: computed from the counts (log2 of the options or of the options searched), split by the label's
      'on the data' or 'by hand', and the two sums equal the total over the finite menus.
"""
import ast, functools, json, math, pathlib, re, subprocess, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
E = json.loads((HERE / "FR_FIB_ENTRY.json").read_text(encoding="utf-8"))
REV = E["as_of_main"]
FAILS = []


def show(path):
    return subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (REV, path)], check=True,
                          capture_output=True).stdout.decode("utf-8")


def tree(prefix):
    out = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "--name-only", REV, prefix], check=True,
                         capture_output=True).stdout.decode("utf-8")
    return out.split()


ARCS = {}
for p in tree("frontier/"):
    m = re.match(r"frontier/(B\d+)_", p)
    if m: ARCS.setdefault(m.group(1), []).append(p)


def arc(b, name="FINDINGS.md"):
    assert len(ARCS[b]) == 1, (b, ARCS[b])
    return show(ARCS[b][0] + "/" + name)


def check(tag, ok, detail=""):
    print("%-4s %-5s %s" % (tag, "PASS" if ok else "FAIL", detail))
    if not ok: FAILS.append((tag, detail))


REG = show("docs/POINT_REGISTER.md")
IDL = show("docs/IDENTIFICATION_LEDGER.md")
PLAN = show("docs/MAINS_PLAN.md")
RULES = show("WORKING_RULES.md")
REG_ROWS = {m.group(1): m.group(0) for m in re.finditer(r"^\| (P-\d+) \|.*$", REG, flags=re.M)}
ID_ROWS = {m.group(1): m.group(0) for m in re.finditer(r"^\| (I-\d+) \|.*$", IDL, flags=re.M)}

# ---------------------------------------------------------------- K1: every citation exists
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
missing = []
for c in sorted(cited):
    if re.fullmatch(r"B\d+", c): ok = c in ARCS
    elif re.fullmatch(r"P-\d+", c): ok = c in REG_ROWS
    elif re.fullmatch(r"I-\d+", c): ok = c in ID_ROWS
    elif c == "GENESIS": ok = bool(show("GENESIS.md"))
    else: ok = False
    if not ok: missing.append(c)
check("K1", not missing, "%d citations, missing: %s" % (len(cited), missing or "none"))

# ---------------------------------------------------------------- K2: the menus, recomputed
cmp41 = arc("B1741", "verification/compare.py")
seat = ast.literal_eval(re.search(r"^SEAT = (\(.*?\))\s*#", cmp41, flags=re.M).group(1))
cov = eval(re.search(r"^COV = (tuple\(.*\))\s*$", cmp41, flags=re.M).group(1), {"tuple": tuple, "range": range})
cen = arc("B1726", "verification/census.py")
fn = next(n for n in ast.parse(cen).body if isinstance(n, ast.FunctionDef) and n.name == "lines")
ns = {"math": math, "Fr": Fr, "functools": functools}
exec(compile(ast.Module(body=[fn], type_ignores=[]), "lines", "exec"), ns)
L = ns["lines"]()
rows = [json.loads(l) for l in arc("B1753", "verification/census.jsonl").splitlines() if l.strip()]
ap = sorted({(r["Re_tau"], r["Im_tau"]) for r in rows})
ims = [a[1] for a in ap]
hors = sorted({k.split("|")[1] for r in rows for k in r if k.count("|") >= 2})
f98 = arc("B1798")
cs = next(s for s in re.findall(r"c ∈ \{([^}]*)\}", f98) if s.startswith("1/3, 1/2, 2/3"))
cvals = [Fr(x.strip()) for x in cs.split(",")]
print("     recomputed: readings SEAT %s (%d), COV %d distinct; lines %d; apexes %d, Im tau %.4f-%.4f; horocycles %s; "
      "c's scan {%s} (%d)" % (seat, len(seat), len(set(cov)), len(L), len(ap), min(ims), max(ims), hors, cs, len(cvals)))
COUNT = {"reading": (len(set(cov)), len(set(cov))), "line": ("open", len(L)), "c": ("open", len(cvals)),
         "horocycle": (len(hors), len(hors)), "weight": ("open", None),
         "end_scale": (2, None), "shared_section": (2, None)}        # the last two: binaries by definition (typed)
for d in E["discrete"]:
    o, s = COUNT[d["id"]]
    check("K2", o == d["options"] and s == d["searched"],
          "%s: options %s (entry %s), searched %s (entry %s)" % (d["id"], o, d["options"], s, d["searched"]))
check("K2", (Fr(2, 5), Fr(1, 10)) in L and len(seat) == 2 and set(seat) <= set(cov),
      "the best row's line is among the 266; SEAT is two of COV's eight")
check("K2", len(ap) == 223 and 2.0 <= min(ims) and max(ims) <= 3.6, "223 apexes inside the band [2.0, 3.6]")
check("K2", Fr(3) in cvals, "c = 3 is in the scan")

# ---------------------------------------------------------------- K3: the quoted sentences, each in its own source
def reg(p): return REG_ROWS[p]
def idr(i): return ID_ROWS[i]
Q = [
    ("WORKING_RULES", RULES, "**FITTED** is a fourth label: a continuous value set by data"),
    ("WORKING_RULES", RULES, "every discrete item in P-406's census, carries one"),
    ("B1753", arc("B1753"), "2.74 at 0.3333 + 3.0368i on (2/5, 1/10), L_max, (S̃, S, S), c = 3"),
    ("B1742", arc("B1742"), "χ²_six 1.188"),
    ("B1742", arc("B1742"), "the pair is chosen by the data out of six"),
    ("B1798", f98, "The Clebsch 3 was chosen knowing the data's R2 = 3.14"),
    ("B1798", f98, "the apex band Im τ ∈ [2.0, 3.6]"),
    ("B1798", f98, "No input removed."),
    ("B1726", arc("B1726"), "35–38% below it, and with them the six fail near the four families' rows"),
    ("B1726", arc("B1726"), "The best six-row** (seat's and covariant menus alike)"),
    ("B1726", arc("B1726"), "seat's rows with the data in view"),
    ("B1726 census.py", cen, "L read at Im tau from its Re tau = 1/4 column"),
    ("B1790", arc("B1790"), "The data's preference for up S̃ fixed it"),
    ("B1790", arc("B1790"), "So the eight assignments are physically distinct"),
    ("B1791", arc("B1791"), "Im τ IS NOT FOUND FORCED"),
    ("B1750", arc("B1750"), "the Higgs's scalar part h₀ = 0"),
    ("B1750", arc("B1750"), "free discrete: the end, the line, c, h₀"),
    ("B1750", arc("B1750"), "| the comparison scale (M_Z) | PRECISION_BAR (HZ2021) | **identification**"),
    ("B1750", arc("B1750"), "L_max a rule informed post hoc"),
    ("B1750", arc("B1750"), "the **bar's**, not physics"),
    ("B1700", arc("B1700"), "ONLY ∂R, THE ONE WITH THE COUPLING TRIPLET'S OWN END CONDITION, GIVES A HIERARCHY"),
    ("B1691", arc("B1691"), "seven weights"),
    ("B1788", arc("B1788"), "PROVED at leading order in Im τ, conditional on § 5's hypotheses"),
    ("B1785", arc("B1785"), "the leptons equal the down quarks on α = 2/5 at the exponent level"),
    ("B1742", arc("B1742"), "For k odd they coincide only for a Higgs with no QI component"),
    ("B1809", arc("B1809"), "D: the weight class; a shared or per-sector section; h; the line"),
    ("B1809", arc("B1809"), "f(d) ≤ 2 with DR at a fixed line"),
    ("B1809", arc("B1809"), "**P-418:** f(d) per frame as a Jacobian rank"),
    ("P-365", reg("P-365"), "the comparison at M_Z is a choice"),
    ("P-365", reg("P-365"), "the Standard Model's H̃ was an identification made by hand (B1660)"),
    ("P-402", reg("P-402"), "selected by the data, not absorbed by τ"),
    ("P-402", reg("P-402"), "the end's scale is now P-421"),
    ("P-384", reg("P-384"), "the line rule is mostly a pick"),
    ("P-421", reg("P-421"), "or the scale is an input"),
    ("P-377", reg("P-377"), "one Higgs read everywhere reaches χ²_nine 47 at best"),
    ("P-432", reg("P-432"), "closed for B1656's frame at the n = 1 window"),
    ("P-418", reg("P-418"), "the scoreboard is a named, graded vector"),
    ("I-32", idr("I-32"), "the weave's Higgs line as the electroweak Higgs"),
    ("I-33", idr("I-33"), "T-NORM by hand, B1654"),
    ("I-35", idr("I-35"), "adopting it would reduce the reading from 3 bits to 1"),
    ("MAINS_PLAN", PLAN, "the slope is selected by the data, stably\n   out of sample, with one number's worth of input (e_up) — not removed"),
    ("MAINS_PLAN", PLAN, "one ratio fixes it (B1788)"),
    ("MAINS_PLAN", PLAN, "Re τ, and the line's position u = Re w mod 1 | continuous (two)"),
    ("MAINS_PLAN", PLAN, "do fitting work without a plan holding them"),
    ("MAINS_PLAN", PLAN, "**Named, not yet planned:** the horocycle and the comparison scale"),
    ("MAINS_PLAN", PLAN, "Today: none removed."),
]
for src, t, q in Q:
    check("K3", q in t, "%s: '%s'" % (src, q.replace("\n", " ")[:96]))

# ---------------------------------------------------------------- K4: the identification rows
def covers(row, b):
    n = int(b[1:])
    if re.search(r"\b%s\b" % b, row): return True
    return any(int(x) <= n <= int(y) for x, y in re.findall(r"B(\d+)[–-]B(\d+)", row))
def status(i): return re.search(r"\*\*(EARNED|REFUTED|UNEARNED)\*\*", ID_ROWS[i]).group(1)
par = {}
def find(x):
    par.setdefault(x, x)
    while par[x] != x: x = par[x]
    return x
used = I["rows"]
for r in used:
    row = ID_ROWS[r["id"]]
    q_ok = r["quote"] is None or r["quote"] in row
    a_ok = all(covers(row, b) for b in r["arcs"])
    check("K4", status(r["id"]) == "UNEARNED" and q_ok and a_ok,
          "%s %s; reduction quote %s; arcs %s %s" % (r["id"], status(r["id"]), "found" if q_ok else "MISSING",
                                                    r["arcs"], "cited" if a_ok else "NOT ALL CITED"))
    find(r["id"])
    if r["reduces_to"]:
        assert status(r["reduces_to"]) == "UNEARNED", r       # edges only into unearned rows (B1266's rule)
        par[find(r["id"])] = find(r["reduces_to"])
groups = {}
for r in used: groups.setdefault(find(r["id"]), []).append(r["id"])
check("K4", len(groups) == I["expected_sources"],
      "union-find: %d rows -> %d sources (entry expects %d): %s" % (len(used), len(groups), I["expected_sources"],
      "; ".join("[%s] %s" % (k, ", ".join(v)) for k, v in sorted(groups.items()))))
unearned = sorted((i for i in ID_ROWS if status(i) == "UNEARNED"), key=lambda s: int(s[2:]))
listed = {r["id"] for r in used} | {r["id"] for r in I["not_used"]} | set(I["not_entered"]["rows"])
check("K4", set(unearned) == listed and len(listed) == len(used) + len(I["not_used"]) + len(I["not_entered"]["rows"]),
      "the ledger's %d UNEARNED rows = %d used + %d not used + %d not entered" % (
          len(unearned), len(used), len(I["not_used"]), len(I["not_entered"]["rows"])))
check("K4", "not adopted" in ID_ROWS["I-35"] and "B1790" in ID_ROWS["I-35"], "I-35: not adopted (B1790)")

# ---------------------------------------------------------------- K5: the bits
on_data = by_hand = total = 0.0
lines_out = []
for d in E["discrete"]:
    o, s = COUNT[d["id"]]
    bm = math.log2(o) if isinstance(o, int) else None
    bs = math.log2(s) if s else None
    if "on the data" in d["label"]:
        on_data += bs
        if bm is not None: by_hand += bm - bs                    # zero for every item here
    else:
        by_hand += bm if bm is not None else math.log2(7)          # the weight: log2 of the seven B1691 computed
    total += bs if "on the data" in d["label"] and bm is None else (bm if bm is not None else math.log2(7))
    lines_out.append("    %-15s %-48s %-60s options %-5s bits %-5s searched %-4s bits %-5s" % (
        d["id"], d["value"][:48], d["label"][:60], o, "%.2f" % bm if bm is not None else "open",
        s if s else "-", "%.2f" % bs if bs is not None else "-"))
check("K5", abs(on_data + by_hand - total) < 1e-12 and all(("on the data" in d["label"]) == (d["searched"] is not None)
      for d in E["discrete"]), "bits: %.2f on the data + %.2f by hand = %.2f; every item chosen on the data has a "
      "search count and no item chosen by hand has one" % (on_data, by_hand, total))

# ---------------------------------------------------------------- the vector
print()
print("THE VECTOR — FR-FIB on the six (%s), at main %s" % ("the H-cov, shared-dR branch, B1753's census", REV))
fc, cc = E["fitted_continuous"], E["chosen_continuous"]
print("  fitted continuous (%d): %s" % (len(fc), ", ".join("%s = %s" % (p["name"], p["value"].split(" (")[0]) for p in fc)))
print("  continuous, set by hand (%d): %s" % (len(cc), ", ".join("%s = %s" % (p["name"], p["value"]) for p in cc)))
print("  discrete (%d; %d chosen on the data, %d by hand):" % (len(E["discrete"]),
      sum("on the data" in d["label"] for d in E["discrete"]), sum("by hand" in d["label"] for d in E["discrete"])))
print("\n".join(lines_out))
print("  bits (a heuristic, not a bound): %.2f searched on the data, %.2f set by hand (the weight at log2 of the "
      "seven B1691 computed)" % (on_data, by_hand))
print("  identifications: %d rows -> %d irreducible sources: %s; not used: %s; not entered: %d" % (
    len(used), len(groups), "; ".join("[%s] %s" % (k, ", ".join(v)) for k, v in sorted(groups.items())),
    ", ".join(r["id"] for r in I["not_used"]), len(I["not_entered"]["rows"])))
print("  tagged hypotheses (listed, not counted; B1809 sec. 1): %s" % ", ".join(h["id"] for h in E["hypotheses"]))
print("  unpriced looks: %d (%s)" % (len(E["unpriced_looks"]), E["unpriced_looks"][0]["what"]))
tally = {}
for p in fc + cc + E["discrete"]: tally.setdefault(p["since_B1750"].split(" (")[0], []).append(p["id"])
print("  since B1750's typed table (2026-10-24; typed in the entry): %s; removed %d" % (
    "; ".join("%s %d (%s)" % (k, len(v), ", ".join(v)) for k, v in sorted(tally.items())), len(tally.get("removed", []))))
print("  bought: %s" % E["reach"]["bought"])
print()
print("RESULT: %s" % ("ALL CHECKS PASS" if not FAILS else "%d FAIL: %s" % (len(FAILS), FAILS)))
sys.exit(1 if FAILS else 0)
