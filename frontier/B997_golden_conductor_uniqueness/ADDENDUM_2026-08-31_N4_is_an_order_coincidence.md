# Addendum (2026-08-31) — this arc's N=4 clause is wrong, and this arc's own sibling test refutes it

**Not an edit. The verdict line and this note stand together.**

## The defect

This arc's `claim_one_line` contains:

> *"|SL(2,ℤ/N)| is a McKay-group order for EXACTLY N in {3,4,5} — 24 = 2T → E6, 48 = 2O → E7,
> 120 = 2I → E8 … note the coincidence that those three N are exactly the three exceptional McKay
> groups 2T, 2O, 2I, i.e. **E6, E7, E8, the whole exceptional series and nothing else**."*

The **order** statement is correct. The **group** statement is not. `SL(2,ℤ/4)` has order 48 = |2O|
and **is not 2O**, nor any binary polyhedral group.

## The refutation, using this programme's own instrument

**B1019 already owns the discriminator.** It killed the silver sibling by counting involutions:
*"silver m=2 gives ORDER 32 WITH SEVEN INVOLUTIONS and no −I."* The same test, never applied at
N = 4, settles it — recomputed here by direct construction:

| group | order | involutions | elements of order 8 |
|---|---|---|---|
| SL(2,ℤ/3) | 24 | **1** | – |
| **SL(2,ℤ/4)** | **48** | **7** | **0** |
| **2O** | **48** | **1** | **12** |
| SL(2,ℤ/5) | 120 | **1** | – |

The kernel of SL(2,ℤ/4) → SL(2,ℤ/2) ≅ S₃ is ≅ (ℤ/2)³, every element an involution. **Every binary
polyhedral group embeds in the unit quaternions, where −1 is the unique involution.** Hence
SL(2,ℤ/4) ≇ 2O, and E₇ is not reached this way.

## What stands

**The arc's conclusion is untouched and slightly strengthened.** The admissible set shrinks from
{3,5} — since m² + 4 = 4 forces m = 0, degenerate and not a metallic word, N = 4 was never reachable
by the metallic family anyway. The uniqueness at **m = 1, the golden** is exactly as proved: m²+4 = 3
has no integer solution, m²+4 = 5 gives m = 1, and the ζ(2) bound (|SL(2,ℤ/N)| ≥ 6N³/π² > 120 for
N ≥ 6) still closes the family.

**What goes is the flourish** — "the whole exceptional series and nothing else" — and the E₇ slot.
Only two moduli give a binary polyhedral group, so there is no three-way coincidence to remark on.

## Why this is worth recording rather than quietly fixing

This programme's own method section refuses to accept a short-catalogue coincidence as evidence.
**The N = 4 clause is a short-catalogue order coincidence, presented as a McKay fact, inside the arc
that proves the entrance uniqueness.** It was found by an external reader, not by us — and the
instrument that refutes it was banked in B1019 before the claim was written. We had the test and did
not turn it on the case that needed it.
