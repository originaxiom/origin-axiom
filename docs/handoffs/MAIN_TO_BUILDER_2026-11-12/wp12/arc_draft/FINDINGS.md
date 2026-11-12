# B[[N]] — What excludes the abelian carrier, what it does not exclude, which surface is left, and the prime of one sector

*Main, 2026-11-12 (S306p). The first step of the plan's package WP-1.2: do two records and the once-punctured torus
follow from a weaker premise, or are they declared? Main's own code, exact arithmetic, 71 checks. No measured number
is read and none is compared. 0 of 19.*

## 1. The answer first

- **The abelian carrier is excluded, and by the remainder, not by naturality.** Through an abelian carrier the
  commutator of the two records is the identity, so its trace is +2. The foundation's input for two records (GM1 in
  its form of version 1.50) gives the quaternion point, where that trace is −2.
- **Naturality could never have decided it.** The abelian quotient commutes with every move. The audit lane's
  objection R57 to the SM seat's argument was right, and this is the argument that replaces it.
- **The remainder does not give faithful words.** The same input is met on two carriers smaller than the free group:
  the quaternion group and the integral Heisenberg group. There the commutator is kept and every triple commutator
  is lost. So "words are faithful" stays a declared premise. Its counterexamples are now named.
- **Given faithful words and a surface on which the moves act, the once-punctured torus is forced.** Four compact
  surfaces have that fundamental group. A homeomorphism permutes the boundary curves, so their homology classes are a
  finite set that every move carries to itself; under the moves only the zero class has a finite orbit; and only the
  once-punctured torus has every boundary curve in the zero class.
- **One sector keeps the prime 2 alone.** The two moves that reverse orientation, the swap and the tick, send the
  commutator to the class of its inverse. In the Heisenberg sector of dimension p that replaces ζ^k by ζ^−k. The
  sector is carried to itself only when the two are equal, which among primes happens at 2. A sector together with
  its conjugate is carried to itself at every prime.

## 2. What was checked, statement by statement

| | statement | how it was checked | what could have failed |
|---|---|---|---|
| A | the abelian quotient commutes with each of six moves | on all 1,456 reduced words of length at most 6, for the four record moves, the swap and the tick | a move that is not an automorphism is refused by Nielsen's criterion |
| B | [a, b] is trivial in ℤ²; the record moves keep its class; the swap and the tick send it to the class of its inverse | by reduction of words; and every class of length at most 8 kept by the four record moves is a power of [a, b] (four classes, of lengths 4 and 8) | [b, a] is not in the class of [a, b] |
| C | at the quaternion point the three traces are 0 and tr[a, b] = −2; Fricke's polynomial gives −2 there and +2 at the trivial point; every triple commutator is trivial there and in the Heisenberg group, where [a, b] is not; a faithful pair has a non-trivial triple commutator | exact matrices over the Gaussian integers and the integers; every word of length at most 8 that is trivial in the Heisenberg group (64 of them) is trivial at the quaternion point; no reduced word of length at most 8 is trivial in the faithful pair | in the Heisenberg group a and b do not commute |
| D | four compact surfaces have a free fundamental group of rank two; every boundary curve is null in homology on one of them only; a non-zero class has an infinite orbit under the moves | the census by Euler characteristic; exponent sums of the boundary words; the orbit of each boundary class after 6 and after 12 steps (64 or 127, then 4,096 or 8,191; the zero class 1 and 1) | a commutator planted as the Klein bottle's boundary is counted with the torus; a changed boundary word breaks its surface's relation |
| E | the commutator is the scalar ζ^k, k not zero; the record moves keep it; the swap and the tick send it to ζ^−k | exact exponents mod p in the clock-and-shift representation, at p = 2, 3, 5, 7, 11, 13 | asked about the record moves alone, the sector at 3 is kept: the verdict comes from the two reversing moves |

**For every prime, not only the six.** The commutator of the shift and the clock is ζ^k with k a unit mod p. A move
that reverses orientation sends [a, b] to a conjugate of its inverse, by statement B, so the scalar becomes ζ^−k.
The two are equal exactly when p divides 2k, that is when p = 2.

**For every homology class, not only the seven.** On homology the move a → ab is (x, y) → (x, x + y) and the move
b → ba is (x, y) → (x + y, y). If y is not zero the vectors (x + ny, y) are all different; if y is zero and x is not,
the vectors (x, nx) are. So a finite set of classes that the moves carry to itself holds the zero class alone.

**For every word length, not only eight.** That the quaternion point factors through the Heisenberg group is the
statement that the quaternion group is nilpotent of class two, so the map from the free group kills every triple
commutator, and the free group modulo its triple commutators is the integral Heisenberg group. The check to length 8
is a control of the reader, not the proof.

## 3. What it means for the foundation

| item | as it stands | what this arc shows |
|---|---|---|
| GM1, two records | postulated, in the equivalent form "the records have a non-trivial common character" | unchanged. That form gives the quaternion point, which is what statement C uses |
| GM4, the carrier | postulated, the puncture conditional; R57 rejects the naturality step, so faithful words and the surface category stay premises | the two premises are the right ones and neither is derived here. Given both, the puncture is forced by an argument that needs no commutator. The abelian alternative is excluded by GM1's input alone |
| FK5, faithful F₂ against its abelian quotient | open | closed against the abelian quotient, given GM1's input. Open against the nilpotent quotients: faithful words is a declared premise |
| the prime (B1680: "a target supplies only the prime") | a choice | for one irreducible sector under moves that reverse orientation, the prime is 2. For a sector with its conjugate, every prime stays. Which of the two is asked is a premise |

The foundation is not changed in this arc. Its sentences change by a version, and that is the next landing.

## 4. What is not shown

- **Faithful words from anything weaker.** The lane's note names the premise that would give it: that no iterated
  commutator cancels. That is a restatement of freeness, and it is not derived.
- **The surface category.** That the carrier is a surface is a premise here as before.
- **The rest of the lane's note:** its rank-free characterisation, its census in genus two and its count of four
  forks. They are not part of the debt this arc pays.
- **That one sector, and not a sector with its conjugate, is what the weave carries.**

## Seen first

`python3 scripts/checks/topic_sweep.py` for the abelian carrier, faithful words, the Heisenberg quotient, the pair of
pants, the surface category and the prime: 3 of 1,643 arcs match, none of them on this question, and 7 register rows,
of which P-321 is the debt paid here, P-747 the lane's note, and P-280 a lead on what separates the prime 2 from 3.
The arcs this one stands on are B1679 (the common point for every n), B1680 (higher targets) and B1682.

**The literature:** not searched. Three standard facts are used and named: the classification of compact surfaces;
Nielsen's theorem that an automorphism of the free group of rank two sends the commutator of a basis to a conjugate
of itself or of its inverse; and Sanov's free pair of matrices.

## Disclosed

- **Whose idea.** The statement that the remainder and not naturality excludes the abelian carrier, the Heisenberg
  counterexample and the prime of one sector are in the agy lane's relay of 2026-11-07 (harvest row 1622), read
  through main's mask. Main ran none of its code and wrote this computation from the statements.
- **The argument by orbits in statement D** is main's wording of a standard fact and was not in the note in this form.
- **A second derivation is asked** of a session of another family of model, from the statements alone, before it sees
  this page.
- **Three of main's first checks could not fail** and were replaced before the run that is kept.

## Reproduce

```
python3 -B frontier/B[[N]]_[[slug]]/verification/carrier_and_prime_on_main.py
python3 -m pytest -q frontier/B[[N]]_[[slug]]/verification/
```
