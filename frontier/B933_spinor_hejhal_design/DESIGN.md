# B933 — The spinor-Hejhal design: the Dirac spectrum of m004

**Status:** DESIGN + executed feasibility probe (double precision, unsealed).
**Date:** 2026-08-06 · **Seat:** computation agent (cc bench).
**Authorization:** the B921-harvested Cell-3 spin fork
(`frontier/B921_branch_harvest/harvested/frontier/B796_coupling_campaign/cell3_spin_fork.*`):
ρ₁ = (A, B) has peripheral trace pattern (2, −2), non-Lie under BOTH sign
conventions ⟹ by Bär's dichotomy the Dirac spectrum of (m004, ρ₁) is
DISCRETE ⟹ the spinor-Hejhal computation is authorized unconditionally.
**Parent instrument:** the scalar Hejhal solver
(`frontier/B878_maass_upper_window/branch_hejhal_m004.py`) and the B922
certified 25-digit scalar protocol (`frontier/B922_lambda2_receipt/FINDINGS.md`).

Mathematics lane. No measured physical number is contacted anywhere in this
design or its probe.

---

## 1. The object

m004 = Γ₄₁\H³, Γ₄₁ = ⟨A, B⟩ the Riley holonomy, A = [[1,1],[0,1]],
B = [[1,0],[−ω,1]], ω = (−1+i√3)/2. H¹(m004; ℤ/2) = ℤ/2 ⟹ exactly two spin
structures = the two SL(2,ℂ) lifts ρ₁ = (A,B), ρ₂ = (−A,−B) (Cell 3,
exact). The fork's data:

| lift | tr(meridian a) | tr(longitude bABaaBAb) | cusp spin structure |
|---|---|---|---|
| ρ₁ | +2 | −2 | non-Lie under BOTH conventions ⟹ **discrete Dirac spectrum** |
| ρ₂ | −2 | −2 | convention-dependent (Lie under C1, non-Lie under C2) |

**This design targets ρ₁ only.** ρ₂'s status is unresolved until the C1/C2
trace-sign dictionary is pinned (obligation O4, out of scope): if ρ₂ is Lie
its essential spectrum is ℝ and no Hejhal method applies to it.

## 2. The operator and every declared choice (WORKING_RULES rule 4)

- **Coordinates**: upper half-space (z, t), z = x + iy, metric
  (|dz|² + dt²)/t², volume t⁻³ dx dy dt.
- **Frame**: (e₁, e₂, e₃) = (t∂ₓ, t∂_y, t∂ₜ), in this order.
- **Trivialization**: the Iwasawa section s(z,t) = [[√t, z/√t],[0, 1/√t]]
  (maps the base point (0,1) to (z,t)); spinor bundle
  Σ = SL(2,ℂ) ×_{SU(2)} ℂ².
- **Clifford/spinor convention**: c(e_i) = σ_i (standard Pauli),
  σ₁σ₂σ₃ = i·I fixing the orientation class.
- **The operator**:

  D = −i [ t(σ₁∂ₓ + σ₂∂_y + σ₃∂ₜ) − σ₃ ]

  Derived three independent ways, all agreeing: (i) Koszul + the spin
  connection with the connection-term sign fixed by the Clifford-compatibility
  bracket identity (with c² = +1 Pauli conventions the Lawson–Michelsohn
  (1/4)Σω_{ijk}c_jc_k term takes a minus sign); (ii) integration by parts in
  L²(t⁻³dV): the coefficient α in −i[tσ·∂ + ασ₃] is self-adjoint iff
  α = −1; (iii) the standard H^{n+1} formula −i[tγ·∂ − (n/2)γ_{n+1}] at
  n = 2.
- **Sign caveat (declared)**: the opposite orientation or the opposite
  Clifford convention flips D → −D. The λ-sign labeling is convention-bound;
  the spectrum as a SET is not — and by §5 the set is exactly symmetric, so
  the ambiguity is empty here.

## 3. The spin structure inside the instrument

Everything the scalar instrument did at the PSL level must be lifted; three
scalar shortcuts are INVALID for spinors and are replaced:

1. **Moves carry exact ρ₁ lifts.** A move is stored as the literal matrix
   product of the generator lifts along its word (ρ₁ is a homomorphism, so
   the sign per PSL element is well-defined). The scalar's sign
   normalization ("flip M so Re c > 0") is REMOVED; PSL dedup is done on a
   sign-canonicalized bottom-row KEY while storing the true lift.
