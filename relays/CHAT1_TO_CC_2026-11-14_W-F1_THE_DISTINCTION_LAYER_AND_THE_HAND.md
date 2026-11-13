# W-F1: three independent distinctions carry the grammar's two records, its commutator and its moves; at the common point the hand of the act flips under every move, as B1607 found

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `verify:` and `reading:`. This note closes card W-F1
(`relays/cards/CHAT1_W-F1_the_distinction_layer_and_the_hand_at_the_common_point.md`, b1928bad0). The card was opened at
the author's word to this seat on 2026-11-14: the foundations are now this seat's main task, and it computes for itself
the checks other seats proposed.

**How it was checked.**
- **Recomputed independently** (on this seat's own code; expectations committed first): B0's census, which is the
  record's, and the part of B3 that overlaps B1607.
- **Computed once** (expectations committed first): Part A, B1, B2's count, and B3 beyond B1607's reach.
- Part B's expectations were derived by hand before the run, without reading B1607, B1610 or the weave page.
- The script was sealed (sha256 `59c583ec…8cf543f4`) and run once. Every expectation was met.
- Tested against planted errors (2):
  - an automorphism claimed to be L that is not. The abelianisation check rejected it.
  - the act's own lift compared with its negation. It reported no flip, as it must. This control is weak: it shows
    only that the comparison can say "no flip".
- The record's definitions of the hand were read through the mask only after the output was committed (a4a928f0b): the
  weave page's B1607 to B1610 sections, and B1607's FINDINGS. W1, W24 to W29 and W34, which the card named, were not
  read.

## 1. Part A: the distinction layer

| line | what was computed | result |
|---|---|---|
| A1 | the Tits form of rank n distinctions with no relations (the universal Coxeter group) | rank 1 positive; rank 2 degenerate (1, 0, 1); rank 3 (2, 1); rank 4 (3, 1); ranks 5 and 6 (n − 1, 1) |
| A2 | in ℤ/2 ∗ ℤ/2 ∗ ℤ/2, with x = ab and y = bc | a[x, y]a = (abc)⁻², as reduced words. With the Pauli triple: s₁s₂s₃ = iI, s₃s₂s₁ = −iI, and [x, y] = −I, trace −2 |
| A3 | three commuting involutions, 200 draws | [x, y] = I, trace +2, every time |
| A4 | the orbifold S²(2,2,2,k) | χ = 0 at k = 2, where [x, y] = 1 (flat); χ < 0 for k from 3 to 12; −½ at the puncture |
| A5 | re-descriptions of the three distinctions, on H₁ of the even part | up to sign, L = (swap a, b)(a through b), R = (swap b, c)(a through b), P = (swap a, c) |

**What it shows.** Three distinctions with no relations among them produce, as exact facts:
- two records: the even part, free on x and y;
- the commutator as the square of the product of the three;
- the quaternion point's trace −2, from the Pauli triple;
- the grammar's L, R and P, as re-descriptions of the three.

The facts themselves are standard. Reading them as a layer under GENESIS § 2 is this seat's, and it is a reading, not
a derivation.
- **What the text search found.** A search of the record's pages for the free product's notation finds nothing. But
  the record has nearby material:
  - the orbifold S²(2,2,2,·), whose group this is, appears in the code and output of B1291 and B749 F2;
  - "three involutions" appears in B1073's FINDINGS, in TERMINOLOGY.md and in the register;
  - the agy lane's bridge note of 2026-11-07 has the two-involution case and the traceless triples;
  - the speculation file `S_THE_FIELDS_GENESIS.md` has the cone points.

  This seat has not read the first two. Whether the record already holds this reading is open.

**The postulates by their opposites.** Part A decides three rows of the test "is the opposite dead or alive?":
- one or two distinctions: dead (finite, or a flat counter). Four or more are alive (signature (n − 1, 1)), so "three
  rather than more" stays a choice by this test;
- compatible distinctions: dead (abelian, trace +2: cancellation completes);
- the puncture against a cone point of order k:
  - k = 2 is dead (flat);
  - k ≥ 3 is alive: χ < 0, a hyperbolic orbifold. This was computed for k = 3 to 12; for every k ≥ 3 it follows from
    the formula χ = 1/k − 1/2.

  So the puncture stays a choice against cone points of order 3 and up. This is consistent with GM4's puncture being
  CONDITIONAL.

Rows not computed here:
- mirrors against half-turns. The thrice-punctured sphere's mapping class group is finite, which is standard and not
  computed here; no verdict is given;
- GM3 (B749 F2);
- SE1 and SE2. On the record's own counts, their opposites are alive: SE1's admits the other states of the census
  (GENESIS § 3); SE2's admits the Gieseking manifold (T-ROOT, GENESIS § 4; B1607 C1). Both stay choices.

## 2. Part B: the arrow and the hand

| line | result |
|---|---|
| B0 | **758 states and 536 manifolds**, the census of GENESIS § 3, recounted. The automorphism of every canonical word abelianises to its matrix (both signs), and so do the inverses of the first 200; rotations and conjugates were not checked this way. 2O has 48 elements |
| B1 | for all 8,190 words of length 1 to 12: rev(w) = D w⁻¹ D, and w⁻¹ = J wᵀ J⁻¹ |
| B2 | **66 of the 536 manifolds** (33 for each sign) are amphichiral, the root among them. On these, reversing the act is a symmetry |
| B3 | 326 odd-trace states (163 for each sign); 3,608 cases, each a state with a sign and a rotation. In every case: the act's lift h is found, unique up to sign, of order 3 or 6. Its class among A₄'s rotations of order 3 (ω against ω²) **flips under inversion**, **flips under conjugation by L, R and P**, and **is kept by D, by −I (ι) and by the inner automorphisms**. The class does not depend on the sign, since −I lifts into Q₈. So on all 163 odd-trace states it takes both values across the rotations of the word |

**B3 agrees with the record where the two overlap.** It is a second computation of B1607's W26 statement:
- the weave page: "the McKay orientation (ω vs ω²) flips at every tick, is not a thread invariant and is not the mirror
  bit";
- B1607 C2b, computed there on σ, σ⁻¹, the mirror rule and the generators' lifts: the lifts of L, R and P lie outside 2T,
  and ι's lift lies inside;
- B1607 C3a to C3c, computed there on the parity 3-cycle of 30 odd-trace words to length 8.

The parity 3-cycle and this note's lift class agree because 2T/Q₈ ≅ ℤ/3. B1607's C1, C2a and C3d have no counterpart
here. This note covers the census to length 12, both signs and every rotation.

**What it means for "the hand is the arrow"**, a reading put to the author by another seat. The record has two hands,
B1607's (i) and (ii). Part B and the record together place each one:
- **The McKay orientation**, hand (ii), this note's bit:
  - it flips when the act is undone;
  - it also flips under the moves L and R, under the swap P (whether P is a move is GM5c, open), and under every odd
    rotation of the word.

  So it belongs to where the word starts, not to the thread: B1607's "not a thread invariant". B1610 calls it a naming
  on other grounds, the torsor's swap bit. It fails the reading's condition that a handed quantity stay put under
  everything else.
- **The records' orientation** (T against T̄), hand (i):
  - it is kept by every move of determinant +1, and by inversion (det φ⁻¹ = det φ);
  - it is reversed only by acts of determinant −1 (B1607, B1610).

  So it does not follow the arrow.
- **The only quantity found that follows the arrow** is the bundle's orientation: the fibre's hand times the arrow.
  B1914's twin depends on that product alone, computed twice (by main, and by this seat in W-C5). On the 66
  amphichiral manifolds the product is a symmetry.

So "the hand is the arrow" does not hold for either of the record's hands as stated. What holds is narrower: one
observable sees only the product of hand and arrow. B1610 already refuted, on 2026-10-08, the sealed headline that the
two hands are one bit; nothing here changes that.

## 3. What was not checked

- Whether the three-distinction reading appears in the record under other words. Only a text search was made.
- The weave page's W30 is the SM seat's finding, marked there as unverified. B1609's "three's hand" is main's. Both
  were read, not recomputed.
- The SM seat's test on acts of determinant −1. It needs that seat's sector modules, and is not run here.

## 4. For main

Two rows, if main agrees:
- **B1607's W26 statement now has a second computation:** this note's B3, to length 12.
- **The distinction layer as a reading to test further.** Its next card would compute the rows of § 1 not decided here.

## 5. Files

`relays/chat1_2026-11-14_wf1/`: `wf1_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf1_checks_out.txt`,
`wf1_checks_err.txt`.

This note was read by one session before it was pushed.

0 of 19.
