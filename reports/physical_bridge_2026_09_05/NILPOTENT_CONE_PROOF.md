# A local logarithmic solution retaining the canonical peripheral pair

September 30, 2026. R66 authored analysis, frozen before execution.
Finite algebraic checks do not independently certify this existence proof.
All conclusions are conditional on the metric, adjoint and action below.

## Actual coefficient data and metric

In zero-based four-dimensional matrix notation set

    N=E02+E23, P=N squared=E03,
    D=diag(1,-3,1,1), H=diag(1,0,0,-1),
    k=log(q), beta=6/(q-q inverse), q>0, q!=1.

The explicit basis in canonical_cusp.py conjugates the actual meridian
to exp(N)=1+N+P/2 and longitude to q^D(1+beta P). This is a Jordan
normal form, not a normal operator. N cubed=0, P squared=0, [N,P]=0;
D commutes with N,P and their adjoints. Also [H,N]=N, [H,P]=2P,
[N,N dagger]=[P,P dagger]=H. The positive trace norms squared of
H,N,P,D are respectively 2,2,1,12.

Take dr squared+r squared h_link, with period-one rectangular torus,
h_link inverse=diag(alpha,1/alpha), alpha>0, unit area. These are supplied
metric units and marking, not a physical scale prediction. The action
has integrand 2 norm(F_C) squared+norm(I) squared/2, times its supplied
positive coupling, where

    I=div(C+C dagger)+g^{ij}[C_i,C_j dagger].

## Exact equations

For real h(r), let G=exp(-h H) and C0=N dx+(kD+beta P)dy. Then

    C=G C0 G inverse-dG G inverse,
    C_r=h' H, C_x=exp(-h)N, C_y=kD+beta exp(-2h)P.

