# B2002 — Listening 17: at the whole's prime 3 the charged pair is an exact half-scale copy of the neutral sector — p_neutral(2x) = 2^d (x² − 9) x S(x) — with only the constant, the alternation and one null mode left out; at other primes no mode pairs; the leading mode at mod 81 lives over a sextic field containing ℚ(cos 2π/9)

**Verdict: PROVED (exact: FLINT characteristic polynomials and factorisations over ℤ; the identity checked exactly, post hoc;
PARI for the field).** Main, 2026-11-25, in the author's /loop "continue the listening line". Data-free. Register row P-882.
**0 of 19.**

## Seen first

- **B2001:** on the 3-tower the charged sectors' leading eigenvalues are half the neutral ones, numerically. The covariant
  whole is the symmetric walk on three move pairs.
- **B1997:** the 3-tower's settled rate lives over ℚ(cos 2π/9), of conductor 9.
- **B1996:** the slowest decay settles on the 3-tower.
- **Swept:** `VERDICT topic-sweep /halving|half the neutral|charged sector|characteristic polynomial of the (covariant|symmetric)|x\^6 - 60/: 13 of 1743 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 8, RETRACTED 1`. The others use "charged sector" for the Standard Model's sectors or "halving" for counts; only B2001 reads this
  halving.
- **The literature (standard):** characteristic polynomials and their factorisation over ℤ (FLINT); nfisincl and nfdisc
  (PARI).

## The results (`verification/halving.py`, `halving_run.txt`)

| level | points | C-orbits | charged polynomial a square | neutral non-top factors whose halved version divides the charged polynomial |
|---|---|---|---|---|
| mod 27, orbit of (3,3,3) | 72 | 26 | yes | all |
| mod 81 | 648 | 218 | yes | all |
| mod 5, leaf | 40 | 14 | yes | none |
| mod 7, leaf | 28 | 10 | yes | none |

- **H1 holds:** at every level the charged pair's polynomial is a perfect square over ℤ. The two charged members are exactly
  equal (B2001's G2, now exact).
- **H2 holds:** on the 3-tower the neutral sector's slowest mode reappears halved in the charged pair.
  - mod 27: x² − 28, i.e. 2√7 against √7;
  - mod 81: x⁶ − 60x⁴ + 1008x² − 4672.
- **H3 holds, in full:** on the 3-tower every non-top neutral factor has its halved version dividing the charged polynomial.
  - **Disclosed:** the run's count of "paired degree" (24 of 24, 216 of 216) did not check that the multiplicities suffice.
    The exact accounting is the post hoc identity below.
- **H4 holds:** at mod 5 and 7 no neutral factor pairs.
- **H5 holds** (PARI): the mod-81 slowest mode's field has degree 6, contains ℚ(cos 2π/9), and has discriminant
  2⁶ · 3⁸ · 73.

## Post hoc, labelled (`identity_posthoc.py`, `identity_posthoc_run.txt`; written after the run was read)

Let S(x) be one charged sector's characteristic polynomial (the charged pair's is S²) and d the neutral degree. Then, exactly
in FLINT:

**p_neutral(2x) = 2^d · (x − 3)(x + 3) · x · S(x)**

- It holds at mod 27 (d = 26) and mod 81 (d = 218).
- It fails at mod 5 and mod 7.

So on the 3-tower each charged sector's spectrum is exactly half the neutral sector's, with three modes left out: the
constant (6), the alternation (−6) and one null mode (0). The neutral sector is three dimensions larger, one for each of the
three points of the orbit that ω's exchange fixes.

## What the whole does, read in its own terms

- **At its own prime 3, the whole remembers ω's charged pair as an exact half-scale copy of how it remembers the neutral
  member.**
  - Every mode of the neutral sector except the constant, the alternation and one null mode reappears in each charged member
    at exactly half the strength.
  - The pair is locked, and the copy is exact.
  - At the other primes run (5 and 7) the two sectors share no mode.
- **The whole's prime ties the 1 + 2 exactly.** The 1 + 2 split, local at (3,3,3) (B2000) and global on the leaf (B2001), is
  at the prime 3 an exact scaling by ½ between the neutral member and the charged pair.
- **The ninth roots run through this sector too:** the leading mode's field at mod 81 contains ℚ(cos 2π/9), as B1997's rate
  did.
- **No rate or ratio is read as physical, and nothing is compared with data.**

## What is open

- **Why the identity holds at the whole's prime:** an intertwining map between the neutral and charged sectors on the 3-tower,
  presumably through the three C-fixed points. Its proof for every level 3ᵏ.
- **Whether it holds at mod 243 and beyond:** the dimension count predicts it.
- **The sextic field's 73:** what, in the 3-tower, the prime 73 in its discriminant comes from.
