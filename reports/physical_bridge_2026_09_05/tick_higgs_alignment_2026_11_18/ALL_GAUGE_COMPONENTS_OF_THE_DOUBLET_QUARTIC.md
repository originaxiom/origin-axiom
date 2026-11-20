# Full static gauge response to the bulk weak doublet

20 November 2026. Physical seat, hand proof for independent review. Work on the original one-circuit exterior, with the cubic flat connection of 068043746, ordinary complete cusp, and minimal positive internal Yang–Mills curvature energy. In 1380f749e the distance-one B exterior-square system W gave one complex weak scalar doublet at linear order. At fa7c672a0 its hypercharge component obstructed a second-order flat deformation with fixed end. Here we keep the entire E8 bracket and let the second-order gauge field vary. The comparison uses compactly supported, smooth first-order representatives of the same physical tangent class.

## Which directions the doublet actually sources

Choose a fixed weak amplitude H in the dual A five. The positive-charge part of the first-order one-form has coefficients H⊗η, where η takes values in W with basis e_j∧e_(j+1), in a local parallel weak frame. The minus sign on the weak space around the meridian is included in the coefficient system of η. Add the compact-real conjugate to obtain the real gauge variation a. Set S=[a∧a]/2. It is covariantly closed and compactly supported.

The bracket of two forward components vanishes for this one doublet: in the regular E8 branching the only possible A component of the bracket of two dual fives is the alternating dual ten and H∧H=0. The same holds for two conjugates. Mixed brackets take values in the A and B adjoints, as follows by decomposing dual 5 ⊗ 5 in A and applying the E8 branching. In A their coefficients are multiples of the single traceless matrix HH†−‖H‖² I/5. This is a *parallel* generator, including its weak and hypercharge components. In B the map to the adjoint is the traceless one-index contraction of two exterior-square tensors (the adjoint occurs once). The basis pairs either coincide, share one vertex, or are disjoint. They then give diagonal entries, off-diagonal entries of the form E_(j,j±2), or zero, respectively. Thus the entire B source is carried by the traceless diagonal space and the two offset-two spaces. A computation of arbitrary unsourced adjoint modes is unnecessary for this particular quartic.

## Interior cohomology in the sourced B adjoint

On the traceless diagonal four-space the fibre has no invariant since X is a full cycle. The puncture acts trivially. Fibre H¹ has dimension four and restriction onto the four boundary coefficients is surjective, by duality and absence of fibre invariants. Its kernel is zero.

For the other two spaces set W_m=span{E_(j,j+m)}, m=+2,−2. X and D preserve each, while the marked return exchanges them. Neither has a fibre invariant: some longitude characters are nonunit and X shifts transitively among the five coordinates. Here and below a nonunit *character value* means a value different from one; all gauge matrices are unitary. On W₂ the longitude entries are c_j/c_(j+2) with c=(ω,1,ω,1,ω). The unit indices are 0,1,2. Thus fibre H¹ has dimension five, boundary quotient dimension three, and the kernel K₂ has dimension two. The dual space W_−₂ gives the conjugate calculation.

