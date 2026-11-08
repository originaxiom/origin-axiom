# Four connection sources: the inherited tail quartic retains Gauss exchange

2026-11-08. **Author analytical derivation, UNREVIEWED.** No science
import, collection, CAS or numerical run. A perturbative boundary
functional in the specified classical gauge sector is calculated below;
no global nonlinear existence, physical scattering or foundational
selection theorem is asserted.

## 1. Exact duty and prior work

Reuse [the inherited gauge action and Poisson profiles](SAME_ACTION_GAUGE_BOUNDARY_RESPONSE_AND_CUBIC_2026_11_08.md)
and [the longitudinal Ward completion](FREQUENCY_CORE_ANGULAR_TAIL_AND_GAUGE_WARD_RESPONSE_2026_11_08.md).
General elimination of a quadratic bulk response and its induced quartic
are already used in [the silver massive-exchange proof](../silver_higgs_quartic_2026_10_11/PROOF.md)
and [the earlier normal-response model](../EXTENSION_6.md). Those models,
their coefficient metrics and their numerical couplings are not copied
into this physical cusp. The addition here is an explicit actual tail
Green function and four-connection kernel with the radial gauge
constraint retained.

Keep the same residual-zero background, globally parallel non-Abelian
unbroken algebra g0, inherited positive trace kappa, Omega=ell/y,
x mod 1 and y>=Y. Both spin fields are retained in the parent and commute
with this classical gauge sector. Work at zero INTERNAL angular momentum;
external Euclidean momenta remain arbitrary.

Specify a small connection source b(Y,z)=epsilon B0(z) and external gauge
trace v_mu(Y,z)=0. The radial connection c=a_y has NO independently fixed
Dirichlet trace. Its equation is Gauss. Physical conjugate Fourier modes
travel together, B(-p)=B(p)^dagger. Other boundary polarizations and the
core are separate response duties, not deleted physical fields.

At first order,

    b=epsilon B+O(epsilon^3),
    B(p,y)=P_b(p,y) B0(p),
    P_b(p,y)=(y/Y)^(-(1+nu_p)/2),
    nu_p=sqrt(1+4ell^2 p^2).

There is no first-order v or c. Their first sourced response is order
epsilon^2. The g0 sector has no local b^4 term: there is only one retained
internal tangential connection component, and the spin commutators are
unchanged. This does not remove other quartics from the full parent.

## 2. The actual quadratic currents and their conservation

Write w=y^2/ell^2. Expanding the two covariant b kinetic squares fixes
the order-epsilon^2 sources for (v_mu,c):

    j_mu=-i[B,partial_mu B],
    j_y=-i w[B,partial_y B].                         (1)

The linear term in the action is g6^-2 integral kappa(v_mu j_mu+c j_y).
No independent current normalization has been introduced. The linear B
equation is

    -partial_y(w partial_y B)-partial_mu partial_mu B=0.

It gives, using [X,X]=0 for each derivative coefficient,

    partial_mu j_mu+partial_y j_y=0.                 (2)

For a Fourier pair p,q with k=p+q, symmetric ordered-pair notation gives

    j_mu(p,q;y)=(q-p)_mu [B0(p),B0(q)] P_b(p)P_b(q)/2,
    j_y(p,q;y)=-i y(nu_p-nu_q)
                  [B0(p),B0(q)] P_b(p)P_b(q)/(4ell^2).

An integration/sum over ordered p,q is understood; the factor one-half
avoids replacing the original current by twice its value. Direct
differentiation gives i k.j+partial_y j_y=0 because
nu_p^2-nu_q^2=4ell^2(p^2-q^2). This independently fixes the radial
source and its sign. A remote j_y tends to zero for these powers.

## 3. Solve the constrained vector response at nonzero external k

For k^2=s>0, use the source-preserving chart v_L=0. The gauge parameter
has zero trace at Y because the specified vector trace is zero. The
finite-energy complete-end gauge space is inherited; no new remote
physical source is selected by this chart. Gauge transformations with
zero trace at Y annihilate the source coupling by (2).

In this chart the quadratic vector/radial functional is

    1/(2g6^2) integral dy kappa(
       |partial_y v_T|^2+(ell^2 s/y^2)|v_T|^2+s|c|^2
                            +2 v_T.j_T+2 c j_y).     (3)

Its radial equation is c=-j_y/s, not c=0. The lost longitudinal vector
equation is recovered from (2), so (3) does not erase Gauss. The
transverse equation uses

    K_v(s)=-partial_y^2+ell^2 s/y^2,
    v_T(Y)=0,

and the same complete-end branch/norm as the previous Poisson response.
Let r_-=(1-nu_k)/2, r_+=(1+nu_k)/2 and u_< =min(y,z), u_>=max(y,z).
The actual Dirichlet Green kernel is

    G_s(y,z)=[u_<^r_+ u_>^r_-
                    -Y^nu_k (yz)^r_-]/nu_k.         (4)

