# Follow-through: joint deck allocation, sealed separately

Written after the successful boundary gate and result commit 4fb7b80b,
before importing or executing the new deck producer/tests. Original gate
files remain unchanged. This is a continuation, not a changed first test.

## Target

For a global irreducible rank-five E on M2 with the prescribed 2+3
meridian, derive the necessary deck-character distribution if its pullback
to M6 has algebraic index three. Treat exterior-square E in the same
cover decomposition. This specifies a future global search; it does not
construct a representation or assign physical generations.

## Sources and predictions

Use the just-verified exact boundary models and dimensions. The general
finite-cover/Shapiro distinction is already proved in this fork's
deck_descent_2026_09_27/PROOF.md; B1297 also uses relative Shapiro.
The new application is to the ACTUAL E5 and exterior-square E10, not the
rank-six induced witness. Galois equality of ranks is also banked in
B1297; its hypotheses must be stated rather than presumed.

1. Prove balanced global H0 for E tensor any line and exterior-square E
   tensor any line when E is irreducible rank five, using the odd-rank
   alternating-map argument for the exterior square.
2. Prove that such E stays irreducible on the normal index-three subgroup.
   This is a finite-index representation argument, not a computational
   assertion about a candidate that has not been found.
3. Relative Shapiro splits upstairs I as J0+J1+J2. Meridian bounds give
   |J| <= (2,1,1) for E and <= (3,2,2) for exterior-square E.
4. Predict exactly three integer distributions for E with sum +3:
   (1,1,1), (2,0,1), (2,1,0), and their negatives for sum -3. These are
   necessary dimension data, not realized cohomology.
5. If E is defined over a field whose extension by omega has an
   automorphism fixing E and inverting omega, prove J1=J2. Then target
   +3 requires (1,1,1). Do not assume that field hypothesis for an E
   already genuinely defined over Q(omega).
6. Check the local Shapiro comparator directly with rational matrices:
   U on E tensor regular(C3), longitude W tensor identity, and geometric
   deck D of order three. Common boundary dimensions must be 4 and 7;
   D-invariant ones 2 and 3. The whole unipotent transport still does not
   cube to identity. Keep this different from the geometric deck operator.
7. Ordinary geometric invariant projection retains J0, whose magnitude
   is at most two for E. This is NOT a no-go for a finite gauge symmetry
   with charged states or a theory with additional twisted sectors.

Use exact rational ranks, the prior two-dimensional Q(omega) model and
an exhaustive small integer enumeration. Full proof in DECK_PROOF.md;
test the simple-eigenline twist sectors also against a different commuting
longitude that removes their boundary invariants. Seal all new sources
and hashes in a local commit before execution. Preserve any first failure.
