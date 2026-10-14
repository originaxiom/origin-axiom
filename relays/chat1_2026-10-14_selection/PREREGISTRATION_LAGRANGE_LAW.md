# The Lagrange law: in the thread frame, is a vacuum's hierarchy a function of its thread's height alone? Out-of-sample test on 57 new threads (chat1, 2026-10-14, evening). Sealed before any code that computes it.

**Why.**
- The thread frame (`FINDINGS_THREAD_FRAME.md`; sealed `0cf01ff11`, run `19417427e`) found on 12 threads (lengths 2–5)
  that the light-to-heavy ratios fall with the height of the thread's closed geodesic (TF5, ρ = −0.986).
- **Fitted after that run, on those 12 threads (stated here, before any new number):**
  - ln(m₂/m₃) = 7.1069 − 7.2941·y_max, with RMS residual 0.20 over 13 e-folds;
  - ln(m₁/m₃) = 5.9196 − 8.1172·y_max, with RMS 0.58.
- **A structural reading, also after that run.** y_max is half the thread's Lagrange (Markov) value: √5/2, √8/2, √12/2,
  √15/2, √21/2 and √32/2 on the threads seen.
  - If the law holds, the golden root, with Hurwitz's minimal value √5, is the least hierarchical vacuum.
  - The Markov threads (Lagrange value below 3) are mildly hierarchical, and the steep hierarchies need threads beyond 3.
- This seal tests the law where it has not been seen: every Lyndon word of length 6, 7 and 8 (57 threads).

**Instrument.**
- `thread_frame.py`'s construction, copied verbatim: the SM seat's W72 forms at `87cf7f551`, B1644's coupling, cycle
  integrals at the image in the fundamental domain, and masses from (K^{−½})ᵀ Y K^{−½}.
- Here N = 256 and N = 384.
- **Admission rule (precision).** A thread enters the cells only if y_max ≤ 3.0 and its two mass ratios agree between
  N = 256 and 384 to 10⁻⁵ relative. Above that height K's condition number passes about 10¹², beyond double precision.
  Excluded threads are listed.
- **Control.** The 12 old threads reproduce the sealed run's ratios to 10⁻⁶.

| | prediction (admitted threads) | prior |
|---|---|---|
| Q0 (control) | the 12 old threads reproduce `thread_frame.json`'s m₂/m₃ and m₁/m₃ to 10⁻⁶ relative | 97% |
| LL1 | Spearman(y_max, ln m₂/m₃) < −0.9 over all admitted threads, old and new | 80% |
| LL2 | the sealed fit 7.1069 − 7.2941·y_max predicts ln(m₂/m₃) on the new admitted threads with RMS residual < 1.0 | 55% |
| LL3 | the golden root LR has the largest m₂/m₃ of all admitted threads | 85% |
| LL4 | every admitted thread with y_max < 1.5 (the Markov threads: Lagrange value below 3) has m₂/m₃ > 0.01, and every admitted thread with y_max > 2 has m₂/m₃ < 10⁻³ | 60% |
| LL5 | the sealed fit 5.9196 − 8.1172·y_max predicts ln(m₁/m₃) on the new admitted threads with RMS < 1.5 | 45% |

**Read-outs (no prior).**
- Per thread: y_max, Vol and CS (from the root-share check's data), both ratios, and which mode is heaviest.
- The fit on all admitted threads.
- The residuals against word length, syllable count, |CS| and amphichirality.
- Pairs of distinct threads with equal y_max (to 10⁻⁶): their ratios.
- The Markov threads found, LLRRLR and LLRRLRLR among the expected.

**What a result means, fenced.**
- **If LL1–LL4 hold**, then in the thread frame a vacuum's hierarchy is fixed by one number, its thread's Lagrange
  value. The golden root, the worst-approximable axis (Hurwitz), is the least hierarchical vacuum.
- B990's law then has a Diophantine form: symmetry is good approximability's opposite, and hierarchy is the excursion
  that a large partial quotient makes toward the end.
- **Not tested.** H-thread itself; other weights or representations; sectors; mixing; which thread is the vacuum.
- No value. **0 of 19.**
