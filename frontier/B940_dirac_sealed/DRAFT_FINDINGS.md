# B940 — THE SEALED DIRAC RUN on (m004, ρ₁): **OUTCOME A**

**Date:** 2026-08-07 · **Seat:** computation agent (cc bench) · **Status:**
DRAFT — for the banking seat. **Preregistration sha-256:**
`6c513b0634c743df4015fc694d5dbd23dbf38e35829b838012a71dbfa75311fe`
(sealed before compute; recorded by stage `seal` into `results.json`, together
with the DESIGN and probe hashes).

Mathematics lane. No measured physical number is contacted anywhere in this
run.

---

## 1. The verdict, verbatim against the sealed criterion

> **Sealed criterion (PREREGISTRATION.md).** In the window |λ| ≤ 4, the
> instrument produces ≥ 1 eigenvalue passing ALL of: two-Y bar |Δλ| < 10⁻⁹ at
> 10-digit working precision; two seeds; P4 restart spread under the sealed
> bar; P3 displaced-λ control finds nothing; gates G1, G2, G2b, assembly
> cross-check pass; the ± partner is present within the same bars (§5a is a
> theorem — enforceable).

**Two eigenvalues in the window pass every element: λ = ±2.9745505801732.**
Per the prereg this is

> **OUTCOME A**: a certified Dirac eigenvalue on a cusped hyperbolic
> 3-manifold, banked **carrying verbatim** the literature-blank caveat (O3),
> the internal-only-validation sentence (§8), and the multiplicity caution
> (§5c).

## 2. The number

> **λ₁ = 2.974550580** (the ten digits the seal's working-precision clause
> names)

Working values, stated so the deepening rung has something to hit:

| quantity | value |
|---|---|
| S1 at the sealed refinement offset d = 10⁻⁶ | `2.974550580173186` |
| d → 0 Richardson limit of the V-crossing refinement (S1) | `2.9745505801708014` |
| spread across the four instruments | `8.15 × 10⁻¹³` |
| refinement d²-bias at the sealed offset | `2.4 × 10⁻¹²` |
| truncation-ladder spread (margins 21 / 32 / 40) | `2.04 × 10⁻¹³` |

So the honest total uncertainty is **≈ 3 × 10⁻¹²** — about twelve digits of
reproducibility, three orders of magnitude inside the sealed 10⁻⁹ bar. The
seal certifies the bars; ten digits is what it names, and the extra two are
reported, not claimed.

The exact partner **λ = −2.9745505801732** is present at `4.00 × 10⁻¹⁵`
(DESIGN §5a is a theorem, and it was enforced, not merely observed).

## 3. The battery, element by element

| sealed element | measured | bar | verdict |
|---|---|---|---|
| two-Y bar (S1 Y=0.75 vs S2 Y=0.62) | 8.15 × 10⁻¹³ (+λ), 8.26 × 10⁻¹³ (−λ) | < 10⁻⁹ | PASS |
| two seeds (S1 seed 11 vs S3 seed 23) | 2.53 × 10⁻¹⁴ (+λ), 1.78 × 10⁻¹⁵ (−λ) | < 10⁻⁹ | PASS |
| word set (S4, maxlen-6 moves) — extra axis | 3.94 × 10⁻¹³ / 4.34 × 10⁻¹³ | < 10⁻⁹ | PASS |
| P4 perturbed restarts, 6 per system × 2 systems | within-system 0.0 and 4.4 × 10⁻¹⁶; joint 8.16 × 10⁻¹³ | < 10⁻⁹ | PASS |
| P3 displaced-λ control (6 starts) | nothing found at any start | must find nothing | PASS |
| G1 operator identity (mpmath dps 40, FD) | 1.88 × 10⁻¹³ max rel. residual | < 10⁻¹⁰ | PASS |
| G2 peripheral twists / cocycle / SU(2) | 2.2 × 10⁻¹⁶ / 3.0 × 10⁻¹⁵ / 1.5 × 10⁻¹⁴ / 8.9 × 10⁻¹⁶ | — | PASS |
| G2b frame gate (conjugate twist) | 8.43 × 10⁻⁷ | < 10⁻⁵ | PASS |
| G2b discriminating control (unconjugated twist) | **1.93** — O(1) failure | > 10⁻² | gate is not vacuous |
| assembly cross-check (24 mpmath-rebuilt rows) | 3.03 × 10⁻¹² max rel. dev | < 10⁻¹⁰ | PASS |
| ± partner (§5a theorem, enforced) | 4.00 × 10⁻¹⁵ | < 10⁻⁹ | PASS |

