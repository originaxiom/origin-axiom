# F01 authored argument: the missing balance is global

Pre-execution proof candidate, 2026-09-20. Expected calculations disclosed in
DESIGN.md. No novelty claim. Computational disposition belongs in FINDINGS.md.

## 1. Finite-energy harmonic metrics force complete reducibility

Let (M,g) be connected, complete, finite volume and without boundary. Let
(E,D) be a smooth complex flat bundle of finite rank n with a smooth positive
Hermitian metric h. Write D=A+Psi, where A preserves h and Psi is self-adjoint.
Assume d_A^*Psi=0 and integral_M |Psi|^2 < infinity.

Take any D-invariant proper nonzero subbundle S, rank r, and its h-orthogonal
complement Q, rank s=n-r. In local h-orthonormal frames adapted to S and Q,

    D = [[D_S, eta], [0, D_Q]],
    A = [[A_S, eta/2], [-eta^*/2, A_Q]],
    Psi = [[Psi_S, eta/2], [eta^*/2, Psi_Q]].

Here eta is a Hom(Q,S)-valued one-form. The original invariant subbundle need
not have had an invariant complement; proving eta=0 is the point. Set

    xi = s Id_S - r Id_Q.

This is a globally smooth self-adjoint trace-free section with constant norm
|xi|^2=rsn. Its covariant derivative obeys, pointwise,

    <Psi,d_A xi> = -(n/2)|eta|^2.                         (1)

This follows by block multiplication: only the off-diagonal blocks contribute.
In particular |eta|^2 <= 2|Psi|^2 and is integrable. Diagonal connection parts
need not themselves be unitary or vanish.

Use compactly supported Lipschitz cutoffs chi_R, equal to one on B_R,
zero outside B_2R, 0<=chi_R<=1 and |d chi_R|<=C/R. Completeness supplies these
via distance cutoffs (smooth approximation, or their Sobolev weak form).
The harmonic equation, tested against chi_R xi, gives

    (n/2) integral chi_R |eta|^2
      = integral <Psi, (d chi_R) xi>.                    (2)

There is no boundary term because the test section is compactly supported.
The right hand side in absolute value is at most

    sqrt(rsn) ||Psi||_2 (C/R) sqrt(Vol(M)),

which tends to zero. Dominated convergence on the left proves eta=0.
Thus S's orthogonal complement is D-invariant. Applying this argument to
every invariant subbundle proves that the monodromy representation is
completely reducible.

No compactness, Kahler structure, cusped asymptotic expansion, or L2 bound
on xi itself beyond the finite-volume consequence was smuggled in. No
boundedness of the metric h in an unrelated reference frame is assumed.
If the base has a physical boundary, the harmonic equation has a source,
the metric is singular, or the energy is not finite, (2) is no longer this
argument: its new terms have to be computed.

**Application is to a flat-bundle harmonic-metric equation**, not a universal
statement about every gauge-Higgs theory. A larger coupled parent may induce
an equation with additional terms on a subsystem; it must exhibit those terms.

## 2. The exact positive witness fails that specific admissibility condition

R27 already supplies the following algebra. For u^2-u+1=0 and
P=[[1,0],[u,1]], simultaneous conjugation gives

    A'=[[u,1],[0,1-u]], B'=[[-1,u^2],[0,-1]].

B' is a nonscalar Jordan block, while the entire group is upper triangular.
All composition factors are one-dimensional. In a completely reducible
representation of this flag type, B' would be diagonal scalar -I. It is not.

For V=Sym^3(rho) tensor chi, chi(a)=u, chi(b)=-1, both generators still
preserve a complete flag. V(b) has only eigenvalue 1, with

    rank(V(b)-I)^j = 3,2,1,0 for j=1,2,3,4.

It cannot be the direct sum of its one-dimensional factors. A commuting
projection onto its first invariant line gives a second exact certificate.
Therefore **neither the rank-two flat bundle nor this actual rank-four
coefficient bundle admits a smooth source-free finite-energy harmonic metric
on the complete finite-volume base**. This applies directly to V; it does
not assume every rank-four metric is induced from a rank-two metric.

