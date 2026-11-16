# Orthogonal reduction in the actual parallel background

2026-11-16. Author hand proof under P-C3b, scope d2937e15a. Independent
review is pending. No scientific import, CAS, collection or run occurred.
The action, complete metric, bundle and stationary parallel pair are the
existing supplied physical construction.

## 1. Use the exact source differential and metrics

Write B=S tensor F, with its unitary symplectic flavour connection and
det B=K. Put E_k=E tensor wedge^k B for k=0,1,2, where E is the complex
adjoint coefficient or an admitted gauge-representation block. Use its
actual tensor metric and the Dolbeault total complex

    A^(0,l)(E_k), l=0,1.

The source spin metric in a holomorphic frame is |s|^2=Omega^-1. The
determinant metric is Omega^-2. The (0,1) form dbar(z) has squared norm
2 Omega^-2, and dvol=Omega^2 dxdy. These conventions reproduce the
source kinetic densities by the following degreewise isometries J_n.

    J0(epsilon)=epsilon,
    J1(a,u,v)=((a/2)dbar(z),(u,v)),
    J2(p1,p2,t)=((p1,p2)dbar(z)/sqrt(2),sqrt(2)i t),
    J3(sigma)=i sigma dbar(z).                              (1)

The source densities are Omega^2; (1/2,Omega,Omega);
(Omega^-1,Omega^-1,2); and 2 Omega^-2. Substitution in (1) gives these
four metrics term by term. The determinant component carries its K
frame in J2 and J3.

Define the holomorphic algebraic differential by

    delta0 epsilon=-i([q,epsilon],[r,epsilon]),
    delta1(u,v)=i([q,v]-[r,u]).                             (2)

On Dolbeault degree l it acts with sign (-1)^l. Let b=bar(partial)
be the actual tensor Dolbeault differential, with coefficient Dbar/2.
The total differential is d=b+delta_signed.

The source physical-complex maps obey exactly

    J_(n+1) D_n=sqrt(2) d_n J_n.                           (3)

For D0 this gives sqrt(2)(bar(partial)epsilon,delta0 epsilon).
For D1 it gives ((p1,p2)dbar(z)/sqrt(2),sqrt(2)i t), with the old
p1,p2 and t. For D2 the two contributions sum to

    (i/sqrt(2))(Dbar t-[q,p2]+[r,p1])dbar(z).

Multiplication by sqrt(2) gives J3 D2. Thus the signs, the factor two
in the last residual metric and the C3 normalization all enter (3).

## 2. Parallelness fixes the mixed adjoint terms

The balanced source pair in orthonormal spin frames is

    Phihat0=(E_++E_-, E_+-E_-)/(2sqrt(2)ell),
    A_spin=s_connection H/2.

Both raising sections have H/2 weight one. Their spin connection
+i s_connection and gauge connection -i ad(A_spin) cancel. The flat
flavour and gauge transitions preserve their pair by the source joint
gluing equation. Consequently

    nabla Phihat0=0

as an actual B-valued adjoint tensor. The bracket and epsilon pairing
are parallel, so nabla delta=0 in (2). Metric compatibility gives
nabla delta^dagger=0 as well.

The Dolbeault signs imply, on compact-support cores,

    b delta_signed^dagger+delta_signed^dagger b=0,
    b^dagger delta_signed+delta_signed b^dagger=0.

For example, on l=0 the first expression is the covariant derivative
of delta^dagger. On l=1 the second is the corresponding metric-adjoint
identity. Parallelness makes them zero. Hence the exact Laplacian is

    (d+d^dagger)^2=Delta_b+Delta_delta,                     (4)
    Delta_delta=delta delta^dagger+delta^dagger delta.

Every term on the right is nonnegative in the declared metric.
Equation (4) uses the parallel background. A nonparallel Higgs section
introduces its covariant derivative in the mixed anticommutators.

## 3. A global orthogonal projection with its domain map

Let P_delta be the orthogonal fibre projection onto ker Delta_delta
in each E_k. Parallelness makes its rank constant and makes P_delta
parallel. It is invariant under the actual combined flat transitions.
Therefore it commutes with b,b^dagger,delta and delta^dagger. It maps
compact-support cores to themselves and is bounded with norm one.

