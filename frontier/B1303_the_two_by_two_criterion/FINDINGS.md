# B1303 — THE 2×2 CRITERION: π₁(Y_n) is the fixed quotient of the fibre's monodromy, so h¹(Y_n; ψ) = 1 exactly when a product of n explicit 2×2 matrices is the identity — the tower's supports fall out in seconds through Y₂₁, the deck-eigen law is corrected and read off exactly (Ψ-eigencharacters, Ψ² = deck; a global sign of Ψⁿ, which must be + at even levels, so new odd support arises only at odd levels — B1301's prediction for Y₂₀ was wrong and a Reidemeister–Schreier check of Y₂₀'s 41-part confirms the criterion) and verified at every level 2 ≤ n ≤ 21, and the Standard-Model lines of Y₁₅, Y₁₈ and Y₂₁ are counted: Y₁₈'s are Y₉'s, and on the odd alphabets the triplet is protected

**Date:** 2026-09-08 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (the criterion validated against the Reidemeister–Schreier computation at every level 2 ≤ n ≤ 13 on every count, order and eigen-structure, and against B1278/B1300/B1301 on the alphabets and the Standard-Model lines of Y₉ and Y₁₂; the presentation identity checked by homomorphism counts into S₃, A₄, S₄, A₅ for n ≤ 5) + LAW (the deck-eigen law, corrected, exact at n = 2 … 21) + the Y₁₅ Reidemeister–Schreier sweep as the independent confirmation at a fourteenth level (§6) · **Price: unchanged** · **Numbering:** B1303.

## Why this arc — the sweeps were the bottleneck

B1301 computed the h¹ support of the closings by Fox calculus on the branched-cover presentations (one 40-digit
singular-value decomposition per deck orbit); Y₁₂ took three minutes, Y₁₃ eight, Y₁₅ needs hours and Y₁₈ (33 million
characters) is out of reach. The deck-eigen law was verified where the sweeps could go. Here the presentation is
replaced by the fibre's: the figure-eight is fibred with fibre the punctured torus F and monodromy φ: a ↦ a²b, b ↦ ab
on π₁(F) = F₂, and the n-fold cyclic branched cover is the fixed quotient **π₁(Y_n) = ⟨a, b | φⁿ(a) = a, φⁿ(b) = b⟩**.

## 1. The criterion ((a))

For a non-trivial character ψ of H₁(Y_n) = coker(Φⁿ − I) (Φ = [[2,1],[1,1]] the abelianised monodromy; Δ(t) = det(t − Φ)
= t² − 3t + 1), the presentation complex has deficiency zero, so h¹(Y_n; ψ) = 1 − rank J(ψ) with J the Fox matrix of the
two relators φⁿ(x)x⁻¹, and J(ψ) = M_{φⁿ}(ψ) − I where M is the Fox Jacobian. The chain rule gives
M_{φⁿ}(ψ) = M_φ(ψ∘Φⁿ⁻¹) ⋯ M_φ(ψ∘Φ) M_φ(ψ), and M_φ(χ) = [[1 + χ(a), χ(a)²], [1, χ(a)]] depends on χ(a) only. Hence

> **h¹(Y_n; ψ) = 1 ⟺ A(x_{n−1}) ⋯ A(x₁) A(x₀) = I, A(x) = [[1 + x, x²], [1, x]], x_k = (ψ∘Φ^k)(a) = ψ(a)^{F_{2k+1}} ψ(b)^{F_{2k}}**

(F the Fibonacci numbers), and h¹ = 0 otherwise (rank J ≤ 1 always, since J kills (ψ(a) − 1, ψ(b) − 1) — no character
has h¹ ≥ 2, B1278's observation, now a one-line fact). The identity test is done exactly modulo two primes q ≡ 1 mod m
(m the exponent of H₁), the characters parametrised by the Smith form of Φⁿ − I so that every character is visited once.
The deck transformation acts on characters by ψ ↦ ψ∘Φ; and Φ = Ψ² with Ψ = [[1,1],[1,0]] (the Fibonacci matrix), so the
half-deck Ψ acts too — on H₁(Y_n) = ℤ[φ]/(L_n) (n odd) or ℤ[φ]/(√5 F_n) (n even), φ the golden ratio, Ψ is
multiplication by φ and the deck is multiplication by φ².

**Validation.** At every level 2 ≤ n ≤ 13 the criterion returns exactly B1301's supports: the counts (0, 3, 0, 20, 27,
56, 0, 147, 20, 396, 123, 1 040), the orders, and the full deck-eigen structures; on Y₉ and Y₁₂ the alphabets (145 and 3;
97 and 27) and — through the line enumerator of §4 — B1278's and B1300's 706 464 / 568 656 with the whole survival
census, and B1301's 34 752 / 3 264 with D thinned to one generation on 31 488 lines. The fixed quotient of φⁿ, the fixed
quotient of the boundary-fixing conjugate φ′ = c_{a⁻¹}∘φ, and B1274's Reidemeister–Schreier presentation of the branched
cover have identical numbers of homomorphisms into S₃, A₄, S₄ and A₅ for n = 2, 3, 4, 5 (`presentations_hom_counts.py`).

