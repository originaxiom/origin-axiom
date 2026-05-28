# B7 — Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Result

The gradient flow of the derived potential (P16),
`∂τ/∂t = (1 + τ − τ²) + D·∂²τ/∂x²`, is a Fisher–KPP reaction–diffusion equation.
Numerically, a small Gaussian seed near `τ = 0` spreads as a travelling wave and
the field converges to the golden vacuum:

```
final ⟨τ⟩ = 1.6180339887,   |⟨τ⟩ − φ| ≈ 3.6 × 10⁻¹¹
Fisher–KPP front speed c = 2√(D·f'(0)) = 2√D = 2.0  (for D = 1)
```

A coupled-Möbius-lattice supplement (`mobius_lattice` in the synthesis scripts)
shows the same attractor from random initial conditions, converging to `φ` at
machine precision in ~100 steps.

## What is exact vs. inserted

**Exact (P16):** the reaction term `f(τ) = 1 + τ − τ² = −V'(τ)/κ`, with
`f(0) = 1 > 0` (zero is unstable) and `f(φ) = 0` (golden vacuum is the stable
fixed point). The Fisher–KPP front-speed formula `c = 2√(D·f'(0))` is a standard
theorem.

**Inserted:** that the dynamics is first-order dissipative (gradient flow) rather
than the second-order wave equation of B6; the diffusion constant `D` (which sets
the front speed); the spatial manifold and boundary conditions.

## Caveat (verbatim from the synthesis)

> This is the gradient flow (dissipative), not the wave equation. Physical
> interpretation as "creation spreading" is suggestive, not derived. The
> wavefront speed `c = 2√D` depends on `D`, which is not determined.

## Verdict

**`STALLED`**

The reaction term is exact and the "nothing is unstable, golden vacuum spreads"
picture is mathematically clean *given* the reaction–diffusion dynamics. But the
dynamics and `D` are inserted, and the dissipative first-order form is a different
choice from B6's conservative second-order form. The two coexisting lifts (B6
wave equation, B7 gradient flow) of the *same* exact potential is itself the
tell: the potential is forced, the dynamics is not.
