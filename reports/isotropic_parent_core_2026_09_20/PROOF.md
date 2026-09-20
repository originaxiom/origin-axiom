# F06 authored candidate: an isotropic full-parent core and its metric price

This argument is frozen before execution. It constructs a LOCAL smooth
solution of specified classical gauge equations on a chosen metric.
It is not a complete physical theory or a fixed-hyperbolic-base solution.

## 1. Finish the isotropic-current equations, not only their projection

Use R39's D5-singlet su4 and its fundamental positive metric. Let U and
N_i be as in DESIGN. The exact algebra is

    [U,N_i]=4 N_i, [N_i,N_j]=0,
    sum [N_i,N_i dagger]=U.

For an arbitrary smooth positive v and positive constant a, set

    g=v^2 delta, h=d log(v)/8,
    C_i=h_i U+a v^-1/2 N_i.

Since dh=0 and d(v^-1/2 dx_i)+4h wedge(v^-1/2 dx_i)=0,
the entire connection is flat. Its off-diagonal Gram matrix is
G=a^2 v^-3 I3, so its lower traceless moment component vanishes.
The remaining off-diagonal equation is also zero:

    div_g(alpha_a)-4 h.alpha_a
      = a v^-3 partial_a(v^1/2)-a partial_a(v)/(2v^(7/2))=0.

Finally div_g h=(Delta_0 v)/(8v^3). Substitution in the full matrix,
not merely its U projection, gives

    I = (Delta_0 v+4a^2) U/(4v^3).                  (1)

Thus every positive solution of Delta_0 v=-4a^2 gives a smooth local
source-free BPS solution in the full parent subalgebra. All E8 residual
components vanish under the existing SU4 embedding, and the residual-
squared classical potential has zero first variation in compactly
supported parent directions. This does not derive a gravity action.

The charge-four ONE-FORM fields supply this current; no new propagating
zero-form Q or external prescribed density has been inserted. It is not
R29's scalar source action. In particular div h=-a^2/(2v^3) has the alpha
row's sign. The dual C'=-C^T solves the same equations and reverses h.
One must track this sign and the charged representation before attempting
any source or spectrum identification.

An explicit family is

    v=c-(2a^2/3)(x1^2+x2^2+x3^2), c>0.             (2)

On every closed ball r<=r0<sqrt(3c/(2a^2)) it is positive, smooth and has
bounded positive metric and finite positive Higgs norm. All curvature,
Higgs and connection components are smooth, including the center.

## 2. The price is geometric, not a new impossibility theorem

Directly for g=v^2 delta in dimension three,

    Ric_ij=-v_ij/v+2 v_i v_j/v^2-delta_ij Delta_0 v/v,
    R=-4 Delta_0 v/v^3+2|dv|_0^2/v^4.

Equation (1) therefore implies

    R=16a^2/v^3+2|dv|_0^2/v^4>0.                  (3)

This restricted isotropic-coordinate ansatz cannot be the curvature-minus-
one hyperbolic metric. For example v=1/z gives R=-6 as it must, but its
moment residual is (1/2+a^2 z^3)U, never zero for real a>0. This excludes
that choice within this ansatz, not all isotropic coframes, nonzero B/beta
fields, other harmonic metrics or deformed internal geometries.

The original figure-eight/cover metric is not silently replaced. The
positive (2) is a candidate local core whose global matching and geometric
origin remain unsolved. A supplied metric change is physical input until
the same theory derives it.

## 3. An explicit, separately priced Einstein--harmonic-map comparison

The defining-four Higgs tensor and its trace are

    S_ij=Tr(Psi_i Psi_j)=3 v_i v_j/(16v^2)+a^2 delta_ij/(2v),
    |Psi|_g^2=3|dv|_0^2/(16v^4)+3a^2/(2v^3).       (4)

Consequently (3) obeys R=(32/3)|Psi|^2. A trace equation is NOT enough
to infer the tensor equation. Retaining its missing part gives, on (1),

    Ric_ij-(32/3)S_ij=-(v_ij+(4a^2/3)delta_ij)/v. (5)

For (2) the full right side vanishes. Conversely (5) forces this Hessian
within the ansatz; adding an arbitrary non-affine harmonic function keeps
(1) but generally breaks (5). For example epsilon(x1^2-x2^2) is a
trace-free-Hessian countercontrol wherever v stays positive.

For context, choose the AUXILIARY three-dimensional Einstein--harmonic-map
action integral sqrt(g)(R-k|Psi|^2), with fixed flat-bundle data and its
positive Hermitian reduction as map variable. Its harmonic-map equation
is d_A^*Psi=0. Compactly supported metric variation yields
G_ij=k(S_ij-g_ij|Psi|^2/2); in three dimensions its trace gives R=k|Psi|^2
and hence Ric_ij=k S_ij. Thus (2) supplies a local solution for k=32/3
in the displayed defining-four normalization.

This is an exact compatibility comparison to an explicitly chosen action,
NOT a derived action of the programme, the stress tensor of every SYM
term, a selected coupling, an observed Newton constant or a four-dimensional
Lorentzian gravitational solution. The value changes with the trace
normalization. No torsion-free G2 metric is constructed from it.

## 4. The boundary cannot disappear from the argument

Put R0=sqrt(3c/(2a^2)). The radial proper distance to v=0 is finite:

    integral_0^R0 v dr=(2/3)c R0.

The metric degenerates there. With r<R0 the norm density in radial
Euclidean coordinates is

    4 pi r^2 [a^4 r^2/(3v)+3a^2/2].               (6)

Its product with R0-r tends to pi a^2 R0^3>0. Therefore the maximal
positive ball has logarithmically divergent Higgs norm, despite every
smaller ball having finite norm. It is not a smooth complete background
of the kind F02/F05 assumed, nor a counterexample to F01.

On a sphere of radius r0<R0 the h flux is

    integral_boundary h(n) dA = -2 pi a^2 r0^3/3,

equal to the integral of div_g h. The nonzero boundary term is essential.
No matching to a hyperbolic exterior or source interface follows just
from assigning it a name. Fields, metric and the necessary interface
conditions must be solved together; here they have not been.

## 5. A pointwise escape from F05 positivity is not a massless particle

At a=c=1 and x=0, the orthonormal Higgs matrices are
S_i=(N_i+N_i dagger)/2. For u in Lambda^1 tensor C4 write
u_i=t_i e0+sum_j b_ij e_j. Direct wedge/contraction algebra gives

    ||T u||^2+||T* u||^2
      = (|tr b|^2+2 sum|t_i|^2+sum_(i<j)|b_ij-b_ji|^2)/4.

The eigenvalues of H1=T*T+TT* are 0 (five), 1/2 (six), and 3/4 (one).
The zero subspace is the symmetric trace-free b space. These are form/
coefficient components at ONE POINT, not five species or generations.

In this background the FULL covariant derivative of Psi does not vanish,
although its traced divergence does. Thus Delta_C includes mixed terms;
the homogeneous F05 identity Delta_C=Delta_A+H_p and its 9/4 bound are
not transferable. A pointwise H_p kernel, or failure of a particular
bound, proves neither a zero eigenfunction nor a nonzero net index.

Computing the physical spectrum requires a global background, positive
kinetic metric and justified boundary/end domain. This checkpoint earns
the local PDE construction and its explicit geometric constraints only.
