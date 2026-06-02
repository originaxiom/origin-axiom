# Frontier — Quarantined Phase B Work

This directory holds **speculative, `open`-status** research — see `../CLAIMS.md`
(O1–O9) and `../GOVERNANCE.md`. Nothing here is a claim; results are logged
observations only.

A result moves from here into the proven core (`../src/`) **only** by passing the
`conditional → proven` gate in `GOVERNANCE.md` §5 — code, a test, scrutiny, and a
logged status change.

**Phase B is in progress.** Probes logged so far:

## Dependency Graph

```text
B13-B16 established the current kernel:
  A1-A6 -> A
  (L X)^2=A -> X=+/-P
  F=L P, F^2=A
  trace lift of F contains the A-sector

B18 trace-lift functoriality
  gates B20, B21, B23, B24

B19 exchange/half-step axiom audit
B17 alternation/persistence selector
B22 spectrum genericity controls

B20 operational awareness test
B21 spacetime / Weil-Petersson dictionary test
B23 BKL / gravity controls
B24 anyon / quantum bridge

B25 Fibonacci spectrum anchor
  depends on B18/B22 and tests the lambda/h=1 spectral bridge

B26 lambda/h=1 derivation attempt
  tests whether projective half-return self-similarity derives lambda/h=1

B27 SL(3) Fibonacci trace lift
  extends the trace-lift calculation to higher-rank character data

B48 SL(3) metallic trace-map certificates
  generalizes B27 from m=1 to phi_m(a)=a^m b, phi_m(b)=a and supports PC12

B49 SL(3) certificate-to-proof hardening
  decomposes PC12's fixed-line splitting certificate into proof modules

B50 PC12 proof-draft assembly
  assembles B48/B49 into an internal theorem-note skeleton

B51 SL(3) symbolic-m factorization
  proves the c=3 fixed-line block factorization with m formal

B52 multichannel Fibonacci bridge control
  shows the naive 3-channel tight-binding bridge gives 6x6 symplectic transfer
  matrices and fails the PC12 third-order trace recursion

B54 general-c exchange structure
  generalizes B51: [J(m,c),P]=0 for symbolic c (whole fixed line); c=1
  Eisenstein/golden twins; m=1 cyclotomic sweep

B55 c=1 fixed-line structure (general m)
  completes B54's c=1 row: symmetric mod-4 (Phi6/Phi4/(t-1)^2), antisymmetric
  (t-1)(t+1)(t^2-mt-1)=char(M) for all m

B56 figure-eight invariant-surface negative control
  diagonal SL(2,C) reps have I in {4,-17/2+-7sqrt5/2}, none=1/4; figure-eight
  I=1/4 bridge DEAD; c=1 Eisenstein resemblance is a cyclotomic coincidence

B57 general-m Diophantine splitting classification
  {c=1,c=3} universal splitting points; m-dependent extras (m=1..6); Hilbert
  class-field coincidence killed for m>=2

B58 SL(4) factor-count tower test (attempt)
  confirms SL(4) identity recursion (r-1)^4 + cubic derivatives; full 15x15
  ambient Jacobian needs SL(4) trace identities; verdict NEEDS-EXPERTISE

B28 projective quotient legitimacy
  controls whether the B26 sign quotient is canonical in lift-independent data

B29 hierarchy/normalization controls
  audits the Lucas hierarchy, full-return control, and lambda/h normalization

B30-B32 selector-first campaign
  proves the quotient is canonical conditional on PSL data, then isolates S1 as
  the extra A-sector self-similarity selector still not derived

B33-B36 extension controls
  test SL(n), Goldman/WP, topology, and Fibonacci-renormalization routes

B37 operational feedback quarantine
  locks feedback language to computable predicates and rejects awareness claims

B38-B47 deep S1 campaign
  shows arithmetic/torsion/filter reuse would force S1, but only conditional on
  T1: tangent return inherits original arithmetic persistence filters

docs/TRACE_SELECTOR_THEOREM.md / C5
  packages B38-B47 as the conditional theorem
  T1 -> S1 -> I=1/4 -> lambda/h=1
```

- **B1–B5** — gluing vs. Chern–Simons flatness, moduli evolution, Regge complex,
  BKL/Gutzwiller, Wheeler–DeWitt.
- **B6–B9** — the field-theoretic lift of the derived potential (P15/P16):
  the field equation `□τ+κ(τ²−τ−1)=0` (B6), Fisher–KPP creation dynamics (B7),
  the particle spectrum and the non-exact `m/g≈φ` near-miss (B8), and the
  fusion–scattering shared polynomial (B9). Each carries its caveat; none is a
  claim. See `../PROGRESS_LOG.md` 2026-05-27.
