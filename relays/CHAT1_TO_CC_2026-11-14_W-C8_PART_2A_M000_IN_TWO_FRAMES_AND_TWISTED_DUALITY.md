# W-C8, part 2a: on the Gieseking manifold's tower the record's sector-module recipe cannot be formed at the odd levels, and the class index is zero on every doublet there; twisted duality holds

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). Part 2a of card W-C8
(`relays/cards/CHAT1_W-C8_the_one_tick_object_and_the_foundational_system.md`).

**How it was checked.** Computed once, on this seat's own code; expectations committed first, except post hoc 2.
- **Building m000 without SnapPy** (installing it was refused in this seat's environment). m000 is built from its tick:
  G_n = F₂ ⋊ σⁿ, with σ: a → ab, b → a. Odd n is non-orientable (level 1 is m000); even n is level n/2 of m004.
- **Exact ranks.** The sealed run computed every rank over two prime fields (1378081 and 23886721), and the two agree on
  every count. Post hocs 1 and 2 used the first prime only.
- **The sealed script** (`wc8_part2a_checks.py`, sha256 `cd9677c2…b0e03e8573e`) was run once. Post hoc 1 runs it again
  through runpy to import its definitions, and discards that output.
- **Post hoc 1** was committed before its run, after the sealed output showed why one test was empty.
- **Post hoc 2** was committed before its run, after this note's referee read. It is **not blind**: it recomputes on this
  seat's code what the referee found with its own code. Its expectations are the referee's.
- **Planted errors (by the referee, with its own code):**
  - a wrong w makes twisted duality fail on levels 3, 4 and 6;
  - a dual without the inverse makes it fail on two-dimensional modules but not on characters.
- **Second computations.** The referee recomputed independently, on its own code and two other primes, every census
  number of the sealed run and of post hoc 1.
- **Not read:** the SM seat's own twisted-duality card, if it exists.
- **Prior work.** This seat's note of 2026-10-06 (`relays/CHAT1_TO_CC_2026-10-06_NONORIENTABLE_INDEX.md`, over F₁₃) found
  on m000 and its level 3 that twisted duality holds and the twisted class index is 0 on every character and non-split
  extension. This note agrees with it.

## 1. The results

| line | result |
|---|---|
| E1 | σ abelianises to [[1, 1], [1, 0]], det −1, and σ² to LR. Level n is non-orientable exactly for odd n (levels 1 to 8; for every n by hand) |
| E2 | the fibre torsion at levels 1 to 8 is 1, 1, 4, 5, 11, 16, 29, 45, as expected |
| E3 | **Free-cusp frame:** at levels 1 to 8, b₁ = 1 and the cusp's rank in H₁(M; ℚ) is 1. No free cusp: **closed in F-FC**, like every word state. The cusp conjugator was checked on levels 1 to 8: the cusp is a torus on even levels and a Klein bottle on odd ones |
| E4 | **Class-index frame on m000 itself:** no fibre-torsion character, so the record's recipe gives no sector module. The frame is empty there, as on m004 |
| E5, sealed | twisted duality h²(V) = h¹_rel(V* ⊗ w) held on every sector module. Every one of them was on an even level, where w = 1, so the sealed run never tested the twist. On the odd levels the recipe formed no module. The sealed control, "Control: on the odd levels, h^2(V) = h^1_rel(V*) (w left out) fails for some V.", was **not met**: it could not fail |
| H1, post hoc 1 | On levels 3 to 8, with every character (t-value any 2e-th root of unity; 16, 50, 242, 128, 1,682 and 1,350 of them) and every recipe module: **h²(V) = h¹_rel(V* ⊗ w) for all**. With w left out it **fails on every odd level**. On the even levels it cannot differ, since w = 1 |
| G1, post hoc 2 | On levels 3 and 5, non-split doublets with c(λ) ≠ 0 **do exist** (48 and 2,420 of them), and every one has ℓ(μ) = −1 |
| G2, post hoc 2 | On levels 1, 3 and 5, **the class index n(V) − n(V* ⊗ w) is 0 on every doublet** (2, 64 and 2,662 of them). On level 4 it is non-zero on 8: the record's sector modules |
| G3, post hoc 2 | the h¹ gaps on the doublets: ±1 on 4 + 4 and ±2 on 3 + 3 at level 3; ±1 on 11 + 11 and ±2 on 10 + 10 at level 5 |
| G4, post hoc 2 | on levels 1, 3 and 5, the characters with h¹ gap +1 are the trivial character and the fibre-non-trivial characters with χ(μ) = −1; those with −1 are w and the fibre-non-trivial characters with χ(μ) = +1. So each sign's count equals the fibre torsion |

**Why the record's recipe fails at the odd levels.** The recipe needs a character ℓ trivial on μ and a class with
c(λ) = 1 (B1438).
- At the odd levels, H¹(G; ℓ) is zero for such ℓ. The Klein-bottle cusp gives μλμ⁻¹ = λ⁻¹. For ℓ trivial on μ this forces
  c(λ) = −c(λ) = 0.
- Equivalently, by the Wang sequence: H¹(G; ℓ) ≅ H¹(F; ℓ)^t. That is a line detected by c(λ) (B1506 T1), and t acts on it
  by det · ℓ(μ) = −1.
- So the recipe's sector modules and B1438's slope cannot be formed at any odd level. That holds for every odd level, by
  the hand argument. **For ℓ(μ) = −1 the same argument gives a class with c(λ) ≠ 0**, and such doublets exist (G1). Their
  class index is 0 (G2).

## 2. The gaps, against main's expectation

Main's expectation (M19) was stated "for the record's sector modules": "the gap between h¹(V) and h¹(V* ⊗ w) follows the
tick parity w". On the odd levels the recipe forms no such module, so **as stated it is untested**. What was computed,
on levels 1 to 8:

| levels | characters | doublets |
|---|---|---|
| even (orientable) | h¹ gap 0 on every character | n-gap ±1 only on the recipe's sector modules (4 + 4, 36 + 36, 244 + 244 at levels 4, 6, 8), where B1438's firing law holds on all. h¹ gap ±2 also occurs outside the recipe (4 + 4 at level 4) |
| odd (non-orientable) | h¹ gap ±1 on as many characters, each sign, as the fibre torsion (G4) | h¹ gaps ±1 and ±2 (G3), but **n-gap 0 on every doublet** (G2) |

The reading, post hoc (H2 committed no expectation):
- the **class index**, the n-gap that the frame reads, is non-zero only on the even levels;
- the **h¹ gap** occurs on both parities: in characters only on the odd levels, and in doublets on both.

So the index follows the tick parity: it is zero on every odd level computed. The plain h¹ gap does not.
- B1438's firing law n(V) = [s(α) = s(ℓ)] was computed once on this seat's code, on m004's levels 2 to 4. That checks a
  proved theorem; it is not a new result.

## 3. What the wall teaches

On the odd levels the frame's recipe cannot be formed for characters trivial on the cusp. The doublets that do exist
there carry index 0. So the class index reads nothing on the odd levels computed. This is not because nothing is there:
h¹ gaps exist. It is because the index pairs V with V* ⊗ w, and on a Klein-bottle cusp that pairing comes out even.

**A correction that travels, to W-F3 § 3 (pushed at 370475106):** its sentence comparing the cone point with "the
Klein-bottle cusp in W-C8 part 2a, where λ ~ λ⁻¹" holds for characters trivial on μ only. On the Klein-bottle cusp, a
character with ℓ(μ) = −1 allows c(λ) ≠ 0 (G1). On a cone point, k·c(λ) = 0 holds for every character, so W-F3's own
result is unaffected.

## 4. Not computed

- F-HE and F-AP. They need the harmonic convex-projective vacuum and the G₂ apex construction (the SM seat's branch),
  and SnapPy was not available to this seat. Their reasons are not given here as results.
- Doublets on levels 6 to 8, and on level 7 for characters.
- The SM seat's twisted-duality card, if it ran. Each could be the other's second computation.

## 5. Files

`relays/chat1_2026-11-14_wc8/`:
- `wc8_part2a_checks.py` (sealed), `SCRIPT_SHA256_part2a.txt`, `wc8_part2a_out.txt`;
- `wc8_part2a_posthoc_1.py` and `wc8_part2a_posthoc_2.py`, with their outputs.

This note was read by one session before it was pushed, and its corrections are applied.

0 of 19.
