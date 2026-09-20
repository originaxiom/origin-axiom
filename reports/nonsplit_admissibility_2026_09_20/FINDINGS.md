# F01: a scoped global harmonic obstruction and a positive local cusp

2026-09-20. New fork audit/fork-2026-09-20. Path-local research checkpoint;
no shared B number and no claimed main-bank certification. Full TOE goal active,
not achieved. The preceding strategic audit was progress: it supplied the
ranked decision that led to this executed admissibility check.

## Outcome

Two complementary statements have now been derived and checked at their
stated scope:

1. **The exact m010 positive is not a smooth source-free finite-energy
   harmonic flat-bundle background on the complete finite-volume space.**
   The written cutoff proof applies to both its rank-two base and its actual
   rank-four Sym^3-twisted coefficient bundle, not just to metrics induced
   from a rank-two metric. It does not alter its exact cohomological I=+1.
2. **Its peripheral data DO admit a finite-energy harmonic local cusp.**
   An explicit solution works for every constant positive flat torus metric.
   The inner boundary supplies the signed flux. Gluing a source-free compact
   core with that same smooth boundary data cannot supply the required balance.

These are authored mathematical results with exact identity checks, **not an
independent review of the infinite-domain proof**, a global sourced solution,
a physical fermion spectrum or a new experimental prediction. No novelty in
the literature is claimed.

The strategic change is specific: do not repeat finite-character or census
searches hoping this particular nonsplit flat bundle becomes an unsourced
finite-energy harmonic vacuum. Do not discard the nonsplit index or its cusp.
First derive the physical admissibility condition from the chosen action.
If it requires this finite-energy class, derive the missing noncentral
source/boundary term and recompute the physical operator in that completion.
The second-pass clarification below explains why a source is not yet proved
the only possible physical continuation.

### Same-day report-guided scope clarification

The [second pass](../report_guided_resweep_2026_09_20/FINDINGS.md) recovered
R28's distinction between harmonic/background norm, static residual potential
and fluctuation kinetic norm. The theorem here assumes integral |Psi|^2 finite;
it does not derive that condition from a physical parent action. An infinite
harmonic-map-energy background with fixed end data, acceptable physical action
and normalizable fluctuations is not excluded by this theorem alone. Its
existence for the nonsplit witness has NOT been established. R28's commuting
source-complement example is not such a global nonsplit construction.

The mathematical obstruction and cusp solution are unchanged. The correction
is to their physical use and the ordering of the next task. Also, a source
`J=j Id` is scalar on this coefficient bundle; not every abelian or Cartan
gauge source acts that way. Check its actual representation before applying
the trace-free projector test. Frozen proofs, instruments and seals are intact.

## What establishes the obstruction

For any flat complex bundle D=A+Psi under the hypotheses above, choose a
D-invariant subbundle S and its metric-orthogonal complement Q, and write
eta for the off-diagonal extension one-form. With r=rank(S), s=rank(Q),
n=r+s, the trace-free Hermitian projector generator is

    xi = s Id_S - r Id_Q.

The exact block identity is

    <Psi,d_A xi> = -(n/2)|eta|^2.

Test d_A^*Psi=0 against a compactly supported cutoff times xi. Completeness
gives cutoffs with gradient O(1/R), and finite volume and energy bound the
error by O(sqrt(Vol(M))*||Psi||_2/R). It vanishes. The nonnegative integral
of |eta|^2 therefore vanishes: every invariant subbundle has an invariant
complement. The marked witness does not, as the exact matrix controls confirm.

[Full hypotheses, proof, and scope](PROOF.md). This supplies the noncompact
cutoff step rather than using the compact hypothesis in Corlette's Proposition
3.2/Corollary 3.5 without checking it. The PDF-reading workflow was used to
inspect the indexed primary text's assumptions; the attempted local download
failed, so no full local-paper reading or successful visual inspection is claimed.

## What establishes the positive local cusp

The marked peripheral holonomies in the invariant-flag frame are exactly

    rho(mu) = [[1,-1],[0,1]], rho(lambda) = [[1,1],[0,1]].

For the source cusp metric dr^2+exp(-2r)h0 and torus coordinates x1,x2, let
K=|d(-x1+x2)|^2_h0. The H3-valued map

    z=-x1+x2, y=sqrt(K/2) exp(r)

has **all three tension components zero**, map-energy density |df|^2=3,
and E_cusp=3 A0/4 on r>=0. A0 is the cross-sectional area at r=0; this is
not a dimensionful physical prediction. For b=-log y,

    Delta(b o f)=2,
    integral_cusp[0,R] 2 = A0 - A0 exp(-2R).

The right side equals the inner plus outer normal flux. Dropping the inner
term produces an explicit mismatch A0. A wrong height normalization produces
nonzero tension -3/2 on the square-torus control. Thus the instrument can reject
both a wrong solution and the mistaken boundary-free application.

