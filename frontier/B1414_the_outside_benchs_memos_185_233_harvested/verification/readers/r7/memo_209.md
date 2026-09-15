# Reader r7 — Memo 209 (`memos/THE_SWEEPS_FALSE_POSITIVES.md` + Addendum 1 to
`memos/THE_TRIAGE_WAS_ALREADY_DONE.md`)

## 1. HEADLINE

"MOST OF THE SWEEP'S HITS ARE HEALTH, NOT DEBT — and memo 208's diagnosis was too broad." No
per-memo date line in the file body; INDEX.md row 307 records "banked 2026-09-12."

## 2. CLAIMS

1. Of the 28 `open_claim_sweep.py` hits memo 208 left unexamined: **2 genuinely stale**
   (`THE_SPINE`'s B171, B1130), **1 correct as written** (`THE_SPINE`'s B1156), **1 exemplary**
   (`OPEN_PROBLEMS` gate D), **1 tracked-pending** (`GRAND_COMPUTATION_LEDGER` I3), **23 benign
   self-citation** (classified, not individually verified). Grade: measured triage (no seal;
   substring tests on tracked files at HEAD).
2. Structural false-positive class identified: `open_claim_sweep.py` ranks by shared-term IDF,
   so a verdict document scores high against the arc that produced its own verdict, "by
   construction" — a healthy pattern, not a sick one (LAW_MAP 7 hits, THE_SM_VERDICT 3,
   main.tex 3, THE_FRAMEWORK 2, PRICED_DOORS 2, CROSSING_REQUIREMENTS 2). Grade: mechanism
   identified and demonstrated.
3. Triage rule: a sweep hit is a true positive only when the surface's claim carries an
   OPEN/never-run/unresolved status **and** the arc settles that same question; a hit on a
   verdict-recording document is expected. Grade: methodological rule, derived from claim 2.
4. **B171** `OPEN` at `THE_SPINE.md:211` vs `frontier/B172_combination_gap_resolution/
   FINDINGS.md:1,4` ("resolved (Phase 1)", "Answers the question B171 opened... affirmatively,
   hedged") → stale in status, not necessarily finished as a programme. Grade: genuinely stale.
5. **B1130** `OPEN` at `THE_SPINE.md:1240` vs `frontier/B1133_c4_single_end/FINDINGS.md:1`
   ("the tower is SINGLE-END", "the two-ended question RESOLVED single-end", not hedged) →
   stale. Grade: genuinely stale.
6. **B1156** `OPEN` on `THE_SPINE` vs its own arc's "Verdict OPEN (seam
   INDETERMINATE/FLOOR...)" → the spine **agrees** with its arc; not stale. Grade: correct.
7. Memo 208's "the write-back step has no owner" is **corrected as too broad** (not rewritten,
   addendum-corrected): `docs/HARVEST_LEDGER.md` is a working write-back loop (its own memo 136
   is already logged there, SCHEDULED, at the line the memo quotes); `docs/OPEN_PROBLEMS.md`
   gate D carries a dated currency note warning future readers not to reuse B1085/B1095's code.
   Corrected sentence: "the programme HAS a write-back loop... `docs/OPEN_LEADS.md` is outside
   it." Grade: corrected-by-addendum (memo 208's count of eleven and 17/10/7 split explicitly
   left unchanged).
8. Fence: 23 of 28 were classified by class, not individually verified — stated explicitly so
   the number "is not later quoted as twenty-three checked rows." Grade: self-fencing.

## 3. CERTIFICATE

- `certificates/the_sweeps_false_positives.py` — EXISTS.
- `outputs/the_sweeps_false_positives.txt` — EXISTS; tail matches the memo's §5 breakdown table
  exactly (per-surface hit counts: LAW_MAP 7, main.tex 3, THE_SM_VERDICT 3, THE_SPINE 3,
  THE_FRAMEWORK 2, PRICED_DOORS 2, OPEN_PROBLEMS 2, CROSSING_REQUIREMENTS 2,
  GRAND_COMPUTATION_LEDGER 2, CLOSED_DOORS 1, THE_ROAD 1 = 28), ends "ALL ASSERTIONS HOLD AT
  THIS HEAD."
