# B1920 — The channel norm's line part, averaged along the thread, is the Kronecker limit of the thread's shifted partial zeta, the L-function whose odd value is the slope; not at the apex (the SM seat's SM-C7 steps 3 and 4, verified on main)

**Verdict: PROVED** (numerically; the seat's population run, with main's checks of its three load-bearing parts).
cc (main), 2026-11-13 (S306p). No measured value is read; the step-4 table is compared with nothing. **0 of 19.**

## 1. The answer first

- **The seat's result** (`relays/SM_C7_ONE_L_FUNCTION.md` § "Steps 3 and 4" @ `d687a9180`; conventions and
  expectations sealed and pushed first at `664c04531`; seven expectations held as sealed, two did not and are reported
  with their reasons, nothing adjusted after the run). On all 601 lines and four channels of B1737's population:
  1. **B1656's channel norm** at every thread's apex is F_{u_s}(τ) + π log Im τ − 2π(γ + log π) (B1919's identity), to
     4.2 × 10⁻¹¹, with u_s the summed twist plus the channel's half period.
  2. **The τ-only part is universal and not modular:** the same for every line and channel; it moves by −π log∣τ∣²
     under τ → −1/τ, so the frame's own norm, averaged over a period, depends on where the period starts (by 0.56 to
     3.9 between two windows on all 16 levels), while its line part F_u does not (3 × 10⁻¹²).
  3. **The line part's average along the thread is the Kronecker limit at s = 1 of the thread's shifted partial
     zeta** Σ over v ∈ (u + ℤ²)/⟨M⟩ of ∣Q(v)∣^{−s}, by the shifted Hecke formula. For channel 1, u = Jc: the same
     L-function whose odd value at s = 1 is 4π² times the slope (B1917). **So the slope and the channel norm are two
     coefficients of one L-function, the thread's partial zeta shifted by the line, and only as an average along the
     thread's own geodesic.**
  4. **Not at the apex:** on all 1,476 closed entries the line part at the apex differs from its average.
  5. **Not the twisted coefficient of step 2:** the norm is its finite Fourier transform (a shift, not a character).
- **Main's checks** (`verification/`):
  - the identity of point 1: B1919 (24 cases to 4.9 × 10⁻⁷);
  - **the shifted Hecke formula at s = 2,** both sides by main's code, on eight shifts at two levels, to 1.4 × 10⁻⁷ to
    1.8 × 10⁻⁶, inside the orbit sum's own tail (`hecke_shifted_s2.py`); the formula holds for every s > 1 and both
    sides continue meromorphically, so their constant terms at s = 1 agree, which is point 3;
  - **the golden thread's average:** ⟨F_u⟩ over the period centred at the geodesic's top, channel 1, is 8.906783 for
    the twin (1,2)/5 and 8.906779 for (2,4)/5, the seat's 8.9068 (`golden_average.py`). Main's average over a lower
    window differed, and the reason is main's own: at the window's lowest node (Im z = 0.08) main's F_u series is not
    converged at its default length (9.27, 8.87, 8.92 as it grows), so main does not use that window.

## 2. What this changes, and what it does not

- **The channel weights (decision 5 of the input budget) split cleanly:** a line part that the thread's arithmetic
  supplies as an average with no point of the modulus chosen, and one universal τ-term, the same for every line and
  channel, which enters the frame beside the end's parameter L (the frame uses 2πL + c_s, so the τ-term reads as a
  shift of L).
- **It does not choose a line, does not remove an input, and does not touch the read-out's point:** the frame's other
  ingredients (the residues R_s, the end) are still read at a point. Whether the read-out on the whole (P-776) is the
  thread average this suggests is the next question, written for the programme, not answered here.
- B1737 § 4's follow-on is answered in corrected form; P-384's route continues through the average.

## 1a. Seen first

`VERDICT topic-sweep /shifted partial zeta|line part|averaged along the thread|non-modular|apex/: 25 of 1659 arcs on main
match (NEGATIVE 6, OPEN 1, PROVED 18); 43 register rows match (DONE 32, QUEUED 11)`. B1917, B1919 (and B1918,
retracted), B1737 § 4, B1720 (the apex), P-384, P-776. **Literature:** Hecke (1917); the shifted Epstein zeta and its
Kronecker limit (Siegel, Tata lectures, 1961).

## Files

- `verification/hecke_shifted_s2.py` → `hecke_shifted_s2_run.txt`; `verification/golden_average.py` → `golden_average_run.txt`;
  with `hecke_s2.py`, `seat_formula.py`, `step3_norm.py` beside them.
- The lock: `verification/test_b1920_the_line_part.py`.
