# Grammar-claims audit: what the programme actually banked, where, and what survived

**Scope**: gauge-group structure, generation counting, chirality mechanism, Weinberg-angle/coupling claims. Repo `/Users/dri/oa-audit-seat/origin-axiom`, branch `audit/b775-braver-questions` (2026-07-28). Verdict scale: **VERIFIED-COMPUTATION** (exact, test-locked, reproduced) / **PLAUSIBLE** (real computation, interpretive framing or scope caveats) / **SHAKY** (demoted, refuted, or explicitly disclaimed).

## 0. What CLAIMS.md contains (branch = origin/main, byte-identical; 229 lines)

- **Proven** P1–P68 (55 rows; gaps intentional): core algebra P1–P16, the 2026-07-03 promotion audit P17–P55, theta-model laws P56–P68. In-scope promoted rows: P30 (Jacobian eigenvalue field = Q(sqrt−3), CLAIMS.md:82), P34/P35 (amphichirality criteria, :86-87), P49 (Niven forces dual-McKay E6+E8, excludes E7 — "no physics content", :101), P50 (dim H1(pi1(4_1), Ad rho_prin) = 6 = rank(E6), exact Fox calculus, :102), P51 (E6 deformations unobstructed **to order 3 only** — **DEMOTED 2026-07-15**, beyond order 3 is CONJECTURE, :103), P54 (no C3 trace field for hyperbolic knots, :106).
- **Conditional**: C-cal (:145) — the one coupling-value-adjacent row: sealed one-shot neutrino comparison, |z|=0.02, **LOW weight** (FPR ≈ 32%), conditional on the typed-functor reading.
- **Certified data**: E8 (2I = SL(2,F5), dims = E8 marks, :175), E14 (one H1 dim per E6 exponent, :181).
- **Open**: O4 "Matter / Standard Model content" is still an open TARGET (:195). **Dead**: D1–D10 incl. D10 "theta* from CKM/PMNS is a fit, not a derivation" (:229).
- **No gauge-group, generation, chirality-mechanism, or Weinberg claim is promoted.** The grammar lives in `docs/LAW_MAP.md` (branch copy is 6 rows behind origin/main — main adds the theta-triviality scoping lemma naming the B780/B784 retractions, the CM-collapse theorem B743, cyclic-cover rank law, adjoint-tower spectrum law, e3 cubic, L39 period theorem), `knowledge/K020`, and frontier PLACEMENT rows.

## 1. Gauge-group structure

### 1a. The E6 substrate (promoted mathematics) — VERIFIED-COMPUTATION
- **Statement**: 4_1 → Q(sqrt−3) → ramified 3 → SL(2,F3)=2T → McKay affine E6 (the "atom", B266); E6 character variety exists with Kostant-exponent grading (P50/E14); E7 excluded by Niven (P49); E8 at the golden end (E8 marks, exhibit E8).
- **Computation**: exact Fox calculus (P50), hand proofs (P49, P54), exact finite-group computation (E8); all test-locked (`tests/test_b264_e6_character_variety.py`, `tests/test_b249_niven_trinity.py`, ...).
- **Audit fate**: P50/P49 survived every audit; **P51 demoted in place** (2026-07-15 audit 5.1: a mod-p Schwartz–Zippel sample was over-read; exact only to order 3).

### 1b. "E6 recurs across three faces" (the flagship structural reading) — SHAKY (formally demoted)
- **Where**: knowledge/K020 §2–4 ("One E6, three ADE hats").
- **Demotion**: **B727 self-audit** (frontier/B727_base_rate_the_structure/FINDINGS.md; error class **E20** in docs/ERROR_LEDGER.md): the McKay/Lie/CIZ faces are ONE canonically-linked ADE classification — P(recurrence | one label) = 1; {E6} is the only exceptional label reachable over an imaginary-quadratic field (no birthday problem); the sister m003 shares Q(sqrt−3) without being a knot; non-arithmetic knots (7_2, 7_3, 8_1) also surject onto 2T. **Only the atom survives as object-specific** (Reid: unique arithmetic knot). Two-seat converged; owner-visible.

### 1c. E6 → SM cascade — SHAKY (generic by its own label)
- K020 §3: the Borel–de Siebenthal chain E6 → ... → SM is "**standard (Slansky 1981) — generic E6, no figure-eight input**"; the whole-chain realization on the A-poly curve was **refuted** (B310). Object-specific content: one omega step (B305/B311).

