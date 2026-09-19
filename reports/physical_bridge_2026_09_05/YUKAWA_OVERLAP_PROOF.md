# R36: charged overlap identity on the declared compact source model

2026-09-19. Authored pre-execution argument, not independent proof
acceptance or a global eigenfunction computation. The working derivation
at febedec0 is prior, not a blind prediction. Four-dimensional spacetime,
the positive kinetic space and the added scalar coupling remain inputs.

## 1. Which fields and which normalization

Use R30's compact absolute realization of d_q=d_A+q dF wedge on a
unitary flat line L. At fixed source width, R29/R31 give bounded F,dF
and bounded Delta F. On smooth compact Q the scalar H0=d_q^*d_q has
Robin data D_n u+q F_n u=0. Let its exact positive eigenfunctions be
orthonormal, H0 u_i=lambda_i u_i, and v_i=d_q u_i/sqrt(lambda_i).
Hilbert-complex pairing gives normalized one-form partners. This is
the R31 scalar/one-form subsector, not every state in the full theory.

For R33's actual subgroup H, the left-Weyl mirror field has profile
conjugate(u_i), while the ordinary field has profile v_i. Keep S=10_2
and its internal profile s, normalized with integral |s|^2=1. L^2 below
denotes the tensor square, not a norm space. On the selected central
flat background s is a section of that square line with the D5 vector
factor understood; we do not postulate a stand-alone charge-two
character of the full H quotient.

The ADDED local contraction uses the symmetric bilinear metric on
equal form degrees and the already checked Spin(10) Y_a and Lorentz
epsilon. In this specified model its two overlap matrices are

    M_ij=integral s conjugate(u_i) conjugate(u_j),
    P_ij=integral conjugate(s) g(v_i,v_j).

They are symmetric matrices. Their physical coefficients also contain
the respective microscopic couplings, which gauge symmetry does not
force equal. Deriving this internal contraction and s from an actual
source or PW action is still necessary; no such derivation is claimed.
The Hermitian current norm is a different tensor: g(v,v) need not
equal g(conjugate(v),v). A complex null vector supplies a type control.

## 2. Covariant integration identity, including the outer boundary

Write Delta_A=div_A D_A with nonpositive Laplacian sign and
V=q^2 |dF|^2-q Delta F. Then H0=-Delta_A+V. For w=u_i u_j,

    Delta_(2A) w
      = u_i Delta_A u_j+u_j Delta_A u_i+2 g(D_A u_i,D_A u_j).

Expanding both Witten differentials and substituting V gives

    g(d_q u_i,d_q u_j)
      = div_(2A) [ (1/2) D_(2A)w+q dF w ]
        + (u_i H0 u_j+u_j H0 u_i)/2.

This is an off-shell product identity, not an assumption about a
specific eigenbasis. Pair it with b=conjugate(s), a section of L^-2.
Applying the dual-connection divergence rule twice yields

    sqrt(lambda_i lambda_j) P_ij
      = (lambda_i+lambda_j)/2 conjugate(M_ij)
        + integral_Q u_i u_j [(1/2) Delta_(-2A)b-q <dF,D_(-2A)b>]
        - (1/2) integral_boundary_Q u_i u_j D_n^(-2A)b.

Indeed the initial flux term b[(1/2)D_n w+q F_n w] vanishes by
the TWO fermion Robin conditions. The separate term -(1/2)w D_n b
does not. Internal chart interfaces cancel for genuine smooth sections;
cutting out a source requires the actual transmission or interface
term. A prescribed discontinuous profile is not a smooth special case.

The smooth argument extends at fixed width to the stated bounded
source problem: F is W^(2,p) for finite p, u_i are H2, their products
are H2 in dimension three, and b may be chosen smooth. Product rules
and Green identities then hold weakly with their Sobolev traces.
No uniform estimate, exchange of limits, or cusp-domain assertion
is obtained by this extension. The finite symbolic controls below
check identities, not this global elliptic regularity argument.

With opposite bundle charges and a real neutral test weight a, the
same product/Green calculation instead gives

    lambda integral a (|v|^2-|u|^2)
      = integral |u|^2 [(1/2)Delta a-q <dF,da>]
        - (1/2) integral_boundary (partial_n a)|u|^2.

At a=1, the normalized current equality of R25/R30 is recovered.
It does not imply equality of the charged overlaps. Nor can one
neglect a small derivative term before dividing by small eigenvalues.
At an exact zero eigenvalue the normalization v=d_q u/sqrt(lambda)
is undefined; zero modes must be treated separately.

## 3. Controls that can fail in opposite directions

The producer checks the off-shell product and Green identities for
arbitrary functions and arbitrary radial volume J(x), with connection
D=d+i c A and charges (1,1) and (1,-1). A variable phase transforms
A to A-d eta, u to exp(i eta)u, b to exp(-2i eta)b. Every differential
and coefficient operator must transform with the correct charge.
Omitting the drift or the scalar conjugation must fail. This checks
metric-volume and connection terms, not just a flat uncharged example.

The two comparator families from the frozen working note are retained:

1. A flat circle times unit-area T2, F=0, alpha=1/3, and any selected
   finite collection of modes u_n=exp(i n x)/sqrt(2pi). Their partners
   are i sign(n+alpha)u_n dx. For arbitrary periodic s, P=-D conjugate(M)D,
   D_nn=sign(n+alpha), so the overlap singular values coincide. The
   concrete direct-integral control uses n=-1,0,1, both momentum signs,
   and four nonzero complex Fourier coefficients of a normalized s.
   Characteristic polynomials of M^dagger M and P^dagger P, and a
   nontrivial unitary basis change, test invariant spectra rather than
   basis entries. L squared has nontrivial order-three holonomy: s
   cannot be globally parallel. This is not the sourced hyperbolic Q.
2. On [0,pi] times unit-area T2, use the exact positive absolute pair
   sqrt(2/pi)cos x and -sqrt(2/pi)sin x dx. The normalized prescribed
   scalar N_t exp(-tx) has N_t=sqrt(2t/(1-exp(-2pi t))). The direct
   integrals should give M/P=(t^2+2)/2, but M~2sqrt(2)/(pi sqrt(t))
   and P~4sqrt(2)/(pi t^(5/2)). Both vanish at fixed microscopic
   couplings, while the scalar gradient norm squared is t^2. This
   comparator has additional zero modes and is not a spectrum census.
   It does not solve a scalar/source boundary equation. Its boundary
   term must be nonzero, and the constant-profile limit must reproduce
   the common normalized overlap 1/sqrt(pi).

A further nonzero-Witten-field control has F=2x,q=1 and normalized
u=sqrt(2/(5pi))(cos x-2sin x), v=-sqrt(2/pi)sin x, lambda=5.
With test coefficient b=x^2 it must obey the identity, including a
boundary correction -2/5. Undeformed Neumann data and omission of
the drift both fail. Here b is a test coefficient, not a normalized
scalar mode; no physical coupling is read from this control's numbers.

## 4. Physical consequence and the remaining calculation

The identity would give a way to compute or bound the ACTUAL charged
overlaps without conflating them with densities. The opposite controls
prevent both a universal equal-Yukawa no-go and a gap claim from a
diverging ratio. They do not select a profile for R29's sources.

The next physical calculation must derive S's profile and mass from
the same action as the source and its boundary/end data, obtain actual
eigenfunctions or sufficient uniform overlap bounds, and retain both
local couplings, scalar backreaction and finite Dirac mixing. R34's
quartic is an interaction candidate, not a known symmetric quantum
phase. A full phase test, anomaly/end completion, gravity and empirical
predictions remain part of the full goal, not replaced by this identity.
