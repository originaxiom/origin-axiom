# Addendum (2026-08-30) — this arc's claim line has the covering direction backwards

**Not an edit; the verdict line and this note stand together.**

## The defect

This arc's `claim_one_line` reads:

> *"…so orientation = choosing the child of the parent is a MATRIX FACT and **the discarded child
> is GIESEKING**."*

**Gieseking is not the child. It is the parent.**

## The computation, run on this bench

| | orientable | volume |
|---|---|---|
| Gieseking (`m000`) | **no** | 1.0149416064 |
| `m004` | **yes** | 2.0298832128 |

Ratio exactly **2.000000**. A double cover has *twice* the volume of its base, so **`m004` is the
orientation double cover OF Gieseking** — Gieseking is the base, `m004` the cover. The discarded
sibling at the orientation fork is therefore the **parent**, not the child.

## The record already had it right elsewhere

`docs/THEOREM_LEDGER.md` C5 states it correctly: *"the discarded det −1 sibling IS the Gieseking
manifold — **m004's own orientation double cover parent** … Orientation = choosing the child of the
parent."* The ledger and this arc's verdict line disagree, and **the ledger is right**.

**Nothing downstream changes.** The fork's grading (F5, FRAGILE), the identity M² = RL, the volume
ratio and the "nearest possible neighbour" reading are all untouched — only the word *child* stands
where *parent* belongs.

## Why it is worth a note

The identical error was live in THE PAPER's §2.1 earlier today and was corrected there. Finding it a
second time, in a banked verdict line, says the slip is **systematic in how this pair gets
described** rather than a one-off typo — the covering direction is easy to invert because the
*dilatation* runs the other way (φ upstairs, φ² down, as C5 itself records). Found by Cell 5's
record read.
