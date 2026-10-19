# A corrected restricted theta sequence and its monodromy duty

October 19, 2026. Analytical continuation of the
[received frontier audit](FRONTIER_RESOLUTION_REPORT_INTAKE.md).
This recovers a nonzero holomorphic bundle sequence on the declared
braid-generated quotient, while proving why that same modulus-only
construction cannot be promoted to the full registered action.
No producer, numerical check or scientific test is executed. This is
pending independent review, not restoration of the withdrawn geometric
puncture sequence or a four-dimensional physical-index calculation.

## Common conventions, rather than another numerical intertwiner

Use E, its character mu=mu_+, its natural inner lifts J_h and
Omega=<l,r> from
[the common-register proof](MATTER_AND_BOUNDARY_COMMON_REGISTER.md).
Thus g_l=(1+i)/sqrt(2), g_r=(1-j)/sqrt(2),
mu(l)=zeta=exp(pi i/4), mu(r)=zeta^-1, mu(J_h)=1.
Set s=r l^-1 r, so g_s=-(i+j)/sqrt(2), mu(s)=zeta^-3.
Here i=diag(i,-i), j=[[0,1],[-1,0]] are quaternion matrices;
scalar occurrences of i have their usual complex meaning.

Write O_g=Ad_g on the ordered imaginary quaternion axes (j,i,k).
The cohomology modules in this convention are

    T_minus(e)=mu(e)^-1 O_g, T_plus(e)=mu(e) O_g.

These names fix concrete hands; a comparison with another paper's T
or inverse-pullback convention requires its actual intertwiner.

The local module has an exact tensor description too. In the raw
frame its action A_e permutes parity blocks and applies the same g
to each doublet. Let C=diag(Q_p), Q_p=(j,i,k), as already used
by B1606. If g Q_p g^-1=s_p Q_q, its block action becomes

    C^-1 A_e C: e_p tensor u -> s_p e_q tensor g u.

Consequently, on the entire E,

    W_local=O_g tensor g
           =T_minus tensor (mu g)
           =T_plus tensor (mu^-1 g).                (1)

This is a constant, exact identification, not a numerical SVD choice.
It does not identify W_local with T_plus direct sum T_minus.
The old local 2+4 decomposition is preserved.

## An actual holomorphic doublet on Omega

Put A(tau)=theta_3(0|2tau), B(tau)=theta_2(0|2tau), and

    v(tau)=(i B(tau), A(tau))^T.                   (2)

This is -j times the received report's doublet (A,-i B)^T.
Changing that frame must also change its matrix action; it is not
licensed by checking only the pointwise rank of a sequence.

