# Can a triplet projector extend at finite cost?

19 November 2026. C8 continuation of 089ed7820. This compares three different physical questions about its four boundary triplets: exact parallel transport, smooth extension, and the energy a positive covariant-gradient term would charge. The answer to the first question cannot settle the other two. All four projectors act on the same given flat geometric coefficient system.

## Amount lost under exact bulk transport

Work in the centre-odd rank-156 bundle V from Λ²W25 and extend a selected orthogonal triplet projector P by zero outside the twelve harmonic coefficient directions. P is parallel on the peripheral torus: the two peripheral holonomies act by scalars on the harmonic coefficient space and preserve its orthogonal complement. Use the defining Hilbert–Schmidt norm on End(V). At a common basepoint the orthogonal projection of an endomorphism to the parallel endomorphisms of the whole flat core is the finite holonomy average

    A(P) = (1/|G|) Σ_g ρ(g)Pρ(g)†.

Each of the six inequivalent 26-dimensional summands in 089ed7820 contains two boundary torus-character lines with inverse characters. Fix a D sign. It retains exactly one of the two lines in each summand. The Frobenius operator S carries this line to a different summand: 5j equals neither j nor −j modulo 24 for an odd j (the latter would require 4|j). Its ± projector therefore contributes exactly 1/2 to the trace of P on each summand, whichever sign was chosen. By Schur orthogonality averaging kills cross terms between different irreducibles and returns (1/2)/26 times the identity on each. Thus

    A(P)=I_V/52,       ||P||²=3,       ||A(P)||²=3/52,
    ||P−A(P)||²=153/52.

Averaging the squared change ||ρ(g)Pρ(g)†−P||² gives 153/26. The result is identical for all four triplets. In particular the full unmarked holonomy average erases even their distinction from each other. It retains exactly 1/52 of the original squared norm. This fraction measures a component of an operator; it is not an energy, a probability of selecting a vacuum, or a dimensionless SM coupling.

## A real extension is possible

Take the compact smooth knot exterior X with its finite cut. The flat V admits a global unitary trivialization: its holonomy determinant character is trivial because G is perfect, and SU(156) bundles on a three-dimensional CW complex are trivial since SU(156) is connected and π1=π2=0. On ∂X=T² the parallel range of P and its orthogonal complement are unitary flat vector bundles with zero integral first Chern class: their real first Chern classes vanish, and H²(T²;Z) is torsion free. A complex vector bundle over a two-dimensional CW complex is classified by rank and first Chern class. Thus both admit unitary frames there. One may also produce these frames directly on the flat torus: diagonalize the two commuting holonomies and multiply each constant line in the covering frame by a linear coordinate phase with the required quasiperiodicity.

In the global trivialization, juxtaposing these boundary frames gives a smooth map from the torus to U(156), conjugating a constant projector to P. Adjust one frame vector by the inverse determinant to obtain a map to SU(156) without changing P. This map is null-homotopic because its domain is two-dimensional and SU(156) is two-connected. Smooth the homotopy relative to the boundary, use it on a collar, and use the constant projector on the rest of X. This gives a smooth orthogonal rank-three projector with precisely the chosen boundary trace. Continue it by the parallel boundary value on a product end if required. Hence there is no absolute extension obstruction to a spatially varying selector. The construction introduces an interior profile.

## Price of a spatially varying selector at a fixed cut

If a physical field in End(V) has positive covariant-gradient energy in this fixed flat gauge background, its least quadratic cost for a specified trace is the Dirichlet energy of the covariant harmonic extension on X. With no projector constraint this Dirichlet problem has a unique solution for each smooth trace: the zero-trace covariant Laplacian is coercive on a compact connected manifold with boundary, by integration by parts and Rellich compactness. A zero value occurs precisely for traces of parallel endomorphisms. Restricted to the finite-dimensional space of boundary-parallel traces at our marking, the energy form therefore has a strictly positive smallest eigenvalue λ_X on the orthogonal complement of the global commutant. Define λ_X using the Hilbert–Schmidt norm at one boundary point; boundary geometry and all dimensional factors belong in it. Consequently each rank-three selector obeys

    ∫_X ||∇P_ext||² ≥ λ_X (153/52) > 0

for every smooth extension with that trace. There is also a finite upper bound for each one, by the explicit smooth-extension argument. The lower bound already permits arbitrary intervening endomorphisms, and so holds after constraining the field to remain an orthogonal projector. No value, equality of the four actual minima, attainment among constrained minimizers, or uniform spectral gap as the cut moves is assumed. A kinetic term of this form would have to come from the physical action with its own normalization. Gauge backreaction or an independent boundary multiplet changes this variational problem.

This is an opportunity for a genuine next test: the specific core metric and interacting kinetic operator could distinguish profiles even when the full finite-group average cannot. It does not follow that the programme contains such an End(V) field, that its stationary amplitude is nonzero, or that a rank-three boundary reading supplies three chiral families. Auditing an actual candidate field and its action is a prerequisite to assigning vacuum weights here. No scientific run or input credit.
