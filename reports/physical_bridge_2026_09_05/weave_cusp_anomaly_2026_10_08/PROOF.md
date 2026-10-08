# The physical index comes from the cusp extremes

Authored conditional derivation in the pinned curved E8 parent and
complete graph domain. Metric, spin, embedding, action, flux and end
law remain supplied. The magnetic solutions are stationary saddles.
This locates the previously calculated anomaly; it does not construct
the missing quantum completion.

## Interior density and the complete line index

At the zero-Higgs endpoint of the established Fredholm homotopy, the
physical mass operator is the direct sum of two spin Dolbeault maps
and two adjoint maps. Its virtual Dolbeault twisting bundle is

    E tensor (2S - 1 - S^2) = -E tensor (S-1)^2.

Let e=c1(E) and s=c1(S), with c1(T Sigma)=-2s. Rank zero and first
Chern character zero follow by expanding

    exp(e)*(2 exp(s)-1-exp(2s))*Td(T Sigma).

Consequently its internal two-form index density vanishes pointwise
at that endpoint. Tensoring with an external unbroken gauge bundle
does not change this cancellation. This statement concerns this
vertical index problem; it is NOT the full six-dimensional anomaly
polynomial under arbitrary gauge/R/gravitational backgrounds. The
actual nonzero-Higgs local density may differ by transgression. Its
index is preserved by the already established gapped homotopy.

For the curvature-minus-one surface of area2pi, the spin curvature
integrates to c1(S)=1/2 in the complete interior Chern-Weil integral.
Thus the Dolbeault density for S^a integrates to B(a)=(a-1)/2.
This is not its global index. The exact L2 result already proved from
the pole cutoff, Weierstrass functions and Hodge adjoint is

    J(a)=h(b(a))-h(b(2-a)).

Separating even and odd integers in that formula gives

    J(a)=B(a)+C(a),
    C(a)=0 for odd a,
    C(a)=sign(1-a)/2 for even a.

No zero sign occurs in the even case. In the cusp coordinate t=log y,
the unitarily normalized zero-angular Dolbeault operator is
partial_t+(1-a)/2. That angular channel exists exactly when a is even;
odd a has the antiperiodic circle. Hence C(a) is half the signature of
the actual surviving radial mass, not a fitted remainder with an
unidentified carrier. The sign convention uses increasing t toward
the cusp. At a=0 and2 the logarithmic integrability endpoints give
J=0 with opposite half contributions; neither endpoint is discarded.

For beta=m+2nq, combining two spin maps and two adjoints cancels every
B term and leaves

    I(beta)=2C(1-beta)-C(-beta)-C(2-beta).

This gives I(0)=0 and -sign(beta)*(-1)^beta otherwise, independently
agreeing with the prior physical index. No new zero-mode species are
introduced by rewriting that SAME index as an end contribution.

## The coupled physical end and every extreme

The previous physical dictionary supplies exact bundle isometries from
the four-Weyl operator to the Hodge map. At c=d=0 the latter contains
the h=0 single-Q block and the ADJOINT of its h=1 spin-shifted copy.
For integer principal spin j, weight m, k=nq and principal amplitude
tau in[0,1], each admissible m-h even pair has operator

    B_h = [[partial_t+delta,tau*b],[-tau*b,-partial_t+delta]],
    delta=k+(m+1-h)/2,
    b^2=(j-m)(j+m+1)/2.

Multiplication by Jrad=diag(1,-1) gives partial_t+C_h with

    C_h=[[delta,tau*b],[tau*b,-delta]].

This Hermitian matrix squares to(delta^2+tau^2*b^2) times the identity.
Every such delta is a nonzero half-integer for integer k. Thus the two
eigenvalues are nonzero and opposite; their signature is zero at every
tau. Taking the adjoint reverses the radial orientation: after the
corresponding unitary multiplication its matrix is -Jrad*C_h*Jrad.
This reverses the signature, rather than adding the h=1 signature.

Each shifted block also has exactly one unpaired extreme:

- if j-h is even, the upper connection mode contributes mass
  -[k+(j+1-h)/2];
- if j+h is odd, the lower spin mode contributes mass k-(j+h)/2.

The h=1 block is then adjointed as above. Both shifts together contain
2(2j+1) horizontal slots. This is the physical gaugino plus connection
and both spin fields, not an auxiliary subtraction. Define Eta(j,k)
as the ordinary finite signature of this FULL end mass matrix.
It is not the eta invariant of the complete five/six-dimensional
gauge-dependent determinant. The extreme formulas give

    Eta(j,k)/2 = -[sign(k+(j+1)/2)+sign(k-(j+1)/2)]/2, j even;
    Eta(j,k)/2 =  [sign(k+j/2)+sign(k-j/2)]/2,       j odd.

By summing the line C terms, these expressions equal
sum_{m=-j}^j I(m+2k) for every integer k. Paired contributions cancel
telescopically; the displayed extreme masses remain. This proves the
all-integer result, with finite exact checks only as controls.