Calculate the double return before restricting to K₂. Let L=g⁻¹ and H'=LX on this adjoint system. On cocycle pairs use the block matrix [[L+H',LX²],[L,H']] as at 4e73d42c3. In its square subtract L² for coboundaries. Of the remaining trace terms, LH', H'L, LX²L and L²X² all shift j by a nonzero offset and have zero trace on W₂ individually. The two surviving terms are H'²=h⁻². The ordered diagonal of h⁻² on the defining five is (1,s,s,s,1) for s=ω². Taking ratios for W₂ gives (s²,1,s,s,s²), with sum −1. The double return on absolute H¹ thus has trace −2. On its three-dimensional boundary quotient the eigenvalues s²,1,s sum to zero.

The determinant on absolute H¹ for this double return is one. In the pair-of-cocycles map between the two offset spaces the word part contributes det X=1, while the two coefficient-sewing factors and the coboundary divisor leave one det L between bases. Composing the two maps contributes det(L²|W₂)=1: g² is diagonal on the original five, and the five ratios between j and j+2 multiply to one. The boundary determinant is also one. Hence the polynomial on K₂ is (z+1)². This argument needs no decision about a Jordan block. One circuit on W₂⊕W_−₂ cannot have a fixed interior fibre vector because its square has no eigenvalue +1 on either interior part.

On these diagonal and offset systems the global H¹ embeds in fibre H¹ by the mapping-torus sequence, since H⁰ of the fibre vanishes. A global class restricting to zero on the torus would give a fixed interior fibre class, which the above calculations exclude. Thus the relevant B systems and their duals have zero image from relative to absolute H¹ on this core.

## A primitive for the complete source

The A source has an ordinary primitive because the ordinary H² of the knot exterior with trivial real coefficients vanishes. For each B source component, relative-to-absolute H² is the transpose, by Poincaré–Lefschetz duality, of relative-to-absolute H¹ for the dual system. Its image therefore vanishes. The compactly supported source has zero ordinary class in every component. A real smooth primitive b exists on the compact core with d_A b=−S. This claim concerns ordinary cohomology. Its relative version fails by the nonzero hypercharge pairing at fa7c672a0.

Choose b_A along the one parallel generator and b_B in the indicated flat subbundle. Near the seam S vanishes. In a collar replace b by a cohomologous representative equal to the harmonic torus period form β, using a cutoff exact correction. The B coefficients of β on the cut are simultaneous invariants of the two unitary holonomies, hence lie in the joint B centralizer. On the longitude-unit pair the peripheral meridian eigenvalues +s,−s are distinct. On the remaining three coordinates they are +1,−1,s and likewise distinct, using the cubic lift. Thus all five joint characters are distinct and the joint B centralizer is abelian. The A component is along a single generator and commutes with B. In particular [β∧β]=0, even if several B periods are present. The hypercharge longitude period of β is nonzero for H≠0.

Extend b along the cusp as χ(r/L)β, with χ equal to one near zero and zero beyond one. The complete second-order residual is just dχ∧β on the end. Its squared norm is ‖β‖²(∫|χ′|²)/L, since the inverse tangential metric cancels the shrinking torus area. The squared kinetic norm of the continuation is L‖β‖²∫|χ|². Each cutoff is finite-norm and preserves the asymptotic flat end. Consequently

    inf_b ‖d_A b+[a∧a]/2‖² = 0

for the entire gauge algebra in this setting. There is no minimizer with finite one-form norm for nonzero H: any exact compensation is closed outside the source, and the forced longitude period would give an infinite norm. At a fixed cut with fixed trace the hypercharge lower bound still holds.

## Check against the exact Yang–Mills energy

Take an amplitude ε>0 multiplying a fixed nonzero real doublet direction, and A_ε=A₀+εa+ε²b_L. On a fixed compact part the remaining curvature is ε³[a∧b]+ε⁴[b∧b]/2. On the long cusp a=0, b_L is abelian and its only curvature is the cutoff derivative. Constants below refer to a fixed compact representative, directions and length units. For L large and ε small this gives

    ‖F(A_ε)‖² ≤ C₁ ε⁴/L + C₂ ε⁶,
    ‖A_ε−A₀−εa‖₂ ≤ C₃ ε²(1+√L).

Choosing L=ℓ/ε gives energy O(ε⁵) and an o(ε) correction in the positive kinetic norm. The nonnegative curvature energy therefore admits configurations tangent to this same doublet whose energy divided by ε⁴ tends to zero, with fixed asymptotic end. A strictly positive, uniform static quartic lower bound in this kinetic topology is impossible in the supplied model. These are trial configurations. They need not be stationary, twice differentiable as a path in the kinetic Hilbert space, or uniformly small pointwise in an orthonormal frame far down the narrowing cusp. A local four-dimensional Wilsonian coupling, a finite external frequency, extra fields, or a stronger allowed topology pose different questions. This estimate neither constructs a Higgs vacuum nor says that an interacting theory has zero potential to all orders.

Review priorities are the sign of the double-return eigenvalue in K₂, absolute versus relative exactness, and commutativity of all end coefficients in the exact curvature estimate. No measured inputs or scientific execution.
