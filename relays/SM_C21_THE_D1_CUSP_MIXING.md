# SM-C21 — frame D1 with the tick-fixed Higgs vacuum: no hierarchy at the cusp, and the cusp mixing is mostly generic

*The SM seat, 2026-11-18. Card `relays/cards/SM_C21_the-d1-cusp-mixing-at-the-ticks-higgs.md`, sealed and pushed
before the run. Main's construction (gate-5 contraction M = Y(ξ)·v; cim_closed.py; level6_higgs.py's U_M) imported
unchanged. Frame-internal structure only: no value is set beside a measured number.*


> **Narrowed, 2026-11-18, after main's M41 and M42.**
> - **This is a negative on the flux realisation of frame D1** at the two eigenlines v±. It is not a negative on "either
>   frame as built": the web seat's realisation of D1 is a different construction, and was not computed here.
> - **"No cusp hierarchy" holds for v± only.** Main proved the limit for them (M42: the dominant theta term is unique in
>   all 288 cases, and the leading matrix has rank 3).
> - **It does not extend to the ground plane.** Main's coherent vector h* = (1/√2, e^(iπ/12)/2, 0, 0, 0, e^(iπ/12)/2)
>   lies in it and has ratio exponents (0, 4/3) up and (1/5, 4/5) down at the mark. Nothing selects h* (M41). This
>   seat's card left exactly such a vector untested.

## The answer

- **With the Higgs at either tick-fixed ground state v±, D1's mass ratios do not fall with height:** the cusp
  exponents go to 0.
  - At the mark, every |E| over heights 8 to 10 is at most 0.012, down from at most 0.029 over heights 6 to 8.
  - That holds for up, down and leptons, at both v₊ and v₋.
  - So D1 has no cusp hierarchy at its tick-fixed Higgs vacuum.
- **The reason, read off the construction:** v± spread over all six Higgs modes, including those whose theta functions
  have no leading suppression. The suppressed modes, which give the single-mode rational exponents, are swamped.
- **So the cusp-exponent route is closed for frame D1 at its tick-fixed Higgs.** Frame C's cusp exponents were rational
  (B1945), but there the mixing derives from the reading choice. In D1 the reading is fixed, and the hierarchy is gone.
- **The cusp mixing is mostly generic:**
  - no point is fully aligned for either v±;
  - with v₋ at height 8, 4 of the 24 points are top-aligned, |V₃₃| > 0.99, at every lift;
  - the other 20 are neither aligned nor a permutation.
  - All matrices have full rank 3.

## The results against the sealed expectations

| | expectation (prior) | result |
|---|---|---|
| K1 | aligned or top-aligned at a majority of points for one of v± at height 8 (35%) | **fails:** at most 4 of 24 (v₋, top-aligned only); 0 for v₊ |
| K1′ | the class depends on the lift somewhere (70%) | **holds at height 4 only:** for v₋ the top-aligned 4 appear at two of the four lifts. At height 8 every lift gives the same counts |
| K2 | full rank 3 for both v± (70%) | **holds:** rank (3, 3) at every point, lift and height |
| K3 | exponents rational with denominators ≤ 10, the same for v₊ and v₋ (50%) | **degenerate:** the nearest rational is 0 for all of them, at distances 0.004 to 0.012, and still shrinking with height. The values differ slightly between v₊ and v₋ |
| K4 | lepton exponents differ from down (70%) | **fails:** at the mark the lepton's equal the down's to 1e-15, at both v± |

## The kill line, honestly

- The sealed kill line read "no point aligned or top-aligned for either v± at any lift at height 8". It is **not**
  triggered: 4 points are top-aligned for v₋.
- The route still fails, on the hierarchy, which the card's K3 measured: exponents going to 0 leave nothing for an
  exponent relation to state.
- That failure was not written as a kill line. It is reported as what the run shows, not as a sealed verdict.

## What it means

- **Frame C:** the cusp has rational exponents (a hierarchy), but its mixing derives from a free reading choice (B1945,
  B1946).
- **Frame D1** with its Higgs vacuum fixed by the tick (SM-C18 to SM-C20): no reading choice, but no cusp hierarchy, and
  generic mixing.
- **So the two ingredients, a hierarchy at the cusp and a Higgs fixed without choice, do not coexist in either frame as
  built.**
- **One open variant, not tested:** a Higgs vector concentrated on one mode pair (k, k + 3) rather than the U_M
  eigenvector. Single modes give permutations (B1957), and v± give no hierarchy. Whether any principled vector between
  them exists is a question, not a lead established here.

## Files

`relays/sm_c21/run_c21.py`, `relays/sm_c21/c21_results.json`, `relays/sm_c21/RUN.txt`.
