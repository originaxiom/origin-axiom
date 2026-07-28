# B793 Harvest — Autopsy of Every Past Interaction/Coupling Attempt

**Agent:** coupling-attempts (B793 information campaign, cc3 audit seat workflow, 2026-07-28)
**Repo:** /Users/dri/oa-audit-seat/origin-axiom (branch audit/b775-braver-questions; B787 read from origin/main)
**Method:** every mandated cell read in full (FINDINGS/RESULTS + reproducers where needed); surrounding coupling-lineage cells surveyed; open-lead ledgers cross-checked so nothing listed as \"never tried\" is secretly banked. All citations are file:line of files actually opened. No literature claims are made here (that is the literature agents' job).

---

## 1. The corpses, one by one

Format per cell: **what coupling was modeled / what was computed / why it failed or stalled (exact stated reason) / what it left untried.**

### 1.1 B9_fusion_scattering — fusion category ↔ scattering vertex
- **Modeled:** identify the Fibonacci fusion rule tau × tau = 1 + tau with the cubic 2↔1 self-interaction vertex of the inserted 1+1 field theory (B6/B8).
- **Computed:** symbolic verification that both rest on tau² − tau − 1 (quantum dimension phi; vertex coefficients ½·kappa·sqrt5 and kappa/3).
- **Death:** **STALLED** — \"shared polynomial, not a rigorous fusion ↔ scattering map… There is no functor here, only a shared characteristic polynomial\" (frontier/B9_fusion_scattering/FINDINGS.md:30-42). The fusion rule is exact MTC data; the vertex is a perturbative artifact of an *inserted* field theory.
- **Left untried:** any actual functor MTC → scattering theory; using the Fibonacci category to *build* an S-matrix coupled to the object.

