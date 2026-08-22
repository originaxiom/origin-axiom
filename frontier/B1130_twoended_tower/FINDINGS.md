# B1130 — P-TWOENDED: is the tower's arithmetic two-ended (E₆/√−3 AND E₈/√5)? PRECISION-FLOOR (leaning single-end)

**Status: banked (frontier). Verdict OPEN (PRECISION-FLOOR: the definitive test is
precision-gated; the cheap C₃ analysis leans single-end but a single data point cannot
decide). Value-probing wave, the structure question. Gate 5 untouched. Lock
`tests/test_b1130_twoended.py`.**

## The question

V-1 (B1124): C₃ = (724351/12597120)√3π³·C₀; its denominator 2⁷·3⁹·**5** grew a factor of 5,
breaking C₁/C₂'s {2,3}-smoothness. The object is two-ended (B981/B248: hyperbolic ℚ(√−3)/E₆
at cone-angle 0, spherical ℚ(√5)/E₈ at π). Is the 5 the E₈/√5 end entering the tower, or a
generic artifact?

## THE ANSWER: PRECISION-FLOOR (undecided, leaning single-end)

**Part A (cheap, C₃ analysed cold, own-bench re-verified):** 724351 = 53×79×173 — three
distinct, unrelated primes, none shared with C₁/C₂'s numerators, no φ/√5 structure; the 5
tested against L(2,χ₅), ζ_K(2), 1/φ^k, √5/π² — **no clean √5 fingerprint**. The 5 is
**equally consistent with generic von Staudt–Clausen denominator growth** (the Bernoulli/
zeta mechanism that introduces new primes) **and** with a genuine E₈/√5 signal — **a single
data point cannot distinguish them.** The structure (unrelated primes, no √5) leans generic.

**Part B (the definitive test): PRECISION-FLOOR.** Deciding it needs C₄/C₅ to ≥18 trusted
digits (to factor their denominators and see whether the 5 grows/recurs or √5 appears in an
odd coefficient). C₄/C₅ reached 0 trusted digits at tractable precision; the tower was
pushed toward N=70M but **the extension was STOPPED at ~1 hour** — a banking-seat resource
call: disproportionate compute for a nice-to-have structure question whose cheap analysis
already leans single-end. Reopenable only by a much larger tower (N ≫ 70M).

## Verdict

Two-endedness **UNDECIDED, leaning single-end** (ℚ(√−3) only) — the C₃ factor-of-5 is most
likely a generic denominator artifact, not the E₈ end. Honest OPEN, precision-gated. Gate 5
untouched.

> **RESOLVED by B1133 (2026-08-22): SINGLE-END confirmed.** C₄ = (278392949/1813985280)·π⁴·C₀
> was recognized via Aitken acceleration on existing data (30 digits vs B1124's computed
> value) — its denominator's prime 5 recurs at exponent 1 (SAME as C₃, no growth), no √5
> anywhere → the tower is ℚ(√−3) only and the C₃ factor-of-5 is a generic von Staudt–Clausen
> artifact. This precision-floor is lifted; the "leaning single-end" is now confirmed.
