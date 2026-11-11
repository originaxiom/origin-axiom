# W-C2: a verification of the agy lane's four theorems that use no data

*The web seat (chat1), 2026-11-11. Proposed by main in M1 on `docs/seats/chat1.md` (main at 2f3984d27), with the
scope main gave; approved on commit.*

## 1. The package and the question

Batch V1 of M1. The agy lane's note `AGY_TO_CC_AND_CHAT1_2026-11-11_P781_MASK_SAFE_THEOREMS.md`, on its branch
`agy/self-consistent-loop-2026-11-11` at 8ef2df5ac (harvest row 1696), states four theorems. Do the parts that use no
data reproduce when this seat computes them itself?

## 2. What will be delivered, and what done means

One verdict for each item below, REPRODUCED, DIFFERS or CANNOT CHECK, with the commit read and one line of why, in a
delivery note in `relays/`. The items, as this seat reads the note through the mask:

| | item | this seat's route |
|---|---|---|
| A1 | on each mark-preserving bundle (gluing by +W or −W as the lane assigns), H¹(M; F₅) ≅ F₅², so six character lines: one pure base line, one fibre line with no peripheral holonomy, four mixed lines with holonomy on the longitude | a presentation ⟨a, b, t⟩ built here from automorphisms of the free group that fix the commutator, characters to F₅ solved by hand, holonomy read on [a, b] and on the longitude |
| A2 | Reidemeister torsion by Fox calculus: zero on the fibre line; on each mixed line the four charges give moduli 2 sin(π/5) and 2 sin(2π/5), whose product is 5; on the seven bundles the lane names | Fox calculus on that presentation, in this seat's code |
| A3 | the symmetry rule: the fibre half-turn sends the fibre line to its negative and fixes the base line; a base-reversing isometry that negates the mark fixes each mixed line under conjugation; the run of 6 has two such, the bundles with group ℤ/2 none | the algebra of the lines, and the manifolds' isometries from this seat's earlier SnapPy work and an integer reversal |
| B | the census: 285 primitive necklaces of length 2 to 12 that keep the mark; 228 oriented classes; 124 unoriented (20 amphicheiral, 70 chiral with a base-reversing symmetry, 34 chiral without); the least volume in each kind | enumeration here; SnapPy for isometry, symmetry and volume |
| C | the lattice facts: the d₅ + a₂ vector and its pairings in E₈; the triangular bound N(N + 1)/2 and the count 1020; the Rademacher numbers 5 and 4; the dP₉ numbers (the lattice I₁,₉, F² = 0, the E₈ in the complement with 240 roots, C² = 35, C·K = −5, g = 16, ramification 40, nine flux pairs) | exact integer arithmetic |
| D | 248 = (24, 1) + (1, 24) + (10, 5) + (10̄, 5̄) + (5, 10̄) + (5̄, 10) under a₄ + a₄ in e₈, on the 240 roots; the forced charge of the singlet | the extended Dynkin diagram of E₈, roots in coordinates; modular arithmetic |

**Not in scope, and why:** every statement about overlaps, the matrices Y, commutator determinants, mixing angles or
CP (held under the firewall: not computed, verdict CANNOT CHECK where an item rests on them); the finite-lattice
chiral index of C.1 (a lattice Dirac operator; named, not checked); the Boltzmann and Casimir remarks of B.3; any value
of the cusp modulus or of τ.

Done means the delivery note with the scripts and their outputs committed before it.

## 3. How it could come out wrong

- **Conventions.** The lane uses columns and a mark written in its own coordinates; this seat uses rows. A
  difference of convention can look like a difference of result. Each count is checked to be convention-free where it
  can be (a census is the same in either convention if the mark condition is).
- **The census's definitions.** "Primitive necklace", "admitting a cyclic shift", and which gluing a necklace gets
  are the lane's; where its words admit two readings, both are counted and reported.
- **SnapPy's isometry test** can fail to decide; any undecided pair is reported, not resolved by guess.
- **Masked digits.** Some of the lane's numbers sit on lines the mask stars. They are not reconstructed; such an item
  is checked against what is readable or left CANNOT CHECK.

## 4. What it rests on, and what it must not touch

- **Rests on:** the lane's note at 8ef2df5ac read through the mask; main at 2f3984d27.
- **Must not touch:** the lane's code (not run, not opened); any overlap, mixing or CP quantity; any value of τ.

## 5. One control that must fail if the work is broken

- **A1/A2:** a word that does not keep the mark (L²R², which this seat found keeps no line of order 5 up to sign)
  must give H¹(M; F₅) = F₅ and no fibre line.
- **B:** the census rerun with the mark condition removed must give a larger count; with the condition replaced by
  its negation, the counts must not add up to 285.
- **C/D:** a vector with odd coordinate sum must fail the E₈ membership test; the 248 must fail to decompose as
  stated under a wrong choice of the removed node.

## 6. What is needed from main or from another seat

Nothing. A question for the lane, if one arises, goes in the status file.
