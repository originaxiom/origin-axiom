# Exact finite statistic and scope of the inference

Authored before the run. A self-contained combinatorial argument, not
outside acceptance or a new physical model.

Let n>1. A_n is the number of rooted aperiodic binary words of length n:
A_n = sum_{d|n} mu(d) 2^(n/d). Each primitive necklace has exactly n
rotations, so uniform primitive necklaces with uniform letters and uniform
rooted aperiodic words with a distinguished site give the same statistic.

For an m-periodic binary sequence chosen from all 2^m rooted words, let
E_m(k) count those in which the distinguished site lies in a run of at
least k equal letters in the infinite periodic sequence. Constant words
are assigned an infinite run, as required when removing their contribution
from the primitive population. If m<=k, only the two constant words qualify.
If m>k, count the complementary finite runs r=1..k-1. There are r possible
positions of the site in a run of length r. Each position has probability
2^(-r-1), including the two choices of letter. Here r<=m-2, so the two
opposite-letter endpoints are distinct sites. Therefore

E_m(k) = 2                            if m<=k,
E_m(k) = 2^(m-k) (k+1)               if m>k.

The marked-site event is unchanged by repeating a nonconstant word.
Mobius inversion on the minimal period yields the exact primitive tail

p_n(k) = [sum_{d|n} mu(d) E_(n/d)(k)] / A_n.

For n=10,k=2 the proposed exact fraction is 744/990 = 124/165,
not 3/4. Its numerical value rounds to the source table's 0.751515.
This prediction must be tested by a different enumeration before being
reported as verified. At k=n the numerator vanishes, as it must.

For 1<=k<n, the unconditioned circular-word probability is (k+1)/2^k.
Let q_n be the probability that such a word is not primitive. Conditioning
on primitiveness changes any event's probability by at most q_n, since
p = (1-q_n)p_primitive + q_n p_nonprimitive. A union bound gives
q_n <= sum_{m|n,m<n} 2^(m-n) <= n*2^(-n/2), which tends to zero.
Thus for each fixed k, p_n(k) tends to (k+1)/2^k. The limit, followed by
k -> infinity, has no mass at an infinite run. It is not exact at every
finite n. No uniformity in jointly varying n,k is silently assumed.

## What a zero atom does not prove

In an infinite fair Bernoulli binary sequence, disjoint length-k blocks
are independent. The probability that none of N such blocks is entirely L
is (1-2^(-k))^N, tending to zero. Applying the argument to arbitrarily late
tails and the countable set of positive k shows arbitrarily long runs
occur almost surely, despite the vanishing occupancy tail above. This
is an example inside the same limiting symbolic measure, not a generated
physical mechanism and not a claim that the selected tick is unbounded.

The corrected code counts letters, not arclength. As a direct check on
identifying the two clocks, words LLLR and LLRR both have four letters,
but traces 5 and 6 respectively. Hyperbolic translation lengths are
2 arcosh(tr/2), hence different. This does not refute a correctly derived
suspension measure; it says that conversion must be exhibited.

Neither a bounded selected periodic orbit nor a zero cusp atom proves
that a field equation, boundary variation, topology or quantum response
cannot fix end data. Such a no-go needs its actual action, allowed class
and a map connecting end data to the measured dynamics. Conversely these
observations do not show that any such action or mechanism is derived.
This audit does not decide FK10, W47's classification or the physical
chirality of the silver model.

The finite height check retains the author's definition: maximum over
cyclic rotations of (tr^2-4)/(4 min(|b|,|c|)^2). A separate theorem is
needed to identify that finite definition with a full modular height or
extend a finite census to every length. No refutation of the classical
golden-geodesic minimum is asserted here.
