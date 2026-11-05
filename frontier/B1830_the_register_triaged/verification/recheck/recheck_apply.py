"""S297: the owner's 'make sure you did them all right and didn't miss anything load bearing' -- main's recheck of the S296
triage, applied. Each replacement asserted to occur exactly once. Data-free bookkeeping."""
import json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
REG = ROOT / "docs/POINT_REGISTER.md"
D = "2026-11-03"
LAW = json.loads((pathlib.Path(__file__).with_name("law_outcome.json")).read_text(encoding="utf-8"))  # written after main's verification
P355 = (pathlib.Path(__file__).with_name("p355_item1.txt")).read_text(encoding="utf-8").strip()

text = REG.read_text(encoding="utf-8")


def row_edit(pid, fn):
    global text
    ls = text.split("\n")
    k = [i for i, l in enumerate(ls) if l.startswith("| %s |" % pid)]
    assert len(k) == 1, pid
    c = [x.strip() for x in ls[k[0]].strip().strip("|").split(" | ")]
    assert len(c) == 7, pid
    fn(c)
    assert all("|" not in x for x in c), pid
    ls[k[0]] = "| " + " | ".join(c) + " |"
    text = "\n".join(ls)


# P-154: a guard of foundation documents with a known blind spot is a debt by the typing's own definition
def p154(c):
    assert c[5].startswith("[PROCESS] "), c[5][:40]
    c[5] = "[DEBT] " + c[5][len("[PROCESS] "):] + (
        " (S297, the triage's recheck: retyped PROCESS -> DEBT -- a check meant to guard the living documents, owed a fix; "
        "partly paid by hand the same day: the eleven statements of the 2026-10-07 and 2026-10-08 tables swept in the 803 "
        "living .md files -- no uncorrected instance; GENESIS.md lines 117, 445, 762 and THE_WEAVE.md line 159 carry their "
        "corrections, the rest are logs and generated views; owed: their swept-shape rows, so the gate sees them)")
    c[6] = D
row_edit("P-154", p154)


def p386(c):
    c[5] = c[5].replace("-- triage S296;", "-- triage S296 (S297 precision: the closure is of the ask -- the non-authoring "
                        "review, the acceptance and the run; the lane's six analytical successors were not banked on main and "
                        "transfer nothing, their question stays with P-210);", 1)
row_edit("P-386", p386)


def p421(c):
    assert c[5].startswith("[LEAD] "), c[5][:30]
    c[5] = "[DEBT] " + c[5][len("[LEAD] "):] + (
        " (S297, the triage's recheck: retyped LEAD -> DEBT -- B1829's candidate THE SIX ON THE STRIP is graded through this "
        "end, the small-cut norm at L_max's height whose geometric ground S238 removed; with the exact norms the six fail "
        "(25.87 against 16.75); owed to the candidate's grading: the end formula counted as an input (P-418) and the "
        "specificity re-read with L free at its look-elsewhere cost, beside P-586's matched null)")
    c[6] = D
row_edit("P-421", p421)


def p585(c):
    c[5] += (" **S297 (seen first, missed at S294 and S295):** the family's looks run through B1726's compute(), so the "
             "candidate is FR-FIB's with the small-cut end at L_max's height (no geometric ground since S238; at the exact "
             "norms the six fail, THE EXACT END's look, 25.87 against 16.75): the card freezes that end formula as a counted "
             "input (P-421, P-418)")
    c[6] = D
row_edit("P-585", p585)


def p355(c):
    c[5] += " **S297, owed item 1 paid (data-free; frontier/B1830_the_register_triaged/verification/recheck/p355/):** " + P355
    c[6] = D
row_edit("P-355", p355)

# new rows
NEW = []
NEW.append(("P-588", "MA", "LAW_MAP's B1739 ROW STATED A WITHDRAWN LAW (found by main's recheck of the S296 triage, at the "
            "owner's 'make sure … didn't miss anything load bearing'): its headline read '∣V_ud∣ ∝ r^½' with status PROVED, "
            "while B1739's FINDINGS (its dated note, lines 99-101) says the power law holds for the median only (quantile "
            "slopes 1.24, 1.14, 0.52, 0.22) and is unearned as a law; the S250 currency read (RETRACTED_PHRASES.md) listed "
            "B1739 among the window's corrections and wrote 'No living surface repeats them' -- LAW_MAP did; no register row "
            "carried it (P-345's bracket held the correction, typed LEAD for its own question)",
            "DONE", "docs/LAW_MAP.md (the row's headline 'THE MEDIAN ∣V_ud∣ FOLLOWS r^½', its status PROVED for h·h = η⁶/4 and "
            "the alignment, the slope a description, the old headline kept in a dated bracket); the class is P-589"))