### 1d. The banked positive gauge claim — PLAUSIBLE (placement)
- **Statement** (B714 one-sentence spine, FINDINGS.md:12-16; LAW_MAP:116-117): "the object authors a **VECTOR-LIKE E6 charged skeleton** ... it is not chiral and not the SM even at the skeleton"; native gauge system = **complex Chern–Simons of E6(C) at Q(sqrt−3)** (B715: no real form contains the holonomy — exact non-real adjoint trace; regular-unipotent meridian kills compact forms). F4 skeleton: stab(v0) = f4, dim 52 verified two seats (B670).
- **Grade**: PLACEMENT, frontier only, "Nothing to CLAIMS". The underlying computations are exact and two-seat; the physics framing is interpretive.

### 1e. G_SM — VERIFIED NEGATIVES
- **Wall 4** (LAW_MAP:150): no G_SM sector alignment of principal blocks — B604 ("the pair-to-block assignment DOES NOT EXIST": principal grading and theta-pair decomposition are incompatible; exact root census), B607/B608 (Rosetta table: 9/12 pair-combos class-mixed at root level).
- **T-NOGO-DGG theorem** (B490): the 3d–3d route cannot yield the SM (3d ≠ 4d; Gang–Yonekura flavor ≠ gauge; DGG gauge sector abelian U(1)^(2m−1)) — subsumes kills K9–K12; 14-kill catalog with the "one category off" firewall.
- **B736 Path C**: rigorous no-go — 0/24 SM parameters reduced (equivariance wall T=0; kind mismatch; bounded F2 ceiling).

## 2. Generation counting

