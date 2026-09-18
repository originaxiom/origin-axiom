# B1427 — THE TOWER'S GENERATION COUNT, VERIFIED ON MAIN WITH INDEPENDENT CODE: one chiral generation per background on 80 800 backgrounds, never two, never three — and the mechanism holds one level further than the record computed

cc, 2026-09-18. The SM lane banked B1374/B1375 on 2026-09-16, past main's harvest pin, and main had not read them.
Verified here **with code written from scratch on this bench**, different primes, and exact cyclotomic arithmetic.
**Verdict: PROVED. Every number the lane reports is reproduced. The mechanism is confirmed and extended to level 7.
Three scoping qualifications are found, one of which is a real completeness gap the lane's own wording half-declares.**

## What was verified, and how independently

Own Fox calculus, own `GF(p)` linear algebra, own cyclotomic field arithmetic (`Φ_m` built from scratch). SnapPy was
used **for presentations and isometry only**. Primes chosen deliberately different from the lane's: **1021, 1201,
1321** against their 421, 541, 601.

**(1) The tower's identity.** The cyclic covers of m004 of degree 2, 3, 4, 5 are m206, s961, t12839, o10_150696.
Isometry on the *oriented* manifolds, corroborated against each mirror and by complex volume Vol + i·CS:

| n | H₁(Y_n) | census name | volume difference |
|---|---|---|---|
| 2 | ℤ/5 ⊕ ℤ | m206 | 0 |
| 3 | ℤ/4 ⊕ ℤ/4 ⊕ ℤ | s961 | 8.9e−16 |
| 4 | ℤ/3 ⊕ ℤ/15 ⊕ ℤ | t12839 | 1.8e−15 |
| 5 | ℤ/11 ⊕ ℤ/11 ⊕ ℤ | o10_150696 | 0 |

All four are **amphichiral**, so chirality carries no discriminating information at these levels — an
orientation-preserving isometry exists, which is what the identification needs.

**(2) The load-bearing fact: h¹(χ²) = 1 at every locus.** On Y₄ at N = 60: 2 700 characters → **89 non-split loci**,
identical at all three primes, and **h¹(χ²) = 1 at every one of the 89, confirmed exactly over ℚ(ζ_m)**. Multiset
`{1: 89}`. Never 2, never 3. χ(λ) = +1 on 44 and −1 on 45, matching the lane. Other levels by the same method:
**Y₂ 9, Y₃ 31, Y₅ 241, Y₆ 639 loci, all h¹ = 1** — every count matching.

**(3) The census, re-run with a *stronger* scan than the lane's.** On Y₄ the index of **every** doublet module over
the whole character group, with **no T5 restriction**: 89 × 2 700 = **240 300 modules**, **976 firing**, **12 800
generation-shaped backgrounds on 64 loci**, **|I| = 1 on all 12 800** (6 400 at +1, 6 400 at −1), ν^c = 0 throughout.
Identical to the lane's numbers. Y₂: 16 firing, 0 generations. Y₃: 0 firing. Y₅: 4 400 firing, **800 backgrounds on
200 loci**, ±1 split 400/400. Four Y₄ backgrounds re-derived **exactly over ℚ(ζ₆₀)** with no prime fields at all.

**(4) The firing signature.** Every firing doublet has (a₀, a₁, t₀, r₁) = **(0,1,1,0) for V and (0,2,1,2) for V\***,
or the reverse; no other signature occurs, on any level. The singlet ν^c has (0,1,1,1) on both sides with I = 0.

**(5) Vacuity guarded in both directions, which is the part that makes this evidence rather than agreement.**
The same code returns **h¹ = 2** at the three order-2 characters of the Whitehead link complement m129 and of m125,
and b₁ = 2 or 3 on other census manifolds — so "1" is a measurement, not a constant the code can only produce. And
the same index code returns **|I| = 2** on t12835 with Sym³(ρ_χ)⊗ψ, signature (0,3,1,2)/(1,3,1,0), reproducing the
record's own ±2 there. The structural reason the tower never shows h¹ = 2: Y_n is one-cusped with b₁ = 1, and with
3 generators and 2 relators h¹ = 2 requires the Fox Jacobian to **vanish**, which happens nowhere on it.

## Beyond the lane: level 7, and one real gap

Solving h¹ ≥ 1 and h¹ = 2 **exactly over the whole of Hom(H₁, ℂ\*)** — by gcd of the 2×2 minors of the Fox Jacobian
and of its six entries, over ℚ(ζ_e) — for n = 2…**7**:

- **h¹ = 2 occurs on no component of any level, including level 7**, one beyond the lane's computed range. So
  h¹ = 1 is not an artefact of the μ_N truncation.
- **The completeness gap, found here:** the μ_N scan misses exactly **two loci per level**. On Y₄ they are the real
  numbers 46.978713… and its reciprocal, which are **((3+√5)/2)^{±4}** — the fourth powers of the roots of the
  figure-eight Alexander polynomial, i.e. **m004's own golden locus lifted to the cover**. They are not roots of
  unity, so no finite-order character on the free part reaches them. **They also have h¹ = 1, so the claim survives**,
  but "complete on the torsion" must not be read as "complete". The lane's Caveat 2 half-anticipates this.

## Three qualifications the lane's wording does not carry

1. The μ_N scan is complete **on the torsion**, not on the character variety: two loci per level are unreachable.
2. **"h¹(χ²) = 1 bounds |I| ≤ 1" is not a proof as stated.** What bounds the index in the data is the interior-class
   count on the doublet (a₁ ≤ 2); t12835's Sym³ gives a₁ = 3 and |I| = 2 in the same code. The verified statement is
   narrower: *on this tower, every firing doublet has signature (0,1,1,0)/(0,2,1,2)*.
3. The unrestricted no-T5 scan was completed on Y₂, Y₃, Y₄ here; Y₅ used the cusp filter, which is a **proved**
   consequence of t₀ ≠ 0 (ρ_V(x) = ψ(x)ρ_χ(x) has eigenvalues ψ(x)χ(x)^{±1}, so t₀ ≠ 0 forces ψ = χ^{∓1} on both
   peripheral curves), and which reproduced the unrestricted count exactly on Y₄.

## What this is NOT

The lane fences itself and the fence stands: these fire on **non-semisimple** backgrounds — the admissibility
question the paper grades with a prior against — and there is **no physics reading, no value, and no three**. One
generation per background is the tower's law as far as computed, and **the count of three is not this mechanism's**
on any level up to seven. Nothing here is derived physics.

## Locks
`tests/test_b1427_tower_generation_count.py`: the tower identity by isometry and complex volume; h¹(χ²) = 1 across
Y₄'s 89 loci; the vacuity controls in both directions (h¹ = 2 on m129, |I| = 2 on t12835); the Y₄ census totals.
