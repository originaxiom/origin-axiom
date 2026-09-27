# R53 authored proof: the actual curve has the earned harmonic velocity

September 27, 2026. Conditional on R42/R44 geometry and all-jet cusp,
R45 density/parent admission and complete domains, R47's actual family,
R49 closed-range/regularity, R50 zero-form inverse, R51 harmonic metrics
and R52 continuity/barrier. This is authored analysis, not independent
proof acceptance. Finite controls verify named identities, not the PDE.

## 1. Fix the problem and the correct Jacobi operator

Fix g0,H0,C0=A0+Psi0 at canonical q0>0,q0!=1. Write s=log(q/q0),
C_s=C0+s c+O(s^2) for R47's actual flat family, with all coefficient
parameter jets bounded in the fixed normalized charts. Set d=d_C0.
R52 supplies unique harmonic metrics H_s and positive H0-isometries
B_s with H_s=B_s^* H0 B_s, B_0=1. Put xi_s=log B_s, a trace-free
H0-Hermitian endomorphism. With the target metric (1/4)tr(H^-1 dH)^2,

    |xi_s|_(H0)=d_Y(H_s,H0)=f_s.

At this harmonic background the zero-form operator is

    J=d^dagger d=delta_A0 d_A0+sum_i ad(Psi0,i)^2.          (1)

Expanding delta_A[Psi,eta]+sum[Psi,d_A eta] cancels the first derivative
cross terms; the remaining term [delta_A Psi,eta] vanishes precisely
because the background moment map is zero. J preserves compact/skew
and Hermitian real subbundles. In R46's notation, for Hermitian eta,

    M(d eta)=J eta, G(d eta)=0,

and for compact eta,

    G(d eta)=J eta, M(d eta)=0.                            (2)

The transported connection has first variation c-d xi'_0 if the
derivative exists. Its moment equation consequently linearizes to
J xi'_0=M(c), with NO extra factor of two: xi is log B, not log H.

R49/R50 give a positive global gap for J and no trace-free zero-form
kernel. In particular every bounded smooth solution J eta=0 vanishes.
Indeed finite volume makes eta L2; multiplying by chi_T^2 eta gives
the Caccioppoli bound for ||d_A eta||^2+||[Psi,eta]||^2 by
4 integral |dchi_T|^2 |eta|^2. Complete cutoffs force both terms zero.
Then d_C eta=0, full holonomy density makes eta scalar, and trace zero
makes it zero. The same argument proves uniqueness among L2 solutions.
No boundedness of a general gauge primitive or positive quotient
injectivity radius is presumed.

## 2. Upgrade the compact anchor to a Lipschitz estimate at zero

Choose a compact core K containing the entire region up to R52's fixed
collar r0. Put A(s)=max_K f_s. This is a CORE maximum, not only a
boundary maximum; omitting the core would leave the normalization
uncontrolled inside. R51 gives A(s)->0. R52's barrier gives globally

    f_s <= A(s)+C|s|(1+r)                                (3)

after smoothly extending a nonnegative height to the core.

Suppose A(s) is not O(|s|). Then some s_j->0 has
A_j=A(s_j)>0 and |s_j|/A_j->0. On every compact set xi_sj/A_j is
uniformly bounded. The harmonic-metric equation, written in positive
matrix coordinates relative to H0, has scalar elliptic principal part.
Subtract the reference equation and use the mean-value identity for its
smooth matrix coefficients. Because H_s->H0 smoothly on compact sets,
the resulting LINEAR difference system has uniformly bounded smooth
coefficients there, with forcing O(|s|). Interior estimates therefore
give compact C^j bounds for the normalized difference for every finite j.
Converting to xi changes none of these bounds and linearizes smoothly.

A diagonal subsequence tends smoothly on compacts to eta with J eta=0.
Equation (3) implies |eta|<=1 at every point: the normalized slope tends
to zero. A maximizing point in the fixed compact K has a convergent
subsequence, so max_K |eta|=1. This contradicts section 1's bounded
kernel exclusion. Hence, for all sufficiently small s,

    A(s)<=C|s|,   |xi_s|<=C|s|(1+r).                      (4)

