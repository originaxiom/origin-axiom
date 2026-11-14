"""The seven process arcs of 2026-08-27 left at verdict OPEN (register row P-745; main's card C11, 2026-11-13).

Each residue an arc names in its own words was checked against the record as it stood on 2026-11-13, at the file that
decides it today, by a quotation from that file.  The outcome of each: DISCHARGED (the record shows it done), CARRIED (it
lives on, open, in a named row or lead), or UNREGISTERED (no row, lead or later arc decides it: it is re-pointed to P-745,
whose dated addition lists it for main).  An arc whose every residue is discharged is closed; the others stay OPEN with a
dated ESCALATED marker that names what carries each residue.

Held here: the table; each quotation stands in its file; each arc's page carries its section, its outcome and its marker;
B1178 is closed and the six others are not; and the aged-debt check excuses an OPEN arc only by a marker."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

# (residue in the arc's own words, outcome, the deciding file, a quotation from it, what carries it)
TABLE = {
    "B1171": [
        ("the time's-arrow instrument was queued and not run", "DISCHARGED", "frontier/B1182_c4prime_resolved/FINDINGS.md",
         "THE TIME'S-ARROW TYPED (the FIRST EXECUTION of cc3's B8144 escape-instrument, the flagged price-reconciliation residue)", "B1182"),
        ("Krutelevich's finite-orbit citation is carried cited, not re-derived", "CARRIED", "docs/OPEN_LEADS.md",
         "Review 74's reader proposed closing this lead; main's check did not confirm it. P-332 carries the transitivity proof route.", "L162, P-332"),
        ("the relayed ask on the R018 numbering gap", "DISCHARGED", "docs/RELAY_LEDGER.md",
         "its substance is the seat arcs it reports, R018, each with a HARVEST_LEDGER row", "R018 exists and is rowed"),
        ("the relayed ask for a re-runnable zeta-12 / dP6 construction certificate", "UNREGISTERED", "docs/OPEN_LEADS.md",
         "SEAM-A is open in B1156, and B1159 calls it a wall only in substance. The lead stays open.", "P-745 (nearest home: L182, which does not name the certificate)"),
    ],
    "B1172": [
        ("the MC1 assignment row was left OPEN", "CARRIED", "docs/POINT_REGISTER.md",
         "MC1, live (from the declined relay of 2026-08-26, P-231): the only internal-diversity control on the hypercharge-forcing theorems", "P-233"),
        ("the Wave 2 and Wave 3 queues recorded in b1172_results.json", "UNREGISTERED", "frontier/B1174_z2_identification/FINDINGS.md",
         "This was the register's Q1 = B1169's S1, **double-discovered** (the sweep and the meditation found", "P-745 (Wave 3's Q1 is B1174; Q2 to Q11 are disposed of nowhere)"),
        ("the review-carry half was handed to Review 50", "DISCHARGED", "docs/CAMPAIGN_STATUS.md",
         "the review gate now **enforces carry continuity** (a `[>]` that never recurs fails by name)", "Review 50; the gate review-actions"),
    ],
    "B1173": [
        ("the thirteen NOT-REACHED digest rows under the umbrella lead L185", "CARRIED", "docs/OPEN_LEADS.md",
         "Review 74's reader proposed closing this lead; main's check did not confirm it. The disposition table is only in a gitignored audit draft, and the row it promises does not exist.", "L185"),
        ("the two-kappa and shadow-library rows flagged as the likeliest reopens", "CARRIED", "frontier/B1060_digest_ledger/DIGEST_LEDGER.md",
         "| 4.6 | the two-κ finding (qL159) | NOT-REACHED | — | vs main's TERMINOLOGY register · NOT-REACHED at partial-close (B1173) → tracked at L185|", "L185"),
    ],
    "B1176": [
        ("the gap U_e", "CARRIED", "docs/POINT_REGISTER.md", "[S305j: HELD unspent by the owner's ruling (P-709) — as P-585]", "P-638"),
        ("the gap the quasinormal channel", "CARRIED", "docs/POINT_REGISTER.md",
         "item (1) U_e split out as P-638; (2) the quasinormal channel covered by P-287 and B1090/B1704", "P-287, L189 (a reader's routing; L189 stays open)"),
    ],
    "B1177": [
        ("the promotion pass (ex-R48-9) stays a named bounded residue", "UNREGISTERED", "frontier/B1177_instrument_bundle/FINDINGS.md",
         "the promotion pass (ex-R48-9) stays a named bounded residue",
         "P-745 (the review item that held it closed with B1207, which does not name the promotion; CLAIMS.md has no row of B909 or B952)"),
        ("three dangling B792 path repairs were owed", "CARRIED", "docs/POINT_REGISTER.md",
         "the chain rule lapsed since B1454 (B758); B1177's four dangling B792 paths; 39 directories with no findings document", "P-322 (which counts four)"),
        ("the first OA_SLOW run was launched, not complete", "DISCHARGED", "frontier/B1207_slow_lane_discharge/FINDINGS.md",
         "enumerated at B1177 and launched there. Its **first-ever complete run** finished after **4 h 45 min**:", "B1207"),
    ],
    "B1178": [
        ("the first OA_SLOW run was still in flight when the arc closed", "DISCHARGED", "frontier/B1207_slow_lane_discharge/FINDINGS.md",
         "enumerated at B1177 and launched there. Its **first-ever complete run** finished after **4 h 45 min**:", "B1207"),
    ],
    "B1179": [
        ("the specialist send-queue waits on a per-item SEND, HOLD or REFRAME", "DISCHARGED", "docs/THE_REMAINING_MATH.md",
         "specialist-send items **HOLD** (`SPECIALIST_SEND_QUEUE.md` decision box); THE PAPER is crafted", "decided: every item HOLD; the queue stays built and unsent"),
        ("the census calls", "CARRIED", "docs/THE_REMAINING_MATH.md",
         "| 6 | census-31-calls (R45-5, owner:cc) · L145a · F11 · K014 · L189 (U_e/quasinormal) | QUEUED — smaller bounded cells |", "the queue of the remaining mathematics, row 6"),
        ("the cold-pass election", "UNREGISTERED", "frontier/B1179_outreach_and_papers/FINDINGS.md",
         "the cold-pass election and the census calls stay the owner's", "P-745 (no row, lead or arc decides it)"),
    ],
}
CLOSED = {a for a, rows in TABLE.items() if all(r[1] == "DISCHARGED" for r in rows)}
HEADING = "## The residues checked, 2026-11-13 (main's card C11; register row P-745)"


def _arc(a):
    return next((ROOT / "frontier").glob(a + "_*"))


def section(a):
    """the section that stands on the arc's page, made from the table"""
    rows = TABLE[a]
    out = [HEADING, "",
           "Each residue this arc names in its own words, checked against the record as it stood on 2026-11-13, at the file that "
           "decides it today, by a quotation from that file. Where nothing decides it (UNREGISTERED), the file read is the one that "
           "names it. The lock is `tests/test_the_seven_process_arcs_checked.py`.", "",
           "| residue | outcome | the file read | quotation | carried by |", "|---|---|---|---|---|"]
    for res, outcome, f, q, by in rows:
        out.append("| %s | %s | `%s` | %s | %s |" % (res, outcome, f, q.replace("|", "∣"), by))
    out.append("")
    if a in CLOSED:
        out.append("**Every residue is discharged, so the arc is closed:** its verdict is PROVED from 2026-11-13, as a process arc whose "
                   "work is done. It states no theorem.")
    else:
        carriers = sorted({r[4].split(" (")[0] for r in rows if r[1] != "DISCHARGED"})
        out.append("**The arc stays OPEN.** ESCALATED(2026-11-13, P-745; carried by %s). A residue marked UNREGISTERED is decided by no "
                   "row, lead or later arc; it is re-pointed to P-745, whose dated addition of 2026-11-13 lists it for main to row or "
                   "to decline." % "; ".join(carriers))
    return "\n".join(out) + "\n"


