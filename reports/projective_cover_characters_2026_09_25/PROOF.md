# F17: exact cover marking and conditional analytic join

This argument is authored before execution. Numerical conclusions are
conditional on the stated finite certificates, reported separately.

## 1. The unfilled cover and its characters

Write Gamma=<m,n | r=mnMNmNMnmN>, uppercase denoting inverse. For
H=ker(exponent mod 3), use transversal 1,m,m^2. Its nontrivial Schreier
generators are z=m^3 and x_k=m^k n m^-((k+1) mod 3), k=0,1,2.
Rewriting r from each initial coset gives three relators in these four
generators. There is NO additional z=1 relation. This is the standard
Schreier presentation, directly justified by lifting the presentation
2-complex; the rewriting telescopes t_start*w*t_end^-1 even before
imposing r. Tests check that free-group identity, not just holonomy.

A mu4 character assigns i^a_j to these four generators. It descends
exactly when every relator's exponent row dotted with a is 0 mod 4.
Enumerating all 4^4 assignments with this condition is complete and
has no floating tolerance, early stopping or discarded zero rows.
The Smith form separately checks the expected Z + Z/4 + Z/4 group.

An F14 base automorphism sigma has exponent sign +1 or -1, so preserves
H. Its three lifts differ by deck conjugation Ad(m^j), j=0,1,2. Rewrite
m^j sigma(g) m^-j to obtain its action A on the four abelianized
generators. Then chi(phi g)=i^(A a)_g. H-conjugate lifts have identical
character actions. We do not claim these exhaust all cover isometries.

## 2. Actual coefficient cohomology, not the branched finite-image model

Put rho_H(g)=rho(word(g)) using F10's literal real SL4 matrices. For
chi_a use rho_a(g)=i^a_g rho_H(g), and dual rho_a(g)^-T. For each lifted
relator use the left cocycle identity f(uv)=f(u)+rho_a(u)f(v).
It gives a 12x16 Fox matrix R and coboundary B=stack(rho_a(g)-I),
16x4. Exact R B=0 and the derivation rule give

    h0=4-rank(B), h1=16-rank(R)-rank(B).

This computes group H1 directly; no Shapiro convention or asphericity
assumption is needed for degree one. Complete-core/local-system H1 is
the same group cohomology. F11's full-complex cusp contraction and F12's
pulled-back harmonic metric identify this with ordinary-L2 harmonic
one-forms in the declared hyperbolic end class. F11 already forces
equal dual counts here. No new chiral index is being asserted.

All entries lie in Q(sqrt(d),i). Its automorphism sqrt(d)->-sqrt(d),
i->i maps the entire marked twisted complex and intertwiner equations
at one quadratic root to the other. Rank, nonzero determinants and
zero identities are preserved. This is an exact implication for the
other roots, not a numerical extrapolation. Selected conjugate-root
reruns provide extra implementation controls, not a second census.

## 3. Restriction stays irreducible

H contains m^3,n^3. For any unipotent four-by-four U, put B=U^3-I.
The finite binomial identity gives

    U=I+B/3-B^2/9+5B^3/81.

Thus an invariant subspace for rho(H) is invariant for rho(m),rho(n).
At each exceptional point the 16 explicit word matrices spanning
Mat4 are checked again. The original representation is irreducible,
hence so is its restriction; multiplying generators by nonzero scalar
characters cannot change invariant subspaces. This argument does not
assume an arbitrary finite-index restriction remains irreducible.
It also makes F13 harmonic-metric uniqueness available on the cover.

## 4. Flat pairings and their phase conditions

For each successful base candidate sigma compute an invertible J with

    rho(h)^-T J = J rho(sigma h).

This is checked first on the two base generators, hence on all words.
For phi=Ad(m^j) sigma set J_j=J rho(m)^-j. The same identity holds for
phi. The real untwisted rho has the same equation for an antilinear
map when the input vector is conjugated. Therefore sufficient scalar
conditions are respectively

    linear: chi(phi h)=chi(h)^-1;
    antilinear: chi(phi h)=chi(h).

The second condition uses conjugation of the unitary character. It is
not interchangeable with the first. Check the actual twisted matrix
equations on all four H generators for every positive witness.
Failure of these sufficient tests is NOT a general no-intertwiner result.

## 5. Which witnesses give the whole physical-operator pairing?

For the orientation-preserving inversions theta and thetaT, every lift
has cusp linear part (-1,-1); deck lifts add translations. There is
one cusp in this cyclic meridional cover. In lifted cusp coordinates
their action is (-x+c,-y+d,z). F10's reference connection is independent
of x,y. Consequently F14's reference identity with the unitary matrix
exchanging basis coordinates 0 and 3 is unchanged by those translations.

In a flat peripheral frame the difference between this reference map
and any actual global invertible J_j is an invertible element of the
same peripheral centralizer: replacing exp(N) by exp(3N) does not change
its centralizer, since their nilpotent logarithms are scalar multiples.
The longitude is unchanged. F14's rescaled centralizer estimate gives
uniformly bounded map and inverse. Unitary character factors cancel
precisely under the linear condition above. Normalize det(J_j)=1 by a
constant fourth root. Pullback of the global harmonic metric and the
metric transported from the dual are harmonic in the same bounded-
distance end class. Section 3 and F13 uniqueness identify them.

Thus any such successful LINEAR inversion witness is a same-degree
unitary equivalence of the actual complete Hodge complexes, including
their closed domains. F14's determinant-volume identity and parent
Weyl lift then give equality of corresponding full classical vertex
and scalar-response norms whenever those sources are in their domains.
Regularity/L4 of charged harmonic profiles follows from the pulled-back
F11 confinement as in F13; no new q-dependent numerical gap is claimed.
This is not a derived Lorentzian CP action, a quantum no-go, spontaneous
symmetry-breaking analysis or selection of q, character or base metric.

The wider algebraic list includes orientation-reversing/antilinear
witnesses. This cell does NOT silently extend the preceding full
interaction proof to that list. If all matter-carrying characters have
a linear inversion witness, that suffices to rule out THIS proposed
escape; if not, the remaining analytic question must stay open.
