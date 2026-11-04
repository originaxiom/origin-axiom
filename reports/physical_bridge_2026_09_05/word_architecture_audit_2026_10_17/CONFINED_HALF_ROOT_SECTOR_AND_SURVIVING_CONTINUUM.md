# A discrete half-root sector survives the centralizer continuum

November 4, 2026. **UNREVIEWED analytical positive and scope refinement.** No scientific imports, collection, CAS, quadrature or tests. This is new proof scope beyond the earlier eight unrun checks.

The quantifier is the full 128 half-root coefficient sector of the balanced coupled quaternion stationary bundle on the supplied complete once-punctured hyperbolic elliptic curve, and its transported marking orbit. A separate cover qualifies only after its actual peripheral action and domain have been checked. This is a linear physical-operator result within the supplied interacting parent, with no computed zero-mode or generation count.

## 1. Reuse the actual stationary background and its grading

The [full compensator lift](FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md) retains all 248 coefficients. Its involution Zeta acts by +1 on the 120 integer directions and -1 on the 128 half-root directions. The [stationary bundle](COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md) has total gauge peripheral Zeta. The spin and flavour peripheral signs cancel each other, so every Weyl slot has that same coefficient transition.

All background gauge fields and both Higgs fields lie in the +1 algebra. The transition matrices preserve Zeta, including the two independent full Spin10 lift signs and the electromagnetic Pin2 correction. Consequently the complete linear physical mass map and its adjoint preserve this grading globally. The orthogonal 120 and 128 Hilbert subspaces are reducing subspaces of the doubled self-adjoint operator. This follows from the actual background and its bundle transitions, rather than treating a pointwise root list as a global decomposition.

The older proof already derives a free spin channel and an escaping sequence in the surviving gauge centralizer. That fact remains. It does not determine the spectrum of the orthogonal 128 subspace. Its nonzero-angular confinement was already identified there. Here the full four-slot estimate upgrades that observation to compact resolvent for this subspace.

## 2. Reconstruct the principal block from the source kinetic metric

Use curvature units ell=1 and the actual cusp coordinate x mod 1, y=exp(t), Omega=exp(-t). The source measures under dx dt are

    lambda: exp(-t), a: exp(t)/2, u,v: 1.

Thus the unitary change to common measure dx dt is

    lambda=exp(t/2) L,
    a=sqrt(2) exp(-t/2) A,
    u=U, v=V.                                           (1)

Use the same unitary density change in the trace-dual target. In a gauge with the flat part encoded by its antiperiodic transition, every coefficient has Fourier frequency k=2 pi(n+1/2), so |k|>=pi. As a principal reference set the background gauge and Higgs zero in the actual local mass expression, retaining the metric derivative terms. This reference need not be stationary. [Source physical mass map](../weave_physical_mass_2026_10_08/PROOF.md)

Its four rows become exactly

    M0(L,A,U,V)=(
        i(partial_t-k exp(t)-1/2) A,
       -i(partial_t-k exp(t)+1/2) L,
        i(partial_t+k exp(t)) V,
       -i(partial_t+k exp(t)) U ).                       (2)

For example the first source row is -Dz a/(sqrt(2) Omega^2). Substituting (1), differentiating its exp(-t/2) factor and rescaling the target gives the first row of (2). The second row is sqrt(2) Dz lambda and differentiates exp(t/2). The last two rows are Dbar v/Omega and -Dbar u/Omega. These checks retain both metric half-shifts and all physical slots.

The flat gauge peripheral is combined with the remaining spin-induced connection to produce the stated common antiperiodic transition. On the tail its residual orthonormal connection is bounded. The balanced orthonormal Higgs fields are constant, so the Higgs and gaugino commutator couplings are bounded matrices in (1). The old Wilson has trivial peripheral and its flat tail connection can be gauged away. Hence the actual doubled operator on this tail has the form

    D=D0+V, D0=[[0,M0 dagger],[M0,0]],
    ||V||<=C_V.                                         (3)

No unbounded angular term was hidden in V. Its exp(t) part is explicitly present in (2). The old local flat gauge transitions and geometric/spin connections still have to be retained when fixing the common peripheral frame.

