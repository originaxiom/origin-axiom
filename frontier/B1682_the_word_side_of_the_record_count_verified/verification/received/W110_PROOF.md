# W110 — the word side of the record count: for n ≥ 3 no non-trivial conjugacy class of F_n is kept by every transvection, even up to inversion; at n = 2 the kept classes are the powers of [a, b] (the proof, written before its checks)

**Why.** Main's relay of 2026-10-20, CC_TO_ALL_SEATS_2026-10-20_TWO_RECORDS_DERIVED_AND_THE_END_LAW_QUESTION.md (§2),
asks this seat for the word-side cell C4 from its relay §162: "Count the conjugacy classes kept by every move at n = 3,
4. … That would join GM1 to PF1 on words." (GENESIS GM1, the two records, and PF1.) W109 settled the character
side for every n.

**Weave or thread.** A WEAVE result about the forms.
- It takes every move of the weave of n records, and every conjugacy class of F_n, with none hand-picked.
- Its quantity is defined by the joint action: a class kept by every move.
- Its claim is about all moves, all classes and all n ≥ 3 at once.

**The order.**
- This proof was worked by hand on 2026-10-20 and is committed before its checks script exists.
- Before it, only §162's exploratory note was on record: at n = 2, 3 of 25,654 classes to length 12 are kept; at n = 3,
  0 of 313 balanced classes to length 8.

## Notation

- F_n is free on a₁, …, a_n. For i ≠ j, R_ij is a_i ↦ a_i a_j and L_ij is a_i ↦ a_j a_i; the other letters are fixed.
- A conjugacy class is a cyclic word: a cyclically reduced word w, read around a circle. ‖v‖ is the length of the
  cyclic reduction of v.
- A move φ **keeps** the class of w when φ(w) is conjugate to w, and keeps it **up to inversion** when φ(w) is conjugate
  to w or to w⁻¹.
- If φ keeps a class, so does φ⁻¹. Either way, keeping implies ‖φ(w)‖ = ‖w‖.

## The theorem

1. **(i) Every n ≥ 3.** If ‖R_ij(w)‖ = ‖R_ij⁻¹(w)‖ = ‖w‖ for every ordered pair i ≠ j, then w = 1. So no non-trivial
   class of F_n is kept by every R_ij, even up to inversion. The same holds for the L_ij.
   - More sharply: if, for one i, the lengths are kept by R_ij^{±1} for every j ≠ i, then a_i does not occur in w.
2. **(ii) n = 2.**
   - **The kept classes.** The classes kept by the record's R (a ↦ ab) and L (b ↦ ab) are exactly those of [a, b]^k,
     for k ∈ ℤ.
   - **With the inversions.** Under all of Aut(F₂), inversions included, the same classes are kept up to inversion,
     and only the trivial class is kept exactly.

So on words, as on characters (W109), a non-trivial object kept by every move exists only at two records. There it is
the commutator [a, b], the word whose trace is GENESIS PF1's κ = tr[a, b].

## The proof of (i)

**Contacts.** Let w be a cyclically reduced cyclic word of length m. Let n_i be the number of letters a_i^{±1} in w.
- The **right contacts** of a_i are the successor of each a_i and the predecessor of each a_i⁻¹. There are n_i of
  them.
- For j ≠ i, write c_ij for the number of adjacent pairs a_i a_j⁻¹ or a_j a_i⁻¹, and c′_ij for the number of pairs
  a_i a_j or a_j⁻¹ a_i⁻¹.
- So c_ij + c′_ij is the number of right contacts of a_i that are a_j^{±1}.