### 2a. What is actually banked — VERIFIED-COMPUTATION
- **Statement**: h1(M; 27) = 3, inside the 3/5/1 dimension grammar; one-per-block: 27 = V17 ⊕ V9 ⊕ V1 with per-block (h0,h1) = (0,1)/(0,1)/(1,1) (B657/W0b, bit-identical reproduction); **reduction theorem** (B656/G5 + B662/A): (i1,i2) = (1,3) forced metallic-uniform ⇒ 3/5/1 for every metallic member — LAW_MAP:84 status **THEOREM (the metallic family)**. B714 rung 6 grades "generation COUNT 3" OBJECT-FORCED.
- **Source of the 3**: cohomology of the E6-27 local system on the double — **not** the Z/3 commensurator, **not** A5.
- **Audit fate**: survived; one early withdrawn version (cc2's h1=3 with an assumed lambda-sign) is logged as error-class E1 and was corrected before banking.

### 2b. "Three generations" as a permutable triple — VERIFIED NEGATIVE
- **6-prime NEGATIVE** (B714 FINDINGS.md:29-39; closed fully in B715 coda, LAW_MAP:118): (i) no Z/3 acts — Isom(4_1) = D4, order 8; (ii) the three classes are incommensurable blocks 17/9/1; (iii) the commensurator-Hecke correspondence preserves blocks, so it cannot cycle them. **Wall 6 / P54** (B307, promoted): no hyperbolic knot has a C3 invariant trace field — "three symmetric generations impossible in one object".
- **B302 (commensurator Z/3)**: the math (Neumann–Reid hidden symmetries; Eisenstein order-3 in PGL(2,O−3); index-12 cover) is VERIFIED and citable, but its FINDINGS carries an explicit fence: "does NOT derive three generations ... firewalled". Never banked as a generation claim; the symmetry route later closed (2b above).
- **Dead ancestors**: "hexagonal cusp → 3 generations" refuted (cusp is rectangular, disc −48 — B486/K8 in B490); the exact Z/3-circulant carries no hierarchy (B324/B325, K020 §confirmation); the Z/3-triality on H1(D;27) does not act (wall 7, LAW_MAP:155-157).
- **A5**: appears only as (a) the sister m003's mod-2 congruence quotient with the Out(A5) observer bit (B732), and (b) Gamma_5-prime ≅ SL(2,5) in the modular-flavor correspondence (B662/I) — a CANDIDATE FUNCTOR to flavor-model space (character equality exact; "supplies what the paradigm postulates"), awaiting the specialist bar. Neither is a generation-count mechanism.

## 3. Chirality mechanism

### 3a. Amphichirality of the object and family — VERIFIED-COMPUTATION (promoted)
- **P34/P35** (CLAIMS.md:86-87): metallic bundles amphichiral ⟺ cyclic-palindrome block sequence; general once-punctured-torus-bundle criterion; GHH-2008 basis + exhaustive certification (5460/7380 cases).

### 3b. Chirality cannot be forced — VERIFIED-COMPUTATION (scoped)
- **B145**: canonicity (minimal volume / arithmetic trace field / simplest substitution / palindromic period) coincides with self-mirror over the 39-bundle catalog; **no arithmetic chiral bundle in range**; GHH ⟺ SnapPy 39/39. **B144**: cusp-glued composites are mirror-closed (GL(2,Z) identity) — no preferred handedness from gluing; explicit-composite build honestly recorded as a tooling limit, not a confirmation.

### 3c. The object's matter is vector-like — VERIFIED-COMPUTATION
- Chiral index ≡ 0 for every single-object construction (B565-T3/B605, wall 5, LAW_MAP:151-152); sigma_omega(4_1) = 0 on the whole circle, forced by amphichirality (B713 probe 3, two-seat). **6-double-prime NEGATIVE** — "even the skeleton is not the SM's kind" (B714:41-44).

### 3d. The positive mechanism candidate — PLAUSIBLE (placement)
- **B713**: "chirality is the observer's" — a non-canonical Z/2 Galois torsor bit (fiber y²−3y+3, disc −3, simply-transitive; same V4 as the fiber functor); enters through the COUPLING. Grade PLACEMENT; the torsor computation is exact, the mechanism reading is the H0 itself.
- **Correction on record (E16)**: the level-15 Atkin–Lehner sign asymmetry read as emergent chirality was retracted — forced by even rank, generic (B695). The chirality-exclusion law (chiral bends collapse h1 5→2, B637) stands as an exact LAW.

## 4. Weinberg angle / coupling structure

| claim | where | fate |
|---|---|---|
| sin²θ_W = 3/8 from Weil 2+3 split (SU(5) reading) | speculations/S058; K2 in B490 | **REFUTED** — classical Weil reducibility (p±1)/2; no SU(5); "a fraction is matched", not an angle computed. The 2+3+4+6 decomposition itself is exactly banked (B476) as finite-group rep theory |
| 1/phi³ = 0.23607 vs sin²θ_W (2.1%); gap-edge 0.2318 (0.26%) | frontier/B558_three_level_negative/FINDINGS.md:43-53 | **named anti-numerology landmines**, both non-significant; recorded so nobody re-excites |
| golden braiding phases = Weinberg | B484 (K7 in B490) | **REFUTED** (Freedman–Larsen–Wang density) |
| Cabibbo ≈ 9/40 | B706 (LAW_MAP:145) | **dead** — wrong field, no mechanism, rung-4 rational |
| C-cal neutrino one-shot | CLAIMS.md:145 | survives as **CONDITIONAL, LOW weight** (FPR ≈ 32%), honestly labeled |
| golden-exact unistochastic mixing P = [[phi/sqrt5, 1/(phi·sqrt5)],...] | B753 | VERIFIED-COMPUTATION, **program-internal only** — explicitly no SM comparison (stopping rule) |
| m_b = m_tau (27³ Yukawa) | B714 rung 4 | graded FORCED-**GENERIC** (any E6-27 setup), not object-specific |

## 5. The named probe directories (B8, B84, B86, B88, B144)

- **B8_particle_spectrum**: mass² = kappa·sqrt5 exact from P16; the m/g ≈ phi near-miss (0.4% off) **explicitly disclaimed** and recorded "so it cannot later be mistaken for a result"; verdict STALLED. — honest, survived.
- **B84_sl5_gauge_barrier**: "gauge" here = gauge/basis ambiguity in the SL(5) Jacobian limit, NOT physics; the author's own conjecture I1 **refuted** (genuine non-convergence). VERIFIED-COMPUTATION (exact F_p), no Origin-core claim.
- **B86_unification_synthesis**: SL(n) tower synthesis; "**the physics chapter is closed**" — every bridge reduced to invariant theory; novelty labels APPARENTLY_NEW pending external check.
- **B88_sl4_census**: degrees {3,4} at rank 4, honest completeness caveat. No core claim.
- **B144_interaction_chirality**: see 3b.

## 6. Later audits — the correction machinery that touched grammar claims

docs/ERROR_LEDGER.md (26 classes): **E20** (B727 — structure-skepticism lagged number-skepticism; the flagship E6 recurrence generic), **E16** (chirality over-read retracted), **E17** (swap/weld hearing conflation corrected), **E1** (withdrawn early h1=3 variant), **E19** (adjudication-by-citation corrected in B724), **E21–E23** (congruence-level thread corrected twice, then convention rule), **E25/E26** (PSLQ false-witness rule; trace-blind negatives → B773 recompute). The 2026-06-15 self-audit had already down-tiered **P10** (only the trace-3 sieve proven) and **B95** ("forced" only under the ansatz). B792's gate seat struck an H0 scope-import sentence from the SM-null write-up ("cite scopes, not headlines") and required a late-seal admission — the discipline is live this week.

## 7. Net assessment for B793

What survives as load-bearing grammar: (1) exact E6-substrate mathematics (P49/P50/E14, the atom B266); (2) **h1 = 3** as a theorem-grade count with the explicit warning that it is a count, never a permutable triple; (3) vector-like/amphichiral matter with chirality relocated to the coupling as a Z/2 torsor bit; (4) the wall system (no G_SM alignment, T-NOGO-DGG, scale-torsor no-go, equivariance wall, kind mismatch discrete-vs-continuous); (5) the coupling thesis itself (H-EAR: being is what the object says, hearing is what a coupled listener receives), now reinforced by the B792 Maass clean null. Every positive SM identification ever attempted is dead, and each death is documented with its mechanism — which is exactly the specification sheet for B793's coupling models: they must supply scale, continuum, compactness, chirality, and generation-mixing from the observer side, under sealed-prereg base-rate protocol, without re-claiming what the walls forbid.

## KEY FACTS (structured)
- CLAIMS.md is byte-identical on audit/b775-braver-questions and origin/main (git diff empty, 229 lines both). It contains 55 proven claims P1-P68 (gaps intentional), conditionals C-cal + C1-C12, certified data E1-E17, open targets O1-O9, dead claims D1-D10. NO gauge-group, generation-count, chirality-mechanism, or Weinberg-angle physics claim is promoted anywhere in it; O4 'Matter / Standard Model content' is still an OPEN target (CLAIMS.md:195).
  - source: CLAIMS.md:1-229; git diff origin/main -- CLAIMS.md (empty)
- The banked gauge-structure claim is: the object authors a VECTOR-LIKE E6 charged skeleton whose native gauge system is complex Chern-Simons of E6(C) at Q(sqrt-3) — explicitly NOT compact Yang-Mills and NOT G_SM. Grade: PLACEMENT (frontier), never promoted.
  - source: frontier/B714_physics_spine/FINDINGS.md:12-16; docs/LAW_MAP.md:116-117 (B714/B715 rows)
- The E6 mathematical substrate that IS promoted: P49 (Niven forces dual-McKay E6+E8, excludes E7 — 'no physics content'), P50 (dim H1(pi1(4_1), Ad rho_prin)=6=rank E6, exact Fox calculus), P51 (E6 deformation unobstructed to order 3 — DEMOTED 2026-07-15: beyond order 3 is CONJECTURE), E8 (2I=SL(2,F5), dims=E8 marks), E14 (one H1 dim per E6 exponent).
  - source: CLAIMS.md:101-103,175,181
- The flagship 'E6 recurs across McKay/Lie/CIZ' structural claim was DEMOTED by self-audit B727 (2026-07-20): the three faces are one canonically-linked ADE classification (P(recurrence|one label)=1); E6 is the only exceptional label reachable over an imaginary-quadratic field; sister m003 shares Q(sqrt-3) without being the knot; non-arithmetic knots also surject onto 2T. Only the atom stands: Q(sqrt-3) is the trace field of the unique arithmetic knot (Reid/B266). Logged as error class E20.
  - source: frontier/B727_base_rate_the_structure/FINDINGS.md:10-68; docs/ERROR_LEDGER.md (E20 row)
- The E6->SM cascade (E6 -> SU(6)xSU(2) -> trinification -> ... -> SM) is explicitly labeled 'standard (Slansky 1981) — generic E6, no figure-eight input'; the whole-chain realization on the A-polynomial curve was refuted (B310). Object-specific content is one step: trinification grading eigenvalue omega in Q(sqrt-3) (B305/B311).
  - source: knowledge/K020_structural_theorem_galois.md:39-47
- G_SM negatives are walls: no G_SM sector alignment of the principal blocks (B604: 'the pair-to-block assignment DOES NOT EXIST' — principal grading and theta-pair decomposition are incompatible; B608: 9/12 pair-combos class-mixed at root level); T-NOGO-DGG theorem (B490): the 3d-3d route cannot yield the SM (3d not 4d; flavor not gauge; abelian gauge U(1)^(2m-1)); B736: 0 of 24 SM parameters reduced, no G_SM landing site.
  - source: frontier/B604_rosetta_blocks/FINDINGS.md:1-33; frontier/B490_the_no_go/FINDINGS.md:41-53; docs/LAW_MAP.md:138,150
- The generation-count claim is exactly: h1(M;27)=3 (with the 3/5/1 dimension grammar) — a machine-verified exact computation on two objects, upgraded to THEOREM for the metallic family via the (i1,i2)=(1,3) reduction (B656/G5 + B662/A), with one-per-block refinement 27=V17+V9+V1 (B657/W0b). It comes from cohomology of the E6 27 local system, NOT from the Z/3 commensurator and NOT from A5.
  - source: docs/LAW_MAP.md:84; frontier/B657_invariant_line/FINDINGS.md (W0b); frontier/B714_physics_spine/FINDINGS.md:27
- 'Three GENERATIONS' (permutable triple) is a banked NEGATIVE (6-prime): no Z/3 acts on the object (Isom(4_1)=D4, order 8); the three classes are incommensurable blocks 17+9+1; the commensurator-Hecke residual was closed in B715 coda; wall 6: no hyperbolic knot has a C3 trace field (B307, hand proof, promoted as P54). The B302 commensurator Z/3 is verified math but its generation reading was always firewalled and never banked.
  - source: frontier/B714_physics_spine/FINDINGS.md:29-39; docs/LAW_MAP.md:118,153-157; frontier/B302_multiplicity_hidden_z3/FINDINGS.md (the fence); CLAIMS.md:106 (P54)
- The chirality mechanism banked is a NEGATIVE + handoff: the object is amphichiral and vector-like (chiral index 0, B565-T3/B605; sigma_omega=0 forced); canonicity coincides with self-mirror (B145 — no arithmetic chiral bundle in range); cusp-glued families are mirror-closed (B144); chirality is the OBSERVER'S non-canonical Z/2 Galois torsor bit entering through the coupling (B713, PLACEMENT). Amphichirality criteria are promoted theorems P34/P35 (GHH-based, exhaustively certified).
  - source: docs/LAW_MAP.md:115,151-152; frontier/B145_forced_chirality/FINDINGS.md:1-40; frontier/B144_interaction_chirality/FINDINGS.md:19-33; CLAIMS.md:86-87
- An attempted emergent-chirality signal (opposite Atkin-Lehner signs w3=+1, w5=-1 at level 15 read as bifocal c-breaking) was RETRACTED: forced by even rank, generic elliptic-curve fact — error class E16, owned in B695.
  - source: docs/ERROR_LEDGER.md (E16 row)
- All Weinberg-angle claims are refuted or flagged: sin^2(theta_W)=3/8 from the Weil 2+3 split is 'numerology (refuted)' — classical Weil reducibility, no SU(5) present (S058; K2 in B490); two persistent near-misses (1/phi^3=0.23607 at 2.1%; a gap-edge ratio at 0.26%) are recorded as named anti-numerology landmines, both non-significant (B558); braiding->SM gauge killed by Freedman-Larsen-Wang density (K7/B484).
  - source: speculations/S058_representation_branching_verdict.md:43-49; frontier/B558_three_level_negative/FINDINGS.md:43-53; frontier/B490_the_no_go/FINDINGS.md:21,26
- The only surviving coupling-value-adjacent ledger row is C-cal: a sealed one-shot neutrino-sector forward comparison consistent at |z|=0.02 but at LOW evidential weight (achieved-precision false-positive rate ~32%), conditional on the typed-functor reading — honestly labeled, unpromoted beyond conditional.
  - source: CLAIMS.md:145
- B792 (current, on this branch): first 17 Maass eigenvalues of m004 computed; Gamma_41 proved congruence of level (4) (SL-kernel convention, E23) with the mod-4 trace law; pre-registered SM comparison = CLEAN NULL at 8-digit precision (39 raw candidates, 0 survive surrogate base-rate gates). The gate seat struck an H0-scope-import sentence: the spectral null may not borrow B713-B716's authority ('cite scopes, not headlines'); the protocol was pre-specified but sealed late.
  - source: CC3_TO_CC_2026-07-28_last_door_closed.md:1-59; CC_TO_CC3_2026-07-28_sm_null_gated.md:19-45
- The probes named in the task are SL(n)-tower mathematics, each explicitly 'no Origin-core claim': B8 = the m/g≈phi near-miss explicitly disclaimed and STALLED; B84 = the author's own conjecture I1 refuted (SL(5) barrier is genuine non-convergence); B86 = synthesis with 'the physics chapter is closed'; B88 = SL(4) census, degrees {3,4}, completeness caveat; B144 = mirror-closure identity (firewall extends structurally).
  - source: frontier/B8_particle_spectrum/FINDINGS.md:44-46; frontier/B84_sl5_gauge_barrier/FINDINGS.md:27-41; frontier/B86_unification_synthesis/FINDINGS.md:38-41; frontier/B88_sl4_census/FINDINGS.md:1-5; frontier/B144_interaction_chirality/FINDINGS.md:19-33
- docs/LAW_MAP.md on the audit branch is 6 rows BEHIND origin/main: main additionally has the cyclic-cover rank law (B489/B785), golden adjoint-tower spectrum law, the theta-triviality scoping lemma (naming the B780/B784 retractions), the CM-collapse theorem (B743: real SM-ratio content collapses to Q(sqrt5)), the e3 cubic, and the L39 period theorem.
  - source: git diff origin/main -- docs/LAW_MAP.md

## CONSTRAINTS FOR B793
- Scale/value constraint (WALL, theorem-grade): only exact dimensionless algebraic observables are typeable — the scale-torsor no-go (docs/LAW_MAP.md:172-188, B660/S3 upgraded B666 cell S) forbids any coupling model that outputs masses, VEVs, Lambda, or running couplings AS VALUES from the object side; scale must enter as an explicit observer-side input (e.g. Henneaux-Teitelboim-type integration constant).
- Kind constraint: the object supplies DISCRETE Galois/F2 bits (bounded observer menu, B733; docs/LAW_MAP.md:136,145); the SM's freedom is ~19 CONTINUOUS parameters (B706, docs/LAW_MAP.md:145). Any B793 coupling model must explicitly supply the continuum (RG scale, moduli, thermal beta, Dehn slope) and state which side owns it.
- Equivariance constraint (WALL): no nonzero linear monodromy-equivariant map classical->stage exists (T=0 exact, docs/LAW_MAP.md:167-171; B736 confirms no G_SM landing site). Couplings must be group-functorial/typed (mod-conductor composed with characters, B644/B650), never module-linear.
- Chirality constraint: the object is provably vector-like (chiral index 0, B565-T3/B605, docs/LAW_MAP.md:151-152; sigma_omega=0 forced by amphichirality, B713). A B793 model must GENERATE chirality in the coupling — the banked candidate mechanism is the observer's non-canonical Z/2 Galois-torsor basepoint choice / c-swap breaking (B713/B723); this is unbuilt (the 'c-breaking of measurement' upgrade path).
- Generation constraint: the object gives generation COUNT 3 only — h1(M;27)=3 as incommensurable blocks V17+V9+V1 (B657/W0b), NOT a permutable triple: no Z/3 acts (Isom=D4), no C3 trace field exists for any hyperbolic knot (B307), commensurator-Hecke route closed (B715 coda). A coupling model must supply the inter-generation mixing/degeneracy structure itself and may not claim an object-side family symmetry.
- Gauge-group constraint: the object's native gauge structure is COMPLEX Chern-Simons of E6(C) at Q(sqrt-3), vector-like, non-compact (B715); no real form embeds (exact adjoint-trace computation). No G_SM alignment of the principal blocks exists (B604/B607/B608, docs/LAW_MAP.md:150), and the DGG/3d-3d route to the SM is closed by theorem (T-NOGO-DGG, B490). A B793 model must supply the compact slice and the gauging, and must not re-derive E6->SM cascades as object-specific (Slansky-generic, K020 §3; B727/E20 base-rate demotion).
- Field-arithmetic constraint: hearing/Q(sqrt5)/phi content is COUPLING-borne (H-EAR four clauses, docs/LAW_MAP.md:51; terminal no-go B685: the object generates being Q(sqrt-3) only; level 15 = 3(object) x 5(coupling)). Born-content ledger (B725-B729): form Q(sqrt-3) + probability weights Q(sqrt5) are native; amplitudes Q(sqrt(2+phi)) and interference phase Q(zeta5) are IMPORTED overlays — a coupling model must declare which quantum content it imports and from where.
- Spectral constraint: the Maass spectrum is a clean base-rate-calibrated null vs SM values at 8-digit precision over 17 eigenvalues (B792); comparisons at higher precision are open but gated. Do not cite H0 across object classes — 'cite scopes, not headlines' (CC_TO_CC3_2026-07-28_sm_null_gated.md:19-31): B713-B716 negatives scope the character variety/torsor/tower, not automatically every new object.
- Protocol constraints (hard, house-enforced): sealed prereg file with sha256 in docs/SEAL_LEDGER.md BEFORE compute (unsealed pre-specification caps citability — B792 lesson); surrogate-null base-rate gates per B743 rules (>=50 surrogates, p<0.02, coefficient-height-aware PSLQ per E25); MB12 vacuity check of every gate; two-seat verify-don't-trust on load-bearing computations; negatives must compute the discriminating fact in-sandbox (E19), and check chord-level/non-abelian sectors before banking trace-level absence (E26); stopping-rule record: SM-value comparisons reopen only via owner + full checklist (docs/LAW_MAP.md:109).
- Base-rate-of-structure constraint (E20): before treating any structural recurrence (ADE labels, small groups, small integers) as object-specific, compute P(recurrence|one label), check catalogue size, and run the sister-m003 control — only content a comparable same-field object does NOT share is object-specific (B727 standing rule).

## OPEN HOOKS
- P51 residue: smoothness of the E6 deformation space beyond order 3 is explicitly [CONJECTURE] after the 2026-07-15 demotion (CLAIMS.md:103).
- B715 upgrade path: 'the compact slice the geometry does not supply' — what turns complex CS E6(C) into a compact gauge sector is exactly a coupling-model question for B793.
- B713 upgrade path: 'the c-breaking of measurement' — the coupling-side chirality mechanism (observer breaks the c-swap by choosing a broken vacuum, B723) is named but unbuilt.
- B670 cheap cell: the F4-refined dimension grammar (h1 = 1+2 under F4(v0)) is priced and unrun; the 'every metallic' F4-form generalization is plausible via B662/A but not written down (docs/LAW_MAP.md:86).
- B662/I Gamma_5-prime correspondence: the hearing rep IS the modular-flavor 2-hat-prime doublet (character equality on all 9 classes); the upstream claim 'the framework derives what the flavor paradigm postulates' awaits the specialist bar (R21-7) — the one live positive-shaped bridge to flavor model space (docs/LAW_MAP.md:77).
- B792 residuals: mult-2 parent-form projection test; 20+-digit precision and 50+-digit algebraicity comparisons untested both directions; the r8863-is-parent prediction (CC_TO_CC3_2026-07-28_PREDICTION_r8863_is_parent.md) pending.
- B719 open control: the h=3 being-filter on arithmetic children stands as observed (4/4) but its inheritance control is OPEN (API-degraded run).
- E26/B773: 4 banked negatives flagged TRACE-BLIND-RISK (computed in projections invisible to the theta-odd chord) — recomputation launched as B773; relevant before any B793 model leans on those negatives.
- B736 open theorem: object-level-observer non-existence for the infinite non-abelian Bianchi tower — both seats flag OPEN, no known route.
- Housekeeping: docs/LAW_MAP.md on audit/b775-braver-questions lacks 6 rows banked on origin/main (incl. the theta-triviality scoping lemma and CM-collapse theorem); B793 planning should read origin/main's copy.
