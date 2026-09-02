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

- **B511 D3.3 (Phase C rerun, R48 — corrected).** `frontier/B511_physics_verdict/d3_wild_access.py` and `d3_measure.py`
  do not produce numbers on this bench: the Fibonacci-type matrix recursion amplifies round-off like φ^t, the pairs leave
  SU(2) after ~70 steps, and every history is NaN by step ~200. The banked `d3_results.json` percentiles "2.0, 2.0, 2.0"
  to 13 digits are the same collapse on an older numpy (finite garbage whose traces give κ = 2 identically), so **those
  specific numbers are artifacts**. The claim itself survives: on trace coordinates (F: (z,x,xz−y), M: (z,z,w),
  D: (x²−2,y²−2,w), w = xyz−x²−y²+2, verified to 1e−15) the dynamics is compact and runs at any precision; at 60 digits
  with no escapes P(classical) / P(wild) = 0.93/0.04 (M10/D10/F80), 0.97/0.02 (D20/F80), 0.85/0.08 (M20/F80), i.e. D3.3's
  "≥ 0.84 / ≤ 0.10" holds (M20/F80 at the bound), and the F-only control keeps κ exact and wild. Ask: replace the two
  scripts by the trace-map version and re-bank d3_results.json. (My first note here said the corrected dynamics
  reverses the verdict; that came from an SU(2)-re-projection method that the φ^t growth makes worthless. Retracted.)

## 2b. Certificates on the codex and outside-bench heads, rerun here (Phase D, R46–R50) — 2026-09-02 04:40 UTC