This does not retract I(V)=+1, alter the cohomology computation, or prove
absence of a sourced physical chiral sector. It specifies an unpaid physical
condition that this unmodified flat-bundle realization cannot meet.

## 3. A scalar balance for the rank-two witness

In the flag frame, every diagonal eigenvalue has modulus one. Its action on
the upper-half-space target is

    z -> a^2 z + a c,   y -> y,

for [[a,c],[0,a^-1]]. Hence b=-log y is invariant under the full image and
b composed with an equivariant map f descends to M. For the curvature -1
target H3,

    Hess b = g_H3 - db tensor db.

If f is harmonic, the chain rule gives

    Delta(b o f) = |df|^2 - |d(b o f)|^2 =: q >= 0.      (3)

Finite map energy implies d(b o f) is L2. Testing (3) with the same cutoffs
forces integral q=0. Therefore the target's horizontal coordinates are
constant. Equivariance would require that constant z to be fixed by B',
whose affine action is a nonzero translation. This is impossible.

This rank-two proof independently explains the sign of the obstruction.
It requires invariance of b, not merely preservation of its ideal endpoint:
a diagonal dilation shifts b and does not satisfy that hypothesis.

## 4. Quantitative cost on a complete one-cusped hyperbolic base

Suppose a smooth harmonic equivariant map existed without the finite-energy
assumption. On a truncated core M_R, with no other boundary or source, let

    Q(R)=integral_M_R q = integral_T_R partial_n(b o f).

For the cusp metric dr^2+e^(-2r)h0, area(T_R)=A0 e^(-2R).
If some fixed core M_r0 has Q0=Q(r0)>0, then Q(R)>=Q0 for R>=r0.
Cauchy-Schwarz on T_R and |df|^2>=|d(b o f)|^2 give

    E(M_R) >= Q0^2/(4 A0) [e^(2R)-e^(2r0)],             (4)

where E=1/2 integral |df|^2. This is a lower bound for a **fixed global map**
with nonzero core horizontal energy. It is not a prediction of the detailed
divergence of all solutions, nor an assertion that such a map exists.

For a family of truncated solutions with bounded total E, (4), applied to
each member, instead forces its Q0 toward zero as the cutoff grows. One must
not hold Q0 fixed while changing the solution, nor identify this collapse
alone with proved convergence to the semisimplified representation.

## 5. Positive control: the isolated cusp DOES have a finite-energy solution

The exact peripheral words for the marked witness are expected to give

    rho(mu)'=[[1,-1],[0,1]], rho(lambda)'=[[1,1],[0,1]].

On a cusp with torus coordinates x1,x2 of unit period, set

    z=-x1+x2, y=sqrt(K/2) e^r,
    K=|d(-x1+x2)|^2_h0 > 0.

This map is equivariant under those exact peripheral translations for
**any constant positive flat torus metric h0**, not just a square shape.
With v=log y, the horizontal tension vanishes; the radial equation is

    v''-2v' + K exp(2r-2v)=0.

The displayed v=r+(1/2)log(K/2) solves it. It has |df|^2=1+2=3,
q=2, and energy E_cusp=3 A0/4 on r>=0, since its volume is A0/2.

There is no contradiction with sections 1-3: the isolated cusp has an inner
boundary. For b=-r-constant, its outward normal derivative is +1 there,
and -1 on an outer cutoff. Thus

    integral_cusp[0,R] q = A0(1-e^(-2R))
                         = inner flux + outer flux.

The inner boundary is supplying the balance. A source-free compact core
cannot glue to this data smoothly: with the opposite normal it would receive
negative total b-flux while its integral q is nonnegative. A smoothed or
modified global solution remains subject to the general argument of section 1.

## 6. What a genuine escape must supply

For a sourced map equation tau(f)=J, (3) becomes

    Delta(b o f)=q+db(J).

Under the finite-energy cutoff conditions and integrability of db(J), a
necessary balance is integral db(J)=-integral q. With physical boundaries,
their signed flux enters instead. This names a **necessary sign and integral**;
it does not construct a source action, prove positivity of its energy, solve
the nonabelian equations, select a vacuum, or show fermions survive.

The new useful task is to produce this term from one consistent action and
then recompute the physical spectrum. An arbitrary compensating J would fit
the equation by hand, not advance the derivation.