This is a derivative estimate at the canonical CENTER. It does not
yet bound differences at arbitrary noncanonical centers s*.

## 3. Identify the local derivative without assuming it

Now normalize by s rather than A(s). The same compact elliptic argument
gives subsequential limits zeta of xi_s/s, each satisfying

    J zeta=M(c),   |zeta|<=C(1+r).                        (5)

Linear growth is L2 in the canonical exp(-r) volume. An inhomogeneous
cutoff energy estimate puts zeta in the complete form domain, and its
weak equation puts it in Dom(J). Uniqueness in L2 gives

    zeta=G0 M(c),    G0=J^-1.                             (6)

All subsequences have this same limit, so xi_s/s converges in C-infinity
on compact subsets. This proves local differentiability at zero, not
yet the required derivative in the full nonlinear norm.

## 4. A rate-preserving global spatial estimate

We expose the elliptic constants needed to pass from local to X. On a
uniform lifted ball at height r, use a C_s-parallel frame normalized to
H0 at its center, as in R52. H0 has uniformly bounded positive matrix
jets there. Put E_s=H_s-H0 and L= C0+C|s|(1+r). Equation (4) gives

    |E_s|/|s| <= C(1+r) exp(C|s|r).                       (7)

R52 gives H_s and its inverse C^{2,alpha} bounds of the form
exp(C L)(1+L)^m on a smaller fixed ball. Take alpha=1/2 by decreasing
the local regularity exponent if needed. In this frame the exact
matrix equation is Delta_geo H=partial H H^-1 partial H, with g
contracting the indices. Subtract its H0 version, whose error and
fixed-order jets are O(|s|), to obtain

    Delta_geo E_s = P_s partial E_s+Q_s E_s+F_s,
    ||P_s||_(C^alpha)+||Q_s||_(C^alpha)<=B,
    ||F_s||_(C^alpha)<=C|s|,
    B<=C exp(C L)(1+L)^m.                               (8)

This is exact: use H_s^-1-H0^-1=-H0^-1 E_s H_s^-1 and expand one
derivative factor at a time. No nonlinear term divided by s is dropped.
To avoid an uncontrolled dependence of elliptic constants on B, restrict
to a concentric ball of radius rho=c(1+B)^-4. Under rescaling to unit
radius, the first- and zeroth-order coefficients and their alpha seminorms
are bounded by rho B, rho^(1+alpha)B, rho^2 B and rho^(2+alpha)B.
They are uniformly bounded. The rescaled principal metric has uniform
ellipticity and bounded jets by the lifted geometry. Interior Schauder
estimates on that ball thus have a constant independent of r,s.
Scaling back costs a finite power of rho^-1, still at most exp(C L)
times a polynomial in L. Equations (7)--(8) yield, for j<=2,

    |nabla^j E_s|/|s| <= C(1+r)^m exp(C|s|r).              (9)

There is no quotient covering loss here: the INPUT is a pointwise
distance bound on lifted balls, not a quotient-L2 mean-value estimate.
The small radius is an estimate device, not a new physical end cutoff.

Positive matrix square root is smooth. Along the positive segment
H0+tE_s its eigenvalues stay between the endpoint bounds. Its first
three Frechet derivatives are bounded by finite powers of inverse
minimum eigenvalue, by successive Sylvester equations. Since B_s-1
vanishes at E_s=0, differentiating this difference through order two
leaves at least one factor E_s or a derivative of E_s. Equation (9)
therefore holds also for B_s-1 and its first two spatial derivatives,
with changed finite constants. This retains noncommuting terms.

Writing the exact transported difference as

    u_s=B_s(C_s-C0)B_s^-1-(d_C0 B_s)B_s^-1

