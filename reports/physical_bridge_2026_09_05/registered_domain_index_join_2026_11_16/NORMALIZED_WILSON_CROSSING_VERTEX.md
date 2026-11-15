# A same-action coupling and current at the retained Wilson crossing

2026-11-16. Author hand derivation under P-C3. Not independently checked. No scientific producer, symbolic engine or numerical integration ran. This reuses the existing order-ten light cubic and derives its normalized coupling relative to its actual gauge current. It is conditional on the source parent, mode/domain theorem and specified Wilson/spin state. It makes no literature-priority claim.

## 1. Derive the vertex before assigning a coupling tensor

The supplied curve parent has connection fluctuation a and spin fluctuations u,v. In its displayed normalization,

    W=(1/2) integral kappa(q Dbar_A r-r Dbar_A q),
    Dbar_A=partial_x+i partial_y-i[A, .].

Expanding A=A0+a, q=q0+u and r=r0+v gives the cubic

    W3=-i integral kappa(u,[a,v])
      = i integral kappa(a,[u,v]).                         (1)

The equality uses invariance of kappa. No integration by parts is needed to obtain (1). The source's boundary primitive is quadratic in q,r and carries no a, so it adds no cubic with these three fluctuation slots. The overall action coefficient is retained below.

For three chiral fluctuations X_i=(a_i,u_i,v_i), polarization yields the symmetric cubic tensor

    T(X1,X2,X3)=i integral sum_cyclic
        kappa(a1,[u2,v3]+[u3,v2]).                        (2)

Equation (2) is the actual bulk vertex to insert on physical mode representatives. The previous quaternion tensor Y(S,M) requires a field/vertex map to this expression or to another explicitly derived term.

## 2. Reuse an already constructed nonzero physical channel

ORDER_TEN_PHYSICAL_CUBIC_AND_EXCEPTIONAL_MODE_PAIRING.md already supplies the following allowed state and modes. Let chi have exact order ten and choose the extending spin eta=chi^5. In the faithful gauge SU5 take

    H=diag(-2,-2,-2,3,3),
    E_+=E_(alpha i), E_-=E_(i alpha),
    [H,E_+]=q E_+, [H,E_-]=-q E_-, q=5,

where i is a colour index and alpha a weak index. Set

    h_H=kappa(H,H)>0, k_E=kappa(E_+,E_-)>0.

The spin lines S L_+ and S L_- have trivial compact extensions and each has a nonzero holomorphic L2 section s_+,s_-. Normalize their frame product by s_+s_-=omega, where omega is a nonzero holomorphic one-form on the compact elliptic curve. The actual modes are

    a0=bar(omega) H, u0=s_+ E_+, v0=s_- E_-.              (3)

The existing proof identifies them with actual harmonic representatives and checks their nonlinear variation class and convergent cubic. It retains all companion modes and gives the gauge representation (3,2) of hypercharge magnitude 5/6 for the charged fields. These are additional vector-like fields in this state. They are not the observed Higgs doublet.

The scalar coefficient of a0 is the neutral Wilson deformation. Its harmonic one-form has nonzero periods, so its continuous fluctuation is a genuine connection modulus in this supplied model.

## 3. Compute all three norms and the gauge normalization together

Write g=Omega^2 |dz|^2 and omega=f(z)dz. Define the coordinate-invariant integrals

    A_omega=integral |f|^2 dxdy=(i/2) integral omega wedge bar(omega),
    A_g=integral Omega^2 dxdy,
    I_omega=integral Omega |f| dxdy.                       (4)

They are positive. A_omega is finite on the compact elliptic curve and A_g is finite by the source geometry. Cauchy-Schwarz then proves I_omega finite. On the stated cusp the source's stronger pointwise mode estimates also give domain and nonlinear-product admission.

Let G=g6^2 be the common positive overall action normalization. The source chiral kinetic densities are (1/2,Omega,Omega) on (a,u,v). Their metrics include this common factor 1/G. The trivial unitary flat parts of S L_+ and S L_- imply constants c_+,c_->0 with

    |s_+|^2=c_+ |f|, |s_-|^2=c_- |f|, c_+c_-=1.          (5)

The coefficients here are in the source's holomorphic spin frames. The spin Hermitian metric is already included by the factor Omega in the kinetic density. Equation (5) uses the compatibility eta=chi^5. It is not a relation for arbitrary twisted sections.

The mode kinetic coefficients are therefore

    Z_a=h_H A_omega/(2G),
    Z_u=k_E c_+ I_omega/G,
    Z_v=k_E c_- I_omega/G.                              (6)

In the same source vector convention, the gauge kinetic term for the internally constant H component is -Z_H F_H^2/4, with

    Z_H=h_H A_g/G.                                      (7)

