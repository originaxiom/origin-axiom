# R52 authored proof: continuous exact fields in the same action domain

September 27, 2026. Conditional on the R42/R44 canonical complete
geometry and all-jet end control, R45 density/parent admission, R47
fixed-bundle flat family, and R51 existence/uniqueness/local continuity.
This is NOT independently reviewed analysis or a machine-certified PDE
theorem. Finite symbolic checks support only the named identities.

## 1. Small reference tension on the fixed base

Fix q0>0, q0!=1, C0, H0 and g0. Put s=log(q/q0). The actual family
C_s=C(q) is flat; R47 constructs its smooth core trivialization and tail

    a_s=C_s-C0=[s D+(beta(q)-beta(q0))P/R]dt.

For sufficiently small |s|, all fixed-order spatial jets of a_s are
O(|s|) in the uniformly normalized lifted charts of R44/R49. The tail
formula proves this there; the remaining region is compact. The fixed
metric H0 and C0 have uniformly bounded jets in those charts.

In the fixed H0 split a_s=b_s+c_s (compact plus Hermitian), R46's exact
moment expansion is its linearization minus sum_i[b_s,i,c_s,i]. Thus
the moment defect of (C_s,H0) is uniformly O(|s|). Harmonic-map tension
differs only by a fixed normalization. Consequently

    |tau_(C_s) H0| <= K |s|                                  (1)

globally, for a constant independent of s in this small interval.
No new harmonic metric or a changing base metric is used in (1).

## 2. A linear target-distance barrier, not a bounded-gauge claim

Let H_s be R51's unique finite-energy C_s-harmonic metric and
f_s=d_Y(H_s,H0), Y=SL4(C)/SU4 with its positive trace metric. Both are
sections of the SAME flat target bundle. Finite energy of both gives
|df_s|<=|dH_s|+|dH0| in L2; R51's anchored cusp Hardy estimate gives
f_s in L2. Joint convexity of distance on the Hadamard product Y x Y,
the chain rule, harmonicity of H_s and (1) yield weakly

    Delta_geo f_s >= -K |s|.                                (2)

For precision use sqrt(d_Y^2+epsilon^2). It is convex on the product,
each endpoint gradient has norm at most one, and it decreases to d_Y.
The tension of the first endpoint vanishes; the second contributes at
worst minus its norm. Distributional passage to the limit gives (2).
Here Delta_geo=div grad, opposite to the nonnegative Hodge convention.

Write r=log R/2. The fixed end converges with all finite spatial jets to

    g_inf=a dr^2+(a/2)e^(-2r)dx^2+a(2k0 dt+dr/2)^2, a=3/4.

In this metric Delta_geo r=-1/a. The actual all-jet convergence, not
mere quadratic-form comparison, implies Delta_geo r -> -1/a. Choose
one fixed deep collar r0 and b>0 such that Delta_geo r<=-b on its end.
Set C(s)=max_(r=r0) f_s. R51 local smooth-topology continuity gives
C(s)->0 as s->0, and bounded C(s) on a smaller closed interval. Define

    w_s=C(s)+(K/b)|s|(r-r0).

Then Delta_geo(f_s-w_s)>=0 and f_s-w_s<=0 at the inner boundary. Both
f_s and w_s are in H1 intersect L2; linear r and bounded dr are square
integrable against the canonical e^(-r) density. Let z=(f_s-w_s)_+.
Its inner trace vanishes. Testing the weak inequality with chi_T^2 z,
using complete cutoffs, gives

    integral chi_T^2 |dz|^2 <= 4 integral z^2 |dchi_T|^2 -> 0.

So z is constant, and its zero inner trace makes it zero. No outer
boundary value was assumed. We have the actual-end bound

    0 <= f_s <= C(s)+A|s|(r-r0).                             (3)

This permits the R51 linear radial resonance; it does not assert that
the complex isometry is bounded, or that C(s)=O(|s|).

## 3. Explicit growth class for spatial derivatives

Use uniform fixed-radius lifted balls from R44/R49, not quotient balls
with an assumed injectivity radius. Their domain elliptic constants,
finite metric jets and Ricci lower bounds are uniform. On each doubled
ball choose a C_s-parallel frame normalized to H0 at its center p.
Bounded coefficients and their jets on this simply connected chart give
uniform local bounds for the frame change and H0, independent of p,s.

