# Addendum (2026-08-30) — this arc's verdict line overstates its own GC-27 cell, for λ

**Not an edit. The verdict line and this note sit together**, per the house rule for corrected
inputs that keep counting.

## What the verdict line says

> *"the sigma and lambda continuous legs sit on the **non-normalizable side** of the sharp
> boundary, which is **WHY they are anchors**"*

## What this arc's own cell record says (`verification/batch5b_cells.json`, GC-27)

> the dichotomy *"cleanly explains why σ and λ sit on **opposite sides** of a sharp boundary"* …
> *"and **λ fails even the theorem's first hypothesis (no (T,G) pair has been read off D for it)**
> — so the general seal is **PARTIAL**, with the two remaining lemmas named exactly"*

GC-27's verdict field is **`PARTIAL`**, not PROVED.

## The discrepancy, stated exactly

Two distinct claims, and they are not compatible:

1. **Side.** The verdict line puts σ and λ on the *same* (non-normalizable) side; the cell puts them
   on *opposite* sides.
2. **Reach — the load-bearing one.** The verdict line says the dichotomy **explains** why λ is an
   anchor. The cell says the theorem **does not reach λ at all**: λ fails its *first hypothesis*,
   because no (T, G) pair has been read off D for it. A theorem whose hypothesis is unmet explains
   nothing about the case.

**The summary is wrong in the direction that makes the record look more finished** — which is the
direction that matters, because the one-line verdict is what downstream surfaces quote.

## What stands, and what does not

- **STANDS**: the three-regime dichotomy itself, a theorem in each regime; the new boundary
  characterization (*prior-vs-point is ill-typed exactly at Haar non-normalizability*); the
  selector-free relational bit ε(A,M) = −1, conjugation-invariant on 8/8 tested conjugators; and
  **σ's** placement, which the cell does support.
- **DOES NOT STAND**: that this arc explains why **λ** is an anchor. It does not. λ's status is
  *hypothesis unmet*, which is a **weaker and more useful** statement — it names precisely what
  would change it.

## Why this is worth a note rather than a shrug

B1220 assembles λ's acceptance gate from GC-15's theorem plus this cell's boundary
characterization, and the gate's **failing** branch is exactly this cell's finding: *no (T, G) read
off D*. Had the verdict line's stronger reading been carried forward, λ would have looked explained
and the gate would never have been written. **E53 at its smallest scale — one arc, two texts, and
the shorter one is the one everybody reads.**
