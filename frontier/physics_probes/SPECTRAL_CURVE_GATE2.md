# Gate 2 — the Seiberg–Witten identification is a forced single-point CM coincidence (negative)

**Date:** 2026-06-04. **Status:** exploratory, committed. Proven core P1–P16 untouched. Script:
`frontier/physics_probes/spectral_curve_gate2.py` (sympy + mpmath). Standalone; **no physics claim
earned**. Final gate of the spectral-curve plan.

**Question.** Even for the single m=2 (m136) spectral curve `y²=M⁴−6M²+1` — now verified to be the
manifold's actual A-polynomial discriminant (Gate 0) — is its `j=1728` / `τ=i` a *genuine*
Seiberg–Witten identification with N=2 SU(2) at the self-dual point, or a forced CM coincidence?

**Verdict: NEGATIVE — a forced single-point CM coincidence, not a SW identification.**

## What was computed (and confirms the web's exact numbers)

- Cross-ratio of the branch points `±(1+√2), ±(√2−1)` is `λ=2` (harmonic) ⇒ `j=1728`, CM by `Z[i]`.
- Period ratio `τ = ±i` (computed: `3.7e-9 − 1.0000000011·i`; `|Re τ|≈0, |τ|=1` — the lemniscatic CM
  point). Holomorphic period `= 2.6220575… = Γ(1/4)²/(2√(2π))`.
- These reproduce the AI-web computations (`τ=i`, the `Γ(1/4)²` period) exactly. **The algebra was
  correct.** They are standard CM consequences of `j=1728`.

## Why it is not a Seiberg–Witten identification

Pure N=2 SU(2) Seiberg–Witten theory is a **family** of curves over the Coulomb branch,
`y²=(x²−Λ⁴)(x−u)`; the SW differential `λ_SW` produces `a(u), a_D(u)`, the prepotential `F(a)`, the
dynamical scale `Λ`, and mass deformations. The self-dual point `u=0` has gauge coupling `τ=i` (the
S-duality fixed point).

The m=2 metallic side is a **single fixed curve** (one manifold, m136): there is **no** Coulomb-branch
parameter `u`, **no** SW-differential family, **no** prepotential function, **no** scale `Λ`. So:

- The entire match is **one number**: `τ=i` (⇔ `j=1728`) = the SU(2) self-dual coupling — and that
  number is **forced by the silver mean** (`a=6` in `κ=P²−6`; `j=1728 ⟺ a∈{0,±6}`).
- "m136's curve IS the SW curve of SU(2) at `u=0`" is **true but vacuous**: it says only that both are
  CM-by-`Z[i]` elliptic curves (hence isomorphic over `ℂ`). There is nothing on the metallic side —
  no Coulomb branch, prepotential, or dynamics — to identify with the gauge theory.

## Synthesis — the whole spectral-curve thread (Gates 0–3)

| gate | result |
|---|---|
| **0** (V32) | the m=2 trace-map curve **IS** m136's A-polynomial (verified, k=0, control-calibrated) |
| **1+3** (V33) | genus `3, 1, ≥2` — **not** "3,1,0"; no uniform family; only m=2 is elliptic; its CM is forced + arithmetically unrelated (`Q(i)` vs the silver field `Q(√2)`) |
| **2** (this) | the `j=1728`/`τ=i` SW "identification" is a **forced single-point CM coincidence**, not physics |

**What survives, exactly and honestly:** m136's A-polynomial spectral curve is the `j=1728` CM
elliptic curve (`τ=i`), a real, isolated, exact fact about one arithmetic 3-manifold — forced by the
silver mean. The web chat's *computations* were correct; the **4D-gauge-theory / Seiberg–Witten
framing was not earned** (no family, no Coulomb branch, no prepotential). The thread is **number
theory, not physics** — consistent with the project's standing finding that the framework does not
cross into dynamical 4D physics. Proven core untouched. The spectral-curve plan is complete; all four
gates banked.
