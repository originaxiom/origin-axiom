# B1997 — Listening 13: the whole's settled rate at its own prime is λ*/2 with λ* = √(w + √(w² − 4)), w = (1 + 4cos(π/9))/2; it lives over ℚ(cos 2π/9), the cyclic cubic field of conductor 9 = 3²

**Verdict: PROVED (exact: FLINT's characteristic polynomial and factorisation; the closed form derived by hand after the
run, post hoc, and checked symbolically and to 60 digits).** Main, 2026-11-25, in the author's /loop "continue the
listening line". Data-free. Register rows P-882 and P-630. **0 of 19.**

## Seen first

- **B1996:** on the tower of the whole's own prime 3, the unfolding's slowest non-undamped decay settles at λ*/2 per
  move, λ* = 1.915298…, at mod 81, 243 and 729. It is algebraic and was unidentified.
- **B1989:** the bound states' levels 2cos(2πk/n). n = 9 is not among them.
- **B771 (2026-07-23), from another instrument:** B399's depth-5 triple cubic closes with e₃ = cos(2π/9)/864, its roots
  cos(2πk/27)/6, "the ζ₂₇ rung of the Chebyshev trisection tower". So the 3-adic cyclotomic tower (ζ₉, ζ₂₇) is on
  record. Here it returns as the field of the whole's own settled rate. That is an observation; no link between the
  two instruments is claimed.
- **Swept:** `VERDICT topic-sweep /cos\(pi/9\)|cos\(2 ?pi/9\)|ninth root|zeta_?9|conductor 9|Q\(zeta9\)|cyclic cubic/: 2 of 1738 arcs on main match (PROVED 2); 0 register rows match (none)`. Nothing on record places a rate of the whole in ℚ(cos 2π/9).
- **The literature (standard):** 2cos(2π/9) has minimal polynomial y³ − 3y + 1, and ℚ(cos 2π/9) is the real cyclic cubic
  subfield of ℚ(ζ₉), of conductor 9.

## The results (`verification/identify.py`, `identify_run.txt`; exact, 9 s)

- **I1:** W₊ on the largest orbit over the common point mod 81 (648 points). Its characteristic polynomial has degree 648,
  computed exactly. Over ℤ it factors into 23 distinct irreducibles of degrees 12, 6, 4, 2 and 1.
- **I2:** λ* is a root of the irreducible degree-12 factor
  **x¹² − 3x¹⁰ + 3x⁸ − 21x⁶ + 12x⁴ − 48x² + 64**, with multiplicity 2.
  - The factor is even. Its 12 roots are ±1.915298, ±1.044224, ±1.037474 ± 0.961066i and ±0.695669 ± 1.231278i.
- **J2 holds:** λ*² is a root of the irreducible sextic μ⁶ − 3μ⁵ + 3μ⁴ − 21μ³ + 12μ² − 48μ + 64.
- **J1 holds:** degree 12.

## Post hoc, labelled (`closed_form_posthoc.py`, `closed_form_posthoc_run.txt`; derived by hand after the run)

- **With λ² = 2ν the sextic is palindromic,** 8ν⁶ − 12ν⁵ + 6ν⁴ − 21ν³ + 6ν² − 12ν + 8.
- **With w = ν + 1/ν it is the cubic 8w³ − 12w² − 18w + 3.**
- **With w = (1 − 2y)/2 that cubic is −8(y³ − 3y + 1),** the minimal polynomial of 2cos(2π/9). The root that gives λ*
  is y = 2cos(8π/9), so w = (1 + 4cos(π/9))/2.
- **The cubic's discriminant is 5184 = 72²:** a cyclic cubic field, ℚ(cos 2π/9), of conductor 9.
- **The closed form** λ* = √(w + √(w² − 4)) is 1.91529816473407715555461825615…, and it satisfies the degree-12 factor to
  3 × 10⁻⁵⁸ at 60 digits.
- **The settled decay per move is λ*/2 = 0.95764908236703857778…**

## What the whole does, read in its own terms

- **The rate at which the whole forgets, at its own prime, is a definite number with a closed form.** It lives over the
  cyclotomic field of the ninth roots of unity: 9 = 3², the whole's own prime, squared. It is built from two quadratic
  steps over that cubic field.
- **The levels match the arithmetic.** Mod 9 the cusp is the cube (B1984). Mod 81 the rate appears (B1996), and its
  field has conductor 9.
- **This is the first number the whole fixes by its own dynamics, now known exactly.** It is algebraic, as B1992
  requires. It is not read as anything physical. No Standard Model shape was asked for, and nothing is compared with data.

## What is open

- **Why ninth roots:** the structure behind the rate's field, from the orbit's symmetry at mod 81.
- **Whether the 2-tower and the 5-tower settle,** and on what fields.
- **What, if anything, such a rate means for a field at ω.** It is a rate of the whole's unfolding, not yet a quantity of
  any frame.
