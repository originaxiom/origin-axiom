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


**Added 2026-09-02 06:20 UTC (Phase C, R51/R52):**

| arc | verdict file says | the record / computation says | fix |
|---|---|---|---|
| B1181_amphichirality_closure (+ LAW_MAP §G row; B1163 addendum "83-of-83"; B1186 `amphichirality_failures: []`) | "83 OF 83 AMPHICHIRAL, zero exceptions … spot-verified 5/5 by the reliable mirror-isometry method (deliberately NOT isometry_signature)" | the method is `M.is_isometric_to(mirror)`, which SnapPy answers True for every orientable manifold (orientation-reversing isometries allowed) — the same vacuity as isometry_signature. By `symmetry_group().is_amphicheiral()` and the CS obstruction (2·CS ≡ 0 mod ½), **74 of the 112 family members are chiral (43 of the 77 all-regular)**, 36 of them provably by CS alone, including B1181's own spot-check o10_150700 (CS = −1/12). B1180's "UNCHECKED — an honest open" was the true state. R51 has the full table. | retract B1181's closure and its §G method-law row; re-scope B1163's family-wide W0 leg to the 34 amphichiral all-regular members; B1186 `amphichirality_failures` → 74 (43 in A); replace the instrument everywhere it appears (B1181, B1184, B1186 reproduce scripts) |
| B8070_anomaly_rank_descent | FINDINGS refutes the arc (commutator norms 2.83/12.73/86.27; cubic −2yL(2yL+3yd)(4yL−3yd)/3) | committed script still prints the refuted computation; the refutation's numbers have no code. The cubic factorisation reproduces exactly by sympy (R52); the norms are unscripted | ship the refutation's script |
| B1195 batch5a, GC-22 cell | q(S = φ⁻⁴) ≈ 1.5e−9 | the cell's own map q = e^{−2π/S} gives 1.98e−19 (its other two inputs reproduce to 6 digits) | correct the number (the exclusion only strengthens) |

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

## 2c. Phase E — the reader red flags, verified at the source (2026-09-02 07:10 UTC; `campaign/phaseE/IDENTIFICATION_LEDGER.md`)

390 flags of the four thesis-relevant kinds were checked against the arc/test/log text by agents (quotes, file:line)
and every UNCAUGHT one judged by the seat: SELF_CAUGHT 215 (the arc names and fences it — the record is better than
the flags suggested), UNCAUGHT 152, RETRACTED_LATER 11, FLAG_WRONG 8.

- **Verdict files contradicted by their own artifacts (fix = the verdict file):** B673 (`d2_results.json`:
  `all_gates_pass: false`, `koszul_antisym_holds_all_slots: false`; FINDINGS/verdict say clean, PROVED); B1082 (its
  own adversarial verifier: `holds: false`, 2 of 4 checks fail, the "no inversion" is a tautology any nested chain
  passes; banked PROVED with one of the two failures fixed and the other dropped); B1195 batch5a ("V4 PROVED trivial by
  direct computation" vs its own cell file's refutation: three "Reg copies" were identical vectors); B1213 (`_out.txt`
  80 % vs banked 89 %).
- **PROVED where the prose says otherwise (fix = verdict enum / scope note):** B232 (ρ_n plethysm — "an honest
  reduction, not a proof; terminal open lemma", PROVED; this one is on the tower spine), B59, B178, B233, B449 (a
  two-point "law"), B485, B665, B933.
- **Identifications carried as results on a type/number match (the T2 class, fix = fence or re-type):** B312 "one E6,
  three ADE hats" (shared Dynkin data is the definition of the label; no map constructed); B305 + B1042 "ω's ℤ/3 is
  the trinification/trit ℤ/3" (B323 and B1232 already cut it); B675 "SU(4)₁ IS the silver's stage"; B8071 "three routes
  point at the same object" (B8068's own cell: isomorphic, not conjugate); B897 lepton pattern from dims 3+6; B448
  third appearance of ℚ(√−7) (the arc's own promiscuity caution should win); B660 φ in the S-transform (forced by the
  shared SL(2,5) representation theory, zero evidential weight); B715 E6(ℂ) Chern–Simons "exactly 3d gravity"; B779
  six identities on hand-fixed literals; B1025 "canonical nomination" by ADE label.
- **"Verified on this bench" backed by grep-locks, not reruns:** B1162 (`reproduce.sh` greps a static
  `witness_sage.txt`), B1170 (only leg 1 runs), B1171 (marker greps). The seat's R46/R47 reruns are the only
  third-party executions of those certificates; cite them or ship the reruns.
- **Unscripted precision claims:** B1110 (1e−91 at N = 80 782), B1111 (layer-3 stabiliser orders), B208's 300 000 (true
  — R31), B485's m = 4, 5 (true — R43).
