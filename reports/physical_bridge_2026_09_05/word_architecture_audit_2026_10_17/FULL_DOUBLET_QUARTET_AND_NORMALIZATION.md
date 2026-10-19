# The full doublet and quadruplet: maps and metric freedom

October 19, 2026. Analytical continuation of the owner's quadruplet
clarification. The preceding clarification turns fixed terminology but
were not new research results. This note derives an actual sector
calculation in the existing local module. No scientific producer or
mathematical test is run. Separate review and experimental admission
remain outstanding.

## Same six-dimensional object, both sectors retained

Use the fixed frame in [the theta repair](THETA_SEQUENCE_REPAIR_AND_MONODROMY_DUTY.md).
The local module W=C3 tensor C2 carries O_g tensor g on the entire
registered group E. Let Q_p=(j,i,k), with the existing quaternion
matrices, and use the standard Hermitian forms for this algebraic
calculation. These are not a derived physical kinetic metric.

The [coherent local proof](COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md)
already establishes two inequivalent irreducible summands, dimensions
two and four. We retain BOTH. They are not the cohomology triplets,
not two/four real components, and not identified spacetime particles.

## Projectors from the actual coefficient algebra

Define K:W->C2 by

    K(sum_p e_p tensor u_p)=sum_p Q_p u_p.

Since Q(O_g x)=g Q(x) g^-1, this intertwines O_g tensor g with g.
The identities Q_p^dagger=-Q_p and Q_p^2=-I give

    K^dagger v=sum_p e_p tensor (-Q_p v),
    K K^dagger=3 I2,
    P2=K^dagger K/3, P4=I6-P2.                    (1)

These are orthogonal equivariant projectors of ranks two and four;
W4=ker K. The (p,q) block of P2 is -Q_p Q_q/3, precisely the
source's C^-1(ones3/3 tensor I2)C formula. No new grading is added.

## Where the theta map goes

For any nonzero doublet v let I_v(x)=x tensor v and B_v x=Q(x)v.
This includes the preceding theta field and any nonzero local value
of its branched fibre candidate. With v=(u,w),

    K I_v=B_v=[[w,i u,i w],[-u,-i w,i u]],
    G2=I_v^dagger P2 I_v=B_v^dagger B_v/3,
    G4=I_v^dagger P4 I_v=||v||^2 I3-G2.           (2)

For any 2-by-2 matrix A, multiplication of the explicit quaternions
gives sum_p Q_p A Q_p^dagger=2 tr(A)I2-A. Applying this to v v^dagger,

    B_v B_v^dagger=2||v||^2 I2-v v^dagger.

Its eigenvalues are ||v||^2 and 2||v||^2, proving rank B_v=2.
Thus, as multisets,

    Spec(G2)=||v||^2 {0,1/3,2/3},
    Spec(G4)=||v||^2 {1,2/3,1/3}.                (3)

These exact consequences hold for every nonzero v, not a tau sample:

- P2 I_v has rank two; P4 I_v has rank three and is injective.
- im(I_v) intersects W4 in a line, since ker B_v has dimension one.
  It intersects W2 in zero, since G4 is positive definite.
- Every x obeys ||P4 I_v x||^2 >= ||v||^2 ||x||^2/3.
  Moving v cannot remove its quartet contribution in this norm.

Projection ranks are not particle or generation counts. Nor does this
select a boundary domain. If its rank-three image were legitimately
used as Lambda in the source's conditional n(dim Lambda-3), that
formula would give zero, not three. The identification itself is unpaid.

## A nonzero quadruplet constructed from the doublet

The pure-W4 line has a constructive generator. With epsilon=j, set

    ell_p(v)=v^T epsilon Q_p v,
    ell(v)=(-u^2-w^2,-2 i u w,i(u^2-w^2)),        (4)
    Psi(v)=ell(v) tensor v.

Substitution gives Q(ell(v))v=0 and ell^T ell=0. But ell is
nonzero for every v!=0: its vanishing would require u w=0 and
u^2+w^2=0. Hence Psi(v) is a nonzero W4 element, cubic in v,
with no independently chosen direction. It does NOT recover four
arbitrary independent field components from only two components.

