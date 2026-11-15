# Physical harmonic transport with its spin and based-word factors retained

2026-11-12. Authored conditional hand calculation under the acceptance
committed at1aa76251f. No scientific producer, CAS, imports, collection
or tests ran. New claims await nonauthoring scrutiny and CC's requested
independent calculation. Exact source pins are in SOURCE_RECEIPT.json.

## 1. Candidate and claim

Use the supplied curved compact-E8 action, balanced quaternion bundle,
complete graph domain, odd extending spin class, pure coherent h4
correction and trivial extra Wilson character. Retain the conjugate
half-root sectors and the vector companion. Put mu=H/2, so
[mu,E_+]=E_+, [mu,E_-]=E_- and exp(2*pi*i*mu)=1 on248.
Keep the h1 phase and other carriers at their previous scope.

The physical half-root form modes carry the trace-dual spin line S^5.
Its factor changes the proposed bare one-form comparison. In an
explicit coherent geometric completion, the active simple-pole line
induced over the three backgrounds has the weave's triplet matrices
in a normalized frame. The full coefficient bundle still has rank9.
The source's cohomology convention makes this the conjugate weave
half when both actions are written as left actions, as specified below.

Two coherent identifications of the geometric spin lift remain in the
declared class. Their difference and the unresolved vector-spin-line
transport are recorded below. The construction establishes actual
normalizable modes and their covariant transport conditionally on this
parent. Exhaustion of the kernel retains the WP-3.1 review premises.
It supplies neither a branch-selection law nor three SM families in
one background.

## 2. Distinguish the based quarter-turn from its homology matrix

Use E={(phi,g):rho phi=Ad_g rho}, epsilon=(id,-1), and
J_h=(Inn_h,rho(h)). Let L(a)=a,L(b)=ab, R(a)=ab,R(b)=b.
Write I=rho(a), J=rho(b), K=IJ and

    gL=(1+I)/sqrt2,  gR=(1-J)/sqrt2,
    s(a)=b^-1, s(b)=a,  gs=(1-K)/sqrt2,
    Delta=L R^-1 L=Inn_a s,
    gDelta=I gs=(I+J)/sqrt2.                         (1)

Both s and Delta have homology [[0,1],[-1,0]]. Their based actions
and quaternion lifts differ. In particular gs is a rotation in the
Pin2 stabilizer and gDelta is a reflection. On the active highest
line, the compensator character is+1 on s and-1 on Delta.
The based identity itself is recovered from
COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md. Its application to the
physical stabilizer character is the new step here.

The earlier P753 F1 counterexample used Delta=LR^-1L, precisely as
main's induced matrices do. Its matrices give-1, while its written
character gave+1. Equation(1) shows how+1 can correctly describe s
instead. Negating matrices was a repair of the printed character.
It did not determine which based generator the physical field sees.
Keep this convention correction beside that review and CC's B1866.

The natural inner subgroup J(F2) is normal and meets{1,epsilon}
trivially. E/J(F2) is a double cover of SL2Z. With t=eL and s=(s,gs),
the relations in this quotient include

    epsilon^2=1, epsilon central,
    s^4=epsilon, (s t)^3=epsilon, [s^2,t]=1.         (2)

For example (s L)^3=id on F2 and (gs gL)^3=-1. Also
s^2 L s^-2=Inn_(a^-1) L with the corresponding uniform lifts.
Together with the standard SL2Z presentation these give the indicated
double cover. Based paths are retained through J_h, not discarded from
the field representation. The earlier coherent-word proof supplies
the right-action convention and Delta^4=epsilon J_c.

## 3. An explicit geometric completion and its two lifts

Let A_phi=[[a,b],[c,d]] be the exponent-column homology action and
D=diag(1,-1). The compatible modular base map is gamma_phi=D A_phi D.
For tau'=gamma_phi tau and j=c_gamma tau+d_gamma, define

    f_phi(z)=z/j,  C_tau=C/(Z+tau Z),  p=0.           (3)

