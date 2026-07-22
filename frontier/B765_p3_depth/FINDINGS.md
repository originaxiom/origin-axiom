# FINDINGS — P3 depth-exposure stratum (the negatives hunt, stratum 3)

cc3, 2026-07-22. Branch `hunt/p3-depth-exposure`. Prereg sha256 0166d9df.
Gate 5-Q binding throughout; nothing to CLAIMS.

## Summary

21 P1-banked negatives whose B' annotations flagged `depth_exposure=true` were
re-adjudicated using the E22 lesson: a finite-depth plateau is not proof of
universality.

**Adjudicated tally:**

| verdict | count | meaning |
|---|---|---|
| DEPTH-CLOSED | 8 | kill argument contains a universal proof step; no depth gap |
| DEPTH-HELD | 6 | depth gap exists but independently closed by P2 spectral face |
| DEPTH-EXPOSED | 7 | genuine E22-pattern open gap; kill is underproved |

No HALT triggered. Method A (structural depth analysis) and Method B (anatomy
cross-validation) agreed on every cell.

## The headline: 7 underproved kills

The 7 DEPTH-EXPOSED cells are kills whose evidence is finite-depth sampling,
whose claims are universal, and whose gaps are not closed by any independent
face in the current anatomy. They are not wrong — they are **underproved**.
The verdicts may be correct, but the evidence standard falls short of the
claim scope.

| id | kill_form | adj | gap | P2 |
|---|---|---|---|---|
| B489 | absence-at-depth-n | unadj | n=1..8 only; claim universal | — |
| B500 | absence-at-depth-n | stable | depth>=6 unswept | — |
| B685 | kind-mismatch | stable | pointwise to n=60/order 20 | — |
| TOMB-L255 | value-mismatch | unstable | n=2..13; sketch not proof | — |
| TOMB-L310 | genericity | stable | L<=10; 5-point inference | — |
| TOMB-L34 | genericity | none | one N, two seeds | — |
| WALL-7 | zero-intertwiner | stable | twisted (f3) 3-point only | FACE-IRREL |

**Common pattern:** all 7 are NOT in P2's spectral-face closure (6 are not in P2
at all; WALL-7's P2 verdict was FACE-IRRELEVANT). This is not accidental — P2
closed all the depth gaps it could reach. The remaining 7 are the honest residual:
kills whose claims outrun their evidence AND whose gap is not bridged by any
independent face.

## Method design

**Method A (structural depth analysis)** classified each kill_form as
depth-independent (category-error, kind-mismatch: the type conflict exists at
any depth) or depth-dependent (the verdict depends on what depths were checked).
Then parsed each depth_note to determine whether the gap is in the
verdict-bearing step or in auxiliary computation.

Key subtlety: 3 cells have structural kill_forms (category-error or kind-mismatch)
but depth-dependent EVIDENCE. B685's kind-mismatch is verified pointwise; the
denominator pattern could converge at higher orders. TOMB-L267 and TOMB-L77's
category-errors are proved for one invariant / one metallic seed, not universally.
These were correctly classified as DEPTH-EXPOSED by Method A despite the structural
form, and caught by the cross-validation warning system.

**Method B (anatomy cross-validation)** checked whether P2's spectral-face verdict
(B754) or other current anatomy independently closes each gap. All 6 DEPTH-HELD
cells are held by P2 KILL-EXTENDS.

## The 8 DEPTH-CLOSED cells

These kills contain a universal proof step that covers the claim scope:

- **B107** — category-error structural: off-principal multichannel sector exists
  at every SL(n) level
- **B437** — slope-5 genericity universally proved (symbolic, every knot)
- **TOMB-L241** — K-J closes fully (symbolic in c, m, lambda, mu)
- **TOMB-L247** — S1a/S1b exact and universal (reducible => kappa=2)
- **TOMB-L258** — derivative kill; falls with K-J (TOMB-L241)
- **TOMB-L63** — ambient unitarity is a general theorem (congruence-subgroup
  finiteness at every k)
- **TOMB-L67** — classical-vs-quantum type distinction structural at every k
- **TOMB-L70** — disc=5 vs disc=-3 field distinction depth-independent

## The 6 DEPTH-HELD cells

These have genuine depth gaps, but P2's KILL-EXTENDS verdict independently
sustains the kill via the spectral face:

- **TOMB-L252** — k>8 unchecked, but B754 spectral face closes
- **TOMB-L267** — m>=7 untested, but B754 spectral face closes
- **TOMB-L334** — n>15 unverified, but B754 spectral face closes
- **TOMB-L339** — Part 3 one-seed, but B754 spectral face closes
- **TOMB-L57** — m>3 unswept, but B754 spectral face closes
- **TOMB-L77** — one invariant only, but B754 spectral face closes

## Stabilization needed for the 7 exposed

Each exposed cell has a named stabilization path in the depth_note. None
requires new mathematics — all are finite-extension or induction proofs
within the existing framework. But none has been executed.

These 7 stabilization tasks are the program's honest depth-closure backlog.

## Relation to the campaign

P1 (B742): 213 records triaged, 30 kills earned, 2 revived.
P2 (B754): 19 spectral-face cells; 17 KILL-EXTENDS, 2 FACE-IRRELEVANT.
P3 (this): 21 depth-exposure cells; 8 DEPTH-CLOSED, 6 DEPTH-HELD, 7 DEPTH-EXPOSED.

The 7 exposed cells represent 7/33 = 21% of P1 negatives. All are honest
residuals — underproved, not disproved. The stabilization backlog is named
and scoped.

## Artifacts

- `compute.py` + `output.txt` (byte-identical on rerun)
- `results.json` (structured verdicts)
- `tests/test_p3_depth_exposure.py` (13 locks, all passing)
