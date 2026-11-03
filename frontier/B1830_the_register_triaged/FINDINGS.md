# B1830 — THE REGISTER TRIAGED: EVERY OPEN ROW TYPED (DEBT, LEAD, PROCESS), ONLY DEBTS AGE, THE 59 DEBTS RANKED BY THE LOAD THEY BEAR (THE OWNER'S RULING ON P-587)

**Verdict: PROVED** (a record of the owner's ruling, the gate that enforces it, and the first triage; nothing computed on
the mathematics). cc (main), 2026-11-03. **0 of 19.**

## 1. The question and the ruling

The owner, 2026-11-03: *"at what time should we deal with all open leads, and queued that are on our register? whats the
point of keepin them there? if theyre open do they bear load on our current math?"* Main measured it (P-587): 255 open
rows; the queue's slot table stale; the point-debt gate about to fail every push from 2026-11-04 (32 rows unmoved since
2026-10-13); 72 open rows question a banked result later work cites, about 15 bearing on current math — one of them, P-355,
on the candidate family B1829 had registered an hour earlier. Main proposed typing every open row DEBT, LEAD or PROCESS,
ageing only debts, and triaging now. The owner: **"yes"**.

## 2. What changed

- **The gate** (`scripts/checks/point_debt.py`, rule 6; `tests/test_point_debt_gate.py`, a new planted test): every QUEUED
  or LEAD row carries exactly one type tag in its *where* cell; only [DEBT] rows age (21 days, then ESCALATED with a next
  action); every open debt is on the ranked list under "## The debts, by load", which names only open debts.
- **The register** (docs/POINT_REGISTER.md): the typing section and the ranked list before the queue; the queue's slots
  kept for the rows that name them, its order superseded by the typing.

## 3. The triage (verification/)

- **Five readers** typed the 250 open QUEUED and LEAD rows and proposed closures with evidence (batch_1–5.md,
  proposals_1–5.json); **main verified every proposed closure** (MAIN_VERIFICATION.md).
- **Closed:** DONE P-386 (B1787), P-495 (B1823, B1825), P-502 and P-503 (the tools calibrated), P-510 (KIND_TABLE's ruling),
  P-520, P-521, P-522 (B1825's card), P-587 (here); P-292 merged into P-337. **Rejected closures** (kept open): P-485 and
  P-487 (the exclusion half never ran; B1825 ran only a restriction), P-218 (its question not carried by P-210).
- **Typed:** 59 debts, 141 leads, 41 process. P-321 retyped a debt by main. 15 debts older than two weeks escalated with
  their next action.
- **The ranked debts, by load:** first the debts bearing on current work — the strip candidate (P-585: P-355's D, P-384,
  P-586, P-446, P-517, P-559, P-444), the live prediction P10 (P-157), B1825's machinery (P-542, P-524, P-557, P-516, P-448);
  then false or stale statements in foundation and front documents (P-318, P-427, P-374, P-579, P-581, P-320, P-321, …);
  then checks that cannot fail and instruments (P-317, P-239, …); then unverified premises under structural results
  (P-156, P-054–P-057, …).

## Seen first

- `VERDICT topic-sweep /point register|POINT_REGISTER|point-debt|triage of the register|register triage|typed (rows|points)/
  (full text): 52 of 1576 arcs on main match (NEGATIVE 7, OPEN 2, PROVED 43); 4 register rows match (DONE 3, QUEUED 1)` — the
  register's own opening (2026-10-13, the owner: points lost between sessions) and its gate; the arcs that cite rows; no
  earlier typing of rows. The lead and relay debt gates (lead_debt.py, relay_debt.py) age their own items and are unchanged.
- **Literature (pointers):** the typing follows the common practice of issue trackers, which separate defects (owed fixes to
  what is in use) from feature requests and chores, and age only the first; an analogy for the shape, not a source.

## Disclosed

- The readers' KEEP means "not confirmed paid", not "confirmed unpaid": three of five batches sampled the record. Leads and
  process rows do not age, so a missed payment there costs nothing until the decadal review reads them; a missed debt ages
  and returns. The ranking within each tier is main's judgement.

## The recheck (S297, the same day; the owner: "just make sure sure sure sure u did them all right and didnt miss anything load bearing")

Main re-read the triage instead of trusting it. The audit trail is in `verification/recheck/`.

**The typing, row by row.** Every open row typed LEAD or PROCESS was screened for a load signal (`screen.py`): a cited arc
with later dependents and a correction word (the 72-row measure of P-587, now 69), a foundation document with a correction
word, or an integrity word. 46 rows were flagged and read in full by main; the 136 unflagged ones were read by their first
lines. Two rows were retyped DEBT. **P-154:** the retraction sweep never reads RETRACTED_PHRASES' 2026-10-07 and 2026-10-08
tables, so it is a guard of the living documents with a known blind spot. Main hand-swept their eleven statements in the 803
living .md files the same day and found no uncorrected instance. **P-421:** the candidate's end; see below. Every other
typing stands. The five OWNER rows bear no load: P-303's two readings select the same Higgs, F₆ (B1731), so B1732's premise
holds under both.

**The closures, re-read against each row's own ask.** All nine stand. P-386 was closed for its ask (the non-authoring
review, the acceptance, the run); its row now says the lane's six analytical successors were never banked on main and
transfer nothing.

**What the triage could not see.** A triage of the register reads only rows, so it cannot see a correction that never got
one. Main's screen of LAW_MAP (`stale_laws_title.py`, `dated_notes_screen.py`) looked for law rows whose headline arc carries
a retraction, a superseding verdict or a dated note that the row does not show. Two readers judged the hits, and main
verified every row they called stale or unsure at its source before any edit (B1216's rule: fan-out reports, main edits).
Of 72 rows screened (46, then 26), **20 were stale and are now sharpened in place** (P-588, P-589), and one scope note was owed: 'the canonical end' in the frame's rows means the small-cut norm at the canonical heights (B1667's row). Among them:
- **B1739** stated "∣V_ud∣ ∝ r^½" as a PROVED law; it is the median's slope only (P-588).
- **The candidate's rows** (B1726, B1734, B1735, B1741) carried no trace of THE EXACT END (S238): their end is the small-cut
  norm at L_max's height, and with the exact norms the six fail.
- **B1788's hypothesis (b)** fails on three slopes, a note made in the arc that morning (S287) that never reached its row.
- **A plain error:** [1/4,∞) for a hyperbolic 3-manifold's continuous spectrum, which is [1,∞).
- **Status lags and member-scope lags.**
- **Owed, and with no row until now (P-589, a DEBT):** the member-scope addenda of the gate's frozen baseline (B429, B713,
  B760, B959, B960, B1157, B1338, B1407: NEGATIVE verdicts that say "the object cannot" for a member's fact, owed since
  B1477), the same screen over GENESIS and THE_WEAVE, and the frame's other rows "at the canonical end" re-read at the
  exact norms.