### The four instruments

| | Y | seed | moves | modes | points (rows) | λ₁ |
|---|---|---|---|---|---|---|
| S1 | 0.75 | 11 | maxlen 5 | 716 | 546 (1092) | 2.974550580173186 |
| S2 | 0.62 | 11 | maxlen 5 | 1044 | 784 (1568) | 2.974550580172371 |
| S3 | 0.75 | 23 | maxlen 5 | 716 | 546 (1092) | 2.974550580173161 |
| S4 | 0.68 | 7 | maxlen 6 | 862 | 658 (1316) | 2.974550580172792 |

### The scan

|λ| ≤ 4 on S1 at dλ = 0.01 (801 points, 467 s), median σ_min = 0.51252 →
**exactly 3 dips**: −2.97, 0, +2.97. Repeated on S2 at dλ = 0.02 (401 points,
718 s), median 0.47914 → the same 3 dips. **The dip lists agree across the two
instruments** — a completeness cross-check the probe did not run.

Detection margin: the measured V slope is 2.66, so a dip sitting at the
worst-case half-grid offset (0.005) would show σ ≈ 0.013 = 0.026 × median,
a factor 19 inside the 0.5 × median dip test. Two eigenvalues closer together
than ≈ 0.01 would merge into one dip; that is not excluded by this run.

### Refinement convergence (the quadratic-convergence analogue)

σ_min(λ) near an eigenvalue is an **exact V** — linear on both branches with
no noise floor down to at least 4 × 10⁻¹⁰. The sealed refinement therefore
intersects the two fitted branches instead of hunting the vertex. Its error is
O(d²) in the fit offset, confirmed:

| d | λ | successive-ratio at doubling d (O(d²) ⇒ 4) |
|---|---|---|
| 5 × 10⁻⁷ | 2.9745505801713983 | — |
| 1 × 10⁻⁶ | 2.9745505801731860 | 5.00 |
| 2 × 10⁻⁶ | 2.9745505801803396 | 4.20 |
| 4 × 10⁻⁶ | 2.9745505802089527 | 4.05 |
| 8 × 10⁻⁶ | 2.9745505803234050 | — |

Richardson extrapolation from **four disjoint pairs** agrees to 10⁻¹⁵:
`2.9745505801708023`, `2.9745505801708014`, `2.9745505801708014`,
`2.9745505801708014`.

---

## 4. Two instrument facts this run establishes (both corrections)

**(i) The probe's Bessel quadrature was under-resolved at large argument, and
the sealed run fixes it.** The probe's trapezoid step h = 0.15 (tol_exp = 45)
holds ~10⁻¹⁵ relative accuracy only out to x ≈ 30; the Poisson error term
~e^{−π(2π/h − λ)/2} is fixed in absolute size while K(x) ~ e^{−x} shrinks. The
x-range the instrument *actually* uses is **[0.562, 99.21]**, and at the top of
it the probe setting is **7.6 × 10⁻⁴ relative**. Because the collocation
columns are normalised before the SVD, the corrupted columns would have been
exactly the exponentially small large-|μ| ones. The sealed instrument uses
h = 0.08, tol_exp = 60: **≤ 1.8 × 10⁻¹³ relative across the whole range**.

Honest follow-through, run as a reproducible post-verdict control
(`dirac_sealed.py qctl` → `results.json → quadrature_control`): refining λ₁ on
S1 under the two quadratures gives **bit-identical** values —
`2.974550580173186` both ways, |difference| = **0.0**. The truncation ladder is
likewise flat to 2 × 10⁻¹³. **So this was a latent defect, not an active one**,
and the sealed number does not depend on the correction. It is reported because
a gate that only fires where it does not matter is still a gate that fired —
and because at a deeper rung (25 digits, or a wider λ-window, where x_max grows)
it would matter.

**(ii) The probe's "8-digit / dev floor 6.2 × 10⁻⁹" was a search artifact, not
a measurement.** All fifteen of the probe's dips reported the *identical*
two-Y deviation `6.159092791335752e-09`. That is `golden_min`'s tol = 2 × 10⁻⁸
bracket-subdivision offset, not a disagreement between the two Y-systems. With
the V-crossing refinement the same two systems agree to 8 × 10⁻¹³. This is why
the sealed run improves on the probe by four orders of magnitude at the same
double precision, and it is the reason the 10⁻⁹ bar was clearable at all.

## 5. The P3 control — and a warning the criterion earned

