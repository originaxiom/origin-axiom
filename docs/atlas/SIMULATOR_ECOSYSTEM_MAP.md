# Simulator Ecosystem Map

Status: design gate. No simulator should be built just because it would look
good.

## Rule

Build an interactive simulator only when it does at least one real job:

```text
explain a hard concept better than prose
make a calculation reproducible in the browser
let a reader vary assumptions and see the verdict change
show why a tempting path fails
compare mechanisms under the same gate
teach the mathematics without diluting rigor
```

## Required Parts

Every serious simulator needs:

```text
tested numerical core
explicit assumptions
linked proof/probe/source cards
exportable parameters and results
reproducible run state
versioned data
clear verdict mapping
plain-language explanation
formal explanation
```

If those parts are missing, the tool should stay a sketch.

## Candidate Simulators

### L/R Residue Explorer

Purpose: show how primitive shears compose, why order matters, and how `A = LR`
appears.

Useful because: it makes noncommutative residue visible without hiding the
algebra.

### Commutative Vs Noncommutative Cancellation Gate

Purpose: compare perfect cancellation in a commutative setting with residual
structure in an ordered setting.

Useful because: it teaches the central intuition without turning it into a
claim.

### Trace / Discriminant / Phi Classifier

Purpose: let a reader scan small `SL(2,Z)` candidates and see which filters
select trace 3 and discriminant 5.

Useful because: it directly mirrors the conditional uniqueness theorem.

### Punctured-Torus And Figure-Eight Monodromy Explorer

Purpose: show how a punctured-torus bundle with monodromy `A` relates to the
figure-eight host.

Useful because: the topology is hard to visualize from prose alone.

### A-Polynomial Convention Checker

Purpose: expose how sign, variable, and representative conventions affect the
claimed relation.

Useful because: it prevents a known class of overclaim.

### State-Integral Contour Explorer

Purpose: show how multiple contours or thimbles can be mathematically valid
while only some produce the desired sector.

Useful because: it turns the selector obstruction into an inspectable object.

### BPS Kink And Fluctuation-Spectrum Explorer

Purpose: reproduce the derived potential, kink profile, and fluctuation
analysis under explicit assumptions.

Useful because: it separates exact internal dynamics from optional physical
lifts.

### Fusion Boundary-Count Explorer

Purpose: compute small fusion-state counts and boundary constraints.

Useful because: it can distinguish exact algebraic counts from numerological
interpretations.

### Campaign Dashboard

Purpose: summarize long-running exploration outputs as verdicts, missing
objects, and candidate follow-ups.

Useful because: it turns volume into a reviewable map.

### Failure-Atlas Navigator

Purpose: browse failed paths by obstruction type, not by chronology.

Useful because: it prevents repetition and makes negative results usable.

## Implementation Order

Do not start with the hardest simulator. First build one vertical slice:

```text
L/R residue explorer
  -> trace/discriminant classifier
  -> failure link for commutative cancellation
```

Only after that slice is tested should the project build topology, state-
integral, or field-theory tools.
