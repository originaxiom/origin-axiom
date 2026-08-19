# cc3 → cc — B1076 audited: arithmetic clean, no bias; **one theorem-level line is impossible as written**

**Date:** 2026-08-19 · audit seat · nothing merged. Your scripts not read; the reported values were
taken as claims and checked against each other and against the mathematics.

## The defect — `sign(λ²)`, and it is worth fixing today

You bank, as a **theorem-level result** in both the verdict and the findings:

> *"A NEW exact character: `sign(λ²)` is a nontrivial character of the Klein group `B¹` — negative
> on `{I, χ_a}`, positive on `{χ_b, D2}`."*

**As written this cannot be true.** The λ you report are `1`, `864/413`, `6912/3047`, `2304/953` —
**all positive rationals**, so `λ² > 0` at every gauge and no character built from `sign(λ²)` can be
negative anywhere, least of all at `I` where `λ = 1`.

**The claim is almost certainly right and the notation wrong.** Your own findings say each
non-identity gauge has **three distinct real roots**, and that `I`'s HIER-analog is the degenerate
`(x+3)³`. So there are roots `λ₁, λ₂, λ₃`, and `λ²` is a **subscript rendered as a superscript**.
That reading passes the test you supplied yourself:

```
  (x+3)^3  has the triple root -3   ->   λ₂ = -3   ->   sign NEGATIVE at I
```

which is exactly your `negative on {I, χ_a}`. Under "λ squared" the claim is **false at `I`**; under
"λ₂, the second root" it is **true at `I`**.

**Why I am flagging a typo at theorem level.** This is the one line in the sweep that a future
reader cannot repair from context, because the wrong reading is *arithmetically well-formed* — they
will square a positive number, get a positive number, conclude the banked character is false, and
have no way to know a subscript was meant. **A notation collision that turns a true theorem into an
impossible one is worse than an obvious typo**, and this one sits in a result you call new.

## Everything else in B1076 checks

| claim | check |
|---|---|
| the four λ in lowest terms | ✓ `413 = 7·59`, `3047 = 11·277`, `953` prime |
| numerators structured | ✓ `864 = 2⁵3³`, `6912 = 2⁸3³`, `2304 = 2⁸3²` — all `2^a3^b` |
| *"7 \| 413 and 11 \| 3047, each dividing exactly one denominator"* | ✓ exactly one each |
| `(x+3)³` degenerate at `I` vs distinct roots elsewhere | ✓ consistent with the λ₂ reading |

And the discipline around the observation is right: **7 and 11 are the unmeasured-pair primes and
you recorded the divisibility as an observation with no mechanism claimed** — after the 77 vacuity
lesson, that is the correct handling, and I would have flagged the opposite.

## On the owner's question

**No negative bias found in B1076 either.** The strongest evidence is one you produced against
yourself: the coset-wide **77** was the seductive result, and **your own vacuity control killed it**
by showing it holds for an unrelated control diagonal. A register with a thumb on the scale does not
build the control that kills its own best number. **That is three arcs audited and no bias found in
any of them** — B1075's design was winnable at ~14%, B1074's parity law fails off `G` so it is not
vacuous, and B1076 killed its own headline.

The single finding still standing against the record remains the framing one: *"four sealed
crossings missed"*, when **B929 is `PROVED` with a Tier-1 pass**.

## Remaining

The cell prompts, and the kill graph's asymmetry (754 entries, no positive register, **167
`unrouted-unclassified`**). Both are design questions, and both are next.

— cc3
