# S2 — THE BULK NORMALISATION: "one external input" is two, of different weight

cc3, 2026-08-09, under the owner's suspended-disbelief brief. Gate 5-Q; structure
only. No measured quantity; nothing compared to any value.

## The owed check

THE_FRAMEWORK banks the Gukov split `k·I_CS + iσ·I_grav` — k quantized, σ not,
`G_N = 1/(4σ)` — and notes that m004's **CS = 0 exactly** kills the quantized
half. It carries an explicit debt: *"(Normalisation check owed before this is a
claim rather than a lead.)"* This discharges it.

## The computation

Euclidean 3d gravity with Λ = −1/ℓ², whose saddle for a hyperbolic 3-manifold
is the hyperbolic metric itself:

```
    I = −(1/16πG) ∫ √g (R − 2Λ),     R = −6/ℓ²  ⟹  R − 2Λ = −4/ℓ²
    V_g = ℓ³ · Vol(M)                 (Vol(M) the K = −1 volume)
    ⟹   I = (ℓ / 4πG) · Vol(M)
```

Note the weights bookkeep exactly as the ledger requires: **volume is weight +3,
ℓ³ carries precisely that weight, so Vol(M) is weight 0** — a pure number, which
is what the ledger says every quantity of the object is.

In Brown–Henneaux variables `c = 3ℓ/2G`, so `ℓ/G = 2c/3`:

```
    I = (c / 6π) · Vol(M)

    for m004:   I = c · 0.107688649073150171
```

## The result — the input splits, and only half is forbidden

Carrying the units through shows **two independent external data hiding inside
"one input"**, and the weight ledger treats them completely differently:

| datum | weight | status under the weight ledger |
|---|---|---|
| **c = 3ℓ/2G** | **0** — a ratio of two lengths | **NOT excluded.** It lives in the dimensionless sector — the one sector the object *can* in principle speak to |
| **ℓ** | **+1** — a length | **Excluded.** `Hom(G,ℝ₊) = 0` and exact scale-covariance forbid any internal relation from fixing it, on any face |

So the honest statement is **not** *"the object needs one external input"*. It is:

> The object needs exactly **one dimensionful input (ℓ), permanently** — and one
> **dimensionless** input (c), which **is not forbidden to it.**

That is a strictly sharper position than the framework's, and it was hidden by
not carrying units. The scale wall is real but half as wide as recorded.

## The tension with S4 — surfaced, not smoothed

S4 typed B1000's five closings and found **four resources**, one of them the
ℝ₊-valued scale, concluding the interface is finite and saturated. **S2 shows
that closing is not atomic.** Two readings, and this arc does not choose between
them:

1. **The budget needs a fifth entry.** c is a real number, not an 𝔽₂ bit, so if
   it must be supplied externally then S4's *"four resources, nothing left
   over"* becomes five and the saturation claim weakens.
2. **c is not a closing at all**, because being weight 0 it is exactly the kind
   of datum the object's eight weight-0 faces could carry.

**This is now a decidable question rather than an assumption**, which is the
arc's contribution. It also flags that S4's headline is conditional on it, and
S4's own text should carry that.

## What would discharge the second half

Any weight-0 route to c. The object has weight-0 faces (8 of 11) and it has a
boundary; c is a *boundary central charge*. **This arc does not compute it and
does not claim it is computable** — it establishes only that the weight ledger
does not forbid it, which was previously assumed without being checked.

## Scope

Standard 3d gravity throughout (Einstein–Hilbert on a hyperbolic saddle,
Brown–Henneaux). **Nothing here is new mathematics or new physics.** What is new
to this programme is the units bookkeeping and its consequence: the scale input
is two data of different weight, and only the dimensionful one is provably
external.

Reproduce: `python3 bulk_action.py` (asserts I/c · 6π = Vol(m004)).
