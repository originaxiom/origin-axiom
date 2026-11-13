# B1921 — The end's shift under S is the channel norm's τ-term: one end parameter, L̃ = L + ½ log Im τ − (γ + log π), is invariant, and the frame's S-covariance is derived (B1724's numerical note, closed)

**Verdict: PROVED** (derived, and checked on nine cases). cc (main), 2026-11-13 (S306p). Main's own code. No measured
value is read; no frame output is formed. **0 of 19.**

## 1. The answer first

- **The open note** (B1724's dated note of 2026-10-23): the frame is covariant under S "with the end passed as
  L + log∣τ∣", tested numerically and not derived in closed form.
- **The derivation, written before the run:** S rescales the fibre by 1/∣τ∣. The kernel K_c has weight one, so
  ∣K_c∣² d²u is unchanged; the excised disc of the channel norm's regularisation (radius ε) becomes one of radius
  ε/∣τ∣, and −2π log(1/ε) moves by −2π log∣τ∣. So **N(c′, −1/τ) = N(c, τ) − 2π log∣τ∣,** with c′ = (b, −a) (and
  N(−c) = N(c)). In the frame's combination 2πL + c_s the end's shift L → L + log∣τ∣ cancels it exactly: that is
  B1724's observation, now derived.
- **The check** (`verification/s_shift.py`): at three τ and three characteristics, N(c′, −1/τ) + 2π log∣τ∣ − N(c, τ)
  is at most 1.9 × 10⁻⁹; without the shift the difference is 0.33 to 1.27.
- **With B1919** (c_s = F_u + π log Im τ − 2π(γ + log π), F_u modular): π log Im τ moves by the same −2π log∣τ∣ under
  S and not under T, so the one combination **L̃ = L + ½ log Im τ − (γ + log π)** is invariant under SL(2, ℤ), and
  **2πL + c_s = 2πL̃ + F_u.** Written with L̃, the frame's channel weights depend on τ only through the modular F_u.

## 2. What this means

- **The end parameter the frame should carry is L̃,** not L: the non-modular τ-term of B1920 is the end's own
  coordinate change, not a property of the lines. With L̃, a thread average of the frame's channel weights does not
  depend on where the period starts.
- **It removes no input:** L̃ is as free as L was (decision 5, the end). It says which coordinate the end's freedom is
  in, and that the read-out as a thread average (P-776's question) is well defined for the channel weights.
- What it does not show: the same for the residues R_s and the full frame's outputs under the thread average; that is
  the next computation.

## 1a. Seen first

`VERDICT topic-sweep /L \+ log|end passed as|covarian.{0,20}S\b|invariant end|regularis.{0,20}disc/: 17 of 1660 arcs on main
match (NEGATIVE 2, PROVED 15); 20 register rows match (DONE 17, QUEUED 3)`. B1724 (the covariance and its note), B1726
and B1836 (T-covariance), B1919 and B1920 (the τ-term), B1716 (the norm's regularisation). **Literature:** none beyond
the scaling of a weight-one form.

## Files

- `verification/s_shift.py` → `s_shift.json`, `s_shift_run.txt`; `verification/step3_norm.py` (the norm).
- The lock: `verification/test_b1921_the_s_shift.py`.
