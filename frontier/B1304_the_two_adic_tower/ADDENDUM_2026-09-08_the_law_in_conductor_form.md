# B1304 addendum (2026-09-08) — the law in conductor form, exact at every level 2 ≤ n ≤ 30

Let d(ψ) be the **conductor** of a character ψ of H₁(Y_n): the smallest d | n with ψ Φ^d-invariant, i.e. the smallest
level ψ is pulled back from. By Lemma 1 (pullback exactness) h¹(Y_n; ψ) = h¹(Y_d; ψ), so a law need only speak about the
characters that are **new** at their level. For the odd-order ones it is one sentence:

> **A new odd-order character ψ of Y_d carries a class iff d is odd, ψ is an eigencharacter of the half-deck Ψ, its order is
> prime to 5, and Ψ^d acts on it by a global sign: u^d ≡ ±1 modulo the order. New characters at even levels never carry a
> class.**

B1303's four clauses were this statement with the sign taken at the level n instead of the conductor d; the two agree
whenever n/d is odd or the character is pulled back from an odd level, and they part at Y₃₀, where the 1 200 mixed 11·31
characters of conductor 15 all have u³⁰ ≡ +1 but split 600 : 600 by the sign of u¹⁵ — exactly as their h¹ does.

`verification/conductor_law.py` (record `conductor_law_run.txt`) constructs every odd-order Ψ-eigencharacter of every
level 2 … 30 (on the eigenlines of each odd prime-primary part and their products; the eigenvalue of a product by the
Chinese remainder theorem), computes its conductor and the sign of u^d, and applies the criterion:

| level | odd eigencharacters | new, odd conductor, unramified, global sign → h¹ = 1 | everything else → h¹ = 0 |
|---|---|---|---|
| 5, 7, 9, 11, 13, 17, 19 (prime) | 20, 56, 36, 396, 1 040, 7 140, 18 696 | all (both signs) | — |
| 15 | 1 280 | 680 (340 +, 340 −) | 600 mixed |
| 20 | 8 504 | 20 (Y₅'s, conductor 5) | 80 of conductor 20 (sign −), 1 600 mixed, 6 804 ramified |
| 21 | 23 996 | 12 236 | 11 760 mixed |
| 22 | 351 344 | 396 (Y₁₁'s, conductor 11) | 176 of conductor 22, 69 696 mixed, 281 076 ramified |
| 23 | 255 116 | 128 156 | 126 960 mixed |
| 26 | 5 204 | 1 040 (Y₁₃'s) | 4 164 ramified; 233 is inert |
| 28 | 159 884 | 56 (Y₇'s) | 560 of conductor 28, 31 360 mixed, 127 908 ramified |
| 30 | 775 004 | 680 (Y₁₅'s 340 + 340, conductor 15) | 600 of conductor 15 with mixed u¹⁵, 120 of conductor 30, 153 600 mixed, 620 004 ramified |

Every row obeys the sentence; the remaining levels 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 24 do too (SELFTEST PASS over
2 … 30). The even-conductor clause now rests on five independent instances (Y₂₀'s 41, Y₂₂'s 89, Y₂₈'s 281, Y₃₀'s 61, and
Y₂₀'s check by Reidemeister–Schreier); the global-sign clause on Y₁₅, Y₂₁, Y₂₃, Y₃₀. With B1304's 2-adic result the
tower's law is complete in this form: the support of Y_n is the union over d | n of the new supports of Y_d, the new odd
support at odd d being the sentence above and the new 2-adic support existing at d = 3, 6, 12 only.

What remains is a proof (L210(iv)): in the unipotent form, that the rank-one nilpotent N of a new eigencharacter vanishes
exactly under the sentence's conditions.
