# B1663 — THE PULL-BACK'S STRENGTH: does anything the motion picture uses depend on how strong the pull-back is? (P-183, step 3): preregistration

cc (main), 2026-10-16. POINT_REGISTER P-183, step 3 of `speculations/S_THE_PUSH_BACK.md` §10.1, after B1662 (GENESIS
v1.48: the pull-back acts on the records). 0 of 19.

- **The setting.** The walk on SL(2, ℤ) whose steps are L and R, each with probability (1 − p)/2, and their pull-backs
  L⁻¹ and R⁻¹, each with probability p/2, multiplied on the right. p is the pull-back's strength: 0 means none, and
  ½ means as strong as the step, the owner's "no preference".
- **The question.** B1662 used transience and escape, which hold for every p. Does any quantity the motion picture uses
  depend on p? If none does, the push-back adds no number. If one does, p is a new input, unless "no preference" fixes
  it at ½.
- **The quantities.**
  - the Higgs's character along the walk (the coherent amplitudes of §8.3b);
  - the side, meaning which end the walk reaches;
  - the escape rate;
  - **the motion's averaged defect:** the time average of f = ∣D∣/∣∣R∣∣² along the geodesic ray to the walk's
    limit ξ, the motion that survives the cancellations. This is the quantity of §5 and §7, there taken along threads
    and the typical motion.

## 0. Seen first

`VERDICT topic-sweep /pull.back.s strength|random walk|harmonic measure|escape rate|exit law|Guivarc|Furstenberg|Kesten/: 3 of 1434 arcs on main match`
— B1083 (the arrow), B186 and B451 (escape rates of the trace map, another dynamics). None asks this question. Read:
B1662 and `S_THE_PUSH_BACK.md` §§5, 7, 9, 10. **Literature:** Kesten (1959), Furstenberg (1963) (transience, positive
escape); Guivarc'h and Le Jan (1993) (a finitely supported walk on a non-cocompact lattice has a singular exit law);
Series (1985) (cutting sequences and continued fractions); the Minkowski question-mark measure as the exit law of the
walk with L and R alone.

## 0b. Disclosed

- **Main's explorations of 2026-10-16**, kept beside the seal (`verification/before_the_seal/`):
  - B1662's walks at p = 0 and ½ (returns; escape 0.0992 at ½).
  - The design of the ray instrument. A first version truncated the digits and gave 0.355 ± 0.013 on the Lebesgue
    control, a bias from dropping cusp excursions. Rebuilt by digits, it gives 0.322 ± 0.004 against 0.315 (40 rays).
  - **The p = 0 value was seen:** with geometric digits (the p = 0 exit law), ⟨f⟩ = 0.517 ± 0.004 (40 rays). So T4(a)
    is not blind. T4(b) and T4(c) are: **no p > 0 average was computed before this seal.**
- **A smoke test** of this instrument: one control ray, one walk at p = 0, and one at p = ½, whose ⟨f⟩ was not
  printed.
- **f is set to 0 above height 7** in the reduced domain, where the theta series underflow. f(6i) = 2.8 × 10⁻⁶ and
  f(7i) = 1.4 × 10⁻⁷.
- **The reviewing agent before the seal:** §5.

## 1. The instrument (`verification/the_pull_backs_strength.py`)

- **p ∈ {0, 0.1, 0.2, 0.3, 0.4, 0.5}, 320 walks each,** with fixed and distinct seeds. Each walk runs until an entry of
  Xₙ reaches 10⁶⁰.
- **The limit ξ ≈ Xₙ(∞) = a/c,** exactly as a fraction. Its continued-fraction digits are taken with the last 20
  dropped, and at least 40 must remain, or the walk is counted as a failure. The side is the sign of ξ.
- **The ray average by digits.** The geodesic coded by ξ's digits is cut at its crossings of Re z = 0. Each piece is an
  arc of the semicircle with endpoints u_k = [a_k; a_{k+1}, …] and v_k = −[0; a_{k−1}, …], both O(1). f is
  integrated by arc length, with 20 digits of look-ahead. f is mirror-invariant, so ∣ξ∣ is used.
