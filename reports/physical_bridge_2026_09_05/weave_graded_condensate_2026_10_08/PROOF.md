# A global matched-grading background and its coupled operator

Authored conditional proof to accompany exact finite checks. The fixed
curvature metric, compact E8 action and domain are supplied, as in the
preceding curved/global packets. A spectral threshold in these units
does not derive a physical mass scale.

## The compact triple and global bundle

Use the previous Euclidean E8 roots of norm squared2. Put
beta=e4+e6, gamma=-e5-e6, v=beta+gamma=e4-e5. Their inner product is-1,
so they generate a regular A2 root subalgebra. Its root generators may
be chosen as E12,E23 in sl3, with compact adjoint transpose-conjugation.
Set E=sqrt(2)(E12+E23), F=E dagger, H=2(H_beta+H_gamma).
Then [H,E]=2E and [E,F]=H. The map sends H to2v, faithfully embeds
this A2 algebra in E8, and commutes with the previously specified color
roots e1-e2,e2-e3. It does not preserve the old weak algebra as a whole.

The earlier four-root proposal is also a valid compact triple with H=2v:
e4+e6,e4-e6,-e5+e7,-e5-e7 are mutually orthogonal roots; their pairwise
sums/differences are not roots. Summing their root triples gives the
stated brackets. Equal H does not, by itself, prove the two triples
conjugate. All centralizer and global dual-map claims below use the
explicit A2 construction.

Since v is an integral E8 cocharacter, exp(2*pi*i*v)=1. The integrated
sl2's central element exp(i*pi*H) is therefore trivial: its compact image
is SO3, not a faithful SU2. In the3, v=diag(1,0,-1). Let S be any of
the four extending spin lines, S^2=K, with unitary connection d+i s and
ds=-dvol/2. Induce the E8 bundle directly from S by the cocharacter v.
A=s v and qhat=E/2 descend: E has v weight1, so the spin connection
and gauge connection cancel in the covariant derivative of qhat.
No square root of S or compensating flat connection has been inserted.

F/dvol=-v/2=-H/4 and [qhat,qhat dagger]=H/4. Thus all vacuum residuals
Dbar q,Dbar r,[q,r],mu vanish globally with r=0, in the SAME action.
In the cusp this is A_x=-H/(4y),q=E/(2sqrt(y)). The positive-x cusp
circle is opposite the compact-core boundary. Its gauge holonomy is
exp(i*v*Area(core)/2), tending to exp(i*pi*v)=p since Area=2pi.
Spin holonomy tends to-1. Flat Z2 changes of S on the two core cycles
do not change that commutator holonomy.

The norm of q is n*pi/2, n=Tr(FE)>0, with n four times a unit root's
trace norm. Expanded densities balance n/16+n/16-n/8. All derivatives
and commutator norms at the end are finite; cutoff tails tend to zero
in the previous graph class. The core is smooth. The squared-residual
potential is zero, its first variation zero, and its complete bosonic
Hessian nonnegative. No equation for a dynamical metric has been solved.

## The complete surviving algebra

The H spectrum on248 has multiplicities1,56,134,56,1 at-4,-2,0,2,4.
Successive highest-weight subtraction gives78 V0+55 V1+V2 (Vj has
dimension2j+1). Thus the compact sl2 commutant has dimension78.

The roots orthogonal to beta and gamma are72 roots of norm2, rank6,
closed under root reflections. Their explicit simple-root Cartan graph
has three arms of lengths1,2,2; it is the E6 root system. These root
spaces and six Cartans commute with the WHOLE A2, so they already
saturate the sl2 commutant. The connected surviving algebra is therefore
compact e6, not inferred merely from dimension78. Curvature forces a
parallel gauge generator to commute with H; the condensate and compact
reality also force commutation with E and F, giving precisely this algebra.

