# Full compensator coherence fixes an electromagnetic phase conditionally

November 4, 2026. **UNREVIEWED author hand derivation.** No scientific imports, enumeration, CAS, tests or numerical execution. This is a constructive successor within the supplied balanced E8 parent, following the owner-approved transport/end work order.

## 1. The full scalar-state stabilizer supplies the correct group

The [old quartic discriminator](REGISTER_FLAVOUR_ACTION_GRAM_AND_QUARTIC_STATE_TEST.md) gives, at the balanced state and fixed flavour reference z,

    C_Phi0(z)=const[(|z1|^2+|z2|^2)^2+sx(z)^2],
    sx(z)=2 Re(z1 bar(z2)).

A flavour U can be undone by a compact gauge transformation only if it preserves that entire polynomial. The induced rotation of the Stokes vector must preserve the unoriented x axis. Its inverse image in SU2 is

    Pin2_x = {R_alpha, R_alpha Fi : alpha mod 2pi},
    R_alpha=exp(i alpha sigma_x),
    Fi^2=R_pi=-I2, Fi R_alpha Fi^-1=R_-alpha.            (1)

This follows by comparing the coefficients of the squared linear form on the unit Stokes sphere. It gives a necessary condition using the whole gauge-invariant polynomial. A finite three-probe sample alone would be weaker.

For each rotation, the actual gauge element

    K_alpha=exp[-i alpha(H_+-H_-)/2]                     (2)

satisfies `R_alpha Ad_(K_alpha) Phi0=Phi0`. The old D5 vector reflection A also compensates Fi. Thus every element of (1) is individually compensable, and the necessary stabilizer condition is sufficient. The old binary dihedral group 2D4 is its intersection with the register image 2O. The full continuous stabilizer is kept here rather than being replaced by that finite intersection.

## 2. Individual compensators and a coherent group map differ

Use the [full-lift notation](FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md),

    A^2=C^-1 P, A^4=Zeta=C^2,
    K_pi=Zeta P, A K_alpha A^-1=K_-alpha.

Therefore

    A^2=C K_pi.                                        (3)

The extra C is invisible on the D5 background but visible on the vector and spinor products. Equations (1)–(3) show why the bare D5 compensators supply a central extension of the finite flavour group. Coherent compensation factoring through Pin2 requires correcting this C while retaining all other physical sectors.

## 3. An explicit correction inside the already chosen electromagnetic circle

The actual source electromagnetic Cartan in the complementary A3 is

    Q_em=(2/3)(e1+e2+e3).

Its four weights are `1` and `-1/3,-1/3,-1/3`. This is the existing colour/electromagnetic identification of the balanced branch, retained as a premise. Set

    h=exp(3 pi i Q_em/4).                               (4)

It lies in the centre of the source's unbroken U3. On the four it has eigenvalues `exp(3 pi i/4)` and three copies of `exp(-pi i/4)`, whose product is one. Its square is `-i I4`.

There is an exact E8-lattice verification of the required identity, without treating the two subgroup centres as independent. The torus logarithm of h^2 is

    (1/2,1/2,1/2,0,0,0,0,0),

whereas C^-1 has logarithm

    (0,0,0,-1/2,-1/2,-1/2,-1/2,-1/2).

Their difference is `(1/2,...,1/2)`, an E8 coroot. Hence in the actual compact E8 group

    h^2=C^-1, h^4=Zeta.                                (5)

The old order-three Wilson transport and the old U3 gauge algebra commute with h. The correction therefore retains that connected unbroken gauge algebra. Its nontrivial action on other A3 fields and mixed sectors must travel with it.

## 4. The coherent compensator homomorphism

Define `A_tilde=A h`. Since h lies in the D5 centralizer, it commutes with A and K_alpha. Equations (3) and (5) give

    A_tilde^2=K_pi, A_tilde^4=1,
    A_tilde K_alpha A_tilde^-1=K_-alpha.                (6)

The period of K_alpha is 2pi on the full E8 representation. Indeed `K_(2pi)=exp[-i pi(H_+-H_-)]=Zeta Zeta=1`. It is faithful on the circle because its action on E_+ has phase `exp(-i alpha)`.

