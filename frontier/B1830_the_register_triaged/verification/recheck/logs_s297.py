"""S297 logs: CHANGELOG, PROGRESS_LOG, CAMPAIGN_STATUS LATEST, B1830's FINDINGS section and MAIN_VERIFICATION addendum,
the claim brackets on B1830 and B1829. Run after recheck_apply.py (p355_item1.txt must exist)."""
import json, pathlib, shutil
ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
P355 = (HERE / "p355_item1.txt").read_text(encoding="utf-8").strip()
P355_SHORT = (HERE / "p355_item1_short.txt").read_text(encoding="utf-8").strip()


def prepend_after(path, anchor, block):
    p = ROOT / path; t = p.read_text(encoding="utf-8")
    assert t.count(anchor) == 1, (path, anchor[:40])
    i = t.index(anchor) + len(anchor)
    p.write_text(t[:i] + block + t[i:], encoding="utf-8")


prepend_after("CHANGELOG.md", "# Changelog\n", """
## S297 THE TRIAGE RECHECKED AT THE OWNER'S WORD: 20 STALE LAW-MAP ROWS, THE CANDIDATE'S END, THE NEGATIVES' SCALE, P-355's FIRST ITEM (2026-11-03)

- **The owner (2026-11-03): "just make sure sure sure sure u did them all right and didnt miss anything load bearing".** Main re-read B1830's triage (its S297 section; verification/recheck/): the 46 lead and process rows with a load signal read in full, the 136 others by their opening lines, the nine closures against each row's own ask — all stand; P-154 (a guard of the living documents with a blind spot, hand-swept clean the same day) and P-421 (the candidate's end) retyped DEBT; P-386's closure narrowed to its ask; the five OWNER rows bear no load (P-303's two readings select the same Higgs).
- **What a register triage cannot see — corrections that never got a row (P-588, P-589):** LAW_MAP screened against later retractions, superseding verdicts and dated notes (72 rows); two readers judged the hits; main verified each at its source before any edit; **20 stale rows sharpened in place** — B1739's '∣V_ud∣ ∝ r^½' stated as a law (the median's slope only), THE EXACT END never carried to B1726, B1734, B1735 and B1741's rows, B1788's hypothesis (b) failing on three slopes, B716's signature (the holonomy's), B726's field, B1750's retired closer, a [1/4,∞) that is [1,∞), status and member-scope lags; one scope note on 'the canonical end' (the small-cut norm, B1667's row); MAINS_PLAN's strip row; dated notes on B1734 and B1735; the S250 currency read's 'No living surface repeats them' corrected in RETRACTED_PHRASES. Owed (P-589, a debt): the eight member-scope addenda the gate's baseline has carried since B1477 with no row, and the same screen over GENESIS and the ledgers.
- **The candidate, corrected (B1829 REGRADE and FINDINGS, LOOK_LEDGER, P-585):** THE SIX ON THE STRIP is a candidate of FR-FIB with the small-cut end, whose geometric ground S238 removed; at the exact norms the six fail (THE EXACT END's look, 25.87 against 16.75). S294 omitted it and S295 missed it. P-421 ranked after P-586.
- **New debt P-590, the negatives' scale scope:** every sealed look compares at M_Z; by the triangle bound with R1's ∣δ∣² = 11.8, B1825, B1712, B1720's T3 and B1695's G1 are scale-robust even at the full ∣δ∣, and the order-5 lines are excluded at any scale through D (it does not run at one loop); B1660 (34.40 against 11.07) and the specificity negatives (B1748 at 1.54%, B1720's T2 at 1.65%) are not covered.
- **P-355's first owed item (data-free):** """ + P355_SHORT + """
- 63 debts (P-154, P-421, P-589, P-590 added), 140 leads, 40 process; FLOOR 590. Nothing compared with data. 0 of 19.
""")

