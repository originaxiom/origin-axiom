# B2000 — Listening 15: agy-exp's native interactions checked on main — at ω's own point (3,3,3) the whole separates the neutral member from the charged pair, 14 : 5, and the pair stays locked; the fusion laws of the common point's realisations hold exactly

**Verdict: PROVED (exact: sympy on the moves' Jacobians; exact rational counts over the group elements, κ classified with
residual ≤ 1.2 × 10⁻¹⁴ against level gaps ≥ 0.38).** Main, 2026-11-25, in the author's /loop "continue the listening line".
Data-free. Harvest row 2009 (agy-exp's NI-1 and NI-3 VERIFIED); register row P-882. **0 of 19.**

## Seen first

- **agy-exp's X-NATURAL-INTERACTIONS** (`origin/agy/self-consistent-loop-2026-11-11` @ `b41678f5d`, harvest row 2009): its
  claim card read at source for NI-1 and NI-3.
- **Main's line:**
  - B1994: the cyclic exchange C = LR⁻¹ and its charge basis.
  - B1995: at the common point the unfolding treats the three alike, 2/3 each. Open: does anything tell them apart in strength?
  - B1989: the nine levels 2cos(2πk/n), and the golden ones only from 2I.
  - B1993: the integer readings, all over the common point mod 3, from (3,3,3).
- **Swept:** `VERDICT topic-sweep /Jacobian|charge basis|fusion|collision|2I|binary icosahedral|tangent/: 114 of 1741 arcs on main match (NEGATIVE 20, OPEN 11, PROVED 83); 20 register rows match (DONE 12, LEAD 1, Q`.
- **The literature (standard):** projecting an operator onto the commutant of a cyclic group keeps exactly its diagonal in the
  group's eigenbasis. The binary polyhedral groups Q₈ ⊂ 2O and 2I's five inscribed Q₈.
- **Disclosed:** N2's spectrum was worked out by hand in main's message just before this card was written.

## The results (`verification/native.py`, `native_run.txt`)

| point | operator | charge-basis diagonal (q = 0, 1, 2) | commutes with C | eigenvalues |
|---|---|---|---|---|
| (0,0,0) | S₂ = J_L + J_R | 2/3, 2/3, 2/3 | no | 1, (1 ± i√7)/2 |
| (0,0,0) | S₆ = Σₖ Cᵏ S₂ C⁻ᵏ | 2, 2, 2 | yes | 2, 2, 2 |
| (0,0,0) | S₁₂ (with L⁻¹, R⁻¹) | 4, 4, 4 | yes | 4, 4, 4 |
| (3,3,3) | S₂ = J_L + J_R | 14/3, 5/3, 5/3 | no | 1, (7 ∓ √41)/2 |
| (3,3,3) | S₆ = Σₖ Cᵏ S₂ C⁻ᵏ | 14, 5, 5 | yes | 14, 5, 5 |
| (3,3,3) | S₁₂ (with L⁻¹, R⁻¹) | 28, 10, 10 | yes | 28, 10, 10 |

- **N1 holds:** B1995 is reproduced, 2/3 each at the common point.
- **N2 holds:** NI-1 is reproduced, (14/3, 5/3, 5/3) and {1, (7 ∓ √41)/2}.
- **N3 holds as stated, but its worry does not:** S₂ does not commute with C, at either point. Its charge-basis diagonal,
  though, is exactly the C-covariant part, because S₆ = 3 · diag(S₂) in that basis. So reading S₂'s diagonal loses nothing.
  That (3,3,3) is fixed by neither L nor R is harmless here: the readings form an affine space, so its tangent spaces are
  identified canonically.
- **N4 holds:** the covariant unfolding at (3,3,3) is diagonal, with the neutral member at 14 and the charged pair at 5 and 5.
  With the inverse moves it is 28 and 10, 10: the same ratio 14 : 5. At the common point it is 2, 2, 2.

| collision (two-body unless stated) | realisations | collisions | branching of κ |
|---|---|---|---|
| Q₈ | 24 | 576 | −2: 1/3, 2: 2/3 |
| 2O | 96 | 9,216 | −2: 1/12, 0: 3/8, 1: 1/4, 2: 7/24 |
| 2I | 120 | 14,400 | −2: 1/15, −1/φ: 2/15, 0: 2/15, 1: 2/5, φ: 2/15, 2: 2/15 (never −φ, −1, 1/φ) |
| 2I, three-body | 120 | 1,728,000 | {18, 12, 6, 41, 38, 12, 51, 41, 6}/225 over the nine levels in ascending order |

- **F1, F2 and F3 hold:** NI-3 is reproduced exactly. The three-body fractions are Galois-symmetric under φ ↔ −1/φ.

## What the whole does, read in its own terms

- **B1995's open question is answered, and agy-exp is credited.** At the common point the unfolding treats ω's three charge
  members alike. At ω's own point (3,3,3), where the moves no longer act linearly, the unfolding separates the neutral member
  from the charged pair, 14 : 5. The pair stays locked; agy-exp's NI-4 attributes the lock to the reflection.
  - So the whole natively gives **3 → 1 + 2**, and no further split without something that breaks the reflection.
  - This is structure again, with one ratio, 14/5, an exact rational of the linearised unfolding at ω's point. It is not read
    as anything physical.
- **The fusion law depends on which finite group realises the states,** and each case is exact:
  - Q₈ reaches only ±2;
  - 2O adds 0 and 1;
  - 2I reaches the golden levels;
  - three-body collisions in 2I reach all nine levels.

  The collision (A₁A₂, B₁B₂) is NI-3's own operation, averaged over every realisation.
- **Nothing is compared with data.**

## What is open

- **NI-2, NI-4 and NI-5** are registered, not checked. NI-2's one-loop reading is a field-theory premise to be located.
- **Whether 14 : 5 at (3,3,3) persists along ω's orbit** (the Markoff tree), or changes, as the unfolding moves outward.
