# INVENTORY: the physics seat, the codex seat, the hostile-review seat, against MAIN

Read-only inventory. No branch checked out, nothing modified. All content pulled with
`git show <ref>:<path>` / `git ls-tree -r --name-only <ref> <dir>`, or read directly from the pinned
worktrees named in the task. MAIN coverage checked from `origin-axiom` on `main`
(commit `c78003cd` at time of writing), via `git grep` and `docs/HARVEST_LEDGER.md`. Paths below are
relative to each worktree/branch root, not to this machine. No AI vendor named. Quoted text is
verbatim from the source named beside it; nothing is graded beyond the three-way
HARVESTED / CITED / ABSENT split the task specifies.

## Refs used

- **Physics seat** = `origin/physics-seat-evaluation-8dkbrl` (identical tip on
  `codeberg/physics-seat-evaluation-8dkbrl`), found via
  `git for-each-ref ... | xargs ... git ls-tree -r --name-only {} reports/fresh_physics_seat_2026-09-01`,
  which returned exactly this branch (both remotes, same commit). Files R56–R72 read directly from
  the pinned worktree `fc-seat-659487bb` (`git -C <worktree> rev-parse HEAD` = `659487bbd93c7990c4686a8b86985b6b66efedc4`,
  `git log -1 --oneline` = `659487bb R72: escape the |Fix| table header` — matches the commit named
  in the task).
- **Codex seat** = `origin/codex/seat-r001`, found by the same method (`MANIFEST.md` present,
  rows `R001`..`R040`). **Caveat:** the pinned worktree `codex-seat-r001` is checked out at
  `0b5429be` (`R022: type the three proposed V4 torsors`), an ancestor of the branch tip — its own
  `MANIFEST.md` only lists rows through `R023`. Rows `R024`–`R040` exist only at the branch tip
  (`f7a49536`, `R040: prove closed free-deck CS zero and exhaust cusped census`) and were read with
  `git show origin/codex/seat-r001:<path>`, not from the stale worktree. This is noted per-row below
  where it matters (it doesn't change any cell's content, only which copy supplied it).
- **Hostile-review seat** = `golden_gate/paper-hostile-review-alero0`, present directly as
  named in the task (no fallback search needed). Its own `session_handoff/MANIFEST.md` tables only
  memos **10–29** (Phase III); memos **1–9** (Phase II) are not in that table — they are listed,
  numbered, in `session_handoff/BANKING_HANDOFF.md`'s "THE MEMOS (phase II), in reading order"
  section instead. Both files are read and quoted below; this is flagged rather than silently
  patched over.

---

## 1. Physics seat — reports R56–R72

Source: `reports/fresh_physics_seat_2026-09-01/` in the pinned worktree. The seat's own "one line" /
"status" column below is quoted verbatim from `reports/fresh_physics_seat_2026-09-01/INDEX_R56-R72.md`
(all entries there say `**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06`, so that is not
repeated per row). MAIN coverage checked with
`git -C origin-axiom grep -l -E "fc:?R<nn>\b|R<nn> \(fc|physics seat.{0,40}R<nn>"` and a
broader `\bR<nn>\b` sweep for files that spell it out differently, cross-checked against
`docs/HARVEST_LEDGER.md`.

| id | title (first heading, verbatim) | seat's own verdict (INDEX status column) | scripts (`computations/`) | run output (`*_run.txt`) present |
|---|---|---|---|---|
| R56 | "R56 — THE ENDPOINT THEOREM: the record's seven chirality walls are one Euler characteristic, and the object has none because it is a knot" | "stands; §0's B915/V-3 lean retracted" | `r56_endpoint_theorem.py` | No |
| R57 | "R57 — THE THREE STRANDS: the object supplies three points, its closing erases them, and the record already holds every piece but the join" | "facts (1),(2),(4) stand; fact (3) **retracted** by R60" | `r57_three_strands.py` | No |
| R58 | "R58 — θ-PARITY COMPUTED: the object's three h¹ classes are all θ-even, the fiber carries a θ-odd sector of 6 and 10, and the closing is what removes it" | "computation stands as a fact about ι (the period-2 involution), **not θ** — see R60" | `r58_theta_parity.py` | No |
| R59 | "R59 — THE TWISTED CLOSING IS THE SISTER, AND IT KEEPS THE SAME EVEN LINE: no orientable closing of the fiber by the rule, twisted or covered, retains a θ-odd class" | "stands for ι; **void as a θ-statement** — see R60" | `r59_twisted_closing.py` | No |
| R60 | "R60 — CORRECTION: the record's θ is the meridian-reversing involution (B347/B353), not the fiber's −I; R57 fact (3), R58 §2–§4 and R59 are retracted as statements about θ" | "stands" | `r60_which_involution.py`, `r60_exact_conjugators.py` | No |
| R61 | "R61 — THE GEOMETRY OF θ ON THE OBJECT: a real structure on two fibers, two arcs pairing the cusp torus's 2-torsion points, and a lemma — every θ-equivariant abelian Higgs configuration has zero net chirality" | "stands with R69's banner" | `r61_theta_geometry.py`, `r61_fast.py` | No |
| R62 | "R62 — THE SYMMETRY GROUP ON THE CUSP, EXACTLY: the mirror is broken by every hyperbolic filling, the strong inversion by none — so no closing in the record's family ever breaks θ" | "stands with R69's banner" | `r62_cusp_actions.py` | No |
| R63 | "R63 — TWO sl₂'s, ONE HOLONOMY: after B1274 the record holds the principal (I-19 EARNED, the B347–B353 θ-grading) and the subregular (B1257/B1274) as *the* embedding of the object's SL(2), and they cannot both be it" | "open" | `r63_sl2_adjoint.py` | No |
| R64 | "R64 — THE FOUNDING RATIO FACTORS: on the golden E₈ the object's order-3 element is the family rotation TIMES an E₆ Weyl element — B1275's open step, answered by a type computation" | "stands (order-3-lift caveat stated)" | `r64_founding_ratio_type.py` | No |
| R65 | "R65 — THE 85 ARE TWO CLASSES: 40 of B1264's trinification gradings are trinification elements and 45 are not; the founding ratio's E₆ factor selects the 40" | "stands" | `r65_gradings_by_class.py` | No |
| R66 | "R66 — THE LIFT HAS ORDER THREE: w₃'s Tits lift in the exact e₆ is of order 3 with Ad-multiplicities (24, 27, 27) — the A₂³ class, no assumption left" | "stands" | `r66_tits_lift.py` | No |
| R67 | "R67 — AN EXACT e₈ AND THE THREE LIFTS: L_g, w_{A₂}, w₃ lift to order-3 elements of E₈ in the SU(9), E₇×U(1) and E₆×SU(3) classes — R64 §4 is now computed, not assumed" | "stands" | `r67_exact_e8_lifts.py` | No |
| R68 | "R68 — I-14 COLLAPSES TO A POINT: of E₆'s 40 trinification subsystems, exactly one is stable under the founding ratio acting from both sides" | "stands" | `r68_g_stable_a2cubed.py`, `r68b_selected_labelling.py` | No |
| R69 | "R69 — ARCS CUT CORNERS: Fix(θ) as a charge locus gives net = ±2, R61's θ-even clause is retracted, R56's "closed ⇒ zero" is scoped to smooth fields, and every filling closes the arcs back to χ = 0" | "stands" | `r69_arcs_cut_corners.py` | No |
| R70 | "R70 — WHAT THE TWO ARE TWO OF: the θ-even directions the object can carry a count on give vector-like spectra, and the 16 sits on the θ-odd direction where the count is zero" | "§1, §3 stand; §2 corrected by R71" | `r70_what_two_of.py`, `r70b_true_theta.py`, `frame_fast.py` | No |
| R71 | "R71 — THE SEATS ON THE CUSP: the SM seat's "no", main's parity theorem and this seat's ±2 are one picture; the θ-odd "no" is exact (region swap, no leading-mode assumption); R70 corrected — on the θ-even directions the ±2 is vector-like **or anomalous**, never a spectrum" | "stands" | `r71_seats_on_the_cusp.py`, `r71_theta_even_pairing.py` | **Yes** (`r71_seats_on_the_cusp_run.txt`, `r71_theta_even_pairing_run.txt`) |
| R72 | "R72 — THREE FROM THE THIRD ROOT: the lift of θ to E₆ is not unique (B353's own item (B)), the inner lift makes every direction even, and on the two-cusped tetrahedral manifold m202 — commensurable with m004 — the order-3 isometry fixes three lines: in the endpoint frame that is 3 × (16 ⊕ 10 ⊕ 1) of SO(10)" | "frontier, stands" | `r72_inner_lift.py`, `r72_m202_snappy.py`, `r72b_m202_lines.py`, `r72c_d2_is_the_so10_axis.py`, `r72d_census_menu.py` | **Yes** (one `*_run.txt` per script above) |

