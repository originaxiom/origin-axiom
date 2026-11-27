# SM-R384 — a principle for α = 2/5 and odd b/10 in B1934's terms, stated before its check, or an observer choice

*Card of the SM seat, 2026-11-25, for register row P-384 (main's M53). Written with its script
(`relays/sm_r384/run.py`, SHA-256 d0c30fbf62479829) before the script is run on the real case. The script was smoke-run
only at the level p = 7, outside the test population, and printed nothing but its completion. Data-free: the check is
an exact enumeration of lines; no measured number is read, loaded or printed.*

## 0. The question

Main's M53: state a principle for α = 2/5 and odd b/10 in B1934's terms before any check, or declare it an observer
choice. A line here is a torsion point v = (a, b) of the fibre, taken up to sign, with a the coefficient that the
cusp ∞ sees (the record's slope α) and b the offset. The class asked about is

  K = {(2/5, b) : b = 1/10, 3/10, 1/2, 7/10, 9/10}, five lines of order 10.

## 1. What the record already says (read first)

- **B1753 (P-340, P-384):** the five-ality rule (orders divisible by 5: 12 lines of order 5, 36 of order 10) passes,
  but the referee showed it is mostly a pick. Only the order-10 lines (2/5, 1/10) and (2/5, 1/2) carry rows below the
  bar. Every rule containing them passes ("divisible by 2" as well as "by 5"), none without them. Order 5 alone fails.
- **P-384's later notes:**
  - B1755: at orders 10, 15 and 20 the good lines all have α = 2/5. The unit-twist reading's further slopes at order 15
    (1/15, 4/15, 11/15, 14/15) carry nothing, so that reading fails as a cross-order rule.
  - B1786: α = 2/5 alone carries at orders 25 and 30. The slope stays an input, selected by the discrete condition
    ‖3α‖ = 1/5, read from data.
  - B1784: a "data-free selection" (the agy lane's) described the class without selecting it.
  - W171: in the surface frame the class is removed, not selected.
- **B1934:**
  - Level 5's Weil representation is an even 3 plus an odd 2, with two Galois-conjugate forms (k = 1: T-exponents
    {0, 1, 4}; k = 2: {0, 2, 3}).
  - The hand is the golden field's quadratic character, the Legendre symbol mod 5, read on the act's eigenvalue at the
    mark (1, 2).
  - Hypercharge mod 5 is SU(5)'s centre. The Higgs has 6Y = 3.
  - The lepton pair copies the down pair exactly at orders dividing 5. The leptons separate only through a second prime.
- **B1943:** the act LR fixes, up to sign, exactly one line of order 5, {k(1, 2)/5}, and no point of any other order.
  RL fixes another, {k(1, 3)/5}.
- **B1976 to B1979:** order 30 on the act's line (5-part on {k(1, 2)/5}). The act fixes the 5-part and does not fix
  the 6-part (B1977, B1978). The menu is 12 converged classes (B1979).
- **SM-C23** (`relays/SM_C23_JOINT_COVARIANCE.md`): frame C is covariant when the modulus and the point move together.
  So reading the point vγ at ∞ is reading v at the cusp γ(∞). Choosing a line is choosing a cusp.
- **SM-C24** (`relays/SM_C24_THE_WHOLE_INSTRUMENT.md`): at order 30, on the cusps that see the 5-part (a has a 5-part),
  the whole level plays the act's line's 12 classes, in the same proportions. Those classes are the level's own.

## 2. The candidate principle, stated before any check

**Π (in B1934's terms).** The object's line is read at:
1. **the least level containing B1934's level 5 at which the lepton copy breaks.** That is a second prime is present,
   and the smallest such level is taken.
2. **a cusp at which the Higgs's twist is a unit of SU(5)'s centre.** The Higgs has 6Y = 3. Its phase on the line is
   e(3a), and Π asks for 3a ≡ ±1/5 mod 1.

Clause 2 has a Galois-invariant shadow: 3a is a non-zero element of (1/5)ℤ/ℤ. Clause 2 itself does not have that
invariance. In the language of B1934 § 2, clause 2 says the Higgs's twist 3·(5a) mod 5 is a square, so its golden
character is +1. Equivalently, the golden character of 5a is −1, because 3 is a non-residue.

**The sources of each clause.**
- Clause 1 rests on B1934 § 3 plus a minimality postulate, "the least such level". Nothing on record derives the
  minimality.
- Clause 2's Galois-invariant part rests on B1934 § 3 (hypercharge mod 5 as the centre).
- Its sign (±1 rather than ±2) rests on nothing structural on record. B1934's two Weil representations and B1923's
  twin exchange the two signs.

**What I argue before running (to be confirmed or refuted by the enumeration, not assumed):**
- **(R1) The offset is not a separate choice.** With a = 2/5 the order is 10 exactly when b is an odd tenth. The map
  T: (a, b) ↦ (a, b − a) (B1733's row convention) moves b by 2/5, so the five lines of K form one ⟨T, −I⟩-orbit. K is
  one cusp of the level-10 instrument.
  - *Inference, for frame C only (SM-C23):* the five offsets are then one line read at τ, τ + 1, …, τ + 4. Which offset
    carries is a condition on Re τ mod 5. This is consistent with W163's "a relation between Re w and τ, not a rule on
    the offset alone".
  - B1753's carriers were found with B1741's instrument, whose joint covariance is not shown. This reading does not
    transfer to it without that check.
- **(R2) α = 2/5 against α = 1/5 is one Galois bit.** Multiplying every point by a unit u of ℤ/10 commutes with
  SL(2, ℤ), with the act and with T. It preserves orders, cyclic subgroups (so the act's line), whether a has a 5-part
  (SM-C24's visibility), and every condition built from those alone. With u = 7, K is sent to its twin
  (1/5, odd/10). So any rule built only from those objects selects K together with its twin, or neither.
  - What separates them is a choice of square class in ℤ/5, the sign in clause 2.
  - On record, only the analytic norm ‖3α‖ = 1/5 discriminates (B1786). B1786 read that norm from data, and B1755
    refuted it as a cross-order rule.
- **(R3) The act's line does not select K.** K's 5-parts are (2/5, 6b) for b ∈ K, running over all five points
  (2/5, k/5). Only (2/5, 4/5), which comes from b = 3/10, lies on the act's line {k(1, 2)/5}. Neither carrier's does.

## 3. Rival principles and plants (all evaluated by the same code)

| rule | its source | what it must show |
|---|---|---|
| divisible by 5 (PLANT) | B1753's rule | selects more than K |
| divisible by 2; order 10; order 5 | B1753's referee | more than K; order 5 none of K |
| 5-part on the act's line (all orders; order 10) | B1943, B1976 | contains one of K, no carrier |
| 5-part = ±mark (1, 2)/5; = ±2·mark | B1934 § 2 | none of K; one of K |
| cusp sees the 5-part; also not the 2-part | SM-C24 | more than K; K and its twin |
| χ(5a₅) = −1; = +1 | B1934 § 2 | each of these rules selects more than K |
| unit twist 3a = ±1/5, alone | B1934 § 3, P-384's reading | more than K (order 5 and the reach) |
| non-zero twist (Galois-invariant) | B1934 § 3 | more than K |
| least level breaking the copy | B1934 § 3 | all 36 lines of order 10 |
| **Π = least level ∧ unit twist** | the candidate | exactly K |
| Π_inv = least level ∧ non-zero twist | the shadow | K and its twin, 10 lines |
| Π with h = 1 in place of the Higgs's 3 (PLANT) | a wrong charge | the twin, none of K |
| DESCRIPTION: order 10 ∧ a = ±2/5 (CONTROL) | none (a description) | exactly K |

The control shows that selecting K exactly is necessary but not sufficient. A description also selects it (B1784's
lesson). Whether a rule is a principle is decided by the source column, not by the enumeration.

## 4. What is computed (`relays/sm_r384/run.py`)

- **The universe:** all lines of order ≤ 12. The record's 266 (B1749, B1753) are expected, including 0 and the three
  2-torsion points.
- **For each rule:**
  - the number of lines selected, the number in K and outside K, and the carriers selected;
  - whether the selection is exactly K;
  - whether it is invariant under scaling by the units of ℤ/N;
  - its order-10 lines;
  - its reach at orders 15, 20, 25 and 30 (the number of lines and their slopes).
- **For K:**
  - its unit closure;
  - the ⟨T, −I⟩-orbits (cusps) of the order-10 lines, marking K and the cusps that see the 5-part.
- **The least level:** the least multiple of 5 at which B1934's own `transposed_orders` says the copy breaks.
- **Imported unchanged:** the act's line from B1943's `fixed_up_to_sign`, and the charges and Legendre table from
  B1934's module (main's checkout passed as argv[1]).

## 5. Expectations, written before the run

| | expectation | prior |
|---|---|---|
| E0 | the universe has 266 lines, 12 of order 5 and 36 of order 10; K is in it; both carriers are in K | 95% |
| E1 | PLANT: "divisible by 5" selects 48 lines ⊃ K, not exactly K; "divisible by 2" ⊃ K, not exactly | 97% |
| E2 | the act's line selects 8 lines (2 of order 5, 6 of order 10), one of K, (2/5, 3/10), no carrier | 85% |
| E3 | ±mark selects none of K; ±2·mark selects one of K, (2/5, 3/10) | 85% |
| E4 | K is not unit-invariant; its unit closure is K ∪ (1/5, odd/10), 10 lines | 90% |
| E5 | every rule built without the sign or a named point is unit-invariant and not exactly K | 90% |
| E6 | the 36 lines of order 10 form 8 cusps; K is exactly one; 4 of the 8 see the 5-part | 85% |
| E7 | the least level is 10 | 97% |
| E8 | Π selects exactly K; Π_inv selects 10 lines; the h = 1 plant selects the twin and none of K | 90% |
| E9 | the unit twist at order 15 selects the slopes ±{1/15, 2/5, 11/15}, a superset of the slope B1755 found | 85% |
| E10 | χ(5a₅) = −1 at order 10 selects the slopes ±1/10 and ±2/5, two cusps | 80% |

## 6. What will be declared (the decision rule, sealed)

- **If E4, E5 and E8 hold,** the card's answer is:
  - **b odd/10 is not an independent choice.** Given a = 2/5 and order 10 it is forced: K is one cusp (R1).
  - **Order 10 has a candidate principle in B1934's terms,** clause 1. It is stated as a candidate resting on a
    minimality postulate, which is not derived.
  - **α = 2/5 over α = 1/5 is one Galois bit.** No unit-invariant object of B1934, B1943 or SM-C24 fixes it, and the
    one discriminator on record (‖3α‖ = 1/5) was read from data. The bit is declared an observer choice: CHOSEN, one
    bit, counted on the board.
  - P-384's remaining content is then that bit, plus which of K's offsets carries. Under SM-C23 the latter is a
    condition on τ, an inference for frame C.
- **If E2 fails because the act's line selects exactly K** (prior 3%), B1943 answers P-384 and no choice is declared.
- **If E4 fails** (K is unit-invariant), R2 is void, the declaration is withheld, and the card is re-read.
- **If any other rule** that is not unit-invariant and has a source on record selects exactly K, it is reported as a
  candidate principle for main. It is not banked here.

## 7. Not checked

- No rate, value or row of any frame is computed. Whether K is the cusp the frame's readings prefer is not asked.
- Joint covariance of B1741's instrument (B1753's) is not shown. R1's cusp reading is checked only combinatorially.
- The minimality in clause 1 is not derived. Why the second prime is 2 rather than 3 (order 15, B1755) is not
  answered by anything here beyond "least".

## 8. Files

The script `relays/sm_r384/run.py`; in phase 2 its output r384_run.txt and r384_results.json in the same folder, the
page relays/SM_R384_A_PRINCIPLE_FOR_THE_TWO_FIFTHS_CLASS.md and the claim card under relays/claims/.
