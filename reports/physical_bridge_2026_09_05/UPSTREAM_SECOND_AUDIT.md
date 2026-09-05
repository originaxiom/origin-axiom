# Second upstream landing: exact positives and bounded corrections

Upstream 8f83b5c8 merged as e3b51950. Design, instrument and classifier tests
sealed at **8659634f before execution**. The isolated B854 rebuild and exact
checks completed in 85.50 s; source stdout, rational invariants and results
are preserved in `upstream_second_first_run.json`. No banked output or
foreign pickle was overwritten or loaded. The subsequent quiescent suite:
**74 passed, 2 failed in 59.57 s**, out of 71 physical-bridge tests and five
B1255 tests. Both failures are the unchanged R7 small-step controls already
diagnosed by polynomial polarization. Raw output: `UPSTREAM_SECOND_TESTS.txt`.
This is not a full-repository green certificate.

## B1254/B497: the named dynamics survive; the classification needs repair

All three trace substitutions have exactly zero polynomial remainders:
metallic kappa'=kappa, decimation kappa'-2=(kappa-2)x^2 y^2, and Thue-Morse
kappa'-2=(kappa-2)(x^2+y^2-xyz). The TM polynomial has odd degree and is
not a square. Explicit rational matrices give class ratio -4, so actual
class change is exhibited, not inferred from a generic polynomial alone.

Three distinct corrections must not be conflated:

1. **Instrument defect.** B1254's square predicate returns True on x^2+1.
   Its dummy-symbol radical check does not ask whether sqrt(F) is a
   polynomial; squaring sqrt(F) then subtracting F is not that test either.
   Independent factorization rejects x^2+1 while accepting genuine rational
   polynomial squares. The two original headline classifications still hold.
2. **Domain boundary.** A=[[0,-1],[1,0]], B=diag(2,1/2) gives kappa=17/4,
   but kappa(A^2,B^2)=2. Thus even injective decimation can take a defined
   square class to the undefined zero locus. Preservation requires xy!=0
   and kappa!=2. The reducible locus remains absorbing; that is not a
   proof that only noninjective maps can reach it.
3. **Stratum scope.** The endomorphism a->abABa, b->b (capitals mean
   inverses) has identity abelianization. At A=[[1,1],[0,1]],
   B=[[1,0],[1,1]], kappa changes from 3 to 6 and its two image matrices
   do not commute. The images therefore generate a rank-two free subgroup;
   Nielsen-Schreier and the Hopfian argument already cited in B497 give
   injectivity. It is not an automorphism: automorphisms of F2 preserve the
   commutator trace. Consequently "injective, det +/-1 = Aut" is false.
   This witness changes kappa, **not** its square class (ratio 4). It does
   not itself refute every proposed square-class classification. The three
   named examples do not establish laws for all maps in their determinant
   strata. Do not replace that unproved generalization with a new one.

This does not revive a claim of derived physical time or erase the actual
mathematical dynamics. Nor does it turn the scoped B1157 physical-law
question into a universal no-dynamics verdict.

## B1255: the matrix obstruction is genuine on its stated carrier

Rebuilding all four B854 invariants gives independent rank 4 and zero mutual
brackets; the restricted E6 Killing form has rank 4. The preserved producer
also reports its 4000 random Jacobi controls, not an exhaustive Jacobi proof.
Using these exact invariants with the pinned B883 27 gives:

- both named cubics irreducible, totally real and S3, discriminant kernel 7,11;
- colored factor degree 6, kernel dimension 18 and D2 split 12/6;
- W18 invariant under D2, with commutator rank **12**;
- stacked (D-I)C^k has full rank 18 through k=2; stacked (D+I)C^k through
  k=1 also has rank 18. Therefore **no** nonzero C eigenvector lies in either
  D2 eigenspace, even after scalar extension. This strengthens an eigenbasis
  sampling check without pretending the matrix tier was covered by upstream CI;
- [D2, Cartan_0]=0 as a genuine positive commuting control.

The elementary **single-carrier** bound stands: three independent 16s need
48 components, more than 27. Even three SM families without right-handed
neutrinos require 45. I-24 remains REFUTED in that linear representation
scope. This does not exclude extra copies, other carriers or a separately
constructed dynamical/composite origin of multiplicity.

## Do not let a correct bounded result close untested doors

D2 is the specified intermediate SO10 grading, not automatically every
physical gauge charge after symmetry breaking. R4 already demonstrates
that the actual light 5bar can mix the old graded subspaces. The dimension
bound does not need this grading assumption and remains valid.

A quadratic number field has at most two primes over a rational prime.
That theorem concerns prime splitting, not every possible field multiplicity.
It does not prove that a physical three requires an irreducible cubic, or
that B1253's h^1 mechanism is the only surviving route. Merely inserting
three copies would supply a count, not derive it; neither is done here.

Similarly, commuting diagonalizable operators need not have degenerate
eigenvalues. Simultaneous diagonalization alone cannot prove the necessity
claim about hierarchy. B923's actual two-form calculation is not refuted:
its causal generalization would require a controlled commuting counterfactual
in that construction. This audit rebuilds the B1255 matrices, not the full
B923 numerical root/ratio calculation or a genealogy of every old three-ness.

Point-of-use addenda accompany B497, B1254 and B1255. Their sealed code and
original findings are retained. The physical continuation remains R7's
controlled broken-phase calculation, not an assumption that a family count
or a complete TOE has now been settled.
