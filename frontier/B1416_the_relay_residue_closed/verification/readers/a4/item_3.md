# Item 3 — CODEX_TO_CC_2026-09-01_WAVE9_QUESTION_MAP.md

## HEADLINE (the relay's ask, verbatim)

> "Verify and harvest the B1221--B1230/R031A/R031B proposition delta. The living map has 201 rows
> and passes its integrity/render locks."
> Nine new canonical rows were required (`OA-C1176`–`OA-C1184`); "B1225/B1227 and the other
> B1228--B1230 subclaims are deduplicated into their existing rows … Please treat the Q11 paragraph
> as a post-send record fence only; no external follow-up is requested."

## THE CLAIM

Codex's Wave-9 question-map delta adds nine rows to a 201-row living proposition ledger
(`documents/PROGRAM_QUESTION_ANSWER_MAP.md` + `documents/program-question-map/inventory/backbone.json`,
in the codex worktree). Each row is a status + one-line disposition drawn from main's own
B1221–B1230 arcs plus codex's own R031A/R031B audits. Per-row detail (question paraphrased from
`documents/program-question-map/evidence/PROGRESS_BANK_2026-09-01_WAVE9.md`):

| id | question (codex's paraphrase) | codex status | disposition | main arc named |
|---|---|---|---|---|
| OA-C1176 | Is the ℤ(SU3)×ℤ(SU2)×U(1)_Y kernel on the full 27 path-independent (SU(5)-free)? | PROVED | ℤ6 kernel, conditional on **primitive integral hypercharge normalization** | B1221 |
| OA-C1177 | Do the anomaly equations + the kernel calc derive that primitive normalization? | REFUTED | they are homogeneous; normalization is consumed, not derived | B1221 |
| OA-C1178 | Does "every proved vanishing is one symmetry obstruction" hold as a universal law? | REFUTED | fails even after correcting B1222's invalid H1-torsion population test | B1222 (+ B1224 correcting the test) |
| OA-C1179 | Does the disc-6237 S3 (cubic field) act on the object's face-V4 as D4 triality? | REFUTED | S3's quadratic resolvent Q(√77) is disjoint from the V4 faces; compositum is direct, not semidirect | B1223 |
| OA-C1180 | Is a mirror-odd invariant on an amphichiral manifold forced to be two-torsion (not necessarily 0)? | PROVED | CS ∈ {0, 1/4}, both realized, 6/6 on census | B1224 (+ B1227 general theorem) |
| OA-C1181 | Is there a typed map identifying the CS two-torsion bit, the surviving "c-bit," and a boundary modular-invariant bit? | OPEN | no typed map exhibited | B1229 |
| OA-C1182 | Is there a 4D EFT map sending the CS bit to a named SM CP-even/odd phase? | OPEN | no map constructed | B1226 |
| OA-C1183 | Does R031A resolve C-2: is B_0 = 4χ_0 with the marked generator acting by I_4 (not a primitive cyclotomic scalar)? | PROVED | generator exponents (0,0,0,0); K-rank 4, ℙ³_K genuine | B1230 C-2 / codex R031A |
| OA-C1184 | Has a finite RCFT/modular boundary receiver been constructed for the geometric complex PSL(2,C) m004 sector? | OPEN | none constructed | B1229/B1230 (item 1 of this harvest) |

## COMPUTED / CITED / ASSERTED

The row-level dispositions are **CITED** summaries of main's own arc verdicts (codex did not
re-derive B1221–B1230's mathematics; it read and re-typed them into the question-map's fixed
status vocabulary). What codex **computed** independently for this delta is confined to R031A/R031B
(items 1 and the OA-C1183/1184 pair above) — covered in items 1 and 2 of this harvest. The row IDs
and counts themselves (201 total, "PROVED 75 REFUTED 61 CONDITIONAL 15 EXTERNAL_BLOCKER 22
EMPIRICAL 2 OPEN 26") are **ASSERTED** bookkeeping about codex's own ledger file, not something this
reader can verify without that ledger (it lives only in the codex worktree).

## ON MAIN ALREADY? (per row)

Main does **not** use the `OA-C11xx` numbering anywhere in real content — confirmed by grepping
each of `OA-C1176` through `OA-C1184` individually across `docs/` and `frontier/` (excluding the
codex worktree): the only hits are `docs/RELAY_LEDGER.md`, `frontier/B1412_the_relay_backlog/FINDINGS.md`,
and one raw TSV row in `frontier/B1412_the_relay_backlog/verification/batch_10.out.tsv` — all of
which are prior bookkeeping *about this same escalation*, not adopted rows. So at the level of "does
main have a row named OA-C1176…1184," the answer for **all nine** is **NOT ON MAIN**.

But the underlying *content* each row summarizes is main's own arc, in every case except one:

- **OA-C1176 — ON MAIN**, exactly: `frontier/B1221_global_form_path_independence/ADDENDUM_2026-08-31_the_Z6_needs_primitivity.md:24-26`
  ("`|kernel| = 6` exactly when `gcd(k, 6) = 1` — the primitive normalisation").
- **OA-C1177 — ON MAIN**, exactly: same file, lines 28-39 ("the anomaly conditions are
  **homogeneous**… the scale that makes the charges primitive is **not supplied** by the anomaly
  computation. It is a convention").
- **OA-C1178 — ON MAIN, close paraphrase.** `frontier/B1222_symmetry_vanishing_thesis/arc_verdict.json`
  ("VERDICT NEGATIVE… a thesis failing its decisive test… is refuted, not partially confirmed") and
  its `ADDENDUM_2026-08-31_the_decisive_test_was_invalid.md:15` ("the thesis remains **partially
  supported and not established**"). Main's language is softer ("partially supported, not
  established") than codex's flat "REFUTED," but not contradictory — both agree the universal
  thesis does not stand as stated.
- **OA-C1179 — ON MAIN**, exactly: `frontier/B1223_triality_correspondence/arc_verdict.json`
  ("Direct is not semidirect… an isomorphism of small groups, not a structural correspondence").
- **OA-C1180 — ON MAIN**, exactly: `frontier/B1224_amphichiral_cs_torsion/arc_verdict.json` and
  `frontier/B1227_one_theorem_two_regimes/arc_verdict.json` (the general two-value-group theorem).
- **OA-C1181 — CONTRADICTED (see DISPUTED below).** Main's `frontier/B1229_the_consistency_turn/FINDINGS.md:60-63`
  does not read as OPEN; it reads as asserting the identification is already established: *"the
  c-bit **IS** the modular-invariant choice, and that matches B1184 **exactly**… arriving from a
  completely independent direction."* No hedge, no OPEN flag, and — checked directly —
  `docs/IDENTIFICATION_LEDGER.md` has **no entry** for a "CS-bit ≡ modular-invariant-bit"
  identification (grep for `c-bit`/`modular-invariant` in that file returns nothing), so it has
  never been priced the way the closely analogous `I-7` (item 1) was. Codex's OPEN grading is the
  more defensible one; main's own text is what needs a fence, not codex's row.
- **OA-C1182 — ON MAIN**, exactly: `frontier/B1226_the_beta_odd_box/arc_verdict.json` cell 3 ("the
  type-matched question… has never been asked… registered as a lead, not banked").
- **OA-C1183 — ON MAIN**, exactly: `frontier/B1232_codex_r031_verified_and_three_columns/FINDINGS.md:29-38`
  ("Retraction 3… `B_0` generator exponents = `(0,0,0,0)`; C12 acts by `I_4`… K-rank 4, not 1").
- **OA-C1184 — NOT ON MAIN** as a stated open row (this is the same gap identified in item 1: main's
  correction of B1229/B1230 stops at "rationality doesn't give finiteness" and never states, as its
  own open question, "no finite RCFT boundary receiver has been constructed for m004").

## NEEDS COMPUTATION HERE

**DOCUMENTARY for all nine** — this is a reconciliation of two ledgers' bookkeeping, not new
mathematics; every row's underlying claim is already computed/verified on one bench or the other
(see the file:line citations above), and this reader's grep sweeps (`OA-C1176`…`OA-C1184`
individually, plus `c-bit`/`modular-invariant` in `IDENTIFICATION_LEDGER.md`) are the discriminating
facts, already run. The one substantive follow-up this surfaces: someone should re-open
`B1229_the_consistency_turn/FINDINGS.md` and add a dated fence to the "c-bit IS the modular-invariant
choice" paragraph (lines 60-63), parallel to the fence B1230's addendum already added to C-5b for
the same species of error, and register the identification in `docs/IDENTIFICATION_LEDGER.md`
(UNEARNED, pending an exhibited map, exactly as `I-7` was).

## GRADE PROPOSAL

- OA-C1176: **ALREADY-ON-MAIN**
- OA-C1177: **ALREADY-ON-MAIN**
- OA-C1178: **ALREADY-ON-MAIN** (softer wording, same substance)
- OA-C1179: **ALREADY-ON-MAIN**
- OA-C1180: **ALREADY-ON-MAIN**
- OA-C1181: **DISPUTED** — codex's OPEN is right; main's own un-fenced text asserts the join
- OA-C1182: **ALREADY-ON-MAIN**
- OA-C1183: **ALREADY-ON-MAIN**
- OA-C1184: **REGISTER** — genuinely missing as a named open question on main (same gap as item 1)

The overall Wave-9 delta should be **REGISTER**ed as a formal harvest into whatever main uses in
place of an `OA-C` ledger (main has no such live ledger of its own — the numbering itself is
codex's), crediting each row's disposition to its already-existing main arc, adding the one missing
row (OA-C1184-equivalent) as new, and adding the one corrective fence (OA-C1181) as a follow-up
addendum to B1229. None of the nine rows calls for new computation; none is SUPERSEDED.
