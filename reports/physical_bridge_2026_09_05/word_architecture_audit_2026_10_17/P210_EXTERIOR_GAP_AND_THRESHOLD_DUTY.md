# Exterior gaps and the symmetric state boundary response

October 24, 2026. Authored conditional analysis for P-210, awaiting
independent review. No scientific code or numerical test was run.

A useful next target is the exterior gap, not another rank census.
In the specified constant-tail, grading-preserving model, a uniformly
gapped exterior with three decaying PLUS modes cannot reach a symmetric
Q8 state with its action retained. A threshold, a changed stabilizer,
a changed grading or failure of the proposed tail identification must
account for the transition. This is NOT an obstruction to every physical
completion or a derivation that the actual OA end has this model.

## Recovered source before proposing a mass comparator

The [exterior response](EXTERIOR_RESPONSE_AND_JOINING.md) already derives
the actual same-action transfer equation and shows that an exterior norm
can select a Cauchy plane once its end and remote state are specified.
The [normal Gaussian](../weave_end_gaussian_2026_10_09/PROOF.md) derives
its normal Hamiltonian from the physical kinetic map, retains the Weyl
overlap and shows why a zero overlap cannot be divided away. Neither
is a derivation of a unique global remote state.

The [same-action transmission](../surface_same_action_transmission_2026_10_16/PROOF.md)
keeps all fields, principal directions, momenta, reality and zero
tangential modes. It does not provide a uniform bound at the singular
end. The [root condensate](../weave_cusp_condensate_2026_10_08/PROOF.md)
already provides a nonzero same-action end solution with some lifted
thresholds and retained gapless companion channels. That conditional
positive is not replaced here by an inserted mass or a claim that the
entire theory has a gap. These source bodies were reread, not executed.

The [preceding P-210 classification](SYMMETRIC_STATE_GREEN_RESPONSE_AND_GRADING.md)
classifies boundary planes; this note asks what happens when a specified
exterior actually generates them. It is a different duty from choosing
one of those planes at a finite cut.

## A complete constant-tail control with the correct Green form

Fix outward coordinate t>=0, ordinary measure dt, the positive coefficient
metric and W=C3 tensor C2. Supply a constant Hermitian matrix K on W.
Let the full two-slot operator be

    D_K = -i sigma1 partial_t - sigma2 tensor K
        = [[0, i(-partial_t+K)],
           [-i(partial_t+K), 0]],
    Gamma=diag(I6,-I6).                                  (1)

Identity matrices in the derivative blocks are implicit. Both zero-order
and derivative terms are Hermitian in the formal operator sense, and
Gamma D_K=-D_K Gamma. Integration by parts has boundary matrix sigma1,
up to the common normal factor i, so its Hermitian current is exactly
u dagger v'+v dagger u' from the preceding note. This matches the
SOURCE QUOTIENT FORM, not a claim that (1) has been derived as its full
curved exterior operator. All coordinate, metric and slot maps would
still need to be exhibited before that identification.

At zero energy the equations and their solutions are

    (partial_t+K)u=0,   (-partial_t+K)v=0,
    u(t)=exp(-tK)u0,   v(t)=exp(tK)v0.                   (2)

If K is invertible, square integrability selects uniquely

    L_ext(K)=E_positive(K) in the PLUS slot
             direct-sum E_negative(K) in the MINUS slot. (3)

The two coefficient subspaces are orthogonal complements. Thus (3) is
maximal current-null and Gamma-invariant. Here the end and its L2 norm
really do remove the finite-cut plane freedom. They remain supplied
inputs of this exact control. Different signs of K select different
domains; neither sign has been derived from the principle.

The squared bulk operator is -partial_t^2+K^2. Its far-tail spectral
threshold is min |eigenvalue(K)|^2. Compact cut conditions or core
perturbations can add discrete modes; no absence of those follows from
the tail threshold. This distinction was already present in the source's
normal Gaussian and polar-map arguments.

## The stabilizer constrains a gapped tail, not just a projector

At the stated symmetric state suppose the SAME exterior matrix obeys

    [K_*, I3 tensor i]=[K_*, I3 tensor j]=0.             (4)

