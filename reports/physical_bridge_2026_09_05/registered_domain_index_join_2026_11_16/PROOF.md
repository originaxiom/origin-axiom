# The residual registering action on actual sections

2026-11-16. Author hand derivation under P-C3, committed scope 4b15876b3. Not independently checked. No scientific code, symbolic engine, producer or test ran. Source hashes are in SOURCE_RECEIPT.json. This note reuses the existing root, flat coefficient, principal-parts and coupling results, and adds an explicit comparison lift and a test for the physical join.

## 1. Three end constructions have different operator data

The recovered sources define the following objects.

| Construction | Base and retained fields | Datum | Established conditional consequence |
|---|---|---|---|
| Relative gauge register | Actual core and complete tail, connection and boundary/transition frame | Relative integer n | The same-action mean response is Gamma_n = 2 pi^2 c_H n^2/(G Area). A reference winding can also occur with zero bulk curvature under different end data |
| Fixed-fibre puncture | E_tau minus p, rank-six quaternion coefficient and ordinary vertical spin | A critical trace subspace Lambda of dimension d | In the finite-distance domain theorem, ind D_Lambda^+ = d-3. The two extreme domains have opposite three-dimensional chiral kernels |
| Modular-cusp extension | A vector bundle over the modular parameter base, with its specified multiplier | Integer modifications of the cusp eigenline extensions | B1641 and B1700 give the recorded modular index and section spaces. Uniform data yield the three-per-unit result |
| Complete curved physical parent | Four Weyl slots, spin-valued Higgs fields, connection and complete graph domain | Physical gauge/spin/end background | The source exhibits M=Uout T Uin and its conditional charged index. Its actual end hypotheses determine that index |

The fixed-fibre finite-distance theorem is an actual Fredholm realization under its analytic assumptions. Its positive result remains intact. The hyperbolic complete cusp has a divergent critical ordinary-spin norm in the corresponding comparison, so a bounded conformal identification cannot transfer that finite-distance realization to the complete cusp. The twisted physical form parent has its own positive constructions.

The modular base and the elliptic fibre are already distinguished in HODGE_GEOMETRY_REDUCTION_AND_FIBRE_MAP.md. A physical field/domain map must identify which of these operator problems it realizes. Equal integer labels alone do not supply such a map.

## 2. Residual inner action after retaining the argument

Start with a flat coefficient system on a cover, with deck action D_h and unitary coefficient representation R_h. Sections satisfy

    Psi(D_h x)=R_h Psi(x).

Let the registered extension E contain J_h with geometric action P_(J_h)=D_h. A constant coefficient lift B_e obeys

    B_e R_k B_e^-1 = R_(phi_e(k)).

The actual section operator is

    (U_e Psi)(x)=B_e Psi(P_e^-1 x).

Substitution, with its argument retained, gives

    U_(J_h) Psi = C_h Psi,
    C_h = B_(J_h) R_h^-1.                            (1)

Compatibility with the inner automorphism implies

    B_(J_h) R_k B_(J_h)^-1 = R_h R_k R_h^-1.

Thus R_h^-1 B_(J_h) commutes with every R_k, including R_h. It consequently equals C_h. Since J_h J_k=J_(hk),

    C_(hk)=C_h C_k,
    C_h in Comm(R).                                  (2)

Equations (1)-(2) specify the exact remaining representation of the inner subgroup. For the natural deck lift B_(J_h)=R_h, it is the identity. A nontrivial registering action requires the actual residual C_h and its action on the physical fields.

For R=I_m tensor rho with rho irreducible, Schur's lemma gives Comm(R)=End(C^m) tensor I. With the product Hermitian metric, unitary residuals lie in U(m). If they preserve the differential operator and domain, they act on its kernel and its boundary response. Those preservation requirements are additional equations that the physical construction must establish.

This reformulates the withdrawn harmonic draft's argument-factor failure as a reusable test. It does not choose the residual and gives no universal restriction on other registering architectures.

## 3. Apply the test to the existing global root profiles

Reuse the common flat frame W=C^3 tensor rho, the actual root geometry and the global doublet F=N/w. The existing source proves

    F(P_e x)=k_e g_e F(x),
    R_h=I3 tensor rho(h).

The three profiles Psi_p=e_p tensor F span the source's H0(E6). Its registered lift is

    B_e^axis=O_(g_e) tensor g_e,

where O_g is conjugation on the three imaginary quaternion axes. Applying the full section operator gives

    U_e^axis Psi_p = k_e^-1 sum_q (O_g)_(q p) Psi_q.
                                                               (3)

This equation reuses the global profile transport already derived in REGISTERED_PRINCIPAL_PARTS_AND_GREEN_TRANSPORT.md. It includes both values and arguments. For inner elements k_(J_h)=1, so

    C_h^axis=O_(rho(h)) tensor I2.                   (4)

In the ordered axes (i,j,k), conjugation by i has signs (1,-1,-1), and conjugation by j has signs (-1,1,-1). This is a permutation of the source's order (j,i,k). The commutator c has rho(c)=-I2, so O_(rho(c))=I3. Therefore J_c acts as identity on these profiles.

