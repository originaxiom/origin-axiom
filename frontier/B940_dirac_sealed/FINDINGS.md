# B940 — THE SEALED DIRAC RUN on (m004, ρ₁): **OUTCOME A**

**Date:** 2026-08-07 · **Seat:** cc (banking), from the computation bench + the
O3 literature panel · **Lane:** MATHEMATICS. No measured physical number is
contacted anywhere in this arc. Gate 5 untouched.

**Preregistration sha-256:** `6c513b0634c743df4015fc694d5dbd23dbf38e35829b838012a71dbfa75311fe`
— sealed and pushed (`7bb6c963`) BEFORE any compute, recorded in
`docs/SEAL_LEDGER.md` line 488 and re-verified at banking against the file on
disk. The instrument recorded the same hash itself, in stage `seal`, together
with the DESIGN and probe hashes.

---

## 1. The verdict, verbatim against the sealed criterion

> **Sealed criterion (B933 §10, verbatim in the prereg).** In the window
> |λ| ≤ 4, the instrument produces ≥ 1 eigenvalue passing ALL of: two-Y bar
> |Δλ| < 10⁻⁹ at 10-digit working precision; two seeds; P4 restart spread
> under the sealed bar; P3 displaced-λ control finds nothing; gates G1, G2,
> G2b, assembly cross-check pass; the ± partner is present within the same
> bars (§5a is a theorem — enforceable).

**Two eigenvalues in the window pass every element: λ = ±2.9745505801732.**

> **OUTCOME A** — a **certified Dirac eigenvalue on a cusped hyperbolic
> 3-manifold**, banked carrying verbatim the literature caveat (O3), the
> internal-only-validation sentence (DESIGN §8) and the multiplicity caution
> (§5c), all reproduced in §7 below.

## 2. The number

> **λ₁ = 2.974550580** — the ten digits the seal's working-precision clause
> names.

| quantity | value |
|---|---|
| S1 at the sealed refinement offset d = 10⁻⁶ | `2.974550580173186` |
| d → 0 Richardson limit (S1) | `2.9745505801708014` |
| spread across the four instruments | `8.15 × 10⁻¹³` |
| refinement d²-bias at the sealed offset | `2.4 × 10⁻¹²` |
| truncation-ladder spread (margins 21 / 32 / 40) | `2.04 × 10⁻¹³` |
| **honest total uncertainty** | **≈ 3 × 10⁻¹²** |

About twelve digits of reproducibility — three orders of magnitude inside the
sealed 10⁻⁹ bar. The seal certifies the bars; ten digits is what it names; the
extra two are reported, not claimed. The partner λ = −2.9745505801732 is
present at `4.00 × 10⁻¹⁵` (DESIGN §5a is a theorem, and it was **enforced,
not assumed** — §5a was verified symbolically and exactly: σ₂·conj(σ_k) +
σ_k·σ₂ = 0 and J² + I = 0 to machine zero).

## 3. The battery, element by element

| sealed element | measured | bar | verdict |
|---|---|---|---|
| two-Y bar (S1 Y=0.75 vs S2 Y=0.62) | 8.15 × 10⁻¹³ (+λ), 8.26 × 10⁻¹³ (−λ) | < 10⁻⁹ | PASS |
| two seeds (S1 seed 11 vs S3 seed 23) | 2.53 × 10⁻¹⁴, 1.78 × 10⁻¹⁵ | < 10⁻⁹ | PASS |
| word set (S4, maxlen-6 moves) — extra axis | 3.94 × 10⁻¹³ / 4.34 × 10⁻¹³ | < 10⁻⁹ | PASS |
| P4 perturbed restarts, 6 per system × 2 systems | within-system 0.0 and 4.4 × 10⁻¹⁶; joint 8.16 × 10⁻¹³ | < 10⁻⁹ | PASS |
| P3 displaced-λ control (6 starts) | found nothing at any start | must find nothing | PASS |
| G1 operator identity (mpmath dps 40, finite differences) | 1.88 × 10⁻¹³ max rel. residual | < 10⁻¹⁰ | PASS |
| G2 meridian / longitude / cocycle / SU(2) | 2.2e−16 / 3.0e−15 / 1.5e−14 / 8.9e−16 | — | PASS |
| G2b frame gate (conjugate twist) | 8.43 × 10⁻⁷ | < 10⁻⁵ | PASS |
| G2b **discriminating control** (unconjugated twist) | **1.93** — O(1) failure | > 10⁻² | gate is not vacuous |
| assembly cross-check (24 mpmath-rebuilt rows) | 3.03 × 10⁻¹² max rel. dev | < 10⁻¹⁰ | PASS |
| ± partner (§5a theorem, enforced) | 4.00 × 10⁻¹⁵ | < 10⁻⁹ | PASS |

