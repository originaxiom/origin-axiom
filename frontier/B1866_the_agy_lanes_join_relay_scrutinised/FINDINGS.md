# B1866 — The agy lane's relay on the register-to-field join, scrutinised at the owner's word

*Main, 2026-11-10 (S306o). The owner: "scrutinize origin/agy/audit-2026-11-02 @ da5c71251
(relays/AGY_TO_CC_2026-11-10_P753_REGISTER_TO_FIELD_JOIN.md) before banking WP-2.2 and WP-3.2 onto main." The relay
was read in full through the sealed mask. None of the lane's code was run or imported. Every claim that main can test
was computed with main's own code (`verification/join_scrutiny.py`). Data-free. 0 of 19.*

## 1. The answer first

- **Where main can test the relay, the relay is right.** Ten of its claims are verified by main's own computation.
  Main found no error in them.
- **Its catch on main's own note is correct.** The closure programme's package WP-2.2 carried an exploratory sentence
  of main's: "of the two coherent lifts, one has characters every move keeps". That is false. The two lifts give one
  and the same pair of lines, and the moves carry that pair to three backgrounds. The physical lane's own text already
  said the two lifts exchange the lines; main had misread it. The sentence is withdrawn.
- **One statement needs a qualifier, and one result is undersold.**
  - "The weave's triplet is not the symmetric square of any 2-dimensional representation" is true of the double cover
    of SL(2, ℤ). It is the symmetric square of a doublet of the braid group, and projectively it is the symmetric
    square of the level-2 doublet.
  - The relay says the lanes' one-form triplet over the three backgrounds "never" has the weave's group of order 96.
    True. Main computes more: it is the weave's triplet after one odd character, χ₉. The two are one projective
    representation.
- **Three groups of claims stay the lane's,** because they are about the lanes' operator, which main has not verified:
  which mode carries which character; how the modes split on one background; the table over all 248 dimensions.
- **So WP-2.2 and WP-3.2 are not closed.** What is banked here is the scrutiny, and the facts main computed itself.
  Each package's question is restated in § 5, sharper than before.

## 2. Claim by claim

| | the relay says | main's check | result |
|---|---|---|---|
| 1 | every move keeps the quaternion holonomy | main's own theorem (the common point at two records) | on main already |
| 2 | every move keeps the odd spin structure; the three even ones are permuted | part 1, exact: spin structures as quadratic refinements mod 2 | **verified** |
| 3 | the trivial character is the one flat character every move keeps | part 1 for the four sign characters; for all characters, (x, y) fixed by both moves forces x = y = 1 | **verified** |
| 4 | one background is not kept: it has an orbit of three, and its stabiliser has index 3 | part 1: the pair of lines {trivial, χ₍₁,₁₎} goes to three pairs; S and L² keep it, L and R alone do not | **verified** for the pair of lines of the physical lane's own formula |
| 5 | the two coherent lifts are one choice, and neither is kept by every move | part 1 (the same unordered pair at α = ±1) and part 2 (in E₈, −1 of SU(4) is −1 of Spin(10), on all 240 roots) | **verified**; main's note withdrawn |
| 6 | on the weave's triplet the moves generate a group of order 96 with centre of order 4 and projective image S₄; S⁴ = −1, so it does not factor through SL(2, ℤ) | part 3: 96; scalars the four powers of i; modulo scalars 24 with S₄'s element orders (1, 9, 8, 6); the braid relation; S² = i, S⁴ = −1, S⁸ = 1 | **verified** |
| 7 | no even twist of the symmetric square of the level-2 doublet is the triplet; it is an odd twist | part 3: all 24 twists. Even twists give orders 24, 48, 72, 144, never 96. Equivalent to the triplet at m = 15 only (m = 3 for the conjugate doublet); to its conjugate at m = 21 (9) | **verified** |
| 8 | the triplet is the symmetric square of no 2-dimensional representation of the double cover | part 3: with t² the odd character, T ≅ Sym²(tD), and (tD)(S)⁸ = −1 | **true, with a qualifier** (§ 3) |
| 9 | the conjugate of (θ₂², θ₃², θ₄²)/η³ transforms by two monomial matrices of eighth roots, equivalent to the triplet | part 4: the two matrices fitted from the functions themselves; they are the relay's; the conjugates are equivalent to the triplet | **verified** |
| 10 | induced over the three backgrounds, the spinor line gives a group of order 6, the one-form line a group of order 24, never 96 | part 5: 6 and 24, each equal to its order modulo scalars | **verified as algebra**; and more (§ 3) |
| 11 | on one background the modes split 1 + 1 + 1 and 1 + 2; which line carries which character; the table over all 248 dimensions; the Szegő residues | not checked | **the lane's** |
| 12 | the count of two plus one on one background is not the weave's triplet; reading it as three families is unearned | follows from 4: on one background only the stabiliser acts | **agreed** |
| 13 | the comparison of modules need not wait for the kernel theorem's domain | — | **agreed in part** (§ 5) |

## 3. What main found beyond the relay

