# R36 — second batch of cheap recomputes (B331, B333, B335, B406, B486, B488/B489, B509/B510, B520)

Script `r36.py` (SnapPy, PARI via cypari, pure Python; ~1 min). Rows from `load_bearing_unrecomputed.tsv`.

| row | claim | R36 | verdict |
|---|---|---|---|
| B331 | χ₂₇(g) = 0 for the order-3 element g = [[0,−1],[1,−1]] of the principal SL(2) | 27 restricted to the principal SL(2) is V₁₆ ⊕ V₈ ⊕ V₀; characters at diag(ω, ω²): −1, 0, +1; sum 0 | MATCH |
| B333 | h(−15) = 2; "14 of the 123 fundamental discriminants down to −400 have h = 2" | h(−15) = 2 ✓. **PARI: 122 fundamental discriminants in [−399, −3], 16 with h = 2** (−15, −20, −24, −35, −40, −51, −52, −88, −91, −115, −123, −148, −187, −232, −235, −267). B333's `fundamental_discriminants()` tests `(−m) % 4 ∈ {2,3}` instead of `m % 4` for D = 4m, so it **includes 21 non-fundamental discriminants** (−12, −28, −44, −60, …) and **excludes 20 fundamental ones** (−4, −20, −52, −68, …); its h = 2 list contains −60 (not fundamental) and misses −20, −52, −148. | numbers WRONG (sign bug), verdict "h = 2 is common, ℚ(√−15) is generic" UNCHANGED (16/122 is even more common) |
| B335 | 3-fold cyclic cover: vol ratio 3 exactly; shortest geodesics multiplicity 3; cusp shape of cover; isometry group order 24 with abelianization (ℤ/2)², not SL(2,3) (abelianization ℤ/3) | ratio 3.0000000000; shortest geodesic 1.0870701449 with multiplicity 3; order 24, abelianization ℤ/2 + ℤ/2 | MATCH |
| B488 / B489 | n-fold cyclic covers of 4₁, n = 1..8: vol = n·vol(4₁); torsion order = \|2 − L(2n)\| (Lucas) | n = 1..8: ratios exactly 1..8; H₁ = ℤ, ℤ/5+ℤ, (ℤ/4)²+ℤ, ℤ/3+ℤ/15+ℤ, (ℤ/11)²+ℤ, ℤ/8+ℤ/40+ℤ, (ℤ/29)²+ℤ, ℤ/21+ℤ/105+ℤ, torsion orders 1, 5, 16, 45, 121, 320, 841, 2205 = \|2 − L(2n)\| | MATCH (the "(ℤ/m)²" wording of B488 is right only for odd m; even m split as ℤ/(m/2)·… — recorded, B489's own table has the true groups) |
| B406 | a_p(15a1) ≡ a_p(40a1) mod 4 at every good prime < 200 | 0 violations over primes < 200 not dividing 30; torsion structures [4,2] and [2,2] as stated | MATCH |
| B486 | figure-eight cusp modulus 2√3·i: rectangular, disc −48, not hexagonal; translations (1, 2√3) orthogonal | shape −1.1e−15 + 3.4641016151 i; Re = 0 to machine precision; (2√3 i)² = −12 so the order ℤ[2√3 i] has discriminant −48 | MATCH |
| B509 / B510 | Y² = X³ − 2X + 1: disc 80, conductor 40, j = 55296/5, torsion ℤ/4, 2-isogenous (not isomorphic) to 40a1; the genus-1 cover d² = (c²−1)(c²−5) has Jacobian this curve; y² = x(x−1)(x−5) is 40a1 | disc 80, conductor 40, j = 55296/5 (in the 40a class, ≠ 40a1's 148176/25), torsion [4]; Jacobian of d² = (c²−1)(c²−5): conductor 40, j = 55296/5 ✓; y² = x(x−1)(x−5): j = 148176/25 ✓ | MATCH — and this is the curve R32 found behind B211/B213's "Φ is 40a1": the bank corrected itself in B509/B510 without touching B211/B213 |
| B520 | S = arccosh(5/2) ≈ 1.5668 | 1.5667992370 = log((5+√21)/2) | MATCH |

**Physics content:** none. "No observable content."
