# The cubic background's interior return in the charged 10

20 November 2026. Physical seat, analytical result for independent review. At f950586f3 the extending charged boundary period had a continuum response. That computation left open states invisible to the boundary. Here we calculate the return on the entire interior degree-one cohomology of the punctured fibre in the B five, the coefficient system of the A ten. No interpolation in complex structure or projection to a chosen Hodge type is used.

## Recover the actual three-dimensional interior space

Keep precisely the flat marked history at 068043746, on the wall p=q=ω=exp(−2πi/3), with special-unitary meridian lift s=ω². Write V for the defining B five, c=[X,D], g for the return and h=X⁻¹g for its peripheral representative. The compact core of the fibre Σ retracts to the two handle circles. H⁰(Σ;V)=0 by irreducibility and nontriviality, so H¹(Σ;V) has dimension five. Restriction to its boundary circle surjects: the next group H²(Σ,∂Σ;V) is dual to the invariants of V*, hence zero. H¹(∂Σ;V) identifies with V/(c−1)V, equivalently the longitude-unit two-plane in this unitary system. The kernel K of restriction thus has dimension three. K is the image of relative cohomology. The intersection pairing with coefficient conjugation, multiplied by i, is nondegenerate Hermitian on K: duality pairs relative with absolute cohomology perfectly and the induced form on the image has precisely the discarded radical. The orientation-preserving marked return and its unitary lift preserve this form. Its signature need not be definite.

On left cocycles (x,y), the representation of the inverse coefficient sewing followed by pullback on words is

    T(x,y) = (g⁻¹((I+X)x+X²y), g⁻¹(x+Xy)).

The two returned words are X²D and XD. Subtract the injective five-dimensional coboundary space, on which the return is g⁻¹. Consequently tr(T|H¹)=2 tr(g⁻¹X)=2 tr(h⁻¹) and det(T|H¹)=1. For the determinant the two left multipliers g⁻¹ have determinant one and on each X-eigenline the remaining 2×2 determinant is the corresponding eigenvalue of X. Their product is one. These two checks use the full fibre cohomology.

On the boundary quotient the map is h⁻¹: the automorphism carries c to XcX⁻¹, and the additional coboundary from that conjugation vanishes in the quotient. On V the map h sends j to −j−1. Its unique fixed index 2 has eigenvalue s; the two two-cycles have zero trace also for h⁻¹. In the longitude-unit sector (indices 1,3) the meridian eigenvalues are +s and −s. It follows that on K the trace is t=2/s and the determinant is d=−s². Preservation of the nondegenerate Hermitian form implies tr(T⁻¹|K)=conjugate(t), so its characteristic polynomial is

    P(z)=z³−t z²+d conjugate(t) z−d
        =z³−2s² z²−2z+s².

Changing to inverse-return conventions reciprocates the roots and preserves all finite-cover conclusions.

## Why no power of the return fixes an interior class

Over the Eisenstein integers the prime 2 has residue field F₄ (x²+x+1 has no F₂ root). P reduces to z³+s². Every nonzero residue has cube one and s² differs from one. Hence the reduced cubic is irreducible, and the monic polynomial is irreducible over Q(s), by Gauss's lemma in the Eisenstein integers.

There is also a useful independent modulus check. For the monic cubic with trace t, second coefficient d conjugate(t) and determinant d of unit modulus, expansion of the usual discriminant gives

    disc(P)/d² = |t|⁴ − 8 Re(t³/d) + 18|t|² − 27 = 29.

Here |t|=2 and Re(−8s)=4. If all three roots lay on the unit circle, each factor (z_i−z_j)²/(z_i z_j) would be a nonpositive real, and the product of the three factors would be nonpositive. Thus at least one root lies off the circle. Since the polynomial is irreducible, a root of unity would force all its conjugates over Q(s) to be roots of unity as well. **No root is a root of unity.** In fact the three roots are simple, with moduli R,1,R⁻¹ for some R>1, since the spectrum of a Hermitian-form isometry is invariant under z↦1/conjugate(z). In particular the unit-modulus root also has infinite order.