## 3. A uniform full-slot tail estimate

For a compactly supported scalar f and real h(t), integration by parts gives

    ||(partial_t+h)f||^2
      =||f'||^2+integral (h^2-h') |f|^2,
    ||(-partial_t+h)f||^2
      =||f'||^2+integral (h^2+h') |f|^2.                 (4)

In (2), h is -k exp(t)-1/2, -k exp(t)+1/2 or k exp(t). For M0 and M0 dagger the possible potentials are

    k^2 exp(2t)+1/4,
    k^2 exp(2t)+1/4 plus or minus 2k exp(t),
    k^2 exp(2t) plus or minus k exp(t).

Every one is bounded below by k^2 exp(2t)-2|k| exp(t). Writing r=|k| exp(t), the elementary inequality r^2-2r >= r^2/2-2 and |k|>=pi give, after summing modes and slots,

    ||D0 psi||^2
      >= ||partial_t psi||^2
         + integral (pi^2 exp(2t)/2-2) |psi|^2.

From ||(D0+V)psi||^2 >= ||D0 psi||^2/2-||V psi||^2 follows

    ||D psi||^2
      >= integral (pi^2 exp(2t)/4-1-C_V^2) |psi|^2       (5)

for compact-support tail sections. Curvature radius ell restores fixed positive derivative and potential factors. It does not change divergence of the lower bound. There is no assumption about a favourable lowest nonzero Fourier mode or a truncated angular roster.

## 4. Compact resolvent, with its precise scope

The source complete graph realization of the doubled Dirac-type operator is self-adjoint. Restriction to the reducing 128 subspace preserves it. Estimate (5) gives uniformly small tail mass for every graph-norm bounded family. To apply it to general sections, use a cutoff which is zero below t=R and one above t=R+1. Its commutator with D is bounded uniformly in R. Thus the graph unit ball has L2 mass above R+1 bounded by a constant times exp(-2R).

On every compact interior set, ellipticity controls H1 locally and the Rellich compact inclusion makes that graph ball precompact in L2. The uniform tail estimate then makes the global graph inclusion compact. The restricted resolvent is compact. Its spectrum is discrete with finite multiplicities, its kernel is finite, and its nonzero eigenvalues can accumulate only at infinity. Equivalently the physical M on this sector has finite kernel/cokernel and closed range. Its index and charged kernels have not been computed here.

This uses the complete cusp and its derived graph domain. It adds no cap, arbitrary boundary projector or boundary mass. The source cutoffs and singular-sequence method are also the relevant comparison in Bär's sections 2 and 3. The estimate (2)--(5) is for the repository's full physical operator. [Primary spectral paper](https://arxiv.org/pdf/math/0010233)

The [geometric/spin operator intertwiner](GEOMETRIC_SPIN_JOIN_AND_FULL_CURVE_OPERATOR.md) transports this result over the whole stated marking orbit. Compact resolvent is a statement for each fixed admitted carrier. No uniform nonzero eigenvalue gap through degeneration of the modulus is asserted. A finite cover can alter the premise. If a cusp has peripheral covering degree m, the pulled-back coefficient involution is Zeta^m. For even m the half-root antiperiodicity becomes periodic, so (5) cannot be copied to that end. For odd m it remains antiperiodic. The pulled-back spin line and any proposed extending replacement must also be distinguished.

## 5. Keep the interactions and the centralizer conclusion

The complete doubled operator still has the gauge-centralizer essential spectrum from the earlier proof. Thus it has a reducing discrete 128 block alongside a continuum in the 120 block. Both statements can hold in the same stationary construction.

The E8 bracket respects the grading, with [128,128] in 120 and [120,128] in 128. Gauge and Higgs interactions of the original action therefore remain across these blocks. Linear compact resolvent does not prove quantum stability or decoupling of an interacting bound state from the continuum. The existing source-normalized non-Abelian gauge coupling to centralizer spin profiles also remains.

The constructive next question is the actual finite charged kernels and their interactions in the 128 block, while deriving a justified physical account of the surviving continuum. This proof supplies a well-posed discrete sector to examine. It supplies no three-generation answer, no selection of this parent and no empirical claim that the complete model is viable.
