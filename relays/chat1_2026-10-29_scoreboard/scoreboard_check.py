"""P-418's graded vector for FR-FIB: print it from FR_FIB_ENTRY.json and recompute every count from main's committed
files at the entry's pinned revision (read with git show; nothing on main is written).  Data-free: no measured number
is read.  The web seat, 2026-10-29.  0 of 19.

Checks:
  K1  every arc (B####), register row (P-###) and identification row (I-##) the entry cites exists at the revision;
  K2  the menus, counted from main's code and data: the readings (B1741's SEAT and COV), the lines (B1726's lines(),
      executed alone), the apexes and their band (B1753's census), the horocycles (the census's keys), c's scan
      (B1798 sec. 4's set), the weights B1691 computed (its stated range);
  K3  the quoted sentences each item rests on occur in their sources;
  K4  the identification rows: each is UNEARNED at the revision, each quoted reduction occurs in its row, and a
      union-find over the rows used gives the irreducible sources;
  K5  the bits, computed here from the counts (log2 of the options or of the options searched), never typed.
"""
import ast, json, math, pathlib, re, subprocess, sys
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
REG_IDS = set(re.findall(r"^\| (P-\d+) \|", REG, flags=re.M))
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
for r in E["identifications"]["rows"] + E["identifications"]["not_used"]: cited.add(r["id"])
missing = []
for c in sorted(cited):
    if re.fullmatch(r"B\d+", c): ok = c in ARCS
    elif re.fullmatch(r"P-\d+", c): ok = c in REG_IDS
    elif re.fullmatch(r"I-\d+", c): ok = c in ID_ROWS
    elif c == "GENESIS": ok = bool(show("GENESIS.md"))
    else: ok = False
    if not ok: missing.append(c)
check("K1", not missing, "%d citations, missing: %s" % (len(cited), missing or "none"))

# ---------------------------------------------------------------- K2: the menus, counted
cmp41 = arc("B1741", "verification/compare.py")
seat = ast.literal_eval(re.search(r"^SEAT = (\(.*?\))\s*#", cmp41, flags=re.M).group(1))
cov = eval(re.search(r"^COV = (tuple\(.*\))\s*$", cmp41, flags=re.M).group(1), {"tuple": tuple, "range": range})
check("K2", len(seat) == 2 and len(cov) == 8 and len(set(cov)) == 8, "readings: SEAT %s (%d), COV %d" % (seat, len(seat), len(cov)))
cen = arc("B1726", "verification/census.py")
fn = next(n for n in ast.parse(cen).body if isinstance(n, ast.FunctionDef) and n.name == "lines")
ns = {"math": math, "Fr": Fr}
exec(compile(ast.Module(body=[fn], type_ignores=[]), "lines", "exec"), ns)
L = ns["lines"]()
check("K2", len(L) == 266 and (Fr(2, 5), Fr(1, 10)) in L, "lines: B1726's lines() gives %d; (2/5, 1/10) among them" % len(L))
rows = [json.loads(l) for l in arc("B1753", "verification/census.jsonl").splitlines() if l.strip()]
ap = sorted({(r["Re_tau"], r["Im_tau"]) for r in rows})
ims = [a[1] for a in ap]
hors = sorted({k.split("|")[1] for r in rows for k in r if k.count("|") >= 2})
check("K2", len(ap) == 223 and 2.0 <= min(ims) and max(ims) <= 3.6,
      "apexes: %d distinct in B1753's census, Im tau %.4f-%.4f; band [2.0, 3.6]" % (len(ap), min(ims), max(ims)))
check("K2", hors == ["L_2", "L_max"], "horocycles in the census keys: %s" % hors)
f98 = arc("B1798")
cs = next(s for s in re.findall(r"c ∈ \{([^}]*)\}", f98) if s.startswith("1/3, 1/2, 2/3"))
cvals = [Fr(x.strip()) for x in cs.split(",")]
check("K2", len(cvals) == 9 and Fr(3) in cvals, "c's scan in B1798 sec. 4: {%s} (%d values)" % (cs, len(cvals)))
f91 = arc("B1691")
wts = [Fr(4 * n - 1, 2) for n in range(0, 7)]          # k = 2n - 1/2 for n = 0..6: -1/2 .. 23/2
check("K2", "seven weights" in f91 and "23/2" in f91 and wts[0] == Fr(-1, 2) and wts[-1] == Fr(23, 2),
      "weights B1691 computed: %s (%d)" % ([str(w) for w in wts], len(wts)))

# ---------------------------------------------------------------- K3: the quoted sentences
Q = [
    ("B1753", None, "2.74 at 0.3333 + 3.0368i on (2/5, 1/10), L_max, (S̃, S, S), c = 3"),
    ("B1798", None, "The Clebsch 3 was chosen knowing the data's R2 = 3.14"),
    ("B1798", None, "the apex band Im τ ∈ [2.0, 3.6]"),
    ("B1726", None, "35–38% below it, and with them the six fail near the four families' rows"),
    ("B1726", None, "The best six-row** (seat's and covariant menus alike)"),
    ("B1750", None, "the Higgs's scalar part h₀ = 0"),
    ("B1750", None, "| the comparison scale (M_Z) | PRECISION_BAR (HZ2021) | **identification**"),
    ("B1750", None, "L_max a rule informed post hoc"),
    ("B1700", None, "ONLY ∂R, THE ONE WITH THE COUPLING TRIPLET'S OWN END CONDITION, GIVES A HIERARCHY"),
    ("B1809", None, "D: the weight class; a shared or per-sector section; h; the line"),
    ("B1809", None, "f(d) ≤ 2 with DR at a fixed line"),
    ("B1809", None, "**P-418:** f(d) per frame as a Jacobian rank"),
    ("P-365", REG, "the comparison at M_Z is a choice"),
    ("P-365", REG, "the Standard Model's H̃ was an identification made by hand (B1660)"),
    ("P-402", REG, "selected by the data, not absorbed by τ"),
    ("P-384", REG, "the line rule is mostly a pick"),
    ("P-421", REG, "or the scale is an input"),
    ("P-377", REG, "one Higgs read everywhere reaches χ²_nine 47 at best"),
    ("MAINS_PLAN", show("docs/MAINS_PLAN.md"), "the slope is selected by the data, stably\n   out of sample, with one number's worth of input (e_up) — not removed"),
    ("MAINS_PLAN", show("docs/MAINS_PLAN.md"), "The eight\n   reading assignments are physically distinct"),
]
for src, text, q in Q:
    t = text if text is not None else arc(src)
    check("K3", q in t, "%s: '%s'" % (src, q.replace("\n", " ")[:90]))

