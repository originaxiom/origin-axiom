# W-F2: of the two pure faces of three distinctions, all mirrors allows no history and all half-turns allows every re-description; the two mixed faces are not computed

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `reading:` with a computation. This note closes card W-F2
(`relays/cards/CHAT1_W-F2_mirrors_or_half_turns_and_what_the_record_holds.md`, 93ee47e4c). The foundations are this
seat's main task, at the author's word of 2026-11-14.

**How it was checked.** Computed once, on this seat's own code; expectations committed first.
- The script was sealed (sha256 `4747a419…36de51d7`) and run once. Every expectation was met.
- Tested against planted errors (1): a peripheral test that compares words exactly, without conjugacy. It rejects a
  step the conjugacy test accepts. This control is weak: it compares one word only.
- The record's pages were read through the mask only after the output was committed (7e8bd21d4).

## 1. The question

Three free distinctions, ℤ/2 ∗ ℤ/2 ∗ ℤ/2, are one abstract group. Geometrically each side of an ideal triangle can be a
mirror or a side folded by a half-turn, independently. That gives **four faces with the same group: three, two, one or
no mirrors.** This card compares the two pure faces:
- **all mirrors** (the reflection group of the ideal triangle): the cusps are the three pair products ab, bc and ca, and
  the even part is the thrice-punctured sphere;
- **all half-turns** (the sphere with three cone points of order 2 and a puncture, under the once-punctured torus): the
  one cusp is the triple product abc, and the even part is the once-punctured torus, with [x, y] conjugate to (abc)⁻².

A re-description, meaning a sequence of W-F1's seven moves, is a *history step* of a face when it carries that face's
cusps to cusps, up to conjugacy and inverse.

## 2. The results (move sequences of length up to four, counted with repeats: 2,800)

| line | result |
|---|---|
| M1 | **All 2,800** carry (abc)² to a conjugate of (abc)^±2: each is a history step of the all-half-turn face |
| M2 | **538** carry the three pair cusps to themselves. On H₁ of the even part, up to sign (that is, up to inner automorphisms), they give **only 6 matrices**, all of finite order: the images of the permutations of the three distinctions |
| M3 | **380** have \|trace\| > 2, for example (a through b)(b through a)(b through c) ↦ [[−3, 2], [2, −1]]. **None** of them keeps the pair cusps. \|trace\| > 2 detects hyperbolicity only at determinant +1. At determinant −1, as B749 F2's own caveat says, a matrix with trace ≠ 0 is hyperbolic too. [[1, 1], [1, 0]] = L·P is among the 2,800 and is not counted in the 380. M2 covers every sequence that keeps the pair cusps, so the verdicts do not change |
| controls | the swap of a and b keeps the pair cusps; "a through b" does not; the exact-word test rejects the swap's image of the half-turn cusp, and the conjugacy test accepts it |

**What it shows, within these sequences.** On the all-mirror face, the history steps act on H₁ only by the six
permutations, up to sign and inner automorphisms. No aperiodic history runs there (GM3). On the all-half-turn face,
every re-description is a step, including hyperbolic ones. **So, of the two pure faces, only all half-turns, whose even
part is the once-punctured torus, lets a history run.**

**What it does not show.**
- That the all-mirror steps form a finite group in full, modulo inner automorphisms. That is the standard finiteness of
  the thrice-punctured sphere's mapping class group. The sequences agree with it within their reach.
- **The two mixed faces.** By the referee's hand work, not checked here: with two mirrors and one half-turn the steps
  look finite. With one mirror and two half-turns there is an infinite-order step, (swap b, c)(c through b), which keeps
  that face's cusp and acts as [[1, 0], [1, 1]], a parabolic. That face is excluded only if GM3 is read as "hyperbolic".
  B749 F2 does put parabolic classes among the degenerate ones, but this card did not compute the mixed faces.

## 3. W-F1's table of opposites, updated

| postulate | its opposite | so it is |
|---|---|---|
| three distinctions | one or two: finite or flat (W-F1, A1) | strengthened against fewer; four or more are alive, so **a choice** against more |
| incompatible distinctions | compatible: abelian, trace +2 (W-F1, A3) | strengthened |
| all half-turns | all mirrors: only the six permutations on H₁ (this note) | **strengthened against all mirrors, given GM3**; the mixed faces are not computed |
| the puncture | a cone point of order k: k = 2 flat (W-F1, A4); k ≥ 3 alive | **a choice** against k ≥ 3 |
| GM3, aperiodic | periodic: degenerate (B749 F2) | strengthened |
| SE1, SE2 | other torsion, and the Gieseking manifold: alive (GENESIS §§ 3–4) | **choices** |

**A narrowed reading.** Between the two pure faces, GM4's carrier reduces to three free distinctions plus GM3.
- Three gaps keep this a reading and not a result:
  - the mixed faces;
  - the standard finiteness fact;
  - GM3 read as "hyperbolic" (for the one-mirror face).
- Freeness of the three is itself the puncture choice of the row above. That it is B1910's freeness premise in other
  words is this seat's reading; B1910 was not read for this card.

## 4. What the record already holds (part 2 of the card)

These lines were read through the mask after the run:
- B749 F2's output, lines 51 and 112;
- B1291's `orbifold.py`, lines 42, 45, 85 and 127, and the head of B1291's FINDINGS;
- TERMINOLOGY.md, lines 627–631;
- B1073's FINDINGS, lines 57–61;
- RECOGNITION.md, lines 20–24;
- the register, rows P-408 and P-409.

What they hold:
- **B749 F2's output** has the geometric fact: the quotient of the once-punctured torus by its order-2 symmetry is
  "S^2(2,2,2) minus point, chi_orb = -1/2", and the closed case is the flat [2, 2, 2, 2]. There it serves GM3: a periodic
  monodromy is degenerate.
- **B1291's orbifold code** lists the closed spherical S²(2,2,2) and the flat [2, 2, 2, 2], not the punctured
  orbifold. That file is headed as withdrawn as an argument and kept as a record.
- **"Three involutions" elsewhere is another object:**
  - in TERMINOLOGY.md (B730), the involutions of the Galois group V₄ of ℚ(√−3, √5);
  - in B1073, the three involutions of the central V₄, with the Galois V₄ beside them;
  - in RECOGNITION.md, a remark on one row of a value table;
  - in rows P-408 and P-409, the involutions of a filling's symmetry group in Witten's frame.

So, on the lines read, the record holds the orbifold but not the reading: three free distinctions carrying the two
records, the commutator and the moves. Pages not read may hold more.

## 5. For main

One row, if main agrees: the distinction layer, with W-F1 and W-F2 as its first two computations. Its open items are
the choices of § 3 and the two mixed faces. A second computation on another seat's code is needed before any of it is
banked.

## 6. Files

`relays/chat1_2026-11-14_wf2/`: `wf2_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf2_checks_out.txt`,
`wf2_checks_err.txt`.

This note was read by one session before it was pushed.

0 of 19.
