# Changelog

All notable changes to the Origin Axiom repository are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/); this project is pre-1.0 and
not yet versioned for release. Detailed working history lives in `PROGRESS_LOG.md`.

---

## 2026-07-12 — B527: the complete Stein-compatible metric cone (chat3) — narrows the B526 no-go

- chat3 package classifying the metrics for which M_* is a positive Stein evolution. **Independently
  recomputed** (own E_s basis + Lyapunov operator): M|E_s stable; the Lyapunov operator 𝓛(S)=S−M̄ᵀSM̄ is
  invertible → **𝓒 = 𝓛⁻¹(PSD(3)) is a 6-dim cone** of Stein-compatible spatial metrics, non-polyhedral (ℝP²
  of extreme rays) → **Stein compatibility alone cannot select a metric**. The Lorentzian completion
  G_{S,α}=S−αℓℓᵀ is (3,1) and Stein-positive (dim 7 w/ time normalization); α is a unit choice
  (T_cᵀG_{S,1}T_c=G_{S,c²}); the four letters are not equivalent null rays (4 distinct α_i).
- **The affine tetrahedral metric S_aff is Stein-compatible (interior of 𝓒)** — verified Q_aff PD. So its
  distinction is affine isotropy, not Stein. **This NARROWS [[B526]]:** B526's no-go was specific to the
  *Perron-weighted* S_tet (driver signature (2,1), ∉ 𝓒); it is **not** a general isotropy–Stein obstruction,
  and "M_* = renormalization" is one option, not forced. Metric verdict: **compatibility YES, selection
  OPEN.** Consistent with PHYS-REFUTED. Next gate = LOCALITY (the Rauzy contact automaton). Lock
  `test_b527.py` (3 pass).

## 2026-07-12 — B525: the "Are You Sure" audit cracked 3 of 10 banked negatives (corrections applied)

- Owner-mandated 61-agent adversarial audit of the program's load-bearing NEGATIVES. **4 CONFIRMED, 2 SHAKY,
  3 CRACKED.** Meta-pattern: every failure = a necessary/cited/proxied condition read as sufficient; the tell
  = the certificate *asserted/cited/posited/logged-timeout* the discriminating fact instead of computing it
  (the 4 that recomputed survived). New memory: [[compute-the-discriminating-fact]].
- **The master negative PHYS-REFUTED CONFIRMED** (recomputed): the object still does not produce physics.
- **CRACKS corrected this session:** (1) **B519 "no external crossing" RETRACTED** — gap-labeling is
  necessary≠sufficient; the mixed-chain gap-**opening** pattern (B1) is a genuinely falsifiable external
  prediction, not a known-theorem corollary (B519 VERDICT + docs/CLOSURE_2026-07-11 corrected). (2)
  **C3-CONE:** the conclusion survives on the signature grounds, but `c3_malament.py` had a sign-convention
  bug (zero eigenvalues → "spacelike") — fixed; the "causal ⟺ evolution verb" nugget retracted. (3)
  **CHILD-NOTSHORT downgraded to PROVISIONAL:** only 115/150 words analyzed (26 bare TIMEOUTs), not 141/9 —
  the KILL is not complete. Locks `test_b523.py`, `test_b500_kill.py` corrected.
- **SHAKY follow-ups:** DGG-ABELIAN ("abelian at every K" is a citation, not computed); GATES-SEALED
  (`verify_gates.py` posits rather than derives the deck action) — conclusions hold, certificates to harden.

## 2026-07-12 — B526: verified the "UNDENIABLE PHYSICS CROSSING" package — title misleading, no crossing

- An owner-uploaded package with an alarmist name turned out to be the **opposite of a crossing claim**: its own
  verdict is "no remaining internal path to an undeniable claim about nature" (prereg: `claim_level:
  structure_only`, `claims_md: forbidden`, crossing requires the external blind test). It **reinforces
  PHYS-REFUTED**, not overturns it.
- Two technical results **independently recomputed** (numerical eigenvalues, from scratch — not by re-running
  their script): (1) the **canonical tetrahedral spatial metric** S_tet = D_r⁻¹(I−¼𝟙𝟙ᵀ)D_r⁻¹ (rank 3, kernel
  = r, Gram = regular tetrahedron) — canonical *conditional on* an imposed 4-letter isotropy the object does
  not force; (2) the **isotropy–Stein no-go**: G_iso (3,1) but W_iso = G_iso−MᵀG_isoM is not positive definite
  (obstruction on E_s: W_stable (2,1), det<0). **Adversarial check:** the no-go is real — W_iso(r,r)>0 (not
  "β>1"), M|E_s spectrally contracting yet W_stable indefinite ⟹ **non-normality**. RG exponents ω_h, ω_γ,
  exp(2π/Ω)=27.2366… exact but not-yet-physical (correctly flagged).
- Banked as STRUCTURE, firewalled; the reframing (M_* = renormalization, time = separate local unitary) is a
  permitted hypothesis, not a theorem. Lock `test_b526.py` (4 pass).

## 2026-07-12 — B524: the two actionable next steps done properly (iwip certified; higher-rank Ptolemy)

- **Part 1 — iwip / word-hyperbolic CERTIFIED.** Coulbois' `train_track` (Bestvina–Handel), validated on
  known iwip/non-iwip cases first, gives **φ is iwip** for φ:a→abccd,b→acd,c→abcd,d→ac (our F₄ automorphism
  relabelled). λ(φ)=3.6762=β but **λ(φ⁻¹)=3.0523** — verified *independently* of train_track by word-length
  growth (free reduction; inverse formula confirmed) ⟹ φ **not geometric** (Handel–Mosher) ⟹ **word-hyperbolic**
  (Brinkmann) and, by **Stallings**, **not a 3-manifold group**. *(Correction: an earlier draft's cd=2 and
  no-ℤ² arguments were invalid — owner-flagged; the correct argument is Stallings' fibration theorem, resting
  on the verified λ asymmetry.)* Group-theory question fully settled: iwip yes, hyperbolic yes, manifold no.
- **Part 2 — higher-rank Ptolemy of 4₁.** SnapPy ptolemy: SL(2)→1 rep (ℚ(√−3)); **SL(3)→4 reps, ℚ(√−3) AND
  ℚ(√−7)** (the √−7 echoes B479's held-breath order-3 torsion); SL(4) deferred (Magma-recommended). Higher
  rank enriches *arithmetic*, but the DGG gauge group is **abelian U(1)^{r_K} at every K** (Dimofte–Gabella–
  Goncharov) — nonabelian gauge is not reached, extending **T-NOGO-DGG (B490) to all ranks**. Lock
  `test_b524.py` (3 pass, incl. the independent λ check); reproducers in the sage env self-assert.

## 2026-07-12 — B523 addendum: the corrected train-track handoff (fix real, iwip uncertified)

- The exploration seat's corrected substitution **φ: a→abAAB, b→aAB, A→abAB, B→aA** verified: **injective**
  (fixes the prior non-injective bug) and **abelianizes to the bootstrap matrix** (char poly x⁴−2x³−5x²−4x−1,
  det −1, primitive, Perron β=φ(1+√φ)) — the Level-1 free-group substitution carries the same β as B517. **[MATH]**
- **But "φ is iwip / word-hyperbolic" is NOT established:** the five tests are abelianization-primitivity
  (necessary, not sufficient); the certificates (Whitehead for Aut(F₄); Bestvina–Handel for iwip) were not run.
  The hyperbolic/atoroidal/CAT(0)/Menger consequences are **conditional** → NEEDS-CERTIFICATE (specialist).
- **T[4₁]/DGG bridge**: correctly cited as external, but its gauge group U(1) is *exactly* the abelian gauge
  **T-NOGO-DGG (B490)** already closed — no route to SM gauge, does not reopen B490. The two owned bugs
  (volume Bloch–Wigner branch; Kashaev asymptotic) are correctly self-caught. Lock `test_b523.py` (5 pass).

## 2026-07-11 — B500 child hunt: depth-5 KILL ("the child is not a short word")

- A stale ~18h streamed hunt (`hunt_d5.py`, wedged on a `gp` subprocess) was killed; its results banked.
  **141/150** depth-5 all-three-verb words solved, **zero hits** (no d_K=−283, no field isomorphism, airlock
  never fired). Pre-registered **KILL fires**: the object does not generate its own child field by any
  depth-≤5 verb word. The words produce generic wild symmetric Galois groups (S₅–S₁₁); the 9 unfinished are
  the double-decimation tail (degree ~9280, `gp` tool-blocked). Corroborates the two-seat closure — generic
  arithmetic, not special values. Lock `test_b500_kill.py` (2 pass).

## 2026-07-11 — B523: the wrong-leap re-examination (no leap found) + a broken Level-1 handoff

- **B523 (S2):** treated the program's own negative as the thing to break; 5 cells recomputed + classified.
  **No wrong leap.** The one UNTESTED-RESIDUAL, **C3/Malament**, was run: the four banked verbs carry four
  different causal types — only the unimodular **evolution** verb yields a proper (3,1) Lorentzian cone;
  decimation → (2,2)/inverted, TM/erasure → det-0 degenerate. The Level-1 monoid preserves **no single
  causal cone** → Malament n/a → the (3,1) is evolution-only and generic. **Confirms the negative.** Nugget
  (firewalled): causal structure ⟺ the evolution (measure-preserving) verb.
- **Incoming Level-1 free-product/genus-2 handoff — verified, partly broken.** SOUND: the direct-product
  obstruction (F₂×F₂ irreps tensor-factor) + |γ|=1/√φ exact. BROKEN: the stated substitution is NOT an
  automorphism (φ(b)=φ(B)=aA, non-injective, det=0 not −1) → the genus-2 "spacetime" does not follow. No new
  door as stated; B515–B517 untouched. Lock `test_b523.py` (4 pass).

## 2026-07-11 — audit reconciliation: integrate-don't-merge + the two-seat closure

- **Parallel closure audit checked before merging (owner directive).** Fable-5's Closure Campaign
  (`oaudit/`, `closure/phase1-duels`) finished with an independent negative closure (four gates
  SEALED/REDUCED/CLOSED; Origin Postulate REFUTED-AS-STATED) that **collides on 8 B-numbers (B496–B503)**.
  Resolution: **integrate, don't merge** — deliverables recorded on this trunk under new numbers, each
  verified by independent recomputation; audit branch stays historical.
- **B479 erratum (F4):** d=5, d=7 held-breath fields were mislabelled ℚ(√41), ℚ(√−239); both integers are
  the *norm* of the discriminant, not the field (d=5 → degree-4/ℚ(√5); d=7 → degree-6/no quadratic subfield).
  Verified independently; corrected in B479 + `SPECIALIST_NOTE_R1` + B491.
- **R1 held-breath → COROLLARY** of Cantat's fixed-locus method (control ℚ(√17) reproduced; completeness now
  unconditional). B491 downgraded APPEARS-NOVEL → COROLLARY.
- **B521 — audit gate seals + R2 prediction, integrated.** Gate A disc −15, Gate B θ=Out(E₆)=ℤ/2, **Gate C
  CLOSES** (ℤ/3 = trinification within one 27, not generation — Fix=0 recomputed in full), Gate D data.
  **R2 blind prediction HIT** verified (pre-committed, sha256-pinned, 0 mismatches) — the object predictively
  produces its *own arithmetic*, not physics values.
- **B522 — tower filtration theorem (SHARPER-REDUCTION):** the Sym⊗det block form is forced for all n
  (dynamics eliminated); n=5 wall located; cores recomputed (character layer, carrier dims n≤4, μ_d).
- **`docs/CLOSURE_2026-07-11.md`** — the unified two-seat terminal document (supersedes CLOSURE_2026-07-05/10
  + B519 VERDICT). Locks: `test_b479_erratum.py`, `test_b521.py`, `test_b522.py` (9 pass). Firewall untouched.

## 2026-07-11 — the golden-3d arc + the whole-repo synthesis

- **B511 physics-verdict campaign:** five of six doors CLOSED (D5 generation=generic-Chebyshev;
  D3 measure=classicalizes/wild-suppressed; D6 signature; D2 time-tower=Mostow triple; D4 gauge=Sₙ
  generic). **D1 REOPENED** (golden 3d, below); verdict correctly suspended.
- **Golden 3d (B515–B517, P015/P016):** coupling two Fibonacci copies F-equivariantly forces the unique
  Pisot inflation β=φ(1+√φ) → a 3d golden Rauzy fractal (constructed). Intertwining THEOREM (cross-seat,
  re-derived): the Pisot bound makes the coupling (F,F²) exhaustively unique. Golden-specific; the
  "double" is selected not assumed; the reading done. Firewall HELD: the "3" is a Rauzy dimension, not
  physical space. Two premature self-kills caught by owner pushback. Novelty: APPEARS-NOVEL (β, the
  construction, the forcing, the anyon link), NEEDS-SPECIALIST. Lorentzian (3,1) real but GENERIC.
- **K025 — whole-repo synthesis:** the root generator named (golden cat map A over ℤ[φ]); the firewall
  is ONE theorem (the two ends' product = the generic seam ℚ(√−15) = the un-paired κ); two ingredients
  genuinely already-present (dynamics; the anchor as scale-by-embedding = a scale-free universality
  class); the absorbing-loop caveat. Registered T-ONE-ROOT/T-HELD-SLOT.


## 2026-07-08/10 — the papers verdict, the no-go theorem, and the monoid opens

- **Papers:** P4 stands (arXiv-style, gauntlet-cleared twice); P1–P3 **frozen as internal notes**
  after three non-converging adversarial re-panel rounds (the math reproduces; the prose kept
  overclaiming — the records are `papers/SCRUTINY_P1P3*.md`). Banked correction: B479's d=5
  held-breath field = degree-4 over ℚ(√5), not ℚ(√41).
- **B490 T-NOGO-DGG:** the SM kills become ONE theorem (3d≠4d; flavor≠gauge; abelian U(1)^{N−c}).
- **B491:** the held-breath law + the seam broken-lattice = APPEARS-NOVEL / NEEDS-SPECIALIST.
- **THE MAP:** the σ-rooted synthesis (14 layers, all bricks classical-cited, the assembly novel);
  grounded figures; lit-gated.
- **The monoid arc (B496–B498):** Thue–Morse enters (the singular verb; foliation destroyed except
  κ=2; the Eisenstein field survives the cancellation). **B497:** End(F₂) = four strata + two
  universal laws (κ=2 absolutely conserved; the classical floor is toral); the singular-verb
  geometry dichotomy (BS(1,2) vs hyperbolic-geometry-less); the measurement algebra
  M Fᵏ M = F_{k+3}·M; the interaction program launders (honest Phase-Z verdict). **B498:** mixed
  words — MFM the unique mirror-restoring word; E[log mult_D] = −2 PROVED; E[log mult_M] = 0 to 26
  digits; the golden monopoly exact at depth 2 (depth-3 computing).
- **Ops:** B470 Reflection Campaign closed; lens probes closed (B480+B492); the Closure Campaign
  (parallel seat) reviewed read-only, numbering deconflicted (B493–B495 theirs, B496+ ours).


## 2026-07-05 — THE CHILD PROGRAM (C0–C3) + the interface arc + a repo audit

- **The interface arc (B426–B434).** The 2026-07-05 handoff adjudication and the Origin Postulate
  (`philosophy/THE_ORIGIN_POSTULATE.md`): `D:object→physics` lives at the **interface**, not the
  interior. B426 the scale-lever closed form (`env₄₅/env₁₅ ∈ ℚ(ζ₉)⁺`, √5-free) + the Galois-orbit
  contraction theorem; B427 exchange acts by the Galois element σ₁₇ (fixes √−15); B428 the two
  bosonic spin walls (three-seat agreed); B429–B433 bosonic rigidity, the sl2 landscape, the seam
  split, filling chirality (all fillings chiral; the forced output exits ℚ(√−15)), the 3d–3d DGG
  calibration (eliminant = −A_CL(M,L)·A_CL(M,−L)); **B434 slope selection** — ±5 = the boundary of
  the maximal exceptional set `{0,±1,…,±4}`, so the forced child = the **Meyerhoff manifold
  `4₁(5,1)`** (H₁=ℤ/5, trace field `x⁴−x−1`, disc −283).
- **THE CHILD PROGRAM, C0–C3 (B435–B440).** Study the forced child and test *"the SM is what the
  object produces, not what it contains"* against the four-part emergence bar.
  - **C0 (B435):** H₁=ℤ/5; the abelian E₆ vacuum count derived = **26** (25 nontrivial + trivial).
  - **C1 (B436):** the Borel identity EXACT — `vol = 12·|d|^{3/2}·ζ_K(2)/(4π²)³` to `4.5×10⁻⁶⁴`.
  - **C2 (B437):** the "golden return" **retracted** as inheritance (numerator-forced; trefoil
    control) → **THE INVERSION LAW** banked.
  - **B438 (the audit's decisive catch):** B436/B437 had skipped the pre-registered FOREIGN
    control; run — `5₂(5,1)` shares the child's −283 field **and** its 121 torsion value ⇒ the
    Inversion Law is **three-tiered** (numerator-forced / commensurability-shared / unique = ∅).
  - **C3 (B439/B440):** the child's SL(2,C) vacuum book. The child has **4 irreducible vacua all in
    the −283 field** (= its own trace field), by two independent methods that agree exactly
    (Cooper–Long A-poly on `L=M⁻⁵` and the closed-manifold character variety). Verdict — **no
    figure-eight-unique feature**: 4₁ and its commensurability neighbour 5₂ **both have 4
    irreducible vacua in the identical −283 field** (adversarial review corrected the first cut —
    the golden ℚ(√5) factor is the *reducible* abelian ℤ/5 characters, universal across all
    K(5,1); the "golden inversion" reading was a parametrization artifact, retracted). Surgery
    launders identity down to the SL(2) vacuum count — a cleaner, stronger negative.
- **Repo audit (`docs/AUDIT_2026-07-05.md`).** Three auditors + a cross-chat audit reconciled:
  the B438 correctness catch; hygiene (B435/B437 wording, the S042/S043/S044 file collisions
  renumbered to S050/S051/S052 with the CATALOG re-indexed); the e₃ `triple_cubic.json` snapshot
  stamped UNSTABLE (unconverged CRT — not the answer); the LEAD_REGISTER/board refreshed; a leads
  re-score (Cluster A metallic A-poly, L54 gate-A torsion, e₃ now-unblockable).
- Emergence bar **not cleared** anywhere; every physics-shaped reading firewalled to
  `speculations/` + `philosophy/`; nothing to `CLAIMS.md`. Locks: test_b426–test_b440 all green.

## 2026-07-04 — B425: two E₆ torsions (dynamical-golden + geometric-Eisenstein)

- **Correction + new result.** Verified a cross-chat catch: B423's golden "E₆ torsion" is the
  **dynamical zeta** of the homological monodromy A (golden by construction), not the geometric
  torsion its prereg claimed. **B425** computes the geometric Reidemeister torsion at the
  discrete-faithful holonomy ρ_geo (u=ω forced by the relator): **Eisenstein** — rational
  coefficients (√−3 cancels, Galois-invariant at all six E₆ exponents), adjoint **−3 = disc
  ℚ(√−3)**, reproducing banked V30/V31 (Porti form) by a third method. The two torsions (−5
  golden, −3 Eisenstein) realize the double-uniqueness cornerstone as two computed discriminants
  meeting at √−15. Emergence bar not cleared (Eisenstein arithmetic, not SM).
- Guard: the raw Fox eigenvalue-product (−25−13ω, "prime 67") is a presentation artifact, not an
  invariant (rational for ∂r/∂a; t-dependent). The invariant is −3.
- Files: `frontier/B425_geometric_torsion/`, `frontier/B423_gateB_torsion/CORRECTION.md`,
  `tests/test_b425_geometric_torsion.py`; corrections in `knowledge/THE_GOLDEN_CAT_MAP_PRINCIPLE.md`
  and `papers/P2_trinity/` (ABSTRACT/OUTLINE/THEOREMS) + `papers/REPRODUCIBILITY_LEDGER.md`.
  Nothing to CLAIMS (firewalled).

## 2026-07-03 — the promotion audit (GOVERNANCE §5.1) executed

- **+39 `proven` (P17–P55), +7 `conditional` (C6–C12), +15 certified-data (E1–E15)** promoted from
  the frontier through the §5 gates (63 candidates adjudicated, 281 lock tests verified standalone,
  6 held with reasons; scrutiny record in `PROGRESS_LOG.md`). Original core P1–P16 unchanged;
  physics firewall untouched. Same day: automated gates + the decadal review instituted (§11);
  campaign wave 2 completed (B355–B370); the Gate-B classical germ completed (B370).

---

## [Unreleased]

### Changed
- **B352 — the cup-product obstruction, computed: all six directions unobstructed at second order (2026-07-02;
  part 2, closing the B265/B270 open item at second order).** The obstruction `[z∪z] ∈ H²(4₁,𝔢₆)` **vanishes for
  every exponent direction** — including the θ-odd `{4,8}` escape sector and its polarization mix — with classes
  ≤ `1e-52` against raw second-order cochains up to `1e16` (the vanishing is *exactness*: `z₂` exists). Controls:
  the `m=1` direction (the real A-poly curve) and coboundaries give zero; the H² pairing is O(1) on random vectors
  (MB12 positive control); θ-parity appears as exact-zeros in the `{4,8}` H²-blocks 5–10 orders below the F₄
  floor. Two honest architecture failures banked en route (double precision cannot span the `e^{±22μ}` block
  range — relator residual `1e+49`; Euclidean chain normalization is not invariant — structure constants
  `1e-6..1e+73`, singular Gram); the working design is two-basis (exact root-basis brackets/Gram ⊕ block-diagonal
  chain-basis action, vectors crossing via `S` at dps 100) with structural-rank/cliff spectra decisions. Honest
  tier: consistent with (evidence for, not proof of) Menal-Ferrer–Porti-type smoothness at exceptional type;
  third order untested. Gate B updated: the CRUX has a genuinely 6-dim local moduli. Lock: fast structural tier
  always-on; the full ~12-min sweep gated behind `OA_SLOW=1`. Firewalled; nothing to `CLAIMS.md`.
- **B351 — the exact Chevalley 𝔢₆ (2026-07-02; part 1 of the `{4,8}`-integrability program).** The cross-session
  cup-product push had stalled at "signed structure constants failed Jacobi." Removed with the standard guaranteed
  construction, verified **exactly over the integers**: Frenkel–Kac cocycle brackets with **0 Jacobi violations on
  all 76,076 basis triples** (and the trap isolated: `[e_α,e_{−α}] = −h_α` is *forced* — the `+h_α` convention fails
  exactly 1440 mixed triples by `2e_β`); the principal sl₂ (`c = 2A⁻¹𝟙 = (16,22,30,42,30,16)`) exact; the exponent
  decomposition `𝔢₆ = ⊕ Sym^{2m}`, `m ∈ {1,4,5,7,8,11}` exact; the diagram involution θ built and verified
  (automorphism, involution, `𝔣₄ = 52` fixed ⊕ `26`), commuting with the principal sl₂ and acting on the six
  exponent lines by **exactly `(−1)^{m+1}`** — settling B347's flagged sign-pattern question at the algebra level
  (the geometric identification stays open). Sets up part 2: the B265/B270 cup-product obstruction against the F₄
  blocks in this exact basis. Firewalled; nothing to `CLAIMS.md`.
- **Suite hygiene — the global-dps test-order failure class fixed, MB13 §4 (2026-07-02).** All 6 B347-E₆ locks
  failed in full-suite order (passed in isolation): B302 lowers the **global** `mp.mp.dps` to 25 at call time and
  runs first alphabetically. B347 now self-guards every entry point (the pre-existing B264/B265/B276 idiom, now a
  written rule); B302 is raise-only; B348 uses scoped `mp.workdps`. `REPRODUCIBILITY.md` MB13 gains §4: entry
  points own their precision, never lower the shared global, "passes alone, fails in suite" is the tell.
- **Main sync + relay disposition (2026-07-02).** Merged main's **B347_e6_tangent_gradings** (PR #424, the peer
  session's corrected E₆ tangent probe — `dim H¹ = 6 = rank E₆`, uniform per exponent; amphichirality a uniform
  real structure; the hyperelliptic involution = the E₆→F₄ folding at the tangent level) and verified its 6 tests
  green in this sandbox. Resolved the same-day probe-ID collision by renumbering this branch's cyclic-cover
  torsion probe **B347 → B350** (main's number stands). Gate B "Settled" updated with the banked B347 facts (the
  relayed in-progress cup-product items noted, not banked). Added the **multi-session probe-ID hygiene rule** to
  `REPRODUCIBILITY.md` (fetch main, take max+1; first-to-main keeps the number).
- **Gate A extension B349 + the gate-based outreach package (2026-07-01).** **B349 — irregular covers through
  index 6:** all covers of the figure-eight enumerated (SnapPy); the census per index is a canonical **multiset**
  (banked exact); the cyclic members cross-validate B350's `coker(Aⁿ−I)` SNF **exactly** (independent routes, one
  answer); and **every** within-index invariant multiplicity (the twin `ℤ/2⊕ℤ²` index-5 covers; the 4×/2×/2×
  index-6 groups) collapses to a **single isometry class** — the object never distinguishes a member (the
  identification lives in the commensurator, cf. B323/B348). Index ≤ 6 honestly flagged as a computational
  horizon, not a theorem. **Eight classes** now sealed at gate A; `OPEN_PROBLEMS.md` updated. **The outreach
  package:** `frontier/EXPERT_OUTREACH.md` extended with the 2026-07 gate-based briefs — one bounded,
  proof-status-honest question per gate (B: `T[4₁;E₆]` state integral at exceptional type; C: commensurator
  `ℤ/3` → family replication or trinification-only; D: non-Hermitian Damanik–Gorodetski at complex `κ`), expert
  picks to verify, sequencing/hygiene rules (one gate one expert; log every send; a "known, see X" reply is a
  good outcome). All CONDITIONAL/firewalled; nothing to `CLAIMS.md`.
- **Gate A extensions B348 + B350 (2026-07-01; B350 originally numbered B347, renumbered after the ID collision with main's B347_e6_tangent_gradings, PR #424).** Two of B330's named untested invariant classes sealed under the
  same Galois-symmetrization mechanism, both in-sandbox, both CONDITIONAL (C-guardrail), nothing promoted.
  **B350 — the cyclic-cover abelian-torsion class:** the n-fold-cover torsion orders are the **P8/C5 Lucas ladder**
  `|det(Aⁿ−I)| = L₂ₙ−2` (one ladder, three faces); the Alexander factor multiset `{Δ(ζₙʲ)}` is a Galois-closed orbit
  with **integer** symmetric functions; SNF gives the groups (n=3 → `(ℤ/4)²`, independently re-deriving B326); and
  the deck action is fixed-point-free for **every** n with the one-line cause `det(A−I)=Δ(1)=−1` a unit — honestly
  tiered as an **MB8 generic-knot** mechanism (Δ(1)=±1 for all knots), not object-specific forcing. **B348 — the
  Bloch/scissors class:** the object's class `β=2[e^{iπ/3}]` has Galois orbit `{+β,−β}` = `{+Vol,−Vol}` (sum 0,
  canonical); the residual sign is the *orientation*, killed by the object's own amphichirality (B318's geometric
  firewall landing in the Bloch group — *self*-symmetrized); plus **the seam identity** `1−z₀ = z̄₀`: at the
  Eisenstein shape the generic Bloch duality involution `z→1−z` *is* the arithmetic Galois conjugation (`z(1−z)=1 ⇔
  z²−z+1=0` — the P12 quadratic is exactly that locus). **Seven classes** now sealed; the untested residual is
  renamed precisely in `OPEN_PROBLEMS.md` gate A (nonabelian Ptolemy/adjoint torsion, CS/η beyond `CS=0`, irregular
  covers, `SL(n≥3)` gluing invariants, extended-Bloch/`K₃` torsion). Nothing to `CLAIMS.md`.
- **External audit + robustness hardening (2026-07-01).** A fresh-clone, fresh-environment reproduction pass:
  3 frontier locks (B101/B106) failed on ill-conditioned numerical certificates and were re-certified
  structurally (nilpotency instead of defective-matrix eigenvalues; a measured-gap 1e-4 neutrality window
  instead of 1e-2; Galois-conjugation-closed scalar comparison) — findings unchanged, certificates hardened;
  banked as guard **MB13** (`REPRODUCIBILITY.md`). The proven ledger's weak spots were closed: **P9**
  de-circularized (independent dilogarithm volume + live SnapPy checks for `H₁`/CS/amphichirality/sister),
  **P5** brute-force word-ensemble sums + exact threshold assertions, **P4** parameter point derived as unique,
  **P11** independent eigendecomposition derivation of `log(A)`, **P10** three auxiliary filters live-checked,
  **C5** given its first executable lock (`tests/test_trace_selector_c5.py`). Stale ceilings/counters corrected
  (frontier B346; 1197 tests / 325 files). Zero label changes; zero promotions; P1–P16 semantics untouched.
- **The deviation-structure sweep B344–B346 + K022 (2026-07-01).** The reframe from B343 (*the object is the symmetric
  centre, not value-blind*) turned into a probe: the object forces the **form of the deviation space** around the centre
  — all dimensionless **relations/textures** (form, per the `sin²θ_W=3/8` precedent), never magnitudes. **B344:** `det(dφ)=1`
  + κ-invariance ⇒ deviations come in a **reciprocal symplectic pair `(λ,1/λ)`**; κ is the un-paired Casimir = the
  scale/cusp door (external); this is *why* the metallic tower is `λ^k↔λ^{−k}` (B65). **B345:** the deviation modes carry
  ℤ/3 charges `{0,1,2}`, forcing a **charge-conservation selection rule** (the anti-diagonal ω-circulant texture, B324) —
  *independent* of the E₆-exponent split (B265). **B346 (the "prize"):** **symplectic conjugation = ℤ/3 charge
  conjugation** (linked), E₆-exponent independent — but **no data-facing second falsifier** emerged (the cross-relations
  are *forms*, not measured predictions), which is the on-brand honest result. **`knowledge/K022`:** the reframe — the
  object is the symmetric centre and forces the *geometry of the perturbations*; the world sets the magnitudes. Deepens
  K020. Nothing to `CLAIMS.md`.
- **B343 — the object forces *exact TBM* (θ₁₃=0), not TM2 (2026-07-01).** Chat-2's three-step self-correction, verified at
  the landing; **corrects B342/S048**. The neutrino residual symmetry is the object's own 2-torsion **Klein group**
  `ℤ₂×ℤ₂` (of `(ℤ/4)²`, B326); the deck ℤ/3 acts **irreducibly** (`Φ₃` irreducible mod 2), 3-cycling the three `ℤ₂`'s and
  selecting **none** → the **full Klein survives → exact TBM (θ₁₃=0)** (not TM1/TM2; `T=diag(1,ω,ω²)` also doesn't
  normalise the neutrino Klein). The **TM2 tension dissolves** (the object never bet on TM2); `θ₁₃=0` is excluded, so the
  TBM-**breaking** (θ₁₃ size + direction) is external. **Unification:** the *same* irreducibility makes the object
  mass-blind (B335), split-blind (B327/B329), **and** direction-blind — one arithmetic property. Surviving content
  (firewalled): lepton mixing is TBM-structured (observed); the deviation external. Nothing to `CLAIMS.md`.