Each branch solves K_v u=0 away from y=z. The kernel vanishes at Y,
is symmetric, has derivative jump -1 and takes the finite-norm branch
at infinity. Its positive quadratic form follows from the inherited
energy identity. Thus v_T(y)=-integral G_s(y,z) j_T(z) dz. This is an
inverse on the stated source class, not a claim of a uniform flat-L2
spectral gap for the complete half-line operator.

Stationary substitution into (3) gives the four-B tail coefficient

    Gamma_tail^(4)[B0]= -1/(2g6^2) integral_k [
       integral dy dz kappa(j_T(-k,y) G_(k^2)(y,z) j_T(k,z))
       + integral dy kappa(j_y(-k,y)j_y(k,y))/k^2 ].   (5)

The second term is the forced Gauss/longitudinal exchange. Setting c=0
would omit it and would not solve the parent's order-two equations.
It is not a freely chosen boundary scalar interaction.

The negative exchange correction is not by itself an instability: it
is a quartic coefficient at fixed sources added to the positive
quadratic response of the original positive gauge functional. Keeping
only a finite polynomial outside its small-source regime would be a
different claim. Correction b3 contributes no extra quartic term, by
the first-order equation and its zero boundary correction; the complete
end surface term vanishes for the retained powers.

## 4. The nonlocal transverse overlap has a closed coefficient

For sources with radial powers (y/Y)^-A and (y/Y)^-B, A,B>=2, direct
integration over the two triangles y<z and z<y in (4) gives

    integral dy dz (y/Y)^-A G_s(y,z) (z/Y)^-B
       =Y^3/[(A+B-3)(A-r_--1)(B-r_--1)].             (6)

One way to check its factors without a proxy matrix: the first triangular
term is Y^3/[nu_k(A+B-3)(B-r_--1)], the other exchanges A,B, and the
separable subtraction is -Y^3/[nu_k(A-r_--1)(B-r_--1)]. Their numerator
is 1-2r_-=nu_k. At coincident intermediate power exponents this expression
uses the continuous logarithmic limit; no spurious pole is introduced.

For pairs (p,q) and (r,t), put A=1+(nu_p+nu_q)/2 and
B=1+(nu_r+nu_t)/2. The radial factor multiplying their transverse
current coefficients is therefore

    I_G=8Y^3/[(nu_p+nu_q+nu_r+nu_t-2)
               (nu_p+nu_q+nu_k-1)
               (nu_r+nu_t+nu_k-1)].                (7)

All denominators are strictly positive on these Euclidean branches.
The external momenta, transverse projectors, commutators and pair sums
in (5) still have to accompany (7); a number alone is not the vertex.
The radial-current overlap uses instead

    integral dy y^2 P_p P_q P_r P_t
                         =Y^3/(A+B-3),              (8)

with the nu differences, i factors and 1/(4ell^2) from (1) kept before
forming its conjugate-paired quadratic form. Omitting those factors
would change the normalization and possibly the sign.

## 5. Retain the zero exchanged-momentum channel properly

At k=0, a pair has q=-p and equal nu. Consequently j_y(0,y)=0 exactly.
There is no division by zero in the original Gauss equation. The radial
connection on this contractible tail is pure gauge; this does not remove
flat core periods from the global theory. All four external vector
components use

    K_v(0)=-partial_y^2, G_0(y,z)=min(y,z)-Y.

The sourced solution can approach a constant at infinity. That constant
has finite ACTUAL vector norm integral ell^2 |v|^2/y^2 dy. It must not
be excluded by incorrectly requiring the flat norm integral |v|^2dy.
The kernel (4) and overlap (6) both have this regular nu_k=1 limit.

The apparent discontinuity between the transverse projector and Gauss
term is controlled by current conservation. For small nonzero k,
j_y(y)=i integral_y^infinity k.j(z) dz. In the zero-parameter limit,

    integral dy |integral_y^infinity j_L(z) dz|^2
       =integral dy dz j_L(y)^dagger
                           [min(y,z)-Y] j_L(z).      (9)

This follows by exchanging the three convergent integrals. The limiting
Gauss contribution supplies precisely the longitudinal piece of the
zero-momentum vector Green form. It must not be discarded because the
pointwise radial source vanishes at k=0. Finite limiting claims use
smooth source families and their conjugate pairing, not arbitrary
independently assigned currents.

## 6. Reduction grade and unfinished physical obligations

Equations (1)--(9) compute the four-connection-source part of the
zero-internal-angular classical tail functional, including its vector
backreaction and Gauss source. Its coupling and finite radial factors
are inherited; no boundary quartic coefficient has been supplied.
This goes beyond the static harmonic-period potential but does not
complete the functional for arbitrary vector, angular, spin and fermion
sources. The actual core still joins through its full response and
common currents; no new interface amplitude or chiral projector is fixed.

This conditional input reduction requires independent proof review and
new separately sealed controls. It is OUTSIDE both the original six-
method packet and the newer seven-method implementation. Their unrun
status is unchanged. No physical SM spectrum, anomaly, stable nonlinear
vacuum, observed parameter, foundational input or gravity is newly earned.