- **B13** — the punctured-torus trace map on the fiber character variety. Exact
  algebra shows the trace-map linearization contains the `A` quadratic as a
  lattice-conjugate rank-2 sector, but the bridge to physical `3+1`, matter,
  gravity, or awareness remains an inserted dictionary.
- **B14** — the half-step square-root selector. Exact algebra shows `A` has only
  two `GL(2,Z)` square roots, `F=L P` and `-F`, and that mixed closures
  `B(a,b)=L_aR_b` admit an integer orientation-reversing square root iff `a=b`.
  The remaining gap is whether the record-swap `P` is forced or inserted.
- **B15** — trace-map invariant controls. Exact algebra confirms the
  Eisenstein-to-golden diagonal linearization family and the discrete
  Fricke-Vogt invariant; it rejects the naive continuum proxy and rejects a
  proposed `sqrt(5)` Fibonacci coupling under the current invariant
  normalization.
- **B16** — record-swap status. Exact algebra shows `P` is unique up to sign as
  the involution exchanging the primitive pair `{L,R}`, but the exchange
  symmetry itself is not forced by the current A1-A6 minimal-record axioms.
- **B17-B24** — half-step kernel campaign. B18 establishes the trace map as the
  canonical half-step trace lift; B19/B17/B22 control the exchange, alternation,
  and spectrum claims; B20/B21/B23/B24 test awareness, spacetime, gravity, and
  anyon dictionaries and leave them stalled where no dictionary is derived.
- **B25** — Fibonacci spectrum anchor. Finite approximants at dimensionless
  `lambda/h=1`
  support a mid-scale box-counting slope near `0.75` and pass strict
  gap-labeling controls. In B25 alone, `lambda/h=1` is only motivated; later C5
  makes it conditional on T1, not proven.
- **B26** — `lambda/h=1` derivation attempt. Exact algebra shows `lambda/h=1` is
  uniquely selected by projective half-return self-similarity, but the
  projective half-return criterion itself remains an added rule. Verdict:
  `STALLED`, with B25 strengthened but not promoted.
- **B27** — `SL(3)` Fibonacci trace lift. Exact algebra gives an
  eight-dimensional trace map whose fixed-point Jacobian factors into golden
  sectors `(t-1)(t+1)(t²-4t-1)(t²-3t+1)(t²+t-1)`. The `A` sector survives and
  the commutator trace pair swaps under the half-step. Physical
  particle/antiparticle language is rejected as an unbuilt dictionary.
- **B48** — metallic `SL(3)` trace-map certificates. The B27 `m=1` lift extends
  to `phi_m(a)=a^m b, phi_m(b)=a`, with exact recurrence checks, commutator
  trace-pair invariant, entropy controls, fixed-line arithmetic classification,
  and compact `SU(3)` diagonal-slice representatives. This supports PC12 as
  standalone trace-map arithmetic and does not change PC11's T1-conditional
  selector status.
- **B49** — `SL(3)` certificate-to-proof hardening. The B48 fixed-line
  splitting classification is decomposed into a universal splitting criterion,
  direct positive families, square-gap propagation, finite positive-strip
  exclusions, and negative-strip/boundary exclusions. PC12 is strengthened but
  remains `NEEDS_VALIDATION`.
- **B50** — PC12 proof-draft assembly. B48/B49 are organized into an internal
  theorem-note skeleton with five theorem blocks and explicit non-claims. This
  makes PC12 structurally ready for proof drafting, not public release.
- **B51** — `SL(3)` symbolic-`m` factorization. The `c=3` fixed-line derivative
  rows are derived from the `(r-1)^3` triple-root recurrence, the symbolic `8x8`
  Jacobian commutes with the exchange involution, and the symmetric /
  antisymmetric block characteristic polynomials are proved for formal `m`.
- **B52** — multichannel Fibonacci bridge control. The simplest three-channel
  Fibonacci tight-binding model yields `6x6` determinant-one symplectic transfer
  matrices. In the commuting control it decouples into three `SL(2)` channels,
  and in the generic control it obeys an order-six trace recursion, not PC12's
  `SL(3)` third-order recursion. Verdict: useful negative control, no physics
  bridge.
