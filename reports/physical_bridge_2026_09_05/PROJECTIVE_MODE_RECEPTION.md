# R43: exceptional modes retained; the same-background join stays explicit

Reuse executed September 22; report September 23, 2026.
Own branch audit/physical-bridge-2026-09-05. No shared B allocation.
This is incoming reproduction and primary-literature reception, not a
new original scientific producer or a claim of completed physics.

## Outcome

The incoming exceptional cohomology classes survive an unchanged
rerun. The original expectation fails again: 27 tests pass and three
fail. The separately sealed correction gives 40 passes. Both outcomes
are preserved, not averaged into a fictitious all-green original run.

Ballas and Long's published result also extends proper convexity and
discrete faithfulness to every positive parameter of the underlying
real family. The exceptional parameters must therefore NOT be rejected
merely for lying outside the earlier nearby-parameter theorem.

These are useful positives. They are still not a same-background
physical spectrum: F11 uses the complete hyperbolic base, whereas R42's
finite-norm background uses the canonical Blaschke base. This intake
does not certify finite volume at every exceptional parameter, nor
transfer the L2 complex between those metrics. The concrete next
question is that end/domain comparison, not another rank scan.

Receipts: [manifest](PROJECTIVE_MODE_RECEPTION_RECEIPTS.json),
[original rerun](FORK_F11_ORIGINAL_REUSE_2026_09_22.txt),
[corrected rerun](FORK_F11_CORRECTED_REUSE_2026_09_22.txt),
[read-only custody checker](projective_mode_reception_check.rb).
The predecessor remains [R42](AFFINE_BACKGROUND.md); its scientific
files, first failure and separately sealed diagnostic are unchanged.

## 1. What was read and rerun

Incoming source pin: 08ff88e0ed841b25274c46ec2490a410729639c2.
Original F11 seal: 8545472529a1df7c16dd6a511b6a7b421a200b62.
Exception correction seal: 15c32b3c4e6dcdd7c56ac45ba4ac437cedac6dfd.

The full design, proof, producer, original tests, exception addendum,
exception producer, corrected tests, seals and findings were personally
read, together with F02's complete-domain proof. No delegated summaries
were used. F10's proof/producer had already been read at R42.

Before either run, twelve seal entries (ten distinct paths) were
matched against their seal commits, the received pin and the execution
snapshot. The snapshot includes the unchanged F10 dependency. The two
test files were run outside the active checkout with the same fixed
pytest options; no root-checkout test fixture or scientific edit was
introduced. This is SAME-IMPLEMENTATION REUSE, not independent algebraic
reimplementation, interval verification or independent global analysis.

The original failures are precisely the three nontrivial-character
instances of test_every_positive_rank_exception_is_geometric. They
are genuine counterexamples to the declared expectation, not the R42
structural-comparison bug. The correction re-exports every unaffected
original test and replaces only that expectation, adding exact
quadratic-field cocycle/nonboundary checks.

The successful all-head/tag fetch on September 23 produced no ref
updates. No other branch was written, merged or renamed.

## 2. The exact positive and its scope

This computes over the stated figure-eight real SL4 family, its four
central character twists and dual sectors. It is not a complete
class/filling/coefficient census. The algebraic exceptional locus is:

| Scalar meridian character | Positive exceptional q | H1 in E and E* |
|---|---|---|
| -1 | 17 - 12 sqrt(2), 17 + 12 sqrt(2) | 1 and 1 |
| +i or -i | 7 - 4 sqrt(3), 7 + 4 sqrt(3) | 1 and 1 |
| +1 | q = 1 only | ordinary H1: 1 and 1; F11's q != 1 L2 theorem does not cover this point |

The exact determinantal factors are q^2-34q+1 and q^2-14q+1.
The implementation computes all 70 maximal minors of each relevant
matrix, checks denominators, counts positive roots, and verifies rank
and nontrivial cocycles in the quadratic extension. At an exceptional
point the coboundary rank is four and the relator-Jacobian rank is
three. The two real embeddings are retained; the explicit cocycles are
cochains, not normalized spatial wavefunctions.

Under F11's specified complete hyperbolic base and cusp coefficient
norm, its authored analytic comparison identifies these groups with
normalizable harmonic one-forms. The partner counts are equal. That
does not establish four-dimensional particle chirality, a selective
mirror mass, a global stationary background at those parameters, or a
spectrum for the whole parent gauge algebra. The nontrivial central
characters are choices; neither the paper nor these ranks selects them.

The untwisted generic vanishing statement survives on its own
parameters. The over-wide assertion that ALL positive parameters and
central twists vanish does not. Likewise, no same-base flat dual
isomorphism is needed for equality of these cohomology dimensions.

## 3. Personally assessed analytic bridge in F11

The proof is not a torus-only calculation. For q != 1 it uses a
longitude operator T = partial_y + C_y whose Fourier inverse is bounded
because k=log(q) is nonzero. In its notation,

    C_y = -k D - beta P/u,
    D = diag(1,-3,1,1),  P^2 = 0,
    ||T^-1|| <= 1/abs(k) + abs(beta)/(u abs(k)^2).

The contracting homotopy is K=i_y T^-1. Full flatness, including the
radial commutator, gives d_C K + K d_C = I. On the FIXED hyperbolic
cusp the vector length is L/z, so the tail norm bound for K tends
to zero. Combined with the complete-domain cutoff argument and local
elliptic compactness, this supports the claimed charged-sector compact
resolvent and closed ranges. Peripheral acyclicity then identifies
compactly supported, relative and ordinary cohomology in this setting.

