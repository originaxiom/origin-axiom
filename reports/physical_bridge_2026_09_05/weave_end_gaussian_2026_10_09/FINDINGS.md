# The normal end vacuum retains a charged Weyl factor

For the actual horizontal end channels of the supplied curved E8
parent, a free normal Gaussian now has an explicit fermion vacuum
and boundary-state overlap. With the declared balanced reference,
its boundary modes carry the opposite net index and perturbative
anomaly to the interior modes.

The compensation has a physical cost in this boundary realization:
the overlap retains a Weyl determinant and charged opposite-chirality
end modes. Keeping only its phase would conceal that cost. This is
not a mirror-free solution, and the reference has not yet been lifted
to a local boundary law for the full six-dimensional cusp.

## From the actual operator to a quantum state

The normal mass map M=partial_t+C gives
D5=gamma5 partial_t+Dslash4+C, with gamma5=+ on the source.
The radial Hamiltonian is H=gamma5(Dslash4+C). For each actual mass
mu and external chiral singular pair it is a two-by-two Hermitian
matrix with energies +/-sqrt(mu^2+|z|^2).

Quantizing both fermionic oscillators gives four occupation states.
The unique ground state fills the negative-energy eigenvector.
The finite Gaussian transfer operator approaches its rank-one
projector with explicit exponential errors. A separate calculation
constructs the four-state Hamiltonian from the anticommutation
relations, rather than importing the two-by-two answer.

For masses +m and -m, with frames anchored at the respective mass
limits, the exact occupied-state overlap is

    -z/sqrt(m^2+|z|^2).

Its phase is the phase of a chiral determinant. Its magnitude has
one zero proportional to |z|, not the square appropriate to a
nonchiral determinant. The checked complex examples distinguish
this overlap from its conjugate, its absolute value and the number1.

The analytic interpretation follows the quantization framework in
[Witten and Yonekura section2.3](https://arxiv.org/html/1909.08775).
The finite algebra is checked here. No infinite-product convergence,
full cusp determinant or globally defined phase follows from it.

## The boundary equation determines the chirality

In the normal model t<=T, choose gamma5 Psi=sigma Psi at the outer
end. The normal solution decays inward exactly when sigma*mu<0.
Its four-dimensional chirality is sigma. This fixes the sign using
the actual source/target map rather than choosing it to cancel
the interior coefficient.

The boundary condition satisfies the complementing-symbol and
Lorentzian flux checks for this five-dimensional normal theory.
That is deliberately not a six-dimensional ellipticity certificate.

The declared reference follows the signs of each coupled positive/
negative mass pair. On each extreme channel it uses the sign at
zero flux. Its reference signs sum to zero in every module, giving

    end index = -signature(C)/2 = -interior index.

The full E8 root calculation and independent tensor/spin-line
calculation agree on the net profiles and all five anomaly
coefficients. They retain all496 horizontal slots, both shifts,
conjugates, the first-flux endpoint and the charge-five exotic.
The independent line reference may have different extra vectorlike
pairs; net agreement does not identify the two boundary conditions.

For positive flux n>=2 the end vector is
(3,6,6,1008,30), and at n=1 it is
(1,5,9/2,1002,24), in the established
(SU3^3,SU3^2 Z,SU2^2 Z,Z^3,gravity^2 Z) convention.
Negative flux reverses it; zero flux has zero net vector.
These are representation coefficients, not observed couplings.

This candidate can supply the opposite response only while its
boundary contribution is retained. It does not remove the anomaly
of the original complete-domain theory by relabeling its end
signature. The old R25 reference-wall lesson is preserved and is
now realized at Gaussian level in these different actual channels.

## What remains before this is a physical completion

If a normalized end mode is admitted in a finite-area completed system,
it still couples to that system's constant gauge field. The kinetic
measure cancels the apparent area suppression. The auxiliary infinite
inward half-line does NOT itself supply a finite-area gauge zero mode;
its volume and the original cusp's area must not be identified. A finite
collar has an explicitly retained exponential tail error. No exact
global finite-core spectrum or finite-area embedding is inferred.

Most importantly, the horizontal projection is an angular Fourier
projection, not pointwise local. Its commutator with multiplication
by exp(i theta) is nonzero. A reference specified on those channels
is therefore not automatically a local boundary condition on the
full parent, including the other angular modes and physical bundles.

The next admission question is the full boundary-symbol and bundle
lift, or a genuinely different relative-phase construction with a
specified reference gauge action. A pure relative phase is not
excluded by this particular physical-boundary calculation; its
locality and behavior through determinant zeros still need proof.
The original complete-domain theory and this supplied boundary
realization must not be silently equated.

## Verification and the first failure

The native route passed19/19 predicates on its first attempt.
The first reference attempt passed7/8 and failed its combined
ground-state projection predicate. Execution stopped before focused
tests. The original source, manifest, logs and exit receipts are
preserved.

The failed comparison was syntactic trace(Pg)==1. After a pre-run
reseal, exact trace, idempotency, Hermiticity and spectral residuals
are checked separately, with a deliberately misnormalized projector
as a rejecting control. The saved diagnostic rows show four false unsimplified comparisons
while every exact trace, projector and spectral residual vanishes
in all six cases. No tolerance, expected overlap, charged count or proof was
changed to obtain agreement.

At reseal4605e1515,19 native and8 separate reference predicates,
10 focused tests and324 twenty-packet regression tests pass.
Final counts and tested commits are recorded in RECEIPTS.json.
Seven scientific files and25 pinned-and-working dependencies are
checked against the rerun seal. Same-author calculations and analytic
arguments are not outside acceptance. The full repository suite is
not claimed; inherited governance failures remain disclosed.

The three statuses remain separate: the finite-mode normal Gaussian
is constructed; a full-cusp local boundary is not; the
parameter-free SM/TOE is unachieved. The nonzero-flux saddles, zero-flux
nonnegative gauge minima, source/silver routes and generated
architecture are preserved. Stable families, genesis selection,
normalized interactions, observer/qualia and gravity remain duties.
