# SM-C16 — the record's action as the weight: with its own sign it pulls the read-out into the bulk

*The SM seat, 2026-11-15. Card `relays/cards/SM_C16_the-records-action-as-the-weight.md`, sealed and pushed at
338a29610 before the run. Value-free and data-free: no frame output and no measured number was computed, only the
threads' volumes, syllables and heights.*

## The answer

- **B1088's action, S = −Vol·σ, weighted as e^{−S} = e^{+σ·Vol}, moves the read-out out of the cusp at every σ > 0.**
  So it cannot be the principle that gives the cusp its weight (B1944's wall), and item 2 of this seat's proposal is
  closed for B1088's action with its sign.
- **The mechanism is the one derived on the card.**
  - On B1928's 3 000 threads, the volume rises with the number of syllables: Spearman 0.85.
  - The volume falls with the longest run: −0.77.
  - The cusp time falls with the volume: −0.93 above height 2, and −0.81 above height 3.
- **The opposite sign, e^{−σ·Vol}, moves the read-out into the cusp.** At σ = 0.5 the time above height 3 rises from
  3.7 % to 10.7 %. Whether the record has a reason for that sign is the next question, and it is not answered here.

## The results against the sealed expectations

| | expectation (prior) | result |
|---|---|---|
| E1 | Spearman(Vol, f_Y) < 0 for Y = 2, 3, 6 (85%) | **holds:** −0.93, −0.81 and −0.03. The last is negative but negligible: above height 6 almost every thread reads 0 (the uniform mean is 0.04 %) |
| E2 | the record's sign lowers ⟨f_Y⟩ for every σ > 0 and Y, by > 3 jackknife errors at σ ≥ 0.2 (75%) | **holds:** at σ = 0.2 the shifts are −31, −31 and −16 errors, and they grow with σ. Above height 3, the time falls from 3.7 % to 1.1 % at σ = 0.5 |
| E3 | the opposite sign raises it, likewise (75%) | **holds at Y = 2 and 3** (+25 and +18 errors at σ = 0.2). **Fails the bar at Y = 6** for σ = 0.5 and 1 (2.7 and 2.0 errors): too few threads ever reach that height for the jackknife to resolve it |
| E4 | Vol is tracked better by the syllables than by the longest run (80%) | **holds:** 0.85 against 0.77 in absolute rank correlation |

**The controls:**
- C1: SnapPy's Vol(LR) = 2.029883212819307, m004's.
- C2: σ = 0 returns the uniform mean exactly.
- C3: shuffling the volumes among the threads moves every mean by less than one error (0.7, 0.1 and 0.7).

## What this does and does not settle

- **Settled:** the real weight e^{−S} built from the record's action favours the bulk, at every value of its one unit
  σ. The run computed no frame value, so this is a statement about where the read-out looks, not about the values it
  would give.
- **Not settled, and not claimed:**
  - The weight as a phase, e^{iS} = e^{−iσ·Vol}. Here B1088's action would enter as interference, not suppression.
    Whether that phase localizes is A2-AMP's kind of question, and it is not computed here.
  - Whether a cusp-favouring weight would give frame C the measured hierarchy. Answering that needs a sealed values
    card, and none is proposed before the weight is derived.
- **For the proposal:** of its two weight items, the record's action with its own sign is now out as a real weight.
  X-MEASURE and A2-AMP remain the live candidates, and so does the phase form above.

## Files

`relays/sm_c16/run_c16.py`, `relays/sm_c16/c16_results.json`, `relays/sm_c16/RUN.txt`.
