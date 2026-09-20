# R40 authored coefficient/parent join

Pre-execution argument, 2026-09-20. Finite exact checks below support this
construction; they cannot certify the existence of its physical vacuum.

## 1. The determinant is part of the coefficient, not a convention

Use R27's marked rank-two representation over u^2-u+1=0,

    rho(a)=[[0,1],[-1,1]], rho(b)=[[0,u^2],[u,-2]],
    P=[[1,0],[u,1]], chi(a)=u, chi(b)=-1.

Conjugation by P gives upper triangular generators with diagonal
(u,1-u),(-1,-1), and upper entries 1,u^2. The coefficient
V=chi Sym3(rho) has determinant chi^4, since Sym3 of an SL2 matrix has
determinant one. On a this is u^4, of order three. Thus this very V
cannot be the defining-four SL4 coefficient of R39. This does not
exclude non-scalar changes, simultaneous gauge holonomy, or other E8 maps.

Every scalar replacement with determinant one is delta Sym3(rho),
delta^4=1. Abelianization of the stated relator is 6a=0, with b free.
Consequently delta(a)=+/-1 and delta(b) is any fourth root: eight cases,
not a bounded numerical census. Their cusp characters are
delta(mu)=delta(a)^-3 delta(b) and delta(lambda)=delta(b)^2. Only
(1,1) and (-1,-1) are trivial on the cusp. Those two have an invariant
nondegenerate bilinear form from Sym3 and delta^2=1, so their interior
indices vanish. In the remaining cases a peripheral eigenvalue differs
from one; the corresponding (scalar times unipotent) matrix minus I is
invertible, hence torus cohomology vanishes. Their interior indices are
computed, not concluded from torus acyclicity alone without checking H0.

## 2. A faithful enlargement retaining the original representation

For any X in GL4(C), j(X)=diag(X,det(X)^-1) belongs to SL5(C).
Multiplicativity of determinant makes j a group homomorphism, and its
first block recovers X, proving injectivity. For this witness L=chi^-4
=chi^2. W=V+L preserves V as a literal invariant direct summand.
It is the smallest determinant-one enlargement if retaining V unchanged
as a full direct summand is required: rank four fails, rank five works.
This is a coefficient-rank statement, not a spacetime dimension or a
selection/uniqueness principle for E8.

Direct-sum additivity of the cochain and restriction maps gives
I(W)=I(V)+I(L). Here I(E)=dim ker(H1(M,E)->H1(T,E)) minus the same
quantity for E dual. This algebraic I is NOT, by definition or without
extra analysis, the physical L2 chiral index on the complete cusp.

## 3. The full candidate E8 roster

The two explicit orthogonal A4 root chains in the design lie in the
E8 lattice. Their product root lattice has index five in E8, checked
against R38's primitive basis and independently by its determinant.
Restricting every root and the eight Cartan directions gives

    248=(24,1)+(1,24)+(10,5)+(bar10,bar5)
                      +(5,bar10)+(bar5,10).

Gauge is the first factor, coefficient/structure group the second.
The center acts trivially exactly on (zeta I5,zeta^-2 I5), zeta^5=1.
Thus the compact subgroup is (SU5 x SU5)/Z5; the individual factors
embed injectively. Complexification permits the flat SL5(C) monodromy;
it is NOT a unitary holonomy assertion. The standard subgroup/global
form is documented in Distler--Sharpe, hep-th/0701244v3, appendix A.
The exact roots and complete joint weight multiset are computed here
to establish the convention and faithful action, not just name it.
No heterotic spacetime or compactification is imported from that paper.

The coefficient for the gauge 10 is W; that for bar5 is exterior-square
W. Their dual coefficients supply the conjugate gauge sectors. The
singlet coefficient is End0(W); the gauge adjoint has the trivial
coefficient. The roster includes every sector of 248 exactly once.

The original four-plus-line split gives

    exterior-square W = exterior-square V + V tensor L,
    exterior-square V = chi^2 (Sym4(rho) + 1),
    End0(W) = End0(V) + 1 + V tensor L^-1 + its dual.

