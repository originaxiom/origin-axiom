# F11 post-failure correction: retain the nongeometric matter loci

September 21, 2026. Original science seal 85454725 remains unchanged.
The first run returned 27 pass / 3 fail: the assertion that every
positive rank exception lies at q=1 was FALSE for the three nontrivial
central characters. This is a failed mathematical expectation, not a
tolerance or symbolic-comparison bug. The producer and all original
assertions are retained, with the first-run transcript separately filed.

The unchanged producer's complete maximal-minor calculation gives:

| central character chi | gcd of J's real/imaginary maximal-minor numerators | positive roots |
|---|---|---|
| 1 | (q-1)^2 | 1 |
| -1 | q^2-34q+1 | 2 |
| i, -i | q^2-14q+1 | 2 each |

The B matrix has gcd 1 in every case, so rank B=4 for all positive q.
Every denominator is a power of q times a nonzero constant. These are
rank-locus certificates, not a fit to sampled ranks. The ordinary
geometric-point control H1=1 passed for chi=1; the other three have
H1=0 at q=1. No physical L2 conclusion is imported at that excluded
endpoint of the cusp argument.

## Corrected claim to test, before the follow-up execution

Expect rank J=3, hence H1=1, at EACH nongeometric root above, for both
the defining four and its dual. The roots are

    chi=-1:      q=17 +/- 12 sqrt(2),
    chi=+/-i:    q=7 +/- 4 sqrt(3).

All are positive, unequal to one, and paired by q->1/q. The polynomial
discriminants are 1152=24^2*2 and 192=8^2*3; both quadratics are
irreducible over Q(i). Therefore a rank and nontrivial-class witness
over Q(i)[q]/p certifies BOTH real embeddings, without floating rounding.
Check an additional 3-by-3 minor nonzero at every root using polynomial
gcd 1 with p. All 4-by-4 minors vanish there by the already computed
certificate. Verify the dual directly as well as through F10's duality.

Compute an explicit nontrivial generator cocycle over each quadratic
field: J v=0, rank B=4, rank(B|v)=5. This is a cohomology representative,
NOT an evaluated harmonic wavefunction. Compare the full symbolic Fox
and affine cocycle matrices on these central-character families before
using their specializations. No changes to the original producer.

If this corrected exact check succeeds, PROOF.md sections 1--4 identify
one normalizable coefficient one-form in EACH dual sector for any
smooth complete realization matching F10's tails. That is an operator
existence and multiplicity result even for a nonstationary chosen metric;
it is a statement about a physical vacuum only conditional on obtaining
a global solution of the parent equations in that same end class.

This improves the next task: test the exceptional backgrounds, not a
generic deformation that the same calculation finds acyclic. The known
Ballas theorem guarantees projective geometry only sufficiently near
q=1; it is NOT cited as a geometric or physical existence theorem at
these distant exceptional parameters. The representation and local tail
are exact for them. Their positive spectra/interaction asymmetry, global
moment equation and allowed end action remain separate.

There is one pair, not three generations and not net chirality. No
measured constant entered the calculation, no physical value is being
predicted, and no action has selected a character or one of the roots.
The fixed-end q variation still has the infinite kinetic norm proved
in the original analytic note. A fixed nonnormalizable parameter is
not thereby a dynamical scalar or a forbidden background.

Seal this addendum, additional producer, corrected tests and preserved
failure transcript before the follow-up test. The old negative expectation
does not survive as an unqualified finding anywhere in the living reports.
