# B6 — Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Result

The Euler–Lagrange equation of `L = (1/2)(∂_μτ)(∂^μτ) − V(τ)`, with the derived
potential `V(τ) = κ(τ³/3 − τ²/2 − τ)` (P16), is exactly

```
□τ + κ(τ² − τ − 1) = 0.
```

Verified symbolically: `dV/dτ = κ(τ² − τ − 1)` is the P16 fact, so the EL
equation follows immediately. The homogeneous (constant) solutions are exactly
the critical points of `V`: `τ = φ` (stable), `τ = −1/φ` (unstable). `τ = 0` is
**not** a solution, because `V'(0) = −κ ≠ 0` — the formal expression of "nothing
is unstable" in this model.

## What is earned vs. inserted

**Earned (exact, in the proven core):** the potential `V` and hence the force
law `V'(τ) = κ(τ² − τ − 1)`. This is the difference from the 2025 work, where the
potential was a guessed cosine with its minimum at zero (see
`legacy/reports/genesis/01_Master.txt` for the original critique). The derived
cubic has its minimum at `φ`, the correct shape for non-cancellation.

**Inserted (the bridge, not derived from A):**

- the canonical kinetic term `(1/2)(∂τ)²` — a choice; non-canonical or
  higher-derivative kinetic structures are equally available;
- the spacetime dimension and signature on which `□` acts;
- the interpretation of `τ` as a field rather than a coordinate on the
  upper half-plane H.

## Caveat (verbatim from the synthesis)

> Promoting a potential to a Lagrangian field theory is a standard operation but
> involves a CHOICE (the kinetic term structure). The potential is derived; the
> field theory is a natural but not unique extension. This is conditional on the
> choice of standard kinetic term.

## Verdict

**`STALLED`**

The field equation is the natural field-theoretic lift of an exact result, but
the lift is a choice. This is the same force-vs-target asymmetry the Phase C
probes named: the potential (the "force") is now derived, but the carrier (the
field theory, its kinetic term and dimension — the "target") is still inserted.
The novelty is that, unlike every Phase C probe, the *potential itself* is no
longer inserted — it is P16. The remaining gap is precisely the kinetic/geometric
structure.
