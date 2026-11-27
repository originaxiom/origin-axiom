# Momentum law for the full source and its weak-to-hypercharge ratio

20 November 2026. Physical seat, hand derivation for review. At 32514763f the real bulk doublet produced a compactly supported closed quadratic curvature source S=[a∧a]/2 at a flat E8 connection. Every sourced component had an ordinary primitive, and the hypercharge longitude period prohibited a finite-norm exact compensation. Here the source is treated as prescribed at external Euclidean momentum of length k>0. We compute its leading response without truncating the end or imposing a boundary mass.

## One variational coefficient for all sourced directions

Use the actual positive invariant gauge metric. Work in the covariantly orthogonal sum of the sourced parallel A and B coefficient systems, or in the full adjoint with its orthogonal complements. On the compact core let b₀ be any solution of d_A b₀=−S with torus-harmonic trace β₀ after the collar correction. Let H_T be the space of parallel-coefficient harmonic one-forms on the boundary torus. Let L be the image of absolute core H¹ in H_T. The coset β₀+L depends only on the source and on the convention for fixing its first-order relative representative. Define β_* to be its element of smallest torus norm, using the metric at the cut. It is obtained by orthogonal projection perpendicular to L. More generally changing a by a compactly supported linear gauge variation changes S by a covariantly exact compactly supported term, by the flat covariant product rule. Its ordinary primitive changes by that compact term and leaves the period coset unchanged.

Suppress 1/(2g₇²). For the source experiment minimize

    J_k(b,f)=‖d_A b+S‖² + ‖ik b−d_A f‖²

over the actual internal one-form response and longitudinal external connection. This retains the linear Gauss variation. No independent boundary kinetic term is supplied. On the end S=0. If u∈H_T is the boundary harmonic trace, projection and completion of the radial square as at f950586f3 give end energy ≥k‖u‖². On the compact core Stokes and duality give, for a constant c>0 independent of k,

    ‖d_A b+S‖²_core ≥ c dist(u,β₀+L)².

Indeed the difference b−b₀ pairs on the boundary with a finite set of harmonic traces of closed dual core one-forms. By Poincaré–Lefschetz duality these functionals have common kernel L. Choose their extensions equal to their harmonic representatives on the collar; the nonharmonic trace components do not enter. Each pairing is bounded by a constant times ‖d_A b+S‖_core. Equivalence of norms on the finite-dimensional quotient gives the asserted estimate.

Minimization of the two lower bounds over u gives kc/(k+c) times ‖β_*‖². For an upper bound choose a smooth core primitive with trace precisely β_* (add an extending closed form and make the collar correction). Continue it as exp(−kr)β_* down the cusp and take f=0 for this trial. Its end energy is k‖β_*‖² and the remaining cost is k² times a fixed core norm. Hence, for fixed S and metric,

    inf J_k = k‖β_*‖² + O(k²),       k→0⁺.

This is an equality for the leading coefficient. Nonharmonic modes, the Gauss variation and arbitrary adjusting bulk traces have all been allowed. The hypercharge period makes the coefficient strictly positive for this nonzero doublet. The static zero infimum and this nonanalytic momentum dependence are compatible. The argument does not replace this forced-source response with a local, momentum-independent Higgs quartic.

## Two contributions have an exact ratio

For the parallel weak and hypercharge directions the bulk coefficient is trivial. On a knot exterior the restriction of ordinary H¹ to the end is the meridian covector line, by abelianization. Thus the only fixed period of a primitive modulo that restriction is its longitude integral. If α has prescribed longitude integral A_λ, the minimal squared torus norm is Area(T) |A_λ|² / length(λ)²: its constant covector is parallel to the metric dual of the longitude displacement. This factor is invariant under a common rescaling of the horotorus. By Stokes the integral of the primitive around λ is minus the integral of S over the fibre. In the A-adjoint this latter matrix is a common real normalization times I times HH†−‖H‖²1₅/5, where I is the intersection self-pairing from fa7c672a0; using the dual-five convention may reverse the overall sign after identifying the Hermitian matrices. The torus minimization factor, physical trace normalization on A, and internal overlap are the same for its two projections.

In the defining-five trace metric choose the integer generator Y₆=diag(−2,−2,−2,3,3), with norm squared 30. The projection of HH†−‖H‖²1₅/5 onto Y₆ is (‖H‖²/10)Y₆, with squared norm 3‖H‖⁴/10. Its weak traceless part is HH†−‖H‖²1₂/2 on the weak block, with squared norm ‖H‖⁴/2. Their sum has squared norm 4‖H‖⁴/5 as a separate trace check. Therefore the **weak contribution divided by the hypercharge contribution to the leading k coefficient is 5/3**. This ratio uses the normalized subspaces in the same induced metric and is independent of a rescaling of the hypercharge generator. It does not determine either absolute term or compare two measured gauge couplings.

The B-adjoint contribution is orthogonal and nonnegative; its absolute period coset has not been evaluated here. The complete leading coefficient is the norm formula above, not the A part in isolation. Its numerical value for a canonically normalized four-dimensional scalar requires the ratio of the intersection self-pairing to the physical kinetic norm, the B period data, the cusp shape and the common gauge normalization. No free relative multiplier between the weak and hypercharge responses occurs in this fixed model. Other source terms in a fully dynamical external-field scattering calculation require the full action and external kinematics. No measured inputs or scientific execution.
