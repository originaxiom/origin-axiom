# S3-a — THE OBSERVER'S CLOCK IS THE GEODESIC FLOW, AND ITS SPECTRUM IS ALREADY BANKED

cc3, 2026-08-09, under the owner's suspended-disbelief brief. Gate 5-Q; structure
only, no value compared to any measured quantity.

## What was open

B721 established **two clocks** and left the second unidentified:

> *"The object's own internal time (B716, the Anosov suspension of σ=[[2,1],[1,1]])
> is a REAL, hyperbolic, MEASURE-PRESERVING flow (det σ=1) — so its von Neumann
> algebra is tracial **type II₁**, and a tracial state has TRIVIAL modular flow…
> A genuine CMR/Connes–Rovelli thermal clock is **type III**… **Two clocks.**"*

B721 named clock 1 and typed clock 2. **This identifies clock 2.**

## The identification

For Γ a lattice in PSL(2,ℂ) — and Γ₄₁ is one, non-uniform, finite covolume —
the observer's algebra is not abstract:

```
        A_obs  =  L^∞(∂H³, Patterson–Sullivan)  ⋊  Γ₄₁
```

Three standard facts do the work, none of them new mathematics:

1. **Type III₁.** For finite covolume the limit set is all of S², the PS density
   has dimension δ = 2 (so PS = Lebesgue up to scale), and the action is
   non-singular, ergodic and amenable. The Maharam extension `∂H³ × ℝ` is
   ergodic **iff the geodesic flow is ergodic** — which holds by Hopf for finite
   covolume. Ergodic Maharam extension ⟹ trivial associated flow ⟹ **type III₁.**
2. **The modular flow is the geodesic flow.** By the continuous decomposition
   (Takesaki duality), `A_obs ≅ core ⋊_σ ℝ` with the core type II_∞ and the
   trace-scaling flow the modular one. On the double boundary
   `∂²H³ × ℝ ≅ T¹H³`, and quotienting by Γ gives **T¹(m004) with the geodesic
   flow** as the ℝ-action. So `core = L^∞(T¹ m004)` and **σ_t = the geodesic
   flow.**
3. **Its periodic data is the length spectrum.** The closed orbits of the
   geodesic flow are the closed geodesics; their periods are their lengths.

**Therefore: the observer's clock is the geodesic flow, and the spectrum of that
clock is m004's length spectrum — the emittance face.**

## The check — and it passes

The prediction is testable against banked numbers, because the length spectrum
is determined by the **trace field**: a loxodromic γ with trace κ has translation
length ℓ = 2 log|λ|, λ a root of z² − κz + 1. Taking the shortest, κ = (3+√−3)/2:

```
  ell computed from Q(sqrt-3) traces : 1.0870701449957391
  banked systole (B850)              : 1.08707014499574
  |difference|                       : 9.0e-16          MATCH
```

## The two clocks are genuinely different, and they sit on different faces

| | clock 1 — the object's | clock 2 — the observer's |
|---|---|---|
| flow | Anosov suspension of σ = RL | geodesic flow on T¹(m004) |
| algebra | **II₁**, tracial, trivial modular flow | **III₁**, core II_∞ |
| entropy | log φ² = **0.9624236501…** | **exactly 2** (= n−1 at K = −1) |
| its field | **hearing** ℚ(√5) — φ² is the dilatation | **being** ℚ(√−3) — the traces give the lengths |
| periodic data | the metallic word's orbits | **the length spectrum** |

The entropies differ (0.9624 ≠ 2), so these are not the same flow wearing two
names — B721's "two clocks" is confirmed, not dissolved.

**And note where each one lives.** The object's clock runs on **hearing**; the
observer's clock runs on **being**. The two faces are not two descriptions of one
time — they are two clocks, and B736's wall (transport ≡ 0 between them) is
exactly the statement that **neither clock can be read off the other.**

## What this does to three banked results

- **B716 — "no canonical arrow."** Re-read: the arrow is the **modular parameter
  of A_obs**. It is not canonical *in the object* because a tracial II₁ algebra
  has no modular flow — precisely B721's Δ = 1. It is canonical in the observer's
  algebra, where Tomita–Takesaki supplies it with no choice.
- **B721 — "the thermal-time lead fails identity."** It fails as an identity and
  succeeds as a **decomposition**: II₁ is what a III₁ algebra becomes after the
  crossed product with its own modular flow, so the object is the
  **time-averaged, observer-included** algebra. Time was integrated over, not
  absent.
- **B725 — Born content open.** The core is II_∞ and carries a trace. Gleason
  forces the *form* ω(P) = Tr(ρP); the missing ingredient was the trace, and the
  continuous decomposition supplies it. **The Born content question is now
  well-posed rather than open-ended.**

## And it explains an anomaly in the weight ledger

The weight ledger found 8 of 11 faces carry only weight-0 data, and only three
are scale-sensitive — emittance among them — and recorded that as a curiosity.
It is not:

> **The only face that can carry a scale is the face that carries time.**

Lengths have weight +1; a clock converts a scale into an observable. Emittance
is scale-sensitive **because it is the time face**. That is why the anchor probe
kept pointing there, and why the B666 torsor no-go's hypothesis class (outputs
in a number field carried by a finite/profinite group — all weight 0) excludes
it by construction.

## Scope, stated exactly

Facts 1–3 are standard (Sullivan, Connes, Krieger, Takesaki); nothing here is
claimed as new mathematics. What is new **to this programme** is the
identification and its consequence: clock 2 has a name, its spectrum is a face
the programme already computed, and the two clocks sit on the two faces the
B736 wall separates. **No dynamics is derived**; no measured quantity appears.

Reproduce: `python3 two_clocks.py`
