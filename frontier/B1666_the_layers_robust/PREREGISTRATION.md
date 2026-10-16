# B1666 — THE LAYERS WITH A ROBUST PHASE (a scoreboard: B1664's and B1665's read-outs were seen; their gates failed at D's two zeros): preregistration

cc (main), 2026-10-16. POINT_REGISTER P-183, steps 1–2, after B1664 and B1665 (both OPEN). 0 of 19.

- **The question:** B1664's, unchanged. Every thread to trace 600; the sizes against the constant wave (L1); the
  amplitude's coherence against length (L2).
- **Why a third seal.**
  - B1664's gate took the period phase as a ratio at one point, which became 0/0 where the instrument sets D to zero in
    the cusp (593 threads).
  - B1665 moved the start to the period's lowest point, which is ω, where D also vanishes (22 threads, up to
    3.7 × 10⁶).
  - Both diagnoses found the mathematics right everywhere. B1665's showed that the least-squares phase over a whole
    period is right on all 30 674 threads, to 1.4 × 10⁻⁸.
- **The one change.** The period phase is now Σ g(s + ℓ)·conj g(s) / Σ∣g(s)∣², over two consecutive periods. No zero
  of D can spoil it, because the period always spends time where D ≠ 0. ⟨f⟩ and the coherence are computed over the
  first period as before.
- **A scoreboard.** L1 (0.3144 against 0.3692) and L2 (−0.269 ± 0.083) were seen twice, identically.

## 0. Seen first

As B1664 (`VERDICT topic-sweep /Duke|equidistribut|trace formula|cycle integral|period phase|layer average/: 2 of 1435 arcs on main match (NEGATIVE 1, PROVED 1)`),
plus B1664 and B1665, read in full. **Literature:** as B1664.

## 0b. Disclosed

- B1664's and B1665's runs and diagnoses, above.
- **A smoke test of this instrument on the guard regions:** LR⁵⁹⁸ in the deep cusp (phase error 1.7 × 10⁻¹¹), two
  words through B1665's worst near-ω starts (3.0 × 10⁻¹⁰ and 3.0 × 10⁻¹²), LR, LLRR.
- **The reviewing agent before the seal,** asked to try the zeros: §4.

## 1. The cells

| cell | prediction | kind |
|---|---|---|
| **L0**, plumbing | layer sizes 1, 2, 2, 3; the least-squares period phase i^(#L−#R) on **every** thread to 10⁻⁵ (a wrong phase misses by at least ∣1 − i∣ = 1.41); every value finite; no failed thread; §8.3b's four coherences to 5 × 10⁻³ | gate |
| **L1**, the constant wave | the top-quarter layer mean of ⟨f⟩ within 0.03 of 0.31500491, and closer than the mean over t ≤ 20 | scoreboard |
| **L2**, no constant wave for the amplitude | over the phase-1 threads with t ≥ 10, the slope of log(coherence) against log(length) is negative by more than 3 SE | scoreboard |
| read-outs | as B1664's | — |

**If L0 fails, nothing after it is read as a result.**

## 2. What it would mean

As B1664's §3. A scoreboard: the meaning is unchanged, and the results become sealed rather than read.

## 3. Files

`verification/the_layers_robust.py`, with `.json` and `_run.txt` after the run.

## 4. The reviewing agent before the seal

One read-only pass, told to try the zeros. **No blocker.**
- **The grid:** the two periods pair exactly (n·ds = ℓ).
- **The cusp threads:** L⁵⁹⁸R, LR⁵⁹⁸, L⁵⁹⁷R and L⁵⁹⁰R have phase errors from 1.7 × 10⁻¹¹ to 2.6 × 10⁻⁸.
- **The square root's branch:** no flip in about 2900 threads, including all 1110 with trace ≥ 560 and twelve or more
  leading L.
- **Precision:** the worst error is 1.1 × 10⁻⁷, on L-run words near trace 598, with about 9× margin to the drafted
  10⁻⁶.
- **Taken:** the gate is moved to 10⁻⁵ before the seal, on that measurement. A wrong phase would miss by at least
  1.41.
- **Runtime:** about 3–5 minutes.
