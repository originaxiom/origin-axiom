# PREREGISTRATION — the reopened G₂ hatch: is the enhancement isolated, in the sense Acharya–Witten needs?

*Outside bench, 2026-09-14. Sealed before computation. Gate 5 untouched.*

## Why this, and why it is the lift axis

The record's own answer to "what dimension does the chirality index live in" is **6 or 7**, never 3.
`docs/IDENTIFICATION_LEDGER.md` **I-26**: *"the index-theorem argument that licenses 'massless
multiplets = dim H¹' lives on a **Calabi–Yau 3-fold (real 6d) or a G₂ 7-manifold**; its transport to a
real 3-manifold's H¹ is never exhibited."* And the sibling branch's index campaign converged on the same
thing from below — B1334/B1339: *"the vanishing is dimension-counting, not the object"*, mechanism
Poincaré–Lefschetz / half-lives-half-dies / **image Lagrangian**.

**And 6d and 7d are the same door here.** B1259's own consequence, verbatim:

> The route to chiral matter therefore requires genuine **CURVATURE** — a conical G₂ singularity, **whose
> local model is a cone over a 6-manifold** rather than a linear action on ℝ⁷.

## The state of the hatch

**B1084 (PROVED, on this branch, reproduced here before sealing):** the flat G₂ orbifold
`(ℂ² × ℝ³)/Ĝ`, **|Ĝ| = 96** — **ONE E₆ locus with pointwise stabilizer exactly 2T** (the object's own
McKay group), **three A₁ families** (orbits 6/12/12, stabilizers exactly ℤ/2), the **Acharya–Witten
COLLISION criterion MET at the apex**, and **ISOLATION FAILING**: census {3: 53, 1: 42}, no
0-dimensional fixed set.

**B1259 (NEGATIVE):** that failure is a theorem, not a census — G₂ < SO(7), and every element of
SO(2k+1) has eigenvalue +1, so **every nontrivial element of any flat G₂ orbifold group fixes at least a
line**. No Ĝ escapes.

**B1304 (sibling branch, absent here until this session) SCOPED it:**

> The SO(odd) lemma does rule out an isolated point of the total orbifold singular set … **It does not by
> itself rule out an isolated enhancement stratum within that set. Its quantifiers may not be
> interchanged.**

verified on (ℤ/2)³ ⊂ G₂ with subgroup-order → fixed-dimension **{1: 7, 2: 3, 4: 1, 8: 0}**: *"**The
origin is an isolated maximal-isotropy stratum although no element has an isolated fixed point.**"*
So *"the hatch 'an isolated enhancement stratum' is **reopened as a question**"*. **No arc has walked it.**

## THE QUESTION, and it separates two readings that have been run together

Acharya–Witten chirality needs an **A-type locus meeting an E-type locus at an isolated point**. Two
different things are called "isolated" in the above:

- **(R1) an isolated maximal-isotropy STRATUM** — the apex, where *everything* meets. B1304 shows this
  survives the SO(odd) lemma.
- **(R2) an isolated A₁–E₆ INTERSECTION** — one A₁ locus meeting the E₆ locus in dimension 0.

**These are not the same, and the reopening establishes (R1), not (R2).** This cell computes (R2)
exactly, on B1084's own Ĝ, with B1084's own exact ℚ(√2) machinery.

**Computed:** for each of the 30 A₁ planes, the exact dimension of its intersection with the E₆ locus,
and the pointwise stabilizer of each intersection.

## THE TWO OUTCOMES

- **A — some A₁ locus meets the E₆ locus in dimension 0.** Then (R2) holds on this Ĝ, AW isolation is
  available in the sense the construction needs, and the hatch is genuinely open — the strongest
  possible result on this axis.
- **B — every A₁–E₆ intersection has dimension ≥ 1.** Then (R2) fails, and B1304's reopening
  establishes (R1) only. **The hatch is open as stated and shut as needed**, and the cell says exactly
  that, with the intersection dimensions as the evidence.

## CONTROLS

| # | control | catches |
|---|---|---|
| **G1** | **B1084's own script is re-run first** and must reproduce its banked items: \|Ĝ\| = 96, census {3: 53, 1: 42}, stabiliser of ℝ³⊕0 = 24 = the 2T copy, 30 planes with stabiliser order 2 in orbits [6, 12, 12] | a drifted or mis-built group; nothing after it counts otherwise |
| **G2** | the intersection dimension is computed by **exact rank over ℚ(√2)**, never numerically, and each intersection's pointwise stabiliser order is printed beside it | a float rank collapsing a transverse intersection |
| **G3** | **the computation must be able to return 0** — run it on a constructed pair of subspaces meeting only at the origin and require dimension 0 | a routine that can only ever report ≥ 1 (#164: an instrument that cannot fire) |
| **G4** | the population is printed before any conclusion: 30 planes, 1 E₆ locus, 30 intersections | the `B1197` vacuity trap |

## WHAT THIS CELL MAY NOT CONCLUDE

**Nothing about what Acharya–Witten's theorem formally requires** — that is literature, and the record's
own fence on B1304's example is *"the example is not an Acharya–Witten construction."* This cell
computes **geometry**, and states the two readings so a specialist can say which one AW needs. **No
chiral matter is derived.** **No generation count** — I-26 is UNEARNED and this does not touch it. No
value. Gate 5 untouched.
