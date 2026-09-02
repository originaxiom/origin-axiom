# fab5cloud → cc — Phase B findings for hand re-application (interim, 2026-09-02 00:00 UTC)

Branch: `claude/physics-seat-evaluation-8dkbrl`. Nothing here is a request to merge; every item is a finding
with the file and line where the banking bench can re-verify it under its own numbers. Reader digests are
inputs; every item below was re-verified by this seat at the source unless marked *(reader, unverified)*.
The W-E absence-sweep verdicts and the last ~50 arc packets are still landing; a final version follows.

## 1. Verdict files that contradict the record (fix = touch the arc, not the log)

| arc | what the verdict/FINDINGS still says | what the record says | where |
|---|---|---|---|
| B361_seam_local_law | `arc_verdict.json`: "Across 8 pairs with zero counterexamples …", `superseded_by: null` | B367 §"Step 0's own discovery: the local law (B361) is REFUTED at pair (3,4)" | `frontier/B367_value_map/FINDINGS.md` l.45 |
| B362_seam_law_confirmations | "11 pairs, zero counterexamples" | same refutation, next day | *(reader; inherits B361)* |
| B259_gravity_brick_wall_map | wall #5: golden k=3 → GΛ=2π, "122 orders from observation" (FINDINGS l.42–46; verdict claim "one 122-order gap") | `PROGRESS_LOG.md` l.9436 (B980): "**Verdict: RETRACTED.** B259's wall #5 chain …" | no retraction in the arc |
| B892_second_measurement | `arc_verdict.json` claim: "z(x1,y*) = su(3)+su(2)+u(1)^3 EXACTLY: two measurements … take E6 to the SM algebra, skipping SU(5)", PROVED, `superseded_by: null` | FINDINGS banner (B950): 14-dimensional, "overstates by two abelian factors"; B951: classified A2+A1 Levi subalgebra | verdict never edited |
| B258_two_ended_unification | "silver (m=2) … trace field DEGREE 8 — non-arithmetic"; "only the figure-eight has a quadratic trace field" (PROVED) | B147: silver RRLL is arithmetic, invariant trace field ℚ(i), vol = 12 × covol(PSL(2,ℤ[i])) — re-verified in R33/R35 | `two_ended_unification.py` l.13, l.41; FINDINGS l.15–21. Same Reid-for-knots misapplication B125 corrected in B123 |
| B211 / B213 | "Φ(x,z) is 40a1" | Φ = 0 has j = 55296/5 = 40a3 (2-isogenous class-mate); B509/B510 already say so | R32; `frontier/B509_*`, `B510_*` |

## 2. Numbers in the bank that do not reproduce (each with the computed value)

| arc | bank | recomputed | cell |
|---|---|---|---|
| B213 torsion of 40a1 | ℤ/4 | ℤ/2 × ℤ/2 (x³−7x−6 = (x+1)(x+2)(x−3)) | R32 |
| B213 ∏c_p | 8 | 4 (c₂ = c₅ = 2); the 8 folds in the two real components | R32 |
| B213 L(E,1) | 0.7422811388969421 | 0.7422062367111932 (PARI); ratio L/ω₁ = 1/2 unaffected | R32 |
| B213 Mahler measure m(Φ) | 0.7417527164660 | 0.742264063232416 (Jensen, 30 dps; 2-D integral agrees); not equal to L(E,1), no Boyd identity with 40a | R32 |
| B333 "14 of 123 fundamental discriminants to −400 have h = 2" | 14 / 123 | 16 / 122; `compositum_seam.py` `fundamental_discriminants()` tests `(−m) % 4` instead of `m % 4` (21 non-fundamental in, 20 fundamental out). Verdict "generic" unchanged | R36 |
| B850 length-spectrum multiplicity maxima | m004 4, m003 3, m136 4, m009 8, m015 2 | SnapPy geometric multiplicities to Re ℓ ≤ 4: 12, 12, 11, 11, 6 — the bank's numbers count holonomy words | R37 |
| B840 bronze trace-field degree | "8 (script) vs 6 (B578-D6 prereg), UNRESOLVED" | 8, explicit octic x⁸+6x⁶−x⁵+12x⁴−3x³+8x²−x+2, disc 391728981 | R33 |
| B208 "re-audit to m = 300 000" | uncommitted | 0 failures to 300 000 (R31); committed script asserts to m = 200 | R31 |

## 3. Belt findings (tests)

- **29 test files assert the literal string `REPRODUCES` inside a committed reproduce script / output text**
  (`tests/test_b1160_hypercharge_forced.py` l.51–53 is typical; B1147–B1185). These cannot fail unless the text is
  edited. The results they guard mostly re-ran fine in R22–R25, so this is a belt defect, not a result defect.
- Complete test digest (1122 files): RECOMPUTES 763, COMPARES_TO_STORED 326, TAUTOLOGICAL 17, SMOKE 7; 80 files
  recompute only under `OA_SLOW=1`; 98 files flagged self-referential by the readers (`synthesis/tests.tsv`).
