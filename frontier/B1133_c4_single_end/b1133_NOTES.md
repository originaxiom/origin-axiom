# C4-FLOOR — closing the B1124/B1130 C_4 remainder

**Verdict: C4-RECOGNIZED. Two-ended verdict: SINGLE-END.**

```
C_4 = (278392949 / 1813985280) * pi^4 * C_0,   C_0 = 3^(-1/4)
    = 11.359092863323493103049187527434817847807906771386...
```

Denominator 1,813,985,280 = 2^11 * 3^11 * 5^1. Numerator 278,392,949 is prime.

## The question

B1130 left C_4/C_5 "PRECISION-FLOORED (0 trusted digits at N<=70M)" and the two-ended
question (does C_3's factor-of-5 grow/recur in C_4's denominator, or does sqrt5 appear ->
the E8/sqrt5 end) UNDECIDED, "leaning single-end". This task re-examined that floor,
bounded to ~45 min of compute, on top of the banked B1124/B1130 data.

## Zeroth finding: the "0 trusted digits at N<=70M" claim doesn't match what's on disk

`frontier/B1130_twoended_tower/b1130_results.json` has `quick_mode: true`, W6 grid maxing
at N=1,500,000 (not the 38M-70M the code's non-quick branch defines), and a 42.9s total
runtime. The prose (FINDINGS.md/NOTES.md/arc_verdict) describes a run "pushed toward
N=70M... stopped at ~1hr" that is not the file on disk — either that run's output was
never saved/was overwritten by a later quick-mode invocation, or the prose describes the
attempted/intended scale rather than the delivered one. No `twoended_checkpoint.pkl`
exists anywhere in the repo (confirmed by search) to recover the larger run. This is a
provenance note for the banking seat, not something this task's scope permits fixing
retroactively — flagged here per the verify-don't-trust discipline (WORKING_RULES.md).

Separately: B1130's own `final_estimates.C4.trusted_digits=0` in that quick-mode file is
itself a **structural artifact**, not evidence of poor accuracy — with only 5-6 points per
window (quick-mode grids), individual windows can't support a K>4 fit (`K_CAP=11`,
`kmax=min(11,n-1)`), so only the POOLED fit produces a C4 estimate at all; with a single
window, `cross_window_agreement.C4` is structurally empty, and `trusted_digits` (which is
`min(within-window convergence, cross-window agreement)`) collapses to 0 by construction.
The POOLED fit's own self-consistency (`stable_digits_est=65`) was not itself trustworthy
either (see below) — but for a different, more interesting reason.

## Step 1 — best extraction on EXISTING data (no new large-N compute)

B1124 already reached N<=35,000,000 (dps_main=200) in a completed, non-quick run and
computed real per-window (W1-W5) + POOLED Chebyshev-in-1/N fits for C4. Three
**independent** extraction routes were cross-validated, using only already-computed data:

1. **B1124's own POOLED fit** (best_K=16): `11.3590928633234931030491875274346494975719159`
2. **B1130's independently-written codebase**, entirely different N-range (N<=1,500,000,
   quick-mode grid, dps_main=400, K up to 30 POOLED fit — different code, different data,
   same target): `11.35909286332349310304918752743481784780790677`
3. **Aitken-Delta^2 acceleration** applied to B1124's own W1..W5 window-estimate sequence
   (a third, independent *extrapolation technique*, not just independent code/data):
   `11.359092863323493103049187527458452` (level-2 Aitken)

All three agree to **28-31 raw digits** (dataset-vs-dataset: 30; Aitken-vs-each: 28).
**Adopted: 28 trusted digits**, comfortably past the >=15 digit gate — using zero new
heavy computation. A fresh, independently-written R_N spot-check (small N, own code)
reproduced the banked values exactly first, confirming the pipeline was understood
correctly before any of this was trusted.

**This means the "digit floor" B1130 hit is not fundamental** — it was an artifact of
having only one (quick-mode) dataset with a structurally-forced-zero cross-window count.
Combining what B1124 and B1130 *each already computed* resolves it for free.

## Step 2 — PSLQ search, and the methodological traps caught along the way

This is the part worth reading carefully — three real bugs were caught and fixed
mid-analysis, in order, each of which would have produced a **false conclusion** (two
false negatives, i.e. would have wrongly reported C4 as an unresolved precision floor,
which was the initial trajectory of this task before the bugs were found):

### Trap 1 — the PSLQ "noise floor" (3-term searches go spurious well below C3's own height)