2. **Lattice reductions carry lift signs.** The translation z → z + n₁ + n₂τ
   has ρ₁-lift (−1)^{n₂}[[1, n₁+n₂τ],[0,1]] (meridian lift +, longitude lift
   −, per the fork). Every z-reduction during pullback multiplies the tracked
   matrix accordingly.
3. **The pullback tracks the full SL(2,ℂ) product** g_j (moves and
   reductions interleaved, left-multiplied in application order), because the
   spin twist needs the actual lifted matrix with its sign.

**The cusp lattice**: Λ = ℤ·1 + ℤ·τ with τ = 2√−3 (probe: found by the
parabolic search; the minimal-Im parabolic IS the longitude word itself, and
|τ − 2i√3| < 3e−16). **The spinor Fourier lattice** for ρ₁ (meridian
periodic, longitude antiperiodic) is the shifted coset

  μ ∈ Λ* + u₂/2,  u₂ = i/(2√3),  |μ|_min = 1/(4√3) ≈ 0.1443

— it contains NO zero mode: Bär's discreteness mechanism is visible in the
instrument itself (no constant term, no Eisenstein sector; the spinor case is
in this sense cleaner than the scalar).

**The twist.** For an automorphic spinor in the s-trivialization,
ψ(γx) = ρ(k(γ,x)) ψ(x) with k(γ,x) = s(γx)⁻¹ ρ₁(γ) s(x) ∈ SU(2) (Iwasawa;
the lift sign lands in the SU(2) factor since the NA part has positive
diagonal). **The representation ρ is the CONJUGATE fundamental:
ρ(k) = conj(k), elementwise.** This is gate G2b, the design's key
non-obvious element, learned from a real failure:

> **The conjugate-twist lesson.** The geometric rotation of the coordinate
> frame (e₁,e₂,e₃) under g ∈ SL(2,ℂ) is Ad(conj k), not Ad(k):
> numerically R_geom = C·Ad(k)·C with C = diag(1,−1,1) to 1e−6 over random
> group elements. With the unconjugated twist the collocation system is
> INCONSISTENT — the probe's first scan produced a completely flat
> σ_min ≈ 0.5 with ZERO dips over |λ| ≤ 7 while every other gate (operator
> identity, SU(2)-ness, cocycle, peripheral ±I, assembly) passed. The
> peripheral and cocycle gates are blind to this defect (translations have
> trivial rotation; the cocycle holds for any s⁻¹gs construction). G2b is
> therefore MANDATORY in the sealed protocol.

Note conj: SU(2) → SU(2) is a homomorphism, so the cocycle survives; and
conj(±I) = ±I, so the peripheral spin characters are unchanged.

## 4. The cusp modes

For Dψ = λψ, separation in the μ-character sector gives the radial system
xU′ = iλU − xV, xV′ = −iλV − xU (x = 2π|μ|t, after peeling t·(·)), whose
decaying solution space is EXACTLY one-dimensional per μ:

  ψ_μ(z,t) = e^{2πi⟨μ,z⟩} t^{3/2} ( K_{iλ−1/2}(2π|μ|t) ,
                                     −i e^{iθ_μ} K_{iλ+1/2}(2π|μ|t) )ᵀ

with θ_μ = arg μ, ⟨μ,z⟩ = Re μ Re z + Im μ Im z. Structural features:

- **weight t^{3/2}** (the scalar has t¹) — the spinor half-shift;
- **order iλ ∓ 1/2** (the scalar has ir): same e^{−πλ/2} scale, so the
  scalar's truncation logic xcut = π·λ_max/2 + margin carries verbatim;
- **conjugation pairing**: K_{iλ+1/2}(x) = conj(K_{iλ−1/2}(x)) for real x, λ
  ⟹ ONE complex Bessel table serves both components (cost exactly 2× the
  scalar's real table);
- **λ = 0 is elementary**: K_{±1/2}(x) = √(π/2x)e^{−x} — the kernel scan is
  cheap and exact-friendly;
- the trapezoid K-integral
  K_{iλ−1/2}(x) = ∫₀^∞ e^{−x cosh u}[cosh(u/2)cos(λu) − i sinh(u/2)sin(λu)]du
  keeps the scalar's exponential convergence (probe: rel. err ≤ 1.4e−14 vs
  mpmath over λ ≤ 4, x ≥ 0.45).

## 5. Structural theorems the spectrum must obey (shape gates)

