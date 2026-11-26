# B2010 — Listening card 25: do the halving's six exceptions live at the bottom of the tower — inflated from mod 27 at every higher level, carried by one small quotient?

Written 2026-11-26, before any run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why

B2009 derived the halving. The charged spectrum is half the neutral one on every irreducible representation where the
stabiliser sees the trivial character and ρ's restriction equally. At mod 27, 81 and 243 the exceptions are the same six, of
degree at most 2.

For the halving to hold up the whole tower, those six must not change from rung to rung. The natural reason would be that they
are representations of the bottom level, mod 27, carried up unchanged. In that case every representation that sees the 3-adic
layer above mod 27 pairs perfectly.

## The checks (GAP through sage)

- **E1:** at mod 81 and 243, let N be the kernel of the reduction G_k → G₃ (the action on the blocks of reduction mod 27).
  Is each of the six exceptional irreducibles trivial on N?
- **E2:** at mod 81 and 243, does every irreducible that is non-trivial on N have m = m′? (This is E1 restated over the whole
  table, as a second, independent count.)
- **E3:** at mod 27, the intersection of the six exceptional characters' kernels. Its order, the quotient's order, and the
  quotient's StructureDescription.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| E1 | the six exceptions are trivial on N at mod 81 and 243 | 0.8 |
| E2 | every irreducible non-trivial on N has m = m′ at mod 81 and 243 | 0.8 |
| E3 | the six live on a quotient of G₃ of order 72 | 0.35 |

## What it means

- **If E1 and E2 hold:** the halving's only exceptions are fixed at the bottom of the tower. The halving's exactness at every
  higher rung then reduces to the bottom level and to the stabiliser seeing the layer evenly.
- **E3 names the small group** that carries the constant, the alternation and the null mode.
- **Nothing is compared with data.**
