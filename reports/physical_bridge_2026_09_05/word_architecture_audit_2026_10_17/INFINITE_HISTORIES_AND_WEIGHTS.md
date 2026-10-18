# Infinite histories, limiting directions and statistical weights

October 18, 2026. Unreviewed analytical specification. These arguments
are outside the existing unsealed seventeen-control package; no new
scientific producer has been executed and no canonical ruling is changed.

The positive record grammar describes a continuum of limiting directions,
not only the golden return. That positive has an exact scope: it concerns
right-extended products and their nested image cones. Chronological
updates of one state need not converge, even with the same positive
generators. Neither construction alone supplies a probability over its
histories. A fixed Sturmian language does, however, have constrained
shift-invariant statistics; that existing positive must not be lost.

## Finite legality and infinite acceptance

For the partial-action specification in [TYPED_ARCHITECTURE.md](TYPED_ARCHITECTURE.md),
fix an initial state x. The maximal infinite-path space is

    Omega_max(x) = {u1 u2 ... : every finite prefix is legal from x}.

Equivalently it is the inverse limit of the sets of legal length-n paths,
with truncation as the bonding maps. This construction retains the actual
updates and domains; it does not add a measure or assert that the state
sequence has a limit.

An additional infinite acceptance rule must be stated separately. For
example, on the total positive alphabet {L,R}, all of the following have
the same set of finite prefixes, namely {L,R}*:

- all infinite sequences;
- sequences in which L and R each occur infinitely often;
- sequences eventually repeating LR.

Every finite prefix extends into each set. The second is the relevant
nondegeneracy condition for the positive Sturmian description below;
the third is only a comparison, not a proposed programme rule. Finite
legality alone cannot distinguish them. The second set is not closed in
the prefix topology: L^n followed by RLRL... converges to LLL... . Thus
its global acceptance condition cannot be replaced by forbidding finite
prefixes. This does not prevent deriving that condition from an explicitly
specified infinite-output requirement.

## The entire positive limiting-direction family

Use column vectors and the admitted record matrices

    L = [[1,1],[0,1]],       R = [[1,0],[1,1]].

For an infinite directive M1,M2,... in {L,R}, set

    W_0 = I,       W_n = M1 M2 ... Mn,       W_(n+1) = W_n M_(n+1).

This is right extension of a description. Function composition acts
rightmost first. It is not the chronological update x_(n+1)=M_(n+1)x_n.

Let u,v be the columns of W_n and let s_u=u1+u2, s_v=v1+v2. Normalize a
nonzero nonnegative vector z by beta(z)=z2/(z1+z2). The projectivized
image of the nonnegative cone is the closed interval

    I_n = [beta(u), beta(v)],       length(I_n) = 1/(s_u s_v).

The length follows from det(u,v)=1. Right multiplication by L replaces
(u,v) by (u,u+v); multiplication by R replaces it by (u+v,v). The child
intervals partition the parent at beta(u+v), with just that endpoint in
common. Hence the intervals along every infinite directive are nested.

Initially s_u=s_v=1. Each update increases s_u+s_v by at least one, while
both sums remain positive integers. Therefore

    s_u+s_v >= n+2,       s_u s_v >= s_u+s_v-1 >= n+1,
    length(I_n) <= 1/(n+1).

Consequently every positive infinite directive determines exactly one
limiting normalized direction alpha in [0,1]. This proves convergence
of the nested directions, not of W_n as a finite matrix: the sum of its
entries grows without bound. No physical scale or time unit occurs here.

The following coverage statement is also exact:

    {directives using L and R infinitely often}
              <-> {irrational alpha in (0,1)}.

To prove it, suppose a reduced rational p/q lies strictly inside I_n.
The integer vector (q-p,p) has a unique expansion m u+k v because W_n
is unimodular. Interior membership forces positive integers m,k, so
q=m s_u+k s_v >= s_u+s_v >= n+2. A fixed rational cannot stay interior
at every depth. Once it is an endpoint, all subsequent choices must keep
that column, requiring an eventually constant directive. Conversely,
an eventually constant directive converges to its fixed rational column.

For any irrational alpha, repeatedly choose the unique child interval
containing it; it never equals their rational splitting point. The
shrinking-interval argument gives its limit, and the preceding argument
forces both letters to recur. Uniqueness follows from the disjoint child
interiors. This is the elementary continued-fraction/Farey construction,
not a new uniqueness theorem discovered by the programme.