**(a) Exact spectral symmetry — proven, not assumed.** J = σ₂ ∘ conj
(antiunitary) satisfies JD = −DJ (direct Pauli computation), maps the
ρ₁-automorphy to itself (σ₂ conj(conj(k)) σ₂⁻¹-relation: σ₂ k̄ σ₂⁻¹ = k for
k ∈ SU(2), and the twist is conj(k)), and preserves the shifted lattice
(2δ = u₂ ∈ Λ* ⟹ the coset is negation-closed). Hence λ ∈ spec ⟺ −λ ∈ spec,
exactly. Probe: the refined ± pairs agree to 3e−13.

**(b) The kernel is even-dimensional.** J restricts to ker D with J² = −1
(quaternionic structure) ⟹ dim ker D is even. Probe: a kernel candidate of
dimension EXACTLY 2 (σ₁ = σ₂ ≈ 1e−12, σ₃ ≈ 0.53 — a 12-order gap) at
|λ| < 1e−8. Whether λ = 0 is exact is obligation O2.

**(c) Kramers-type doubling, observed and open.** The probe's ENTIRE
singular spectrum is doubled at every λ (all σ's in equal pairs, on- and
off-eigenvalue) — an instrument-level λ-preserving antiunitary, candidate
J ∘ (a lift of the amphichiral symmetry of m004). Consequence if confirmed:
every Dirac eigenvalue has even multiplicity, and the banked multiplicity
language must say "quaternionic multiplicity 1" vs "complex multiplicity 2"
deliberately. Resolving the mechanism is obligation O1 and blocks the seal
of multiplicity CLAIMS (not of eigenvalue claims).

## 6. The collocation system

Sample points (z_j, Y) on a horosphere below the domain; pull back with
tracked g_j to (z*_j, t*_j); each point contributes TWO complex rows

  Σ_μ a_μ [ ψ_μ(x*_j) − conj(k_j) ψ_μ(x_j) ] = 0

with one column per shifted-lattice mode (|μ| ≤ Rcut = xcut/(2πY)). Rows
2·npts ≥ 1.35·nmodes (npts ≈ 0.68·nmodes — HALF the scalar's pullback
count for the same overdetermination). Columns normalized; σ_min via SVD;
dips located on a λ-grid then golden-refined; Y-stability distinguishes
real eigenvalues from spurious dips. All r-independent precomputation of the
scalar (pullbacks, phases, E-matrix of the trapezoid) carries over; per-λ
cost = one complex Bessel table (2× scalar) + same-size SVD.

## 7. The certification protocol, adapted from B922 element-by-element

| B922 scalar element | spinor adaptation |
|---|---|
| coarse scan → dip list | identical (grid dλ = 0.01 sufficed at double precision) |
| auto-Y (≥97% rise) + golden refine | identical (probe: Y = 0.75, refine Y₂ = 0.62) |
| two-Y stability bar | identical, plus two-SEED and two-WORDSET (probe used all three) |
| 8-digit certified table tier | the probe's 8-digit bracket set plays this role for the first sealed window |
| 10-overlap-digit validation gate vs certified value | **replaced** — see §8 (no external anchor exists) |
| P4 perturbed restarts, spread bar | identical |
| P3 displaced must-fail control | identical (probe analogue: σ(3.7) = 0.47, background, clean) |
| +5-digit stability certification, quadratic convergence, sealed \|dr\| bar | identical in structure; bar to be sealed in the prereg |
| PSLQ rung (B798 discipline, licensed heights) | identical; runs on λ₁ and the kernel question output |

New mandatory elements: G2b (frame gate), the assembly cross-check (dumb
mpmath row rebuild vs vectorized rows; probe: 3e−12), and the shape gates
§5(a),(b).

## 8. The anchor question and the literature blank — stated honestly

**The scalar had** its own previously-certified 8-digit table and the
Grunewald–Huntebrinker 51.014 lineage as external anchor. **The spinor has
no external number to anchor to.** Search performed (2026-08-06, arXiv API;
session limits prevented a broader engine sweep): three targeted queries
plus one must-pass control (the control returned 64 papers including Bär
2000 "The Dirac operator on hyperbolic manifolds of finite volume" and the
Bolte–Stiepan Selberg trace formula for Dirac on hyperbolic SURFACES):

> **No numerically computed Dirac/spinor eigenvalue on ANY hyperbolic
> 3-manifold was found; the targeted surface query found trace-formula and
> bound results only, no computed spectra.** The blank is real to the depth
> searched. Caveats: arXiv-only, English-only, one session. Completing the
> sweep (MathSciNet/zbMATH-grade) is obligation O3 and MUST precede any
> banked sentence containing the word "first".