prepend_after("PROGRESS_LOG.md", "## 2026-11-03 — S296 the register triaged\n\n- Every open row typed; only debts age; 59 debts ranked by load, P-355 first (B1830). 0 of 19.\n",
"""
## 2026-11-03 — S297 the triage rechecked

- The owner's 'make sure … didn't miss anything load bearing': typings and closures stand (P-154, P-421 retyped debts);
  20 stale law-map rows corrected in place (P-588, P-589); the strip candidate is the small-cut end's, which fails the six
  at the exact norms (B1829 corrected); P-590 the negatives' scale scope; P-355's first item paid. 0 of 19.
""")

p = ROOT / "docs/CAMPAIGN_STATUS.md"; t = p.read_text(encoding="utf-8")
anchor = "**LATEST (2026-11-03, S296:"
assert t.count(anchor) == 1
t = t.replace(anchor, "**LATEST (2026-11-03, S297: the triage re-checked at the owner's word. Every typing and every closure "
  "stood, except two points marked as ideas or housekeeping that are in fact owed checks; both are debts now. The re-check "
  "also found what a register cannot show: twenty rows of the law map still stated results that later work had corrected. "
  "The most important is that the candidate found at S294 holds only with an approximate formula for the boundary; with the "
  "exact one, the six masses fail. All twenty are corrected in place, the candidate is recorded as weaker, and the habit "
  "that let the corrections stall is written down (P-589). 0 of 19.)**\n\n" + anchor, 1)
p.write_text(t, encoding="utf-8")

# B1830: the recheck section, the audit trail, the claim bracket
arc = ROOT / "frontier/B1830_the_register_triaged"
sec = (HERE / "B1830_recheck_section.md").read_text(encoding="utf-8").replace("⟨P355⟩", P355)
f = arc / "FINDINGS.md"; s = f.read_text(encoding="utf-8")
assert "## The recheck (S297" not in s
f.write_text(s.rstrip("\n") + "\n" + sec, encoding="utf-8")
dst = arc / "verification/recheck"; dst.mkdir(exist_ok=True)
for n in ["screen.py", "flagged.json", "unflagged.txt", "stale_laws.py", "stale_laws_title.py", "law_hits.json",
          "evidence_old_era.txt", "evidence_fibre_era.txt", "dated_notes_screen.py", "dated_notes_hits.txt", "law_apply.py",
          "law_apply2.py", "law_outcome.json", "recheck_apply.py", "logs_s297.py", "p355_item1.txt"]:
    shutil.copy(HERE / n, dst / n)
mv = arc / "verification/MAIN_VERIFICATION.md"
mv.write_text(mv.read_text(encoding="utf-8").rstrip("\n") + "\n\n**S297, the recheck (the owner's 'make sure … didn't miss "
  "anything load bearing'):** the typing re-read (`recheck/screen.py`; 46 flagged rows read in full) — P-154 and P-421 "
  "retyped DEBT; the nine closures re-read against their asks — all stand, P-386 narrowed to its ask; the readers' law-row "
  "verdicts (`recheck/evidence_*.txt`, `recheck/dated_notes_hits.txt`) each verified by main at the source before the edits "
  "(`recheck/law_apply.py`, `law_apply2.py`; rows 334 and 258 by hand). See FINDINGS, The recheck.\n", encoding="utf-8")
for a, br in (("frontier/B1830_the_register_triaged", " [S297, rechecked at the owner's word: P-154 and P-421 retyped DEBT; "
               "20 stale LAW_MAP rows corrected (P-588, P-589); new debts P-589, P-590]"),
              ("frontier/B1829_genesis_v1_61", " [S297: the candidate is FR-FIB's with the small-cut end; at the exact norms "
               "the six fail (THE EXACT END, 25.87 against 16.75; P-421)]")):
    vp = ROOT / a / "arc_verdict.json"; v = json.loads(vp.read_text(encoding="utf-8"))
    assert "S297" not in v["claim_one_line"]
    v["claim_one_line"] += br
    vp.write_text(json.dumps(v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("logs, B1830 section, claim brackets written")
