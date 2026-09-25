# R44: exceptional paired modes on the same finite-energy background

September 25, 2026. Own branch audit/physical-bridge-2026-09-05.
Path-local authored result, not a shared B allocation or independently
accepted proof. Pre-execution seal: f52629a87046e1e206d84ce438c4b36df4dd70b7.

## Outcome toward the mission

The canonical-metric join is now an explicit authored argument, with
all 17 new finite controls passing. It puts the already received
exceptional defining/dual H1 classes on the SAME complete positive,
finite-Higgs-energy background supplied by R42. It does not combine a
background in one norm with a spectrum proved only in another.

This is a constructive compatibility result toward a physical model,
not a theory of everything and not net chirality. The counts remain
one and one. The projective structure, its parameter, central twist,
parent field/action and physical interpretation remain declared inputs.
The full parent spectrum and interactions are not computed here.

Evidence: [frozen proof](CANONICAL_CUSP_PROOF.md),
[pre-execution design](CANONICAL_CUSP_DESIGN.md),
[preflight and source limits](CANONICAL_CUSP_PRIOR.md),
[input hashes](CANONICAL_CUSP_INPUTS.json),
[execution receipts](CANONICAL_CUSP_RECEIPTS.json).

## 1. What changed

R43 correctly kept three questions separate: positive-parameter proper
convexity, global finite volume, and the complete canonical-metric
complex. R44 supplies an authored chain for the latter two:

1. The literal peripheral matrices force a graph domain and a bounded
   difference from the type-one model boundary. This gives a two-sided
   cusp bound for any invariant proper convex domain at q>0, q!=1.
2. The projective Margulis lemma gives an embedded proper torus end.
   A relative compact-core argument and H2(Gamma;R)=0 force its
   complement to be compact. No general projective tameness theorem
   or unproved marked diffeomorphism is silently assumed.
3. A determinant-one pointed rescaling has the product-cone limit.
   Affine-sphere jet continuity controls BOTH the base and the actual
   positive coefficient metric. On the end,

       h_B asymp dR^2/R^2 + dx^2/R + dt^2,
       dvol_h_B asymp R^(-3/2) dR dx dt.

   Thus the end is complete and finite volume. R42's energy estimate
   applies globally on this same canonical base.
4. The longitude operator has a uniformly bounded inverse for every
   Fourier frequency. The full, radially compatible chain homotopy is
   bounded in the actual norms. Complete-domain cutoffs and local
   ellipticity give finite-dimensional Hodge kernels and closed ranges.
   The explicit cutoff maps identify L2, compactly supported and ordinary
   cohomology, since the entire peripheral coefficient is acyclic.

These arguments are not finite-sample certificates. External existence,
Margulis, jet-continuity and relative-core theorems remain cited inputs;
the new applications have not received independent proof review.

## 2. The retained positive, without recounting it

F11's exact cohomology calculation was already reproduced in R43. R44
does not run another rank census or claim to have discovered its roots.

| Meridian scalar twist | Positive exceptional parameters q | Defining H1 / dual H1 |
|---|---|---|
| -1 | 17 - 12 sqrt(2), 17 + 12 sqrt(2) | 1 / 1 |
| +i or -i | 7 - 4 sqrt(3), 7 + 4 sqrt(3) | 1 / 1 |

Under the proof's cited inputs, these are now normalizable harmonic
one-forms on the canonical finite-energy background. No explicit
normalized spatial wavefunction, coupling integral or four-dimensional
particle assignment is supplied. Generic q!=1 in the four tested
central-twist families has no ordinary H1, hence none in this L2 complex.
The q=1 inverse degenerates and is deliberately not covered by R44.

## 3. What the metric change does and does not permit

The meridian shrinks; the longitude does not. Its limiting squared
length is 3 log(q)^2 in the normalized product control. Consequently
the homotopy is bounded, not decaying. This is sufficient for the
cohomology join, but F11's stronger compact-resolvent proof on the old
hyperbolic base cannot simply be copied. R44 neither computes the
essential spectrum nor claims that every positive mode is discrete.

