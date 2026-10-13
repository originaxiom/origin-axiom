# Global harmonic admission in a prescribed flag end class

October 13, 2026. Authored before execution. This is a proposed application of a published noncompact existence theorem, with an explicit verification of its geometric and stability hypotheses. Finite checks support the algebra and radial identities, not the analytic existence theorem. It does not derive the chosen flat bundle, metric, end amplitude, parent action or physical spectrum from genesis.

## Fixed data and claim

Let M be the complete connected one-cusped hyperbolic three-manifold of the marked m135 candidate, with compact smooth core and end metric dr squared plus exp(-2r/ell) h_T, ell positive. The rank-five flat bundle W is the supplied nonsplit extension 0 to V to W to 1 to 0. The actual rank-four generator matrices and extension coordinates are in candidate.json. Their relators, nonsplitting and full associative matrix algebra are obligations of the sealed verifier, not assumptions inferred from a manifold name.

On its end use the flat identification with Joining Gate 3's literal peripheral split coefficient. In that packet's orthonormal coefficient frame the connection is

    C5 = diag(C4,0) - b0 exp(2r/ell) Xi dr,
    Xi = diag(1,1,1,1,-4), b0 > 0.

C4 is the actual trace-free Hermitian-matrix lift of its nonabelian rank-two cusp connection. This end is flat and harmonic; its identification with the marked peripheral holonomies and the whole moment equation were reproduced in joining_review_2026_10_13. Its radial flag current is -20 A0 b0, with A0 the positive seam area. This is the structure factor, not a gauge color/weak splitting.

Choose a smooth determinant-one reference metric K on W that equals this end metric outside a compact set. The metric fibre is contractible, so a positive extension over the core exists; determinant normalization preserves the end value. The underlying flat D is not changed. The claim is: after verifying the stated algebra, W admits a unique determinant-one harmonic metric H mutually bounded with K, with D(K^-1 H) in L2 as in the theorem below. No boundary metric at an artificial finite cut is an additional input. K's asymptotic class, including b0, is still an input.

## The external existence theorem and its exact scope

