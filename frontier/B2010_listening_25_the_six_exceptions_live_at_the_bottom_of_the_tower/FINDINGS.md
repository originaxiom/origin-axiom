# B2010 — Listening 25: the halving's six exceptions live at the bottom of the tower, on one group of order 18, S₃ × ℤ₃ (the three's permutations times ω's charge); every representation that sees the 3-adic layer above mod 27 pairs exactly

**Verdict: PROVED (exact: GAP character tables and kernels through sage; E3 failed as worded, with a sharper answer).** Main,
2026-11-26, in the author's /loop "continue the listening line". Data-free. Register row P-882. **0 of 19.**

## Seen first

- **B2009:** the halving derived. Its exceptions are the same six irreducibles at mod 27, 81 and 243.
- **B2006 and B2007:** G_k is S₄ with a 3-adic layer.
- **B1991:** at 2 the linear group is S₃, the three.
- **B1994:** ω's exchange labels the three by charge.
- **Swept:** `VERDICT topic-sweep /C3 x S3|S3 x Z3|Z3 x S3|inflated|six exceptions/: 1 of 1751 arcs on main match (PROVED 1); 0 register rows match (none)`.
- **The literature (standard):** inflation of characters from a quotient. S₃ × ℤ₃ has nine irreducibles: S₃'s three
  (trivial, sign, 2-dimensional) times ℤ₃'s three characters.

## The results (`verification/bottom.py` through sage, `bottom_run.txt`)

| level | \|G\| | kernel N of G_k → G₃ | irreducibles | non-trivial on N | E1: the six trivial on N | E2: every irreducible non-trivial on N has m = m′ | the six's common kernel | its quotient |
|---|---|---|---|---|---|---|---|---|
| mod 27 | 216 | 1 | 19 | 0 | yes | (vacuous) | order 12 | order 18, **C3 x S3** |
| mod 81 | 1,944 | 9 | 85 | 66 | **yes** | **yes** | order 108 | order 18, **C3 x S3** |
| mod 243 | 52,488 | 243 | 399 | 380 | **yes** | **yes** | order 2,916 | order 18, **C3 x S3** |

- **E1 holds:** at mod 81 and 243 the six exceptions are trivial on the kernel of the reduction to mod 27. They are mod 27's
  six, carried up.
- **E2 holds:** every irreducible that sees the layer above mod 27 (66 at mod 81, 380 at mod 243) has m = m′, so it pairs
  exactly.
- **E3 fails as worded:** the six live on a quotient of order 18, not 72, and the same one at every level: GAP's
  StructureDescription "C3 x S3".

## What the whole does, read in its own terms

- **The halving's only exceptions are the representations of S₃ × ℤ₃.**
  - S₃ is the permutation group of the three (B1991).
  - ℤ₃ is ω's charge (B1994), the order-3 half of the modular group's character.
  - The six exceptions include the constant, the alternation and the null mode. These are the three the neutral sector sees,
    the modes the identity leaves out.
- **Everything the 3-adic layer adds above mod 27 pairs exactly,** at every level run.
- **So at the whole's prime, the charged pair is an exact half-scale copy of the neutral member everywhere except on "the
  three with their charge", a group of order 18 that does not grow up the tower.**
- **No rate is read as physical, and nothing is compared with data.**

## What is open

- **A proof of E1 and E2 for every 3ᵏ, k ≥ 4.** It would close the halving for the whole tower, since the exceptions are fixed
  at mod 27.
- **The six as S₃ × ℤ₃'s characters by name:** which three of its nine they are, and why exactly those.
