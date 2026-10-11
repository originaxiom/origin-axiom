# Minimal symmetry requirement for the puncture condition

Pre-execution conditional proof and source audit, 2026-10-11. This strengthens the algebraic certificate for W28 E4 without claiming a new physical selection law. The hand arguments precede the new exact verifier's first execution; execution outcomes will be recorded separately.

## The existing result and its exact hypotheses

Use W28's local puncture coefficient space C6 with its positive Hermitian metric, in the parity block basis. Its move representation is unitary and has commutant span(P2,P4), where

    V2 = {(v,v,v) : v in C2},
    V4 = {(v1,v2,v3) : v1+v2+v3=0},
    P2 = (1/3) J3 tensor I2,   P4 = I6-P2.

Here J3 is the all-ones matrix. The commutant statement is rederived below directly from the move matrices, without enumerating the finite group. The associated fibre index dim(Lambda_plus)-3 is a further premise of the puncture model, not a theorem about every physical Dirac operator.

W24, W28 and W49 identify the flat coefficient as three copies of the quaternion doublet. Let U1,U2,U3 be its three distinct quaternion units, chosen with the signs and order appropriate to that identification. They are unitary and form a complex basis of the traceless 2 by 2 matrices. Set Phi=diag(U1,U2,U3). The flat endomorphism algebra is

    F_X = Phi (X tensor I2) Phi^-1,   X in M3(C).

This is the established flat coefficient identification. It is not yet an identification with an interacting gauge-matter sector.

## Direct proof of the move commutant

In W28's parity order the move matrices have the form

    L = Pi13 tensor (I2+i Z)/sqrt(2),
    R = Pi23 tensor (I2-i Y)/sqrt(2),

where Z and Y are the usual Pauli matrices and Pi13,Pi23 are the transpositions of three blocks. Overall lift signs do not affect commutants. The squares are

    L^2 = I3 tensor i Z,
    R^2 = I3 tensor (-i Y).

Every 6 by 6 matrix K commuting with L and R therefore has each 2 by 2 block commuting with Z and Y. Commutation with Z makes that block diagonal; commutation with Y makes its diagonal entries equal. Thus K=X tensor I2. Commutation with L and R now requires X to commute with Pi13 and Pi23. These transpositions generate all permutations of three letters. Invariance of X under simultaneous row and column permutation makes all its diagonal entries equal and all its off-diagonal entries equal. Consequently X=a I3+b J3, which is precisely span(P2,P4) after tensoring with I2.

Conversely, P2 and P4 commute with both moves, so the calculation is an equality, not only an upper bound. The group is unitary. The orthogonal projection onto any invariant subspace commutes with it and hence is a P2+b P4 with a,b each 0 or 1. Therefore its invariant subspaces are exactly 0,V2,V4,C6. This gives the needed content of W28 E2 without floating-point ranks or group-order assumptions. The input matrices remain those of the stated puncture representation; their physical identification is not derived by this argument.

## Exact proof of the scalar stabilizer

Suppose F_X sends V2 into V2. There is a 2 by 2 matrix T such that, for every v, all three output blocks of F_X(v,v,v) equal Tv. Therefore for each i,

    sum_j X_ij U_i U_j^-1 = T,
    sum_j X_ij U_j^-1 = U_i^-1 T.

The left side is traceless. Hence Tr(U_i^-1 T)=0 for i=1,2,3. These three matrices span sl2(C), whose trace pairing is nondegenerate and whose orthogonal complement in M2(C) is the scalars. Thus T=lambda I2. Comparing coefficients in the basis U_j^-1 gives X_ij=lambda delta_ij. Conversely, scalar X plainly preserves V2. This proves that its stabilizer inside the full flat endomorphism algebra is exactly the scalars.

Since Phi is unitary, F_X dagger=F_(X dagger), and V4=V2 perpendicular. If F_X preserves V4, then F_X dagger preserves V2: for w in V2 and v in V4, their pairing through F_X is zero. The result just proved forces X dagger, hence X, scalar. Conversely scalars preserve V4. This is the second stabilizer statement. Neither direction uses sampling, tolerances or a matrix-group census.

