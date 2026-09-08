# B1301 — THE TOWER'S ALPHABET: the h¹ support of every closing Y₂ … Y₁₂ obeys a deck-eigen law — its odd part is exactly the deck-eigencharacters whose eigenvalue is a root of the figure-eight's Alexander polynomial of exact order d ≥ 3 modulo a prime of the Lucas–Fibonacci torsion (pulled back from level d), confirmed by a pre-registered prediction on Y₁₁ (396 characters at the prime 199); its 2-adic part is Y₆'s and Y₁₂'s own (orders 8 and 16); and Y₁₂ is a second Standard-Model closing, on which the Wilson lines thin the colour triplet to ONE generation on 31 488 of its 34 752 SM lines — the doublet–triplet mechanism B1300 ruled out on Y₉ exists in the tower, two generations deep and never three

**Date:** 2026-09-08 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (eleven exhaustive supports: Fox calculus on one representative per deck orbit, deck invariance checked, every positive confirmed exactly over ℚ(ζ_order)) + LAW (the deck-eigen law holds at every level 2–12 and its Y₁₁ prediction was written down before the computation; conjectured beyond) + POSITIVE (Y₁₂'s one-triplet Standard-Model lines) · **Price: unchanged** · **Numbering:** B1301, second of the requested range.

## Why this arc — is Y₉'s alphabet an accident of the prime 19?

B1278 found the three-generation alphabet on the object's 9-fold closing and nothing on Y₃, Y₆; B1300 proved the
triplet's protection from the shape of that alphabet — letters of order 1, 19, 38 whose 2-part is the family group. Both
facts rested on one closing. The tower Y_n (the n-fold cyclic branched covers of the object along the figure-eight knot —
the Fibonacci manifolds, |H₁(Y_n)| = L_n² for odd n and 5F_n² for even n) is the object's own, and the question was
whether the support of h¹ has a law across it, which closings carry Standard-Model lines, and whether B1300's hypothesis
— that only the family characters project — survives on a closing whose 2-torsion is larger. It does not survive on
Y₁₂, and what replaces it is the first Wilson-line thinning of the colour triplets in the corpus.

## 1. The deck action and eleven exhaustive sweeps ((a))

The presentation of Y_n (B1274: Schreier generators z = aⁿ, x₀ … x_{n−1}; z filled) makes the deck transformation the
shift x_k → x_{k+1}, so it permutes the characters of H₁(Y_n) and h¹ is constant on its orbits: one Fox computation per
orbit (40 digits; the accepted/rejected singular values are separated by ≥ 35 orders of magnitude at every level),
h¹ recomputed on every element of 30 random full orbits (no mismatch), and **every positive confirmed exactly** over
ℚ(ζ_o), o the character's order, with three zero controls per level.

| n | H₁(Y_n) | characters | deck orbits | support | by order | new at this level | eigencharacters (λ mod order; h¹) |
|---|---|---|---|---|---|---|---|
| 2 | ℤ/5 | 5 | 3 | **0** | — | 0 | (5; λ = 4; h¹ = 0) ×4 |
| 3 | (ℤ/4)² | 16 | 6 | 3 | 2: 3 | 3 | none |
| 4 | ℤ/3 ⊕ ℤ/15 | 45 | 13 | **0** | — | 0 | (5; 4; 0) ×4 |
| 5 | (ℤ/11)² | 121 | 25 | 20 | 11: 20 | 20 | **(11; 5; 1) ×10, (11; 9; 1) ×10** |
| 6 | ℤ/8 ⊕ ℤ/40 | 320 | 58 | 27 | 2: 3, 8: 24 | 24 | (5; 4; 0) ×4 |
| 7 | (ℤ/29)² | 841 | 121 | 56 | 29: 56 | 56 | **(29; 7; 1) ×28, (29; 25; 1) ×28** |
| 8 | ℤ/21 ⊕ ℤ/105 | 2 205 | 283 | **0** | — | 0 | (5; 4; 0) ×4 |
| 9 | (ℤ/76)² | 5 776 | 646 | 147 | 2: 3, 19: 36, 38: 108 | 144 | **(19; 6; 1) ×18, (19; 16; 1) ×18** |
| 10 | ℤ/55 ⊕ ℤ/275 | 15 125 | 1 527 | 20 | 11: 20 | **0** (all from Y₅) | (5; 4; 0) ×4, **(11; 5, 9; 1) ×20**, (55; 9, 49; **0**) ×80 |
| 11 | (ℤ/199)² | 39 601 | 3 601 | **396** | 199: 396 | 396 | **(199; 63; 1) ×198, (199; 139; 1) ×198** |
| 12 | ℤ/144 ⊕ ℤ/720 | 103 680 | 8 678 | 123 | 2: 3, 8: 24, 16: 96 | 96 (27 from Y₃, Y₆) | (5; 4; 0) ×4 |

Pullbacks Y_d → Y_n (d | n; x_k → x_{k mod d}) are characters, and the support of Y_d always lands in the support of Y_n
(the transfer makes the pullback on twisted H¹ injective) — checked for every pair. The family characters (n ≡ 0 mod 3)
have h¹ = 1 at every level and the deck permutes them as a 3-cycle.

## 2. The deck-eigen law — the odd part of every support ((b))

> **Law (verified at every level 2 ≤ n ≤ 12; conjectured beyond).** Let ψ ≠ 1 be a character of H₁(Y_n) of odd
> prime-power order, p ∤ 2. Then h¹(Y_n; ψ) = 1 iff ψ is an eigencharacter of the deck transformation, t·ψ = ψ^λ, whose
> eigenvalue λ ∈ 𝔽_p — necessarily a root of Δ(t) = t² − 3t + 1 modulo p — has exact order d ≥ 3 (then d | n and ψ is
> pulled back from Y_d, where it is new); otherwise h¹ = 0. Y₂ = L(5, q) is the one exception: its order-5
> eigencharacters have λ = −1 of order 2 and h¹ = 0, as they must on a lens space, and they stay at 0 on every even level.

What was seen: on Y₅, Y₇, Y₉, Y₁₁ the support is *exactly* the set of all non-trivial eigencharacters (2(p − 1) of them,
on the two eigenlines of the roots of Δ mod p); on Y₄, Y₆, Y₈, Y₁₀, Y₁₂ the eigencharacters with λ = −1 (mod 5) all have
h¹ = 0, and on Y₁₀ the 80 eigencharacters of order 55 — λ ≡ −1 mod 5 and of order 5 mod 11 — have h¹ = 0 while the 20
of order 11 (pulled back from Y₅) have h¹ = 1; the 3-parts of Y₄, Y₈, Y₁₂ (Δ has no root mod 3) carry nothing. **The
Y₁₁ row was a pre-registration:** before Y₁₁ was computed, the roots of Δ mod 199 (63 and 139, of order 11) were written
into the driver with the prediction "396 = 2 · 198 eigencharacters, all with h¹ = 1, nothing else" — the sweep found
exactly that (396 of 39 601), every one confirmed over ℚ(ζ₁₉₉). So the prime 19 of B1278 is not an accident: 19 is the
prime at which Δ acquires roots of exact order 9, and B1300's remark — 6 and 16 = 6⁻¹, primitive 9th roots of unity
mod 19 — is the law's Y₉ instance. The prime-2 face of the same law is the family group: Δ ≡ t² + t + 1 mod 2 has its
roots in 𝔽₄ (order 3), and the deck permutes the three family characters as a 3-cycle at every level divisible by 3; that
their h¹ is 1 is the flat closing's (B1273), not the eigen mechanism's.

The law reads off the tower from arithmetic alone (the roots of Δ modulo the primes of |H₁(Y_n)| and their orders, by
hand for n ≤ 24): new odd support exists at n = 5 (11), 7 (29), 9 (19), 11 (199), 13 (521: predicted 1040), 15 (31:
predicted 60, plus Y₅'s 20 pulled back), 17 (3571), 19 (9349), 20 (41), 21 (211, plus Y₇'s 56), 22 (89), 23 (139 and
461) — and none at 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 24, where every prime is either inert for Δ (3, 7, 13, 17, 23, 47)
or carries a root of order 2 (5) or a root pulled back from a lower level (19 at n = 18, 29 at n = 14, 11 at n = 10, 20).
Y₁₃ and Y₁₅ are the next tests (registered, L210); Y₁₅ also decides whether products of two odd parts from different
levels (Y₅'s 11-part and the new 31-part) lie in the support — the one case the law leaves open, since the only products
seen so far are with the family group (Y₉: all in; Y₁₂: not all in, §3).

## 3. The 2-adic part — Y₆'s and Y₁₂'s own ((a), (c))

At n ≡ 0 mod 3 the 2-part of H₁ is (ℤ/4)² for odd n and grows with the 2-adic valuation of n; the new 2-adic support is
Y₃'s 3 (order 2), Y₆'s 24 (order 8) and Y₁₂'s 96 (order 16) — nothing at order 4 anywhere, nothing new at Y₉ (its 2-part is
Y₃'s). None of these is a deck eigencharacter, nor eigen up to a family character. Y₆'s 24 meet 12 family cosets with
exactly two positives each, so an order-8 character has generation count Σ_g h¹(χ_g ψ) = 1 — it carries one generation
— while Y₁₂'s 96 have generation count 3 and are letters. The support of Y₁₂ is not closed under the family group (Y₉'s
was); the 2-adic pattern "new support of order 2^{k+2} at n = 3 · 2^k" is an observation from three points, not a law.

## 4. The alphabets, the lines and the triplets ((d))

From each support file the lines (ψ_Q, ψ_u, ψ_L) ∈ K3³ are enumerated with the weight table of B1300 (every other
multiplet's character an integer combination; the 72 roots' coordinates derived from B1277's descent data,
`e6_roots_qul.json`, 8 of them trivial = the SM's):

| closing | K3 | candidates | three generations | SU(5) broken | SM vacua | full spectrum | D total on the SM lines |
|---|---|---|---|---|---|---|---|
| Y₃, Y₆ | {1} | — | — | — | 0 | 0 | — |
| Y₉ | 145 (orders 1, 19, 38) | 3 048 625 | 758 593 | 737 568 | 706 464 | 568 656 | **3** on all (B1300) |
| **Y₁₂** | **97 (1 and 96 of order 16)** | 912 673 | 190 849 | 181 440 | **34 752** | 3 264 | **1 on 31 488, 3 on 3 264** |

Y₉ is reproduced from its support file alone — a third route agreeing with B1278's pipeline and B1300's model on every
count, histogram and root census. **Y₁₂ is a second Standard-Model closing**: 34 752 SM-commuting Wilson lines, valued in
characters of order 16 (no odd part at all), break SU(5) to the Standard Model with three generations of Q, u^c, d^c, L,
e^c and ν^c, ⟨N⟩ and ⟨ν^c⟩ available and both Higgs doublets present. And on 31 488 of them — 10 496 per generation, by
the deck's 3-cycle — **exactly one generation of the colour triplet D survives**, the other two projected; D̄ keeps 0 to 3
generations (0 on 7 872 lines), H_u and H_d 1 to 3, N 1 to 3. The (H_u, H_d, D, D̄) census has 30 entries; among them
(3, 3, 1, 3) on 2 304 lines — three Higgs pairs, one triplet — and (3, 3, 1, 0) on 1 536 — three Higgs pairs, one D and no
D̄ from the 27s at all. The 3 264 full-spectrum lines are exactly those with ψ_Q = 1. Every one of the 34 752 lines keeps
exactly the Standard Model's 8 roots among SU(5)'s 20 (B1278's statement, now on Y₁₂ too; the extra E₆ roots kept on
5 952 lines are broken by ⟨N⟩, ⟨ν^c⟩), with 8 to 64 E₆-adjoint chirals from the broken roots.

**Why one and not zero.** ψ_D = ψ_Q⁻² still governs (B1300's identity is E₆'s, not Y₉'s). On Y₁₂ the letters have order
16, so ψ_Q⁻² has order 8, and the squares of the 96 letters are Y₆'s 24 pulled-back characters — in the support, with
generation count 1. So the triplet is thinned to the one generation g with χ_g ψ_D in the support, on every SM line with
ψ_Q ≠ 1, and never removed. B1300's theorem holds where its hypothesis holds (the alphabet's 2-part is the family group:
Y₉, and by the law every closing whose alphabet is odd); Y₁₂ is the first closing where the hypothesis fails, and the
conclusion fails by exactly one step.

## 5. What this settles, and what it opens

- **The alphabet is a law of the tower, not a property of Y₉.** Which closings carry Standard-Model lines is decided
  by the roots of the figure-eight's Alexander polynomial modulo the primes of the Lucas–Fibonacci torsion: an odd
  alphabet at n = 9, 15, 21, … (and the pullbacks at 18, 24 …), a 2-adic one at 12 (24?). The selection question L206 —
  which of Y₉'s 706 464 lines — becomes tower-wide: Y₁₂ has 34 752 more, of a different kind.
- **The doublet–triplet problem, one step.** Wilson lines of the tower can thin the triplets: on Y₁₂ two of three
  generations of D are projected while every SM multiplet keeps three. With B1283's mechanism (the light Higgs pair is
  generation g's, from μ_jk = λ|ε_ijk|⟨N_i⟩) a line whose surviving triplet is generation g₀ ≠ g pairs D_{g₀} with a
  surviving D̄_k through ⟨N_g⟩ (k ≠ g, g₀) — no light triplet pair from the 27s at tree level while the Higgs pair of
  generation g stays light. Whether Y₁₂'s vacuum manifold has such a branch on such a line is the next computation
  (L210; B1283's method on Y₁₂'s spectra).
- **The tower's alphabets are predictable by hand** (§2's list) and two predictions are registered for the next sweeps:
  Y₁₃ (1 040 eigencharacters at 521, nothing else) and Y₁₅ (60 at 31 and Y₅'s 20; the mixed order-341 products open).
- Not a chirality statement: every closing is vector-like (B1260); "SM line" names the group and the count. 0 of 19
  values; price unchanged.

## Controls (MB12)

- **Three routes on Y₉:** B1278's pipeline, B1300's structural model and this arc's support-file enumerator agree on
  every count, histogram, root census and adjoint-chiral census.
- **Exactness:** every positive at every level confirmed over ℚ(ζ_order) by exact Gaussian elimination (B1278's
  routine, applied to the character reduced to its order); the numeric gap between accepted and rejected singular values
  is ≥ 35 orders of magnitude at every level; deck invariance of h¹ checked on 30 full orbits per level.
- **Pre-registration:** the Y₁₁ prediction (396; λ = 63, 139) preceded the computation and is recorded in the driver's
  comment; the hand table of roots and orders for n ≤ 24 preceded the sweeps of Y₅, Y₇, Y₈, Y₁₀ (all as predicted, save
  that Y₁₀'s 20 are Y₅'s pulled back, which the first phrasing of the law forgot and the final phrasing includes).
- **The weight table** is B1300's, re-derived from B1277's descent data in the roots file and asserted equal.
- **E70-class:** additive character algebra only; no representation matrices.
- **Hand checks:** Δ(6) = 19, Δ(16) = 209 = 11 · 19; Δ(63) mod 199 = 0 and Δ(139) mod 199 = 0; L₉ = 76, L₁₁ = 199,
  F₁₂ = 144, 5 · 144² = 103 680.

## Verification

- `verification/tower_alphabet.py` — the sweeps, the deck action, the eigen census, the pullbacks, the alphabets and
  lines (parts (a)–(d)); ~9 min with three workers; SELFTEST PASS; run record `tower_alphabet_run.txt`; writes
  `support_Y{n}.json` (positives, family characters, H₁) for n = 2 … 12.
- `verification/lines_from_support.py` — the line enumerator from a support file (B1300's weight table; the root census).
- `verification/e6_roots_qul_derive.py` → `e6_roots_qul.json` — the 72 roots' coordinates modulo the SM roots (B1277's
  loaders, ~2 min); run record `e6_roots_qul_derive_run.txt`.
- Lock `tests/test_b1301_the_towers_alphabet.py`: fast — the lines of Y₉ and Y₁₂ from the stored supports, the sweeps
  of Y₂ … Y₉ with the eigen census; slow — Y₁₀, Y₁₁, Y₁₂ and the roots derivation.
- Depends on B1278 (the pipeline's routines and Y₉), B1300 (the weight table, the theorem), B1274 (the tower's
  presentations), B1273 (the family characters), B1277 (descent data), B1283 (the light pairs).
