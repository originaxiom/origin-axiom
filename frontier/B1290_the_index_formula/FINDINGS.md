# B1290 — THE INDEX FORMULA APPLIED: net chirality = −χ(∂⁺M), and I-26 becomes a question about the cusp

**Verdict: PROVED** (the arithmetic and its consequence) — with an explicit CITED-NOT-DERIVED fence
on the formula itself.

## The claim in one line

Applying the index formula `net chirality = χ(M, ∂⁺M)` to m004 gives **net chirality = −χ(∂⁺M)**,
so the zero this programme keeps finding is **forced whenever ∂⁺M is annular** — a *fourth*
independent route to it — and **I-26 stops being a representation-theory question and becomes a
question about the cusp torus**: *what is ∂⁺M, and what is its Euler characteristic?*

## What was computed here

```
chi(m004) = 1 - 2 + 1 = 0      # SnapPy's presentation: 2 generators, 1 relator;
                               # a cusped hyperbolic 3-manifold is homotopy equivalent
                               # to its presentation 2-complex
chi(T^2)  = 0                  # the single cusp's boundary torus

net chirality = chi(M, d+M) = chi(M) - chi(d+M) = -chi(d+M)

  d+M = torus          chi =  0  ->  net chirality =  0   ZERO
  d+M = annulus        chi =  0  ->  net chirality =  0   ZERO
  d+M = disc           chi =  1  ->  net chirality = -1   NONZERO
  d+M = pair of pants  chi = -1  ->  net chirality =  1   NONZERO
```

`python3 verification/index_formula.py` → `SELFTEST: PASS`.

## Why this matters, stated plainly

**χ(m004) = 0 is not an accident of this manifold** — it is true of *every* cusped 3-manifold with
torus boundary (χ of a compact 3-manifold with boundary is half the χ of its boundary, and tori have
χ = 0). So the whole content of the index formula, on any manifold of this class, sits in **χ(∂⁺M)**.

And **the natural pieces of a cusp-torus decomposition are annuli, which have χ = 0.** Any ∂⁺M
assembled from annuli returns zero net chirality *identically*, with no computation about
representations, twists, or embeddings entering at all.

### This is the FOURTH independent route to the same zero

| route | bench | method |
|---|---|---|
| B1267 | this bench | numerically, on the cusped mapping torus (index 0; W1/W2 rigid) |
| SM seat (sB1267–sB1276 range) | SM-derivation branch | exactly over ℚ(ω): `h¹(M;27) = 3 = h¹(M;27̄)` |
| fc R61 | physics seat | θ-equivariant abelian Higgs configurations have zero net chirality |
| **here** | this bench | **χ(∂⁺M) = 0 whenever ∂⁺M is annular** |

Four benches, four methods, one answer — and **none of the first three cited the others.** The
convergence is now recorded rather than rediscovered a fifth time.

It also joins the two *general* walls already banked: **E65** (self-duality of `Sym^n(SL(2))` ⇒ net
chirality identically zero) and **B1260** (Poincaré duality + χ = 0 kills net chirality on any
*closed* oriented 3-manifold). This arc is the *cusped* statement of the same phenomenon, and it
locates the escape precisely where B1260 said the cusped case was still open.

## How it reframes I-26

I-26 asked: *why does `h¹` count generations at all?* — and its price was **"exhibit the
compactification (or index theorem) in which this h¹ counts 4d chiral generations."** With the
formula in hand the price is **paid in form and unpaid in content**, and it becomes sharper and
geometric:

> **WHAT IS ∂⁺M, AND WHAT IS ITS EULER CHARACTERISTIC?**

A generation count needs **χ(∂⁺M) ≠ 0**, i.e. ∂⁺M must contain **discs** (χ = +1) or
**corner-carrying pieces** (a pair of pants, χ = −1) — *not* annuli. That is a statement about the
cusp torus alone. It is checkable. It is not a statement about representation theory.

**The I-26 row is updated accordingly**: its price is no longer "exhibit the compactification" but
**"identify ∂⁺M and compute χ(∂⁺M)"**. The row stays **UNEARNED** — the reframing does not pay it,
and the ratchet does not move.

## The named candidate (harvested, NOT verified here)

fc's **R61/R62** (harvested at B1277) reports **`Fix(θ)` = two arcs**, pairing `0 ↔ τ/2` and
`1/2 ↔ (1+τ)/2` on the cusp torus, and that **the mirror is broken by every generic filling, θ by
none**.

**Arcs cut corners, and corners are exactly what takes a torus decomposition off χ = 0.** Whether
`Fix(θ)`'s two arcs give `χ(∂⁺M) ≠ 0` is the concrete next computation. **It is fc's, not this
bench's** — it belongs to the cusp geometry, and this arc records the question rather than
answering it.

## Fences

1. **The formula is CITED, not derived here.** `net chirality = χ(M, ∂⁺M)` comes from the
   SM-derivation seat's literature sweep of the M-theory Higgs-bundle frame (harvested at B1277).
   This arc supplies χ(M) = 0, χ(T²) = 0, the annulus consequence, and the reframing — nothing more.
2. **The identification of "net chirality" with a physical generation count is I-26 and remains
   UNEARNED.** This arc *reframes* its price; it does not pay it.
3. **The R61 arc structure is harvest, not verification.** It is named as a candidate, with its
   provenance on the physics seat, and no claim about χ(∂⁺M) is made here.
4. **χ(M) = 0 is generic, not special to m004.** Nothing in this arc distinguishes the object; the
   discrimination, if any, must live in ∂⁺M.

## Controls (MB12, both directions)

- χ(M) is **computed** from SnapPy's own presentation, not assumed.
- The surface table exhibits **both** χ = 0 pieces (torus, annulus) **and** χ ≠ 0 pieces (disc, pair
  of pants) — so "annuli give zero" is not a vacuous claim about all surfaces.
- The consequence is stated as an **iff**, so a nonzero χ(∂⁺M) would *falsify* the zero rather than
  be absorbed into it.
