# Actual cone fermion operator and neutral boundary domains

September 30, 2026. R68 authored argument, frozen before finite checks.
The supplied metric, action and canonical background are inputs. This
is a local linear analysis with one explicit nonlinear compatibility
test, not independent analytic review or physical completion.

## Full coefficient operator

Use R66's matrices N,P,D,H and C_r=h' H, C_x=t N,
C_y=k D+beta t squared P, t=exp(-h). The link inverse metric is
diag(alpha,1/alpha), alpha>0, with period-one coordinates. In the
orthonormal link coframe (dx/sqrt(alpha),sqrt(alpha)dy), let
Pdeg=diag(0,1,1,2), M=Pdeg-1. Use the R63 isometry to L2(dr),

    U(a,b)=sum_p r^(p-1) a_p + dr wedge sum_p r^(p-1) b_p.

Here b_p has total degree p+1. In any coefficient representation rho
whose Hermitian pairing gives rho(C) dagger=rho(C dagger), define

    K=r rho(C_r),
    Zx=sqrt(alpha)[i xi+rho(C_x)],
    Zy=[i zeta+rho(C_y)]/sqrt(alpha),
    E=e_x tensor Zx+e_y tensor Zy, L=E+E dagger.

xi,zeta are real Fourier momenta; periodic modes use 2pi times integers.
Tensor identity matrices are implicit. Direct metric adjunction gives

    r U^-1 d_C U = [[E,0],[r partial_r+M+K,-E]],
    r U^-1 delta_C U = [[E dagger,-r partial_r+M+K dagger],
                        [0,-E dagger]],
    Q=U^-1(d_C+delta_C)U=Gamma(partial_r+A(r)/r),
    Gamma=[[0,-1],[1,0]],
    A=[[M+K,-L],[-L,-M-K dagger]].

On this background K is Hermitian, so A is Hermitian and anticommutes
with Gamma. Formal symmetry is also visible directly in the paired
off-diagonal blocks. No constant indicial operator is substituted for
A(r). The identities apply to the fundamental representation and to
the adjoint with the trace pairing: (ad C) dagger=ad(C dagger).
They do not assert that fundamental forms by themselves are physical
fermions in an unchosen parent theory.

For a trial radial power r^sigma, let D_sigma be the displayed d matrix
with r partial_r replaced by sigma. Since d_C has the extra factor 1/r,
its square includes D_(sigma-1)D_sigma AND the radial derivative of
D_sigma. Flatness uses r t'=-r h' t and [H,N]=N,[H,P]=2P.
Omitting the radial connection or treating t as constant spoils this
identity. A limiting normal spectrum does not supply full boundary
traces for the actual logarithmic operator.

## An exact reducing adjoint direction

Let Z=D=diag(1,-3,1,1), with tr(Z squared)=12. For every positive radius,

    [C_i,Z]=[C_i dagger,Z]=0.

Consequently the orthogonal coefficient projection

    Pi(X)=Z tr(Z X)/12

annihilates ad C_i on both sides and commutes with the entire d_C,
delta_C and Q. This is an EXACT reducing coefficient, not an asymptotic
approximation. It is unique among constant traceless reducing
coefficients: commuting with N and N dagger forces a scalar on the
irreducible three-chain span(e0,e2,e3) and a scalar on e1. Tracelessness
leaves only Z. Equivalently the linear commutator system has rank 15
on the sixteen matrix entries. Commuting only with N and D instead
leaves three traceless dimensions (Z,N,P); N and P do not commute with
the Hermitian adjoints. A holonomy invariant is not automatically an
orthogonally reducing coefficient.

This local centralizer is not identified with a globally unbroken
physical U(1). The actual core may mix it with other coefficient
directions, and the global gauge algebra is not determined here.

## Boundary data that the background does not eliminate

On Z-valued harmonic link one-forms, write u=(a,b), representing
a+dr wedge b. Both components have radial measure dr. In the
orthonormal link frame the exact operator is

    Q0=[[0,-1],[1,0]] partial_r

on four complex components. A cutoff equal to one near r=0 and zero
near the collar's outer boundary gives four independent elements of
the maximal local graph domain. Their apex traces span C^4. Green's
identity, in coordinate coefficients with Hlink=diag(alpha,1/alpha), is

    <Q u,v>-<u,Q v>=[u dagger G v]_0^R,
    G=[[0,Hlink],[-Hlink,0]],