def test_each_quotation_stands_in_the_file_that_decides_it():
    for a, rows in TABLE.items():
        for res, outcome, f, q, by in rows:
            assert outcome in ("DISCHARGED", "CARRIED", "UNREGISTERED"), (a, res)
            assert any(q in line for line in (ROOT / f).read_text(encoding="utf-8").split("\n")), (a, res, f)
    # planted: a quotation changed by one word is not found
    a, rows = "B1171", TABLE["B1171"]
    f, q = rows[0][2], rows[0][3].replace("FIRST", "SECOND")
    assert not any(q in line for line in (ROOT / f).read_text(encoding="utf-8").split("\n"))


def test_each_page_carries_its_section_and_the_verdicts_follow_it():
    assert CLOSED == {"B1178"}
    for a in TABLE:
        page = (_arc(a) / "FINDINGS.md").read_text(encoding="utf-8")
        assert page.count(HEADING) == 1 and section(a) in page, a
        v = json.loads((_arc(a) / "arc_verdict.json").read_text(encoding="utf-8"))
        assert v["verdict"] == ("PROVED" if a in CLOSED else "OPEN"), a
        if a not in CLOSED:
            assert "ESCALATED(2026-11-13, P-745" in page, a
    v = json.loads((_arc("B1178") / "arc_verdict.json").read_text(encoding="utf-8"))
    assert "[CLOSED 2026-11-13 (main's card C11; register row P-745):" in v["claim_one_line"]


def test_the_aged_debt_check_excuses_an_open_arc_only_by_a_marker():
    sys.path.insert(0, str(ROOT / "scripts" / "checks"))
    import lead_debt
    for a in TABLE:
        if a in CLOSED:
            continue
        page = (_arc(a) / "FINDINGS.md").read_text(encoding="utf-8")
        assert lead_debt.ESCALATED_RE.search(page)
        # planted: the page with every marker taken out is excused by nothing
        bare = re.sub(r"ESCALATED\(\s*\d{4}-\d{2}-\d{2}", "", page)
        assert not (lead_debt.ESCALATED_RE.search(bare) or lead_debt.BY_DESIGN_RE.search(bare)), a
    # and the arcs the check finds OPEN do not include the closed one
    assert "B1178_l184_lazyfy" not in {d["arc"] for d in lead_debt.open_arcs()}


def test_the_register_row_lists_the_unregistered_residues():
    row = [l for l in (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8").split("\n") if l.startswith("| P-745 |")]
    assert len(row) == 1 and "[2026-11-13, main's card C11:" in row[0]
    for a, rows in TABLE.items():
        for res, outcome, f, q, by in rows:
            if outcome == "UNREGISTERED":
                assert res in row[0], (a, res)
