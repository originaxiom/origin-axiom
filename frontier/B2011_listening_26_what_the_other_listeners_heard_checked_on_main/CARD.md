# B2011 — Listening card 26: what the other listeners heard, checked on main — agy's C60 and agy-exp's ninth-roots card

Written 2026-11-26, before any run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why

- **The author asked** how we know we listened properly and nothing escaped our ears. Main's answer: we don't yet. The locks
  show that what we heard is there; nothing shows we heard everything. The first guard named was to read the other
  listeners before computing again.
- **Three deliveries arrived since the pins.** Two bear on the listening line:
  - **agy's C60** (`origin/agy/cusp-action-2026-11-20` @ `5bdaced13`): a proof of the halving for every 3ᵏ, built from a
    bipartition, a gauge γ and an intertwiner J_k; exact polynomials at mod 243; a level, mod 135, where ℤ₆ survives and
    C fixes 3 points yet the halving fails. If so, B2005's "the halving holds exactly where ℤ₆ survives" fails as a law
    outside the eleven levels it ran.
  - **agy-exp's X-NINTH-ROOTS-AND-CHIRALITY** (`origin/agy/self-consistent-loop-2026-11-11` @ `4c1d39aa3`): one closed
    formula for the slow decay at the primes 3, 5 and 7 (a honeycomb Bloch law), the mod-81 orbit as a honeycomb torus, the
    outward flow of B2000's 14 : 5, and the leading term of (LR)³ − id.
  - agy-002's A2-WHOLE-INSTRUMENT (@ `2d2ac11a4`) is on the order-30 line, which is on hold; it is registered, not checked
    here.
- Each claim is rebuilt on main's own code (B1996's orbits over the common point, B2002's sectors, B2000's linearisation),
  not by running the seats' scripts.

## The checks

From agy's C60:
- **A1, mod 135:** the orbit of (3,3,3); its size; C's fixed points; whether ρ factors through G₁₃₅ (it does if reduction mod
  27 maps G₁₃₅ onto G₂₇, through which ρ factors by B2005); the exact sector polynomials; the charged roots not paired with
  half the neutral ones (the quotient of the charged polynomial by its gcd with p_neutral(2x)/2^d).
- **A2, mod 45:** the gcd of p_neutral(2x)/2^d and the charged polynomial.
- **A3, mod 243 exactly:** p_neutral(2x) = 2^d (x² − 9) x S(x) over ℤ, by characteristic polynomials modulo enough primes
  to fix every coefficient (each coefficient bounded by 7^d, since ‖W‖ ≤ 6).
- **A4, the proof's ingredients, rebuilt and run at k = 3 to 7 (mod 2187), and 8 if the time allows:**
  ε(3a, 3b, 3c) = abc mod 3 splits the orbit in equal halves that every move exchanges; C's three fixed points lie in O⁺
  for k ≥ 3; γ rises by 1 under C and under σᵢσⱼ on O⁻; J_k keeps O⁻, commutes with the six σᵢσⱼ, and J_k C = τ C J_k.
- **A5:** the orbit is the whole congruence set: |O_{3ᵏ}| = 8 · 3^{2k−4} equals the number of v mod 3ᵏ with every coordinate
  ≡ 0 mod 3, abc ≢ 0 mod 3, and x² + y² + z² − xyz ≡ 0 mod 3^{k+1}.
- **A6:** the order of [C⁻¹, σ]³ on the orbit at mod 27, 81 and 243.
- **A7:** P₆(x) = x⁶ − 60x⁴ + 1008x² − 4672 divides p_neutral at mod 81, and its largest root is 2√(5 + 4cos(π/9)).

From agy-exp's card:
- **B1, the honeycomb law:** Λ(M)/2 = √(w_M + √(w_M² − 4))/2, with w_M = (1 + 4cos(π/M))/2, against main's own slowest decay of
  W₊ = P_L + P_R on the largest orbit over the common point, at mod 125 (M = 5), 625 (M = 25) and 343 (M = 7), recomputed
  to 10⁻¹⁰ (main recorded 0.8389, 0.9947 and 0.928).
- **B2, the outward flow:** on ω's tree, the C-average of B2000's covariant linearisation gives neutral : charged
  = (4s + 6) : (s + 6), s = x + y + z (14 : 5 at (3,3,3)).
- **B3, the honeycomb torus:** the largest orbit over the common point mod 81 (648 points) is isomorphic, with L and R, to
  {0,1} × (ℤ/18)² under the card's L and R; ⟨L², R²⟩ is abelian of order 324.
- **B4:** the lowest-degree part of (LR)³ − id is (x(z² − y²), y(x² − z²), z(y² − x²)).

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| A1 | mod 135: 2880 points, C fixes 3, ρ factors, and exactly 10 charged roots go unpaired, the roots of (x² − 2x − 2)(x² + 2x − 2)(x³ − 3x − 1)(x³ − 3x + 1) | 0.7 |
| A2 | mod 45: the gcd is x²(x − 2)(x + 2) | 0.7 |
| A3 | mod 243: the halving identity holds exactly over ℤ | 0.9 |
| A4 | every ingredient holds at every k run (k = 4 to 7 for J_k) | 0.75 |
| A5 | the orbit is the whole congruence set at k = 3 to 7 | 0.65 |
| A6 | [C⁻¹, σ]³ is trivial at mod 27 and 81 and of order 3 at mod 243 | 0.8 |
| A7 | P₆ divides p_neutral at mod 81 with largest root 2√(5 + 4cos(π/9)) | 0.85 |
| B1 | the law gives main's slowest decay at mod 125, 625 and 343 to 10⁻¹⁰ | 0.7 |
| B2 | the ratio is (4s + 6) : (s + 6) identically | 0.85 |
| B3 | the isomorphism holds and ⟨L², R²⟩ is abelian of order 324 | 0.75 |
| B4 | the lowest-degree part is as stated | 0.8 |

## What it means

- **If A1 holds:** B2005's correlation was a fact about the eleven levels it ran, not a law; B2009's stabiliser condition,
  not the survival of ℤ₆, is what decides. Main's statement of 2026-11-26 ("the halving fails exactly at the levels where the
  character doesn't survive") is then wrong and is corrected in the record.
- **If A3 to A5 hold:** the seat's all-k argument has every computed ingredient checked to k = 7. Whether it is a proof for
  every k turns on the induction's algebra, which is read, not run; the reading is recorded as such.
- **If B1 holds:** the slow decay at the primes 3, 5 and 7 follows one law that main did not hear: something that escaped
  our ears, heard by another listener.
- **Nothing is compared with data.**