This is an independent short derivation of the result already stated by W28 E4, whose producer obtains it by numerical nullspace and stabilizer calculations. It is not claimed as a previously absent theorem. Formal banking and executable exact controls remain pending.

## The smaller sufficient requirement

Retain the move-invariance premise. Let U be one extra unitary symmetry on C6. The commutant of the enlarged group is scalar exactly when [U,P2] is nonzero. Indeed, every operator commuting with the moves has the form a P2+b P4, and its commutator with U is (a-b)[P2,U]. A unitary representation has no proper invariant subspace when its commutant is scalar, since the orthogonal projection onto an invariant subspace would belong to the commutant.

In particular, any single non-scalar unitary F_X from the flat flavour group excludes both V2 and V4. Full U3 symmetry is sufficient but is more than this step needs. Breaking the U1 factor, or failing to preserve the full U3, would therefore not by itself refute the route to the two extreme conditions. The relevant check is whether some actual surviving symmetry has the required nonzero commutator.

A concrete sufficient element is D=diag(1,-1,-1) tensor I2 in the parity block basis. It is also F_X for X=diag(1,-1,-1), because this X commutes with Phi. It is unitary, has order two, and X has determinant one. The (1,2) block of [D,P2] is (2/3)I2, so it has the required nonzero commutator. Conjugating by the move permutations generates the other parity signs. Thus, subject to the move-invariance and boundary-invariance requirements, one specified Z2 flavour symmetry is enough; no continuous flavour group is needed for this algebraic step. Conversely, a scalar phase commutes with P2 and does not remove either intermediate condition.

Under these assumptions the puncture choices are 0 and C6, with stipulated fibre indices -3 and +3. This argument does not choose a sign, a modular cusp integer, a gauge representation, or a spacetime interpretation. It also retains the assumption that the boundary subspace is invariant under the move representation. A covariant family of subspaces depending on the modulus is a different problem; symmetry relating two moduli is not automatically a symmetry fixing either member of that family.

## The doubled local boundary model separates symmetry from grading

This paragraph concerns an explicitly supplied local coefficient model, not the complete curved parent's physical domain. Take E=C6 with the unitary move-plus-D action above, whose commutant is scalar. On E plus E let the group act diagonally as U plus U. Use the nondegenerate Hermitian Green pairing

    B((u,v),(u',v')) = u dagger v' + v dagger u',
    Gamma(u,v) = (u,-v).

For real t, the six-dimensional subspace L_t={(u,it u)} is null for B: its pairing is it u dagger u' minus it u dagger u', identically zero. Since B has signature (6,6), its null dimension is maximal. It is invariant under every diagonal U, because U(it u)=it Uu. The subspace L_infinity={(0,v)} has the same properties.

This exhausts the invariant maximal-null subspaces of this declared model. Every operator on E plus E commuting with the group has scalar multiples of I6 in its four blocks. The orthogonal projector onto a group-invariant subspace is therefore a two-by-two Hermitian projector tensored with I6. Rank six means that the two-by-two projector has rank one, with range a line spanned by (a,b). Nullity is Re(conjugate(a)b)=0. If a is nonzero the line is (1,it) for real t; if a is zero it is the remaining endpoint (0,1).

Gamma takes L_t to L_minus_t. Only t=0 and the infinite endpoint are grading invariant. These are E plus 0 and 0 plus E, corresponding to the two extreme choices of Lambda_plus in the earlier graded model. Thus the original symmetry-plus-grading conclusion is preserved, while symmetry alone admits a continuous local family in the doubled model. The ungraded members are not assigned the earlier chiral sheaf index; absence of that grading is not a calculation of zero physical index.

A real graph (u,t u) has B equal to 2t u dagger u' and fails nullity for nonzero t. This supplies a rejecting control without imposing the desired endpoints by definition. The verifier also checks the full symbolic projector, diagonal invariance and grading commutator.

