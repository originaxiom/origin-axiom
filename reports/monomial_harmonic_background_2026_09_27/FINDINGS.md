# A source-free rank-five classical family, with finite norm but no neutral gap

2026-09-27. Lifecycle: mechanism application. Uses: the two monomial SL5
families, verified marked M2/M6 topology, parent admission, R17 cusp
machinery, and the supplied twisted gauge action. Own local branch
`audit/fork-2026-09-20`; no shared bank allocation or push.

## Constructive result and evidence grade

For each of the two studied monomial families, the fixed complete
hyperbolic M2 admits a smooth real trace-free diagonal harmonic one-form
beta representing its nontrivial parameter deformation. It has finite
positive L2 norm, is bounded and in L4, and has rapidly decaying cusp
derivatives. With the finite unitary permutation connection A0,

    A_z=A0+i Im(z) beta,   Psi_z=Re(z) beta

solves the chosen action's complete source-free flatness and moment
equations for every finite complex z. Its flat bundle is the literal
E(t), t=exp(z), by an explicit associated-bundle identity. Pullback gives
the corresponding solution on M6. This is a global construction, not
just a cusp solution, a tangent vector or a formal second-order jet.

**Grade:** an AUTHORED analytic argument with explicit geometric/action
assumptions, supported by exact algebraic prerequisites and controls.
The proof has not received independent specialist review, and no numerical
global PDE profile was computed. Tests alone are not a proof of the
infinite-domain analysis. See [PROOF.md](PROOF.md).

## What was verified exactly

The actual trace-free diagonal permutation module has positive Gram
G=I+ones. For BOTH seeds on BOTH M2 and M6, its cohomology tuple is

    (a0,a1,t0,t1,r1)=(0,3,2,4,2).

Thus its interior dimension is one. The actual exponent cocycle is closed,
has exactly zero marked peripheral periods, and is not an ordinary gauge
coboundary: global d0 rank four becomes five when the cocycle is adjoined.
The M6 cocycle was obtained from the inclusion words and cross-checked
against independent logarithmic monomial word exponents. No mode count
was inferred from fibre rank or multiplied by the covering degree.

The analytic construction uses a compactly supported representative
alpha0 and the ZERO-form inverse:

    beta=alpha0-d_A0 Delta0^-1 d_A0^dagger alpha0.

A cusp Hardy estimate plus compact-core compactness and the checked a0=0
prove that inverse exists. On a finite trivializing torus cover the full
Fourier series of its cusp correction has only constant and decaying
Bessel branches. Differentiation removes the constant branch. This proves
the needed L4 and graph-domain statement, rather than assuming L2 implies
it. The finite Gram/Hodge control rejects the wrong sign and sends an
exact class to zero. R17 already contained the Bessel and threshold
mechanisms; their application here is not claimed as a new general theorem.

Because all components of beta commute, the full nonlinear commutators
vanish, while its closed/coclosed conditions remove the derivative terms.
The curve is linear and differentiable in the SAME fixed nonlinear space
Dom(Q0) intersect L4; no unbounded gauge exponential is used to assert
membership. Its residual-square potential is identically zero classically.

## Physical content earned within the supplied model

The variation delta z beta is a normalizable zero mode with a finite
positive kinetic coefficient

    K=(c5/g7^2) integral tr_5(beta wedge *beta).

Here c5 fixes the parent trace convention. Both the complete branching
calculation and an independent sum over ALL 240 E8 roots give c5=60
for RAW adjoint-E8 trace. This is not a derived measured gauge coupling;
g7, metric scale and trace convention remain inputs, and K is not evaluated
numerically. M6 pullback multiplies the integral by three, not the number
of physical generations.

The deformation is not removed by gauge transformations in the full E8
parent. A separately sealed [projection argument](FULL_PARENT_ADDENDUM.md)
shows the orthogonal projection onto the diagonal module commutes with
d_Cz on the whole adjoint. A parent gauge primitive would therefore give
the forbidden diagonal primitive. Exact structure-Weyl controls preserve
the entire root set; 200 non-normalizing reflections fail the projection
test, so no arbitrary-E8-holonomy invariance was assumed.