All six displaced starts (λ_d = 1.0, 1.5, 2.0, 2.5, 3.5, 3.7; each ≥ 0.47 from
any eigenvalue) **found nothing**. In every case the golden search ran to a
*bracket endpoint* (offset exactly ±0.006 = the half-width), i.e. there is no
interior minimum at all, and σ there sat at 0.91–1.02 × the scan median.

**But note carefully:** at λ_d = 2.5, 3.5 and 3.7 the two-Y *agreement alone*
was 4.3 × 10⁻¹⁰, 3.9 × 10⁻¹⁰ and 1.3 × 10⁻⁹ — at or below the sealed 10⁻⁹ bar.
That is not a spectral coincidence: with no interior minimum, both systems
terminate at the *same* deterministic bracket endpoint, so the "agreement" is
an artifact of the bracket. **The two-Y bar is therefore NOT by itself
discriminating; the σ-depth requirement is what kills the control.** The
sealed criterion is a conjunction, and this run is the demonstration that the
conjunction is doing real work rather than decorating a single test.

## 6. The kernel — recorded, EXCLUDED from this seal

Per the prereg, λ = 0 is deliberately outside the claim. Recorded for O2:
|λ| < 10⁻¹⁴ on all four instruments; σ₁ = σ₂ ∈ [1.0, 1.6] × 10⁻¹², σ₃ ∈
[0.50, 0.53] — a **twelve-order gap**, so the kernel of the truncated system
has dimension **exactly 2**, consistent with DESIGN §5(b) (J² = −1 on ker D ⇒
even-dimensional; verified symbolically here: σ₂conj(σ_k) + σ_kσ₂ = 0 exactly
and J² + I = 0 exactly). Whether λ = 0 is *exact* remains obligation **O2** and
is untouched by this run.

## 7. Weyl screen (screen, not a gate)

2·vol/(6π²) = 0.0685567; expected ≈ **4.39** states at |λ| ≤ 4; found **4**
(the two eigenvalues × the §5c doubling) **plus the kernel's dimension 2**.
Leading term only; the sub-leading cusp terms for the Dirac operator are
unknown.

## 8. The three verbatim caveats the prereg attaches to OUTCOME A

### (a) The internal-only-validation sentence (DESIGN §8, verbatim)