- **The CP/mixing sweep B339–B342 + S048 (2026-07-01).** The flow interior (H107–H109) + Chat-2's lepton-mixing reading,
  all firewalled, **zero `CLAIMS.md`**. **B339 (H107):** the chiral-flow sub-leading is `CS(1,n)=−1/(2n)+1/(24n³)+…` —
  `c₂=0` (amphichirality theorem) and `c₃=1/24=1/(2·h(E₆))`, **rational, no √−3** (the flow's arithmetic is `|τ|²=12`, not
  Eisenstein). **B340 (H108):** the CP phase `κ` along the flow — `±π/6` is **extremal at the amphichiral cusp** (CS=0);
  chirality *lowers* `arg κ` at `O(CS²)`; the CP sign is external (orientation). **B341/H109:** resolved by B337 (no probe)
  — the ordered spectrum is a 3-seed multiplicity invariant, E₆ is single-object → structure⊕ordering forbids both in one
  config. **B342 + `speculations/S048` (heavily firewalled):** the object's ℤ/3 *is* the trimaximal (magic) symmetry
  (`(1,1,1)/√3` = ℤ/3-invariant = TBM middle column) — a **math fact**; but the honest data comparison (the check Chat-2
  skipped) shows **current data favours TM1 over TM2** (θ₁₂: TM1 34.3° vs TM2 35.7° vs obs 33.4°). Guardrails explicit:
  symmetry-not-magnitude, B322 null, HELD unmet, the δ-sign joint (PMNS-in-ℚ(√−3)) unweldable → NEEDS-SPECIALIST. *(θ★/D10
  is a separate defunct project, not a constraint — noted in memory.)* Verified-not-trusted throughout.
- **The symmetry-broken sweep B336–B338 + S047 (2026-07-01).** Two cross-chat insights (both verified here), probed *in*
  the symmetry-broken sector instead of deferring. **B336 (Chat-1, chirality):** the value would live in the imaginary
  seam `ℚ(√−15)`; confirmed `J_N(4₁;ζ₁₅)` real (amphichiral → zero √−15), but the chiral *routes* are provably closed —
  monodromy `{t²−4}∌−15`, commensurables all `ℚ(√−3)≠ℚ(√−15)` (O₋₃ vs O₋₁₅), fillings non-arithmetic. With B333 (√−15
  generic), the value's home is **doubly separated** (generic arithmetic + not a geometric invariant). **B337 (Chat-2,
  multiplicity):** the **structure⊕ordering** theorem — a symmetric object gives E₆ + *democratic* `{52,1,1}`; distinct
  seeds give *ordered* `{10.2,−4,−0.2}` but distinct fields (`√−3,ℚ(i),deg≥4`) → no shared E₆; `{1,2,3}` not forced
  (arithmeticity selects `{1,2}`). Same symmetry forces structure and forbids ordering — no static config has both.
  **B338 (the bridge):** the object *contains* a flow — Dehn filling `(1,n)` from the symmetric cusp (`CS=0`) to
  broken/chiral configs, with the chiral order parameter **`CS ~ −1/(2n)`** — but the flow *parameter* (the slope) is
  external, so the value is **selected, not forced**. **`speculations/S047`** holds the firewalled reunification reading
  (symmetric UV → filling flow → broken IR). All firewalled; nothing to `CLAIMS.md`.
