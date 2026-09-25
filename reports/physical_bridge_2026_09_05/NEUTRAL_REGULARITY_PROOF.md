# R49 authored argument: the neutral nonlinear-domain join

September 25, 2026. Conditional on the same R42/R44 canonical
background, all-jet cusp limit, compact core and complete domains.
R45 identifies End0(E) as the parent's neutral coefficient; R47 supplies
its nonzero harmonic direction. This is authored analysis with exact
finite controls, NOT independent analytic acceptance.

## 1. Normalize the actual limit rather than an equivalent metric

R44's product-cone solution is
u=-A z^(1/4)(X0-Y^2/2)^(3/8), A^8=2048/27.
At p=(1,1,0), its Blaschke metric in (X0,z,Y) is
[[15/64,-3/32,0],[-3/32,3/16,0],[0,0,3/8]].
Write w=(1,1,0,1), l=(3/8,1/4,0). The radial graph/tangent frame,
apart from its common factor 1/A, has columns
w, e0-l0 w, e1-l1 w, e2.
Transporting diag(1,h) through this frame gives
H_inf=A^2 diag(3/8,1/4,3/8,3/8).
The scalar A^2 cancels on End(E); the unequal entries must be retained.

Set r=log(R)/2 and v=2k t+r/2, k=log q !=0. R44's normalized spatial
vectors give, in the coframe (dr,exp(-r)dx,dv),

    g_inf=diag(a,a/2,a), a=3/4,
    dvol_inf=constant exp(-r) dr dx dv.                       (1)

For example the columns (2,1,0),(0,0,1),(0,-2,0) pull h to (1).
The exact connection, in the same moving frame, is

    C=C_inf+(beta/(2k)) exp(-2r) P (dv-dr/2),
    C_inf=H0 dr+N exp(-r)dx+(D/2)dv,                         (2)
    H0=2J-D/4=diag(1,0,0,-1), P=N^2.

The coefficient of the remainder and its covariant derivatives are
bounded for EACH FIXED q; no q->1 uniformity is asserted.

R44's pointed-domain all-jet convergence applies to the actual spatial
jets, not just metric values. In a normalized affine chart at each
point, take derivatives while its normalizing matrix is fixed; the
explicit derivatives of the moving frame are then given by (2).
Thus the actual base metric and induced coefficient metrics approach
(1) and H_inf, with their derivatives in the bounded vector fields dual
to this coframe. This is C^j convergence for every fixed finite j on
uniform lifted balls. No rate, smooth compactification, exact translation
symmetry, or polyhomogeneous expansion is assumed for the actual metric.
This transfer retains R44's external Benoist--Hulin input and its
authored global cusp/core obligations.

## 2. The complete constant-meridian indicial operator

Let A=ad(H0), B=ad(N), L=ad(D)/2 on sl4, with Gram metric induced by
H_inf. Then A^*=A, L^*=L, B^*=ad(N^T), [A,B]=B,
[A,B^*]=-B^*, and L commutes with A,B,B^*.

Separate meridian Fourier modes in the LIMIT MODEL only. On its
zero-meridian mode, write partial_r=lambda and partial_v=i nu.
The three covariant derivatives are X=lambda+A, Y=B, Z=i nu+L.
The exterior derivative includes d theta_x=-dr wedge theta_x.
For instance, on a one-form (u_r,u_x,u_v),

    d u=((X-1)u_x-Yu_r, X u_v-Zu_r, Y u_v-Zu_x).             (3)

The formal derivative adjoint for exp(-r)dr is -partial_r+1.
Using the positive form Gram matrices and (3), every exterior degree
has the same coefficient indicial Laplacian, with its form multiplicity:

    Delta_inf(lambda,nu)
       =(4/3) [(-lambda^2+lambda+nu^2) I + T],
    T=A^2+A+2 B^* B+L^2.                                   (4)

