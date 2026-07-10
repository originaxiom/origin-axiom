# B499 — CL-3D / Gate D: **DATA-BANKED** — the non-Hermitian spectral data package at κ = √3·e^{±iπ/6}: horseshoe-signature escape, Cantor-like zero-area spectrum in ℂ, *tame* non-normality, and two precisely posed conjectures

**Status: banked (frontier), Closure Campaign Phase 3, CL-3D (prereg
`docs/CLOSURE_CAMPAIGN_2026-07.md` + local `README.md`; outcome enum DATA-BANKED / SURPRISE).
Verdict: DATA-BANKED — no structure contradicting the DG picture was found (no positive-measure
bounded set, no spectral pooling, no boundary catastrophe); the deliverable is conjecture-shaped
data, never a claim. Firewalled; nothing to `CLAIMS.md`.**

Gate D (`docs/OPEN_PROBLEMS.md`): at real κ>2 the metallic trace map is the Fibonacci Hamiltonian
(Cantor spectrum — Sütő, Damanik–Gorodetski horseshoe; `K007`/`K010`). The object's actual
κ = √3·e^{±iπ/6} is **complex**: κ−2 = e^{±2iπ/3} = ζ₃ (a primitive cube root of unity, `K020` §5),
so the coupling is λ = e^{±iπ/3} — a **primitive 6th root of unity** — and the Schrödinger cocycle
is **non-self-adjoint**. This probe produces the data a non-self-adjoint spectral theorist needs,
each item bracketed by the Hermitian controls (MB6: run the control) and by explicit resolution
caveats. Everything numerical is **tier: num** (controls locked, seeds/grids logged in
`b499_nonhermitian_dg.json`); the algebra in §1 is **tier: exact** (sympy, no floats).

## 0. Controls (prereg: fail ⇒ INVALID; all six PASS)

