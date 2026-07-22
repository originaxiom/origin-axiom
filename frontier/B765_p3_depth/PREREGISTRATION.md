# PREREGISTRATION — P3 depth-exposure stratum

cc3, 2026-07-22. Branch `hunt/p3-depth-exposure`.

## Design

The E22 error class (premature non-congruence from a shallow level-check) established
that a finite-depth plateau can be misleading: the conclusion can change at a deeper
level. P3 applies this lesson to the 21 depth-exposed P1 negatives identified in the
B' annotations.

### Question

For each of the 21 targets whose `depth_exposure=true` in `bprime_annotations.json`:
does the kill verdict rest on a finite-depth check whose scope falls short of the
claim's universal scope? If so, is the gap closed by independent means (P2 spectral
face, structural kill_form, current anatomy), or is it genuinely open?

### Targets

21 P1 negatives with `depth_exposure=true`:
- 14 overlap with P2 (spectral-face adjudicated in B754)
- 7 are P3-only: B437, B489, B500, B685, TOMB-L255, TOMB-L310, TOMB-L34

### Method

**Method A — structural depth analysis.** For each target:
1. Parse the `depth_note` to extract: (a) what was checked, (b) what scope the
   killed claim requires, (c) whether the check is universal-by-proof or finite-sampling.
2. Classify the kill_form as depth-dependent or depth-independent:
   - Depth-independent forms: category-error, kind-mismatch (structural; the type
     conflict exists at any depth)
   - Depth-dependent forms: absence-at-depth-n, value-mismatch (the value might
     change at unchecked depths), genericity (the genericity argument might not
     extend)
3. Cross-reference: if kill_form is depth-independent AND the structural argument
   is universal, the depth gap is IRRELEVANT.

**Method B — anatomy cross-validation.** For each target:
1. Check whether P2 (B754) independently closes the cell (KILL-EXTENDS verdict)
2. Check whether the current anatomy (B734 congruence tower, B737-B753 spectral
   surface, QP sequence B759-B762, chain C1-C19) provides an independent argument
   at all depths
3. HALT if Method A and Method B disagree on any cell's exposure status

### Verdicts (per cell)

| verdict | meaning |
|---|---|
| DEPTH-CLOSED | kill argument is universal-by-proof; no depth gap |
| DEPTH-HELD | depth gap exists but independently closed by anatomy/P2 |
| DEPTH-EXPOSED | genuine E22-pattern open gap; the kill is at risk |

### HALT mechanism

Global HALT if:
- Any cell classified DEPTH-CLOSED by Method A but lacking the universal proof
  step when checked
- Any cell classified DEPTH-HELD by Method B but the independent closure is
  actually depth-dependent itself
- Method A and Method B contradict on exposure status