A naive first sweep (dps=24, maxcoeff up to 1e10) found "hits" on **every single**
base/qtype combination, including deliberately-wrong-pi-power controls. Diagnosis: ran the
identical 3-term search against `C_2` (a quantity *known* to have zero sqrt3/sqrt5/sqrt15
content — plain rational * pi^2 * C0) and found spurious "hits" there too (15/18 tested
combinations). This reproduces the "noise-on-every-basis trap" B1130's own NOTES.md
describes catching once already — it recurred here independently. **Fix**: calibrate the
safe maxcoeff ceiling empirically, per relation-type, using negative controls (`C_2` for
3-term; `pi`/`C0`/`sqrt(2)` for 2-term, none of which have any small-height rational or
quadratic-irrational form). Result: **2-term (Q-type) safe to >=1e12**; **3-term
(quadratic-type) safe only to ~1e8** (with a half-decade-bisection-refined margin) — a
ceiling uncomfortably close to C3's own already-known height (12,597,120), which the first
(coarse, x10-step) calibration pass actually clipped below, failing its own positive
control (recovering C1/C2/C3's known relations) until the bisection was refined to
half-decade steps. **Lesson embedded in the script**: 3-term PSLQ recognition is far less
powerful than it looks at a given precision; a "clean null" on the sqrt3/sqrt5/sqrt15
two-ended probe only means something if the validated ceiling actually clears the height in
play — B1124/B1130's own sweeps did not check this, and neither did this task's first pass.

### Trap 2 — the L180 bug in its most easily-missed form

After Trap 1's fix, two new "hits" appeared (base=pi^2/Q(sqrt5), base=pi^3/Q(sqrt15)).
Reconstructing C4 from them and comparing against the independent B1124/B1130 values
(the mandatory cross-check gate this script enforces on every raw PSLQ hit) showed only
~14-15 digit agreement — squarely at the search precision, the signature of noise, not a
relation. Root cause, found by tracing it down: `base_defs = {"pi^2": PI ** 2, ...}` was
evaluated **outside any `with mp.workdps(...)` block** — even though `PI` itself carries
100+ correct digits, `PI ** 2` computed at Python's *ambient default* dps=15 silently
rounds the result down to ~15 digits. This is the L180 bug (freeze constants at high dps
before lower-dps use) in a form that doesn't look like the usual case (a low-dps constant
used directly) — it's two *already*-high-precision constants combined by an arithmetic
operator outside any precision context. **Fix**: every derived base (pi^2, pi*sqrt3,
pi/sqrt5, ...) is now frozen ONCE at module load, inside the same `with
mp.workdps(DPS_VOL):` block as the primitives — see `c4floor.py` section 0.

### Trap 3 — after fixing Trap 2, PSLQ itself missed the real relation; continued fractions caught it

With Trap 2 fixed, the spurious hits vanished, but a **new**, mathematically-inconsistent
hit appeared: base=pi/sqrt5, Q-type, height ~1.39e9, agreeing with B1124 to 30 digits and
with B1130 to **44 digits** — far beyond noise. But since `(pi/sqrt5)^4 = pi^4/25` is just
a rational rescaling of `pi^4`, if this were genuine, the **directly equivalent** search on
base=pi (which this task had already run, generously, to maxcoeff=1e12) should have found
the *same* relation at a *smaller* height (~1.8e9/25 legroom aside, still well under 1e12)
— and it hadn't. Independent verification via **continued fractions** (an algorithmically
different method from PSLQ, provably correct for 2-term/rational recognition) resolved
this cleanly: the CF expansion of `T_pi = C4/(C0*pi^4)` contains **278392949/1813985280**
as an actual convergent, immediately followed by a partial quotient of **27,502,942,826,811**
— an astronomically large next term (Gauss-Kuzmin: P(term > N) ~ 1/N, so this has
probability ~4e-14 of arising by chance), the classical signature of sitting suspiciously
close to an exact rational. **Raw `mpmath.pslq()` simply missed this relation on the
direct base=pi search** (confirmed: a dedicated, generous re-run at maxsteps=2,000,000
*still* returned `None`) — a real, empirically-observed PSLQ blind spot for this specific
case, not a precision or logic error. **Fix**: `c4floor.py` now runs a dedicated
`cf_rational_recognize()` continued-fraction search as a **mandatory complement** to PSLQ
for every 2-term (Q-type) test, not a fallback used only when convenient.

(A related **off-by-one bug** was then caught and fixed *inside* that new CF function
itself — it was initially returning the convergent computed one iteration *before* the
giant partial quotient, rather than the one produced immediately before it appears. Found
by tracing the exact loop index against the known target rational digit-by-digit; see
`step20_cf_index_check.py` in this directory for the trace that pinned it down.)

### The payoff: full self-consistency, 8 independent confirmations

With all three fixes in place, the final sweep finds the **same** rational
`278392949/1813985280` via continued-fraction recognition across **8 independently-tested
base normalizations** (pi, pi/2, pi*sqrt3, pi/sqrt3, pi*sqrt5, pi/sqrt5, pi*sqrt15,
pi/sqrt15) — a canonical-form cross-check confirms all 8 agree exactly. A ninth,
3-term "hit" (base=pi/2, Q(sqrt3)) is correctly auto-demoted as a redundant overfit of the
same base's already-validated Q-type answer (a 3-term search has an extra free parameter
that can absorb a good rational fit into rational+tiny-irrational form even when the true
answer has no irrational part at all — exactly the mechanism Trap 1 exposed at the noise
floor, recurring here in a slightly different guise even *above* the noise floor).

All C1/C2/C3 **positive controls** (recovering the already-known 11/108, 697/7776,
724351/12597120 relations through this *exact* calibrated pipeline) pass exactly, before
any C4 result was trusted.