with the positive coefficient factor 12 restored if Z is not normalized.
G is nondegenerate. Every graph limit of compact-support fields has
zero trace, since the restricted graph norm is the H1 interval norm.
The cutoff constant traces therefore cannot lie in the minimal domain:
each has a nonzero Green pairing with another maximal-domain cutoff.
There are at least these four independent complex apex data for the
full operator. This does not enumerate the complementary channels.

Thus the minimal first-order operator is not self-adjoint at this apex.
This remains an apex obstruction if a regular outer boundary condition
has already been fixed, because the witness cutoffs vanish there.
No choice of q>0, q!=1, or alpha>0 within this ansatz removes it.
R67's degree-one X0 has zero trace in this block. It is a legitimate
bosonic variational class, not by itself a self-adjoint fermion domain.

## Explicit linear choices and their scope

Let Omega=[[0,1],[-1,0]], S=-Omega Hlink, so S squared=-1. For a
complex line W in C^2 let Wperp denote its Hermitian Hlink complement.
The separated trace condition is

    (a,b) in L_W=W direct-sum Wperp.

L_W has complex dimension two and annihilates G; it is maximal for
this condition. On the neutral block over a finite collar interval,
take H1 fields with L_W at each endpoint (possibly different W's).
Integration by parts and surjectivity of the H1 trace show that the
adjoint has exactly the same domain. This proves self-adjointness of
THIS block. Compact interval H1 inclusion gives compact resolvent.
It is not a Fredholm assertion for the full singular coefficient.

The internal reality map, up to an overall phase, is

    C(a,b)=(S conjugate(b),-S conjugate(a)).

It squares to one. As in R61, every complex line is bilinear symplectic
Lagrangian, which makes L_W invariant under C. This formula now acts
on an actually reducing sector of the nonabelian background: Z dagger=Z.
For example Wplus=span(1,-i alpha) and Wminus=conjugate(Wplus) are
distinct, and both pass reality and current cancellation. Bare star
and bare conjugation separately need not preserve either one. This
is not an identification of a physical spacetime parity lift.

The block also has a closed differential complex: d differentiates a
into the b slot, with a in H1 and endpoint values in W; b is arbitrary
L2 in D(d). The Hilbert adjoint differentiates b with endpoint values
in Wperp. Their intersection is the stated Q domain. Degree parity
preserves it. Q and i(d-dagger) give the usual two internal linear
supercharges, with equal squares and zero anticommutator on the common
square domain. This is linear supersymmetric quantum mechanics in
the isolated block, NOT closure of the full interacting 7d superfield
variations, compact gauge action or quantum anomaly cancellation.

If the same W is used at both endpoints, constant block solutions have
one complex degree-one and one degree-two coefficient. That artificial
collar count is paired and is not a global massless-particle count.

## Why separate linear domains cannot simply be glued

The reducing coefficient is not a Lie algebra ideal in sl4. Let
X=E01 and Y=E10. Pi(X)=Pi(Y)=0, but

    [X,Y]=E00-E11, Pi([X,Y])=Z/3.

Complementary fluctuations therefore source the neutral channel through
the actual parent bracket. The neutral boundary law must be compatible
with their products and with the gauge and superfield derivative laws.
One cannot infer nonlinear closure by attaching an arbitrary domain
for the complementary sector to L_W.

There is also a useful limit to the L4 sufficient criterion. A constant
real deformation a=c Z dx commutes with C and its adjoint. C+a stays
flat and moment-flat exactly, so its full residual-square action is
zero, although its radial L4 density is 144 c^4 alpha^2/r^2 and diverges
for c!=0. It changes the meridian by exp(c Z) and so is not admitted
when the actual peripheral conjugacy class is fixed. This is a control,
not a proposed rescue of that fixed-holonomy model. It proves only that
L4 is sufficient, not necessary for every zero-residual family.

The next physical task is a compatible domain and end law for all
coupled channels, followed by core matching. Neither the local choice
nor its linear self-adjointness derives chirality, metric selection,
the supplied action, gravitational dynamics or a complete theory.