The S250 currency read had written "No living surface repeats them"; LAW_MAP did. That is recorded in RETRACTED_PHRASES.

**The candidate (B1829), corrected.** THE SIX ON THE STRIP is a candidate of FR-FIB with the small-cut end, a chosen formula
without geometric ground. At the exact norms the six fail (THE EXACT END's sealed look: 25.87 against 16.75). S294's
re-grade had omitted this and S295 had not caught it; both are corrected in B1829's REGRADE and FINDINGS, LOOK_LEDGER and
P-585. P-421 is retyped DEBT and ranked after P-586.

**New debt: the negatives' scale scope (P-590).** Every sealed look compares tree-level outputs at M_Z. If a frame's values
belong at another scale, the target moves by a fixed vector δ (R1: ∣δ∣² = 11.8 for the ten). By the triangle inequality, a
value NEGATIVE is scale-robust when (√χ²_best − ∣δ∣)² still exceeds its bar.
- **Robust, even at the full ∣δ∣:** B1825, B1712, B1720's T3 and B1695's G1. So is the order-5 lines' exclusion, at any scale, through D, which does not run at one loop.
- **Not covered by the bound:** B1660 (34.40 against 11.07: too close to call) and every specificity negative, the nearest
  B1748 (1.54%) and B1720's T2 (1.65%).

**P-355's first owed item, paid (data-free).** Among the 528 points (α, β) of order ≤ 12 (266 lines up to sign), at two τ (0.3 + 2.6i, 0.7 + 3.1i), two seeds and both radii (B1830's verification/recheck/p355/: identity_lines_v2.py, summarise_v2.py), the lepton and down spectra coincide for EVERY Higgs exactly on B1703's d = e points — M_e = λM_dᵀ on orders 1 and 5 (B1728's SU(5)), M_e = λM_d on orders 2 and 4 (B1728's Pati–Salam), 40 points — and for a Higgs with NO QI component exactly on their 40 β-half-lifts, the points (α, β) with (α, 2β) a d = e point (α ∈ ¼ℤ with β ∈ odd/8: 16 points of order 8; α ∈ ⅕ℤ with β ∈ odd/10: 24 of order 10), which extends B1742's α = 2/5 case to every such line; everywhere else they split (coincidences to 9 × 10⁻¹⁵ of the heaviest mass, splits at least 2 × 10⁻⁴, the smallest where the lightest mass is about 10⁻⁴ of the heaviest; no point classed differently at the two τ or the two radii). With the frame's lepton factor c = 3, D = 9 exactly wherever the spectra coincide, so on the strip's lines (2/5, odd/10) the candidate rows' D ≈ 10.9 reflects their Higgs's QI admixture (B1742: the departure is linear in it). A re-verification of B1703, B1728 and B1742; the half-lift statement computed, not proved. A first scan (identity_lines.py) compared spectra by their ratio, which is noise where both sectors carry an exact zero, and missed order 4: superseded, disclosed. Items 2 and 3 stay owed

**Disclosed.**
- The screens are keyword and dated-note screens. A stale row whose arc carries no marker, or whose correction lives
  elsewhere, is not found by them; the old-era reader found two such rows (B716, B726) by reading past its hits.
- LAW_MAP, IDENTIFICATION_LEDGER and KIND_TABLE were screened systematically; the latter two had no stale row. GENESIS and
  THE_WEAVE were checked only for the claims corrected here (neither repeats one); their systematic screen is owed (P-589).
