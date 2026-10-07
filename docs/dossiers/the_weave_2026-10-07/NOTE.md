# The weave: what the joint action of every allowed move forces on every thread at once

cc (the SM-derivation seat), 2026-10-07. **Structure and proofs only. No count is read.** Written for the owner's rule,
stated daily for a year and given a fixed name today, **the weave** (`docs/THE_WEAVE.md`). The rule: reality comes from
the interaction of all the objects the principle allows, together, and not from single objects or from covers of one.
- A **thread** is one allowed object, a closed path of moves through the shared fibre.
- **The weave** is the joint action of all the moves on that fibre, and what it forces.

Nothing below is read off one thread. Each step is PROVED here and checked by the scripts beside this note, unless it is
marked READING or OPEN. Nothing is promoted, and 0 of 19 stands.

## The setting

- **The shared fibre** is the two records, F₂ = ⟨a, b⟩, with puncture loop [a, b] (GENESIS GM1, GM4).
- **The moves.**
  - L and R are GENESIS GM2.
  - The sign −I is GM5b, and the swap P is GM5c; both are OPEN in GENESIS.
  - The weave below uses all four. Where L and R alone give a different answer, both answers are stated.
- **The threads** are every hyperbolic word in the moves, with either sign.
  - To length 8 there are 2,554, and 1,308 of them have odd trace.
  - m000 (LP, the Gieseking manifold), m003 (−LR), m004 (+LR) and +LLLR are among them.
  - None is derived from another.

## W1. The three (`moves_and_parities.py`)

- **The parities.** Mod 2 the records have three non-zero parities: (1, 0), (0, 1) and (1, 1).
- **Each single move fixes exactly one of them and swaps the other two.**
  - L fixes (1, 0), R fixes (0, 1) and P fixes (1, 1).
  - −I fixes all three.
- **Any two of L, R and P generate all six permutations of the three** (GL(2, F₂) = S₃), and their product cycles all
  three.
- **So the three belongs to no single move.** It appears as three parities permuted with none distinguished only when
  moves act together.