now gives |u_s/s|+|nabla(u_s/s)| bounded by the RHS of (9). Choose the
parameter interval so its fourth-power exponential rate is strictly
less than the volume decay rate one. Dominated convergence, using (6),
proves IN THE SAME X=Dom(Q0) intersect L4

    u_s/s -> v=c-d G0 M(c).                              (10)

The complete domain follows by inherited minimal=maximal cutoff theory.
The local derivative alone would not justify (10); (9) supplies that join.

## 5. Compact gauge gives the actual harmonic tangent

The derivative v is moment-flat but need not satisfy the compact
background-gauge condition. Put kappa=G0 G(c), a compact zero-form.
Equations (1)--(2) give G(v)=G(c) and M(d kappa)=0. The complete
Hodge decomposition for closed c then yields

    v-d kappa=c-d G0 d^dagger c=Pi_1 c=alpha.             (11)

This can be implemented by ACTUAL compact bundle isometries
U_s=exp(s kappa), not just formal gauge jets. To check their domain,
first apply R50's inhomogeneous estimate to d kappa, since
Q(d kappa)=G(c), and then to kappa, since Q kappa=d kappa. Both have
subexponential spatial jets of every fixed order and all finite Lp.
Unitarity gives ||U_s||=1, |U_s-1|<=|s||kappa| and Duhamel estimates
|nabla U_s|<=|s||nabla kappa|, with the corresponding second derivative
bound by |s||nabla^2 kappa|+s^2|nabla kappa|^2. These remain integrable
when combined with (9), choosing the small exponential margins first.

The compactly transported exact curve therefore still lies in X, and
its difference divided by s tends to alpha in X. It is horizontal AT
ZERO. We do not assert an exact nonlinear Coulomb slice for every s.
R47's compact detector has L(alpha)=12, so alpha is nonzero. Equally,
R52's full E8 longitude character has nonzero d/ds at q0!=1 and is
unchanged by either transport. An infinitesimal gauge conjugation under
the WHOLE parent has zero character derivative. Thus this velocity is
not removed by introducing complementary full-parent gauge parameters.

## 6. Quadratic physical normalization at this background

Use the SAME supplied twisted gauge action, fixed g0 and positive parent
trace as R46. The mixed scalar kinetic term has coefficient 1/g7^2;
see Braun et al., [equation (2.13)](https://arxiv.org/html/1812.06072v2).
Only its local nonabelian action and normalization are used, not the
later abelian background restriction or a global gravity embedding.
For the horizontal real amplitude s at the canonical center,

    K0=(60/g7^2) integral tr_4(alpha^dagger wedge *alpha),
    L_kin,quadratic=-K0 partial_mu s partial^mu s,
    0<K0<infinity.                                      (12)

The factor 60 is the RAW E8-adjoint trace restricted to sl4, already
checked by R45 and independently checked here from actual root weights.
Different trace conventions rescale g7; this is not a predicted coupling.
The real canonically normalized infinitesimal scalar is sqrt(2K0) s
if the convention is -1/2 times its gradient squared. For q rather
than log q the quadratic coefficient is K0/q0^2.

R47 gives explicit profile-dependent bounds

    (60/g7^2)144/||h||_2^2 <= K0 <= (60/g7^2)||c||_2^2,

where h is the actual compact detector's Riesz representative. No
numerical value of these global integrals or g7 is computed. Because
alpha is compact-gauge-horizontal, the linearized Gauss constraint
does not require a longitudinal correction to this kinetic norm.
R45's orthogonal parent branching is preserved by C0 and its adjoint;
thus the structure-adjoint harmonic equation also gives orthogonality
to gauge variations in every complementary parent summand.
This is a quadratic statement, not a proved consistent nonlinear
finite-dimensional truncation of the parent theory.

R52's exact static potential remains zero. Neither (12) nor that
classical flatness selects q, computes a quantum effective potential,
breaks R48 pairing, yields physical chirality or derives gravity.
This establishes differentiability at s=0 for each separately fixed
canonical base, not a C1/C2 theorem on an entire fixed-base interval,
the second derivative of R50's two-jet, or the full neutral spectrum.
