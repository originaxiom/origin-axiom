# R32: the C3 module of the sourced modes, and what projection retains

2026-09-16. Authored pre-execution argument, not independent proof review.
This is a conditional calculation in the R19/R20/R30/R31 realizations.
It does not identify an arithmetic-parent quotient with a physical vacuum.

## 1. Precisely which action, bundle and domain

Let Q be the compact C3-invariant torus-boundary truncation of m202 used
in the source construction. Let g be either generator of its actual
order-three isometry group. R20's exact word actions and certified
canonical enumeration establish that g preserves orientation and both
cusps, with three fixed points on each cusp torus. Its fixed locus has
three proper arcs and possibly additional closed circles. A nonidentity
orientation-preserving hyperbolic isometry is locally a rotation about
an axis; thus there are no extra isolated fixed points. Six boundary
endpoints account for three arcs; closed components contribute Euler zero.
No assertion that closed components are absent is needed here.

Take invariant disjoint solid neighborhoods N_j of the three proper
arcs, N their union, and C the source exterior. Retain the lateral tube
boundary T and the complementary punctured cusp boundary E. The
equivariant excision equivalence is (C,T) ~ (Q,N), not (Q,E).

The line L is unitary and flat on Q, extends across every N_j, and has
an HONEST order-three connection-preserving lift U of g. R20 constructs
such line lifts for the three invariant adjoint characters

    (x,y)=(1,1), (zeta,zeta^-1), (zeta^-1,zeta), zeta^2+zeta+1=0.

A fixed basepoint splits the orbifold extension by C3. An invariant
character extends to the semidirect product with any of the three
scalar C3 phases. This is a line-system statement, not a classification
of principal E6 lifts. R20's simply connected scalar-lift obstruction
is unchanged. The form-complex action here is not an asserted spin lift
on a different untwisted spinor theory.

Use an invariant metric, real source potential F, and outer data.
For the singular comparison assume exactly R19's strong positive-source
maximal domain and q beta_j>=1. Invariant cutoffs, radial integration
and collars make its comparison maps equivariant; a finite-group
average of a bounded chain homotopy remains a bounded chain homotopy.
Thus its charged H1 module is H1(Q,N;L), not merely a vector space of
the same dimension. No invariant-mode projection was performed in R20.

For finite widths use exactly R30's extending-flat, positive bulk norm,
absolute outer Hilbert complex, with R31's compact normalized Poisson
source when discussing light modes. Symmetric sources and Dirichlet
data give invariant F_epsilon by uniqueness. The truncation is fixed;
no uniform estimate in cusp length is asserted.

## 2. Fixed-fibre trace, without treating fixed arcs as permuted arcs

