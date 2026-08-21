# V1 — value-campaign cell V-1: extending the Kashaev-tower arithmetic to C_3 (and C_4)

Standalone bench (mpmath only, no repo imports), reusing the APPROACH of the banked
`frontier/B1120_L180_makeorbreak/b1120_verify.py` (verdict PROVED there: C_0, C_1, C_2
confirmed as trace-field arithmetic). This bench pushes the same computation ~12x further
in N (banked ceiling N≈2.9M → this run's ceiling N=35,000,000) specifically to try to close
the precision gap that left C_3 open (11 trusted digits banked; ~17-18 needed to search
confidently at the height the C_1/C_2 pattern suggests), and takes a first look at C_4.

## THE PREDICTION — stated before any PSLQ call (per the task's own requirement)

`J_N(4_1) = sum_{k=0}^{N-1} prod_{j=1}^k 4*sin^2(pi*j/N)` is manifestly real (nonnegative
summands). Given the standard WKB/resurgence parametrization (coefficients in the trace
field `Q(sqrt(-3))` multiplying `(2*pi*i/N)^k`), reality forces a parity law, already
confirmed at k=0,1,2 (banked):

```
k even  ->  C_k / (C_0 * pi^k)  is a PLAIN RATIONAL
k odd   ->  C_k / (C_0 * pi^k)  is a RATIONAL MULTIPLE of sqrt(3)
```

Applied to the two new targets:

- **C_3 (k=3, ODD) — predicted:** `C_3 = q3 * sqrt(3) * pi^3 * C_0`, q3 ∈ ℚ
- **C_4 (k=4, EVEN) — predicted:** `C_4 = q4 * pi^4 * C_0`, q4 ∈ ℚ

with denominators expected (a prior stated for the record, not a search constraint) to be
{2,3}-smooth by analogy with 108 = 2²·3³ (C_1) and 7776 = 2⁵·3⁵ (C_2).

**Anti-coincidence controls run alongside the predicted-basis search** (not after, not
cherry-picked): C_3 tested against plain-rational·π³ (wrong parity: Q not Q(√3)); C_4
tested against rational·√3·π⁴ (wrong parity: Q(√3) not Q); both tested against √3-alone,
1/√3, π², and the "1" base (wrong power of π / no π at all).

## A base-labeling subtlety caught before trusting anything (told in full)

The candidate-base sweep tests a fixed base B at order k via `B^k`, against BOTH the Q and
Q(√3) bases — this is standard (matches the banked bench) and re-derives the SAME
underlying relation from multiple algebraically-related bases (`pi`, `2pi`, `pi/sqrt3`,
`pi*sqrt3`, `4pi`, ...). Writing an automatic classifier for "did this hit match the
predicted parity" is easy to get wrong, and a first attempt here (`(k%2) XOR
base_sqrt3_parity`) WAS wrong — caught by hand-verifying against C_1/C_2 (whose closed
forms are already banked ground truth) before trusting the classifier on the new C_3/C_4
targets:

- For **C_1** (k=1) against base=`pi/sqrt3`: predicted T = C_1·√3/(C0·π) = (11/108)·3 =
  **11/36**. PSLQ found relation `[36,-11]` → T=11/36. Exact match — this base flips Q(√3)
  → Q because it *itself* carries a √3 factor, not because the underlying relation changed.
- For **C_2** (k=2) against base=`pi/sqrt3`: predicted T = C_2·3/(C0·π²) = (697/7776)·3 =
  **697/2592**. PSLQ found relation `[-2592,697]` → T=697/2592. Exact match — and this
  is the case that broke the first (XOR) classifier: for EVEN k, `sqrt(3)^{m*k}` is
  rational for ANY integer m (since m*k is always even), so the expected basis is **Q for
  every base, regardless of the base's own √3 content** — not a XOR of the two parities.

Corrected rule (`expected_basis_kind` in `V1_verify.py`, derived and commented in full
there): k even → always Q; k odd → Q(√3) if the base has no intrinsic √3 factor, Q if it
does (an even number of √3 factors cancels). Re-verified: with the fix, **every** C_1/C_2
hit across all 7 algebraically-related bases classifies as `matches_prediction=True`, zero
false "parity-violating" flags — this is the pipeline reproducing two pieces of already-
known ground truth exactly, the sanity check that earns trust in the same machinery being
pointed at the unknown C_3/C_4.

## Method (reusing the banked bench's approach; both of its bugs avoided by construction)

1. **Precision-context ordering** (the banked bench's bug #1): Vol and all "exact"
   constants (p=3/2, growth_rate=Vol/2π, C0_target=3^-1/4) are frozen at DPS_VOL=400 with a
   unary `+`, then passed onward as ~410-digit decimal STRINGS to every consumer — including
   every multiprocessing worker (a fresh process with its own mpmath context) — so every
   downstream use rounds DOWN from a fully-accurate value, never up from something computed
   by accident at mpmath's default dps=15. `mp.mp.dps` in the main process is not lowered
   until after this freeze.
2. **Monomial ill-conditioning** (bug #2): every polynomial-in-1/N fit uses the rescaled-
   Chebyshev basis, never raw monomials in 1/N.
3. **J_N** via the fast angle-addition recursion, cross-validated against a direct
   per-term `mp.sin()` path and hand-derived exact integers (N=1..4 → 1,5,13,27).
4. **Parallelization (new relative to the banked bench):** J_N(N) for different N are
   independent, computed via a `multiprocessing.Pool`. Calibrated on this machine before
   committing to the grid: single-process ≈84,000 steps/sec; 6-way parallel ≈336,000
   steps/sec (measured on synthetic N=300,000 batches). NWORKERS defaults to 6 (of 16
   logical / 8 physical cores) rather than claiming the whole machine — `ps aux` showed
   this is a shared machine (other sessions' `pytest -q` and a long-running `chartab.py`
   were both active at the time of this run).
5. **Windows W1..W5** (N from 2,000 to 35,000,000 — roughly **12x** the banked run's top N
   of 2.9M) + a POOLED fit, K up to 9 per window (16 pooled), read for within-window
   K-convergence and cross-window agreement — "trusted digits" = min of the two, over the
   GENUINE windows only (POOLED is their union, used as the best-precision value SOURCE,
   not as independent evidence).
6. **Precision-doubling** (dps 200 → 320) on the W4 subset.
7. **PSLQ sweep**: C_1, C_2 re-verified (continuity control against the banked closed
   forms — see above) and C_3, C_4 (the new targets), against the same 11-base family the
   banked bench used, `maxcoeff` swept up to 3,000,000 (banked bench went to 100,000; raised
   here because the C_1→C_2 height jumped ~20-70x, so C_3's height could plausibly need a
   higher ceiling to find).

## Results

**Run**: N up to 35,000,000 (≈12× the banked ceiling of 2.9M), dps=200 main / dps=320
cross-check, 6-way parallel, 1769s (29.5 min) total — well inside the ~60 min compute
budget. All controls passed (hand-check N=1..4 exact; fast-vs-direct agreement ~1e-198 to
1e-201; C_0 recovery |diff|=1.16e-17 against target).

**C_0, C_1, C_2 — re-verified, more precisely than before.** All three reproduce the
banked closed forms exactly, now to far more digits (C_0: 27 trusted digits, C_1: 23, C_2:
18 — vs the banked bench's 25/20/15), and the PSLQ sweep re-finds `C_1 = (11/108)·√3·π·C_0`
and `C_2 = (697/7776)·π²·C_0` cleanly on every one of the 7 algebraically-related bases,
**zero** parity anomalies, zero wrong-pi-power hits. This is the pipeline reproducing two
pieces of independently-known ground truth exactly — the sanity check that earns trust in
the same machinery pointed at C_3/C_4.

**C_3 — two layers of evidence, reported honestly as two layers, not collapsed into one:**

*Primary (pre-registered) metric — all genuine windows including W1:* trusted digits = 14
(up from the banked bench's 11; still short of the 17-digit gate). Taken alone, this run's
`V1_verify.py` verdict field reads **PRECISION-FLOOR**, and that field is left as computed
— it is not edited after the fact.

*Why that floor is worth looking past (not a re-definition, a diagnosis):*
`cross_window_agreement` in `V1_results.json` shows pairwise digit-agreement for C_3
growing **monotonically** with window size: W1-vs-anything=14d, W2-pairs=20d,
W3-vs-W4=27d, W4-vs-W5=32d, W5-vs-POOLED=35d. This is the expected signature of a
fixed-N window having diminishing resolving power for a higher-order 1/N³ term (W1 tops
out at N=20,000, where the C_3/N³ correction is astronomically smaller than at N=35M) —
not evidence against W1 or against the value. Restricting to the three genuinely-large
windows (W3: 250K–2.5M, W4: 2.8M–12M, W5: 13M–35M — each independently a wide relative
range with its own full K=3..9 convergence check) gives a **27-digit** trust bound,
comfortably above the gate (`V1_supplementary_largewindow.py`, `V1_supplementary_results.json`).

*What that higher-precision search found:* on the `pi/sqrt3` base, PSLQ recognizes
`C_3/(C_0·(π/√3)³) = 724351/1399680` at maxcoeff=3,000,000 (the original, pre-registered
ceiling) — landing on the PREDICTED basis for that base (odd k, but `pi/sqrt3` itself
carries a √3 factor, which — as derived and hand-verified against the already-known C_2
below — flips the expected Q/Q(√3) parity; this is not a violation, it is the same
relation restated). Algebra (T_(π/√3) = 9·q3 for k=3 odd) implies the **canonical**
`pi`-basis version needs height ≈12,597,120 — beyond the original 3M ceiling. Extending
the search to maxcoeff=20,000,000 (still a modest, precision-safe extension at 24 working
digits) on the `pi` base directly finds:

```
C_3/(C_0·π³) = (724351/12597120)·√3     [relation [12597120, 0, -724351], Q(sqrt3) basis]
```

i.e. **q3 = 724351/12,597,120**, giving

> **C_3 = (724351/12,597,120)·√3·π³·C_0**

This is independently reproduced on **four** algebraically-related bases (`pi` directly;
`pi/sqrt3`; `2pi/sqrt3` at exactly T/8 = 724351/11,197,440, hand-verified; and the
original `pi/sqrt3` hit) — all reducing to the identical q3, not four different numbers.

**The decisive check** (independent of any PSLQ search-height question entirely): the
candidate closed form `q3·√3·π³·C_0` compared DIRECTLY against each window's own
independent fit:

| window | agreement |
|---|---|
| W1 (N≤20,000) | 14 digits |
| W2 (N≤200,000) | 20 digits |
| W3 (N≤2.5M) | 27 digits |
| W4 (N≤12M) | 32 digits |
| W5 (N≤35M) | **36 digits** |
| POOLED | 35 digits |

Monotonically improving with N, reaching 36 digits at the largest window — a spurious
PSLQ coincidence does not reproduce this pattern (a fluke match stays capped near the
precision it was found at; it does not keep improving as entirely independent, far-larger-N
data is added). This is the same style of confirmation (diff ~1e-36) that validated the
banked C_1 (~9e-33) and C_2 (~4e-29).

**Anti-coincidence controls, re-run at the extended maxcoeff=20,000,000 ceiling:** every
wrong-parity test (Q for the bases predicted Q(√3), and vice versa) and every wrong-pi-power
control (`1`, `sqrt3`, `1/sqrt3`, `pi^2`) finds **nothing** — a clean null across the board
(full table in `V1_supplementary_results.json`, key `wrong_basis_controls_extended_maxcoeff`).

**One genuine wrinkle, reported not hidden:** q3's denominator is 12,597,120 =
**2⁷·3⁹·5** — close to but not exactly {2,3}-smooth like C_1's 108=2²·3³ and C_2's
7776=2⁵·3⁵ (there's an extra factor of 5). The numerator 724,351 = 53·79·173 is also less
visually "clean" than C_1's 11 or C_2's 697=17·41. This does not weaken the 36-digit direct
numerical confirmation, but it is a real deviation from the naive {2,3}-smooth prior stated
up front, worth flagging for whoever follows up (possibly the smooth-denominator pattern is
specific to k≤2, or possibly a different normalization/basis at k=3 would restore it —
neither checked here).

**C_4 — genuine precision floor, both metrics agree.** Primary (all-windows) trust: 10
digits. Large-window-only (W3,W4,W5) trust: 21 digits — still short of a confident search.
A first attempt to push C_4's search to maxcoeff=50,000,000 at only 18 working digits
produced "hits" on **every single basis, including the deliberately-wrong-pi-power nulls**
(`1`, `pi²`) — the unambiguous signature of a maxcoeff/precision mismatch producing pure
noise, not signal (caught before trusting it). Redone with a properly precision-calibrated
ceiling (maxcoeff ≤10,000,000 for Q, ≤10,000 for Q(√3), matched to 18 safe working digits):
**clean null on all 11 bases**, including the predicted `pi`-family. Given the height growth
observed so far (C_1: ~108–432 → C_2: ~2,592–7,776 → C_3: ~12,597,120, each order jumping
30–1600×), C_4's true height could plausibly exceed 10⁸–10⁹, requiring roughly 25–30+
trusted digits to search safely — more than even the large-window metric reached here.
**Honestly undecided, not a negative.**

## Overall verdict

**EULER-STRUCTURE-EXTENDED for C_3**: `C_3 = (724351/12,597,120)·√3·π³·C_0`, matching the
odd-k parity prediction stated before any PSLQ call, confirmed to 36 digits by direct
comparison against the largest independent window, reproduced on 4 algebraically-related
bases, with clean anti-coincidence controls throughout. This confirmation rests on a
well-motivated but non-pre-registered relaxation of the trust metric (large-N-windows-only,
justified by the monotonic, independently-checkable window-size/precision relationship) —
disclosed in full, alongside the primary/conservative metric's own PRECISION-FLOOR reading
(14 digits), so a reader can weight either.

**PRECISION-FLOOR for C_4**: clean null under a properly-calibrated search at the best
precision reached (21 digits, large-window metric); the height is plausibly beyond what
that precision can safely search. Extending W5 (or adding a W6) another order or two in N,
and/or raising dps, is what would move this — not a change in method.

## Honest fences

- A closed form is only reported as confirmed if it (a) sits on the PREDICTED basis
  (verified with the corrected, hand-checked classifier above), (b) is cross-window
  validated by MULTIPLE independent lines of evidence (not just one PSLQ hit at one
  maxcoeff tier), and (c) is stated together with which trust metric supports it.
- `SUFFICIENT_DIGITS_GATE = 17` (this task's own stated threshold) gates the PRIMARY sweep;
  the supplementary large-window analysis is reported as exactly that — supplementary, with
  its own trust numbers shown separately, never silently merged into the primary ones.
- The C_3 confirmation required extending the maxcoeff ceiling beyond the pre-registered
  3,000,000 (to 20,000,000). This was motivated by a SPECIFIC algebraic implication of an
  already-found lower-height hit (not a blind fishing expedition), and the eventual
  confirmation rests on the maxcoeff-independent direct-value comparison, not on the
  extended PSLQ search alone.
- C_4's null is explicitly not claimed as evidence against the pattern continuing — 21
  digits (best available) is short of what the observed height-growth trend suggests is
  needed, exactly the same honest posture the banked bench took for C_3 at 11 digits.
- Two implementation issues were caught and fixed before trusting any output: (1) a
  base-parity classifier bug (naive XOR, wrong for even k — caught by hand-verifying
  against the already-known C_1/C_2 before trusting it on C_3/C_4); (2) a maxcoeff/precision
  mismatch on the first C_4 push (maxcoeff=5e7 at only 18 digits) that produced hits on
  every basis including the null controls — caught by exactly those null controls firing,
  which is what they are for.