- **All 11 chain-critical codex certificates run and pass on this bench** (R46): r019 hypercharge (the ratio theorem
  is universal given SM multiplicities, "independently of E6" in its own words), r017 up-Yukawa rank 0 (both the no-go
  and the cup-product scope), r006 twisted_double (h¹(M;27) = 3, adjoint closure 78), check_charge_bracket, r013 rung
  transfer (Paper II's eleven Levi dimensions), r023 generation obstruction, r024, r026, r010, r020 (its own negative).
- **Fourteen chain-critical outside-bench certificates run and pass here** (R47): breaking_chains (unique SM chain,
  necessary-condition level), susy_test (no supercharge), anomaly_payment, the Yukawa family, carrier, parity lemmas.
  So B1162's "cited, not re-run" items D3/D5 now have a third-bench rerun (sweep #1207 annotated).
- **One certificate contradicts itself (R49):** cloud's `spacetime64.py` (re-fired by `a2_glue64.py`, memos 27/33)
  prints `color-singlet (0,0) content in the complement: 2 (0 = NO hypercharge room; matches memo 11)`. The 2 are the
  two Cartan directions of e6 outside so(3,1) ⊕ su(3) (rank 6 − 4); they commute with the whole subalgebra, so the
  centraliser is at least u(1)², i.e. there IS room for two abelian charges. The "no hypercharge room" sentence should
  not travel into main; the 64-gluing theorem of memo 33 (θ a bracket-equivariant bijection, 3 ↔ 3̄) reproduces here
  and discharges B1140's NOT-checked fence (sweep #1186 updated).
- **A live mechanism disagreement, not a contradiction (R47):** cloud's `yukawa_texture.py` says the object's kinematics
  ALLOWS an up-type Yukawa with 6 nonzero entries, while codex r017 (and main's B1167) say the heterotic dressing forces
  μ_u = 0. Both pass; they answer different questions (coupling structure vs bundle cohomology). B1185 already records
  the pair; the paper-facing sentence should say "forbidden by the dressing", not "forbidden by the object".
- **Committed scripts that no longer run as banked, while their claims survive by direct recomputation:** B511 D3.3
  (R48, above) and B775's V4 genericity table (R50: `v4_genericity_test.py` misreports every manifold as non-amphicheiral
  on this SnapPy because of a fragile `symmetries()[0]` probe; the 8-row table itself is right — m004, m003, m025, R²L²
  amphicheiral, m009/m010/RRL/RLL not).
- **Housekeeping for reruns:** outside-bench certificates that read the corpus pin commit 3c58527b, which is on no
  branch; `git fetch origin 3c58527bc3851ae44fef4f48ecc1eac8aa9dd41b` restores them. `c3_ohtsuki_large.py` "fails" only
  in the sense the record already states (the ≥ 60-digit gate unmet: honest negative); `paired_summary_check.py` is the
  record's own BUILT-NOT-ADOPTED P1-USELESS instrument.

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

## 6. Absence claims (owner rule 1: sweep before concluding absence) — the W-E sweep, all five parts

**Correction first.** My earlier drafts of this section said 1068/1535 claims were swept. A defect in my own tooling
(the rollup re-sorts `absence_claims.tsv`, so the row index the sweep parts were keyed to shifted between runs) meant
only 1094 of 1535 distinct claims had been swept and 441 rows were duplicates. Found 2026-09-02, repaired: part 5 swept
the 441 missed claims (arcs B436–B771); `campaign/phaseB/sweeps/sweep_index_map.tsv` ties every verdict to its claim.
Coverage is now 1535/1535 distinct claims; the counts below are per distinct claim.

1535 absence claims were swept over the six other heads and the deleted-file corpus; verdicts by hand on every LEAD,
REGISTRY_ECHO and UNSWEEPABLE claim (`campaign/phaseB/sweeps/VERDICTS.md` lists the ones that matter; `VERDICTS.tsv` has
every row): CONSISTENT 554, REGISTRY_ECHO 290, NOISE 132, SUPERSEDED 90, GENERIC 29, STANDS 16, OPEN_LATER 10,
CONTRADICTED 3.

- **Wrong as written (3):** (1) B778_cleanup's own FINDINGS l.21–24 ("Pending the next pass … CL-W4115 … Never ran. /
  CL-LATIN … Never ran.") contradicts its own directory: `frontier/B778_cleanup/cells/CL-W4115/` holds a completed run
  (compute.py, output.txt, results.json: chord '1,5,19,71' REAL True; wall re-verified as field-disjointness) and
  `cells/CL-LATIN/` exists; `tests/test_b778_cleanup.py` locks the stale text. (2) B1191 GC-15 evidence "Only F3 … has
  ZERO test coverage anywhere in the repo": `tests/test_b279_spin_structure_bit.py` exists on main. (3) B8141
  "AUDIT_B1076_ONE_NOTATION_DEFECT.md and I_WAS_WRONG_THE_REAL_DEFECT.md are absent but not gitignored": both exist on
  `origin/paper/structure-genesis-first` (B8084 / B8090 relays). Fix for each = touch the arc text, not the log.
- **Stale, never corrected in the arc (89):** the part-1/2 list stands (B58/B742-5; B265-B270/B273; B849-B852/B797-B1007;
  B73-75/B88; B306/B892; B872/B921; B204/OI-063; B21/B259; B126/W3-067; B85/B742; B289/B855-B995; B272/B862-B1160;
  B931-B855/m009; B958-B974/B978; B968-B952/B951-B970; B1009/B1019; B1119/B1125; B1107-B1113/B1207; B909 exists; B796
  files/B921). New from parts 3–5, cc-relevant because a paper or a verdict file still carries the stale sentence:
  B8080 deposits the assembly code and finds the six-group classification FALSE AS STATED (all six admit a 27-dim
  assembly; the structure paper's Scope (assembly) still says "code not deposited … read as unverified"); B8081 rebuilds ρ
  (Scope (2880) still says "not reconstructed"); B8082 computes the geodir H¹ count (Scope (geodir) still says "not
  computed"; unobstructedness genuinely still owed); B8079 closes B8078's ℚ̄ residue; B8119 closes the dynamical-E6 rows;
  B1162 dual-homes codex's height-308 witness (B1155/B1167 still say single-homed); B1181's 83/83 amphichirality
  supersedes B1165's vacuity worry; B1207 records the completed OA_SLOW run (B1177 says launched-not-complete); B1191
  closes GC-7; B8146/B8095/B8111/B8153 close the L173-precision, lane-6, Phase-0-item-0 and nine-words rows; B598 STEP 7
  re-derives the dial map (B582 "code NEVER COMMITTED"); B631 computes the matrix-level comparison (B629/B630 "never
  computed"); B662 L103 persists the golden σ* matrix (B660 "never persisted"); B792/B797/B1007 compute the m004 Maass
  eigenvalues (B735/B739 "Sage unavailable / no numerical E_m004"); B754 consults the scattering spectrum (B738 "zero
  kills"); B742 TOMB-L277 + B8081 for the 2880 enumeration; B775 P2W5-HERED executes B471's follow-up; B645 has
  ARTIFACT_HASHES.txt; LAW_MAP has §G method-laws (B1054); B1074–B1076 exist (B8084 relay); B767 ran 6 of 7 P3-depth kills;
  B1164's addendum registers time's arrow; B727/B743/B747/B748 ran their own "never run" tests.
- **Answered only off main, or contradicted there (10):** B1026_the_one_involution and B1030 (ONE continuous
  dimensionless input remains — contradicting B1025's "none" on main) on `origin/claude/new-session-qor5up`;
  B1039/B1043/B1045; the Maass degree-law / full window on `audit/b775-braver-questions`; B1162's cited
  `check_charge_bracket.py` on `origin/codex/seat-r001` and the structure-genesis head (so cloud's breaking_chains /
  susy_test could now be re-run; they were not).
- **A computed cell deleted from history, re-run, reproduced:** `frontier/B775_phase2_wave1/cells/_verify_Z1/` (the exact
  Z_k = Tr ρ_k(A1) ladder to k = 22, incl. Z_18 = 2 − √5), removed by c8f3167c as "accidentally-committed scratch";
  recovered and re-run in `recompute/R39_recovered_Z1_ladder/`: 21/21 shared levels agree. If the table is wanted, it
  belongs beside the Wave-4 correction as a results file.
- **STAND after direct check (16):** e.g. Regina not installed on this bench either; no f(n,d) for d ≠ 2; h(ℚ(√5)) = 1
  and the fundamental unit φ never computed in-repo (PARI here: bnfinit(x²−x−1).no = 1, .fu = −φ); 5₂ not fibered
  (Alexander 2t²−3t+2 non-monic); no `tests/test_b507*` on any of the 7 heads; `stage1_classes.pkl` on no head; B595's
  absent equivariant map is now B650's theorem (T = 0 uniquely); B8135's 2-vs-3 primitive-class count at m = 12: **both numbers are right about different equivalences** — the class group of
  discriminant 148 is ℤ/3, so 3 proper (SL(2,ℤ)) classes and 2 full (GL(2,ℤ)) classes (R42, corrected 2026-09-02 after my first
  version botched the improper identification; codex r010_gl_class_m12.py says the same). B8148's "settled at 3 under both
  SL(2,ℤ) and GL(2,ℤ)" is wrong for GL(2,ℤ); Paper I's remark should say which equivalence its table uses.
- The rest: 554 CONSISTENT, 132 NOISE, 29 GENERIC, 290 registry-only echoes; 224 claims the sweep could not test
  (DOC_ECHO / NO_HIT), 187 GENERIC by status.

## 7. Final state

Nothing still landing. Coverage 131/131 arc packets, 1310/1310 arc records, 11/11 log chunks, 14/14 test packets
(`campaign/phaseB/synthesis/coverage.md`); absence sweep 1535/1535 distinct claims. The one correction this note carries
against its own earlier drafts is the sweep-coverage one above (and the earlier B806→B778 attribution fix of 2026-09-02 01:00 UTC — an index-alignment error in the same tooling).