I checked the cutoff/primitive argument's degree issue: for a degree
zero closed primitive on the tail the contraction identity makes it
zero; higher-degree primitives are replaced using the cutoff homotopy.
The relevant Hilbert-complex closed-range/Hodge framework was checked
against Arnold, Falk and Winther, sections 3.1.1-3.1.3 and the start of
3.2, through Theorem 3.1:
https://arxiv.org/html/0906.4325v3#S3.SS1.SSS3 .
Only these sections, not their entire paper, were read.

This is personal analytic review of an authored argument. The finite
tests do not certify the analytic theorem. It applies to the specified
norms, their stated uniform-equivalence class and covered hypotheses;
it does not make all positive spectra dual-paired or establish compact
resolvent in the neutral/whole-parent sector. The divergent fixed-base
Higgs norm and nonnormalizable q variation remain separate from the
existence of these finite-norm fluctuations.

## 4. The literature changes one premise, not all of them

Samuel Ballas and Darren Long, *Constructing thin subgroups
commensurable with the figure-eight knot group*, Algebraic & Geometric
Topology 15 (2015), 3009-3022:
https://msp.org/agt/2015/15-5/agt-v15-n5-p16-s.pdf .

All fourteen pages were read through extracted text, including the
appendix and references. Printed pages 3014, 3015 and 3020 were rendered
and inspected directly. Theorem 3.3 gives the positive-parameter
proper-convex/discrete-faithful continuation. The appendix's rational
generators are literally R42's matrices with t=q/2, and the alternative
parameter satisfies v=2t=q. This is a direct matrix-source comparison,
not a new symbolic run or an independently reconstructed proof of
their global theorem.

The conservative received content is preservation of an invariant
properly convex domain for all q>0. The theorem's definition does NOT
include a finite-volume assertion. Therefore the R42 energy estimate's
finite-volume hypothesis is not silently discharged by this citation.
The quotient's marked end/volume control remains a stated verification
duty in this intake. The paper's arithmetic lattice construction is
not identified with a compact physical gauge group.

The projective theorem concerns the underlying real representation.
The complex central twists used in F11 require their own coefficient-
metric descent statement. Multiplication by a unitary character must
not be confused with changing the real projective developing geometry
or with physical selection of that character.

Prior retrieval was also checked. The broad query 'Ballas Long thin
convex' returns 247 hits and 43 settled matches, including
incidental long/thin substrings. The more specific query 'Ballas
Thistlethwaite projective' returns twenty hits and no settled match at
its two-term threshold; B199's actual reference concerns a different
SL3 character-variety calculation. These are retrieval diagnostics,
NOT a whole-history absence certificate or a novelty claim.

## 5. Revised next test and mission direction

The useful next calculation must keep one bundle, positive norm,
background, action and operator domain together:

- [x] Preserve and rerun both the false original expectation and the
  corrected exceptional classes.
- [x] Receive the published all-positive proper-convexity theorem with
  the literal parameter map, rather than excluding distant parameters
  using a merely nearby theorem.
- [ ] Establish the chosen quotient's marked cusp and finite-volume
  hypotheses at the exceptional parameters, citing the exact global
  and end theorems. Proper convexity alone is insufficient.
- [ ] Specify the canonical positive metric for each actual twisted
  coefficient and its complete form/gauge domains.
- [ ] Prove or refute boundedness of the longitude contraction in those
  ACTUAL base and coefficient norms, including radial terms. F11's
  factor L/z is not available by renaming the new metric.
- [ ] If only a bounded inverse remains, test closed range and the
  cohomology comparison separately from compact resolvent; they are
  different claims. If the contraction fails, compute the actual end
  spectrum rather than inferring either vanishing or chirality.
- [ ] Determine all relevant modes and their gauge/interaction/anomaly
  interpretation in that same background before claiming particles.

This keeps effort aimed at the physics bottleneck: the compatibility
of the background with its excitations. A positive join would be a
better mathematical field-theory candidate, not yet a TOE; paired
modes would still leave a chirality mechanism to derive. A scoped
negative would redirect this lane to the registered R40/R41 noncentral
source/end-action route without deleting its interior-index positives
or declaring a universal no-go.

Base dynamics, parameter/character selection, four-dimensional field
identification, full quantum/anomaly consistency, gravity, scale and
discriminating observations are not paid by these reruns. R42 remains
the latest original scientific execution. No new B, new original
scientific seal, full-suite green, independent main-bank acceptance
or completed mission is claimed by this reception checkpoint.

The [next working note](CONVEX_CUSP_MODE_WORKING_2026_09_23.md) records
a proposed pointed-domain/longitude-contraction comparison. It is
explicitly UNSEALED and UNEXECUTED, not an additional scientific result.
Its actual-domain and coefficient-norm hypotheses must be proved before
the limiting comparator can carry a physical-mode conclusion.

Reporting checks retain 26 passing governance categories and four
previous failing categories. Relay debt has aged from 29 to 30 stale
items; unchanged categories do not mean unchanged debt. Custody and
staged whitespace checks pass. No full suite or independent main-bank
review is claimed; see PROJECTIVE_MODE_RECEPTION_FINAL_CHECKS.txt.
