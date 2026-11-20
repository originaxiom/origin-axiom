# The extending weak doublet has a continuum response

20 November 2026. Author hand derivation for independent review. The calculation joins the compact core to the whole complete end on the threefold background of 2fe95628c. It determines the leading quadratic boundary response for the charged *connection one-form*, including the longitudinal Gauss variation. This is a consequence of a supplied minimal Yang–Mills action on four flat external directions times the three-dimensional hyperbolic exterior. The earlier six-dimensional surface parent does not derive this seven-dimensional choice. Its quadratic gauge term is also present in the ordinary gauge sector of a seven-dimensional twisted model at zero background matter.

## Observable and variational problem

Use a flat unitary background and take a nonzero Euclidean external Fourier momentum of length k. Suppress the common positive factor 1/(2g₇²) and normalize the torus harmonic inner product at the cut. Let a be an internal connection variation in a charged coefficient system V and b the external component parallel to the Fourier momentum. The internal and mixed curvature terms in the quadratic action give

    E_k(a,b) = ‖d_A a‖² + ‖ik a − d_A b‖².

At this flat background the different representations are orthogonal. Transverse external components add independent nonnegative terms and attain zero for the prescribed internal trace. Gauge shifts (a,b)↦(a+d_A f,b+ik f) preserve E_k. Vary b rather than setting it equal to zero in the lower bound; its Euler equation is the Gauss constraint d_A*(ik a−d_A b)=0. The trial field for an upper bound need not solve this constraint, since minimizing over b can only reduce its energy.

Let H be the harmonic tangential one-forms on the cut torus with coefficients in V, and prescribe the projection α of the trace to H. Exact gauge variations have zero projection. Define F_k(α) as the infimum over finite-action continuations smooth across the seam in the form-domain sense, allowing the other traces and the Gauss component to vary. No independently adjustable cut field is introduced. For each charged sector with one parallel coefficient in 2fe95628c, H has complex dimension two and the image L of H¹(core;V) in H has dimension one. The dual-five weak doublet has such a line, its color partner has H=0.

## Bound from the end and matching trial field

In the product trivialization along the cusp rays project the tangential part of a at each r onto H, obtaining u(r). In d_A a the normal–tangential component projects to u′ because tangential gradients of the radial component are orthogonal to H. The projected mixed external curvature is ik u for the same reason, even after the b variation. The end metric is dr²+exp(−2r/ℓ)g_T. For a tangential one-form its inverse metric factor cancels the slice-area factor. Angular harmonic projection is unchanged by this constant conformal factor on each two-torus. Therefore

    E_k ≥ ∫₀^∞ (‖u′‖²+k²‖u‖²) dr ≥ k‖α‖².

The second inequality follows from completing the square ‖u′+ku‖² and the L² condition for k>0. The half-line minimizer is u=e^(−kr)α. This is a statement about the entire cusp, including gauge variations and the orthogonal angular modes. A cut made at a different radius uses the same harmonic one-form norm.

For α∈L choose a smooth closed extension η on the compact core. On its collar η and the constant parallel radial extension of α differ by an exact form, since they represent the same torus cohomology class there. Subtract the differential of a cutoff primitive to make η exactly equal to α near the seam. On the end use e^(−kr)α and take b=0 in this trial. The joined form is continuous across the seam; it belongs to the form domain, with smooth approximants. Its energy yields the other inequality

    k‖α‖² ≤ F_k(α) ≤ k‖α‖² + k²‖η‖²_core.

The coefficient of k is thus exact in the normalized action. Integrating out massive modes or minimizing over the external gauge component cannot cancel it here. If only the L projection of the trace is prescribed and its orthogonal component is allowed to relax, the same two inequalities hold by orthogonality and by using the same trial. The proof is uniform on the finite-dimensional L after choosing a linear extension on a basis.

## The complementary direction has a distinct static cost

If α has a component outside L, duality supplies a closed core form η* in V* whose boundary wedge pairing with α is nonzero: L is the annihilator of the dual restriction image by the long exact sequence and Poincaré–Lefschetz duality. Adjust η* to its harmonic representative near the seam by the same collar argument. The pairing sees precisely the harmonic projection of the tangential trace. Stokes gives

    |∫_T ⟨α∧η*⟩| = |∫_core ⟨d_A a∧η*⟩| ≤ ‖d_A a‖_core ‖η*‖_core.

For a fixed nonextending component this gives a strictly positive, k-independent stiffness. Merely counting the two torus one-forms would incorrectly give two equally soft directions.

## Physical meaning and outstanding duties

The inverse response on the freely matched extending line is proportional to |p|+O(p²), where k=|p|. The corresponding linear susceptibility scales as 1/|p|. In particular p² times this susceptibility tends to zero. There is no four-dimensional massless simple pole with nonzero residue in this trace. A finite positive local boundary kinetic term proportional to p² alone cannot change the leading power. Without an end cutoff, its static zero profile is constant along an infinite unweighted radial interval and has divergent norm. This differs from the scalar channel at 2fe95628c, whose constant mode is normalizable on the isolated finite-volume end and has positive compact-core cost.

The continuum interpretation can also be checked on actual transverse fluctuations. Compactly supported tangential waves f(r)α arbitrarily far down the cusp satisfy d_A* a=0 and have radial Maxwell operator −f″ in the physical unweighted norm. Long translated and normalized cutoffs of exp(i m r) supply Weyl sequences for every m²≥0. Their coefficients are co-closed and orthogonal to longitudinal gauge variations. This supplies a genuine charged continuum in the geometric gauge model; it gives no count of global massless fermions, additional invisible core states or generation multiplicities. The conjugate doublet has the same response.

The inverse response does not specify the orientation of L inside H. A calculation of that slope or an interior overlap must use the actual core differential. A physical Higgs or chiral source would also have to survive descent or justify selecting the cover, have a finite four-dimensional norm and the correct fermionic and nonlinear action. No momentum, coupling or length was fitted to observation. Proof and field identification require independent review.
