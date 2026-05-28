# Probe B7 — Fisher–KPP creation dynamics

> **Speculative frontier work.** Everything here is a *logged observation*, not a
> claim (see `../../GOVERNANCE.md` §5). Nothing in this directory is promoted to
> `CLAIMS.md`.

## The question

The *gradient flow* (first-order, dissipative) of the derived potential (P16) is

```
∂τ/∂t = −V'(τ)/κ + D·∂²τ/∂x²  =  (1 + τ − τ²) + D·∂²τ/∂x²,
```

which is a **Fisher–KPP reaction–diffusion equation** with reaction
`f(τ) = 1 + τ − τ²`, satisfying `f(0) = 1 > 0` and `f(φ) = 0`. Does a seed near
`τ = 0` spread as a travelling wave that converts the unstable state `τ = 0`
("nothing") to the stable vacuum `τ = φ`?

## What the probe computes (`probe.py`)

A standard explicit finite-difference integration of the reaction–diffusion
equation from a small Gaussian seed at `x = 0`. Measures (i) the final spatial
average against `φ`, and (ii) the Fisher–KPP front speed `c = 2√(D·f'(0)) = 2√D`.

## The caveat (verbatim from SESSION3_SYNTHESIS.md)

> This is the gradient flow (dissipative), not the wave equation. Physical
> interpretation as "creation spreading" is suggestive, not derived. The
> wavefront speed `c = 2√D` depends on `D`, which is not determined.

So: `f(τ) = 1 + τ − τ²` is exact (it is `−V'(τ)/κ`, P16). The *dynamics* — first
order vs. second order, the diffusion constant `D`, the spatial manifold — are
inserted. The Fisher–KPP front-speed theorem is standard mathematics applied to
an inserted equation.

## Verdict

`STALLED` — the reaction term is exact; the reaction–diffusion dynamics and `D`
are inserted. See `FINDINGS.md`.
