# Smooth compact gluing curve and its horizontal kinetic tangent

Authored conditional proof frozen before execution. R85 compact
admission, R86 family, R87 parent type and the declared finite checks
are premises. Independent analytic review remains owed. Standard
compact elliptic estimates, Hodge theory and the smooth Banach implicit
function theorem are external mathematical tools, not machine-certified
results of the producer.

## One fixed bundle and determinant

At either positive real field embedding let rho_s be the actual joined
representation with t=exp(s). The diagonal Gamma action on
universal-cover(Y) times I times C5 uses rho_s on the fibre. It is free
and proper because its action on universal-cover(Y) is free and proper;
no freeness or properness of rho_s on SL5/SU5 is needed. Its quotient
is a smooth vector bundle over compact Y times a small interval I,
with smooth flat slice connections and a parallel determinant volume.

Choose an interval-direction connection preserving that volume and
use parallel transport to identify the slices with E0. Such a connection
exists by local determinant-one frames and partition of unity. Thus
D_s is a smooth family on ONE bundle, D_0=A+Psi, and
c=partial_s D_s|0 is a smooth trace-free one-form with d_D c=0.
Different volume-preserving identifications change c by d_D of a
zero-form; they do not change its flat cohomology class or loop detector.
There is no noncompact tail or asymptotic domain to borrow from R53.

## The actual Jacobi operator is invertible in the structure sector

Fix the R85 positive harmonic metric H0, determinant one. Write any
variation u=a+phi with a compact/skew and phi Hermitian. With orthonormal
base indices, moment and compact-gauge linearizations are

    M(u)=delta_A phi+sum_i[Psi_i,a_i],
    G(u)=delta_A a+sum_i[Psi_i,phi_i].

The sum is the full variation of delta_A Psi; it is not just an ordinary
divergence. At mu=delta_A Psi=0 the zero-form operator is

    J=d_D dagger d_D=delta_A d_A+sum_i ad(Psi_i)^2.

Indeed delta_A[Psi,eta]+sum[Psi_i,nabla_A,i eta]=[mu,eta]; this
remainder vanishes here and not at a nonharmonic background. J preserves
the Hermitian and compact trace-free real subbundles. In particular
M(d_D eta)=J eta and G(d_D eta)=0 for Hermitian eta; the two identities
are exchanged for compact eta. The sign gives positive energy

    <eta,J eta>=||d_A eta||2^2+sum||[Psi_i,eta]||2^2.

On compact closed Y, J is self-adjoint elliptic. Its kernel is the
space of parallel End0(E) sections: zero energy forces both terms
zero, hence d_D eta=0. Full Mat5 holonomy makes any parallel endomorphism
scalar; trace-free scalars vanish in characteristic zero. This uses the
actual full algebra, not Schur's converse for a nonsplit piece. Thus J
has positive first eigenvalue and is an isomorphism C^{k+2,beta}->
C^{k,beta} on trace-free Hermitian sections, for k>=0,0<beta<1, by
compact elliptic Fredholm theory and regularity. No gap value is computed.

This is NOT an inverse on the whole E8 adjoint. The gauge su5 factor
has parallel zero-forms. We only invert the structure End0 summand.

## The harmonic family follows from the implicit equation

For a small trace-free H0-Hermitian xi put B=exp(xi), and transform
D_s into the fixed H0 frame as B D_s B^-1. Its connection difference
contains -(d_D B)B^-1. Split it by the FIXED H0 and denote its moment
by F(s,xi). This is a smooth second-order nonlinear map between the
compact Holder spaces above, with F(0,0)=0 and

    partial_xi F(0,0)=-J,   partial_s F(0,0)=M(c).

The exponential, inverse, products, derivatives and adjoints are smooth
in these Banach charts, so the implicit function theorem yields a local
smooth xi(s), xi(0)=0, with F(s,xi(s))=0. Spatial elliptic bootstrapping
and parameter differentiation give smooth spatial fields and smooth
parameter derivatives; no real analytic base metric is asserted.
B(s) is a genuine smooth positive determinant-one bundle map.

