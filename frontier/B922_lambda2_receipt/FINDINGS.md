# B922 — λ₂ RECEIVED: 25 decimal places on the figure-eight complement

> ## ⚠ TITLE AND CLAIM CORRECTED BY B943 (2026-08-07)
>
> This arc originally read *"the first 25-digit Maass eigenvalue on any hyperbolic
> 3-manifold."* An adversarial prior-art panel, run retroactively when Review 40 found
> that the O3 gate had been applied only prospectively, returned **PRIOR ART FOUND —
> PARTIAL**. Three corrections, none touching the mathematics:
>
> 1. **The precedent number was wrong.** This arc asserted "~10 digits"; the published
>    figure is **13 decimal places** (r = 6.6221193402528, Picard orbifold ground state,
>    Aurich–Steiner–Then 2004 §8 — the "~10" came from their tables, which print 8).
>    **The 25 places lead by 12, not 15.**
> 2. **"On any hyperbolic 3-manifold" was wrong twice over** — Maass eigenvalues on
>    hyperbolic 3-manifolds have been computed since 1991 (an eight-item literature),
>    including on genuine **closed** ones (Inoue). The qualifier **"cusp form"** is
>    load-bearing and was absent.
> 3. **The pullback caveat**: Γ₄₁ ⊂ PSL(2,O₃) at index 12, so every published *parent*
>    eigenvalue is already an m004 eigenvalue. Resolved by a fact computed in-sandbox for
>    B943 — the parent's Weyl count at this height is **0.336**, its ground state at
>    r ≈ 7.072 — so this eigenvalue is **not inherited** from the parent. Screened, not
>    proven (see B943 §3).
>
> **The corrected statement, carrying no priority word** (the O3 standard is still half
> met — MathSciNet remains unreachable):
>
> > *The second Maass **cusp form** eigenvalue of the figure-eight knot complement,
> > r = 4.9000853730625213014795758, to 25 decimal places — improving the published
> > precedent for a Maass eigenvalue on a quotient of H³ from 13 decimal places to 25, and
> > **not inherited** from the parent Bianchi group PSL(2,O₃).*
>
> The 25-decimal computation, its seal, its battery and its certification are **unchanged**.
> The text below is retained unedited as the record of what was claimed.

**Date:** 2026-08-06 · **Seats:** cc3 (the computation, 58.1 h, sealed protocol
prereg `169e9042` — the hash on main's SEAL_LEDGER since the loss-audit repair)
· cc (banking receipt + independent spot-checks).

## The number

> **r = 4.9000853730625213014795758 · λ = 1 + r² = 25.0108366633012685587659**

For scale: H² computations reach 1000 digits; H³ had reached ~10. This is the
precedent-setting number, on the figure-eight knot complement's spectrum.

## The protocol (cc3's sealed chain, summarized for the record)

Validation gate: 10 overlap digits against the certified 8-digit value ·
P4: two perturbed restarts, spread 0.0 (three independent convergences) ·
P3 (the displaced must-fail control): PASSED — ended 0.385 away, found nothing
false · stability certification at +5 digits, quadratic convergence,
**|dr|_stab = 9.93×10⁻²⁷ against the sealed 10⁻²⁶ bar — a pass at 0.7%
margin, logged as close** (the honest note carried verbatim).

## The first sealed PSLQ pass (rung i): CLEAN

Both r and λ against all six programme fields + the minimal-polynomial box,
14 powered combinations under the B798 discipline: **no algebraic relation at
25 digits** within licensed heights (H ≤ 10⁴ quadratic). Scope exactly as
sealed: instrument validation + the first power step — NOT the campaign
falsifier (the 100-digit box). The first real data point on the campaign's
central question, pointing where the literature prior expects: no low-height
algebraicity.

## This bench's independent spot-checks (banked)

The arithmetic identity λ = 1 + r² recomputed at 40 dps ✓. The parked-H4 axis
run at 26 dps: r and λ against the BTZ entropy value log((5+√21)/2), Vol(4₁),
π², ζ(3), log φ, √21 — **CLEAN** (no PSLQ relation, coefficients ≤ 10⁴). The
quantum-gravity-spectrum reading (S073/H4) thus gets its first honest datum:
the eigenvalue is not a low-height combination of the banked gravitational
constants either.

## Standing

The parent run (7.072004187) launched detached (~2.5 days to the certified
25-digit parent = the definitive check on Grunewald–Huntebrinker 51.014);
then the PSLQ stage re-runs on both. The wave-1 re-audit (R37-6's carried
item) is now unblocked. The Maass paper's headline exists.

## Files

`spot_checks.py` (this bench's verifications) → locks in
`tests/test_b922_lambda2.py`. cc3's full corpus on their branch (B921's
harvest list).