- **Narrative headings on computations (no observable content):** B760 "awareness without choice", B761 "no private
  states", B762 "quine"; B1169 places "awareness = mirror-even" in its solid core while its own fence calls it a chain.
- **Self-referential locks:** the complete list (≈ 80 test files) is in the ledger §D/§E; same class as Phase B §3.

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

## 8. Fresh-eyes addendum (R53, 2026-09-02) — for cc to re-apply by hand where it touches main

Computed, not delegated (`recompute/R53_field_vs_manifold/`):

| finding | bearing | where it lands |
|---|---|---|
| The route disc → N → SL(2,Z/N) → McKay emits only for N ∈ {1,3,5} (N ≤ 24 exhaustive, composites included) | on hyperbolic manifolds the image is {E6}; "hits the exceptional primes" is the instrument, not the object | B206 (extend "p ≤ 5" to composite conductors), B210 (restate "unique metallic mean"), B8118 (cite) |
| B208 reduces by the integer det(γ+I) = m²+4; B206/B8118 by the field discriminant | "unique at m = 1" holds only under the integer convention; the E6 side needs the field convention | B208 / LAW_MAP: state the convention once |
| Census 14/1200 labelled, all E6, indices 12/24/30 in PSL(2,O₋₃) | "m004 carries E6" ≡ "shape field Q(√−3)" ≡ "torsion-free finite-index subgroup of the Bianchi group" | B1136 scope note |
| Sister bit: det(A ∓ I) = (φ ∓ φ⁻¹)² = 1, 5; spin action of A and −A identical | B1136's sole separator H1 = Z is a Fibonacci identity of the trace-3 monodromy; B804's Arf machinery is blind to the bit | B1136, B197, B804 |

Owner election words carried verbatim from this session: "i was expecting you not to give up that easy and
try to see what were not seing because you have fresh eyes." The note `FRESH_EYES_2026-09-02.md` is the
seat's answer; nothing in it is banked to main by the seat.

## 9. Chirality and tracker sweep (Phases F/G, R54) — for cc to re-apply by hand

Owner election words carried verbatim: "before you conclude the chirality verdict, please sweep the repo because we dealt
with it, and get the results. regarding what the tracker dows to the world, we need to compute all possible options and
not lean on my intuition or opinion but on math."

Result: the record's settled position (B1163 theorem, B1168 parity law, B1169 naming, B1174 mirror = c, B1083 torsor
typing, B766 rank-3 lattice, B1164/B1166 two bits + one dilaton) STANDS and is reproduced by independent computation
(`recompute/R54_tracker_space/`). The complete list of tracker options is the character table of Sym(m004) = D4
(`campaign/phaseG/TRACKER_LEDGER.md` §1). Propagation defects (`campaign/phaseF/CHIRALITY_LEDGER.md` §2):

| # | where | what to change |
|---|---|---|
| F1 | B571 CHIRALITY_DOSSIER.md / REPORT.md; B572 | scope note: "breaks c" = "has mirror-odd data"; the sign is not the object's (B1163) |
| F2 | B532-I6 log entry, B571 item 5 | the 24-permutation check is not a conjugacy test; the language arrow holds for the 4-letter rule (R54d) and fails for the 2-letter rule; name the object |
| F3 | B1181, B1186 | replace `is_isometric_to(reverse_orientation)` with `symmetry_group().is_amphicheiral()`; R51 gives the corrected family counts |
| F4 | B723 arc_verdict.json; LAW_MAP B717 row | banner: chirality clause and torsor clause refuted (B942, B957) |
| F5 | B783 P16.2 | the letter complement is the C-type (mirror) bit, not γ5 (R54 §3, r54e) |
| F7 | docs/RETRACTIONS.md | carry the B723 refutations and B132's in-arc withdrawal |
| F8 | B582 FINDINGS:48-53 | wording: existence of a chiral construction, not a derivation of the hand |

## 10. The locking dictionary (R55) — a proposal, not a bank

Owner election words carried verbatim: "its not what i want but what reality choses" / "please build it".
`recompute/R55_locking_dictionary/DICTIONARY.md` maps B766's closing lattice to reality's measured signs under CPT
(exhaustive enumeration: three admissible dictionaries; c = P, γ5 = T is the testable one). Predictions P1–P4 and a
protocol are stated with their falsifiers; the chord sign (T6) has no physical reading in the record and is left as a
slot. For cc: if adopted, record the dictionary as a declared input (E1), and write the predicted sign of the leptonic
CP phase and of the EDM sign-pattern BEFORE those measurements arrive. The θ column and T3 identification in B766 remain
NOT re-derived by the seat.

## 11. Misstep note and the full object-level check (R56)