### 1.2 B143_interaction_feasibility — the venue verdict for two-object coupling
- **Modeled:** the two-seed interaction (B131's A-polynomial fiber product in the (kappa = tr[A,B], trT) trace coordinates) and its chirality content.
- **Computed:** the mirror (swap_{R↔L} ∘ reverse) verified to preserve every trace for seeds 1,2,3 and compositions.
- **Death:** \"the chirality-of-interactions question cannot be answered in the algebraic (trace) venue — that venue is mirror-blind\" (FINDINGS.md:9-18). The topological venue needs Regina — \"Regina is not installed\" (:22-24). The hyperbolic 2-cusped link realization \"is itself a construction question (open)\" (:25-26). The \"588 irreducible reps\" external claim was not reproducible and its falsifiable part was dead (s776 is not Brunnian) (:27-30).
- **Left untried:** the hyperbolic link realization of the two-seed interaction; the Regina JSJ pipeline (later attempted in B144, still blocked).

### 1.3 B144_interaction_chirality (+ B145) — chirality of cusp-glued interactions
- **Modeled:** closed JSJ composites of two amphichiral pieces glued by phi ∈ GL(2,Z); can interaction produce preferred handedness?
- **Computed:** the MB12 vacuity chain (orientation-independent invariants can never distinguish M from its mirror; orientation-sensitive ones only flip sign/conjugate, FINDINGS.md:7-17); the mirror-closure identity M̄(m1,m2,phi) ≅⁺ M(m1,m2,h2·phi·h1⁻¹) — \"the family is mirror-closed ⟹ no preferred handedness can arise\" (:21-25).
- **Death (of the naive campaign):** \"Seed-heterogeneity injects contingency (B131's discrete kappa-fork) but not chirality-breaking — they are different axes\" (:29-30). The explicit Regina build hit a tooling limit: \"explicit closed-composite certification is not in-session-tractable\" (:36-41).
- **Redirect and its closure:** preferred handedness needs \"a chirally-asymmetric input: a substitution / interaction *not fixed by swap+reverse*\" (:47-50). B145 then proved the forced version impossible: \"canonicity coincides with the self-mirror (amphichiral) condition; chirality requires leaving the canonical locus\" (frontier/B145_forced_chirality/FINDINGS.md:1-7) — so the chiral input is irreducibly **contingent**.
- **Left untried:** nobody ever *modeled the contingent chiral input as the observer's contribution* — i.e., accepted non-canonicity and placed the asymmetry in the coupling. That is exactly H0-shaped and is the flip B793 can make on this corpse.

### 1.4 B185 / B190 / B191 / B174 — the gluing landscape (context corpses)
- B185: all-unit interaction **caps at pairs** (graph-theoretic degree count) (frontier/B185_constraint_selection/FINDINGS.md:22).
- B190: abstract iterated gluing \"does not converge to a forced-unique value\" — proliferation, not selection (frontier/B190_iterated_gluing/FINDINGS.md:1-8).
- B191: a *coupling* 2-cusp connector nests the kappa-fork to N≥3 (discrete-and-proliferating); \"the true geometric metallic 2-cusp 3-manifold is the NEEDS-SPECIALIST residual\" (frontier/B191_two_cusp_connector/FINDINGS.md:3-9).
- **Left untried:** the geometric connector itself; any dynamics ON the discrete fork (the forks were only enumerated, never weighted/evolved).

### 1.5 B187_interacting_open_collective + B188_lindblad_dissipative — many-body coupling channels
- **Modeled:** B187: spinless fermions with Hatano–Nelson non-Hermitian hopping + metallic Sturmian potential + nearest-neighbour interaction U (does interaction protect against the thresholdless arrow?). B188: dephasing Lindblad dissipators (Liouvillian gap).
- **Computed:** exact diagonalization, L=10–16, 2–3 fermions: g_c(U) ≈ 0 at all U (no protective gap); localized control protected at all U (frontier/B187_interacting_open_collective/FINDINGS.md:29-35). B188: no slow relaxation, no intrinsic scale (frontier/B188_lindblad_dissipative/FINDINGS.md:1-6).
- **Death (as a coupling source):** \"the arrow's source is the externally-imposed openness (the imaginary gauge field is *input*) — not self-generated. So the interacting open collective adds no scale and no self-generated arrow\" (B187:37-40).
- **Left untried:** thermodynamic-N (NEEDS-SPECIALIST, B187:52-54); D3/B450 interacting-entanglement extension (queued, POWER-GATED, docs/OPEN_LEADS.md:321).

### 1.6 B476_interaction_algebra — \"critical interaction algebra = SM gauge algebra\"
- **Modeled:** seat-1's claim that the dim of span{W1^j W2^l} at level 15 is 36 = 4×9 = gl(2)⊗gl(3) ⊃ su(3)⊕su(2)⊕u(1).
- **Computed:** exact SVD ranks: span dim **49** (not 36); mod-3 factor **5** = C⊕M2 (not 4); mod-5 factor **13** = M2⊕M3 (not 9); 5×13 = 65 ≠ 49, does not factor (FINDINGS.md:9-16).
- **Death:** the su(2)/su(3)-shaped blocks are \"the arithmetic of the primes 3 and 5 — unavoidable, pair-independent, criticality-independent… the equivariance-inversion trap in its purest form: a structure you cannot fail to find cannot fire\" (:26-31). Ninth float-kill.
- **Left untried:** the (1,3)/(2,3) controls deciding whether the 16 exact inter-sector lock relations (the 65−49 deficit) are pair-specific or level-forced — \"the named follow-up\" (:52-53), never run.

### 1.7 B489_self_interaction_tower — the cyclic cover tower as self-interaction
- **Modeled:** b++(RL)^n = n-fold cyclic cover of 4₁ as \"the object interacting with itself\"; SM reading via DGG gauge rank and twist-knot surgery.
- **Computed:** tower verified n=1..8 (torsion |L(2n)−2|, vol = n·v₄, rectangular cusps).
- **Death:** \"DGG is abelian at every level… U(1)^{2n−1}… No SM gauge group at n=4, n=8, or any n\" (FINDINGS.md:33-38); the surgery bridge 4c refuted on a wrong volume — \"the lead is DEAD\" (:43-46); the §3 \"tower generates the program's numbers\" reading is \"LARGELY NUMEROLOGY\" — only 5 = det(4₁) = disc Q(√5) is structural (:53-64).
- **Left untried:** the **level-16 Weil-rep lock count** — the one named computable bridge test for the 4b coincidence (:50-52).

### 1.8 B566_self_interaction — the five self-interaction channels (H123–H127)
- **Modeled:** the object applied to itself: prime-power dark hyperbola (S1), thermal self-clock/KMS (S2), canonical two-end entanglement (S3), measurement-of-measurement (S4), defect charge vs topology (S5).
- **Computed & survived:** the triple identity Z/11 = N(phi⁵−1) = 5-fold-cover torsion (RESULTS.md:8-27); KMS weights (5±√5)/20 ≠ letter frequencies (:45-55); S(5:3) = 0.3217 (modal only among *entangled* doubles — the mode is 0) (:56-65); SL(2,Z/15)^ab = Z/3, one collapse then a fixed point (:67-74).
- **Stall points:** S1 is a LIVE empirical law whose \"symbolic proof (degenerate Gauss sums at p²) is the named open step\" (:39-41); S2's Connes–Rovelli reading \"stays a tagged HOOK\" (:54-55).
- **Joint lesson:** self-interaction \"does not smear — it quantizes and closes\" into small exact residues (:76-83). Self-coupling produces grammar, not values — consistent with H0.

### 1.9 B629 → B630 → B631 — the interaction round (the values → design → run discipline)
- **Modeled:** the interaction LAYER as matrices (the program's own three-layer split: spectrum = chirality, trace = field, matrix elements = listener coupling — B611/B613, cited at B629 FINDINGS.md:12-15), with exactly ONE authorized comparison.
- **Computed:** B629 sealed the E₆₂ 3×3 odd hearing form (exactly unitary, |B_ij|² an exact doubly-stochastic circulant in Q(zeta14,√7)), the golden frame angle arctan(1/phi), a ~40-value composite inventory (NOT-FOR-COMPARISON), and PDG couplings RG-run to object scales Lambda_A = 3.86e14, Lambda_B = 3.52e16 GeV (NOT-FOR-COMPARISON) (B629 FINDINGS.md:23-82). B631 ran the one comparison: |B|² vs |U_PMNS|².
- **Death:** \"0/9 at 1%… p_D = 0.700… **STRUCTURED-NULL. The stopping rule fires: the program's SM-comparison capability at this level is exhausted.**\" Any future SM-facing comparison \"requires a new owner-level directive with its own principled preregistration\" (B631 FINDINGS.md:36-59). Controls proved this was a real null, not a broken pipeline (a near-PMNS unitary at eps=0.02 fires p=0.00027) (:84-90).
- **Left untried (frozen, gated):** L86 — the object-scale coupling comparison against the frozen §4 targets; L87 — the composite ↔ observable structural derivation (docs/OPEN_LEADS.md:532; B631:104-105). These are the only SM-facing doors left, and both are owner-gated by design.

### 1.10 P2W2-SPECTRIPLE — the Connes spectral triple attempt (OI-036)
- **Modeled:** A = E6 character ring, H = seam space (multiquadratic Galois C[(Z/2)³]), D = Fox-built Dirac.
- **Computed (exact, over Q(t), t²=t−1):** the Fox complex is a genuine cochain complex; D = d+d* is exactly self-adjoint on H_geo = C⁸; R(E6) acts on H_geo graded by the E6 exponents; the analytic axioms are vacuous in finite dim (output.txt:1-27).
- **Death:** \"R(E6) has NO canonical action on C[(Z/2)³]; D_Fox is NOT defined on C[(Z/2)³]… the bridge pi: A → B(H_seam) with [D,pi(a)] bounded: False… the dim-8 coincidence (2+4+2 vs 2³) is not a bridge\" — verdict RESOLVED-B, FORMULATION-OBSTRUCTION-NAMED (output.txt:30-44).
- **Left untried:** (a) the real-structure (J,gamma) first-order conditions on the *well-posed geometric* triple — named in-cell as \"the only non-vacuous target in finite dim\" (results.json, axioms.real_content) and never computed; (b) any **spectral action** Tr f(D/Λ) on that triple; (c) *constructing* a bridge (e.g. from Frobenius/class-field data acting on both sides) rather than checking whether a canonical one already exists.

### 1.11 B787 (origin/main) — the interaction programme: six doors, six MISSes, one HIT
Standing record stated in-file: **1-for-21** (FINDINGS.md:7). Per-door (table at :17-23, tally :25):
- **D1 Fox-calculus bridge — MISS:** \"every Fox observable is a signed sum of prefix group-elements, hence lives in the trace ring. Verify found the stronger reason: **sigma_mirror = a⁻¹.sigma.a** exactly… the hoped theta-content is a trace-trivial inner automorphism\" (:18). *Coupling idea killed: a group-ring-level theta-intertwiner richer than traces.*
- **D2 R-matrix braiding — MISS:** the diagonal-R self-overlap Born is exactly V4-invariant with floor sin²36° = (5−√5)/8 = 0.34549; JUNO (0.30902) and |S_tautau|² (0.27639) lie strictly below — \"structural impossibility, not near-miss\" (:19). *Killed: braiding Born probabilities as the coupling's value channel (in the diagonal class).*
- **D3 15A8 newform @ Fibonacci — MISS:** a_{F_n} generic; \"Fibonacci is additive, Hecke is multiplicative — orthogonal structures, no mechanism\" (:20).
- **D4 E6(78) under V4 — MISS:** premise false — \"Aut(E6 Dynkin) = Z/2… has room for ONE involution, not four\"; the folding tau is neither c nor theta individually (:21). (Exact sub-result: the tau-parity split of exponents, banked as hint.)
- **D5 state integral Z(u) — MISS:** programme-point values are generic deformed-dilog periods; the only structured transcendental (Vol(4₁) = (3√3/2)L(chi₋₃,2)) sits at u=0, the COMPLETE structure, not a programme point; near-misses below the ~6.7 look-elsewhere budget (:22).
- **D6 Habiro c_n @ Fibonacci — MISS:** generic super-factorial growth; the phi-drift is an envelope artifact (:23).
- **HIT (structural): iota = inversion is a genuinely independent 4th involution** — flips T7 (time) but fixes T3 (basepoint, by A5-ambivalence), de-welding what B766 welded (:18, :49). Deliberately NOT established: whether iota is an *observer* closing operation (rank-3 vs rank-4 menu) — open item 2 (:150-153).

### 1.12 The coupling-path lineage (B697, B706, B720, B721, B722, B723) — where \"coupling\" went after the reframe
- **B706:** the SM flavor freedom does not match the object at either rung — \"the flavor is fully in the coupling\" (frontier/B706_rung2_sm_freedom/FINDINGS.md:1-8). This is the cell that *created* H0's division of labor.
- **B720:** three external bridge programs NO-MATCH (renormalization: wrong cyclotomic branch Z[i] vs Q(zeta3); holography: 3d has no local DOF; positive geometry: finite-mutation vs finite-type); the strongest lead = the CMR Bost–Connes KMS torsor over Q(√−3) (FINDINGS.md:15-44).
- **B721:** that lead run: **OUTCOME B, rung-mismatch** — \"the coupling's thermal clock is a DIFFERENT KIND than the object's own clock\" (type II₁ tracial, trivial modular flow) (FINDINGS.md:11-15).
- **B722:** the Kashaev resurgence is \"the ONE discrete→continuous machine that consumes the object's A-polynomial today\", its phases ARE being/hearing (rung 1), **but the continuum is arithmetically RIGID over Q(√−3)** — every Phi^(n)(t*) ∈ Z[√−3], Borel singularity at i·Vol(4₁), only discrete freedoms; \"NO free continuous parameter\" (FINDINGS.md:11-35). Completion: \"every object continuum is rigid/scale-free, none the SM's free coupling\" (:42-49).
- **B723:** the observer apparatus is built (type-III completion) and \"the observer is a PHASE TRANSITION, not a state\" (FINDINGS.md:1-11) — but no order parameter / value consequence was ever extracted from that SSB.
- **B535/B539:** the coupling space is FINITE (6 Perron types, 7 canonical systems, 17 degree-4 read-outs, one-measurement uniqueness) (B535 FINDINGS.md:20-77); the relations comparison ran: forced-bin control PASSES, **SM bin NO-MATCH** (0 hits at 1e-5) (B539 FINDINGS.md:36-47). Note for completeness: B535's \"SM comparison as RELATIONS\" follow-up DID run (B539) — do not list it as untried.
- **B410:** the class action has no window-local origin — \"the class-group generator acts at TRACE/aggregate level… NO cell-local window origin\" (frontier/B410_coupling_derivation/FINDINGS.md:7-12): couplings that exist only in aggregate cannot be localized into a mechanism.

---

## 2. Failure taxonomy — why couplings die in this repo

1. **Venue blindness.** Trace/character data cannot see mirror/theta content (B143); even Fox calculus — one level below traces — collapses back into the trace ring because the mirror is an inner automorphism (B787 D1). Any coupling carrying orientation/chirality content must leave the trace venue *by construction*.
2. **Equivariance-inversion traps.** Level arithmetic manufactures su(2)/su(3)-shaped blocks unavoidably (B476); dim coincidences (8=8 SPECTRIPLE; 16=16 B489) recur. A structure you cannot fail to find cannot fire.
3. **Arithmetic rigidity.** Every continuum the object generates is rigid over its own fields with only discrete freedoms (B712/B719/B721/B722). There is no dial in the object; the dial must be supplied by the coupling model itself.
4. **Value numerology dies at base-rate.** 1-for-21; B631 p=0.700; B539 SM NO-MATCH; B787 D2/D5 near-misses below budget. Every value-facing corpse died the same way.
5. **No bridge maps.** The geometric side (Fox/E6 cochains) and the arithmetic side (seam/Galois) have no constructed morphism (SPECTRIPLE). Identifications were repeatedly attempted by dimension-matching and always refused.
6. **Tooling walls.** Regina gluing (B143/B144), the geometric 2-cusp connector (B191), thermodynamic-N ED (B187) — three couplings stalled on capability, not on refutation. These are *suspended*, not dead.
7. **Externally-sourced dynamics.** Where dynamics was inserted by hand (non-Hermitian gauge field, Lindblad dissipators), the resulting arrow/scale was traceable to the insertion (B187/B188) — a warning template for B793: a coupling model must make the source of its dynamics explicit or it proves nothing.
8. **Kind-mismatch.** The one field-matched external coupling (CMR KMS over Q(√−3)) failed on *kind* (thermal vs tracial clock, B721). Field agreement is rung 1; a coupling claim needs the structure to be the same object, not the same field.

---

## 3. What the corpses left standing (assets B793 inherits)

- The **kappa-fork discrete selection** survives gluing and nests to N≥3 (B131/B174/B191) — a discrete, proliferating interaction observable with no dynamics yet on it.
- The **mirror-closure + canonicity=amphichirality theorems** (B144/B145): parity violation, if modeled, must be a contingent coupling input — this is a *positive design constraint*, not just a no-go.
- The **iota rank-4 de-weld** (B787): time's arrow (T7) and basepoint (T3) are separable by a native involution; its observer status is the open hinge.
- The **well-posed geometric spectral triple** (SPECTRIPLE): exact, self-adjoint, graded by E6 exponents — built and then abandoned one step before its only non-vacuous test.
- The **resurgence dictionary** (B722): saddles = being/hearing, A² = M, the c-swap realized as the sigma1↔sigma2 Kashaev exchange — the closest thing the repo has to the object appearing *inside* a physics formalism.
- The **finite coupling-space census + read-out dictionary** (B535): 6 types, 17 exact degree-4 read-outs, one-measurement completeness.
- The **frozen, hash-sealed comparison assets** (B629): tuning-proof by construction, waiting on principled designs (L86/L87).

---

## 4. The NEVER-TRIED list (explicit)

Coupling-shaped ideas with **no cell, no prereg, no run** anywhere in the repo (ledgers cross-checked: docs/OPEN_LEADS.md, HINT_LEDGER references in B631, B787 §5):

**A. Dynamics (the empty quadrant — B793's own plan admits \"the repo has none\", INFORMATION_PLAN.md:20-23):**
1. **Any joint Hamiltonian / Lagrangian / action functional coupling observer DOF to object DOF.** Never written, in any cell. Every past \"interaction\" was kinematic (gluing, spans, spectra, comparisons).
2. **The spectral action on the well-posed geometric triple** (Tr f(D/Λ) for D = d_Fox + d_Fox*, A = R(E6) on H_geo) — SPECTRIPLE built the triple and stopped; the (J,gamma) real-structure/first-order conditions it named as the only non-vacuous content were never computed.
3. **A spectral action / trace-formula dynamics fed by the actual object spectrum** — B792's 17 Maass eigenvalues and the banked length spectrum have never been consumed by anything coupling-shaped.
4. **RG running WITH an object-supplied boundary condition** at a principled scale — the L86 door: frozen targets exist (B629 §4), the principled scale-argument + prereg has never been attempted (owner-gated, not dead).
5. **Dynamics ON the observer's free parameters:** promote the free choices the repo has *proven* free — the covering-scale ladder (B719), the torsor basepoint (B701), the contingent chiral input (B145) — to dynamical variables with a flow/potential, and ask what dynamics selects. No cell has ever put dynamics on a freedom; they were only ever catalogued.
6. **Order parameters of the observer SSB:** B723 proved the observer is a phase transition and never computed what condenses (the VEV-analogue) or any value consequence.

**B. Two-sided algebraic couplings:**
7. **Constructing (not searching for) the geometric↔arithmetic bridge:** e.g. build a map from the Fox/E6 cochain side to the multiquadratic seam side out of Frobenius/class-field data. SPECTRIPLE only verified no canonical action exists.
8. **A composite von Neumann algebra:** object (type II₁, tracial — B721) tensor/crossed-product observer (type III — B723) with a joint state; test whether the *joint* modular flow is nontrivial. The repo proved the object alone has trivial modular time; nobody coupled the two algebras to see if time lives in the pair.
9. **Actually building the Bost–Connes-type coupled system over Q(√−3)** (Marcolli–Xu-style knot QSM referenced in B720): B721 adjudicated an *identity* question (is B701's torsor the CMR torsor — no, rung-mismatch) and never constructed the coupled system itself.

**C. QFT-native couplings:**
10. **T[m004] used as an actual theory:** the 3d-3d dictionary is marked borrowed/POSTULATED (K006); the repo only ever computed the DGG gauge rank (abelian, B489). Partition functions of T[m004] on chosen backgrounds, its moduli, its couplings-as-functions-of-geometry, or coupling T[m004] to a listener sector: never tried.
11. **The coupled / pair state integral:** the wave-2 queue item \"coupled state integral\" (docs/OPEN_LEADS.md:270) never ran; B787 D5 evaluated only the single-object Z(u). The partition function of the *glued pair* (where the kappa-fork lives) has never been computed.
12. **A genuine MTC→scattering functor** (closing B9's gap): use the Fibonacci category to build a scattering/S-matrix theory whose target the object constrains.

**D. Structure-breaking and selection couplings:**
13. **The contingent chiral input as the observer's contribution:** B144/B145 proved the object cannot supply parity violation and that any chiral input is non-canonical — no cell then *modeled* such an input as part of the coupling (the H0-shaped inversion of the old dead end).
14. **Selection dynamics over the finite coupling-space census** (B535's 6 Perron types / 7 canonical systems): no stability, entropy, iteration-fitness, or environmental-selection principle over the finite menu has ever been proposed or tested.
15. **Observer–observer coupling through the object (intersubjectivity):** every hearing/listener cell (B584–B594, B640, B654, B702, B726, B751) is single-listener. Two listeners coupled via the same object — do their read-outs constrain each other? — never posed.

**E. Suspended-on-tooling geometric couplings (not dead, unbuilt):**
16. The **hyperbolic 2-cusped link realization** of the two-seed interaction (B143 scout); the **explicit Regina closed JSJ composite** (B144 gate); the **geometric metallic 2-cusp connector** (B191, NEEDS-SPECIALIST).
17. **Thermodynamic-N interacting open collective** (B187) and the queued POWER-GATED D3/B450 interacting-entanglement extension (docs/OPEN_LEADS.md:321).

**F. Named computable follow-ups no one ran:**
18. The **level-16 Weil-rep lock count** (B489 4b bridge test); the **(1,3)/(2,3) lock-relation controls** (B476); the **symbolic p² dark-hyperbola proof** (B566 S1); **iota's observer-status adjudication** (B787 open item 2 — decides whether the coupling's discrete closing menu has rank 3 or 4, which any B793 coupling model must fix as an input).

---

## 5. One-paragraph verdict for the masterplan

The repo has attempted coupling at every level *except* the dynamical one: object-object (gluing — discrete, proliferating, mirror-closed, pair-capped), object-self (covers, self-substitution — abelian, quantizing into grammar residues), algebra-algebra (spans, spectral triples — no bridge, equivariance traps), object-formalism (resurgence, KMS, NCG — field-matched but rigid or kind-mismatched), and values-vs-SM (sealed comparisons — structured nulls, stopping rule fired). Every corpse is consistent with H0 and none contradicts it; the common cause of death is that each attempt asked the object or its kinematics to produce what only a dynamical coupling could. The genuinely virgin territory is short and precise: write dynamics (an action, a flow, a joint state) whose *fixed structural input* is the banked grammar and whose *free input* is one of the repo's proven freedoms (scale ladder, torsor basepoint, contingent chiral input), then let the base-rate protocol judge what the dynamics selects. Items 1–9 and 13–15 of §4 are the pre-registerable shapes of that move; items 16–18 are the suspended computations that de-risk them.


## KEY FACTS (structured)
- The chirality-of-interactions question cannot be answered in the algebraic (trace) venue: the mirror (swap+reverse) preserves every trace, so the trace venue is structurally blind to mirror-distinction; the topological venue needs Regina (not installed); the hyperbolic 2-cusped link realization of the two-seed interaction is an open construction question.
  - source: frontier/B143_interaction_feasibility/FINDINGS.md:9-26
- Mirror-closure identity: for two amphichiral pieces glued along a torus by phi in GL(2,Z), the mirror of the composite is another composite of the same family (h2.phi.h1^-1), so no preferred handedness can arise from cusp-gluing; preferred handedness requires a chirally-asymmetric input not fixed by swap+reverse.
  - source: frontier/B144_interaction_chirality/FINDINGS.md:21-33,47-50
- B145 closed the redirect's forced version: canonicity coincides with the self-mirror (amphichiral) condition — chirality requires leaving the canonical locus, so a chiral input is irreducibly contingent (observer-side).
  - source: frontier/B145_forced_chirality/FINDINGS.md:1-7
- Interacting open collective: a two-body interaction U opens NO protective gap (g_c ~ 0 at all U in 0..4); the arrow is genuine but dimensionless and externally sourced (the imaginary gauge field is input) — no scale, no self-generated arrow; thermodynamic-N regime is NEEDS-SPECIALIST.
  - source: frontier/B187_interacting_open_collective/FINDINGS.md:29-40,52-54
- The 'critical interaction algebra = SM gauge algebra' claim is refuted on all four numbers (span dim 49 not 36; CRT factors 5 and 13, not 4 and 9; no tensor factorization). The su(2)/su(3)-shaped blocks are the unavoidable parity-block arithmetic of level 15 — the equivariance-inversion trap. Residue: 16 exact inter-sector lock relations, with the (1,3)/(2,3) controls the named, never-run follow-up.
  - source: frontier/B476_interaction_algebra/FINDINGS.md:9-31,43-53
- The self-interaction (cyclic cover) tower of 4_1 is clean verified mathematics (torsion |L(2n)-2|, vol = n*vol(4_1)), but its SM reading is refuted: DGG gauge rank 2n-1 gives U(1)^(2n-1) — abelian at every level n=1..8; the surgery lead 4c is dead on a wrong volume; the 16-locks/torsion-16 coincidence (4b) is unbridged, with the level-16 Weil-rep lock count the named open computable test.
  - source: frontier/B489_self_interaction_tower/FINDINGS.md:33-51
- B566's five self-interaction channels all terminate in small exact residues (Z/11 = N(phi^5-1) triple identity; KMS weights (5±sqrt5)/20 distinct from letter frequencies; seam entanglement S(5:3)=0.3217 modal only among entangled doubles; SL(2,Z/15)^ab = Z/3 one-collapse). Open: symbolic proof of the prime-power dark-hyperbola law (degenerate Gauss sums at p^2).
  - source: frontier/B566_self_interaction/RESULTS.md:8-83
- The one authorized interaction-layer comparison (3x3 odd hearing form |B|^2 vs |U_PMNS|^2, sealed values B629 + sealed design B630) returned STRUCTURED-NULL: 0/9 matches at 1%, p_D = 0.700; the stopping rule fired — 'the program's SM-comparison capability at this level is exhausted'; any future SM-facing comparison needs a new owner-level directive with its own preregistration. Controls proved the instrument could have detected a real match (eps=0.02 perturbation gives p=0.00027).
  - source: frontier/B631_matrix_comparison/FINDINGS.md:10-59,84-90
- B629 sealed-and-froze two never-compared assets: the ~40-value composite inventory (needs a structural derivation of which composition <-> which observable BEFORE any distance) and the object-scale RG coupling targets (PDG couplings run to Lambda_A = |tau_8|/|tau_4|*GeV = 3.86e14, Lambda_B = 3.52e16, mu_ref = 1e16 GeV). Both deferred, hash-frozen; registered as gated leads L86/L87.
  - source: frontier/B629_interaction_values/FINDINGS.md:66-82; docs/OPEN_LEADS.md:532
- B9: Fibonacci fusion (tau x tau = 1 + tau) and the cubic self-interaction vertex share only the polynomial tau^2 - tau - 1; STALLED — 'shared polynomial, not a rigorous fusion <-> scattering map'; no functor between the fusion category and any scattering amplitude was ever built.
  - source: frontier/B9_fusion_scattering/FINDINGS.md:36-42
- P2W2-SPECTRIPLE (Connes triple A = R(E6), H = seam, D = Fox): RESOLVED-B, formulation obstruction named — a well-posed Fox/E6 triple exists on the geometric cochain space H_geo = C^8, but no bridge pi: R(E6) -> B(H_seam) exists; the dim-8 coincidence (2+4+2 vs 2^3) is not a bridge; the analytic axioms are vacuous in finite dim and the only non-vacuous content — the real-structure (J,gamma) first-order conditions — was never computed.
  - source: frontier/B775_phase2_wave1/cells/P2W2-SPECTRIPLE/output.txt:30-48; results.json 'axioms.real_content'
- B787: all six doors MISS (D1 Fox: sigma_mirror = a^-1.sigma.a inner, trace-ring ceiling; D2 R-matrix: Born floor sin^2 36 = 0.34549 puts JUNO structurally out of reach; D3 newform@Fib generic; D4 premise false, Aut(E6 Dynkin) = Z/2; D5 state-integral values generic, the one structured transcendental sits at u=0; D6 Habiro@Fib generic). One HIT: iota = inversion is an independent 4th involution (rank 3->4), de-welding T7 (time) from T3 (basepoint); its status as an OBSERVER closing operation is deliberately open.
  - source: git show origin/main:frontier/B787_interaction_programme/FINDINGS.md:17-25,49,150-153
- Every continuum the object produces is rigid/scale-free: the A-polynomial deformation curve (B712), the covering ladder (B719, the observer's free scale), the object's own time (B721, tracial type II1, trivial modular flow), and the hbar resurgence series (B722, coefficients in Q(sqrt-3), Borel singularity at i*Vol(4_1), only discrete freedoms) — none is the SM's free coupling (B706 reconfirmed at every level).
  - source: frontier/B722_resurgence_coupling/FINDINGS.md:27-49
- The coupling-path map: renormalization (Connes-Marcolli, wrong cyclotomic branch), holography (dimensional no-go), positive geometry (wrong regime) are NO-MATCH; the strongest lead — the CMR Bost-Connes KMS torsor over the object's own field Q(sqrt-3) — was run in B721 and came back OUTCOME B: field-matched but a rung-mismatch (the observer's thermal clock is a different kind than the object's tracial clock). The coupled QSM system itself was never constructed.
  - source: frontier/B720_coupling_path/FINDINGS.md:15-44; frontier/B721_thermal_time/FINDINGS.md:11-15
- The coupling space is finite and fully mapped (6 Perron types, 7 canonical systems, 17 read-out components all degree 4 over Q, one-measurement uniqueness theorem); the relations comparison ran in B539: forced-bin positive control PASSES, SM bin NO-MATCH (0 hits surviving 1e-5). No selection dynamics over this finite menu has ever been proposed or tested.
  - source: frontier/B535_coupling_space/FINDINGS.md:20-95; frontier/B539_relations_campaign/FINDINGS.md:36-63
- B793's own information plan concedes the repo-wide gap the autopsy confirms: 'Building a coupling is qualitatively harder than anything done so far: it needs dynamics, and the repo has none.' Every prior interaction attempt was kinematic (gluing, algebra, spectra, comparisons) — no dynamical coupling law was ever written down.
  - source: frontier/B793_coupling_campaign/INFORMATION_PLAN.md:20-23

## CONSTRAINTS FOR B793
- VENUE: the algebraic/trace venue is mirror-blind — the R<->L mirror preserves every trace, so no chirality-of-coupling content can be read from character-variety/trace data; orientation-sensitive tooling is mandatory (B143 FINDINGS:9-18).
- VACUITY PRE-CHECK (MB12): before computing toward any target, check it can fail. Orientation-independent invariants NEVER distinguish M from its mirror; orientation-sensitive ones only flip sign/conjugate (B144 FINDINGS:7-17).
- CHIRALITY: canonical/forced objects are amphichiral (B145); seed multiplicity/heterogeneity never breaks the R<->L mirror (B144 mirror-closure identity). If the coupling model needs parity violation, the chiral asymmetry must be a CONTINGENT observer-side input, not derived from the object.
- TRACE-RING CEILING: every Fox-calculus observable lies in the trace ring, and the Fibonacci mirror is INNER (sigma_mirror = a^-1.sigma.a) — no group-ring-level theta content beyond traces exists (B787 D1, origin/main FINDINGS:18).
- RIGIDITY: every continuum the object produces is arithmetically rigid/scale-free — A-polynomial curve (B712), hbar resurgence series over Q(sqrt-3) (B722), tracial type-II1 modular flow (B721), covering ladder (B719). A coupling model must SUPPLY its own continuous dial; the object has none to offer (B706, B722 FINDINGS:42-49).
- TIME: the object algebra is tracial (type II1, trivial modular flow) — time cannot be object-intrinsic; it must arise on the coupling/observer side (B721, B723: the observer is a phase transition / SSB).
- BORN FLOOR: diagonal Fibonacci-R self-overlap Born probabilities are exactly V4-invariant with floor sin^2(36 deg) = (5-sqrt5)/8 = 0.34549; JUNO 0.30902 and |S_tautau|^2 = 0.27639 are structurally unreachable in that class (B787 D2, origin/main FINDINGS:19,138).
- STOPPING RULE: B631 fired STRUCTURED-NULL (p=0.700) — any SM-facing comparison requires a NEW owner-level directive plus its own principled preregistration; the B629 seals (composite inventory, RG targets Lambda_A=3.86e14, Lambda_B=3.52e16, mu_ref=1e16 GeV) are frozen and cannot be tuned (B631 FINDINGS:53-59; B629 FINDINGS:66-82; OPEN_LEADS L86/L87 GATED).
- BASE RATE: the interaction programme is 1-for-21; every numeric door needs a pre-enumerated target set, tolerance window, and expected-chance-hit count; a ~0.3-1% coincidence is a MISS (B787 PREREGISTRATION base-rate control). Structural coincidences get the same knife (B476's equivariance-inversion trap: a structure you cannot fail to find cannot fire).
- NO DIM-COINCIDENCE BRIDGES: dim 8 = dim 8 (SPECTRIPLE geometric vs seam), 16 locks vs torsion 16 (B489 4b) — equal numbers are not maps; a bridge requires a constructed morphism plus a theorem before any identification is used.
- NO SCALE FROM INTERACTION: two-body interaction opens no protective gap (B187), Lindblad dissipation has no intrinsic scale (B188), and the arrow is externally sourced and dimensionless — inserting openness by hand imports the arrow, it does not derive it.
- NO FORCED UNIQUENESS FROM ITERATION: gluing selection is discrete-and-proliferating, never converging to a forced-unique value (B185/B190/B191); all-unit interactions cap at PAIRS — N>=3 needs a >=2-cusp connector whose geometric realization is unbuilt.
- SELF-INTERACTION IS ABELIAN: the cyclic-cover tower has DGG gauge rank 2n-1 = U(1)^(2n-1) at every level — no gauge enhancement from unwrapping the object (B489 FINDINGS:33-38).
- METHOD: never place a value and a function of itself in the same test list (B539); pipeline positive/power controls are the house standard (B631 addendum, B575); prereg sealed BEFORE compute; two-outcome cells only ('a cell that cannot fail cleanly does not run', B793 INFORMATION_PLAN:73).
- DYNAMICS GAP (the honest starting point): no Hamiltonian, Lagrangian, action functional, probability rule, or equation of motion coupling observer DOF to object DOF has EVER been written in this repo — every prior 'interaction' was kinematic/algebraic (B793 INFORMATION_PLAN:20-23 states it: 'it needs dynamics, and the repo has none').

## OPEN HOOKS
- L86 (GATED): the object-scale coupling comparison against the frozen B629 §4 RG targets — needs a new owner-level directive + principled preregistered scale/coupling/target argument (docs/OPEN_LEADS.md:532).
- L87 (GATED): the composite-inventory comparison — needs a structural derivation of which composition <-> which observable stated before any distance (B629 FINDINGS:66-72; B631 FINDINGS:104-105).
- L88: symbolic proof of the E62 Latin-square closed form (B631 addendum).
- B787 open item 2: reconcile iota's status as a measurement-torsor generator vs B766's banked rank-3 observer menu — decides whether the coupling's discrete closing menu is rank 3 or 4 (origin/main B787 FINDINGS:150-153).
- B787 open item 4: re-run the iota-id on the canonical primitive-6th-root Riley rep from B71/B99/B101 (verdict expected unchanged).
- B489 4b: compute the level-16 Weil-rep lock count — the one named computable bridge test for the torsion-16 coincidence (B489 FINDINGS:47-51).
- B476 follow-up: the (1,3)/(2,3) controls deciding whether the 16 inter-sector lock relations are pair-specific or level-forced (B476 FINDINGS:52-53).
- B566 S1: symbolic proof of the prime-power dark-hyperbola law (degenerate Gauss sums at p^2); PC22-successor material (B566 RESULTS:36-41).
- Wave-2 queue item never run: the COUPLED state integral (pair-level partition function; B787 D5 was single-object only) (docs/OPEN_LEADS.md:270,285).
- H5-a residual: the true geometric metallic 2-cusp connector 3-manifold (existence, which phi_c, dim-2 character variety) — NEEDS-SPECIALIST (docs/OPEN_LEADS.md:200; B191).
- B143 scout: a hyperbolic 2-cusped link realization of the two-seed interaction — never constructed (B143 FINDINGS:25-26).
- B144 gate: the explicit Regina-built closed JSJ composite certification — tooling limit, never done (B144 FINDINGS:36-43).
- D3/B450 (queued, POWER-GATED): interacting entanglement — extend B187's ED engine to level statistics / EE scaling (docs/OPEN_LEADS.md:321); thermodynamic-N interacting open collective NEEDS-SPECIALIST (B187).
- Escalator tower E0 lit-gate: is the (M,M^2) self-coupling functor's Perron escalation law known? (docs/OPEN_LEADS.md:206).
- B721 leftover: the CMR/Bost-Connes coupled system over Q(sqrt-3) was adjudicated as an IDENTITY question (rung-mismatch) but never BUILT as a composite object-observer algebra with a joint state.
- L71: what ARE the theta-odd deformations geometrically, and does the object's sigma-coupling single out a preferred theta-odd direction (docs/OPEN_LEADS.md:494).
- B792's 17 Maass eigenvalues are a brand-new asset: nothing coupling-shaped (spectral action, trace-formula dynamics, heat kernel) has consumed them yet.