Project every E8 root into A2 and its orthogonal complement. The A2
adjoint and orthogonal adjoint occupy8+78. Each of the three defining
A2 weights occurs27 times, and their negatives occur27 times. Their
orthogonal projections form a single27-element E6 Weyl orbit and its
distinct negative orbit. These establish the complex conjugate sectors:
248=(78,1)+(1,8)+(27,3)+(bar27,bar3).
All gauges/charged spaces here refer to this actual embedding, not
the earlier flat quaternion roster. The E6 gauge norm is positive and
finite because its generators are parallel and the surface area is finite.

## Deriving the full fermion blocks from the parent

The curved packet fixes chiral metrics(1/2,Omega,Omega) for(A,q,r),
gauge metric Omega^2, and W=(1/2)integral(q Dbar r-r Dbar q).
The normalized gauge Killing map is sqrt(2) times the infinitesimal
gauge action, with these metrics. Its adjoint gives the gaugino coupling;
the W Hessian gives the other half. No Yukawa is dropped.

On a zero-angular end channel put t=log y. The canonical radial fields
are lambda=sqrt(y)*u_lambda, delta A=sqrt(2/y)*u_A,
delta q=u_Q, delta r=u_R. Each has measure dt (constant circle/trace
factors suppressed). These rescalings come from dxdy=y dxdt and the
four stated kinetic weights, not a choice made to tune a gap.

In a spinj module let H weight be2m and
e_m=sqrt((j-m)(j+m+1)). The gauge map sends lambda_m to(A_m,Q_(m+1)):
after harmless constant unitary phase changes,

    D1=(D_m,-k_m),  D_m=d/dt+(m+1)/2,  k_m=e_m/sqrt(2).

Indeed sqrt(y) Dbar(sqrt(y)u_lambda) gives iD_m u_lambda;
sqrt(2)[epsilon,q0] gives the raising coefficient-k_m. The
linearized holomorphic equation gives D2=(k_m,D_m) on(A_m,Q_(m+1)).
It obeys D2 D1=0 because the background solves Dbar q0=0.
The coefficient k_m is also obtained directly from the cubic W:
y*q0*delta A has coefficient1/sqrt(2). Thus the Hessian and gauge
normalizations agree independently.

The invariant trace pairs R at weight -m-1 with the target Q at m+1.
It is NOT permissible to label that R slot by m+1. Converting the
R field to the dual Hilbert slot and using the trace metric gives
the complete first-order singular-value block

    B_m=(D1,D2 dagger)=[[D_m,k_m],[-k_m,D_m dagger]],
    D_m dagger=-d/dt+(m+1)/2.

The self-adjoint fermion realization is the off-diagonal operator
with B and B dagger. Rephasing fields or dualizing the trace slot does
not remove a Weyl species. The physical left roster still contains
lambda,A,Q,R with the right fields their Hermitian conjugates.
In Fourier radial variable xi,

    B_m dagger B_m =
      (xi^2+(m+1)^2/4+(j-m)(j+m+1)/2) I_2.

The R diagonal equals the earlier scalar Hessian threshold evaluated
at R weight -m-1. This is a same-action check against an independently
derived block. At the extreme weights, keep the existing one-dimensional
block when the other slot is absent; its threshold is(m+1)^2/4.
The gaugino is a physical fermion, not a Faddeev-Popov ghost. Bosonic
gauge directions are treated by the corresponding elliptic gauge
condition, not deleted matter fields. The fermion calculation needs
no artificial gauge-quotient deletion of lambda.

Since p=(-1)^m, scalar/connection zero-angular slots require m even;
spin slots require m odd because bounding spin contributes-1. On V0
the singular threshold list is[1/4]; on V1 it is[1/4,5/4,5/4];
on V2 it is[9/4,9/4,9/4,13/4,13/4]. Combining the exact248
decomposition gives 1/4:133,5/4:110,9/4:3,13/4:2.
There are496 original left-field angular slots arranged in248 paired
singular channels. Neither population is a particle/generation count.

