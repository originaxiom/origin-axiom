# R4 — a scalar vacuum and the mass spectrum it actually supplies

2026-09-05. Designed after R1–R3 and the audit commit `a507ab93`, before
executing R4. The algebra below suggests the outcomes; this is not a blind
discovery design or an empirical test. No observed values enter.

## Scope and prior art

P0: this tests a **declared four-dimensional, non-supersymmetric compact-E6
gauge theory at the algebra/breaking stage**, using the banked 27 and cubic,
two complex scalar 27s and one real adjoint scalar. It does not quantify over
the whole relational program or force this real form, spacetime, field content,
potential, VEV scales, or Yukawa couplings from A1–A7. Those are paid inputs.

The relevant ladder entries are X8/X9/X10/X19/X20/X24 and the audit's PB-MASS.
This follows the corrected instrument and the explicit mass requirement: it
tests the potential and spectrum underlying a physical continuation, not a
re-probe of an old toral no-go. Other ends, rows, cuts and holonomy mechanisms
are outside this conditional model, not excluded by its outcome.

Preflight: fresh fetched main remains `f06d3405`; `already_banked.py` on
`singlet exotic mixing mass` returned settled hits, which led to the B884,
B885/B889, B962/B964 and B970 bodies and original producers. The atlas context
card was run, with its epoch-blindness caveat. LAW_MAP, OPEN_LEADS, the ladder
and kill graph were searched for mass, VEV, singlet, mixing and their Unicode
forms. B883's build/representation and B884's producer were read directly.

Already banked: the exact cubic; two 5bars with identical SM charges; S mass
coupling; the 27-only SU5 limitation; adjoint symmetry breaking; the distinction
between a vector stabilizer and a line stabilizer. **None is a new discovery.**
The new task is an explicit action/vacuum fluctuation and mixed-mass calculation
that can feed, or correct, the earlier low-energy spectrum.

Primary comparator: Schwichtenberg, Tremper and Ziegler,
[EPJC 78 (2018) 910, section 2](https://doi.org/10.1140/epjc/s10052-018-6388-6),
accessed 2026-09-05. Their 27+351prime+78 theory mixes the two 5bars; it assumes
its scalar vacuum and does not explicitly solve gauge unification. We do not
adopt its fitted parameters, claim to improve its phenomenology, or infer a
potential from its subgroup diagram. The potential below is our explicit
conditional construction, not an assertion about a measured field.

## Conventions, fields and the potential

Use B883's weight-basis ordering and normalize the cubic's first nonzero
coefficient to +1. Independently solve polynomial invariance equations over Q;
certify against all 78 matrices. Verify a positive compact invariant Hermitian
form before treating coordinate norms as kinetic norms. If identity is not
that form, stop and amend the normalization before any mass interpretation.

Use the B970 Bourbaki chain: SU5 on simple roots 3,4,5,6; color on 3,4 and
weak on 6; Q=T3+Y with Y(Q)=1/6. Derive Y by the commuting-Cartan equations.
S denotes the SO10 singlet; N the SU5 singlet inside its 16. Distinct **scalar
fields** with VEVs S and N are not one scalar with VEV S+N.

Let phi_1, phi_2 be complex 27s, A a Hermitian matrix representing the real
adjoint, and C(u,v)_a=d_abc u_b v_c the invariant cubic contraction into 27bar.
With all displayed coefficients strictly positive, choose

```text
V = sum_a lambda_a (phi_a^dagger phi_a - v_a^2)^2
    + kappa |phi_1^dagger phi_2|^2
    + eta sum_(a<=b) ||C(phi_a,phi_b)||^2
    + lambda_A (Tr A^2 - w^2)^2
    + zeta sum_a ||A phi_a||^2.
```

Each term has degree at most four. Include positive scalar kinetic terms,
the Yang–Mills term, and left-handed Weyl 27 fermions with
`-1/2 sum_a Y^a_ij d_ABC psi_i^A psi_j^B phi_a^C + h.c.`; the Lorentz
two-spinor contraction is understood and requires symmetric family Y^a.
No supersymmetry, additional scalar, higher-dimensional operator or finite
threshold correction is implicit. All other allowed operators are set to zero
as a model choice whose quantum stability is NOT presumed.

## Computations and two-sided checks

1. Reconstruct and certify the cubic, rather than read its support count.
   Check Cartan/root weights, compact adjoints and the representation's simple
   generator/Serre relations. A flipped cubic coefficient must fail invariance.
2. Compute the complete SM-invariant subspace of the 27. Compare with the SU5
   invariant subspace; do not identify charge zero alone with a singlet.
3. Contract the cubic with `s S+n N`, for symbolic real s,n and complex controls.
   Extract the triplet and doublet rectangular heavy/light mass blocks and
   their kernels. Singular values, not signed eigenvalues, define masses.
   Zero VEVs must give zero rank; either nonzero pure VEV must be considered,
   including a pure N that changes the light-5bar identification.
4. Test the potential at `phi_1=S, phi_2=N, A=Y`, using `v_1=v_2=1` and
   `w^2=Tr Y^2` as **arbitrary dimensionless representative scales**, not fitted
   physical units. If every square vanishes, this is a global classical
   minimum because V>=0. This does not make it isolated or quantum stable.
5. Compute the compact vector stabilizers for S, S+2N, (S,N), and (S,N,Y).
   Check the final unbroken generators as actual matrices, not dimension alone.
   Expected dimensions from prior theory: 45,45,24,12. The last algebra should
   be su3+su2+u1 on the chosen embedding, not merely an arbitrary 12-dimensional
   algebra. Zero VEVs and removal of the adjoint are positive enlargement controls.
6. Compute the real constraint Jacobian J on all 108+78 scalar coordinates.
   At a zero of every square, the Hessian is a positive weighted `2 J^T J`.
   Determine its exact rank, independently compare numerical rank, exhibit the
   gauge orbit, check `J G=0`, and subtract its rank from the zero-mode count.
   Identify any residual scalar representations by their actual generator
   action. Radial and symmetry-breaking perturbations must raise V; finite
   directional differentiation checks the Jacobian/Hessian construction.
7. State the actual tree-level spectrum and whether it justifies R2's assumed
   effective spectrum. Any extra massless scalars are retained, not discarded
   as convenient thresholds. Do not reuse R2's fitted matching condition for a
   different spectrum. No all-loop or global no-go is authorized.

Prior: the specified potential admits an SM-preserving global minimum, but
non-gauge scalar flat directions likely remain. Singlet-VEV mixing is expected
to give complete SU5-degenerate heavy multiplets, not the required splitting.
Either a counterexample or a confirmed limitation must be reported together
with the positive mass/symmetry-breaking construction. No claim of uniqueness,
physical selection, radiative stability, realistic electroweak breaking or a
completed TOE follows from this cell.

Code and this design are hashed and committed before execution. Outputs use
exclusive creation; any failed run and any normalization repair get separate
artifacts. Register surviving work and any newly proved sublemmas at banking.
