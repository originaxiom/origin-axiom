# B598 — the L85 campaign opened; P0 (the C1 baseline) computed

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities. The
campaign document: CAMPAIGN.md (cells P0–P3, the constraint sheet, locked
outcomes per the adopted D1 prereg). Locks `tests/test_b598_p0.py`.
Provenance: all verification internal (owner + AI seats) — see the
pre-committed Review-18 scope in docs/progress/REVIEWS.md.**
Run: `python3 p0_c1_baseline.py` (mpmath, ~2 min).

## P0 — the C1 baseline, computed in-sandbox

The Kashaev invariant ⟨4₁⟩_N (the Habiro sum), N = 100..1600 at 40 digits:
- **The growth gate:** the corrected rate equals Vol(4₁)/2π to 1.15×10⁻⁴¹.
- **The 1-loop constant:** Richardson-extrapolated,
  > r_∞ = 0.759835685659812 = **3^{−1/4}** (agreement 8×10⁻¹²; the nearest
  > competing candidate is 24% away).
So ⟨4₁⟩_N ~ N^{3/2}·3^{−1/4}·e^{N·Vol/2π}: the τ₁-content is exactly where
the semiclassical correspondence puts it. Normalization bridge (recorded):
in the standard 1/√T one-loop form, T = √3 with **T² = |τ₁| = 3** (B581's
convention) — the Gaussian width enters squared, consonant with the hearing
law's quadratic structure. This upgrades the D1 prereg's B425-row from
[CITED] to [COMPUTED]: the SL(2) dictionary's baseline datum is now
in-sandbox.

## The campaign (CAMPAIGN.md)

P1 (the cusp table: the six H¹ representatives restricted to the peripheral
subgroup — the classical domain made explicit), P2 (the quantization arrow
through the Weil model at κ = 5, checked against the five-item constraint
sheet), P3 (the verdict cells C2/C3 and the locked A/B/D outcome). The
machinery inventory distinguishes what exists (B575/B581/B587 machinery)
from what P1/P2 must build (the per-block Fox H¹ solver with the peripheral
restriction; the Jordan-filtration pairing with the theta-basis).

## Governance registered alongside (owner directive)

Review 18's pre-committed scope now includes the provenance sweep (no
banked language may read as external verification/peer review — all
verification is internal, owner + AI seats since day 0; PROVENANCE.md to be
created at review) and the inner-terminology legibility sweep
(TERMINOLOGY.md or rephrasing). Registered in docs/progress/REVIEWS.md and
in the standing memory.

## Anchors

Chat-1's D1 prereg via B597 (adopted, corrected), B595/B596/B597 (the
constraint sheet), B581 (τ₁ = −3), B587 (the Weil machinery for P2), B575
(the H¹ model for P1), B67 (the longitude convention to pin in P1).

## P1 — THE CUSP TABLE, computed (exact; the classical domain data for P2)

`p1_cusp_table.py` (OA_SLOW; full output with all exact values:
`p1_cusp_table_output.txt`). For every block m ∈ {1,4,5,7,8,11}: a fresh Fox
cocycle solve over the exact B575 model gives **dim H¹ = 1** (an independent
re-derivation of B575-G4 — and a second, more direct discharge of B572-V2),
the regular-unipotency gate rank(ρ(a)−1) = d−1, and the exact peripheral
values **ξ(μ = a)** and **ξ(λ = [b,a])** (the fiber-boundary longitude, B67's
convention), normalized to leading coordinate 1. The m = 1 row, in full:
ξ(μ) = [1, 0, 3/8 − w/8], ξ(λ) = [3/4 + 3w/4, 1/4 + w/4, −w/2] (w = √−3).
The six (ξ(μ), ξ(λ)) pairs are the campaign's 6×2 boundary data — the dial's
cusp shadow, now explicit, exact, and entirely ℚ(√−3)-arithmetic (the
role-separation law's structural side, on display).

## The handoff adjudication (HANDOFF_ADJUDICATION.md)

The shifted-saddle ansatz adopted; the S₁-factorization registered as a P3
gate; the number-field claim CORRECTED in-sandbox (√−3 ∉ ℚ(ζ₂₀); the
amplitude lives in ℚ(ζ₅)) and replaced by the cleaner role-separation law;
the width bridge's θ-odd extension registered as P3's check; the anisotropy
remark held as a [HOOK]. Review-18 timing override registered (fires on L85
resolution, owner directive).
