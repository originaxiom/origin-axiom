# Origin Axiom — Claims Ledger

**This is the living source of truth for what the project claims.** It is governed by
`GOVERNANCE.md`. Every result must appear here with an ID, a status label, and an evidence
pointer. Prose elsewhere in the repo may not exceed the label of the claim it rests on.

**Status labels:** `proven` · `conditional` · `open` · `dead` (see `GOVERNANCE.md` §3).
**Evidence** points to the test that locks the claim. All fifteen `proven` claims are locked
by passing tests. P1–P10 were frozen at tag `phaseA-foundation-freeze`; P11–P13 were added in
the session-3 integration; P15–P16 in the session-3 *synthesis* (P14 is intentionally unused).

**Last updated:** 2026-07-03 (the §5.1 promotion audit: +39 `proven` P17–P55, +7 `conditional` C6–C12, +15 certified-data E1–E15 — scrutiny record in `PROGRESS_LOG.md`; the original core P1–P16 unchanged) · the proven core P1–P16 is **unchanged through all frontier work to
date (B1–B352)** — **B69–B352 produced zero promotions** to this ledger (the SL(n) trace-map tower,
the chirality / class-S / firewall arc, the object-mapping arc — the four faces, the elliptic
curve `40a1`, the dual McKay `E₈`+`E₆`, the emergent `N=1` superconformal `c=7/10` symmetry — and the
structural-theorem arc B231–B314, the two-ended object / the cascade / Face IV / *the firewall as a
Galois theorem* (`knowledge/K020`, `philosophy/P013`) — all
live entirely in `frontier/` / `knowledge/` / `speculations/` / `papers/`; the
date/range lag is not claim drift) · proven ledger unchanged at 15 claims; C1 evidence upgraded by
`docs/UNIQUENESS_THEOREM.md`; C5 added as a conditional trace selector theorem; trace-map and spectrum
work B13–B47 otherwise remains frontier only.

> **Frontier navigational pointer.** Until 2026-07-03 none of the frontier work was promoted; the
> §5.1 audit changed that — its mathematics-tier results now sit above as P17–P55 / C6–C12 / E1–E15,
> each through the `§5` gates. What remains *unpromoted* (physics-boundary rows, computer-assisted
> evidence, exploratory arcs) is deliberately not here, by the firewall and the bar. For the honestly-labelled frontier results see: `knowledge/K020` (the current headline — the
> structural theorem as a Galois theorem), `docs/OPEN_PROBLEMS.md` (the current frontier — four gates),
> `CHANGELOG.md` (recent history), `ROADMAP.md` (the Phase B probe table), `papers/metallic_one_object/
> SYNTHESIS.md` (the four-faces map), `papers/VALIDATION_LEDGER.md` (`V1…V238`), `docs/OPEN_LEADS.md`
> (`L1…L50`), and `speculations/` (the firewalled physics readings).
> This pointer exists so a reader is not misled into thinking the rich frontier is *absent* — it is
> deliberately *not here*, by the firewall.

**2026-07-03 — the promotion-audit lane instituted (GOVERNANCE §5.1/§11).** The zero-promotions
posture above was Phase-B *practice*, not law. The §5 gates now run on a cadence (the decadal
review, `docs/progress/REVIEWS.md`) and a dedicated **promotion audit** is registered
(`docs/OPEN_LEADS.md`) to sweep B69–B370 for entries that meet the bars — mathematics is eligible
on its own terms; the framing lock is untouched. Entries land only through the gates, each logged.
A **Certified data** section (`E`-ids) is added below for exact computational exhibits.

---

## Proven — exact, checkable, safe to build on