- **The control.** 160 Lebesgue-random rays with 160 digits each.
- **The run.** Eight workers, single-threaded BLAS (the owner's rule).

## 2. The cells

| cell | prediction | kind |
|---|---|---|
| **T0**, plumbing | f(−τ̄) = f(τ) to 10⁻¹² and f under z ↦ z + 1 and z ↦ −1/z to 10⁻¹⁰ at five points; every control ray finite; the ray instrument recovers the typical motion's 0.31500491 within 3 SE on the Lebesgue control (main's exploration sat 1.6 SE high, so a T0 failure is possible) | gate |
| **T1**, the character | χ(L) = χ(R⁻¹) = i and χ(R) = χ(L⁻¹) = −i, so each step multiplies χ by i with probability ½ for every p: exact. The count within 4 SE at every p is bookkeeping, a check of the letters' coding, not a measurement | exact + bookkeeping |
| **T2**, the side | P(ξ > 0) is 1 at p = 0, ½ within 3 SE at p = ½ (the mirror), and non-increasing in p within 3 SE | test |
| **T3**, the escape rate | different between p = 0 and ½ by more than 10 SE (positivity is a theorem; the stopped estimator cannot test it) | test |
| **T4**, the motion's averaged defect | E_p⟨f⟩, the mean over walks: (a) at p = 0 it differs from 0.315 by more than 5 SE (seen: 0.517); **(b) it differs between p = 0 and p = ½ by more than 5 SE, so the pull-back's strength is not idle; (c) at p = ½ it differs from 0.315 by more than 5 SE, so the no-preference motion is not the typical motion (an empirical contrast: Guivarc'h–Le Jan make the exit law singular, which need not change ⟨f⟩).** Failures (fewer than 40 digits, or a non-finite average) are at most 10% per p, and they are part of the cell. Read-outs: E_½⟨f⟩ and the spread over all six p | test |

**If T0 fails, nothing after it is read as a result.**

## 3. What it would mean

- **If T4(b) holds,** the pull-back's strength matters for the motion's averaged defect. Then p is a new input, unless
  "no preference" fixes it at ½, in which case E_½⟨f⟩ is a definite number of the principle with its pull-back, for
  this generator set (L, R and their inverses) and equal weights within each pair.
  - A number without a dictionary. No comparison with data is made or implied.
- **The power.** Per-ray spread is about 0.025, so the SE per p is about 0.0015–0.002 and the 5 SE threshold about
  0.015. A true difference of 0.02 is found with about 90–95% power; 0.01 is not.
- **If T4(b) fails,** there is no difference larger than about 0.015 between p = 0 and p = ½. The four intermediate p
  enter only through the spread read-out, so "idle" would be the reading only if that spread is also small. Together with T1 (the character is p-free), the push-back's
  strength would then add no number the picture uses. Only the side (T2) and the rate (T3) would see it.
- **T4(c)** is an empirical contrast with the typical motion. It neither tests Guivarc'h–Le Jan nor refutes them.

## 4. What it does not show

- Any value of the Standard Model.
- That the walk is the physical motion. This is the push-back picture's reading, firewalled.
- The exit law itself, beyond what ⟨f⟩, the side and the rate read off it.
- Other quantities than f, the character, the side and the rate.

## 5. Reviewing agent before the seal, and files

- **One read-only reviewing agent** (its check script kept in `verification/before_the_seal/review/`). No blockers.
  Taken:
  - `failures_ok` made part of T4;
  - T4(b)'s failure worded as "no difference above ~0.015", with the spread over all p as a read-out;
  - T4(c) reworded as an empirical contrast;
  - E_½ scoped to the generator set and weights;
  - T1 called bookkeeping;
  - T3's vacuous "positive" dropped;
  - T and S invariance and a finiteness check added to T0;
  - a NaN guard;
  - DROP 14 → 20 (its check: at most 11 digits lost at p = ½ in 300 walks).
- **Files:**
  - `verification/the_pull_backs_strength.py`, with `.json` and `_run.txt` after the run;
  - `verification/before_the_seal/` (the explorations, the smoke test).
