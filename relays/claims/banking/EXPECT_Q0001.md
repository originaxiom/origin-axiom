# EXPECT_Q0001 — sm2 (fam1-v1-unset-05), committed before any run

Card: Q0001, `relays/claims/CLAIM_2026-11-27_B2011_main_trial.md` on main at 0fd0a70f43722056a17992667016a31b34cfb1d3 (the
queue record's commit). Written from the card and its queue record alone, before reading or running the card's script and
before running any code of mine. Not read: the peer's note, the other banking seat's branch, B2011's files.

## What I will recompute, with my own code (python-flint for exact integer polynomials, the standard library)
1. The orbit of (3,3,3) mod 135 and mod 27 under L, R and their inverses; that reduction mod 27 maps the first onto the
   second; that C maps the orbit to itself (needed for the sectors); C's fixed points in the orbit (expected three).
2. rho: that L -> -w^2, R -> -w is well defined on the group the moves generate on the mod-27 orbit (the premise B2005,
   checked rather than cited, K4), so that it factors through G_135 by the reduction.
3. W, the six-move sum, on the C-invariant functions (p_neutral, degree d) and on the q = 1 charged span of the size-3
   C-orbits (S, degree 959 if the card is right); exact characteristic polynomials; the degree of
   gcd(p_neutral(2x)/2^d, S(x)); the unpaired part of S, its factorisation over Q; and whether p_neutral(2x)/2^d equals
   (x - 3)(x + 3) x S(x) (it should not, if 10 roots go unpaired).
4. Two-sided controls (K8): the same code at a modulus where the halving is said to hold (27, or 45 if the orbit allows),
   where I expect gcd degree = deg S, so that my instrument can see the halving hold and fail.

## Expectation
- I have no independent prior on the number 10. I expect the structural statements (orbit reduces onto mod 27; three C
  fixed points; rho through G_27) to hold, and the count to be the card's, 959 charged with 10 unpaired; if my count
  differs, REFUSE.
- Scope (K9): the card's effect is to condition B2003's and B2005's correlations to "tables of the levels run, not laws".
  One modulus where the halving fails supports "not a law at every level"; it does not say where else it fails. I will
  hold the effect to that reading.
- The card says the 10 are the roots of "the four factors named", but does not name them on the card. If I cannot tell
  which four factors are meant, I check only that the unpaired part has degree 10, report its factorisation, and say that
  this part of the claim is not decidable from the card (RETURN on that point alone would be too strong if the rest holds;
  I will say how it bears on the verdict).
- Heavy: the charged sector of degree about 960 needs exact characteristic polynomials of integer matrices of that size;
  with python-flint I expect minutes, not hours. If it runs past the runner's limit, I mark it heavy.
