# Exact finite probability controls

Authored before execution, October 4. These are elementary known
probability facts, not a new statistical method or physical prediction.

On a uniform finite space, event probabilities are cardinality fractions.
For independent equal-probability events of rate p the union probability
is 1 minus (1 minus p) to the power n. Independence, or a separately
proved appropriate joint inequality, is the missing contract for using
this formula as a general calibration. Correlation by itself does not
always invalidate Sidak: some classes obey the requisite inequality.

Independent control: on the 100 ordered pairs of digits, the events that
the first or second digit is zero have rate one tenth, intersection
one hundredth, and union 19 hundredths.

Counter-control: on 100000 equally likely points choose two disjoint
sets, each with 501 points. Each marginal rate is 501/100000. The actual
union rate is 1002/100000 = 0.01002, whereas the independent formula gives
0.0099948999. One is above, the other below the prose threshold 0.01.
These can be valid null p values: each test outputs its event rate on
its event and one elsewhere. Its distribution is superuniform, since
P(P_i <= t) is zero below that rate, the rate up to t less than one,
and one at t equal to one. Their dependence is not independent.
This does not establish the actual dependence of B1518's looks or alter
any particular verdict. An upper confidence bound used as the local
rate could change the numerical decision too; it is not replayed here.

For a population of five objects with one hit, two distinct uniformly
selected objects have hit probability four tenths. The independent
replacement formula gives nine twenty-fifths, which is correct for two
draws with replacement. The finite-population no-hit probability is
C(N-H,n)/C(N,n), not generally the independent expression. An actual
deterministic enumeration is not a random sample until a null sampling
law has been specified.

For arbitrary events, the union's cardinality is at most the sum of
their cardinalities. Thus min(1, sum p_i) is a valid union bound without
independence. The producer exhausts every pair of subsets of a five-point
space, including empty, identical, disjoint and full events. This bound
requires valid marginal probabilities; it cannot manufacture a missing
physical null model or repair all post-selection choices.

The source function already says independent looks. The actionable error
is the broader prose-to-application contract, not floating arithmetic.
Retain base-rate and comparable-object controls, but distinguish rarity
under a declared null from mathematical derivation and physical causation.