Owner election words carried verbatim: "the duty of this seat is not to be called on old banked data but to scrutinize
whatever exist prior … dont call on old data anymore" / "run a full check all you can".
`MISSTEP_2026-09-02.md`: the chain leaves the object at the shape field (step 3); steps 4–7 are functions of ℚ(√−3)
and of 2T = SL(2,𝔽₃); seat rule 3 proposed (compute an instrument's image before reading its output as the object's).
`recompute/R56_object_beyond_field/`: the 14 field-mates' object-level invariants (H1, cusp shape and subgroup growth
single out m004; 8 of 14 chiral), m004 vs m003 closings (every filling differs), the two gluing matrices and the two
deformation curves (verified), the DGG theories at the fork. For cc: the object-level restart, if elected, begins at
T[M]; nothing after step 3 should be written in the object's name.

## 12. The E6 → "SM structure" chain rebuilt from scratch (oa-distill `audit/AUDIT.md`) — for cc

Owner election words carried verbatim: "did you go all the chain to the sm structure all the way to before the values".
Rebuilt independently (e6 with Jacobi verified; principal sl(2); exact 2T action; centralizers):

| record | audit | status |
|---|---|---|
| B854: Cent(2T) = u(1)⁴ in degrees 8, 14, 16, 22 | same | reproduced |
| B874: Cent(C) = 12 (sl3 + centre 4); Cent(x8) = 30; the 26-stratum over the closure | same; the 26 = su(5)+2u(1) stratum is codimension 2 in C | reproduced |
| B892/B950: joint centralizer 14 = su(3)+su(2)+u(1)³ at a complex "wall point" | the 14-dimensional algebra is a codimension-ONE stratum: six hyperplanes of the 2T-torus; the record's pencils cross A3 strata (18) and the SO(10)+U(1) line (46), not a wall point | reproduced as a stratum; the "wall point" framing should be replaced |
| B950: "14 not 12; two U(1)s left" | rank theorem: centralizers of semisimple elements in e6 have rank 6; the 12-dim SM algebra (rank 4) is never a centralizer; the two U(1)s are forced by the method | structural, not a refinement |

Consequence for the record's language: "the second measurement yields the SM algebra" should read "a point on one of
six hyperplanes of the field-level torus has centralizer SM ⊕ U(1)², which is a Levi subalgebra of E6 in the standard
E6 ⊃ SO(10)×U(1) ⊃ SU(5)×U(1)² ⊃ SM×U(1)² pattern; nothing in the object selects the hyperplane". The seat does not bank
this; cc applies by hand.

## 13. "Higgs sector and 12 vs 14 solved in the repo?" — the record read whole, reconciled, two checks added — for cc

Owner election words carried verbatim: "highs sector and 12 vs 14 dimensions is solved in the repo, no? search all you
van about this provess because you should be upgrading the project not downgrading. read all unification docs yourself,
all mds please". Reading ledger: `READING_2026-09-02_unification_record.md` (every doc and arc, one line each).

Correction to §12 first: §12's phrase "the record does not have [a mechanism]" is withdrawn. The record caught 14 ≠ 12
(B950), proved the rank theorem (B952), named the missing piece (B964: the cascade is an adjoint Higgs mechanism; the
object lacks the rank-reducing 27 VEV) and computed two candidates (the 27-VEV route with its purity condition and
canonical lines, B1025/B1092, Route A open; the holonomy hatch, B1098–B1102/B1112/B1236). The seat's audit §1–§6 agrees
with B952 and adds the stratification.

Two independent checks (oa-distill `audit/A7`, `A8`, tests green):

| record | seat | result |
|---|---|---|
| B1098: A2 class → su(3)⊕su(3) (16, rank 4); A1 → su(6) (35, rank 5) | A8 on the seat's own e6 | reproduced |
| B1102: 18 exact hypercharge directions at the A2 landing, none colour-commuting; B1118: two S₃×S₃ orbits fused by the mirror, not the swap | A7 at the weight level (27 = (3,3̄) ⊕ 3·(3̄,1) ⊕ 3·(1,3)) | reproduced; side 2 has a one-line proof: a direction pure on one factor gives ≥ 9 zero eigenvalues, the target has 2 |

The reading the seat adds (a finding for cc to re-apply by hand, e.g. as an addendum beside B1102): with the exact Y, the
(3,3̄) nonet carries the lepton–Higgs charges, the 3·(3̄,1) carry q_{1/6} and D_{−1/3}, the 3·(1,3) carry d^c, D^c, u^c —
with the triple multiplicity as the colour index. So the exact hypercharge forces the *eaten* factor to be colour, broken
to the so(3) of its principal sl(2): **the A2 landing is trinification SU(3)_L × SU(3)_R with SU(3)_C → SO(3)_C; the
rank drop 6 → 4 is paid with colour, not with U(1)_ψ, U(1)_χ.** This answers B1102's follow-up (ii) (no colour inside the
centralizer can work) and, with B1098's table (only a₂⊕a₂ and the excluded b₃⊕u(1) have rank 4), follow-up (i): no
sl(2) stratum gives an unbroken su(3)_C ⊕ su(2)_L ⊕ u(1)_Y at rank 4. Follow-up (iii) (a 6Y frame map) is untouched.

