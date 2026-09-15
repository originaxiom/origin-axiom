# B1413 — THE AUDIT LANE'S R21–R31 HARVESTED: R27's theorem and its exact counter-example verified on main (the one-cusped index is a theorem-zero on every geometric finite twist, and a characteristic-zero non-semisimple module with I = +1 exists), nine rounds re-run green, two of main's own arcs narrowed in scope

**Date:** 2026-09-15 · **Seat:** cc (main) · **Lane:** HARVEST (MASTERPLAN v3.1 §1a; the consolidation). **Source:** the codex operator's live lane `audit/physical-bridge-2026-09-05` at **5e063851** (origin's head; worktree `<audit>/wt-audit`). **Verdict:** VERIFIED (R27 both halves, on main's own code and against the published source); RUN AND REGISTERED (R22–R26, R28–R31: the lane's own tests re-run on this bench, claims rowed with the seat's grades, independent re-derivation not done and said so); READ (fifteen documents). **Depends on:** B1304 (R0–R20), B1297, B1335, B1341, B1411, B1321. **Price:** none. **Credit:** the audit lane, round by round.

## 0. The rule applied
§1a: the seat speaks first; scripts are run, not read; no grade lower than the seat's without a computation here. Three readers (bounded verification) read the fourteen rounds and documents and ran every round's own tests in the pinned worktree; their reports are in `verification/readers/`. Main read R27 itself, recomputed its exact example, and checked its theorem against the published statement.

## R27 (FINITE_TWIST) — VERIFIED on main, both halves; the most consequential item of the lane's window

**Seat's headline:** *"R27: geometric zeros explained; an exact complex positive preserved."*

**(a) The theorem, checked against its source.** For M complete, non-elementary, topologically finite hyperbolic, h a lift of the complete geometric holonomy, m ≥ 1 and F any finite-image representation, put V = Sym^m(h) ⊗ F and n_Q(V) = dim ker[H¹(Q;V) → H¹(T;V)] (the interior image, B1297's n(V) = a₁ − r₁). Then n_Q(V) = n_Q(V*) = 0, so I_Q(V) = 0. Input: Menal-Ferrer–Porti, Osaka J. Math. 49 (2012) 741–769, **Theorem 0.1**, read on main from the arXiv text (1001.2242v2, p. 2): *"Let M be a complete, nonelementary, hyperbolic 3-manifold that is topologically finite, and n ≥ 2. Then the inclusion ∂M̄ ⊂ M̄ induces an injection H¹(M;E_ρn) ↪ H¹(∂M̄;E_ρn), with dim H¹(M) = ½ dim H¹(∂M̄)"* — n is the dimension of the irreducible representation, so every non-trivial symmetric power qualifies. Transfer: on the finite cover N = ker F the twist is trivial and h|π₁(N) is N's own geometric holonomy, so restriction is injective there; tr∘p* = (degree)·id on cohomology with pulled-back local coefficients, invertible over ℂ, so injectivity descends; the dual by the SL₂-invariant pairing on Sym^m and the finite-image dual of F. The argument is standard and correct; the lane grades it "an application of published mathematics plus an explicit transfer argument, not a new general vanishing theorem", and main agrees. **Consequence for the record:** every zero of the one-cusped index on B1297's cyclic tower, B1324's two sectors, B1330–B1335's covers and B1333's multi-cusp sectors (all of them geometric symmetric powers with finite twists) is forced by this theorem; B1334's partial proof on S⁰ and the "vanishing conjecture" are superseded on that class; the paper's falsifier 6 (a live index on a chiral cover) cannot fire inside the class, and the "non-vacuity" worry of the paper's chirality section is answered: the instrument is identically zero on D ∩ {geometric finite twists}, by theorem.

**(b) The exact positive, recomputed here** (`verification/main_r27_exact_lift.py`, exact over ℚ(u), u² − u + 1 = 0): SnapPy's presentation of m010 (⟨a,b | aabaBaaBab⟩, μ = AbAA, λ = babA) matches the lane's; A = [[0,1],[−1,1]], B = [[0,u²],[u,−2]] have determinant 1 and satisfy the relator; χ(a) = u, χ(b) = −1 is trivial on the relator and on both peripheral words. For V = Sym³(ρ) ⊗ χ: **a₀ = 0, a₁ = 1, t₀ = 1, t₁ = 2, r₁ = 0, n = 1; V*: a₁ = 2, r₁ = 2, n = 0; I(V) = +1** — the lane's table to the digit. The base representation is reducible and non-split: (1, u) is a common eigenvector with eigenvalues u and −1 (conjugated to upper-triangular [[u,1],[0,1−u]], [[−1,u−1],[0,−1]]); its semisimplification gives a₀ = 1, a₁ = 4, t₀ = 4, r₁ = 4, n = 0 on both sides, **I = 0**. So: a characteristic-zero, non-self-dual, non-semisimple local system with a nonzero index exists, and it has the same trace on every word as its semisimplification (a corollary of the invariant flag). This is the mathematical escape from the vanishing, exhibited exactly, and it sits outside B1297's reductive domain D.

**(c) The correction main owes to its own record.** B1335's "irreducibility filter" (`primescan.py`, now on main) tests only for a common eigenvector with the *same* eigenvalue for every generator; an invariant line with different eigenvalues (here 4 and 12 over F₁₃) passes it. So B1335's finite-field positive is real but its domain certificate is invalid: the example is non-reductive, and B1335's claim "in domain D" is withdrawn to "over F₇ and F₁₃, and exactly over ℚ(u), on a non-semisimple module outside D". ERROR_LEDGER row (E66 shape: an enforcement narrower than its rule). B1335's arithmetic and the lane's "vanishing is not formal" headline stand — with the domain corrected.

**(d) What it does not do**, in the lane's own words, kept: not the physical chirality theorem for the singular source operator (R18/R19/R26 are a different domain: a punctured source manifold, a real mass term, the maximal weighted complex); not an admissible harmonic metric, field equations, finite action or the four-dimensional fermion dictionary; not a validation of B1334's whole character-torus statement.

**FRESH_EYES Q16, updated:** the index on D restricted to geometric finite twists is a theorem-zero; a nonzero index requires extension data (non-semisimple modules), exhibited exactly; whether extension data can be physical is the open question, and it is now stated with a witness.


## Rounds R22–R26, R28–R31 — run on this bench, rowed with the seat's own grades
### R22 — the completion must change more than the four-dimensional field list
**Seat's verdict, quoted by the reader:** "R21's anomaly-free added-field theory remains valid, but its fermions are not supplied by the unchanged source operator. The proposed negative-charge vectors emerge with the opposite chirality. Finite-norm nonparallel charged profiles do exist as trial sections; normalizability is not the obstruction. A single minimally coupled scalar condensate with no compensating current cannot keep this order-three connection flat." It states these "direct the next calculation to an actual source/defect, inflow or coupled-field completion. They do not close that route, derive the Standard Model, or establish a full physical TOE."
**Tests on this bench:** ```
**Claims, graded as the seat grades them:**
  1. Applying R19's same-source charged operator to R21's added H-representation (16_1+10_-2+1_4 and CPT partner) nets 3×(16_1+10_+2+1_4), not the intended anomaly-free spectrum — COMPUTED.
  2. For any finite same-source enlargement by CPT pairs, Tr u and Tr u^3 are strictly positive sums over |q|, so this class cannot self-cancel R21's anomaly — PROVED-BY-SEAT.
  3. Finite-norm, nonzero charged trial sections exist on the order-three charge-four cusp line despite nonintegral holonomy — COMPUTED.
  4. A single minimally-coupled current-free scalar cannot hold a flat connection with non-real (order-three) holonomy, by an exact unique-continuation argument (input cited, not proved here) — CONDITIONAL (explicitly scoped to "one minimally coupled complex scalar... no other current").
**What main would have to verify:** Recompute the H1(q)/H1(-q) table and the six-variable anomaly polynomial from R21's actual weight sets (not labels); independently check the finite-norm tail-integral bounds and the Maxwell/unique-continuation argument's scope (single scalar, no other current) before citing any of this as an obstruction beyond that stated class.
### R23 — the source operator supplies normalized anomaly transport, not a boundary completion
**Seat's verdict, quoted by the reader:** "The existing charged differential is explicitly mapped to the two-flavour mass operator used in anomaly-inflow calculations. Its mass direction supplies an integrally normalized angular form... This constructs a specific local anomaly-transport candidate from the same operator, not another appended list of fields. It does NOT yet construct the global singular determinant or its boundary sector. Even granting perfect local inflow, dropping the outer-boundary term would fake cancellation of the three-spinor gauge-zero-mode anomaly."
**Tests on this bench:** ```
**Claims, graded as the seat grades them:**
  1. The R16 exterior/adjoint operator maps exactly onto a two-flavour Clifford mass-Dirac operator with kinetic symbol −σ·∂ and Hermitian mass m·σ — PROVED-BY-SEAT (own exact computation, checked against original operator).
  2. The induced mass-eigenline first Chern form integrates to exactly ±1 on a reference sphere (unit angular response, not doubled) — COMPUTED.
  3. Bulk anomaly descent from this operator cancels a localized charge only by transporting the identical charge to the outer boundary; a globally-constant gauge parameter leaves this bulk term's variation exactly zero — PROVED-BY-SEAT (within the stated Stokes/CS5 setup).
  4. An incoming SM-seat claim ("B1351": whole-cusp-torus acyclicity forces zero index for every Morse partition) is refuted on explicit relative cochains for a disc partition (H*=(0,k,0,0), χ=−k) — COMPUTED, explicitly scoped as "not a physically selected disc boundary."
**What main would have to verify:** Reproduce the U-matrix/Clifford identification and the K/Chern-form integral independently; recheck the CS5 descent's boundary bookkeeping (outer + source-tube + corner terms); and resolve which seat's "B1351" is meant before treating the acyclicity refutation as bearing on any specific main claim.
### R24 — the actual sourced field has nonzero total mass-eigenline flux
**Seat's verdict, quoted by the reader:** "The global boundary charge is computed, not inferred from three assumed Morse points. In R15's specified positive-source class, with every cusp incident to a source, the actual field obeys integral_(whole rounded boundary C) K = sign(q) * k... the existing three-arc construction has total flux +3 at positive charge. This is the same signed net chirality as R18/R19's conditional relative spectrum. The source selection, singular-domain law and quantum boundary completion are NOT consequences of this integer." Explicitly: "not an independently reviewed physical TOE."
**Tests on this bench:** ```
**Claims, graded as the seat grades them:**
  1. On R15's positive-source class, the total boundary flux of R23's mass-eigenline Chern form equals sign(q)·k, k = number of prescribed source arcs — PROVED-BY-SEAT (topological/Stokes argument plus exhaustion, "not only three: it is NOT a three-family selector").
  2. The mass-eigenline curvature form equals minus Nie's secondary Euler form under matched conventions, verified symbolically on two charts — COMPUTED (input theorem from Nie cited, not reproved).
  3. For k proper source arcs, χ(core)=−k, χ(source-tube)=0, χ(exterior cusp)=−2k, giving the stated per-sign incoming-region index — COMPUTED.
  4. A corollary: for k>0 the actual gradient must vanish somewhere in every admissible core (else Stokes is contradicted) — PROVED-BY-SEAT, with the explicit caveat "Neither Morseness nor exactly k points is proved."
**What main would have to verify:** Independently reconstruct U's action on the natural Levi-Civita connection (Γ⊗1+1⊗Γ) and confirm the K=−Φ identity against Nie's stated conventions; recheck the corner-rounding homotopy argument (frozen vs. variable field) and the cusp-asymptotic exhaustion order (high caps → small tubes → corners) before citing k=3 as anything beyond a topological identity in this fixed source class.
### R25 — the reference wall supplies the opposite response, with mirror modes
**Seat's verdict, quoted by the reader:** "Implementing R23's positive reference mass as a free physical collar produces a six-dimensional Weyl channel on the actual negative-mass eigenline. On R24's whole rounded source boundary its effective four-dimensional index is -k, opposite the interior +k. Its anomaly is the negative of the FULL R23 eigenbundle response... The cost is also computed: it is a mirror sector, and moving its normalized modes toward the ends does not decouple them from the unchanged normalizable constant gauge field... This is therefore an explicit conditional free completion, NOT a source-selected defect, a mirror-free physical theory, or a no-go for other completions. R19's conditional three/zero kernel is not 
**Tests on this bench:** ```
**Claims, graded as the seat grades them:**
  1. Interpolating R23's positive reference mass to a free scalar-mass "wall" on the source boundary produces a normalizable six-dimensional Weyl channel with four-dimensional index exactly −k (opposite the interior +k) — PROVED-BY-SEAT (within the stated free/product-collar ansatz).
  2. This wall's anomaly polynomial equals minus R23's full degree-eight eigenbundle response, for either reference sign — COMPUTED.
  3. Localizing the wall's modes toward the ends does not decouple them from the existing normalizable constant gauge zero mode (charge is not suppressed by small overlap) — PROVED-BY-SEAT (for the stated minimally-coupled constant-profile gauge field).
  4. This is "an explicit conditional free completion," not a derivation of a physical mechanism, source selection, or mirror-free spectrum — CONDITIONAL, as the seat itself states.
**What main would have to verify:** Reproduce the Gamma_r·∂_r+M_wall normal-mode solution and its normalization integral; independently confirm the compact-spin-surface Riemann–Roch index (deg S = g−1, twisted by L⁻) for the actual genus/k used; and check the gauge-coupling-independent-of-localization argument's dependence on the assumed finite, constant gauge-zero-mode profile before treating −k as a physically realized compensatin
### R26 — localized curvature can preserve the sourced chiral sector
**Seat's verdict, quoted by the reader:** "Conditional on R18/R19's strong-source maximal-domain theorem, the actual
graded Dirac index survives bounded Hermitian odd perturbations supported
in the regular interior, or uniformly vanishing at every end of the
punctured manifold. For the original pair-free sector, a perturbation
smaller in operator norm than the original positive gap preserves exactly
three odd and zero even zero modes... This answers the registered analytic
backreaction sub-question, not the stationary source/end problem... Only
this analytic stability sub-duty closes; a stationary source/end and
quantum completion remain open."
**Tests on this bench:** `python3 -m pytest tests/test_physical_bridge_index_stability*.py -q --no-header -p no:cacheprovider`
**Claims, graded as the seat grades them:**
  1. Bounded Hermitian odd perturbations, compactly supported in the regular
  interior or uniformly vanishing at all ends, preserve the graded Dirac
  index of the R18/R19 operator. — PROVED-BY-SEAT (conditional on R18/R19).
  2. Below the original spectral gap, such perturbations preserve the exact
  pair-free kernel (3 odd / 0 even zero modes). — PROVED-BY-SEAT
  (conditional; "no numerical value for delta has been computed").
  3. An explicit nonflat, compactly supported unitary connection at small
  nonzero amplitude belongs to this stable class. — COMPUTED (existence
  construction only; "not the solution of its Maxwell equation").
  4. Index stability without smallness does not imply pair-free stability,
  even with a noncompact resolvent. — PROVED-BY-SEAT (control example).
**What main would have to verify:** The R18/R19 domain construction and gap delta (external to this round);
the exterior/Clifford sign conventions from R23; independently re-derive
the resolvent-factorization self-adjointness argument and the Rellich
compactness step, since only algebraic/finite controls were executed here,
not the noncompact operator theorem itself.
### R28 — a stationary bulk field is not yet a dynamical source
**Seat's verdict, quoted by the reader:** "The prescribed chiral background is a stationary, zero-potential solution
of the adopted twisted bulk theory on the source complement. Its source
strengths and through-flux parameters are nevertheless nonnormalizable in
that theory's four-dimensional kinetic metric. Resolving a specified
commuting core has a sharp bare cost. These facts distinguish a useful
classical background from a complete source theory; they neither discard
R19's conditional modes nor complete the physical goal."
**Tests on this bench:** `python3 -m pytest tests/test_physical_bridge_source_action*.py -q --no-header -p no:cacheprovider`
**Claims, graded as the seat grades them:**
  1. The prescribed R15 background is a stationary, zero-potential minimum of
  the adopted twisted 7d SYM static potential off the source lines. —
  PROVED-BY-SEAT (conditional on the adopted action and R15 ansatz).
  2. Source residues and through-flux parameters have divergent (log-divergent
  or worse) kinetic norm in this fixed metric/action — they are
  nonnormalizable 4D scalar moduli. — PROVED-BY-SEAT (conditional; does not
  forbid the backgrounds, only says they are not ordinary finite-norm
  fields).
  3. Resolving a specified commuting abelian core at fixed flux has a sharp
  bare D-residual cost growing as epsilon^-2; a bounded-cost completion
  must change some declared input. — PROVED-BY-SEAT (scoped to "smooth
  commuting core," "stated flux/cap/commuting class").
  4. B1341's claimed extension to "no stationary action" for the half-step is
  false; a time-dependent Lagrangian and an enlarged multiplier action both
  supply one. — PROVED-BY-SEAT (counterexample), explicitly a "standard
  -action-class correction, not a novel theory or a retraction of the
  useful monodromy mathematics."
**What main would have to verify:** Whether B1341's own stated scope already restricts to regular-autonomous
same-state Lagrangians (in which case R28 is a scope clarification, not a
correction) or whether main's downstream summaries (VERDICT_LEDGER,
REPRESENTATION_TRIAGE, THE_ROLES_ACCOUNTING) overstate B1341 as "no
stationary action" without that qualifier, requiring a dated note like the
B766/B1083 precedent already in CAMPAIGN_S
### R29 — a coupled finite-width source, and the gauge mass it does not retain
**Seat's verdict, quoted by the reader:** "The added charge-four tube fields give a stationary zero-residual classical
source construction on compact truncations... The resulting extra-U1
transverse vector operator is derived... At finite radius on a compact
truncation its lowest eigenvalue is positive. The bare shrinking-tube
version does NOT retain a positive gauge gap on the stated bulk Hilbert
space, however large its nonnegative localized mass coefficient becomes...
This is a capacity effect, not a failure of the finite-width solution and
not an exclusion of renormalized defect theories."
**Tests on this bench:** `python3 -m pytest tests/test_physical_bridge_defect_gauge*.py -q --no-header -p no:cacheprovider`
**Claims, graded as the seat grades them:**
  1. A finite-width, stationary, zero-residual coupled classical source
  solution exists for the charge-four tube model on compact truncations
  with boundary. — PROVED-BY-SEAT (conditional on the added bosonic
  model's stated inputs).
  2. At any fixed finite tube radius on a compact truncation, the extra-U1
  transverse gauge operator has a strictly positive lowest eigenvalue. —
  PROVED-BY-SEAT (explicit Poincare-gap bound
  `lambda0 >= mu*delta/(2*delta+mu+2*K) > 0`; "no numerical value of
  delta on the actual cusp geometry was produced").
  3. As the tube shrinks to zero radius, the spectral bottom of this gauge
  operator tends to zero regardless of the mass coefficient's height — a
  codimension-two capacity effect, not exclusion of renormalized/finite-
  width defect theories. — PROVED-BY-SEAT.
  4. A literal delta-function line-mass term is not closable on the bulk
  Hilbert space (explicit non-Cauchy sequence). — PROVED-BY-SEAT.
**What main would have to verify:** The R21 H-subgroup construction and its charge-four character (external to
this round); independently re-derive the Poincare-gap bound's constants
mu, delta, K for the actual m202 cusp geometry, since "no numerical value
of delta on the actual cusp geometry was produced" here.
### R30 — what happens to the chiral sector when its cores are resolved?
**Seat's verdict, quoted by the reader:** "The added R29 source model now has an explicit quadratic fermion
extension with positive bulk kinetic norm, a self-adjoint compact operator
domain, and full transmission through artificial core interfaces. In this
specified smooth, flat/exact, absolute-boundary class, its finite-width
zero modes are ordinary twisted cohomology. The two nontrivial
source-C3-compatible m202 characters have no zero modes at finite width...
There is also a conditional low-energy result: sufficiently strong
shrinking logarithmic wells produce light opposite-chirality pairs, not a
proof that unwanted partners become heavy."
**Tests on this bench:** `python3 -m pytest tests/test_physical_bridge_resolved_fermion*.py -q --no-header -p no:cacheprovider`
**Claims, graded as the seat grades them:**
  1. In the added finite-width quadratic-fermion extension with absolute
  boundary data, the two nontrivial source-C3-compatible m202 characters
  have zero kernel (no zero modes) at every finite core width. —
  PROVED-BY-SEAT (conditional on the stated smooth/flat/absolute-boundary
  class; explicitly not a retraction of R19's singular three/zero result
  on its own different domain).
  2. Under additional quantitative well conditions (uniform log-behavior on
  an interior arc, a_j >= 1), resolving k source cores produces at least
  k light opposite-chirality Dirac pairs as width shrinks, not heavy
  partners. — CONDITIONAL ("this is not a certified global Poisson
  asymptotic for the actual m202 solution").
  3. (zeta,1),(zeta^-1,1) is not the source's actual C3-fixed character pair;
  the correct fixed points are (0,0),(1/3,2/3),(2/3,1/3) via the rebuilt
  action A=[[-1,-1],[1,0]]. — PROVED-BY-SEAT (self-correction of the
  round's own earlier design/test naming).
  4. Full-form transmission through an artificial core-cutting interface
  requires matching both normal and tangential Green-form data; tangential
  matching alone fails. — PROVED-BY-SEAT.
**What main would have to verify:** Independently reconstruct the R20 word-map action A=[[-1,-1],[1,0]] and its
three fixed torus points to confirm the corrected C3 locus; verify the
chain-homotopy attachment argument at t=0 vs. t!=0 for the k=3 case
directly against the frozen R19 Fox complex.
### R31 — actual compact Poisson wells and their light fermion partners
**Seat's verdict, quoted by the reader:** "The missing R30 estimate is supplied for one actual global source family,
not just its radial comparator... The solution is uniformly bounded off all
the arcs, including at the outer boundary. On any fixed small interior
observation cylinder around one arc, its difference from the matched
infinite hyperbolic tube potential is bounded uniformly in epsilon...
For the fixed compact normalized uniform-source family and R30's declared
absolute extending-flat fermion realization, the global potential has the
required interior logarithmic wells and off-source bounds; k strong arcs
with q beta_j >= 1 and nontrivial L therefore give at least k positive
light Dirac pairs as width tends to zero, not k
**Tests on this bench:** `python3 -m pytest tests/test_physical_bridge_global_poisson*.py -q --no-header -p no:cacheprovider`
**Claims, graded as the seat grades them:**
  1. For the fixed compact normalized uniform-source family, the global
  Poisson potential F_epsilon is uniformly bounded off all source arcs
  (including at the outer boundary) as epsilon -> 0. — PROVED-BY-SEAT
  (conditional on the fixed-geometry, fixed-strength hypotheses stated).
  2. On an interior subsegment, |F_epsilon - beta_j log r| <= C uniformly in
  epsilon, giving the logarithmic well needed by R30's light-mode
  argument. — PROVED-BY-SEAT (explicitly not uniform in cusp truncation
  length, not valid at an active Dirichlet endpoint).
  3. Consequently, k strong arcs with q*beta_j >= 1 and nontrivial extending
  line L give at least k positive light Dirac PAIRS as width -> 0, not
  k unpaired Weyl generations. — CONDITIONAL (composes claim 2 with R30's
  min-max mechanism; "no exactly-k count or lower mass bound follows").
  4. The hyperbolic point kernel g(d)=(coth d - 1)/(4*pi) and the compact
  Dirichlet Green-function bound derived from it are correct for this
  domain-monotonicity argument. — CITED + PROVED-BY-SEAT (kernel identity
  cited to Cohl-Kalnins; the compact-domain bound argument is the seat's
  own construction from it).
**What main would have to verify:** Independently confirm the Cohl-Kalnins H3 kernel normalization and the
seat's compact-domain Green-function monotonicity argument
(G_Q <= G_(Q+)); re-derive the source-mass bound "2 pi beta_j times arc
length plus O(beta_j epsilon)" and the matching-annulus parametrix error
bound used to transfer the infinite-tube comparator to the actual compact
solution, since these are the seat's own analytic c


## Two of main's own arcs are narrowed by this window
- **B1341 (the action of the object; from the paper-verification lane).** R28 §4 exhibits a time-dependent Lagrangian and an enlarged multiplier action that generate the anti-symplectic half-step. B1341's theorem stands for regular autonomous same-state discrete Lagrangians (the class it actually proves); its downstream summaries ("no stationary action") overstate it. Dated addendum on B1341; the paper-impact item that would have written "an action at the monodromy, provably obstructed at its square root" is NOT applied to the paper.
- **B1351's cusped half (the SM seat; harvested in B1411).** R23 §4 refutes, on explicit relative cochains for a disc partition, the statement "whole-cusp-torus acyclicity forces zero index for every Morse partition": with ∂⁺M a disc per source arc, H* = (0, k, 0, 0) and χ = −k. B1411 verified only the closed half; the cusped half holds for the whole-torus and annular conventions of ∂⁺M (rows A–C of chat1's I-26 table) and not for the disc conventions (rows D–F). Dated addendum on B1411.

## Fifteen documents, read
- `ASSELMEYER_MALUGA_READ.md` — Literature read (a direct, page-by-page reading and primary-source-checking log of sixteen Asselmeyer--Maluga arXiv papers, 448 pages, feeding a separate transf
- `ASSELMEYER_MALUGA_TRANSFER.md` — -
- `BIG_PICTURE_REVIEW_2026_09_10.md` — -
- `BOUNDARY_WALL_INTAKE.md` — A status/intake report on newly fetched branch heads following scientific runs, grading each new item as RECEIVED, capability, or independently checked.
- `CHIRALITY_REFRESH.md` — A cross-seat documentary audit (custody refresh + source correction), not a new B arc or numerical proof.
- `DEFECT_GAUGE_INTAKE_2026_09_13.md` — -
- `INDEX_STABILITY_INTAKE.md` — -
- `INDEX_STABILITY_REGRESSION_CAPTURE_LOSS.md` — A correction/incident note recording a failed test-run capture and the replacement procedure adopted.
- `JORGENSEN_SOURCE_AUDIT_2026_09_13.md` — -
- `MISSION_ROADMAP_2026_09_13.md` — -
- `MISSION_STATUS_2026_09_10.md` — -
- `OBSERVATIONAL_COMPATIBILITY_2026_09_13.md` — -
- `PUNCTURED_TORUS_GEOMETRY_2026_09_14.md` — -
- `PUNCTURED_TORUS_READING_2026_09_14.md` — -
- `R29.md` — -
- `R30.md` — -
- `RELAY_TRIAGE_2026_09_12.md` — A read-only triage of other seats' branches (index branch and outside bench), raising proof obligations rather than issuing verdicts.
The Asselmeyer-Maluga read (78 claims) agrees with main's adjudication (KNOWN-ADJACENT; the figure-eight named in none of the sixteen papers); the Jørgensen source audit agrees with B1345/chat1 (J(m004) = 1, Callahan); the punctured-torus geometry read is the lane's own literature intake (Minsky, Lackenby), now also in the paper's recognition list.

## What the seat is told
Harvest done for R21–R31. Its lane stays active. Owed by main: the B1335 domain correction (done here), the B1341 scope (done here), the B1351 cusped-half scope (done here). Owed by the seat: nothing.