These are the actual D_s representations, with positive harmonic fibre
metrics H_s=B(s) dagger H0 B(s), not a formal jet or an assumed smooth
selection among the existence theorem's solutions. Flatness is preserved,
so both residuals vanish exactly along this local curve and the SAME
bare V=0. Slegers' Theorem2.8 is not invoked: its target quotient and
uniform-free/proper hypotheses remain unverified. Its compact
Proposition3.3 method is adapted to bundle sections by the fixed-bundle
construction and direct Jacobi calculation here.

## The earned velocity and full parent gauge redundancy

Differentiating the implicit equation gives xi'(0)=J^-1 M(c). The
transported curve has v=c-d_D J^-1 M(c), so M(v)=0. Put
kappa=J^-1 G(c), compact. Actual unitary maps exp(s kappa) remove its
compact longitudinal derivative. The resulting velocity is

    alpha=c-d_D J^-1 d_D dagger c,
    d_D alpha=0, d_D dagger alpha=0.

J preserves the two real parities, so the combined formula includes
exactly the metric relaxation and compact gauge terms, without an
extra factor of two. Compact smoothness gives finite norms for the
curve and all these first derivatives; there is no strong-domain
infinity problem. Hodge projection also shows independence from the
chosen smooth slice identification. It is horizontal at the center,
not an asserted nonlinear global Coulomb slice.

The actual mixed loop's parent character has nonzero derivative

    partial_s chi248|0=-5[P1+2P2],  X=exp(-5s).

Finite checks rederive this from the literal right bend and all joined
relators. An exact d_D zero-form tangent gives infinitesimal conjugation
on every based holonomy, annihilated by a representation trace. Thus
alpha cannot be zero. More strongly it cannot be removed by a full E8
gauge tangent. The orthogonal R40 branching is preserved by D and its
positive adjoint, so a structure harmonic alpha is orthogonal to d_D
of a zero-form in every complementary summand as well. The genuine
parent character derivative independently excludes a full-parent pure
gauge interpretation. Neither argument inverts the parent zero modes.

## Quadratic kinetics in the supplied theory

Use the same supplied twisted gauge action and the positive parent
trace as R47/R53/R76. Its mixed scalar kinetic coefficient is1/g7^2.
The actual E8 trace restricts to60 times defining-five trace, checked
on the complete rank-four Cartan Gram and extended by invariant forms.
At the center the horizontal real amplitude s therefore has

    K0=(60/g7^2) integral_Y tr5(alpha dagger wedge *alpha),
    Lkin,quadratic=-K0 partial_mu s partial^mu s,
    0<K0<infinity.

The positive norm is finite by compact smoothness and strictly positive
because alpha is nonzero. Compact horizontality solves the linearized
Gauss constraint; no longitudinal norm is counted. The real canonical
infinitesimal coordinate is sqrt(2K0)s in the -1/2 gradient convention.
The source-free static potential stays identically zero nearby, so
there is no classical potential mass along this curve in this model.

This is a local collective-coordinate statement, not a proof of a
consistent nonlinear truncation to one four-dimensional field. K0,
the gap and their scales are not numerically computed or predicted;
g7 and the internal metric are supplied. The coordinate is a gauge
singlet in the retained su5 dictionary, not an identified SM Higgs.
Quantum corrections, other-field instabilities and gravity are not
computed. No vacuum/level/join selection, net Weyl chirality, generations,
normalized Yukawas, physical observer or qualia are derived. R85 charged
pairing and su5 remain; full parameter-free SM/TOE remains unachieved.

Primary-source method comparison: Slegers, Equivariant harmonic maps
depend real analytically on the representation, version of record,
Theorem2.8 and Proposition3.3, https://doi.org/10.1007/s00229-021-01345-z.
The whole paper was personally read. The fixed-bundle smooth adaptation
and its hypothesis verification above are authored work, not that
paper's certified application or nonauthor acceptance.
