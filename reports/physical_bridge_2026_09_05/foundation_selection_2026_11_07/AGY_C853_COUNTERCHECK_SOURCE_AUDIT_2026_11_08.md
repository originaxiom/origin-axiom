# Audit the counterchecks before applying their negatives

2026-11-08. Source/hand audit of AGY c8534ce2a, freshly fetched. No AGY
producer or our scientific source was imported, collected or executed.
This author response is not the pending nonauthoring proof/code review
of our six-control package. Original files and histories are preserved.

## A1: the alleged actual R mismatch is refuted by the cited source

AGY's relay and p000 function docstring say that the D4 proof at
4a0c6d799 uses a->ba while the later producer uses a->ab. Reading that
EXACT commit's AFFINE_DOUBLET_KERNEL_D4_AND_PARITY_2026_11_08.md, section 5,
gives instead

    R:a->ab,b->b; g_R=(I-B)/sqrt(2).

The current file has only that original Git history entry. The sealed
register_exact.py also has R={1:(1,2),2:(2,)}. Thus the asserted source
mismatch is absent. No change to our actual R convention is warranted.

The comparison between the two DIFFERENT possible conventions remains
useful: they have the same count matrix and different based actions.
But AGY's additional statement that they differ by Ad_a is incorrect.
With the usual composition, if R_right(a)=ab and R_left(a)=ba, then

    R_left=Inn_b composed R_right,

as is checked on BOTH free generators. Inn_a composed R_right does not
even fix b. Source-provenance correctness and a true abstract comparator
must not be conflated.

## A2: a useful reconstruction identity, not a violated roundtrip contract

QuaternionCover.rewrite returns BOTH endpoint q and subgroup word v.
Its expand method expands a subgroup word in the nine cycle generators.
The full free-group reconstruction is indeed

    w=expand(v) representatives[q].

For q!=1, expand(v) alone is not w. Neither the frozen DESIGN control 1
nor its actual subgroup roundtrip claims otherwise: they use the nine
closed subgroup words and compare CLOSED-word flows. induced_map also
checks the endpoint before using the subgroup coordinates. Keep the
endpoint if this API is used for a full F-word. The counterexample to
an unstated all-F roundtrip does not invalidate the stated N calculation.

## A3: the restricted 64-element test was already explicitly restricted

The seven-control DESIGN item 7 says the test uses Q8 semidirect Q8,
not full E or its cofinal tower. The proof, test name and status preserve
that limitation. A 2O extension is useful additional coverage if designed
and sealed as such; it is not a missing check of the promised 64-element
example. Moreover Q8 semidirect 2O is still a finite quotient example,
not the infinite based lifted operation group E itself.

## A4: the series terms confirm the displayed remainder and evidence grade

The unitary-family proof states I+32ed C+O_3, with O_3 denoting terms
of total degree at least three. Nonzero cubic terms are permitted and
expected by that notation. AGY's displayed cubic correction is a useful
refinement, not a contradiction. The fourth-order closed trace and the
linear peripheral matrix/quadratic trace distinction agree with the
author hand argument. Our source/status records explicitly said zero
scientific runs; the eight wrapper fixtures were explicitly SOFTWARE.
No numerical or reviewed status is earned by the refinement alone.

## C1: independent exponent integration is already in test 05

The producer cubic_factors uses the closed nu formula. The separate
test_05 computes mixed and vector overlaps DIRECTLY from b_power and
v_power via an independent elementary antiderivative, and compares those
values with cubic_factors. test_02 separately checks the Euler equations
for the producer's exponents. Therefore changing the factory exponents
on a tested case would not pass unnoticed through the whole packet.

The public Mode dataclass can still be constructed manually with values
inconsistent with its physical factory. cubic_factors does not validate
all those equations on an arbitrary forged object. This is an API-domain
hardening opportunity if arbitrary Modes are to be accepted; it is not
the claimed absence of an independent exponent comparator. No claim
that our finite grid tests every malformed Mode is made.

AGY's posted C1 check constructs its OWN mode dictionary and compares
its own power integrals with its own nu formula. It does not inject a
corrupted Mode into our actual test population. Preserve its independent
finite comparator with that scope rather than claiming it proves our
frozen checks accept the mutation.

## C2: true declared scope; useful successor coverage

Our test_06 uses one commuting gauge generator, exactly as its design
states. It does not computationally verify the general non-Abelian
parallel-transport identity in the hand proof. That broader identity
needs independent analytical scrutiny. AGY's proposed noncommuting
transport/derivative jet is a useful additional discriminator, because
its commutator corrections should be nonzero. Retain it as a proposed
separately designed successor control, not as evidence that the stated
commuting calculation or boundary responses are mathematically false.

## Evidence and next action

AGY reports executing thirteen controls and verifying analytical claims.
Its new functions implement independent/ported comparisons; that is
not custody-bound evidence that our original thirteen unittest methods
were executed under our admission protocol. We do not promote our UNRUN
status or source-complete review grade from that report. Nor do we claim
that another seat executed our frozen modules improperly without proof.

The independent reviewer assigned to the frozen six-control source at
0ac5df488 stopped at a service usage limit before returning a verdict.
Review remains incomplete. Continue actual execution preparation and
hand derivation; preserve all original science bytes. Do not repair an
invented R convention discrepancy or hide useful extra coverage behind
an inflated error label. No physical input or full SM result is banked.