The central sheet epsilon has P_epsilon=id and g_epsilon=-I2. The source's nonzero F then forces k_epsilon=-1, and (3) gives minus identity. Since Delta^4=epsilon J_c, the fourth power also acts as minus identity. The profile parity and the retained central sign are compatible.

## 4. A comparison lift has the same central sheet and quadratic operator

Every g in 2O acts on the axes by a signed permutation O_g. Let Pi_g be its underlying unsigned permutation. Since each row and column has one nonzero entry, Pi_(gh)=Pi_g Pi_h. Define a second lift

    B_e^perm=Pi_(g_e) tensor g_e.                  (5)

It is a representation of the same E and satisfies the same deck-intertwining relation, because both multiplicity actions commute with I3 tensor rho. Its global profile action is

    U_e^perm Psi_p = k_e^-1 sum_q (Pi_g)_(q p) Psi_q.
                                                               (6)

For h in Q8 the axis action is diagonal, hence Pi_(rho(h))=I3 and C_h^perm=I. At epsilon both lifts have coefficient -I6 and the same geometric action. Both have U_(Delta^4)=-I3 on these profiles.

They are inequivalent as actions on this same profile space. At J_a one has eigenvalues (1,-1,-1) and the other (1,1,1). A change of profile basis cannot identify their spectra. A common scalar line also cannot turn a nonscalar operator into the identity. The inner elements fix tau, so a tau-dependent change of basis cannot remove this test.

Equations (3) and (6) describe the unspun H0(E6) profiles. The prior vertical-spin construction multiplies both by its declared j_e, giving j_e/k_e times the corresponding multiplicity matrix. Its j_epsilon=-1 cancels the unspun minus sign, as the existing Green-transport proof states. On J_a and J_b that common spin factor is one, so the comparison remains inequivalent. The four-slot curved physical theory needs its own slotwise spin and gauge factors. The unspun central sign is not assigned to all its fields.

The ordinary fixed-fibre Dolbeault/Dirac operator with these three identical flat coefficient copies commutes with constant transformations of C^3. Its product coefficient metric does as well. Both lifts therefore give the same differential expression, profile norms and spectrum at a fixed background. Where the scalar-spin geometric transport preserves the family metric and extreme domains, it preserves them for both multiplicity lifts. This is a conditional comparison within that free coefficient model. It asserts no new E8 physical realization of (5).

For a general trace subspace Lambda, covariance must be checked separately. Extreme domains are preserved by every coefficient unitary, and the equal-copy solution-trace subspace C^3 tensor span(b) is preserved by both transported lifts. Their presence alone cannot distinguish (3) from (6).

Thus the central fourth-power test, quadratic expression, norms and equal-copy free index leave two explicit coherent possibilities. The physical interaction and registering law can add the missing constraint.

## 5. The actual interaction can supply an additional test

Let V be the traceless quaternion matrices with its bracket beta(X,Y)=[X,Y]. In its oriented orthonormal basis, beta is a fixed multiple of the vector cross product. For an orthogonal transformation A,

    beta(Ax,Ay)=det(A) A beta(x,y).                 (7)

O_g has determinant one and preserves this bracket. For the quarter-turn g_L, Pi_g exchanges two axes and has determinant minus one. Its bracket acquires the extra sign in (7). If the physical field map identifies the mode multiplicity with this bracket module and keeps the vertex's target line fixed, the two lifts give different vertex covariance.

The same distinction can be expressed as a map to V tensor the determinant line. Permitting that line changes the test. Spin, Higgs and scalar automorphy factors must therefore be retained before deciding which lift the physical interaction admits.

The existing REGISTERED_COUPLING_TRANSPORT.md already derives O_g Y O_g^T from its actual quaternion contraction and the simultaneous transformations of S and M. Its separate scalar condition alpha beta=z^-2 also remains necessary. That prior result supplies a concrete interaction map to test. The missing physical step is to identify the actual normalized zero modes and action vertex with those particular contraction slots. Choosing their names does not establish that identification.

On a general curved physical bundle, two lifts of the same geometric operation that preserve the same connection differ by a covariantly constant bundle automorphism. This follows by composing one connection-intertwining map with the inverse of the other. Preserving the full background and action additionally constrains the Higgs fields, spin slots and interactions. The residual in (1) should therefore be computed from the actual physical transitions and compensators before using this free comparison in that parent.

## 6. Full covariance classifies the constant interaction lifts

The existing coupling also admits an exact classification under explicit hypotheses. Keep its independent inputs S,M in M2(C), its basis (C1,C2,C3)=(j,i,k), epsilon=[[0,1],[-1,0]], and

    Y(S,M)_ab = sum_mn (C_a^T epsilon S C_b)_mn M_mn.       (8)

The preceding source already derives

    Y(g S g^-1,g M g^T)=O_g Y(S,M) O_g^T.                 (9)

Here g is in SL2(C), O_g is its bracket-preserving conjugation action, and O_g^T O_g=I. The following statements classify constant, state-independent matter actions on this entire specified input family. A stabilizer at a single selected S,M can be larger.

