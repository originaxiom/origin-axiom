# B1813 — THE WEAVE'S OWN MEASURE DEPENDS ON HOW ITS THREADS ARE COUNTED (THE OWNER's WHOLE-EXISTENCE COMPUTATION, STAGE 1; P-107; DATA-FREE): LEFT UNFORCED, THE THREADS PRODUCE A DEFINITE MEASURE ON τ FOR EACH COUNTING RULE, AND THE RULE IS A CONTINUUM. COUNTED MOVE BY MOVE (MINKOWSKI's MEASURE, B1663), THE LIMIT KEEPS OUT OF THE CUSP: P(Im τ > Y) ≈ 3.9·4^(−Y)/√Y (0.0346 AT Y = 3). COUNTED BY GEOMETRIC LENGTH, IT APPROACHES HYPERBOLIC AREA (0.315 AT TRACE ≤ 400, AGAINST 0.318). WEIGHTING WORDS BY e^(−s·ℓ) INTERPOLATES, THE CUSP TAIL's RATE FALLING TO ZERO AT THE FAREY MAP's PHASE TRANSITION (s = 1, B852), WHERE AREA LIVES. P-107 IS RELOCATED, NOT SETTLED: THE COUNTING RULE IS CHOSEN

**Verdict: PROVED** (computed; two orderings and the family between them; convergence checked; independently reproduced
by the referee). Data-free; none of the 19. cc (main), 2026-10-29, at the owner's "go for it" and his question whether
the two counts interact.
- The frame card was written before any computation (`verification/FRAME_CARD.md`).
- Its stage-1 prediction (the τ-marginal approaches hyperbolic area; prior 70%) **failed** for the move count and **held**
  for the geometric count.
- Corrected before landing at its hostile referee (§ 5).

**0 of 19.**

## 1. The question and the frame (labels by WORKING_RULES' rule of 2026-10-29)

- **The owner (2026-10-29):** "see what program produces when not forced", "its natural unraveling"; then, "should we count
  in both ways and see whether both ways interact".
