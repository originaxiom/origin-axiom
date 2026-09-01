# S8 — THE INSTRUMENTED E53 HUNT (internalization sweep, 2026-09-01)

**Seat role:** digest-and-flag only. Nothing below is graded dead or proved; every flag is
for the evaluating seat's adjudication.

## COVERAGE MODULUS

**Read / ran:**
- `scripts/checks/open_claim_sweep.py` — full source read (245 lines), then run in
  **report mode only** (`python3 scripts/checks/open_claim_sweep.py`, no arguments, nothing
  modified). `--selftest` NOT run (task asked for report mode). Full stdout captured;
  reproduced verbatim in §1 below (242 lines). NOTE the instrument's own truncation: it
  found **47** rows but prints only `rows[:40]` — the bottom 7 rows (score < ~27.8) are in
  neither its output nor this digest.
- `scripts/checks/already_banked.py` — source read (first 60 lines, incl. usage);
  run **aimed** twice (§3.4): once at the L154 kind-map/boundary-character topic, once at
  the su(3)+g2 descent topic.
- Live surfaces grepped (patterns: `never computed`, `uncomputed`, `candidate set is
  empty`, `no arc`, `never run`, `no script`, `blind-to-k`, `⟺ amphichiral`, `σ rational`,
  `forcing theorem`, `MENU-1`, `B994`, `kind-map`, `L154`, `su(3)+g2` variants, `k = 1`):
  `docs/*.md`, `README.md`, `papers/P3_THE_PAPER/main.tex`. Targeted context reads:
  THE_CLAIM.md (rows 15–46), LAW_MAP.md (grep-hit rows), MASTERPLAN.md 55–64,
  OPEN_PROBLEMS.md 110–120, PRICED_DOORS.md 143–152, OPEN_LEADS.md 1425–1445,
  GRAND_COMPUTATION_v0.md §§5–6, 8 (lines 178–258, 292–310), GRAND_COMPUTATION_LEDGER.md
  (rows C4, H5, I3), CROSSING_REQUIREMENTS.md R10/R11, main.tex 585–612 and 785–800.
- Board era: `docs/CAMPAIGN_STATUS.md` lines 1–140 read in full (B1216–B1232 entries),
  plus grep for B1216–B1232 across the file.
- Campaign results consulted: `campaign/BATCH1_REPORT.md` (head, verdict table),
  `campaign/G1_su3_g2_descent/FINDINGS.md` (head 40) + VERIFICATION verdict line
  (CONFIRMED), `campaign/T9_kind_map_survey/FINDINGS.md` (head 30) + VERIFICATION verdict
  line (DEGRADED — census gap found AND dispositioned; emptiness stands at the enlarged
  0/27 census per commit 895aa5a / G4), `campaign/G3_surface_application/CHANGESET.md`
  (first 80 lines, full change-set tables), `papers/P3_THE_PAPER/
  TERMINALITY_SECTION_CANDIDATE.md` (header + G1-amendment location), CAMPAIGN_TYPE_MATCHED.md
  (head 30). Git log (last 8 commits) for what landed when.

