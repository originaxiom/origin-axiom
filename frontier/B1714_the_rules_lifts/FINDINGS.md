# B1714 — THE RULE'S LIFTS (P-225; no data): the rule and the moves lift to SU(2) only at the common point, where the rule's eigenvectors are exactly the T-type magic states; off it these moves give no gate set

**Verdict: PROVED** (an exact computation). cc (main), 2026-10-22. No physical quantity. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /Fibonacci anyon|Jones representation|quantum representation|TQFT|SU\(2\)_3|level.?3|magic state|universal (gate|quantum)|Freedman/`
— B218 (golden is the unique metallic mean realisable as a unitary anyon, Fibonacci), B220 and B222 (the golden chain's
tricritical Ising), B226 and B254 (SU(2)₃ and the Fibonacci theory inside (E₆)₁), B24 (NEGATIVE: level 3 is not
selected by the framework), B313 (matter = Fibonacci anyons refuted), B1688 (tricritical Ising as Ising × Fibonacci).
B1607 computed the rule's lift at the common point (order 6 in 2T). None computes where else the rule lifts.
**Literature:** standard facts only — the Fibonacci trace map (Kohmoto, Kadanoff and Tang); the T-type magic states
(Bravyi and Kitaev 2005); the density of the Fibonacci braiding (Freedman, Larsen and Wang 2002).

## 1. The question (P-225, main's reading)

The rule's lift at the common point rotates about the (1, 1, 1) axis, whose eigenstates are the qubit's T-type magic
states. LP = [[1, 1], [1, 0]] is the Fibonacci anyon's fusion matrix, whose braiding is universal, while the qubit layer
is the Ising anyon's (Clifford). P-225 asked for the eigenvectors and whether the weave with the rule is dense anywhere
off the common point. It stayed a reading until computed.

## 2. What was computed (`verification/the_rules_lifts.py`, exact in sympy; the lifts in numpy)

**The criterion.** A mapping class φ lifts to SU(2) at a character χ when χ∘φ = ε·χ for a central character
ε: F₂ → {±1} (four twists: signs e₁, e₂ on a and b, with tr ab picking up e₁e₂).

**The actions on traces**, with x = tr a, y = tr b, z = tr ab:
- the rule a → ab, b → a acts as (z, x, xz − y), the Fibonacci trace map;
- L (a → a, b → ab) acts as (x, z, xz − y);
- R (a → ba, b → b) acts as (z, y, yz − x).

L and R generate SL(2, ℤ), so their common fixed points are those of every move.

| result | value |
|---|---|
| the rule's fixed set, each twist | two points: the common point (0, 0, 0) and one central character (2, 2, 2), (−2, 2, −2), (−2, −2, 2) or (2, −2, −2) |
| L's and R's fixed sets | lines: L fixes y = z = 0 and x = 2, y = z (untwisted), and x = 0, y = ±z or x = −2, y = −z (twisted); R the mirror sets |
| points fixed by two of the three, any twists | only (0, 0, 0) and the four central characters (no curve) |
| the rule's lifts at the common point (ρ(a) = i, ρ(b) = j) | one per twist, orders 3 and 6, the quaternions ±½ ± ½i ± ½j ± ½k: rotations by 120° about the (±1, ±1, ±1) axes |
| their eigenvectors | Bloch vectors exactly (±1, ±1, ±1)/√3, the T-type magic states |

## 3. What it means

- **The magic-state reading holds**, computed rather than read. The rule's lifts at the common point (B1607's order-6
  class, with its order-3 negatives) have the T-type magic states as eigenvectors.
- **Off the common point these moves give no gate set.** The rule lifts nowhere else except at the central characters.
  There the representation is central and every element of SU(2) intertwines, so a lift exists but is not determined.
  No pair of the three moves shares a fixed point elsewhere. "Dense off the common point" therefore has nothing to act
  on in this frame: the moves do not stabilise any other character.
- **What is not computed.** Characters stabilised by other mapping classes, such as the finite orbits of the action
  (the once-punctured torus's analogue of the algebraic Painlevé VI solutions), could carry larger lift groups.
  - Where ρ has finite image (2T, 2O, 2I), those lifts lie in the image's finite normaliser.
  - The infinite-image case is not computed here.
- **Where the universality lives.** The Fibonacci braiding's density is a property of the level-3 quantum representation
  of the mapping class group, not of the character variety. The record has that representation's arithmetic (B218,
  B226, B254) and found its level not selected (B24, NEGATIVE). So the "universal tick" reading needs the quantum
  representation's level, which the framework does not supply.

## 4. Disclosed

- The computation is main's own, written after the point was registered (P-225, main's reading). It is not sealed, since
  the result is an exact algebraic statement with no data and no free choice.
- The central-twist criterion is the standard one for a projective (SO(3)) lift; at the common point it reproduces
  B1607's lift class.
