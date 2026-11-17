# B1949 — The lepton–down relation in the frame, level by level: the leptons always share the down quarks' hierarchy exponents, and the level only changes an order-one factor

**Verdict: PROVED** (data-free; R1 to R3 exact and as the card predicted; R4 computed; R5 found in R4's output and tested
after it was read, not blind). Main, 2026-11-15 and 2026-11-17. Step 2 of the goal P-862. Card sealed at ddee39436
before any run. **No measured number is set beside any value here.** 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /Georgi|lepton.down|lepton factor|doublet.s sign|twist negated|charges proportional/: 19 of 1690 arcs on main match (NEGATIVE 7, OPEN 2, PROVED 10); 34 register rows match (DECLINED 3, DONE 22, QUEUED 9)`.
- **What the record already holds:**
  - **order 5:** the leptons are the down quarks transposed, exactly (B1698, B1934);
  - **order 10:** the averaged lepton rows are the down rows with the doublet's twist negated (the SM seat's SM-C13b,
    harvest row 1819);
  - **order 15:** the leptons keep the order-5 down rows and the quarks move (B1942);
  - **the exponents:** B1788's closed form and tropical rule, which frame C obeys on every cell (B1945);
  - **the lepton factor:** the coarser line does not supply it (B1729), nor does E₆'s cubic (B1738).
- **What is new here:** the general identity behind those three (R1), its consequence for the exponents at every level
  (R2, R3), and the order-10 factor as a number (R4, R5).
- **The literature:** the Georgi–Jarlskog factor between the down quarks and the charged leptons (standard).

## The results

- **R1, exact** (`verification/r1_r3.py`). The frame's coupling depends on a sector only through its charges times the
  point. The leptons' charges (−3, 6) are 3·(−1, 2), so

  Y_lep(τ, w) = Y_{(−1, 2)}(τ, 3w),

  with difference 0 in 36 cases (three moduli, six points, both readings). The sector (−1, 2) is the down sector with
  the doublet's sign negated; the down sector itself differs (the lock).
- **R2, the exponents.** e_lep(α) = e_down(3α) for both generations and both readings, exactly, on all 556 slopes of
  denominator up to 30 (B1788's rule). The exponents do not see the sign of a leg.
- **R3, the levels.**

  | level N | lepton exponents over the level |
  |---|---|
  | 5, 10, 20 (3 ∤ N) | the same multiset as the down quarks' at N |
  | 15, 30 (3 ∣ N) | the down quarks' at order N/3, not at N |

- **R4, the order-one factor** (`verification/r4_gj_factor.py`, heights 16, 22 and 28, column x = 0.13). The ratio of
  the level's averaged lepton and down σ₂/σ₃, same reading in both:

  | level | reading S | reading S̃ | first generation (σ₁/σ₃) |
  |---|---|---|---|
  | 5 | 1 exactly | 1 exactly | 1 exactly |
  | 10 | 0.634644 | 1.575687 | tends to 1 (within 1e-6 at height 28) |
  | 15 | no constant: falls with height (2.2e-3, 2.5e-4, 2.5e-5) | the same | S: falls; S̃: 0.55, 0.66, 0.76 |

  - At order 10 the two constants are reciprocal, and they move by 2e-6 between heights 22 and 28.
  - **They are not quite free of Re τ** (`verification/r4_second_column.py`, added after the run was read): on the
    column x = 0.37 they are 0.634449 and 1.576172, a shift of 3e-4. The frame holds its end at the table's top value
    above height 6, and that value still depends on Re τ. The constant as a function of the end is owed.
- **R5, what the order-10 constant is** (`verification/r5_reading_swap.py`, not blind). High in the cusp the leptons
  under S have the down quarks' ratios under S̃, and the reverse, to six digits at height 28.
  - So the order-10 lepton–down factor is the down sector's own ratio between its two readings.
  - It is a cusp-limit relation only: in the bulk the two differ by 6 to 25 %.
  - The control: at order 5 the same-reading copy holds exactly at every modulus.

## What it means

- **In this coupling the level cannot give the leptons a hierarchy of their own.** At every level not divisible by 3
  the leptons and the down quarks have identical exponents. The level changes only an order-one factor: 1 at order 5,
  and at order 10 the factor between the down sector's two readings.
- **At order 10 the first generation is not split at all** in the cusp limit, and the second is split by 0.63 or
  1.58.
- **At levels divisible by 3 the leptons are more hierarchical than the down quarks,** since they see the coarser
  level's exponents.
- **These are relations that hold at every point of the frame, with no selection** (type F in B1948's terms): three
  candidate relations for the goal's step 3, one per level.

## Foreknowledge, disclosed (as the card requires)

- Main recalls the measured lepton–down split: about a factor of 3 in the second generation, with the leptons above,
  and about one third in the first. The record's own B1693 quotes the second-generation pair with its band.
- **By that recall, main expects each of the three relations to fail when compared:**
  - order 5 is already refuted (B1698);
  - order 10 gives at most 1.58 in the second generation and no split in the first;
  - order 15 puts the leptons below the down quarks.
- No comparison is made or banked here. A formal one needs a sealed rule first (P-862, step 3), and it counts this
  recall.

## Not claimed

- Any comparison with data.
- The order-10 constant in closed form, or its exact cusp limit with the true end.
- Anything outside frame C's coupling (B1656's four-channel form with the exact weight).
