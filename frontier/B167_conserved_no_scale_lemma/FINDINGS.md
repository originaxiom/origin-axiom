# B167 — the conserved ⟹ no-internal-scale lemma (the firewall, stated)

**Date:** 2026-06-18. **Status:** sharpens the **POSTULATED** prose of `STRATEGIC_SYNTHESIS` §8a (the five-door
map) + B148 (κ conserved, dimensionless) + B151 (the scale lives in `ℏ/k` + the squashing radius) + P010 (the
Betti/flat category root) into a **stated structural argument** — a lemma with explicit hypotheses, a non-vacuity
witness, and an (argued-complete; POSTULATED) door-map case analysis. This is **firewall-side**: it *sharpens* the wall; it asserts **no
scale, no Λ, no crossing**. The conservation/dimensionlessness backbone is **[exact]**; the lemma + door-map are
**POSTULATED → "stated argument"** (the intended ceiling, owner-explicit). **Nothing promotes to `../../CLAIMS.md`**;
P1–P16 frozen. Ledger V158. Reproducer `conserved_no_scale.py`. (P3 of Masterplan II.)

## The lemma (stated)

> **Lemma (conserved ⟹ no internal scale).** Let `T` be a polynomial automorphism of the once-punctured-torus
> `SL(2,ℂ)` character variety (the trace map / the `SL(2,ℤ)` mapping-class action), and let `κ = x²+y²+z²−xyz−2`
> (`x,y,z = tr A, tr B, tr AB`) be its Fricke–Vogt first integral. Then:
> 1. **[exact] κ is conserved** — `κ∘T = κ` for the Dehn twists `Ta, Tb` and hence every metallic monodromy
>    `φ_m = Ta^m∘Tb^m`. It is constant along every orbit: *it does not run.*
> 2. **[exact] κ is dimensionless** — a polynomial in traces (pure numbers); it carries no free parameter with
>    units (it is not unit-homogeneous: it mixes `u⁰, u², u³`, so the only consistent unit assignment to the
>    traces is the trivial one).
> 3. **[stated] κ cannot source a dimensionful scale from within.** A dimensionful observable requires a quantity
>    that *runs* (a β-function / anomaly / flowing coupling). A conserved, dimensionless first integral is the
>    antithesis of a running coupling. So any scale must be supplied **externally**; from within the object there
>    is none.
>
> **Non-vacuity (the witness).** The lemma can fail in exactly one way: an **externally imported** scale `Λ`, with
> κ riding as a dimensionless coefficient (`κ·Λ⁴` — the θ-angle pattern). Units then come entirely from `Λ`, not
> from κ. So the lemma is *not* "scales are impossible" (false) — it is "scales are not **internal**", and the
> hypothesis it rests on is *no external scale is admitted* (the project's zero-parameter premise).

The backbone (1)–(2) and the witness are re-derived in `conserved_no_scale.py` (`ALL CHECKS PASS`), with an
**MB6/MB12 control**: a coordinate is *not* conserved (`Tb: x↦z`), so "conserved" is a real, falsifiable property
that κ has and a generic coordinate lacks.

## The door-map (the case analysis — argued complete; POSTULATED)

There are **argued to be** exactly five ways a scale can enter a scale-free structure; four are shut from within,
the fifth yields a *ratio*, not a scale. (This is §8a made precise — a taxonomy argument, not a proof of
exhaustiveness; each door is the physics mechanism + why it is blocked or external.)

| # | door | mechanism it needs | verdict for this object |
|---|---|---|---|
| 1 | **dimensional transmutation** | a *running* coupling (β-function) | **blocked** — κ is a conserved first integral; it does not run (L1) |
| 2 | **anomaly** | κ promoted to a *dynamical coupling* in an action with broken scale invariance | **blocked** — in 3d–3d κ stays a fixed label in the exponent (B151), never a coupling |
| 3 | **VEV / spontaneous breaking** | a dimensionful potential parameter | **blocked / hand-input** — no such parameter is present |
| 4 | **explicit imported scale** (`Λ_QCD`, Planck, the squashing radius) | put a scale in by hand, κ a dimensionless coefficient | **opens — but external** (the θ-angle pattern); the **non-vacuity witness**; it *exits* the zero-parameter program |
| 5 | **κ-discreteness → a dimensionless ratio** | a quantized/topological ratio (θ, Chern number, Hall conductance) | **a ratio, not a scale** — the only logically-open lane; its survivor is L14 (the trace-map = N=2\* S-duality identity), which is **mathematics** (`MB9`/`MB10`), not the SM's gauge content |

**Net:** the scale-lane is structurally shut (doors 1–3); the only door that opens (4) is external; the ratio-lane
(5) yields math, not a scale. **The wall has no internal door** — exactly the §8a verdict, now a stated argument.

## Scope / honesty (what this is NOT)

- It is **about this object's invariants** (a conserved first integral of the trace map; a topological invariant in
  `ℂ/4π²ℤ`), **not** a universal physics no-go theorem. As B148 states honestly: the dimensional argument is *an
  absence*, not a cited no-go. The lemma formalizes *that absence for this object*.
- It is **POSTULATED → "stated argument"** — the logical step (3) "no running ⟹ no internal scale" is a clean
  dimensional/RG argument, not a verify-gate-passing computation; only the conservation/dimensionlessness backbone
  (1)–(2) and the non-vacuity witness (4) are `[exact]`. **It does not promote to `CLAIMS.md`.**
- The Betti↔Hitchin grounding — *the scale enters on the Hitchin/Higgs side, externally* (P010/§8c) — sharpens
  doors 4/5 and will be folded in as a **later PR after P1** locates the scale concretely. This finding states the
  core lemma + door-map; the grounding fold-in is deferred (Masterplan II, P3-G).

## Firewall

This **is** a firewall artifact: it sharpens the wall without asserting a scale, a Λ value, or a crossing. No
spectral-mass identification; physics stays POSTULATED/one-way-cited; nothing to `CLAIMS.md`; P1–P16 untouched.

## Anchors
`STRATEGIC_SYNTHESIS` §8a (the five-door map this states) + §8c (the category root), B148/V137 (κ conserved by the
Dehn twists; dimensionless; κ=4·I_FV+2), B151/V140 (the scale lives in `ℏ/k` + the squashing radius; CS=0),
B130/V119 (κ free first integral; the elimination method), P010 (the Betti/flat category root), K001 (the Fricke
cubic + trace map), `speculations/S024` (the Hitchin side, where the scale is external). Ledger V158. External:
dimensional transmutation / β-functions (standard); GTZ / Dimofte / Córdova–Jafferis (the 3d–3d dimensional flow,
via B151).

## Reproduction
`python frontier/B167_conserved_no_scale_lemma/conserved_no_scale.py` — L1 conservation (Ta,Tb,φ_{1,2,3}); L2
MB6/MB12 control; L3 dimensionless; L4 the door-4 non-vacuity witness. Prints `ALL CHECKS PASS`.
