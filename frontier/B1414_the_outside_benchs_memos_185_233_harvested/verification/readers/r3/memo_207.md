# Reader r3 — memo 207 (THE_REGISTER_IS_BEHIND)

## 1. HEADLINE
"THE LEAD REGISTER IS BEHIND ITS OWN ARCS, AND THE CORPUS'S OWN INSTRUMENT ALREADY
SAYS SO." **2026-09-12.**

## 2. CLAIMS
1. **L53**: row says `OPEN — first in the queue` (`OPEN_LEADS.md:521`) while the
   file's own primary row (`:270`) says `L53 CLOSED.` on B578-D1. — **self-contradiction inside one file, verified by substring test**
2. **L72**: row says `OPEN (B579)`, "Phases 2-3... gated on phase 1" (`:531`) while
   `frontier/B775_phase2_wave1/cells/P2W5-L72/compute.py:9,11` says "PHASE 1 is
   banked: B581" / "THIS CELL RUNS PHASES 2 AND 3." — **contradicted by an arc file, verified by substring test**
3. **L78**: row says `OPEN — Round 2 first` ★★★★ (`:552`) while
   `frontier/B583_chiral_content/FINDINGS.md:45` says "L78 resolves" on the rank-6
   result (`:43`). — **contradicted by an arc file, verified by substring test**
4. **L174**: row says `OPEN — C1 first` ★★★★★ (`:1922`) while C1-C4 all read
   `**DONE (B1088/B1090/B1089/B1091` at `:1915-1918`, eight lines above. — **self-contradiction inside one file, verified by substring test**
5. `scripts/checks/open_claim_sweep.py` already exists and already fires:
   `--selftest` gives positive control 5/5 (each hand-found lock ranks first) and
   negative control PASS (max score on off-corpus text 0.00, floor 6.0); the live
   sweep reports **52 open claims with a strongly-matching SETTLED arc**, 18 of them
   OPEN_LEADS rows, and flags **L78 → B583_chiral_content at score 36.4**, the
   highest-scoring lead row in the file. — **VERIFIED by running the certificate**
6. The sweep's reach is bounded honestly: it did **not** flag L53, L72, or L174 —
   those were found by reading, not by the instrument. — **stated limitation, not a defect claim**
7. Memo 206's E₆ level-2 stage is an **independent re-derivation**, not a new
   instrument: `P2W5-L72/compute.py` already built the same Kac-Peterson sum over
   |W(E₆)|=51840; the two builds agree exactly on all nine level-2 conformal
   weights as rationals (values tabulated: 0, 13/21×2, 4/3×2, 25/21×2, 6/7, 9/7). — **VERIFIED, agreement exact**
8. Honest split of memo 206's actual novelty: the E₆ level-2 stage = corroboration
   not novelty; B583 X3's rank-6 = a first reproduction (arc holds
   `FINDINGS.md`/`READING_RAW.md`/`arc_verdict.json`/`x2r_recompute.py`, none
   computing X3; the lock is level-1 only, confirmed); CELL 2 = new as a stated
   fact; CELL 3's reach law = new. — **stated grading, not independently re-derived beyond what's in the certificate**
9. **INTERPRETIVE finding, not a math finding**: the rows are wrong about *status*,
   not about *content* — L53's vanishing, L174's C1-C4, L78's rank-6 are all
   correct; this says nothing about the other 14 flagged (non-assigned) rows. — **explicit scope limit**
10. Rule filed: before ranking any lead as open, run `open_claim_sweep.py` AND read
    the lead's row together with adjacent rows — generalizing "BENCH ERROR #25"
    from memo 206 (which was too narrow: per-lead reading only). — **process rule, documentary**