**What replaces the anchor** (internal-only validation, weaker than the
scalar's anchored gate — this sentence goes verbatim into the banked
FINDINGS): (i) the probe's 8-digit reproducibility across three instruments
(two Y's, two seeds, two word sets); (ii) G1: the operator identity
Dψ_μ = λψ_μ verified at the mode level by finite differences against an
independent mpmath implementation (probe: ≤ 1.9e−13 rel. residual) — this
validates the mathematics independently of the Hejhal machinery; (iii) the
theorem-backed shape gates §5(a),(b); (iv) the P3/P4/two-Y battery; (v) the
Weyl screen (leading term only: N_states(|λ|≤Λ) ≈ 2·vol/(6π²)·Λ³ ≈
0.0686·Λ³; probe: 30 states (with doubling) vs 22.7 expected at Λ = 6.92 —
right ballpark, screen only, sub-leading cusp terms for Dirac unknown).

## 9. Cost (measured + extrapolated)

Measured (this machine, double precision): validate ≈ 40 s; the 1401-point
scan over |λ| ≤ 7 at 496 modes ≈ 400 s; two-system golden refinement of 15
dips ≈ 510 s; third-instrument check ≈ 90 s. **The full probe ≈ 20 min.**

Scalar anchors: 58.1 h for the 25-digit certified λ₂ (B922); ~2.5 days for
the 25-digit parent. Spinor multipliers: Bessel 2×, assembly 2×, SVD 1×
(same matrix size at equal truncation), twist tracking negligible.

| rung | est. cost |
|---|---|
| sealed 10-digit first-window table (\|λ\| ≤ 7, 15 distinct values + kernel) | 1–3 days |
| sealed 25-digit λ₁ = 2.9745… (B922-grade certification) | **100–180 h** (2–3× the scalar's 58 h; extrapolation, stated as such) |
| PSLQ rung on λ₁ (B798 discipline) | hours |

Recommended ladder: probe (done, this arc) → sealed 10-digit table → sealed
25-digit λ₁ → PSLQ. The kernel-exactness question (O2) rides a separate
instrument (interval/index-theoretic), not this ladder.

## 10. The two-outcome shape of the first sealed run

**Sealed criterion** (vacuity-checked per MB12: CAN pass — the probe bracket
λ₁ = 2.9745506 exists with 8-digit cross-instrument agreement; CAN fail —
the displaced control produces clean background):

> In the window |λ| ≤ 4, the instrument produces ≥ 1 eigenvalue passing ALL
> of: two-Y bar |Δλ| < 10⁻⁹ at 10-digit working precision; two seeds; P4
> restart spread under the sealed bar; P3 displaced-λ control finds nothing;
> gates G1, G2, G2b, assembly cross-check pass; the ± partner is present
> within the same bars (§5a is a theorem — enforceable).

- **OUTCOME A**: banks as the first certified Dirac eigenvalue on a cusped
  hyperbolic 3-manifold — carrying verbatim: the literature-blank caveat
  (O3), the internal-only-validation sentence (§8), and the multiplicity
  caution (§5c). The 25-digit deepening and the PSLQ rung are then priced
  next steps.
- **OUTCOME B**: banks as an instrument-negative (the probe's 8-digit
  reproducibility becomes the recorded anomaly; the Weyl tension forbids
  reading B as "m004 has no Dirac spectrum"). Routes to a debug arc. NOT
  bankable as a spectral no-go.

No third outcome. The kernel (λ = 0, dim 2) is deliberately EXCLUDED from
the first seal — its claim shape ("exactly zero"?) needs the O2 instrument.

## 11. Obligations routed (registration-over-preservation)

- **O1** — the doubling mechanism (Kramers antiunitary: construct it
  explicitly or refute; decides multiplicity language). Blocks multiplicity
  claims only.
- **O2** — kernel exactness: is λ = 0 exact (harmonic spinors, index-type
  argument) or merely < 10⁻⁸? Separate instrument.
- **O3** — complete the prior-art sweep before any "first" sentence banks.
- **O4** — the C1/C2 trace-sign dictionary (decides ρ₂'s spectral type;
  independent of everything above).
- **O5** — port of the branch's high-precision (mpmath/arb) scalar driver to
  the spinor system for the 25-digit rung (the driver lives in the cc3
  branch corpus, B921 stage-2 scope).

## 12. Files

`probe.py` (stages: validate / scan / refine — all gates included) ·
`validate_out.json` (G1/G2/G2b numbers) · `scan_results.npz`,
`scan_dips.json` (the σ(λ) landscape) · `refined.json` (two-Y refined
eigenvalues + pairing) · `results.json` (consolidated) ·
`DRAFT_FINDINGS.md`.
