# Transport of parity cohomology and local end data

Assume the specified common-point representation rho and its three parity twists rho_p=chi_p rho. This construction is an input: no claim here forces the quaternion point or its matter interpretation from PF1–PF3. The degree-one cohomology is computed directly from cocycles z(xy)=z(x)+rho_p(x)z(y), modulo coboundaries delta v(x)=(rho_p(x)-I)v.

## Cohomology and inner transport

The free group has no relations, so z(a) and z(b) are arbitrary. Since rho_p(a) has eigenvalues +i and -i, rho_p(a)-I is invertible. Each cohomology class has exactly one representative with z(a)=0, with coordinate

    z(b) - (rho_p(b)-I)(rho_p(a)-I)^-1 z(a).

Thus each parity contributes two dimensions. The second chart z(b)=0 exists for the same reason and has transition matrix -(rho_p(a)-I)(rho_p(b)-I)^-1. No numerical rank or published dimension formula is needed.

For an automorphism f and a chosen intertwiner g satisfying rho(f(x))=g rho(x) g^-1, the pullback is

    C(f,g)[z] = [g^-1 z(f(x))]

in parity p composed with f. The cocycle identity shows that this maps cocycles to cocycles; a coboundary delta v maps to the coboundary with vector g^-1 v. Composition reverses: C(f g, g_f g_g)=C(g,g_g) C(f,g_f), with the automorphism g and its lift distinguished by the subscripts in this identity.

For h=J_q and U=rho(q), expand the cocycle directly:

    U^-1 z(q x q^-1)
      = chi_p(q) z(x) - (rho_p(x)-I) U^-1 z(q).

The second term is a coboundary. Consequently C(h,U) is chi_p(q) times the identity on that parity. On the direct sum it is D_q=diag(chi_p(q) I2), a constant unitary involution. For f'=h f h^-1 and g'=U g U^-1, functoriality gives

    C(f',g') = D_q^-1 C(f,g) D_q.

This proof holds for every word q, not only the four words used to reconcile the elementary pairs. All parity projectors commute with D_q. Every invariant subspace transports, and the two algebraic triplets transport without changing dimensions. In particular, any block-diagonal Hermitian pairing on the parity sum is preserved by D_q: scalar signs cancel on each block. Thus a previously established Hodge-sign assignment with that direct-sum pairing is preserved, not newly established by this calculation.

## The local puncture representation is different

Let u_(1,0)=j, u_(0,1)=i, u_(1,1)=k, so rho_p=u_p rho u_p^-1. B1606's local matrix for an elementary move f has block p to r=p composed with f equal to u_r^-1 g u_p. This is the local solution representation, not the cocycle quotient above. For the transported lift, its block becomes

    u_r^-1 U g U^-1 u_p
      = (u_r^-1 U u_r)(u_r^-1 g u_p)(u_p^-1 U^-1 u_p).

Therefore the independently reconstructed local matrices satisfy M'=E_q M E_q^-1 with E_q=diag(u_p^-1 U u_p). Since U and all u_p are unitary quaternion matrices, E_q is unitary and commutes with the parity projectors. This holds for the original block convention as written; no assumption identifying a local pushforward with the cohomology pullback is made.

Invariant orthogonal projectors B correspond bijectively under B'=E_q B E_q^-1. Their dimensions, commutation with parity grading, and commutation with the corresponding move matrices are preserved. The exact commutant computation in the producer checks B1606's stated dimensions 2 and 1. For unitary generators, commutant dimension one implies irreducibility: a proper invariant subspace would have a nontrivial commuting orthogonal projector. The graded extreme conditions 0 and the full local space are consequently unchanged as subspaces. This proves transport of the algebraic local condition, not the existence or uniqueness of a physical self-adjoint extension on a specified noncompact spacetime.

## The lift sign is preserved

For c=aBAb, rho(c)=-I while chi_p(c)=1. With the natural intertwiner rho(c), C(J_c,-I)=I. Changing that intertwiner's sign gives C(J_c,+I)=-I. Both cover the same word automorphism. This is why a based automorphism and its metaplectic lift cannot be substituted for each other.

Multiplying an original move lift by -1 multiplies its induced matrices by -1. Conjugation by U preserves that sign, and replacing U by -U changes neither conjugated move lift. Hence coherent base-point transport requires no new sign choice but does not remove the previously chosen central-lift information. In particular it cannot turn B1634's genuine representation into a merely projective one or discard its nontrivial central action.

## Uniform pole order and the remaining conditions

For a constant invertible matrix D and a vector Laurent series s(t)=t^m v+terms of higher order with v nonzero, D s(t)=t^m D v+terms of higher order and D v is nonzero. The order is exactly m. Thus such transport preserves every uniform pole-order condition. The same observation applies to constant changes within parity blocks and to the transported local projectors defining half-exponent extensions.

This statement uses the same base coordinate and transports the coefficient system. It neither constructs the global compactification nor proves the index formula of W45/W46. In any Fredholm realization whose operator and domain are both transported by these bounded unitary maps, kernels and cokernels correspond by direct conjugation, so its index is unchanged. That last assertion is conditional on having that realization and on transporting its domain; it is not a substitute for proving those analytic hypotheses.

The consequence is a strengthening, not a new physics claim: the coherent positive-pair convention does not introduce a further freedom into these existing graded mathematical constructions. The representation-to-matter link Λ, the original lift conventions and the unit of cusp data still have to be justified on their own terms. Changing base point supplies no preferred pole order and no physical interpretation.
