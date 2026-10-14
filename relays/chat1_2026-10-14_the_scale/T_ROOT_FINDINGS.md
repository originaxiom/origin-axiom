# T-ROOT: at c = 6 the weave is a plurality that sees k; it becomes its root only at c of order 10²

chat1, 2026-10-14. This check puts numbers on the tension stated in `THE_SCALE.md` §5.
- **Sealed** at `13d31f042` (sha256 3fd25436…) before any code.
- **The script** `t_root.py` was committed at `fc82fe02a` before its one run. Its output is `t_root_run.txt`,
  `t_root.json` and `t_root_threads.json` (`f8fe26015`). The run took 90 s.
- The c = 6 shares were recomputed from the saved threads by a separate snippet, and agree to four digits.
- **Every cell held as sealed. 0 of 19.**

## Scored

| | prediction | prior | outcome |
|---|---|---|---|
| Q0 (control) | lengths ≤ 12 reproduce the earlier check; all 31,040 geometric; Guéritaud–Futer holds | 97% | **HOLDS.** 745 of 745 reproduced; 0 non-geometric; 0 violations |
| Q1 (control) | p(c) increasing under all three weights | 99% | **HOLDS** |
| T1 | p(6) under (A) 2^{−n} in [0.15, 0.40] | 80% | **HOLDS: 0.274** (with the tail bound, [0.264, 0.274]) |
| T2 | p(6) under (B) 3^{−n} in [0.35, 0.65] | 75% | **HOLDS: 0.502** (the tail is negligible) |
| T3 | p(6) under (C), per-length uniform, in [0.50, 0.80] | 70% | **HOLDS: 0.660** (with the tail, [0.615, 0.660]) |
| T4 | chiral share at c = 6 under (A) above 0.5 | 85% | **HOLDS: 0.659** |
| T5 | N_eff(6) under (A) at least 5 | 85% | **HOLDS: 32.4** |
| T6 | c_{0.99} in [80, 250] under all three | 80% | **HOLDS: 137.6 (A), 125.3 (B), 105.3 (C)** |
| T7 | c_{0.5} under (A) in [10, 40] | 75% | **HOLDS: 19.1** |
| T8 | tail bound below 1% of Z at c = 6 under (B) | 90% | **HOLDS: 3.1e-6 against Z ≈ 0.116** |

## The table

Root share p, chiral share f and effective number of threads N_eff.

| c | (A) p | (A) f | (A) N_eff | (B) p | (B) f | (B) N_eff | (C) p | (C) f | (C) N_eff |
|---|---|---|---|---|---|---|---|---|---|
| 2 (σ = 1/3) | 0.176 | 0.746 | 136 | 0.436 | 0.509 | 9.5 | 0.584 | 0.375 | 8.2 |
| **6 (σ = 1, L154)** | **0.274** | **0.659** | **32.4** | **0.502** | **0.457** | **6.6** | **0.660** | **0.312** | **4.7** |
| 24 | 0.564 | 0.417 | 5.2 | 0.709 | 0.281 | 3.0 | 0.830 | 0.165 | 2.1 |
| 64 | 0.875 | 0.125 | 1.7 | 0.919 | 0.080 | 1.4 | 0.958 | 0.042 | 1.3 |
| 128 | 0.986 | 0.014 | 1.09 | 0.991 | 0.009 | 1.06 | 0.995 | 0.005 | 1.03 |
| 256 | 0.9998 | 0.0002 | 1.00 | 0.9999 | 0.0001 | 1.00 | 0.9999 | 0.0001 | 1.00 |

- Thresholds for (A): c_{0.5} = 19.1, c_{0.9} = 70.7, c_{0.99} = 137.6.
- For (B): 5.9, 57.5, 125.3.
- For (C): p(0) is already 0.53; c_{0.9} = 39.2, c_{0.99} = 105.3.

**Read-outs.**
- **Composition.** Of the 31,040 threads, 514 are amphichiral (CS = 0) and 30,526 are chiral.
- **The heaviest threads at c = 6 under (A).** LR 0.274. LLR and LRR 0.112 each. LLLR and LRRR 0.050 each. LLRR 0.041.
  LLLLR and LRRRR 0.024 each. LLLRR and LLRRR 0.017 each. The mirror pairs carry equal weight and opposite CS.
- **Per-length sums at c = 6** fall by a factor of about 0.74 per letter under (A), and 0.49 under (B).
- **The level's footprint at c = 6 under (A).**
  - Defined as 1 − Re Z(k)/Z(0), with the phase e^{2πi·k·CS/π²}. This convention was chosen at the seal; the factor
    between SL(2) and PSL(2) normalisations is not settled.
  - Values: 0.076 at k = 1, 0.26 at k = 2, 0.48 at k = 3, 0.66 at k = 4. From k = 6 on it lies between 0.83 and 0.88.
  - So the weave's weighted sum depends on the level at order one.

## What it shows

1. **At L154's candidate, c = 6, the weave is a plurality, and it sees k.** **[MATH, given the weights]**
   - Under the maximal-entropy weight (A), the root is about a quarter of the weave, N_eff ≈ 32, and two-thirds of
     the weight is chiral.
   - Under steeper weights the root is half (B) or two-thirds (C), with N_eff between 5 and 7.
   - In every case a large share is chiral, and the weighted sum depends on the level at order one.
   - So B1228's "k = 1 by inventory" is not a free relabelling there.
2. **The weave becomes its root only at c of order 10².**
   - The root reaches 99% only at c ≈ 105 to 138, depending on the weight.
   - That is two orders of magnitude above L154's 6. It is also fourteen orders of magnitude below the c ~ 10¹⁶ that a
     3D version of the observed hierarchy would need (`THE_SCALE.md` §7).
3. **The three readings, placed.** **[READING]**
   - **"Existence is the weave of all allowed threads, not one object like m004"** (the owner). This holds as a
     plurality only for c of order 1 to 10. There the classical weight spreads over many threads, mostly chiral.
   - **L154's c = 6** sits inside that regime. The weave framing and L154 are consistent with each other.
   - **"The threads are classical spaces"** (chat1's field note) needs c ≫ 1, and at c ≳ 10² the weave reduces to m004.
     That is the odd reading out.
   - So if existence is the weave, 3D space is not classical: it is a quantum plurality of geometries, with no
     hierarchy in 3D. The observed hierarchy then has to come from the 4D crossing, which is not posable yet.
4. **One caution.** At c of order one the classical weight is not the quantum weight: one-loop and higher terms are of
   order one. These numbers say where the classical weight puts the weave, not what the quantum weave is.

## Fence

- **Object.** Threads to length 18. Three word weights, none fixed by the record: B1629's uniform measure is per length.
  Classical action weight. Reach: *members*, up to length 18, with rigorous tail bounds for (A) and (C) and a
  negligible tail for (B).
- **Not tested.** The quantum weave; any c fixed by anything; L154's bridge; H-RES; any 4D statement.
- No value. **0 of 19.**