The only external topology input in this step is existence of a finite
equivariant triangulation including the boundary. It is explicitly
stated for this situation in Luck--Rothenberg, Definition 5.2/Theorem
5.3, PDF pp.33--34, [author-hosted primary text](https://him-lueck.uni-bonn.de/data/neumann.pdf).
Their hypotheses allow a compact manifold with boundary and a finite
smooth group action; stabilizers need not act freely. The accessed
definitions/theorem and surrounding argument were read, not the whole
64-page paper. Illman's original journal PDFs were not obtained and
are not represented as personally read. In this example R20 also
supplies a finite canonical triangulation with the actual action;
invariant truncation and subdivision give the same cellular setting.

Here is the needed local-system trace argument. Barycentrically
subdivide so that a stabilized simplex is fixed pointwise. Nonfixed
simplex orbits have length three and zero trace on their cochain
summands, including transport phases. A fixed simplex contributes its
fibre trace with its cochain-degree sign. That trace is constant along
each connected fixed component because U preserves the flat connection.
Cancellation on boundaries and coboundaries (the Hopf trace identity)
therefore gives

    sum_p (-1)^p tr(U | H^p(Q;L))
        = sum_{F component of Q^g} chi(F) tr(U | L_F).

This uses ordinary twisted cohomology with a finite group action, not
the Cartan/Borel equivariant cohomology differential. It is also not
an APS formula. A closed fixed circle contributes zero, even when the
restricted local system has holonomy; its twisted Euler trace is zero.

At either nontrivial invariant character R19's actual Fox complex is
acyclic in every degree: its polynomial is P=-2. Write lambda_j for
the lift's fibre eigenvalue on the j-th fixed arc. Each is a cube root
of unity. The trace identity gives

    lambda_1 + lambda_2 + lambda_3 = 0.

Let n_a count eigenvalues zeta^a. Reducing the sum modulo
zeta^2+zeta+1 yields (n_0-n_2)+(n_1-n_2) zeta=0. Since 1,zeta are
rationally independent and n_0+n_1+n_2=3, all three n_a are one.
Thus H0(N;L) is the REGULAR C3 module 1 + zeta + zeta^2.
The arcs are individually fixed; it is their flat fibre weights which
differ. No ordered identification of a particular weight with a
particular geometrical arc is claimed. Changing the overall lift phase
or reversing the generator permutes the three weights.

## 3. Relative source module and its quotient

The pair's long exact sequence is equivariant. Since H*(Q;L)=0 and
N consists of three contractible neighborhoods, its connecting map is
an isomorphism

    H0(N;L) --delta--> H1(Q,N;L),

and all other relative groups vanish. Consequently the full source
three/zero kernel is one copy of the regular C3 module. For every
honest scalar lift its invariant subspace has dimension ONE. Invariants
are exact over C, by averaging; projecting the complex or its cohomology
therefore gives the same result. Complementary-boundary duality gives
the conjugate sector in degree two and does not supply a second H1.

If the added internal gauge factor W is unchanged by C3, this is one
copy of W after projection, rather than three. More generally, for a
constant honest C3 action on W, (Reg(C3) tensor W)^C3 has dimension
dim W. As a representation of the gauge centralizer of that C3 action
it is isomorphic to W restricted to that centralizer. Noncentral gauge
actions can change the unbroken gauge group; the statement must not
be advertised as preserving all of Spin(10) in that case.

This is a specific UNTWISTED invariant-sector calculation. It neither
adds nor counts new fields localized on orbifold strata. It does not
derive that C3 is gauged. Keeping C3 as a global symmetry leaves the
full three source modes intact. B325 already distinguishes the three
one-dimensional C3 irreducibles and their independent allowed masses;
no degeneracy or numerical mass prediction follows from this module.

## 4. Trivial-line control: same net module, different kernel

For the trivial line and the natural lift, H0(Q)=1 and H1(Q)=zeta+zeta^2:
the actual R20 H1 matrix has characteristic polynomial t^2+t+1.
H2(Q)=1: Q is the two-component link exterior with b2=1, and the
orientation-preserving action fixes both boundary tori; their fundamental
classes surject onto H2 with their one total-boundary relation.
H3(Q)=0. Also H0(N)=3 copies of the trivial representation.

The long exact sequence and semisimplicity over C give

    H1(Q,N) = 2*1 + zeta + zeta^2 = Reg + 1,
    H2(Q,N) = 1.

Multiplying the lift by mu=zeta^a twists every group uniformly. The
projected (H1,H2) dimensions are (2,1), (1,0), (1,0) for a=0,1,2.
Their virtual odd-minus-even module is always Reg, and their net
invariant index is one. This control is not the nontrivial-line
three/zero kernel. In particular acyclicity cannot be omitted from
the fixed-fibre argument to assign one weight to each arc: for the
trivial natural lift all three fibre weights are instead one.

## 5. Core gluing and positive-energy pairing survive an honest projection

For the nontrivial characters R30's split relative-plus-core complex
has Reg in odd degree and Reg in even degree. The boundary connecting
map identifies the two modules; a nonzero equivariant attachment is
an isomorphism. Projecting this exact complex retains one on EACH side
at zero attachment and no cohomology at nonzero attachment. Dropping
only the even copy is not the same group projection.

This also holds at the analytic positive spectrum without identifying
an algebraic attachment parameter with a physical mass. Let D be the
closed self-adjoint odd Dirac operator, and U a unitary, grading-preserving
symmetry which preserves its domain and commutes with D. On each
positive eigenspace of D^2 with eigenvalue lambda,

    D / sqrt(lambda) : even eigenspace -> odd eigenspace

is an equivariant unitary isomorphism. Hence ANY isotypic projection
preserves positive-energy partners. The hypotheses about the operator
and domain are essential. This does not force the zero eigenspaces
to pair. A counterexample to that over-wide statement is ordinary
de Rham theory on a circle: reflection acts as +1 on H0 and -1 on H1;
its invariant zero modes have counts one/zero, while every positive
Fourier level still has equally many even and odd invariants.

For the invariant R31 source family, choose invariant whole-arc
cutoffs. A parallel section s_j on N_j transforms by its fixed-arc
weight lambda_j, so exp(-qF_epsilon) chi_j s_j lies in that isotypic
sector. The three trial functions therefore span Reg, not three
invariant functions. R31's bounds give one trial Rayleigh quotient
tending to zero in EACH sector. Applying min-max separately in the
three invariant closed sector subspaces gives at least one positive
light pair in each, hence at least ONE retained positive light Dirac
pair after the invariant projection. Positivity uses H0(Q;L)=0.
For its arc a_j=q beta_j, the unchanged upper bound is
lambda<=C epsilon^(2a_j-2) if a_j>1, or C/log(1/epsilon) if a_j=1.
No exactly-one count, lower mass bound or uniform complete-cusp result
follows. A lift phase selects another arc sector without removing its
positive-energy partner.

## 6. Physical scope and a concrete next test

The unquotiented singular construction retains three/zero. Its honest
C3 invariant sector has one/zero for the nontrivial flat characters.
The resolved absolute compact realization is acyclic at each width,
and retains at least one positive light pair after projection in the
strong shrinking-source regime. These are three different statements,
not a retraction of the singular result or a universal orbifold no-go.

An interacting defect, additional localized sectors, a different
boundary/kinetic space, a noncentral parent lift or a different cover
changes hypotheses and requires its own spectrum. A productive next
test is an explicit defect/end coupling whose full Dirac domain and
gauge transformations are specified, followed by its kernel, current
normalization and anomaly calculation. Selective deletion of a core
partner is not yet such an action. The added operator, source strengths,
parent/global form and quotient choice remain physical inputs here;
no coupling, mass, spacetime dynamics or TOE is derived.
