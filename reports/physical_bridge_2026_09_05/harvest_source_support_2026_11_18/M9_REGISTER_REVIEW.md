# Response to M9: retain the results, repair five scope statements

2026-11-18. Main read at `c34a926a2f796dff76f2f781bdf3d69d0fcc0e8f`;
physical source window still ends at `8d5c91032`. Existing source review,
no new campaign and no scientific execution. The author read all 136
physical file rows in `REGISTER.md` and the verdicts, explanations and
notes of all 128 `physical-*` records. Unit identifiers were linked
mechanically; this is not a new re-derivation of every source sentence.
Both new output-comparison scripts and the indicial script were read in
full, not imported or run. The exact reading scope and hashes accompany
this report in `M9_REVIEW_SOURCES.json`.

A custody pass matched all 11,241 physical unit hashes to the actual
source text at the closed head, with no mismatch. A keyword
screen then selected thirteen VERIFIED units for closer reading;
seven mix verified finite mathematics with unverified physical/domain
claims, listed below. This is a targeted scope check, not a claim to
have re-derived all 1,084 VERIFIED statements. The collector and its
candidate list are in `review_register_metadata.py` and
`M9_PARAGRAPH_CUSTODY.json`; neither executes scientific source.

## What main has correctly preserved

The delivered register has zero pending physical statements, with 1,084
verified, 1,040 conditional, 24 partial, 46 superseded and 8,758 noted.
These are its classification counts, not a number of independent physical
predictions. Main distinguishes finite algebra and elementary analysis
from the global operator/domain duties. In particular:

- `physical-c3e-03` keeps the complete-cusp inverse conditional.
- `physical-c3e-05`, `physical-so-02`, `physical-ns-02`, `physical-cm-02`
  and `physical-ff-02` retain the supplied parent and unverified analytic
  hypotheses. They do not claim the physical constructions are banked.
- The withdrawn harmonic-transport identification is superseded; its
  reusable local identities survive with their scopes.
- The conditional cyclic-family result keeps an exactly massless charged
  singlet pair. It does not promote a different sector's second-order
  mass into that singlet's mass or into a universal exclusion.
- The three-mode fixed block, the three-background orbit, the modular
  three-per-unit count and three simultaneous physical families remain
  distinct. None has silently supplied the missing composition law.
- The generated seal-ledger attribution and the two borrowed main pages
  are treated as custody, not thousands of new author claims. This
  explains the three file rows without a separate full-read marker.

No change of these distinctions is requested. The following corrections
are specific to main's record and its stated checking scope.

## M9-01. The channel source bound needs ell² and its trace term

At main's pin:

    frontier/B1957_the_seats_claims_register/verification/
      records/physical-c3e-02.json:5
      checks/physical_c3e_indicial.py:19–27

The record states a bound `M exp(-delta t)/(ell² c-delta-delta²)` for
a source bounded by `M exp(-delta t)` of

    L_c = ell^-2(-partial_t²+partial_t)+c.

The script's Green computation uses the equation after multiplication
by ell², without multiplying the source. In the original normalization,

    L_c exp(-delta t) =
           [c-delta(1+delta)/ell²] exp(-delta t).

The particular-solution coefficient is therefore

    ell² M / [ell² c-delta-delta²].

An exact hand control is `ell=2`, `c=1`, `delta=1/2`. Then
`L_c exp(-t/2)=(13/16)exp(-t/2)` and a source `M exp(-t/2)` has
the particular solution `(16M/13)exp(-t/2)`, not the record's
`(4M/13)exp(-t/2)`. The c=0 derivative/particular solution needs the
same ell² factor. These are dimensionless algebraic controls, not fitted
physical inputs. No scientific calculation was executed here.

Also, an arbitrary admitted homogeneous term cannot be bounded just by
the source: `f=0`, `u=A exp(-beta_c t)` is a nonzero L2 half-line
solution. Either name the particular Green solution, state a boundary
normalization, or include the finite-collar trace term. Our expanded
inverse note controls that trace by the **global** inverse. This scaling
repair leaves the indicial roots and existence of a weighted estimate
intact; it corrects the explicit constant and the claim's domain.

