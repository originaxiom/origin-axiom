# ADDENDUM 2026-09-06 — B1290 supplies the CUSPED statement this arc left open

**B1260's verdict is unchanged.** This addendum records where its named gap was filled.

## What B1260 established

The **closed** wall is general: Poincaré duality plus χ = 0 kills net chirality on **any closed
oriented 3-manifold**. And in the **cusped abelian** sector, Alexander reciprocity walls it too.
B1260 named **W1** and **W2** and left the **cusped, non-abelian** case as the surviving room.

## What B1290 adds

Using the index formula `net chirality = χ(M, ∂⁺M)` — **cited from the SM-derivation seat's
literature sweep, not derived on main** — the cusped case reduces to a single Euler characteristic:

```
chi(m004) = 1 - 2 + 1 = 0      (SnapPy's presentation; generic to cusped torus-boundary manifolds)
chi(T^2)  = 0
=> net chirality = -chi(d+M),   ZERO IFF chi(d+M) = 0
```

**So the surviving room B1260 named is not automatically nonzero — it is nonzero exactly when
`χ(∂⁺M) ≠ 0`.** Annuli (χ = 0) give zero identically; **discs** (χ = +1) and **corner-carrying
pieces** (χ = −1) are what can escape.

## Why this sharpens rather than reverses B1260

B1260's negative was about *what the closed wall forbids*. B1290 is **not** a fifth wall: it is the
**condition** under which the cusped room is genuinely open, and it is checkable. Read together:

- **closed** → zero, always (B1260, PD + χ = 0)
- **cusped abelian** → zero (B1260, Alexander reciprocity)
- **cusped, annular ∂⁺M** → zero (B1290)
- **cusped, ∂⁺M with discs or corners** → **the only room left**, and now stated as a computation

**The named candidate**, harvested from fc's **R61/R62** and **not verified on main**: `Fix(θ)` is
**two arcs** on the cusp torus (0↔τ/2, 1/2↔(1+τ)/2). **Arcs cut corners.**

**I-26 remains UNEARNED**; its price is restated at B1290 to *"identify ∂⁺M and compute χ(∂⁺M)"*.