The images of the old cycles in the new period basis are
(a,-c_gamma) and(-b_gamma,d). Thus f_* has matrix A_phi. This
checks the direction against the source holonomy action K phi^-1.
For a nontrivial based inner part include its path and K,rho transport.

Use the complete hyperbolic metric of curvature-1/ell^2 in each
conformal class. Its naturality gives

    Omega_tau'(z/j)=|j| Omega_tau(z).                 (4)

Equivalently, the argument works on transported metric pairs satisfying
(4). The metric and ell remain supplied. The uniformization statement
was checked in Mnev's lecture4, first slide. [Source](https://academicweb.nd.edu/~pmnev/CFT2011/CFT_Lecture4.pdf).

A compatible spin lift has holomorphic square root b_e(tau)^2=j.
There is an explicit identification q0 from(2) to the geometric
metaplectic group under which

    q0(t)=(tau -> tau-1, b=1),
    q0(s)=(tau -> -1/tau, b=sqrt(tau)),
    q0(J_h)=identity, q0(epsilon)=(id,-1).            (5)

The principal roots on the upper half-plane satisfy(2). For instance
(q0(s)q0(t))^3 has base identity and root-1. The quotient presentation
therefore supplies the coherent all-word map, with based gauge paths
still present. R=Inn_(b^-1) s L^-1 s^-1 gives the source R lift too.

A second map q1 multiplies both displayed generator roots by-1.
These are the two choices over the same base map, with trivial
geometric action assigned to J(F2). Their ratio is the sign character
of SL2Z, chi12. The relation(st)^3=1 on the base forces the two
generator signs to agree. A physical identification with one of them
has not been selected by the source spin class alone.

In a full-E lift, triviality on J(F2) is also forced within this
geometric double-cover problem. Its image there is a central sign
character of F2 invariant under all Aut+ moves. The full mod2 action
has no nonzero invariant linear functional. On the stabilizer alone
that conclusion would fail. This conditional restriction does not
select the physical parent or its supplied gauge linearization.

## 4. Actual fields, norm, mass operator and complete domains

Put sigma_e=b_e/|b_e| and Uspin=exp[-i arg(sigma_e) mu]. This is
well-defined since mu is an integral cocharacter. The source's
spin-induced gauge bundle supplies this compensation. A mu=1
background raising field gets sigma_e from spin and sigma_e^-1 from
gauge, so the balanced background is preserved by their product.

For e in E_theta, its quaternion g lies in St=2O intersect Pin2.
Use the existing coherent Pin2 homomorphism G. Since K=G rho,

    K phi^-1=G(g)^-1 K G(g),
    g Ad_G(g) Phi0=Phi0.                             (6)

G(g) commutes with H. Thus it composes coherently with Uspin.
In the source's unitary gauge and holomorphic spin coefficient frames,
the forward slot maps are the coordinate pushforward followed by
these existing gauge/flavour factors,

    lambda' = Ad_(Uspin G(g)) lambda,
    a'      = bar(j) Ad_(Uspin G(g)) a,
    (u',v') = b_e [g tensor Ad_(Uspin G(g))](u,v).     (7)

Arguments on the right are z=j z'. The affine connection retains its
actual derivative compensator when local frames change. Here j and
the displayed fibre compensators are constant in the surface coordinate.
The four kinetic densities give, after d2z'=|j|^-2 d2z,

    Omega'^2 -> |j|^2 Omega^2,
    (1/2)|a'|^2 -> (|j|^2/2)|a|^2,
    Omega'(|u'|^2+|v'|^2) -> |j|^2 Omega(|u|^2+|v|^2).

These are exact unitary maps of the actual physical Hilbert spaces.
Transport the opposite-charge left input and its conjugate trace-dual
target. The source action, its Hessian and gauge-Killing term then give

    M_tau' Ue_in=Ue_out M_tau.                        (8)

The target coordinate factors are(1,j,bar(b_e),bar(b_e)), with
the trace-dual flavour action on the last pair. For example p transforms
by bar(j)b_e and p/Omega therefore by bar(b_e), whereas both terms
of the a-target row transform by j. The lambda-target row's |j|^2
numerator cancels Omega'^2. These check the actual mass rows rather
than assigning the input factors to the output.