Consequently

    G(R_alpha)=K_alpha,
    G(R_alpha Fi)=K_alpha A_tilde                       (7)

defines a group homomorphism `Pin2_x -> E8`. It is injective. A reflected element exchanges the two independent triple directions whereas a rotation preserves each, so no reflected element can lie in its kernel. The joint action `U Ad_(G(U))` fixes Phi0 for every U in Pin2_x.

In particular `Fj=R_(pi/2) Fi` has gauge image `B_tilde=D A_tilde`. These two gauge images satisfy the exact Q8 relations on the full 248 representation. Thus a full quaternion compensation exists in this supplied parent when the complementary gauge factor is retained.

The construction also gives the full binary dihedral stabilizer as an exact compact E8 subgroup. It does not provide a compensator for word moves outside the stationary state's stabilizer. The covariant family of changed states and marked holonomies continues to use the companion's all-word transport law.

## 5. A precise conditional reduction

Start with an unspecified electromagnetic correction `h(theta)=exp(i theta Q_em)` multiplying the same D5 reflection. Requiring the actual Pin2 relation fixes

    h(theta)^2=C^-1.

On the defining A3 four, both equations are

    exp(2i theta)=-i,
    exp(-2i theta/3)=-i.

They give

    theta=3pi/4 modulo 3pi.                             (8)

The faithful electromagnetic circle has period 6pi on all retained E8 coefficients, since charges 1, 2/3 and -1/3 occur. Thus (8) leaves two values in that circle, differing by Zeta. A continuous proposed correction phase has become a twofold discrete lift choice under the stipulated compensation problem. The source trace and charge normalization are retained throughout.

This is a conditional constraint within a supplied physical model. Its hypotheses include the balanced state, its existing electromagnetic circle and the requirement that the physical compensation factor through Pin2. A free-group representation does not itself require that last condition. The finite based register can retain the larger central extension, as the companion proof explains. No foundational input is certified removed by preferring one realization.

## 6. The end follows the commutator, not the core phase alone

The electromagnetic correction commutes with both D5 generators. Therefore

    [A_tilde,B_tilde]=[A,B]=Zeta P.                     (9)

For quaternion flavour holonomy the [stationary cusp construction](COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md) and its free centralizer channels persist. Fixing the full-group relation does not change their combined spin/flavour/gauge peripheral transition.

There is a positive control within the same stabilizer. Let the two physical flavour holonomies be rotations R_alpha and R_beta about the x axis, with gauge holonomies K_alpha and K_beta. They commute in both factors. Their flat peripheral transports are identity. The source bounding spin and original gauge P then give the old alternating spin/weight cusp transitions. In particular the unbroken gauge-centralizer spin fields are antiperiodic and have no zero-angular channel of the kind derived for the quaternion case.

This control admits all rotation angles before any selection. A rank-two order-five abelian character pair can be placed in this circle after a fixed flavour frame change. That is a permitted comparison, not an earned physical identification with the order-five mapping-torus construction. Its whole spectrum and universal-family extension need their own operator analysis.

More generally, in the surviving gauge algebra the asymptotic spin/flavour eigenphases are those of `-Hol_F(c)`, since the gauge holonomy acts trivially on a surviving parallel gauge generator. A zero angular frequency appears exactly when `Hol_F(c)` has eigenvalue -1. For SU2 that is precisely `Hol_F(c)=-I2`.

Thus compatibility and the end law impose different constraints. The continuous Pin2 group is the complete compensable stabilizer of this stationary state. Its quaternion commutator creates the free-channel duty. Its abelian rotation subfamily avoids that particular channel while leaving its own physical identification and selection duties explicit.

## 7. Verification duties

The executable successor must check the full-root lattice equality (5), actual spinor lifts, all group relations and the common action/metric maps. It must retain the old quadratic Gram and quartic controls, the electromagnetic charge normalization and the unbroken gauge algebra. For the end, it must reconstruct the source mass map with both actual angular transition sets before comparing responses or kernels.

The direct Weyl sequence and graph-domain hypotheses require analytical review. No finite matrix pass substitutes for them. This note and its predecessors remain authored conditional proofs pending independent review and appropriate scientific admission.