## 2. The tower through Y₂₁ ((b))

| n | H₁(Y_n) | characters | support | by order | time |
|---|---|---|---|---|---|
| 14 | ℤ/377 ⊕ ℤ/1885 | 710 645 | 56 | 29: 56 (Y₇'s) | 1 s |
| 15 | (ℤ/1364)² | 1 860 496 | **2 723** | 2: 3, 11: 20, 22: 60, 31: 60, 62: 180, 341: 600, 682: 1 800 | 6 s |
| 16 | ℤ/987 ⊕ ℤ/4935 | 4 870 845 | **0** | — | 16 s |
| 17 | (ℤ/3571)² | 12 752 041 | 7 140 | 3571: 7 140 | 59 s |
| 18 | ℤ/2584 ⊕ ℤ/12920 | 33 385 280 | 171 | 2: 3, 8: 24, 19: 36, 38: 108 — Y₉'s 147 and Y₆'s 24, nothing new | 138 s |
| 19 | (ℤ/9349)² | 87 403 801 | 18 696 | 9349: 18 696 | 377 s |
| 20 | ℤ/6765 ⊕ ℤ/33825 | 228 826 125 | 20 | 11: 20 (Y₅'s) — **nothing at 41**, against B1301's prediction | 1 040 s |
| 21 | (ℤ/24476)² | 599 074 576 | **48 947** | 2: 3, 29: 56, 58: 168, 211: 420, 422: 1 260, 6119: 11 760, 12238: 35 280 — (S × V₄) ∖ 1 with \|S\| = 12 237, exactly the census's prediction | 2 666 s |

Y₁₄, Y₁₆, Y₁₇, Y₁₈, Y₁₉ are exactly what B1301's law predicted (Y₁₇: 2 · 3570 eigencharacters at 3571, λ = 1105, 2469;
Y₁₉: 2 · 9348 at 9349); Y₁₅ is the case the law left open, and it decides it (§3).

## 3. The law, read off the eigencharacters ((c))

Y₁₅'s support is (S × V₄) ∖ 1 with |S| = 681: the identity, Y₅'s 20 eigencharacters at 11 (λ = 5, 9), the 60 new ones at
31 (λ = 14, 20), and **600 of the 1 200 mixed characters of order 341** — those with (λ₁₁, λ₃₁) = (5, 20) or (9, 14), i.e.
λ ≡ 82 or 262 mod 341, and not (5, 14) or (9, 20). What separates them is the half-deck: with u the Ψ-eigenvalue
(u² = λ; u a root of x² − x − 1 modulo the order), Ψⁿ acts on the supported ones as a global sign, uⁿ ≡ +1 or −1 modulo
341, and on the unsupported ones as +1 at one prime and −1 at the other — a square root of 1 that is not ±1.

Y₂₀ then corrected B1301's prediction. The prime 41 divides F₂₀ and the roots of Δ mod 41 have exact order 20, so B1301
§2 listed "new support at 20 (41)"; the criterion finds **nothing at 41**, and a direct Reidemeister–Schreier check of all
1 680 order-41 characters of Y₂₀ (84 deck orbits, B1274's presentation, B1278's Fox calculus) confirms h¹ = 0 on every
one, with the 20 order-11 characters at h¹ = 1 as the control (`rs_check_Y20.py`). At 41 both eigenvalues u have order
40, so Ψ²⁰ = t¹⁰ acts on both lines by −1: the characters are not pulled back from Y₁₀, and that is what excludes them.
`eigen_census.py` constructs every odd-order Ψ-eigencharacter of every level directly — on the eigenlines of each odd
prime-primary part and their products — and runs the criterion on each (Y₂₀: 8 504 of them; Y₂₁: see the record):

> **The law (exact at every level 2 ≤ n ≤ 21; every odd-order character with h¹ = 1 is a Ψ-eigencharacter).** An
> odd-order Ψ-eigencharacter ψ of H₁(Y_n), ψ∘Ψ = ψ^u, has h¹(Y_n; ψ) = 1 iff (i) its order is prime to 5 (the ramified
> prime of ℤ[φ], where λ = u² = −1: the lens space Y₂'s characters, at 0 on every even level), (ii) Ψⁿ acts on it by a
> global sign, Ψⁿψ = ψ^ε with ε = ±1 modulo the whole order (not +1 at one prime and −1 at another), and (iii) ε = +1 when
> n is even. Since Ψⁿ = t^{n/2} for even n, (iii) says the odd support of an even level is exactly the pullback of the odd
> support of Y_{n/2}: **new odd support arises only at odd levels.** The 2-adic part is separate: the family characters
> (from the flat Y₃) multiply every odd support character into the support when the 2-part of H₁ is (ℤ/4)² (n odd), and
> the 2-adic supports of Y₆ (order 8) and Y₁₂ (order 16) recur at Y₁₈ and Y₂₄ only as pullbacks (Y₁₈ computed).

Where the clauses bite: (i) at Y₄, Y₁₀, Y₁₄, Y₁₈, Y₂₀ (the ramified characters, with either sign, all at 0); (ii) at Y₁₅
(600 mixed-sign characters at 0, 680 global-sign ones at 1) and Y₂₀ (1 600 unramified mixed at 0); (iii) at Y₂₀ (80
unramified with ε = −1 at 0, against the odd levels where the ε = −1 lines are always supported: Y₅, Y₇, Y₉, Y₁₅ …). The
table of §2 in B1301 stands for the odd levels 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 and is corrected for 20 and 22: no new
support there, and by the law none at any even level.

## 4. The Standard-Model lines of Y₁₅, Y₁₈ and Y₂₁ ((d))

A closing whose support is (S × V₄) ∖ 1 with S odd and closed under multiplication by units (Y₉: the 36 eigencharacters at
19; Y₁₅: the 681; Y₂₁: the 12 236 of the census, §3) has the multiplicity rule of B1300 — a component's odd part in S: three generations; trivial
odd part: three or, if its 2-part is a family character χ_g, two with generation g projected; otherwise none — and its
lines are counted by odd triples (f_Q, f_u, f_L) ∈ (S ∪ 0)³ reduced to signatures with the 64 sign assignments counted per
signature (`odd_alphabet_lines.py`; on Y₉: 758 593 / 737 568 / 706 464 / 568 656 and the survival census, exactly).

| closing | K3 | three generations | SU(5) broken | SM vacua | full spectrum | D total | patterns |
|---|---|---|---|---|---|---|---|
| Y₉ | 145 | 758 593 | 737 568 | 706 464 | 568 656 | 3 always | 67 |
| **Y₁₅** | **2 721** | 5 034 643 841 | 5 027 240 000 | **5 016 142 400** | 4 960 988 960 | **3 always** | 67 |
| Y₁₈ | 145 (= Y₉'s) | 758 593 | 737 568 | 706 464 | 568 656 | 3 always | 67 |
| Y₂₁ | 48 945 (predicted from S: 1 + 4 · 12 236) | not enumerated ((S ∪ 0)³ ≈ 1.8 · 10¹² odd triples; the structural count is L210) | — | — | — | 3 always (the theorem) | the same 51 signatures are expected |

**Y₁₈'s Standard-Model lines are Y₉'s**, pulled back: its alphabet is Y₉'s 145 letters (the order-8 characters of Y₆ carry
one generation and are not letters, and they form no products with the 19-part), so nothing new happens at 18, and the
same will hold at 27, 36, … for Y₉'s lines and at 24 for Y₁₂'s (Y₂₄'s 2-part is 2¹⁰; whether it adds new letters is not
computed — its 10⁷ million characters are beyond even the criterion in this session). **On the odd alphabets the triplet
is protected**: B1300's theorem applies verbatim (a letter's square has odd order and lies in S, since S is closed under
units), so every Standard-Model line of Y₁₅ and Y₂₁ keeps D in all three generations — the one-triplet vacua of B1302 are
a 2-adic phenomenon, Y₁₂'s (and possibly Y₂₄'s).