## Global cohomology and the physical zero-mode test

On the n-circuit mapping torus X_n the fibre invariants vanish. The mapping-torus sequence (or the cocycle equation for its return generator modulo coboundaries) therefore identifies H¹(X_n;V) with the fixed subspace of Tⁿ on H¹(Σ;V), including the appropriate A-side sign on each SM component. A class vanishing at the peripheral torus in particular restricts trivially to the longitude in each fibre, so lies in K. No finite-order return multiplier can make any eigenvalue of Tⁿ on K equal one. Therefore restriction of global H¹ to the peripheral torus is injective in these charged sectors for **every finite cyclic cover** of this specific history, including the conjugate ten. The same argument works if the meridian lift changes by a scalar fifth root. On the third cover the rank-one visible class per parity component at 2fe95628c is consequently the entire global H¹ for that component. On the first cover the group is zero. These conclusions concern this B five and its dual; the B exterior square requires a separate calculation.

For the ordinary flat Hodge/gauge operator on the complete hyperbolic three-dimensional exterior this excludes even an L² harmonic one-form whose ordinary cohomology class might be zero. First, the torus harmonic component of a closed form is constant along the cusp and its nonzero period would have divergent norm, as at f950586f3. Hence the class of an L² closed form has zero boundary restriction and is globally exact by the result above. If a harmonic form is d_A f, the global primitive f can be taken in L². In a radial parallel frame put F(r)=exp(−r/ℓ)f(r) as an L²(T)-valued function. Then F(r) is the sum of exp(−r/ℓ)f(0) and the convolution of exp(−r/ℓ) on the positive half-line with exp(−r/ℓ)∂_r f. The second input is square integrable by the derivative norm, and the convolution kernel has finite L¹ norm ℓ. Thus F is square integrable, exactly the required scalar cusp norm. Integrating against compactly supported cutoffs of f on the complete metric now gives ‖d_A f‖²=0 by co-closedness. This uses the positive flat unitary metric and ordinary complete domain. The boundary continuum still exists; this result excludes a discrete massless one-form in the ten under this operator.

## Allowing a continuously adjusted meridian does not recover a full ten here

For an algebraic control retain the same fibre representation and consider an arbitrary complex return multiplier in A commuting with the SM group and preserving its defining-five determinant. It has form diag(z⁻²,z⁻²,z⁻²,z³,z³): given block entries a,b with a³b²=1 one recovers z=ab. On Q,uᶜ,eᶜ the multipliers on the ten are z,z⁻⁴,z⁶. They include the former parity when z=−1. On a fixed n-fold cover take z to parametrize its return. Interior classes require the relevant multiplier times a root raised to the nth power to equal one (or use all inverse conventions).

If |z|≠1, the three distinct nonzero absolute charges 1,4,6 give three different nonunit log magnitudes in absolute value. The two off-circle eigenvalues supply only one nonzero absolute log magnitude, n log R. At most one of the three charge types can satisfy the equality. For |z|=1 only the unique unit-circle root can contribute. Equality at two different charges would force z to be a root of unity, already excluded by that root's infinite order. Even a separately chosen multiplier for a single component supplies at most one interior direction, since the three return eigenvalues have distinct moduli. This is an exact obstruction to restoring a complete ten by tuning a single commuting holonomy on this history. Nonunitary holonomies here are solely a cohomological comparison; the earlier unitary kinetic proof does not establish a stationary or normalizable nonunitary background.

The missing route to SM3 therefore cannot be a degree-one interior mode of this flat ten recovered by raising the cover degree. A different global operator, background, or genuine charged source still needs to be assessed under its own equations. No new calculation about vacuum selection or gravity is inferred. Independent review should prioritize the boundary correction to the return, the cubic discriminant, and the complete-domain primitive estimate. No scientific program was run and no measured input was used.