## Result

```
C_4 = (278392949 / 1813985280) * pi^4 * 3^(-1/4)
```
- Agrees with B1124's independently-computed value to 30 digits, with B1130's
  independently-computed value to 44 digits.
- Denominator 1,813,985,280 = 2^11 * 3^11 * 5^1 (numerator 278,392,949 is prime).
- Height (1.8e9) is comfortably inside the empirically-validated-safe 2-term search
  ceiling (>=1e12) established via negative controls — this is not a lucky find outside
  the task's own validated confidence region.
- C4/C3 (denominators): 1,813,985,280 / 12,597,120 = **144** exactly (=2^4*3^2) — a clean
  integer ratio, though not a continuation of C1->C2->C3's own ratio pattern
  (72, then 1620) in any simple way; not force-fit, just reported.

## Two-ended verdict: SINGLE-END

- **5-exponent in the denominator: C1=0, C2=0, C3=1, C4=1.** The prime 5 **recurs at the
  same exponent — it does not grow.**
- **No new prime enters** beyond {2, 3, 5}.
- **No sqrt5 (or sqrt15) appears algebraically anywhere in C4** — C4 is a *plain rational*
  times pi^4 times C0, exactly the form the established parity law predicts for even k
  (k=0,2,4 -> Q; k=1,3 -> Q*sqrt3), with **zero** irrational admixture.

This **confirms** (not just "leans", as B1130 had it) the single-end reading: C3's factor
of 5 is most consistent with a generic, non-growing combinatorial/denominator-growth
artifact (the von Staudt-Clausen-type mechanism B1130's Part A already flagged as the
leading alternative), not the E8/sqrt5 end entering the tower's arithmetic. The object's
Kashaev-tower arithmetic remains anchored to Q(sqrt-3)/E6 alone through (at least) C4.

**Caveat, stated plainly**: this is one more data point (C4), not a proof the 5 can never
grow or that sqrt5 can never appear at some later, untested order (C5, C6, ...). The
3-term (irrational-type) search itself is only validated safe to height ~1e8 at this
precision — below C3's own height — so a **genuine** two-ended signal at C4, had one
existed as an actual irrational (not a plain-rational-in-disguise), might not have been
distinguishable from noise by the quadratic-type search alone; it was the Q-type route
(safe to 1e12) that actually resolved this coefficient, and it happened to resolve to a
plain rational. C5 was not attempted (out of this task's bounded scope; the N=35M data
needed for a C5 fit at usable precision was not fully exploited here since C4 already
closed the question this task was scoped to answer).

## Trusted-digit / search-height floor model (for future reference)

Fit from B1124's own cross-window agreement (digits vs characteristic N):
`digits ~ 5.999*log10(N) - 19.294` (matches B1124's own C3 model, slope ~6.98, in kind).

| target digits | N needed | Q-ceiling (2-term) | quad-ceiling (3-term) | est. runtime (B1124-scaled) |
|---|---|---|---|---|
| 24 | 1.6e7 | 1e10 | 1e7 | ~1 min |
| 28 | 7.7e7 | 1e12 | 1e8.4 | ~6 min |
| 35 | 1.1e9 | 1e15.5 | 1e10.8 | ~89 min |
| 40 | 7.7e9 | 1e18 | 1e12.6 | ~607 min |
| 50 | 3.6e11 | 1e23 | 1e16.1 | ~28,204 min |

Reaching a 3-term (two-ended) search ceiling that clears C3's own height (1.26e7) with
real safety margin needs only ~24-28 digits (already in hand); reaching one that clears a
*much* larger plausible height (comfortably matching or exceeding C4's actual 1.8e9, i.e.
~1e10-1e11) needs ~30-35 digits, i.e. N~1e9 — starting to approach B1130's own abandoned
38M-70M attempt in cost, consistent with why that attempt was cut short. None of this was
needed here because the Q-type route resolved C4 first.

**Smarter-than-brute-N**: the Ohtsuki/quantum-dilogarithm asymptotic recursion for the
figure-eight-knot Kashaev invariant would give these C_k as exact rationals directly (zero
precision loss, sidestepping the N-scaling floor entirely) — not attempted here (deriving
or reproducing an unfamiliar recursion from memory risks silent, hard-to-catch error, which
is exactly the failure mode this task's own three caught-bugs episode illustrates the cost
of; flagged as the natural next step for a from-first-principles derivation, not executed).

## Files

- `c4floor.py` — standalone (mpmath + sympy only, no repo imports, no machine paths).
  Reproduces the full pipeline: R_N spot-check -> triple cross-validation -> empirical
  noise-floor calibration (via negative controls) -> positive controls (C1/C2/C3) -> C4
  sweep (PSLQ + continued-fraction recognition, cross-validated hit-gating, redundant-hit
  de-duplication) -> floor projection. Run: `python3 c4floor.py`.
- `results.json` — full structured output of the run described above.
- `step1_crossvalidate.py` .. `step21_final_confirm.py` — the exploratory/debugging trail
  that found the three traps above, kept for audit purposes (not part of the polished
  pipeline, superseded by `c4floor.py`).