The field is neutral under the declared gauge SU5. Do not assume that this
is the entire unbroken group at every special parameter: the actual gauge
centralizer and possible enhancement remain part of the next spectrum
audit. Finite gauge identifications are not classified here.

## The simultaneous limitation: zero lies in the neutral essential spectrum

The peripheral diagonal fixed space has dimension two. Its actual
torus-harmonic one-form fluctuations obey the radial operator -d_r^2,
not the scalar operator -d_r^2+1. Their brackets with the background beta
vanish. An escaping, normalized compactly supported profile of length L
gives exact bounds

    Rayleigh quotient = 12/L^2,
    squared Laplacian residual = 504/L^4.

Disjoint supports tending into the cusp form a zero-energy Weyl sequence.
Thus there is NO positive neutral one-form spectral gap in this same
hyperbolic model. The finite-norm zero mode remains, but a separated
finite-dimensional four-dimensional low-energy theory does not follow.
This is an application of the existing scalar/form threshold distinction,
not a new universal impossibility theorem or a quantum instability claim.

The result keeps both sides: exact finite-norm stationary backgrounds
exist in this chosen parent, and their neutral sector is not spectrally
isolated. Neither fact can be substituted for the other.

## Mission effect and next test

**Later same-day update:** the
[charged L2 bridge](../charged_l2_bridge_2026_09_27/FINDINGS.md) now supplies
the authored comparison requested below, including invariant cusp channels,
actual H0/H3 and the local action's fermion grading. All 127 combined tests
pass. This upgrades the specified classes to conditional normalizable linear
zero modes, not an independently accepted analytic theorem or an isolated
four-dimensional theory. Full-parent gauge enhancement remains uncomputed.
The paragraphs below preserve the original harmonic-result checkpoint.

This pays a constructive dynamics/admissibility obligation in the correct
rank-five structure slot. It does not derive the parent, spacetime or
physical metric from Origin Axiom. The construction works more generally
for suitable finite unitary diagonal systems with interior cohomology;
object-specificity lies in the verified coefficient/class, not a newly
exclusive physical law.

The complete common-hypercharge ordinary-index obstruction is unchanged.
It must not yet be called a physical-spectrum theorem. The next useful
join is between those computed interior classes and the actual complete
charged zero-mode operators on THIS background, including gauge enhancement
and the role of the gapless cusp. The earlier acyclic-cusp compact-resolvent
comparison cannot be imported: its hypothesis fails here.

See [NEXT_PHYSICAL_SPECTRUM.md](NEXT_PHYSICAL_SPECTRUM.md). Chirality, full
interactions, quantum/anomaly consistency, gravity and empirical tests remain.
There is no selected z, physical three-generation claim or TOE completion.

## Receipts and cross-seat status

Original science seal `8a91cbbd03eb240fc555cffdb28d1c6916ff24e1`:
native exit 0; seven focused tests pass in 1.19 seconds; 109-test combined
run passes in 23.38 seconds. First receipts committed at `05e33e61`.
Full-parent addendum sealed at `fe0c2d712fc87cd575b4e43c012feda0ab31c7c1`:
native exit 0; three tests pass in 0.81 seconds; final combined
**112 tests pass in 23.67 seconds**, terminal exit 0. Optional tkinter
GUI warning only. All 16 scientific/dependency hashes remain unchanged.
No scientific failures or repairs. This is not a full repository suite
or independent/shared-banking certificate.

The refreshed physics branch advanced through R51's report at a4a29464,
R52's seal e7006dab and diagnostic seal 58860e3b. R51's report and R52's
complete design/proof were personally read; their new producers were not
independently rerun. R51 reports nonlinear finite-energy existence on its
DIFFERENT rank-four canonical base, with the strong-domain join unpaid.
R52's subsequent diagnostic design explicitly preserves a real commuting
fixture defect: first native 33/35, dedicated 11 pass/2 fail, regression
121 pass/4 fail including two older failures. Its replacement diagnostic
is a seal, not a completed result at that checkpoint. Those failures do
not refute the authored Sylvester identity, and are not retroactively green.
No R52 success or canonical-to-hyperbolic transfer is claimed here.
