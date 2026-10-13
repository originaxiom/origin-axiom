# Ordinary and logarithmic spin extensions are different

This is an authored scope and extension calculation for the existing modular sheaf index. It does not replace the punctured-fibre Dirac proof, select a physical completion, or certify a four-real-dimensional operator at a degenerating cusp.

## The geometry determines an open line but not an omitted cusp divisor

Let B=M1,1, Bbar its usual stable compactification, D its cusp divisor, and lambda the extended Hodge line. Hain Proposition4.4 identifies K_Bbar(D) with lambda^2; Exercise34 and Theorem6.9 identify O(D) with lambda^12. These statements distinguish the compactified orbifold from its open part. Locally the first follows from d tau=dq/(2 pi i q), not from a regular dq frame. Consequently

    K_Bbar = lambda^-10,
    K_Bbar(D) = lambda^2.

For the universal stable elliptic surface p:Ebar->Bbar let C=p^-1 D. The relative dualizing line is p*lambda: its invariant differential is nowhere zero in that line, including a nodal fibre, where it is represented on the normalization by dw/w. The ordinary dualizing line of the total surface is the relative line tensored with p*K_Bbar. This gives

    K_Ebar = p*lambda^-9,
    K_Ebar(C) = p*lambda^3.

The local node model xy=q confirms there is no extra canonical pole: (dx/x) wedge dq = dx wedge dy. In the logarithmic version divide by q. Removing the marked section does not change these identities on its complement. This calculation does not choose the coefficient extension at that section or at the node.

On the root gerbe where lambda^(1/2) exists, the displayed ordinary and logarithmic spin lines can be chosen as p*lambda^(-9/2) and p*lambda^(3/2). They differ by p*lambda^6. On B, lambda^6 is a nontrivial order-two line, while lambda^12 is trivialized by the discriminant; on Bbar it is not torsion. Thus dropping the cusp divisor is not automatically harmless even at the spin level. The gerbe and any further flat spin choices are named mathematical data, not a derivation of physical spin.

W45's weight3/2 is the logarithmic extension of this formula. It is valid on the open surface. Calling it the unique ordinary compact spin extension would be a stronger statement. Neither the geometry here nor this comparison says which extension should be used by the physical parent.

## Exact conversion to the already tested opposite sign

Let epsilon be the order-two modular character with epsilon(S)=epsilon(T)=-1. The classical eta laws give

    eta^12: weight6, multiplier epsilon, cusp order1/2,
    (eta^12)^2=Delta.

The discriminant result is already proved in theta_cusp. Eta has no zeros on the upper half plane. Multiplication by eta^12 therefore identifies the OPEN automorphic bundles at (k-6,rho) and (k,epsilon rho). The multiplier change is exactly W46's already tested other overall sign. It is not a new metaplectic lift.

The identification need not preserve their canonical cusp extensions. Diagonalize rho(T), and write a component as q^alpha sum_(m>=0) a_m q^m, with 0<=alpha<1. Under multiplication its exponent becomes alpha+1/2. The normalized exponent of epsilon rho is

    beta = alpha+1/2-floor(alpha+1/2).

If alpha<1/2, the image begins at q^beta. If alpha>=1/2, it begins at q^(beta+1): its canonical leading coefficient must vanish. The remaining factor product_(n>=1)(1-q^n)^12 is an invertible holomorphic germ. Conversely that leading-coefficient condition lets division by eta^12 recover a canonical source germ. This proves the cusp sheaf identification in both directions, including alpha=1/2, rather than comparing only monodromy eigenvalues.

Writing E_k(rho) for the canonical modular sheaf with these cusp exponents, the exact sequence is

    0 -> E_(k-6)(rho) --eta^12--> E_k(epsilon rho)
      -> C_D^(r_high) -> 0,
    r_high = sum of multiplicities with alpha>=1/2.

The quotient is understood in the effective cusp chart; the compatible central character makes the weighted bundle descend there. The sheaf map is invertible away from D and has exactly the specified one-order zeros at D, so no other divisor contributes. Euler characteristic is additive even when global evaluation on the leading coefficients is not surjective. Hence

    chi_(k-6)(rho) = chi_k(epsilon rho) - r_high.

This all-weight identity is an elementary modification law. Substitution into W45's Riemann--Roch expression provides a second check: the volume term changes by -d/2, the S and ST terms agree after the sign change, and the exponent sum contributes d/2-r_high. Simply changing the sign at the original weight, as W46 H3 does, omits this extension correction.

## The original zero baseline is retained

The normal-form triplet comes from (theta2^2,theta3^2,theta4^2)/eta^3. Its S and T matrices are specified in the preregistration and give cusp exponents (1,3,7)/8; its dual gives (1,5,7)/8. This uses the established theta identification, not a new derivation of its physical meaning. The six-dimensional local coefficient is reconstructed separately from the W28 moves; it is not equated with the cohomology triplet by dimension.

At W46's weights (3/2 for the first triplet, 1/2 for its dual, 1 for the local subquotients), the original and sign-twisted exponents all exceed or equal1/8. Divide a holomorphic modular section by eta^3. At weights below3/2 the quotient has negative weight and no cusp pole; finite unitary monodromy allows passage to a finite cover, where the corresponding negative-degree line has no section. At weight3/2 it has weight zero; boundedness extends it over the cusps, so its coordinates on that finite cover are constant. The exact simultaneous S/T invariant-space test for rho/chi_eta^3 is zero. The same argument applies to the dual spaces of weight2-k. Thus the old zero Euler numbers are retained. The scalar eta^3 itself is a positive control: after dividing by itself its invariant line survives.

The verifier also evaluates the old formula exactly, with scalar calibrations, reconstructs exponent multiplicities by spectral projectors, and checks the shifted identity. The numerical Euler tables to be reported are consequences for these specified modular sheaves. They are not a new spectrum of a compactified total-space Dirac operator.

## Consequences for the genesis duty

The distinction is not a reason to reject W45/W46's tables in their stated modular convention. It explains why an open canonical-bundle formula and testing two lift signs do not, by themselves, identify every spin extension at the cusp. A six-weight change can be rewritten as the other already known sign together with a specific nonuniform cusp condition. This removes an ambiguity in comparing the existing descriptions; it does not generate a preferred nonzero unit.

A physical use still has to supply the same field bundle, spin extension, metric and closed total-space domain, including the degeneration of the fibre. The newly proved fixed-fibre Fredholm statement does not provide those uniform cusp estimates. Nor does this packet establish the full family-index map or transport the sheaf calculation into the silver compact-cover parent. No Standard-Model parameter, physical generation count or new action is inferred. The next duty is to compare the actual parent with these explicitly distinguished extensions before claiming a natural cusp condition is forced.