### Retraction / supersession marks in R57–R60's own text (as required), plus the R61/R62/R69–R72 chain

- **R57** carries its own **"RETRACTION BANNER (R60, 2026-09-06)"**: *"fact (3) below — that θ fixes
  the three half-periods — is **withdrawn**. The record's θ (B347/B353) is the meridian-reversing
  strong inversion, whose fixed set is two arcs; the three half-periods are the fixed points of the
  meridian-preserving period-2 involution ι, a different symmetry."*
- **R58** carries **"RETRACTION BANNER (R60, 2026-09-06)"**: *"the involution computed here is the
  fiber's −I (the period-2 symmetry ι), **not** the record's θ. ... §2's headline, §4's "settles" and
  "opens" are **withdrawn** as statements about θ."*
- **R59** carries **"RETRACTION BANNER (R60, 2026-09-06)"**: *"the twist here is by the period-2
  involution ι, **not** the record's θ ... every use of the word θ in this report is **withdrawn**."*
- **R60** is itself titled **"CORRECTION"** and opens with *"# R60 — CORRECTION: the record's θ is
  the meridian-reversing involution (B347/B353), not the fiber's −I; R57 fact (3), R58 §2–§4 and R59
  are retracted as statements about θ"*, followed by a section "0. What I got wrong, and how."