NEW.append(("P-589", "MA", "THE CLASS: A CORRECTION THAT REACHED ITS ARC BUT NOT THE SYNTHESIS SURFACES (P-588's class; the "
            "triage read the register only, so it cannot see a correction that never got a row): main's screen of LAW_MAP "
            "(audit/drafts/register_triage/recheck/: stale_laws_title.py, then dated_notes_screen.py) -- of 316 law rows, 46 "
            "whose headline arc carries a retraction, a superseding verdict or a correction word the row does not show, then "
            "26 more whose headline arc carries a dated note (Sharpened, Scoped, Corrected) the row does not show; two readers "
            "judged them, main verified every row called stale or unsure at its source before any edit (B1216's rule: fan-out "
            "reports, main edits); 20 rows were stale, among them the strip candidate's own rows (THE EXACT END never carried "
            "to B1726, B1734, B1735, B1741) and a plain error ([1/4,∞) for a 3-manifold's continuous spectrum)",
            LAW["disposition"], LAW["where"]))
NEW.append(("P-590", "MA", "THE NEGATIVES' SCALE SCOPE (R1 and FL-13 applied backwards; the recheck): every sealed look "
            "compares tree-level outputs at M_Z (LOOK_LEDGER: 'at M_Z unless marked'); a frame whose values hold at another "
            "scale moves the target by a fixed vector δ (R1: ∣δ∣² = 11.8 for the ten at 2 × 10¹⁶ GeV, about 5.9 for the six), "
            "so by the triangle inequality a value NEGATIVE is scale-robust when (√χ²_best − ∣δ∣)² still exceeds its bar. "
            "Robust even at the ten's full ∣δ∣ = 3.44: B1825 (291 → at least 185 against 23.21), B1712's H3 (108.5 → 48.7 against 16.75), B1720's T3 (79.4 → 29.9 against 16.75), B1695's G1 (61.3 → 19.3 against 14.86); the "
            "order-5 lines whatever the scale, since D = (m_μ/m_e)(m_d/m_s) does not run at one loop (same-sector ratios; "
            "R1's s/b and d/b both +13.1%) and is 9 there against 10.58 ± 0.11 (P-355). NOT covered: B1660 (best 34.40 "
            "against 11.07 over five ratios -- the bound gives about 11.8, too close to call); every specificity negative "
            "(the bound says nothing of a null's rate), the nearest B1748 (1.54% against 1%, on the heavy ratios, which run "
            "strongly), B1720's T2 (1.65%) and B1698 (1.675%; its conclusion is carried by D anyway)", "QUEUED",
            "[DEBT] Q2: B1660, B1748 and B1720's T2 re-graded at a declared scale as sealed read-outs, or scoped 'at M_Z, tree level' "
            "where they close a route (the kill graph, LAW_MAP); no data compared outside a seal"))
anchor = text.split("\n")
last = max(i for i, l in enumerate(anchor) if re.match(r"^\| P-\d{3} \|", l))
assert anchor[last].startswith("| P-587 |"), anchor[last][:20]
for pid, origin, body, disp, where in NEW:
    if disp is None: continue
    assert "|" not in body + where, pid
    anchor.insert(last + 1, "| %s | %s | %s | %s | %s | %s | %s |" % (pid, D, origin, body, disp, where, D)); last += 1
text = "\n".join(anchor)

# the ranked list: tier 3 gains P-590 and P-154 after P-317 (by load: a seal's scope under banked negatives, then the guard),
# tier 2 gains P-589 if it stays open
ls = text.split("\n")
h = ls.index("## The debts, by load (worked in this order)")
e = next(i for i in range(h + 1, len(ls)) if ls[i].startswith("## "))
items = [(i, re.match(r"^(\d+)\. (P-\d{3}) — (.*)$", ls[i])) for i in range(h, e)]
items = [(i, m) for i, m in items if m]
order = [m.group(2) for _, m in items]
desc = {m.group(2): m.group(3) for _, m in items}
desc["P-590"] = "Sealed negatives graded at M_Z with tree outputs; B1660, B1748 and B1720's T2 are not covered by the scale bound."
desc["P-154"] = "The retraction sweep never reads RETRACTED_PHRASES' 2026-10-07 and 2026-10-08 tables (hand-swept clean at S297)."
k = order.index("P-317") + 1
order[k:k] = ["P-590", "P-154"]
desc["P-421"] = "The strip candidate's end is the small-cut norm at L_max's height, without geometric ground since S238; with the exact norms the six fail."
order.insert(order.index("P-586") + 1, "P-421")
if LAW["disposition"] == "QUEUED":
    desc["P-589"] = LAW["rank_desc"]
    order.insert(order.index("P-318"), "P-589")
assert len(order) == len(set(order))
lines_by_item = {m.group(2): i for i, m in items}
out, n = [], 0
for i in range(h, e):
    m = re.match(r"^(\d+)\. (P-\d{3}) — ", ls[i])
    if not m:
        out.append(ls[i]); continue
    pid = m.group(2)
    # emit any inserted ids that precede this one in the new order
    while order[n] != pid:
        out.append("%d. %s — %s" % (n + 1, order[n], desc[order[n]])); n += 1
    out.append("%d. %s — %s" % (n + 1, pid, desc[pid])); n += 1
while n < len(order):
    out.append("%d. %s — %s" % (n + 1, order[n], desc[order[n]])); n += 1
ls[h:e] = out
text = "\n".join(ls)
REG.write_text(text, encoding="utf-8")
print("register: P-154 retyped, P-386/P-421/P-355 noted, new rows", [x[0] for x in NEW if x[3]], "; ranked", len(order))