No conclusion about global selfadjoint extensions, ellipticity, spin seams, Majorana reality or Lorentz covariance follows just from this coefficient calculation. In particular, it does not show that the two actual physical slots carry the same diagonal U action or that its graph is an admissible field boundary. Those identifications are required before a physical use. The full physical mass map already available on the other branch uses its own source, target and domains rather than this illustrative model.

## What must be tested in the interacting model

For a proposed physical use, give the coefficient map into the actual field bundle and the induced U on these six local data. Verify that its action on every field preserves the kinetic metric, differential operator, interaction tensors, background and specified end structure. An automorphism of a free coefficient system is not sufficient evidence for this whole statement. A canonical boundary assignment from those data would then be invariant under their automorphisms; the necessity of that canonical-assignment requirement is still part of the genesis question.

The existing curved parent is informative but has different stated inputs. Its proof uses adjoint E8 fields A,Q,R and a nonzero vertex Tr(q[A,r]); it keeps the corresponding Yukawa and moment-map terms. It specifies a complete cusp graph domain. W27 instead declares a field in F-MC's E6 representation 27 carrying W. Neither the representation types nor these domain specifications can be identified merely because both accounts discuss quaternion holonomy and zero modes. The map has to precede any transfer of a symmetry or index result.

For the curved parent's internal adjoint vertices, a constant map that preserves the invariant metric and Lie bracket preserves the displayed algebraic interaction tensors. In a background problem it must additionally intertwine the covariant derivatives and preserve the background and domains. Those are concrete tests for a proposed symmetry, not a proof that any given F_X extends to such a map. The newer silver fermion packet supplies an explicit operator/domain map for its own compact-core construction; its proof expressly retains its supplied boundary polarization and parent. That earned map should be preserved without using it as an unstated identification with W27.

## The gauge sign in the supplied interacting frame

The next source comparison recovers a positive answer within a specified frame, rather than leaving every action extension untested. W24 supplies an SU6 embedding in compact E8 with W in the defining six. The physical form-parent proof explicitly uses this SU3 x SU2 x SU6 branching and its family subgroup. Keep the existence and choice of this embedding as supplied; agreement of adjoint characters through another subgroup is not used as proof of an identification of embeddings.

Let iota denote that supplied group homomorphism and let the flat holonomies be iota(W(a)),iota(W(b)). The matrix

    D = diag(1,1,-1,-1,-1,-1)

has determinant one, is unitary, squares to one, and commutes with both block-diagonal W holonomies. Thus g=iota(D) defines a globally parallel gauge transformation of this flat bundle. On the universal cover it is constant; commutation with the holonomies makes it descend. It is not killed by a possible central kernel of iota, since D is not central in SU6. In the untwisted multiplicity coordinates it is the order-two element diag(1,-1,-1) of the supplied family SU3. The action on the defining six is exactly the D used above; on the conjugate and exterior tensor sectors it is the corresponding induced action, not a separately chosen sign.

Set R_g=Ad(g) on every adjoint field in the displayed curved action. Conjugation obeys

    R_g[X,Y]=[R_g X,R_g Y],
    R_g(X dagger)=(R_g X) dagger,
    kappa(R_g X,R_g Y)=kappa(X,Y).

Because g is parallel for A0, nabla_A0 R_g=R_g nabla_A0. Apply the same transformation to the connection fluctuation and both spin fields. Their metric kinetic terms, the cubic trace q[A,r], the full antisymmetric derivative superpotential, all commutator residuals and the moment-map norm are invariant. This uses the generic E8 action already written in the curved-parent proof, instantiated on the specified flat bundle; it does not suppress the companion fields or Yukawa terms. At A0,q=r=0 the background is fixed and the quadratic operators commute with R_g.

The domain statement can also be made directly at this origin. R_g is a bounded unitary map, sends compactly supported smooth sections to such sections, and commutes with the linear kinetic operators. It consequently preserves their graph norms and graph closures. For the nonlinear domain the bracket identities preserve the required integrability of the residuals. Hence D is an actual symmetry of this supplied complete-cusp action and its stated domain, not just a symmetry of an isolated free six-dimensional coefficient. This proof does not extend the claim to a Higgs background that fails to commute with g or to a boundary structure that g does not preserve.

