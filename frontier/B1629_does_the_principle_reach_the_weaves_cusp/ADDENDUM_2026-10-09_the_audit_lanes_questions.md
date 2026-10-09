# B1629 — ADDENDUM (2026-10-09, S112): the audit lane's two questions (its relay "negative-audit intake", @ 4fcee76ab)

**Sharpened; the verdict and every computed number stand.**

**1. The finite fraction is not the limit.** §2's P4 row says the fraction of letters in runs of length ≥ k "is
(k + 1)/2^k … the same at every n = 10 … 18". That is the limit, not the saved values. (k + 1)/2^k is the size-biased run
law of a fair coin: on a bi-infinite fair sequence the run through a given letter has length j with probability j/2^{j+1},
so the probability that it is at least k is Σ_{j≥k} j/2^{j+1} = (k + 1)/2^k. The saved values over primitive cyclic threads
(`post_seal_cusp.json`) differ from it at finite n. At n = 10 they are 0.751515, 0.501010, 0.313131, 0.191919, 0.111111,
0.062626 and 0.034343 for k = 2 … 8, against 0.75, 0.5, 0.3125, 0.1875, 0.109375, 0.0625 and 0.035156. The largest
relative deviation in the table is 2.4% (k = 5, n = 10), and at n = 16 the k ≤ 7 entries agree to six places. **The
corrected sentence:** the fraction tends to (k + 1)/2^k and is within 2.4% of it at every n = 10 … 18 and k = 2 … 8; it decays
geometrically in k.

**2. "Therefore not dynamical": the implication, with its quantifier.** No theorem was invoked, and the sentence claimed
more than was computed. What was computed:
- (a) the tick's closed geodesic has height √5/2 and the clock's word stays below 2.3, so neither forced datum enters
  the horoball of height > 2.3;
- (b) under the uniform measure on threads, the mass at depth ≥ k tends to (k + 1)/2^k, so for every ε > 0 there is a
  depth k(ε) whose horoball the measure charges with weight < ε in the limit. In other words, there is no atom at the cusp.

So the precise statement is: **no datum the principle forces (the tick, the clock) and no expectation under the weave's
uniform measure on threads of an observable supported in ever-deeper horoballs produces a non-zero weight at the
cusp.** Other measures (non-uniform, or concentrating on long runs) and other dynamics are not excluded. "Not dynamical"
is read in that scope, and the end datum, if forced, is a boundary datum. The owner's tagging of the unit as a postulate
(GENESIS v1.39) does not rest on this sentence.