| ID | Claim | Evidence |
|---|---|---|
| P1 | `L=[[1,1],[0,1]]`, `R=[[1,0],[1,1]]` are primitive parabolic shears; `A=LR=[[2,1],[1,1]]` has trace 3, det 1, `χ_A=t²−3t+1`, eigenvalues `φ²`, `φ⁻²`. | `tests/test_algebra.py` ✓ |
| P2 | `A = P·Nτ²·P` and `Aⁿ = P·Nτ²ⁿ·P`, where `Nτ=[[0,1],[1,1]]` is the Fibonacci fusion-count matrix and `P` the basis swap. | `tests/test_fibonacci.py` ✓ |
| P3 | `L+R=[[2,1],[1,2]]` is exactly a normalized 1D zero-field Ising transfer matrix at `K=½log2`; correlation length `ξ=1/log3`. | `tests/test_ising.py` ✓ |
| P4 | `A=LR` is exactly a Zimm–Bragg helix-coil transfer matrix at `s=2`, `σ=½` (weakly cooperative). | `tests/test_zimm_bragg.py` ✓ |
| P5 | Word-ensemble thermodynamics: `Z_N^count=2ᴺ`, `Z_N^trace=Tr((L+R)ᴺ)=3ᴺ+1`; thresholds `β_c^count=log2`, `β_c^trace=log3`. | `tests/test_thermo.py` ✓ |
| P6 | `L` and `R` preserve only degenerate symmetric forms; `A` preserves the non-degenerate `G=[[-2,1],[1,2]]`, signature (1,1), det −5; null directions of `G` = `φ`-eigenvectors of `A`. **Phase-space, not spacetime.** | `tests/test_preserved_form.py` ✓ |
| P7 | The gluing identity `S_A = ext_{m,s}[S_L − F_R + ms]` holds exactly (Sympy-verified); model-level. | `tests/test_gluing.py` ✓ |
| P8 | `|det(Aⁿ−I)|` equals the torsion order of `H₁` of the mapping torus of `Aⁿ`; `(1/n)·log|det(Aⁿ−I)| → log(φ²)`. | `tests/test_torsion.py` ✓ |
| P9 | Figure-eight knot (4₁): `vol≈2.0299`, `H₁=ℤ`, `CS=0`, amphichiral. Sister m003: same volume, `CS=0.25`, `H₁=ℤ⊕ℤ/5`. | `tests/test_snapdata.py` ✓ |
| P10 | The **trace-3 algebraic sieve** selects the figure-eight: among integer traces, only `tr=3` gives a torsion-free hyperbolic complement (PROVED). Four further filters (minimum hyperbolic volume [ties the sister m003 among all bundles, cf. P9, but **uniquely selects 4₁ among torsion-free** — m003 carries ℤ/5 torsion (B197); volume is unique-*given*-torsion-free, **not** an independent proof], amphichirality, rank-2 categorifiability, Eisenstein triangulation) **independently point to 4₁ but are documented, not proven to uniquely select it** — suggestive convergence, NEEDS-SPECIALIST. | `tests/test_sieve.py` ✓ (trace-3 sieve) |
| P11 | `log(A)` decomposes exactly in the sl(2,ℝ) basis as `a·H + d·(E+F)` with `a = log(φ²)/√5`; the ratio `d/a = 2` exactly and the antisymmetric `(E−F)` coefficient is exactly `0`. Pure algebra (a closed form for `log A`); no physical interpretation. | `tests/test_sl2_decomposition.py` ✓ |
| P12 | The figure-eight gluing equation `z²(z−1)²=1` (the SnapPy edge equation `z⁴−z²+2z−1` in the reciprocal `z→1/z` shape coordinate — see `topology.py`) factors exactly as `(z²−z+1)(z²−z−1)` — an Eisenstein quadratic (discriminant −3, the complete structure) times a golden quadratic (discriminant 5). | `tests/test_gluing_equation.py` ✓ |
| P13 | The shape matrix of `log A`, `[[1,2],[2,−1]]`, and the preserved form `G` are isospectral (both det −5, eigenvalues ±√5). Elementary corollary of P11 + P6. | `tests/test_preserved_form.py` ✓ |
| P15 | The Möbius action of `A` on `H`, `τ→(2τ+1)/(τ+1)`, has fixed points `φ`, `−1/φ`; its generating vector field (from `log A`, P11) is exactly `v(τ)=−κ(τ²−τ−1)` with `κ=2·log(φ²)/√5`. Exact: `v(φ)=v(−1/φ)=0`, `v(0)=κ≠0`. Pure algebra; no physical interpretation. | `tests/test_mobius_vector_field.py` ✓ |
| P16 | The gradient potential of P15's flow is `V(τ)=κ(τ³/3−τ²/2−τ)`, so `V′(τ)=κ(τ²−τ−1)`. Minimum at `φ` (`V″=+κ√5`), maximum at `−1/φ` (`V″=−κ√5`), and `τ=0` is **not** a critical point (`V′(0)=−κ`). Exact: integrate P15. No physical interpretation. | `tests/test_derived_potential.py` ✓ |

*(P14 intentionally unused — reserved during the session-3 synthesis numbering.)*

### Promoted by the 2026-07-03 audit (GOVERNANCE §5.1; scrutiny recorded in `PROGRESS_LOG.md`)