- **No seal** — the memo states this explicitly ("Every claim is a substring test on a tracked
  file at HEAD"), so there is no sha256 to check.
- The claimed Addendum 1 to `THE_TRIAGE_WAS_ALREADY_DONE.md` (memo 208) — CONFIRMED present:
  I read the full addendum text at the tail of that file; it matches memo 209's own description
  of the correction exactly, word for word on the corrected sentence.

## 4. ON MAIN ALREADY?

- **B171/B1130 (claims 4–5): (c) NOT on main / not yet fixed.** I re-checked `docs/views/
  THE_SPINE.md` at current HEAD: `B171` is still `OPEN` at line 211, `B1130` is still `OPEN` at
  line 1240 (with `B1133 PROVED` at line 1243 stating the tower is single-end) — the staleness
  memo 209 flagged has **not** been corrected on `THE_SPINE.md` as of this read. This is not a
  contradiction of memo 209 (memo 209 never claimed it would fix them, only diagnosed them) but
  it means the diagnosed staleness is still live.
- **B1156 (claim 6): (a) already on main**, self-consistently — `THE_SPINE`'s OPEN row and the
  arc's own FINDINGS both say OPEN; verified this is the state memo 209 describes.
- **GRAND_COMPUTATION_LEDGER I3 (claim 1's "tracked-pending"): (d)-adjacent — superseded by a
  LATER main event.** At the time memo 209 was banked (2026-09-12) I3 was "SCHEDULED" per
  `docs/HARVEST_LEDGER.md:417` (confirmed: that exact line, quote, and memo-136 citation are
  present verbatim at HEAD). But `docs/GRAND_COMPUTATION_LEDGER.md:98` **now shows I3 as
  `closed`**, with text: "DEAD — the row was closed 2026-09-14 and this cell was left asserting
  it live... Owner confirmed the closure 2026-09-15." So the specific "tracked-pending" status
  memo 209 measured on 2026-09-12 has since moved — not a contradiction (I3's SCHEDULED-in-
  HARVEST_LEDGER status is a distinct, still-accurate fact from I3's since-changed
  GRAND_COMPUTATION_LEDGER row), but it is now stale in the other direction and a verifier
  should note the row it discusses has since closed.
- **The write-back-loop correction (claim 7): (a) already on main, confirmed exactly.**
  `docs/HARVEST_LEDGER.md:417` matches memo 209's quote character-for-character ("SCHEDULED
  (no main text names it — the slice D backlog, read before Review 57)", memo 136, dated
  2026-09-09). `docs/OPEN_PROBLEMS.md` gate D's currency note also exists as described (not
  independently re-quoted here but the HARVEST_LEDGER line's exact match gives high confidence
  in the memo's accuracy).
- **`open_claim_sweep.py` itself is real and on main**: `frontier/B1218_open_claim_sweep/` and
  `frontier/B1219_reverse_sweep/` both exist, confirming the instrument memo 209 audits is a
  real, banked main-line tool, not an outside-bench-only artifact.

## 5. NEEDS COMPUTATION HERE

- Claims 4–5 (B171/B1130 staleness): DOCUMENTARY (grep/read, not a mathematical computation) —
  a verifier should simply re-diff `THE_SPINE.md`'s status tokens against the cited arcs'
  FINDINGS.md headlines; already done above and confirmed still stale.
- Claim 1 (23 benign self-citation, unverified individually): NEEDS COMPUTATION per the memo's
  own fence — a verifier could spend the effort to check all 23 individually (cheap: read each
  cited surface line and its named decider) to confirm none is a true positive the
  classification hid. Recipe: for each of the 28 `open_claim_sweep.py` hits, check whether the
  surface's own claim text carries an OPEN/unresolved status independent of the decider it
  names.
- Claim 7 (write-back loop): DOCUMENTARY — confirmed above by direct read; no computation needed
  beyond the grep/read already performed.
- Claim 2 (IDF false-positive mechanism): DOCUMENTARY — a methodological observation about the
  sweep tool's ranking algorithm, not a numeric claim requiring recomputation, though a verifier
  could re-run `open_claim_sweep.py` and confirm the claimed per-surface hit counts (28 total,
  broken down as listed) reproduce exactly.

## 6. SUPERSESSION

- Memo 209 itself corrects memo 208 by addendum (claim 7) — this is documented supersession-in-
  place, not a hidden problem.
- I3's GRAND_COMPUTATION_LEDGER status (part of claim 1) has since been overtaken by later main
  events (closed 2026-09-14/15, per B1405/B1407/B1408) — see §4. This doesn't invalidate memo
  209's 2026-09-12 snapshot but a reader should know the row it discusses has moved on.
- No later INDEX.md row marks memo 209 itself as withdrawn.

## 7. GRADE PROPOSAL

**REGISTER.** This is a documentary audit (substring tests, no seal, no mathematics) whose
value is the triage rule (claim 2/3) and the corrected write-back diagnosis (claim 7) — both
confirmed accurate against main at HEAD. The two genuinely-stale items (B171/B1130) remain
unfixed on `THE_SPINE.md` and should be logged as a small, concrete, still-open cleanup item
rather than re-computed; nothing here is DISPUTED, and nothing rises to the level of a
computation worth its own arc.