Coordinate differentiation, including C_r, gives F_C=0 identically.
The remaining residual is

    I={2(r squared h''+2r h')+alpha exp(-2h)
       +(beta squared/alpha)exp(-4h)}H/r squared.          (1)

The moment equation is precisely that the braces vanish. Omitting or
reversing C_r spoils flatness. A nonzero inverse-link cross component
adds beta exp(-3h)h^{xy}(E02+E20-E23-E32)/r squared. Hence this scalar
ansatz does not solve arbitrary nonrectangular links; no hexagonal-link
conclusion is borrowed. The reducible block inclusion diag(C,0) preserves
the two equations in SL5, but is E4 plus 1, not the monomial rank-five
family or a new Standard Model realization.

## Existence for every fixed parameter pair

Put s=-log(r), u=exp(-2h)>0, v=dh/ds. Equation (1) becomes

    du/ds=-2uv,
    dv/ds=v-(alpha u+(beta squared/alpha)u squared)/2.

For z=v-alpha u/2, the system is

    du/ds=-alpha u squared-2uz,
    dz/ds=z+(alpha squared-beta squared/alpha)u squared/2
             +alpha uz.                                 (2)

Its linearization is diag(0,1); the remaining vector field is polynomial
and vanishes to second order. The local center-manifold theorem applies.
Specifically, [Sideris section 9.1](https://web.math.ucsb.edu/~sideris/pdffiles/BookPublishedComplete.pdf),
Corollary 9.1, gives a C1 invariant graph z=eta(u), tangent to z=0.
Theorem 9.2 estimates that graph from an approximate invariant graph and
its invariance residual. This application does not assume an analytic
graph, uniqueness of a global center manifold, or convergence of a
formal series. The proof of Theorem 9.2 cited by Sideris is an external
input, not a proof reproduced here.

Let gamma=(beta squared-alpha cubed)/(2alpha). The graph
z=gamma u squared has invariance residual
3alpha gamma u cubed+4gamma squared u fourth. The graph
z=gamma u squared-3alpha gamma u cubed has residual O(u fourth).
Theorem 9.2 therefore supplies a local invariant graph with

    v=F(u)=alpha u/2+gamma u squared+O(u cubed).            (3)

For sufficiently small u>0, alpha u/4<F(u)<3alpha u/4.
On the graph, u decreases and stays positive: its derivative lies
between -3alpha u squared/2 and -alpha u squared/2. These comparison
bounds prevent reaching zero in finite s, keep the trajectory inside
the local chart for all later s, and imply u tends to zero. Local ODE
regularity then gives an exact smooth h(r) for all sufficiently small
r>0, satisfying both full equations. The collar size may depend on
alpha,beta; no uniform limit as q approaches one is asserted.

Writing zeta=1/u gives zeta_s=alpha+2gamma/zeta+O(zeta^-2).
First zeta/s tends to alpha, then zeta-alpha s=O(log s). Subtracting
(2gamma/alpha)log s leaves derivative O(log s/s squared), which is
integrable. Thus

    zeta=alpha s+(beta squared-alpha cubed)/alpha squared log s+O(1),
    h=log(alpha s)/2+
       (beta squared-alpha cubed)/(2alpha cubed) log(s)/s+O(1/s),
    v~1/(2s).                                           (4)

This is an existence argument, not an observed numerical fit.

## Exact comparator and a failed approximation

When beta squared=alpha cubed, the elementary function
h=log(alpha(s+c))/2, s+c>0, solves (1) exactly. On the square alpha=1,
beta=+1 and -1 correspond to q=3+sqrt(10) and sqrt(10)-3. These are
comparators, not selected physical parameter values.

For general beta the same elementary leading expression instead gives

    I=(beta squared-alpha cubed)H/[alpha cubed r squared(s+c) squared].

Its residual-action density is
(beta squared-alpha cubed) squared/[alpha^6 r squared(s+c)^4].
Unless the coefficient vanishes, the improper integral diverges.
Consequently keeping only the leading logarithm does not establish
finite action. The exact branch in (3) is essential.

## Holonomy and the bounded transport hypothesis

For each r>0, the peripheral matrices are simultaneously conjugated by
G to

    M_r=1+exp(-h)N+exp(-2h)P/2,
    L_r=q^D[1+beta exp(-2h)P].

They retain the complete original peripheral representation at every
positive radius. M_r-1 has nilpotency index three there. As r tends to
zero, M_r tends to 1 and L_r to q^D. By (4), the condition number of G
is exp(2h)~alpha s, which diverges. Moreover rC_r=-vH tends to zero but
is not O(r^delta) for any delta>0. This is outside R65's bounded radial
transport class, not a contradiction of its theorem. G is a complex
change of metric frame, not an admitted compact gauge identification.

## Action and the old fluctuation space

The limiting reference is C_infinity=kD dy. It is flat and moment-flat,
but it is not R62's constant-helicity wX background. Put a=C-C_infinity.
The metric and positive trace norm give the radial densities

    r squared norm(a) squared=2v squared+2alpha u+beta squared u squared/alpha,
    r squared norm(C) squared=previous+12k squared/alpha,
    r squared norm(Psi) squared=2v squared+alpha u+12k squared/alpha
                               +beta squared u squared/(2alpha),

where Psi=(C+C dagger)/2. These are integrable against dr near zero:
dr has magnitude exp(-s)ds and the a-density is asymptotic to 2/s.
This connection norm is a calculation in the declared frame, not a
gauge-invariant physical energy by itself.

However the L4 density of a is asymptotic to 4/(r squared s squared).
It is not integrable. Directly d_Cinfinity a=-a wedge a, and

    r squared norm(d_Cinfinity a) squared
      =[2alpha v squared u+4beta squared v squared u squared/alpha]/r squared
       ~1/(2r squared s cubed),
    d_Cinfinity dagger a=(v-v_s)H/r squared
      =[alpha u+beta squared u squared/alpha]H/(2r squared),
    r squared norm(d_Cinfinity dagger a) squared
       ~1/(2r squared s squared).

Both graph terms diverge separately. Hence the exact solution is NOT
an admissible fluctuation in the old graph-plus-L4 space about this
reference. This does not prevent studying it as a different background
with its own relative domain; that new domain must be justified.

For the exact solution F_C=I=0 pointwise and the supplied residual-square
integral is zero. On a singular space this alone neither proves that
all uncompleted-square action terms are finite nor licenses discarding
boundary contributions. The physical variational law, coupled fermion
domain, compact gauge group, global core extension and normalized
observables remain necessary. There is no claim of physical chirality,
global stability, a selected link metric or completed physical theory.
