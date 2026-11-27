# SM-C23 — frame C is covariant when the modulus and the point move together: the act changes the cusp, not the frame

*The SM seat, 2026-11-25. Card `relays/cards/SM_C23_frame-cs-joint-covariance.md`, pushed with its script before the
run. Data-free. Main's frame (B1945's `parts` and `U_of`) is used unchanged; only the canonical end is supplied, by
B1927's law L(γτ) = L(τ) + log|cτ + d|. Run: `relays/sm_c23/c23_run.txt`; post hoc:
`relays/sm_c23/posthoc_full_precision_end_run.txt`.*

## Result

| | expectation (prior) | outcome |
|---|---|---|
| J0 | T a symmetry under some declared action (90%) | **holds** under C1, (a, b)γ⁻¹: 2.5e-30 masses, 1.4e-31 \|V\| |
| J1 | S a symmetry under some declared action, all three moduli (40%) | **holds** under C1 (C2 to C4 agree for S) |
| J2 | the act M a symmetry under some declared action (40%) | **holds** under C1 (C4 agrees, M being symmetric) |
| J3 | if J1 fails, only the mixing fails (35%) | does not apply |
| P | both plants fail by more than 1e-3 (90%) | **holds**: point unmoved, 3.3 to 3.6; end unshifted, 0.07 to 0.35 |

- **The sealed run's floor for S and the act is about 1e-17.** The sealed script passes the shifted end to the frame as
  a double. The post hoc rerun, disclosed and run after the sealed one, keeps L in mpmath: S holds to 3.9e-29 and the
  act to 7.1e-27 on the twelve orbit points at τ₀ = 0.13 + 1.2i.
- **Every other declared action fails** by O(1), including C5, the action on the characteristic (a, 2b).
- **Scope:** three moduli in the fundamental domain, twenty points (the act's orbit of (4/15, 1/30) at order 30, the
  four order-5 points on the act's line, four order-6 points), reading S. It is a computation on these, not a proof.

## Reading

- **Frame C, read with its canonical end, is SL(2, ℤ)-covariant point by point,** with the point carried by the record's
  own row convention (B1733). The end's shift is needed: without it, the plant fails.
- **So B1978's change of rate class is a change of cusp.** The rates of the point Mv read at the cusp ∞ are the rates of
  v read at the cusp M⁻¹(∞). The act does not change the frame; it changes the hole the frame is read through.
- **The whole instrument is then the point's rates at every cusp of its level.** A reading of B1978's orbits that is
  earned, not chosen, is that table, and the menu question becomes how the cusps' readings combine. This is the next
  card, not a result here.
- **This does not contradict agy-002's level-5 obstruction (M34).** That concerns flat unitary connections; frame C's
  end is not one, and its covariance needs the end's shift.

## A note for main, not a test

- B1927's table of L₂ stops at Im τ = 6. Above it `canon` returns the value at 6 (2.2505) and its flag `_extrapolated`
  is dropped by the callers (checked by calling it at 8, 20, 30 and 50).
- B1976 to B1979 read the rates at heights 20 to 50. The covariance above holds only with the true end. Whether the
  frozen end moves the rates, which are slopes, is not checked here.