## 3. CERTIFICATE
`outside_bench/certificates/the_register_is_behind.py` exists.
`outside_bench/outputs/the_register_is_behind.txt` exists. Tail of the output
confirms the C1-C4 substring checks (`[OK] C3 is banked ... "**DONE (B1090"`, etc.)
and closes with: *"ALL STRING ASSERTIONS HOLD AT THIS HEAD."* — this **agrees**
with the memo's headline (every quoted contradiction is a live, currently-true
substring pair). **No seal** — the memo states this itself ("every claim is a
substring test on a tracked file at HEAD, failing loudly if the string moved");
sha256 check N/A.

## 4. ON MAIN ALREADY?
- Claims 1-4 (the four contradictory rows): **(b) applied via the merge, as a
  literal in-place correction of the rows this memo (and its sibling memo 206/208)
  diagnosed.** Verified directly on current main:
  - `docs/OPEN_LEADS.md:521` — the struck-through `~~OPEN — first in the queue~~` is
    followed by `**[SUPERSEDED IN PLACE 2026-09-12 — outside-bench memos
    206/208/210/211/213/214/215...]**` and `**SUPERSEDED — this file's own primary
    L53 row reads "L53 CLOSED."**`
  - `docs/OPEN_LEADS.md:531` (L72) — similarly struck and marked **SUPERSEDED**,
    quoting `P2W5-L72/compute.py:9,11` exactly as memo 207 does, and additionally
    reporting Phase 2/3 now executed by later memos (210/211).
  - `docs/OPEN_LEADS.md:552` (L78) — struck and marked **RESOLVED**, citing B666
    cell T and memo 206's reproduction.
  - `docs/OPEN_LEADS.md:1922` (L174) — struck and marked **SUPERSEDED — C1 through
    C4 are all BANKED**, citing B1088/B1090/B1089/B1091 exactly as in memo 207.
  **Note the write-back credits "outside-bench memos 206/208/210/211/213/214/215"
  by number in every one of the four rows — memo 207 itself is not named in the
  citation list**, even though memo 207 is the memo that most directly enumerates
  and diagnoses these four specific rows (memo 208, `THE_TRIAGE_WAS_ALREADY_DONE`,
  explicitly says "memo 207 proposed to triage the flagged OPEN_LEADS rows" and
  extends the count to eleven). Substantively APPLIED; nominally uncredited.
- Claim 5 (`open_claim_sweep.py` exists and fires): **(a) already on main.**
  `scripts/checks/open_claim_sweep.py` confirmed present (10521 bytes,
  2026-08-30), i.e. it predates this memo — consistent with the memo's own point
  that the instrument existed and simply wasn't run against this file.
- Claim 10 (the "read adjacent rows + run the sweep" rule): **(c) NOT on main** as
  a codified process rule anywhere I can find (no `docs/PRACTICES.md` entry citing
  memo 207 by number); it is documentary and applied informally (the corrected
  rows above show the *outcome* of the rule being applied, not the rule itself
  being written into `PRACTICES.md`).

## 5. NEEDS COMPUTATION HERE
- Claim 5: re-run `scripts/checks/open_claim_sweep.py --selftest` (expect 5/5
  positive, negative-control max score 0.00) and the full sweep (expect ≥52 open
  claims flagged, L78→B583_chiral_content scoring highest among OPEN_LEADS rows).
- Claim 7: re-run the E₆ level-2 Kac-Peterson conformal-weight computation
  independently (integer Weyl sum, float64) against `P2W5-L72/compute.py`'s
  high-precision build and confirm all nine rational weights agree.
- All four contradiction claims (1-4): DOCUMENTARY — substring presence/absence
  checks on tracked files, not numeric claims; re-verifiable with `grep -n` at the
  cited line numbers (done above, all four confirmed superseded/resolved in place).

## 6. SUPERSESSION
Not withdrawn. **Extended, not superseded**, by memo 208
(`THE_TRIAGE_WAS_ALREADY_DONE`, same day, `outside_bench/INDEX.md:306`), which
finds a pre-existing 2026-07-17 triage table (`frontier/B666_leads_campaign/cellT/TRIAGE_TABLE.md`)
already parsed 38 rows with 17 SUPERSEDED, and that memo 207's four rows were four
of **eleven** total unwritten-back verdicts (adding L112 and three unapplied triage
decisions: L26, L54, L64, L65, L73, L74 — memo 208's "7 NOT APPLIED"). Memo 208
explicitly frames itself as generalizing memo 207, not contradicting it: "the
failure is not analysis and not effort... THE WRITE-BACK STEP HAS NO OWNER."

## 7. GRADE PROPOSAL
**ALREADY-ON-MAIN** — all four flagged rows (L53, L72, L78, L174) are now visibly
struck through and marked SUPERSEDED/RESOLVED in `docs/OPEN_LEADS.md` at the exact
lines memo 207 cites, consistent with the merge. One documentary gap worth noting
to the owner: the write-back attributes the correction to "outside-bench memos
206/208/210/211/213/214/215" and never cites memo 207 by number, even though 207 is
the memo that first assembled all four contradictions in one place with the
generalized diagnosis ("the register is behind its own arcs") — a minor
attribution/provenance omission, not a mathematical or status dispute.
