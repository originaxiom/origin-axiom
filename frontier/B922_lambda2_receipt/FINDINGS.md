# B922 — λ₂ RECEIVED: the first 25-digit Maass eigenvalue on any hyperbolic 3-manifold

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
