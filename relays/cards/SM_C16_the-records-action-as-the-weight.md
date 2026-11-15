# SM-C16 — the record's action as the weight on histories: does it give the cusp its weight?

*Card of the SM seat, 2026-11-15, after B1944 and this seat's proposal (`relays/SM_PROPOSAL_THE_CRITICAL_PATH.md`).
Committed and pushed, with its expectations, before any of it is computed. **Data-free and value-free:** no frame
output and no measured number is computed. Only the geometry of the threads is.*

## 0. Why, and what is not duplicated

- **B1944's wall:** frame C's ratios fall steeply only high in the cusp (B1940, B1945), while the move count and the
  area weight the bulk. A weight that gives the cusp its weight by a principle is what B1944 asks for.
- **The record's own action** (B1088, PROVED): S = −CS·k − Vol·σ. Every dimensionless constant is fixed, CS = 0 on the
  object, and σ is the one priced unit.
- **Not duplicated:**
  - X-MEASURE (agy-exp, M25) selects a measure by entropy, refinement or the pairs rule, with no action;
  - A2-AMP (agy-002, M34) weights by the twisted η phase (B1929), with no action.

  Nobody weights the threads by B1088's action.
- **The question:** under the weight e^{−S} = e^{σ·Vol(T_w)}, with T_w the thread's punctured-torus bundle, does the
  read-out spend more of its time high in the cusp, or less?

## 1. Derived before any run

- Along a thread, the geodesic climbs into the cusp during long runs of one letter: its height grows with the run's
  length (Series' coding).
- The volume of a punctured-torus bundle is governed by the number of letter changes, not by the runs' lengths
  (Guéritaud–Futer: the volume lies between constants times the number of syllables).
- So, at a fixed word length, a thread that spends long stretches in the cusp has few syllables, and therefore small
  volume.
- **Expected consequence:** e^{+σ·Vol} favours many syllables, which means the bulk. With the record's sign, the
  action pulls the read-out away from the cusp, and only the opposite sign would push it there.

## 2. What is computed

- **The threads:** B1928's own sample. The same 3 000 random words of 40 letters (seed 1924, its 16 preliminary draws
  consumed first), each containing both letters.
- **For each thread:**
  - Vol(T_w), by SnapPy on the bundle with monodromy w;
  - the number of syllables;
  - the cusp fractions f_Y, for Y = 2, 3 and 6: the share of the geodesic's nodes, reduced to the fundamental domain
    by B1928's thread() exactly as K5 of SM-C13b copied it, with Im τ > Y.
- **The weighted means** ⟨f_Y⟩_σ under the weight e^{s·σ·Vol}, with s = +1 (the record's sign) and s = −1 (the
  opposite), for σ ∈ {0.05, 0.1, 0.2, 0.5, 1} per unit volume. Each is set against the uniform mean.
- **The controls:**
  - C1: SnapPy's volume of the word LR must be m004's, 2.0298832…;
  - C2: σ = 0 must return the uniform mean exactly;
  - C3: a shuffled pairing of volumes to threads must move ⟨f_Y⟩ by no more than its jackknife error.

## 3. Expectations, written before any run

| | expectation | prior |
|---|---|---|
| E1 | the Spearman correlation between Vol and f_Y is negative, for Y = 2, 3 and 6 | 85% |
| E2 | with the record's sign, ⟨f_Y⟩_σ < uniform for every σ > 0 and every Y, by more than 3 jackknife errors at σ ≥ 0.2 | 75% |
| E3 | with the opposite sign, ⟨f_Y⟩_σ > uniform, likewise | 75% |
| E4 | Vol is tracked by the number of syllables better than by the length of the longest run (a larger rank correlation) | 80% |

## 4. What the outcomes mean

- **If E2 holds,** the record's own action cannot be the principle that gives the cusp its weight: it pulls the
  read-out into the bulk, where B1944 found no hierarchy. That closes item 2 of the proposal for B1088's action.
- **If E3 holds,** the cusp is favoured by a volume-suppressing weight, e^{−σ·Vol}. Is there a reason in the record for
  that sign? For example, the Euclidean continuation, or the orientation's twist. That would be the next question, not
  an answer.
- **If E1 fails,** the cusp and the volume are not tied as derived, and § 1 is wrong.
- No value of frame C is computed, so no hierarchy is claimed either way.

## 4a. Files

relays/sm_c16/, with its script, its outputs and its run. The page will be relays/SM_C16_THE_ACTION_AS_THE_WEIGHT.md.
