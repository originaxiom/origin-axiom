# B1304 — THE 2-ADIC TOWER ENDS AT Y₁₂: Y₂₄'s support is Y₁₂'s pulled back — the same 97 letters, the same 34 752 Standard-Model lines, the same 768 one-triplet vacua — so the closing that thins the colour triplets is Y₁₂ and no other; and the matrix product of the criterion is unipotent on every non-trivial character, h¹ being the vanishing of its rank-one nilpotent part

**Date:** 2026-09-08 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (the 2-primary subgroup of Y₂₄'s character group, 1 024 characters, under B1303's criterion; the alphabet and the lines enumerated; Y₁₂ reproduced as the control; the unipotent structure proved in one line and confirmed over 1.98 million characters) · **Price: unchanged** · **Numbering:** B1304.

## Why this arc — the last open question of the tower

B1303's law settled the odd part of every closing's support: new odd support only at odd levels, so every even level's odd
support is Y_{n/2}'s. The 2-adic part was left as an observation from three points — Y₃'s family characters, Y₆'s 24 of
order 8, Y₁₂'s 96 of order 16 — with the natural question whether Y₂₄ adds order-32 letters and thins the colour triplets
further, or differently, than Y₁₂ (B1301, B1302). Y₂₄ has 10 749 957 120 characters, beyond even the criterion in one
session, but its 2-primary subgroup is (ℤ/32)² = 1 024 characters, and by the law its odd support is empty (Y₁₂'s is), so
the whole support of Y₂₄ lives in those 1 024 and the criterion decides it in seconds.

## 1. Y₂₄ ((a))

`two_adic_lines.py` runs the criterion on the 2-primary subgroup of Y_n (the Smith coordinates restricted to the 2-parts
of the two cyclic factors), finds the family characters (the order-2 positives), the alphabet K3, and enumerates the lines
(ψ_Q, ψ_u, ψ_L) ∈ K3³ with B1300's weight table — everything stays inside the 2-primary subgroup — with every multiplet's
survival, and hands the survival patterns to B1302's vacuum census.

| | Y₁₂ (control) | **Y₂₄** |
|---|---|---|
| 2-primary subgroup | (ℤ/16)², 256 | (ℤ/32)², 1 024 |
| support | 123 = 3 + 24 + 96 (orders 2, 8, 16) | **123 = 3 + 24 + 96 (orders 2, 8, 16) — no order 32** |
| K3 · K2 | 97 (1 and 96 of order 16) · 27 | **97 · 27** |
| three generations · SU(5) broken · SM vacua · full | 190 849 · 181 440 · 34 752 · 3 264 | **the same four numbers** |
| D totals on the SM lines | 1 on 31 488, 3 on 3 264 | **the same** |
| survival patterns · one-triplet lines (n_T = 1, n_H = 3) | 265 · 768 | **265 · 768** |

**Y₂₄'s support is Y₁₂'s, pulled back along Y₂₄ → Y₁₂, and nothing else**: no new 2-adic support at level 24, and
therefore the same alphabet, the same Standard-Model lines, the same thinning of the colour triplet to one generation on
31 488 lines, and the same 768 one-triplet vacua with the same best configurations (B1302's census rerun on Y₂₄'s
patterns is identical, entry for entry). The 2-adic new supports of the tower are Y₃'s (order 2, the family), Y₆'s
(order 8) and Y₁₂'s (order 16) — and then no more. With B1303's law this closes the description of the tower: the
support of every level is the pullback of its divisors' new supports, new odd support arising at odd levels from the
half-deck's eigencharacters and new 2-adic support at 3, 6 and 12 only.

*Remark.* 6 and 12 are exactly the indices at which the Fibonacci numbers have no primitive prime divisor (Carmichael's
theorem, cited not verified here: F_n has a primitive prime divisor for every n except 1, 2, 6, 12; F₆ = 8, F₁₂ = 144).
The levels whose torsion brings no new odd prime are the two that bring new 2-adic support instead. Whether this is a
coincidence or the 2-adic face of the same law is registered, not claimed (L210).

## 2. The unipotent structure ((b))

For a non-trivial character ψ the Fox matrix J = P − I of B1303's criterion kills the vector (ψ(a) − 1, ψ(b) − 1), so it
has rank ≤ 1 and P has the eigenvalue 1; and det P = Π_k x_k = ψ(Σ_k Φ^k a) with Σ_k Φ^k = (Φⁿ − I)(Φ − I)⁻¹, where Φ − I
is unimodular (det = −1), so the sum lies in the image of Φⁿ − I and ψ kills it: **det P = 1**. Hence P is unipotent on
every non-trivial character, P = I + N with N nilpotent of rank ≤ 1, and **h¹(Y_n; ψ) = 1 iff N = 0**. The census
(`unipotent_census.py`, exact modulo two primes) confirms it on all 1 984 917 non-trivial characters of Y₅, Y₆, Y₉, Y₁₀,
Y₁₂, Y₁₅: every one has trace 2 and determinant 1, the trivial character alone does not, and the identity occurs exactly
on the supports (20, 27, 147, 20, 123, 2 723). So the law of B1303 is a statement about when a rank-one nilpotent
built from n Galois-related factors vanishes — the form in which a proof should be sought (L210(iv)).

## 3. What this settles

- **The closing that thins the triplets is Y₁₂, alone in the tower**: Y₆ has no Standard-Model lines, Y₂₄ has Y₁₂'s, the
  odd-alphabet closings keep D everywhere (B1300, B1303), and there is no other 2-adic level. The one-triplet vacua of
  B1302 — one vector-like generation, two Higgs doublets, no exotic triplet — are Y₁₂'s and its pullbacks', and no
  closing does better at tree level.
- **The tower is described**: supports, alphabets and Standard-Model lines of every closing follow from the half-deck's
  eigencharacters at odd levels and the three 2-adic levels 3, 6, 12.
- Vector-like throughout (B1260); 0 of 19; price unchanged.

## Controls (MB12)

- **Control level:** Y₁₂ through the same 2-primary route reproduces B1301's support and alphabet, B1301's lines and
  survival census, and B1302's vacuum census, entry for entry.
- **The odd part of Y₂₄** is empty by B1303's law (an even level pulls back Y₁₂'s odd support, which is empty); the
  criterion on the full group is not run (10¹⁰ characters), and the claim "Y₂₄'s support is Y₁₂'s" rests on the law for
  the odd part and on the computation for the 2-part.
- **The unipotent structure** is a proof, with the exact census as its check.
- **E70-class:** additive character algebra and 2×2 modular products only.

## Verification

- `verification/two_adic_lines.py` — Y₁₂ and Y₂₄: the 2-primary support, alphabet, lines, survival census and B1302's
  vacuum census; 21 s; SELFTEST PASS; run record `two_adic_lines_run.txt`.
- `verification/unipotent_census.py` — trace and determinant of the product on every character of Y₅, Y₆, Y₉, Y₁₀, Y₁₂,
  Y₁₅; run record `unipotent_census_run.txt`.
- Lock `tests/test_b1304_the_two_adic_tower.py` (fast).
- Depends on B1303 (the criterion and the law), B1302 (the vacuum census), B1301 (Y₁₂'s support and lines), B1300 (the
  weight table).