- **Banked-anchor reproduction:** the B186 escape-rate estimator (verbatim) gives γ(λ=3) =
  **0.5094** vs the banked early-window **0.51** (B451: asymptotic 0.445 ± 0.006 — the anchor
  locks the *estimator*, per B451's correction note). ✓
- **The V=1 level set** (κ=3, the Fibonacci Hamiltonian, DG-proven Cantor): γ = **0.139 > 0**
  (exponential escape = horseshoe signature) and the B165 MST max-gap/diameter is **persistent,
  0.1641 → 0.1641** across 610→1597, vs the κ=2 band's **0.005 → 0.002 → 0**. ✓
- **The κ=2 periodic limit behaves exactly as K010's dictionary says:** γ = **0.000**; the
  non-escaping real set is the band [−2,2] — measured fraction of the [−3,4] test line
  **0.5714 = 4/7** to 4 decimal places. ✓
- **Box-dim (B186 C2, matched depth 13):** V=1 cloud 1.071 < band 1.103. *Honest caveat: this
  finite-depth diagnostic only weakly separates at V=1 (the λ=1 Cantor set is thick); the strong
  controls are the escape rate and the MST.* ✓
- **Spectrum = non-escaping set consistency:** control eigenvalues sit deep (median escape time
  17 vs 7 generic — the shadowing depth ~ log(1/spacing)/log φ). ✓

## 1. The level set, named exactly (tier: exact)

κ − 2 = ζ₃ satisfies **Φ₃(κ−2) = 0** — the Eisenstein cyclotomic; |κ−2| = 1 (the unit
obstruction, `K020`). The coupling λ = e^{iπ/3} obeys λ² = κ−2, so the non-self-adjoint operator
is H = Δ + λ·χ_Fib with |λ| = 1. The ℚ(√−3) Galois ℤ/2 (√−3 → −√−3, B285) **swaps the ± pair**
κ ↔ κ̄. The trace map T(x,y,z) = (2xy−z, x, y) conserves I = x²+y²+z²−2xyz−1; the Schrödinger
seed ((E−λ)/2, E/2, 1) lies on I = (λ/2)² for **all** E (B186 C0). Fixed points of T: (0,0,0)
(I=−1: κ=−2, the figure-eight point, B67) and (1,1,1) (I=0: κ=2, the void; Jacobian spectrum
**{φ², −1, φ⁻²}** — B124, recomputed exactly).

## 2. Escape structure on the object's level surface (tier: num)

- **E-plane escape-time map** (800×300 grid, K≤60, trap R=20): survivor counts
  240000 → 500 (K=20) → **0 (K≥32)** — clean exponential escape, **γ₂D = 0.514** over ≥3 decades.
  Same signature as the DG-proven control; the band control gives exactly 0. **Zero-area
  non-escaping set** — *no pooling, no positive-measure bounded set* (the SURPRISE trigger did
  not fire).
- **Real section: empty** (0 survivors of 4001 at K=40) — the spectrum genuinely leaves ℝ; the
  eigenvalue cloud sits in **0.200 ≤ Im E ≤ 0.803**.
- **Eigenvalues sit deep** (median escape time 16 vs 5 generic), mirroring the control — the
  finite-approximant spectra track the non-escaping set.
- **Symmetric x=y slice** (both z-branches of the level quadric): exponential escape
  (γ = 0.61 / 0.53), no survivors at K=40 — thin on the slice too.
- **The diagonal line through the two fixed points** (x=y=z=w; each point on its own level):
  bounded orbits exist on the line only near the *elliptic* fixed point (0,0,0) (the κ≈−2
  region); its **three** intersection points with the object's level (roots of 3w²−2w³−1 = ζ₃/4)
  all **escape** (times 8, 4, 7) — the diagonal meets this level surface only in the escaping set.
- **The conjugate level is the exact mirror:** the escape-time map at κ̄ on the conjugated grid
  is **identical** (integer-exact) — the ± pair is one Galois orbit, computed, not assumed.

## 3. Pseudospectra of the non-self-adjoint approximants (tier: num)

σ_min(z−H) portraits via complex-Schur + inverse iteration, **validated against direct SVD**
(150-point subsample, max rel. error 3.6%); periodic Fibonacci approximants, sizes 89–1597.

| quantity | object (κ = √3e^{iπ/6}) | Hermitian control (V=1) |
|---|---|---|
| amplification max dist(z,Λ)/σ_min (n=233) | **3.16** (≤ cond(V) = 10.8, Bauer–Fike) | **1.000** (normal) |
| cond(V) at n = 89/144/233/377/610 | 6.8 / 9.2 / 10.8 / 14.2 / 17.4 → **~n^0.48** | 1 (exact) |
| OBC↔PBC spectral movement (Hausdorff/diam, n=610) | **0.0385** | 0.0305 |
| ε-areas, ε = 10^{−1}…10^{−2} decades (n=233) | 1.35 / 0.43 / 0.10 → slope 1.13, **d_eff ≈ 0.87** | 0.56 / 0.20 / 0.00 |

The non-normality is **tame**: eigenvector condition numbers grow only *polynomially* (~√n over
one decade of sizes — honest caveat: 5 sizes), pseudospectral amplification stays O(10) and under
the Bauer–Fike bound, and the boundary-condition sensitivity **matches the Hermitian control**
(no Hatano–Nelson-type spectral pooling under BC change). ε-decades below ~10^{−2.5} enter the
finite-size point regime (spacing ~ diam/n) and are reported but not fitted.

## 4. Dimension / scaling (tier: num, resolution-honest)

- **B165 MST diagnostic at the object's κ:** max-gap/diam = **0.1304 / 0.1307 / 0.1305** across
  610/987/1597 — persistent (totally-disconnected signature), 25–65× the band control. Compare
  the banked ladder: V=1 real Cantor 0.164; κ=−2 golden 0.206 (B165); band → 0.
- **Escape-based box-count** (1920×720 grid): K-survivor-set slopes **1.72 → 1.49 → 1.26 → 1.03**
  (K = 10→16), decreasing monotonically as the neighborhood tightens; survivor counts decay
  exponentially. Reading: upper estimates → **box-dim ≈ 1.0–1.3 bracket**, decisively < 2.
- **Eigenvalue-cloud box-dims** (610/987/1597): 0.93 / 1.01 / 1.05 (finite-sample effective
  values); ε-area scaling gives d_eff ≈ 0.87 (~1.5 decades only). Honest summary: the data
  supports **dimension ≈ 1 within ±0.2**; it cannot distinguish a Cantor subset of a curve from
  a genuinely 1-dimensional fractal cloud. What it *rules out* at accessible resolution:
  positive area, pooling, dimension → 2.

## 5. Symmetry structure (checked, not assumed)

- **Exact:** H(λ̄) = conj H(λ) entrywise ⇒ spec(κ̄) = conj spec(κ) — the ± pair is a single
  **Galois/amphichiral ℤ/2 orbit** (the `K020`/B285 involution acting on spectra); verified on
  eigenvalues to 1.3×10⁻⁸.
- **Exact:** H^T = H — the cocycle/operator is **complex symmetric** (transpose-symmetric, not
  self-adjoint): the structural class a specialist should work in.
- **Absent:** intra-κ PT-type reality **fails** — the spectrum is not conjugation-symmetric
  (Hausdorff asymmetry 0.32 of diameter; the whole cloud has Im E > 0). The antiunitary symmetry
  acts only *across* the conjugate pair, not within one member. (Contrast B163/B165's κ<2 real
  case, which is PT-like; the object's complex κ is genuinely outside that family too.)

## 6. The deliverable: two precisely posed conjectures

**DATA-SUPPORTED CONJECTURE D1 (a non-Hermitian Damanik–Gorodetski theorem at the object's
level) — not a claim.** *For κ = √3·e^{±iπ/6} (κ−2 = ζ₃, coupling λ = e^{±iπ/3}), the Fibonacci
trace map T(x,y,z) = (2xy−z, x, y) restricted to the complex level surface {I = (κ−2)/4} is
uniformly hyperbolic on its non-escaping set — a complex horseshoe in the Bedford–Smillie sense;
the Schrödinger line ((E−λ)/2, E/2, 1) meets its stable lamination in a compact, totally
disconnected set Σ ⊂ ℂ of zero Lebesgue area with box dimension ≈ 1; and Σ is the spectrum of
the non-self-adjoint metallic operator H = Δ + λ·χ_Fib (Hausdorff limit of the approximant
spectra, boundary-condition independent).* Evidence: γ₂D = 0.51 exponential escape (the
signature validated on DG ground truth), MST persistence 0.130 across three sizes vs band 0.002,
box-count slopes ↓ 1.03, empty real section, deep-eigenvalue consistency.

**DATA-SUPPORTED CONJECTURE D2 (spectral–pseudospectral correspondence) — not a claim.** *The
transfer cocycle at the object's κ is complex symmetric with eigenvector condition numbers
growing only polynomially in volume (measured ~n^{1/2}), so the ε-pseudospectra of the
approximants converge to the ε-neighborhood of Σ with polynomially bounded amplification — no
spectral pooling and no exponential boundary sensitivity: DG-type spectral data survive
non-self-adjointness at this κ, with pseudospectra (not self-adjoint spectral measures) as the
correct regularity language.* Evidence: amplification 3.16 ≤ cond(V) = 10.8 vs control 1.000;
cond(V) 6.8→17.4 over 89→610; OBC/PBC movement 0.039 ≈ control 0.031; ε-area d_eff ≈ 0.87
consistent with the escape-based dimension bracket.

**What would refute the picture (the committed SURPRISE triggers, none fired):** a
positive-measure non-escaping set (survivor fraction stabilizing > 0), box-count slopes → 2,
spectral pooling under BC change, or exponentially growing cond(V).

## 7. Honest scope

Finite grids (finest 1920×720), finite iteration depth (K ≤ 60), approximant sizes ≤ 1597, one
decade of sizes for the cond(V) fit, ~1.5 usable ε-decades; the escape-based dimensions are
*upper* estimates at each K; the eigenvalue-cloud box-dim diagnostic is weakly separating at
this depth (recorded in the control). None of this is a proof and none of it promotes: the
rigorous statement — uniform hyperbolicity of the complexified trace map on the non-escaping set
of a *complex* level surface, and the operator-theoretic spectral identification — stays
**NEEDS-SPECIALIST** (non-self-adjoint spectral theory / complex horseshoes), exactly as Gate D
says. This probe's contribution is the conjecture-shaped data package above.

## The fence

`probe.py` (runnable, ~2.5 min, exit 0, `ALL CHECKS PASS`, parameters logged in PARAMS) →
`b499_nonhermitian_dg.json`; locks `tests/test_b499_nonhermitian_dg_data.py` (<60 s: exact tier +
controls recomputed + coarse banked invariants, no fragile floats). Cross-refs: **K007/K010**
(the Hermitian dictionary), **K020 §5 / B285** (κ−2 = ω², the Galois ℤ/2), **B163/B165** (the
MST diagnostic + the C8 conditional: uniform hyperbolicity ⟹ Cantor off-axis), **B186/B451**
(the escape-rate certification + the anchor's correction note), **B317** (the object as
transcendental Painlevé-VI — the dynamics is genuinely chaotic, consistent with the horseshoe
data), **B67/B124** (the κ=−2 and κ=2 fixed-point anchors), `docs/OPEN_PROBLEMS.md` Gate D,
`docs/OPEN_LEADS.md` L19/L20. Lit: Damanik–Gorodetski (the Hermitian horseshoe); Sütő (the
invariant); Bedford–Smillie (complex horseshoes); Trefethen–Embree (pseudospectra of nonnormal
operators); Bowen–Ruelle (escape rate = pressure).

**Nothing to `CLAIMS.md`; firewall untouched.**