The middle identity is checked by an explicit invertible six-dimensional
intertwiner, not only by matching characters of reducible monodromy.
It is the standard SL2 Clebsch--Gordan identity. In the unnormalized
Sym3 basis, start from e0 wedge e1; its F-lowering chain divided by
4!/(4-j)! gives the Sym4 columns, and the simultaneous E,F kernel
provides the invariant column. All actual generator equations must hold.

## 4. A diagnostic for the proposed physical dictionary

The block-preserving compact U1 generator is T=diag(1,1,1,1,-4).
It commutes with W's monodromy. Under SU5 x U1 the candidate matter
coefficients are V for 10_1, L for 10_-4, exterior-square V for
bar5_2, V L for bar5_-3, and V L^-1 for singlet_5, with conjugates.
For a block-compatible positive background it also commutes with that
background. This does not prove that these are all physical gauge modes.
Even ordinary H0 invariant sections need a positive metric/domain test.

Normalize SU5 cubic A(5)=A(10)=1 and quadratic T(5)=1,T(10)=3.
They are verified as polynomial trace identities on the full Cartan,
including the sign of the conjugate cubic trace. If the stated I's
were left-Weyl multiplicities, then the anomaly coefficients would be

    SU5^3: I(W)-I(exterior-square W),
    SU5^2 U1: 3(I(V)-4I(L))+2I(exterior-square V)-3I(VL),
    gravity^2 U1: 10(I(V)-4I(L))+5(2I(exterior-square V)-3I(VL))
                    +5I(VL^-1),
    U1^3: 10(I(V)-64I(L))+5(8I(exterior-square V)-27I(VL))
                    +125I(VL^-1).

Conjugates are represented by the signed index, not counted twice.
End0(V) and the real adjoint/singlet pieces have zero net index;
their ordinary cohomologies are nevertheless retained explicitly.
Any nonzero expression refutes anomaly cancellation for THIS roster
under THIS dictionary without additional matching contributions.
It does not refute the bundle or every physical realization. A zero
expression only passes this necessary conditional algebraic check.

## 5. Positive metric and source map; the physical obligation survives

Choose a positive Hermitian metric H4 with flat-frame transition rule
H4 -> X^dagger H4 X. Then

    H5=diag(H4,(det H4)^-1)

is positive, has determinant one, and transforms under j(X) as a metric
on W. Such smooth metrics exist by the usual positive-metric patching;
harmonicity is a different equation. For K4=H4^-1 dH4,

    K5=diag(K4,-tr K4),
    divergence K5=diag(divergence K4,-tr divergence K4).

Thus within this block ansatz harmonicity is equivalent, not automatically
solved by the enlargement. The differential of j also sends a connection
to diag(C4,-tr C4); curvature and its real moment residual transform by
the same block map. This follows from trace of a commutator being zero
and preservation of the adjoint by j_* in unitary frames. A prescribed
current J4 maps to diag(J4,-tr J4). It is a candidate-parent current,
not a derived source action or a solution of the source field equations.

For Hermitian tangent fields the defining-five norm is

    tr5 j_*(X)^2 = tr4 X^2 + (tr4 X)^2.

The E8 adjoint trace restricts to 60 tr5, verified on all Cartan
variables. Positivity and finite/infinite norm must be tested in the
actual metric; no indefinite Killing-form cancellation is used.
The F01 finite-energy splitting obstruction still applies to a
smooth complete source-free nonsplit W. F04's rank-four growth bound
transports to metrics in this block ansatz, not to every rank-five
metric by dimension analogy. F02 fixes the ordinary positive-L2 graph
domain only after an actual smooth complete background is specified.

The geometric R39/F05 gap is likewise not automatically a gap for
this nongeometric coefficient. Conversely its nonzero algebraic I
does not imply a zero eigenmode of a physical positive operator.
The next physical computation must solve/justify the source-end
background and calculate the full physical spectrum in that one model.