The golden control (LR)(LR)... gives alpha=(3-sqrt(5))/2: the period
matrix sends (1-alpha,alpha) to (2-alpha,1), so invariance requires
alpha=1/(3-alpha). But the construction also includes the cubic slope
cube_root(2)-1 from [AUDIT.md](AUDIT.md), with no stationary-return
requirement. Failure of that cubic slope to have a nontrivial stationary
unimodular return is not failure to have a limiting description.

## A limit direction is not a complete pointed word

The literature already supplies the relevant symbolic completion.
Berthe and Delecroix, [Beyond substitutive dynamical systems](https://arxiv.org/abs/1309.3960),
Examples 3.2, 3.6 and 3.8, distinguish the directive, its language and its
pointed outputs. Their first pair is (L,Rbar) in our word conventions.
With both directives recurring it generates the Sturmian languages;
obtaining every pointed word also requires the stated shift or alternative
lift data and their admissibility conditions. Their sections 3.3 and 3.4
distinguish the two shifts and relate directions to incidence cones.

The [lift-family note](LIFT_FAMILY_AND_REGISTER.md) gives the finite
common-frame transport between (L,R) and (L,Rbar). That finite identity
alone is not a proof that an arbitrary proposed infinite based expression
converges. A pointed-word limit must retain its seed, shifts and topology.
The positive cone proof above neither adds those choices nor erases them.

## Chronological state evolution has a different limit question

Now hold the interpretation fixed as x_(n+1)=M_(n+1)x_n on positive
vectors x=(a,b). Then x_n=M_n ... M_1 x_0, not W_n x_0. Direct calculation
gives

    beta(L^k x) = b/(a+(k+1)b) <= 1/(k+1),
    beta(R^k x) = (ka+b)/((k+1)a+b) >= k/(k+1).

For the chronological sequence of blocks

    L R L^2 R^2 L^3 R^3 ...

the states after L^k blocks approach beta=0, whereas those after R^k
blocks approach beta=1. Both symbols recur infinitely often, but the
state directions do not converge. This does not contradict the
right-extension theorem: it is a different ordered sequence of products.
Reversing a finite product can translate conventions; reversing longer
and longer prefixes does not supply a single reversed infinite directive.

With inverse moves admitted there are also elementary right-product
controls. Put S=L R^-1 L=[[0,1],[-1,0]]. Repeating the three-letter block
S has no adjacent inverse cancellations, but its products at block ends
cycle: S^2=-I and S^4=I. On projective directions the axes alternate.
There is no universal boundary limit for every signed history. At the
based-word level the same fourth power is the retained boundary twist
from B1634/R79, not the identity; do not discard that register.

These controls do not refute almost-sure convergence under a specified
random-walk law. B1663 explicitly uses right-multiplied sampled steps;
its convention agrees with its stated experiment. Nor do these controls
exclude evolution without a limiting state, or a physically justified
restriction on which histories occur.

## What symmetry does and does not determine statistically

Here is a direct comparison under stated weak statistical requirements,
not a claim that every possible foundational requirement has been tested.
For any 0<q<1, give the two positive labels the stationary Markov law

    pi(L)=pi(R)=1/2,
    P_q = [[q,1-q],[1-q,q]].

For a nonempty cylinder [u1...un] its probability is

    mu_q([u1...un]) = (1/2) product_(j=1)^(n-1) P_q(uj,u_(j+1)).

Row sums give consistency under extension; the uniform stationary vector
gives shift invariance; the symmetric matrix gives reversal invariance.
Exchanging L and R preserves the law. Every finite cylinder has positive
weight. Both letters recur almost surely, since the probability of an
eventually constant tail is zero (a fixed constant tail has probability
bounded by q^m for every m, and there are countably many starting times).

Nevertheless mu_q([LL])=q/2. Thus equal one-step probabilities, exchange
symmetry, stationarity, reversal symmetry and full support do not select
one process. The irrational-direction bijection transports these to
different measures on the same slope family. For example the interval
0<alpha<1/3 corresponds to the LL prefix, with endpoints of zero weight;
its weight is q/2. This is a difference between measures, not a numerical
claim about a particle parameter.

The four signed labels admit the same control with uniform pi=1/4,
P_q(i,i)=q and P_q(i,j)=(1-q)/3 for i!=j. It is invariant under every
permutation of the labels, including the inverse and exchange relabelings,
and under reversal. But mu_q([LL])=q/4. Independent uniform increments
are the particular q=1/4 law, not the only symmetric stationary process.
No assertion about these correlated laws' exit distributions is made.

There is a stronger possible requirement: **conditional on every past,
each next allowed label has the same probability**. For these full
alphabets the chain rule then gives the uniform independent law. If that
condition is adopted or derived, the ambiguity just exhibited is removed.
It must not be silently substituted for the weaker statement that label
names have no preferred status. The exact next foundational question is
whether that history-independent conditional rule follows from PF1 and
the registering relation, or is a further premise.

Preserve a different positive. Once an irrational Sturmian slope alpha
and the output shift are fixed, the shift-invariant probability on that
language is unique. In the rotation coding its block weights are the
lengths of the intervals of phases producing those blocks. This is an
existing result in the cited paper's sections 2 and 3, not a measure over
different slopes. Equidistribution of the irrational rotation fixes the
frequencies for each phase; it does not choose alpha. These internal
statistics are not automatically a physical sampling law or Born rule.

The frequency mechanism can be checked without a numerical experiment.
For each nonzero integer k, the normalized sum of
exp(2 pi i k (beta+j alpha)), j=0,...,N-1, tends to zero by the finite
geometric-series formula; its denominator is nonzero because alpha is
irrational. Trigonometric approximation then gives the visit frequency
of any interval as its length. Each finite output block corresponds to
a finite union of phase intervals. Their endpoints have zero length and
an irrational orbit hits each at most once, so endpoint conventions do
not change these frequencies. Those block frequencies determine the
shift-invariant measure on the fixed Sturmian language. No part of this
argument places probabilities on different values of alpha.

## Consequences for the current programme

The calculation should carry a typed history and its register, then apply
the appropriate observation:

| Requested output | What this analysis supplies | What is not obtained by that step |
|---|---|---|
| Positive description direction | Complete irrational-family coverage and an explicit interval bound | One favoured slope or every pointed output |
| State evolution | Exact finite action, with a nonconvergent positive control | A universal asymptotic state or a physical clock |
| Signed histories | The admitted finite action with its based lift retained | A boundary limit for every legal path |
| Statistics | Internal fixed-language frequencies; explicit symmetric alternative history laws | A uniquely derived weighting across histories |
| Physical joining | Compatibility and transport already specified in JOINING_LAW_ANALYSIS | Selection of interfaces, fields, action or fermion domain |

B1663's producer uses fresh pseudo-random draws against fixed thresholds
at each step; its results are conditional on that independent-increment
model. Its October 17 addendum already limits the post-seal digit check
to marginal frequencies, not digit independence or equality of exit laws.
That correction must travel with any reuse. None of the analytic controls
above recomputes its numerical results or negates its scoped experiment.

This closes a drafting gap in the infinite-history specification. It
does not settle GM3's intended meaning on every branch, pay a complete
physical-input row, or complete the goal's verification stage. The
existing joined-action and interaction positives remain the physical
recovery cases; a different history space is not permission to borrow
their fields or spectra without the required maps.

## Source and verification record

The repository pin is main 2e5716bd9bea013d69f3cd733f083b61a6f59dbd.
B1663 FINDINGS, PREREGISTRATION, the full main producer and its post-seal
digit producer were read, not executed. The already-banked query was
`Sturmian directive projective limit`; its broad matches are not evidence
of absence. Targeted source searches included S-adic, directive sequence,
Stern-Brocot, continued fraction, Bernoulli and Markov. This is not a new
whole-repository absence claim.

The cited arXiv v2, accessed October 18, was read at the relevant symbolic,
S-adic and frequency passages, particularly Examples 3.2/3.6/3.8 and the
distinction between output and directive shifts. No new full-paper read
or visual-layout inspection is claimed. The displayed cone, chronology,
path-acceptance and Markov arguments are explicit analytical controls,
awaiting non-authoring review and appropriately admitted executable
checks. The previous seventeen-test design is not silently expanded.
