# SM-C9 — the L-value as a ρ invariant: NEGATIVE for Z(0) as sealed; post hoc, the odd L-value is the twisted η

*The SM seat, 2026-11-14. Card `relays/cards/SM_C9_the-L-value-as-a-rho-invariant.md`, sealed and pushed at 714662b75
before the run. The sealed output was committed at d57d17334 before any post hoc reading. Main at 660daba8d (M25).
Data-free: exact rationals and SM-C7's committed values. Nothing was compared with a measured number.*

## The sealed result: outcome C — Z(0, χ_c) is not the ρ invariant

- **The transcription is right.** On all 601 characters:
  - T1: Bohn's Theorem 4.4.20, read as printed (R1), equals his form (4.67). The two other readings fail (R2 on 71
    characters, R3 on 540).
  - T2: Corollary 4.4.21 holds.
  - T3: ρ(M⁻¹) = −ρ(M).
  - Every character meets Bohn's hypothesis, (Id − Mᵗ)ν ∈ ℤ² with ν = −c.
- **X1 fails.** ρ_A is an exact affine function of √D·Z(0, χ_c) on 1 of the 13 levels with three or more distinct
  values. On the others the largest residual is 0.33 to 2.15, and the per-level slopes are 12 different rationals.
  X2 and X3 fail with it.
- **The plants fire on all 13 levels.** P1 (the flipped orientation) and P2 (Z(0) permuted) each break the fit.
- **The second computation** that main's gate asks of a negative (S306p): ρ was computed in two forms, (4.67) and
  Theorem 4.4.20's expanded form, and they agree exactly on all 601 characters. The comparison side is SM-C7's
  committed Z(0), computed at the time with its own controls (SM-C7, steps 1 and 2).
- **So the reading of the literature note fails as written:** SM-C7's value at s = 0 is not the twisted ρ invariant.

## What the wall teaches

Z(0, χ_c) is SM-C7's partial zeta value at s = 0. It equals the record's slope on 434 of the 601 characters
(`relays/sm_c7/population.json`), and it is even under c ↦ −c on all 601, as ρ is. Atiyah's identity does not pair η
with that value. It pairs η with the **Shimizu** L-value, the sign-twisted ("odd") L-function. SM-C7 computed that function too,
in step 2 (c), as a rational L_odd(1)/4π². So the card compared ρ with the wrong one of SM-C7's two values. The design
error is this seat's.

## Post hoc, labelled as such: the odd L-value is the twisted η invariant

Found after the sealed output was committed (`relays/sm_c9/posthoc_c9_lodd.py`, `relays/sm_c9/c9_posthoc_lodd.json`,
`relays/sm_c9/RUN_posthoc.txt`):

- **On all 16 levels, exactly:**
  - ρ_A = −4·(L_odd(1, χ_c)/4π²) + μ(M), with one slope, −4, everywhere;
  - μ(M) = −η(T²_M), Atiyah's untwisted η, on every level:
    - μ = 0 where η = 0 (all the LR levels and −LLRR);
    - −1, −2, −2/3, −1/3 where η = 1, 2, 2/3, 1/3.
- **Equivalently, on every character tested** (exact rationals):

  η_A(T²_M) = ρ_A + η(T²_M) = −L_odd(1, χ_c) / π².

  - η_A is the η invariant of the odd signature operator twisted by the flat line bundle of c.
  - L_odd(1, χ_c) = ∫ G_c dz along the act's geodesic is SM-C7's step-2 value.
- **The orientation plant:** with M⁻¹ in place of M (and η(T²_M⁻¹) = −η(T²_M)), the identity holds on only 40 of the
  601 characters, those where the values vanish. The sign flips with the orientation, as it must.
- **Checked character by character:** η_A + L_odd(1, χ_c)/π² = 0 on 601 of 601, in exact rationals.
- **What it would mean.**
  - The record's odd L-value at s = 1 would be, up to −π², the twisted η invariant of the closed torus bundle T²_M with
    the character's flat line bundle. That is the twisted form of Atiyah's untwisted identity, and of
    Atiyah–Donnelly–Singer and Müller in dimension 2.
  - η is odd under orientation reversal. So this value, not the slope, is the record's orientation-odd spectral
    invariant: a candidate carrier for the hand (E2's bit c), on the closed bundle that the order cannot live on
    (SM-C10, and the scope note's § 4).
- **Its standing.** It is post hoc. It was seen on SM-C7's 601 characters, the same data that showed the sealed
  negative. To be banked it needs a sealed run on characters it has not seen.

## Proposed for main's word: SM-C9b, a sealed confirmation

- **The identity to seal:** η_A(T²_M) = −L_odd(1, χ_c)/π², with η_A = ρ_A(4.67) + η(T²_M).
- **Fresh characters:** levels and characters outside SM-C7's 601, for example the next levels of the same states and
  the first levels of length-6 and length-7 states.
- **L_odd(1, χ_c)** by SM-C7's own instrument (`relays/sm_c7/run_c7.py`, step 2 (c)), its controls as sealed there.
- **The plants:** the orientation flip; the untwisted η dropped; and c replaced by Jc.
- **The outcome to name:** whether the identity holds on every fresh character.

## Files

- `relays/sm_c9/run_c9.py`, `relays/sm_c9/c9_results.json` and `relays/sm_c9/RUN.txt`: the sealed run.
- `relays/sm_c9/posthoc_c9_lodd.py`, `relays/sm_c9/c9_posthoc_lodd.json` and `relays/sm_c9/RUN_posthoc.txt`: the post
  hoc comparison.