- **The triplet is a symmetric square after all, one cover up.** Let D be the level-2 doublet (L ↦ diag(1, i),
  R = H·diag(1, −i)·H). Its group has order 96 and S⁴ = −1 on it.
  - Sym²(D) twisted by the character χ₁₅ (L ↦ ζ₂₄¹⁵) is the triplet. A square root of χ₁₅ is not a character of the
    double cover, whose characters are the 24th roots.
  - Take t = ζ₄₈¹⁵. Then tD is a doublet of the braid group, the triplet is Sym²(tD) exactly, and (tD)(S)⁸ = −1,
    (tD)(S)¹⁶ = 1. So tD lives on a further double cover.
  - Main's prediction of the morning, "the weave's triplet is the doublet's symmetric square", therefore holds
    projectively and over the braid group, and fails as a statement about linear modules of the double cover. The
    relay's sentence is the second half of that; the first half belongs beside it.
- **The lanes' one-form triplet is the weave's, up to one odd character.** Induce a line from the stabiliser of one
  background to all the moves, with the signs the relay gives for the one-form line (−1 on L², +1 on S). The result
  generates a group of order 24 and is an honest module of SL(2, ℤ). Twisted by χ₉ it is equivalent to the weave's
  triplet (by χ₁₅, to its conjugate).
  - So the two have the same action on three objects, the octahedral one, and differ by a character of order 8.
  - **What that character means is the open question.** An odd character of the double cover is what a half-form
    carries and a one-form does not. Whether the physical modes are one-forms or carry the half-weight is not settled
    by this algebra. It decides between "the lanes' three over the orbit is the weave's three" and "it is not".
  - The spinor line (signs +1, −1) gives a group of order 6. No twist makes it the triplet.

## 4. What is not verified

- **Anything about the lanes' operator.** Which zero modes exist on a background, how they split under the
  stabiliser, and which line carries which sign are the lanes' analysis. Main has not verified the kernel theorem
  (the programme's WP-3.1).
- **The lane's scripts.** Its "verified to machine precision" lines are its own. Main ran none of them.
- **The masked numbers.** The sealed mask hides most digits of the relay. Where the relay's number is hidden, main
  reports its own number. The visible structure agrees everywhere (one-digit and two-digit twists, the four orders
  over even twists, the monomial matrices).
- **That the lanes' "balanced carrier" is the pair of lines of the physical lane's formula.** Main takes that from the
  physical lane's own text, read through the binding-minimum mask.

## 5. What changes on main

- **WP-2.2, the background.** Verified: three data are kept by every move (the quaternion holonomy, the odd spin
  structure, the trivial character). The pair of lines is not: one background is one of three, a thread choice, and
  the three together are kept. The lift's sign is not a separate choice. **Left:** that the lanes' model's data are
  these, which needs the action verified on main (WP-2.1); and what the sum over the three backgrounds is physically.
- **WP-3.2, the join.** The first of P-753's three outcomes is refuted on one background, where only the stabiliser
  acts. The third holds there: the moves do not keep the background. Across the three backgrounds the question is now
  one sentence: **is the odd character χ₉ physical?** If the modes carry the half-weight, the lanes' three over the
  orbit is the weave's three. If they are one-forms, it is the same octahedral action and a different module.
- **P-753's prediction, scored.** Main gave 65 % to "a doublet and a singlet under the moves, the triplet the
  doublet's symmetric square". The first half is wrong: the moves do not act on one background's modes. The second
  half holds projectively. The alternative main gave 25 %, that the background sits over one of three parities, is
  what holds on one background.
- **The order of work.** The identification of the weave's own triplet (rows 6 to 9) needs nothing from the lanes and
  is banked here. Which modes exist on a background still needs the kernel theorem, so WP-3.2 keeps WP-3.1 as a need
  for that half.
- **Labels.** Rows 2, 3 and 6 to 9 are statements about the joint action of the moves: weave. Rows 4, 5 and 11 are
  about one background: thread. Row 10 is about the orbit of three taken together: weave in form, on the lanes'
  characters.

## Seen first

- **The repo sweep:** P-753's row and main's statement before computing; B1610 and B1611 (the triplet's
  construction); B1687 (the weave's group as the Clifford group modulo phases); the physical lane's kernel proof,
  re-read at its equations for the two lines through the binding-minimum mask; the relay itself, lines 1 to 116,
  through the sealed mask.
- **The literature:** the theta constants' transformation laws and the duplication formulas are classical; they are
  recomputed here from the series, not cited as evidence. The Weil representation at level 2 is standard.

## Disclosed

- **Main's own note was wrong and another lane caught it.** It stood for a few hours in the programme's source, marked
  exploratory, and was never banked.
- **Main reads the agy lane only through the sealed mask,** which hides most digits. The scrutiny is therefore of the
  relay's statements and structure, with main's own numbers in place of the hidden ones.
- **Two of the ten verifications are floating-point** (the triplet's matrices come from main's own cohomology code;
  the theta vector from its series). The groups are finite, their elements are separated by order one, and the
  equivalences are tested by characters over the whole group.

## Reproduce

```
python3 -B frontier/B1866_the_agy_lanes_join_relay_scrutinised/verification/join_scrutiny.py
python3 -m pytest -q frontier/B1866_the_agy_lanes_join_relay_scrutinised/verification/
```
