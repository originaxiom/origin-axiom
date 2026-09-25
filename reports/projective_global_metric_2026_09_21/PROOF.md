# F12 authored global harmonic-metric completion

Pre-execution argument. Exact exceptional irreducibility is a separately
tested hypothesis; the differential-geometric argument is not certified
by finite tests. All energies here mean integral |Psi|^2.

## 1. A sharp lower bound, not subtraction of arbitrary infinities

Let h be ANY smooth determinant-one positive Hermitian metric for the
flat SL4 bundle on a cusp. In a unitary frame write D=A+Psi with
Psi self-adjoint and traceless. Fix x,z and a nonzero parallel vector
v(y) in the longitude's simple q^-3 eigenline. It exists even though
the global representation need not preserve a line. Its normalized
orthogonal projector P(y) has trace one and P^2=P. Then

    d_y log |v|_h = -tr(P Psi_y),
    integral_0^1 tr(P Psi_y) dy = 3 k,   k=log q.

Use trace Psi_y=0 and |P-I/4|_F^2=3/4. Cauchy-Schwarz gives

    9 k^2 <= (3/4) integral_0^1 |Psi_y|_F^2 dy.

This is valid separately for every x,z, with no metric asymptotic
assumption. The actual hyperbolic norm and volume therefore imply

    E_h(Z<z<R) >= a log(R/Z),     a=12 k^2/L.            (1)

Unitary scalar twists do not change the longitude or this inequality.
It also holds for nonsmooth finite-energy competitors by Sobolev
approximation, or by the absolutely continuous loop representative.
The loop calculation is used almost everywhere, not at exceptional
Sobolev slices. The trace constraint is essential to the sharp factor.

## 2. The exact harmonic end has finite excess above (1)

Keep F10's harmonic tail h_ref, with u=(z^2-c)/4,
c=4 beta^2/L^2>0, and z>=Z>sqrt(c). Its already derived norm density
has the exact decomposition (after integration over x,y of periods 1)

    e_ref(z) = a/z + r(z),
    r(z) = 2L (3z^2-c)/[z (z^2-c)^2] > 0.

The tail integral is explicit:

    R(Z) = integral_Z^infinity r(z) dz
         = L [2/(Z^2-c) - log(1-c/Z^2)/c].             (2)

In particular r(z)=6L/z^3+O(z^-5) and R(Z)=3L/Z^2+O(Z^-4).
For Z^2>=2c, r(z)<=24L/z^3 and R(Z)<=12L/Z^2.
This is finite excess, not finite total E. Subtracting the weaker
9k^2/L floor would leave 3k^2/L log R divergent and would NOT prove
the needed bound. The sharp determinant-one estimate closes that gap.

Extend h_ref smoothly over the compact core in the same flat bundle.
Such a positive determinant-one extension always exists: the fiber
X=SL4(C)/SU4 is contractible, and geodesic interpolation in its
positive-metric model preserves positivity and determinant one. It
need not solve the moment equation on the core. From now on this is
one fixed reference section h0, not a new choice for each cutoff.

## 3. Compact-domain solutions: hypotheses and bundle issue

Let M_R be the smooth compact truncation with outer boundary z=R.
Minimize the harmonic-map energy over sections of the flat X bundle
with boundary value h0. The compact-domain Hadamard Dirichlet theory
gives a smooth minimizer h_R, harmonic in the interior. The energy
functional is convex under pointwise geodesic interpolation, since
X is complete, simply connected and nonpositively curved.

The flat-bundle version is not an identification of this bundle with
a globally trivial map. In parallel charts its transition maps are
constant isometries of X. Local Sobolev compactness, energy lower
semicontinuity and regularity therefore glue unchanged. For a minimizing
sequence s_j the global scalar distance w_j=d_X(s_j,h0) has zero
boundary trace and |dw_j|<=|ds_j|+|dh0|. The compact-domain Poincare
inequality bounds its L2 norm. This anchors the sequence in X over
each finite parallel-chart cover; properness and metric Sobolev
compactness yield a weak minimizing section with the assigned trace.
Geodesic convexity and local Dirichlet replacement give the usual
Hadamard-target interior regularity (smooth for this smooth target).
The energy and compactness facts apply in dimension three, not by
conformal invariance of surface energy.

For the general local results and normalizations see
Riestenberg--Smillie, section 2.3, Propositions 19--22:
https://arxiv.org/html/2511.11469v3#S2.SS3
They record Hamilton/Korevaar--Schoen's Dirichlet theorem and compactness.
This paragraph supplies the flat-bundle adaptation; their new global
coarse-stability hypotheses are not asserted for our cusp map.

## 4. Uniform local energy, without assuming a global solution

Minimality and (1) give, for Z<=S<R,

    E(h_R;M_S)
      <= E(h0;M_R) - a log(R/S)
      <= E(h0;M_Z) + a log(S/Z) + R(Z).                (3)

The right side is independent of R for fixed S. This is the central
exhaustion estimate. No divergent whole energy is declared finite.
The comparison h0 has the right boundary data; (1) applies to h_R
itself, so neither a fixed-core-energy assumption nor a presumed
limiting metric is involved.