This uses the parent's vector metric Omega^2 kappa and its standard four-dimensional N=1 component normalization. It is a convention to carry consistently when checking the formula, rather than a newly adjustable relative coefficient. The actual mass-map source also fixes the chiral a coefficient to one half.

Expanding the covariant kinetic derivative on u0 gives the raw current insertion q Z_u. Rescaling u and the gauge field by their positive coefficients yields the actual charge-current coupling

    e_H=|q|/sqrt(Z_H).                                  (8)

It is independent of the frame constants c_+,c_-. The opposite field has the opposite charge. H is an unbroken normalizable gauge generator in this state, so the constant gauge mode is retained.

The standard vector component normalization used in (7)-(8) was checked against Martin's equations 3.3.3 and 3.4.2-3.4.9. Their use remains conditional on this supplied supersymmetric parent. [A Supersymmetry Primer](https://arxiv.org/html/hep-ph/9709356v7)

## 4. The normalized cubic has a geometric relation to that current

Substituting (3) into (1), using s_+s_-=omega and the root bracket, gives the magnitude of the raw coefficient

    |Y_raw|=|q| k_E A_omega/G.                           (9)

For the three distinct chiral coefficients, canonical normalization gives

    |y|=|Y_raw|/sqrt(Z_a Z_u Z_v)
       = |q| sqrt(2G A_omega)/(sqrt(h_H) I_omega).

Combining this with (8) yields

    |y|^2/e_H^2 = 2 A_omega A_g/I_omega^2.              (10)

The common gauge/action normalization G, the trace normalization, the root pairing k_E and both mode-frame constants cancel. Rescaling omega or the overall internal metric also leaves the right side unchanged. A coordinate change transforms Omega and f together and leaves all three integrals invariant. A physical coupling and measuring current have been normalized from the same action.

If a different overall component convention is used, (6)-(9) must be converted together before comparing (10). Rescaling the a mode while leaving its vertex fixed would change the result and fails the source normalization duty.

Define the positive shape factor

    zeta=I_omega/sqrt(A_omega A_g).

Cauchy-Schwarz gives 0<zeta<=1, hence

    |y|/e_H=sqrt(2)/zeta >= sqrt(2).                     (11)

Equality requires Omega proportional to |f| almost everywhere. The complete hyperbolic cusp metric and the smooth nowhere-zero elliptic one-form do not satisfy that equality, so the inequality is strict in the source cusp geometry. The flat constant-conformal-factor calculation supplies an equality control for the normalization algebra. It is not asserted to retain the original curved background or its entire spectrum.

This is a tree-level relation for the specified physical channel over its allowed geometric family. Quantum corrections, mixing with other channels and effective-theory matching have their own duties. It is not a comparison with an observed Standard Model coupling.

## 5. Relation to the physical operator and the family problem

The same coefficient is the projected first derivative of the spin-fermion mass operator under the Wilson deformation a0. The actual mass-map proof gives its fourth row as -p1/Omega, with p1=Dbar_A u+i[q,a]. On the u0 input alone, varying the background connection gives

    delta(-p1/Omega)=i[a0,u0]/Omega.

The trace-dual bilinear against the opposite-charge left field v0 carries the target metric density Omega. It is therefore

    integral Omega kappa(v0,i[a0,u0]/Omega)
       =i q k_E A_omega.

Including the same 1/G action factor recovers (9) directly from the physical operator. In this j=0 block the background commutators with u0 and v0 vanish. The other derivative rows contain no additional contribution to this projected entry.

At an isolated charged zero eigenspace with an admitted inverse on its actual complement, the first-order reduced mass is this projection. Complementary reconstruction and its induced norm must be retained at higher orders, as in FULL_MODE_ELIMINATION_AND_INDUCED_KINETIC_METRIC.md. A vertical gap alone cannot provide that inverse.

The charged u and v partners and their conjugate root blocks remain in the full spectrum. The flavour-antisymmetric partner channel follows from (1) with its own sign. A calculation of the entire matrix must retain it. This one nonzero normalized channel provides a control for the field/vertex/current map before applying a three-dimensional quaternion tensor.

The scalar modulus, Wilson/spin compatibility and parent action remain supplied. The shape factor is an output of that metric, rather than a freely assigned flavour weight. Equation (11) is independent of its selected numerical value. No foundational input or physical three-family multiplicity is counted as derived here.

## Verification duties

Independent review should check the source's harmonic/domain premises, all form and spin factors, the one-half a metric, vector normalization (7), root and trace conventions, and the absence of an extra identical-field factor in this three-distinct-field monomial. It should compare (9) with the first variation of the physical mass map. Rejecting controls should retain the flat equality case, a nonconstant positive metric, phase/rescaling changes of both spin modes with their inverse product, and simultaneous trace/coupling rescaling.

The earlier nonzero cubic and neutral higher-order mass maps are reused positives. This note derives the normalized current relation and geometric inequality under the exact hypotheses above. Their independent verification is pending.
