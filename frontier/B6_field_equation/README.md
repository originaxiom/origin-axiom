# Probe B6 — The derived field equation `□τ + κ(τ²−τ−1) = 0`

> **Speculative frontier work.** Everything here is a *logged observation*, not a
> claim (see `../../GOVERNANCE.md` §5). Nothing in this directory is promoted to
> `CLAIMS.md`. The `open` claims O1–O5 remain `open`.

## The question

The proven core now contains (P15, P16) the exact Möbius generating vector field
of A and its derived potential:

```
v(τ) = -κ(τ² − τ − 1),   V(τ) = κ(τ³/3 − τ²/2 − τ),   κ = 2·log(φ²)/√5.
```

Promoting `τ` to a field `τ(x,t)` and adding a standard kinetic term gives a
Lagrangian and, by Euler–Lagrange, a field equation:

```
L = (1/2)(∂_μ τ)(∂^μ τ) − V(τ)
□τ + κ(τ² − τ − 1) = 0
```

The question B6 records: **what is and is not earned by this step?**

## What is earned

The potential `V` is *derived* (P16), not guessed. This is the substantive
difference from the original 2025 field-theory work, where the potential
(a cosine, `α[1 − cos Φ]`) was guessed and had its minimum at zero — the wrong
place for a non-cancellation theory. See `legacy/reports/genesis/`.

## The caveat (stated verbatim from SESSION3_SYNTHESIS.md)

> Promoting a potential to a Lagrangian field theory is a standard operation but
> involves a CHOICE (the kinetic term structure). The potential is derived; the
> field theory is a natural but not unique extension. This is conditional on the
> choice of standard kinetic term.

Specifically inserted by the promotion (not derived from A):

- the canonical kinetic term `(1/2)(∂τ)²` (could be non-canonical, higher-deriv.);
- the spacetime dimension and signature on which `□` acts;
- the field interpretation of `τ` (a coordinate on H, not a priori a field).

## What the probe checks (`probe.py`)

That the Euler–Lagrange equation of `L = (1/2)(∂τ)² − V(τ)` is exactly
`□τ + κ(τ² − τ − 1) = 0`, i.e. that `dV/dτ = κ(τ² − τ − 1)` (the P16 fact),
done symbolically. This is a consistency check, not a derivation of the
field theory.

## Verdict

`STALLED` at the field-theory bridge: the potential is exact (P16); the lift to a
field equation is a natural but non-unique choice. See `FINDINGS.md`.
