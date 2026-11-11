# P-783: the golden state is the lowest twin-odd state in all four classes, and simple — by a scan, not a proof; no state at the lane's two values

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:`, closing main's card P-783 for this seat
(register row P-783; `docs/handoffs/CC_TO_CHAT1_2026-11-11_YOUR_THREE_CARDS_ANSWERED.md`, row "golden state 4").
**The card:** `relays/cards/CHAT1_P-783_the_golden_state_lowest_and_simple.md`, committed with its script before any
run (a6b381e01). **Files:** `relays/chat1_2026-11-11_p783/`.

**How it was checked (§ 12):**
- **The sealed run:** computed once; expectations committed first (sealed a6b381e01, output c13cbc521).
- **The post hoc check:** computed once; expectations committed first (f3c9d62ec, output 76df0a668). It was written
  after the sealed output was read, and uses the sealed script's functions.
- **No independent recomputation is in the record.** A second computation with separate code exists only as the
  earlier referee's scan by collocation (the golden-state relay's § 7). Its script and output are not in the record,
  so § 12's "recomputed independently" does not apply. Main recomputes when it lands.

## 1. The answer

| prediction | sealed rule | result |
|---|---|---|
| **L, lowest** | no eigenvalue below R₀ − 10⁻⁶ in any class; in (σ, ε) = (−1, −1) the lowest is R₀ to 10⁻⁸ | **holds.** The lowest values are 3.2642513026 in (−1, −1), which is R₀ to 2 × 10⁻¹³, then 4.8937812914 in (−1, +1), 6.5285026053 in (+1, +1) and 7.4946304901 in (+1, −1) |
| **S, simple** | at R₀ the class (−1, −1) has one scaled singular value below 10⁻⁶ of the median and the next above 10⁻³; the other classes none below 10⁻³ | **holds:** 1.7 × 10⁻¹⁵ and 0.94 in (−1, −1); the least in the other classes 0.74, 0.23, 0.063 |
| **X, no exceptional eigenvalue** | none with R = it, 0 < t < ½, in any class | **holds:** no sign change of H was found in any class |

**The space.** The twin-odd states are the Maass cusp forms of weight 0 on Γ₀(5) with the character χ(d) = (d/5),
in four classes:
- σ, the sign under the mirror x ↦ −x;
- ε, the sign under W: z ↦ −1/(5z).

The golden state is in (−1, −1) at R₀ = π/(2 ln φ).

## 2. The controls

| control | rule | result |
|---|---|---|
| K0, the K-Bessel function by the trapezoid rule against mpmath, 12 points | 10⁻⁹ of e^{−πR/2} | 8.0 × 10⁻¹¹ |
| C1, the golden state's coefficients at R₀ | a₂ = a₃ = 0, a₄ = 1, a₅ = −1, a₉ = 1, a₁₁ = −1.11318395792, to 10⁻⁶ | largest error 8.9 × 10⁻¹³ |
| C2, the next forms of the golden field | each in exactly one class, to 10⁻⁷ | π/ln φ in (+1, +1); 3π/(2 ln φ) in (−1, −1) |
| C3, a value that is no eigenvalue (R₀ + 0.1) | automorphy fails, above 10⁻³ | 0.26 |

## 3. The spectrum to R = 11, by class

| R | classes (σ, ε) | |
|---|---|---|
| 3.2642513026 | (−1, −1) | the golden state, R₀ |
| 4.8937812914 | (−1, −1), (−1, +1) | doublet |
| 6.2149037377 | (−1, −1), (−1, +1) | doublet |
| 6.5285026053 | (+1, +1) | π/ln φ, the golden field's next form |
| 6.9638742407 | (−1, −1), (−1, +1) | doublet |
| 7.4946304901 | (+1, −1), (+1, +1) | doublet; the second class post hoc |
| 7.7360920284 | (−1, −1), (−1, +1) | doublet |
| 8.7545035832 | (−1, −1), (−1, +1) | doublet |
| 8.9232624074 | (−1, −1), (−1, +1) | doublet |
| 9.2608655254 | (+1, +1), (+1, −1) | doublet; the second class post hoc |
| 9.7927539079 | (−1, −1) | 3π/(2 ln φ), the golden field's next form |
| 10.0596584255 | (−1, −1), (−1, +1) | doublet |
| 10.1305739828 | (+1, −1), (+1, +1) | doublet |
| 10.5733379644 | (−1, −1), (−1, +1) | doublet |
| 10.9484540107 | (+1, −1), (+1, +1) | doublet |

- **Every value is confirmed by both truncations.** The difference between them is below 8 × 10⁻¹¹ (below 5 × 10⁻¹² for
  R < 9; below 2 × 10⁻¹³ for R < 8.7). Each passed the automorphy test under E1 and W to 7 × 10⁻¹⁰ or better.
- **The count is 27 states in 15 values,** the count the seat's earlier referee reported for the agy lane. The sealed
  run confirmed 25 states.
  - Two values, 7.4946304901 in (+1, +1) and 9.2608655254 in (+1, −1), were found by the first truncation and passed
    its tests. The second truncation's refinement then failed: H had the same sign at the two ends of its bracket of
    ±0.004 (only the normalisation a₁ = 1 was refined there).
  - A post hoc check, committed before its run (f3c9d62ec; output 76df0a668), finds both at both truncations, within
    10⁻¹⁰, with scaled singular values near 10⁻¹¹ and automorphy errors below 10⁻⁹.
  - It also finds a second crossing 0.0012 and 0.0013 from the two values (7.4958069157; 9.2621414937). There the
    next coefficient is huge or failing (3 × 10¹⁰; 1.9 × 10⁻²) and the automorphy errors are 2 to 3 × 10⁻². That is
    most likely a pole of H, which would explain why the bracket's two ends had the same sign.
- **The pattern.** The three dihedral values (R₀, π/ln φ, 3π/(2 ln φ)) are single. Every other value is a doublet:
  the same R in both W-classes of one parity. This is what a form f whose coefficients are not real would give, since
  W sends f to a multiple of the form with conjugate coefficients. It is an observation, not checked further.

## 4. The lane's third and fifth rows: neither is a state in any class

| the lane's value | nearest state, by class | smallest scaled singular value there |
|---|---|---|
| 5.8442600315 | 0.37 in (−1, ±1); 0.68 in (+1, +1); 1.65 in (+1, −1) | 0.12 to 0.33 in the four classes |
| 6.6632356489 | 0.13 in (+1, +1) (π/ln φ); 0.30 in (−1, ±1); 0.83 in (+1, −1) | 0.0035 in (+1, +1); 0.14 to 0.48 in the others |

- **The class (+1, +1) near 6.6632, post hoc.** Over R from 6.60 to 6.72 the smallest scaled singular value dips to
  1.5 × 10⁻⁴ at 6.672 in the first truncation, and to 3.7 × 10⁻⁶ at 6.620 in the second. At the lane's value it is
  3.5 × 10⁻³ and 1.1 × 10⁻².
- **By P2's committed rule, this is no state.** There is no dip below 10⁻⁶ at both truncations and no confirmed
  root. But the second truncation's dip is below the rule's 10⁻⁴, so the rule's "no state at this resolution" is not
  met. The reasons below were written after the output was read.
- **Why it is not read as a state.**
  - A cusp form sits at one R in both truncations, as every confirmed state above does (difference below
    8 × 10⁻¹¹). Where its singular value was computed (R₀; the post hoc's two values), it is 2 × 10⁻¹⁵ to
    3 × 10⁻¹¹.
  - These dips move with the truncation, and their depth changes by a factor of 40.
  - The two sign changes of H there behave as poles: H jumps between values of order 10² to 10³.
- **What it could be.** This class carries continuous spectrum, so a near-solution of its system there is one
  candidate. That is not tested.
- **What the lane computed at these two values cannot be said from here:** its code and outputs are not opened.

## 5. What is disclosed

- **Not blind.** The golden state's class and R₀ were known. So were the earlier referee's results: no state below
  R₀ in any class, its doublets at 6.2149, 6.9639 and 7.4946, no state at the lane's two values, and the lane's count
  of 27 in 15.
- **A scan, not a proof.**
  - The scan covered R from 0.02 to 11, and R = it for t from 0.01 to 0.49. R < 0.02 and t outside [0.01, 0.49] were
    not scanned.
  - The step was 0.01. Two values of one class closer than that would be missed, and so would a value with a pole of
    H in the same step in both normalisations.
  - Lowness rests on the scan finding nothing below R₀ in any class.
  - Simplicity rests on the singular values at R₀.
  - **The card's Weyl-law comparison (its § 3) was not made.** The count equals the lane's 27 in 15, as quoted. Two
    of the lane's rows are not states here, so that equality is no evidence that the list is complete.
- **Why the labels are "computed once".** The earlier referee's collocation scan (the golden-state relay's § 7) is a
  second computation with separate code. Its script and output are not in the record. The sealed run's predictions L,
  S and X, and all four controls, held as written.
- **This note's read-only check** also recomputed by a separate method (particular solutions, with its own K-Bessel
  function). It found:
  - R₀ in (−1, −1), and no state in any class for R from 0.02 to 3.4, nor for R = it, 0 < t < ½;
  - 4.8937812914, 7.4946304901 and 9.2608655254 each in both classes of its parity;
  - no state at either of the lane's values. Near 6.6632, in (+1, +1), it found no dip at all, which makes the
    continuous-spectrum reading of § 4 less likely.

  Its scripts are not in the record, so this is information, not a label.
- **Rule (iii) rejected two states that the post hoc check confirms** (with the same code). The sealed count stands at 25 in
  its own output; 27 rests on the post hoc check.
- **The even classes** are found only through their cusp forms. The continuous spectrum, from ¼, is not computed.
- **Nothing on the firewall list was computed:** no value of τ, no frame at any point, no quantity of P-585 or
  P-638.
- **Commits:**
  - the card and its script: a6b381e01;
  - the output: c13cbc521;
  - the post hoc check: f3c9d62ec, its output 76df0a668.

0 of 19.