**The lemma (Whitehead's count).** ‖R_ij(w)‖ = m + n_i − 2c_ij and ‖R_ij⁻¹(w)‖ = m + n_i − 2c′_ij.
- **The insertions.** R_ij writes a_j after each a_i and a_j⁻¹ before each a_i⁻¹. That adds n_i letters.
- **The cancellations.** An inserted a_j cancels exactly when the a_i is followed by a_j⁻¹. An inserted a_j⁻¹ cancels
  exactly when the a_i⁻¹ is preceded by a_j. Each cancellation removes two letters and uses a different letter of w.
- **No cascade.** After a cancellation the a_i (or a_i⁻¹) meets the image of the next (or previous) letter. No image
  begins with a_i⁻¹ or ends with a_i, so nothing further cancels. Between images without a cancellation, the only
  possible inverse pairs are the counted ones, or a pair a_k^{±1} a_k^{∓1} that a reduced w does not contain.
- **The inverse.** R_ij⁻¹ is a_i ↦ a_i a_j⁻¹, the same count with a_j replaced by a_j⁻¹.

**The count.**
- If the lengths are kept, then c_ij = c′_ij = n_i/2 for every j ≠ i.
- So the right contacts of a_i with a_j^{±1} number n_i, for each of the n − 1 letters j ≠ i.
- These contacts are disjoint, and there are only n_i in all. So (n − 1)·n_i ≤ n_i, that is (n − 2)·n_i ≤ 0.
- For n ≥ 3 this gives n_i = 0. Since this holds for every i, w = 1. ∎

**The left moves.** Let rev be the anti-automorphism that reads a word backwards, without inverting its letters. Then
L_ij = rev ∘ R_ij ∘ rev, and rev keeps cyclic lengths. So the L_ij keep the lengths of w exactly when the R_ij keep the
lengths of rev(w), and (i) applies to rev(w).

## The proof of (ii)

- **⊇.** Every automorphism of F₂ sends [a, b] to a conjugate of [a, b]^{±1}, with the sign of its determinant on ℤ²
  (Nielsen). The record's L and R have determinant 1. The inversion a ↦ a⁻¹ has determinant −1, and [a, b]^k is not
  conjugate to [a, b]^{−k} for k ≠ 0 (in a free group, w conjugate to w⁻¹ forces w = 1).
- **⊆.**
  - L and R map onto SL(2, ℤ) = Out⁺(F₂), so a class kept by L and R is kept by every automorphism of determinant 1.
  - On the once-punctured torus these are the mapping classes. The only free homotopy classes kept by every mapping
    class are the peripheral ones: a non-peripheral class meets some simple closed curve essentially, and the twists
    about that curve move it.
  - This standard fact is cited, not proved here. The census below checks it to length 12.

## A reading, not claimed new: the kept point and the kept word meet at κ = −2

- **The character side.** W109's kept point at n = 2 is the quaternion point (0, 0, 0), where tr[a, b] = −2.
- **κ = −2 is the root's value** (GENESIS PF1's mathematical form: the fibre's commutator trace, −2 at the root, the
  parabolic cusp).
- **The point is singular there.** On the level surface κ = x² + y² + z² − xyz − 2 = −2, the gradient
  (2x − yz, 2y − xz, 2z − xy) vanishes only at (0, 0, 0). So the quaternion point is the one singular point of the
  root's level surface.
- **The word side.** The kept word is the commutator, whose trace is κ.
- So the two sides meet on PF1's κ. On words the moves keep exactly the commutator. On characters they keep exactly
  one point, the singular point of the commutator trace's root level. This may be on record already (B160, B1404); it
  is offered as a reading.

## What is used, and what is new

- **Used.** Whitehead's length count for the elementary automorphisms (step (i) needs nothing else), Nielsen's
  theorem, and, for (ii) ⊆ only, the mapping-class fact.
- **New here.**
  - Statement (i), with its counting proof.
  - "No non-trivial class keeps even its length" is stronger than "no class is kept", and needs no census.
  - Statement (i) is probably known in some form. This seat has not searched the literature.

## The checks (one script, the_kept_words.py, committed before its one run)

The proof does not rest on them. Each check names its expected outcome and a prior.

| check | what | expected | prior |
| --- | --- | --- | --- |
| C1 | the lemma, by direct reduction, for every R_ij^{±1} and L_ij^{±1} (the latter through rev) on every class of the census | it holds on every class and move | 95% |
| C2 | n = 3 to length 8 and n = 4 to length 7: the classes kept by every transvection and by the full moves (inversions and transpositions added), exactly and up to inversion; and the classes keeping their length under every R_ij^{±1} | 0 in every count | 97% |
| C3 | n = 2 to length 12: the classes kept by ⟨L, R⟩, by the four transvections and by the full moves, exactly and up to inversion | [a, b]^k for k = 1, 2, 3 (three classes up to inversion) in every count but one; 0 for the full moves kept exactly | 95% |
| C4 | the singular points of the level surface κ = −2 | only (0, 0, 0) | 99% |

- **If a check fails,** it is recorded as failed. A failure of C1 or C2 would be a failure of (i), and it would be
  withdrawn as stated. A failure of C3 would put (ii) ⊆ in question. A failure of C4 would withdraw the reading.

## The scope

- Words are read as conjugacy classes, with the moves the record allows, for every n.
- Whether matter attaches to words or to characters stays a reading.

0 of 19.