- **B335 — the generation ℤ/3 is an exact isometry: the mass degeneracy is a *theorem* (2026-07-01).** Probed the real
  Level-4 geometry in-sandbox (SnapPy) instead of deferring. The three generations are related by the **deck
  transformation** of the 3-fold cover — an **isometry** — so every real invariant (volume 3× exactly; shortest
  geodesics at multiplicity 3; CS; cusp shape `2√3·i`, `|·|²=12=h(E₆)`) is **ℤ/3-equal → masses exactly degenerate.**
  The hierarchy is the *breaking* of an exact isometry (external by definition), not a hidden value. What the object
  *does* distinguish is the ℤ/3-eigenvalue `{1,ω,ω²}` — a **phase (CP/mixing), not a mass**. This is the geometry-side
  proof of `n₁=n₂` (B327/B329/B331). **Refuted (verify-don't-trust, on this seat):** the cover's order-24 symmetry group
  is **not** 2T (its abelianization is `(ℤ/2)²`, not `ℤ/3`) — the McKay-group hope killed before it became a claim.
  Firewalled; nothing to `CLAIMS.md`.
- **`knowledge/K021` — the founding-identity synthesis + B334 (2026-07-01).** A specialist-facing explainer tying the
  session's verified spine into one self-contained document (the axiom → `g = −R·L⁻¹` → the two ends → E₆ + generations →
  `n₁=n₂`/Level 4 → the seam). **B334 (Chat handoff, verified):** the seam's Hilbert class field **`H(ℚ(√−15)) =
  ℚ(√5,√−3)`** — the two ends are the *arithmetic completion* of the seam (genus theory; verified by the splitting law
  `principal ⟺ p≡1,4 mod 15` + a binary-form cross-check, 0 mismatches). Reconciles B333: the seam is **intrinsically
  generic** (h=2 common) yet **relationally distinguished** (its HCF is the two ends); the `137` prediction is **dead**
  (non-principal fraction ≈ 0.556, a coin flip). Firewalled; nothing to `CLAIMS.md`.
- **B333 — the compositum seam probe: the firewall holds *at* the seam (2026-07-01).** The first probe run *in* the seam
  (not on one side). The B332 meditation located a value's home in the compositum's third subfield **ℚ(√−15)**
  (`√5·√−3`, ramified at `15=3·5`). Run with a **null test** up front: `h(−15)=2` (Chat-1's claim, verified) — **but
  `h=2` is common** (14 of 123 fundamental discriminants to −400), units `{±1}` generic, ramification at `{3,5}`
  tautological. So **ℚ(√−15) is arithmetically GENERIC** → no SM structure → **firewall holds at the seam.** Retires the
  compositum `[HOOK]` (verify-don't-trust on this seat's own proposal): the seam is the correct *structural* home of a
  value, but the value is not in the field's arithmetic — the specific gluing needs external input (Level 4), as B326/B331
  already located. Firewalled; nothing to `CLAIMS.md`.
- **B332 — the two ends = product and ratio of the founding letters (2026-07-01).** Chat-1 handoff, verify-don't-trust.
  **Verified exact:** `g = −R·L⁻¹` (the generation ℤ/3 element *is* the signed ratio of `σ`'s two letters `R,L`), and
  `g⁻¹a = −L`. The two simplest length-2 combinations land on the two arithmetic ends: **product `RL`** (trace 3, disc 5)
  → `ℚ(√5)` → **E₈** (golden); **ratio `g`** (order 3, disc −3) → `ℚ(√−3)` → **E₆** (Eisenstein, gauge + generations).
  **Corrected** Chat-1's inverted labeling ("product→E₆" is wrong-ended; product is √5/E₈) and the "golden ratio → ℚ(√−3)"
  field-conflation. **Quarantined (not banked):** the overlap index `[Γ:Γ∩gΓg⁻¹]=3` (reported; `g` commensurates but
  index-3 unverified — needs Bianchi computation); the `1/4` suppression (DEAD — Chat-1's null test) and `16=4+h(E₆)`
  (inconsistent hook). Firewalled; nothing to `CLAIMS.md`.
- **B331 — the SL(2,ℂ) "complex escape" closed at its root (2026-07-01).** Chat-1's meditation (structure = real
  invariants / values = phases) proposed that the holonomy being in `SL(2,ℂ)` (not `SU(2)`) could give `n₁≠n₂` via a
  holomorphic non-self-dual lift, then self-corrected. **Verified + sharpened:** the generation element
  `g=[[0,−1],[1,−1]]` is **elliptic and ambivalent** (`g~g⁻¹`, eigenvalues `{ω,ω²}`), so `χ_27(g)` is **real in every
  representation — holomorphic and compact coincide (both 0)**. Holomorphicity is invisible at a finite-order element; it
  only distinguishes *loxodromic* elements (volume/CS = structure). Corrects Chat-1's "center/non-center" heuristic (the
  central `z` gives `χ_27=27ω`, complex — "order-3 ⇒ real" is false) *and* B329's σ-stability framing. Closes the escape
  for the arithmetically-relevant lift (Riley = an `SL(2,ℂ)` rep) → **Level 4 confirmed**; the fully-general all-embeddings
  claim stays open (H103). Firewalled; nothing to `CLAIMS.md`.
- **The in-sandbox attack sweep B329–B330 + S046 + R7 (2026-07-01).** A "research / get-informed / meditate / sober /
  attack" push on the computable frontier (don't-give-up; compute-before-deferring), all firewalled, **zero `CLAIMS.md`
  promotions.** **B329 ([VERIFIED]):** `27|₂T` computed for *both* natural embeddings from a from-scratch 2T character
  table — principal (quaternionic SU(2)) `= 3·1⊕3·1′⊕3·1″⊕6·3`, trinification (complex SU(3)) `= 9·1⊕3·1′⊕3·1″⊕3·2′⊕3·2″`
  — **both give `n₁=n₂` → Level 4.** Tightens B327: even the *complex* SU(3) route can't split the light generations
  (the 27's balanced `3/3̄` pairing restores reality; non-vacuity witnessed — the SU(3) `3`|₂T is genuinely complex).
  Level 3 needs a chiral (non-σ-stable) embedding no canonical candidate supplies. **B330 ([CONDITIONAL], gate A/S032-A):**
  the no-forced-choice capstone attacked via one Galois-symmetrization mechanism — folds B130+B314+B318 and stresses two
  fresh classes (B326 cover-torsion `(ℤ/4)²`, cohomology `H¹`); **five classes now sealed**, no forced choice among them;
  worded per the C-guardrail (`open`, not universal proof; untested classes named). **L34 (silver/bronze Weil zeta):
  DORMANT** — the m=1 `40a1` was a 2-bridge-Riley artifact; the trace-map fixed locus is genus-0 (m=1) / irregular
  (m=2,3); the full canonical-component arithmetic is NEEDS-SPECIALIST (R7: Baker–Petersen gap). **H14:** already resolved
  by B315 (checked, not re-banked). **Research (`NOVELTY_AUDIT.md` R7):** four cited verdicts (the `27|₂T` table, the
  complex embedding, the `Δ` two-ends coincidence, silver/bronze curves). **Meditate (`speculations/S046`, firewalled):**
  "the value lives at the seam" — every value is a symmetry the object leaves unbroken; a speculation→calculation table
  (new hints H103–H106). All firewalled; nothing to `CLAIMS.md`.
- **The hierarchy-atom handoffs B326–B327 (2026-07-01).** Two three-seat reports pushed the mass-hierarchy bottleneck;
  both verified in-sandbox before banking (verify-don't-trust). **B326 (Chat-2, [VERIFIED]):** the generation `ℤ/3`
  breaking is **finite congruence torsion**, not transcendental — `H₁(3-fold cyclic cover of 4₁)=ℤ⊕(ℤ/4)²` (SnapPy 3.3.2
  *and* the exact Alexander module ℤ[t]/(Δ,t³−1), Smith form diag(4,4)); the deck `ℤ/3` acts irreducibly with char poly
  `Φ₃ = Δ mod 4` (since `−3≡1 mod 4`); and the *same* `Δ=t²−3t+1` carries **both arithmetic ends** (`disc=5`→√5,
  `mod 4=Φ₃`→√−3). Finite torsion ⇒ *texture, not magnitudes*. **B327 (Chat-1, [VERIFIED + SHARPENED]):** the hierarchy
  CRUX = the branching `27|₂T`; a cross-chat contradiction was resolved by direct E₆ computation (principal
  `27 = V(16)+V(8)+V(0)`, spins 8,4,0 — Chat-2 right, Chat-1's `9V₀+6V₁` wrong), and `n₁=n₂` was shown forced by
  **self-duality** of the SU(2) restriction (not integer spin — the half-integer "McKay-SL(2) escape" fails). Sharpened
  atom: the fork is *self-dual (quaternionic) SU(2) → Level 4* vs *non-self-dual complex embedding → Level 3*, the
  standard quaternionic `2T` favouring **Level 4**. `docs/OPEN_PROBLEMS.md` gate B updated to this atomic form. All
  firewalled; **zero promotions** to `CLAIMS.md`.
- **The specialist-handoff arc B315–B325 + `docs/OPEN_PROBLEMS.md` (2026-07-01).** After the consolidation, the
  forgotten leads and cross-chat handoffs were run to conclusion and the frontier was mapped to a specialist handoff.
  **New results:** B315 (the E₇-exclusion *contains* heterotic's, shared root = pseudoreality); B316 (`√−7` is the
  chirality field, not a metallic-ladder rung); B317 (the object is a *transcendental* Painlevé-VI solution; corrects
  P010's stale "unrun"); B318 (amphichirality is the *geometric* firewall for the Eisenstein end; golden end
  arithmetic-only); **B322 (the value hunt, run: the object's invariants match the SM at chance, `p≈0.5` — the firewall
  confirmed by a null test, not just proven)**; B323 (the four-level framework — object D₄ / seam ℤ/2×ℤ/2 / E₆-center ℤ/3
  / commensurator ℤ/3); B324 (Chat-1's ω-circulant generation matrix verified exactly in `ℤ[ω]` — structure, not values);
  B325 (Chat-2's "ℤ/3-protection obstruction" refuted — the light degeneracy is accidental, the CRUX stays Level 3).
  **The deliverable:** `docs/OPEN_PROBLEMS.md` — the honest specialist handoff (four gates: A/S032-A in-sandbox, B/CRUX,
  C/multiplicity, D/non-Hermitian DG) with the counterweight to the "one step from a TOE" framing. `knowledge/K020`
  extended (§6a the empirical firewall, §8 the four levels). All firewalled; **zero promotions** to `CLAIMS.md`.
- **The structural-theorem arc B231–B314, and the recontextualization audit + masterplan (2026-07-01).** The
  object-mapping arc sharpened into a single proven statement — *the object forces form/structure, never physical
  values* — and the documentation layer (which had fallen ~80–190 probes behind) was brought current. **The math
  (B231–B314):** the **two-ended object** (`E₆`/`ℚ(√−3)` Eisenstein ↔ `E₈`/`ℚ(√5)` golden, `E₇` excluded by Niven;
  B248/B258/B261); the **arithmetic atom** + figure-eight **`E₆` character variety** (B266/B282/B264); the
  **principal-grading cascade** = standard Slansky Lie theory + the one object datum, the Eisenstein `ω` at trinification
  (an irreducible A-poly branch point; B305/B306/B310/B311); **Face IV houses the *form*** (the CIZ `SU(2)₁₀` `E₆`
  modular invariant, one `E₆`/three ADE hats, both ends, generic level; B312/B313); the **four faces of one `κ`** (B309);
  and **the mechanism — the firewall is a Galois theorem**: every discrete invariant is a Galois orbit of the object's
  own arithmetic, two ends/two `ℤ/2` (the CP sign via `√−3→−√−3`, B285; the colored-Jones data via `√5→−√5`, B314).
  Open: the all-invariants `S032-A`; the three specialist gates (`T[4₁;E₆]` CRUX, multiplicity→generations,
  non-Hermitian Damanik–Gorodetski). **The consolidation:** a full 8-agent A-to-Z repo audit
  (`docs/RECONTEXT_AUDIT_AND_MASTERPLAN_2026-07.md`), the new `knowledge/K020` + `philosophy/P013` (the Galois theorem's
  homes), README/CLAIMS/GOVERNANCE refreshed to B314, and the obstruction-repo suspicion closed (examined file-by-file;
  its core = P008, confirmed by reading). All firewalled; **zero promotions** to `CLAIMS.md` (proven core P1–P16 frozen).
- **SYNTHESIS consolidation — the dual-McKay, all of B211, the V212 correction, and on-site, woven in (2026-06-25;
  V215).** The "metallic one object, four ways" synthesis had been updated for B206–B208 but **dropped** the later
  results — chat1 flagged that updating only for B210 would repeat the "agreed-then-dropped" pattern one layer
  deeper. Folded in all of it: (B0) §9 "for the golden mean **alone**, the **unique** exceptional McKay group" →
  "golden is the **minimal/fundamental** member of the `ℚ(√5)` family" (propagating the B206/V212 correction);
  (B) a **dual-McKay** paragraph — golden carries `E₆` (hyperbolic `ℚ(√−3)`, figure-eight = two ideal tetrahedra →
  `2T=E₆`) **and** `E₈` (monodromy `ℚ(√5)` → `2I`), missing `E₇` (Arnold trinity), reconciling "E₆ impossible in
  the *monodromy* arithmetic vs present in the *hyperbolic* one"; (B1) **all of B211** — the character *variety's*
  own arithmetic (non-CM elliptic curve `40a1`), the WRT period as a **Pisano period**, **family-wide
  amphichirality** (`CS=0`), and the **Borromean-complement parent**; plus the B212 silver-degeneracy note; (C)
  the **on-site uniqueness** result (B200/R2) into §7 + the `S038` table (the "forced not chosen" / HELD reading,
  firewalled). **Next-layer drop caught:** §7 still listed the B204 cross-lemma as open — now marked closed (L36).
  Completeness guard: every banked B204–B212 has a synthesis touchpoint. Exposition only, **no new theorem; nothing
  to `CLAIMS.md`.**
- **B204 — the WRT level-period law is now `[proved]` (the cross-period lemma closed; 2026-06-25; V214).** The one
  remaining lemma of the B204 proof — a closed form for the cross Gauss-sum period `L_c` (its 2-adic part) — is
  **closed**: `L_c = (4+ab)/2^{min(v₂a,v₂b,2)}`, proved by exact integer arithmetic (no numerics). (1) The cross
  Gauss sum `Γ_t(N)=∑_m c_m ω^{Nm}` has non-negative integer counts `c_m` (no cancellation), so a finite
  exponential sum over a `2D`-th root has period **exactly** `2D/gcd(2D, support)`. (2) The **content
  `gcd(2D,{Q_t(y)}) = 2^{min(v₂a,v₂b,2)}`** — every term of `Q_t=b y₁²+4t y₁y₂−a y₂²` has `v₂≥c` (the `4t` cross
  caps the 2-power at 2), no odd prime divides it (`p∣a,p∣b ⇒ p∣4`). (3) The `lcm(lcm(a,b),L_c)=lcm(a,b)·(4+ab)/
  gcd(4+ab,4)` identity (9-case 2-adic, verified 200×200). So **`per|Z(a,b)| = lcm(a,b)(4+ab)/gcd(4+ab,4)` is
  proved** (metallic diagonal `P(m)=m(m²+4)/gcd(m²+4,4)`). The reciprocity inputs + the framework remain KNOWN
  (Jeffrey 1992, V199) — this closes the repo's own period-formula proof; the formula's novelty stays per V199 (do
  not claim). chat1's "highest-value next step" (L36). Firewall: standalone quantum-topology/arithmetic; **nothing
  to `CLAIMS.md`.** `gauss_proof.py` (+`cross_period_closed/exact/support_gcd`), `PROOF.md`, `FINDINGS.md`,
  `tests/test_b204_*` (+2 locks).
- **Re-audit of the quietly-banked batch B205–B209 (2026-06-25; V212).** Acting on the owner's challenge — that
  findings banked *without* an explicit verify-push may carry the same superficiality that verify-requests keep
  exposing — each of the five findings banked this session without a push (B205–B209) was **independently
  re-derived from scratch** (5 parallel adversarial verifiers + own confirmation of every substantive fix).
  **Verdict: every load-bearing *number* held (the math is correct in all five), but the prediction was right for
  the *framings* and *tests*.** Fixes applied in place: **B206 (real over-claim)** — "golden is the *unique*
  metallic mean whose spin shadow is McKay-E₈ / field 5 only for m=1,4" is **false** (a cap-`m≤8` artifact + a
  field-vs-shadow conflation): the field is exactly `ℚ(√5)` for the whole Lucas family `{1,4,11,29,…}` and the
  `2I=SL(2,𝔽₅)` shadow appears for every `m` with `5∣m²+4` (since `⟨R,L⟩=SL(2,ℤ)` surjects mod 5 for *any* m) →
  corrected to "golden = the **minimal/fundamental** member of the `ℚ(√5)/E₈` family," and the test now locks the
  genuine **surjection** `⟨R,L⟩→120` (the prior lock checked only one element's order 10 — the same gap caught in
  B210/V210). **B207 (framing over-reach)** — the "volumes → Borromean" limit was asserted from a value-coincidence
  + an Aitken estimate (~3·10⁻³ short); the structural drill that *earns* it lives in B211/L31 — FINDINGS reworded
  and the fragile `<0.01` Aitken lock replaced with honest "approaches, bounded-above" bounds. **B205 (test
  soft-spot)** — the `is_automorphism` relation-clause was **vacuous** (applied the map to an already-reduced=0
  relation; returned True even for `X→2X`); the math is right (`R_q,L_q` *are* automorphisms) but the check now
  substitutes images into the un-reduced relation + three negative controls. **B208 (under-claim upgraded)** — the
  divisibility `squarefree(m²+4) ∣ P(m)` is in fact a **theorem** (proven; 0 failures to m=300 000), not just
  "checked m=1..300". **B209 (confirmed)** — `Λ*(ℝ⁶)` under A₅ `=(64,0,4,4,4)`, all mult 4, spinorial `{2,2,4,6}`
  absent, fully re-derived; added an explicit dimension-saturation lock. Firewalls all clean; **nothing to
  `CLAIMS.md`; P1–P16 untouched.** The honest meta-lesson: the banked *quantities* were sound, but two
  uniqueness-framings and three tests carried exactly the predicted superficiality — verify-don't-trust now applied
  to one's own quietly-banked work.
- **Verification corrections (Phase V, 2026-06-23): B192 REFUTED, B189 framing fix.** An independent adversarial
  verification pass on the recent batch (B189/B192/B196) cleared **B196/S037** (identities exact, firewall airtight)
  but caught two problems. **B192 — the Lyapunov "parity law" is REFUTED** (retracted in place to a recorded
  negative): the claimed *symmetric-iff-`n`-even / special-to-metallic* law was an artifact of cherry-picked
  energies (it **inverts** on a fair energy grid — n=4→0.34, n=3→0.03, n=6→0.50, no even/odd alternation) plus a
  rigged dense-Gaussian control (a *random potential* in the same companion matches metallic, n=4: 0.34). The
  approximate ±-symmetry is a generic reciprocal-pair transfer-matrix property, not a law and not metallic-special;
  V29 holds at the algebra level but is *not* realized as a Lyapunov parity. Only "spectrum sums to 0" survives;
  **B166's original results are unchanged.** **B189 — framing fix**: the C3 "indistinguishable from the null"
  overstated — Ω's `d_MM=3.94` sits `~0.15` (≈12σ, 30 seeds) **above** the null `3.78` (sparser/more tree-like → even
  *less* manifoldlike); same *order* (both ~4 graded-DAG artifacts), and the headline (d≈4 is an artifact, vacuous as
  physics) **stands and is strengthened**. Reproducers/tests/FINDINGS/ledger/OPEN_LEADS reworded. (verify-don't-trust
  working — the 3rd and 4th self-corrections of the Masterplan III batch, after B190.)

### Added
- **S041 — the framework search started: the object's signatures as a filter against SM/GR frameworks; first
  verdict = structural rhymes, no crossing (2026-06-27; V234).** Owner ask (via chat1): use the object as a filter
  against heterotic / F-theory / Connes NCG / moonshine. Started with discipline (a shared object = the null
  hypothesis; a *crossing* needs a derivation + a null test, HELD). Skeptical scout: **F-theory** — generic
  modularity only, and the special CM→rational-N=(2,2)-SCFT realization is *blocked* (40a1 is non-CM, a Betti
  object); **heterotic** — same E₈ algebra, different role (Galois/McKay vs gauge); **NCG** — no shared data;
  **moonshine — the one genuine HOOK** — the object's dual McKay E₈+E₆ (E₇ excluded, B210) are exactly McKay's
  Monster- and Fischer-seeding diagrams, so the object's arithmetic *selects Monster+Fischer, excludes the Baby
  Monster* — but shared rep-theory, not physics. **Verdict:** every overlap a structural rhyme; the firewall holds
  a 5th time, now against external frameworks. Continuation registered (deeper super-moonshine scout; novelty-check
  the E₈+E₆−E₇ selection). Firewalled (S041); novelty UNCHECKED. **Nothing to `CLAIMS.md`; P1–P16 untouched.**
- **B230 — golden's SUSY-uniqueness is robust to AFM/FM; the FM "silver SUSY" is a central-charge coincidence,
  not real (2026-06-27; V233).** A stress-test of B224/B228 (chat1) with a verify-don't-trust catch. The su(2)_k
  chain: AFM → M(k+1,k+2), FM → Z_k parafermion (`c=2(k-1)/(k+2)`). A naive c-test flags silver FM (Z₆,
  `c=5/4=c(SM(6))`) — but the Z₆ parafermion (`SU(2)₆/U(1)`) and SM(6) (`(SU(2)₄×SU(2)₂)/SU(2)₆`) are **different
  cosets → different CFTs**, so it's a central-charge coincidence, **not** SUSY. With B228's rigorous coset
  criterion, the only genuine N=1 super metallic chain in *any* coupling is golden+AFM (= TCI). So golden's
  SUSY-uniqueness is **robust to AFM/FM**, and the episode reinforces "use the coset identity, not c-matching."
  Also this PR: B226 FINDINGS updated (the two faces are *algebraically unified* by B228's SU(2)₃ coset coincidence,
  not merely "SU(2)₃ on both sides"); registered the B227 near-square observation `|H₁|=(2m²+7)²+2 ⇒ |H₁|≡3 mod 4`.
  3 pytest locks. Firewalled. **Nothing to `CLAIMS.md`; P1–P16 untouched.**
- **B229 — the TCI's two 3d-3d bulk realizations are different 3-manifolds: one CFT, two bulks (2026-06-26;
  V232).** The L45 residual completed — the explicit **super-Seifert** dual of the tricritical Ising. Both 3d-3d
  recipes share the form `S²((P,P−R),(Q,S),(3,1))`, differing only by the determinant = the SU(2) level: **ordinary
  `M(P,Q)` has `PS−QR=1` (SU(2)₁); super `SM(P,Q)` has `PS−QR=2` (SU(2)₂)**. So the TCI realizes as: ordinary
  M(4,5) → `S²(3,4,5)`, `|H₁|=83`; super SM(3,5) → `S²(3,3,5)`, `|H₁|=66`. **Same boundary CFT (c=7/10; the cosets
  coincide, B228) but different bulk 3-manifold** — one CFT, two distinct bulks, distinguished by the
  SU(2)₁-vs-SU(2)₂ structure; the coset coincidence does *not* lift to the bulk. Only golden is both (the metallic
  ordinary models have `|P−Q|=1`, the unitary super series `|P−Q|=2`; the unique overlap is TCI = M(4,5) = SM(3,5)).
  Ordinary recipe `[verified]` (B227); TCI=SM(3,5) `[verified]` (super c-formula, arXiv:2405.05746); super recipe
  `[cited]` (verbatim abstract, arXiv:2511.04524); super `|H₁|=66` `[computed]`, not anchored on a published super
  worked example (flagged; the different-base-orbifold conclusion needs only the recipe-fixed cone orders). 5 pytest
  locks. Novelty UNCHECKED. Firewalled (S040). **Nothing to `CLAIMS.md`; P1–P16 untouched.**
- **B228 — the mechanism behind golden's SUSY-uniqueness: the ordinary/super coset coincidence at SU(2)₃
  (2026-06-26; V231).** The L45 follow-on, answered cleanly **in-sandbox** (no Seifert recipe needed). The ordinary
  minimal model `M(m,m+1) = (SU(2)_{m−2}×SU(2)₁)/SU(2)_{m−1}` and the N=1 super minimal model
  `SM(m') = (SU(2)_{m'−2}×SU(2)₂)/SU(2)_{m'}` **coincide** (same numerator multiset + denominator) only at
  `(m,m')=(4,3)` — the **TCI, denominator SU(2)₃ (golden)**. So `SU(2)₃` is the unique level where the
  `SU(2)₁`-based (ordinary) and `SU(2)₂`-based (super) coset constructions coincide — the **structural** reason
  behind B224's central-charge uniqueness (deepens "c-coincidence" → "coset-coincidence"). Metallic statement:
  chain `m` has GKO denominator `SU(2)_{m²+2}`, which is `SU(2)₃` only for `m=1`, so **golden is the unique metallic
  chain whose coset is also a super-minimal-model coset** — settling the L45 follow-on without the super-Seifert
  recipe. Verified in-sandbox (both coset families reproduce the known central charges; the coincidence is unique).
  4 pytest locks `[exact]`; super-GKO `[cited]`. Novelty UNCHECKED. Firewalled (S040). **Nothing to `CLAIMS.md`;
  P1–P16 untouched.**
- **B227 — L45: the metallic SUSY chains have explicit Seifert 3-manifold duals (2026-06-26; V230).** The concrete
  lead from the L43 scout. B224's metallic chains flow to `M(m²+4, m²+3)`; Gang–Kang–Kim (arXiv:2405.16377, recipe
  verified) realize `M(P,Q)` as a class-R theory on Seifert `S²((P,P−R),(Q,S),(3,1))`. For the metallic family the
  condition `PS−QR=1` is solved by **`(R,S)=(1,1)` for all m** → **`S²((m²+4, m²+3),(m²+3,1),(3,1))`** (m=1
  reproduces the paper's TCI Seifert, `|H₁|=83`). **Pattern:** cone orders `(m²+4, m²+3, 3)` — largest = the
  **metallic discriminant** `m²+4` (5,8,13,20,29,…); `|H₁| = 4m⁴+28m²+51 = (2m²+7)²+2`; all base orbifolds
  hyperbolic → `SL₂~`/non-hyperbolic (consistent with B226). So the metallic SUSY chains are the subfamily of
  unitary-minimal-model Seifert spaces with largest cone order = a metallic discriminant — a concrete bridge from
  the repo's metallic structure to the active 3d-3d minimal-model program. Recipe `[cited]`, construction/invariants
  `[exact]` (4 pytest locks; `|H₁|` cross-checked vs sage Smith form; m=1 validated vs the published TCI). Follow-on
  (open): golden-SUSY-uniqueness as a Seifert-overlap with the SUSY-minimal-model family. Novelty UNCHECKED.
  Firewalled (S040). **Nothing to `CLAIMS.md`; P1–P16 untouched.**
- **B226 — L43 resolved: the two SUSYs are two faces, separated by the hyperbolic/non-hyperbolic divide
  (2026-06-26; V229).** The deepest open question (chat1): the same golden/figure-eight object carries SUSY twice —
  the licensed 3d-3d SUSY (`T[4₁]` N=2, `M_SUSY=M_flat`=40a1) and the emergent N=1 superconformal chain SUSY
  (`c=7/10`). One structure or two? **Two faces.** A literature scout (WebSearch/WebFetch): 2D Virasoro minimal
  models — *including the supersymmetric ones (the tricritical Ising)* — are realized as 3d bulk theories from
  **non-hyperbolic (Seifert / torus-knot)** 3-manifolds via `T[SU(2)]`/`SU(2)_k` (Gang et al.,
  arXiv:2405.16377 → TCI via Seifert `S²((5,−1),(4,5),(3,1))`; 2511.04524=JHEP 03(2026)066; 2512.23122). The
  **figure-eight is hyperbolic** → its 3d-3d theory is the complex-SL(2,ℂ)/3d-gravity object (`Vol=2.03`,
  arXiv:2401.13900), **not** a minimal model. So the shared ingredient is `SU(2)₃`/`T[SU(2)]`, **not** the
  figure-eight's geometry — the golden-chain CFT (TCI) and the figure-eight knot sit on opposite sides of the
  hyperbolicity divide, two distinct 3-manifolds in the same Class-R framework. (Rhymes with B217's
  closed-Sol/cusped-hyperbolic split.) Exact `4₁` 3d-3d→2d reduction stays NEEDS-SPECIALIST; the qualitative
  answer is settled. Firewalled (S040); central charges `[exact]`, the split `[literature-grounded]`. **Nothing to
  `CLAIMS.md`; P1–P16 untouched.**
- **B225 — conductor-decomposition test: 5 = golden filling (holds), 2 = octahedral parent (refuted) (2026-06-26;
  V228).** A verify-don't-trust test of chat1's "game-changer": does 40a1's conductor `40=2³·5` split as
  `(octahedral parent 2) × (golden filling 5)`? With a validated 2-bridge pipeline (reproduces B211's `Φ` and bad
  primes `{2,5}=40a1`): **SOLID** — `5` is the golden filling (the figure-eight branch locus `(x²−1)(x²−5)`; the
  `x²=5` branch = the golden monodromy discriminant `t²−4=5` for trace 3). **REFUTED** — `2` is not the octahedral
  parent: prime 2 appears in *every* 2-bridge knot, twist (Whitehead fillings) **and non-twist** (`6_2,6_3,7_6,
  8_3,8_8,9_4`), so it is universal to 2-bridge character varieties, not parent-specific. So `40` does **not**
  decompose as `(parent)×(filling)`. Foundations verified (Whitehead/Borromean ℚ(i) prime 2; fig-8 ℚ(√−3) prime 3;
  golden ℚ(√5) prime 5). Method limit: disc-of-disc overcounts for genus ≥ 2 (clean only `4_1`,`5_2`); higher
  conductors = Jacobian-conductor NEEDS-SPECIALIST. Resolves L44 (one half real, one half not). **Nothing to
  `CLAIMS.md`; P1–P16 untouched.**
- **B224 — golden is the UNIQUE metallic mean whose chain is supersymmetric (2026-06-26; V227).** chat1's
  "close the circle." The su(2)_k anyon chain → minimal model `M(k+1,k+2)` (Feiguin–Trebst–Ludwig; `k=3`→`M(4,5)`
  `c=7/10` = the golden chain, reproduced B220/B222). **Among all unitary minimal models `M(q,q+1)`, only `M(4,5)`
  is N=1 superconformal** (= SM(3); the only `c<1` solution of `1−6/(q(q+1))=(3/2)(1−8/(p(p+2)))`). In the metallic
  family (level `k_m=m²+2`, since `n=k+2=m²+4` = the discriminant): `m=1`→`c=7/10` (SUSY); `m=2`(silver)→`25/28`;
  `m=3`(bronze)→`25/26`; `c_m→1`, none superconformal but golden. So **golden is the unique metallic mean whose
  chain is supersymmetric** — the SUSY point needs exactly the golden level `k=3` (`n=5=m²+4`). Closes the circle:
  golden is minimal, exceptional (`E₈`/`E₆`), least-hierarchical, **and** uniquely supersymmetric — all via `5=m²+4`
  at `m=1`. Flow `[cited]` (k=3 reproduced); central charges + uniqueness `[exact]`; novelty UNCHECKED. Firewall:
  dimensionless CFT, not a scale. **Nothing to `CLAIMS.md`; P1–P16 untouched.**
- **The SUSY thread — golden multiplicity produces emergent SUPERSYMMETRY (B221/B222/B223 + S040; 2026-06-26;
  V224–V226).** The thing hiding in plain sight: `c=7/10` (B220) is not "a number" — it **is** the tricritical
  Ising `M(4,5)` = the **first N=1 superconformal minimal model**, so the object's multiplicity (golden, B218)
  produces, by interaction alone, an **emergent supersymmetric** theory.
  - **B221 (the exact anchor; V224).** `c=7/10` by three agreeing exact derivations — the GKO coset
    `(SU(2)₂×SU(2)₁)/SU(2)₃` (`SU(2)₃` = the golden level), the Virasoro minimal `M(4,5)`, the N=1 superconformal
    series (`m=3`); the 6 TCI primaries `{0,1/10,3/5,3/2,7/16,3/80}` (the `h=3/2` = the supercurrent); the golden
    quantum dimension `d₁(SU(2)₃)=φ`; and **`content(RᵐLᵐ)=m`** — L39/B219's period-controlling invariant *is* the
    multiplicity (= B212's congruence modulus = B204's `gcd(a,b)`). All `[exact]`.
  - **B222 (Act I; V225).** Momentum-resolved ED (with a machine-precision correctness gate
    `⊕ₖ spec(Hₖ)=spec(H_full)`) reproduces the **full** tricritical-Ising operator content: NS `{0,1/10,3/5,3/2}`
    **including the `h=3/2` supercurrent** at `x=3.0` essentially exactly (`[reproduced]`), and the Ramond
    primaries `{3/80,7/16}` from the odd-N sector (`[consistent]`). Emergent N=1 SUSY confirmed from the spectrum.
  - **B223 (Act II; V226).** The golden chain's SUSY is **emergent/IR-only** — no conserved `(−1)^F`
    (`‖[H,(−1)^F]‖=0.97`, `[TESTED-NEGATIVE]`) — while **exact lattice N=2 SUSY** lives on the Fendley–Schoutens
    sibling of the same Lucas Hilbert space (`Q²=0`, `H={Q,Q†}`, integer Witten index, `E_gs=0`; `[exact]`). The
    SUSY is collective/external, not on-site.
  - **S040 (firewalled).** The two-SUSY question (the figure-eight's licensed 3d-3d SUSY, `M_SUSY≅M_flat`,
    vs the emergent chain SUSY — bridged by `SU(2)₃` on both sides; a HOOK, not asserted) and the "external"
    thesis (interaction manufactures the *symmetry*; the *scale* enters from outside). Physics classical
    (Friedan–Qiu–Shenker; Feiguin 2007; Fendley–Schoutens); novelty UNCHECKED. **Nothing to `CLAIMS.md`;
    P1–P16 untouched; no `[proved]` on any physics reading.**
- **B220 — L41 closed: the golden (Fibonacci anyon) chain CFT reproduced in-sandbox, `c=7/10` (2026-06-26;
  V223).** The B218 residual. B218 *cited* the chain CFT `c=7/10` because a first ED gave a **gapped artifact**
  (`c≈0`). Corrected ED: the golden chain (`N` Fibonacci anyons on a ring; fusion-path basis `l∈{1,τ}`; constraint
  no-two-adjacent-identities; Hilbert dim = Lucas `L_N`); local term = projector onto the **identity** fusion
  channel, the only nontrivial piece the `(τ,τ)` rank-1 block `P = F·diag(1,0)·F = [[φ⁻²,φ⁻³ᐟ²],[φ⁻³ᐟ²,φ⁻¹]]`.
  **The bug before:** the off-diagonal `φ⁻³ᐟ²` (the kinetic term) was dropped → a trivially gapped chain. With
  `H_AFM=−Σĥ_i`, `c` from the PBC entanglement entropy (slope → `c/3`, no velocity): `N=14..22` is **gapless**
  (`gap·N≈0.86` const) with `c_ent≈0.71` (mean `N≥16` = 0.7135) = **tricritical Ising `c=7/10`**, distinct from 0
  (gapped) and 0.8 (Potts). FM → 3-state Potts `c=4/5` consistent but noisier. So the chain CFT is now
  **reproduced, not cited** (upgrades B218 `[cited]`→`[reproduced]`). Physics classical (Feiguin 2007); the
  contribution is the correct in-sandbox reproduction. **Firewall:** a dimensionless central charge, not a scale.
  **Nothing to `CLAIMS.md`; P1–P16 untouched.**
- **B219 — L39 resolved: the class-field period law is the form CONTENT (elementary), not genus-theoretic — overturns
  B216 (2026-06-26; V222).** A **compute-before-deferring win**: B216/V219 deferred the `f≥8` boundary to a
  specialist (genus theory); the actual answer is **elementary**. The period-controlling invariant is the
  binary-quadratic-form **content** `content(γ)=gcd(b,c,a−d)` = the largest modulus where `γ ≡ s·I` for *any* scalar
  `s`. **Theorem (verified):** `P(γ)=lcm(t−2,t+2)/content(γ)`, a function of `(trace, content)` **only — no genus
  dependence**. B216 tested `γ≡±I` (only ±1), which fails at `f=8` because `(ℤ/2^k)^×` has extra square-roots of 1
  for `k≥3` (mod 8 = {1,3,5,7}); `GAMMA_A=[[13,−8],[−8,5]]≡5·I (mod 8)` → true content 8, not 4. **Decisive:**
  exhaustive `f=8` (`t=18`, `D=320`, all four genera) — every content-1 class has period 80 (334 reps), content-2→40,
  content-4→20, content-8→10; **genus-independent** (B216's "not minimal" flags were short-window detector false
  positives). Generalizes to `f=16` (`9·I mod 16` → period 68); reproduces B204 (`content(RᵃLᵇ)=gcd(a,b)`).
  **Overturns B216/V219** (NEEDS-SPECIALIST → RESOLVED). Novelty UNCHECKED. **Nothing to `CLAIMS.md`; P1–P16
  untouched.**
- **B218 — does metallic *multiplicity* select an emergent theory? Yes: golden, the unique anyon (2026-06-26;
  V221).** The probe of the interaction/multiplicity thesis. **Answer (exact): multiplicity selects golden** as the
  *unique* anyon-realizable metallic mean, via the **Jones-index selection** — `λ_m<2` (a quantized unitary anyon
  dimension) iff `m=1`; `λ_1=2cos(π/5)=φ` exactly = the **Fibonacci anyon** (SU(2)₃ = the dual-McKay E₈ point,
  B206/B210); `λ_m≥1+√2>2` for `m≥2` (above the index-4 wall). The golden **anyon chain** flows to a specific CFT
  (tricritical Ising `c=7/10`, Feiguin 2007) — **cited, not reproduced** (my in-sandbox ED was inconclusive: a
  first anyon-chain Hamiltonian was buggy/gapped, the XXZ proxy under-resolved near criticality; flagged, not
  banked). **Firewall (the thesis limit):** what multiplicity selects is a **dimensionless topological/CFT
  structure** (an anyon theory, a central charge), **not** physical content/scale — chiral fermions + the SM are
  theorem-blocked (Nielsen–Ninomiya). So "content from multiplicity" = **selected topology** (golden / Fibonacci /
  tricritical-Ising), not emergent scale — the most positive honest answer the object supports. Novelty UNCHECKED.
  **Nothing to `CLAIMS.md`; P1–P16 untouched.**
- **B217 — L40 resolved: the Borromean bridge is the geometric origin of the VOLUME (cusped), not the period
  (closed/algebraic) (2026-06-26; V220).** chat1's L40 asked whether B204's period law has a geometric origin via
  the Borromean parent (L31). **Answer (computed): no** — the period and the Borromean live on *different*
  manifolds sharing only the monodromy `γ` (the closed-Sol / cusped-hyperbolic duality, V200). (1) B204's
  `Z_k=tr(ρ_k(γ))` is the **closed** torus bundle: verified `Z_k(identity)=Z(T³)=k+1`; the figure-eight closed
  bundle is the period-5 `1/φ` object — **the period is algebraic** (B204–B216). (2) The **cusped** figure-eight
  (m004 = 2 ideal tetrahedra; the metallic family = Borromean Dehn fillings, L31) carries the hyperbolic **volume**
  via the Kashaev volume conjecture: `(2π/N)log⟨4_1⟩_N → Vol=2.02988` (confirmed with the Ohtsuki `(3π logN)/N`
  correction). **The Borromean parent governs the VOLUME, not the period.** A Borromean surgery presentation of the
  closed bundle reproduces `Z_k` only by topological invariance — a re-presentation, never an explanation —
  confirming + sharpening chat1's caveat (it can only reproduce; it actually governs a *different* invariant). So
  the period's origin is algebraic (trace/Gauss sums); the Borromean/geometric content is the volume. Novelty
  UNCHECKED (closed/cusped + volume conjecture classical; the L40 resolution for this family is the contribution).
  Firewall: standalone quantum-topology/hyperbolic geometry; **nothing to `CLAIMS.md`; P1–P16 untouched.** The
  WRT-period arc (B204→B214→B215→B216→B217) is now complete in-sandbox; the f≥8 genus theory is the specialist
  residual.
- **B216 — the f≥8 boundary of the class-field period law: genus-theoretic, NEEDS-SPECIALIST (2026-06-26; V219).**
  The focused attack on L39 (B215's `f≥8` residual). (A) Built a **correct, validated general WRT factorization**
  (`SL(2,ℤ)→S,T`) so `Z_k(γ)=tr(ρ_k(γ))` is computable for *arbitrary* `γ`, not just block words — validated to
  machine precision against B204/B214's block-word `Z` (a real bug in a first quick version was caught and fixed:
  the `e=−1` final block is `S²T^{−m}`, not `−T^m`). (B) **The obstruction:** at `f=8` (`t=18`, `D=320`) two
  **non-conjugate** classes `[[13,−8],[−8,5]]` (d=8) and `[[17,−4],[−4,1]]` (d=4) have **identical** elementary
  invariants (scalar-depth 4, order-profile (1,1,2,4)) — so `d` is **not** a function of scalar-depth or
  order-mod-2^k; it is a finer **form-class / genus** invariant (Latimer–Macduffee = the repo's B92). All
  elementary refinements fail uniformly. **Verdict:** the full `f≥8` law is genus-theoretic (2-adic genus /
  spinor-genus / metaplectic level) → **NEEDS-SPECIALIST** — a *named* boundary (the counterexample + the validated
  tool), reached by computing to **exhaustion** of the elementary methods. B215 stands exact for `f∈{2,3,4}`.
  Novelty UNCHECKED. Firewall: standalone quantum-topology/arithmetic; **nothing to `CLAIMS.md`; P1–P16 untouched.**
  (L39's algebraic side now: closed form f≤4 + genus-theoretic boundary f≥8; the geometric Borromean bridge is the
  separate L40.)
- **B215 — the class-field period law: the closed form for B214's conductor-split (2026-06-26; V218).** Hunted and
  **found** the closed form: `P(γ) = lcm(t−2,t+2)/d(γ)`, with `d(γ) = max{d′∣f : γ ≡ ±I (mod d′)}` — the
  **scalar-reduction depth** of the conjugacy class (how deep `γ` reduces to the center `±I`). **Verified exact for
  conductor `f ∈ {2,3,4}`** (every class at `t=6,7,10,11,14,22`; the depth ranges over all divisors of `f`). The
  SL(2,ℤ) classes of trace `t` are the ideal classes of the order `ℤ[λ]` of conductor `f` (Latimer–Macduffee = the
  repo's B92), so the period reads the **form class** via its scalar depth — `B204 → B214 → B92`. **Named boundary
  (open):** at `f=8` (`t=18`, the golden field with conductor 8) the law is incomplete — the `≡I mod 4` class splits
  by `d=4` as predicted, but two order-2-mod-2 classes split by an extra factor 2 the scalar criterion misses (and a
  naive "order-2" rule is refuted: `f=2`'s order-2 class has `d=1`, `f=8`'s have `d=2`); the higher-2-power split is
  a finer 2-adic phenomenon → NEEDS-SPECIALIST. Novelty UNCHECKED (Gauss-sum period theory classical; the
  scalar-depth form is the candidate-new piece). Firewall: standalone quantum-topology/arithmetic; **nothing to
  `CLAIMS.md`; P1–P16 untouched.** Next: the Borromean-surgery bridge + the 2-adic refinement (`OPEN_LEADS` L39).
- **B214 — the general-word WRT period law + its class-field refinement + the Funar deflation (2026-06-26; V217).**
  Extends B204 off the metallic diagonal: for *arbitrary* hyperbolic words `γ=∏R^{aᵢ}L^{bᵢ}∈SL(2,ℤ)`, the WRT
  level-period is, **on the principal class, `P(γ)=lcm(det(γ−I),det(γ+I))=lcm(tr−2,tr+2)`** (verified on many
  words, distinct traces, incl. non-symmetric). **The new content — a class-field refinement:** the period reads
  the conjugacy / **ideal class** (Latimer–Macduffee; the repo's B92), not just the trace — at *fundamental*
  discriminant `D=t²−4` (conductor `f=1`) all classes share the period, but at conductor `f>1` it **splits**
  (non-principal classes get `lcm/d`, `d∣f`: `D=32→{8,4}`, `D=45→{45,15}`, `D=320→{80,40}`); B204 lived where
  `h=1`, so the split was invisible. **The deflation (verify-don't-trust on both an over-read and a relayed
  claim):** three trace-15 words give identical `|Z|`, but that is neither "content from interaction" (a same
  monodromy giving the same invariant is the *definition* of a topological invariant) **nor** "all three are
  conjugate" (orbit reduction: `M₁~M₂` conjugate, but `M₀` is **not** — yet identical `|Z|`, period 221 = **Funar's**
  non-conjugate-same-WRT phenomenon). So `|Z|`-equality ≠ conjugacy; the banked content is the formula + the
  conductor-split. Novelty: Jeffrey + Funar known; the conductor-split closed form is the candidate-new piece
  (UNCHECKED). Firewall: standalone quantum-topology/arithmetic; **nothing to `CLAIMS.md`; P1–P16 untouched.** Next:
  the exact class-field period law + the Borromean-surgery bridge (`OPEN_LEADS` L39).
- **B213 + S039 — the do-or-die program, Act I: the Higgs-side period data (firewalled; 2026-06-25; V216).** The
  owner's do-or-die question (explain the cosmological-constant problem / unify QM–GR) taken at full weight, behind
  the firewall (`speculations/S039`, POSTULATED). The move: the firewall (no invariant sources a scale) is banked
  across 3 modes (K018); the one bridge built-up-to-but-not-crossed is the **Hitchin/Higgs side**, where the scale
  would live (B169). B211 gave the key — the figure-eight character variety **is** the elliptic curve `40a1`, a
  genuine Higgs-side handle. **Act I (computed):** does it carry a forced tiny dimensionless number (a CC-hierarchy
  candidate)? **No** — `40a1` data all `O(1)`/BSD-generic (`Ω=1.484`, `L(E,1)=0.742`, `L/Ω=1/2` exact, `Ш=1`,
  regulator 1, Mahler `m(Φ)=0.742≈Ω/2`); the **null test** kills the only candidate (`L/Ω=1/2` is generic — every
  rank-0 curve gives a simple BSD rational), so no numerology survives (S014 stays dead). **The firewall holds a
  4th independent time, now on the Higgs side** (confirms B181: criticality ⇒ no hierarchy). Structural find:
  conductor `40=2³·5` sees the golden/`E₈` prime 5 (`ℚ(√5)`), not the hyperbolic prime 3 — the variety is a Betti
  object, its arithmetic tracks the Betti/monodromy side. **The positive structural claim banked (S039, [LEAP]):**
  vacuum-energy scale is a **form↔filling matching datum**, not an intrinsic output; the canonical object
  (figure-eight) sits *at* the `Λ=0` vacuum `κ=−2` (B67). Not a solution — a proof, in a fully-computable toy, of
  *where the scale must come from and why this structure cannot supply it.* Acts II/III + the metallic tower stay
  open. Firewall: physics readings are one-way HOOKs; no `[proved]`; **nothing to `CLAIMS.md`; P1–P16 untouched;**
  the 4d-gravity lift stays NEEDS-SPECIALIST (K006).
- **B212 — the metallic congruence/monodromy shadow, computed (corrects B210's silver line; 2026-06-25; V213).**
  chat1 flagged that B210's "silver = degenerate prime 2 → S₃ both sides" was *assumed by analogy* — the exact
  asserted-not-computed pattern the golden verify-it-all pass (V210) and the V212 re-audit kept catching. Computed:
  (1) the **congruence-group shadow** `⟨R,L⟩ mod (m²+4) = SL(2,ℤ/N)` (golden 120=2I=E₈, silver 384=SL(2,ℤ/8),
  bronze 2184=SL(2,𝔽₁₃)) — a property of the modulus; (2) the **monodromy element** `RᵐLᵐ mod p` is order `2Q(m)`
  generically but **`≡ I` for even m** — silver `R²L² ≡ I mod 2` is **trivial, not S₃** (the "S₃" is the `⟨R,L⟩`
  *group*, conflated); (3) the **proved law** `RᵐLᵐ≡I mod p ⇔ p∣m ⇔ p=2,m even` (m=1..15); (4) the **hyperbolic**
  shadow (m136 via snap) is trace-**degenerate** — silver's square-traces `2,±2i` all `≡0 mod (1+i)` ⇒ no order-3
  element survives (no McKay-exceptional structure, vs golden's full `2T=E₆`), while the holonomy is a **quaternion
  order over ℚ(i)** (square-matrices not in `SL(2,ℤ[i])`) so the image-**group** is a named residual. Net: B210's
  silver line corrected; golden's `2T=E₆`/`2I=E₈` (integral & full) unaffected. Firewall: McKay rep-theory, not
  physics; **nothing to `CLAIMS.md`; P1–P16 untouched.** Resolves `OPEN_LEADS` L35 (+ the L29 shadow-structure).
- **B211 — the metallic family's three faces: geometric limit, chirality spectrum, and the arithmetic of the
  variety itself (2026-06-25; V211).** The six remaining *computable* leads (L29–L34), run properly and verified —
  each computed (not asserted), with its load-bearing step locked in a test. **Headline (L34, a new arithmetic
  face):** the arithmetic of the character *variety* itself (its Weil zeta over `𝔽_p`), never touched — all prior
  arithmetic was a number *field* (monodromy `ℚ(√(m²+4))` or hyperbolic trace `ℚ(√−3)`). The figure-eight's
  non-abelian `SL(2,ℂ)` character variety polynomial `Φ(x,z)=z²−(x²+1)z+(2x²−1)` is **derived** from the Riley
  relator and **verified** at the complete structure (`x=2 → u²+u+1`, roots `ω`). It is an irreducible genus-1 curve
  and **`#X^{na}(𝔽_p) = p − 1 − a_p(E)` exactly** (23 good primes `p≤97`) for `E: y²=x(x−1)(x−5) =` Cremona
  **`40a1`** (conductor 40, `j=148176/25`, **non-CM**, rank 0): the variety is birational to a weight-2 newform of
  level 40 — *not* the `ℚ(√−3)` of the trace field (whose ramified prime 3 isn't even among the variety's bad primes
  `{2,5}`). **L31:** drilling the short core geodesics of `RᵐLᵐ` returns `m`-independently the **Borromean rings
  complement** (`6³₂=L6a4=t12067`, two ideal octahedra, vol `2·v_oct`) — the metallic bundles are large-twist Dehn
  fillings of one fixed parent (corrects B207's then-unearned "→Borromean"). **L32:** every `RᵐLᵐ` (`m=1..6`) is
  **amphichiral** (isometric to its orientation-reversal) ⇒ `CS=0` for all `m` (firewall L15 holds family-wide).
  **L33:** the B204 WRT level-period **is a Pisano period** of `x_{n+1}=m·x_n+x_{n−1}` (`π(m,m²+4)=4Q(m)`,
  `P_WRT=(m/4)π`). **L29:** `ord(RᵐLᵐ mod m²+4)=2Q(m)`. **L30 (resolved-neg):** the skein quotient at
  `q=e^{2πi/5}` (`SU(2)₃` Verlinde, rank 4) is **not** the `2I` rep ring (rank 9) — consistent with B210's WRT image
  of order 2880; the WRT/skein↔shadow link is arithmetic (B208), not a rep-ring identity. Novelty **UNCHECKED** on
  L34 (the `40a1`/Weil-zeta framing — the polynomial is classical), L31 (likely folklore), L33 (Pisano standard);
  L32/L29/L30 are characterizations/consequences. Firewall: standalone low-dim topology / arithmetic geometry /
  quantum topology; **nothing to `CLAIMS.md`; P1–P16 untouched.** `frontier/B211_metallic_arithmetic_geometric_faces/`
  + `tests/test_b211_metallic_faces.py` (7 locks, the L34 relation load-bearing). `OPEN_LEADS` L29–L34 → DONE.
- **B210 — golden's dual McKay (E₈ + E₆); WRT image ≠ 2I; computable-paths catalog (2026-06-25; V209).** Two
  uncomputed paths, run. **(1) Dual McKay:** the metallic bundles' *complex* hyperbolic invariant trace fields
  (the cusped manifold's arithmetic, distinct from the real monodromy field) — golden = `ℚ(√−3)` (m004),
  silver = `ℚ(i)` (m136), bronze deg 8, m=4 deg 4. So golden carries **both** exceptional McKay-congruence
  groups: `E₈` (monodromy `ℚ(√5)` mod 5) **and** `E₆` (hyperbolic `ℚ(√−3)` mod 3) — the two exceptional McKay
  primes {3,5}; `E₇=2O` excluded (not a congruence quotient). Golden is the *unique* metallic mean hitting
  exceptional McKay primes on both arithmetics (silver = degenerate 2; bronze+ non-arithmetic). **(2)
  Resolved-negative:** the WRT modular-rep image at the golden level is order **2880** (`SL(2,ℤ/20)`-related),
  **not** `2I` — so the quantum face is a bigger object; the WRT↔shadow link is purely arithmetic (`m²+4`, B208),
  not a group iso. Also **marked all computable paths** (`OPEN_LEADS` L27–L34, with status). Novelty UNCHECKED;
  McKay/rep-theoretic `E₆`/`E₈`, not physics; nothing to `CLAIMS.md`; P1–P16 untouched.
- **B209 — the classical/quantum boundary: the tiling sees A₅, the spinorial E₈-completion is absent (2026-06-25; V208).**
  The icosahedral quasicrystal's exterior algebra `Λ*(ℝ⁶)` (A₅ acting via `3⊕3'`) decomposes into exactly the **5
  bosonic A₅ irreps**, each at multiplicity **4** (total `64=2⁶`; the golden ratio in the character table cancels
  to a clean 4). The **4 spinorial irreps of the double cover `2I` — `{2,2',4',6}`, exactly the affine-`E₈` nodes
  beyond `A₅` — are absent**: the classical tiling sees only `A₅`; the `E₈`-completing spinorial irreps require
  the quantum/spin lift `2I` (the `SL` level of B206 vs classical `PSL=A₅`). The classical/quantum boundary **is**
  those 4 irreps — the same spin `ℤ/2` as B206, made concrete as which representations are visible classically vs
  only quantumly. McKay/representation-theoretic `E₈`, not physics' `E₈`; firewalled. Nothing to `CLAIMS.md`.
- **B208 + synthesis punchline — the WRT period and the congruence shadow are the same arithmetic (2026-06-25; V207).**
  B204 (the WRT period, Face IV) and B206 (the congruence shadow, Face I) are two reads of one homological
  invariant `det(γ+I)=m²+4`: `squarefree(m²+4)` (the field radicand) **always divides** `P(m)`, and at golden the
  three collapse — `P(1)=5 = det(γ+I) = disc ℚ(√5) = the McKay prime`, `SL(2,𝔽₅)=2I=E₈` (the three 5's are one).
  And `papers/metallic_one_object/SYNTHESIS.md` finally gets its **punchline (§9)**: the four faces are shadows of
  one conjugacy class whose arithmetic shadow at disc 5 is the unique exceptional McKay group — golden-specific
  because 5 is *simultaneously* the smallest fundamental discriminant (extremal) and the largest McKay prime
  (exceptional); the minimal point and the exceptional point are the same point, for the same reason. Nothing to
  `CLAIMS.md`; P1–P16 untouched.
- **B207 (symmetry-breaking door, finished) — no GUT chain (2026-06-25; V206).** Finished the symmetry-breaking
  door with a clean **arithmetic negative**: `E₆=2T=SL(2,𝔽₃)` never occurs (`m²+4≡1,2 mod 3`, 3 never ramifies);
  `E₇=2O` never occurs (`|2O|=48` is no `|SL(2,𝔽_p)|`); only `E₈` (`ℚ(√5)`, m=1,4,11) is hit. So the `E₈→E₆`
  branch is golden's *internal* subgroup lattice, **not** a family-realized chain, and the dynamics selects
  `2D₅` not `2T`. The object does **not** realize a GUT-style symmetry-breaking chain — the firewall holds; the
  genuine structures are the κ=2 wall (dynamical) and golden's isolated `E₈`. Flips the S038 item to
  done-negative. Nothing to `CLAIMS.md`.
- **B207 (scale door, computed) — the metallic bundle volumes are bounded (2026-06-25; V205).** Pushed the
  scale door with SnapPy: the hyperbolic volumes of `RᵐLᵐ` (m=1=figure-eight) are **bounded and converge** —
  golden = `2·v_tet` (the minimal cusped hyperbolic volume), silver = `v_oct` exactly (m136), `Vol_m ↗ 2·v_oct`
  (Borromean) as m→∞. So the volume-conjecture rate `e^{N·Vol_m/2π}` **saturates**: the object can't supply an
  unbounded exponential rate; **all unbounded scale is the level `N`** — confirms + sharpens the firewall (B151).
  Golden = the minimal rate (extremal again). *Verify-don't-trust:* an initial pass misread the volumes as
  linear growth; canonizing to geometric triangulations showed convergence. Flips the S038 scale item to done.
  Nothing to `CLAIMS.md`.
- **B207 + S038 — the firewall-content push: scale & symmetry breaking (2026-06-25; V204).** Per owner steer
  (keep the math threads; push the firewall content questions). Firewall-clean math (`frontier/B207`) + the
  firewalled reading (`speculations/S038`, POSTULATED, one-way, nothing to `CLAIMS.md`). **Symmetry breaking:**
  the golden shadow `2I=SL(2,𝔽₅)=E₈` (B206) read as `G→H` — the metallic dynamics `⟨RL⟩` selects residual
  `2D₅`; the finite McKay sub-chain `2I⊃2T(=E₆)` but `2I⊉2O(=E₇)`, so golden's shadow breaks **`E₈→E₆`,
  skipping `E₇`** (icosahedron has no octahedral subgroup) — *finite-group structure, firewalled from gauge*;
  and breaking is *generic not fine-tuned* (the κ=2 wall). **Scale:** the metallic dimensionless scale-spectrum
  grows only **logarithmically** (no intrinsic exponential hierarchy), so any hierarchy is a quantization-**level**
  effect (volume conjecture), not the geometry — *confirms* the firewall (B151) and *locates* where a scale
  would enter; golden is the *least-hierarchical* point (the triple coincidence at 5: extremal + exceptional +
  least-hierarchical). Negatives kept prominent (gauge free, spacetime (1,1), chirality mirror-closed, no
  absolute scale — the closed doors). Both pushes confirm relocation, do not breach. Nothing to `CLAIMS.md`;
  P1–P16 untouched.
- **B206 — the golden object's spin shadow is 2I = SL(2,𝔽₅) = McKay-E₈ (2026-06-25; V203).** The McKay seam
  question, computed (not hedged). The golden mean (`m=1`, field `ℚ(√5)`, disc 5) has congruence shadow
  `SL(2,𝔽₅) = 2I` (binary icosahedral = McKay partner of affine `E₈`). Classical/trace level = `PSL(2,𝔽₅)=A₅`
  (5 irreps); quantum/spin level = `SL(2,𝔽₅)=2I` (9 irreps = affine `E₈` marks); the `ℤ/2` between them is the
  center `{±I}` = the spin cover SU(2)→SO(3) = the half-trace `κ=4I+2`; the **4 extra spinorial irreps `{2,2,4,6}`**
  are what the quantum level sees and the classical cannot. So "does the quantum level carry spinorial structure
  the classical can't?" = **yes, structurally** (not a φ-rhyme). **Golden-specific:** `SL(2,𝔽_p)` is
  binary-polyhedral only for `p≤5`, and only the `ℚ(√5)` family (`m=1,4`) hits disc 5 — golden is the unique
  metallic mean whose spin shadow is McKay-`E₈`. **Honest:** ingredients all standard (assembly is the
  contribution); novelty **UNCHECKED** (golden↔`E₈` known in physics, Coldea 2010; → L26). **Firewall:** this is
  McKay/representation-theoretic `E₈`, **not** physics' `E₈` gauge group. Nothing to `CLAIMS.md`; P1–P16 untouched.
- **Synthesis — "the metallic once-punctured-torus object, seen four ways" (2026-06-24; V202).**
  `papers/metallic_one_object/SYNTHESIS.md`: a synthesis / cross-face dictionary (an **exposition, not a new
  theorem**) assembling one object — the `SL(2,ℤ)` trace map / metallic mean `λ_m` — through four lenses:
  **(I)** character variety / Fricke trace map (incl. the SL(n) tower as higher-rank Face I), **(II)** closed
  geodesic on the modular surface (`ℓ=4 log λ_m`, multiplier `λ_m²` = Cantat–Loray dynamical degree), **(III)**
  Fibonacci/quasicrystal spectrum (`κ=2+λ²`, Kohmoto), **(IV)** quantum (WRT = Jeffrey 1992 at roots of unity;
  skein/DAHA at generic `q`). The hinge: `λ_m²` is simultaneously the geodesic multiplier, the dynamical degree,
  and the trace-map periodic-orbit multiplier (verified). **No novelty claimed** — each face is banked
  (B71/B148/B150/B198–B205, K002/K007/K010, B160–B186) or literature-owned (Jeffrey, Cantat–Loray,
  Damanik–Gorodetski, DAHA/MGO); the contribution is the unified map. Explicit scope boundary (Ω cone, Hitchin
  flow, off-axis spectral, chirality barrier marked out-of-scope); firewall + proven-core relation stated;
  cross-referenced to `STRATEGIC_SYNTHESIS.md`/`ARCHITECTURE.md`. Consolidates the four-leads investigation
  (exponent → no-law; period → Jeffrey; unification → trace-map core; quantum → DAHA), whose meta-finding is
  that the object is real but **well-charted mathematics**. Nothing to `CLAIMS.md`; P1–P16 untouched.
- **B205 — the quantum (skein) trace map for the metallic family (2026-06-24; V201).** The "quantum swerve"
  (path C) — the first **generic-`q`** (not root-of-unity, so *not* WRT/Jeffrey) quantum computation in the repo.
  Derives + **verifies** the Kauffman-bracket skein algebra of the once-punctured torus, its central element
  `Ω(q)` (solved, verified central; classical limit = the Fricke `κ=tr[A,B]`, half-trace), and the quantum Dehn
  twists `R_q,L_q` as **verified automorphisms** (preserve all relations + `Ω`; classical limit = the Kohmoto
  trace map). q-Chebyshev `[m]_q` structure. **Honest novelty (`NOVELTY.md`): the machinery is KNOWN** — skein
  algebra (Bullock–Przytycki), the `SL(2,ℤ)` action = the Askey–Wilson algebra / spherical DAHA
  (Terwilliger; Cherednik). B205 = the in-repo construction + verification + metallic specialization; **no theorem
  claimed**; the "quantum metallic mean" (à la Morier-Genoud–Ovsienko) is **UNCHECKED, suspected already-known**.
  Standalone quantum-algebra; nothing to `CLAIMS.md`; P1–P16 untouched.
- **B204 — the WRT level-period law for once-punctured-torus bundles (2026-06-24; V197).** Pins the live Path-A
  metallic period question and shows the metallic law is the **diagonal** of a law for **all** once-punctured-torus
  bundles `RᵃLᵇ`. The SU(2)_k Reshetikhin–Turaev modular trace `Z(a,b;k)=tr(ρ_k(RᵃLᵇ))=tr(TᵃST⁻ᵇS⁻¹)` has level-period
  **`per|Z(a,b)| = lcm(a,b)·(4+ab)/gcd(4+ab,4)`** (predict-then-confirm on 21 `(a,b)` + 12 metallic cells, all
  fundamental). The metallic diagonal `a=b=m` gives **`P(m)=m(m²+4)/gcd(m²+4,4)`** (`P(1..8)=5,4,39,20,145,60,371,136`;
  `m=1` reproduces chat1's verified figure-eight period-5 `Z={1,0,−1/φ,0,1}`). The period is read off the mapping
  torus: `4+ab=det(γ+I)` (homology) × `lcm(a,b)` (twist). **Why the metallic family is special:** the constant phase
  `e^{−2πi(a−b)/(4n)}` is 1 iff `a=b`, so metallic `Z` is *real* and periodic; for `a≠b` only `|Z|` is periodic.
  **Periodicity PROVED (V198, `PROOF.md`):** `Z̃` extends to a full period (`sin²` vanishes at the boundary) →
  clean Gauss sums; Landsberg–Schaar gives the diagonal (the `√(2n)` amplitudes cancel `1/(2n)` — why a
  growing-dimension trace stays bounded & periodic), 2D Gauss reciprocity gives the cross (binary form
  `det = −(4+ab) = −det(γ+I)`); `per(diagonal)=lcm(a,b)` is proved. The exact period is verified on 14 cells; a
  closed form for the cross Gauss-sum period is the one remaining lemma to full `[proved]`.
  **Corrects** the prior exploratory memo ("no clean law / period absent when `m²+4` prime" — a search-bound artifact;
  `m=1`, disc 5 prime, has the smallest period). **Novelty CHECKED (V199, `NOVELTY.md`) — DEFLATED:** an
  adversarial 99-agent prior-art pass found the framework **and** the proof mechanism are KNOWN — `Z_k=tr(ρ_k(A))`
  of a torus-bundle mapping torus as a quadratic Gauss sum via reciprocity is exactly **Jeffrey 1992** (CMP 147,
  eq 4.8 for `|Tr|>2`, which already carries *both* `|Tr∓2|` moduli = `ab` and `4+ab`); our proof re-derives her
  method. Exact SU(2)_k periodicity is PARTIALLY-KNOWN (congruence subgroup property + Funar's abelian
  `|Z_k|=|H¹|^{1/2}`); the explicit `(a,b)`-period and metallic reality are APPEARS-NOVEL but NEEDS-SPECIALIST
  (the period likely drops out of Jeffrey eq 4.8; reality likely folklore). **Framing corrected:** `Z_k` is the
  WRT invariant of the **closed-torus** mapping torus (Jeffrey's Sol-manifold object), not the cusped
  punctured-torus bundle — shared monodromy, different 3-manifold. **Do not claim novelty.** Standalone
  quantum-topology/arithmetic; nothing to `CLAIMS.md`; P1–P16 untouched.
- **B203 — the 4 silver SL(3) components classified: all irreducible & cusped-type (2026-06-24; V196).** Identifies
  the new silver component (B201's comp3) and **explains B202** (resolves OPEN_LEADS L23(b)). All four components of
  the silver SL(3) character variety are **irreducible** (Burnside dim 9) with **A, B, µ of infinite order**
  (continuous trace) — cusped/loxodromic-type, **none a finite-order-A Dehn-filling component**. So comp3
  (`{tr A+tr A⁻¹=−1, tr B+tr B⁻¹=−1}`, no figure-eight analog) is a *genuine new irreducible* component. **Why this
  explains B202:** the figure-eight's tidy `M³=L`/`M³L=1` live on its *finite-order-A* Dehn-filling components
  (`W1={x1=x4=1}` → `A=diag(1,i,−i)`, order 4); silver has no such torsion locus, so no tidy `[A,B]=c·µᵏ`. The
  figure-eight's tidy Dehn-filling A-variety is a special low-trace phenomenon, absent for m≥2. Completes the silver
  SL(3) story (B201 → B202 → B203); silver SL(3) A-polynomial uniformly Falbel-size → `NEEDS-SPECIALIST` (B199).
  Standalone character-variety math; P1–P16 untouched; nothing to `CLAIMS.md`.
- **B202 — the silver SL(3) A-variety: no tidy `[A,B]=c·µᵏ` (2026-06-24; V195).** Completes the SL(3)
  metallic-A-polynomial direction (B201 → its peripheral relations; resolves OPEN_LEADS L23(a)). **Result
  (validated):** the silver (m=2) bundle has a *correct commuting* cusp meridian `µ=A⁻²t` (B154; `cdev~1e-9` on all
  four components), but **none of its four character-variety components carries a tidy matrix relation `[A,B]=c·µᵏ`**
  (matexp best-score medians 16.1, 6.5, 2.8, 1.2 — all ≫1e-6) — whereas the figure-eight's Dehn-filling components do
  (`W1: c·µ³ = M³=L`; `W2: c·µ⁻³`). So **the figure-eight's tidy Dehn-filling A-variety is non-generic** in the
  metallic family; the silver A-variety is all-Falbel-size. **Method:** the pairing-free **matrix exponent**
  (`[A,B]·µ⁻ᵏ` scalar; B71/B198), gated on the figure-eight (recovers `M³=L`/`M³L=1` exactly) — fixing the
  eigenvalue-ordering scramble that sank B201 Part 2. Honest SL(3) picture now complete: SL(2) tidy (B67/B69); SL(3)
  figure-eight tidy only on its trace-1 Dehn-filling components (B71); SL(3) silver no tidy component at all (B202) →
  closed-form silver SL(3) A-polynomial `NEEDS-SPECIALIST` (per B199). A verify-don't-trust arc (the ratio pipeline
  failed its gate → not banked → matrix-exponent method gated → the negative banked). Standalone character-variety
  math; P1–P16 untouched; nothing to `CLAIMS.md`.
- **B201 — the metallic (silver) SL(3) character variety from the trace-map fixed locus (2026-06-24; V194).**
  Extends B71 (figure-eight SL(3)) to the metallic family — the SL(3) face of "the metallic A-polynomial on the
  geometric component" (the object the B199 integer exponent was a shadow of). **Part 1 (banked, exact):** the silver
  (m=2) bundle monodromy `T_2²` (B48 metallic trace map) has fixed locus `Fix(T_2²)` decomposing into **four** dim-2
  components — **one more than the figure-eight's three** — the geometric `{tr A=tr A⁻¹, tr B=tr B⁻¹}` (same form as
  B71's V0, contains Sym²), two Dehn-filling-type, and a **new `{tr A+tr A⁻¹=−1, tr B+tr B⁻¹=−1}` component with no
  figure-eight analog**. m=1 reproduces B71's 3 components exactly (validation). So the silver SL(3) character variety
  is *richer* than the figure-eight's. **Part 2 (deferred, not banked):** the per-component peripheral A-variety
  relations (the silver analog of B71's `M³=L`) — a quick in-house pipeline failed its figure-eight `M³=L` validation
  gate, so per verify-don't-trust nothing from it is banked; the fault is isolated (B71's *native* peripheral machinery
  recovers `M³=L` cleanly), and the correct next step (explicit silver component parametrizations → B71-native
  peripheral with `µ=A⁻²t`) is recorded. Expected: Dehn-filling tidy, geometric Falbel-size (NEEDS-SPECIALIST, per
  B199). Standalone character-variety math; P1–P16 untouched; nothing to `CLAIMS.md`.
- **B200 — verification of the chat1 independent-computation handoff (2026-06-24; V193).** Three incoming
  "MATH" results re-derived before banking (verify-don't-trust; cf. B197 for chat2). **R2 VERIFIED + banked:**
  *on-site is the unique finite-range interaction preserving the Fibonacci Sturmian alphabet* — the paired potential
  `V_n+V_{n+d}` at d=1 (NN) has 2 values but complexity `p(4)=6` (not Sturmian), d=2 (NNN) has 3 values; only d=0
  preserves it (structural reason: d≥1 sees *pairs*). Refines K019 / the B171–B176 interaction frontier; honest scope
  (alphabet-preserving is a proxy for metallic-preserving). **R1 REFUTED:** the "κ₁=κ₂=3 at U=t doublon fixed point"
  used the *strong-coupling* formula `t_eff=2t²/U` out of regime (at U=t it gives `t_eff=2t`; a genuine 2-body Hubbard
  ED shows no doublon band and RMS 3.77 vs the prediction), and its "RMS=0 verification" was *circular*
  (effective-Fibonacci-chain-with-`λ_eff` vs the single particle, equal by construction at U=t). Recorded refuted.
  **R3 standard ETH** (not banked; its specific Poisson→GOE numbers didn't even reproduce in a quick check). The
  **"not nothing" ladder** stays firewalled/POSTULATED (known results + selection-bias deflation; nothing to
  `CLAIMS.md`). Only R2 survives as a new increment. Standalone condensed-matter / symbolic-dynamics math; P1–P16
  untouched.
- **B199 — the metallic exponent: no closed-form law; the clean exponent is a *sublocus*; SL(5) exact-symbolic
  exhausted (2026-06-24; V192).** A multi-agent **Workflow** (113 agents, ~4.5M tokens, 4h: adversarial verify → law
  propose+judge panel → 4 Goal-B exact routes → deep-research novelty → consolidate) closing the flagship by
  computation. **Three results.** *(A) No closed-form law.* No single-valued `k(o,m)` (or `…,gcd`, or `k(A^m-spectrum)`)
  survives — three decisive, independently-reproduced refuters: the **o=4/o=8 collision** (both → k=3 at m=1; shared
  `eff_o=4` = eigenvalue-ratio-group order — kills `k=7−o`, every `f(o)`, gcd-rules, and the `eff_o` candidate too), the
  **A^m-spectrum collision** (`A²[o4]=A³[o6]=diag(1,−1,−1)` exactly, yet k=2 vs 1), and **non-monotonicity** (o=4 column
  3,2,3; brute force → zero affine fits). The only surviving closed form is the **sign `s=(−1)ⁿ⁻¹`** (splits at o=8).
  The exponent is the structural metallic-A-polynomial slope; order-not-rank survives; degree=rank refuted at SL5
  (k=2≠5). *(B) Verify-don't-trust correction of B198.* The rigid `[A,B]=µ²` holds only on a **~1% rigid sublocus** of
  the dim-4 loxodromic component (grid 8/887; workflow 24/3486) — B198's "305/305 on the geometric component" was an
  `err`-filter selection artifact; the **k=2 value stands** (at the complete cusped rep), only the *scope* is
  down-tiered (B198 corrected in place). At SL3 it holds on the whole component; the sublocus emerges with rank.
  *(C) SL(5) exact-symbolic exhausted.* All four maximal routes → `NEEDS-SPECIALIST` at a sharp wall — the *first*
  degrevlex Gröbner basis at 25 vars does not terminate in 600s over ℚ(ζ₅) *or* F_p; the engines are validated
  exact-mod-p on SL(3); R4 found the k=2 locus is **not rationally parametrizable**. Novelty (19 sources): R1
  PARTIALLY-KNOWN (higher-n + metallic APPEARS-NOVEL), R3 APPEARS-NOVEL. Standalone character-variety math; firewall
  intact; P1–P16 untouched; nothing to `CLAIMS.md`.
- **B198 — the B157 metallic-exponent wall, breached by computation (2026-06-23; V190).** A direct test of the
  "we compute before deferring to a specialist" directive and the new `GOVERNANCE.md` §6.1 **(C)** guardrail.
  B157 had marked the SL(5)/o≥5 exponent cells `NEEDS-SPECIALIST` ("needs a real CAS"); **two of the three
  premises were tooling/diagnosis, not math.** (1) **Sage is installed in-environment** (`command -v sage`) and
  reproduces the SL(3) cells **exactly** via the geometric component (o=3→k=4, o=4→k=3 — the Gröbner sympy could
  not finish). (2) The "SL(5) Newton wall" was **gauge-induced Jacobian rank-deficiency**; **gauge-fixing** the
  diagonal torus makes Newton converge, reaching the previously-unreachable **SL(5) o=5, m=1 → `[A,B]=+µ²`, k=2**,
  certified three independent ways (two Newton solvers + an mpmath dps=60 certificate where `‖[A,B]−µ²‖` falls in
  *lockstep* with the relation residual to 1.5e-23, proving exactness; `c=+1`; neighbours excluded). This
  **extends the figure-eight (m=1) row to o=5** (note `k=2≠rank 5`, so it *reinforces* B157's "order-determined,
  not degree=rank"); the certified rep is confirmed on the **geometric / cusped component** (meridian `µ`
  loxodromic, infinite order). The wall **moved** — the residual is the *exact-symbolic* `k` at SL(5) (primary
  decomposition at 25 vars; Sage stalls already at SL(4)/16 vars). A first high-precision certificate **failed**
  (a seed-selection bug in the certificate script), was caught and fixed — verify-don't-trust. **Grid follow-up +
  self-correction (same day, V191):** B198's *first-draft* secondary claims — `k=4−m(o−3)` governing m∈{1,2} in
  value+existence-boundary, and a `gcd(m,o)` anomaly lead — were **REFUTED** by extending the grid to o=8 and
  filtering by meridian order: the exponent must be read on the `order(µ)=∞` (cusped) stratum (finite-order-`µ`
  Dehn-filling reps give spurious exponents), and even there **o=4 and o=8 both give k=3** at m=1 → **no simple
  `k(o,m)` law**. The headline (wall breach + SL(5) k=2) stands and is strengthened; the closed form stays
  `NEEDS-SPECIALIST` with the correct object now identified (the geometric-stratum exponent). B157 FINDINGS
  corrected in place. Standalone character-variety math; firewall intact; P1–P16 untouched; nothing to `CLAIMS.md`.
- **B197 — the figure-eight volume-tie broken by torsion-freeness (a verified chat2 increment) (2026-06-23; V189).**
  A cross-session (chat2) foundation-stress probe of the figure-eight Step-1 selection (C1), **independently
  re-derived** before banking. The bulk re-derives banked work (K016 criteria, P10 filters) — cited, not re-banked.
  **The one genuine increment:** P10's *unresolved* m003 volume-tie is **broken by torsion-freeness** — m003 carries
  ℤ/5 torsion (not a b++ bundle), so among torsion-free bundles the figure-eight is the **unique** volume minimum
  (verified over all 241 b++ bundles to length 10). Sharpens P10's volume filter. Framed per **V145** (trace-3 the
  *only* proof; volume "unique *given* torsion-free" — leans on the torsion-free locus, **not** an independent axis;
  the "prefer-simplicity" premise is permanent), so it **hardens C1 modestly**, not "independent overdetermination"
  (the chat2 headline overstated; the corrected reading is banked). Also: the chiral pair `b++RRL`/`b++RLL` —
  equal volume, opposite CS=±1/48. A one-line **P10 sharpening is proposed for owner approval** (not committed).
  Form-side, K010; nothing to `CLAIMS.md`. `tests/test_b197_*` (2).
- **B193 — the SL(3) sealing / field-content scouts (Masterplan III, Track G) (2026-06-23; V188).** Closes Track G.
  **L8:** chirality (cyclic-palindrome block sequence, B128/B134) and the **SU(2)_k eigenvalue field** (B132) are
  **independent** — all four (chirality, field) combinations occur, so the field is the quantum mod-4 spin-content,
  not chirality (extends B133 across composition). **L10:** the field-fusion to `Q(ζ₁₂)=Q(√−3,i)` is a **quantum**
  (SU(2)_k) phenomenon (a silver block already reaches it), while the **classical** metallic seed trace-fields stay
  **disjoint** (`Q(√−3)∩Q(i)=Q`, exact). **L5/L6:** the non-metallic SL(3) sealing search is **scoped
  NEEDS-SPECIALIST** (the B137 method + SnapPy-gated trace fields = intricate numerics; the B192 lesson cautions
  against rushing it). Reinforces K015/K016 (field = quantum-group arithmetic, not chirality). Emergent
  quantum-topology / character-variety math (K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b193_*` (2).
- **B191 — the formal 2-cusp connector (Masterplan III, Track F; H5-a) (2026-06-23; V187).** B185 capped the
  1-cusp metallic units at *pairs*, so `N≥3` needs a `≥2`-cusp **connector**. Computed at the trace-ring level: the
  κ-selection **nests** — a *coupling* connector (modeled by its internal mapping class `φ_c`,
  `boundary₂=φ_c(boundary₁)`) propagates leaf₁'s A-poly constraint into a **discrete** fork on leaf₂ (`T→9, S→16,
  ST→32`), while the **identity/uncoupled** connector gives a **continuum** (the control). Discrete-and-
  **proliferating** (grows with `φ_c`, never forced-unique), so the selection mechanism extends past B185's pair-cap
  to `N≥3` in principle; the B185 dim count agrees (`(1+2+1)−2·2 = 0`, discrete iff coupled). The **true geometric
  metallic 2-cusp 3-manifold connector** (existence, which `φ_c`) is the NEEDS-SPECIALIST residual. Closes Track F.
  Emergent character-variety math (K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b191_*` (2).
- **B196 + S037 — the entropy↔conformal-dimension bridge, and the firewalled cosmogony (2026-06-23; V186).**
  *Solid math (B196):* under Painlevé VI ↔ c=1 (Gamayun–Iorgov–Lisovyy), the metallic once-punctured-torus object
  is a **c=1 four-twist-field** (Δ=1/16) conformal block whose single nontrivial datum is the dimension of its
  (hyperbolic) bundle/time-monodromy, **`Δ = −(ln λ_m/π)² = −(topological entropy/2π)²`** — the object's *dynamics*
  dressed as a CFT dimension, dimensionless and non-unitary. Rests on the exact identity `λ_m²+1/λ_m² = m²+2`.
  Forces **no** physical content (c=1 trivially fixed; Δ dimensionless; no scale/mass); the precise PVI channel
  placement is the one NEEDS-SPECIALIST detail (the value is exact). *Firewalled speculation (`speculations/S037`):*
  the four-part dualism — object = form (a conformal block whose content is its own entropy); Higgs field = scale;
  bath = arrow; import = identity — three legs external (the wall). Negatives kept prominent (B169 time=modulus,
  B151/B167 scale=import, B189 the artifact warning): this **confirms relocation, does not breach**. Emergent
  quantum-topology math (K010); nothing to `CLAIMS.md`; P1–P16 frozen. `tests/test_b196_*` (3).
- **B192 — SL(n≥3) higher-rank Lyapunov spectra (Masterplan III, Track D; L20 deepened) (2026-06-22; V185).**
  Computed the *full* Lyapunov spectrum (QR-flag) of the metallic SL(n) transfer cocycle, turning V29 into a
  **measured property**. **A clean parity law:** the spectrum is **symmetric (symplectic) iff `n` is even** (defect
  n=2: 0.000, n=4: 0.003) and **asymmetric (non-Hermitian) iff `n` is odd** (n=3: 0.22, n=5: 0.11) — exactly
  tracking "a symplectic form exists iff `n` even" (V29). The even-`n` symmetry is **special to the metallic
  cocycle** (a generic SL(n) is asymmetric for all `n`: n=4 defect ≈0.52, `163×`) — so the metallic even-`n`
  cocycle is conjugate to a symplectic one (it *uses* the form), while odd-`n` is genuinely non-Hermitian. Spectrum
  sums to 0 (SL(n)); the bounded set + one golden tower scale persist. Rigorous higher-rank spectral theory stays
  NEEDS-SPECIALIST. Emergent non-Hermitian math (K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b192_*` (2).
- **B189 — the Ω accretion causal-set dimension (Masterplan III, Track E; L21, FIREWALLED) (2026-06-22; V184).**
  Computed the Myrheim–Meyer ordering-fraction dimension of the Ω class DAG (B156/B159) — *and hunted the artifact*.
  The estimator (calibrated on Minkowski sprinklings, matches Meyer's `f(d)` to a few %) gives `d_MM ≈ 3.94` for the
  full poset — but it is a **generic graded-DAG / truncation artifact, not a spacetime dimension**: it **drifts**
  upward with truncation (`2.08→2.70→3.28→3.63→3.94` for `L≤6…10`, no convergence) **and** is **matched by a random
  graded-DAG null control** (`3.79±0.01`, same level sizes + edge counts). So the program's most over-readable
  number (a "4") is vacuous as physics — the firewall holds **by computation**, preempting any "Ω predicts 4D"
  over-read. L21 computed and closed firewalled; combinatorial-only, nothing to `CLAIMS.md`. `tests/test_b189_*` (2).
- **B190 — abstract iterated gluing (Masterplan III, Track F) (2026-06-22; V183).** Pushes B174's trace-ring gluing
  past B185's pair-cap, **in both directions**, to test whether iterating forces a *unique* selection. **It does
  not.** **Open** gluing proliferates — the fork-polynomial **degree** (a Bézout/resultant *upper bound*, not the
  geometric count) grows `T^k → 8+k` (linear in twists), swaps `~double` (S=16, ST=32); never collapses to 1, never
  empties. **Closed/loop** (over-determination = fixed points) collapses the continuum to a **finite discrete** set
  whose **total** count grows (ST→1, TST→2, STST→3, STSTST→4); the lone count-1 case (ST) is the **trivial** point
  `(2,2,2)` (MB12-vacuous), and the genuine non-trivial fixed points are **golden-field** `((√5−1)/2, …)` and
  **non-monotone** (seq `0,0,2,0` — appear at STST, vanish at STSTST). So selection-to-discrete **yes**,
  selection-to-forced-unique **no** — confirms B185 in the trace ring (both directions). The literal closed-loop
  3-manifold realization is multi-cusp = NEEDS-SPECIALIST. *(Two precision fixes applied post-merge after in-batch
  adversarial verification — see FINDINGS; core unchanged.)* Emergent character-variety math (K010); firewalled,
  nothing to `CLAIMS.md`. `tests/test_b190_*` (2).
- **B188 — the driven-dissipative metallic chain (Masterplan III, Track B) (2026-06-22; V182).** The genuinely
  **dissipative** (Lindblad) channel — **computed** the Liouvillian gap (slowest relaxation rate) of a dephasing
  metallic chain vs controls. **An inversion of the naive "criticality ⟹ gapless" guess:** the **localized**
  (Aubry–André) control is the near-gapless one (gap `~100×` smaller — localization ⟹ slow relaxation), while the
  permanently-critical metallic chain relaxes like an **extended** chain (gap `~` periodic). The gap decays to zero
  in the thermodynamic limit (diffusive — no finite emergent timescale) and is **homogeneous in the external rates**
  (`Δ(sH,sγ)=sΔ` exactly → no intrinsic scale). Completes the open-system trilogy B183/B187/B188 — a real but
  externally-sourced, dimensionless arrow; no emergent scale. Interacting Lindblad = NEEDS-SPECIALIST. Emergent
  open-quantum-systems math (K010 boundary); firewalled, nothing to `CLAIMS.md`. `tests/test_b188_*` (2).
- **B187 — the open / interacting many-body collective (Masterplan III, Track B) (2026-06-22; V181).** Extends B183
  (single-particle) to the **interacting** case S036 left open — **computed** by exact diagonalization of a few
  fermions. B183's *thresholdless arrow* **persists with interactions**: the permanently-critical metallic chain's
  many-body real→complex (point-gap) threshold `g_c(U) ≈ 0` for all `U=0…4` (a two-body interaction opens **no**
  protective gap — slightly *more* fragile), while the Aubry–André localized control stays **protected** (finite
  `g_c ≈ 0.7–1.4`) at every `U`. Robust across `L=10–16`, 2–3 particles. The arrow is genuine but `g_c` is
  **dimensionless** and the arrow's **source is the externally-imposed openness** (not self-generated) → no scale,
  extends B183's firewall verdict to the many-body case. Thermodynamic-N driven/MBL regime = NEEDS-SPECIALIST.
  Emergent condensed-matter many-body math (K010 boundary); firewalled, nothing to `CLAIMS.md`. `tests/test_b187_*` (2).
- **B186 — off-axis hyperbolicity certification (Masterplan III, Track C) (2026-06-22; V180).** The first frontier of
  the computable-frontier program (compute every open branch to its boundary; defer nothing prematurely). Grounds
  B165's *conditional* theorem for the off-axis κ<2 Cantor spectrum (L19): the hyperbolicity hypothesis is
  strengthened from **one** diagnostic (B163's MST) to **three independent** ones, the key one **validated on the
  Damanik–Gorodetski-proven κ>2 case**. The trace-map **escape rate** `γ` (a Bowen–Ruelle hyperbolicity signature:
  exponential escape ⟺ hyperbolic repeller) is `>0` off-axis (κ<2) exactly as on the proven κ>2 case and `≈0` on the
  κ=2 band (calibrator) — fixing B165's escape-contaminated naive ratio; robust to trapping radius and sampling.
  Plus **box-counting dimension** (off-axis `<` band, golden+silver), independent of the MST. Two *local* diagnostics
  recorded NEGATIVE (per-point `|λ_max(DT)|`, bounded-orbit Lyapunov — verify-don't-trust). Only the rigorous off-axis
  uniform-hyperbolicity *proof* (a non-Hermitian Damanik–Gorodetski) stays NEEDS-SPECIALIST. Emergent
  spectral/dynamical math (K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b186_*` (2).
- **B185 — the selection / constraint door (S036 hunt 5) (2026-06-22; V179).** The route to selection-to-*unique*
  that B182 left as "a constraint (gluing) phenomenon, multi-cusp NEEDS-SPECIALIST" — **computed** up to the genuine
  boundary. The constraint (gluing) side **genuinely selects**: cusp-gluing collapses each piece's character-variety
  *curve* (a continuum) to a **discrete** κ-fork (B174/B131) — the real ">1 building block" selection, unlike
  superposition which proliferates (B182). **But not to a forced-unique value:** the fork has size `>1`, **multiplies**
  under iteration (grows, B174), and is a topological invariant of the *freely-chosen* gluing data (unique-per-choice,
  choices proliferate). And the metallic units are **1-cusped** (SnapPy) → leaves in any gluing graph → `2(k−1)≤k` →
  all-unit interaction **caps at pairs** (a closed κ-fork); `N≥3` needs `≥2`-cusp **connectors** that are *not*
  once-punctured-torus bundles = the genuine **NEEDS-SPECIALIST** boundary. The dimension count `dim = Σcusps −
  2·gluings ≥ 0` (closed → `0`, discrete) shows no forced point. So **selection-to-discrete: yes; selection-to-unique:
  no** — neither channel forces uniqueness; this sharpens B182 into a computed boundary. Emergent character-variety /
  3-manifold gluing math (K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b185_*` (3).
- **B184 — the symmetry / gauge door (S036 hunt 4) (2026-06-22; V178).** Does the interaction of multiple units
  **force** a symmetry (a gauge group)? **No — computed, not asserted.** Each unit has a *forced* symmetry: the
  modular **SL(2,ℤ)** duality (B150 — real, but a *duality* not the SM gauge group) and a self-similarity
  **inflation** `×λ_m` = the companion `[[m,1],[1,0]] ∈ GL(2,ℤ)`. But the interaction of *distinct-field* units
  **breaks** the global inflation (the cross-product `α₁α₂` escapes the rank-3 module; the dilation factors
  `λ₁,λ₂` are multiplicatively independent) and only **multiplies** the per-unit dualities — a product that
  **proliferates** with N (mirrors B182), not a selected Lie/gauge group. Same-field units keep a *shared*
  inflation (`α₁α₄=2−3α₁`, field-not-count). So the **gauge** content stays **free input** (the S036 null), now
  computed. **Unifying fact across B182/B184:** the *same* distinct-field / cross-product-escape arithmetic that
  grows the gap-label rank (B182) is what breaks the inflation symmetry (B184) — proliferation and symmetry-breaking
  are two faces of one fact. Emergent quasicrystal/character-variety symmetry math (K010); firewalled, nothing to
  `CLAIMS.md`. `tests/test_b184_*` (4).
- **B183 — the open / driven collective arrow door (S036 hunt 3) (2026-06-22; V177).** The last untested arrow/scale
  door B181 left open ("an *open/driven* large-N collective"), **computed, not deferred.** Two naive PT probes are
  artifacts (a halves-split gives `max|Im|=γ` trivially; a staggered ±iγ gives `γ_c→0` for any `V≠0` — a
  **chiral-symmetry** artifact, not localization). The discriminating, theorem-backed probe is the **Hatano–Nelson**
  imaginary gauge field under PBC: the real spectrum goes complex (a non-unitary, **irreversible** point gap = an
  arrow) at `g_c = min` Lyapunov over the spectrum = the inverse localization length. **Result — the same inversion
  as B181:** the metallic collective is **thresholdless** (`g_c≈0`, since permanently critical, B181) — it gains an
  irreversible spectrum under the *slightest* drive; criticality = **maximal fragility** to the arrow, not robustness.
  A localized control (AA `V=8cos`, off-metallic) is **protected** up to the *exact* finite `g_c=ln4=1.386`. **The
  firewall holds:** the arrow is genuine (unlike combinatorial Ω, B168 / reversible trace map, B177) but `g_c` is
  **dimensionless** (no scale) and the arrow's **source is external** (the openness is input — not self-generated).
  So the **ARROW** ingredient upgrades to "emergent in the open collective, thresholdless, dimensionless, externally
  sourced"; **SCALE** stays external. Permanent criticality is **double-edged** — it *is* the scale-freeness (`ξ→∞`)
  **and** the zero-threshold arrow-fragility (`g_c=0`). Validated against exact `ln4`; controls pass. Emergent
  non-Hermitian/localization math (K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b183_*` (3).
- **B182 — the selection / multiplicity door (S036 hunt 2) (2026-06-19; V176).** The direct answer to "2 / more /
  set / infinity of units?" for the **superposition (weaving)** channel: it **proliferates**, it does **not**
  select-to-unique. PSLQ shows weaving `N` distinct-field metallic units gives a gap-label module of **rank `1+N`**
  (→ ∞ as N→∞); it's the number of **distinct fields** that grows it, not the unit count (same-field `m=1,4` are
  dependent, `−1+2α₁−α₄=0`). **The fence:** selection-to-*unique* is a **constraint** (gluing/over-determination)
  phenomenon — finite κ-fork pairwise (K014/B174), over-determined when iterated — multi-cusp **NEEDS-SPECIALIST**;
  superposition only enriches. And the proliferating structure stays dimensionless + scale-free (B181). So "infinity
  of units" → infinitely rich, still scale-free; SELECTION-uniqueness stays open on the constraint side. Pure
  arithmetic (K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b182_*` (2).
- **S036 + B181 — the search specification, and its first hunt (the criticality scale-door) (2026-06-19; V175).**
  **`speculations/S036`** (firewalled, POSTULATED) is the **search specification** prompted by the reframe *"the ToE
  emerges from the interaction of multiple units, not the single one — clarify what we're searching for so we
  recognize a result and don't bypass it."* It registers each physics ingredient with **what would count** as it
  emerging from interaction and **the null to reject** (the MB12 vacuity-check at program scale): the *form*
  ingredients are present/emergent; the *content* ingredients (scale, arrow, selection-uniqueness, gauge, masses) are
  external/dead at single+pair, with **multiplicity (N→∞)** the untested lever. **`B181`** runs the first hunt — the
  **large-N / criticality** scale-door — and finds an **inversion:** the metallic quasicrystal is **permanently
  critical** (Lyapunov γ≈0 on the spectrum at *all* coupling — no metal–insulator transition, vs the Aubry–André
  control which localizes at λ>2 with γ=ln(λ/2)). Permanent criticality ⟹ `ξ→∞` ⟹ scale-invariant ⟹ **scale-free
  *by* criticality** — so criticality *explains* the scale-freeness rather than providing a scale; a finite emergent
  length needs *breaking* criticality (off the metallic class) and is *dimensionless* (lattice units → external). The
  scale-search points to the Hitchin/Higgs side; open = an *open/driven* large-N collective. Emergent criticality math
  (K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b181_*` (2).
- **B180 — the two-faces dictionary: one hinge quantity + two analogous operations (2026-06-19; V174;
  understand-completely #5).** Resolves "is *two faces of one principle* (K019) an identity or an analogy?" →
  **a sharpening.** **C1:** `κ = tr[A,B]` is the *same conserved number* on both faces — the character-variety
  boundary coordinate *and* the trace-map invariant (the Dehn-twist trace maps conserve κ, symbolic). **C2 [live]:**
  κ's value sets the spectral type — coupling 0 (periodic) → full band (0 gaps), κ>2 → Cantor (13 gaps); so the
  character-variety κ **governs** the spectral face (the real bridge, K010). **C3 [fence, MB12]:** the two
  *interaction operations* — cusp-gluing (bundle κ-fork) vs potential-weaving (gap labels) — are **distinct math
  with distinct outputs** (trace values vs IDS fractions), sharing only the signature single=continuum/distinct=structure.
  The naive "κ-fork = gap labels" is **false**. K019 sharpened (no retraction). Emergent topology/spectral math (K010);
  firewalled, nothing to `CLAIMS.md`. `tests/test_b180_*` (2).
- **B179 — the metallic "numbers" unified: one object, several views (2026-06-19; V173; understand-completely #3).**
  Pure symbolic algebra. The whole geometric/arithmetic tower of a metallic seed `m` is **one algebraic object** —
  `λ_m = (m+√(m²+4))/2`, the root of `x²−mx−1` — and every number we carry is an exact function of it: the gap-label
  frequency `1/λ_m`, the bundle trace `m²+2 = λ_m²+λ_m⁻²`, the dynamical degree `λ_m²`, the field `ℚ(√(m²+4))`, the
  Hurwitz constant `1/√(m²+4) = 1/(λ_m+1/λ_m)`, the tower eigenvalues `±λ_m^k`. Bridge identities: `λ_m ± 1/λ_m =
  √(m²+4)` resp. `m`. **Honest boundary (MB12):** three same-named parameters are **distinct** and must not be
  conflated with `λ_m` — the Schrödinger coupling `λ` (free knob), the Fricke modular `λ̃` in `κ=λ̃+1/λ̃` (a free
  character-variety coordinate), and the gap-labeling IDS (a derived combination). Golden `m=1` collapses the tower to
  `φ`. No new claim; pure algebra of what we have. `tests/test_b179_*` (4).
- **B178 — the perturbative mechanism: the width law + golden privilege are ONE textbook thing (2026-06-18; V172;
  understand-completely consolidation).** Identifies the single perturbative mechanism behind both flagships: the
  combination gap `(n₁,n₂)` is the order-`|n₁|+|n₂|` term, ∝ `λ₁^{|n₁|}λ₂^{|n₂|}`, Diophantine-robust — *order* gives
  the width law (B175), the *Diophantine factor* gives the golden privilege (B176). Introduces the **contamination-
  robust index method** (gap pinned to its gap-labeling eigenvalue index) and confirms the **per-frequency structure**
  (power-1 clean; (2,1)/(1,2) carry a distinct higher power ~1.7). **Honest limit:** the exact integer (=2) is
  textbook but numerically **plateaus at ~1.7** (saturation + finite-N), not cleanly resolved in-sandbox →
  NEEDS-SPECIALIST. Golden privilege = a Diophantine-amplification heuristic. **A multi-step verify-don't-trust
  record:** a window-max "derivation" was wrong → over-hastily called a "failure" → an owner challenge surfaced that
  the window-max *can* contaminate → the index method confirmed the structure and showed the power-2 shortfall is
  *genuine saturation, not contamination* → an intermediate "B175 is contaminated" alarm was itself **walked back**
  (B175 stands). Both over-claim directions corrected. Emergent quasicrystal math (K010); firewalled, nothing to
  `CLAIMS.md`; B175/B176 unchanged. `tests/test_b178_*` (3).
- **B177 — the metabolism test, "is it alive?" H3 to the knife (2026-06-18; V171; S035 register, firewalled).**
  The decisive test of a cross-session ("chat2") life-hunt: does κ>2 order **starve** when you stop feeding the
  chain (a self-maintaining *cell*), or is it conserved/frozen (a *crystal*)? **Verdict: a conservative
  active-chaotic CRYSTAL/HORSESHOE, not a cell.** **C1** κ (the Fricke–Vogt first integral) is **conserved** across
  generations (drift <1e-8) — cannot starve (H3 original form dead by the conservation law). **C2** the real
  Sturmian gap **converges/freezes** (1.0653, |Δw|→1e-4) — held by static *structure*, not *flux*; doesn't close
  (H3 revised form dead — a conservative spectral problem has no metabolism). **C3** the trace map is **invertible**
  (no arrow). **C4** there *is* an active set (the κ>2 horseshoe, cited B163/B165) but it's reversible chaos — *order
  that wanders, not order that maintains itself*. So metabolism/homeostasis/arrow **relocate external** (K018 in the
  life register); "heredity already owned" is an over-read (κ-conservation is a symmetry, not heredity). *Verify-
  don't-trust:* my own C4 divergence demo was escape-contaminated (B165's recorded lesson) → replaced by the cited
  clean result. Firewalled; nothing to `CLAIMS.md`. `tests/test_b177_*` (4).
- **K019 — the collective (multibody) metallic spectrum (2026-06-18; multibody-extraction plan P4).** The
  textbook-layer **synthesis** of the multi-seed arc (B171–B176), companion to K007/K010 (the single chain). The
  one-line result: *a lone unit only parametrizes; structure no single unit has appears only with interaction of
  distinct units, and it is predictable.* Consolidates the **two faces** (spectral combination gap ↔ character-variety
  κ-fork), the **two-number predictability** (heights exact by gap-labeling; widths by the weak-coupling order-power
  law), the **golden privilege** (φ stands alone), the **model caveat** (heights universal, openings potential-dependent),
  and the honest physics-contact statement (both genuine contacts are *collective*; predictivity over structure, not
  constants). INDEX + ARCHITECTURE bumped to K019. No new claims (explainer); nothing to `CLAIMS.md`.
- **B176 — the golden privilege, with controls (2026-06-18; V170; multibody-extraction plan P3).** Controlled test
  of a cross-session ("chat2") claim that the woven chain "dresses the most irrational resonance." **Confirms-yet-
  corrects:** **φ/golden is genuinely privileged** — its combination satellite ladder dominates *both* silver's (8.9×
  cosine, 3.3× Sturmian) and bronze's (3.4×), θ-averaged, in **both** models, and **not** because golden has a wider
  bare gap (ladder ratio 8.9× ≫ principal-width ratio 1.6×). **But it is golden-stands-alone, NOT a monotone order**
  — silver and bronze are comparable (s/b 1.5/0.77), so it does *not* continue golden>silver>bronze. The
  golden=most-irrational=most-robust math is real (Hurwitz/KAM); the P000-anchor tie is a one-way **`[RHYME]`** with a
  real kernel, not a derivation; the effect is cosine-dominant; a rigorous theorem is NEEDS-SPECIALIST. Emergent
  quasicrystal physics (K007/K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b176_*` (3).
- **B175 — the collective spectrum is two-number predictable (2026-06-18; V169; multibody-extraction plan P1+P2).**
  The disciplined version of a cross-session ("chat2") "combination ridge." The woven metallic spectrum is
  predictable from two pairs of numbers: **`(α₁,α₂)` fix every gap *height* exactly** at all couplings (gap-labeling,
  seed-robust across golden+silver & golden+bronze, label-error ~8e-5), and **`(λ₁,λ₂)` fix every gap *width*** via
  the order-power law `width ~ λ^(|n₁|+|n₂|)` **at weak coupling** (order-2 slope **1.92/2.01**, order-3 →3). So four
  numbers forecast the whole weak-coupling spectrum — a **collective** phenomenon (the single unit has no combination
  gaps). **Bound (once):** the width law is **perturbative** — it saturates at strong coupling; predictivity over
  **structure**, not a fundamental constant. **Model distinction (reconciles B172/B173, corrects the over-reach):**
  the ridge **opens in the cosine (bichromatic) model** (0.211) but is **~closed in the metallic Sturmian chain**
  (0.016) — heights are potential-independent (the theorem), *which* gaps open is potential-dependent. **3
  verify-don't-trust self-corrections** (ridge-is-metallic→cosine-specific; clean-law→weak-coupling-law; the null
  threshold). Emergent quasicrystal physics (K007/K010, *measured* materials); firewalled, nothing to `CLAIMS.md`.
  `tests/test_b175_*` (3).
- **B174 — the GL(2,ℤ) gluing-map landscape (2026-06-18; V168; H5).** The cusp-gluing lane — the
  **character-variety companion** to the spectral multi-seed arc (B171–B173). Extends B131 (identity gluing) and
  B134 (one swap) to the gluing-map landscape via the abelian peripheral trace ring `(p,q,r)` and the mapping-class
  action. **Validation:** identity glue `(1,1)`→CONTINUUM, `(1,2)`→`{−4,−2}` (B131); swap fig-8 self-glue →
  `p=f(f(p))` degree 16 (B134). **Landscape:** CONTINUUM only on the measure-zero curve-aligned locus
  (identity/same-seed); **discrete for every nontrivial φ**, the fork size φ-dependent — **multiplies under swaps**
  (S→16, ST→32) and grows slowly under twists (T→9, T²→10); finiteness = Kitano–Nozaki Bézout. **Cross-face
  agreement:** same principle as B171–B173 — interaction of *distinct* units forces structure no single unit has
  (spectral combination gap ↔ character-variety κ-fork). **H5 → CHARACTERIZED.** Scope: pairwise only (once-cusp);
  large-N/multi-cusp + the all-φ theorem NEEDS-SPECIALIST. Emergent topology (K010); firewalled, nothing to
  `CLAIMS.md`. `tests/test_b174_*` (3).
- **B173 — the gap-labeling reduction, Phase 2 (2026-06-18; V167; multi-seed plan, L16).** Reduces B172's
  combination gap to the **gap-labeling theorem** (a citable consequence, not a new claim) and **confirms the L16
  rank formula**. For the 1D superposition operator the gap-label group is the **frequency module ℤ+ℤα_g+ℤα_s —
  rank 3, product-free** (Johnson–Moser 1982; Bellissard; Damanik–Fillman 2022, arXiv:2203.03696). **R1/R2 (PSLQ):**
  golden+silver have no integer relation → rank 3, and the *full* L16 formula `rank = 1 + #distinct quadratic fields`
  is confirmed (distinct fields → 3; same-field golden m=1 & m=4 → dependent `−1+2α₁−α₄=0` → caps at 2). **R3:** the
  product α_g·α_s is a genuine 4th direction that the 1D theorem **excludes** (products are a ℤ^d≥2 / 2D-tiling
  feature — Elliott 1984, Forrest–Hunton–Kellendonk) ⟹ L16's **√(dᵢdⱼ) worry is dispelled**. **Novelty (tiered):**
  the mechanism is **KNOWN** (not claimed); the explicit golden+silver construction **APPEARS-NOVEL** as a worked
  example (≠ Damanik–Gorodetski "Square Fibonacci," arXiv:1601.01639) → NEEDS-SPECIALIST. Residual: discontinuous-`f`
  exact group + realized-gaps. Emergent quasicrystal math (K007/K010); firewalled, nothing to `CLAIMS.md`.
  `tests/test_b173_*` (4).
- **B172 — the combination gap resolved, Phase 1 (2026-06-18; V166; multi-seed plan, L16).** Answers B171's question
  — *does heterogeneous interaction generate a rank-3 combination gap?* — **affirmatively (hedged)**. **C1:** the
  woven metallic quasicrystal has a **real, persistent** spectral gap (in-gap to N=128 000, width 0.114) whose IDS
  (≈0.6114, via the exact Sturm/pivot count) is **not any single-frequency ladder value** — ≥8× closer to the
  combination label (3,−3) than to the nearest single-freq value of any order ⟹ it needs **both** frequencies ⟹
  **interaction-born** (a rank-3 feature no single seed has). **Honest limit:** the IDS plateaus at the finite-size
  floor (~2e-4); the *specific* label is consistent with (3,−3) but a sharp many-digit certification is
  **NEEDS-SPECIALIST**. **C2:** bilingual inheritance is **seed-robust** (3 metallic pairs); small-label combination
  gaps essentially **absent** (one non-robust golden+bronze (1,−2) hit) — the combination structure lives at larger
  labels. *Verify-don't-trust (3rd self-correction):* the probe's first-draft "clean convergence to (3,−3)" was
  **refuted by its own run** and rewritten to "combination gap, label ~(3,−3)." Emergent quasicrystal math
  (K007/K010); firewalled, nothing to `CLAIMS.md`. `tests/test_b172_*` (3).
- **B171 — the heterogeneous metallic quasicrystal, Phase 0 (2026-06-18; V165; multi-seed plan, L16).** Opens the
  multi-seed-interaction frontier in the **substitution / gap-labeling** lane (the spectral face of the κ↔spectrum
  bridge, K010). Builds the woven two-frequency metallic Schrödinger operator + its IDS gap labels. **B2:** the woven
  spectrum is **bilingual** — both pure rank-2 ladders (golden & silver `±1`) survive [credible]. **B3 [density
  trap]:** the rank-3 label set is **dense** (chance-hit 1.0%→2.9%→5.8%→9.6%→20.3% for sum ≤1,2,3,4,6) ⟹ only
  **small labels (sum ≤ 3)** are credible. **B4 [verification]:** the cross-session "first combination gap" IDS 0.611
  is a **real, wide** gap (w 0.11) but its only match is the **large** label (3,−3) (sum 6, ~20% null) ⟹
  **plausible-yet-UNVERIFIED**, not established. *Verify-don't-trust applied twice* — to the cross-session over-read
  **and** to this probe's own first-draft "density artifact" over-claim (the gap is real; corrected to "real gap,
  unverified label"). The rank-3 combination-gap question is **OPEN** (Phase 1: IDS-convergence + small-label hunt,
  seed-robust). Emergent quasicrystal math (K007/K010 boundary); firewalled, nothing to `CLAIMS.md`. `tests/test_b171_*` (3).
- **B170 — the relational/Machian scale leap, ASSESSED (2026-06-18; V164; closes S035's last `[LEAP]`).** Assesses
  whether "external" dissolves into "self-referential" — the Machian reading that a purely relational universe has
  only ratios, so the firewall would **dissolve** not relocate. **L1 [structural]:** **undecidable from within** —
  the Machian and external readings give the **same** dimensionless math; no internal computation distinguishes
  them (interpretive, not a calculation). **L2 [num, null-test]:** the only predictive form is **value-matching**,
  which is **dead** — the program's φ²/metallic/`log 2` numbers match observed constants (`α⁻¹`, `m_p/m_e`, …) no
  better than a **random** base (median exponent-distance-to-integer 0.258 vs 0.251 — indistinguishable; the S014
  lane, now with a control). **Verdict:** the leap **reinterprets** the wall (its honest philosophical face) but
  does **not dissolve** it; **POSTULATED**, value-matching **forbidden**. Closes S035's last leap: the wall
  relocates in every reachable mode (B167/B168/B169 → K018). Firewalled; nothing to `CLAIMS.md`. `tests/test_b170_*` (2).
- **B166 — SL(n) higher-rank aperiodic operators (2026-06-18; V163; P2b, L20).** Pushes the tower past SL(2).
  **Q0 [exact]:** the symplectic obstruction (V29) — odd n has no nondegenerate antisymmetric form, so SL(n≥3) is
  **not** a self-adjoint operator's transfer group (Sp=SL only at n=2) ⟹ **intrinsically non-Hermitian**; the
  SL(2)↔Fibonacci quantum spectrum is the n=2 coincidence. **Q1 [recorded negative]:** a naive SL(3) metallic
  cocycle shows **no clean Cantor thinning** (fib fraction ≈ periodic) — SL(2)'s Cantor structure does **not**
  trivially transfer; genuinely open. **Q2 [cited]:** one golden tower scale `±φᵏ` (B107/B60). **Verdict:**
  non-Hermitian + one scale + structure-open → **NEEDS-SPECIALIST** (no higher-rank ground truth). Emergent/
  condensed-matter at most; nothing to `CLAIMS.md`. L20 → CHARACTERIZED. `tests/test_b166_*` (3).
- **B165 — toward the off-axis (κ<2) Cantor theorem (2026-06-18; V162; P2a).** Strengthens B163. **D1:** B163's
  MST-max-gap diagnostic extended to **golden/silver/bronze** — the κ<2 Cantor structure is **seed-robust**
  (persistent gaps 0.21/0.20/0.18 vs the κ=2 band →0). **Conditional theorem:** the κ<2 spectrum = the
  non-escaping set of the complexified trace map; *uniform hyperbolicity ⟹ Cantor* — reducing the open theorem to
  **one** hypothesis (off-axis hyperbolicity), numerically supported but **NEEDS-SPECIALIST** (Damanik–Gorodetski
  is Hermitian-κ>2 only). **Verify-don't-trust record:** two attempted new diagnostics (ε-component-count, naive
  trace-map "domination") **failed** to separate Cantor from band and were discarded — B163's MST remains the clean
  one. Firewalled; nothing to `CLAIMS.md`. `tests/test_b165_*` (2).
- **B169 — the isomonodromy (Painlevé-VI) flow + the firewall-relocation verdict (2026-06-18; V161; completes P1).**
  P1/PR2 of Masterplan II. Builds the **Schlesinger / Painlevé-VI flow** on the (0,4) cubic (the genuine new
  engineering) and reaches the verdict. **P1 [exact]:** the cover dictionary done right — the metallic `M_m` acts
  with dynamical degree **`λ_m²`** (homological / Cantat–Loray), *correcting B164's orbit-norm proxy*. **P2 [num]:**
  the Schlesinger flow **preserves the monodromy** (all local conjugacy classes; drift `4.25×10⁻¹⁰`) while the
  residues move — *isomonodromy* — with a wrong-ODE control (drift 16). **P3 [POSTULATED]:** the flow's "time" is a
  dimensionless modulus and the system is scale-free ⟹ **the scale is external (Higgs-side); the Hitchin side
  RELOCATES the firewall, it does not cross it** — confirming P010/§8c and grounding B167's door-4/5. Full
  Hitchin/Higgs construction is **NEEDS-SPECIALIST**. Firewalled; nothing to `CLAIMS.md`. `tests/test_b169_*` (2).
- **B168 — the Ω accretion as a generative process (the first generative pass, S035) (2026-06-18; V160).** The
  step-back: read the Ω cone (B156–B159) as an **accretion** (forward-only, seed-rooted), not a spectrum. **G1**
  the arrow (non-cancellation grows, entropy log 2; cancellation doesn't, entropy 0 — *bare growth is generic,
  MB12-honest; the asymmetry is the content*). **G2** emergent rates (retention `0.583→0.397`, decreasing +
  decelerating). **G3** null-test: not i.i.d.-generic (the constraint tightens with depth); the limiting rate's
  specialness is unresolved on 6 points (needs L≥11). **G4** every rate is **dimensionless ⟹ no ensemble scale —
  the firewall RELOCATES** (3rd time, after B107/B151 and B167; S035 N1 confirmed). The generative reading is
  *real* but the gain is understanding, not a crossing. Sub-branches flagged (limiting-rate / multi-seed /
  firewalled causal-set dimension). Firewalled; nothing to `CLAIMS.md`. `tests/test_b168_*` (3).
- **B164 — the 4-punctured-sphere Fricke cubic + the metallic monodromy (2026-06-18; V159).** P1/PR1 of Masterplan II
  (the Betti→Hitchin direction, H5-c). The only other dim-2 Fricke cubic besides the OPT seed is the (0,4) sphere —
  the **Painlevé-VI / class-S monodromy manifold**. Built: the **Jimbo–Fricke cubic** + its three **Vieta involutions**
  (the MCG/Painlevé-VI dynamics) which preserve it `[exact]`; the **bridge** `tᵢ=0 ⟹` the OPT cubic at **κ=2** (the
  void fiber) `[exact]`; the **metallic degrees** `λ_m²` / trace fields `ℚ(√(m²+4))` `[exact]`; and the dynamics is
  **loxodromic** `[num]` (with a period-2 control). **Verify-don't-trust self-correction:** a draft "dynamical
  degree = φ²" was refuted by the numerics (orbit-norm growth ≠ dynamical degree) and removed. **Deferred to PR2:**
  the OPT↔(0,4) cover dictionary (→ degree `λ_m²` per metallic m), the isomonodromy **flow**, and the
  firewall-relocation verdict. Standalone dynamics math; nothing to `CLAIMS.md`. `tests/test_b164_*` (3).
- **B167 — the conserved ⟹ no-internal-scale lemma (the firewall, stated) (2026-06-18; V158).** P3 of Masterplan II.
  Sharpens the POSTULATED §8a five-door map + B148/B151/P010 into a **stated structural argument**: a
  conserved/topological first integral (`κ`) of a measure-preserving map **does not run ⟹ cannot source a
  dimensionful scale from within**; a scale enters only by **external import** (door 4 — the θ-angle pattern, the
  non-vacuity witness). Backbone **[exact]** (re-derived fresh: `κ` conserved by the Dehn twists + `φ_{1,2,3}`;
  dimensionless; MB6/MB12 control + witness). Five-door taxonomy **POSTULATED (argued complete)**. Independently
  **adversarially red-teamed** (6th-door stress test — holography/backreaction/Casimir/modular-weight/regulator/
  adiabatic — each reduces to door 1/4/5; firewall/scoping/tiering pass). **Firewall-side**: no scale, no Λ, no
  crossing; nothing to `CLAIMS.md`; stays POSTULATED. Betti↔Hitchin grounding deferred to a post-P1 PR.
  `tests/test_b167_*` (4).
- **B163 — the κ-sweep resolved: the κ<2 spectrum is a Cantor set; no figure-eight encoding (2026-06-18; V157).**
  Resolves the two open items B162 left (L19), each with a control / null-test. **(3a) [num, control-bracketed]:**
  the non-Hermitian κ<2 spectrum is a **genuine Cantor set (totally disconnected)**, not a curve — the largest
  spectral gap (max MST edge / diameter) **converges to a positive constant** across F=144→1597, tracking the
  κ>2 known-Cantor control (~0.16) and the opposite of the κ=2 full-band control (→0). Upgrades B162's
  "thin/zero-area" to "Cantor". **(3b) [num, negative + null-test]:** **no spectral encoding** of the figure-eight
  geometry — every feature is smooth through κ=−2 (no kink at the cusp-opening) and no figure-eight invariant
  (vol, √−3, 2/φ) matches specially there (neighbors equal/better). The figure-eight link is the **boundary trace
  κ=−2 alone** (B160), not the spectrum — the "spectrum deforms into hyperbolic geometry" reading is refuted at
  the spectral level. **(3a)-as-theorem stays OPEN** (no ground truth off the real axis). Firewalled; nothing to
  `CLAIMS.md`. `tests/test_b163_*` (2).
- **B162 — the κ-sweep: κ=2 is the unique cancellation↔non-cancellation wall (2026-06-18; V156).**
  The geometric face of the non-cancellation obstruction (S034/B161). The figure-eight monodromy foliated over
  `κ=2+λ²` has a spectrum that is **positive-measure only at κ=2** (the full AC band, `|σ|=4.000` — the
  trivial/cancellation vacuum) and **zero-measure everywhere else**: a real **Cantor** set for κ>2
  (4.000→1.817→0.706→0.097) and a **thin** complex set for κ<2 (2D area→0; lift-off `max|Im E|≈0.91μ`). Method =
  self-validated finite-chain diagonalization (V1 Hermitian sanity, V2 bulk BC-robustness, V3 size convergence,
  V4 chiral `E↔−Ē`). κ=−2 endpoint = figure-eight cusp (λ=2i, parabolic commutator, symbolic). **OPEN** (no
  ground truth off the real axis): whether the κ<2 thin set is a true Cantor set, and whether κ=−2 encodes the
  hyperbolic geometry. A **mathematical bridge, not a crossing** (both ends established — Sütő, Thurston);
  nothing to `CLAIMS.md`. `tests/test_b162_*` (3). Promotes `OPEN_LEADS` L19.
- **B161 — the cancellation-locus stratification: the non-cancellation obstruction, as math (2026-06-18; V155).**
  Math infrastructure for the spine `speculations/S034`. Reframes the dead "does κ source a Λ value?" into "is exact
  cancellation structurally non-generic?". **R1 [exact]:** the cancellation locus κ=2 (commuting/abelian/periodic) is
  **codim-1 / measure-zero** — `{κ=2}` a single hypersurface; κ **free** on the φ_m fixed locus (κ-elimination empty,
  re-derived m=2,4, *not* `sp.solve`); commuting pairs measure-zero (null-test, generic to non-abelian dynamics, the
  metallic family not special); MB12 abelian control κ≡2 (falsifiable). **R2 [exact]+[num]+[proved]:** cancellation is
  the **trivial** fiber (κ=2 ⟺ λ=0 = free Laplacian, full band [−2,2] measure 4), non-cancellation **fractures** it
  (κ>2 measure 4.000→1.817→0.706→0.097; MB6 control); Ω-cone analogue B156 entropy 0 vs log 2. **Reconciliation:**
  *the value is free* (B130) vs *the zero is non-generic* (here) — **refutes fine-tuning, NOT "forced/empty"** (κ=2
  attained). Pure MATH, firewalled (physics reading in S034 only); nothing to `CLAIMS.md`. `tests/test_b161_*` (5).
  Formalizes `OPEN_LEADS` L17.
- **B160 — the metallic-quasicrystal bridge: independent rediscovery + bronze + the κ-sweep lead (2026-06-17; V154).**
  A fresh cross-session worker (no repo access) re-derived `κ = tr[A,B] = 2+λ²` → the Fibonacci-Hamiltonian
  quasicrystal → zero-measure Cantor spectrum, and converged on the **identical bridge-not-crossing firewall**.
  Verify-don't-trust finding: the **entire bridge is already banked** (B107/A, B148/V137, K007, K010, B124, B127,
  S023) — **corroboration, not new physics**. Verified increments: the explicit transfer-matrix proof
  (`z=xy−2 ⟹ tr[A,B]=2+λ²`, E-independent, symbolic); an **independent bronze (m=3)** trace map (Cayley–Hamilton)
  conserving the Fricke invariant with a zero-measure Cantor spectrum (ratio ~0.719); and the **κ-sweep** lead —
  one foliated monodromy from the quasicrystal (κ>2, K007) to the **figure-eight hyperbolic point** (κ=−2 ⟺ λ=2i,
  parabolic commutator, B67), the κ<2 middle left **OPEN**. Emergent/condensed-matter math, **bridge not crossing**;
  nothing to `CLAIMS.md`. Reproducers + `tests/test_b160_quasicrystal_bridge.py` (5 passed).
- **B159 — the Ω strict-full class-graded DAG L4–L10, independently verified (2026-06-17; V153).**
  A cross-session "gate2 class DAG export" (the charpoly-class–graded transition graph of the Ω strict-full cone,
  L4–L10) ingested and **independently verified**: full L4–L10 conservation/structure (classes 1,2,6,18,49,115,283;
  histories 96→2 488 080; matrices 36→65 472), **every one of the 474 classes reciprocal** (TC-2 cone-wide), the
  L4 **seed = Ω₄ = B155**, and a **from-scratch re-enumeration** reproducing L4–L7 class-by-class and edge-by-edge.
  Metallic spectra (figure-eight T=3, silver T=6, bronze T=11) appear as reciprocal factors. The Myrheim–Meyer /
  causal-set "Gate-2" reading is **firewalled** (the export itself disclaims a manifold verdict). Reproducer +
  `tests/test_b159_omega_class_dag.py` (6 passed).
- **B158 — the Ω↔tower bridge audit: a spectral-only correspondence (2026-06-17; V152).**
  Resolves the open lead **L18**. The Ω charpoly factors into reciprocal quadratics with the exact relation
  **`(p−2)(q−2) = −2(m+1)`**, and **every metallic bundle-monodromy charpoly `x²−T_M x+1`** (`T_M=M²+2` =
  3,6,11,18,…) is realized as a reciprocal factor of the integer Ω family **on the live cone** (signature
  (1,3)) — the figure-eight (T=3)×Φ₆ is Ω₄=B155, the **silver (T=6)×Φ₆ is the integer point `R_{7,1}`**.
  **But** the strict-full shears commute (`A·C=C·A`), so there is **no faithful mechanism** and no functional
  `κ↦δ` pullback. **Verdict:** Ω is the **abelianized *spectral* image** of the metallic tower (monodromy
  spectra realized as Ω reciprocal factors at lattice points), not its dynamics — sharpening B156's qualitative
  "abelianized shadow" to a precise positive statement. MATH tier; nothing to `CLAIMS.md`; P1–P16 untouched.
- **B157 — the metallic degree=rank exponent: `k=4−m(o−3)` REFUTED; order-not-rank survives (2026-06-17; V151).**
  Phase 2 (derive the "metallic A-polynomial" exponent), a two-route workflow (B67 eliminant + B89 ideal
  algebra) with adversarial synthesis — the adversary (high confidence) couldn't break it and strengthened the
  SL(4)-emptiness leg. **Headline (a self-correction):** the empirically-banked closed form **`k = 4 − m(o−3)`
  is REFUTED** — extending to **bronze (m=3)** gives genuine non-degenerate counterexamples `(3,4)→k=3` (formula
  predicts 1) and `(3,6)→k=1` (predicts −5); it was an artifact of m∈{1,2}, and no ≤3-parameter law fits the
  corrected grid. **What survives** (the hedged part of B154): `k` is **order-determined, rank-independent**
  (`o=3 ⇒ k=4` at n=3 and n=4). **New exact figure-eight cells:** `o=3→4` over ℚ(ω) and **`o=4→3` over ℚ(i)**
  (`[A,B]=c·µ³`, two ways). **New machinery:** the general-m bundle system + the exact identity
  `φ_m([A,B])=Aᵐ[A,B]A⁻ᵐ` ⟹ cusp meridian `µ=A⁻ᵐt` for all m. **SL(4) `{1,1,i,−i}` (o=4) provably empty**
  (Lemma 1: `det(UR)·det(LL)` in the bundle ideal over ℚ(i); reducible). Corrects **B154/V146** in place. MATH
  tier; nothing to `CLAIMS.md`; P1–P16 untouched.
- **B156 completion — source-chat cross-check + TC-1/TC-4 + the commuting-shears scope (2026-06-16; V150).**
  The owner supplied the **source reasoning** (the ChatGPT/Ω chat that produced the work, which itself ingested
  the ~1085pp AI trace — the two chats cross-examined each other). An agent cross-check + fresh re-derivation
  here: **(1)** confirmed B156 is faithful (our re-derivations even strengthen the source) and that history
  entropy **log 2** is final (it supersedes the older `(1/3)log 7` bound); **(2)** banked two missed theorems,
  each re-derived (not transcribed) — **TC-1** [exact]: Ω₄ is the *unique minimal* strict-full seed (minimal
  level L=4; every strict-full L4 history has charpoly (4,5,4)=golden×phase), and **TC-4** [proved]: an
  orientation *no-go* (relabel-closed ensembles have zero net Pfaffian residual — orientation is boundary-induced,
  the rigorous core of "non-cancellation"); **(3)** the decisive scope — **Ω is the abelianized shadow of the
  trace-map tower, not its mechanism**: the strict-full shears `A=S₀₃, C=S₂₃` **commute**, so `R↦A, L↦C` cannot
  represent the noncommutative monodromy; the Ω↔tower **bridge audit** (κ↦δ/det G? χ_Ω↦Dickson?) is the open
  frontier (`docs/OPEN_LEADS.md` L18), never run; **(4)** the independent heavy re-run re-confirmed the **full
  strict-full count tower L4–L10 = 96/672/3840/20928/105312/521904/2488080** (state-propagation, fresh code),
  matching the handoff artifacts at every level — Phase 1 closed. Updated `frontier/B156`,
  `docs/UNIFIED_STATE.md`, PC18. MATH tier; firewall
  intact; nothing to `CLAIMS.md`.
- **B156 — the Ω strict-full cone: full integration of the cross-session Ω program, Phase 1 (2026-06-16; V149).**
  Banks the **Ω-specific** content (the SL(4) lift of P6) onto current main, with **all four Ω theorems
  independently re-derived + adversarially verified** (a 4-claim workflow with skeptics; 4/4 confirmed, none
  refuted): **(1)** core R/G algebra — `R_{a,m} ∈ SL(4,ℤ)`, `det R=1`, palindromic
  `χ = x⁴−ax³+(2a−2m−4)x²−ax+1`, `RᵀGR=G`, `det G=−δ/(m+1)`, shears `A:δ→δ+2`/`C:δ→δ−1`, signature **(1,3)**
  on the live cone (wall `δ=0` → (1,2,1); (2,2) below) — constancy *rigorous* (det `G<0` + Sylvester pivot
  certificate); **(2)** TC-2 — strict-full ⟹ reciprocal char poly; **(3)** the **Fibonacci** block-count
  (`F_{n+1}`, growth `φ`); **(4)** wall-avoiding **history entropy = log 2** (exact: `W_n(δ) ~ (1−φ^{−δ})·2ⁿ`).
  Strict-full **survivor counts** L4–L7 = 96/672/3840/20928 re-confirmed by **two** from-scratch enumerators
  (exact `det` test, with/without the reciprocity shortcut); L8–L10 = 105312/521904/2488080 from artifacts,
  independent re-run in progress. **Verify-don't-trust payoff:** the handoff's own brute-force script counts
  strict-full *per char-poly class* and **over-counts** (L5: 3120 vs the true 672) — the correct count is
  *per-matrix*; a 40 hr blind run of that script would have computed the wrong quantity. Also caught + fixed a
  TC-2 exposition imprecision. Firewall claim-boundary table copied **verbatim**; signature (1,3) = algebraic
  inertia, entropy = word-growth, **no physics**. Expert one-page note → `papers/omega_strict_full_note/`
  (**PC18**). MATH tier; nothing to `CLAIMS.md`; P1–P16 untouched.
- **`docs/UNIFIED_STATE.md` — the cross-branch "Unified State of Knowledge" brief banked (2026-06-16).**
  A single source of truth across **Branch A** (trace-map / character variety, this repo) and **Branch B** (the Ω
  history-enumeration handoff), privacy-cleaned (generic source labels; math branch names kept) and status-labelled.
  Carries a **verify-don't-trust banner**: Branch A is banked/tested here (B1–B155, V1–V148); Branch B is a *separate*
  handoff program whose B-numbering (B206…B907) is distinct, of which only the **core Ω₄/TC-1 theorem** has been
  independently re-derived in-sandbox (counts, TC-2, history-entropy `log 2` are `[confirm-with-Ω-handoff]`).
  Records the **B-number bridge** (Ω-side "B206" = this repo's `frontier/B155`) and folds in the V148 sharpening of the
  B206 ≅ Ω₄ unification (shared canonical object — same charpoly + signature + ℚ-conjugacy class; the integer Ω family
  reaches the charpoly only at half-integer `m=−1/2`, so not a common integer lattice point). Firewall preserved;
  nothing to `CLAIMS.md`.
- **PC17 — "Two Results from the Metallic Trace-Map Program" external-review note banked (2026-06-16).**
  A specialist-facing consolidation (`papers/metallic_trace_map_note/`, privacy-cleaned, status-labelled) of three
  standalone results: **A** `L=−M⁴` on the figure-eight SL(4) spectrum-pinned *slice* + completeness (the honest,
  corrected scope of the deflated PC13 "component"); **B** `κ=2+λ²` (the trace map *is* the Fibonacci–Hamiltonian
  trace map); **C** the "golden × phase" rational spectral bridge at n=4 (= `frontier/B155`). Registered as PC17 in
  `papers/CANDIDATES.md`. Results A/B repackage banked repo work; only C (B155) is new. Novelty of A/C is
  NEEDS-SPECIALIST; §5 firewall load-bearing.
- **B155 — the "golden × phase" spectral bridge at n=4 (2026-06-16; V148).**
  Processing an external-review note (Result C) + an AI-assisted cross-session synthesis (the "Ω" history-enumeration
  program) one-by-one through governance, each **independently re-derived** before banking. A single integer matrix
  `M_g = [[1,1,0,0],[0,1,1,0],[1,1,1,1],[1,1,0,1]] ∈ SL(4,ℤ)` realizes **"figure-eight monodromy × order-6 phase"**
  as a rational block structure: `charpoly(M_g) = (x²−3x+1)(x²−x+1)` — the *golden* factor (figure-eight monodromy
  trace poly, disc 5, root φ², real/Anosov) times the *phase* factor (`Φ₆`, disc −3, finite order 6). It is ℚ-similar
  to `[[2,1],[1,1]] ⊕ [[0,1],[−1,1]]` and nonderogatory; it glues the two invariant 2-planes inside ℤ⁴ with cokernel
  **(ℤ/2)²** (class-specific — the block-diagonal form with the same χ has trivial glue); and it carries an invariant
  symmetric form of **signature (1,3)** with discriminant **−15 = disc ℚ(√5)·disc ℚ(√−3)**. **B206 ≅ Ω₄, honestly
  scoped:** the Ω positive-shear family `R_{a,m}` reaches this characteristic polynomial only at the *half-integer*
  point `a=4, m=−1/2`, so the bridge is the **shared canonical object** (same charpoly + signature + ℚ-conjugacy
  class), not a common integer lattice point. **Firewall:** signature (1,3) = algebraic inertia of a bilinear form,
  **not** spacetime; no physics claim. MATH tier; nothing to `CLAIMS.md`; P1–P16 untouched.
- **B154 — the metallic meridian `µ=A⁻ᵐt` and the order-based degree=rank exponent (silver bundle; 2026-06-16; V146–V147).**
  Phase C of the B153 campaign (does degree=rank generalize from the figure-eight m=1 to the silver bundle m=2, R²L²?).
  **(1) The metallic meridian:** `µ=A⁻ᵐt`, derived from the exact free-group identity `φ_m([A,B])=Aᵐ[A,B]A⁻ᵐ` (the
  monodromy fixes the fiber boundary up to conjugacy; the figure-eight's `A⁻¹t` is the m=1 case). **(2) degree=rank
  GENERALIZES** to the metallic family: with `µ=A⁻ᵐt` the matrix identity `[A,B]=±µᵏ` holds for silver too — so it is
  *not* figure-eight-special. **(3) The exponent is ORDER-based, not rank-based** — "degree=rank" (`k=n`) is a
  coincidence of the principal spectra (B95 ties their order to the rank); the decisive test is that figure-eight
  `{1,ω,ω²}` (order 3) gives `k=4` at *both* n=3 and n=4. Closed-form fit **`k=4−m(o−3)`** (o = boundary-spectrum
  order) on all accessible points; `k` is the A-polynomial slope. **(4) Geometry:** the silver `{1,ω,ω²}`@SL3 locus
  is a fixed-spectrum component (codim 0) that is an A-free slice (tr A moves) — the figure-eight n=4 pattern.
  A first-principles *derivation* of `k=4−m(o−3)` is open (the metallic A-polynomial, the B67→B89 program generalized).
  Several verify-don't-trust self-corrections along the way (best-rep over-read → wrong-meridian → derived positive;
  "slice"→ the precise component/slice deformation theory). Also: the **lean self-audit workflow completed** (V147) —
  48/50 confirmed, only P10/P12 flagged (both already handled; it reversed its own P12 verdict), 2 minor honesty
  caveats applied. MATH tier; nothing to `CLAIMS.md`; P1–P16 untouched.
- **B153 — the rank-stratified degeneration of degree=rank + a self-scrutiny campaign that corrected merged work (2026-06-15; V142–V145).**
  Replaces the deflated PC13 "SL(4) figure-eight A-polynomial component" with the honest, stronger result: the figure-eight
  degree=rank relation `L=(−1)^{n-1}Mⁿ` is **rank-stratified** — a genuine SL(n,ℂ) character-variety **component at n=3**
  (`L=+M³`, Falbel; **now exact over F_p**, 3 primes: geometric dim-5 component tangent 11/rigid/irreducible, with a
  reducible slice tangent 10 — correcting an earlier numerical "tangent 14"), a measure-zero **slice at n=4** (`L=−M⁴`,
  exact over ℚ(ω): A-free tangent 29/kernel 19), and **not realized on any irreducible representation at n=5**. A validated
  reusable toolkit (`sln_toolkit.py`) seals the recurring bug classes (finite-difference, sqrt-branch, near-singular `t⁻¹`).
  **The self-scrutiny campaign (multi-agent workflow) found real bugs in merged results, verified and corrected them:**
  (i) **n=5 (V143):** the banked "non-ss: 0/120, no irreducible reps" was a `det t=0`-drift artifact — with `det t=1` pinned,
  irreducible SL(5) reps with spectrum {1,1,1,−1,−1} **do exist** (non-semisimple `[3]`-block Jordan types; two independent
  certificates, Burnside rank 25 **and** Schur commutant dim 1); degree=rank fails on them, so the headline survives, reason
  corrected. (ii) **B95/V79:** "the principal spectrum is *forced*" → forced *given* the mult-(n−2)/finite-order ansatz
  (counterexample {1,ω,ω²,e^{±iπ/3}}); and the **finite-order insight** — a principal/Dehn-filling rep has `A` finite-order
  ⟹ semisimple ⟹ `A²=I` ⟹ dihedral ⟹ reducible, so **no irreducible principal rep at n=5 is PROVEN** (upgrading the n=5
  endpoint from numerical to proven, reconciling B95 ↔ B153). (iii) **P10** (owner-approved CLAIMS.md down-tiering):
  "five independent filters all select 4₁" → trace-3 sieve **PROVED**; the other four documented/suggestive
  (NEEDS-SPECIALIST). (iv) **B92/V76-V78:** "all det=−1 trace-`m` matrices conjugate to the companion" is **false at m≥4**
  (form class number `h(m²+4)=2` at m=4, disc 20); the companion is one GL(2,ℤ) class among `h`. (v) **V99/B112:** the
  "sign half for all n" headline (already self-relabeled by B116/B117/B118) given a ledger back-pointer. The audit's B95 flag
  and the independent n=5 re-derivation *converged* on the same gap. MATH tier; **two-mirrors** (the audit de-risks, novelty
  still NEEDS-SPECIALIST); nothing promoted to `CLAIMS.md` (P10 was reworded *down*); P1–P9, P11–P16, B85 untouched.
- **B152 — Chern–Simons as a one-sided parity order parameter (2026-06-11; V141).** Census test of *amphichiral ⇒ CS is
  2-torsion* over SnapPy `OrientableCuspedCensus[:240]`: **0 necessity violations**, exactly **one converse counterexample**
  (m208, chiral with CS=0) — so CS-2-torsion is **necessary but not sufficient**, the correct order-parameter behaviour.
  Method guards: amphichirality gated on `is_full_group()`; CS torsion by *circular* distance mod ½. No physics; a census fact.
- **B127 — chirality, Fibonacci, arithmetic, and the object's proper name (2026-06-08; V116).** Resolves the
  "threads 3 & 4 + Fibonacci" investigation (verify-don't-trust; every claim re-derived in-sandbox). The
  physics-bridge claim returns a **clean, multiply-confirmed negative** (the firewall `P007` confirmed from a third
  and fourth independent direction — chirality and arithmetic). **Surviving MATH:** the golden substitution's
  **fusion algebra** is the Fibonacci/Yang–Lee fusion algebra (`λ²−λ−1`, Perron `φ`; the categorification is *not* a
  framework output); the metallic family is the **achiral (Chern–Simons ≡ 0) + imaginary-quadratic corner** of the
  once-punctured-torus bundles (CS=0 to machine precision m=1..6 vs a discriminating census mix); **expansion ⊥
  unitary topological order** (hyperbolic→non-unitary, CS=0→`c₋=0`); and the **arithmetic trichotomy** — fusion
  `ℚ(√(m²+4))` (real) vs manifold imaginary-quadratic vs braiding `ℚ(ζ5)`, with `ℚ(ζ3)∩ℚ(ζ5)=ℚ` (disjoint).
  **The proper name (`knowledge/K010`, `philosophy/P008`):** the object is the **metallic-mean Schrödinger cocycle**
  analyzed by its **Kohmoto–Kadanoff–Tang trace map**, `κ` its **Fricke–Vogt invariant**; the exact dictionary `κ=2`
  (commuting/periodic/AC spectrum) vs `κ>2` (irreducible/hyperbolic Damanik–Gorodetski horseshoe/Cantor spectrum) —
  **non-cancellation = Fricke–Vogt positivity = Cantor spectrum**. Emergent aperiodic-order physics (real, observed),
  firewalled from fundamental — the strongest honest "this is physics" the arc has produced. New: `λ_m<2` **only for
  m=1** → only golden can be a quantum dimension; the three BMR arithmetic classes named `{RL→ℚ(√−3), RRLL→ℚ(i),
  RRL→ℚ(√−7)}` (√−7 non-metallic). **Four kills tombstoned** (K-A/K-B det=−1-breaks-chirality DEAD+INVERTED — CS≡0,
  det=−1 is the orientation-reversing *symmetry*, distinct from B124's algebraic tower P-parity which stands; K-C
  figure-eight = *physical* Fibonacci DEAD — non-unitary→Yang–Lee, fusion-rule-only, ζ5≠ζ3; K-D unitary topological
  order DEAD; K-E forced scale DEAD); `S030` = the Fibonacci/Yang–Lee fork (DORMANT). **Citation fixes** to the merged
  B126: re-attach Floor-2 SUSY from mis-attached Cho–Gang–Kim arXiv:2007.01532 (which is non-hyperbolic→unitary —
  supports K-D) to Gang–Yonekura arXiv:1803.04009; split "Generalized Global Symmetries of T[M]" Part I (2010.15890,
  JHEP04(2021)232) / Part II (2511.13696, JHEP05(2026)087). MATH + emergent-physics tier; physics POSTULATED/
  quarantined; nothing to `CLAIMS.md`; P1–P16 and the functorial `Sym(W)→trace-ring` wall untouched.
- **B126 — the ladder to physics: how far does the metallic rigidity propagate? (2026-06-08; V115).** A
  foundational-question investigation (direct computation + a five-agent literature survey). **Answer: the metallic
  object's classical rigidity propagates exactly two floors up the ladder (quantize → 3d `T[M]` → 4d → particle
  content), provably, then hits a nameable wall.** **Floor 1** (arithmetic → quantization): the invariant trace field
  determines the *field* of the perturbative quantum series — a *theorem*, proven for our exact family
  (once-punctured-torus bundles, Yoon arXiv:2110.11003; Dimofte–Garoufalidis 1202.6268). **Floor 2** (Mostow → `T[M]`
  rigidity): no marginal couplings; `M` selects the SUSY phase (`4₁` → unbroken SUSY, gapped vacua, Cho–Gang–Kim
  2007.01532); `H₁` torsion → one-form/center symmetry. **The wall:** 3d→4d is data of the 2d *boundary* surface, not
  the 3-manifold; the SUSY-breaking *scale* is orthogonal input. Honest ceiling **N=4 SYM / N=2\*** (geometric
  Langlands) — not the Standard Model. So we lack no concept; we lack what no 3-manifold can carry. Two in-house
  facts: **(A)** `H₁(M_m) = ℤ ⊕ (ℤ/m)²` (Smith normal form of `M_m²−I = m·M_m`; SnapPy `m=1..7`) — the metallic `m`
  *is* the order of the homology torsion; **(B)** arithmetic(`m=1,2`) ⟺ `κ` rational in z on the geometric component
  (κ-degree over `ℚ(z)` = `[1,1,3,3,7,6]`) — **family-specific, not a law** (no "arithmetic ⟺ simple A-poly"
  theorem). Firewalled readings: `speculations/S029` (the `H₁`-torsion → center-symmetry / `m→ℤ/m→`SU(m)→SM reading,
  POSTULATED, with **five** explicit kill conditions — incl. that `T[M]` is rank-1 *abelian* so `ℤ/m` is a
  line-spectrum symmetry, not an `SU(m)` gauge group), `philosophy/P007` (the object as a **maximal probe** of the
  geometry↔QFT correspondence, not a seed of reality), `speculations/LADDER_LITERATURE.md` (the citation map), the
  `PHYSICS_BRIDGE_MAP` ladder section. Also **corrects** the inherited "exactly two arithmetic punctured-torus
  bundles" off-by-one (Bowditch–Maclachlan–Reid 1995 = *three* commensurability classes; "m=1,2 arithmetic" is a
  family-restricted statement) across K009/K002/B125. MATH/number-theory tier; physics POSTULATED/quarantined; nothing
  to `CLAIMS.md`; P1–P16 and the functorial `Sym(W)→trace-ring` wall untouched.

### Changed
- **B125 — arithmeticity correction (overturns K009; 2026-06-08; V114, TESTED-POSITIVE).** With SnapPy now runnable
  in-sandbox, the invariant trace field `kM` of the metallic family is computable directly. Result: **arithmeticity
  does *not* uniquely select `m=1`** — it selects **{m=1 golden `ℚ(√−3)`, m=2 silver `ℚ(i)`}** and kills `m≥3`. The
  orientable metallic members are the once-punctured-torus **bundles** `M_m² = R^m L^m` (`m=1` = the figure-eight,
  `m004`); the two arithmetic ones are in different Bianchi families (not commensurable) — the "exactly two arithmetic
  punctured-torus bundles" K009 already cited. This **corrects** the B123/K009 "third *independent* / *unique* `m=1`
  arithmetic" sub-claim, which mis-applied **Reid 1991** (a *knot* theorem) to bundles. **Corrected:**
  `knowledge/K009` (arithmeticity is a two-element selector; systole + expansion still uniquely select `m=1`),
  `K002`, `K004`, `knowledge/INDEX`, and the V112 ledger row (annotated). **Preserved:** Reid 1991 stands
  (knots ≠ bundles; `m=2` being arithmetic confirms its scope); the order-6 echo stays an observation. **Honest:** the
  two arithmetic verdicts + the `m≥3` non-arithmetic verdict reproduce robustly two ways (shape field +
  traces-of-squares); the exact `m≥3` field degree is precision-sensitive and not over-claimed. Tooling availability
  recorded in `REPRODUCIBILITY` (SnapPy 3.3.2 + cypari installable in-sandbox — gate lifted; MAGMA still
  unavailable). MATH tier only; physics POSTULATED/quarantined untouched; nothing to `CLAIMS.md`; P1–P16 and the
  functorial `Sym(W)→trace-ring` wall untouched.
- **Documentation refresh to B124/V113 (2026-06-08; docs only, no math, no claims).** Brought the whole governed
  documentation layer up to the current state of the research, which had run well ahead of it. **`knowledge/`
  completed:** wrote all seven stubbed explainers — `K001` (trace map & character variety), `K002` (the metallic
  family & continued fractions), `K003` (the Dickson tower), `K004` (figure-eight / Dehn filling / A-polynomials),
  `K005` (the opposition involution `θ=−w₀`), `K006` (the 3d-3d correspondence + its firewall), `K007` (the
  Fibonacci/quasicrystal trace map); the layer is now `K001–K009`, all written (standard material cited to the
  literature, project use cited to `B`/`V`, no new claims). **`story/`:** added chapter `09 — the representation,
  crystallized` (the B111–B124 arc: the sign half proved, `ρ_n = Sym^n(W)`, the external monodromy fundamental, the
  functorial wall) and refreshed `08`. **`docs/atlas/`:** added the representation-program sections to
  `SUCCESS_ATLAS`, `RESEARCH_TREE`, and `GLOSSARY`, and a "Pattern G" block of B111–B124 kills to `FAILURE_ATLAS`.
  **`ROADMAP`:** refreshed the Phase B probe ladder through B33–B124 and the suite count (369 passed). **Stale live
  ranges fixed:** `S001…S021 → S001…S028`, `K001–K007 → K001–K009 (all written)`, `P000–P003/P005 → P000–P006`
  across `ARCHITECTURE`, `README`, `philosophy/PHILOSOPHICAL_PATHS`, `speculations/GOVERNANCE`, `knowledge/INDEX`
  and `knowledge/GOVERNANCE`. Nothing promoted to `CLAIMS.md`; P1–P16 untouched; the firewall and the functorial
  `Sym(W)→trace-ring` prize are unchanged.

### Added
- **B124 — reciprocal `(λ,1/λ)` pairs + the time-reversal involution `λ↔1/λ` (2026-06-08; V113).** Two
  **strictly-separated** tiers. *Generic (symplectic):* the trace map is a reversible area-preserving map, so the
  Jacobian spectrum at a hyperbolic fixed point is **reciprocal-closed** `(λ,1/λ)` and time-reversal (the inverse
  map) acts as `λ↔1/λ`, swapping stable/unstable — symplectic geometry, **not** a metallic feature; the only
  metallic-specific datum is the **rate** `log φ²` (same lesson as unitarity / tautological roots / the volume
  conjecture). Anchor: the SL(2) **void** Jacobian `{φ²,−1,φ⁻²}`, `det=−1`. *Metallic-specific (the supplement):* at
  SL(n≥3) `det=−1` the tower carries **negative** reciprocal-pair modes (`char(−M^h)` sectors; `det=+1` has **none**)
  — a `det=−1` **sign/chirality** imbalance `O(n/2)` (= amphichirality B118/B121, via the inversion identity
  `char(M⁻¹)=char(−M)`). **Decisive recompute: expanding count == contracting count EXACTLY, every n, both det → NO
  arrow** — the asymmetry is **chirality (P)**, not time-direction (T). The exact constant is **open** (the raw `±1`
  excess is period-4, not `⌊n/2⌋`; n≥5 inflated by the B117 middle-band doubling — do **not** bank the closed form).
  Math banked in `knowledge/K008`; the **"two-headed time"** *reading* (Carroll–Chen / CPT-symmetric resonance) is a
  **labeled overlay**, firewalled in `philosophy/P006` and the dynamics fork `speculations/S002` (corrected to **no
  arrow** + one DORMANT metallic-specific thread: does the seed select the reference point?). Tier discipline: the
  math and the interpretation never share a sentence. Physics quarantined; nothing to `CLAIMS.md`; P1–P16 untouched;
  the functorial `Sym(W)→trace-ring` wall is untouched.
- **B123 — m=1 arithmeticity, the third independent `m=1` selection criterion (2026-06-08; V112, `SUPPORTED`).**
  The figure-eight complement's regular ideal-triangulation shape is the 6th cyclotomic root `z₀ = e^{iπ/3}`
  (`z²−z+1 = Φ₆`), invariant trace field `ℚ(√−3)` → **arithmetic**; by **Reid (1991)** the figure-eight is the
  *unique* arithmetic knot complement, so the `m≥2` metallic manifolds are not arithmetic. This joins the **systole**
  (B92/S001) and the **expansion threshold** (P004/B120) as a third *independent* import that picks `m=1` — written
  up as `knowledge/K009`. **Computed in-house:** the Φ₆ shape and the **order-6 echo** (the `(0,0,0)` non-void
  Jacobian spectrum `λ³+1` at `κ=−2`, the geometric cusp — banked as an *observation, not a connection*). **Cited /
  gated:** Reid 1991; the `m≥2` trace-field non-arithmeticity is the **named confirmation step** (SnapPy/Magma — no
  in-house classifier), so `SUPPORTED` not `TESTED-POSITIVE`. Triage companions, same PR: **five quantum/knot
  observations tombstoned** as standard theory in our notation (unitarity `|λ|=1` / roots-of-unity tautology /
  Kashaev=volume conjecture / `z₀`-k=4 coincidence / "three regimes") in `speculations/TOMBSTONES.md`; one **DORMANT
  tooling-gated target** sharpened (`speculations/S027` §3, the metallic phase-structure discriminator). The `det=−1`
  middle-eigenvalue `=−1` is the proved **B121** parity (asset, cross-ref). Physics quarantined; nothing to
  `CLAIMS.md`; P1–P16 untouched.

### Changed
- **B122 interlude extensions — the det layers split + the Sym tower is void-specific (2026-06-07; annotations, no
  new ledger row).** Two terrain-sweeping findings banked as extensions of B122 (verify-don't-trust): **(F1)** the
  **magnitude layer** (the W-identity / `μ_d`) is **`det`-independent** — a polynomial identity in `(x,y)`, holds
  `det=+1` as well as `det=−1` (verified through n=14), so it is *more general than the metallic ray*; the **sign
  layer** (the inversion identity `char(M⁻¹)=char(−M)`, the parity factor) is **`det=−1`-specific** (the parity
  `(t−1)(t+1)→(t−1)²` collapses going golden → fig-8 `=`golden², `det=+1`). **(F2)** the `Sym` tower is
  **void-specific**: at SL(2) the void Jacobian `=Sym²(M)`, the other fixed point `(0,0,0)` is **6th roots of unity**
  (`λ³+1`, `DT⁶=I` — order 6, a corrected narration slip of "order 3"), elliptic not `Sym` (corroborates B106).
  Confirmations: the W-identity holds through n=14; the S023 box-dimensions do not cleanly separate (finite-size,
  reconfirming the W1 demotion). None touch the wall — the functorial `Sym(W)→trace-ring` construction is still the
  one missing piece. Nothing to `CLAIMS.md`; P1–P16 untouched.
- **Firewalled triage of the cross-chat "seven hints" (2026-06-07; docs/governance, no math).** Banking the
  physics-facing hints on the `μ_d` object as **different tiers** so the firewall does not leak: `philosophy/P005`
  (laws vs states — INTERPRETATION on B120's spectral/geometric split); `speculations/S028` (the
  `Sym⁴(3-space)=sl(4)` reading — the **algebra is proved** in B122, the **"3+1" geometry is fenced** POSTULATED,
  "spacetime" stripped as adjacent to the DEAD S017/S018, bound to B122's open functorial hinge; the spin-2/gravity
  overlay recorded fenced *underneath* the math, never in `knowledge/`). The CS-crossover `k≈4↔n=4` is **tombstoned**
  (m-dependent volume coincidence). Watch-item fixes: **S023** re-scoped so `TESTED-POSITIVE` rests on the exact
  arithmetic field-distinctness (box-dimension demoted to supporting/finite-size); **S027** sharpened so the golden
  4₁ Kashaev is the *textbook* feasibility witness and the new content is the **m≥2** cocycle. **`S028 ≠ S024`** (a
  numbering collision in the incoming handoff, corrected). Nothing to `CLAIMS.md`; physics chapter CLOSED.
- **Intellectual-architecture reorganization (2026-06-07; docs/org only, no math).** Introduced four governed rooms
  for the evolving speculative ideas, all firewalled (nothing promotes to `CLAIMS.md`; the physics chapter stays
  CLOSED; the mathematics never cites them): **`speculations/`** (the catalog `S001…S021` with a proof-status enum
  incl. `HELD(value-matching)`, the "final theory" exercise `PHYSICS_EXERCISE.md`, per-live-speculation files, the
  DEAD `TOMBSTONES.md`, and `archive/`); **`philosophy/`** (`GOVERNANCE` + `P000–P003` + the migrated `P1–P5`
  register + `METALLIC_FOUNDATIONS`); **`story/`** and **`knowledge/`** (per the priority order); and the one-page
  `ARCHITECTURE.md` (the one-way firewall arrow). **Migration:** `paths/philosophical/{PHILOSOPHICAL_PATHS,
  METALLIC_FOUNDATIONS}.md → philosophy/`; `paths/philosophical/{PHYSICS_RESONANCES, COSMOGONY_FROM_THE_VOID}.md →
  speculations/archive/` (COSMOGONY superseded by the corrected `PHYSICS_EXERCISE.md` — notably the κ=−2 cusp fix
  and the HELD tier). All **live** references redirected (frontier firewall banners, READMEs, REPO_STATE, atlas,
  this file, the repo-map); append-only `PROGRESS_LOG.md` history and historical ledger rows left intact, with a
  migration mapping recorded in `PROGRESS_LOG.md`.

### Added
- **B122 — the tower is symmetric powers of the external fundamental `W = V⊕1` (2026-06-07, Ledger V111; no
  physics).** Banks Chat-2's W-identity (audited, verify-don't-trust) and **unifies it with B121** (one object, not
  two). The two-sequence re-expressed as a virtual `GL(2)`-module: `ρ_n = Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)`, `W=V⊕1`.
  A **genuine `GL(2)`-module iso** (symbolic in general `(x,y)`, det-independent, n≤8; module-level proved n=3,4 via
  B103) — *not* vacuous (the tower is a `GL(2,ℤ)`-rep). **`W` is B121's external monodromy fundamental:** `det(W)=−1`
  (external) vs `det(Fricke=Sym²V)=+1` (internal/Kostant), so Chat-2's "`W`=Fricke" kill **is** B121's
  external≠internal; the tower's odd weights = `Sym^n(V⊕1)∋V` = the B121 parity obstruction. `Sym⁴(3-space)=15=sl(4)`
  is the unique saturating order (the n=4 fixed point, B117). **Honest:** a repackaging + a canonical `W`, **not** a
  wall-bypass (no functorial `Sym(W)→trace-ring` map; the `Sym⁴(3)=15` saturation is n=4-only). Re-aims the prize
  ("prove the tower is *functorially* `Sym^n(W)⊕…`") without lowering the wall; magnitude layer only (signs = the
  det=−1 layer, B118). K008 extended. The 3+1/spin-2 readings are firewalled (S028). Nothing to `CLAIMS.md`; P1–P16
  untouched.
- **Physics-bridge sweep, Phase 3 — the heavy forks mapped + the Kashaev feasibility (2026-06-07, Ledger V110;
  FIREWALLED).** The three heavy/deferred bridges are mapped as `DORMANT` speculations with concrete computations +
  obstructions: **S025** (off-principal independent spectral content at higher rank — EMPTY at 4₁/SL(3), B110; open
  only at SL(4)/SL(5) or other manifolds; obstruction = no SL(4) char-variety classification + non-Hermitian
  realization), **S026** (does the SL(n) tower organize the `T[4₁]` state-integral at fixed knot / varying rank? —
  moduli/A-variety level in-house, the quantum state-integral is research-level), **S027** (the metallic Kashaev
  invariants as quantum modular forms — **feasibility shown in-house**, `kashaev_feasibility.py`: `J_N(4₁)→vol(4₁)`
  monotone; the open part is the Zagier–Garoufalidis cocycle + the per-knot arithmetic in `ℚ(√(m²+4))`). All target
  structural/arithmetic content, **not** new fundamental physics; the continuous family-in-m is dead, so the forks
  vary the rank `n`, not the seed `m`. Firewalled; nothing to `CLAIMS.md`; physics chapter stays CLOSED; P1–P16
  untouched. **This completes the physics-bridge sweep** (Phases 0–3): the terrain is fully mapped (dead/live/heavy),
  the two live leads are banked (S023 distinct real quasicrystals, B121 the monodromy/Hitchin grading), and the
  heavy forks are scoped with feasibility + obstructions.
- **Physics-bridge sweep, Phase 2 — the monodromy sl(2) grading (2026-06-07, Ledger V109; no physics in the math).**
  B121 gives the **positive** characterization of the banked negative "tower ≠ Kostant" (B89-T/B98): the `(n²−1)`-dim
  tower carries two `SL(2)`-actions on the adjoint — the **internal principal** `sl(2)⊂sl_n` (Kostant `⊕Sym^{2i}`,
  even weights, `det=+1` = the Hitchin/Fuchsian section, B101) and the **external monodromy** `GL(2,ℤ)` (the tower
  `⊕Sym^d(M_m)^{μ_d}`, mixed parity, `det=−1` = the mapping class group). They agree only at n=2; for n≥3 the tower
  has **odd** highest weights (Kostant is even-only) ⇒ inequivalent, and the obstruction **is** `det(M_m)=−1`
  (`det Sym^d(M_m)=(−1)^{d(d+1)/2}`; the odd blocks are the `char(−M^h)` sectors, B112/B118 — the program's own
  catalog parity, B93/B94). **Not** a dimension coincidence. The monodromy is the Hitchin section's `det=−1`
  monodromy partner; the Hitchin/Langlands/class-S *reading* is firewalled (`speculations/S024`, ceiling N=4 SYM).
  No physics in the math; nothing to `CLAIMS.md`; physics chapter stays CLOSED; P1–P16 untouched.
- **Physics-bridge sweep, Phase 1 — the metallic means are distinct real quasicrystals (2026-06-07, Ledger V108;
  FIREWALLED, no physics promotion).** A brave-but-honest sweep of the bridges to physics. First the **terrain map**
  (`speculations/PHYSICS_BRIDGE_MAP.md`): every bridge classified DEAD (masses/Λ/spacetime/holography/anyons/
  SW-family/SL(n≥3)-Hermitian-chain/tower=Kostant — do not revive), LIVE, or HEAVY. Then the Phase-1 live result
  (`frontier/physics_probes/metallic_spectra.py`, S023, `TESTED-POSITIVE`): the SL(2) Hermitian metallic
  quasicrystals (golden m=1, silver m=2, bronze m=3) are **arithmetically distinct real materials** — the
  gap-labeling module lives in `ℚ(√(m²+4))` = `ℚ(√5),ℚ(√2),ℚ(√13)` (three distinct fields), with distinct RG scale
  `φ_m` and spectral dimension — **even though** the tower *algebra* (the Sym two-sequence `μ_d`) is m-universal
  (B120). The algebra is one object; the physics is a family of distinct, buildable materials. **Honest scope:** 1D
  condensed matter, **not** fundamental physics; the SL(n≥3) extension is blocked (non-Hermitian). Firewalled;
  nothing to `CLAIMS.md`; the physics chapter stays CLOSED; P1–P16 untouched.
- **B120 — the trivial-point tower is determined by `(n; trace, det)` (2026-06-07, Ledger V107; no physics).**
  Banks the Chat-2 exploration interlude (Q2/Q3) + the computed Supplement (S1–S5), verify-don't-trust. The
  `(n²−1)`-dim tower (the Sym two-sequence, B117/B103) is **one object** fixed by two inputs — the unfolding depth
  `n` and the abelianization seed `(trace, det)`. **Q3:** distinct same-`(trace,det)` integer matrices give
  identical towers. **S2 (the deep lead):** the Sym content `μ_d` is m-independent — the `μ_d` are plethysm
  multiplicities of the `GL(2,ℤ)`-rep `ρ_n`, trace-blind; this **reframes the prize as a plethysm** but is a
  *reduction, not a closure* (proved n=3,4; same trace-ring wall). **Q2:** degree=rank **splits** — (I) spectral
  `char(Mⁿ)` factor ⟺ `μ_n=1`, all n / (II) geometric longitude=meridianⁿ, n∈{3,4} (order `{4,3,2,∞}`) — dissolving
  the apparent B117-vs-B119 tension. **Three corrections** (verify-don't-trust): S1's `(n²−3n)/2` → `(n−4)(n+1)/2`
  (the doubling band forced); S5's `2·max(1,n−h−1)` guess refuted **and** a closed form found (heights run 0..n:
  `count(n,0)=n−1`; `2(n−2)` h∈{1,2}; `2(n−h)` 3≤h≤n−1; `2` h=n); S4 confirms B116 is factor-level (the Chat-2
  "n=3 divergence" was a units error). **Governed-folder banking:** `knowledge/K008` (the determination explainer),
  `philosophy/P004` (expansion is interaction-born — `M_m=(twist)ᵐ·(swap)`, the SL(2,ℤ) finite-order-generation
  spine), and the **downgrade** of the Markov-blanket / boundary-open reading to low-rank n∈{3,4} (TWO_SYMMETRY_FRAME,
  S022). The all-`n` prize is unchanged and un-fused: prove the Sym two-sequence `μ_d` (B103), now seen as a plethysm.
- **B118/B119 — the sign-half gate closed + the power-half sharp negative (2026-06-07, Ledger V105–V106; no
  physics).** Chat-2's Path 1 (the gate) and Path 3 (the hard path). **B118 (V105):** B112 proved the `(+1,−1)`
  eigenspace *dimensions* of `θ=−w₀` on the height-`h` roots by a permutation argument; the `⌈`-vs-`⌊` tip is
  decided by the sign θ carries on the lone fixed root (odd `m=n−h`). Path 1 asked whether that sign is `+1` for
  all `(n,h)` (which would make B64 a uniform "`+1` sector = `char(M^h)`" theorem). Realizing θ as the genuine
  *signed* contragredient involution `τ(X)=−J Xᵀ J⁻¹`, the **fixed-root sign `= (−1)^{h+1}`** (symbolic + verified
  `n≤12`) — `+1` for odd `h`, `−1` for even `h`: **NOT a uniform +1.** So B64's "`+1` sector = `char(M^h)`" holds
  only for odd `h` — a **refinement/correction** of B112's unsigned "fixed root is always +1". The `(⌈,⌊)`
  dimensions stand; B112's `char(M^h)=⌈` labeling stays tower-verified `n≤5` (B118 supplies the all-`n` sign).
  Emergent (non-circular): the fixed-root sign `= +1` ⟺ the inversion identity `char(M^{−h})=char(−M^h)` ⟺ `h`
  odd. The θ-split is **not the tower** (the Sym two-sequence, B117; diverges `n≥6`).
  **B119 (V106) — a sharp negative:** `Mᵏ` central on the principal iff `order(a)|k` (`a+1/a=3−n`,
  `order(a)={4,3,2,∞}`); `k=n` is non-central where the principal exists (n=3,4) but **not unique** ⇒ centrality
  does **not** force `k=n` (the proved A-poly B83 pins it), and for **n≥5 the principal does not exist
  irreducibly** (B95) ⇒ `exponent=rank` is an `n∈{3,4}` phenomenon; the brave `k=n` proof cannot be completed. The
  secondary 2n-type gives exponent `n−1` (extends B111). Emergent (B111 ADD2 correction): the cusp order is
  `{4,3,2,∞}`, not a clean `{n−1,n+1,2n}` law (B111 ADD2 conflated three components). The all-`n` tower stays the
  prize = prove the Sym two-sequence `μ_d` (B103).
- **B117 — the interleaving insight: the tower is the Sym two-sequence; the "promotion" is a `Sym¹` absence
  (2026-06-07, Ledger V104; no physics).** The **headline reframing** of the B111–B116 run (the Opus interleaving
  insight, verify-don't-trust). The `(n²−1)`-dim trivial-point tower is **one object** — the **Sym two-sequence**
  (B103/B58) — not two separable halves (sign + power). A **dimension identity**
  `(n+1)(n+2)/2 − (n²−1) = −(n−4)(n+1)/2` (roots `{−1,4}`) **derives** B103's `μ_d = [2≤d≤n]+[0≤d≤n−3]` (n=4 the
  unique perfect fit; n=3 omits `Sym¹`, the unique subset `{0,2,3}`; n≥5 doubles `Sym²..Sym^{n−3}`). So **the
  "promotion" is a `Sym¹` absence** — the B111/B113 "two-halves"/"promotion" framing is **superseded and
  tombstoned** (the height-1 `char(−M)` at n=3 is `Sym³`'s contribution, not a "promoted `Sym¹`"). **degree=rank's
  `char(Mⁿ)` = `Sym^n` presence** (`μ_n=1` ∀n; dim-forced only at n=3 — *not* "by dimension"; rep-theory n=2,4;
  two-sequence form n≥5). `Sym⁰..⁴` product = the B80 proved n=4 tower. **B112 relabeled to three tiers** (the
  `−w₀` multiplicity structure up to the fixed-root label — proved all n; the labeling = B64, pending B118; the
  tower realization with powers — verified n≤5, superseded). **Re-aimed prize:** prove the **Sym two-sequence
  `μ_d`** for all n (B103's open problem).
- **B116 reconciliation + a CORRECTION to B112 (2026-06-07, Ledger V103; no physics).** The B112↔B103
  reconciliation (run to join the prize's two halves) found a **verify-don't-trust correction** instead: the
  **Sym two-sequence (B103) = the actual tower** (it matches the resolved SL(5) and carries `char(Mⁿ)`
  automatically), while the **θ-split (B112) = the tower only `n ≤ 5`** and **diverges at `n=6`** (the banked
  V26/V27). **B112's "sign half proved for all n" is explicitly downgraded to "n ≤ 5"** (the combinatorial lemma
  stands for all n; the *tower-identification* — the V25 gap — holds only n≤5). The all-`n` sign half is **OPEN**;
  the live route is the **Sym two-sequence** proof (B103), the better tower-candidate.
- **The ρ_n sign half PROVED + the five follow-on paths — B112–B115 (2026-06-07, Ledger V99–V102; no physics).**
  **B112 (V99) — the headline:** the **sign half of `ρ_n` is proved for all n**, engine-free — an elementary
  root-system reversal lemma (`θ=−w₀` acts as the reversal on the height-`h` roots of `A_{n−1}`, `(+1,−1)`
  eigenspace dims `(⌈(n−h)/2⌉, ⌊(n−h)/2⌋)`, verified all n≤12) × the banked B64 parity assignment ⇒
  `mult char(M^h)=⌈(n−h)/2⌉`, `char(−M^h)=⌊(n−h)/2⌋`. The first catalog piece proved from first principles for all
  n. **B113 (V100):** the proved closed form **resolves the SL(5) sign sectors** at heights 2–4 by proof
  (including `char(M²)²·char(−M²)` = B62's two gauge-corrupted modes the eps-series could not resolve), and
  **localizes degree=rank to height-1 + `char(Mⁿ)`** (the promotion is n-dependent — the power half stays open).
  **B114 (V101):** the covering-degree mechanism is **TESTED-NEGATIVE** (full covering degree `~k^{n−1}`, not `k`).
  **B115 (V102):** the known SL(4) Dehn-filling reps are forced-locus (like SL(3)); off-locus SL(4) + genus-2
  degree=rank scoped **OPEN** with named obstructions. **State of the prize:** the sign half is proved (all n);
  the open piece is the **power half** (the single degree=rank promotion `char(M)→char(Mⁿ)`, localized to the
  height-1/top-power interface).
- **B111 — the tower's sign structure + the degree=rank exponent (2026-06-07, Ledger V98; no physics).** The
  "sign findings" handoff. The opposition-involution all-heights **closed form** (`⌈(n−h)/2⌉` / `⌊(n−h)/2⌋`,
  matching B62 height-2) is **not** the proved tower: `Tower(n) = [closed form, heights 1..n−1]` with **exactly one
  `char(M¹)` promoted to `char(Mⁿ)`** (verified n=3,4) — the single non-bulk piece being `char(Mⁿ)` = the
  **degree=rank** top power. So the tower's **sign half is closed-form** (bulk θ); the only open piece is the
  degree=rank promotion (peripheral). **ADDITION 1 (proved):** on the SL(4) secondary `M⁴=−1` is scalar ⇒ `k=4`
  algebraically impossible (`k=3` forced); on the principal `M⁴` non-scalar ⇒ `k=4` allowed (`k=n` not proven).
  **ADDITION 2:** cusp orders `{n−1,n+1,2n}`; the `ord−1` formula TESTED-NEGATIVE. SL(3) parity corrected to
  `(t−1)(t−det N)`. Opens two leads (`speculations/S022` peripheral ℤ/4 + `TWO_SYMMETRY_FRAME`); `s_n↔c` DEAD.
- **The Final Computation Arc — B108/B109/B110 (2026-06-07, Ledger V95–V97; no physics).** **B108 (V95):** the
  top-priority `θ=−w₀ → c` derivation — the mandatory **hinge fails**; `θ` is an involution (order 2) and predicts
  the order-`≤2` Dehn-filling scalars `c∈{1,−1}` but **not** the order-4 secondary `c=i`, so degree=rank's `c`
  stays **OPEN** (missing a `ℤ/4` ingredient; cusp-spectrum candidate, B95). `θ` *is* confirmed a tower symmetry
  (`[P,J(m)]=0`). **B109 (V96):** the trace-map dynamics at the void (D2) — verify-don't-trust corrected the
  handoff's coordinate-axis facts to the rigorous linearization (`DT₁²` eigenvalues `{1,φ⁴,φ⁻⁴}`; the void's
  center manifold = the tower's root-of-unity parity sector, dim 1@SL2/2@SL3; a (2,1) `κ` saddle) + L5 literature
  (degree=rank `Mⁿ=L` apparently new; the `W₄` anchor real but generic). **B110 (V97):** the off-locus irreducible
  sector of `4₁` at SL(3) is **EMPTY** (HMP's three components all on the forced locus); the higher-rank fork stays
  open. Plus the **dead-ends register** (`docs/atlas/FAILURE_ATLAS.md`: ~30 kills by pattern, REVIVABLE lens) and
  probe updates **S001** (all-`m` amphichiral PROVED), **S006** (Bell → TESTED-NEGATIVE).
- **B107 physics-connection audit — banked as a NEGATIVE (2026-06-07, Ledger V94; POSTULATED/FIREWALLED).**
  Banks the CC-web physics exploration as a first-class **dead-end log**; *all* physical readings are
  **POSTULATED and firewalled** to `speculations/archive/PHYSICS_RESONANCES.md` (Path 8), **nothing to
  `CLAIMS.md`**, the physics chapter stays **CLOSED**, P1–P16 untouched. **A (anchor, verified):** the SL(2)
  metallic trace map `φ_m: a→aᵐb, b→a` **is** the Kohmoto–Kadanoff–Tang / Fibonacci-Hamiltonian trace map —
  `tr[A,B]=x²+y²+z²−xyz−2` (Sütő/Fricke–Vogt) conserved ∀m (symbolic m=1..4), `φ_1=(z,x,xz−y)`. **B (the
  headline negative, verified):** every SL(3) `m=1` tower eigenvalue is `±φᵏ` — **one geometric scale `log φ`**;
  a mass spectrum is a Hessian, not one ratio, so the tower is **re-presented moduli-space monodromy, not new
  physics**. **C:** the tower/torsion `=` masses/dimensions identifications are **withdrawn category errors**
  (only the moduli-space `M_SUSY ≅ M_flat` + three-branch ↔ three-fixed-point map is citable). **D:** citations
  confirmed (GKLP 1305.0937; DGG 1108.4389, 1112.5179). **E:** the one open fork = the off-principal
  multichannel reps. Reproduced (`quasicrystal_anchor`, `tower_roots_are_golden`); locking test; FINDINGS A–E.
- **B106 Dehn-filling anatomy + hygiene (2026-06-07, Ledger V92/V93; no physics).** The trace map at the
  never-computed **third** fixed-point class (Dehn-filling reps, after trivial=tower and geometric=torsion).
  **D1:** three classes, three distinct Jacobian signatures — Dehn-filling **partially elliptic** (SL(3)
  `(1,1,6)`, SL(4) `(4,4,7)`, root-of-unity neutral eigenvalues); honest negative — the stability *type* does
  not encode the degree=rank exponent. **D4:** `Lᵢ=c·Mᵢ^k` per eigenvector (`c` a root of unity). **D3:** `M⁴=L`
  / `M³=L`, conjugates absent. **[V93 hygiene]** the D1 root-of-unity values pass the **B84 gauge-noise gate**
  (seed-stable); the D4 **principal** (`c=−1`) **corroborates** the proved B89/B83 (not new), the new content
  being the **secondary** (`c=i`, numerical), **SL(3) W2**, and the **per-eigenvector method**.
- **B105 three-obstacle correction + sharpened ρ_n target (2026-06-07, Ledger V91; no physics).** A further
  explicit downgrade of B105's "one collision is the common root cause": **n=5 is a structural threshold
  where three *distinct* `A_{n−1}` obstacles degenerate** — degree=rank (B95, eigenvalue `−1`, `A²=I`), the
  tower/eps-series doubling (B62, golden `char(M²)²` from the A₄ height-2 `θ=−w₀` (4,2) split), and trace-ring
  non-closure (engine-free, onset n=4) — different eigenvalues (`−1` vs `φ²`), independent derivations,
  different onset. The open `ρ_n` target is **sharpened**: prove `char(ρ_n)=catalog` by reproducing the
  opposition-involution multiplicities directly from `ρ_n`, the contested n=5 piece being *only* B62's
  `char(M²)²` (the degree=rank `−1` and trace-ring non-closure are separate, untouched problems). The n=4
  scope claim is hedged. Verified (`three_obstacle_distinction()`); banked in B105 (`CORRECTIONS_V91`).
- **The n=5 wall + the ρ_n convergence, with the V90 audit (2026-06-07, Ledger V89 + V90; suite 278+ pass, 1
  skip; no physics).** `frontier/B105_n5_wall_and_convergence/`: the "n=5 Resolution" handoff, then **two
  explicit inference downgrades (V90)**. **N5:** the SL(5) eps-series resolves **21/24** Dickson factors, the
  resolved 21 are **universally catalog-consistent** (across seeds and monodromies); the 3 unresolved are
  supported as `Sym²` by **structural routes** (B62/B89-T/B103). **[V90 Correction A]** the seed-variation of
  the 3 unresolved factors is the eps-series rank-deficiency signature (B84), **uninformative** about the
  truth — so the explicit **n=5 catalog is OPEN** and a structural deviation there is neither ruled in nor
  out (the earlier "coordinate artifact, not structural / formula-doesn't-change" inference is **withdrawn**).
  **[V90 Correction B]** there is **no proved "natural boundary at n=4"** — `char(J(n))=catalog` is a class
  function for **all `n`** (B103); n=4 is a *methodological ceiling*, not a theorem (the earlier "complete at
  n=4 with a proved boundary" is **withdrawn**); the cusp collision is a *candidate* root cause. **Convergence
  + open frontier:** the project converges on one object `ρ_n` (the `GL(2,ℤ)`-rep on the SL(n) trace ring),
  fully characterized n=3,4, **explicit n≥5 OPEN** — the live target being to prove `char(ρ_n)=catalog`
  directly from `ρ_n` + B62's multiplicities. Literature L1 (GKLP 1305.0937) + L4 (Bonahon–Dreyer 1209.3526 /
  Douglas–Sun 2011.01768) cited; H1–H6 / C1–C4 tabulated; physics quarantined.
- **The Dehn-twist route: SL(4) universality + the SL(5) wall (2026-06-07, Ledger V88; suite 274 passed, 1
  skip; no physics).** `frontier/B104_dehn_twist_tower/`: executes the "Dehn-Twist Route" handoff in full —
  build any monodromy's trace map by composing the elementary twists `U,L,S` inside the eps-series (not the
  Procesi ring, the B85 wall). **SL(4) (proven):** the GATE reproduces B80's metallic tower; `J` factors
  through `N`; `char(J(N))` = the two-sequence catalog with **det-sign parity** for **metallic and
  non-metallic** `N` (e.g. `U²L=[[3,2],[1,1]]`, det +1) — the explicit SL(4) catalog is a computed theorem.
  **SL(5):** the engine inherits the eps-series gauge degeneracy (`char(J)≠catalog`, **21/24 Dickson factors
  resolve**, the doubly-degenerate sector, B61/B66) — a **computational** wall, not a rep-theory failure; the
  n≥5 obstruction is isolated to the eps-series degeneracy. Cite B103, B80, B61/B66, Lawton/Procesi.
- **The SL(n) tower as a GL(2,ℤ) representation (2026-06-07, Ledger V87; suite 269 passed, 1 skip; proven
  core P1–P16 untouched; no physics).** `frontier/B103_tower_equivariance/`: a **fourth route** to the
  metallic tower, synthesizing two CC-web handoffs. **Route 1 (universality, all n):** `J_φ(n)` factors
  through the abelianization `N ∈ GL(2,ℤ)` ⇒ `ρ_n` is a `GL(2,ℤ)`-rep ⇒ `char(J)` is a **class function =
  the catalog**, universal for metallic **and non-metallic** monodromies; **det-sign parity** sharpens B94
  (verified at SL(3) via the exact Lawton maps `U,L,S`). **Route 2 (n=3,4 exact over ℚ[m]):** an explicit
  `m`-independent invertible `P` with **`P·J(m)·P⁻¹ = ⊕_d Sym^d(M_m)^{μ_d}`** (intertwiner dim `=Σμ_d²`
  Schur), realizing the module-iso **(M)** constructively + exactly for n=3,4; sign sectors = `det=−1` twists.
  **Reframing:** the all-n tower = **decompose the `GL(2,ℤ)`-rep `ρ_n`**; universality structural (all n),
  explicit `μ_d` open n≥5 (the Procesi wall) — continuation B104. Cite B94, B85/B89-T, B80, Lawton, Procesi.
- **The W1/W2 dichotomy + the R4 boundary-controlled cubic continuation (2026-06-06, Ledger V86; suite 263
  passed, 1 skip; proven core P1–P16 untouched; no physics).** `frontier/B102_hitchin_continuation/`: two
  follow-ons to B101, verified before landing. **D1:** Cayley–Hamilton on `T₁²` forces every irreducible
  `Fix(T₁²)` SL(3) character into Case I (`trA=trA⁻¹`, self-dual) or the `trB=trB⁻¹=1` branch (0 "neither").
  **D2/D3:** realizing B71's components, **W1→`ρ(a)` elliptic `{1,i,−i}`, W2→`ρ(b)` elliptic** ⇒ **not
  Hitchin** (the genuine non-`Sym²` components are excluded by **ellipticity**, the cleaner obstruction; V0's
  geometric rep by complexity, `Q(√−3)`). **D4:** the `{1,i,−i}` spectrum = Task M's `n=3` spectrum (B95).
  **D5:** the boundary-controlled cubic family keeps the cusp real **only to first order** — generic
  second-order complexification; the handoff's `t*≈3.775` geodesic boundary does **not** reproduce
  (ray-dependent); the unipotent-preserving continuation is `open`. Cite Heusener–Muñoz–Porti, Labourie,
  Hitchin/Fock–Goncharov/Goldman/Marquis.
- **The Hitchin-component reframing (2026-06-06, Ledger V85; suite 256 passed, 1 skip; proven core P1–P16
  untouched; physics chapter stays CLOSED; physics chain firewalled).** `frontier/B101_hitchin_reframing/`:
  the geometric component V0 (B71, `Sym²` of the Fuchsian `SL(2,ℝ)` rep) **is the Fuchsian locus of the
  `SL(3,ℝ)` Hitchin / Fock–Goncharov positive component** of the once-punctured torus. **R1** (`STRUCTURAL`):
  the Anosov hallmark + the unique `SO(2,1)` form, signature `(2,1)`. **R2** (`dead`): the symmetric-space
  ladder — the principal `SL(2)` lands in split real forms; Lorentzian only at `k=2`, does not climb ⇒ **no
  tower of spacetimes** (kills the "3+1D at SL(3)" idea structurally). **R3**: `sl(3)=V₂⊕V₄`; `V0={cubic=0}`.
  **R4** (genuinely-new): `H¹(F₂,sl(3)_Ad)=8` splits `3⊕5` (Teichmüller ⊕ cubic) + an explicit Anosov
  deformation leaving V0 and breaking the `SO(2,1)` form. The Hitchin→Higgs→geometric-Langlands→N=4 SYM
  chain (Kapustin–Witten) is **cited context only** (`PHYSICS_RESONANCES.md` Path 7) with the ceiling stated
  (N=4 SYM, *not* the Standard Model / gravity / the universe); three dead-thread heuristics recorded in
  `docs/atlas/FAILURE_ATLAS.md`.
- **Geometry-invariants + literature-bridge pass (2026-06-06, Ledger V80–V84; suite 249 passed, 1 skip;
  proven core P1–P16 untouched; physics chapter stays CLOSED; physics interpretation quarantined).**
  "Compute the numbers, quarantine the interpretation" — bounded quantum-topology invariants on the
  metallic mapping-torus manifolds, banked as mathematics; every physics reading lives only in
  `speculations/archive/PHYSICS_RESONANCES.md` (`SPECULATION`, never promoted).
  `frontier/B96_geometry_invariants/` (V80): metallic volumes strictly monotone (`2.030<3.664<4.814`,
  `m=1`=systole); the volume Hessian is **definite `(0,2)`, NOT Lorentzian** (155/156 fillings of `4_1`
  below `V₀`) — the most-leveraged physics path returns negative.
  `frontier/B97_sl2r_lorentzian/` (V81): the `(2,1)` Lorentzian form is **located** as the
  `so(2,1)=sl(2,ℝ)` gauge algebra on the SL(2,ℝ)/Teichmüller component (toy 2+1 gravity) — structural, not
  emergent; the 3+1 wall untouched.
  `frontier/B98_geometric_jacobian/` (Probe 1, V82): at the **geometric** rep (not the trivial fixed line),
  `char(D T₁²)=(t−1)(t²−5t+1)` = the **adjoint torsion `τ₁=−3`** (twisted Alexander), **NOT** the Dickson
  tower — so the tower is a trivial-rep phenomenon (*consistent with* Daly arXiv:2411.04431 + 3d-3d, cited);
  tower ≠ Kostant branching.
  `frontier/B99_geometric_jacobian_sl3/` (Probe 1c, V83): the SL(3) geometric Jacobian is torsion-type
  (the `c=5` SL(2) torsion pair carried by `Sym²`), not the SL(3) tower.
  `frontier/B100_literature_crosscheck/` (Probes 2+6, V84): the Zickert/SnapPy **Ptolemy variety** of `4_1`
  (2 obstruction classes, 6 trivial-class reps) cross-validates B71 from an independent code path, and the
  **Baker–Petersen** (arXiv:1211.4479) twisted Alexander **is** the B98/B99 geometric Jacobian — two
  published frameworks agree (methods cited, not claimed).
- **Task M — the degree=rank mechanism (2026-06-06, Ledger V79; suite green; P1–P16 untouched).**
  `frontier/B95_degree_rank_mechanism/`: the V75 audit killed "exponent = Cayley–Hamilton degree"; B95
  finds what the exponent reads. The principal spectrum is **forced** by `tr A=tr A⁻¹=1` ({1,i,−i},
  {1,1,ω,ω²}, {1,1,1,−1,−1}, impossible n≥6); at n=5 it degenerates (`A²=I` → dihedral → reducible, no
  irreducible SL(5) principal rep — upgrades B78). So **"exponent = rank" is an n∈{3,4} phenomenon**; the
  mechanism reads the cusp's forced finite-order spectrum, explaining the n≥5 wall on both the tower and
  degree=rank. Corrects the handoff's SL(5) spectrum guess.
- **Paper 0 — the self-reference grounding (2026-06-06, Ledger V76–V78; suite 230 passed, 1 skip;
  proven core P1–P16 untouched; philosophy quarantined).** A foundational thread characterizing the
  metallic family by a condition (`m` free). `philosophy/METALLIC_FOUNDATIONS.md` (quarantined
  motivation, never a claim). `frontier/B92_metallic_classification/` (Layer 1, V76, `proven`): the family
  = the `det=−1`/period-1 slice up to `GL(2,ℤ)` conjugacy (entries ≤5), with MyCalc-2 (conjugacy census)
  and MyCalc-5 (systole/contingency). `frontier/B93_det_parity_bridge/` (Phase C, V77): MyCalc-1
  (`det=−1 ⟺` the tower's parity sectors) and MyCalc-4 (parity ≠ Galois — refines the handoff).
  `frontier/B94_tower_universality/` (G1, V78): **"universal catalog, det=−1 parity"** — the Dickson
  catalog survives any `GL(2,ℤ)` monodromy but the sign/parity sectors are `det=−1`-specific (so `det=−1`
  is structurally distinguished); degree=rank is det-agnostic (two problems).
- **Audit correction (2026-06-05, Ledger V75).** Corrected B90's framing: L1a is a tautology and
  "exponent = rank from Cayley–Hamilton" is refuted (the hinge test); only L1b is genuine. Strengthened
  B89-T with the J(m) cross-check against B80.
- **"Complete the Tower" run (2026-06-05, Ledger V70–V74; suite 220 passed, 1 skip; proven core
  P1–P16 untouched; `EXPERT_OUTREACH.md` dormant).** The CC-web handoff reconciled against `main` and
  the genuine open prizes executed:
  `frontier/B87_m3_genus/` (Task 3, V70) the m=3 spectral-curve genus — sequence `3,1,…`, m=2 a minimum
  (the `3,1,0` reading refuted), m=3 trace-relation curve genus 1;
  `frontier/B88_sl4_census/` (Task 2, V71) the SL(4) Dehn-filling census — **degrees {3,4}**, two
  components (`{1,1,ω,ω²}→M⁴=L`, `{prim 8th}→M³=L`);
  `frontier/B89_sl4_symbolic_M4L/` (Task 1a, V72) **`M⁴=L` PROVED symbolic-exact at SL(4)** over ℚ(ω)
  (upgrades V54 from ~1e-31), via the 10-equation exact ideal + the rank-drop-locus family;
  `frontier/B89T_tower_route/` (Task T, V73) the tower's **cohomological route closed** (a 3rd dead
  shortcut) + the explicit two-sequence **Sym-product** reduction (symbolic-in-m, proved n≤4) to one
  module-isomorphism;
  `frontier/B90_degree_rank_peripheral/` (Task 1b, V74) degree=rank's **uniform peripheral reduction** —
  Lemma 1 (`λ=μX⁻¹μY⁻¹`, `XμX⁻¹=μA`) proved uniformly; reduced to one collapse-lemma, exponent = rank
  from A's degree-n Cayley–Hamilton.
  Net: both flagships (the tower, degree=rank) reduced to one clean lemma each with n≤4 proved; the
  cohomological route closed. Open: Task 6 (genus-2 generality).
- **Comprehensive Paths A–F mandate (2026-06-05, Ledger V53–V59; suite 179 passed, 1 skip; proven
  core P1–P16 untouched).** Two prizes + a fully-labeled speculative tail:
  `frontier/B73_sl4_apoly/` (Path A, V54) the **degree=rank tower law** `Mⁿ=L` on the principal
  Dehn-filling component, confirmed at SL(4) (~1e-39);
  `frontier/B70_trace_ring/symbolic_m_pinv.py` (Path D, V55) the symbolic-m ε-series pinv-limit
  construction, reproducing the SL(3) tower from first principles;
  `frontier/physics_probes/spectral_curve_coulomb_test.py` (Path B, V53) confirms the j=1728 kill;
  `frontier/B74_higher_spin_grading/` (Path C, V56) the W_N parity grading = `−w0` of `A_{n−1}`
  (STRUCTURAL), spectrum diverges, dynamics SPECULATIVE-ANALOGY;
  `frontier/B75_metallic_degree_rank/` (Path F1, V57) the **m-axis** of degree=rank (odd metallic
  bundles m=1,3 give `M³=L`; convention-independent `eig[A,B]=eig(t)ⁿ`);
  `frontier/B76_cusp_quantum_group/` (Path F2/F3, V58) cusp k-set = SU(2)_{k−2} root-of-unity level
  set (closes B69), no categorical family lift (SPECULATIVE-ANALOGY);
  `frontier/B68_aj_conjecture/cyclotomic_numeric.py` (Path E, V59) confirms the V52 AJ bounded negative.
- **Open-paths sweep (2026-06-05, Ledger V43–V52).** `frontier/B71_sl3_apoly/` the SL(3) figure-eight
  A-variety (Fix(T_1²) = 3 components, matches Heusener–Muñoz–Porti / Falbel; `W1=D2→M³=L`,
  `W2=D3→M³L=1`); P1 Dehn-filling exact; P3 m=2 framing = m136; P4 rank-independent meridian; P5
  trace-ring scoping; P6 AJ bounded-negative.
- Full audit of all prior work: `AUDIT_REPORT.md`, `PROVENANCE.md`.
- Phase 0 governance scaffolding: `GOVERNANCE.md`, `CLAIMS.md`, `README.md`, `ROADMAP.md`,
  `PROGRESS_LOG.md`, this changelog, `REPRODUCIBILITY.md`, `docs/ARCHIVE.md`, `.gitignore`.
- Claims ledger established: 10 `proven`, 4 `conditional`, 9 `open`, 10 `dead`.
- `legacy/` — prior history consolidated: curated text under `legacy/reports/`,
  `legacy/handoff/`, with the ~4 GB raw archive git-ignored under `legacy/raw/`.
- Phase A: the `origin_axiom` package (`src/`) and `tests/` suite locking every
  `proven` claim P1–P10 — 33 passing tests. Packaging via `pyproject.toml`.
- Session-3 integration: claims P11–P13 promoted to the proven core (exact-algebra
  results — sl(2) decomposition of `log A`, gluing-equation factorization,
  isospectrality), with tests (suite now 39 passing). Frontier probes B4
  (BKL/Gutzwiller) and B5 (Wheeler-DeWitt) added as logged observations.
- **Phase C kickoff** — `paths/` directory created: 25-path registry (20
  mathematizable E1–E20 across 11 mechanism classes; 5 philosophical P1–P5 in a
  separate register). The project's goal becomes *exhaustively surveying* the
  mechanisms by which "nothing being unstable" could produce reality, with the
  *map of attempted paths* as the deliverable. First batch selected: E14, E11, E5.
- **Session-3 synthesis** — the 2025 field-theory line reconnected to the algebraic
  skeleton. Claims **P15** (Möbius generating vector field `v(τ)=−κ(τ²−τ−1)`) and
  **P16** (derived potential `V(τ)=κ(τ³/3−τ²/2−τ)`) promoted to the proven core as
  exact algebra about A, with tests (`src/origin_axiom/mobius.py`,
  `tests/test_mobius_vector_field.py`, `tests/test_derived_potential.py`). Frontier
  probes **B6–B9** added (field equation, Fisher–KPP creation, particle spectrum
  with the non-exact `m/g≈φ` near-miss, fusion–scattering shared polynomial), each
  with caveats. Synthesis doc + scripts under `docs/SESSION3_SYNTHESIS.md` and
  `scripts/`. Four Oct-2025 genesis documents filed under `legacy/reports/genesis/`
  (historical only). Ledger: **15 `proven`**, 4 `conditional`, 9 `open`, 10 `dead`.
- Roadmap integration started with `docs/atlas/INTEGRATION_MANIFEST.md`, a
  public-safe manifest for migrating atlas, paper-candidate, campaign-synthesis,
  and review-packet material from private staging into the canonical repository.
- Research Atlas skeleton added under `docs/atlas/`: auditor guide, research
  tree, failure atlas, success atlas, glossary, and simulator ecosystem map. This
  is a navigation layer only; governed claims remain in `CLAIMS.md`.
- Paper-candidate registry added under `papers/`: candidate index, artifact
  manifest, and first paper cards for conditional uniqueness, noncommutative
  residue, and the quantum selector / state-integral bridge problem.
- Quantum selector campaign summarized under `docs/atlas/campaigns/`: public-safe
  synthesis of the 232-cycle run, preserving verdict counts, survivors, killed
  routes, stalled bridge classes, and theorem questions without raw run artifacts.
- PC02 validation packet added, giving readers a concise audit path for
  the conditional uniqueness theorem, its tests, caveats, and missing topology
  lemma.
- Noncommutative cancellation residue dossier added as an atlas node, with the
  PC04 paper card updated to point at canonical atlas evidence and the campaign
  synthesis.
- State-integral selector-gap dossier added as an atlas node, with the PC06 paper
  card updated to frame the route as an expertise-bound theorem question rather
  than a solved bridge.
- Atlas/paper integration roadmap closed through R7: manifest now marks R0-R6
  complete and records the final QA, merge, and tag gate for
  `atlas-paper-integration-v1`.
- Post-merge manifest cleanup: R7 marked complete after merge/tag, and stale
  closure wording removed. Existing `atlas-paper-integration-v1` tag left
  unchanged.
- PC02 paper-support lemma added: mapping-torus homology/torsion proof for the
  conditional uniqueness theorem, with PC02 paper card and review packet updated
  for external mathematical review.
- PC02 validation brief added, and PC02 readiness advanced from
  `EVIDENCE_EXISTS` to `NEEDS_VALIDATION` pending independent mathematical
  validation.
- Conditional uniqueness theorem formalized: `docs/UNIQUENESS_THEOREM.md` and
  `tests/test_uniqueness_theorem.py` lock the machine-checked algebra
  `A1-A7 -> A=LR` up to order, while keeping C1 conditional.
- Trace-map character-variety frontier campaign B13-B25 added. B18 establishes
  the canonical half-step trace lift; B22 kills the special parity narrative
  while preserving the special `A` quadratic sector; B25 records the Fibonacci
  spectrum at dimensionless `lambda/h=1` as a finite-approximant numerical
  anchor, initially classified as motivated, not derived. No claims promoted.
- Trace selector package added: B26-B47 refine the `lambda/h=1` selector, and
  `docs/TRACE_SELECTOR_THEOREM.md` formalizes conditional claim C5:
  `T1 -> S1 -> I=1/4 -> lambda/h=1`. The selector is conditional on T1, not
  proven or physical.
- PC11 validation packet added, plus `papers/REVIEWABILITY_INDEX.md` routing
  PC02 and PC11 through reviewability and falsifiability checks. PC11 readiness
  advances to `NEEDS_VALIDATION`, pending independent validation of T1.
- Reviewability/falsifiability workflow added: `papers/VALIDATION_WORKFLOW.md`,
  `papers/VALIDATION_LEDGER.md`, PC02 `REVIEWABILITY_CHECKLIST.md`, and
  validation briefs replace communication-oriented artifacts. No person-specific
  names or private correspondence are tracked in the repo.
- Falsifiability matrix added: `papers/FALSIFIABILITY_MATRIX.md` maps PC02,
  PC04, PC06, PC07, and PC11 to missing objects, validation questions, and
  kill/rescope conditions. PC07 now has a paper card, and public-surface hygiene
  is covered by `tests/test_public_surface_scan.py`.
- Metallic `SL(3)` trace-map intake added: B48 generalizes the B27 `m=1`
  Fibonacci trace lift to the family `a -> a^m b, b -> a`; PC12 now tracks the
  standalone arithmetic candidate with certificate-backed fixed-line controls.
  Raw side-work bundles remain private and are not copied into the repo.
- B49 proof-hardening added for PC12: the fixed-line splitting classification is
  decomposed into a universal splitting criterion, direct split families,
  square-gap propagation, finite strip exclusions, and negative boundary
  controls. PC12 remains `NEEDS_VALIDATION`.
- B50 proof-draft assembly added for PC12: B48/B49 are organized into an
  internal theorem-note skeleton with explicit theorem blocks, reproduction
  commands, non-claims, and draftability gates. PC12 remains `NEEDS_VALIDATION`.
- B51 symbolic-`m` proof module added for PC12: the `c=3` fixed-line Jacobian
  factorization is now verified with `m` formal, via closed-form derivative
  sequences and exchange block diagonalization.
- B52 multichannel Fibonacci bridge control added: the simplest three-channel
  tight-binding model gives `6x6` symplectic transfer matrices and fails the
  PC12 third-order `SL(3)` trace recursion, keeping PC12 mathematical.
- B53 literature screen completed for PC12 (`LITERATURE_POSITIONING.md`): the
  trace-map formula, commutator invariant, entropy, exchange decomposition, and
  symbolic factorization are `STANDARD_REPACKAGE` (Lawton; Baake-Grimm-Roberts;
  Bellon-Viallet); only the fixed-line splitting (Thm 4) is `APPARENTLY_NEW` and
  elementary. PC12 rescaled `THEOREM_NOTE` -> `COMPUTATIONAL_REPORT` (still
  `NEEDS_VALIDATION`).
- B54 general-`c` exchange structure added (`frontier/B54_general_c_exchange_structure/`):
  `[J(m,c),P]=0` proved for symbolic `c` (exchange block-diagonalization on the
  whole fixed line, generalizing B51), with the `c=1` Eisenstein/golden twin
  polynomials (disc -3, 5) echoing P12 and the `m=1` cyclotomic sweep.
- Phase-C path E21 added (`paths/E21_self_evidencing_closure/`): the
  self-evidencing / variational-free-energy framing of `lambda=m` is quarantined
  with verdict `STALLED` (structural analogy only; the exact fact is the single
  identity `4c^2-2=m^2+2`; predicts no observable). Kept out of PC12.
- PC02 draft note reconciled: the formal theorem-note structure (axiom table
  A1-A7, mapping-torus torsion lemma via the Wang sequence, the LR/RL
  based-invariant table, explicit theorem + proof) becomes the canonical
  `papers/candidates/PC02_conditional_uniqueness/DRAFT_NOTE.md`, replacing the
  earlier review-brief draft; the half-step / trace-map / conditional
  spectral-anchor material is retained as a clearly-marked non-theorem appendix.
  Editorial consolidation; PC02 stays `CONDITIONAL_THEOREM` / `NEEDS_VALIDATION`.
- B55 c=1 general-m structure added (`frontier/B55_c1_fixed_line_structure/`):
  the c=1 fixed-line symmetric sector is classified **mod 4** (`Φ₆` for m≡1,3;
  `Φ₄` for m≡2; degenerate `(t−1)²` for m≡0) and the antisymmetric sector is
  `(t−1)(t+1)(t²−mt−1) = char(M)` for all m, proved per residue class. Corrects
  the earlier odd/even reading and completes B54's c=1 row.
- B56 figure-eight invariant-surface negative control added
  (`frontier/B56_figure_eight_invariant_surface/`): the diagonal SL(2,C) reps
  have `I ∈ {4, −17/2 ± 7√5/2}`, none `= 1/4`; the figure-eight ↔ `I=1/4` bridge
  is `DEAD` and the c=1 Eisenstein resemblance is a cyclotomic coincidence. The
  P12 gluing-equation discriminant echo is unaffected.
- B57 general-m Diophantine splitting classification added
  (`frontier/B57_general_m_splitting/`): `{c=1, c=3}` are universal splitting
  points; m-dependent extras classified for m=1..6; the Hilbert-class-field
  coincidence (`h(−15)=2`) is killed for m≥2. Extends PC12's Theorem-4 content.
- E21 self-evidencing controls added (`paths/E21_self_evidencing_closure/`): two
  further session results, integrated as quarantine controls. (i) The Fisher
  information of `D(I)` equals `16/disc(char(M²)) = 16·g_WP(m²+2)` (a
  Goldman/Weil–Petersson coefficient) — exact but a chain-rule identity, geometric
  reading not promoted. (ii) Aubry self-duality at `λ=m` is dead (`λ=m` is the
  trivial fixed point of `λ→m²/λ`; no metal–insulator observable). Both strengthen
  E21's `STALLED` verdict; the Aubry kill is recorded in
  `docs/atlas/FAILURE_ATLAS.md`.
- SL(n) factor-count tower recorded as an **untested prediction** in PC12's
  `DRAFT_NOTE_SKELETON.md`: the rank-two `SL(n,C)` Jacobian is conjectured to
  factor into a parity block plus `(n²−1−parity)/2` degree-2 `char(M^k)` factors
  (confirmed n=2,3; SL(4)→7 untested). Not a claim; a candidate future probe.
- B58 SL(4) tower test added (`frontier/B58_sl4_tower_test/`): an attempt at the
  n=4 prediction. Confirms the mechanism (SL(4) identity recursion `(r-1)^4`,
  cubic derivative sequences) and the obstruction (the fixed-line point is the
  degenerate identity representation, so a representation-based numerical Jacobian
  cannot recover the ambient map). Verdict `NEEDS-EXPERTISE`; the 7-factor
  prediction stays untested. The full `15×15` ambient SL(4,C) trace map (Procesi
  generators + substitution action) is the required next build.
- B59 SL(4) fixed-line factorization added (`frontier/B59_sl4_factorization/`):
  resolves B58 numerically (method validated on SL(3) ground truth to ~4 digits).
  The SL(4) spectrum factors as
  `char(M^-1)char(M)char(M^2)char(M^3)char(M^4) · char(-M^2) · (t-1)^2(t+1)` —
  5 clean `char(M^k)` (k=-1..4), a sign sector, and a degree-3 parity block —
  **refuting** the naive `7 char(M^k) + parity` tower prediction. Numerical, not
  a symbolic proof; no claim promoted.
- B60 SL(n) tower added (`frontier/B60_sln_tower/`): generalizes B59's method and
  builds the corrected cross-n structure map. n=3: powers `{-1,2,3}`, parity
  deg 2; n=4: powers `{-1,1,2,3,4}` + `char(-M^2)` + parity deg 3 (powers climb,
  a sign sector appears, parity grows). **SL(5) unresolved** (`cond(Dx)~1e11`;
  needs a stable high-precision SVD solver or the symbolic ambient SL(5,C) trace
  ring). Numerical, method-validated for n=3,4; no claim promoted.
- B61 SL(5) high-precision factorization added (`frontier/B61_sl5_high_precision/`):
  ports the method to mpmath (dps 60) with a stable SVD pinv, and shows B60's
  "`cond(Dx)~1e11` wall" was a **rank-23** forward-only word set (the 24th
  singular value is the dps zero-floor, mis-read as `1e11` in double precision).
  Inverse-word coordinates (`A,B,A^-1,B^-1`) restore rank 24 at `cond~1e4`, and
  **22 of 24** SL(5) multipliers resolve to the catalog:
  `char(M^-1)·char(M)^2·char(M^2)·char(M^3)·char(M^4)·char(M^5)·char(-M^2)·char(-M^3)·(t-1)^2(t+1)^2`
  (powers climb to 5, sign sectors `-2,-3`, parity deg 4 -- the n=5 tower row).
  The last 2 modes are a **method limit** (fixed-line rank-loss makes the pinv
  `eps->0` limit gauge-dependent; residual scatters across seeds), needing the
  symbolic ambient SL(5,C) ring. SL(3)/SL(4) reproduce to ~4e-14/~3e-9.
  Numerical, high-precision; no claim promoted.
- PC12 made review-ready for an external specialist: a polished, self-contained
  `DRAFT_NOTE.md` (standard blocks Sec 2-5 with citations; the apparently-new
  fixed-line splitting classification in Sec 6; the numerical cross-n tower as a
  labeled Appendix A), plus `REVIEW_PACKET.md` (five sharpened questions) and
  `REVIEWABILITY_CHECKLIST.md`, mirroring PC02. A bounded literature refresh added
  the entropy=spectral-radius citation (arXiv:0812.0853) and found no prior art
  for the Sec-6 splitting or the cross-n tower. `PAPER_CARD` readiness advanced to
  `READY_FOR_REVIEW`; ledger row V12. No claim promoted.
- B62 opposition involution (`frontier/B62_opposition_involution/`): identifies
  B61's 2 unresolved SL(5) fixed-line modes. The B61 numerics cannot decide them
  (`tr(DT0)`/`det(DT0)` scatter across seeds). Identifying the exchange involution
  with the opposition involution `theta=-w0` on the `sl(n)` root system, its
  height-2 eigenspace split is exact and reproduces SL(3) (`char(M^2)`) and SL(4)
  (`char(M^2).char(-M^2)`); for SL(5) it is `char(M^2)^2.char(-M^2)`, so the 2
  unresolved modes are a second `char(M^2)` = {phi^2, 1/phi^2} (residual modes
  positive, corroborating). Completes the SL(5) tower row (22 numerical + 2
  structural). Recorded as a **live structural result**; a symbolic proof needs
  the ambient SL(5,C) trace ring. Ledger V13. No claim promoted.
- B63 SL(4) factorization over Z[m] (`frontier/B63_sl4_symbolic_m/`): establishes
  the metallic SL(4) fixed-line factorization for general `m` and proves
  m-independence. Building the symbolic Procesi trace ring (B58) is harder than
  "one level deeper" -- `e_2(A)` forces the 6-dim `Lambda^2` representation
  (depth-6) or multi-block words `tr((A^m B)^2 A)`; documented as the real reason
  B58 is hard. Instead, SL(4) being gauge-clean, the high-precision Jacobian is
  computed for `m=1..6`, each factor's eigenvalue sum extracted (= exact
  `tr(M^k)`) and interpolated in `m`:
  `char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1)` with
  `L_2=m^2+2, L_3=m^3+3m, L_4=m^4+4m^2+2`. The M-power/sign/parity structure is
  m-INDEPENDENT; m=1 reproduces B59. Computer-assisted symbolic (not a hand-built
  trace ring); the explicit `k(alpha)` root map is supplied by B62. Ledger V14.
  No claim promoted; proven core P1-P16 unchanged.
- B64 parity mechanism (`frontier/B64_parity_mechanism/`): proves the tower's
  `k(alpha)` sector-assignment formula as exact symbolic algebra. Depth-n
  Cayley-Hamilton makes the fixed-line Jacobian polynomial in `m`; `P` is the
  contragredient (`m -> -m`); Dickson parity `L_k(-m)=(-1)^k L_k(m)`. Hence
  **even-|k| `char(M^k)` sits in the P-symmetric sector, odd-|k| in the
  P-antisymmetric** (the root-height split B62 identified). Verified in full
  symbolic-`m` form for SL(3) (symmetric=(t-1)(t+1)char(M^2), antisym=
  char(M^-1)char(M^3)); applied to SL(4)'s factorization (even-k {M^2,M^4,-M^2}
  symmetric, odd-k {M^-1,M,M^3} antisymmetric). The depth-4 derivative sequences
  are built; a full symbolic SL(4) Jacobian's one remaining need is localized to
  `e_2 = tr(Lambda^2 A)` (the 6-dim exterior square, the even-k sector). Ledger
  V15. No claim promoted; proven core P1-P16 unchanged.
- B65 symbolic SL(4) Jacobian (`frontier/B65_sl4_symbolic_jacobian/`): determines
  the full 15x15 SL(4) fixed-line Jacobian `J(m)` exactly over `Z[m]` and factors
  `char(J(m))` directly as symbolic algebra. A hand-built trace ring needs
  multi-block reductions (rank check: single-block V+`Lambda^2` traces span only
  12/15), so instead the canonical (seed-independent) degree-4-in-m entries are
  reconstructed from high-precision numerics (SL(4) is gauge-clean) for `m=1..7`,
  over-determined (degree 4 fixed by 5 points, verified on 7); `sympy.factor`
  gives
  `char(J(m))=char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1)`.
  Matches B63/B64; `m=1` reproduces B59. The factorization is now *derived*
  (direct factoring of `J(m)`), not matched -- the strongest form short of a
  hand-derived Procesi trace ring (B58, still open). Computer-assisted entries +
  exact symbolic factorization. Ledger V16. No claim promoted; proven core
  P1-P16 unchanged.
- B66 SL(6) numerical tower (`frontier/B66_sl6_tower/`): computes the `n=6` row
  (35-dim) by the inverse-word method to settle the tower multiplicity formula.
  The opposition-involution theta-split sector dims (9 odd-height + 6 even-height
  + 5 parity = 35) are exact (the 9/6 is a root-height count, = |k|-parity only
  for odd n); the |k|=3 region resolves cleanly to exactly two quadratics
  (`char(M^3)`, `char(-M^3)`), so the **|k|=3 multiplicity = 2 — refuting
  `max(n-d,1)=3`** (SL(6) is the first `n` that distinguishes 3 from 2). Honest
  limit: 26/35 resolve, 9 modes gauge-corrupted (the B62 mechanism amplified from
  SL(5)'s 2 modes). Ledger V17. Numerical, no claim promoted; proven core P1-P16
  unchanged.
- B66 validation campaign (`frontier/B66_sl6_tower/{validate,second_m,gauge}.py`,
  `VALIDATION.md`; Ledger V19): stress-tested `mult(|k|=3) = 2` four ways. The
  identical inverse-word pipeline recovers SL(3..6) = 1,1,**2**,2 (SL(5)=2 under
  the same gauge-handling, auto-selected words); m=2 and m=3 give 2 with the |k|=3
  root tracking `L_3(m)`; the |k|=3 eigenvalues are seed-stable while the 8 gauge
  modes scatter (up to 3.8) across base points. Exact-over-Q is the honest
  negative -- the numerical Jacobian is non-canonical (`||dt0(20)-dt0(24)||~7e3`),
  so the from-first-principles exact route for n>=5 remains the trace ring (B58).
- B67 figure-eight A-polynomial from the trace map (`frontier/B67_figure_eight_apolynomial/`;
  Ledger V20): the metallic SL(2,C) trace map's fixed-point set (monodromy
  `phi=[[2,1],[1,1]]=M^2`, trace map `T_1^2`) reproduces the **published Cooper-Long
  (1996) figure-eight A-polynomial exactly** -- `A(M,L)=M^4L^2+(-M^8+M^6+2M^4+M^2-1)L+M^4`.
  A fiber rep extends over the bundle iff its character is `T_1^2`-fixed, so the fixed
  locus `y=z=x/(x-1)` is the A-polynomial curve; the monodromy `t` gives meridian
  `M=eig(t)`, longitude `L=eig[B,A]`, with trace identity `tr[A,B]=tr(t)^4-5tr(t)^2+2`.
  First derivation of this A-polynomial from a trace-map computation -- an independent
  cross-check of the SL(n) tower (B59-B66). SL(3) (Garoufalidis-Thurston-Zickert) is the
  open next step. No claim promoted; proven core P1-P16 unchanged.

### Fixed
- Tower verification pass (Ledger V18). **SL(2)/n=2 parity correction:** the
  `DRAFT_NOTE.md` cross-`n` tower table listed the `n=2` parity block as `none`,
  under-counting the 3-dimensional `SL(2)` variety; the identity-fixed-point
  Jacobian is `(t+1)·char(M^2)` for all `m` (parity eigenvalue = `det(M) = -1`),
  so the block is `(t+1)` — corrected. **B66 labeling:** the `sector_prediction`
  "9 odd-k + 6 even-k" is a root-HEIGHT count, equal to the `char(M^k)` |k|-parity
  count only for odd `n` (SL(4) is |k|-parity `(3,3)` but height `(4,2)`);
  relabeled "odd/even-height" throughout B66 + Ledger V17. The B66 `|k|=3 = 2`
  result (direct root-matching) is unaffected. Both facts, plus
  `char(-M^k)=char(M^{-k})` for odd `k` only and `L_k(-m)=(-1)^k L_k(m)` through
  `L_8`, are now locked in `tests/test_b66_sl6_tower.py`.
- **CORRECTED MISCONCEPTION (B58 Stage 1, Ledger V21).** The scoping guesses that
  the cotangent dimension is `3n^2-10n+11` (=8,19,36) and the excess `2(n-2)(n-3)`
  (=0,4,12) were **never validated and are REFUTED** by the Đoković cross-check.
  Kept visible (not deleted) so they are never re-derived. Actual cotangent (d-sigma
  on `m/m^2` of the two-traceless-matrix trace algebra, modular over F_p, prime-stable):
  `9` (n=3, = Teranishi 11 GL gens − 2) and `30` (n=4, = Đoković, exact per-degree
  distribution), `>= 111` (n=5, PARTIAL lower bound). Actual excess (cotangent − the
  `n^2-1` Jacobian) = `1, 15, >= 87` — a large mixed Dickson+parity multiset, the
  *secondary* trace invariants (n=3: `det[X,Y]`). This **closes the cotangent route to
  the `a_d` multiplicities** (see FAILURE_ATLAS); `a_d` needs the exterior-power
  Cayley-Hamilton hand proof. (arXiv 2603.00816 Ishibashi-Mizuno confirmed real by
  independent search; Kozai 1509.07487 and 2411.04431 pre-2026, fetched.)
  *Forward guard:* no entropy/"spectral-weight" probe was produced; if one is ever
  added, note that it computes `Σ|k|` spectral weight, NOT topological entropy
  (= `n·log μ`, linear) — no `n^2` scaling, no fixed "antisymmetric fraction".

### Added
- B58 Stage 1 (`frontier/B58_stage1/`): the modular-F_p cotangent computation and the
  Sym^{2k}/Kostant diagnostic (Step 2: bare = even-only/overshoot, coupled = odd-only,
  neither = tower — B64's parity split is a sorting, not a formula). Tests in
  `tests/test_b58_stage1.py`.
- Overnight exploratory queue (`frontier/overnight_2026-06-03/`, Ledger V22/V23):
  Job 1 time-reversal = Jacobian-level Dickson parity (corollary); Job 4 SL(7) partial
  (constraints, char(M^3)=a_3=1 at n=7, INCONCLUSIVE); Job 2 SL(3) A-poly Sym^2 NO-GO
  (geometric component is boundary-unipotent/GTZ); Job 3 cross-m m=2 = census m136,
  framing OPEN; Job 5 skipped (gate). Job 6 AJ (`frontier/B68_aj_conjecture/`,
  `frontier/aj_conjecture_check.json`): shelved, NOT promoted (order-2 recursion match
  is below B67's exact-identity bar; q=1 limit unresolved). Literature review in
  `frontier/literature_search.md` (principal-SL(2) / adjoint-torsion / Kozai framing).
- B58 Phase A (`frontier/B58_phaseA/`, Ledger V24–V26): an EXACT `(n^2-1)` fixed-line Jacobian
  engine (`jacobian_closure.py`; eps-series dual numbers over F_p; the least-squares form of
  B66's pinv limit). VALIDATED at n=4 — reproduces B65's `a_d=(1,1,1,1)` exactly, prime-stable.
- Candidate general-`n` `a_d` formula recorded (`frontier/B58_phaseA/CANDIDATE_A_D.md`): the
  opposition-involution θ-split, `a_h=⌈(n-h)/2⌉`, `b_h=⌊(n-h)/2⌋` for `h=2..n-1`, plus an
  OBSERVED height-1/wrap piece (`char(M^1)^{n-3}·char(M^-1)·char(M^n)`) and parity. Reproduces
  the n=3,4,5 towers EXACTLY (integer-valid + dimension-sum `=n^2-1`, n=3..7). **CONJECTURED —
  unproven (needs the trace-ring identification, B58) and incomplete (height-1/wrap observed).**
- B62 proof status clarified (`frontier/B58_phaseA/B62_STATUS.md`): State 3 for the full `a_d`,
  State 2 (verified candidate) for height-2 only; θ-eigenspace dims are exact Lie theory, the
  identification with the Jacobian is unproven.
- **Phase-8 physics-paths sweep (`frontier/physics_probes/`, Ledger V28–V39): robustly negative.**
  A systematic probe of every reachable physics anchor. Headline: real mathematics, **no crossing
  into fundamental or new-quantum physics** — every anchor is special to `n=2`/`m=1`. Metallic
  anyons (V28, closed: categorifiable only at `m=1`, Ostrik rank-2) and SL(n) quasicrystal spectra
  (V29, closed: the symplectic obstruction, `SL(n)=Sp` only at `n=2`) both negative; Chern–Simons
  torsion family (V30, no pattern) with `τ_m` identified as **Porti's adjoint Reidemeister torsion
  form** (V31). The `m136`/`m=2` A-polynomial framing is **RESOLVED** — the m=2 trace-map eliminant
  `M²L²−(M⁴−4M²+1)L+M²` IS census-m136, confirmed by holonomy-match (V32) and an independent
  from-scratch null-space-dim-1 fit (V38). Consolidated in `PHYSICS_PROBES_SUMMARY.md`.
- B69 metallic A-polynomial family + cusp-torsion law (`frontier/B69_metallic_apoly_family/`, Ledger
  V35/V39/V40): VERIFIED m=1..4; cusps at elliptic-torsion `x=2cos(π/k)`. **Novelty: STANDARD_REPACKAGE**
  — the cusp law is the known Baker–Petersen once-punctured-torus-bundle ideal-point structure
  (arXiv:1211.4479), not new.
- B70 trace-ring attack on `a_d` (`frontier/B70_trace_ring/`, Ledger V41/V42): the SL(n) two-block /
  `e₂=tr(Λ²A)` obstruction is **rank-1 at leading order** (pinned exactly to `e₂`; verified SL(4),SL(5)
  on the traceless `sl(n)` tangent), and its full closure is a **bounded, finite multi-generator** set
  (bidegree `≤(3,3)` by `c=n` nilpotency). The two-block barrier is now a precise finite structure —
  computer-assisted characterization, **not PROVEN**. The `SL(3)` GTZ A-polynomial (Track B) is the
  deferred more-tractable follow-on.

### Changed
- **REFUTED (kept visible as honest history): the exact-`Q` "field fix" hypothesis for the n=5
  `a_2` shortfall.** The shortfall is the pinv-limit CONSTRUCTION, not the field/metric — three
  realizations (F_p random metric; F_p `S=I`, prime-stable `= Q` mod `p`; real positive-definite
  mpmath) all return `a_2=1` where the truth is `2`. The `eps->0` least-squares limit is
  non-canonical at the degenerate `char(M^2)^2/(t+1)^2` collision (defective non-Dickson cubic).
  So the pinv / ambient-Jacobian route (B59–B66 + the Phase A engine) **under-counts degenerate
  multiplicities** — *wrong* from n=5, not merely ceilinged at n=6 (FAILURE_ATLAS, sharpened).
- `b_d=[d<=n-2]` DOWNGRADED: an n<=5 match only — it diverges from the θ-split at n=6 (`b_2`:
  1 vs 2). OPEN for n>=6.
- `a_3(n=6)` is now OPEN (Ledger V17 annotated): B66's numerical `1` is understood as the pinv
  under-count at a degenerate collision; the θ-split candidate predicts `2` (better-supported,
  not asserted).
- Strategic state: the pinv / ambient-Jacobian route is EXHAUSTED as a path to *degenerate*
  `a_d`; the B58 trace ring (structural form + identification proof) is the sole remaining route
  that both computes and proves it. The fork — bank the candidate + finding as a written result
  vs commit to the multi-session B58 trace-ring proof — is DEFERRED (human decision).

### Changed
- Project framing locked to the disciplined V4 / Reality-Check line; the optimistic
  `handoff.md` framing demoted to historical record.

### Notes
- This repository consolidates four prior GitHub repositories and the May-2026 session
  archive into a single canonical home.
- The four prior repositories (`origin-axiom-framework`, `origin-axiom-theta-star`,
  `origin-axiom-obstruction`, `00_origin-axiom`) have been archived read-only with
  "superseded by" pointers. They are preserved, not deleted.
