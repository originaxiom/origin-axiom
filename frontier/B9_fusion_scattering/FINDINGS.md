# B9 — Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Result

Two structures rest on the same polynomial `τ² − τ − 1`:

- **Fibonacci fusion** (P2, exact category theory): `τ × τ = 1 + τ`, i.e.
  `τ² − τ − 1 = 0`, with quantum dimension `φ`.
- **The cubic vertex** of B8: expanding `V(φ + ε)` gives quadratic coefficient
  `½·κ√5` (the mass term) and cubic coefficient `κ/3` (the `2 ↔ 1` self-
  interaction vertex). Verified symbolically.

Both descend from `τ² − τ − 1`. This is the same "six faces" observation
(one polynomial in several mathematical contexts), not a new equivalence.

## What is shared vs. what is NOT derived

**Shared:** the polynomial `τ² − τ − 1`. Genuinely the same object in both the
fusion rule (P2) and the potential/vertex (P16).

**NOT derived:** a map between the Fibonacci fusion category and a scattering
amplitude. The fusion rule is exact modular-tensor-category data; the cubic
vertex is a perturbative artifact of the *inserted* 1+1 field theory (B6). There
is no functor here, only a shared characteristic polynomial.

## Caveat (verbatim from the synthesis)

> "analogous to" is not "derived from." The fusion category is exact algebra; the
> cubic vertex is a perturbative field theory artifact. They share a structure but
> the mapping is not rigorous.

## Verdict

**`STALLED`** — shared polynomial, not a rigorous fusion ↔ scattering map.

This is the weakest of B6–B9 in terms of what it earns: B6 lifts an exact
potential, B7 evolves an exact reaction term, B8 reads off exact `mass²`/coupling;
B9 only observes that two *separately exact* facts (P2 and P16) involve the same
polynomial. Worth recording as part of the "six faces" picture, but it should not
be described as deriving particle scattering from anyon fusion.