For a hypothetical smooth global harmonic map with nonzero fixed-core
horizontal energy Q0, the same scalar identity gives the necessary bound

    E(M_R) >= Q0^2/(4 A0) [exp(2R)-exp(2r0)].

It is a conditional lower bound, not an existence statement or an asymptotic
equality. For cutoff-dependent solution families, Q0 need not remain fixed.

## The next action is now constrained, rather than merely named

The map version of a source tau(f)=J requires, under the stated integrability
and cutoff conditions,

    integral db(J) = -integral q,
    q=|df|^2-|d(b o f)|^2 >= 0.

There is also a direct flat-bundle consequence of the proved block identity.
If d_A^*Psi=J, with <J,xi> integrable, the same cutoff calculation yields

    integral <J,xi> = -(n/2) integral |eta|^2.

This last displayed implication is a post-run analytic consequence, not a
new numerical experiment. Since trace(xi)=0, a purely central source J=j Id
has zero pairing and cannot balance a nonsplit extension under these hypotheses.
A candidate source must couple to the invariant splitting, or a physical
boundary must provide the corresponding flux. The equation is covariant;
it is not a license to choose a compensating current by hand.

**Next bounded task (clarified by the second pass):** derive admissibility and
end variations from the available parent/source action. If that selects the
finite-energy class, inspect its actual source contribution for the required
sign, representation and boundary behavior. Then solve its regularized
background and test the fermion domain. If different fixed asymptotics are
admitted, test existence and normalizable fluctuations there explicitly.
Neither route is supplied by relabeling the old cohomology.

## Verification and failure custody

- Initial seal commit: `0c271c08`.
- First producer: exit 1, no scientific verdict. expand_complex introduced
  re(p1)/im(p1) before a complex-linear solve. Source and raw log retained;
  [sanitized first failure](RUN_FIRST_REDACTED.txt).
- Correction seal commit: `4480bd44`. [Correction note](CORRECTION_V2.md).
  Only the complex-linear simplification and versioned seal/module paths changed.
- Corrected standalone producer: exit 0, every explicit assertion passed.
  [Exact output](results_v2.json), [transcript](RUN_V2.txt).
- Focused suite first attempt: **7 passed, 10 setup errors in 5.55 s**;
  Sage's runtime could not access its cache lock. No lock was deleted and
  no failed mathematical assertion was skipped or weakened.
  [Sanitized environmental failure](TESTS_V2_REDACTED.txt).
- Unchanged focused suite with runtime access: **17 passed in 20.70 s**.
  [Receipt](TESTS_V2_RUNTIME_RETRY.txt). This includes all seven F01 checks
  and ten existing R27 exact-field/cohomology controls over F13 and Q(u).
- Repository gates: **26 pass, 4 fail**, exit 1; [full output](GATES_CHECKPOINT.txt).
  Failures are attribution, test-vacuity, seal-provenance and aged relay debt.
  The named older scientific files/tests and gate code were not modified in
  this fork. A historical-time baseline run was not performed; this is not
  a full-green certificate or a claim that all gate debt is unchanged.
- Original sealed verify.py and test_verify.py remain frozen; the current
  implementation is verify_v2.py, selected explicitly by test_verify_v2.py.
  The original failed test file is not silently overwritten or marked xfail.

Exact controls include the relator/peripheral words, full invariant flag,
nonsplitting, split control, all projector signs, Busemann Hessian and a
dilation countercontrol, full cusp tension, boundary flux and energy integral.
The analytic theorem is the written argument, not extrapolation from these
finite checks. The exact +1 index remains checked by the existing independent
Sage producer as part of the successful regression.

No full repository suite, independent banking audit, parent field-equation
solution, anomaly completion, quantum mirror gap, 4D gravity or observational
comparison has been established by this checkpoint. It must not be quoted
as either a complete TOE or a universal obstruction to one.

Public failure transcripts redact workstation prefixes and trim trailing
horizontal whitespace. Their byte-faithful originals remain locally in place,
excluded from Git; EXECUTION_RECEIPT.json records their original SHA-256 values.

## Sources and reproducibility

- [Frozen design and search receipt](DESIGN.md), [proof candidate](PROOF.md),
  [current producer](verify_v2.py), [current tests](test_verify_v2.py).
- [R27 original mathematics and domain distinction](../physical_bridge_2026_09_05/FINITE_TWIST.md).
- [R35 source-scope review](../physical_bridge_2026_09_05/LITERATURE_AND_SEATS_2026_09_19.md).
- [Whole-picture audit that selected this question](../whole_picture_audit_2026_09_20/AUDIT.md).
- Corlette, *Flat G-bundles with canonical metrics*, JDG 28 (1988),
  361-382, [primary paper DOI](https://doi.org/10.4310/jdg/1214442469).
  Relevant indexed PDF pages read: introduction and sections 2-3, especially
  pp. 366-368; not the complete existence proof in section 4.
