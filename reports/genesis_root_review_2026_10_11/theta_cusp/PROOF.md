# The cusp discriminant from the existing theta functions

On the upper half plane set q=exp(2 pi i tau), and use the analytic choices q^a=exp(2 pi i a tau). Define

    theta2 = sum_(n in Z) q^((n+1/2)^2/2)
    theta3 = sum_(n in Z) q^(n^2/2)
    theta4 = sum_(n in Z) (-1)^n q^(n^2/2)
    eta = q^(1/24) product_(m>=1) (1-q^m).

These series and products converge locally uniformly. The product for eta is nonzero: on every compact set the tail logarithms are absolutely summable and none of the individual factors vanishes. This is a statement about the standard analytic functions, not about an arbitrary vector with their finite-dimensional multiplier.

## The two generator laws

For T: tau -> tau+1, n(n+1) is even and n^2 has the parity of n. Substitution in the series gives

    (theta2,theta3,theta4)(tau+1)
      = (exp(pi i/4) theta2, theta4, theta3)(tau).

For S: tau -> -1/tau, use Poisson summation on the Schwartz Gaussian g_tau(t)=exp(pi i tau t^2), whose Fourier transform with kernel exp(-2 pi i t xi) is

    ghat_tau(xi)=(-i tau)^(-1/2) exp(-pi i xi^2/tau).

The square root is the analytic one positive for tau on the positive imaginary axis. The Gaussian integral proves this there; holomorphic continuation proves it throughout the upper half plane. Poisson summation without a shift gives the theta3 law. A half translation in t multiplies its Fourier series by (-1)^n; modulation by exp(pi i t) shifts its Fourier transform by one half. These give the theta2/theta4 interchange:

    (theta2,theta3,theta4)(-1/tau)
      = (-i tau)^(1/2) (theta4,theta3,theta2)(tau).

These agree with [DLMF 20.7.27 through 20.7.33](https://dlmf.nist.gov/20.7#viii). With P=theta2 theta3 theta4, the laws are P(T tau)=exp(pi i/4) P(tau) and P(S tau)=(-i tau)^(3/2) P(tau). Consequently

    Dtheta = P^8/256
    Dtheta(tau+1)=Dtheta(tau)
    Dtheta(-1/tau)=tau^12 Dtheta(tau).

The last equality uses (-i)^12=1, not a dropped metaplectic phase. Since S and T generate SL(2,Z), their composition law gives weight twelve for every modular transformation. The Euclidean algorithm on the first column of a unimodular matrix supplies that generation statement; -I also acts trivially at this even weight.

Within powers of this particular product, eight is the least positive power with trivial T multiplier. This is not a classification of all possible covariants or physical couplings.

## Identifying the product and the cusp zero

The Jacobi triple product specializes to

    theta2 = 2 q^(1/8) product (1-q^m)(1+q^m)^2
    theta3 = product (1-q^m)(1+q^(m-1/2))^2
    theta4 = product (1-q^m)(1-q^(m-1/2))^2.

The source uses the nome exp(pi i tau), whose square is q here: [DLMF 20.5.2 through 20.5.4](https://dlmf.nist.gov/20.5#i). This nome conversion is essential.

Multiplication leaves, besides 2 q^(1/8) product(1-q^m)^3, the square of

    product_(m>=1) (1+q^m)(1-q^(2m-1)).

Replace 1+q^m by (1-q^(2m))/(1-q^m). The even and odd factors exhaust the positive integers, so the last product is one. These rearrangements are justified by locally absolute logarithmic convergence. Therefore

    P = 2 eta^3
    Dtheta = eta^24 = q product_(m>=1)(1-q^m)^24 = Delta.

Thus Delta has the full weight-twelve transformation law, no zero in the upper half plane and precisely a simple zero at the cusp, with leading coefficient one. The compactified weight-twelve line has divisor the cusp; Delta trivializes its restriction to the open modular base. This supplies exactly HDelta in the earlier cusp_connection proof. The earlier curvature, real-flux examples and norm identities can now use that trivialization without leaving its transformation law as a hypothesis.

This is the same classical product already present in W51, now connected explicitly to the local HDelta dependency. It does not discover an additional independent structure or a new physical constant.

## Why the identity does not select a physical sector

Let x_p=|theta_p/eta|^2. Then

    x_2 x_3 x_4 = |P/eta^3|^2 = 4.

The normalized joint parity quantity is constant, despite the nontrivial unnormalized cusp divisor. Its logarithmic curvature is zero. One cannot infer a nonzero matter-line curvature from this scalar normalized product. This does not classify determinant lines, their phases or connections for some other physical operator; those require their own family-index and boundary analysis.

The triplet used in W50 is also not the unsquared theta vector. For f_p=theta_p^2/eta^3 (weight -1/2), its component product is 4 eta^-3, and

    (product f_p)^8 = 4^8 Delta^-1.

For the holomorphic dressed triplet g_p=eta^21 theta_p^2=Delta f_p (weight23/2),

    (product g_p)^8 = 4^8 Delta^23.

Both are explicit covariants with the same finite multiplier and different weights and cusp orders. They exhibit available poles or zeros, not a rule compelling matter to use either. The identity in the first line is potentially useful when testing an actual coupling: it locates a reciprocal discriminant already in the meromorphic theta realization. Merely forming that covariant does not make it the physical action or fix its multiplicity.

Likewise the open metrics (y^12 |Delta|^2)^s in the earlier packet remain well-defined for all real s, and its specified Yang-Mills functional still allows zero flux. Constructing the divisor is not imposing the extension O(D), coupling its inverse to a particular field, or excluding the zero sector. No chirality index or Standard-Model parameter is computed here.

## Verification scope

The analytic proof supplies the generator laws, convergence and the all-orders product identity. Exact truncated integer series check normalization, signs, the nome convention and cusp order through degree256 in x=q^(1/8). They are safeguards for this proof, not substitutes for Poisson summation or the Jacobi triple product. No numerical grid is used to promote an identity to a theorem, and no representation identification alone selects a distinguished analytic section.