- **Which threads cycle the three.** A thread cycles them exactly when its trace is odd (sm:B1550's parity lemma). That is
  1,308 of the 2,554 threads, m000, m003 and m004 among them.
- **GENESIS's SE1** (∣2 − tr φ∣ = 1, so tr φ is 1 or 3) admits only odd-trace threads.

## W2. The common point (`the_common_point.py`, part 1)

- **The moves act on the fibre's characters** (x, y, z) = (tr a, tr b, tr ab) by polynomial maps that keep tr [a, b].
- **One point is fixed by every move.**
  - The puncture is parabolic: tr [a, b] = −2, which is the Markov surface x² + y² + z² = xyz.
  - The ideal of points fixed by every move is then (x, y, z), so there is exactly one such point: the origin.
  - The origin is the quaternion representation a ↦ i, b ↦ j, ab ↦ k, [a, b] ↦ −1.
  - Without the cusp condition the moves fix one more point, (2, 2, 2), where the puncture is trivial.
- **Each thread fixes the origin and its own geometric points besides** (exact Gröbner bases):
  - ±LR: two points, the roots of z² − 3z + 3, the same two for m004 and m003, since the sign acts trivially on
    characters;
  - +LLR, +LLLR and +LLRR: four points each;
  - an orientation-reversing thread such as m000: its geometric point is fixed by the map followed by complex
    conjugation. The map itself fixes only the origin.
- **So the threads' geometries differ, and the one structure they all share is the quaternion point.**
  - A single shear already fixes only the origin on the Markov surface.
  - A single shear is not a thread.
- **On record.**
  - Main's B141 has the quaternion point as the unique irreducible fixed point of the metallic map.
  - Main's B148 places it on the Markov surface.
  - This seat's sm:B1538 has its character ζ_H invariant under every Anosov monodromy.
  - **New here:** it is the only point every move fixes.

## W3. The common point on every thread (part 2)

- **The quaternion point extends to every thread.**
  - t ↦ g in the binary octahedral group 2O, with g i g⁻¹ = ρ(φ(a)) and g j g⁻¹ = ρ(φ(b)).
  - There are two choices, ±g.
- **On all 2,554 threads to length 8 the image is the binary tetrahedral group 2T = SL(2, F₃), of order 24, exactly when
  the trace is odd.**
  - It is Q₁₆ when φ fixes one parity, and Q₈ when φ fixes all three.
  - Modulo ±1 it is the fibre-parity group: A₄, D₄ or V₄.
- **So the tetrahedral cover and the spin cover built on m004 are not m004's.** They are sm:B1550's and the held
  sm:B1551's.
  - They are the kernels of this common structure on one thread.
  - m000, m003, +LLLR and every odd-trace thread carry the same A₄ and the same 2T.

## W4. The triplet (part 3)

- **The shared fibre carries a three-dimensional space with one line for each non-zero parity.**
  - The space is the parity-twisted cohomology ⊕_χ H¹(F₂; χ), summed over the three non-trivial parity characters.
  - Each line is one-dimensional, because the punctured torus has Euler characteristic −1.
- **The moves and the fibre's own inner automorphisms act on it by signed permutations.**
  - The group they generate has order 48 and acts irreducibly: Σ tr² / ∣G∣ = 1.
  - L, R and the fibre alone generate a group of order 24, also irreducible.
- **Every odd-trace thread acts on it as an irreducible triplet.**
  - The group of the thread's monodromy and the fibre is A₄, of order 12, for m004, m003 and +LLLR.
  - For the orientation-reversing m000 it is A₄ × ℤ/2, of order 24.
- **Even-trace threads split it.** +LLRR splits it into three lines, and +LLR into 1 + 2.
- **It matches the quaternion axes thread by thread, not on the weave as a whole.**
  - On m004, m003 and +LLLR it is the same representation as the axes i, j, k under the common point, with equal traces on
    all 12 elements.
  - On m000 it is the same up to m000's orientation sign.
  - On the weave as a whole the two triplets are different representations. Together they generate 192 pairs.
- **Prior: the A₄ triplet of flavour physics.**
  - The triplet of A₄ flavour models: Ma and Rajasekaran (hep-ph/0106291); Altarelli and Feruglio (hep-ph/0504165).
  - Altarelli, Feruglio and Lin obtain the A₄ from the four fixed points of T²/ℤ₂ (hep-ph/0610165). Their ℤ/3 comes from a
    hexagonal torus.
  - Here no torus is special. The ℤ/3 is the monodromy mod 2 of any odd-trace thread, and the triplet is the weave's.
- **Prior: the mathematics.**
  - Looijenga's Prym representations, Geom. Dedicata 64 (1997), study the mapping class group on such twisted cohomology.
  - Goldman, Geom. Topol. 7 (2003), studies the modular group on the one-holed torus's characters.

## What the weave gives, and what it does not

| step | status | what |
|---|---|---|
| W1 | PROVED | three non-zero parities, permuted with none distinguished only when moves act together |
| W2 | PROVED | one structure all threads share: the quaternion point |
| W3 | PROVED | on every odd-trace thread, the same A₄ and the same 2T from it |
| W4 | PROVED | one irreducible triplet, the same on every odd-trace thread; even-trace threads split it |
| W5 | READING (GENESIS FK14) | the three generations are this triplet: three, alike, carried into one another by the weave |
| W6 | OPEN | what each line carries: a whole generation (5̄ + 10) with its chirality |
| W7 | OPEN | which moves are in the weave (GENESIS GM5b, GM5c): the triplet's group has order 24 with L and R, 48 with all four |

- **In the owner's terms (READING).**
  - The three generations are on no object. They are the three parities of the shared records, and the weave makes them
    one triplet.
  - A thread with odd trace carries the whole triplet; every thread GENESIS's SE1 admits is such a thread. A thread with
    even trace breaks it.
  - The triplet does not depend on which thread is chosen.
- **What W6 needs.** The frame that reads a generation (sm:B1515's F-HE) is built on one thread's own holonomy, so it is
  a thread instrument. A weave instrument for a generation's content is not built.

## Files

- `moves_and_parities.py` → `moves_and_parities.json`: W1, every word to length 8.
- `the_common_point.py` → `the_common_point.json`: W2–W4. sympy's `solve` drops roots it cannot write in radicals, so
  the points are read from Gröbner bases. The quaternion closures are numerical on a group of 48 elements.
