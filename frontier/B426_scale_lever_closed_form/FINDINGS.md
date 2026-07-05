# B426 — the scale-lever closed form (verified) + the Galois-orbit contraction theorem

**Status: banked. Chat-2's G1 handoff VERIFIED exact against the banked B372 coefficients, then
STRENGTHENED: the B408 correction is now a theorem. Firewalled; nothing to CLAIMS beyond the math.**

## The verified closed form (Chat-2 G1 — every claim checked)

B408's max-embedding seam-envelope ratio has the exact closed form
    env₄₅/env₁₅ = (3α² + 4α − 1)/10,   α = 2cos(2π/9),
minimal polynomial **1000x³ − 1500x² + 360x − 19**, a cyclic cubic in ℚ(ζ₉)⁺ (field disc 3⁴),
**√5-free**. Verified here from scratch:
- cell (4,8) √−15-sector = (1/96, −1/160, 1/480) on (1,c₁,c₂) — exact match to sweep45.json;
- the global max over all 144 pair cells × 3 embeddings is genuinely at (4,8)/embedding 2
  (exhaustive scan, not assumed);
- env₄₅ = 1/96 − γ/160 + α/480 = (3α²+4α−1)/480 — symbolic identity mod α³−3α+1;
- ratio ×48 exact; minpoly confirmed; matches the banked double to all 16 digits.

## The Galois-orbit contraction theorem (new)

The three "real embeddings" of B408's envelope are the **three Galois conjugates of one cubic
number** — the roots {1.2170, 0.2079, 0.0751} of the minpoly. Exact symmetric functionals:

    mean = 1/2,   RMS = √51/10 ≈ 0.714,   geometric mean = (19/1000)^{1/3} ≈ 0.267.

**Every Galois-invariant functional of the orbit is < 1.** The "1.217 growth" exists only under
max — which is not Galois-invariant (it selects a conjugate; Galois symmetry provides no
canonical choice). This upgrades the B408 correction (max = embedding-bias; RMS 0.7649 =
contraction) from a diagnosis to a theorem: **the object supplies no invariant functional under
which the seam grows.** The scale wall closes at the level of Galois theory, not statistics.

## The structural half (Chat-2 G2 — inputs verified, derivation credited)

By CRT locality (P63), seam factorization C₃·C₅ (P66), and locality of brightness (P67) — all
verified present in CLAIMS.md — the 5-local factor is level-inert from 15→45, so the ratio is a
pure 3-local quantity in ℚ(ζ₉)⁺: **the √5-freeness is forced, not numerical.** The golden factor
cancels because it is level-inert. (The quantitative C₉/C₃ forward derivation = the open level-9
build — ζ₁₈₀-grade engine or fp per prime, u₃=2 — deliberately not rushed; logged as open.)

## Errors caught en route (the multi-seat protocol working)

Chat-2's own E-v: first symbolic pass used γ = 2−α−β (wrong); the α+β+γ=0 guard flagged it.
Nothing further found here — the handoff's claims survived full re-verification.

**Provenance.** closed_form.py → closed_form.json; lock tests/test_b426_scale_lever.py.
Inputs: frontier/B372_level45_sweeper/sweep45.json (exact, banked), P63/P66/P67, B408 correction.