| ID | Claim | Evidence |
|---|---|---|
| P17 | Deck equivariance of the level-15 pair invariant: for the 3-fold fiber cover of the golden bundle (theta-lift `W₁³`) and partner m=2, `t_cover(a,b) = t_base(7a mod 20, b)` exactly on all 240 cells (`P_a(W^k)=P_{k⁻¹a}(W)` for gcd(k,ord)=1); the tower singles `W₁^k` (k=2..5) have exactly zero √−3, √−15 components. | `frontier/B368_cover_tower` · `tests/test_b368_cover_tower.py` ✓ |
| P18 | Concatenation kills the seam: each two-block word `R^{m₁}L^{m₁}R^{m₂}L^{m₂}`, (m₁,m₂) ∈ {(1,2),(2,1),(1,3),(2,3),(3,4),(1,4)}, is seam-null at level 15 (all eigenprojector Par-readouts exactly free of √−3, √−15) while the (3,4) *pair* is seam-bright; cyclic rotation acts on the readout by the √5-Galois involution, `r₍₂,₁₎(a) = σ(r₍₁,₂₎(a))` exactly. | `frontier/B369_concatenation_kill` · `tests/test_b369_concat_kill.py` ✓ |
| P19 | The seam dichotomy at level 15: the theta-lifted Par-inserted pair invariant of (golden, silver) has nonzero √−15 component on 44/49 nonzero doubles (exact, ℚ(ζ₆₀) Fractions; three independent computations agree), the canonical Par-commuting lift's √−15 component vanishes identically, and every single-seed control is exactly √−3/√−15-free. | `frontier/B358_seam_certification` · `tests/test_b358_seam_certification.py` ✓ |
| P20 | Non-locality of the seam form: the exact six-pair value map does not factor through (m mod 3, m mod 5, CRT labels) in the declared three-factor product class (true data inadmissible; 0/200 matched random tables pass the identical solver), and the ellipticity-type selection rule is refuted by (3,4) bright vs (1,3) dark with identical covering pattern. | `frontier/B367_value_map` · `tests/test_b367_step0.py` ✓ |
| P21 | The metallic-tower sector-assignment formula k(α) proved full-symbolic at SL(3), with the Dickson parity `L_k(−m) = (−1)^k L_k(m)`; the SL(4) instance verified. | `frontier/B64_parity_mechanism` · `tests/test_b64_parity_mechanism.py` ✓ |
| P22 | The SL(4) fixed-line Jacobian J(m) over ℤ[m]: char poly = the seven Dickson factors — proved twice independently (B65 direct symbolic reconstruction + exact factorization; B80 CRT/F_p first-principles construction, gate-checked agreement). | `frontier/B65_sl4_symbolic_jacobian` · `tests/test_b65_sl4_symbolic_jacobian.py` ✓ |
| P23 | The SL(2,ℂ) metallic trace-map fixed locus reproduces the figure-eight A-polynomial in literal equality with the published Cooper–Long form (route novelty not claimed). | `frontier/B67_figure_eight_apolynomial` · `tests/test_b67_figure_eight_apolynomial.py` ✓ |
| P24 | The SL(3) figure-eight character variety from the trace-map fixed locus: exactly three components, each of dimension 2 (exact sympy; agrees with the published Heusener–Muñoz–Porti / Falbel picture), with `M³ = L`. | `frontier/B71_sl3_apoly` · `tests/test_b71_sl3_apoly.py` ✓ |
| P25 | `M⁴ = L` symbolic-exact over ℚ(ω) on the SL(4) figure-eight component (upgrading the prior 1e−31 numerics). | `frontier/B89_sl4_symbolic_M4L` · `tests/test_b89_sl4_symbolic_M4L.py` ✓ |
| P26 | The peripheral form L1b: `XμX⁻¹ = μ_A` holds uniformly in n (a random non-bundle control fails it). Scope note: L1a (a relabelled tautology) and the refuted Cayley–Hamilton mechanism are explicitly NOT part of this claim. | `frontier/B90_degree_rank_peripheral` · `tests/test_b90_degree_rank_peripheral.py` ✓ |
| P27 | The metallic-family classification criterion: period-1 eigenvalue continued fraction ⟺ the (tr, det) criterion (finite verification, entries ≤5, plus standard CF theory; scoped per the recorded self-correction). | `frontier/B92_metallic_classification` · `tests/test_b92_metallic_classification.py` ✓ |
| P28 | det = −1 is exactly the metallic tower's parity (the parity sectors coincide with the det = −1 locus). | `frontier/B93_det_parity_bridge` · `tests/test_b93_det_parity_bridge.py` ✓ |
| P29 | Tower universality at ranks 3, 4 (exact): the Dickson catalog is universal; the parity phenomenon is det = −1-specific. | `frontier/B94_tower_universality` · `tests/test_b94_sl2_nonsquare.py` + `tests/test_b94_tower_universality.py` ✓ |
| P30 | The SL(2) trace-map Jacobian at the figure-eight geometric representation has eigenvalue field exactly ℚ(√−3) — the invariant trace field. | `frontier/B98_geometric_jacobian` · `tests/test_b98_geometric_jacobian.py` ✓ |
| P31 | The SL(n) figure-eight trace-map Jacobian is a GL(2,ℤ) representation with class-function universality for all n; the constructive module isomorphism `ρ_n = ⊕_d Sym^d(M_m)^{μ_d}` exact over ℚ[m] at n = 3, 4 (the explicit catalog for n ≥ 5 remains open). | `frontier/B103_tower_equivariance` · `tests/test_b103_tower_equivariance.py` ✓ |
| P32 | The SL(4) Dehn-twist catalog theorem: `char(J(N)) = ∏_d char(Sym^d N)^{μ_d}` for all metallic and non-metallic monodromies computed (the SL(5) wall is a characterized computational degeneracy, not part of the claim). | `frontier/B104_dehn_twist_tower` · `tests/test_b104_dehn_twist_tower.py` ✓ |
| P33 | The opposition-involution height lemma (Tier 1 only, per the probe's own relabel): θ = −w₀ on A_{n−1} height-h roots has (+1,−1)-eigendimensions (⌈(n−h)/2⌉, ⌊(n−h)/2⌋) for all n (elementary hand proof). | `frontier/B112_closed_form_proof` · `tests/test_b112_closed_form_proof.py` ✓ |
| P34 | Metallic block bundles are amphichiral ⟺ the block-length sequence is a cyclic palindrome — a corollary of the published Goodman–Heard–Hodgson (2008) criterion plus an exhaustively certified string identity (5460 cases); adversarial novelty audit recorded. | `frontier/B134_chirality_recursion_proved` · `tests/test_b134_chirality_recursion_proved.py` ✓ |
| P35 | The amphichirality criterion for ALL once-punctured-torus bundles (reverse-order + component-swap invariance of the LR word), same GHH-2008 basis, exhaustively certified (7380 cases); specializes to the metallic palindrome law. | `frontier/B136_general_amphichirality` · `tests/test_b136_general_amphichirality.py` ✓ |
| P36 | The principal-image sealing lemma (all n, hand proof): the `Sym^{n−1}` image of an SL(2,K) representation is a trace-map fixed point with all word-traces in K (the converse remains open). | `frontier/B138_s031_principal_lemma` · `tests/test_b138_s031_principal_lemma.py` ✓ |
| P37 | B89's family is the COMPLETE irreducible SL(4) figure-eight component for A-spectrum {1,1,ω,ω²}, and `M⁴ = L` is unconditional on the irreducible locus (exact ideal decomposition over ℚ(ω) + exact F_p Burnside; the decisive cell is empty). | `frontier/B149_sl4_ideal_completeness` · `tests/test_b149_sl4_ideal_completeness.py` ✓ |
| P38 | degree=rank is rank-stratified: a genuine component at n=3 (exact/F_p), a measure-zero slice at n=4 (exact/ℚ(ω)), absent for the principal finite-order family at n=5 (proven). The n=5 non-semisimple existence side is verified-numerical and excluded from this claim. | `frontier/B153_degree_rank_degeneration` · `tests/test_b153_degree_rank_degeneration.py` ✓ |
| P39 | The six Ω strict-full theorems (R/G algebra; TC-2 reciprocity; history-entropy = log 2; TC-1 unique minimal seed Ω₄; TC-4 orientation no-go; Fibonacci block-count), independently re-derived and adversarially verified (novelty NOT claimed — NEEDS-SPECIALIST stands). | `frontier/B156_omega_strict_full_cone` · `tests/test_b156_omega_strict_full_cone.py` ✓ |
| P40 | The WRT level-period law for once-punctured-torus bundles: `P = lcm(a,b)(4+ab)/gcd(4+ab,4)`, proved via Landsberg–Schaar + two-dimensional Gauss reciprocity (framework of Jeffrey 1992 cited; novelty not claimed). | `frontier/B204_metallic_wrt_period` · `tests/test_b204_metallic_wrt_period.py` ✓ |
| P41 | squarefree(m²+4) divides the metallic WRT period P(m) — hand proof unifying the level-period law and the congruence shadow. | `frontier/B208_period_congruence_unification` · `tests/test_b208_period_congruence_unification.py` ✓ |
| P42 | The metallic congruence law: `RᵐLᵐ ≡ I (mod p)` for p | m²+4 ⟺ p = 2 and m even (corrects the earlier silver framing). | `frontier/B212_silver_congruence_holonomy_shadow` · `tests/test_b212_silver_congruence_holonomy_shadow.py` ✓ |
| P43 | Golden is the unique metallic mean in the Jones window: λ_m < 2 ⟺ m = 1 (φ = 2cos(π/5)) — the unique anyon-realizable member (elementary exact). | `frontier/B218_metallic_anyon_selection` · `tests/test_b218_metallic_anyon_selection.py` ✓ |
| P44 | The class-field period law is form CONTENT: `P(γ) = lcm(t−2, t+2)/content(γ)`, exhaustively exact through f = 8, with the 2-adic mechanism lemma proved (all-t closure open). | `frontier/B219_period_content_law` · `tests/test_b219_period_content_law.py` ✓ |
| P45 | The golden chain's critical CFT is exactly c = 7/10 = M(4,5), the tricritical Ising model — the first N=1 superconformal minimal model (three exact derivations; identification of a classical SCFT). | `frontier/B221_golden_chain_susy` · `tests/test_b221_golden_chain_susy.py` ✓ |
| P46 | M(4,5) is the unique unitary minimal model (c < 1) that is also N=1 superconformal — hence golden is the unique metallic member whose chain is superconformal (exact rational). | `frontier/B224_golden_unique_susy_metallic` · `tests/test_b224_golden_unique_susy_metallic.py` ✓ |
| P47 | SU(2)₃ is the unique level at which the ordinary and N=1 minimal-model coset constructions coincide ((m, m′) = (4,3) unique; exact rational) — the mechanism behind the golden SUSY-uniqueness. | `frontier/B228_golden_susy_coset_mechanism` · `tests/test_b228_golden_susy_coset_mechanism.py` ✓ |
| P48 | The unimodular trace-field law: disc = t² − 4 ⇒ the only imaginary-quadratic trace fields are ℚ(i) and ℚ(√−3) (floor −4); ℚ(√2) (the E₇ candidate) is parity-excluded. Elementary proof. | `frontier/B239_reconciled_trace_field_law` · `tests/test_b239_reconciled_law.py` ✓ |
| P49 | Niven's theorem forces the figure-eight orbifold's dual-McKay pair to be exactly E₆ + E₈ and geometrically excludes E₇ (hand proof; geometry/McKay statement — no physics content). | `frontier/B249_niven_trinity` · `tests/test_b249_niven_trinity.py` ✓ |
| P50 | dim H¹(π₁(4₁), Ad ρ_prin) = 6 = rank(E₆), with tangent directions beyond F₄ (the {4,8} pair) — exact Fox calculus; a worked E₆ instance of the cited Menal-Ferrer–Porti / Falbel–Guilloux framework. | `frontier/B264_e6_character_variety` · `tests/test_b264_e6_character_variety.py` ✓ |
| P51 | ρ_prin is a smooth point of the figure-eight's E₆ character variety (dimension 6): the e₆ quadratic cup obstruction vanishes identically (exact mod large primes + Schwartz–Zippel) and the cited smoothness criterion applies — E₆-irreducible flat connections on 4₁ exist unconditionally. | `frontier/B273_e6_obstruction` + `frontier/B274_all_orders_smoothness` · `tests/test_b273_e6_obstruction.py` + `tests/test_b274_smoothness.py` ✓ |
| P52 | The amphichiral symmetry τ of 4₁ fixes BOTH spin structures (hand proof: the Spin torsor plus ambient invariance of the S³-bounding structure). | `frontier/B279_spin_structure_bit` · `tests/test_b279_spin_structure_bit.py` ✓ |
| P53 | m004(0,1) is the unique Sol torus-bundle among the ten exceptional fillings of the figure-eight, with monodromy exactly A = LR (homology-forced uniqueness; verified three independent ways). | `frontier/B287_distinguished_closing` · `tests/test_b287_distinguished_closing.py` ✓ |
| P54 | No hyperbolic knot has a cyclic-cubic (C₃) invariant trace field: C₃ Galois ⇒ totally real, while a hyperbolic invariant trace field always has a complex place (hand proof; 500-manifold census illustration). | `frontier/B307_totally_real_obstruction` · `tests/test_b307_totally_real_obstruction.py` ✓ |
| P55 | The classical interface laws: the divisibility law `RᵐLᵐ ≡ I (mod p) ⟺ p | m`, and the Gröbner-exact strong-channel kill (the classical pair-point fields admit no quadratic subfield — the classical seam-null). | `frontier/B354_interface_pairing_certificates` · `tests/test_b354_interface_pairing_certificates.py` ✓ |
| P56 | The minimal two-state sector: the level-15 quantization contains a 2-dim subspace (the a∈{6,14} eigenspaces of `W₁`) invariant under the full Weil image, irreducible via the global dihedral relation `ŜW₁Ŝ⁻¹ = W₁⁻¹`, with helicity pairing (`tr ρ(Ŝ) = 0`, eigenvalues exactly ±ζ₆₀⁹, swapped by Ŝ), golden action by exactly the pentagon angle (`tr ρ(A₁) = tr ρ(A₄) = 1−φ`; seeds 2,3 trace 1), and seam self-coupling at exactly ±1/48 on the cells {6,14}×{2,10} of the banked (1,2) table. | `frontier/B371_minimal_two_state_sector` · `tests/test_b371_two_state_sector.py` ✓ |
| P57 | The true parity and the Weyl identity of the level-15 theta model: naive parities do not commute; the parity is `J = Ŝ²` (`Ŝ = D⁻¹·WR·D⁻¹`), monomial with support `j → 1−j`, commuting exactly with both generators; and `J·Par = ζ₆⁻¹·X·Z` exactly — the banked Par-inserted pair observable inserts the elementary Weyl operator XZ up to parity sign and a fixed sixth root (the seam = a parity-signed one-step hopping amplitude between spectral projectors). | `frontier/B371_minimal_two_state_sector` · `tests/test_b371_two_state_sector.py` ✓ |

*Provenance of P7 and P9 (the `proven` basis made explicit):* **P7** is an exact identity
verified in Sympy — computer-assisted-exact, not a hand proof. **P9** is figure-eight / m003
census data (volume, `H₁`, Chern–Simons, amphichirality) from SnapPy plus the standard
literature — software-verified established census facts. Both are `proven` on that basis;
all other P-claims are exact algebra / standard sieve results.

The field-theoretic lift of P15/P16 — the field equation `□τ+κ(τ²−τ−1)=0`, the
Fisher–KPP creation dynamics, the particle spectrum (including the **non-exact**
near-miss `m/g≈φ`), and the fusion–scattering shared polynomial — is **frontier,
not proven**. See `frontier/B6`–`B9` (each carries its caveat). The polynomial
`τ²−τ−1` appears across six contexts (golden ratio; `charpoly(F)`; the Möbius
force law P15/P16; Fibonacci fusion P2; the Markov/Hurwitz constant via
`disc=5`; the attractor `x=1+1/x`); `scripts/six_faces.py` checks each. The
*identification that they are the same polynomial* is the observation — see
`PROGRESS_LOG.md` 2026-05-27 for the independence audit (1 defining + 4
independent + 1 via-discriminant).

---

## Conditional — true only given assumptions that were chosen, not forced

| ID | Claim | Named assumption |
|---|---|---|
| C1 | `L` and `R` are *forced* as the primitive record moves; extended: the first mixed closure is forced to `A = LR` *up to order* (trace 3, φ-spectrum), 144→1 under the torsion-free filter. | Depends on the minimal record axioms A1–A6 (see V4 paper §2). Formalized + machine-checked: `docs/UNIQUENESS_THEOREM.md`, `tests/test_uniqueness_theorem.py` ✓. Stays `conditional` (axioms motivated, not forced). |
| C2 | The Fibonacci `|F|²` probability matrix is reconstructed from `A`'s Perron eigenvector. | Requires an additional "Perron-switch / degeneracy" rule; plain MaxEnt gives ½,½. |
| C3 | Trace 3 is the unique torsion-free hyperbolic trace. | Holds only within once-punctured torus bundles with `SL(2,ℤ)` monodromy. |
| C4 | The `(disc 5)(disc −3)` state-integral factorization is unique to the figure-eight. | Verified for 11 census manifolds only — a census check, not a proof. |
| C5 | The primitive projective tangent return selects the `A` sector `t²−3t+1`, hence `I=1/4` and dimensionless `lambda/h=1`. | Depends on **T1**: the primitive projective tangent return inherits the original arithmetic persistence filters. Formalized in `docs/TRACE_SELECTOR_THEOREM.md`; locked as frontier evidence by B38-B47; the post-T1 algebra (`mu=4I+2`, T1-filters ⟹ `mu=3` ⟹ `I=1/4` ⟹ `lambda/h=1`, the Lucas-hierarchy control, and its identity with the P8 torsion ladder) is test-locked by `tests/test_trace_selector_c5.py` ✓ (2026-07-01 audit — C5 was previously the one ledger entry with no executable evidence). Stays `conditional`; T1 is motivated, not derived. |
| C6 | Within the named premise — pair states realized as level-15 theta functions on the fiber torus with the standard Heisenberg/metaplectic action — the half-characteristic (seam-bearing) polarization is the unique one whose geometric S-transformation closes at fixed modulus (the canonical polarization's S-image lives at (z/2, τ/4)), and it contains the unique MCG-invariant spin sector; hence the theta lift is forced and the B358 seam form is an invariant of the quantized pair. | The quantization premise (level-15 fiber theta functions) is chosen, not forced. Evidence: `frontier/B366_invariant_spin_sector` · `tests/test_b366_invariant_spin_sector.py` + `tests/test_b366_s_transformation.py` ✓ |
| C7 | Within the principal (finite-order, multiplicity-(n−2)) family, the spectrum is forced ({1,i,−i}; {1,1,ω,ω²}; {1,1,1,−1,−1}) and degenerates at n ≥ 5 (A² = I ⇒ dihedral ⇒ reducible). | The principal/finite-order ansatz (named); the full degree classification is open. Evidence: `frontier/B95_degree_rank_mechanism` · `tests/test_b95_degree_rank_mechanism.py` ✓ |
| C8 | IF the complexified Fibonacci trace map is uniformly hyperbolic on its non-escaping set, THEN the off-axis (κ<2) spectrum is a Cantor set; the Fricke–Vogt conservation leg is exact. | Uniform hyperbolicity off-axis — named, NEEDS-SPECIALIST. Evidence: `frontier/B165_kappa_cantor_offaxis` · `tests/test_b165_cantor_offaxis.py` ✓ |
| C9 | Within five named invariant classes (trace-ring / WRT / Eisenstein-CP / cover-torsion / H¹), every discrete trace-map invariant is a symmetrizable Galois orbit — no forced choice. | The five classes are an enumerated horizon, not exhaustive. Evidence: `frontier/B330_s032a_galois_symmetrization` · `tests/test_b330_s032a_galois_symmetrization.py` ✓ |
| C10 | The figure-eight's Bloch/scissors class β = 2[e^{iπ/3}] is a self-symmetrized Galois orbit {β, −β}, with the exact seam identity 1 − z₀ = z̄₀. | Gate-A class extension of C9's framework (same horizon caveat). Evidence: `frontier/B348_bloch_class_galois` · `tests/test_b348_bloch_class_galois.py` ✓ |
| C11 | All covers of 4₁ through index 6 are canonical multisets; every within-index invariant multiplicity is resolved by isometry — no forced choice at this horizon. | The index ≤ 6 horizon (named). Evidence: `frontier/B349_irregular_covers_galois` · `tests/test_b349_irregular_covers_galois.py` ✓ |
| C12 | The cyclic-cover abelian torsion class is a symmetrizable Galois orbit: orders = the Lucas ladder L₂ₙ − 2 (exact) with the deck action fixed-point-free for all n (exact) — no forced choice in this class. | Class-level statement (the no-forced-choice conclusion is horizon-bound; the ladder and deck facts are exact). Evidence: `frontier/B350_cyclic_cover_torsion_galois` · `tests/test_b350_cyclic_cover_torsion_galois.py` ✓ |

---

## Certified data — exact computational exhibits (reproducible, test-locked; data, not statements)

*(Instituted 2026-07-03, GOVERNANCE §5.1. Seeded by the promotion audit; entries land only through
the gates. `E`-ids.)*

| ID | Exhibit | Evidence |
|---|---|---|
| E1 | The seam flagship and table: `tr(Par·P₀Q₄) = −1/48 − (1/80)√5 − (1/48)√−3 + (1/48)√−15` exactly, and the 49-double H-valued table for the (golden, silver) theta-lift pair. | `frontier/B358_seam_certification` · `tests/test_b358_seam_certification.py` ✓ |
| E2 | The complete exact six-pair seam tables over seeds {1,2,3,4} (entries in ℚ(√5,√−3), no floats): forced row/column sum rules; aggregates Σs² = 43/7200, 1/2304, 3/3200, 1/192, 0, 0; the (1,2) matrix of rank 4 with Coxeter antisymmetry and disjoint {4,8}-sector support. | `frontier/B367_value_map` · `tests/test_b367_step0.py` ✓ |
| E3 | The (golden, silver) gluing fork, exact: κ discretized to exactly {−4, −2} (Bézout/resultant); mechanism lineage (Kitano–Nozaki 2020) cited. | `frontier/B131_two_seed_fork` · `tests/test_b131_two_seed_fork.py` ✓ |
| E4 | An integer SL(4,ℤ) matrix realizing golden × phase: charpoly (x²−3x+1)·Φ₆, genuine ℚ-block split, invariant form of signature (1,3) with disc −15, glue (ℤ/2)² — all exact (a spectral-arithmetic exhibit; no dynamical claim). | `frontier/B155_golden_phase_bridge` · `tests/test_b155_golden_phase_bridge.py` ✓ |
| E5 | The Ω strict-full class-graded DAG, depths L4–L10: exact class counts (1, 2, 6, 18, 49, 115, 283); all 474 charpoly classes reciprocal; independently re-enumerated from scratch at L4–L7. | `frontier/B159_omega_class_dag` · `tests/test_b159_omega_class_dag.py` ✓ |
| E6 | The metallic unification table: gap frequency, monodromy trace m²+2, dynamical degree λ_m², trace field ℚ(√(m²+4)), Hurwitz constant, and the Dickson eigenvalues — each an exact function of λ_m over ℚ(m), with the do-not-conflate boundary. | `frontier/B179_metallic_numbers_unified` · `tests/test_b179_metallic_numbers_unified.py` ✓ |
| E7 | The four silver SL(3) character-variety components: all irreducible (Burnside dimension 9) and cusped/loxodromic type (exact Sage/QQbar classification). | `frontier/B203_silver_components_classified` · `tests/test_b203_silver_components_classified.py` ✓ |
| E8 | The golden monodromy's mod-disc image: 2I = SL(2,𝔽₅) (surjection of order 120, 9 classes, dimensions = the E₈ marks) — exact finite-group computation. | `frontier/B206_golden_spin_cover_e8` · `tests/test_b206_golden_spin_cover_e8.py` ✓ |
| E9 | The figure-eight non-abelian SL(2,ℂ) character curve is birational to elliptic 40a1, with #X(𝔽_p) = p − 1 − a_p(40a1) verified exactly at 23 primes (novelty not claimed). | `frontier/B211_metallic_arithmetic_geometric_faces` · `tests/test_b211_metallic_faces.py` ✓ |
| E10 | The explicit metallic Seifert duals S²((m²+4, m²+3), (m²+3, 1), (3, 1)): largest cone order = m²+4, |H₁| = (2m²+7)² + 2 (exact invariants; construction recipe cited). | `frontier/B227_metallic_seifert_duals` · `tests/test_b227_metallic_seifert_duals.py` ✓ |
| E11 | The binary-polyhedral quotient census: silver carries no 2O; 2O absent from golden/silver/bronze; the quotient structure is manifold-specific (exact GAP; includes the recorded refutation of a relayed universality claim). | `frontier/B237_silver_2O_l48` · `tests/test_b237_silver_2O.py` ✓ |
| E12 | Golden integrality: [N]·J_N(4₁; e^{2πi/5}) = {1, −2, −2, 1} (Galois-rigorous, exact); among amphichiral knots of ≤10 crossings only 4₁ is pure-ℤ (the physics reading stays HELD). | `frontier/B240_golden_jones_integrality` · `tests/test_b240_golden_jones.py` ✓ |
| E13 | H₁ of the 3-fold cyclic cover of 4₁ = ℤ ⊕ (ℤ/4)² with the deck ℤ/3 acting irreducibly (Φ₃ mod 4) — verified two independent ways (SnapPy + the exact Alexander module). | `frontier/B326_congruence_torsion` · `tests/test_b326_congruence_torsion.py` ✓ |
| E14 | dim H¹(4₁, Sym^{2m}) = 1 per E₆ exponent (six blocks; discrete rank-cliff outputs at ~10⁸⁵ margins) with the hyperelliptic θ-grading (−1)^{m+1} = the E₆ → F₄ split (second path: the exact total of the E₆ tangent claim + independent per-block rank cliffs). | `frontier/B347_e6_tangent_gradings` · `tests/test_b347_e6_tangent_gradings.py` ✓ |
| E15 | The exact pair-point minimal polynomials: (1,3): T⁵−13T⁴+60T³−121T²+114T−47; (2,3): T³−16T²+68T−72 (odd degree ⇒ no quadratic subfield). | `frontier/B354_interface_pairing_certificates` · `tests/test_b354_interface_pairing_certificates.py` ✓ |
| E16 | The exact level-45 tables (seeds 1, 2): singles = exactly four nonzero cells (a ≡ 1 mod 15), each exactly 1/4, purely rational; the full 60×12 pair table has 144 nonzero cells, every one carrying √−15-type content and genuine ℚ(ζ₉)⁺ dependence — the seam persists at level 45 and its arithmetic home is the 12-dim compositum ℚ(ζ₉)⁺·ℚ(√5,√−3). CRT/F_p exact (3 primes, held-out-embedding verified; the N=15 pipeline gate reproduces the banked flagship). | `frontier/B372_level45_sweeper` · `tests/test_b372_level45.py` ✓ |

---

## Open — research targets (Phase B / `frontier/`). NOT partial results.

| ID | Target |
|---|---|
| O1 | Physical spacetime emergence (beyond a phase-space form). |
| O2 | Derivation of 3+1 dimensions. |
| O3 | Einstein's field equations. |
| O4 | Matter / Standard Model content. |
| O5 | The cosmological constant. |
| O6 | The fine-structure constant. |
| O7 | Any empirical prediction outside toy/transfer models. |
| O8 | Fibonacci `F`-symbol amplitudes and `R`-symbol phases (i.e. genuine anyon physics). |
| O9 | Derivation of the marked cusp incidence data from the action alone. |

Handoff-document steps 3B → 6 ("path to Einstein") map onto O1–O5. The first concrete
frontier probe is whether the gluing identity `W = S_L − F_R + ms` maps onto the discrete
Chern–Simons flatness condition `F = 0` — a well-defined yes/no computation.

Current trace-map frontier work (B13-B47) refines O1-O8 but does not close any
of them. The half-step trace lift is canonical, the `SL(3)` lift preserves the
`A` sector as higher-rank trace algebra, and the Fibonacci spectrum at
dimensionless `lambda/h=1` is a useful finite-approximant anchor. The selector
bottleneck is isolated as C5: `lambda/h=1` follows from T1, the assumption that
the primitive projective tangent return inherits the original arithmetic
persistence filters. The required physical dictionaries remain open.

---

## Dead — falsified or shown circular. Permanent. See `docs/ARCHIVE.md`.

| ID | Killed claim | Why it died |
|---|---|---|
| D1 | `k ≈ 137` sets the cosmological constant. | Wrong Chern–Simons normalization; correct scaling gives no special `k`. |
| D2 | `Λ = Λ_Planck · φ⁻²ᴺ`. | Circular — `N` is defined by the answer it is meant to predict. |
| D3 | Dynamic dark energy `Λ(t)`. | Predicts `w ≈ −0.04`; ruled out at ~30σ by observation. |
| D4 | `|Z| = 1/φ` is a unique signature of the figure-eight. | Generic feature of level-5 `SU(2)` cyclotomic algebra. |
| D5 | Casimir energy depends on `φ`. | Leading-order Casimir energy is universal across cavity ratios. |
| D6 | Phonon zero-point stability is maximized at `φ`. | Coefficient of variation is flat across mass ratios. |
| D7 | The figure-eight cusp minimizes the Epstein zeta function. | The figure-eight cusp is rectangular, not equilateral. |
| D8 | Positive `L`, `R` satisfy the braid relation `LRL=RLR`. | Direct computation: `LRL ≠ RLR`. |
| D9 | The `φ^φ` axiom. | Tested computationally in early work; failed. |
| D10 | `θ*` extracted from CKM/PMNS observables is a *derivation*. | It is a one-parameter fit, not a derivation. |
