# The free cusp response and its retained gauge coupling

November 4, 2026. **UNREVIEWED analytical successor**, outside the original eight-control implementation design. No scientific imports, computation or execution. Scope is the actual free centralizer spin block identified in the coupled quaternion stationary bundle, in the supplied complete E8 parent.

## 1. Recover the operator and its unitary doubled form

The [stationary cusp proof](COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md) derives from the full physical mass map

    M_spin=-sigma2 partial_t

on the two retained spin coefficients, with canonical measure dt. Its self-adjoint doubling is

    D_free=[[0,M_spin-dagger],[M_spin,0]]
          =i tau2 tensor sigma2 partial_t.

The constant radial symbol `-tau2 tensor sigma2` is Hermitian, squares to I and has two eigenvalues of each sign. A constant unitary change therefore gives two copies of

    D0=-i sigma1 partial_t, t>=T.                       (1)

This is the same L2 Hilbert space and derivative normalization, with no chosen boundary mass. The number of copies is operator bookkeeping and is not a particle or generation count.

Use one copy and write its boundary data as `psi(T)=(a,b)`. The source chart is `Gamma0=a`, `Gamma1=i b`, with the usual exterior Green orientation. It is the nonsingular chart used in the old [actual cusp norm proof](ACTUAL_CUSP_WEYL_RESPONSE_AND_INDUCED_NORM.md).

## 2. Solve the actual complex spectral equation

For Im(z)>0, the unique decaying solution with given a is

    psi_z(t)=exp[i z(t-T)] (a,a).                      (2)

Indeed sigma1(a,a)=(a,a), and direct differentiation gives `(D0-z)psi_z=0`. The complementary eigenvector grows at infinity. Consequently the exterior response in this chart is

    M_ext(z)=i I, Im(z)>0,
    M_ext(z)=-i I, Im(z)<0.                            (3)

These are the two analytic half-plane responses. Their boundary limits on the real line differ. They cannot be treated as a real, analytic-in-a-gap response at zero.

At `z=i epsilon`, epsilon>0, direct integration gives

    ||psi_z||^2=|a|^2/epsilon
               =a-dagger Im(M_ext(z)) a/Im(z).          (4)

The divergent exterior norm is therefore explicit. The derivative of the constant half-plane response is zero, but using that derivative as a real spectral-gap norm would be incorrect. The old derivative formula required a real gap and a real self-adjoint response. The applicable complex Green identity uses the divided imaginary part in (4).

At real z the solutions (2) are oscillatory and fail to be L2 unless their amplitude vanishes. At zero they are constant. Thus an actual global L2 zero mode must have zero outgoing/free-channel trace on this end. This is a necessary matching condition, not an arbitrary new boundary projector or a theorem that all other modes vanish.

## 3. What compact-core joining can decide

The full field/action transmission conditions can still be written using the actual core response and (3). The imaginary exterior response records propagation into the continuum. An exterior may be retained as part of a coupled system, or its limiting response may enter a resonance calculation. A finite boundary norm at zero is not produced by eliminating this exterior.

An embedded normalizable core state could survive if its physical trace into every free channel vanishes. That is an operator/kernel question. A statement that no physical state survives would exceed the present calculation. Conversely, the existence of confined 128-sector angular tails alone does not show that their interacting states decouple from the remaining continuum.

The primary spectral comparison is the cusp radial reduction and singular-sequence method in Baer, sections 2–3. The new mass operator, its multiplicities and its coupled flavour assignment are derived from this programme's supplied action. [Baer, The Dirac Operator on Hyperbolic Manifolds of Finite Volume](https://arxiv.org/pdf/math/0010233)

## 4. Gauge interactions are fixed by the same source kinetic term

Take an unbroken gauge generator X with its source parallel internal profile. Its four-dimensional gauge kinetic coefficient is

    1/g4^2=Area(Sigma)/g6^2

in the fixed trace convention. Normalize the external gauge field canonically, and let a spin-field profile f have unit norm in the actual source density. The existing covariant four-dimensional kinetic term then gives the gauge generator acting on f with coefficient g4. Its internal integral is precisely the same norm integral defining `||f||=1`.

For the translated unit-norm profiles in the free centralizer channel, there is no extra suppression from moving their support down the cusp. If a surviving non-Abelian gauge generator acts nontrivially on their coefficient T, `[X,T]` is retained and its coupling stays g4. The unbroken colour adjoint supplies such directions. The Abelian adjoint directions can have different charge behavior and are not interchangeable with these non-Abelian coefficients.

This follows from the full kinetic term, not an invented boundary interaction. It prevents declaring the entire free sector physically irrelevant merely from its remote localization. Detailed continuum normalization, thresholds and phenomenological limits require their own physical comparison.

## 5. The next same-action duty

The combined construction now supplies stationary gluing, complete central phases, the variational domain, an explicit free exterior response and its induced-norm behavior. It also keeps the source gauge interaction with that exterior.

The physical question is consequently precise. Does the generated architecture select different combined peripheral transport, a different geometric completion, or an additional interaction that is derived from the same physical principle and retains the gauge fields? Existing complete-cusp deformations that commute with the surviving gauge generators do not create a commutator mass for their spin partners. Decaying and compact-core changes preserve their escaping sequence.

The commuting-rotation comparison of the [Pin2 proof](PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md) avoids this particular free channel by changing the actual flavour peripheral. It remains a family whose physical selection and complete spectrum need derivation. The main all-word geometric/spin join stays a distinct unresolved map.

No empirical value or physical-input payment is claimed. This analytical successor requires independent scrutiny, and any executable controls must be explicitly amended and sealed before implementation.