> **What replaces the anchor** (internal-only validation, weaker than the
> scalar's anchored gate — this sentence goes verbatim into the banked
> FINDINGS): (i) the probe's 8-digit reproducibility across three instruments
> (two Y's, two seeds, two word sets); (ii) G1: the operator identity
> Dψ_μ = λψ_μ verified at the mode level by finite differences against an
> independent mpmath implementation (probe: ≤ 1.9e−13 rel. residual) — this
> validates the mathematics independently of the Hejhal machinery; (iii) the
> theorem-backed shape gates §5(a),(b); (iv) the P3/P4/two-Y battery; (v) the
> Weyl screen (leading term only: N_states(|λ|≤Λ) ≈ 2·vol/(6π²)·Λ³ ≈
> 0.0686·Λ³; probe: 30 states (with doubling) vs 22.7 expected at Λ = 6.92 —
> right ballpark, screen only, sub-leading cusp terms for Dirac unknown).

### (b) The literature-blank caveat (DESIGN §8, verbatim — and now superseded in depth)

> **No numerically computed Dirac/spinor eigenvalue on ANY hyperbolic
> 3-manifold was found; the targeted surface query found trace-formula and
> bound results only, no computed spectra.** The blank is real to the depth
> searched. Caveats: arXiv-only, English-only, one session. Completing the
> sweep (MathSciNet/zbMATH-grade) is obligation O3 and MUST precede any banked
> sentence containing the word ⟦the priority word — elided here under the O3
> gate; restore verbatim at banking⟧.

**This caveat has since been superseded by the parallel O3 panel**, whose
report landed in this cell directory during the run
(`O3_PRIOR_ART.md`, `o3_results.json`). The banking seat MUST read it before
writing any priority sentence. Its load-bearing content:

- **No prior art was found for a computed *nonzero* Dirac eigenvalue on any
  hyperbolic 3-manifold**, at a depth that reached **zbMATH Open** (MSC-coded
  structured queries + full reviewer texts), OpenAlex full-text and citation
  graph, arXiv, Semantic Scholar, INSPIRE-HEP, and the complete 59-work citing
  set of Bär 2000, read individually. **MathSciNet was NOT reachable** (auth
  wall) — so the standard named in the B933 seal is **half met**.
- **The must-pass control came back positive**: Gesteau–Pal–Simmons-Duffin–Xu,
  *Bounds on spectral gaps of hyperbolic spin surfaces* (arXiv:2311.13330)
  computes Dirac eigenvalues on hyperbolic spin **surfaces/orbifolds**. The 3D
  blank is therefore not a search artifact.
- **The near-miss that constrains the wording**: Lin–Lipnowski, *Dirac spectral
  flow and Floer theory of hyperbolic three-manifolds* (arXiv:2506.07238)
  certifies, by computer assistance, **zero** eigenvalues of spin^c Dirac
  operators on **closed** hyperbolic 3-manifolds — no eigenvalue *value* is
  published. Any unqualified priority sentence is contestable; the qualifiers
  **"nonzero"** and **"cusped"** are load-bearing, and Lin–Lipnowski should be
  cited positively as the nearest prior work.
- Fortunate but worth stating rather than relying on silently: the only
  eigenvalue Lin–Lipnowski pin is **zero** — precisely the object this seal
  **excludes**.

### (c) The multiplicity caution (DESIGN §5c, verbatim)

> **(c) Kramers-type doubling, observed and open.** The probe's ENTIRE singular
> spectrum is doubled at every λ (all σ's in equal pairs, on- and
> off-eigenvalue) — an instrument-level λ-preserving antiunitary, candidate
> J ∘ (a lift of the amphichiral symmetry of m004). Consequence if confirmed:
> every Dirac eigenvalue has even multiplicity, and the banked multiplicity
> language must say "quaternionic multiplicity 1" vs "complex multiplicity 2"
> deliberately. Resolving the mechanism is obligation O1 and blocks the seal of
> multiplicity CLAIMS (not of eigenvalue claims).

Reconfirmed at sealed settings over the whole 801-point scan: σ₁ vs σ₂ median
relative gap **8.7 × 10⁻¹⁶** (max 9.7 × 10⁻⁵), and σ₃/σ₁ median 1.037 — the
doubling is not confined to the dips. **No multiplicity is claimed here.**

---

## 9. Declared readings and honest limits

1. **"10-digit working precision."** The collocation/SVD path is IEEE-754
   binary64 throughout (≈ 15.95 decimal digits), which exceeds a 10-digit
   working-precision requirement with ~6 digits of headroom; mpmath at dps
   30–50 supplies the *independent* G1, assembly and Bessel checks. The
   25-digit rung needs the O5 driver port and was **not** attempted. This
   reading was declared in stage `seal`, before the battery ran.
2. **"The sealed bar" for the P4 spread.** The preregistration seals exactly
   one numeric bar (10⁻⁹). "P4 restart spread under the sealed bar" is read as
   that same 10⁻⁹. Declared in stage `seal` before the battery ran. The
   measured spreads (0.0 and 4.4 × 10⁻¹⁶ within a system) make the reading
   immaterial.
3. **Deliberate deviation from the probe**: the Bessel quadrature step
   (§4(i)) and the refinement method (V-crossing rather than golden-vertex,
   §4(ii)). Both are declared in `results.json → seal.declared_choices` and
   both are tightenings, not loosenings.
4. **Not claimed**: multiplicity (O1); kernel exactness (O2); any priority
   sentence (O3, and the qualifiers above); ρ₂'s spectral type (O4);
   25-digit certification (O5); PSLQ (not run — the sealed criterion does not
   include it and 12 digits is under the licensed-height threshold that made
   the scalar's PSLQ rung meaningful).
5. **Scan resolution**: eigenvalues closer together than ≈ 0.01 would merge
   into a single dip. Not excluded.

## 10. Cost (measured, this bench, double precision)

Gates 4 s · scan 1186 s (801 + 401 λ-points on two instruments) · refinement
443 instrument-seconds over 12 refinements · P4 24 restarts · P3 12
refinements. **Full sealed battery ≈ 50 minutes**, against DESIGN §9's 1–3 day
estimate for the 10-digit rung — the V-crossing refinement is why.

## 11. Files

`dirac_sealed.py` (stages: seal / gates / scan / refine / p4 / p3 / verdict,
plus the post-verdict `qctl` control; each dumps `results.json` on completion)
· `results.json` (every stage, every number) · `scan_S1.npz`, `scan_S2.npz`
(the σ(λ) landscapes) · `run.log` · this draft. The O3 panel's `O3_PRIOR_ART.md` and `o3_results.json` arrived
independently in the same directory.

**Routed to the banking seat**: `tests/test_b940_dirac.py` (the prereg puts
seal-integrity ahead of everything else in it) is not written here; the
PROGRESS_LOG / CHANGELOG /
CAMPAIGN_STATUS updates per WORKING_RULES rule 10; and the priority wording,
which is the O3 panel's call, not this bench's.