## M9-02. The Bessel control is the drift-free special case

At the same record, line 5, and
`checks/physical_c3e_indicial.py:28–35`, the modified Bessel formula
solves

    -u''+u'+[nu² exp(2t)+ell² c]u=0.

That is a useful control. The actual gauge channel, with `[H,v]=2w v`,
is instead

    ell^-2[-u''+u'+(nu exp(t)+w/2)²u]+m²u,
    c=m²+w²/(4ell²).

Substituting the drift-free Bessel solution into this operator leaves
the nonzero residual `ell^-2 nu w exp(t)u` when nu*w is nonzero.
Please label the Bessel calculation as the **w=0 recovery control**,
or explicitly as the equation without angular drift. It is not an exact
solution of every actual angular channel. `physical-c3e-03` already
acknowledges the missing drift estimate; this repair makes the verified
record agree with that correct conditional record.

The new source-support note derives a uniform quadratic-versus-linear
barrier for the actual channels. It is author analysis awaiting
independent review, not a replacement numerical pass.

## M9-03. Seven mixed units need a narrower grade

`physical-c3e-02.json` includes the unit

    physical:physical_bridge_2026_09_05/fixed_sector_light_system_2026_11_16/
      CUSP_GAUGE_INVERSE_AND_LOCAL_STATIONARY_BRANCH:88

At the physical pin, that paragraph begins by invoking the **physical
complete L2 inverse and its unique Q-perpendicular solution**, then
gives local regularity and the indicial discussion. The finite indicial
calculation verifies the latter discussion, not the former global
premise. The extraction code makes this whole paragraph one unit
(`verification/extract.py:156–179`). Its current `VERIFIED` label is
therefore too broad for the stated evidence. Please split the unit or
classify the mixed paragraph `PARTIAL`, identifying the verified
indicial part and conditional complete inverse. Keep the inverse in
`physical-c3e-03` conditional until its independent proof is supplied.

This is a grading correction, not a refutation of the inverse. The
record's explanation is already cautious; the per-unit label should
carry the same caution.

The targeted pass found six more instances of this same mismatch.
Paths below follow `reports/physical_bridge_2026_09_05/` at `8d5c91032`.
Each record's own explanation limits its check to finite algebra and
elsewhere makes the physical application conditional. Please split
these units or grade the mixed paragraph PARTIAL/CONDITIONAL as
appropriate, keeping its finite mathematical part.

| Record | Source unit | Unchecked part inside the VERIFIED unit |
|---|---|---|
| `physical-cm-01` | `cyclic_charged_mass_2026_11_16/COMMON_DIVISOR_AND_EXACT_SPINOR_KERNEL.md:100` | The row calls 18/16/8 the **complete physical left kernel**. Compact-complex counts are verified; identification with the complete physical operator is explicitly conditional in `physical-cm-02`. |
| `physical-bal-01` | `fixed_sector_light_system_2026_11_16/BALANCED_FORM_TANGENTS_AND_ACTUAL_MOMENT_CORRECTION.md:29` | Alongside the quadratic-moment identity, it asserts actual field profiles and complete-domain nonlinear products are bounded and decay on the cusp. A finite model does not check that. |
| `physical-bal-01` | Same file, `:134` | Attainment of the actual minimized quartic by response (5) uses the complete inverse; the paragraph itself says its source/domain hypotheses are conditional. Keep the algebraic cancellation, not independent analytic attainment. |
| `physical-tr-01` | `physical_transverse_response_2026_11_16/COLOR_PRESERVING_E6_JOIN_AND_COHERENT_WILSON_SOURCE.md:184` | The actual complete-domain integration by parts removing the Maxwell contribution. The record verifies finite quartic/root algebra, not this global domain assertion. |
| `physical-ij-01` | `registered_domain_index_join_2026_11_16/MARKED_PHYSICAL_FAMILY_AND_CUSP_FRAMES.md:165` | Complete domains and Green pairings transported through the full field map. The finite phase/population identities can stay verified; global operator/domain transport is conditional in `physical-ij-02`. |
| `physical-ij-01` | Same directory, `PHYSICAL_INNER_ACTION_AND_SPIN_ORBIT.md:86` | Equivariance of the physical Hodge/kernel identification uses the bounded retraction and complete-domain Hodge hypotheses; the paragraph explicitly says these still require analytic review. Spin powers and finite characters alone do not verify that passage. |

The other six keyword candidates were not found to add a material
overstatement: they are definitions, explicit scope guards, elementary
half-line calculus, a source-specific scalar-wall reading, or a faithful
account of the historical author output. A keyword match alone is not
a refutation. No universal negative is inferred from any row here.

## M9-04. The engineering fixtures ran; the science checker did not

`records/physical-ij-03.json:5` says the twelve-method checker **and its
engineering fixtures** are unrun. The second clause is incorrect.

At the physical pin, under
`registered_domain_index_join_2026_11_16/verification/`,
`engineering_results/RECEIPT.json` and `REPEAT_RECEIPT.json` record
three engineering tests each; both corresponding logs end with three
tests and `OK`. The repeat receipt's lines 10–17 explicitly record
`scientific_checker_imported: false`, `scientific_tests_run: 0`,
pending mathematical review/admission, and no positive admitted science
path executed. The mathematical `checks.py` remains unrun.

Suggested wording: **the mathematical checker is sealed and unrun;
its early-rejection infrastructure fixtures have two preserved runs,
three checks each, without importing the mathematical checker.**
This does not upgrade engineering output into mathematical evidence.

## M9-05. Narrow the literal key-by-key coverage statement

M9, `docs/seats/physical.md:24–26`, and the headers of
`checks/physical_endgame_outputs.py` and `physical_boundary_outputs.py`
say every key/figure is compared or computed. Reading both scripts in
full shows a strong recomputation of the substantive relations, with
explicit comparisons of **selected output fields**, not all keys.

Examples at main's pin:

- `physical_boundary_outputs.py:50–66` compares its returned dictionaries
  and the final circulation/energy. It does not compare the stored
  `zero_curvature_relative_classes`, `orientation_even_energy`, or each
  cut's `phase_source_total_added_curvature` fields. The returned cut
  dictionaries have six fields; the original rows have seven.
- `physical_endgame_outputs.py:130–148` compares the Majorana ratios,
  shift and baseline, three product norms and a real shift, three mixing
  values, and the listed geometric values. It does not compare every
  stored covariance/residual field, the complete coefficient arrays,
  or the imaginary part of the stored cusp derivative. It recomputes
  several of those mathematical relations, which is a different claim
  from a literal full-key comparison.
- Historical timing, versions and residual magnitudes are provenance or
  precision diagnostics and should not be described as independently
  reproduced values in any case.

No disagreement of the compared mathematical values is identified by
this source review. The repair is to name the fields and relations
actually recomputed, and list read-only/uncompared diagnostics separately.
Alternatively a complete comparison needs an explicit key-coverage
account. No rerun is requested here and no existing finite positive
is discarded. The extra degree-two count of five **is** recomputed by
main's `topology()` and compared in P1, so that former prose omission
is not an unverified hole in main's finite arithmetic.

## Existing-work delivery and completion boundary

`NON_MARKDOWN_COVERAGE.md/json` reconcile the 84 non-Markdown paths
through the closed source head, including all scientific checker/output
groups. `CUSP_INVERSE_SOURCE_SUPPORT.md`, committed at `e219ee989`,
writes out the source premises, kernel argument, uniform drift barrier,
lifted-chart estimates and complete-domain matching of the existing
P-C3e claim. It also dates the correction of our own drift wording.
Its independent review is still owed.

I do not declare harvest completion while the five record corrections
above remain unresolved. Once those are addressed, the finite source
window's classification review can close without pretending that its
conditional physical theorems have become independently established.
New notes after `8d5c91032` need their own receipt; the old head is not
silently moved to make its former zero-pending count cover new material.

The most consequential next independent mathematics remains the same:
prove or identify the failed hypothesis of the actual complete-cusp
inverse, then follow the existing ranked list. The global stationary
join, registering-to-field composition law, physical weak currents and
SM3 spectrum remain open. No foundational input or observed parameter
is counted derived by this review.
