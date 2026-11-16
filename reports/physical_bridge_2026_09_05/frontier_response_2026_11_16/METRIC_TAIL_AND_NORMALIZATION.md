# The cusp tail and the normalized coupling calculation

2026-11-16. PHYSICAL-C5 author hand derivation, pending independent review.
The source under review is AGY-exp af08bc3d272c01a85e7341da91cfcc43d230d64c.
No scientific producer, import, collection, CAS or integration ran here.

## 1. The metric identity still needs to be earned

X-FRONTIER-2 lines 183–210 choose tau=i sqrt(3) and define

    R(z)=exp[-pi (Im z)^2/Im tau] |theta1(z)/theta1'(0)|,
    Omega(z)=1/[R(z) (1+|log R(z)|)].                    (1)

The periodicity of R and its puncture asymptotic are useful checks of
this explicit comparator. The physical parent used a complete hyperbolic
metric on the marked punctured elliptic surface. Equality of (1) to that
metric requires the actual uniformization equation, the marked conformal
parameter and the source frame map. A three-dimensional cusp modulus does
not supply that two-dimensional conformal identification by its name.

For a direct diagnostic, work in a region R<1 away from the puncture.
Put u=log R, L=1-u, y_tau=Im tau and use the flat Laplacian. Holomorphicity
of theta1 away from its zero gives

    Delta u=-2pi/y_tau,
    Delta log Omega=(2pi/y_tau)(1-1/L)+|grad u|^2/L^2,
    curvature(Omega^2 |dz|^2)
       =-R^2 [(2pi/y_tau)(L^2-L)+|grad u|^2].           (2)

Thus the appropriate source check is the Liouville residual
Delta log Omega-Omega^2/ell^2, including global regularity wherever the
absolute value in (1) changes branch. Periodicity alone leaves (2)
unchecked. This note does not assign a curvature failure at an untested
point or dismiss the comparator's finite-area cusp.

## 2. An omitted area term survives both quadrature grids

The source integrates the polar cusp only for

    r=r0 exp(-t), r0=1/4, 0<=t<=T=18.

The odd theta expansion and its nonzero derivative at zero give uniformly
in angle

    R(z)=r[1+O(r^2)].

Let a=1+log(1/r0). For sufficiently large t the absolute value in (1)
therefore gives

    1+|log R|=t+a+O(r0^2 exp(-2t)),
    Omega^2 r^2=(t+a)^-2
                    [1+O(r0^2 exp(-2t))].             (3)

Integrating the uncomputed region proves the asymptotic tail formula

    delta A(T)=integral_(t>T) Omega^2 r^2 dt dtheta
       =2pi/(T+a)+O(r0^2 exp(-2T)/(T+a)^2).            (4)

For the stated cutoff the leading term is 2pi/(19+log 4). The error
constant in (4) requires theta bounds before this becomes a certified
finite-T enclosure. The positive tail is algebraic in T. Comparing a
16-node and a 24-node quadrature with this same T does not measure it.
Neither grid contains an analytic tail term in lines 218–265.

The other integrals used in that function have different tails. Writing
n_+=1 and n_-=theta3/theta1=O(1/r), their polar integrands have orders

    integral Omega               -> r/(t+a),
    integral |n_+|^2 Omega^-3     -> r^5 (t+a)^3,
    integral |n_-|^2 Omega^-3     -> r^3 (t+a)^3,
    integral |n_+|^2 Omega^-2     -> r^4 (t+a)^2,
    integral |n_-|^2 Omega^-2     -> r^2 (t+a)^2.         (5)

All integrals use the same Euclidean area element. These tails decay
exponentially in T. An area estimate and a spin/form norm estimate cannot
share a single cutoff argument without these weights.

## 3. What the missing area changes

Define the integrals actually used by X-FRONTIER-2

    A=integral Omega^2, J=integral Omega,
    K_p(n)=integral |n|^2 Omega^-p.

Its formula is

    (lambda_n/e_Q)^2=2 A K_3(n)/[J K_2(n)].             (6)

The area tail affects each absolute coupling in (6). Their ratio cancels
A and J exactly, so that particular common error does not by itself
invalidate the reported hierarchy. The ratio still needs the actual
metric identification and controlled K_2,K_3 quadrature. The exterior
quadrature also discards rectangle nodes using a sharp disk indicator,
which needs an error estimate across that artificial interface.

The narrow rational intervals reported upstream are numerical observations
on this cutoff comparator. Equations (3)–(6) prevent treating the existing
two-grid difference as a complete error bound for the physical couplings.
No replacement physical decimal value is supplied here.

## 4. A useful normalization control

For the formula (6), keep its holomorphic n and coordinate measure fixed
and set Omega_epsilon=exp(epsilon f) Omega, with f smooth and compactly
supported away from the cusp. Define weighted averages using the indicated
positive densities. Direct differentiation gives

    d log(lambda_n/e_Q)/d epsilon at 0
      =1/2 [2 <f>_(Omega^2)-<f>_Omega
                 -3 <f>_(|n|^2 Omega^-3)
                 +2 <f>_(|n|^2 Omega^-2)].            (7)

A constant rescaling cancels because 2-1-3+2=0. General shape dependence
is retained by the four different normalized densities. In the ratio of
two channels the first two averages cancel. A claimed scale-free number
still needs the shape and the field metrics that enter the remaining
averages.

Equation (7) is a comparator sensitivity identity. Arbitrary f need not
preserve the hyperbolic curvature equation. It does not create an extra
physical modulus in a fixed conformal class. Its role is to detect an
incorrect identification or a normalization that has silently forgotten
the metric.

## 5. Route to an actual physical coefficient

First identify the marked parent curve, its exact source metric and the
unitary/holomorphic frame conversion. Then transport the gauge bracket,
sections and all three kinetic Grams into the integral. Reuse the existing
rank-one multiplication proof. Compute a complete cusp contribution or
an analytic tail enclosure, control the artificial quadrature interface,
and refine the norm integrals as well as any Fourier inverse. Only then
attach an error enclosure to a physical coefficient.

For X-FRONTIER-3 the Fourier grids change while the physical-norm Gram
quadrature is fixed at 16 nodes and T=18. The same metric identity duty
survives. Agreement of its Fourier and residue routes can check the
holomorphic map for those common inputs. It cannot independently verify
the shared metric and Gram inputs.

The mathematical rank-one result and its nonzero coefficient are retained
within the supplied parent and its domain hypotheses. Independent review
of those physical proofs remains with SM. Foundational inputs counted
removed by this correction remain zero.