**The four instruments.** S1 (Y 0.75, seed 11, maxlen 5, 716 modes, 546 pts) →
`2.974550580173186`; S2 (Y 0.62, seed 11, 1044 modes, 784 pts) →
`2.974550580172371`; S3 (Y 0.75, seed 23) → `2.974550580173161`; S4 (Y 0.68,
seed 7, maxlen 6, 862 modes) → `2.974550580172792`.

**The scan.** |λ| ≤ 4 on S1 at dλ = 0.01 (801 points, median σ_min 0.51252) →
exactly 3 dips: −2.97, 0, +2.97. Repeated on S2 at dλ = 0.02 (401 points,
median 0.47914) → the same 3 dips. **The dip lists agree across two independent
instruments** — a completeness cross-check the probe never ran. Detection
margin: at the measured V slope 2.66, a dip at the worst-case half-grid offset
would show σ ≈ 0.026 × median, a factor 19 inside the 0.5 × median dip test.

**Convergence.** σ_min(λ) near an eigenvalue is an **exact V** — linear on both
branches, no noise floor down to at least 4 × 10⁻¹⁰ — so the sealed refinement
intersects the two fitted branches instead of hunting the vertex. Error is
O(d²), confirmed by doubling ratios 5.00 / 4.20 / 4.05 against the predicted 4,
with Richardson limits from **four disjoint pairs** agreeing to 10⁻¹⁵.

## 4. Two instrument facts this run establishes — both corrections to the probe

**(i) The probe's Bessel quadrature was under-resolved at large argument.** Step
h = 0.15 (tol_exp 45) holds ~10⁻¹⁵ relative accuracy only to x ≈ 30, while the
instrument's actual range is **[0.562, 99.21]** — at the top, the probe setting
is **7.6 × 10⁻⁴ relative**. Because collocation columns are normalised before
the SVD, the corrupted columns would have been exactly the exponentially small
large-|μ| ones. The sealed instrument uses h = 0.08, tol_exp = 60 (≤ 1.8 × 10⁻¹³
across the whole range). **Honest follow-through**, run as a reproducible
post-verdict control (`qctl`): refining λ₁ under the two quadratures gives
**bit-identical** values, |difference| = **0.0**. So this was a *latent* defect,
not an active one, and the sealed number does not depend on the correction — it
is reported because a gate that only fires where it does not matter is still a
gate that fired, and because at the 25-digit rung or a wider window (where x_max
grows) it would matter.

**(ii) The probe's "8-digit / two-Y dev floor 6.2 × 10⁻⁹" was a search artifact,
not a measurement.** All fifteen probe dips reported the *identical* deviation
`6.159092791335752e-09` — that is `golden_min`'s tol = 2 × 10⁻⁸ bracket
subdivision offset, not a disagreement between the two Y-systems. With the
V-crossing refinement the same two systems agree to 8 × 10⁻¹³. This is why the
sealed run improves on the probe by four orders at the same double precision,
and it is why the 10⁻⁹ bar was clearable at all.

## 5. The P3 control — and the warning the criterion earned

All six displaced starts (λ_d = 1.0, 1.5, 2.0, 2.5, 3.5, 3.7, each ≥ 0.47 from
any eigenvalue) **found nothing**: in every case the golden search ran to a
bracket *endpoint* (no interior minimum at all), with σ at 0.91–1.02 × the scan
median.

**But note carefully.** At λ_d = 2.5, 3.5 and 3.7 the two-Y *agreement alone*
was 4.3 × 10⁻¹⁰, 3.9 × 10⁻¹⁰ and 1.3 × 10⁻⁹ — **at or below the sealed bar**.
That is not a spectral coincidence: with no interior minimum, both systems
terminate at the *same* deterministic bracket endpoint, so the agreement is an
artifact of the bracket. **The two-Y bar is therefore not by itself
discriminating; the σ-depth requirement is what kills the control.** The sealed
criterion is a conjunction, and this run is the demonstration that the
conjunction does real work rather than decorating a single test. Banked as a
methodological lesson: *a reproducibility bar measures the instrument's
determinism, not the object's spectrum.*

## 6. The kernel — recorded, EXCLUDED from this seal