- Later chain (beyond R57–R60, listed for completeness since it's the same retraction thread): **R61**
  carries a **"RETRACTION BANNER (R69)"** withdrawing its θ-even net-zero clause; **R62** carries a
  **"CORRECTION BANNER (R69)"**; **R69** itself retracts R61's clause and scopes R56; **R70** is
  corrected at source by R71 (banner in R70 §2); **R71**/**R70**/**R69** §4/§2/§3 are in turn scoped
  to "the outer lift" by **R72**'s own banner.

### MAIN coverage, R56–R72

`git grep -l -E "fc:?R<nn>\b|R<nn> \(fc|physics seat.{0,40}R<nn>"` against `docs frontier` returned
**zero files for every R56–R72** — none of these reports is cited in that exact shorthand anywhere on
main. Broadening to a plain `\bR<nn>\b` sweep (still scoped to `docs` and `frontier`) plus
`docs/HARVEST_LEDGER.md` finds real content for most of them, quoted below.

| id | MAIN coverage | evidence |
|---|---|---|
| R56 | **HARVESTED** (independent re-derivation, credited) | `frontier/B1293_seat_harvest_2026-09-06/FINDINGS.md`: *"fc's R56 derived `net chirality = χ(M, ∂⁺M)` — with *"zero on any closed 3-manifold, zero for a knot"* and *"the record's seven chirality walls are one theorem"* — before main's B1290. B1290 and B1291 are **independent confirmation and extension**, not discovery."* |
| R57 | **ABSENT** | zero hits for `R57` anywhere in `docs/` or `frontier/` |
| R58 | **ABSENT** | zero hits |
| R59 | **ABSENT** | zero hits |
| R60 | **ABSENT** | zero hits |
| R61 | **CITED**, explicitly marked not re-verified | `frontier/B1277_leak_closure/arc_verdict.json`: *"HARVEST, not re-verified: physics-seat R61 (a real structure on the fiber, the cusp lattice Z + Z(2+4w) exactly, and the LEMMA that theta-equivariant abelian Higgs configurations have ZERO NET CHIRALITY ...)"*; `frontier/B1290_the_index_formula/arc_verdict.json`: *"NAMED CANDIDATE, harvested and NOT verified here: fc's R61/R62 ..."* |
| R62 | **CITED**, explicitly marked not re-verified (same sentence as R61 in both sources above) | same two files; also `frontier/B1293_seat_harvest_2026-09-06/FINDINGS.md` §6: *"fc's **R61** says ... **R62** says ... **Different spaces — not a contradiction.**"* |
| R63 | **HARVESTED** (verified, one premise corrected) | `frontier/B1277_leak_closure/FINDINGS.md` title: *"B1277 — LEAK CLOSURE: fc's R63 verified (one premise corrected) ..."*; body: *"Every R63 claim is recomputed on main's own data, not accepted; the one that fails is reported as failing rather than smoothed."* |
| R64 | **ABSENT** | zero hits |
| R65 | **HARVESTED** | `frontier/B1293_seat_harvest_2026-09-06/verification/harvest.py` / `arc_verdict.json`: *"CONFIRMED HERE from structure alone: fc R65/R68's 120 A2 and 40 A2^3 subsystems of E6 (matching \|W(E6)\|/\|W(A2)^3 x S3\| = 51840/1296)"* |
| R66 | **HARVESTED** | `frontier/B1293_seat_harvest_2026-09-06/FINDINGS.md`: *"fc's collapse reproduces on this bench with no icosian construction. R65/R66 identify the element as lying in the **A₂³ class**, and that class is realisable directly in W(E₆) ..."* |
| R67 | **ABSENT** | zero hits |
| R68 | **HARVESTED for the labelling claim; explicitly NOT for the collapse claim** | `arc_verdict.json`: *"CONFIRMED HERE from structure alone: ... fc R68's selected labelling c = (1,0,2,2,0,2) grading the 27 as 9+9+9 ..."* — but the same arc's `verification/harvest.py` prints: *"NOT VERIFIED HERE, and fenced as harvest: R68's icosian 4 -> 1 collapse (needs their rebuilt ..."* |
| R69 | **HARVESTED** | `frontier/B1296_the_charge_locus_parity_lock/arc_verdict.json`: *"the sign pair is the closer's (fc R69 sec. 4 confirmed by symmetry)"*; `frontier/B1294_the_chirality_bit/arc_verdict.json` lists *"fc:R69 -- Fix(theta) as charge locus gives net +-2 or 0 ..."* among "THE SEATS' RESULTS FIRST" and re-derives the surrounding geometry independently |
| R70 | **HARVESTED** (corrected/sharpened, not simply cited) | `frontier/B1296_the_charge_locus_parity_lock/arc_verdict.json`: *"CORRECTION to fc R70 (sharpening; HOLD): 'theta-even => 2(R+Rbar) vector-like' holds on 11 of 15 F_4 faces and FAILS on 4 ... R70's conclusion survives strengthened"*; also `docs/HARVEST_LEDGER.md` row 7 ("R70 §2 corrected at source") |
| R71 | **HARVESTED (VERIFIED)** | `docs/HARVEST_LEDGER.md` row 7: *"**VERIFIED** — scripts re-run in the pinned worktree (`fc_r71_*_rerun.txt`, `fc_r72c_*_rerun.txt`); the dichotomy is B1296's spectral half, credited there at landing"* | B1298 | 2026-09-08 |
| R72 | **HARVESTED (mixed VERIFIED/REGISTERED/SCHEDULED)** | `docs/HARVEST_LEDGER.md` rows 1, 2, 3, 4, 24 — row 1: *"**VERIFIED** — inner lift: 32 fixed roots, A₅⊕A₁, all of 𝔥; outer: 24, F₄ ..."*; row 3: *"**REGISTERED** — I-28 UNEARNED"*; row 4: *"**SCHEDULED** (r72c re-run in B1298: see row 7)"*; row 24: *"**VERIFIED** for the geometry ... the count 3 × (16 ⊕ 10 ⊕ 1) is PW's localized count under fc's two named choices ... — recorded as fc records it, not re-derived as a spectrum"* |

---

## 2. Codex seat — cells R001–R044 (`MANIFEST.md`)

`MANIFEST.md`'s own table (branch tip `f7a49536`) runs **R001 through R040**, reaching **44 rows**
only by counting lettered sub-cells (`R029A`, `R031A`, `R031B`, `R031C`, `R031D`) — there is no
`R041`–`R044`. **`R032` does not appear as a row at all**; `R031C`'s own claim text says why:
*"R032 deliberately withheld pending characteristic-zero adjudication."* The "title" column below is
the manifest's own "narrow claim" text verbatim (codex cells do not carry a separate prose heading
the way the physics-seat reports and hostile-review-seat memos do — the certificate path plus this
claim sentence is the manifest's whole row). MAIN coverage was checked two ways: the task's own
`codex ?R0nn|R0nn \(codex` pattern (only **R017** and **R019** match that literal shorthand), and a
broader `\bR0nn\b` sweep of `docs/` and `frontier/`, which is what most rows below are sourced from.

| id | title (MANIFEST claim, verbatim) | certificate/script | MAIN coverage |
|---|---|---|---|
| R001 | "independent closure audit and heterotic-route state" | `documents/codex-seat-r001.md` (doc, no script) | ABSENT |
| R002 | "delta-driven closure-campaign protocol" | `documents/codex-seat-r002-masterplan.md` (doc, no script) | ABSENT |
| R003 | "all 11 accepted odd rows pass the selected-beat identities; beat selects none" | `documents/codex-seat-r003/verify_cp1_all_odd.py` | **HARVESTED** — "the fourth bench (codex R003) re-verified memo 30 byte-identical + an all-11-odd-rows extension" (`docs/CAMPAIGN_STATUS.md`; `frontier/B1148_carrier_harvest/`) |
| R004 | "Wave-3 108-question map checkpoint" | `documents/program-question-map/validate.py` | ABSENT (manifest itself marks it "SUPERSEDED BY R015") |
| R005 | "clean `main@9d6979db` omits the `reproduce.log` required by its B1147 lock" | `certificates/check_b1147_lock.py` | ABSENT |
| R006 | "exact E6/27 symmetric and ordered invariant multiplicities; fixed-linearization cubic covariance" | `certificates/r006_e6_invariants/{jordan_beat,tensor_invariant_counts}.py` | **CITED only** — appears solely as a dependency need in `frontier/B1201_lee_verified_and_harvest/verification/cells.json` ("R020 needs R006's vendored e6 builder"), not verified as its own content |
| R007 | "even labels imply even omega-one grade for integral E6 characteristics; census completeness stays separate" | `certificates/oa_c1070_omega1_parity.py` | ABSENT |
| R008 | "the full Riley-component deck involution sends kappa to tr(ab^-1); the constant 3-kappa formula is parabolic only" | `certificates/r008_peripheral_sheet_conjugacy.py` | ABSENT |
| R009 | "B1153's relative D improvement reproduces dependency-free; it supports an empirical Wigner-surmise renewal model, not exact GUE independence" | `certificates/r009_c4_superposition/superposition_stdlib.py` | **HARVESTED** — "corroborated by codex R009" (`frontier/B1158_cloud_wave2_harvest/FINDINGS.md`) |
| R010 | "Paper I's m=12 discrepancy is 3 proper classes versus 2 full GL classes; the m=6 threshold survives" | `certificates/r010_gl_class_m12.py` | **HARVESTED** — "**R010** Paper-I m=12 GL class-count bug resolved (threshold m=6 unchanged)" (`docs/CAMPAIGN_STATUS.md` / `docs/views/VERDICT_LEDGER.md`) |
| R011 | "Paper III's exact dictionary is an M-character identity for k>=3; n=2, no-finite-torsion and full-cusped-gravity upgrades do not follow" | `certificates/r011_ruelle_scope.py` | **HARVESTED** — "codex R011 Ruelle fence CORROBORATES our B1157 dynamics_null -- two seats, same infinity-point" |
| R012 | "fixed D5/bridge frames give the exact 40+5 cubic support and distinct parities; U(1)_psi naming and physical dark-sector fences restored" | `certificates/r012_dark_ledger_scope.py` | **HARVESTED** — "codex R012 dark-ledger == cloud ANOMALY_PAYMENT -- apparent conflict dissolves at scope" |
| R013 | "torality plus the single explicit E6 A2 Weyl orbit transfers the charged C to the exact 109-flat/11-value Qbar arrangement" | `certificates/r013_rung_transfer.py` | **HARVESTED** — "**R013** Paper-II Q̄ rung closed (conditional on the principal 2T embedding)" (`frontier/B1158_cloud_wave2_harvest/FINDINGS.md`) |
| R014 | "normalized volume refutes the literal scale theorem; exact s955 gluing refutes the exhaustive 14-member family" | `certificates/r014_paper4_counterexamples.py` | **HARVESTED** — "**R014** Paper-IV **both literal claims REFUTED** (the scale theorem by its own normalized-volume counterexample ...; the exhaustive-14-family claim by witness **s955** ...)" |
| R015 | "Wave-4 canonical 120-question map; four explicit live computations; latest main/outside/paper refs reconciled" | `documents/program-question-map/validate.py` | **HARVESTED (partial/"adopted")** — "codex R015/R016 -- two adoptions: B1153 grade-note ('exact 2-fold GUE' bounded to the verified scope p in {5,7}, r in {1,2}, order <= 8..." |
| R016 | "compatible cube-root embedding repairs the four tested zeta-three Habiro tables; universal/local-valuation upgrade remains unproved" | `certificates/r016_habiro_zeta3_embeddings.py` | **HARVESTED** — "R016 performed the computation B1158 stated but didn't ship" |
| R017 | "exact height-308 up-Yukawa zero and same-monad exact-one-Higgs repair no-go are now branch-local" | `certificates/r017_yukawa_primary/verify_yukawa_{cup_product_308_scope,exact_spectrum_no_go}.py` | **HARVESTED** — literal `codex R017` match in `docs/RELAY_LEDGER.md`, `docs/views/VERDICT_LEDGER.md`, `frontier/B1167_seat_harvest/arc_verdict.json`, plus further use in `B1171_seam_harvest`, `B1185_yukawa_three_mechanisms`, `B1212_two_replies` |
| R018 | "Wave-5 canonical 154-question map; eleven explicit live questions; main through B1168 plus current outside/paper/Golden refs reconciled" | `documents/program-question-map/validate.py` | **CITED only, re: a numbering question, not content** — `frontier/B1171_seam_harvest/FINDINGS.md`: *"**R018 numbering gap** (R017→R019, no R018 anywhere — asked, not assumed lost)"* (manifest itself marks R018 "SUPERSEDED BY R023") |
| R019 | "selected trinification frames realize the universal anomaly-ratio theorem; frame, physical spectrum, gauging and normalization remain unselected" | `certificates/r019_hypercharge/hypercharge_trinification_scope.py` | **HARVESTED** — literal `codex R019` match in `frontier/B1170_arena_rescope/verification/reproduce.sh`; further use across `B1171`, `B1172`, `B1175`, `B1194` |
| R020 | "on the source-locked B1140 compact-color representative, the principal semilinear beat does not preserve the Killing-orthogonal 64 or any of its three named summands" | `certificates/r020_beat64/r020_beat64_principal.py` | **HARVESTED** — `frontier/B1175_charter_close_harvest/FINDINGS.md`: "## The codex trio — verified on this bench (all byte-identical)" ... "Σ² = Ad(meridian) verified on all 78 basis inputs"; independently re-run again in `frontier/B1201_lee_verified_and_harvest/verification/cells.json` ("ran in 32.0s, exit 0, `diff` ... = BYTE-IDENTICAL") |
| R021 | "m000 has two Pin-minus structures whose restrictions to m004 coincide in one unnamed spin structure; identifying that image with B1141 remains open" | `certificates/r021_gieseking_pinminus/gieseking_pinminus_restriction.py` | **HARVESTED** — same `B1175`/`B1201` re-runs as R020 ("the restriction is **CONSTANT**"); also `frontier/B1208_cross_seat_harvest/verification/verify_r021.py` |
| R022 | "regular four-point V4 actions agree abstractly; field-annotated branch and being-by-hearing actions separate conditionally; the original three-way named claim remains ill-typed/open" | `certificates/r022_v4_torsors/v4_named_action_audit.py` | **HARVESTED** — same B1175/B1201 re-runs; `frontier/B1182_c4prime_resolved`: "R022's convention fence ABSORBED"; B1201: "DISPOSITION: ADOPT (R022 CONFIRMS/is-consistent-with B1182)" |
| R023 | "Wave-6 canonical 185-question map plus exact outside-tip hostile checks, the B1196 `16` versus `9+9+9` carrier obstruction, B1197's full-census clock negative and B1199's 745-class selection recheck; main through B1209, outside `287e8f75` and paper `a31456d2` reconciled" | `documents/program-question-map/validate.py`; `certificates/r023_wave6_outside_hostile.py`; `r023_b1196_generation_obstruction.py`; `r023_b1197_clock_coherence.py`; `r023_b1199_selection_recheck.py` | **CITED, with an apparent numbering mismatch flagged, not resolved here** — `frontier/B1205_the_dimension_ledger/FINDINGS.md`: "the tensor entries are not banked (the 𝒯 char-0 evaluator remains commissioned to codex, R023)"; `frontier/B1206_one_condition_short/FINDINGS.md`: "exactly a datum codex's commissioned 𝒯 evaluator (R023) would settle"; `frontier/B1212_two_replies/FINDINGS.md` (later): "the 𝒯 evaluator's own territory (R023), still uncommissioned in its load-bearing half." These three main citations describe an R023 that is a *pending* char-0 tensor evaluator — a different task from the manifest's actual R023 (the Wave-6 question map). Read-only note only; not adjudicated here. |
| R024 | "both retained height-308 branches place `e^c` and `l` in coarse character zero; its use of the `A7` tail rule for the lepton discussion is superseded by R025" | `certificates/r024_lepton_character_datum.py` | **HARVESTED** — `frontier/B1212_two_replies/verification/r024_lepton_character_datum.py` + `r024_rerun.txt` (dedicated re-run) |
| R025 | "the lepton raw leg is `A11`, so its B-pair sum is 4 rather than 8; the physical `B2 x B2` pure-tail term is the alternating square of one tail line and vanishes, while all mixed/connecting entries remain open" | `certificates/r025_lepton_tail_selection/lepton_tail_selection.py` | **HARVESTED** — `frontier/B1217_seat_integration/FINDINGS.md`, under "## VERIFIED ON THIS BENCH": "**codex R025 — independent confirmation of B1215.** They certify the same law this bench derived separately" |
| R026 | "exact ordered Euler eigenframe, determinant comparison and sparse local connecting formula for the norm-308 down/lepton evaluator; the `H3(O_Y)` trace and Serre tails remain open" | `certificates/r026_yukawa_determinant_frame/determinant_frame.py` | **HARVESTED** — same B1217 section: "**codex R026 — the determinant frame.** Their certificate runs here with output identical to theirs" |
| R027 | "exact marked `H2(K_dP6)` class and cyclic dual trace, with a normalized 384-simplex product trace on the 36-chart cover of `dP6 x dP6`; the hypersurface connecting image and Serre tails remain open" | `certificates/r027_toric_top_trace/toric_top_trace.py` | **HARVESTED** — same B1217 section: "**codex R027's simplification — confirmed, and it matters.** ... **384 confirmed here**" |
| R028 | "exact all-chart ray ordering, common Laurent frames, `C12` chart action and 18/18 residue-orientation census; characteristic-zero `Phi`/Bezout data remain open" | `certificates/r028_toric_chart_frames/toric_chart_frames.py` | **CITED** (used as a methodological template, and separately as a scope fact, not independently re-run for its own claim) — `frontier/B1219_reverse_sweep/FINDINGS.md`: "the form codex's R028 certificate uses"; `frontier/B1220_campaign_premise_audit/FINDINGS.md`: "codex R028 pinned the frame layer but claims no Yukawa entry" |
| R029 | "Wave-7 canonical 186-question map; main through B1217 and outside last-chain reconciled, including the newly typed L173 distinctive-differential refutation" | `documents/program-question-map/validate.py`; `evidence/PROGRESS_BANK_2026-08-30_WAVE7.md` | **CITED** — `docs/ERROR_LEDGER.md` (E53 row): "codex's R029 independently re-derived, ten days later, a negative main had banked at B1095 and not surfaced where they would meet it" (documents the relationship; not a re-run of R029 itself) |
| R029A | "B1218/outside-memos-156–157 hostile reconciliation: Gate C closes on one-carrier conjugacy, B632 cell 2 was already run and does not yield generations, Gate D's sign is unselected and its finite masks have exact dimension two; canonical map expanded to 192 questions" | `certificates/r029_upstream_hostile_corrections.py`; `documents/program-question-map/validate.py`; `memos/QUESTION_MAP_WAVE8.md` | ABSENT (no `R029A` token anywhere in `docs/` or `frontier/`) |
| R030 | *(see flag below, ≤40 words)* | `certificates/r030_phi_cover_specialization/phi_cover_specialization.py`; `memos/YUKAWA_PHI_COVER_SPECIALIZATION_308.md` | **CITED, and superseded-in-status by the time main used the number** — main's own text calls it "in flight," not landed: `frontier/B1220_campaign_premise_audit/arc_verdict.json`: "STATUS: BLOCKED ON CODEX R030's IN-FLIGHT characteristic-zero Yukawa computation -- a scheduling fact, not a mathematical gap." No later main text was found re-verifying R030's actual delivered content (the GF(1009) unit identities). |
| R031 | *(see flag below, ≤40 words)* | `certificates/r031_sparse_toric_trace/sparse_toric_trace.py`; `memos/YUKAWA_SPARSE_TORIC_TRACE_308.md` | ABSENT for the bare `R031` token (main only ever cites the lettered sub-cells `R031A`/`R031B`, below) |
| R031A | "C-2 exact retrieval: after passage to a splitting field `B_0=4 chi_0`, so the generator acts by `I_4`; a primitive scalar rank-one module has the distinct orbit `chi_1+chi_5+chi_7+chi_11`, and the physical Higgs-line space remains `P^3_C`" | `certificates/r031a_b0_character_field/b0_character_field.py` | **HARVESTED** — `frontier/B1232_codex_r031_verified_and_three_columns/FINDINGS.md` title: "CODEX R031A/R031B VERIFIED, THREE RETRACTIONS, AND A THIRD COLUMN"; body: "codex's certs were **re-run on this bench**"; "`r031a`, re-run here: `B_0 generator exponents = (0,0,0,0)`; C12 acts by **I₄** ... Controls bite" |
| R031B | "primary-literature hostile audit: RCFT rationality is conditional and not finiteness; complex `PSL(2,C)` m004 has no established finite RCFT boundary; MMS is `(2,0)`-scoped; trace-field Galois `Z/2`, trinification `Z/3` and fusion `Z/3` are untyped; the post-send Q11 scope is reconciled; sigma remains open" | `certificates/r031b_rcft_scope/rcft_scope.py` | **HARVESTED** — same B1232 arc: "Codex's `r031b` cert, re-run here: *"rationality alone permits arbitrarily large finite subsets of (0,1) and rational midpoints"* — **PASS**" |
| R031C | "Wave-9 canonical 201-question map: B1221--B1230, R031A/R031B and Q11 reconciled into 9 new propositions with 26 live OPEN rows; R032 deliberately withheld pending characteristic-zero adjudication" | `documents/program-question-map/validate.py`; `memos/QUESTION_MAP_WAVE9.md` | ABSENT |
| R031D | "exact `identify or descend` parameter rule: a one-dimensional quotient and vanishing on `wedge^2 C` make the mixed observable independent of all lift choices; raw `P^3` presentation dimension is not automatically three physical parameters" | `certificates/r031d_observable_quotient/observable_quotient.py` | ABSENT |
| R033 | *(see flag below, ≤40 words)* | `certificates/r033_identification_ratchet/{identification_ratchet.py,source_snapshot.json}` | **CITED only, as a pending/OPEN item** — `docs/FRESH_EYES_2026-09.md`, Q2: "I-13 (the listener map) is the top debt on three surfaces and has never been attempted... \| Phase 4 (7) / **B1306 (codex R033)** \| OPEN". (Note: `B1306` there is this very arc's own number — i.e. main has already flagged codex R033 as unresolved work for this branch, not adjudicated it.) |
| R034 | "Phase-C adjudication preserves B1141/B1145 and B359--B364 internally but types two missing physical maps as legacy UNEARNED identifications: internal odd-A1 lift to 4d Lorentz spin, and boundary theta polarization to beat-selected bulk/observer spin" | `certificates/r034_spin_identifications/{spin_identification_audit.py,source_snapshot.json}` | **HARVESTED** — `frontier/B1235_two_seat_harvest/FINDINGS.md`: "Sources: ... codex R034/R036 (`origin/codex/seat-r001` @ `4ec3e07f`)"; "## Identifications (I-10, I-11; codex R034)" — tracked as an identification-ledger source, not merely mentioned |
| R035 | "the correct mixed-dual `27=(15,1)+(bar6,2)` makes the lifted A1/SU6 route an exact full joint SM-shaped-27 match at `Y6=diag(-1/3^3,1/2^2,0)`; charge-only and external/diagonal-weak controls bite; A1 selection, extra-U1 breaking and every physical bridge remain open" | `certificates/r035_a1_su6_sm_branching/{a1_su6_sm_branching.py,source_snapshot.json}` | **HARVESTED** — `frontier/B1236_a1_landing_exact/verification/a1_su6_branching.py` (dedicated re-run script) |
| R036 | "fresh-main hostile audit: B1233's origin is a strict local, not global, minimum on `R^3`; arithmetic can define continua; B1234's 40/40, cover-isometry and 48/48 cores stand, but its amphichirality-to-all-walls arrow contradicts B1224/B1226 and its physical-E6/map-inheritance join remains uncomputed; two ledger drifts identified" | `certificates/r036_fresh_main_scope_audit/{fresh_main_scope_audit.py,source_snapshot.json}` | **HARVESTED** — `frontier/B1235_two_seat_harvest/verification/a6_cover_cs.py`, `markoff_box_minimum.py` (dedicated re-run scripts); cited as one of the two sourced seats in that arc's header |
| R037 | "exact map-level correction to B1234: the 48 m000 surjections restrict two-to-one onto 24 of m004's 48, so exactly one of two `Aut(2T)` quotient classes extends; the other is the central `H^1` twist; no spin/ALE/physical-E6 identification" | `certificates/r037_a6_2t_restriction/{a6_2t_restriction.py,source_snapshot.json}` | **HARVESTED** — `frontier/B1238_seat_harvest_40a3_bronze_octic/verification/r037_verify.py` (dedicated re-run) |
| R038 | "the R035 A1 route contains a Y-neutral `bar6` component whose SU6-gauge stabilizer is exactly SU5 (rank 5->4); full-product stabilizer instead has algebra u5 (E6 image U5/C2) with a diagonal U1, and one decomposable VEV is not D-flat; zero mode, VEV selection and physical matter map remain open" | `certificates/r038_a1_rank_reduction/{a1_rank_reduction.py,source_snapshot.json}` | **HARVESTED** — `frontier/B1238_seat_harvest_40a3_bronze_octic/verification/r038_verify.py` (dedicated re-run) |
| R039 | "projection through `2T->A4` makes the m000-to-m004 restriction bijective on the single 24-map A4 quotient class; every A4 map has two finite Spin3 lifts, exactly one cover lift extends, and the parent H1 bit restricts to zero; no tangent/internal/4d spin identification" | `certificates/r039_a4_2t_lift_torsor/{a4_2t_lift_torsor.py,source_snapshot.json}` | **HARVESTED** — `frontier/B1238_seat_harvest_40a3_bronze_octic/verification/r039_verify.py` (dedicated re-run) |
| R040 | "free orientation reversal forces full `cs=0 mod 1` for closed hyperbolic 3-manifolds by Kawauchi plus APS/CGHN; all 1260 SnapPy nonorientable cusped orientation covers are numerically `cs=0 mod 1/2`, but the universal cusped theorem remains open" | `certificates/r040_free_deck_cs/{free_deck_cs.py,source_snapshot.json}` | **HARVESTED** — `frontier/B1239_quarter_class_is_cusp_local/verification/{r040_census_rerun.py, r040_closed_control.py, r040_quarter_is_a_cusp_phenomenon.py}` (three dedicated re-runs); also `frontier/B1238_seat_harvest_40a3_bronze_octic/`, `frontier/B1273_seat_harvest/`, `frontier/B1293_seat_harvest_2026-09-06/` |

**R041–R044 do not exist.** `origin/codex/seat-r001`'s `MANIFEST.md` tip is `R040`; there is no
`R041`, `R042`, `R043` or `R044` row, script, or memo anywhere in the branch.

### R030, R031, R033 — flagged explicitly, headline claims quoted verbatim (≤ 40 words)

- **R030**: *"exact GF(1009) unit identities for the same four Phi components on all 36 toric charts
  plus proper-image closedness prove a four-open principal cover over Q(zeta12); explicit trace
  collapse and Serre tails remain open"* (33 words, `MANIFEST.md`).
- **R031**: *"exhaustive exact support search finds the minimum normalized dP6 trace (four
  triangles), proves it homologous to R027 and reduces the product contraction from 384 to 96
  simplices"* (27 words, `MANIFEST.md`).
- **R033**: *"B1231 admits an unpriced listener identification absent from its seven-row ledger; its
  green two-UNEARNED count is therefore a seed state, not a completed census, and registering legacy
  debts requires the gate's documented dated baseline migration; six SM-load-bearing Phase-C
  candidates are..."* (first 40 words of a 45-word claim, `MANIFEST.md`; truncated here only for the
  word cap, not edited).

---

## 3. Hostile-review seat — memos #1–21

Branch used: `golden_gate/paper-hostile-review-alero0` (present directly, exact name match —
no fallback search needed). **Sourcing caveat, stated plainly:** the branch's own
`session_handoff/MANIFEST.md` tables only memos **10–29**; memos **1–9** are not in that table at
all. They are numbered and described in `session_handoff/BANKING_HANDOFF.md`'s section "## THE
MEMOS (phase II), in reading order," which is where rows 1–9 below are sourced from. Titles are the
first Markdown heading (`#`) of each memo file in `session_handoff/memos/`. "Status marks" are quoted
from whichever of the two files actually carries a status for that memo (`MANIFEST.md`'s `2B`/`1B`/
`RT`/`NEG` column for 10–21; `BANKING_HANDOFF.md`'s prose for 1–9, which does not use that same
code).

| # | memo file | title (first heading, verbatim) | status mark (quoted) |
|---|---|---|---|
| 1 | `JORDAN_MEMO.md` | "THE JORDAN MEMO — the pattern above the patterns (outside bench, 2026-08-21)" | not coded 2B/1B in `MANIFEST.md` (memo predates that table); `BANKING_HANDOFF.md`: "forced = semisimple/class-function/closed-orbit, free = unipotent/frame/torsor; nine-result audit; NEW VERIFIED: the t-meter ... Cells C-J1..3." |
| 2 | `PROJECTIVE_HATCH.md` | "THE PROJECTIVE HATCH — the object's unlifted geometry selects the trinification landing" | `BANKING_HANDOFF.md`: "the spin-bit repricing ... hatch price 4.3 → ~2.6 bits, 0 SM-facing. Cross-checked against B1098/B1100 banked numbers." |
| 3 | `LORENTZ_ON_THE_DOUBLE.md` | "LORENTZ ON THE DOUBLE — where the 3+1 signature actually lives, and what it costs" | `BANKING_HANDOFF.md`: "VERIFIED: two commuting A2-class triples with joint commutant exactly one su(3) (color) ... the gravity/EW double-duty competition." |
| 4 | `SPENDING_ORDER.md` | "THE SPENDING ORDER — the hatch DAG, the cosmological match, and what the 27 is in the gravity reading" | `BANKING_HANDOFF.md`: "NEW VERIFIED: the 27's joint bi-weight table {(±2,±2):1,(±2,0):4,(0,±2):4,(0,0):7} exact ... no half-integer spin anywhere." |
| 5 | `ASYMPTOTIC_CHANNEL.md` | "THE ASYMPTOTIC VALUE CHANNEL — the archimedean door is open, and the action is a growth rate" | `BANKING_HANDOFF.md`: "VERIFIED: Vol extracted from the Kashaev tower to 6.5×10⁻¹¹, power 3/2, constant 3^{−1/4}." |
| 6 | `DEFLATION_RUN.md` | "THE DEFLATION RUN — three cells executed: the last hypercharge bit, the Lorentz host, the one-loop arithmetic" | `BANKING_HANDOFF.md`: "(1) B1102's 18 hypercharge directions re-derived independently ... ⟹ the last hypercharge bit is P; (2) the Lorentz-host construction (see ANOMALY_RESOLVED) ...; (3) Ohtsuki c₁ ≈ 11π/(36√3) provisional." |
| 7 | `ADELIC_OBJECT.md` | "THE ADELIC OBJECT — the owner's frame, verified: two shadows, one lattice point, and the observer at infinity" | `BANKING_HANDOFF.md`: "TWO VERIFIED ANCHORS: (a) B1106's laboratory windows = the convergent denominators of φ ...; (b) Vol(m004) = 9√3·ζ_K(2)/π², verified to 4×10⁻³²." |
| 8 | `ANOMALY_RESOLVED.md` | "THE ANOMALY, RESOLVED — a fake Killing form, caught by the classification itself" | `BANKING_HANDOFF.md`: "closes memo 6's logged anomaly SAME-BENCH: the defect was a fake invariant form ... detection method banked: the classification theorem as checksum." |
| 9 | `PRIME_LANE.md` | "THE PRIME LANE — ruling, fence, and gated cells (owner-agreed)" | `BANKING_HANDOFF.md`: "the prime/zeta ruling (owner-agreed): the toolkit enters only where it intersects existing open nodes, queue order, never a destination; RH fenced as a BOUNDARY question." Gated cells PR-1..5. |
| 10 | `SIMULTANEOUS_CLOSING.md` | "THE SIMULTANEOUS CLOSING — one conjugation buys Lorentz signature AND compact color, and every such conjugation lands in E₆(−26) = M(𝕆,ℂ)" | `MANIFEST.md`: "**2B (B1134)**" |
| 11 | `FORK_THEOREM.md` | "THE PRICE OF SPACETIME — the D5 fork is a centralizer theorem, the three A2's are a frame torsor, and the corpus is running two color frames without knowing it" | `MANIFEST.md`: "**2B (B1138)**" |
| 12 | `GAUGE_CLOSING.md` | "THE GAUGE CLOSING — the EW slot closes as su(2,1) = u(2) ⊕ doublet, the gauge branch's host is E₆(−14), and the five real forms of E₆ are the five postures of the observer" | `MANIFEST.md`: "**2B (B1135)**" |
| 13 | `Y_SELECTION.md` | "THE Y-SELECTION — the gauge closing spends the last hypercharge bit itself: one closing, one hypercharge, and the nine closings tile all eighteen directions" | `MANIFEST.md`: "**2B (B1138)**" |
| 14 | `AMBIENT_LADDER.md` | "THE INSTALLMENT PLAN — the hypercharge room after Lorentz + color is 0 in E₆, exactly 1 in E₇, exactly 8 in E₈: the exceptional series sells the Standard Model one layer per step" | `MANIFEST.md`: "**2B (B1138)**" |
| 15 | `FAMILY_TRIPLET.md` | "THE FAMILY TRIPLET — the algebra that first affords the full stack also fixes the matter count: the 27 enters E₈ exactly three times, indexed by an A₂ triplet" | `MANIFEST.md`: "**2B (B1138)** — NB: its E₈ Cartan matrix is SYMMETRIC (audit §2; B1138's asymmetry note is false)" |
| 16 | `FIRST_BEAT.md` | "THE FIRST BEAT — the Gieseking extension made explicit: the object's own antilinear element is W = [[1, q],[0,1]] acting by z ↦ z̄ + q, its square is the meridian because q + q̄ = 1, and it factorizes exactly like the observer's closing" | `MANIFEST.md`: "**1B — discharges B1141's NEEDS-CERT**" |
| 17 | `BEAT_DESCENT.md` | "THE DESCENT — the beat reaches the algebra: Σ = exp(ad qE)∘gal extends the Gieseking element to e₆, and Σ² = Ad(tick) — the object supplies antilinearity but can never supply a real structure while it is ticking" | `MANIFEST.md`: "**1B — ditto**" |
| 18 | `SIGMA_27.md` | "Σ-27 — the beat on matter: Ω² = A27 (the tick reaches the module, so matter has no object-side reality), the 27-rep extends to the non-orientable group, and the L79 mirror IS the beat" | `MANIFEST.md`: "**1B — ditto**" |
| 19 | `S4_TORSOR.md` | "THE S₄ TORSOR — W(E₈) realizes the full S₄ on the four A₂ slots: at E₈ every physical slot assignment is a frame choice, and the normalizer is computed exactly" | `MANIFEST.md`: "**1B**" |
| 20 | `AW_TYPING.md` | "THE HATCH TYPED SHUT — B1111's stabilizer-typing residue executed: no transversal pair of the flat cone's order-96 group generates an ADE (SU(2)-type) stabilizer; the order-24 candidates are D₁₂, not 2T" | `MANIFEST.md`: "**NEG, 1B**" |
| 21 | `UNIT_DICTIONARY.md` | "THE UNIT DICTIONARY — every geodesic eigenvalue is a unit of an explicit palindromic quartic labeled by two rational integers, and geodesic length is its log-Mahler measure" | `MANIFEST.md`: "**1B**" |

### MAIN coverage, memos #1–21

The branch's own numbers already point at the bank: each phase-II/III memo maps 1:1 onto a specific
`frontier/B11xx_*` arc whose `FINDINGS.md` opens with "Harvest arc (<MEMO_FILE>.md...)". Confirmed by
reading each arc's own header:

| # | memo | MAIN coverage | evidence |
|---|---|---|---|
| 1 | JORDAN_MEMO | **HARVESTED** — `B1113_tmeter` | `frontier/B1113_tmeter/FINDINGS.md`: "Harvest arc (the JORDAN_MEMO §B; cloud..." |
| 2 | PROJECTIVE_HATCH | **HARVESTED** — `B1112_projective_hatch` | `frontier/B1112_projective_hatch/FINDINGS.md`: "Harvest arc — the criterion is the..." |
| 3 | LORENTZ_ON_THE_DOUBLE | **HARVESTED** — `B1114_lorentz_double` | `frontier/B1114_lorentz_double/FINDINGS.md`: "Harvest arc (LORENTZ_ON_THE_DOUBLE.md; ..." |
| 4 | SPENDING_ORDER | **HARVESTED** — `B1115_spending_order` | `frontier/B1115_spending_order/FINDINGS.md`: "Verdict PROVED (the DAG's edges are each a banked..." |
| 5 | ASYMPTOTIC_CHANNEL | **HARVESTED** — `B1116_asymptotic_channel` | `frontier/B1116_asymptotic_channel/FINDINGS.md`: "Verdict PROVED (the scope audit is a complete quantifier..." |
| 6 | DEFLATION_RUN | **HARVESTED** — `B1118_deflation` | `frontier/B1118_deflation/FINDINGS.md`: "Verdict PROVED (the P-bit fusing map reproduced on THIS..." |
| 7 | ADELIC_OBJECT | **HARVESTED** — `B1117_adelic_object` | `frontier/B1117_adelic_object/FINDINGS.md`: "Verdict PROVED (Anchor B reproduced on THIS bench to 32..." |
| 8 | ANOMALY_RESOLVED | **HARVESTED** — `B1119_anomaly_resolved` | `frontier/B1119_anomaly_resolved/FINDINGS.md`: "Verdict PROVED (a resolved error + a banked detection..." |
| 9 | PRIME_LANE | **ABSENT** | zero hits for "prime lane" / "prime-lane" / "PR-1"/"PR-2"/"PR-3" anywhere in `docs/` or `frontier/`; no `B1112`–`B1145`-range arc mentions it, including `B1144_adoption_audit` (checked directly) |
| 10 | SIMULTANEOUS_CLOSING | **HARVESTED** — `B1134_simultaneous_closing` | `frontier/B1134_simultaneous_closing/FINDINGS.md`: "Verdict PROVED (the MATH: a single involution realizes..." — matches `MANIFEST.md`'s own "2B (B1134)" |
| 11 | FORK_THEOREM | **HARVESTED** — `B1138_structural_completion` (bundled) | `frontier/B1138_structural_completion/FINDINGS.md`: "four structural results ... (cloud memos 11/14/13/15, verified two-bench)" |
| 12 | GAUGE_CLOSING | **HARVESTED** — `B1135_gauge_closing` | `frontier/B1135_gauge_closing/FINDINGS.md`: "Verdict PROVED (the MATH: the factor-preserving involutive..." |
| 13 | Y_SELECTION | **HARVESTED** — bundled in `B1138_structural_completion` (same as #11) | title cites "cloud memos 11/14/13/15" |
| 14 | AMBIENT_LADDER | **HARVESTED** — bundled in `B1138_structural_completion` (same as #11) | title cites "cloud memos 11/14/13/15" |
| 15 | FAMILY_TRIPLET | **HARVESTED** — bundled in `B1138_structural_completion` (same as #11) | title cites "cloud memos 11/14/13/15" |
| 16 | FIRST_BEAT | **HARVESTED** — via `B1145_sp2_fermion_seat` and `docs/RELAY_LEDGER.md` | `docs/RELAY_LEDGER.md`: "the cloud's cert reproduced exactly here → **B1145**; B1141's beat-trilogy NEEDS-CERT dischargeable"; `docs/THEOREM_REGISTRY.md` T-SPIN-PAYMENT row: "NEEDS-CERT: ... (beat-trilogy 16/17/18)"; `frontier/B1145_sp2_fermion_seat/FINDINGS.md` references `gieseking_beat` directly |
| 17 | BEAT_DESCENT | **HARVESTED** — same B1145/RELAY_LEDGER beat-trilogy discharge as #16 | `frontier/B1145_sp2_fermion_seat/FINDINGS.md` references `beat_descent` directly |
| 18 | SIGMA_27 | **HARVESTED** — same B1145/RELAY_LEDGER beat-trilogy discharge as #16 | `frontier/B1145_sp2_fermion_seat/FINDINGS.md` references `sigma27` directly |
| 19 | S4_TORSOR | **ABSENT** | zero hits for "S4 torsor" / "S₄ torsor" / "s4_torsor" anywhere in `docs/` or `frontier/` |
| 20 | AW_TYPING | **ABSENT** | zero hits for "AW typing" / "aw_typing" / "hatch typed shut" anywhere in `docs/` or `frontier/` |
| 21 | UNIT_DICTIONARY | **ABSENT** | zero hits for "unit dictionary" anywhere in `docs/` or `frontier/`. One coincidental false-positive checked and ruled out: `docs/atlas/FAILURE_ATLAS.md` and `frontier/B674_generation_leg/.../S1_SILVER_CC2.md` both use the unrelated phrase "palindromic quartic" in a much earlier (pre-existing, B674-era) construction about a silver-field unit, not this memo |

**B1144/B1145, which the task named as the memos that "reconciled some":** `B1144_adoption_audit`
is the corrective pass over the whole hostile-review record (title: "THE ADOPTION-LAYER CORRECTION:
four fixes from the cloud's CORPUS_ADOPTION_AUDIT, verified from primary source — the math was never
wrong"); `B1145_sp2_fermion_seat` is specifically where memo 29 (SP-2, outside range 1–21) is banked
and where memos 16–18's beat-trilogy content is discharged as shown above.