## From the end calculation to the global essential spectrum

For nonzero angular frequency nu, each diagonal derivative has a term
nu*exp(t). Squaring gives nu^2*exp(2t) plus at most linear exp(t)
terms with bounded matrices and constants. Periodic/antiperiodic
frequencies have |nu|>=1/2 off the zero sector. The quadratic term
uniformly dominates, so this part has compact resolvent at the end;
its eigenvalues also go to infinity with |nu|. It does not add a
low essential branch hidden in an infinite angular sum.

The zero-angular squared blocks are constant-coefficient half-line
Schrodinger operators. Dirichlet cutting at a finite t yields the
intervals[mu^2,infinity); normalized cutoff plane waves produce the
inclusion, and the norm-square identity supplies the lower bound.
Our explicit polynomial test of the endpoint Rayleigh sequence has
excess10/L^2; it is a FORM quotient, not an operator-residual norm.

The full operator is elliptic of Dirac type on a complete surface,
with a smooth unitary connection and bounded Higgs endomorphism.
Exhausting cutoffs with gradient tending to zero give essential
self-adjointness: a deficiency vector's integration-by-parts identity
bounds its norm by the cutoff commutator and makes it zero. Local
elliptic estimates hold on compact sets. Its square is Laplace type.
One can therefore cut the square with Dirichlet boundary conditions
and use the decomposition principle of Baer, section2 Proposition1,
https://arxiv.org/pdf/math/0010233, pp9-13. This source supports
compact-core invariance under these hypotheses; it does not supply
our mass matrices or physical interpretation.

Consequently the squared full fermion essential spectrum is
[1/4,infinity) in the supplied curvature units. The first-order
operator has an essential gap(-1/2,1/2), and its zero kernel is finite
and isolated; it is Fredholm at zero. This does NOT claim that there
are no discrete eigenvalues or zero modes in that interval, nor
compute their multiplicities. The actual elliptic operator and its
domain, not a flat sheaf Euler characteristic, now define the finite
low-energy question. The old single-root background's54 odd commuting
directions still have free channels; the new H grading has no odd
spin0 spectators. The two conclusions concern different backgrounds.

## A charged pairing that survives this nonflat condensate

In the defining3 put J=anti-diag(1,-1,1). It is unitary, invertible
and symmetric; for T=H,E,F it satisfies J T=-T^T J. It also
intertwines diag(z,1,z^-1) with its inverse transpose, so it descends
through every spin-induced gauge transition, including the core
cycles and p. It is a COMPLEX-LINEAR internal map from3 to dual3,
not a claim that the E6 representation27 is itself self-dual.

The E6-charged sectors have exactly those two coefficient systems.
Tensor J with the same scalar, form or spin line in each of the
four Weyl slots. It intertwines their covariant derivatives, E/F
Yukawas, kinetic metrics and adjoints, globally on this background.
It maps compactly supported smooth sections onto each other, is
unitary in L2, and therefore maps their graph closures and kernels.
Thus each left-handed27 zero sector and its bar27 counterpart have
equal multiplicities. No global multiplicity has been guessed.
The adjoint78 and singlet gauge sectors are self-conjugate.
This particular isolated charged spectrum is vector-like.

This is not an all-SU3 theorem: for an explicit generator outside
the principal SO3, J T+T^T J is nonzero. Additional holonomy or
non-SO3 fields, sources or different domains require fresh checks.
A mirror orientation not being gauge-equivalent, even if later
established, would not override the charged operator intertwiner.
The comparison of oriented geometries is not performed here.

All four extending spin lines admit the construction and the same
end threshold; their flat signs have trivial peripheral commutator,
and J respects their induced transitions. This does not show that
their global discrete kernels are equal or select the odd spin line
against the three even ones. Supplied action, metric, scale and
condensate choice remain explicit. No full SM/TOE, observer or qualia
identification is earned by the admitted E6 phase.