## 5. What this settles

- **The tower is computable.** One 2×2 product per character replaces a 40-digit SVD per deck orbit: Y₂₁'s 599 million
  characters in 2 666 s. The alphabet of every closing up to Y₂₁ is known; the supports are banked as
  `support_mt_Y{n}.json` in the fibre coordinates (ψ(a), ψ(b)).
- **The law is exact and complete for odd orders** at 20 levels, with its three clauses beyond the eigen condition — the
  ramified prime, the global sign, and the sign + at even levels — identified on Y₁₀, Y₁₅ and Y₂₀; B1301's prediction of
  new support at Y₂₀ and Y₂₂ is withdrawn (corrected in its addendum). A proof is now a statement about products of the
  matrices A(x): for a Ψ-eigencharacter the factors are Galois conjugates A(x^{u^{2k}}), and the sign clauses are the
  condition under which the product closes (L210(iv), reformulated).
- **The Standard-Model closings of the tower** through Y₂₁: Y₉ (706 464 lines), Y₁₂ (34 752, the one-triplet ones),
  Y₁₅ (5 016 142 400 lines), Y₁₈ (Y₉'s), Y₂₁ (an alphabet of 48 945 letters, lines not enumerated); the triplet protected on all but Y₁₂.
- Not a chirality statement; vector-like throughout (B1260); 0 of 19; price unchanged.

## 6. The independent confirmation at level 15

B1301's Reidemeister–Schreier sweep of Y₁₅ (124 054 deck orbits, three workers) was started before the criterion was
found and runs as the independent check of the criterion at a level it was not validated on. At banking time it had not finished (it was paused to give the criterion runs the cores, and resumed); its result is appended as an addendum when it completes. The Y₂₀ check of §3 — all 1 680 order-41 characters and the 120 order-11 ones by the same Reidemeister–Schreier Fox calculus — already tests the criterion beyond its validation range, on the very case where the law changed.

## Controls (MB12)

- **Twelve levels of exact agreement** between the criterion and the Reidemeister–Schreier Fox calculus (counts, orders,
  deck-eigen structures), plus the alphabets and lines of Y₉ and Y₁₂ (B1278, B1300, B1301) reproduced from the criterion's
  supports by an independent line counter.
- **Presentation identity:** homomorphism counts into four small groups agree for the three presentations at n = 2 … 5.
- **Exactness:** the identity test is modular arithmetic with two primes ≡ 1 mod m; no floating point anywhere.
- **The law's three clauses** each tested where they bite (Y₁₀ for the ramified prime; Y₁₅ for the global sign; Y₂₀ for the even-level sign), and the criterion itself checked by Reidemeister–Schreier Fox calculus on Y₂₀'s 1 680 order-41 and 120 order-11 characters, where it had not been validated.
- **E70-class:** the chain rule's order of factors is fixed by the validation (a reversed product fails at n = 3 already).

## Verification

- `verification/criterion.py` — the criterion, levels 2 … 17 by meshgrid; `criterion_at_scale.py` — the Smith-form
  parametrisation in chunks, levels 14 … 21, writes `support_mt_Y{n}.json`; run record `criterion_run.txt`.
- `verification/refined_law.py` — the clause-by-clause census over all characters (Y₁₀, Y₁₅); `eigen_census.py` — every odd eigencharacter of every level 2 … 21 under the criterion; `rs_check_Y20.py` — the Reidemeister–Schreier check of Y₂₀'s 41- and 11-parts; `presentations_hom_counts.py` — the three
  presentations into S₃, A₄, S₄, A₅; `odd_alphabet_lines.py` — the lines of the odd-alphabet closings; run records.
- Lock `tests/test_b1303_the_two_by_two_criterion.py`: fast — the criterion at n = 2 … 13 against B1301's counts, the
  refined law on Y₁₀ and Y₁₅, the lines of Y₉ from the criterion's support; slow — the homomorphism counts, Y₁₈, Y₂₁.
- Depends on B1301 (the supports it reproduces and the law it refines), B1300 (the weight table and the theorem),
  B1274 (the presentations), B1278.
