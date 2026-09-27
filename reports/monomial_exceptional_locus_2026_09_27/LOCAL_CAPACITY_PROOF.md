# Nearby full-parent capacity at the exceptional points

Post-result follow-through, separately sealed before its verification run.
The initial exceptional-locus result is 2c6d66a3. This is an authored local
proof with exact cochain checks, not independent peer review.

## Question and hypothesis ledger

At t^5=1 both monomial families have a two-dimensional meridian-relative
off-monomial tangent. Does that justify nonlinear continuation toward
ordinary index three in the actual E5 coefficient?

Consider ALL sufficiently nearby rank-five SL5 representations of the
certified M2 group, not just monomial ones, keeping the M2 meridian in
the conjugacy class of T=(012) with two fixed coordinates. Restrict to
the actual M6 cover. Require H0(M6;E)=H0(M6;E*)=0, as for an irreducible
upstairs background. This explicitly excludes unbalanced nonsplit cases;
it is not silently imposed on the existing nonsplit positive examples.

Let b=h0(boundary;E) and b*=h0(boundary;E*). At our exceptional points
the preferred longitude fixes three directions. Its rank-two nonzero
minor persists nearby, so b,b*<=3. Because the M2 meridian cubes to I,
the M6 peripheral pair is (I,L); consequently b=b*, even when L is
nonsemisimple, since L-I and L^-transpose-I have the same rank.
Longitude may vary: it is NOT being fixed in this argument.

## The relative cohomology bound

The direct finite-dimensional mapping-cone cochain complex of
(M6,boundary M6) is built from the verified presentation and peripheral
restriction map. Its H1 dimension is upper semicontinuous in the
representation: it is kernel dimension minus rank of the preceding
differential; both negatives of ranks are upper semicontinuous.
Here the preceding cone differential includes an identity block and
therefore always has rank equal to the coefficient dimension.

The earlier tuples predict h1(M6,boundary;E)=3 and the same for E* at
EVERY fifth root, for both seeds. The new producer verifies those
dimensions from the cone matrix itself and compares the exact sequence

    h1(M,boundary;V) = n(V) + h0(boundary;V) - h0(M;V).

After that verification, upper semicontinuity gives h1_relative(E)<=3
and h1_relative(E*)<=3 in a neighborhood of each exceptional point.
Under the stated zero-global-invariant hypothesis,

    0 <= n(E), n(E*) <= 3-b,
    hence |I(E)| <= 3-b.

The previously verified boundary identity independently gives
|I(E)|<=b under these same global-invariant hypotheses. Combining them,

    |I(E)| <= min(b,3-b) <= 1,  for integer b in {0,1,2,3}.

In particular, retaining boundary capacity three forces BOTH interior
dimensions to vanish nearby. Losing some boundary capacity cannot
produce index three either.

## What this does and does not close

If the direct cone check confirms its inputs, these exceptional tangents
cannot lead IMMEDIATELY to a nearby zero-global-invariant, fixed-meridian
E5 background of index three, even outside the monomial ansatz and with
longitude free. No nonlinear-integrability claim is needed to obtain
that scoped bound, and the two-dimensional tangent is not erased.

This does not classify distant points on a continued branch, give a
numerical neighborhood radius, exclude unbalanced nonsplit backgrounds,
allow meridian-class changes for free, or constrain a different physical
operator/source/domain. Nor does it prove that the entire monomial
family has zero interior index at every nonexceptional parameter.
It tells us why chasing these particular small-neighborhood tangent
directions is not the next direct route to the declared joint target.

Preserve first-order positive, finite controls, and all prior partial
positive indices. Physical admission and the full TOE mission remain open.
