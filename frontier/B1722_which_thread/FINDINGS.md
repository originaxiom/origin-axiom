# B1722 — WHICH THREAD? (the completion map's C2, P-285): NEGATIVE AS SEALED — NEITHER OF THE RECORD'S MEASURES OVER THREADS SELECTS THE DATA'S THREAD; BOTH CONCENTRATE ON SHORT THREADS WHOSE APEXES SIT TOO LOW FOR A HIERARCHY

**Verdict: NEGATIVE as sealed (W1 and W2 fail), as the preregistration expected.** cc (main), 2026-10-22. Sealed
`a9a5d46f9` (sha256 120707ad) before its instrument ran. The output was committed unread at `7f5b6f599` and read once.
**0 of 19.**

## 1. The result

The rows are B1720's stored output, its sha256 pinned. The statistic is E_μ(t) = Σ_k μ(k) ln f_k(t), the
measure-weighted mean log-misfit of a thread drawn from μ, with f_k a class's best worst factor.

| cell | the measure | E_μ(data) | random median | fraction of 4 000 random hierarchies as good | result |
|---|---|---|---|---|---|
| **W1** | μ_U, the weave's uniform word measure (B1629): n·2⁻ⁿ per class of length n | 3.85 | 4.62 | **25.4%** | **FAILS** (bar 1%) |
| **W2** | μ_A, the action weight at L154's c = 6: e^{−Vol/π} | 3.04 | 3.77 | **21.0%** | **FAILS** |

**Where the measures put their weight.**
- **μ_U:** LR 7.6%, LLR and LRR 5.7% each, then LLLR, LLRR and LRRR. Their best factors are 4 506, 198, 198, 34, 444
  and 34.
- **μ_A:** the same short threads lead, but the measure is nearly flat. Volumes run from 2.03 (LR) to 8.82
  (computed after the read), and e^{−Vol/π} decays slowly, so LR carries only 2.7%.
- **The best class L⁵RLR²** (volume 6.548) carries 0.27% of μ_U and 0.65% of μ_A.
- **P_μ(f ≤ 2):** 1.1% under μ_U and 2.6% under μ_A.

## 2. What it means

**Read as written before the run** (both fail): the record's measures do not select the data's thread.
- Both favour short threads, whose apexes (Im τ ≈ 1.1–2.3) sit too low for the frame's hierarchy.
- The selection therefore needs a measure not on record, or a principle beyond the measure (P-139).

**With B1720, the picture is sharp.**
- A thread fixes the point. The apex is its natural point. Some thread comes within 1.80 of all six ratios.
- But neither the weave's uniform measure nor the action weight at c = 6 prefers that thread over random-hierarchy
  fitters.
- Nature's thread, if the frame is right, is a high-run thread of length about 9 (runs 5, 1, 1, 2). The record's measures
  weight such threads at under 1%.

**What it does not do.**
- Other measures: the SM seat's W57 invariant measure, other c, measures on longer words.
- A dynamics other than the walk. The walk's limit point (C4) reduces to W1 (§3).

## 3. After the read (labelled): the walk's limit point reduces to W1 (the completion map's C4, P-286)

C4 asked for a rule that reads a thread from the pull-back walk's limit point (B1662, B1663).
- **The check** (`verification/after_the_read/walk_digits.py`; 3 000 walks at each strength, seed 1722). The limit's
  continued-fraction digits are i.i.d. with P(k) = 2⁻ᵏ at p = 0 and at p = ½: marginals 0.498, 0.251, 0.126, 0.063 and
  0.499, 0.251, 0.125, 0.063. Consecutive digits are independent to 0.003 and 0.001.
  - At p = 0 this is exact by construction. B1663 had read the marginals only, not the independence.
- **So the limit is a uniform random infinite word.** A window of length n is any given word with probability 2⁻ⁿ, and
  a thread read from the limit is drawn from the uniform measure, W1's μ_U.
- **The uniform measure is flat within a length.** Every primitive class of length n carries n·2⁻ⁿ. Among the census's
  54 classes of length 9, L⁵RLR² has the same weight as each of the other 53.
  - Even a length rule that put all its weight on length 9 would give it 1/54 (1.9%).
- **C4 is therefore not a separate selection.** The walk can select at most a length, never a thread within it, and with
  the census's length weighting it is W1, which failed.

## Seen first

`VERDICT topic-sweep /measure over threads|uniform measure|action weight|c ?= ?6|root share|which thread|thread weight/ (full text, aliases: the weave's measure): 33 of 1493 arcs on main match (NEGATIVE 5, OPEN 4, PROVED 24)`. Bearing on it:
- B1629 (the uniform measure's run statistics);
- B1088 and B1015 (L154's c = 6σ);
- the web seat's root-share check (the weights favour the root);
- B1720 (the census and its best class).

**Literature:** none beyond the record.

## Disclosed

- **As sealed:**
  - B1720's full read-out was known;
  - the measures are the record's;
  - the expected direction was stated before the run.
- **After the run, before the read:** the run log's two lines of SnapPy's tkinter import warning, which carried an
  absolute path, were removed by pattern.

## Files

- `PREREGISTRATION.md` (sealed) and `ARTIFACT_HASHES.txt`.
- `verification/which_thread.py` → `which_thread.json`, `which_thread_run.txt`.
- After the read (labelled): `verification/after_the_read/walk_digits.py` → `walk_digits.json`.
- The lock: `tests/test_b1722_which_thread.py`.
