# R34 authored matching argument and checks to be executed

2026-09-19. This is a local calculation in the ADDED R33 field theory.
It is not a derivation of these fields or four-dimensional spacetime
from the arithmetic parent. The actual H lattice and D5 representation
map are those already tested in MIRROR_INTERACTION_PROOF.md sections 1--2.

## 1. Grassmann operator, not a commuting-spinor placeholder

For either chiral 16 let theta=(u_0,...,u_15,d_0,...,d_15) be independent
Grassmann generators, with epsilon_ud=+1. R33's Y_a are symmetric, so

    B_a = theta^t (epsilon tensor Y_a) theta
        = 2 sum_AB Y_a,AB u_A d_B.

Products B_a commute as even elements, but are NOT ordinary numerical
variables. Define Q=sum_a B_a B_a in their exterior algebra. The
coefficient of u_i u_k d_j d_l for i<k and j<l is exactly

    -8 sum_a (Y_a,ij Y_a,kl - Y_a,il Y_a,kj).

This follows by moving each first d through the next u, then summing
both row and column orderings. It gives an independent all-coefficient
check of the reused wedge implementation. Full antisymmetrization of
(theta^t A_a theta)^2 over four distinct indices gives a third witness
check with 24 permutations, not the same wedge helper.

Under delta theta=diag(T_ab,T_ab)theta, R33's intertwiner identity gives
delta B_c=delta_ca B_b-delta_cb B_a, hence delta Q=0. Lorentz sl2 acts
on u,d and preserves epsilon, hence each B_a and Q. The direct checks
apply all generators to Q rather than only quoting these arguments.
Nonvanishing is to be determined by the exact coefficient computation,
not inferred from this symmetry argument. A single commuting internal
spinor has a DIFFERENT symmetric degree-four tensor; its Fierz
cancellation, if verified, does not imply Q vanishes.

## 2. Gaussian scalar integration including the measure

Take real kappa and complex Phi and a ten-component source J with
charge -2. The quadratic Euclidean density is

    V = r S* dot S - kappa(Phi* S dot S + Phi S* dot S*)
        + S dot J + S* dot J*,
    J = y_m B_m + y_p* B_p*.

B_m has charge -2, B_p has charge +2. The matrix of stationary
equations, on (S,S*), and its determinant are

    N = [[r, -2 kappa Phi], [-2 kappa Phi*, r]],
    D = r^2 - 4 kappa^2 |Phi|^2.

At D nonzero the solution is

    S  = -(r J* + 2 kappa Phi J)/D,
    S* = -(r J  + 2 kappa Phi* J*)/D,
    V_eff = -[r J dot J* + kappa Phi J dot J
              + kappa Phi* J* dot J*]/D.

Differentiate the original V and substitute this solution to verify
both stationarity and value. Completing the real square proves the
same source term for the Gaussian integral. Convergence, stronger than
D nonzero, requires r>2|kappa Phi|. In a local phase choice Phi=f>0,
S=(x+i y)/sqrt(2), the 20-real-variable Hessian has r-2 kappa f ten
times and r+2 kappa f ten times. Its determinant is D^10, hence the
ultralocal Gaussian normalization is proportional to D^-5. If Phi is
dynamical it contributes 5 log D per regulated site, relative to a
chosen reference determinant. It cannot be dropped as a constant.
The log argument requires that reference to be dimensionless; no
regulator-independent finite vacuum energy follows from this formula.

For y_p=0 the density includes

    -r |y_m|^2 B_m dot B_m*/D
    -[kappa Phi y_m^2 Q_m + h.c.]/D.

If Q_m is nonzero, the second term changes a fermion-only mirror
phase by four units. Phi supplies its +4 gauge charge, so the FULL
term is H invariant. Setting kappa or Phi to zero removes this
particular number-changing term. Omitting Phi or conjugating it
incorrectly fails the gauge test. This is not an anomaly calculation.
The residual discrete phase overlaps the Spin(10) center after Phi
reduction; do not infer an independent Z4 gauge factor.

## 3. No symmetry-only mirror selectivity

For nonzero y_p the SAME integration supplies ordinary-sector and
mixed terms. With (a,b,c,d)=(B_m,B_m*,B_p,B_p*) the numerator is

    r (y_m a + y_p* d)(y_m* b + y_p c)
    + kappa Phi (y_m a + y_p* d)^2
    + kappa Phi* (y_m* b + y_p c)^2.

All ten coefficients and H charges will be tested. Pure-sector Q's
are tested with actual Grassmann fields; the channel expansion alone
is not a proof of their nonvanishing. It does not claim that every
Lorentz Fierz basis channel is independent.

In phase columns (psi,chi,S,Phi), constraints from y_m, y_p, mu and
kappa are respectively (0,2,1,0), (2,0,-1,0), (1,1,0,0), (0,0,2,-1).
Their kernel should be only the gauge phase (1,-1,2,4). Removing y_p
while retaining mu does not restore a protective independent
continuous phase; removing kappa does enlarge the continuous kernel.
This inventories rephasings, not all discrete/flavour symmetries.
Setting y_p=0 can define a tree-level input but is not a derived
geometric hierarchy or an all-loop technical-naturalness proof.

## 4. What this calculation cannot earn

The integration is exact for an ultralocal auxiliary S with no kinetic
or quartic scalar term. For R33's propagating S with lambda(S* S)^2
it is leading low-momentum TREE-LEVEL four-fermion matching: scalar
self-interactions contribute higher-fermion terms at tree level,
kinetic terms give momentum dependence, and loops can change matching.
Its common stable regime is around S=0, not R33's ordered Spin(9)
vacuum. At r -> 2|kappa Phi| the light scalar must be retained; an
inverse denominator blowing up is not controlled evidence of SMG.

In assumed four dimensions, [B]=3, [Phi]=[S]=1, [r]=2, [kappa]=1.
The conserving operator is dimension six with coefficient dimension
-2; Phi Q has dimension seven with coefficient dimension -3. After
fixing Phi, the induced quartic is still dimension six. Weak-coupling
matching alone is not a controlled strong-coupling phase construction.

R31's finite positive Dirac mixing and normalized currents, R33's
anomaly and C3 constraints, and the full source/end geometry remain.
No fermion/boson spectrum, volume limit, composite-channel census,
source-selected coupling or empirical parameter is produced here.
Next derive the actual form/locality coupling and normalized overlaps
for both partners, then specify a local positive-norm regulator and
test the fully interacting phase with all those duties retained.
