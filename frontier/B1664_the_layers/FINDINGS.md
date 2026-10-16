# B1664 — THE LAYERS: the sealed gate failed on the instrument's own cut-off; the read-outs say the sizes reach the constant wave and the amplitude's coherence decays, with the cusp, not the root, most coherent

**Verdict: OPEN.** The sealed gate L0 failed, so by the preregistration L1 and L2 are not results. They are read-outs.
The failure is the instrument's own: its cut-off set D to zero above height 50, and a thread whose sampling started
there gave a 0/0 period phase. A post-seal diagnosis (labelled) confirms it, and **B1665 re-seals the corrected test,
a scoreboard.** cc (main), 2026-10-16.
- Sealed `beaa42ff6` (sha256 20c39c08) before the run. The output was committed unread at `74165eaf4`: one run of
  188 s, exit 0, the instrument unchanged since the seal (sha256 75a15320).
- **0 of 19.** POINT_REGISTER P-183, steps 1–2.

## 0. Seen first

As sealed: `VERDICT topic-sweep /Duke|equidistribut|trace formula|cycle integral|period phase|layer average/: 2 of 1435 arcs on main match (NEGATIVE 1, PROVED 1)`
— B1633 and B1142. **Literature:** Bowen and Margulis; Duke (1988); Sarnak (1982); Hejhal; Katok–Sarnak (1993).

## 0b. Disclosed

- In full in the preregistration's §0b and §5. The root's cell was withdrawn before the seal (L⁹R out-coheres LR).
- **After the run:** one labelled diagnosis, `verification/after_the_seal/gate_diagnosis.py` with its output.

## 1. The sealed run (`verification/the_layers.py`, unchanged; `.json`, `_run.txt`)

| cell | prediction | result |
|---|---|---|
| **L0**, plumbing | layer sizes 1, 2, 2, 3 at t = 3–6; the period phase i^(#L−#R) on every thread to 10⁻⁶; finite; §8.3b's coherences | **FAILS:** sizes, finiteness and the four coherences hold (0.6368, 0.2435, 0.2592, 0.3211), but the phase check is NaN |
| **L1**, the constant wave | the top-quarter layer mean of ⟨f⟩ within 0.03 of 0.31500491 and closer than t ≤ 20 | **not a result** (the gate failed); read-out 0.3144 against 0.3692 |
| **L2**, no constant wave for the amplitude | the per-thread log–log slope of the phase-1 coherence negative by > 3 SE | **not a result**; read-out −0.269 ± 0.083 (7688 threads) |

## 2. The diagnosis (post-seal, labelled)

- **The NaN threads:** 593 of 30 674, every one starting above the cut, the lowest start at height 50.15. No other
  thread starts above it.
- **The rest:** on the other 30 081 threads the period phase equals i^(#L−#R) to 3.2 × 10⁻¹⁰.
- **The defect is the gate's rule, not the mathematics.** The rule asked for the phase on every thread but did not
  exclude starts in the region where the instrument sets D to zero. An E74 instance: a preregistered rule
  mis-derived, binding.

## 3. The read-outs (not results; B1665 re-tests them as a scoreboard)

- **The sizes reach the constant wave.**
  - The layer averages of ⟨f⟩ approach the typical motion's 0.31500491: 0.3144 over traces 451–600, against 0.3692
    over t ≤ 20.
  - Their distance from it falls as t^(−0.51 ± 0.05): the weave's layers, read by trace, come out at the wave side's
    constant.
- **The amplitude's coherence decays with length.**
  - Slope −0.269 ± 0.083, slower than random phase (−½).
  - The top-quarter mean is 0.285 against 0.444 at t ≤ 20.
  - A quarter of all threads (0.2508) are phase-1, as the character predicts.
- **The coherent rule favours the cusp, not the root.**
  - The cusp family L^(4m+1)R climbs toward 1: 0.285, 0.717, 0.861, 0.919, … 0.989 at word length 46, and 0.99994
    for the longest. LR stays at 0.637.
  - The coherent amplitude is carried by one passage deep in the cusp, the point where the defect f vanishes. Under
    coherent averaging the weave's own "nothing" end dominates.

## 4. What it does not show

- Any result for L1 or L2. That is B1665's.
- Any value of the Standard Model.

## 5. Credit

The reviewing agent before the seal found the root's cell false before the run.