- **THE_WEAVE's rule:** "nothing on record is yet a weave result by minimization"; the democratic thread sum is flat
  (§ 320). If the interaction selects no point, its unforced output is a measure (the owner's framing of 2026-10-13).
  P-107: the invariant measure is not unique.
- **Labels:**
  - the counting rule is CHOSEN;
  - the limit given the move rule is FORCED given the rule (this arc and the classical lift of Minkowski's measure);
  - the length weight per thread is CHOSEN (the limits do not depend on it);
  - the hierarchy reading (§ 3) is conditional on B1691's H-cov and on a Higgs carrying end data on v₊ (B1697, B1700).
- **A deviation from the card, disclosed.** The card named B1720's apex rule (one point per thread). The run's measure is
  each thread's arclength measure, weighted by its length. Equidistribution concerns the length measure, not the apex.
  The apex rule is reported beside it (§ 2).

## 2. Computed (`verification/stage1_threads_measure.py`, `stage1b_by_trace.py`, `stage1c_two_clocks.py`)

**The method.** Each thread's closed geodesic (the axis of its matrix, one period of length 2 arccosh(t/2)) is sampled
uniformly in arclength and reduced to the standard fundamental domain. This is exact at these sizes (ℓ ≤ 32); the
referee's check 7 shows the float sampler fails near ℓ ≈ 40.

**By moves** (every primitive positive word with both letters, word length ≤ n):

| n | threads | P(Im τ > 1.5) | > 2 | > 3 | > 4 | > 6 |
|---|---|---|---|---|---|---|
| 10 | 224 | 0.382 | 0.168 | 0.0345 | 0.0069 | 0.0000 |
| 12 | 745 | 0.383 | 0.168 | 0.0346 | 0.0074 | 0.0002 |
| 14 | 2 536 | 0.383 | 0.168 | 0.0346 | 0.0075 | 0.0003 |
| the limit (the referee's: i.i.d. Geometric(½) runs with their roof) | — | 0.3829 | 0.1676 | 0.03462 | 0.00754 | 0.00039 |

- **The measure** is the maximal-entropy measure of the Farey coding, Minkowski's question-mark measure, lifted to the
  geodesic flow (B1663 found it as the walk's).
- **Its tail:** P(Im τ > Y) ≈ 3.9·4^(−Y)/√Y. The local slope is 1.5–1.6 at Y = 2–4, falling toward 2 ln 2 ≈ 1.39: a run of
  a letters reaches height about a/2 with probability 2^(−a).
- **The mean geodesic length per move** is 0.7924, twice B1663's escape rate.
- **B1662's walk with inverses** gives the same height marginal (P(Im τ > 3) = 0.034–0.035; the referee's check 5).

**By geometric length** (every primitive positive class with trace ≤ T; complete):

| T | classes | P(Im τ > 3) | P(Im τ > 6) |
|---|---|---|---|
| 12 | 29 | 0.192 | 0.000 |
| 30 | 151 | 0.268 | 0.099 |
| 100 | (the referee's) | 0.306 | 0.144 |
| 400 | (the referee's) | 0.315 | 0.155 |
| hyperbolic area | — | 0.318 | 0.159 |

The approach is monotone from below from T = 30 on. This is equidistribution by length on the modular surface (Pollicott
1986; Sarnak; Roblin 2003 in general), not proved here.

**The family between them** (words of length n weighted by e^(−s·ℓ); main's stage 1c, matched by the referee's check 6
from n = 16 to 20):

| s | 0 | 0.25 | 0.5 | 0.75 | 0.9 | 1.0 | 1.25 |
|---|---|---|---|---|---|---|---|
| P(Im τ > 3), n = 12 | 0.0349 | 0.054 | 0.084 | 0.130 | 0.167 | 0.195 | 0.274 |
| P(Im τ > 3), n = 14 | 0.0347 | 0.054 | 0.085 | 0.135 | 0.177 | 0.211 | 0.306 |

- **Below s ≈ 0.75** the limit has converged at these lengths. From s ≈ 1 it keeps rising with n.
- **The phase structure.** This is the Farey map's thermodynamic family. The cusp tail's rate is about twice the pressure
  P(s): 2 ln 2 at s = 0, vanishing at the phase transition s = 1 (B852's plateau), where hyperbolic area lives. Beyond it
  the weight runs into the cusp.

**The apex rule** (B1720) is a third choice: P(Im τ > 3) = 0.29 at n = 14.

**The lines.** Summed over the 2 536 threads, the vectors of exact order N that a thread fixes number 1.64–2.10 per thread
for N = 3, …, 30 (0.99 for N = 2).
- This is Burnside's lemma: 2 per order for any family equidistributed mod N. It carries no information about the threads
  and does not test the card's line prediction.
- Because every order carries equal weight, the threads' line marginal is not normalisable over N without a CHOSEN cutoff.

## 3. What it means

- **Among the measures the threads themselves generate, P-107's non-uniqueness reappears as the counting rule.** The rule
  is a continuum:
  - by moves (Minkowski's measure), the measure keeps out of the cusp;
  - by geometric length (s = 1), it is hyperbolic area: W57's "seed's own measure", the critical point of the move
    family;
  - in between, distinct limits.

  P-107 is relocated, not settled: the counting rule is CHOSEN.
- **For the hierarchy (a reading, conditional on H-cov and on end data on v₊).** Near the cusp the frame's m₂/m₃ falls
  like 18·e^(−π Im τ) (B1691; it holds from Im τ ≈ 2, S163; S164, S245 and S248 leave the cusp column standing).
  - **Under the move rule:** P(m₂/m₃ < x) falls like a power of x — about x^0.44 asymptotically, up to a (log 1/x)^(−½)
    factor (about x^0.49 at Im τ = 2–4). Deep hierarchies are suppressed.
  - **Under hyperbolic area:** it falls like 3/ln(C/x). Deep hierarchies are common (W57's finding).
  - **At the transition:** the weight moves into the cusp. A world with deep hierarchies would correspond to the weave
    near its critical point. **Why the weave would sit there is the question this arc leaves.**
- **What it does not do.**
  - It does not compute the frame's outputs under these measures (stage 2).
  - It does not compare with data (stage 3, sealed).
  - It does not prove the limits' forms (the convergence here is numerical; the referee's limit computation is
    analytic-numerical).
- **0 of 19.**

## 4. Scope

- The threads are primitive positive words with both letters, i.e. PSL(2, ℤ)'s hyperbolic classes.
- The arclength measure per thread.
- The standard fundamental domain's height marginal only.

## 5. The referee (hostile, read-only; `verification/referee/`)

- **Its verdict:** PASS WITH CORRECTIONS. Every number reproduces from independent code:
  - two samplers;
  - the run-segment method;
  - an independent enumeration of the trace set, to T = 400;
  - the move clock's limit;
  - the walk.
- **Required corrections, applied:**
  - (R1) the Seen first omitted B1663, which had found the move clock's measure (Minkowski's) — and B852;
  - (R2) "P-107 settled by the clock" overclaimed: the rule is a continuum, so P-107 is relocated;
  - (R3) the lines tally is Burnside's lemma, not a finding;
  - (R4) the card's apex rule against the run's arclength measure, disclosed; the hierarchy reading labelled and
    conditioned.
- **Recommended, applied:**
  - the tail's form;
  - the walk identification computed;
  - "orders" rather than "weights";
  - the T = 400 values;
  - the equidistribution citation for the cusped surface.
- **Main's verification:** the referee's checks 1, 2, 4 and 6 regenerated on main. The s-family agrees with main's own
  stage 1c at every printed digit.

## Seen first

- `VERDICT topic-sweep /typical|typicality|hyperbolic (area )?measure|invariant measure|Haar measure|equidistribut|ensemble|anthrop.c|probability (of|that) .{0,20}Im ?τ|measure over τ|distribution of τ/ (full text): 37 of 1560 arcs on main match (NEGATIVE 14, OPEN 3, PROVED 20); 4 register rows match (QUEUED 4)`
  (rerun at landing with an equivalent pattern; the counts now include this arc and P-437) — P-091, P-107, P-413.
- The referee's: `VERDICT topic-sweep /word length|uniform words|Farey|Gauss measure|continued fraction.{0,30}measure|tick.{0,20}measure|clock/ (full text): 109 of 1559 arcs on main match; 5 register rows match`.

**Bearing on it:**
- **B1663:** the move clock's measure, the uniform-word motion, Minkowski's question-mark measure, the same at every
  pull-back strength. It averaged one τ-function under it (0.517 against the typical 0.315). None computed its height
  marginal, set it beside the trace ordering, or asked how it depends on the counting rule.
- **B852:** the Farey map's pressure and its phase transition.
- **W57** (the SM seat; harvest row 1099): the hyperbolic measure in the ruled-branch frame.
- The SM seat's § 320; B1720; B1733; B1662; B1629; B1630; THE_WEAVE's rule.

**Literature (pointers, not read on the bench unless marked):**
- Minkowski's ?(x) (Denjoy; Salem); Kinney (1960); Kesseböhmer–Stratmann (2007);
- Pollicott (1986), equidistribution by length on the modular surface;
- Pollicott–Sharp (1998), word length against geometric length;
- Series, the continued-fraction coding;
- Hofbauer, and Prellberg–Slawny, the Farey map's phase transition.