The actual charged modules are V2 at q=1,4,6, V1+V3 at q=2,3 and V0
at q=5, with their gauge multiplicities and conjugates. For j=2,k=1
the two extreme masses have opposite signs, so the index is zero.
For j=2,k>=2 they have the same sign, giving minus one. The other
rows similarly give(-1,2,2,-1,-1,-1) at positive n>=2, with charge1
zero at n=1. Opposite flux reverses them. At n=0 all vanish.

Finite c,d multiply the decaying physical section psi and are graph-
compact. They leave the end matrices and index unchanged. Coupled
paired masses remain opposite at tau=1, not only at the zero-Higgs
endpoint. Neutral and charged modules retain all248 internal weights
and496 horizontal slots. The same physical color/weak/Z trace applied
to Eta/2 reproduces all five prior anomaly coefficients, including
the charge-five exotic. End signature is the source of that nonzero
index, not its compensator.

Albin--Rochon, [Families index for manifolds with hyperbolic cusp
singularities](https://arxiv.org/html/0801.1969v2), section1.4 and
section2.1, distinguish the vertical circle kernel from the horizontal
operator on that kernel, and require a renormalized trace when the
heat operator is not trace-class. This motivates the type of check;
our explicit matrices/global counts establish the identity here.
No uncomputed families eta form or regulator phase is borrowed.

## Gauge modes and why the gap is insufficient for a determinant

Let T be an unbroken generator commuting with A_n,Q,R. An internally
constant four-dimensional gauge field has positive kinetic coefficient

    1/g4^2 = Area(Sigma)/g6^2 = 2pi/g6^2

in the same trace convention. g6 and the curvature unit remain supplied.
For a normalized internal fermion wavefunction, the constant generator
acts by its actual representation matrix; no vanishing cusp overlap
or separately chosen coupling removes its gauge interaction.

The constant internal section is in the complete scalar graph domain.
For a cutoff equal to1 before t=T0 and0 after T0+1, with uniformly
bounded derivative, its lost norm and derivative norm are bounded by
constants times exp(-T0), since cusp area is ell*exp(-t)dt. Smooth
approximations give compact-support graph convergence. Parallel
unbroken gauge transformations commute with the operator, preserve
its compact core and hence its closure. Spacetime-dependent parameters
of compact spacetime support retain this internal action. Excluding
these transformations would be a changed theory, not an anomaly cure
already implied by the complete domain.

Nevertheless the internal heat operators are not trace-class. Take
one unpaired end channel of mass mu and normalized functions supported
on successively disjoint intervals [T_i,T_i+L]. A Dirichlet sine bump
(or smooth approximants) has squared-operator Rayleigh quotient
mu^2+pi^2/L^2. Moving it out leaves this bounded; decaying c,d terms
give vanishing corrections. The functions are orthonormal. By the
spectral theorem and Jensen's inequality,

    <f_i,exp(-s H) f_i> >= exp(-s <f_i,H f_i>) > constant >0

for fixed s>0 and uniformly bounded energies. Their sum diverges, so
exp(-sH) is not trace-class. This does not contradict a positive
essential gap. The two individual traces of a putative supertrace
are divergent; cyclic cancellation cannot be assumed without specifying
the relative/renormalized trace and its end defect.

Witten--Yonekura, [Anomaly Inflow and the Eta Invariant](https://arxiv.org/html/1909.08775),
section2.1 and the regulator discussion in section2.2, derive an inflow
phase from a specified massive fermion, regulator and boundary problem.
Their phase is not inferred from a finite signature alone. Our complete
cusp is not their already-specified local boundary problem. Matching a
finite anomaly coefficient does not supply that missing physical map.

## What an interior condensate can and cannot change

Consider M as a bounded Fredholm map from its graph Hilbert space to
the target, and let V be graph-compact and color-equivariant. A bounded
parametrix for M has identity remainders compact; composing it with
M+tV still has compact remainders. Hence M+tV is Fredholm and its
index is constant along the norm-continuous path for finite t.

The same argument applies to each SU3 isotypical multiplicity space:
compact-group projections commute with M,V and preserve compactness.
The parent has only finitely many color types, so its equivariant
index and cubic color-anomaly coefficient stay fixed. Smooth
color-preserving compact-core field changes, and bounded decaying
zeroth-order changes with the same domain, obey these hypotheses.

Thus such a deformation alone cannot change the computed nonzero
SU3^3 coefficient. It may change individual kernels by vector-like
pairing and may improve classical stability; neither changes the net
anomaly. This does NOT cover changing the Fredholm end, passing through
an essential gap closure, changing domains/field content, or breaking
color. It also does not exclude a full parent/end quantum compensation.

No inflow action, determinant phase, gauge-invariant quantum measure,
global anomaly cancellation, new stable condensate or selected physical
generation is derived here. The next load-bearing duty is the regulated
parent/end Ward identity for these very finite-norm gauge modes, with
the outer end retained. Foundation-to-parent selection, source/silver
alternatives, observer/qualia and gravity remain separate obligations.
