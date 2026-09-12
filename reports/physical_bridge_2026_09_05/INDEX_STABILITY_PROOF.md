# R26: the fixed-domain backreaction argument

Pre-execution proof candidate, September 12, 2026. Read with
[the design](INDEX_STABILITY_DESIGN.md). The mathematical controls have
not yet run at this writing. This is an application of standard operator
theory to the declared R18/R19 class, not an independently reviewed theorem
or a stationary physical completion.

## 1. Which index is under discussion

Fix [R19's](HOLONOMY_SPECTRUM.md) complete sourced geometry, strong-source
maximal domain, metric, unitary flat line bundle L, and real H=qF. Put

    d0 = d_A+dH wedge,
    D0 = d0,max + d0,max*,
    E = Dom(D0) = Dom(d0,max) intersection Dom(d0,max*).

R18/R19 supply a self-adjoint odd D0, a finite kernel, closed range, and
a positive gap delta off its kernel. No compact resolvent is assumed.
Let H_o and H_e be the odd- and even-form L2 spaces and E_o=E intersect H_o.
The closed graded block T0:E_o -> H_e has adjoint given by the opposite
block of D0. Equip E_o with the original graph norm.

For the pair-free three-arc character the odd/even dimensions are 3/0,
so index(T0)=3. At trivial or Alexander-exceptional transport they are
4/1 with the same index. This is minus the Euler characteristic of
the cochain complex. After a curved perturbation there need not be a
cochain complex at all: the surviving notation is the odd/even Dirac
kernel, not curved H1.

## 2. The genuine connection perturbation and its domain

In an orthonormal frame let epsilon(a) denote wedge multiplication and
iota(a) metric contraction by a real one-form a. For a real abelian
connection perturbation and real mass one-form v,

    B = -i q [epsilon(a)-iota(a)] + epsilon(v)+iota(v).

The sign of the connection term comes from the SAME unitary connection
in the formal metric codifferential. The real mass term instead has the
opposite sign inside its star formula. The resulting B is Hermitian,
form-parity odd and zeroth order. The exterior matrices give

    B^2 = (q^2 |a|_g^2+|v|_g^2) I

for scalar coefficients. Noncommuting bundle-valued coefficients do
not have this scalar norm formula; a triangle bound by the sum of their
pointwise operator norms remains available.

If the zeroth-order changes to d0 and d0* are bounded on L2, their
maximal/adjoint domains coincide with the original ones. For example,
u and (d0+C)u are L2 exactly when u and d0u are L2, since Cu is L2.
For the adjoint, boundedness gives (d0+C)*=d0*+C* on Dom(d0*).
Thus their sum on the original E is D0+B. This does not use d0+C
squaring to zero. A general bounded Hermitian odd B can also be
defined directly on E without representing it as a cochain differential.

Self-adjointness on E follows without choosing a fresh singular extension.
For a real kappa>||B|| and R0=(D0-i kappa)^-1,

    D0+B-i kappa = (I+B R0)(D0-i kappa).

The first factor is invertible by a norm-convergent Neumann series because
||R0||<=1/kappa. The analogous factor at -i kappa is also invertible.
The symmetric operator D0+B therefore has both nonreal resolvent points
and is self-adjoint on E. Its graph norm and the old graph norm are
equivalent by the triangle inequality. Its grading and fixed-sector
interpretation must still be specified; self-adjointness alone supplies
neither of them.

## 3. Local compactness, not a compact resolvent

Suppose B is bounded and supported in a compact subset K of the regular
punctured manifold M minus Delta. A slightly larger regular compact
neighborhood admits finitely many smooth bundle charts. Ellipticity of
the Dirac principal symbol gives, for a cutoff chi supported there,

    ||chi u||_(H1) <= C_K (||D0 u||_(L2)+||u||_(L2)),   u in E.

All coefficients, including the formerly singular mass, are smooth and
bounded on this fixed neighborhood. The estimate is local; it asserts
no uniform Sobolev bound at a source or cusp. Apply compact Sobolev
embedding to any graph-bounded sequence. A subsequence converges in
L2 near K, hence its images under bounded multiplication by B converge
in L2. Therefore B:E -> L2 is compact. Multiplication by B:L2 -> L2
need not be compact.

If B instead tends uniformly to zero outside compact subsets of the
punctured manifold, choose compact cutoffs chi_j with

    ||(1-chi_j)B||_(L2 -> L2) -> 0.

Their products are graph-compact by the preceding argument. Since the
graph norm dominates the L2 norm, this is convergence in operator norm
from E to L2 as well. Its limit is compact. This condition includes
approach to each removed source line, not only large cusp height.

The standard inputs are local elliptic parametrices and Sobolev
regularity, compact embedding, norm closure of compact operators, and
compact-perturbation invariance of a bounded Fredholm index. Their
statements are in [Dyatlov's 18.155 notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf),
Theorems 14.23, 15.1 and 15.8, Proposition 15.6, and Propositions
15.17--15.18. Only these operator-theoretic inputs are used; the notes'
subsequent compact-manifold index formula is not applied to this space.

## 4. Index stability and the separate pair-free bound

Let C=B|H_o, mapping E_o to H_e. It is graph-compact and

    T_s = T0+s C : E_o -> H_e

is a compact perturbation of the fixed bounded Fredholm map T0. For
every finite real s it is Fredholm with index(T_s)=index(T0). Its
opposite block is its unbounded Hilbert adjoint on the unchanged even
domain, by the preceding domain argument. This is the retained graded
Dirac index; no deformed cohomology formula is asserted.

Suppose now that the original even kernel vanishes. For every even
u in E the old gap applies to the whole even space:

    ||D0 u|| >= delta ||u||.

Consequently

    ||(D0+s B)u|| >= (delta-|s| ||B||) ||u||.

If |s| ||B||<delta, the new even kernel remains zero. Fredholm index k
then forces the new odd kernel to have dimension exactly k. The exact
three/zero result follows when k=3. It does not require a numerical
value of delta to prove that an open neighborhood exists; using the
bound for a specified finite physical perturbation would require an
actual estimate of that perturbation and of the gap.

For a paired original kernel this argument does not apply to the entire
even space. Nor does it forbid extra pairs under larger compact
perturbations. Those restrictions are real, not merely conservative
reporting conventions.

## 5. Two infinite-dimensional controls

Set H_o=C^k direct-sum ell2 and H_e=ell2, with
T0(v,u)=delta*u for delta>0. The self-adjoint odd D0 has kernel k/0,
and its nonzero spectrum is +/-delta with infinite multiplicity.
Its resolvent is not compact: normalized mutually orthogonal positive
eigenvectors have resolvent images whose pairwise squared distance is
2/(delta^2+1) at spectral parameter i.

Change only the first matched coefficient from delta to delta-t. This
is rank-one on T and finite-rank on D, so it is relatively compact.
At t=delta the kernel becomes (k+1)/1; elsewhere it is k/0. The index
stays k at the crossing. This proves that index stability without
smallness does not imply pair-free stability, even in an infinite
model with noncompact resolvent. Finite matrices in the producer check
the changed block; the untouched infinite tail supplies the stated
infinite-dimensional model.

By contrast, taking B=-D0 on the WHOLE infinite tail makes D0+B zero
and gives an infinite-dimensional kernel. This bounded perturbation
is not graph-compact and has norm delta. It is outside both the
relative-compact hypothesis and the strict smallness bound. Removing
those hypotheses is therefore not a licensed extension. A scalar
identity shift provides a separate control: it is grading-even, and
cannot be described as the same odd Fredholm block problem.

## 6. A nonflat trial connection inside the stable class

Choose a relatively compact coordinate ball whose closure avoids all
sources and ends. After rescaling its coordinates to the unit ball,
put b(x)=exp(-1/(1-|x|^2)) inside it and zero outside. The one-form

    a = epsilon b(x) x0 dx1

extends smoothly by zero. At the center, da=(epsilon/e) dx0 wedge dx1,
so the connection is nonflat for nonzero epsilon. The scalar covariant
square is -i q da wedge; the real exact mass dH does not cancel it.
This is exactly the cochain failure identified in R22, now combined
with a bounded compactly supported change in the full Dirac operator.

On the compact patch the actual metric is uniformly comparable to the
coordinate metric. Hence ||B||<=C |q epsilon| for a finite C, and the
additional curvature energy is finite. Sufficiently small nonzero
epsilon lies in the pair-free neighborhood. The source singularities,
strong amplitudes, outer periods and global line bundle have not changed.
This is an existence construction of an admissible nonflat trial
connection, not the solution of its Maxwell equation, the original
flat BPS equations, or a coupled stationary source/Higgs system.

## 7. Physical meaning and remaining work

For scalar transport in the fixed Cartan direction u, the Spin(10)
factor and its positive charged spinor block remain intact, so the
scalar index k still labels k copies of that spinor. A matrix-valued
connection on a larger bundle may preserve only a total component
index. If it mixes the opposite charged sectors or breaks the group
used to define a multiplet, the old single-block count is not a
physical invariant of the new problem without an additional map.

In particular this result cannot be used to assume away the costs of
a charge-four Higgs or a new boundary completion. The unchanged extra
U(1) anomaly remains for the isolated three-spinor interior sector.
The neutral sector has not acquired a gap. A change in source strength,
a nondecaying cusp Wilson period, or the added R25 end wall is not a
compactly supported regular-interior perturbation by declaration.

The analytical progress, if the operator controls hold, is therefore
specific: localized curvature need not erase the conditional chiral
index or even the pair-free kernel. The next physical duty is to derive
a stationary source/end action and demonstrate that its actual coupled
solution and admissible gauge symmetries fall within an appropriate
stability class. Anomaly completion, neutral spectrum, gauge breaking,
gravity and empirical normalization are not discharged here.