The identity g^T epsilon g=epsilon proves

    ell(g v)=O_g ell(v),
    Psi(g v)=(O_g tensor g) Psi(v).               (5)

For a field with v'=a(e,x)g v, therefore,

    Psi(v')=a(e,x)^3 (O_g tensor g) Psi(v).       (6)

All scalar automorphy and branch factors must be cubed, not dropped.
The restricted theta field has a=j_e mu(e), giving factor j_e^3 mu(e)^3
on W4. This defines a nonvanishing holomorphic section on that
restricted quotient. For the branched fibre doublet the puncture
sign -1 remains -1 after cubing, matching local W4 rather than
the cohomology triplets' +1 commutator action.

The construction spans W4 as v varies. At v=(1,t), the coefficients
of 1,t,t^2,t^3 in its six coordinates are independent: coordinate
three isolates t, coordinate four isolates t^2, and the remaining
constant and t^3 coefficients have disjoint nonzero supports.
The induced linear map Sym^3(C2)->W4 is thus an isomorphism.
By the source's established W4 irreducibility and Schur's lemma,
this equivariant homogeneous holomorphic cubic map is unique up
to one scalar. That scalar and any physical field or action
coupling remain unselected. No spacetime spin-3/2 particle is inferred.

This constrains an allowed map; it does not force the theory to
include that field or vertex. Conjugate-dependent maps and additional
coefficients have other domains and are not excluded by this uniqueness.

## What symmetry does and does not fix about normalization

Inequivalence and irreducibility imply every CONSTANT invariant
Hermitian form on this W has matrix

    H=h2 P2+h4 P4, h2>0,h4>0.                   (7)

There are two coefficients: a relative ratio and an overall scale.
The scale is not declared physically redundant; its effect on
normalized interactions must be tracked before removing it from
a physical input count. Symmetry does not fix h2/h4.
State-dependent covariant forms, integrated harmonic-profile Grams
and physical boundary metrics need not belong to this constant class.
Those conditions must be derived before (7) prices a physical input.

Pulling (7) back through the SAME I_v gives

    G_H=h4 ||v||^2 I3+(h2-h4)G2,
    Spec(G_H)=||v||^2 {
              h4, (h2+2h4)/3, (2h2+h4)/3 }.       (8)

These three values are in arithmetic progression, in increasing
or decreasing order. Their shape depends on h2/h4, not the
direction of v; ||v|| supplies a common scale. At h2=h4 they
coincide. As h4/h2 tends to zero the Gram becomes ill-conditioned;
positivity alone supplies no uniform lower bound on that ratio.

Thus theta direction alone cannot produce arbitrary three-eigenvalue
kinetic hierarchies in this restricted class. The relative metric
remains explicit. These are not fermion-mass predictions: the actual
interaction tensor and all kinetic slots are still required, as in
[the normalization analysis](KINETIC_NORMALIZATION_AND_WEIGHT_THREE.md).

## Status under the input-reduction mission

- Forced conditional on the given module and algebraic metric:
  projectors, projection ranks/bounds and the cubic covariance above.
  The homogeneous equivariant cubic is unique up to scale.
- Allowed, not forced physical content: a W4 field/vertex built
  this way, and constant invariant metrics (7).
- Excluded in that stated class: dropping W4 from I_v, calling
  its image a pure doublet, or obtaining arbitrary Gram eigenvalue
  ratios by moving v alone in (8).
- Undetermined: physical realization, normalization and h2/h4,
  full fibre-field modular/branch transport, actual puncture
  evaluation/domain and a compatible variational action.

No complete physical-input row is paid. This derives a constraint
and a positive map, not a preferred root, forced boundary condition
or Standard Model. Frozen v2/v3 remain unchanged. An admitted
successor should test the identities, both sector projections,
two-sided metric/rank controls and cubic covariance in actual source
frames. None of those new scientific controls was executed here.