As before, the quaternion algebra generates M2(C), so
K_*=A_* tensor I2 with A_* Hermitian on C3. If it is invertible, its
positive eigenspace has dimension 2r for r=0,1,2,3. Consequently the
L2 response (3) has even PLUS rank. If the compact interior is also
the earlier admitted finite-distance ordinary-spin problem, its index
formula would give 2r-3, not zero. That transfer additionally requires
matching the actual operator, metric, frames, interface and domain.
The constant-tail control alone proves no interior physical index.

Let K(s) be a continuous Hermitian family for s>=0, with K(0)=K_*.
If min |eigenvalue(K(s))|>=delta>0 near s=0, the number of positive
eigenvalues is constant. For example, the variational formula for
ordered Hermitian eigenvalues gives

    |lambda_j(K(s))-lambda_j(K(0))|<=||K(s)-K(0)||.

For norm difference below delta/2, no eigenvalue changes sign. Hence
an exterior response with PLUS rank three for s>0 cannot converge to
an invertible K_* satisfying (4). The full response remains subject
to the same rank obstruction, now expressed as a specific spectral duty.

This argument is finite-dimensional constant-tail analysis. Extending
it to a nonconstant or infinite-channel exterior requires the actual
asymptotic operator, a uniform gap and continuity of its decaying-space
or resolvent construction. No such general theorem is asserted merely
from the finite eigenvalue bound. In particular the source's full cusp
and its gapless angular companions cannot be replaced by K(s) alone.

## An exact threshold control retains what elimination would lose

On the source's supplied state space use the Hermitian field
H2(S)=S S dagger-tr(S S dagger)I2/2. A comparator is

    K(S)=I3 tensor H2(S).                              (5)

At S_s=(I2+s n.sigma)^(1/2), with |n|=1 and 0<s<1,
K(S_s)=s I3 tensor n.sigma. Its positive eigenspace is exactly the
earlier rank-three candidate. Its full L2 trace space is (3), including
the three MINUS modes. As s tends to zero the tail gap closes and
both decay lengths diverge as 1/s. The normal matrix at S=I2 is zero.

At K=0 every zero-energy solution of (2) is constant and none is L2
on the half-line unless zero. This does not define a maximal null
six-plane by continuity. Zero has become a continuum threshold, not
an index-zero finite Fredholm sector selected by regularity.

For an explicit approximate-zero sequence let chi be a smooth function
supported in (0,1) with integral |chi|^2=1, and choose a unit constant
spinor xi. On disjoint far-tail intervals define

    f_L(t)=L^(-1/2) chi((t-T_L)/L) xi,
    ||f_L||=1,  ||D_0 f_L||^2=L^(-2) integral |chi'|^2.  (6)

Choose T_L so these intervals escape every compact set. They vanish
near the finite interface, meet every homogeneous local condition
there, and have no convergent norm subsequence. Thus there is no
positive far-tail bound at zero. Deleting these threshold directions
as if the exterior inverse stayed bounded would lose physical spectral
data in this control. This mechanism is not a newly computed particle
spectrum of the programme.

Equally, a supplied K=m I6 with m nonzero is Q8-compatible and selects
one extreme in (3), while -m selects the other. A continuous path from
(5) to either gapped choice changes a hypothesis or crosses an eigenvalue
zero; the source's symmetric coupling -2 I3 is not a derivation of m
or an identification of the required six-component normal mass map.

## What this changes about the next physical calculation

P-210 should ask for the ACTUAL exterior Hessian or radial operator
on the transported fields at and near the stabilizer locus. One must
determine whether it has a gap, which channels reach threshold, what
its L2/remote-state condition is, and whether its Cauchy relation retains
Gamma. The output can be a response relation with threshold modes,
not necessarily an everywhere-invertible response matrix. This is the
positive use of the singularity: it indicates precisely which modes
must be retained rather than forcibly integrated out.

No full E8 spin/gauge map, stationary background, grading law or
exterior state is supplied by (5). A compensating sector, different
geometric end or changing stabilizer can change the problem; the
earlier full-gauge audit preserves those possibilities. The source's
nonzero end solutions and magnetic indices retain their own scope.
Neither this control nor a symmetry argument excludes them.

The next sealed controls can verify (1)--(6), with a wrong Green sign,
wrong decay orientation, omitted MINUS slot, gapped scalar comparison
and the zero-threshold case all retained. They are post-derivation
verification, not evidence that an inserted mass was physically forced.
No scientific execution, independent acceptance, physical-input payment
or closure of P-210 is claimed.