This follows on compact-support cores from the covariant derivative,
S^2=K, invariant trace and parallel flavour epsilon. Unitarity extends
it to the complete graph closures and actual adjoints. Hence
P0_tau' Ue_in=Ue_in P0_tau, where P0 is the Hilbert projection onto
the full kernel. This identity needs no gap in the other sectors.
Nonlinear residual norms, gauge constraints and the oriented Green
pairing transport with the action.

At epsilon, the geometric compensation is P=exp(-i*pi*mu), with a
minus on physical spin slots. The Pin2 compensation is Kpi=Zeta P,
also with a flavour minus. Their product gives

    U_epsilon=Ad_Zeta on EVERY physical slot.         (9)

It is-1 on the128 and+1 on the120. This retains the source gauge
grading and distinguishes a physical mode from a bare coefficient
local system. Both q choices have the same action(9).

## 5. Exhibit the harmonic form modes rather than a block template

For highest mu=J0, the degree-zero line is S^-J0 L. Its Hermitian
metric is Omega^J0. Serre/Hodge duality uses K(S^-J0 L)^*=S^(J0+2)L^-1.
In a local unitary flat frame the actual physical solution is

    Psi_a(f)=(0, Omega^(-J0/2) bar(f) vtop,0,0),
    ||Psi_a(f)||^2=(1/2) integral Omega^-J0 |f|^2 d2z. (10)

Here f is the holomorphic coefficient of that dual spin line.
The source gauge derivative on vtop is
D_z=2 partial_z+J0 partial_z log(Omega), so D_z a=0 exactly.
Both raising maps annihilate vtop, giving every other row of M Psi=0.
The expression is anti-linear in f, as physical Hodge duality requires.

For J0=3 use f=1,wp when L=O, and f=S3,S3' when L=chi11.
The normalized Szego function is
S3(z,tau)=pi theta1'(0,tau) theta3(pi z,tau)/
[theta3(0,tau) theta1(pi z,tau)]. Its residue is1.
All these modes have finite physical norm at the puncture. The source
strict pole bound permits orders0,1,2 in the S^5 dual. Complete
cutoffs with vanishing differential prove membership in the actual
graph domain, directly from(10), independently of kernel exhaustion.

The source middle harmonic representative provides the third mode,
the constant section on the trivial summand of S(L_+ plus L_-).
Its two physical spin entries lie on opposite mixed extremes.
Their outgoing and adjoint Higgs maps vanish separately. The remaining
derivative is the holomorphic spin equation and the norm is finite.
Thus the explicit2+1 modes are actual solutions. The assertion that
there are no further modes is still the complete-kernel WP-3.1 duty.

## 6. Keep the spin power in modular transport

The flat top-line compensator kappa_a is trivial on Pin2 rotations
and equals alpha on reflections. The bare active line alpha=-1
therefore has characters

    kappa_a(L^2)=-1, kappa_a(s)=+1,
    kappa_a(Delta)=-1.                              (11)

For the middle spin zero line, a rotation R_(n*pi/4) acts by(-1)^n
and Fi acts by+1. Its character is the sign of the permutation of
the three quaternion axes. In particular L^2 acts by+1, while s
and Delta act by-1. These follow by acting on the source's mixed
extremes, not from an assumed3x3 matrix.