Per the prereg, λ = 0 is deliberately outside the claim. Recorded for obligation
O2: |λ| < 10⁻¹⁴ on all four instruments; σ₁ = σ₂ ∈ [1.0, 1.6] × 10⁻¹² against
σ₃ ∈ [0.50, 0.53] — a **12-order gap**, dimension exactly 2, consistent with
DESIGN §5b. No kernel claim is banked here.

**Weyl screen** inside the window: 2·vol/(6π²) = 0.0685567 predicts ≈ 4.39
states at |λ| ≤ 4; found 4 (two eigenvalues × the §5c doubling) plus kernel
dimension 2. Screen only — sub-leading cusp terms for Dirac are unknown.

## 7. The three caveats the seal requires, carried verbatim

**(a) Internal-only validation (DESIGN §8, verbatim).**

> **What replaces the anchor** (internal-only validation, weaker than the
> scalar's anchored gate): (i) the probe's 8-digit reproducibility across three
> instruments (two Y's, two seeds, two word sets); (ii) G1: the operator
> identity Dψ_μ = λψ_μ verified at the mode level by finite differences against
> an independent mpmath implementation (probe: ≤ 1.9e−13 rel. residual) — this
> validates the mathematics independently of the Hejhal machinery; (iii) the
> theorem-backed shape gates §5(a),(b); (iv) the P3/P4/two-Y battery; (v) the
> Weyl screen (leading term only).

There is **no external anchor** for this number. Every check above is internal
to this programme. That sentence is the caveat, and it stands.

**(b) The literature caveat (DESIGN §8, verbatim) — now superseded in depth by
the O3 panel.** The original: *"No numerically computed Dirac/spinor eigenvalue
on ANY hyperbolic 3-manifold was found… Completing the sweep
(MathSciNet/zbMATH-grade) is obligation O3 and MUST precede any banked sentence
containing the word "first"."* (The priority word appears there as a **mention**
inside the quoted gate, not as a use; see §8.)

**(c) The multiplicity caution (DESIGN §5c, verbatim).**

> **Kramers-type doubling, observed and open.** The probe's ENTIRE singular
> spectrum is doubled at every λ (all σ's in equal pairs, on- and
> off-eigenvalue) — an instrument-level λ-preserving antiunitary, candidate
> J ∘ (a lift of the amphichiral symmetry of m004). Consequence if confirmed:
> every Dirac eigenvalue has even multiplicity, and the banked multiplicity
> language must say "quaternionic multiplicity 1" vs "complex multiplicity 2"
> deliberately. Resolving the mechanism is obligation O1 and blocks the seal of
> multiplicity CLAIMS (not of eigenvalue claims).

Reconfirmed at sealed settings across the whole 801-point scan: σ₁ vs σ₂ median
relative gap **8.7 × 10⁻¹⁶** (max 9.7 × 10⁻⁵), σ₃/σ₁ median 1.037 — the doubling
is not confined to the dips. **No multiplicity is claimed.**

## 8. O3 — the prior-art sweep, and the gate it leaves CLOSED

The panel ran adversarially (mandate: *try hard to find prior art; a found
citation converts OUTCOME A into a reproduction, which is the more valuable
result*). Its report is `O3_PRIOR_ART.md` + `o3_results.json`.

**What it reached.** zbMATH Open (MSC-coded structured queries, full reviewer
texts), OpenAlex (full-text index + citation graph), arXiv, Semantic Scholar,
INSPIRE-HEP, general web — run over raw HTTP against bibliographic APIs. Its
highest-yield move: the **complete 59-work citing set of Bär 2000** (the
discreteness dichotomy that makes the problem well-posed) enumerated and read
individually. **Every one is theoretical.**

**What it did NOT reach: MathSciNet** — HTTP 302 to a subscription auth wall.
**The gate names "MathSciNet/zbMATH grade" and the standard is therefore HALF
MET.**

> **THE GATE STAYS CLOSED.** No priority sentence is banked in this arc. The
> word is absent from every claim sentence here, from `arc_verdict.json`, and
> from the three ledgers, by deliberate choice and not by oversight. Half a
> named standard is not the standard.

**The three findings that will govern the sentence if the gate ever opens:**

1. **The must-pass control came back POSITIVE.** Gesteau–Pal–Simmons-Duffin–Xu,
   *Bounds on spectral gaps of hyperbolic spin surfaces* (arXiv:2311.13330,
   publ. 2025) computes Dirac eigenvalues on hyperbolic spin **surfaces and
   orbifolds** (e.g. `[0;3,3,5]` → t₁ ∈ [4.4021, 4.4109]; `[1;3]_sym` →
   t₁ ∈ [2.8293, 2.8369]) via the Selberg trace formula. **So computed spinor
   eigenvalues exist in 2D and are absent in 3D — the 3D blank is a result, not
   a search artifact.** Sharper still: the method was already available and
   already applied to Dirac in 2D and to hyperbolic 3-manifolds in the
   scalar/Floer setting; nobody carried it to a nonzero Dirac eigenvalue value
   in 3D.
2. **The near-miss that constrains any wording.** Lin–Lipnowski, *Dirac spectral
   flow and Floer theory of hyperbolic three-manifolds* (arXiv:2506.07238,
   2025) certify by computer assistance that a spin^c Dirac eigenvalue equals
   **exactly zero** at certified parameters on **closed** census manifolds. Every
   number they publish is a *parameter* (τ ∈ [0.1537, 0.1556]), not an
   eigenvalue; no eigenvalue value appears in their tables. **The only
   eigenvalue they pin is zero — precisely the object this seal EXCLUDES.**
   That is fortunate, and it is stated here rather than relied on silently.
   They should be cited **positively** as the nearest prior work.
3. **The contrast case.** Explicit Dirac spectra on 3-manifolds exist only where
   closed forms do — **flat** (Pfäffle 2000, Bieberbach) and **spherical**
   (Boldt 2017, lens spaces; Bär 1996, Killing spinors). None hyperbolic, as
   expected: hyperbolic 3-manifolds admit no closed form, so a number there
   requires numerics.

**Load-bearing qualifiers, recorded now for whoever writes that sentence later:
"nonzero" and "cusped".** An unqualified priority claim would be contestable and
must never be banked. The safe forms — held in escrow, NOT asserted here —
qualify on both.

## 9. Declared readings and honest limits

1. **"10-digit working precision."** The collocation/SVD path is IEEE-754
   binary64 throughout (≈ 15.95 decimal digits), exceeding a 10-digit
   requirement with ~6 digits of headroom; mpmath at dps 30–50 supplies the
   *independent* G1, assembly and Bessel checks. If the intent was
   arbitrary-precision arithmetic throughout, **this run does not satisfy it** —
   that is the O5 driver port and the 25-digit rung, explicitly not attempted.
   The reading was declared in stage `seal`, **before** the battery ran.
2. **"The sealed bar" for the P4 spread.** The prereg seals exactly one numeric
   bar (10⁻⁹); the spread bar is read as that same 10⁻⁹. Declared in stage
   `seal` before running; the measured spreads (0.0 and 4.4 × 10⁻¹⁶ within a
   system) make the reading immaterial.
3. **Deliberate deviations from the probe**: the Bessel quadrature step (§4(i))
   and the V-crossing refinement (§4(ii)). Both recorded in
   `results.json → seal.declared_choices`; both are tightenings, not loosenings.
4. **Not claimed**: multiplicity (O1); kernel exactness (O2); any priority
   sentence (O3, gate closed); ρ₂'s spectral type (O4); 25-digit certification
   (O5); PSLQ (not run — 12 digits is under the licensed-height threshold that
   made the scalar's PSLQ rung meaningful).
5. **Scan resolution**: eigenvalues closer together than ≈ 0.01 would merge into
   a single dip. Not excluded.

## 10. Cost

Gates 4 s · scan 1186 s · refinement 443 instrument-seconds over 12 refinements
· P4 24 restarts · P3 12 refinements. **Full sealed battery ≈ 50 minutes** on
this bench at double precision, against DESIGN §9's 1–3 day estimate for the
10-digit rung — the V-crossing refinement is the whole difference.

## 11. Files

`PREREGISTRATION.md` (sealed, hash above) · `dirac_sealed.py` (stages seal /
gates / scan / refine / p4 / p3 / verdict + the post-verdict `qctl` control;
imports the B933 probe machinery rather than copying it, and never writes into
the B933 directory) · `results.json` (every stage, every number, the declared-
choices block) · `scan_S1.npz`, `scan_S2.npz` · `run.log` · `O3_PRIOR_ART.md`,
`o3_results.json` · `DRAFT_FINDINGS.md` (the bench's draft, retained) ·
locks `tests/test_b940_dirac.py`.

---

**Verdict: OUTCOME A.** A certified Dirac eigenvalue on a cusped hyperbolic
3-manifold, λ₁ = 2.974550580, carrying all three caveats verbatim, with the
priority gate closed on a half-met standard and no priority sentence banked.
