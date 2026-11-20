# A normalizable weak doublet in the interior of the original exterior

20 November 2026. Physical seat, hand proof for independent review. Compute the other mixed E8 sector of the same cubic-root flat connection as at 4e73d42c3: the A dual five carries the B exterior square. The two charged representations inside that dual five have A-meridian parity +1 for the color antitriplet and −1 for the weak doublet. The first exterior already supports a weak-doublet interior zero mode even though neither component has a periodic boundary coefficient there. The third cover acquires two interior color-antitriplet copies alongside its weak one. These are statements about the positive quadratic gauge-one-form action on the complete exterior.

## Two five-dimensional coefficient systems and their traces

Use indices mod five and for d=1,2 take the basis v_j=e_j∧e_(j+d). These two subspaces partition the ten coordinate pairs. Both are preserved by the fibre handles and return: X shifts the index by one, D shifts it by two with phases, and g sends j to −j−d with an exterior reordering sign. Write X,g,h for their actions on each block in what follows, always with h=X⁻¹g. For the defining five the longitude has unit eigenvalues at 1,3 and ω at 0,2,4. On the d=1 block the longitude has no unit eigenvalue. On d=2 its only unit line is e₁∧e₃, moved by X. Consequently neither block has a fibre invariant. Each absolute fibre H¹ has dimension five. The interior part K has dimension five on d=1 and four on d=2.

Keep the complete cochain operator and subtract its coboundary operator as at 4e73d42c3. With L=g⁻¹ and H=LX, the block matrix before passing to cohomology is [[L+H,LX²],[L,H]]. Expanding the diagonal blocks of its square and using cyclicity of trace gives

    tr T = 2 tr(h⁻¹),
    tr T² = 2 tr(L²X) + 2 tr(h⁻²) + 2 tr(L²X²) = 2 tr(h⁻²).

Here g² is diagonal and X, X² are fixed-point-free shifts. The determinant on fibre H¹ is det(X)/det(g)=−1 on either wedge block: X is an even five-cycle and g is a reflection permutation of five (two transpositions) with a minus sign on each of the five basis vectors. Its other phases multiply to one because the defining-five return coefficients have product one.

For a check using the original five, h⁻² has ordered diagonal (1,s,s,s,1), with s=ω². The determinants of h on its swapped defining pairs (0,4) and (1,3) are respectively −1 and −s². Those pairs supply its unique fixed basis lines in d=1 and d=2. Thus the two traces of h⁻¹ on the wedge blocks are −1 and −s. Summing the five pairwise products of the ordered diagonal gives the traces of h⁻² as 1+2s+2s²=−1 and 4s+s², respectively. On the boundary quotient in d=2 the eigenvalue is −s; the quotient for d=1 is zero.

## Factor the two interior characteristic polynomials

On each K the oriented intersection Hermitian form is preserved. For a return with determinant D of unit modulus the elementary eigenvalue coefficients satisfy e_(m−j)=D conjugate(e_j) in dimension m. Use e₂=((tr T)²−tr T²)/2.

* For d=1, trace −2, trace of square −2, and determinant −1 give

      P₁(z)=z⁵+2z⁴+3z³+3z²+2z+1=(z+1)(z²+1)(z²+z+1).

  All five roots are simple. The interior return has orders two, four and three, with multiplicities one, two and two.
* For d=2, subtract the boundary line before taking these coefficients. The interior trace is −s, the trace of the square is 8s+s² and the determinant is s². This gives

      P₂(z)=z⁴+s z³−4s z²+s z+s².

  It has no unit-modulus root. Otherwise dividing by s z² would give s²z²+z+z⁻¹+s z⁻²=4. Four unit numbers can sum to four only if all equal one. The term z would force z=1 and the first term would then equal s²≠1.

## Count on the original exterior and its covers

On an n-circuit cover the A color sign is +1 and the weak sign is (−1)ⁿ. For d=1 there is no peripheral cohomology at all (c−I is invertible), so **every returning fibre class gives an interior global class** by the mapping-torus sequence and vanishing fibre invariants. For d=2 any interior global class would have to restrict to a returning element of K, excluded for every n by P₂. This avoids treating fixed fibre-boundary classes as interior classes. No semisimplicity assumption on the full d=2 extension is needed.

| cover | interior color-antitriplet multiplicity | interior weak-doublet multiplicity | connected gauge group |
|---|---:|---:|---|
| original, n=1 | 0 | 1 | SM |
| third, n=3 | 2 | 1 | SM |
| any odd n | 2 if 3 divides n, otherwise 0 | 1 | SM |

For even n the group grows to SU(5) and both components have the same count: one from −1, two more if four divides n, and two more if three divides n. This restores complete multiplets as required by the enhanced gauge symmetry. Complex conjugation yields corresponding dual modes. The real internal connection identifies conjugate amplitudes, so a single original weak-doublet multiplicity in the complexified adjoint and its conjugate describe one complex scalar doublet at quadratic order; they do not establish a chiral Weyl doublet.

## The physical norm and kernel

An interior class admits a smooth compactly supported closed representative η: on the collar its boundary restriction is exact, allowing subtraction of a cutoff primitive. Its harmonic projection for the complete flat unitary L² complex has the same ordinary class. Indeed a closed L² form differs from its harmonic projection by an L² limit of exact forms. Pairing with each compactly supported closed two-form in the dual coefficient system is continuous in L² and kills exact forms. These pairings distinguish ordinary classes by duality. Conversely every L² harmonic one-form has zero restriction at the cusp, and an exact one vanishes by the weighted-primitive estimate at 4e73d42c3. This gives the stated absolute, finite-norm counts. Independently, on a finite cover trivializing the finite holonomy one can apply the ordinary cusped hyperbolic result and take the equivariant components. [Han, §2, harmonic forms and compactly supported cohomology](https://arxiv.org/pdf/2011.14457)

For the supplied Yang–Mills quadratic form the internal closedness gives zero mass energy and co-closedness enforces the longitudinal Gauss equation for the mode. With its finite positive norm the mode has an ordinary external p² kinetic term and its own normalized mode projection has a massless pole in the linearized theory. It is not an exact gauge variation. On the third cover it lies in d=1, orthogonal to the periodic doublet line in d=2 whose trace has the |p| continuum response at f950586f3. On the original exterior the bulk mode exists despite absence of any harmonic charged boundary trace. This corrects an inference one could have drawn from the boundary measurement alone. It does not establish the mass of the interacting mode, a vacuum expectation value, the Higgs potential or a fermion Yukawa coupling. In particular the ten-sector calculation found no corresponding normalizable flat gauge-one-form quark modes. The complete gauge operator, the twisted fermion action and gravity have distinct obligations.

No new numerical or scientific code ran. The wedge reorder sign, the two-cocycle-square traces, the absence of a boundary quotient in d=1, and the distinction between the two doublet observables are the highest-priority independent checks.
