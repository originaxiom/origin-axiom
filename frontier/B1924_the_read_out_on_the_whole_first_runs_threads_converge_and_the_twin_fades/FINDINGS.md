# B1924 — The read-out on the whole, first runs: the threads' averages settle as the history grows, and the dependence on the twin fades

*[UPGRADED 2026-11-14 to PROVED for the claims as corrected, on an independent second computation (harvest row 1790); see the section "Second computation, corrections and upgrade" below. This header is kept as written; Review 82, agy-exp's reading.]*

**Verdict: OPEN** (numerical evidence at the 10⁻² level; no limit is proved; an independent second computation is
owed). cc (main), 2026-11-13 to 14 (S306p). Values are written to the json files only, before any comparison; none is
printed, none is set beside a measured number, and no read-out is compared with any value of τ on record. **0 of 19.**

## 1. The answer first

- **The condition, written before any run** (`417a64e72`, register row P-845). The allowed words are those that keep
  the mark ±v at level 5: B1872's stabiliser. Each allowed word is a closed thread whose own line is the mark, so with
  the invariant end (B1921) the frame is periodic along its geodesic (B1922) and its thread average A(w) is canonical.
  **The read-out on the whole** is R = lim R_n, where R_n is the move-count average over allowed words of n moves (each
  letter L or R equally likely), each word's thread average weighted by its geodesic's length.
- **Instruments.**
  - **The channel norm** uses B1919's closed form (`fast_norm.py`). It equals the frame's own quadrature to 1.9 × 10⁻¹²,
    and the frame's outputs to 4 × 10⁻¹⁴. It is about 2 000 times faster, which is what makes the runs possible.
  - **The thread average** uses the trapezoid rule over one period, which converges spectrally because the integrand is
    periodic (B1922).
  - **Ratios, not log ratios, are averaged.** Along the golden period the smallest log ratio reaches −8.7: a near-zero
    singular value gives the log an integrable singularity.

  | quadrature check (`convergence.py`, `run6_convergence.py`) | ratios averaged | log ratios averaged |
  |---|---|---|
  | golden thread, 32 against 64 nodes | 1.2 × 10⁻⁴ | 1.8 × 10⁻² |
  | golden thread, two windows at 64 nodes | 2.9 × 10⁻⁵ | 6.6 × 10⁻³ |
  | the run of 6, 128 against 192 nodes; two windows | 5.7 × 10⁻⁴; 1.5 × 10⁻³ | — |

- **Three runs** (fixed seeds; every thread at 30 nodes per unit of length, at least 64):
  1. n = 8 to 16 in steps of 2, 20 words each (`whole_average.py`). R_n's sampling error, a jackknife over words, is
     2.5 to 4.4 × 10⁻². Its largest change between successive n is 5.4 to 7.3 × 10⁻², the size two such errors make.
  2. n = 10 and 16, 60 words each, every word read at the mark (2/5, 4/5) and at its twin (1/5, 2/5)
     (`whole_average_2.py`).
  3. n = 22, 60 words, at the mark and at the twin (`whole_average_3.py`). The largest sampling error is 1.2 to
     1.4 × 10⁻².
- **The comparisons** (`twin_compare.py`). Each compares the read-out's 48 numbers one by one: the frame's 20 outputs,
  at both ends and both covariant readings. Pure noise would give a median ∣z∣ of 0.67, with 5 % above 2:

  | comparison | median ∣z∣ | share above 2 | largest |
  |---|---|---|---|
  | the mark, n = 10 against 16 (independent words) | 0.78 | 4 % | 2.98 |
  | **the mark, n = 16 against 22** | **0.94** | **0 %** | 1.88 |
  | the twin, n = 10 against 16 | 0.85 | 12 % | 2.94 |
  | **the twin, n = 16 against 22** | **0.67** | **2 %** | 2.21 |
  | the mark against its twin at n = 10 (paired, the same words) | 2.35 | 58 % | 3.19 |
  | the mark against its twin at n = 16 (paired) | 0.92 | 4 % | 2.11 |
  | **the mark against its twin at n = 22 (paired)** | **0.57** | **0 %** | 1.77 |

- **So:**
  - **The read-out settles as the history grows.** From n = 16 to 22 it changes by no more than its sampling error,
    about 1.3 × 10⁻².
  - **The twin fades.** The read-outs at the mark and at its twin are clearly different at n = 10: 58 % of the 48
    numbers lie more than two errors apart, on the paired test. At n = 16 and n = 22 they cannot be told apart.

## 2. What this means, and what it does not

- **It is the first evidence that the read-out on the whole exists as a limit**, and that in that limit it does not
  depend on which of the two twins is read, to the resolution of these runs. If it holds, the condition named what it
  would remove: τ, and the choice of a reading point. Both are replaced by an average over the weave's own threads.
- **Not shown:**
  - The limit is not proved. The convergence is statistical, at about 10⁻², with 60 words and fixed seeds.
  - A drift below the sampling error is not excluded: the mark's median ∣z∣ from 16 to 22 is 0.94 against noise's 0.67,
    though none of the 48 is above 2.
  - How fast the twin's influence decays is not measured. Whether it vanishes in the limit, or only falls below
    10⁻², is not shown.
  - The end L̃ is still free. Both conventions of B1724 (L_max and L_2) are carried, not chosen between.
  - The weight is the condition's: words by the move count, threads by length. The alternative named in the condition
    (B1913's hyperbolic area) is not run.
    [2026-11-14, agy-exp's point, relayed by the author: weighting the words by length keeps the singular letter-count
    measure, because the lengths concentrate (Furstenberg's law). The hyperbolic area needs the closed geodesics
    ordered by length, and before that the frame's integrability at the four cusps of X₁(5). So this run is the
    principle's measure, (a), and only (a).]
  - The 48 numbers share one sample of words, so the shares above are indicative, not independent tests.
- **Before the record changes** (the budget's τ and reading point; A01, FL04), three things are owed:
  1. longer histories and larger samples;
  2. an independent second computation on a seat's own code: agy-002, on its page (M23), expectations committed first;
  3. the end L̃.
- **Nothing measured is read.** The read-outs are in the json files, written before any comparison was made. No count,
  rate or ratio is given a physical meaning here.

## 3. Mistakes made on the way and mended (disclosed)

- **The first quadrature was Gauss–Legendre.** It does not respect periodicity, and it left a window dependence of 0.1.
  It was replaced by the trapezoid rule.
- **The first averages were of log ratios.** Their singularities slow the convergence (the table in § 1). Ratios are
  averaged now.
- **The second run's printed statistic was coarse.** It is the median over 20 outputs of each output's largest component,
  for which noise gives about 1.5, not 0.67. This page reports every one of the 48 numbers.
- **The twins were first compared with unpaired errors.** They are read on the same words, so the right error is the
  paired jackknife of the difference. With it the conclusion is the same: 2.35 at n = 10 falls to 0.92 and then 0.57.

## 1a. Seen first

`VERDICT topic-sweep /read.out on the whole|thread average|move.count average|weave.s measure|twin fades/: 4 of 1663
arcs on main match (PROVED 4); 8 register rows match (QUEUED 8)`. Read for this arc:
- B1922: periodicity at the thread's own line.
- B1921: the invariant end.
- B1919: the closed form of the channel norm.
- B1872: the stabiliser.
- B1868 and B1913: the two weights named in the condition.
- B1912 and B1885: the golden state.
- P-776 and P-845.

**Literature:** the trapezoid rule's spectral convergence for periodic analytic integrands (standard); the jackknife
(standard).

## Files

- `verification/fast_norm.py`: the closed form against the quadrature.
- `verification/thread_average.py` (→ `thread_average.json`, `thread_average_run.txt`), `convergence.py`,
  `run6_convergence.py`: the thread average and its quadrature.
- `verification/whole_average.py`, `whole_average_2.py`, `whole_average_3.py` (→ their json and run files): the three
  runs. `twin_compare.py` (→ `twin_compare_run.txt`): the comparisons.
- The lock: `verification/test_b1924_read_out_on_the_whole.py`. It runs five tests in about 30 s, each with a planted
  case: the closed form against the quadrature (with the shift dropped it fails); a stored thread average recomputed from
  its word (a stored number changed by 10⁻⁶ is caught); the mark kept and refused; the twin's fading recomputed by the
  paired jackknife (a planted difference of three errors is caught); the golden ratio average's convergence.

## Reproduce

```
cd frontier/B1924_the_read_out_on_the_whole_first_runs_threads_converge_and_the_twin_fades/verification
python3 -B twin_compare.py && python3 -m pytest -q .
# the runs themselves (minutes to hours, single thread):
OMP_NUM_THREADS=1 python3 -B whole_average_2.py && OMP_NUM_THREADS=1 python3 -B whole_average_3.py
```

## Correction (2026-11-14, the same day): the two end values are chosen constants, not B1724's two ends

The runs hold the end at two fixed constants, 1.3 and 0.9, in the code's coordinate L + ½ log Im τ (B1921's L̃ plus
γ + log π). The code labels them "L_max" and "L_2". **They are not the values of B1724's two ends.** In that coordinate:
- the canonical cusp's L_max (B1667, the column Re τ = 1/4) runs from 0.69 at Im τ = 1 to 1.34 at Im τ = 4. It
  reaches 1.3 only near Im τ ≈ 3.7, far above the golden thread, whose geodesic stays below Im τ ≈ 1.12;
- its L_2 runs from 2.72 to 2.99, nowhere near 0.9;
- neither is constant in L̃: across B1667's 54 points the spread is 0.41 to 0.65 for L_max and 0.16 to 0.27 for L_2.
  So the canonical cusp does not fix the invariant end as one number.

**What changes.** § 2's sentence "Both conventions of B1724 (L_max and L_2) are carried, not chosen between" is
withdrawn. The runs are at two chosen values of the free end L̃. The conclusions stand at those two values: the
read-out settles in n, and the twin fades. Nothing here shows they hold at other values, or which value is right. The
end stays the read-out's free continuous input, as the condition and the author's reading both say. Owed: the same
comparisons at other values of L̃, including the canonical cusp's ends taken point by point along each thread (not
constant, so their periodicity along a thread must first be checked, B1922's condition).

## Addendum (2026-11-14): longer histories and a second independent sample

`verification/whole_average_4.py` (expectations in its docstring, written before the run) adds n = 28 (60 words) and a
second, independent sample at n = 22 (60 new words), each at the mark and the twin, with the same two end values.
`twin_compare_4.py` (→ `twin_compare_4_run.txt`):

| comparison | median ∣z∣ | share above 2 | expectation |
|---|---|---|---|
| (a) the two n = 22 samples, at the mark | 1.01 | 2 % | near 0.67: **partly met** |
| (a) the two n = 22 samples, at the twin | 0.66 | 0 % | met |
| (b) n = 22 (both samples pooled) against n = 28, the mark | 0.27 | 0 % | met |
| (b) the same, the twin | 0.34 | 0 % | met |
| (c) the mark against its twin at n = 28, paired | 0.38 | 0 % | met |
| the mark against its twin, the second n = 22 sample, paired | 0.49 | 4 % | met |

- **No change from n = 22 to 28**, and the twin is not told apart at n = 28.
- **At the mark, the jackknife error may understate the spread.** Two independent samples differ with median 1.01
  instead of 0.67. The error there may be too small by up to a half, so every "within errors" statement at the mark is
  to be read with errors half again as large. At the twin, the two samples agree as noise predicts.
- The verdict stays OPEN. Owed: agy-002's independent computation (M23 to M25). A proof of the limit is drafted
  by main, to be landed with its numerical test, which is running. The end question is now the canonical end (B1667),
  run separately.

## Second computation, corrections and upgrade (2026-11-14; agy-002's A2-B1924, harvest row 1790, read through the mask)

- **Confirmed, more strongly.** agy-002 computed the read-out on the whole by exhaustive exact populations, with no
  sampling error: every allowed word at n = 8 to 16 (5 453 hyperbolic words at n = 16). It used both of this arc's end
  values and a third of its own. The population read-out changes by 3.6 × 10⁻² from n = 8 to 10, 1.15 × 10⁻² from 10
  to 12, 6.8 × 10⁻³ from 12 to 14, and 3.6 × 10⁻³ from 14 to 16. From n = 22 to 28, with 400 words each, the change
  has median ∣z∣ 0.74, 92 % within two errors. It agrees with this arc's numbers within their errors.
- **Corrected: the twin does not "fade"; it is exactly equal at every n.** agy-002's theorem:
  - The reverse-swap involution w ↦ w* (reverse the word, swap L and R) gives W(w*) = W(w)ᵀ. It preserves length, and
    it maps allowed words to allowed words, because the mark's vector (1, 2) is null mod 5.
  - S W(w)ᵀ S⁻¹ = W(w*)⁻¹, so S carries w's thread onto w*'s. Under B1724's S-covariance the mark goes to the twin.
  - So A(w, mark) = A(w*, twin) for every allowed word, and the population read-outs at the mark and at the twin are
    **identical at every n**.
  The difference this arc saw at n = 10 came from samples that do not hold a word together with its dual. They were
  drawn with replacement: one sample of 60 held 41 distinct words, which this arc did not disclose and discloses now.
  What does fall with n is the word-by-word spread between the mark and the twin. §§ 1 and 2's sentences on the twin
  "fading" are superseded by this.
- **Withdrawn: the addendum's caution that the mark's jackknife errors may be understated by up to a half.** On the
  exact population at n = 16, agy-002 drew 2 000 pairs of 60-word samples. The jackknife error matches the true
  sampling spread to 1 % (median ratio 0.993), and the share above two errors is 5.1 %, the nominal rate. The median
  ∣z∣ of 1.01 between two samples is the fluctuation of a median over 48 outputs computed from one set of words.
- **Four conventions of the frame's code, now stated:**
  1. the theta pairings are evaluated at 2τ, with the real twist doubled;
  2. each residue is multiplied by √(max(0, 2πL̃ + F_u)) on the channel's characteristic;
  3. γ = Wᵀ on w = aτ + b, and the samples were drawn with replacement;
  4. the outputs are 48 numbers: 12 sector ratios and 12 mixing moduli at each of the two ends.
- **Verdict upgraded from OPEN to PROVED,** for the claims as corrected: the read-out on the whole at the two constant
  ends settles in n to the precision stated, on two independent computations, and the mark's and twin's population
  read-outs are equal at every n. The limit itself is B1928's (OPEN). The canonical end is B1927's.