For example the off-diagonal r,x block is
2([A,B^*]+B^*)/a=0. The x,x alternative
A^2-A+2 BB^* equals A^2+A+2 B^*B.
The v cross blocks vanish because L is self-adjoint and commutes.
The code constructs (3) in ALL degrees from wedge signs, as a separate
check of the expanded component formula.

T is self-adjoint in the positive Gram metric. Its characteristic
polynomial and annihilating polynomial are

    det(z I-T)=z(z-2)^3(z-6)^11,
    T(T-2I)(T-6I)=0.                                       (5)

The zero-D-weight subspace has dimension nine, and instead has
multiplicities (1,3,5). The extra six adjoint directions are NOT
discarded: their nonzero L^2 adds to the coefficient potential.
One can understand (5) by the SL2 action on V3 plus its singlet line:
End(V3) contains spins 0,1,2, and each off-diagonal V3/line block
has spin 1 and L^2=4. The explicit commutator calculation, not this
naming, certifies the actual representation and positive metric.

At nu=0, the radial roots are (0,1),(-1,2),(-2,3).
A coefficient exp(lambda r) is L2 only if Re(lambda)<1/2;
L4 needs Re(lambda)<1/4. Nonzero nu changes each root to
(1 +/- sqrt(1+4(T_eigen+nu^2)))/2, so the nonpositive branch
does not acquire a root in (0,1/2).
These are MODEL exponents, not an asserted expansion of actual modes.

For compactly supported model forms on the zero-meridian sector,
conjugate u=exp(r/2)w. Equation (4) becomes the positive radial form

    (4/3)( ||partial_r w||^2
             + <w,(1/4+T-nabla_v^2)w> ).                    (6)

Its exterior lower bound is 1/3 in every degree. This number uses
the normalized internal Blaschke metric, not physical units or a
measured mass. A global kernel is entirely compatible with this
EXTERIOR estimate.

## 3. The nonzero meridian modes and perturbation to the actual end

On each nonzero meridian frequency omega=2 pi n, the model operator is
partial_x+exp(-r)B. B is nilpotent (B^5=0), so

    (i omega+exp(-r)B)^-1
      =sum_{j=0}^4 (-exp(-r)B)^j/(i omega)^(j+1).

The model full-complex Cartan homotopy obtained by contraction with
partial_x has norm O(exp(-r0)) on r>r0, since that vector shrinks.
Flatness includes the radial equation. Exactly as in R46, its pairing
with a compactly supported form gives a lower bound
c exp(2r0) on this nonzero-frequency subspace. The zero-frequency
inverse does not exist and is not used. The model metric, connection
and operator commute with meridian translations, so these Fourier
subspaces are orthogonal for both norm and quadratic form.
For a sufficiently deep tail, (6) is therefore the lower bound 1/3
for the WHOLE model adjoint complex, not only the nine zero weights.

To transfer the bound, identify the actual and model Hilbert bundles
unitarily using their positive metric/volume square roots. Section 1
gives, for compact smooth v supported far out,

    ||(Q_actual-Q_inf)v|| <= epsilon(r0)(||nabla_inf v||+||v||),
    epsilon(r0)->0.                                        (7)

The model has uniformly bounded local geometry and connection
coefficients/curvatures on its lifted balls. The integrated local
Dirac/Weitzenbock estimate gives
||nabla_inf v|| <= C(||Q_inf v||+||v||).
This estimate does not require a positive injectivity radius on the
quotient: it is a local covariant identity integrated on compactly
supported forms. Collapse is handled separately below.
Combining with (7) transfers the quadratic bound with an arbitrarily
small loss. Thus for every gamma<1/3 there is r0 such that

    ||Q_actual v||^2 >= gamma ||v||^2, supp v subset {r>r0}.  (8)

The actual metric need NOT preserve a Fourier mode or the peripheral
weight splitting. Those are used only to prove the reference estimate.
The perturbation is on the FULL fifteen-dimensional coefficient.

The complete-domain cutoff argument of R45 extends (8) to its form
domain. Compact-core elliptic Rellich compactness plus (8), as in
R44 section 5, gives finite-dimensional harmonic spaces, closed ranges
of the Hilbert complex, and a positive spectral gap on the orthogonal
complement of each global harmonic space. No numerical GLOBAL gap or
full neutral H1 dimension has been computed. R47's nonzero H1 remains;
it is not killed by an exterior threshold.

