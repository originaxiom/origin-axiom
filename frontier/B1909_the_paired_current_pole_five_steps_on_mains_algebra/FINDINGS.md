# B1909 — The physical lane's paired current pole: five of its seven steps on main's own algebra, and what the other two need (P-749 (e); R80-5)

**Verdict: OPEN** (steps 1, 2, the arithmetic of 3, 5 at the level of roots, and 7 are computed exactly on main and hold;
the analytic half of step 3, step 4, the operator's part of step 5, and step 6 need the lane's operator written out on
main, which is the plan's WP-2.1). cc (main), computed 2026-11-12, landed 2026-11-13 (S306p). The lane's proofs were read
through main's binding-minimum mask; none of its code was run. No data; the pole's value and the couplings' common size
are not evaluated, and nothing is compared with a measured value. **0 of 19.**

## 1. The answer first

- **The lane's statement** (its proof of 2026-11-08, in main's words): in the supplied parent (compact E₈, the coherent h4
  lift, η = O, χ = 0, the lane's kinetic metrics and graph domain) the charged vectors at the pole m₀² = 7/(2ℓ²) are two
  complex species, not one: w_L = z₊ (charge +1, grade −2) with a left quark current, and w_R = J z₋ (charge +1, grade +2)
  with a right one, and |g_R| = |g_L| in this background. So a claim of chirality must account for the whole pole. Its
  scope is this parent only, at tree level.
- **What main has computed, exactly, and found to hold:**
  - **Step 1, the constant.** With the lane's operator form P_v = 2k†k, k = (D̄_A, ad q, ad r), q = E₊/(2ℓ), r = E₋/(2ℓ), the
    potential (1/(2ℓ²))(F₊E₊ + F₋E₋) on all sixteen weight vectors of V(3/2) ⊗ V(3/2) has the grade −2 plane as an
    eigenspace with the value 7/2 (units 1/ℓ²): the lane's 7/(2ℓ²). The conjugate form takes the same value at the
    opposite weights, vector by vector, so the two charges' spectra match term by term; the two forms differ by μ/ℓ², the
    curvature's term. Planted: on V(1/2) ⊗ V(1/2) no weight has 7/2.
  - **Step 2, the transitions.** A = iασ_x, D = diag(i, −i), B = DA are unitary, square to −1 and have commutator −1, for both
    charges; the image is the quaternion group of order 8, irreducible; T = 1 or diag(1, −1) intertwines the two charges.
  - **Step 3, its arithmetic.** An irreducible flat bundle with −1 at the puncture, half-weights, has degree 1 after the
    twist; an indecomposable bundle of rank 2 and degree 1 on an elliptic curve has exactly one section (Atiyah), so h⁰ = 1.
    The no-splitting arithmetic is checked.
  - **Step 5, at the level of roots, on main's own E₈** (the 240 roots in eight coordinates; D5 on 1..5, A3 on 6..8; the two
    Spin5 on (1, 2) and (3, 4), grades m = 2x₁ + x₂, n = 2x₃ + x₄): a pair of grades and an A3 weight name exactly one root,
    in both modules. The non-zero products of a vector component with a down component are exactly a with v′ at (0, −2) and
    b with u′ at (−2, 0), in (10, 6), for all twelve ordered pairs of different A3 weights, and none for equal ones; the
    conjugate module has the same pattern. That is the lane's "C b d_u and C a d_v".
  - **Step 7, the residue.** The residue matrix on the two currents is diag(|g_L|², |g_R|²) under any unitary change of the two
    vectors: rank two, positive.
- **What is open, and why.** That a profile with D̄z = 0 exists and lies in the domain (step 3's analytic half); that D̄*D̄
  is the whole of the first term on such a profile in the lane's weighted adjoint; that compact conjugation commutes with
  the operator (step 4); that M kills the products, and their norms (step 5's operator part); the equal-norm step (step 6).
  Each needs the lane's operator P_v, its mass map M and its kinetic metric written out and re-derived on main: the plan's
  WP-2.1, the first step of the package on the curved action. **R80-5 cannot close before it**, and this arc says so in
  place of a fifth carry.

## 1a. Seen first

`VERDICT topic-sweep /paired.{0,20}pole|current pole|P-749|weak current|WP-3.3/: 0 of 1648 arcs on main match (none); 3
register rows match (DONE 1, QUEUED 2)`. The pole has no arc on main before this one; P-749 (e) is the row. **Literature:**
Atiyah's classification of vector bundles on an elliptic curve (an indecomposable bundle of rank 2 and degree 1 has one
section) and the Mehta–Seshadri correspondence for parabolic bundles are used, not proved; that every non-zero bracket of
root vectors in a simply-laced algebra has the same size in an orthonormal frame is used, not proved.

## 2. Assumed, and said

- The two Spin5 are the block ones of Spin10, which is what the lane's "(4, 4)" and "(5, 1) + (1, 5)" describe.
- The charges are not labelled on main's E₈ here: the lane's charge is T₃ + Y in its own frame, not yet written on main's.
- That the cusp norm allows exactly a simple pole and no more is the lane's, not checked.
- "S²V" in the lane's text is the square of the spin bundle times V, not the symmetric square of V (main's first reading
  was the second, and was corrected before anything was written).

## 3. What the pole does not settle

The pole is computed at one supplied background, and that background is kept by the object's own reversing involution (it
acts as complex conjugation here, carrying the left current's vector to the right one at the same mass). So the pole cannot
decide whether the object has a hand. Main's question on that is a different one: whether a weight on histories, derived
and not chosen, reads the parity of the number of ticks.

## 4. The checks (`verification/`, exact)

| | what | checks | planted |
|---|---|---|---|
| `the_transition_matrices.py` | step 2, step 3's arithmetic, step 7 | 16, none failing | three |
| `the_pole_constant.py` | step 1 | 7, none failing | one |
| `the_brackets_at_root_level.py` | step 5 at the level of roots | 9, none failing | two |

Each script lists its checks in its own `.json` and prints them in its `_run.txt`. The lock: `verification/test_b1909_the_paired_pole.py`.

## Reproduce

```
cd frontier/B1909_the_paired_current_pole_five_steps_on_mains_algebra/verification
python3 -B the_transition_matrices.py; python3 -B the_pole_constant.py; python3 -B the_brackets_at_root_level.py
```