Likewise F10/F11's infinite Higgs norm and nonnormalizable q variation
were proved on the FIXED hyperbolic base. They remain true there. The
parameter-normalizability conclusion is not transferred to the new
canonical base by citation. Its actual deformation/metric kinetic
norm requires a separate calculation; integrable end volume alone
does not prove smooth parameter dependence or a dynamical modulus.

The longitude argument applies to the defining four and its dual
because every semisimple weight is nonzero. A parent representation
with zero weights needs its own end analysis. In particular the full
neutral/gauge/adjoint sector is not covered by calling the defining-
sector check a whole-parent spectrum.

## 4. Source audit and verification grade

Ballas--Long's all-positive proper-convexity theorem and literal matrix
family are credited, not rediscovered. Ballas' original finite-volume
theorem was only near the hyperbolic point; its two-sided cusp and
Margulis mechanisms motivate, but do not replace, R44's all-q proof.
Cooper--Long--Tillmann Theorem 6.29 is an openness theorem, not by
itself a global finite-volume assertion. Selected complete sections
were personally read; no whole-56-page reading is claimed.

Harris--Scott's entire twelve-page article was personally read; its
printed p.149 explicitly states and uses McCullough's relative compact-
core theorem. That page and CLT pp.1393--1394 were rendered and inspected.
McCullough's original full proof was not accessible. It remains an
external theorem input, not a claimed independent reconstruction.
Exact URLs, reading limits and source hashes are in the proof/inputs.

The new finite tests verify literal conjugacy, the actual SL4 scaling,
the product Monge--Ampere equation/positivity, full radial flatness,
both Fourier inverses, the whole exterior Cartan identity and controls
that reject a wrong logarithm sign, omitted radial terms, q=1 and
zero semisimple weights. They do not solve the global PDE numerically
or independently certify the analytic/topological reasoning.

## 5. Execution and custody

- All six scientific files were committed, pushed and server-confirmed
  BEFORE first execution; they are unchanged afterward.
- Native algebra/control output passes; [17 new tests](CANONICAL_CUSP_TESTS_FIRST.txt) pass.
- [Three-file focused regression](CANONICAL_CUSP_FOCUSED_FIRST.txt):
  46 pass, one retained failed ID,
  test_physical_bridge_affine_background.py::test_generic_tensor_identity[ricci].
  This is the previously diagnosed structural-comparison failure; its
  separately sealed R42-V2 controls pass again. No new failure is hidden.
- Preseal cumulative custody: 693 artifact paths and 186 latest distinct
  seals agree. Governance: 26 pass/four historical failing categories;
  relay debt has aged to 41 flagged items. No full-suite-green or
  independent main-bank certificate is claimed.

The first failed SSH fetch and successful HTTPS/keychain retry are both
retained. No new remote head appeared, and no other seat branch was
written or merged. The read-only receipt checker validates the actual
bytes and fixed populations; it is not an independent mathematical audit.

The first report-stage cumulative check failed on a stale GOAL_VERDICT
hash. Diagnosis: an append patch matched an earlier duplicate anchor,
placing the new hash block before older rows, which the latest-row rule
then preferred. That failed capture is preserved. An explicitly EOF-
anchored appended block fixes the metadata; no scientific file, old
hash row, transcript or test was changed to obtain the repair.

## 6. Progress checklist and the next physical test

- [x] Retain and reproduce the exceptional algebraic classes (R43).
- [x] Supply the same-background end/norm/cohomology join at authored-
  proof grade, with explicit external inputs and passing controls (R44).
- [ ] Obtain independent review of the global/core/domain proof.
- [ ] Put the ENTIRE chosen parent roster on this background; derive
  the unbroken gauge algebra, zero-weight end operator and full domain.
- [ ] Check the q-deformation's actual canonical-metric kinetic norm
  and selection problem; do not import the old-base answer.
- [ ] Derive normalized interactions from the SAME action and decide
  whether an admissible mechanism removes mirror partners selectively.
- [ ] Complete source/end quantum consistency, anomalies, gravity and
  quantitative empirical tests. These are not paid by R44.

The next bounded research step is the full-parent/zero-weight join,
with a fresh prior-art lookup before any producer. A new geometric
analogy or another scan of the same exceptional ranks is not the next
step. Keep R40/R41's nonsplit/source route registered separately.