These statements extend to the complete first-order graph closures.
They give a reducing orthogonal sum for the complete doubled operator.
The source's physical mass map is unitarily related to its odd-to-even
Hodge map by its already exhibited physical maps. Combining those maps
with (1)-(3) gives isometries I_in,I_out with

    I_out M=sqrt(2)(d+d^dagger)|odd I_in.                   (5)

The physical source and target projections are obtained from P_delta
through these two isometries. The complete domains, adjoints and norms
are retained in (5).

On the orthogonal complement of P_delta, let c_delta be the smallest
positive eigenvalue of the finite fibre matrix Delta_delta. It is
positive and constant on this fixed parallel background. Equations
(4)-(5) imply the actual full-field estimate

    ||M x||^2>=2 c_delta ||x||^2                           (6)

on that complementary source domain. The adjoint has the same bound
on the complementary target. Closed range and the adjoint-kernel test
then give a bounded inverse between these complementary spaces, into
the actual graph domain.

This complement is the algebraically contractible part of the full
operator. The retained harmonic-bundle operator is exactly the tensor
Dolbeault Hodge operator. A zero-angular continuum in that retained
part remains. The old whole-parent centralizer continuum is preserved.

There is no uniform bound asserted as a background is varied through
a rank-changing endpoint. The positive constant in (6) belongs to the
stated fixed parallel pair.

## 4. Apply the reduction to the entire half-root block

For V_j tensor V_l with j=l=3/2, the fibre harmonic lines are

    degree 0: |j,j>,
    degree 1: e_+ tensor |-j,j>, e_- tensor |j,-j>,
    degree 2: e_+ wedge e_- tensor |-j,-j>.                (7)

The middle assertion follows directly from a positive norm identity.
In the unitary raising-field basis, its two conditions are

    E_+ v-E_- u=0,
    E_+^dagger u+E_-^dagger v=0.

Because the two triples commute with each other's adjoints,

    ||E_+ v-E_- u||^2+||E_+^dagger u+E_-^dagger v||^2
      =||E_- u||^2+||E_+^dagger u||^2
        +||E_+ v||^2+||E_-^dagger v||^2.                 (8)

Thus u lies on the first mixed-extreme line and v on the second.
Degree zero is the common raising kernel; degree two the common
lowering kernel. Their actual bundles are S^-3 L_top, two S-valued
middle lines and S^5 L_bottom. The old full cohomology action on (7)
is retained, with its alpha character and central core signs.

All these reduced lines are antiperiodic in their complete cusp frames.
Their nonzero angular frequencies give the diverging quadratic angular
term after unitary radial rescaling. The remaining connection/drift
terms have lower order. The usual tail estimate and compact-interior
ellipticity give compact resolvent on each such line Hodge block.
This is the complete operator on that line with its inherited domain.

Together with (6), this proves closed range and finite kernels on the
full half-root block. On the retained lines, restriction away from the
finite kernel has a positive spectral gap for each fixed surface.
Combining their inverse with (6) gives the full charged-block inverse
off its actual kernel and adjoint kernel. Its numerical norm and
nonzero eigenvalues have not been calculated.

For colour singlets of charge magnitude one in this source roster,
the other integer-root representations carry different U3 charges.
The above inverse therefore covers the full stated charged block.
The neutral and other charged blocks retain their own continua and
inverse conditions.

## 5. Relation to the older reduction

The source already supplies a bounded Koszul retraction and its kernel
counts. Equations (1)-(8) give a separate orthogonal route in this
parallel background, with explicit source constants and actual graph
domains. They remove reliance on an unspecified choice of homotopy
when defining the harmonic projection used below.

The companion direct-kernel proof gives the charged representatives
and counts. The state-orbit proof then constructs its invariant
spin-mode inclusion. Both charged conjugates and all omitted
complementary fields remain part of the physical operator.

Independent review must check (1)-(4), parallelness in the actual
tensor metrics, complete-domain extension and the line end estimate.
No finite matrix pass has been substituted for those analytic duties.
The source parent and physical identification hypotheses retain their
input status.
