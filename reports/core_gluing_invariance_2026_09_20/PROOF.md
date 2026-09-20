# F07 authored comparison: the global complex survives regular core replacement

This is an application of standard closed Hilbert-complex theory with
an explicit quantitative estimate. It is frozen before its finite controls
run. No independent proof acceptance or global physical completion.

## 1. The comparison is of complexes, not of identical Laplacians

Use the same underlying graded vector spaces and distributional flat
differential d, with reference and new norms satisfying

    m ||u||0^2 <= ||u||1^2 <= M ||u||0^2,
    0<m<=M<infinity,                              (1)

in every degree. The L2 sets and topologies are identical. The maximal
graph domain {u:u,du in L2} is identical, and minimal graph closure of
compact smooth forms is also identical. Thus either consistently chosen
closed complex remains the same complex. We do NOT choose a new boundary
condition and declare it equivalent.

The adjoints need not be identical. If G is the bounded positive degree-
preserving metric operator, d1*=G^-1 d0* G on its properly transported
domain. This is not d0* and does not identify the two Dirac spectra. For
smooth complete positive geometric realizations, F02 supplies the
self-adjoint de Rham Dirac realization. The argument also works directly
with the closed Hilbert complex and its quadratic form.

## 2. Reference gap gives a bounded contraction

Suppose Q0=d+d0* is self-adjoint and

    ||Q0 u||0 >= delta0 ||u||0, delta0>0.          (2)

The closed-range Hodge decomposition is acyclic. On exact forms define
K0 to be the minimum-norm primitive in the orthogonal coexact subspace;
set K0 to zero on that coexact subspace. The reduced minimum modulus of
d is at least delta0 by (2), so ||K0||0<=1/delta0. Equivalently
K0=d0* Delta0^-1, but no informal commutation of arbitrary unbounded
operators is needed: on the Hodge summands its domain and action give

    K0:H -> Dom(d), dK0=P_exact,
    dK0+K0d=I on Dom(d), K0^2=0.                 (3)

The old gap and Hodge decomposition are justified by the same Hilbert-
complex closed-range argument already used in R18; F05 provides (2) for
the chosen geometric coefficient system. This is not an application of
compact-manifold Hodge theory to an unexplained cusp boundary condition.

## 3. Transport and a quantitative gap with the new adjoint

By (1), the very same K0 is bounded in the new norm with

    ||K0||1 <= B := sqrt(M/m)/delta0.             (4)

Its image is still in Dom(d), and (3) still holds. For any closed u,
u=dK0u. Therefore ran d=ker d is closed, so the new complex is acyclic.
In particular both unreduced and reduced cohomology vanish.

Here is a direct proof of the new quantitative bound, including the
adjoint's role. If y is in Dom(d) and orthogonal to ker d in the NEW
metric, then y-dK0y=K0dy and dK0y is in ker d. Consequently

    ||y||1^2=<y,K0dy>1 <= B ||y||1 ||dy||1.

If x is in ker d and Dom(d1*), then x=dK0x and

    ||x||1^2=<d1*x,K0x>1 <= B ||d1*x||1 ||x||1.

For a general u in the form domain Dom(d) intersect Dom(d1*), split
u=x+y orthogonally into ker d and its complement. The latter is ker(d1*)
because ran d=ker d. Thus x,y retain the required domains, dy=du and
d1*x=d1*u. Adding the two inequalities gives

    ||du||1^2+||d1*u||1^2 >= B^-2 ||u||1^2
                          =delta0^2(m/M)||u||1^2. (5)

This establishes a positive bound for the associated self-adjoint
Laplacian. In the complete smooth Dirac realization it gives
|Q1|>=delta0 sqrt(m/M). It needs no small perturbation norm and no
parallel-Higgs identity in the deformed metric. Derivatives of the
metric can change local mixed terms without changing this conclusion.

For F05's coefficient four and its dual, separately,

    Delta1 >= (9/4)(m/M)>0.                      (6)

This is a lower bound, not an exact bottom or an observed mass.

## 4. What geometric changes meet these hypotheses?

Smooth positive base and fiber metrics agreeing with the old ones
outside a compact set have bounded positive relative eigenvalues and
bounded inverses on that compact set. Exterior-power norms AND volume
densities therefore satisfy (1). For example g1=b^2 g0 in dimension
three and fiber h1=c^2 h0 scale the degree-p norm density by

    c^2 b^(3-2p), p=0,1,2,3.