On the ball, |r-r(p)| is bounded. By (3) the harmonic H_s image lies in
a target ball of radius L_p=C_0+C(s)+A|s|r(p), enlarging C_0 as needed.
The local harmonic-map gradient estimate gives |dH_s|_Y<=C L_p on a
smaller ball. A precise primary statement is Riestenberg--Smillie,
[section 2.3, Proposition 20](https://arxiv.org/html/2511.11469v3#S2.SS3),
with radius rescaled to our fixed ball. Only this LOCAL estimate is
used, not the paper's global stability theorem.

Here is why subsequent constants grow at most exponentially in L_p.
In the parallel frame H=H_s is a positive determinant-one matrix. The
target-distance bound gives ||H||+||H^-1||<=C exp(c L_p). The intrinsic
gradient bound then gives ||partial H||<=C exp(c L_p)(1+L_p). Its
harmonic equation is the componentwise uniformly elliptic system

    Delta_geo H = g^{ij}(partial_i H)H^-1(partial_j H).       (4)

The right side is bounded by exp(c L_p) times a polynomial in L_p.
Interior W^{2,p} estimates with p>3 yield the same growth class for
C^{1,alpha} norms on a smaller ball. Derivatives of the inverse use
partial H^-1=-H^-1(partial H)H^-1, so the RHS is C^{0,alpha} with
the same type of bound. Interior Schauder estimates give C^{2,alpha}
bounds of this type. Only finitely many products, inverse factors and
uniform DOMAIN elliptic constants occur; an uncontrolled double
exponential in target radius is not being hidden in a regularity claim.

## 4. Positive isometry, actual transport and the complete domain

Let K_s=H0^-1/2 H_s H0^-1/2 and S_s=K_s^1/2. The positive H0-self-adjoint
bundle isometry from H_s to H0 is

    B_s=H0^-1/2 S_s H0^1/2,  B_s^* H0 B_s=H_s, det B_s=1.

It is intrinsic under bundle frame changes. Its derivatives need not
commute with it. Differentiating S_s^2=K_s gives the Sylvester equations

    S dS+dS S=dK,
    S d_i d_j S+(d_i d_j S)S=d_i d_j K-d_i S d_j S-d_j S d_i S.

On Hermitian matrices the inverse Sylvester operator has norm at most
1/(2 lambda_min(S)). The eigenvalue bounds in section 3 therefore give
B_s, B_s^-1 and two spatial derivatives bounds of the form
C exp(c L_p)(1+L_p)^m. H0 has bounded jets in the chosen charts.

Transport the whole connection by this isometry:

    C'_s=B_s C_s B_s^-1-(dB_s)B_s^-1,  u_s=C'_s-C0.         (5)

H_s-harmonicity becomes H0-harmonicity of C'_s; flatness is preserved.
Complex gauge here CONSTRUCTS another physical field configuration;
it is not declared a physical redundancy. At s=0, B_0=1 and u_0=0.
Equations (3)--(5), in the uniformly bounded fixed-background frames,
imply for some finite constants C,L,m

    |u_s|+|nabla_0 u_s| <= C(1+r)^m exp(L |s| r).            (6)

Choose epsilon>0 with 4L epsilon<1 (if L=0 take any sufficiently small
interval). The canonical volume density is comparable to e^(-r).
Thus (6) supplies a single L4 envelope for u_s and L2 envelope for its
first derivative for |s|<=epsilon. Q0 has bounded zeroth-order
coefficients in these charts; hence u_s and Q0 u_s are L2. Completeness
identifies the maximal and minimal Q0 domains by R44/R45's cutoff
argument. Therefore u_s belongs to the SAME X=Dom(Q0) intersect L4.

R51's local C-infinity continuity, smoothness of positive matrix square
root and (5) give local convergence of u_s and its spatial derivatives
as s varies. Dominated convergence with (6) proves

    s -> u_s is continuous in X; ||u_s||_X -> 0 as s->0.     (7)

The split C'_s=A'_s+Psi'_s solves all three exact residual equations.
R46's residual-square potential is a nonnegative C1 polynomial on X;
therefore V(u_s)=0 and dV(u_s)=0. This is an actual continuous family
of admissible stationary configurations, not merely R50's two-jet.

## 5. Distinct orbits in the full supplied parent

A defining SL4 trace is not automatically an invariant under the full
parent gauge group. Use the adjoint character instead. R45 admits
248=(45,1)+(1,15)+(10,6)+(16,4*)+(16*,4).
For the actual preferred longitude Lambda(q), the literal generators
give T4=3q+q^-3, T4*=3q^-1+q^3 and T6=3(q^2+q^-2). Consequently

    T248=54+48(q+q^-1)+30(q^2+q^-2)
              +16(q^3+q^-3)+3(q^4+q^-4).                  (8)

The producer checks this using literal longitude matrices and exterior
minors and independently R45's actual parent root-weight enumeration.
The fixed mu4 twist is trivial on the preferred longitude (zero knot
abelianization), so it does not alter this detector. Moreover

    q dT248/dq=(q-q^-1)[48+60(q+q^-1)+48(q^2+1+q^-2)
                                  +12(q^3+q+q^-1+q^-3)].

The bracket is positive for q>0. Thus (8) is strictly monotone on EACH
side of 1. It is reciprocal-symmetric, so no global q-versus-1/q
distinction is claimed. The small interval avoids 1. Transport (5)
conjugates longitude holonomy and cannot change (8). Distinct nearby
q give distinct full-parent gauge orbits. The classical minima are
therefore non-isolated within the declared X configuration space.

## 6. Scope and the remaining physical join

Continuity is not differentiability. We have not bounded C(s)/|s|,
identified u'_0 with R47's compact-gauge-fixed harmonic mode, or proved
a finite-positive normalized collective-coordinate kinetic tensor.
Finite L2 differences of static fields do not prove a finite L2 time
derivative. R50's two-jet remains separate until that identification.

This local result does not select q, classify all minima, lift the
classical flat direction quantum mechanically, break R48 pairing,
supply a physical chiral spectrum or gravitational dynamics. It does
not prove the supplied action/parent is forced by the object or nature.
Other coefficient/source/end routes remain open in their stated scope.
