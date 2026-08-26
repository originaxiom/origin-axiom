# B8129 — n2 no breakdown

**Arc dated:** 2026-08-25 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification claimed in this arc.

> **RECONSTRUCTED 2026-08-26 from this arc's own banked record** (`arc_verdict.json`
> and `results.json`). **This seat stopped writing `FINDINGS.md` at B8110 and the
> omission ran unbroken through B8134 — sixteen arcs.** It went uncaught because the
> lock that detects it lives in a suite too slow to finish inside a session. **This
> document is faithful to the banked record but is NOT contemporaneous, and is marked
> so rather than backdated.**

## Verdict

**PROVED**

THE n=2 FACTOR SHOWS NO BREAKDOWN AT THE ABSCISSA, ON AN INSTRUMENT PROVED ABLE TO SEE ONE.
B8113 left the n=2 residue as possibly non-existent. Approaching the abscissa from above, where
R(s,sigma_2) converges absolutely, |R| is smooth and monotone through s=2 (1.1075 at 2.6 to
1.1936 at 2.0) with no pole, no discontinuity, and a cutoff spread growing gently from 1.03e-4
to 1.71e-3. THE BITE CONTROL IS WHAT MAKES THAT MEAN ANYTHING: below the abscissa, where
divergence is certain, the spread grows sharply -- 1.6x at s=1.9, 2.5x at 1.8, 6.7x at 1.6,
21.8x at 1.4 -- so the instrument discriminates and a tame spread at s=2 is informative. The
reading: the abscissa of ABSOLUTE convergence is not a barrier to CONDITIONAL convergence here;
the phases cancel. EXISTENCE IS NOT PROVED -- three cutoffs, cutoff-to-infinity untested -- and
the residue stays one of B8113's three. But it moves from 'may not exist' to 'no evidence of
breakdown', which is a different thing to hand a referee. Numerical, over the m004 length
spectrum to cutoff 5.5, three cutoffs, seven values of s. Does not prove convergence and does
not compute the analytic continuation. Gate 5 untouched.

## What the arc recorded

### `verdict`

THE n=2 FACTOR SHOWS NO BREAKDOWN AT THE ABSCISSA, ON AN INSTRUMENT PROVED ABLE TO SEE ONE.
B8113 left the n=2 residue as possibly non-existent. Approaching the abscissa from above, where
R(s,sigma_2) converges absolutely, |R| is smooth and monotone through s=2 (1.1075 at 2.6 to
1.1936 at 2.0) with no pole, no discontinuity, and a cutoff spread growing gently from 1.03e-4
to 1.71e-3. THE BITE CONTROL IS WHAT MAKES THAT MEAN ANYTHING: below the abscissa, where
divergence is certain, the spread grows sharply -- 1.6x at s=1.9, 2.5x at 1.8, 6.7x at 1.6,
21.8x at 1.4 -- so the instrument discriminates and a tame spread at s=2 is informative. The
reading: the abscissa of ABSOLUTE convergence is not a barrier to CONDITIONAL convergence here;
the phases cancel. EXISTENCE IS NOT PROVED -- three cutoffs, cutoff-to-infinity untested -- and
the residue stays one of B8113's three. But it moves from 'may not exist' to 'no evidence of
breakdown', which is a different thing to hand a referee.

### `scope`

Numerical, over the m004 length spectrum to cutoff 5.5, three cutoffs, seven values of s. Does
not prove convergence and does not compute the analytic continuation. Gate 5 untouched.

### `what_this_does_NOT_establish`

EXISTENCE IS NOT PROVED. Three cutoffs, and the cutoff -> infinity limit is untested; a spread
that is small at 5.5 can still fail to converge. What is established is the ABSENCE of a
breakdown signature at the abscissa, on an instrument shown able to detect one 22x over.

### `status_change`

B8113's residue moves from 'may not exist' to 'no evidence of breakdown; existence unproved'. It
is still one of the three residues; it is no longer the alarming one.

### `method`

R(s,sigma_2) = prod_gamma (1 - e^{2 i theta} e^{-s l}) converges ABSOLUTELY for s > 2, so
approach the abscissa from above and watch the cutoff-dependence. Three cutoffs (4.5, 5.0, 5.5)
over the m004 length spectrum.

### `bite_control`

THE CONTROL THAT MAKES THE READING MEAN ANYTHING: go BELOW the abscissa, where divergence is
certain, and check the instrument can see it. It can -- the spread grows monotonically and
sharply: s=1.90 1.6x, s=1.80 2.5x, s=1.60 6.7x, s=1.40 21.8x the s=2 value. So a tame spread at
s=2 is informative rather than vacuous.

### `finding`

|R(s,sigma_2)| is SMOOTH AND MONOTONE THROUGH s=2 -- 1.1075 at s=2.6 rising to 1.1936 at s=2.0
-- with NO pole, NO discontinuity, and a cutoff spread that grows gently (1.0e-4 to 1.7e-3)
rather than diverging. There is NO SIGNATURE OF BREAKDOWN AT THE ABSCISSA. The phases e^{2 i
theta} cancel enough that the product behaves like a convergent one at s=2 and degrades only
gradually below it.

### `question`

B8113 left the n=2 factor as 'at best conditionally convergent; whether the limit exists and is
order-independent is OPEN'. This attacks it directly.

## Depends on

`B8113`, `B8112`, `B8100`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