This discharges the existence of an interaction-compatible sign in this frame. It does not derive the frame or action from genesis, require this gauge symmetry to remain unbroken in every candidate phase, or identify its full adjoint matter with W27's E6-27 dictionary. W24's branching and the physical form roster retain both conjugate coloured weak sectors. The rank-six multiplicity must not be counted again as three complete generations independently of that roster.

## Why the domain comparison remains load bearing

The same physical branch already separates three quantities in weave_puncture_operator/PROOF. First, the upper modification exact sequence on the compact elliptic curve gives the sheaf Euler characteristic d-3. Second, a smooth finite-distance deleted point has square-root critical spinor data and a Green-form classification. Third, the complete hyperbolic cusp with ordinary spinor kinetic norm has a different closed operator and end behavior. Its canonical conformal image of the square-root pole has divergent norm, and the ordinary-spin zero-angular channel is not Fredholm at zero. The one-form Hodge norm remains finite; that positive is explicitly retained in the form-parent construction.

These are the physical branch's scoped analytic statements, not new analytic proofs in this draft. They explain why the graph-domain symmetry just proved cannot import the finite-distance sheaf index automatically. In particular, a complete graph domain preserving D need not be described by choosing one of W22's finite-distance critical subspaces. An operator/domain map, or a justified different end law, must precede the index transfer. The later silver packet demonstrates such a map for its own compact-core action and supplied boundary; that is a useful standard of proof, not an identification with this fibre.

The same branch's earlier weave_physical_mass_2026_10_08 packet also supplies an actual four-Weyl operator/domain map for its complete curved parent. Its explicit M=Uout T Uin identity uses the metric, superpotential Hessian and gauge Killing coupling; all four input slots are left Weyl fields. That positive means an internal-grading derivation is not a missing ingredient of every physical realization. The pending doubled Green-data checks concern a separately declared local model, not a replacement for that physical mass operator. The operator-intake draft records a direct algebraic check and an unchanged rerun of the existing physical-mass reference calculation, with 15 predicates passing and byte-identical output.

The next physical obligation is therefore more precise than finding a sign: determine how the genesis chooses the field/operator realization and its end law, while retaining the interaction-compatible symmetry and existing physical operator map. The actual map should be reused; its parent, geometry and stationary background must not be silently identified with W27 or the modular cusp construction. No new symmetry census is indicated. No universal absence or rejection of other completions follows.

## Source scope and verification status

SM reference: 6877cc87d31941a85f139e2f25e5e13694e22ce6. Sources are W24 D0-D1, W28 Rule and NOTE Part I, W28 producer Part I and stored E2-E5 results, W27 Rule, and W49's multiplicity producer. W49's factorization is source evidence, not a fresh numerical reproduction. W50's correction about the ruled branch and fixed-modulus grading remains in force.

Physical reference: 9e434bfaa63cff9450959d54384e1a6ad969546a. The full PROOF files for weave_curved_action_2026_10_08, silver_fermion_action_2026_10_11, weave_puncture_operator_2026_10_08, weave_form_parent_2026_10_08, weave_two_neutral_index_2026_10_08 and weave_sm_parallel_2026_10_08 were read for this comparison. The last two contain a different SU2 acting on the two spin fields Q,R; it is not substituted for the family sign. W24's coefficient and character producer and the physical form producer's roster function were inspected. Their published-source citations and global analytic theorems have not been independently reverified in this continuation; their stated domain distinctions remain source claims here. The gauge-sign and graph-invariance arguments above are explicit conditional derivations for the displayed action and supplied embedding.

The proof above should receive exact executable controls with positive and negative cases after a pre-execution seal, including direct reconstruction of the move matrices, their squares, the flat coefficient intertwiners, and the two commutant dimensions before and after D. The all-matrix arguments above do not depend on those finite safeguards. No existing scientific result, canonical genesis status or bank number is changed by this packet. This proof refines the physical obligation and strengthens known conditional algebraic steps; it does not complete the active goal.
