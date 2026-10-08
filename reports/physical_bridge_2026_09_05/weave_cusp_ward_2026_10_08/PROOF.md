# The end term in the regulated phase current

Authored conditional analytic argument in the pinned supplied physical
parent and complete domain. This tests a candidate phase-current
prescription, not every quantum completion. The prior continuum heat
result is retained. Stable vacua and foundational selection remain
separate obligations.

## The candidate comes from the physical inverse

Write the actual doubled product operator as D=[[0,Kdagger],[K,0]]
in its total grading Gamma. Without a regulator,

    -(1/2) Str(D^-1 delta D) = -i Im Tr(K^-1 delta K).

This is the formal imaginary variation of -log det K. The same physical
one-representative or half-full-charge prescription avoids doubling the
original Weyl content. This algebraic origin motivates, but does not
prove integrability of, the candidate

    Omega_e,T(delta D)=-(1/2) Str(chi_T D^-1 exp(-e D^2) delta D). (1)

Here e>0. The finite-cutoff expression is defined; existence of a
renormalized one-form on arbitrary external variations is NOT assumed.
Below we establish its limits on gauge directions and test the necessary
condition for those limits to come from one action. External spacetime
is compact with an invertible D4, as
constructed below. D^2=D4^2+D_internal^2 then has a strictly positive
lower bound, so its inverse and proper-time integral exist. The
spatial insertion makes the differentiated smoothing traces finite.
For external variations [chi_T,delta D]=0. Adjoint and graded cyclic
identities imply (1) is imaginary; no real action is silently substituted.

Gauge transformations are D -> U D U^-1 with U=exp(i alpha), so
delta_alpha D=i[alpha,D]. Put R=D^-2 exp(-e D^2). Moving the last D
through a legitimate finite-cutoff supertrace gives

    Str(chi D R alpha D)
       =-Str(chi D^2 R alpha)-Str([D,chi] D R alpha).

Consequently

    Omega_e,T(delta_alpha D)/i
       =Str(chi alpha exp(-eD^2))
         +(1/2) Str([D,chi] D^-1 exp(-eD^2) alpha).       (2)

The second term is a PROPAGATOR end current. It is not the finite
horizontal signature inserted as a new fermion. A vanishing first
term in a limit says nothing by itself about this second term.

## Factorization and the order of limits

For each unbroken gauge representation let

    a_R(s)=Tr4(gamma5 alpha exp(-s D4_R^2)),
    S_R(s)=lim_T Str_internal(chi_T exp(-s D_internal,R^2)).

