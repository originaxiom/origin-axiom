# SM-C17 — the record's action as a phase: interference does not favour the cusp either

*The SM seat, 2026-11-15. Card `relays/cards/SM_C17_the-action-as-a-phase.md`, sealed and pushed before the run.
Value-free and data-free: only volumes, Chern–Simons invariants and heights of B1928's 3 000 threads were computed.*

## The answer

- **With B1088's action as a phase, e^{iS} = e^{−i(2πk·CS + σ·Vol)}, no setting makes the cusp-heavy threads coherent
  while the bulk cancels.**
  - Wherever any bin stays coherent above its shuffled floor, the bulk does, and it is the more coherent bin.
  - The Chern–Simons term (k ≥ 1) drives the cusp-heavy threads *below* their floor while the bulk stays above it.
- **So B1088's action is closed as the weight in both forms:**
  - as a real weight (SM-C16), it pulls the read-out into the bulk;
  - as a phase (here), interference keeps the bulk and cancels the cusp.

## The results against the sealed expectations

The bins are the cusp-heavy top 10 % (300 threads, mean time above height 3: 12.2 %) and the bulk bottom 50 % (1 500
threads, 0.5 %). The floor is the 95th percentile of each bin's coherence over 200 shuffles of the phases.

| | expectation (prior) | result |
|---|---|---|
| E1 | at σ ≤ 0.1 with k = 0, both bins coherent, C > 0.9 (80%) | **holds:** 0.98–1.00 in both |
| E2 | at σ ≥ 0.5, both bins at the floor (55%) | **fails at σ = 0.5 and 1.** Both bins stay above the floor, the bulk more: at σ = 1, cusp 0.21 against 0.13, and bulk 0.26 against 0.08. **Holds at σ = 2**, where both fall below it |
| E3 | for k ≥ 1 the CS term scrambles both bins at every σ (60%) | **fails.** It scrambles the cusp-heavy bin: at k = 2, σ = 0, it reads 0.15 against a floor of 0.49. The bulk stays above its floor for σ ≤ 1 (0.54 against 0.45) |
| E4 | the cusp-heavy bin never above its floor while the bulk is at it (60%) | **holds** at every k and σ: there is no localization on the cusp by interference |

**The controls:**
- C1: CS(LR) = −1.5 × 10⁻¹⁶ and Vol(LR) = 2.029883212819307, m004's.
- C2: at k = 0 and σ = 0, C = 1 in both bins.
- C3: the shuffled floor approaches 1/√n where the phases scramble. At σ = 2 it is 0.097 (1/√300 = 0.058) and 0.038
  (1/√1 500 = 0.026).

## A trap, said

- The card's "effective cusp share", |Σ e^{iφ} f₃| / |Σ e^{iφ}|, rises to 0.08–0.13 at σ = 1 and 2, against a uniform
  0.037.
- That is not localization. There the total coherence |mean e^{iφ}| is only 0.006 to 0.053, so the share is a ratio of
  two cancelled sums. The bins above, measured against their floors, show no cusp coherence.
- The share is read only where the total is coherent (σ ≤ 0.5). There it stays at 0.034 to 0.039, the uniform value.

## What it means for the critical path

- **Closed by this seat (SM-C16, SM-C17):** the record's own action as the weight on histories, in its real form and
  its phase form.
- **Open:** X-MEASURE (a measure from entropy, refinement or the pairs rule) and A2-AMP (the twisted η phase of B1929).
- **A pointer, not a claim:** the CS term is the part of the action that sees the hand, and it de-coheres exactly the
  cusp-heavy threads. A2-AMP's phase is also orientation-odd (η_A). If it behaves the same way, the orientation-odd
  phases favour the bulk, and the cusp would need something else.

## Files

`relays/sm_c17/run_c17.py`, `relays/sm_c17/c17_results.json`, `relays/sm_c17/RUN.txt`.