Use normalized residue-one Szego sections. Under a compatible modular
map their scalar function has weight d=1, its derivative has d=2,
and wp has d=2. The constant function has d=0. The theta identities
give these laws, with character labels permuted. [Theta source](https://dlmf.nist.gov/20.7.viii).

For a half-root form line put k=5-2d. Equations(7) and(10) give
forward coefficient bar(j)^(k/2). Its actual norm rescales by
|j|^(-k/2). The normalized coefficient is consequently sigma_e^-k,
times kappa_a. A unit norm middle spin coefficient instead has
sigma_e, times its character kappa_spin.

Let v(tau)=eta(tau)/|eta(tau)|, a unit phase on the upper half-plane.
For q0, the standard eta law reads

    v(gamma_e tau)=chi_-1(e) sigma_e(tau) v(tau),
    chi_m(L)=exp(2*pi*i*m/24), chi_m(R)=chi_m(L)^-1,
    chi_m(J_h)=1.                                   (12)

This uses gamma_L:T^-1, not T. The normalized frame change
e_hat(tau)=v(tau)^(-k)e(tau) turns the form coefficient into
chi_-k kappa_a. For the spin line k=-1, giving chi1 kappa_spin.
The change is unitary and all interactions/measuring data transform
with it. It inserts no extra scalar line or adjustable coupling.
Only the eta phase is used, so its absolute cusp size never changes
the physical norm. [Eta source](https://dlmf.nist.gov/23.18.E5).

At the check point tau=i, s has sigma=exp(i*pi/4). The active simple
pole has eigenvalue exp(-3*pi*i/4) under s, and its inner factor
under Delta changes that to exp(pi*i/4). Under L^2, the eta frame
gives(-1) exp(-pi*i/2)=i. These two direct checks fix the signs.

## 7. Induce all modes and compare actions in the same convention

The bare active form line induces the oriented-axis representation A
of2O. Its stabilizer character is exactly(11). In unit phase frames
over axes(I,K,J) choose

    AL=[[1,0,0],[0,0,i],[0,i,0]],
    AR=[[0,-i,0],[-i,0,0],[0,0,1]].                    (13)

Conjugation by diag(-i,1,i) gives the literal adjoint rotations of
gL,gR on the imaginary quaternion axes in that order. Thus(13)
is an actual induction from the top-line action. It has rank3.
Let P+ be the ordinary axis-permutation module and P- its sign twist.
The trivial top line induces P+, and the middle spin line induces P-.

For q0, the full per-gauge-coefficient rank9 decomposition over the
three backgrounds is

| Top line | Form mode1 | Form mode2 | Spin mode |
| --- | --- | --- | --- |
| Active chi_p, p!=0 | chi21 A, simple pole | chi23 A, double pole | chi1 P- |
| Trivial | chi19 P+, regular | chi23 P+, double pole | chi1 P- |

Each entry has rank3. Use the actual positive Gram matrix to normalize
the modes. Its invariant regular/pole flag admits an orthogonal
complement under the unitary transport. That quotient keeps the
listed automorphy factor. The active odd/even Szego pair is also
orthogonal when the metric's inversion isometry is used.

The exact weave calculation already gives

    TD_L=chi21(L) AL, TD_R=chi21(R) AR.               (14)

W10 calls its contravariant right action D_e. Its left action is
U_e=D_(e^-1). The monomial TD_L,TD_R are symmetric and unitary.
Therefore(14), for the forward LEFT physical action used here,
matches the LEFT conjugate weave half, with matrices
conj(TD_L)^-1=TD_L and conj(TD_R)^-1=TD_R. Inner J_h actions also
match the corresponding parity signs. The central action is-1.
This fixes the conjugation label rather than dropping the action order.

The second form summand is chi2 times this one. It has a different
linear character. The spin and trivial-top summands have projective
permutation image, so none is silently replaced by the whole rank9.
Changing to q1 multiplies every half-root summand by chi12.

The opposite gauge representation supplies independent left fields.
Its highest flat character determines which row applies and is retained
from the full-E8 core-sign table. The coherent h4 and Zeta-h4 changes
exchange the active/trivial assignments together with their core signs.
The trace-dual adjoint-kernel and right-antiparticle maps use the actual
conjugate operator. No left field is removed by identifying it with
its Hermitian conjugate.

For the source +h4 and diagonal positive core signs, the active top
line occurs in the16 singlet and conjugate16 coloured coefficient.
The other two coefficients have trivial top line. Thus this particular
orbit triplet is not already a common family representation of the
complete charged roster. Its weak-current and interaction intertwiner
remains to derive in the same construction.

## 8. Vector companion, residual choices and acceptance status

The vector(10,6) form modes have J0=2 and trace-dual line S^4 G0^*.
Each of its two nontrivial character channels has one simple pole.
Formula(10) gives their actual fields, finite norm and graph-domain
membership. Their geometric normalized factor is sigma^-2, hence
chi22 after the same eta frame convention. Their two-channel gauge
map is the restriction of G(g) to the highest pair. In its A0 eigenbasis,
L^2 has opposite signs and s acts through the transported D-half
intertwiner. Its off-diagonal coefficient has the Spin10 phase.
Keeping that second generator proves this conditional form doublet's
irreducibility. A swap check alone does not.

The one vector spin zero is a section of the rank-two parabolic
extension S^3 E(V3)(p). Its full normalized generator phase has not
been evaluated here. Its determinant/extension identification over
moduli must be transported, not inferred from its one-dimensional H0.
Its actual action is given by(7)-(8) on that section. This is an
explicit remaining component of the acceptance task.

There is nevertheless a whole-block discriminator already proved by
(9). Every vector-companion mode is epsilon-even, whereas either
weave triplet is epsilon-odd. Thus no physical vector-companion
subrepresentation is that triplet in this completed action. Its bare
quaternion coefficient cohomology and the physical spin bundle differ
by their retained geometric factors. This statement is scoped to
this candidate and coherent completion.

This discriminator uses the full E action and its labelled epsilon.
For the braid subgroup, Delta^4=epsilon J_c also involves the based
inner action. A braid-only representation can behave differently.
Do not extend the full-E statement to that restriction without carrying
J_c and the actual gauge/reference quotient. The transport constructed
here is an equivariant field-family map, with its stated flat based
reference action. It does not assert a Berry or time-evolution law.

At tau=i, q0 and q1 give different linearized eigenvalues on the
active half-root branch. With the same labelled s and field reference,
the q0 spectrum is{exp(-3*pi*i/4),exp(-pi*i/4),exp(-3*pi*i/4)}.
The q1 spectrum is its negative. Selection, or an identification using
the full registering/measuring and gauge equivalence, remains a duty.
This calculation does not price those two descriptions as a new
independent physical bit without that equivalence audit.

The two lifts agree on ker(chi12). Restricting to that subgroup would
remove this difference, but needs its own derivation. chi12 is the
abelianization sign inside SL2Z. It is distinct from det=-1 versus+1
and from the one-tick/two-act question. Main's B1886 retains even-tick
observation as a condition for a weight to deliver. It does not supply
ker(chi12), so no such reduction is taken here. An extension to the
orientation-reversing tick and its Pin data remains a separate task.
Equation(9) is a statement on gauge-covariant physical field modes.
Zeta is an E8 gauge element. Any claim of an independent observable
family symmetry must also descend the full gauge/reference action and
transport the interaction tensors. That additional physical duty is
not discharged by the coefficient representation alone.

| Duty | Result at this checkpoint |
| --- | --- |
| Typed geometric spin/register completion | Two explicit coherent choices q0,q1 under stated marking and inner-path convention |
| Full action/norm/domain covariance | Exact conditional transport(7)-(9), with measuring data retained |
| Actual half-root modes and their transport | Explicit solutions and complete rank9 table if WP-3.1 supplies exhaustion |
| Odd scalar multiplier on active form line | Derived from S^5 Hodge weight within q0, giving one actual orbit triplet |
| Vector modes | Explicit form modes and central action, unresolved normalized spin-line phase |
| Input reduction | Full-E covariance restricts the geometric lift to two choices at fixed Pin2 gauge map, with no foundational choice certified removed |
| Three physical families in one vacuum | Requires the state/interaction join and complete SM weak-current test |

The next check is independent scrutiny of(3)-(14), especially the
action direction, based s/Delta distinction and eta-frame multiplier.
The next unfinished analytical piece is the vector spin-line transport,
followed by WP-3.1 exhaustion and the physical state/interaction meaning
of the orbit. No numerical control or banking acceptance is inferred.