The preceding packet gives S_R(s)=sum_mu erf(mu sqrt(s))/2 and its
derivative from the ACTUAL end current. Since
D^-1 exp(-eD^2)=integral_e^infinity D exp(-sD^2) ds,
the product Clifford trace in (2) gives

    Omega_e(delta_alpha D)/i
       =sum_R [a_R(e) S_R(e)
                    +integral_e^infinity a_R(s) S_R'(s) ds]. (3)

The D4 term in the end numerator has odd external Clifford trace;
the internal term has precisely the previous factor2*S_R'. Both
physical source and target slots are kept. Use one representative
per conjugate pair, or half the full trace. This is the same convention
that yielded the earlier five anomaly coefficients.

For fixed external background D4 has a gap. Its heat insertion is
bounded near0 by the local chiral heat expansion and decays at infinity.
The actual finite half-integer end masses make |S_R'| bounded by a
finite sum const*s^-1/2*exp(-mu^2 s), integrable on(0,infinity).
The T limit inside the proper-time integral needs a bound BEFORE
taking T to infinity, not just a bound on the limiting S_R'. Here is
that extra step. Write H=D_internal^2>=0 and let P_T be multiplication
by the indicator of the width-one shell supporting chi_T'. At any
fixed v>0 the prior normal-kernel bounds give

    sup_T Tr(P_T exp(-v H) P_T) = C_v < infinity.

The finite horizontal Gaussian density is uniform on these shells;
the nonzero-angular part tends to zero there, and the compact range
of T is bounded by ordinary local smoothing. Finite short-range c,d
do not change this fixed-v bound. For s>=e, the spectral inequalities
exp(-s H)<=exp(-e H/2) and
H exp(-s H)<=2/(euler_number*s)*exp(-e H/2), together with localized
Hilbert-Schmidt Cauchy-Schwarz, imply

    |Str([D_internal,chi_T] D_internal exp(-s H))|
                <= const_e / sqrt(s), uniformly in T.

The multiplier [D_internal,chi_T] has uniformly bounded norm. The
external heat insertion has an exponential large-s bound at this fixed
background because D4 is gapped. This yields an integrable dominator
on[e,infinity), so the fixed-s normal limit passes through the integral.
Only AFTER that T limit do the explicit finite end masses bound S_R'
and permit e to0. Thus, since S_R(0)=0,

    Omega(delta_alpha D)/i
          =sum_R integral_0^infinity a_R(s) S_R'(s) ds.    (4)

This is generally NOT zero. Equivalently, integration by parts gives
-sum integral a_R'(s) S_R(s) ds, because a_R(infinity)=0. Treating
a_R as a constant all the way to infinity would lose that control.
These global limit statements remain authored analytic work, not
certified by the finite matrix or quadrature checks.

## A smooth admitted external test with no zero modes

Use the flat four-torus with coordinates x_i in[0,2pi], antiperiodic
spin in x1 and periodic in the other directions. The free Dirac gap
is1/2. Turn on the globally defined Hermitian color connection

    A=h*T*(sin x1 dx2+sin x3 dx4), T=diag(1,1,-2),
    alpha=T*cos x1*cos x3, 0<h<1/12.

All color representations in the full parent are1,3,bar3,8, with
operator norm of T at most3. The Dirac perturbation is bounded by6h,
strictly below the free gap. Thus every D4_R is invertible, including
the color-neutral sectors. This is a controlled external gauge probe,
not a selected spacetime geometry or vacuum background.

The curvature is h*T*(cos x1 dx1 wedge dx2+cos x3 dx3 wedge dx4).
Its integrated tr(F wedge F) is zero, consistent with invertibility.
But the local gauge insertion gives

    integral tr_fund(alpha F wedge F) = -48*pi^4*h^2 !=0. (5)

Now dilate the external metric by L^2 while keeping these connection
and parameter one-forms fixed. The normalized operator is D4,L=D4,1/L,
so exactly a_R,L(s)=a_R,1(s/L^2). The gap stays positive for every
finite L; it is not assumed uniform as L goes to infinity. The bounded
function a_R,1 and the integrable |S_R'| allow dominated convergence
in (4). The local chiral heat coefficient a_R,1(0) is the usual
covariant tr_R(alpha F^2) coefficient. Therefore

    lim_L->infinity Omega_L(delta_alpha D)/i
               =sum_R a_R,1(0)*ind M_R.                 (6)

Relative to one left fundamental Weyl color coefficient, this is -1
at n=1 and -3 at n>=2; signs reverse at negative n and n=0 gives0.
The first result is thus recovered as a LOW-ENERGY propagator response,
despite the previous zero ultraviolet heat trace. Nonzero limit implies
nonzero response at sufficiently large finite L. No particular finite
threshold L or full external heat kernel was numerically computed.

The complete end response can also be tested against Laplace functions:
if H_n(s)=sum E_mu erf(mu sqrt(s)) is the full color heat coefficient,

    integral_0^infinity exp(-z s) H_n'(s) ds
                   =sum E_mu*mu/sqrt(mu^2+z), z>=0.      (7)

At z=0 this equals the old color anomaly. Exponentials are instrument
controls; they are NOT asserted to be the actual external heat trace.
The physical slow-field argument above uses dilation and domination.

## Why this candidate is not a consistent phase variation

The cutoff and regulator in (1) transform equivariantly under the
external gauge group. This exact covariance passes to the finite
gauge-direction limits; it does not require constructing the limit on
arbitrary variations. Let X_alpha(D)=i[alpha,D]. For fixed parameters
the vector-field bracket is X_c with c=-i[alpha,beta]. Define
B_D(alpha)=Omega_D(X_alpha), using the established gauge-direction
limit. Equivariance implies

    X_alpha B(beta)=B(c),
    X_beta B(alpha)=-B(c).

Hence any one-form with these gauge-direction values must have

    dOmega(X_alpha,X_beta)
       =X_alpha B(beta)-X_beta B(alpha)-B(c)=B(c).        (8)

An exact variation delta W has zero exterior derivative. Thus any
nonzero B(c) disproves the identification of (1) with delta W. In
the slow-field limit this is the familiar factor2 on the left versus
factor1 on the right of the consistency condition for a nonzero
covariant anomaly. The conventions above fix the bracket sign.

This is not only a formal bracket possibility. Let
X=(E13+E31)/2, Y=(E13-E31)/(2i), f=cos x1 cos x3;
choose alpha=fX, beta=2Y. Then c=f*diag(1,0,-1), and with the SAME
background A the insertion integral is -24*pi^4*h^2, nonzero. Equation
(6) makes B(c) nonzero for sufficiently large finite L whenever n!=0.
The color coefficient alone suffices; no abelian rescaling can erase it.

Bilal [sections4.2 and9.1](https://arxiv.org/html/0802.0634v1) distinguishes
covariant currents from functional derivatives and explains the
consistency condition. Here (2)--(8) identify the concrete end defect
for our operator rather than citing a generic anomaly as a substitute.
Witten--Yonekura [section2](https://arxiv.org/html/1909.08775) constructs
an actual massive-regulator phase with specified boundary data; that
different problem is not a phase we have earned by a heat coefficient.

An exact counterterm delta W_ct cannot repair this curl: its exterior
derivative is zero. A corrected current must therefore differ by a
NONEXACT current correction (as in a covariant-to-consistent current
conversion), or arise from a different regulated action/end system.
Constructing that conversion does not by itself cancel the resulting
consistent anomaly. These are separate duties.

The verdict is deliberately narrow: the naive covariantly regularized
inverse current (1) is not an integrable phase variation on this family
at nonzero flux. It is NOT a no-go for another regulator, an end sector,
counterterms within a different consistent construction, or the full
supplied parent. A correction
must repair the one-form and be derived from one quantum action, not
discard (2)'s end. The unsigned action and full-loop renormalization
remain separate, as do stability, three families and genesis selection.
