# B1733 — THE THREAD'S OWN LINES (P-312, P-336): A THREAD FIXES A FLAT LINE OF ORDER N EXACTLY WHEN N DIVIDES THE LARGER SMITH INVARIANT OF A ∓ I; AT ORDER 5 IT FIXES ONE PAIR {v, 2v}; THE 3-MANIFOLD'S ORIENTATION-REVERSING SYMMETRIES SWAP THE PAIR — YET THE CHOICE IS A REAL BIT, INVISIBLE ONLY AT τ = i

**Verdict: PROVED** (proved, and checked exhaustively where stated). cc (main), 2026-10-23. No data. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /Smith (invariant|normal form)|fixed (flat )?lines?|lines? (a|the) thread fixes|tr ?≡ ?±2|t ?- ?2|coker\(A|X_?1\(5\)|half-turn|glide/ (full text): 151 of 1505 arcs on main match (NEGATIVE 39, OPEN 4, PROVED 106, RETRACTED 2)`;
the matches are mostly "t − 2" in other senses. Bearing on it:
- B1720 (the thread's apex and the lines its monodromy fixes; e.g. the order-28 line of L⁵RLR², ∣det(A − I)∣);
- B1698 (the tick's order-5 lines);
- B1703 and B1728 (the line's order as a quotient of hypercharge);
- B1724 (the readings' SL(2, ℤ) covariance).

The rule was found independently by eight readers of the parked-items sweep (P-309, P-313; audit room), in four forms:
- the trace congruence;
- an eigenvalue argument;
- H₁ of the thread's double branched cover;
- B44's ∣det(A ∓ I)∣ = ∣2 ∓ t∣.

One reader corrected the trace form to the Smith form. **Literature:** the Smith normal form; the modular curves
X₀(5), X₁(5); standard.

## 1. The rule (`verification/the_threads_own_lines.py`, part A)

A thread is a positive word A in L, R; a flat line is w = ατ + b with (α, b) ∈ (ℚ/ℤ)², acted on by
(α, b) ↦ (α, b)γ⁻¹ (the frame's SL(2, ℤ) covariance, whose T-case (α, b) ↦ (α, b − α) is the census's own control).
- **The lines A fixes up to sign** are the points of coker(A − I) and coker(A + I). These are finite abelian groups
  ℤ/d₁ ⊕ ℤ/d₂ (d₁ ∣ d₂) of orders ∣2 ∓ t∣, t = tr A.
- **So a line of exact order N is fixed iff N divides d₂(A − I) or d₂(A + I)**, the exponent of either group.
- **The trace rule** N ∣ t − 2 or N ∣ t + 2 is this rule's squarefree case: a squarefree N divides d₁d₂ iff it
  divides d₂.
- **Checks:** brute force over (ℤ/N)² for every class to length 10 (241 classes) and N ≤ 30, 6 989 cases. The Smith
  rule has 0 mismatches. The trace rule fails 153 times, all at non-squarefree N (e.g. L⁸R² at N = 16, 20); 0 at
  squarefree N. Orders 5 and 10 are squarefree, so the trace rule is exact on B1726's lines.

## 2. The order-5 pair, and the 3-manifold's orientation (parts B, C)

- **The pair.** When 5 ∣ d₂ and 5 ∤ d₁ the 5-torsion is cyclic, and the fixed order-5 lines are exactly ±v and ±2v:
  99 of 99 such classes. Multiplication by 2 commutes with every A, so nothing built from the thread alone can choose
  between them. This is the deck involution of X₁(5) → X₀(5). When A ≡ ±I mod 5, all twelve order-5 lines are fixed
  (L⁵R⁵).
- **The orientation.** Over B1720's classes with exactly one order-5 pair, take every symmetry g of A in GL(2, ℤ)
  (gAg⁻¹ = A^e):
  - every g with e·det g = −1, i.e. reversing the mapping torus's orientation, swaps v ↔ 2v (28 of 28);
  - every g with e·det g = +1 fixes the pair (188 of 188).
- **The two kinds of reversing symmetry.** Glides have det g = −1 and e = +1; on the tick g² = A, e.g.
  g = [[−2, 1], [−1, 1]]. Half-turns have det g = +1 and e = −1.

## 3. What the bit is (parts D, E)

- **The frame is mirror-covariant:** ratios(τ, α, b) = ratios(−τ̄, −α, b) to 1.0 × 10⁻¹¹ at six random points. The
  unchanged line at −τ̄ moves them by 0.8–6.4, except one self-mirror line.
- **So a reversing symmetry g relates (P, v) to (g·P, 2v).**
  - A glide has no fixed point: it shifts the axis by half a period while reflecting. So v at P and 2v at P remain
    different outcomes.
  - A half-turn fixes a point Q on the axis, and there covariance forces ratios(Q, v) = ratios(Q, 2v). On the tick, Q
    reduces to τ = i, and v and 2v agree to 4.3 × 10⁻¹⁴.
- **At B1720's apexes v and 2v differ** by 4.7 (LR) to 8.7 (L⁵R) in log over the sector ratios.
- **So the bit is real.** The orientation pairs (P, v) with (g·P, 2v), but the two outcomes stay distinct
  everywhere except at the half-turn's point. That point is τ = i, where the frame's hierarchy degenerates (B1667,
  B1657). It is not a naming convention.

## 4. What it means (labelled readings)

- **For the selection problem** (L219, L253; the completion map's C1): a thread fixes τ (its apex) and its own lines,
  and on the order-5 and order-10 lines where B1726's fit lives, the line up to one real bit. "Which τ" and "which
  line" become "which thread", plus that bit.
- **For P-312's sealed test:** the bit must be declared in advance, or both of its values counted in the calibration's
  menu.

## Files

- `verification/the_threads_own_lines.py` → `the_threads_own_lines.json`, `the_threads_own_lines_run.txt`.
- The lock: `tests/test_b1733_the_threads_own_lines.py`.
