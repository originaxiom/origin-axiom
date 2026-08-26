# Wave 2 campaign intake: semantic split before execution

## Locked source

This intake audits Origin Axiom commit
`0fe97f9070384d9a5a98c625b1b70131de2556f1` on
the outside-bench remote ref.  The source adds `outside_bench/CAMPAIGN.md` and
`outside_bench/CAMPAIGN_CELLS.json`; it does not add a proof certificate or an
executed output for any proposed cell.

The campaign proposals are useful, but proposal, execution, and closure are distinct states.  A
feasible unrun proposal is therefore registered as `OPEN`, not promoted to `CONDITIONAL` or
`EXTERNAL_BLOCKER` merely because the older registry admitted only terminal statuses.

## Intake corrections

The source advertises twelve cells.  A proposition-level ledger has fourteen new rows:

1. The Markdown merges two different A2 questions: action of the rational map `T` on the full
   64-dimensional complement, and action of the semilinear beat `Sigma` on that complement.  The
   JSON correctly gives these separate computations.  They have different operators and different
   falsifiers, so they cannot share one canonical row.
2. The Markdown includes C4, the large-`T` GUE test, but the claimed full-detail
   `CAMPAIGN_CELLS.json` omits it.  The question remains real and is registered from the Markdown;
   its promised preregistered two-outcome detail does not exist in the locked source.
3. B1 asks whether the degree-four invariant space is spanned by `C^2`, where `C` is cubic.  This
   is false by grading: `C^2` has degree six.  The malformed degree-four assertion is closed
   `REFUTED`; the correctly graded degree `1,2,3,4` invariant census is a separate `OPEN` repair.

Thus the source's twelve scheduling labels become thirteen distinct proposed computations plus
one immediately closed type/degree error.

## Canonical mapping

| source label | canonical row | intake status | exact interpretation |
|---|---|---|---|
| A1 | OA-C1065 | `OPEN` | construct the invariant cubic and test selected-beat covariance |
| A2, rational `T` | OA-C1066 | `OPEN` | run `T` over both spin-2 quintuplets and all colored basis vectors |
| A2, semilinear `Sigma` | OA-C1067 | `OPEN` | test preservation/action of `Sigma` on the 64-dimensional complement |
| A3 | OA-C1068 | `OPEN` | compute the peripheral homology action in the marked meridian/longitude basis |
| A4 | OA-C1069 | `OPEN` | compute the Pin-minus obstruction/torsor and restriction to the orientable cover |
| A5 | OA-C1070 | `OPEN` | decide whether the omega-one parity clause is redundant |
| B1 malformed degree-four clause | OA-C1071 | `REFUTED` | a square of a cubic cannot span a degree-four component |
| B1 corrected | OA-C1072 | `OPEN` | compute invariant dimensions in degrees 1 through 4 with grading respected |
| B2 | OA-C1073 | `OPEN` | compute full-E6 and actual trinification trilinear invariant multiplicities |
| C1 | OA-C1074 | `OPEN` | derive the exact completed-L-function zero-counting main term and error |
| C2 | OA-C1075 | `OPEN` | define and verify a scoped Habiro/cyclotomic congruence table |
| C3 | OA-C1076 | `OPEN` | perform a preregistered high-precision asymptotic extraction and recognition test |
| C4 | OA-C1077 | `OPEN` | define and execute a powered, preregistered spacing test; absent from source JSON |
| C5 | OA-C1078 | `OPEN` | compute the degree of the peripheral restriction map on the selected component |

## Effect on the closure cut

None of these rows closes any strict endpoint gate C0--C7 as proposed.  A1/B1/B2 are structural
representation-theory inputs, not physical Yukawa tensors.  A2--A5 sharpen the beat/holonomy
record, not the missing Pin-to-four-dimensional-spin/QFT functor.  C1--C5 are arithmetic or
spectral probes and do not construct dynamics or normalize Standard-Model observables.

They remain worth running: short exact cells can expose errors, reduce ambiguity, and prevent a
future synthesis from leaning on an unchecked slogan.  Their priority does not supersede the
critical flavor task, whose current missing object is a normalized cyclic/Serre chain map for the
Calabi--Yau Cech--monad complex.

## Execution discipline

Every `OPEN` row contains its own closure criterion and falsifier.  On execution it must move to a
terminal status with a standalone artifact and exact scope.  Campaign exhaustion is impossible
while any `OPEN` row remains.  A source prediction is not evidence, and a bounded numerical scan
cannot become a theorem by being listed in a campaign document.