**Skipped (silent-truncation disclosure):**
- The 7 sweep rows below the top-40 cut (the instrument's own truncation, not mine).
- Full line-by-line reads of OPEN_LEADS.md (~2000+ lines), CAMPAIGN_STATUS.md beyond
  line ~260 (grep only), main.tex beyond the sections named above, all `docs/views/*`,
  HINT_LEDGER, COSMOLOGY_LEDGER, THEOREM_LEDGER (grep hits only).
- The generic patterns `open` / `unresolved` / `missing` alone produce thousands of hits;
  I did NOT enumerate them exhaustively — I triaged via the task-named candidates
  (su(3)+g2, T9, B994) plus the B1216–B1232 retraction list. A claim outside those beams
  could be missed.
- Batch-2/R-ring recompute cells (R01–R18) not read; T1/T2/T4/T5 details taken from
  BATCH1_REPORT only. already_banked.py aimed at only 2 topics, not per-claim.
- No verification of the sweep's IDF machinery beyond reading it; its matches were not
  independently re-scored.

---

## 1. THE RECORD'S OWN INSTRUMENT — `open_claim_sweep.py`, report mode, VERBATIM

Command: `python3 scripts/checks/open_claim_sweep.py` (run 2026-09-01, working tree at
HEAD 680be7a). Output, verbatim and complete:

```
OPEN-CLAIM SWEEP: 47 open claims with a strongly-matching SETTLED arc

==============================================================================
[  85.3] docs/THE_SM_VERDICT.md
  CLAIM: 1. **The VEV *direction* is an input in every framework.** Group theory gives the finite menu; the potential's free parameters pick off it. **Nobody d
    -> [  85.3] PROVED    B968_sm_verdict   shared: two-vev, measure-zero, vevs, homogeneous, configuration, transitive
    -> [  40.0] PROVED    B1025_input_derivability   shared: b962, homogeneous, pick, derives, vev, menu
    -> [  35.6] PROVED    B926_crossing_anatomy   shared: vevs, nobody, parameters, menu, input, space
==============================================================================
[  71.1] docs/THE_SM_VERDICT.md
  CLAIM: **The one door left open, and it is precise.** B803's usual quotation is **over-wide**; its own addendum narrows it: a step depending only on the **tr
    -> [  71.1] PROVED    B993_cornerstone_verified   shared: over-wide, usual, quotation, depending, b803, tier-2
    -> [  30.3] PROVED    B1062_bridge_cell   shared: narrows, quaternion, arithmeticity, anywhere, door, addendum
    -> [  27.5] NEGATIVE  B790_maass_adjudication   shared: nowhere, arithmeticity, anywhere, door, addendum, step
==============================================================================
[  66.4] docs/LAW_MAP.md
  CLAIM: | **MULTIPLICITY/SCALE IS THE OBSERVER'S (B719)** | 'how many units' (the trillions, the size) is an IMPORTED SCALE = the covering degree, NOT an obje
    -> [  66.4] PROVED    B926_crossing_anatomy   shared: being-filter, multiplicity/scale, b719, preferred, covering, deg
    -> [  36.8] PROVED    B556_escalator_tower   shared: covering, deg, grows, extended, size, cover
    -> [  31.4] PROVED    B722_resurgence_coupling   shared: b719, c-swap, covering, placement, index, multiplicity
==============================================================================
[  66.2] docs/LAW_MAP.md
  CLAIM: | **THE MEETING IS A PRODUCT, NOT A FUSION (B698 Leg A, analytic side)** | the level-15 meeting does NOT couple 3 and 5 analytically — by Flath's theo
    -> [  66.2] PROVED    B692_level15_literature   shared: borot, eynard, 15a, isogeny, 15a8, automorphic
    -> [  48.8] PROVED    B700_fiber_functor   shared: b698, theorem-grade, fusion, meeting, base-rate, among
    -> [  43.5] PROVED    B689_meeting_holds_ground   shared: automorphic, newform, couple, genus, meeting, level-15
==============================================================================
[  64.5] docs/OPEN_LEADS.md
  CLAIM: | **H2 — citation check (the novelty gate)** | **DE-RISKED by R4 (2026-06-11, `NOVELTY_AUDIT.md`); SPECIALIST CLOSE still OPEN — the user's.** | An ad
    -> [  64.5] NEGATIVE  B199_metallic_exponent_law   shared: guilloux, appears-novel, cooper, falbel, novel, long
    -> [  46.7] PROVED    B204_metallic_wrt_period   shared: appears-novel, implicit, novel, art, corrections, framework
    -> [  45.6] NEGATIVE  B281_crux_scoping   shared: guilloux, falbel, novel, confirm, settled, specialist
==============================================================================
[  62.3] docs/THE_FRAMEWORK.md
  CLAIM: **The input side of the whole derivation is priced, not estimated.** The counted external-input floor is **one dimensionful unit, two 𝔽₂ bits, and one
    -> [  62.3] PROVED    B926_crossing_anatomy   shared: licensed, yukawa, dimensionful, freedom, story, priced
    -> [  48.6] PROVED    B1014_proof_form   shared: docs/the_claim, licensed, endpoint, counted, dimensionful, deliberately
    -> [  43.5] PROVED    B1220_campaign_premise_audit   shared: drawn, yukawa, another, priced, triple, floor
==============================================================================
[  57.5] docs/PRICED_DOORS.md
  CLAIM: > **Review 41 — 2026-08-09.** Two doors repriced this window. **X8 (the Higgs doublet)** was registered as the campaign's top rung and **dissolved** —
    -> [  57.5] PROVED    B987_X8_higgs_doublet   shared: b298/b299, scopes, b978, b884, triplet, dissolved
    -> [  31.3] NEGATIVE  B986_b500_stragglers   shared: l145a, reopen, 2026-08-09, unchecked, child, concrete
    -> [  25.1] PROVED    B952_gut_ledger_rank   shared: triplet, doublet, higgs, splitting, down, written
==============================================================================
[  50.6] docs/THE_FRAMEWORK.md
  CLAIM: **What this buys, and what it still owes.** A second, self-standing theory the object supports, with a genuinely parameter-free classical action, a qu
    -> [  50.6] PROVED    B1090_partition_bridge   shared: arithmetic-cs, hilbert, founding, analogue, saddle, quantization
    -> [  40.5] PROVED    B1088_action_card   shared: parameter-free, arithmetic-cs, buys, analogue, completion, fenced
    -> [  35.7] PROVED    B1069_hearing_biography   shared: attempted, hilbert, assembled, fenced, further, term
==============================================================================
[  49.4] docs/OPEN_PROBLEMS.md
  CLAIM: ### D — The non-Hermitian Damanik–Gorodetski theorem (the spectral gate) **Question.** The metallic trace map at real `κ>2` gives the Fibonacci Hamilt
    -> [  49.4] PROVED    B160_quasicrystal_bridge_corroboration   shared: k007/k010, non-hermitian, gorodetski, cantor, hamiltonian, damanik
    -> [  42.2] NEGATIVE  B166_sln_aperiodic   shared: k007/k010, non-hermitian, cantor, damanik, hermitian, cocycle
    -> [  36.0] PROVED    B148_kappa_fricke_metallic   shared: painlev, gorodetski, hamiltonian, damanik, tier, fibonacci
==============================================================================
[  47.1] docs/LAW_MAP.md
  CLAIM: | **THE FRAME-ARC LAWS (B909 — the pending row PAID whole)** | sin²θ_W = 3/8 — PAID standalone by B919 (`tests/test_b919_traces.py`, one-prime tier, s
    -> [  47.1] PROVED    B926_crossing_anatomy   shared: b919, d-chain, one-prime, b909, 3/8, typing
    -> [  46.7] NEGATIVE  B915_the_crossing   shared: open-diagnosed, b919, d-chain, cmt, one-prime, 3/8
    -> [  35.7] NEGATIVE  B925_second_crossing   shared: d-chain, cmt, b909, 3/8, typing, compact
==============================================================================
[  46.7] docs/OPEN_LEADS.md
  CLAIM: | **L26** | **Prior-art for the golden→2I=SL(2,𝔽₅)=McKay-E₈ framing (B206)** — is the specific connection *metallic-monodromy → conductor-5 congruence
    -> [  46.7] PROVED    B210_dual_mckay_hyperbolic   shared: b206, ingredients, unchecked, prior-art, assembly, congruence
    -> [  37.5] PROVED    B211_metallic_arithmetic_geometric_faces   shared: b206, unchecked, link, mckay, until, novelty
    -> [  33.8] PROVED    B926_crossing_anatomy   shared: ours, assembly, congruence, mckay, mass, ratios
==============================================================================
[  46.4] docs/CROSSING_REQUIREMENTS.md
  CLAIM: **Today, as of B1101, there is no licensed candidate class for a value crossing.** What remains open is not a candidate but two structural questions t
    -> [  46.4] PROVED    B926_crossing_anatomy   shared: crossings, licensed, touches, document, gated, supplies
    -> [  35.1] PROVED    B950_sm_spec_ledger   shared: crossings, successor, today, document, supplies, crossing
    -> [  30.9] NEGATIVE  B1066_lane3_nomination   shared: licensed, decision, touches, targets, crossing, lane
==============================================================================
[  45.2] docs/OPEN_LEADS.md
  CLAIM: The vanishing count of B1103's coupling was channel-independent in every channel the outside session tested (26 in all three; 28 on the free-group cen
    -> [  45.2] PROVED    B1110_spectral_cluster   shared: b1103, free-group, listener, vanishing, fourth, typed
    -> [  23.5] PROVED    B154_silver_bundle_foundation   shared: cheapest, free-group, locus, coincidence, tested, word
    -> [  23.3] NEGATIVE  B592_mirror_listener   shared: listener, signal, vanishing, fourth, outside, channel
==============================================================================
[  44.8] docs/LAW_MAP.md
  CLAIM: | **The congruence-shadow theorem (the conductor is the ear's modulus)** | on ker(det), ρ_hear = χ_golden ∘ (reduction mod 5): the ear at the minimal 
    -> [  44.8] PROVED    B650_typed_functor   shared: congruence-shadow, b644, hear, hears, plane, congruence
    -> [  44.4] PROVED    B700_fiber_functor   shared: b640/b642, hear, irrep, psl, shadow, fibonacci
    -> [  44.3] PROVED    B654_listening_synthesis   shared: pentagon, hears, congruence, conductor, shadow, needs-specialist
==============================================================================
[  43.1] docs/LAW_MAP.md
  CLAIM: | **THE γ₅′ CORRESPONDENCE (the ear in the flavor-model catalog)** | the modular-flavor Γ₅′ ≅ SL(2,5) paradigm CHOOSES its group (10–13 catalog; geome
    -> [  43.1] PROVED    B926_crossing_anatomy   shared: parameters, functor, origin, correspondence, selects, hearing
    -> [  42.3] PROVED    B700_fiber_functor   shared: placement, functor, cc2, selects, hearing, supplies
    -> [  39.7] PROVED    B928_d2_decode   shared: equality, derives, functor, origin, twist, sweep
==============================================================================
[  42.9] docs/OPEN_LEADS.md
  CLAIM: **The specific staleness.** Door 5 is the *ratio* lane, and B167 calls it *"the only logically-open lane"* — then dismisses it because its survivor is
    -> [  42.9] PROVED    B976_cascade_recovery   shared: gaugeable, b862, b864, calls, derives, cancellation
    -> [  30.7] PROVED    B978_phaseA_bank   shared: b862, b864, derives, hypercharge, anomaly, global
    -> [  28.8] PROVED    B1081_hydrogen_audit   shared: b862, b864, cancellation, hypercharge, anomaly, assumed
==============================================================================
[  42.6] docs/OPEN_LEADS.md
  CLAIM: | B921-9 | [MAIN-STATE] L10 ledger debts (route as one register-sweep lead): THEOREM_REGISTRY/LEDGER zero B8xx/B9xx rows; RETRACTIONS ≥5 missing rows;
    -> [  42.6] PROVED    B920_register_sweep   shared: comms_protocol, orphan, theorem_registry/ledger, tier-3, legal, retractions
    -> [  16.1] PROVED    B1069_hearing_biography   shared: roadmap, law_map, lead, false, route, ledger
    -> [  15.2] PROVED    B1067_rayclass_harvest   shared: roadmap, harvest, law_map, missing, route, zero
==============================================================================
[  41.9] docs/GRAND_COMPUTATION_LEDGER.md
  CLAIM: | I3. **THE DESIGNED CROSSING, never run** | **SPEC'D-READY, off-queue**: the mirror (θ-even) row is THE LAST LICENSED CONTACT ROW (KIND_TABLE consump
    -> [  41.9] PROVED    B1188_grand_retrieval   shared: irreversible, election, firing, accounting, licensed, contact
    -> [  34.1] PROVED    B1070_listener_derivation   shared: kind-row, non-commuting, t_m, contact, adjudication, everything
    -> [  33.2] PROVED    B1014_proof_form   shared: accounting, licensed, contact, designed, look-elsewhere, everything
==============================================================================
[  41.0] docs/OPEN_LEADS.md
  CLAIM: | **H4 — why is the figure-eight minimal along every axis?** (seeing question) | **OPEN (MATH); SHARPENED — mostly deflates.** | Under the project's o
    -> [  41.0] PROVED    B148_kappa_fricke_metallic   shared: b147, project, tree, markov, arithmeticity, deep
    -> [  34.1] PROVED    B855_wrong_null_audit   shared: mostly, arithmeticity, reid, axis, complement, once
    -> [  34.1] PROVED    B123_arithmeticity_m1   shared: simplest, arithmeticity, deep, smallest, reid, complement
==============================================================================
[  40.6] docs/CROSSING_REQUIREMENTS.md
  CLAIM: **Status since (2026-08-20).** Items 1–4 ran to completion, and the lane they opened is now **SPENT**: every row the kind table licenses in the coupli
    -> [  40.6] PROVED    B926_crossing_anatomy   shared: crossings, checklist, document, executed, gated, left
    -> [  33.1] PROVED    B787_interaction_programme   shared: checklist, doors, completion, executed, left, ran
    -> [  32.8] PROVED    B950_sm_spec_ledger   shared: crossings, governs, missed, document, ran, crossing
==============================================================================
[  39.8] docs/LAW_MAP.md
  CLAIM: | **The swap real structure** | the deck involution acts antilinearly (J² = +1); Y∘σ* = conj(Y); the phase geometry follows. PRECISION (2026-07-16, B6
    -> [  39.8] PROVED    B654_listening_synthesis   shared: b638, fig-8, subfield, conj, definition, objects
    -> [  35.6] PROVED    B647_core_mechanism   shared: gauge-variant, b649, b638, conj, swap, silver
    -> [  33.4] PROVED    B700_fiber_functor   shared: 6/r23-4, b638, subfield, objects, imaginary, swap
==============================================================================
[  37.9] docs/LAW_MAP.md
  CLAIM: | **The unit cross-ratio law + the 13-dial** | the unique normalization-free invariant of the Y-tensor (Y[023]·Y[134])/(Y[034]·Y[123]) = **1 exactly**
    -> [  37.9] PROVED    B647_core_mechanism   shared: 13-dial, b645, spectator, cross-ratio, doubles, double
    -> [  37.7] PROVED    B649_silver_holonomy   shared: y-tensor, spectator, cross-ratio, doubles, quantity, always
    -> [  21.7] PROVED    B1069_hearing_biography   shared: 1+2, meaning, always, unit, prime, split
==============================================================================
[  37.0] docs/OPEN_LEADS.md
  CLAIM: | **L7** | **One-theorem capstone** — fold S031 (sealing) + S032-A (no-forced-choice) + the chirality recursion (B134/K011) into a single structural s
    -> [  37.0] NEGATIVE  B130_no_forced_choice   shared: no-forced-choice, s031, capstone, sealing, synthesis, target
    -> [  32.0] NEGATIVE  B140_compute_reconciliation   shared: b134/k011, s031, sealing, recursion, variety, math
    -> [  28.0] PROVED    B132_quantum_layer   shared: no-forced-choice, s031, sealing, recursion, synthesis, math
==============================================================================
[  36.6] docs/OPEN_LEADS.md
  CLAIM: | **L78 — the level-2 filling span (Route A)** | Row-0 covectors of ρ_level-2(g_{p,q}) over the slope sweep; SVD against the θ-even/θ-odd split. Rank 
    -> [  36.6] PROVED    B583_chiral_content   shared: covectors, l78, amplitude, round, span, becomes
    -> [  27.2] PROVED    B742_negatives_hunt_p1   shared: level-2, pinned, slope, filling, controls, missing
    -> [  24.5] PROVED    B586_round3_handoff   shared: level-2, torsions, amplitude, round, filling, sweep
==============================================================================
[  35.9] docs/views/THE_SPINE.md
  CLAIM: - **B171** `OPEN` `test_b171_heterogeneous_quasicrystal.py` — Phase-0 baselines show the woven metallic spectrum inherits both rank-2 ladders and quan
    -> [  35.9] PROVED    B172_combination_gap_resolution   shared: woven, b171, ladders, rank-3, rank-2, density
    -> [  24.3] PROVED    B173_gaplabel_rank_reduction   shared: woven, b171, rank-3, density, combination, trap
    -> [  21.5] PROVED    B175_collective_spectrum_predictivity   shared: woven, b171, rank-3, combination, spectrum, metallic
==============================================================================
[  35.0] docs/OPEN_LEADS.md
  CLAIM: | B921-6 | Cell 3 spin fork (= L7): the two spin structures of m004 are DISTINGUISHED by cusp data (ρ₁ trace pattern (2,−2), ρ₂ (−2,−2)); ρ₁ is non-Li
    -> [  35.0] PROVED    B933_spinor_hejhal_design   shared: non-lie, spinor-hejhal, dirac, conventions, spin, fork
    -> [  23.6] PROVED    B804_dirac_spectrum   shared: spinor-hejhal, dirac, spin, structures, m004, cusp
    -> [  21.6] PROVED    B803_commensurability_audit   shared: authorized, dirac, structures, m004, cusp, spectrum
==============================================================================
[  33.2] docs/OPEN_LEADS.md
  CLAIM: | **L5** | **General-word sealing, SL(3) first pass** — the concrete SL(3) entry point to L6: run the B137-style off-sublocus search for a few non-met
    -> [  33.2] PROVED    B138_s031_principal_lemma   shared: b129/b137, b137-style, off-sublocus, sealing, among, words
    -> [  27.3] PROVED    B193_sealing_field_scouts   shared: off-sublocus, non-metallic, scout, sealing, search, words
    -> [  20.1] PROVED    B590_revival_remainders   shared: off-sublocus, sealing, guard, pipeline, irreducible, pass
==============================================================================
[  32.5] docs/OPEN_LEADS.md
  CLAIM: > **That makes it an OBJECT-LEVEL quantity — precisely the address B993 left open when it showed the > trace-field route is class-level. Almost everyt
    -> [  32.5] NEGATIVE  B1006_lambda2_pslq   shared: b993, address, class-level, object-level, trace-field, showed
    -> [  21.8] PROVED    B997_golden_conductor_uniqueness   shared: b993, class-level, showed, else, quantity, left
    -> [  20.3] PROVED    B803_commensurability_audit   shared: class-level, object-level, commensurability, everything, precisely, makes
==============================================================================
[  32.5] docs/OPEN_LEADS.md
  CLAIM: > **Review-37 note (2026-08-03).** Scoped stale-check clean for the B848–B877 window (the > long-standing OPEN rows belong to other subsystems). New s
    -> [  32.5] PROVED    B876_descent   shared: reformulation, across-breakings, multiplication, 2026-08-03, descent, graded
    -> [  22.1] PROVED    B875_triality_tiling   shared: multiplication, 2026-08-03, descent, graded, solo, sector
    -> [  21.3] PROVED    B874_measurement_ladder   shared: subsystems, 2026-08-03, solo, measurement, carried, audit
==============================================================================
[  31.9] docs/THE_SM_VERDICT.md
  CLAIM: - **The external inputs are counted (B1000): five closings over four sectors, charge taking two — and B963 proves the two compete.** The interface is 
    -> [  31.9] PROVED    B1017_recount   shared: compete, b1000, b963, interface, counted, closings
    -> [  17.1] PROVED    B1009_verification_pass   shared: b1000, counted, closings, finite, external, question
    -> [  15.1] PROVED    B926_crossing_anatomy   shared: closings, typing, inputs, charge, external, question
==============================================================================
[  31.8] docs/OPEN_LEADS.md
  CLAIM: | L122 | **The m003 mod-4 hint completion** — the branch DID the raised cutoff (m003-only ≡ 1 mod 4 exactly, 43 norms, single class); harvest + amend 
    -> [  31.8] PROVED    B794_congruence_level4   shared: cutoff, mod-4, hint_ledger, norms, hint, m003
    -> [  23.5] NEGATIVE  B790_maass_adjudication   shared: cutoff, mod-4, norms, m003, cc3, mod
    -> [  17.4] PROVED    B920_register_sweep   shared: hint_ledger, norms, hint, cc3, branch, class
==============================================================================
[  31.8] docs/OPEN_LEADS.md
  CLAIM: | **L113** | **the algebraicity (d, H) box** — B798 seals it: BSV parity needs **100** digits, not 50; the 100-digit stack needs **its own** certifica
    -> [  31.8] NEGATIVE  B1006_lambda2_pslq   shared: bsv, 100-digit, algebraicity, b798, box, digits
    -> [  26.2] PROVED    B922_lambda2_receipt   shared: 100-digit, algebraicity, b798, box, certification, digits
    -> [  21.5] PROVED    B878_maass_upper_window   shared: 100-digit, b798, box, certification, digits, sealed
==============================================================================
[  31.8] docs/PRICED_DOORS.md
  CLAIM: > ## STATE AT REVIEW 45 (2026-08-13) > > The factorisation reading is on the record (an SM value = a class invariant × a substrate > scale; we hold on
    -> [  31.8] PROVED    B1062_bridge_cell   shared: 2026-08-13, aperiodic, doors, window, blind, door
    -> [  24.8] PROVED    B1116_asymptotic_channel   shared: factorisation, substrate, doors, door, factor, scale
    -> [  23.5] NEGATIVE  B1066_lane3_nomination   shared: 2026-08-13, targets, review, priced, door, crossing
==============================================================================
[  31.5] docs/OPEN_LEADS.md
  CLAIM: > **So the question — is the child (x⁴−x−1, d_K = −283) a short word? — is OPEN at 23% unchecked, > the reopen action is written down, the arithmetic 
    -> [  31.5] NEGATIVE  B500_child_hunt   shared: d_k, reopen, short, unchecked, child, register
    -> [  27.0] NEGATIVE  B986_b500_stragglers   shared: reopen, unchecked, child, concrete, down, register
    -> [  16.4] PROVED    B1187_depth_closure   shared: d_k, specified, child, sweep, word
==============================================================================
[  29.9] docs/OPEN_LEADS.md
  CLAIM: | **C5 — the arithmetic-CS hole** | the one true specialist gap (B708, Kim's bar), now SHARPENED: the object's CS value is 0, so the arithmetic analog
    -> [  29.9] PROVED    B1088_action_card   shared: arithmetic-cs, hole, analogue, fenced, needs-specialist, term
    -> [  23.6] NEGATIVE  B1108_c5_archimedean   shared: arithmetic-cs, kim, analogue, fenced, term, volume
    -> [  20.5] NEGATIVE  B1157_dynamics_null   shared: specialist, bar, needs-specialist, term, sharpened, volume
==============================================================================
[  29.9] docs/OPEN_LEADS.md
  CLAIM: **Fences**: Gate 5-Q throughout Phase 0 (no measured value enters any main artifact until a sealed crossing cell exists with its prior declared); expl
    -> [  29.9] PROVED    B1033_generation_adjudication   shared: the_claim, 5-q, main, until, throughout, declared
    -> [  26.6] PROVED    B1062_bridge_cell   shared: membership, 5-q, numeric, banks, throughout, declared
    -> [  25.0] NEGATIVE  B1066_lane3_nomination   shared: enters, fences, until, throughout, declared, crossing
==============================================================================
[  29.5] docs/OPEN_LEADS.md
  CLAIM: All five gaps computed (5 locks). ★ S5: **the triple identity** — ℤ/11 = N(φ⁵−1) = the 5-fold-cover torsion prime (the charge is GEOMETRIC; n=5-specif
    -> [  29.5] PROVED    B533_coupling_invariance   shared: frequencies, original, end, counts, symbolic, prime
    -> [  29.1] PROVED    B1199_register_reads_and_L188   shared: dark-hyperbola, register, counts, symbolic, charge, proof
    -> [  27.4] PROVED    B637_corrected_cell3   shared: recursive, doubles, 2/3, weights, eisenstein, step
==============================================================================
[  28.9] docs/GRAND_COMPUTATION_LEDGER.md
  CLAIM: | D2. generation count 3 | **PARTIAL** — NULL on-object; external (E8 fence). **Off-surface tension: B891 (sealed, passed): a SINGLE observer register
    -> [  28.9] PROVED    B1220_campaign_premise_audit   shared: off-surface, registers, restated, partial, internal, generation
    -> [  27.6] PROVED    B1145_sp2_fermion_seat   shared: on-object, generations, internal, generation, fence, matter
    -> [  26.7] PROVED    B926_crossing_anatomy   shared: generations, internal, generation, null, matter, either
==============================================================================
[  28.5] docs/OPEN_LEADS.md
  CLAIM: | L-PI7 (new) | **OPEN — a new structure fact, mechanism unknown**: ALL six mult-1 Γ₄₁ newforms at level (4) have an exact zero at π₇ — and only π₇ am
    -> [  28.5] NEGATIVE  B790_maass_adjudication   shared: parent, follow-up, share, cc3, sits, census
    -> [  25.1] PROVED    B936_cohomology_reading   shared: nor, share, among, primes, census, neither
    -> [  24.1] PROVED    B1069_hearing_biography   shared: share, among, primes, sits, census, error
==============================================================================
[  27.8] docs/views/THE_SPINE.md
  CLAIM: - **B1156** `OPEN` `test_b1156_seam_a_gate2.py` — SEAM-A Gate 2 (the prize crossing), sharpened by the WF-1 adversarial workflow (10 agents; 3 scouts 
    -> [  27.8] NEGATIVE  B1157_dynamics_null   shared: b1156, refuters, workflow, agents, adversarial, seal
    -> [  18.0] NEGATIVE  B199_metallic_exponent_law   shared: refuters, prize, workflow, agents, adversarial
    -> [  12.4] PROVED    B1188_grand_retrieval   shared: prize, workflow, adversarial, crossing, gate
```

**Digest of the instrument's report (not my adjudication):** 47 units matched; the printed
40 span 10 surfaces (OPEN_LEADS 16, LAW_MAP 8, THE_SM_VERDICT 3, THE_FRAMEWORK 2,
PRICED_DOORS 2, CROSSING_REQUIREMENTS 2, GRAND_COMPUTATION_LEDGER 2, OPEN_PROBLEMS 1,
views/THE_SPINE 2, OPEN_LEADS review-notes several). Caveat from reading the source: many
top matches pair a claim with the arc the claim itself DISCUSSES (e.g. the Review-41
PRICED_DOORS entry matching B987, or B921-9 matching B920) — the instrument excludes only
arcs the unit cites by `B\d+` number, so prose references slip through; several rows are
therefore self-matches rather than lost locks. The evaluating seat should treat scores as
leads, not verdicts. Also note: the two `views/THE_SPINE.md` rows (B171 `OPEN` matching
B172/B173/B175; B1156 `OPEN` matching the NEGATIVE B1157) are the classic E53 shape —
an OPEN spine row with named settled successors — and worth an aimed check.

---

## 2. STALE-OPEN HUNT (my complementary patterns) — surfaces still calling batch-1..3-computed things uncomputed

**S8-1. The T9/G4 kind-map survey is RUN; two GC surfaces still present it as the pending
instrument, and one asserts the count T9 refuted.**
- `docs/GRAND_COMPUTATION_v0.md:185` — σ row: "the typed instrument for the next attempt:
  survey ALL banked series + the prefactor↔weight kind-map".
- `docs/GRAND_COMPUTATION_v0.md:206` — deletion-schedule row 1: "the L154 bridge cell
  (batch-2 retry, typed instrument from GC-6: survey ALL banked object-side series …)".
- Closing artifact: `reports/fresh_physics_seat_2026-09-01/campaign/T9_kind_map_survey/`
  (FINDINGS: EMPTY-CONFIRMED, 16 computable entries + 10 not-comparable, 0/16 pass;
  verifier DEGRADED with the census gap dispositioned at the enlarged 0/27 census —
  commit 895aa5a "G4 census gap dispositioned (0/27 at enlarged census)"). The survey is
  no longer un-run; the surfaces still read as if it is. (Campaign results are report-side,
  not banked arcs, so `already_banked.py` cannot see them — §3.4; the staleness is
  surface-vs-report, pending owner merge adjudication.)
- Sharper sub-flag: `docs/GRAND_COMPUTATION_LEDGER.md:49` (row C4) and
  `docs/GRAND_COMPUTATION_v0.md:299-300` state GC-12's count — "the full survey finds
  exactly one banked q-series (B672's doublet)" / "exactly one banked q-series exists".
  T9's FINDINGS §1 delivers a **split verdict: "REFUTED as a count"** (the genuine-series
  census is ~twelve streams / 16 computable entries) while confirming the emptiness
  conclusion. The "exactly one" wording on both GC surfaces is stale against T9.

**S8-2. The su(3)⊕g₂ descent is COMPUTED; three surfaces state B994 rule-independence /
endpoint-set-size-one without the scope restriction G1 proved necessary.**
- Closing artifact: `reports/fresh_physics_seat_2026-09-01/campaign/G1_su3_g2_descent/`
  (verifier CONFIRMED): every registerable chain through su(3)⊕g₂ terminates at su(3) —
  a NON-SM endpoint; on the specials-inclusive menu min-dim picks su(3)⊕g₂ at step 1, so
  the unrestricted rule-independence quantifier is "refuted by computation, not just
  unproven" (G1 FINDINGS headline 1). The paper candidate
  (`papers/P3_THE_PAPER/TERMINALITY_SECTION_CANDIDATE.md`) carries the G1 AMENDMENT
  (line 293) — though its own header (line 4) still says "PENDING the G1 cell's …
  outcome", a minor internal inconsistency in one file.
- Surfaces WITHOUT the restriction:
  - `docs/THE_CLAIM.md:26` — "endpoint **rule-independence** — all six registerable
    selection functions end at the SM | THEOREM | B994" (no menu qualifier).
  - `docs/THE_CLAIM.md:42` — "Within the registerable universe the reachable endpoint set
    has size **one** (B994)" — G1 exhibits a registerable-respecting selection function
    (min-dim over the specials-inclusive menu) reaching su(3).
  - `README.md:41` — claimable residue "the terminality **plus** its rule-independence
    (B994)" with no menu restriction.
  - `docs/LAW_MAP.md:330` — "THE CASCADE'S ENDPOINT IS RULE-INDEPENDENT" headline; the
    row does carry "SCOPE: about B861's menus, whose completeness is certified by B873's
    P5 gate", which is arguably the fence — but the headline reads wide, and G1's
    computed counterexample lives exactly one menu-widening away. (G3's CHANGESET
    deliberately skipped LAW_MAP:330 for the *novelty* item B1; the *quantifier* item
    postdates that skip — G1 landed in commit 895aa5a, after G3's 1d33afe.)
  - `papers/P3_THE_PAPER/main.tex:588-600` — the termination scopenote fences with "not
    exhaustive over exotic conformal embeddings"; still literally true, and G1 has now
    computed the one conformal special (non-SM endpoint), so the fence could be replaced
    by the computed fact. Not asserting anything false; noted as an upgrade-available.
- Also relevant, uncorrected-in-kind: G1 headline 2 — terminality is a property of the
  (algebra, content) pair, not the algebra; B863's statement stands only with the banked
  generation content. No live surface states this sharpening.

**S8-3. B994's "never asked before" — the propagation reached the arc addendum but the
LAW_MAP row keeps the phrase.** `frontier/B994_rule_variation/ADDENDUM_2026-09-01.md`
scopes "never asked before" to *in this corpus*; `docs/LAW_MAP.md:330` still opens with
"The rule-variation axis had **never been asked**" un-scoped. G3's CHANGESET item B1
explicitly and with reasons declined this edit (the row's grade clause fences it) — so
this is a *declared* residual, not a lost one; recorded for completeness.

**S8-4. The L149 block "no arc runs the cascade on any m ≥ 2 grammar … UNCOMPUTED, not
zero" is stamped OVERTAKEN in one surface and un-stamped in three.**
`docs/OPEN_LEADS.md:1432` carries "*(stamp 2026-08-19: OVERTAKEN on 2026-08-10 by B1019
… the silver/bronze grammars have NO McKay door at all, so no m ≥ 2 cascade can BEGIN)*".
The same block appears verbatim WITHOUT the stamp at `docs/MASTERPLAN.md:59-61`,
`docs/OPEN_PROBLEMS.md:114-116`, and `docs/PRICED_DOORS.md:147-149`. Pre-campaign
staleness (the closer is banked B1019, not a batch cell), same E53 replication class.

---

## 3. REVERSE DIRECTION — surfaces asserting as live what the B1216–B1232 era retracted or refuted

**S8-5. `docs/LAW_MAP.md:107` still asserts the biconditional B1226 refuted.** The CP
RATIO LAW row: "CP **sign** = sign of Chern–Simons, CS = 0 ⟺ amphichiral (B303)". B1226
(CAMPAIGN_STATUS lines 94–105; THEOREM_REGISTRY:269 T-BETA-ODD-IS-BIT-VALUED) refutes
`CS = 0 ⟺ amphichiral` in both directions (m003/m135/m207 amphichiral with CS = ¼;
m208 chiral with CS = 0); B1224 corrects it to "amphichirality forces CS ∈ ℤ/2 = {0, ¼}".
B1226's entry says "six surfaces corrected (two THEOREM rows in THE_CLAIM.md)" — THE_CLAIM
rows 29–30 indeed carry the correction, and RELAY_LEDGER:60 + THE_FRAMEWORK:325 are
corrected — but **LAW_MAP is not among the files citing B1226** (grep: B1226 appears in
CAMPAIGN_STATUS, OPEN_LEADS, RELAY_LEDGER, SM_SPECIFICATION_LEDGER, THEOREM_REGISTRY,
THE_CLAIM, THE_FRAMEWORK, THE_PATTERN_MEDITATION_2, THE_WHY_CAMPAIGN,
THE_WITHHOLDING_TAXONOMY — not LAW_MAP). Nearby rows LAW_MAP:146 ("amphichirality
(K=K̄, CS=0, CANONICAL)") and 148 restate CS=0-as-amphichirality's-content; 148 is
scoped to X(4₁)/m004 where the conclusion holds, 146/107 read general. Retracted content
reading as live — flag class (c).

**S8-6. `docs/GRAND_COMPUTATION_v0.md` §6b (lines ~218–231) carries B1229's "σ is
rational — not a continuum" and "σ ∈ {1/3, 1} — one bit" without the later fences.**
B1231 (CAMPAIGN_STATUS lines 19–34): Anderson–Moore/Vafa "is a PHYSICS-ARGUMENT, unread,
and does not automatically cover a CS boundary… B1229's 'robust core' **is not robust**;
… σ now carries **three conditionals, none stated when banked**." B1232 (lines 3–17):
"RETRACTED: (1) σ ∈ ℚ establishes nothing — ℚ IS DENSE IN ℝ, so B1229's 'robust core'
was not weakly grounded but **empty**". GRAND_COMPUTATION_v0.md contains no B1231/B1232
annotation (grep clean); §6b reads as a standing reading rule with the σ-rational chain
intact. (§6a, by contrast, DOES honestly carry B1228's same-session σ=1 retraction —
"Row 1 is NOT deleted … the geometric boundary WZW is A₁".)

**S8-7. `docs/GRAND_COMPUTATION_v0.md:240-241` — "the level forced by inventory … only
level 1 needs no level datum" is the inference pattern B1232 retracted as law.** B1232
retraction (2): "'no receiver for k ⇒ k = 1' is a default-value inference from absence
(adopted law: absence of a typed receiver means quotient-invariance or underdetermination,
never a default)". The v0 §6a text recording B1228's "level forced by inventory" piece has
no fence against that adopted law. Same class as S8-6: the campaign log carries the
retraction; the v0 surface does not.

**S8-8. Borderline, both directions: `papers/P3_THE_PAPER/main.tex:793` — "the current
candidate set is empty" (σ row).** Two later artifacts bear on it in opposite directions:
B1228 (CAMPAIGN_STATUS:79) moves row 1 "from *empty candidate set* to *unique named
candidate*" ((E₆)₁ vacuum module — a named TARGET type, arguably not a banked candidate
character); T9/G4 confirm at corpus scale that no banked artifact SUPPLIES such a
character (0/16, 0/27). Whether "empty" is stale (vs B1228's named candidate) or
confirmed (vs T9's supply-side emptiness) depends on which set the sentence quantifies
over; handed to the evaluating seat un-graded.

**S8-9. Checked and CLEAN (recorded so the absence is not silent):**
- B1225's closure ("the most-cited open item closes, by proof") — the surfaces that
  discuss the forcing-theorem search (GRAND_COMPUTATION_LEDGER:161,165; the "missing in
  kind: a forcing theorem for the value arm" line replicated across LEAD_REGISTER:231,
  MASTERPLAN:302, OPEN_PROBLEMS:590, PRICED_DOORS:314, ROADMAP:101) are B1203/B1204-era
  statements about the *reader's-column* residue, which B1225 explicitly does NOT close
  ("does not close whether a selector exists on β-odd or dimensionful data"). I found no
  surface still asserting the pre-B1225 form ("that theorem does not exist; it is the
  single thing standing between…") as live outside quoted history. NOT flagged; the
  five-fold replication of the same sentence is noted as a consistency-maintenance risk
  only.
- G3's own propagation (T4/T5): spot-checked THE_CLAIM ℤ₆ row (REPRODUCED, B1221 note
  present), README lines 37–41, main.tex 941–947 — all carry the corrections the
  CHANGESET claims. G3's two declared skips (LAW_MAP:330 novelty wording,
  CAMPAIGN_STATUS:240) are as documented.
- B1223's triality refutation and B1224's gate-catch: no live surface found asserting the
  V₄⋊S₃/triality correspondence as established (beams: `triality` rows in LAW_MAP are
  B875/B952-era and differently scoped). Shallow check only.

## 3.4 Aimed `already_banked.py` runs (per its usage; corpus-side control)

- `already_banked.py "kind-map survey banked q-series boundary character L154"` →
  top hits B1191 (PROVED, 7/7 terms), B1190 FINDINGS, B1194 (4/7). Confirms the banked
  corpus's latest word on the kind-map is GC-12's one-series claim — i.e. the bank itself
  does not yet contain T9's corrected census (expected: campaign cells are report-side,
  pending owner adjudication). So the S8-1 staleness is surface-and-bank vs report.
- `already_banked.py "su(3) g2 descent specials menu registerable endpoint"` → top hits
  B869 FINDINGS (5 terms), B863 (4), B994 (4), B1028 (3), B871 (3). Same shape: the bank's
  latest is B863/B994's restricted-menu-uncomputed state; G1's computation exists only
  under reports/. Confirms S8-2's staleness is real and also that nothing already-banked
  pre-empts G1.

---

## 4. FLAG SUMMARY FOR THE EVALUATING SEAT

| flag | file:line | stale assertion | closing/opening artifact |
|---|---|---|---|
| S8-1a | docs/GRAND_COMPUTATION_v0.md:185, :206 | kind-map survey = "typed instrument for the next attempt" (unrun) | campaign/T9_kind_map_survey (EMPTY-CONFIRMED 0/16; G4 0/27; verifier DEGRADED-dispositioned) |
| S8-1b | docs/GRAND_COMPUTATION_LEDGER.md:49; docs/GRAND_COMPUTATION_v0.md:299-300 | "exactly one banked q-series (B672's doublet)" | T9 FINDINGS §1: "REFUTED as a count" (~12 streams / 16 entries) |
| S8-2 | docs/THE_CLAIM.md:26, :42; README.md:41; docs/LAW_MAP.md:330 (headline); main.tex:588-600 (fence upgradable) | B994 rule-independence / endpoint-set-size-one without the menu restriction G1 proved necessary | campaign/G1_su3_g2_descent (CONFIRMED: NON-SM-ENDPOINT on the specials-inclusive menu); TERMINALITY_SECTION_CANDIDATE.md G1 AMENDMENT |
| S8-3 | docs/LAW_MAP.md:330 | "never been asked" un-scoped (declared G3 skip) | frontier/B994_rule_variation/ADDENDUM_2026-09-01.md |
| S8-4 | docs/MASTERPLAN.md:59-61; docs/OPEN_PROBLEMS.md:114-116; docs/PRICED_DOORS.md:147-149 | "no arc runs the cascade on any m ≥ 2 grammar … UNCOMPUTED" without the OVERTAKEN stamp | B1019 (per docs/OPEN_LEADS.md:1432 stamp) |
| S8-5 | docs/LAW_MAP.md:107 (also :146) | "CS = 0 ⟺ amphichiral (B303)" as live law | B1226/B1224 (T-BETA-ODD-IS-BIT-VALUED, THEOREM_REGISTRY:269); LAW_MAP absent from B1226's corrected-file set |
| S8-6 | docs/GRAND_COMPUTATION_v0.md:218-231 (§6b) | "σ is rational — not a continuum"; "σ ∈ {1/3,1} — one bit" unfenced | B1231 (three unstated conditionals; AMV unread) + B1232 retraction (1) |
| S8-7 | docs/GRAND_COMPUTATION_v0.md:240-241 | "only level 1 needs no level datum" (default-from-absence) | B1232 retraction (2) + its adopted law |
| S8-8 | papers/P3_THE_PAPER/main.tex:793 | "the current candidate set is empty" — ambiguous vs B1228's unique named candidate; supply-side reading confirmed by T9/G4 | B1228; T9/G4 |
| S8-9 | (clean checks recorded above) | — | — |

Plus §1's instrument-output rows, verbatim, for the seat's own triage — with the noted
self-match caveat and the two THE_SPINE `OPEN` rows (B171, B1156) as the most E53-shaped
leads in the instrument's list.
