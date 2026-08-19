# B1071 — THE SEALED LISTENER: all three claims HOLD; the derivation is PROMOTED

**Date:** 2026-08-19 · **Seat:** cc (banking) · sealed BEFORE compute (`docs/SEAL_LEDGER.md`
row of 2026-08-19; the prereg's hash committed pre-computation) · three independent
re-implementations (one per claim, no code reuse from the exploration cell wf_e25251a5-72a —
each rebuilt the instrument from the banked defining data by hand, own cyclotomic ring, own
reduction algorithms) · 3/3 agents, 0 errors · Gate 5 untouched.

## The verdicts

| claim | verdict | the decisive check | the fail-witness, exercised |
|---|---|---|---|
| C1 (the orbit backbone) | **HOLDS** | projective group EXACTLY 60 (icosahedral profile {1:1,2:15,3:20,5:24}); orbits exactly 12/20/30 + generic-60 witness; the fourth-orbit EXCLUSION proved (Möbius ≤2 fixed points + every non-identity element fixes exactly 2 of the 62; incidence 118 = 12·4+20·2+30·1) | an MB12 NEGATIVE CONTROL: corrupting the 12-orbit by one point makes exactly the removed vertex's order-5 stabilizer fire — the check is sensitive, not tautological |
| C2 (the pair) | **HOLDS** | u3/u6 on the size-12 orbit (R's eigen-axis, projective order 5); the UNIQUE Galois-individually-fixed pair — all 16 automorphisms applied to all 12 points exactly | BITE exhibited: every non-u3/u6 point moved by ≥8 of 16 automorphisms; the two closest calls (the real golden points, 8/16) explicitly located — no near-miss; no 13th point |
| C3 (the channels) | **HOLDS** | M_odd(g) = χ(g)·W(g) with W ∈ SU(2) EXACTLY for ALL 2880 elements (four exact criteria, 0 failures); Re = ½tr W proven + spot-verified at 3 complex ears; Im = ⟨n(g), Bloch(u)⟩ with exact axes m = 1..5, the two-direction separation witness exhibited | the all-2880 sweep IS the test (as sealed); the float margin quoted for orientation only, never in the verdict line |

## What is now true, and what is still gated

**PROMOTED**: the crossing prereg may cite **the derived listener pair** — Λ = "the minimal
exceptional orbit's Galois-individually-fixed directions" outputs exactly {u3, u6}, at
seal grade, twice independently (the exploration cell's three verifiers; this cell's three
fresh builds). The B641 credit line is inside the sealed claim itself (C3: the closure and
pointwise form of B641's law — "the strict law was SU(2) membership").
**STILL GATED (the seal's own scope clause)**: this is NOT a completed listener map under
`docs/LISTENER_MAP_SPEC.md` — AC3 runs on the silver instrument (B1072, designed), AC6's
type-conformance run is unattempted. Any citing text says "the derived listener pair."

## Method note (the file-drawer lock shaped the flow)

The B837 lock fired on the sealed-but-unreported tree and is RIGHT: the seal commit stays
local until the computation reports — the hash timestamps the seal; the push carries seal
and findings together. Recorded here so the next seal inherits the flow without the catch.

## Artifacts

- `b1071_results.json` — the three agents' full returns, verbatim (scrubbed of machine paths).
- The independent implementations lived in the session scratchpad (READ-ONLY discipline;
  each agent's audit trail and negative controls are quoted inside its return).