# ---------------------------------------------------------------- K4: the identification rows, union-find
def covers(row, b):
    n = int(b[1:])
    if re.search(r"\b%s\b" % b, row): return True
    return any(int(x) <= n <= int(y) for x, y in re.findall(r"B(\d+)[–-]B(\d+)", row))
par = {}
def find(x):
    par.setdefault(x, x)
    while par[x] != x: x = par[x]
    return x
used = E["identifications"]["rows"]
for r in used:
    row = ID_ROWS[r["id"]]
    status = re.search(r"\*\*(EARNED|REFUTED|UNEARNED)\*\*", row).group(1)
    q_ok = r["quote"] is None or r["quote"] in row
    a_ok = all(covers(row, b) for b in r["arcs"])
    check("K4", status == "UNEARNED" and q_ok and a_ok,
          "%s %s; quote %s; arcs %s %s" % (r["id"], status, "found" if q_ok else "MISSING", r["arcs"], "cited" if a_ok else "NOT ALL CITED"))
    find(r["id"])
    if r["reduces_to"]:
        tgt = r["reduces_to"]
        assert re.search(r"\*\*UNEARNED\*\*", ID_ROWS[tgt]), tgt    # edges only into unearned rows (B1266's rule)
        par[find(r["id"])] = find(tgt)
groups = {}
for r in used: groups.setdefault(find(r["id"]), []).append(r["id"])
nu = E["identifications"]["not_used"][0]
check("K4", "**UNEARNED**" in ID_ROWS[nu["id"]] and "B1790" in ID_ROWS[nu["id"]] and "not adopted" in ID_ROWS[nu["id"]],
      "%s UNEARNED and not adopted (B1790): counted as the reading's choice instead" % nu["id"])

# ---------------------------------------------------------------- K5: the vector
print()
print("THE VECTOR — FR-FIB on the six, at main %s" % REV)
fc, cc = E["fitted_continuous"], E["chosen_continuous"]
print("  fitted continuous (%d): %s" % (len(fc), ", ".join("%s = %s" % (p["name"], p["value"].split(" (")[0]) for p in fc)))
print("  chosen continuous (%d): %s" % (len(cc), ", ".join("%s = %s" % (p["name"], p["value"]) for p in cc)))
print("  discrete (%d):" % len(E["discrete"]))
counted = {"reading": (len(cov), len(seat)), "line": ("open", len(L)), "c": ("open", len(cvals)),
           "horocycle": (2, len(hors)), "weight": ("open", None), "end_scale": (2, None), "shared_section": (2, None)}
fit_bits = hand_bits = 0.0
for d in E["discrete"]:
    o, s = counted[d["id"]]
    assert (o == d["options"]) and (s == d["searched"]), (d["id"], o, d["options"], s, d["searched"])
    bm = math.log2(o) if isinstance(o, int) else None
    bs = math.log2(s) if s else None
    if d["label"].startswith("FITTED"):
        fit_bits += bs
        if bm is not None and bs is not None: hand_bits += bm - bs        # the reading: the menu of two picked by hand
    else:
        hand_bits += bm if bm is not None else math.log2(len(wts))       # the weight: the seven B1691 computed
    print("    %-15s %-48s %-46s options %-5s bits %-5s searched %-4s bits %-5s" % (
        d["id"], d["value"][:48], d["label"][:46], o, "%.2f" % bm if bm is not None else "open",
        s if s else "-", "%.2f" % bs if bs is not None else "-"))
print("  bits (a heuristic, not a bound): %.2f searched on the data (the FITTED items), %.2f set by hand "
      "(the CHOSEN items and the reading's hand-picked menu; the weight at log2 of the seven B1691 computed)" % (fit_bits, hand_bits))
print("  identifications: %d rows used -> %d irreducible sources: %s" % (
    len(used), len(groups), "; ".join("[%s] %s" % (k, ", ".join(v)) for k, v in sorted(groups.items()))))
print("  tagged hypotheses (listed, not counted; B1809 sec. 1): %s" % ", ".join(h["id"] for h in E["hypotheses"]))
print("  unpriced looks: %d (%s)" % (len(E["unpriced_looks"]), E["unpriced_looks"][0]["what"]))
tally = {}
for p in fc + cc + E["discrete"]: tally.setdefault(p["since_B1750"].split(" (")[0], []).append(p["id"])
print("  since B1750's typed table (2026-10-24): %s" % "; ".join("%s %d (%s)" % (k, len(v), ", ".join(v)) for k, v in sorted(tally.items())))
print("  removed since B1750: 0")
print("  bought: %s" % E["reach"]["bought"])
print()
print("RESULT: %s" % ("ALL CHECKS PASS" if not FAILS else "%d FAIL: %s" % (len(FAILS), FAILS)))
sys.exit(1 if FAILS else 0)