First, the linear span of the matrices Y(S,M), with S and M varying, is all M3(C). To prove this, suppose coefficients z_ab satisfy

    sum_ab z_ab Y(S,M)_ab=0 for every S,M.

Nondegeneracy of the entrywise bilinear pairing with M implies

    sum_ab z_ab C_a^T epsilon S C_b=0 for every S.

Vectorizing S gives the superoperator

    sum_ab z_ab (C_b^T tensor C_a^T epsilon)=0.            (10)

The C_b^T are three independent elements of M2(C). The C_a^T epsilon are also independent, since epsilon is invertible. Their nine tensor products are independent. Hence every z_ab is zero. The annihilator of the span is zero, proving the claim. This uses a linear span of allowed couplings and does not require every individual matrix to be the image of one pair S,M.

The span remains all M3(C) when S is restricted to traceless matrices. Use the standard oriented quaternion basis Q1,Q2,Q3 for this proof. Reordering it to (j,i,k) changes no independence statement. Since C_a^T epsilon=-epsilon C_a, a putative annihilator on traceless S would give

    K_z(S)=sum_ab z_ab Q_a S Q_b=0 for every traceless S.

The quaternion identity gives

    K_z(Q_d) = (tr z) Q_d
               -sum_b z_db Q_b -sum_a z_ad Q_a
               +sum_ab z_ab epsilon_abd I2.              (10a)

The three identity coefficients in (10a) force the antisymmetric part of z to vanish. The three vector equations then give 2z=(tr z)I3. Taking their trace gives tr z=0 and hence z=0. Thus traceless S suffices for the span argument. M can also be restricted to rank-one matrices if all such matrices are admitted independently, because their linear span is M2(C). A fixed background curve of linked S and M values needs a separate span check.

Let invertible left- and right-matter matrices A_L(g),A_R(g) preserve the bilinear scalar for every S,M under the input transformations in (9). Covariance requires

    A_L^T O_g Y O_g^T A_R = Y for every Y in M3(C).        (11)

Set L=O_g^T A_L and R=O_g^T A_R. Taking Y=I yields L^T R=I. Substituting R=L^-T into (11) gives

    L^T Y L^-T=Y for every Y.

Only scalar matrices commute with the full matrix algebra. Thus for a nonzero scalar c(g),

    A_L(g)=c(g) O_g,
    A_R(g)=c(g)^-1 O_g.                                  (12)

If these are group representations, c is a character. If the reference matter metric is the product unitary metric and g is in SU2, unitarity further gives |c|=1. With the same lift required on both matter slots, c^2=1. With a geometric scalar line over a family, the corresponding factors can be cocycles and must be tracked in that line.

If S and M also carry scalar factors alpha(g) and beta(g), the same proof gives

    A_L=c_L O_g, A_R=c_R O_g,
    c_L c_R = (alpha beta)^-1.                            (13)

Equation (13) recovers the earlier scalar compatibility condition while classifying the remaining constant matrix freedom. It leaves the split between scalar lines to their actual field geometry.

There is a direct hand rejecting control for the unsigned lift. In the source's order (j,i,k), use its own

    S0=diag(1,0), M0=[[0,-1],[0,0]],
    Y0=[[-1,0,-i],[0,0,0],[i,0,-1]].

For the inner element J_b with rho(b)=j, O_j=diag(1,-1,-1), while Pi_j=I. Equation (9) reverses the two nonzero off-diagonal entries of Y0. Both unsigned matter slots remain unchanged, so they fail (11). The signed slots satisfy it. This is a failure of the proposed unsigned lift for the complete supplied interaction with its specified input and scalar transport. It leaves state-dependent lifts, different interactions and differently carried scalar data at their own scope.

The rejecting control also lies in the traceless-S subfamily. With S=diag(1,-1) and the same rank-one M0, direct multiplication of i=diag(i,-i), j=epsilon and k=i j gives

    Y=[[-1,0,-i],[0,1,0],[i,0,-1]].

The same J_b changes its off-diagonal entries, so the unsigned slots still fail. This supplies a concrete check for the weaker hypothesis in (10a).

Consequently the free lift ambiguity can be reduced by retaining this actual interaction family. The physical duty is to derive (8) from the same action on the actual normalized zero modes and to derive the field transformations of S and M. Those maps remain supplied in the contraction model. No foundational input is counted as paid by (12)-(13).

## 7. The next physical calculation is specified

Extract the actual deck transitions and point-push compensators on all four physical Weyl slots of the curved quaternion candidate. Include the connection's local frame change and the spin factor. Form their residual, determine its restriction to the actual harmonic modes, and retain the vector companion and conjugate sectors.

The primary controls are (1)'s natural cancellation, (4)'s known parity, the common central fourth power, and the vertex test (7) with its target line retained. A complete physical identification also needs the graph-domain intertwiner and its boundary Green form. The exterior response norm must be transported along with its zero-energy trace.

This determines which existing triplet can participate in the physical index map. Selecting an end class then requires a stationary end/source law in that same construction. The current result reduces a representation-comparison problem to an explicit residual and vertex calculation. It removes no foundational input and supplies no three-family physical spectrum by itself.