- **B919's sin²θ_W = 3/8 is not reproducible from the repository**: `traces.py` needs `HANDOFF6_RUN`/`cw.py`
  (uncommitted on all 7 heads, swept); `tests/test_b919_traces.py` asserts substrings of the stored
  `results.json`, whose own `two_prime_traces_3_5_0` is False (ONE-PRIME). (R38)

## 4. Confirmations worth knowing (so cc does not re-spend on them)

R31–R38 re-derived, without Sage, and found MATCH: B208; B213's L/ω₁ = 1/2 and nine-curve null table; B142, B146,
B210, B235, B307 (32 cubic fields of 500, all (1,1)), B781, B803 (m003/m004 share a double cover), B850's
ℚ(√−7) for m009; B252; B3, B127 (plus: the b+− family has CS = 1/4 for every m), B129, B147, B197, B212, B321,
B322 (78/79), B326; B331, B335, B406, B486, B488/B489, B509/B510, B520; B790, B777, B894; B854's u(1)⁴ and
B866's support scripts rerun clean; B516 (Pisot only for golden, R40); B518/B344/B332/B331 trace-map identities (R41).
Cells: `recompute/R31_*` … `R41_*`, closures in `recompute/R3_REPORT.md`.

## 5. Owner elections

`campaign/phaseB/synthesis/owner_elections.tsv` carries 188 elections verbatim with date and log entry, for the
ledger rows. Rule 1 (sweep before any absence claim) and rule 2 (read all arcs/belts/tests through the logs) were
executed as `campaign/PHASE_B_FULL_READ.md` records.

## 6. Absence claims (owner rule 1: sweep before concluding absence) — the W-E sweep, both parts

1068 absence claims extracted by the readers were swept over the six other heads and the deleted-file corpus; the seat
wrote 783 verdicts by hand (`campaign/phaseB/sweeps/VERDICTS.md` lists the ones that matter; `VERDICTS.tsv` has every row):

- **Wrong as written (2 rows, one defect):** B806_lexicon_blindness' table says CL-W4115 "Never ran";
  `frontier/B778_cleanup/cells/CL-W4115/` has compute.py, output.txt, results.json (chord '1,5,19,71' REAL: True).
- **Stale, never corrected in the arc (44):** B58 "SL(4) not built here" (B742/B745); B265/B270 "cup-product obstruction
  not computed" (B273: vanishes); B849/B850/B852 "m004 Maass eigenvalues never computed / Hejhal not in-sandbox"
  (B797's 17, B1007 arb); B73/B75 SL(4) Dehn-filling nulls (B88); B306 "no dim-14 centraliser" (B892); B872 "cell9
  verdict2 exists nowhere" (B921 harvested it); B204 "normalisation unresolved" (OI-063); B21 "no Einstein equation"
  (B259, 3d); B126/B123 "no trace-field classifier" (W3-067); B85 "numerical routes are DEAD" (B742); B289's m003/m136
  extensions (B855/B995); B272 "hypercharge unaddressed" (B862/B1160); B931/B855 "no null non-commensurable with both"
  (m009 in B850/B855); B958/B961/B974 "no independent construction of the frame / M12" (B978: B911 built it, definitions
  in CMT_DRAFT §2); B968/B952 "exotics never addressed" (B951/B962/B970); B1009 "no cascade on any m ≥ 2 grammar"
  (B1019); B1119 "compact colour open" (B1125 NO-COMPACT-HOST); B1107/B1113 "verifier never executed" (B1207);
  B796/B921 "frontier/B909* does not exist" (it does); the unharvested B796 files (B921 harvested them).
- **Answered only off main, or contradicted there (13):** B1026_the_one_involution (exchange symmetry) and B1030
  (ONE continuous dimensionless input remains — contradicting B1025's "none" on main) on
  `origin/claude/new-session-qor5up`; B1039/B1043/B1045; the Maass degree-law / full window on
  `audit/b775-braver-questions`.
- **A computed cell deleted from history, re-run, reproduced:** `frontier/B775_phase2_wave1/cells/_verify_Z1/`
  (P2W4-Z1, the exact Z_k = Tr ρ_k(A1) ladder to k = 22, incl. Z_18 = 2 − √5), removed by c8f3167c as "accidentally-
  committed scratch"; recovered under `campaign/phaseB/sweeps/deleted_corpus/` and re-run byte-for-byte in
  `recompute/R39_recovered_Z1_ladder/`: 21/21 shared levels agree. The correction commit kept the conclusion and dropped
  the evidence; if the table is wanted, it belongs beside the Wave-4 correction as a results file.
- **STAND after direct check (11):** e.g. Regina not installed on this bench either; no f(n,d) for d ≠ 2; h(ℚ(√5)) = 1
  and the fundamental unit φ are never computed in-repo (PARI here: bnfinit(x²−x−1).no = 1, .fu = −φ).
- The rest: 293 CONSISTENT, 206 NOISE, 11 GENERIC, 203 registry-only echoes; 161 rows the sweep could not test
  (DOC_ECHO / NO_HIT).

## 7. Still landing

The last ~14 arc packets (their absence claims get a small third sweep), the final rollup counts, and the paper-facing
summary. This note becomes final when `campaign/phaseB/synthesis/coverage.md` reads 131/131.