Bounds must include every relevant degree. Equality of pointwise fiber
norms alone is not a full kinetic-norm comparison. More general uniformly
equivalent metrics also work; a degenerating family need not have common
m,M. Completeness is preserved by a fixed smooth compact modification
of a complete base.

If the flat connections are related by a smooth bundle isomorphism T,
first transport the second complex to the first: d1=T^-1 d0 T. After
pulling back the positive metrics, apply the preceding comparison when
T,T^-1 and the transported norms are bounded as specified. A compactly
supported smooth change of flat trivialization has this property. This
is NOT a unitary conjugacy of Dirac operators in the unchanged norm.

## 5. Why filling a regular ball leaves the holonomy fixed

Let M be connected and three-dimensional, and B_j finitely many disjoint
embedded closed balls contained in the regular interior. Use collars to
apply van Kampen to M=(M minus interiors B_j) union balls. Each overlap
retracts onto S2, which is simply connected, and each ball is simply
connected. Thus the exterior inclusion induces an isomorphism on pi1.

Suppose two smooth flat coefficient bundles/connections are identified
on that exterior and its collars, and both extend smoothly across the
balls on the SAME underlying manifold. Their based holonomy representations
are identical, since every generator is represented in the exterior.
Parallel transport constructs a flat-bundle isomorphism globally, agreeing
with the given identification outside; path independence is exactly the
holonomy equality. On the finitely many compact balls its matrix and
inverse are bounded for any smooth positive metrics. Apply sections 1--4.

Therefore a hypothetical regular F06-type core matched to the unchanged
F05 geometric exterior, with ordinary complete L2 and no added singularity,
new boundary or extra field, STILL has no charged spinor zero modes.
This result is conditional on existence of that matching; it neither
constructs nor disproves the classical gluing itself. Its point is that
even successful gluing with those preserved data does not solve chirality.

This is not an assertion for arbitrary regions whose exterior fails to
carry all pi1 generators, replacing a ball by a handle, a source arc
running out a cusp, a drilled tube with a new boundary, or a change in
global holonomy. Those cases must be checked separately.

## 6. Exact controls keep three different conclusions apart

For a finite acyclic complex C -> C2 -> C with
d0=(1,0)^T and d1=(0,1), the reference total Laplacian is I. Changing
the positive metric changes its adjoint and its nonzero eigenvalues but
keeps exactness. The exact non-diagonal metric in the producer gives
eigenvalues 2/9 and 1/8, each twice; the coarser bound m/M=1/36 holds.
This is an algebraic control, not a discretized physical manifold.

For the two-term differential d=1 with norm matrices (t^2,1), t>=1,
the Laplacian is t^-2 I. Thus bound (5) is sharp in general and a family
can have arbitrarily light positive pairs while every finite t remains
acyclic. Uniform equivalence degenerates as t tends to infinity. This
retains R30/R31's warning that no exact zero does not imply heavy matter.

Changing the differential is different. On a circle of length 2pi,
flat unitary d_alpha=d+i alpha dtheta has mode eigenvalues (n+alpha)^2
in both degrees. For alpha=1/2 the bottom is 1/4; for alpha=0 there is
one zero in each degree. The would-be removing gauge exp(i alpha theta)
is not periodic at half-integer alpha. This is a changed holonomy control,
not an example of chiral matter or unchanged-holonomy ball surgery.

Finally, on the real line d0=d+dx wedge has Q0^2=-partial_x^2+1.
The same ordinary trivial bundle with d1=d+x dx wedge instead has the
Gaussian zero mode exp(-x^2/2). The chain multiplier relating them is
exp(x^2/2-x), unbounded at infinity. Ordinary bundle isomorphism alone
does not satisfy (1)--(4). This reuses the known oscillator/end control,
not a new BPS source or a physical one-dimensional replacement theory.

## 7. Physical consequence and next-action change

R26's general odd compact perturbations may add pairs without changing
an index; there is no contradiction. Here the stronger restriction is a
fixed FLAT COMPLEX under bounded chain/norm equivalence, so all kernels
remain zero. F06's lost pointwise bound does not defeat this global one.

Do not spend the next effort seeking massless matter through a regular
compact replacement with unchanged geometric holonomy. The local core
remains a valid positive background and a geometry comparator. A matter
mechanism needs to change load-bearing data: a suitable nongeometric
global flat system, non-equivalent end behavior, a physically selected
singular/domain completion, nonflat/non-BPS terms or an enlarged field
system. These are necessary distinctions, NOT proof that any such option
is sufficient or already realized. All full-parent, anomaly, interaction,
gravity and empirical requirements remain.