Reconciled verdict (the seat's; nothing banked): 12 vs 14 is located and priced in the record, not solved — the record's
own sentence "two steps from the SM's own twelve, not zero" (THE_FRAMEWORK) and GUT ledger §D's "what no lane yet
supplies is the color-commuting product with the exact values" stand, now with the colour reading attached. The Higgs
representation (doublets in the 10 ⊂ 27; charge-forced Yukawa support, B884/B987) is derived structure, standard E6
content; the Higgs mechanism (GUT VEV point, doublet–triplet splitting, the ℙ³ line one condition short, ⟨H⟩ and m_H)
is external, part by theorem — as every hatch arc already fences ("EWSB remains outside").

Suggested wording for cc wherever the 14 appears (a finding, not an edit): "SM ⊕ U(1)² on one of six hyperplanes of the
field-level torus; rank 4 is reached by the object's holonomy only with colour broken; the SM product at rank 4 needs
the 27-VEV point, which the object does not select (B1225)."

## 14. R55/T07 corrected: the locking dictionary fixes no sign, relative or absolute — for cc

The seat tested its own R55 proposal (relay §10). Every quantity R55 said the dictionary fixes — the relative sign of two
K-type asymmetries (P1), of two W-type handedness signs (P2), of two EDMs (P3) — is a product of two signs of the same
CPT type, hence of type (ε_P, ε_C, ε_T) = (+,+,+), EVEN. EVEN quantities are dynamical and lie in the image of no
dictionary (checked in oa-distill T07). P1–P3 are withdrawn; P4 is CPT's own bookkeeping. The lattice-to-flips map
(rank 2 mod CPT; three admissible dictionaries) stands as mathematics; it predicts nothing about measured signs. If
R55's DICTIONARY.md §3 is ever cited on main as a prediction, this section is the correction.

## 15. T17: the beta-odd bit — the tree's one falsifiable particle-physics statement — for cc

After the owner's criticism ("you ais telling program doesnt have this or that and refusing to look"), the seat swept
the record for what the object actually outputs in the beta-odd sector. Found: B303 ("the CP sign is literally the sign
of Chern-Simons"), B1224 (amphichirality forces CS to 2-torsion: CS ∈ {0, 1/2} mod 1; m004 at 0, m003 at 1/4), B1226
(box D: beta-odd parameters {θ_QCD, δ_CKM, δ_PMNS} are the ONLY box where the object has an output; that output is CS,
one bit), L192 (the type-matched question in the beta-odd box — does the object's ℤ/2 fix the CP-conservation bit?
Never asked).

T17 (oa-distill `theorems/T17_beta_odd_bit.py`, tests green) computes:

1. The object's CS is odd under both c (cusp det) and γ₅ (H₁ sign), hence E-type in the dictionary.
2. Amphichirality (|Sym| = 8, four orientation-reversing) forces 2·CS ≡ 0 mod 1/2, confirmed numerically.
3. Under dictionary c = P, γ₅ = T (the A8 dictionary), the three object axes map to types: T4 (chirality) → W,
   T7 (time) → K, CS (absent odd-odd axis) → E.
4. SM dimensionless beta-odd parameters by type: θ̄_QCD = E (P-odd, C-even, T-odd); δ_CKM, δ_PMNS = K.
5. **Prediction:** θ̄_QCD ∈ {0, π}. m004 at CS = 0 → θ̄ = 0 (strong CP conserved). Weak CP phases are free bits.
6. **Bite:** of 594 chiral one-cusped census manifolds, exactly 1 (m004) sits at a 2-torsion CS value.

This is a different claim from the withdrawn P1–P3 (relative signs within a CPT family, proved empty). T17 is a
type assignment (E → θ̄_QCD) plus a value (2-torsion → {0, π}) from the object's own Chern-Simons. The distinction:
P1–P3 tried to fix *ratios* of same-type signs (all EVEN, so dynamical); T17 fixes a *type-to-observable* map and reads
off the object's single datum. The current bound |θ̄| < 10⁻¹⁰ is consistent but does not test it (it is also consistent
with dynamical relaxation).

Updated in oa-distill: PREREGISTRATION.md (T17 section), PHYSICS_CONTACT.md (C7 row), RECOMMENDATIONS.md, README.md.