On each fixed compact set the harmonic-map Bochner inequality has
Delta e >= -C e, with C fixed by the base Ricci bound and nonpositive
target curvature. Local mean-value estimates on slightly larger
compact sets convert (3) to a uniform gradient bound. The constants
need not be uniform as the compact set goes up the cusp; uniformity
in R on each fixed set is sufficient. See the same primary source,
Theorem 17 and Proposition 19. In the smooth case this also follows
directly from the Bochner formula and scalar Moser iteration.

Sagman's section 5.1 provides a related energy-exhaustion strategy:
https://arxiv.org/html/1911.06937v3#S5.SS1
Its published main theorem concerns surface domains. Equations (1)--(3)
and the higher-rank algebraic compactness below are the application
proved here, not an invocation of that theorem for a three-manifold.

## 5. Exact word algebra prevents escape in the target

Fix a basepoint p and generator loops contained in a fixed compact
core. The gradient bound implies uniform target displacements
d_X(H_R,G^*H_RG) for H_R=h_R(p) and each generator G (using inverse
pullback instead gives the same bound). For the metric
ds_X^2=(1/4)tr(H^-1dH)^2, this distance is

    (sum_i log^2 sigma_i(G;H_R))^(1/2).

Here sigma_i are the singular values in the H_R norm. Consequently
each generator and its inverse have uniformly bounded operator norm
in H_R. Every fixed word inherits such a bound.

Suppose the finite tested word list W_j spans all Mat4(C), equivalently
its vectorizations have rank 16. Express each matrix unit E_ab as a
fixed linear combination of W_j. The coefficients depend on the fixed
representation, not on R. Its operator norm in H_R is bounded. Since
E_ab has rank one, its Hilbert-Schmidt and operator norms coincide and

    |E_ab|_(HS,H_R)^2 = (H_R)_aa (H_R^-1)_bb.

Summing bounds tr(H_R) tr(H_R^-1), hence the eigenvalue condition
number. Since det H_R=1, both H_R and H_R^-1 are uniformly bounded.
Thus H_R stays in a compact subset of X. The gradient bound along
paths now bounds h_R on every compact piece of the universal cover.

This uses the FULL generated algebra. Having H0=0, or even a scalar
commutant, is not enough for this step. The exact field tests decide
whether the actual exceptional representations meet its hypothesis.
No sequence of R-dependent conjugations of the representation is used.

## 6. Global harmonic limit and its actual end class

On compact sets the preceding bounds and elliptic bootstrapping give
a smoothly convergent subsequence on a diagonal exhaustion. Its limit
h is a smooth positive determinant-one harmonic metric for the same
flat representation. Equivariance is preserved. It solves d_A^*Psi=0;
flatness of D gives the other two adopted parent equations. This is
an existence argument, not an explicit spatial profile computation.

We must still verify F11's end norm hypothesis. On Z<=z<=R both h_R
and h0=h_ref are harmonic. The squared target distance between them
is subharmonic by the nonpositive-curvature second variation. It is
zero on z=R, and bounded uniformly on z=Z by the fixed-compact bounds.
The maximum principle on this COMPACT annulus gives

    d_X(h_R,h_ref) <= C,           Z<=z<=R,

with C independent of R. The inequality survives in h. Bounded target
distance bounds every log eigenvalue of h_ref^-1 h, hence

    exp(-2C) h_ref <= h <= exp(2C) h_ref               (4)

in the stated metric convention. On the fixed base, these inequalities
also give uniformly equivalent norms for coefficient-valued forms in
every degree; dual bounds follow by inversion. No derivative bounds
at infinite height are needed to identify those Hilbert complexes.
Therefore F11's compact-resolvent and ordinary-L2 comparison apply
to this ACTUAL harmonic completion, not just an arbitrary smooth one.

Unitary scalar twists act trivially on X, so the same metric solves
all central-twist metric equations. The dual metric h^-T is harmonic
for the dual connection. Pullback yields a harmonic completion in the
same end class on any finite cover; we do not assume the restricted
representation remains irreducible. Cover multiplicities still need
their own cohomology computation.

## 7. Consequence conditional only on the finite certificate

If the algebra tests give full rank at both p14 and p34, there exist
smooth complete global harmonic metrics with the required asymptotic
norm class at all four exceptional positive q values. F11 then gives
one normalizable coefficient one-form in each dual sector for chi=-1
at p34 and chi=+/-i at p14. The finite tests do not prove existence by
themselves: sections 1--6 are the accompanying authored analytic proof.

Embedding the SU4 connection and Higgs into the adopted E8 parent
preserves its classical source-free bulk equations. This is NOT a
derivation of that parent, base metric or fixed asymptotic q; not net
chirality, three generations, a gravitational solution, a finite total
Higgs norm, a quantum phase, a physical end action, or a full vacuum
selection law. The harmonic-map minimization functional is a method
for solving the bulk moment equation, not a substitute physical action.
Stationarity under general allowed end variations, product integrability
and normalized parent interactions remain separate, testable duties.
