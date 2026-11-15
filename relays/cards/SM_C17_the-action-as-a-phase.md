# SM-C17 — the record's action as a phase on histories: does interference favour the cusp?

*Card of the SM seat, 2026-11-15, completing SM-C16's open form. Committed and pushed, with its expectations, before any
of it is computed. **Value-free and data-free:** only the threads' volumes, Chern–Simons invariants and heights are
computed.*

## 0. The question

- SM-C16 found that the real weight e^{−S} built from B1088's action, S = −k·CS − σ·Vol, favours the bulk.
- The remaining form is the phase, e^{iS} = e^{−i(2πk·CS + σ·Vol)}: a sum over histories with phases.
- Interference selects a region if the threads that live there carry coherent phases, while the others cancel.
- **The question:** are the cusp-heavy threads more coherent than the bulk threads?

## 1. What is computed

- **The threads:** B1928's 3 000 words of 40 letters (seed 1924), as in SM-C16.
- **For each thread:** Vol and CS by SnapPy (CS mod ½, as SnapPy gives it), and the cusp fractions f₂ and f₃ above
  heights 2 and 3, from B1928's thread() copied verbatim.
- **The bins:** the top 10 % of threads by f₃ (the cusp-heavy) and the bottom 50 % (the bulk).
- **The coherence** of each bin, C = |mean of e^{iφ}| over its threads, with φ = −(2πk·CS + σ·Vol). It is computed for
  k ∈ {0, 1, 2} and σ ∈ {0.05, 0.1, 0.2, 0.5, 1, 2}.
- **The floor:** the same coherence with the phases shuffled among all threads, over 200 shuffles. Its 95th percentile
  is the bar.
- **The effective cusp share:** |Σ e^{iφ} f₃| / |Σ e^{iφ}|, set beside the uniform mean.
- **Controls:**
  - C1: CS(LR) = 0 and Vol(LR) = m004's;
  - C2: k = 0 with σ = 0 gives C = 1 in every bin;
  - C3: the shuffled floor lies near 1/√n.

## 2. Expectations, written before any run

| | expectation | prior |
|---|---|---|
| E1 | at σ ≤ 0.1 with k = 0, both bins are coherent (C > 0.9): the phase selects nothing | 80% |
| E2 | at σ ≥ 0.5, both bins fall to the shuffled floor (C below the 95th percentile): no region is selected | 55% |
| E3 | for k ≥ 1, the Chern–Simons term scrambles both bins at every σ | 60% |
| E4 | the cusp-heavy bin is never above the floor while the bulk bin is at it (no localization by interference) | 60% |

## 3. What the outcomes mean

- **If E4 holds:** the record's action as a phase does not localize the read-out on the cusp either, and B1088's action
  is closed as the weight in both forms.
- **If E4 fails** (the cusp bin coherent above the floor while the bulk cancels): interference favours the cusp. That
  would be the first principled weight to do so, and a sealed values card would be justified next.
- No frame value is computed, so no hierarchy is claimed.

## 4. Files

relays/sm_c17/, with its script, outputs and run. The page will be relays/SM_C17_THE_ACTION_AS_A_PHASE.md.