The classical lattice-parameter laws were read directly in
[DLMF 20.7.27--33](https://dlmf.nist.gov/20.7#viii).
Separating even and odd summation indices gives
theta_3(0|tau/2)=A+B and theta_4(0|tau/2)=A-B. Hence

    A(tau+1)=A, B(tau+1)=i B,
    A(-1/tau)=sqrt(-i tau)/sqrt(2) (A+B),
    B(-1/tau)=sqrt(-i tau)/sqrt(2) (A-B).           (3)

Choose j_l=1 and j_s=sqrt(tau), with the same metaplectic
product law as the earlier geometric-field proof. Then (3) implies

    v(tau+1)=diag(i,1) v(tau)=mu(l) g_l v(tau),
    v(-1/tau)=sqrt(tau) zeta^-1/sqrt(2)
                   [[-1,i],[-i,1]] v(tau)
              =j_s mu(s) g_s v(tau).              (4)

For the second equality, multiply
zeta^-3 g_s=zeta^-1 [[-1,i],[-i,1]]/sqrt(2).
The generators l,s generate Omega since r=l s l. Therefore

    v(e tau)=j_e(tau) mu(e) g_e v(tau), e in Omega. (5)

This derivation checks the actual generators and their square-root
convention, not just sampled values at tau. Both sides use the
same registered lift under composition.

The doublet never vanishes on the upper half-plane. In fact A
itself is nonzero there: with q=exp(2 pi i tau), |q|<1,
the product A=product_(n>=1)(1-q^(2n))(1+q^(2n-1))^2 has no
zero factor and converges to a nonzero product. The underlying
product was read in [DLMF 20.5.3](https://dlmf.nist.gov/20.5#E3).
This is an analytic nonvanishing proof; finite sampling is unnecessary.

## The resulting exact bundle sequence, with its scope stated

Let E_k(R) mean the holomorphic equivariant bundle over the
upper half-plane with factor j_e^(2k) R(e), on the quotient by
the specified Omega action. This notation fixes the automorphy;
it does not presume a compact cusp extension or a physical metric.
Let epsilon=[[0,1],[-1,0]], and define

    I_tau(x)=x tensor v(tau),
    D_tau(x tensor u)=x [v(tau)^T epsilon u].

Equations (1) and (5), together with g^T epsilon g=epsilon,
give the equivariant holomorphic sequence

    0 -> E_k(T_minus) --I--> E_(k+1/2)(W_local)
                    --D--> E_(k+1)(T_plus) -> 0.   (6)

For I, the scalar factors multiply as
mu^-1 times mu=1 and j^(2k) times j=j^(2k+1).
For D, v'^T epsilon g=j mu v^T epsilon, yielding the
target factor j^(2k+2) mu O_g. These verify the domain and
codomain weights as well as the matrix action.

Since v is nonzero, I and D have ranks three everywhere on
the upper half-plane, D I=0, and ker D=im I. Their local
holomorphic exactness follows, not only vector-space exactness.
For k=1/2 the weights are 1/2,1,3/2, with the concrete hands
specified in (6). They must not be silently reversed when
substituting into the received report's Euler calculation.

This is a positive: a missing constant intertwiner need not
forbid a weight-dependent holomorphic sequence on this restricted
quotient. But (6) is not yet the actual puncture sheaf sequence.
That identification requires its genuine evaluation/connecting
maps, higher direct images and cusp/parabolic extensions.
Here B tends to zero and A to one at the cusp; rank in this
frame does not establish exactness in every chosen cusp lattice.
No Euler characteristic, physical boundary domain or 4D index
is inferred from (6).

Its image is a tau-dependent rank-three subbundle, not a fixed
subspace invariant under every local matrix at one fixed state.
It neither contradicts the fixed local 2+4 splitting nor selects
the extreme boundary dimensions zero or six. If its rank were
simply inserted as dim Lambda=3 in the old conditional boundary
formula, that formula would give zero, not three. Such an insertion
would itself need a justified identification with the boundary domain.

## The full-register extension fails on the declared reduced base

Let c=a b^-1 a^-1 b. The natural lift J_c has g=-1 and
mu=1. Its actions are therefore

    T_minus(J_c)=T_plus(J_c)=+I3,
    W_local(J_c)=-I6, j_(J_c)=1.                  (7)

It fixes tau. It also fixes every point of the earlier lattice
coordinate base X={(tau,z): z not in Z+tau Z}: its inner word
has zero exponent sums, so its translated coordinate is unchanged.
Suppose a linear map F_x from the stated triplet bundle to the
local bundle were equivariant on either of those bases. Equation
(7) would require

    F_x=F_(J_c x)=(-I6) F_x (I3)^-1=-F_x.

Thus F_x=0. The reverse-direction map vanishes by the same argument.
No nonzero rank-three sequence of this type is equivariant on the
entire E while the base and coefficient actions remain as stated.
This is a fixed-stabilizer obstruction, not a physical no-go.

A scalar character of E cannot repair this sign: J_c is a
commutator in the natural J(F2), and every scalar character
kills commutators. The metaplectic weight pulled from E/J(F2)
is also trivial on J_c. One must change more than an eta power
if the same source and target are to be joined over the full E.

## What must be retained next

There is an explicit fibre control, not just a dummy state register.
Return to the received report's proposed doublet field and make the
same fixed frame change as (2). In period-one argument convention set

    f(z,tau)=(i theta_2(z|2tau),theta_3(z|2tau))^T
                         /sqrt(theta_1(z|tau)).    (8)

This is the coefficient of a proposed field, not yet a physical
zero mode; including dz changes its coordinate transport. The square
root is taken on the universal cover of the punctured fibre, where
theta_1 is nonzero and a logarithm can be chosen. The usual theta
notation in (8) means vartheta(pi z|tau).

For its numerator N, the quasi-period and half-period identities
in [DLMF 20.2(ii)--(iii)](https://dlmf.nist.gov/20.2#iii) give

    N(z+1)=diag(-1,1) N(z),
    N(z+tau)=t(z,tau) i j N(z),
    t(z,tau)=exp(-pi i tau/2-pi i z),
    theta_1(z+1)=-theta_1(z),
    theta_1(z+tau)=-t(z,tau)^2 theta_1(z).

Thus continuation along chosen lifts of the two periods gives

    f(z+1)=sigma_a i f(z),
    f(z+tau)=sigma_b j f(z), sigma_a,sigma_b in {+1,-1}. (9)

The signs record the square-root/path choices; they must be retained.
For example root factors +i and +i t give sigma_a=sigma_b=+1.
Irrespective of those central signs the two matrices anticommute,
and their commutator is -I. This recovers exactly the puncture
monodromy that (7) demands and that the lattice coordinate cover
forgets. Equation (9) is a continuation law on the lifted punctured
fibre, NOT two commuting translations acting on a single-valued
doublet on X. No contradiction with the fixed-base obstruction arises.

Two losses in passing from (8) to a theta constant are now explicit.
First, with d(tau)=partial_z theta_1(0|tau), the leading coefficient is

    f(z,tau)=z^(-1/2) v(tau)/sqrt(d(tau))
                         +O(z^(3/2)).             (10)

It is a half-order pole and a branch coefficient, not ordinary
evaluation of a holomorphic field at the puncture. Dropping either
z^(-1/2) or sqrt(d) changes the geometric map to be identified.
Second, under tau->tau+1 at fixed z, choose the continuous root
factor exp(pi i/8) of theta_1's exp(pi i/4). Then

    f(z,tau+1)=exp(pi i/8) g_l f(z,tau).           (11)

This differs from v's mu(l) g_l=exp(pi i/4) g_l factor.
A differential dz does not remove that difference on this generator.
One must derive the full branch and modular cocycle of (8), including
its normal half-order frame, before using it as the section in (6).
Equations (9)-(11) recover the missing data without establishing that
the received field is the required geometric evaluation map.

The full punctured-fibre universal cover, unlike the lattice
coordinate cover, distinguishes the commutator deck path.
The coefficient monodromy rho(c)=-1 is precisely information
that a modulus-only or lattice-only description discards.
A candidate map depending on such a lifted fibre state is not
excluded by the fixed-base argument. Neither is a correctly
derived change of the source coefficient or geometric lift.
One must construct that map and check its transformations; merely
adding a dummy free register would not identify the physical field.

This also explains why the earlier meromorphic TRIPLET theta
field can live on X: its local coefficient is not this doublet
module and its J_c action is +1. Its success cannot transfer
the present sign-sensitive map by analogy.

The next bounded derivation is therefore the full doublet
field/evaluation map on the punctured universal family, with
its square-root branch, puncture transport and exact target
module retained together. Then test whether its actual geometric
sequence agrees with (6) on Omega and extends on the larger base.
Only after that can its cusp extensions and any physical
operator/domain comparison be posed without an information loss.

No complete priced-input row is paid by this conditional repair.
It preserves a useful positive and identifies the missing
register rather than forcing three or abandoning the route.
The frozen v2/v3 packages are unchanged. Generator, nonvanishing,
rank, cusp-lattice and full-J_c countercontrols belong in an
admitted successor, not a retroactive claim that v3 tested them.