## 4. Weighted decay, with the collapsing-volume factor retained

Let alpha be a complete L2 harmonic form with End0(E) coefficients.
For ANY fixed 0<epsilon<1/2 choose a tail so that (8)'s gamma exceeds
(4/3+o(1))epsilon^2, with a small margin. Here
|dr|_actual^2 ->4/3 by section 1.

Apply (8) to f_T alpha, with
f_T=chi(r) exp(epsilon min(r,T)), where chi vanishes on the core
and equals one farther out. For each finite T this bounded Lipschitz
multiplier preserves the complete domain. The commutator is Clifford
multiplication, Q(f_T alpha)=c(df_T)alpha.
Use |d(chi exp(epsilon r))|^2 with factor 1+eta on the exponential
part and a fixed compact-annulus remainder. Choose eta small enough
to preserve the margin; a fixed factor two would unnecessarily lose
part of the allowed epsilon range. Absorb and take T to infinity:

    integral exp(2 epsilon r)|alpha|^2 dvol < infinity
                    for every epsilon<1/2.                 (9)

This is an L2 WEIGHT estimate, not pointwise decay by fiat.
Lift a fixed-small-radius ball about a point at height r to the
unwrapped cusp, taking its radius smaller than a fixed longitudinal
period and radial band. The normalized projective charts give uniform
elliptic estimates on that lifted ball. Its projection covers at most
C exp(r) fundamental meridian cells; the nonshrinking longitudinal
direction adds only a fixed factor. Norms are measured using the
equivariant positive bundle metric, so nonunitary flat holonomy is
not an extra unbounded multiplier. Therefore

    |alpha(p)| <= C exp(r/2) ||alpha||_(L2(quotient band))
               <= C_epsilon exp((1/2-epsilon)r).             (10)

The compact core is handled by ordinary elliptic regularity.
For any finite p>=2 select epsilon with 1/2-1/p<epsilon<1/2.
Equation (10) and dvol asymp exp(-r)dr dx dv give alpha in Lp.
In particular epsilon=3/8 supplies an integrable fourth-power bound.
There is NO L-infinity conclusion from this argument: its constants
may diverge as epsilon approaches 1/2.

The scalar counterexample exp(3r/8) is L2 but not L4 with this volume.
It explains why R47's quadratic norm alone was insufficient. The
operator and the covering factor, not just finite volume, pay the
additional regularity.

## 5. What this pays in the parent action, and what it does not

R47's nonzero harmonic projection alpha is now in
X=Dom(Q) intersect L4, the sufficient nonlinear space of R46.
The positive invariant bracket gives alpha wedge alpha and the
quadratic moment-map residual in L2. All straight-line quartic
coefficients of the supplied residual-square action are finite.
For u=s alpha, with its compact/skew and Hermitian split a+psi,
the linear curvature and moment-map residuals vanish. Its potential
begins as the finite nonnegative expression

    V(s alpha)=(2 s^4/g7^2)
       (||alpha wedge alpha||^2
          +||sum_i [a_i,psi_i]||^2).                         (11)

The index contraction uses the actual metric. No value or
nonvanishing of this global profile integral is computed here.
A nonzero straight-line quartic would NOT alone obstruct a curved
flat branch: massive fields can relax at order s^2. Conversely finite
quartics do not prove a nonlinear harmonic-flat branch, select q,
or stabilize an asymmetric phase. Those require solving the coupled
equations and their obstruction/response, with actual profiles.

The parent's field dictionary, normalized physical couplings, quantum
phase, anomalies, source/end/parameter selection and gravitational
completion remain duties. R48's classical duality persists. R40/R41
is a separate source/coefficient route. The scope is nonlinear
ADMISSIBILITY of canonical adjoint harmonic modes, not physical TOE
completion or a no-go on the wider relational object.
