# B1665 — THE LAYERS, RE-SEALED WITH THE GATE REPAIRED (a scoreboard: B1664's read-outs were seen): preregistration

cc (main), 2026-10-16. POINT_REGISTER P-183, steps 1–2, after B1664 (OPEN: its gate failed on the instrument's own
cut-off). 0 of 19.

- **What is re-tested.** B1664's question and cells, unchanged: every thread to trace 600; the sizes against the
  constant wave (L1); the amplitude's coherence against length (L2).
- **What is repaired, the one change.** Each period's sampling now starts at its lowest point in the reduced domain,
  chosen from 64 candidates. It never starts above height 50, where the instrument sets D to zero. In B1664, 593
  threads started there, and their period phase was 0/0.
  - For phase-1 threads the coherence and ⟨f⟩ do not depend on the start (the integrand is periodic).
  - The phase check is a ratio over one full period, so it does not depend on the start either.
- **A scoreboard.** B1664's read-outs were seen: L1 0.3144 against 0.3692; L2 −0.269 ± 0.083; the cusp family's
  coherences. The cells below are predicted to hold as those read-outs say.

## 0. Seen first

`VERDICT topic-sweep /Duke|equidistribut|trace formula|cycle integral|period phase|layer average/: 2 of 1435 arcs on main match (NEGATIVE 1, PROVED 1)`
(B1664's sweep), plus B1664 itself, read in full. **Literature:** as B1664 (Bowen, Margulis; Duke; Sarnak; Hejhal;
Katok–Sarnak).

## 0b. Disclosed

- **B1664's run and its diagnosis.** The read-outs above; 593 NaN threads, all starting above the cut; the phase
  i^(#L−#R) to 3.2 × 10⁻¹⁰ on the other 30 081.
- **A smoke test of this instrument:** the deep cusp thread LR⁵⁹⁸ (phase error 1.4 × 10⁻¹¹, finite) and LR
  (0.6368).
- **No reviewing agent.** The change is the start point alone, in an instrument that was reviewed before B1664's seal.
  This is said here rather than hidden.

## 1. The instrument (`verification/the_layers_resealed.py`)

B1664's instrument with the repaired start point and its own output names. Otherwise identical: the enumeration, the
amplitude carried with the Higgs's character, the cut-off, the fits, eight workers, single-threaded BLAS.

## 2. The cells

| cell | prediction | kind |
|---|---|---|
| **L0**, plumbing | layer sizes 1, 2, 2, 3 at t = 3–6; the period phase i^(#L−#R) on **every** thread to 10⁻⁶; every value finite; no failed thread; §8.3b's four coherences to 5 × 10⁻³ | gate |
| **L1**, the constant wave | the top-quarter layer mean of ⟨f⟩ within 0.03 of 0.31500491, and closer than the mean over t ≤ 20 | scoreboard (seen: 0.3144 against 0.3692) |
| **L2**, no constant wave for the amplitude | over the phase-1 threads with t ≥ 10, the slope of log(coherence) against log(length) is negative by more than 3 SE | scoreboard (seen: −0.269 ± 0.083) |
| read-outs | as B1664's, with the most coherent phase-1 thread and the cusp family | — |

**If L0 fails, nothing after it is read as a result.**

## 3. What it would mean, and not

- **Meaning:** as B1664's §3.
  - The sizes come out at the constant wave by layer.
  - The amplitude has no constant wave, so coherent averaging suppresses long threads.
  - The coherent rule favours the cusp family over the root (a read-out).
- **What it does not mean:** no Standard Model value, and a scoreboard, not a blind test.

## 4. Files

`verification/the_layers_resealed.py`, with `.json` and `_run.txt` after the run.