Wu and Zhang, [Poisson metrics and Higgs bundles over noncompact Kähler manifolds](https://arxiv.org/html/2109.01776v1), Theorem 1.3, Corollary 1.1, Proposition 3.8 and Proposition 4.1, accessed October 13, 2026, apply their existence and uniqueness result to Riemannian bases under Assumption 2.1, flatness, analytic stability and a weighted tension bound. Completeness with finite volume supplies the additional base alternative. The harmonic conclusion uses zero trace of the reference tension. Their result bounds the relative metric and its covariant derivative; it does not require the reference Higgs norm itself to be L2.

The paper's compact Dirichlet result alone would not imply this claim. The following arguments establish the additional hypotheses for the stated end class. No Kähler or pluriharmonic structure on M is imported.

## The weighted maximum principle on this cusp

Use the convention Delta=div grad. On radial functions,

    Delta u = u'' - (2/ell) u'.

Choose a smooth strictly positive function phi which is bounded below on every fixed compact subset and equals exp(-epsilon r/ell) on the end beyond a fixed seam, epsilon positive. It is integrable because the volume density is A0 exp(-2r/ell). There is no claim that the constant choice phi=1 gives the required estimate.

For a nonnegative bounded f with Delta f >= -B phi, put on that end

    v(r) = ell squared [1-exp(-epsilon r/ell)] / [epsilon(epsilon+2)],

resetting r=0 at that seam and absorbing the fixed seam factor in B. Then v(0)=0, v is bounded nonnegative and Delta v=-phi. The function w=f-Bv is bounded and subharmonic on the end. Since exp(2r/ell) is harmonic and unbounded, apply the maximum principle to w-delta[exp(2r/ell)-1] on finite cylinders, then let the outer cut tend to infinity and delta decrease to zero. This yields

    sup_end f <= sup_seam f + B ell squared/[epsilon(epsilon+2)].

Interior local L1-to-sup estimates for the scalar inequality on a fixed compact neighborhood of the core and seam bound sup_core f by a constant times its integral on a slightly larger compact neighborhood, plus a constant times B. On that neighborhood phi has a positive lower bound, so the integral is bounded by a constant times integral_M f phi. Combining the two gives Assumption 2.1's sup bound C(B)[1+integral f phi]. The local estimate is standard elliptic analysis on a fixed compact set; no uniform injectivity radius at infinity is assumed. Weak distributional subsolutions use the same comparison and local estimates by their weak versions.

For the other clause of Assumption 2.1, let f be bounded with Delta f >= 0. Take smooth nonnegative exhaustion cutoffs chi_R, one up to cusp height R and zero above R+1, monotone in R. Their derivatives are uniformly bounded and the radial Laplacian formula gives integral |Delta chi_R| <= C exp(-2R/ell). Distributionally,

    0 <= integral chi_R Delta f = integral f Delta chi_R
       <= ||f||_infinity C exp(-2R/ell).

The nonnegative measure Delta f therefore vanishes. Compactness of the core, completeness and finite volume of M are already among the fixed geometric premises. This verifies the base hypotheses without replacing the cusp by a compact boundary.

## The actual invariant subbundle and its analytic degree

If the complex associative algebra generated by the candidate's V matrices is Mat4(C), V is irreducible. The exact word-span test below is sufficient for that statement. A nonzero proper invariant subspace S of W intersects V in either 0 or V. In the first case its projection into W/V is injective; a nonzero S would be a one-dimensional invariant complement, contradicting the verified nonsplitting. In the second case S=V unless S=W. Thus V is the only proper nonzero invariant subbundle. This argument does not assume that W is semisimple.

Use Wu-Zhang's definition degree_K(S)=-integral tr D_KS^* psi_KS. Taking a trace removes connection commutators. Consequently the integral over a compact truncation is the outward boundary integral of tr psi_KS. On the end, K is block diagonal and the induced V connection has

    tr psi_KV,r = -4 b0 exp(2r/ell).

The trace-free C4 contributes zero. Multiplying by the slice area gives a constant -4 A0 b0, independent of cut. Outside the compact transition this induced trace divergence vanishes, so the degree integral is well-defined. There is no contribution from an artificial inner boundary of the complete M. Hence

    degree_K(V) = -4 A0 b0,
    degree_K(W) = 0,
    slope_K(V) = -A0 b0 < 0 = slope_K(W).

The second equality uses the D-parallel determinant trivialization and det K=1. Equivalently degree_K(V) is one fifth of the already-computed outward Xi current. This supplies analytic stability for every fixed b0>0. It is not inferred from a negative number alone: the invariant-subbundle classification is essential. At b0=0 the strict inequality disappears; at b0<0 it reverses. Those controls delimit this sufficient application, not all possible asymptotic completions.

## Tension and the global conclusion

The full reference tension D_K^* psi_K vanishes on the exact end, so it is smooth and supported in a compact region. Since phi is positive there, its norm is bounded by C phi. Its trace vanishes everywhere: the determinant connection and determinant metric are parallel and fixed. Flatness of D is the candidate's relator property on the fixed manifold, not a property created by changing K.

Corollary 1.1 and Proposition 3.8 therefore give a smooth harmonic H with det(K^-1 H)=1, bounded relative metric and L2 covariant relative derivative. The determinant condition and positivity also bound the relative inverse. Proposition 4.1 gives uniqueness among mutually bounded harmonic metrics with the same determinant. Changing only the compact extension of K preserves its mutual-boundedness class; the resulting harmonic H is the same by uniqueness. Thus an independently chosen finite-cut metric is not required for existence in this prescribed asymptotic class.

In the supplied flatness/moment residual action this background has zero residuals pointwise. The result is analytic background admission, not an independent derivation of that physical action, its quantum validity or its boundary variations at infinity. The infinite norm of the reference growing Higgs field is not misrepresented as a finite-energy harmonic map.

## What this does not transport

The theorem gives bounded relative metric and an L2 relative derivative. It does not say H equals the explicit end metric outside a compact set, approaches it in a specified C1 weighted norm, or keeps the old finite-cut framing. Therefore the explicit Whittaker profiles, full zero Cauchy plane, decoupled charge channels and compact-domain family count must not be copied onto H without a further operator/asymptotic argument.

All positive b0 values satisfy the stated stability inequality. Existence therefore does not select its magnitude, an integral cusp unit, a gauge 3+2 phase, a parent or a generation number. Genesis selection remains a separate requirement. The meaningful removed condition is an extra assumption of global harmonic existence for this particular fixed end class, subject to the proof's analytic review and exact coefficient checks. Physical real-gauge/fermion/boson matching, spectrum, normalization, anomaly, gravity and a complete TOE remain unproved.
