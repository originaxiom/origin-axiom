# Combined symmetry of the balanced background and current-density repair

2026-11-09. Personal author hand derivation accompanying the review of
AGY4ff94e619. Source setup is the supplied balanced h4, W=1, eta=O
curved E8 model. Formal independent review and new computational controls
remain open. The previous22-test reproduction covered older finite code.

## An actual global symmetry controls the natural operator algebra

Put H=H_plus+H_minus and P=exp(i pi H/2). All retained E8 principal
grades mu are integers, so Ad_P^2=1. On grade mu,

    Ad_P X=(-1)^mu X.

The flat gauge transitions A,D,h4 commute with H and hence P. The spin-
induced gauge connection also commutes with P. Thus Ad_P is a global
parallel unitary involution on the physical adjoint bundle. The scalar
minus identity is a parallel automorphism of the actual flavour bundleF,
commuting with both quaternion holonomies and preserving epsilon_F and
its Hermitian norm.

Consider their simultaneous action Sigma on fields. On flavour-singlet
gauge vectors, lambda and a, it acts asAd_P. On the flavour doublets
(q,r) and(u,v), it acts as-Ad_P. The balanced q,r have gauge grade+1,
and their compact adjoints have grade-1. Therefore Sigma fixes the full
background, including the connection. The tensor connections, metrics,
trace, bracket and flavour contractions respect Sigma. Gauge covariance
and the existing unitary flavour action consequently preserve the action.

Take a covariant local operator constructed from this background, its
covariant derivatives, curvature and the declared invariant tensor
contractions. Naturality under Sigma at a Sigma-fixed background gives

    Sigma_target L=L Sigma_source.                    (1)

This holds for finite sums and compositions of such operators. The
source/target domains include every tensor index used in forming them.
On flavour-singlet gauge-vector bundles Sigma_source=(-1)^mu. Hence
the component ofL frommu=-2 tomu=-1 obeys

    -L=L, therefore L=0.                             (2)

Equivalently an odd number of q/q-dagger insertions gives odd grade
shift and an odd number of flavour indices. Contraction by the invariant
Hermitian or epsilon tensors removes those indices in pairs. Equation(1)
gives that index argument a global bundle and symmetry meaning.

This proves a restriction on the declared natural-operator algebra at
this background. A profile, reference tensor, sector map or state that
transforms oddly under Sigma must travel with its map and inputs. A
different stationary background can have a different stabilizer. These
are the precise hypotheses for applying(2).

## The Higgs tangent retains the complete tensor type

The old physical dictionary identifies the effective gauge weight bundle
E_mu with S^-mu times its flat coefficient. For the projected Higgs map,

    E_-2 -> S tensor F tensor E_-1.

Its effective target power isS2 F, since the gauge weight changes as
the physical S factor is inserted. In coordinate coefficients,

    (L_phi w)_plus=(sqrt(Omega)/ell)w2 f2,
    (L_phi w)_minus=(sqrt(Omega)/ell)w1 f1.

The output uses spin-slot densityOmega and the input usesOmega^2.
Therefore the projected two-entry map obeys

    ||L_phi w||_spin^2=||w||_gauge^2/ell^2.             (3)

In physical orthonormal frames the corresponding coefficients have
factor1/ell. This is part of the actual gauge tangent intoC1. It obeys
(1), because its target has an extra flavour sign as well as grade-1.
Its tensor and physical-norm accounting explains why it does not supply
the requested flavour-singlet vector map.

Dbar carries a barK factor and D_z a K factor. The effective powers
of their compositions with the Higgs map therefore change by-2 and+2,
respectively, before any additional contractions. Coordinate/orthonormal
conversions must carry their own target metric and derivative connection.

On compact-support cores all of these parallel involutions are smooth
unitary bundle maps and preserve the source differential expressions.
Their boundedness and core intertwining extend to the graph closures
and the vector quadratic-form realization. A proposed derivative
intertwiner still needs its own boundedness and closed-domain argument.

## Correct the normalized lepton/quark comparison

Use the source's normalized coefficient conventions

    z=Omega^-1 chi/sqrt(Iw),
    |d|^2=Omega^-1 |dhat|^2,
    Id=||d||_spin^2=integral |dhat|^2 dxdy,
    IN=(1/2) integral Omega^-1 |chi|^2 dxdy,
    J=integral Omega^-3 |chi_plus chi_minus|^2 dxdy,
    K=integral Omega^-2 |chi|^2 |dhat|^2 dxdy.

Let N1^2=kappa(E_plus dagger E_plus) in the fixed principal normalization.
Let Cq>0 be the common magnitude of the two actual E8 quark bracket
coefficients on orthonormal weight vectors. The known fibre identities
then give

    g_lepton=g6 sqrt(6) sqrt(J)/(N1 sqrt(IN Iw)),
    |gL|=g6 Cq sqrt(K)/(sqrt(2) sqrt(Iw Id)),
    g_lepton/|gL|=2sqrt(3)/(N1 Cq) sqrt(J Id/(IN K)).   (4)

Both products are nonidentically zero under the earlier holomorphic
section and bracket hypotheses, so their integrals and the ratio are
positive. The value of the geometric integrals remains to evaluate.

At fixed marked dimensionless geometry Omega=ell Omegahat, the powers
are IN~ell^-1, J~ell^-3 and K~ell^-2, while Iw and Id have no remaining
ell factor in these holomorphic coefficient conventions. Equation(4)
makes each coupling scale as g6/ell and cancels ell in the ratio.

For kappa rescaled by a positive lambda, orthonormal weight vectors scale
as lambda^-1/2. The components of their Lie brackets scale as lambda^-1/2
as well, so Cq~lambda^-1/2. Fixed principal E,H give N1~lambda^1/2.
Consequently N1 Cq is invariant. Any simultaneous choice of holomorphic
generator normalization must be transported through all five integrals.
No independent action normalization or marked geometry is selected by
this ratio calculation.