- **B54** — general-`c` exchange structure. `[J(m,c),P]=0` is proved for symbolic
  `c`, so the exchange block-diagonalization holds on the whole fixed line, not
  only at B51's `c=3` (the reason is structural: `P`-equivariance at the
  `P`-invariant fixed line). At `c=1` the symmetric sector is the Eisenstein
  quadratic `t^2-t+1` and the antisymmetric is the golden `t^2-t-1`
  (discriminants -3 and 5 — the same pair as the P12 figure-eight gluing
  equation); for `m=1` the symmetric quadratic `t^2-ct+1` sweeps
  `Phi_3, Phi_4, Phi_6, (t-1)^2, char(A)` at `c=-1..3`. Standalone trace-map
  math; no claim promoted.
- **B28** — projective quotient legitimacy. The B26 sign flip is legitimate as
  a central-sign / `PSL` lift ambiguity at the special orbit, and the trace map
  is equivariant under that sign action. The choice to use the quotient as a
  selector remains an added bridge criterion.
- **B29** — hierarchy and normalization controls. The Lucas hierarchy selects
  dimensionless `(lambda/h)^2=L_n-2` under the projective criterion; literal
  full-return matching gives a different hierarchy. Finite spectral controls at
  the first hierarchy values pass gap-labeling checks, but no physical
  prediction is promoted.
- **B30-B32** — selector-first campaign. B30 shows the central-sign quotient is
  canonical if the state space is lift-independent `PSL` trace data; B31 shows
  primitive projective return alone leaves `I=c²-1` free; B32 isolates the
  remaining missing object as S1, the extra rule that the primitive projective
  return linearization reproduce the original `A` sector.
- **B33-B36** — extension controls. The `SL(3)` tower decomposes into
  symmetric-power sectors but no full `SL(n)` trace theorem is built; the
  Goldman/WP bracket and sign topology support the quotient but do not select
  `I=1/4`; Fibonacci spectral/gap controls remain compatible with many
  couplings and do not independently select `lambda/h=1`.
- **B37** — operational feedback quarantine. Feedback and invariant language
  are reduced to computable predicates; awareness/consciousness/religion/
  metaphysics-adjacent interpretations remain outside the claim system.
- **B38-B47** — deep S1 campaign. B38/B43/B44/B45 show that integer
  hyperbolic trace, minimal discriminant, torsion-one closure, or primitive
  renormalization hierarchy each recover `I=1/4` if applied to the tangent
  return. B39/B40/B41/B42/B46 show that this filter inheritance is not derived
  by the current framework. B47 records the clean verdict:
  `T1 -> S1 -> I=1/4 -> lambda/h=1`, where T1 is an explicit conditional
  assumption. `../docs/TRACE_SELECTOR_THEOREM.md` packages that verdict as C5;
  the files here remain frontier evidence, not proven claims.
- **B55** — c=1 fixed-line structure for general `m`. Completes B54's `c=1` row:
  the symmetric sector is **mod 4** (`Φ₆` for `m≡1,3`; `Φ₄` for `m≡2`; degenerate
  `(t−1)²` for `m≡0`) and the antisymmetric sector is `(t−1)(t+1)(t²−mt−1)=char(M)`
  for all `m`. Proved per residue class via the `c=1` closed forms (roots
  `{1,i,−i}` + a resonant linear term); `m=1` reproduces B54's twins.
- **B56** — figure-eight invariant-surface negative control. The diagonal
  `SL(2,C)` reps `w³−2w²−2w+1` give Fricke–Vogt `I ∈ {4, −17/2 ± 7√5/2}`, none
  `= 1/4`, so the figure-eight ↔ `I=1/4` (self-evidencing) bridge is **dead**; the
  `c=1` Eisenstein resemblance to the figure-eight tetrahedron shape is a
  cyclotomic coincidence. The separate P12 gluing-equation echo is unaffected.
- **B57** — general-`m` Diophantine splitting. Classifies integer splitting of the
  antisymmetric quartic for `m=1..6`: `{c=1, c=3}` universal, m-dependent extras,
  counts `[4,4,4,3,2,5]`; the Hilbert-class-field coincidence is killed for `m≥2`.
  Extends PC12's Theorem-4 content. Standalone trace-map math; no claim promoted.
- **B58** — SL(4) factor-count tower test (attempt). Confirms the mechanism (the
  `SL(4)` identity recursion is `(r-1)^4`, so derivative sequences are cubic in
  `k`; degree `n-1`) and the obstruction (the fixed-line point is the degenerate
  identity representation, traces second-order, so a representation-based numerical
  Jacobian cannot recover the ambient map). The full `15×15` ambient Jacobian
  needs the SL(4,C) 15-coordinate trace map (Procesi + substitution action), not
  built here. Verdict `NEEDS-EXPERTISE`; the SL(4) 7-factor prediction is untested.
