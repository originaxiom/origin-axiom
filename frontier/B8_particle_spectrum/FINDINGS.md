# B8 — Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Result

Expanding `τ = φ + ε` in the B6 field equation gives `□ε + κ√5·ε + κε² = 0`:

```
mass²    = V''(φ) = κ√5 ≈ 1.924847          [exact — P16, mass_squared()]
mass     = √(κ√5)       ≈ 1.387389
coupling = κ           ≈ 0.860818
m/g      = √(5/(4·log φ)) ≈ 1.611710        [exact closed form]
φ        ≈ 1.618034
|m/g − φ| ≈ 0.006324                         ← near-miss, NOT zero
```

The closed form `m/g = √(5/(4·log φ))` was verified symbolically: it reduces
(using `(1+√5)² = 2(3+√5)`) to a clean expression in `log φ`, and it is **not**
`φ`. The agreement to ~0.4% is a coincidence of the logarithm, not an identity.

## What is exact vs. inserted vs. explicitly disclaimed

**Exact (functions of κ, hence of A):** `mass² = κ√5` and `coupling = κ`.

**Inserted:** the reading of these numbers as a *particle* mass and coupling
requires the 1+1 field theory of B6 (itself an inserted lift). "Particle" here
means a small oscillation of that field around its minimum.

**Explicitly disclaimed:** the near-miss `m/g ≈ φ`. This probe exists partly to
record it honestly so it cannot later be mistaken for a result.

## Caveat (verbatim from the synthesis)

> "particles" here means small oscillations of a 1+1 field around its minimum.
> This is standard QFT language but has no connection to observed particles. The
> near-miss `m/g ≈ φ` is NOT exact and should NOT be inflated.

This is the same failure mode the project archived as D-class numerology
(`docs/ARCHIVE.md`): a suggestive constant that is close to a meaningful number
but not equal to it. Logging it here under an explicit disclaimer is the
disciplined alternative to either inflating it or hiding it.

## Verdict

**`STALLED`** — and the `m/g ≈ φ` near-miss is explicitly **not** promoted.
