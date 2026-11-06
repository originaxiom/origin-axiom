"""R76-1, the register half (P-617): Review 74's reader's proposals for the register's [LEAD] rows, each confirmed or not
by main at its pointer (S306i, 2026-11-06). Applied once; every edit asserts the row's state first. A closed row keeps
its old where-cell in full inside [was: ...] (a retyped row's old tag written '(typed LEAD)', since rule 6 counts tags).
Run from the repository root: python3 frontier/B1849_the_leads_confirmed_one_by_one/verification/apply_r76_1.py"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
REG = ROOT / "docs" / "POINT_REGISTER.md"
TODAY, S = "2026-11-06", "S306i"
TAG = "R76-1, %s; main's check at the pointer" % S

ANSWERED = {
    "P-044": "the orphan is reconnected: B1795 FINDINGS cites B1484's ½ for complete multiplets, with B1801–B1803; the gauge question lives on P-396",
    "P-062": "each is engaged on main: W49 by B1642 (the multiplicity space), W25 by B1607 (read before its seal), W36 by B1616, W48 by B1652 (D2's c = 24 source); re-running a seat's computation is the seat-positive-verified gate's job, not this row's",
    "P-064": "B1641 FINDINGS: the Banking Seat's Gate 11 obstruction (Δ⁴ = −I₃) is the commutator loop's sign",
    "P-070": "argued: B1677 and B1682 FINDINGS — read as a finite orbit, every finite-image character persists and nothing is selected, so the common point is a jointly fixed character; GENESIS GM1 POSTULATED in that form at v1.50",
    "P-258": "J is a sealed cell: B1726's R6 (∣J∣, its PREREGISTRATION) and B1825's ten targets (the six, ∣V_us∣, ∣V_cb∣, ∣V_ub∣ and ∣J∣)",
    "P-269": "W122 verified on main (B1719); W123's verification half paid (B1796 FINDINGS); W124 read (HARVEST_LEDGER row 1302)",
    "P-371": "answered by the record: W150 reproduced with corrections (HARVEST row 1371); the web seat's design study (row 1470): μ/M̃ is set by one renormalisation-group invariant, CHOSEN; W158 and W159 NEGATIVE (rows 1409, 1410); what fixes Im τ is P-373's",
    "P-380": "both stages ran: Stage A W154 (HARVEST row 1388), Stage B W155 (row 1390); W154's analytic form is debt P-117; the height question is P-373's",
    "P-393": "the plan's steps 1–4 are worked (docs/MAINS_PLAN.md: B1785, B1788, B1786; B1789; B1790; B1791), their residues carried by P-384, P-294, P-295 and P-373; step 5 is named in the plan, which stays live",
    "P-412": "with the qualifier: answered by the web seat's sealed frame null (HARVEST row 1469; rule e56a311ce; both cells INTERMEDIATE), read on main, not recomputed; docs/LOOK_LEDGER.md: not a look",
    "P-437": "stages 1 and 2 landed (B1813, B1814); B1814 FINDINGS sends the clock question to the theory side, P-438 and P-439 (P-438 merged into P-439 here)",
    "P-443": "the inventory exists: docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md § 6 (the inherited assumptions) and docs/FRAMING_LEDGER.md (B1827)",
    "P-462": "the first was run: B708 (B707's test #1, sealed 96ebff1d: MEET); B707's own 'none run' is stale (the class of debt P-334)",
    "P-465": "computed: docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md, row E — no hierarchy from the principle followed literally; the residue is P-439",
    "P-468": "form (1) answered in the row itself (no point), form (2) by the web seat's critical line (HARVEST row 1475), form (4) in docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md; form (3) is P-475",
    "P-523": "on the card: B1825 PREREGISTRATION § 4, the vacuity calibration measured, NOT VOID",
    "P-538": "on the card: B1825 PREREGISTRATION § 3, the line's price (main's ruling: the 266 lines priced uniformly, 8.06 bits)",
    "P-543": "on the card: B1825 PREREGISTRATION, the census's structure count — R and t = −5/288 structurally dead for our world",
    "P-554": "on the card: B1825 PREREGISTRATION states it, and its FINDINGS read K with it",
    # superseded
    "P-046": "superseded by B1800: the couplings computed as bulk overlaps of the fibre's zero modes (symmetric, ∝ θ_r^(−1/2)) against B1642's boundary residue coupling (θ_r², antisymmetric; B1800 FINDINGS § 2) — B1089's interface reading set against L251 in substance, though B1089 is not cited by name",
    "P-267": "superseded: the reading's test ran — B1732 NEGATIVE as sealed (P-307 DONE); PF1-W's scope ruled by the owner on 2026-11-04 (P-303)",
    "P-329": "superseded: a comparison at the unification scale is scale-dependent, so it is made only inside a sealed card (P-715's guard) — the scale card's design is P-722, the bar's scale clause P-574",
    "P-402": "superseded: the horocycle is priced by the end cards — B1839 NEGATIVE (the free level) and B1841 PROVED as sealed, a reading (P-421 DONE); the web seat's sealed horocycle test (HARVEST row 1444)",
    "P-474": "superseded: the web seat's Door D design study, NOT FOUND as scoped (HARVEST row 1513); the several-address frame is P-555's hatch",
    "P-494": "disclosed: B1825's dated note of 2026-11-06 records this sighting with the dropped CM arm (P-527)",
    "P-526": "lapsed at the seal: B1825 ran with its own hostile referee (FINDINGS § 2: an independent brute-force scan of all 50 612 352 stored rows); HARVEST row 1515",
    "P-039": "the escalation's data-free check run: a 3-cycle-covariant symmetric coupling in its charge basis is nonzero only where k + l ≡ 0 mod 3, which is B345's anti-diagonal texture (frontier/B1849_the_leads_confirmed_one_by_one/verification/p039_cyclic_texture_run.txt) — the texture is the order-3 cyclic structure (B1736's family group) seen in its eigenbasis, generic to every ℤ/3-covariant coupling; nothing further to follow",
    "P-476": "checked on main: vol(LᵃR) rises to the Whitehead link's 3.66386 from below, the gap about 18/a² at a = 55 (frontier/B1849_the_leads_confirmed_one_by_one/verification/p476_whitehead_volumes_run.txt), so e^(−Vol/π) does not decay along the family and μ_A's weight on short threads is set by B1720's length cutoff, not by the weight; the scope sentences added as dated notes to B1722, LAW_MAP's B1722 row and docs/THE_WEAVE.md",
    "P-527": "re-disposed with the reason: B1825 ran without a CM read-out; the drop and P-494's sighting are disclosed in B1825's dated note of 2026-11-06; P-425 and P-449 merged into P-419 (no card carried CM), P-494 DONE",
}
MERGED = {   # row -> (host, reason)
    "P-023": ("P-257", "C5; its own escalation tied it there (no hierarchy at ω or i, B1691)"),
    "P-184": ("P-210", "answered in substance by the record, the row's own note (B1641); the ±1 or ±3 question at the symmetric state is P-210's"),
    "P-345": ("P-566", "route (a) B1740, route (b) B1742; the live form is the sector-odd singlet, under P-555"),
    "P-357": ("P-566", "B1744's det Y factor makes the sector-odd singlet the Higgs invariant this row asks for; W158 and W159 NEGATIVE (HARVEST rows 1409, 1410)"),
    "P-366": ("P-566", "the principled second object or non-holomorphic section is the sector-odd singlet's question"),
    "P-377": ("P-566", "the mixing at the strip; B1825 NEGATIVE as sealed puts the masses and the mixing at different addresses (P-555)"),
    "P-558": ("P-566", "FR-COV's pass is a post-hoc fit (B1826 § 2); its sector scalar a₀ is the sector-odd singlet's candidate (B1827)"),
    "P-394": ("P-295", "the same question, the reading rule (B1790: not derived in B1656's frame)"),
    "P-397": ("P-294", "the lepton factor's route left (B1789)"),
    "P-567": ("P-294", "its open step is the lepton/down factor on the centre lines (2/5 + j/3, k/30) at c = 1, the lepton factor's question; Review 74's reader proposed P-593 item 2, which does not carry it"),
    "P-403": ("P-294", "L250's design as a route to the lepton factor (B1800 did the geometry-first step)"),
    "P-460": ("P-294", "a route: the doublet legs on a spin structure"),
    "P-453": ("P-294", "a route: flux as the puncture degree"),
    "P-315": ("P-355", "the lepton–down split on the order-10 lines is the identity debt P-355 tests"),
    "P-343": ("P-373", "what places τ is what fixes Im τ (its own escalation's merge; P-327 stays open on its own row)"),
    "P-398": ("P-373", "a frame-internal height (B1791: the ρ′ Higgs's Petersson peak 2.8406, outside the strip)"),
    "P-457": ("P-373", "the conventions that set the height, tabulated data-free"),
    "P-455": ("P-022", "the period average removes the point instead of selecting it"),
    "P-413": ("P-439", "the forced weight is B1813's counting parameter s, a clock question"),
    "P-438": ("P-439", "followed or counted"),
    "P-440": ("P-439", "the pure move clock"),
    "P-477": ("P-439", "thermal clocks; its condition carries over: verified at source (Connes–Rovelli) before any use"),
    "P-478": ("P-439", "the literature transfers; its condition carries over: read at source before any is cited"),
    "P-479": ("P-439", "the likelihood design for a two-clock test"),
    "P-422": ("P-411", "gauging the fibre's involution is a class-selecting condition"),
    "P-454": ("P-411", "the Weil filter as a class selection"),
    "P-456": ("P-411", "a least-description line rule"),
    "P-416": ("P-415", "local G₂ models, a tower"),
    "P-424": ("P-415", "whether the two W's meet on the object"),
    "P-463": ("P-415", "the two E₈'s"),
    "P-425": ("P-419", "CM by the object's compositum, selection by inversion; no card carried a CM read-out (P-527 re-disposed)"),
    "P-449": ("P-419", "the CM points' value table, data-free first (P-527 re-disposed)"),
    "P-450": ("P-419", "the Hirzebruch–Zagier reading of the three-generation curve, to be verified at source"),
    "P-569": ("P-323", "θ̄ as a constraint (θ̄ is on V's held-out list: no value computed here)"),
    "P-404": ("P-337", "the Weinberg pair's CP-line zeros, under the zero law"),
    "P-330": ("P-289", "C10 on m004, under C10's limit"),
    "P-034": ("P-033", "L252"), "P-040": ("P-033", "L252"), "P-041": ("P-033", "L252"),
    "P-331": ("P-033", "the θ-odd 2I on one order-5 line, L161 Phase 1b, kept by name"),
    "P-038": ("P-036", "L253"),
    "P-059": ("P-058", "the silver-cover dossier"), "P-060": ("P-058", "the silver-cover dossier"),
    "P-570": ("P-574", "one bar amendment: the running and the allowance"),
    "P-575": ("P-574", "one bar amendment: a declared theory error"),
    "P-576": ("P-574", "one bar amendment: the frame's own length"),
    "P-582": ("P-574", "one bar amendment: existence before sealed looks (under D11 for held-out targets)"),
}
PARTS = {   # rows closed in parts, some merged
    "P-069": "superseded in parts: (a) the valley, B1723 NEGATIVE as sealed; (b) merged into P-287 (C6, a content holding τ in the band); (c) merged into P-022 (averaging τ)",
}
KEPT = {   # proposals main did not confirm: the row stays open with the reason
    "P-327": "Review 74's reader proposed closing this; main did not confirm: the escalation's condition (B1704's potential re-run on main on the ten α = 2/5 lines) is unmet — B1704 searched only Re τ = 0 and ½; the web seat's e17/e18 (row 1401) stay an input",
    "P-562": "the proposed closure not confirmed: the row's own S301 note keeps the twisted Serre computation open",
    "P-177": "items 1, 3 and 4 answered (its escalation); item 2 folded into P-277 (DONE); the row now carries item 5 only — seal the enlarged-thread-set census or decline it",
    "P-328": "not closed: the J rule's derivation from B1821's mirror map is Review 74's reader's, unverified on main; the input-ledger half is carried by docs/MAINS_PLAN.md and docs/TOTAL_INPUTS_SCOREBOARD.md",
    "P-073": "the reader's merge into P-139 not applied: B1833 joined this row under P-629",
    "P-218": "the merge into P-210 proposed again; main's S296 decline stands",
    "P-485": "the merge into P-487 proposed again; main's S296 decline stands",
    "P-461": "the reader's merge of (b) into P-323 not applied: the FPST half is answered in this row's own note; the DH valley half stays a lead here",
    "P-280": "the reader's merge into debt P-321 not applied: P-321 (GM4 derived) does not carry the p = 2 against p = 3 question",
    "P-537": "the reader's candidate merge into debt P-025 not applied: P-025 asks about imported holomorphy and minimal Kähler, not a forced normalisation",
    "P-137": "the reader's candidate merge into debt P-492 not applied: P-492 asks about L154's AdS₃ boundary assumption, this row about the weave's quantised sector",
}
RETYPE = {
    "P-063": "[PROCESS] Q9 (R76-1, %s): the inequality checked by hand for every real p — 96p(1 − p) ≤ 24 < 25, so C₂ ≤ −1/432 < 0; the formula's derivation is the Banking Seat's, to be re-derived on main before any use" % S,
    "P-574": "[PROCESS] Q1 (R76-1, %s): the host of one bar amendment — every future card declares its scale (or a menu priced in bits), runs its outputs at one loop at least, names and pays its theory error (P-575), charges its searched design bits (P-576) and gates any sealed value look on an unsealed existence scan (P-582, under D11 for held-out targets); P-570's running and allowance are this clause; data-free" % S,
}


def rows(text):
    out = {}
    for i, line in enumerate(text.split("\n")):
        m = re.match(r"\| (P-\d{3}) \| ", line)
        if m:
            c = line.split(" | ")
            assert len(c) == 7 and c[6].endswith(" |"), (m.group(1), len(c))
            out[m.group(1)] = (i, c)
    return out


def main():
    text = REG.read_text(encoding="utf-8")
    lines = text.split("\n")
    R = rows(text)
    hosts = {}
    for pid, (host, why) in MERGED.items():
        hosts.setdefault(host, []).append(pid)
    for pid in ("P-069",):
        hosts.setdefault("P-287", []).append(pid + " (b)"); hosts.setdefault("P-022", []).append(pid + " (c)")
    touched = set(ANSWERED) | set(MERGED) | set(PARTS) | set(KEPT) | set(RETYPE)
    assert not (touched & set(hosts)) or (touched & set(hosts)) == {"P-574"}, touched & set(hosts)

    def put(pid, disp, where):
        i, c = R[pid]
        c = list(c); c[4] = disp; c[5] = where; c[6] = TODAY + " |"
        lines[i] = " | ".join(c)

    def was(where):
        return " [was: %s]" % re.sub(r"\[(DEBT|LEAD|PROCESS)\]", r"(typed \1)", where)

    for pid, note in ANSWERED.items():
        i, c = R[pid]; assert c[4] in ("QUEUED", "LEAD"), (pid, c[4])
        put(pid, "DONE", "%s: %s%s" % (TAG, note, was(c[5])))
    for pid, (host, why) in MERGED.items():
        i, c = R[pid]; assert c[4] in ("QUEUED", "LEAD"), (pid, c[4])
        assert R[host][1][4] in ("QUEUED", "LEAD"), (host, R[host][1][4])
        put(pid, "DONE", "merged into %s (%s): %s%s" % (host, TAG, why, was(c[5])))
    for pid, note in PARTS.items():
        i, c = R[pid]; assert c[4] in ("QUEUED", "LEAD")
        put(pid, "DONE", "%s (%s)%s" % (note, TAG, was(c[5])))
    for pid, note in KEPT.items():
        i, c = R[pid]; assert c[4] in ("QUEUED", "LEAD"), (pid, c[4])
        put(pid, c[4], "%s [%s, R76-1: %s]" % (c[5], S, note))
    for pid, where in RETYPE.items():
        i, c = R[pid]; assert c[4] == "QUEUED"
        put(pid, "QUEUED", where + was(c[5]))
    for host, kids in sorted(hosts.items()):
        if host == "P-574":
            continue      # its retyped where names its four
        i, c = R[host]; assert c[4] in ("QUEUED", "LEAD"), (host, c[4])
        put(host, c[4], "%s [%s, R76-1: carries %s (closed as merged; see each row)]" % (lines[i].split(" | ")[5], S, ", ".join(kids)))
    # P-617: the register half done
    i, c = R["P-617"]
    n_ans = len(ANSWERED); n_mer = len(MERGED); n_kept = len(KEPT)
    put("P-617", "QUEUED", c[5] + (" [%s, R76-1 — THE REGISTER HALF CONFIRMED ONE BY ONE (B1849): every proposal for the register's"
         " lead-typed rows checked by main at its pointer — %d rows closed as answered, superseded or paid (P-039 and P-476 after"
         " main's own checks, debt P-527 paid by B1825's disclosure), %d merged into %d hosts (each host notes what it carries),"
         " P-069 closed in parts, P-063 and P-574 retyped as process rows, %d kept open with dated reasons (P-073, P-137, P-177, P-218,"
         " P-280, P-327, P-328, P-461, P-485, P-537, P-562); P-020 and P-418 were already DONE; the OPEN_LEADS half"
         " (77 leads) stays open]") % (S, n_ans, n_mer, len(hosts) - 1, n_kept))
    text = "\n".join(lines)
    # the ranked debts list names only open debts: P-527 leaves it, the rest renumbered
    head = text.index("## The debts, by load"); end = text.index("## The queue", head)
    block = text[head:end]
    assert block.count("\n70. P-527 — ") == 1
    out, n = [], 0
    for ln in block.split("\n"):
        m = re.match(r"(\d+)\. (P-\d{3}) — ", ln)
        if m:
            if m.group(2) == "P-527":
                continue
            n += 1; ln = "%d. %s" % (n, ln[len(m.group(1)) + 2:])
        out.append(ln)
    text = text[:head] + "\n".join(out) + text[end:]
    REG.write_text(text, encoding="utf-8")
    print("closed %d (answered, superseded, paid), merged %d into %d hosts, P-069 in parts, kept %d, retyped %d; debts list %d"
          % (n_ans, n_mer, len(hosts) - 1, n_kept, len(RETYPE), n))


if __name__ == "__main__":
    main()
