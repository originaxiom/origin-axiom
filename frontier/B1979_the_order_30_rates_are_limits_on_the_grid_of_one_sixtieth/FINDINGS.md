# B1979 — The order-30 rates are limits on the grid of 1/60: twelve classes, not seventeen, and the lepton m2/m3 rate is 2/5 at every point

**Verdict: PROVED (numerically, on three intervals of height and two columns; the limits on the grid are read, not
derived).** Main, 2026-11-25. Data-free. Register rows P-845 and P-860 (d). **0 of 19.**

## Seen first

- **The web seat's check of B1977 (CHK-1),** at chat1/web-seat 580bb80a1 and 5e4db6850, with its relays THE LOAD-BEARING
  SWEEP and CHK-2 of 2026-11-24.
  - It reproduced B1977's 96-point table with two assemblies of its own.
  - It found the rates on 30–40 within 4.2e-4 of the grid of 1/60.
  - Its R3 failed as worded: at the column 0.31, on 20–30, 32 rates differ by up to 2.4e-3.
  - It judged that B1977's 17 classes are a menu and a trials factor.
  - This arc is main's own run of the same questions, with one more interval. The web seat's numbers were not read into
    it, only compared afterwards.
- **The record:**
  - B1977 (the rates on 20–30, its 17 classes at three decimals, G1 to G5);
  - B1978 (the act's eight orbits of twelve, and its dated caveat on τ);
  - B1976 (the 96 points).
- **The literature:** none needed. The question is numerical (are the finite-interval rates limits?), and the limits
  are read, not derived.

## The results (`verification/heights.py`, `heights_run.txt`; `orbits_classes.py`, `orbits_classes_run.txt`)

### The rates are limits

- **Reproduction.** On 20–30 at the column 0.13 the run reproduces B1977's json at all 864 rates, with difference 0.
- **Convergence onto the grid of 1/60.** All 864 rates on each interval at the column 0.13:

  | interval | largest residual to the grid | median |
  |---|---|---|
  | 20–30 | 3.6e-3 | 6.3e-7 |
  | 30–40 | 4.2e-4 | 1.2e-9 |
  | 40–50 | 5.1e-5 | 2.2e-12 |

  - The residual falls about eightfold per interval.
  - The four rates off the grid on 20–30 (B1977's G3, 860 of 864) are finite-height effects. On 30–40 and 40–50 all
    864 are on it.
- **The column.** On 30–40, the column 0.31 moves no rate by more than 2.2e-4. The web seat's 2.4e-3 on 20–30 is the same
  finite-height error, and it falls with height.
- **The drift between intervals** is 3.1e-3 from 20–30 to 30–40, and 3.7e-4 from 30–40 to 40–50.
- **The slow 2–3 mixing.**
  - 18 points have V₂₃'s rate near 1/30 on 20–30. These are B1977's five and thirteen others within 3e-3.
  - At the five, the rate moves 0.03247 → 0.03322 → 0.03332. At the other thirteen it moves 0.03311 → 0.03331 → 0.03333.
- **Alignment.** All 96 points are aligned (least diagonal ≥ 0.9) at heights 40 and 50.

### Twelve classes, not seventeen

- **B1977's 17 classes were partly an artefact of the finite interval.** B1977 keyed its classes at three decimals, below
  the 20–30 error.
  - With B1977's key, the count is 17 on 20–30, 13 on 30–40 and 12 on 40–50.
  - With the rates snapped to the grid of 1/60, the count is **12**, and every point's class is the same on 30–40 and on
    40–50 (96 of 96).
- **The twelve classes** have sizes 12, 12, 12, 12, 8, 8, 6, 6, 6, 6, 4, 4. Their rates are listed in `heights_run.txt`.
- **The lepton m2/m3 rate is 2/5 at every one of the 96 points.** The lepton m1/m3 rate is 1, 7/5 or 11/10.
- **V₁₃'s rate is V₁₂'s plus V₂₃'s** in 6 of the 12 classes.
- **The classes on the act's orbits** (B1978, at a fixed τ; its dated caveat applies):
  - the act keeps the converged class at 8 of 96, as with B1978's two-decimal key;
  - the orbits fall into two families of four, each family carrying six classes: {2, 3, 4, 8, 9, 10} and
    {0, 1, 5, 6, 7, 11}.
- **The classes on the parts of the point.**
  - Each 5-part value carries 6 classes, and each 2-part value carries 6.
  - Each 3-part value carries 4 or 8.
  - Each of the 24 values of the 6-part carries 2 or 4 classes. So the 6-part alone does not fix the class, and the
    5-part is needed too.

## What it means

- **The menu for route (d) is 12, not 17.** If no principle fixes the class, the sealed card on the scale-free ratios
  declares these 12 converged classes and pays their trials factor.
- **The lepton m2/m3 rate of 2/5 at every point** is the first order-30 rate the choice of point does not touch. Whether
  it is a theorem of the frame (a charge identity mod 30) is open.
- **The web seat's judgement stands:**
  - level 30 was reached after level 5 failed structurally;
  - the 6-part is not fixed;
  - "hierarchical" in G1 and G5 means positive rates, which any large height turns into a hierarchy.

  This arc fixes the size of the menu, not the choice from it.

## What is open

- **A principle for the class (P-845).** agy-exp's canonical 24-point shell E_τ[6]_prim is the set of the 6-part's
  24 values (the web seat's observation, CHK-2 § 0 item 6). It is read next, at source.
- **The lepton 2/5 as an identity.**
- **The joint covariance of B1978's caveat.**
