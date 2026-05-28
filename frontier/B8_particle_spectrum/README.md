# Probe B8 — Particle spectrum around the golden vacuum

> **Speculative frontier work.** Everything here is a *logged observation*, not a
> claim (see `../../GOVERNANCE.md` §5). Nothing in this directory is promoted to
> `CLAIMS.md`.

## The question

Expanding the field of B6 around its minimum, `τ = φ + ε`, gives a massive scalar
with cubic self-interaction:

```
□ε + κ√5·ε + κε² = 0
mass²   = V''(φ) = κ√5 ≈ 1.924847   (this part is exact — P16 / mass_squared())
coupling g = κ ≈ 0.860818
m/g = √(5/(4·log φ)) ≈ 1.611710
```

The number `m/g ≈ 1.6117` is *close to* `φ ≈ 1.6180` but **not equal**.

## The caveat (verbatim from SESSION3_SYNTHESIS.md)

> "particles" here means small oscillations of a 1+1 field around its minimum.
> This is standard QFT language but has no connection to observed particles. The
> near-miss `m/g ≈ φ` is NOT exact and should NOT be inflated.

This probe exists in part to **record the near-miss honestly** so it is not later
mistaken for a result. `m/g = √(5/(4·log φ))` is an exact closed form (verified
symbolically), and it is exactly `√(5/(4·log φ))`, which is *not* `φ`. The
difference `|m/g − φ| ≈ 0.0063` is real.

## What the probe computes (`probe.py`)

`mass² = κ√5`, `mass = √(κ√5)`, `coupling = κ`, the ratio `m/g`, and its exact
closed form `√(5/(4·log φ))`, alongside `φ` to make the near-miss explicit.

## Verdict

`STALLED`; the near-miss `m/g ≈ φ` is explicitly **not** promoted. The mass²
and coupling are exact functions of κ; their *interpretation as a particle
spectrum* requires the inserted 1+1 field theory of B6. See `FINDINGS.md`.
