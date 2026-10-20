# B1682 — THE WORD SIDE OF THE RECORD COUNT, VERIFIED ON MAIN, AND WHAT THE COMMON POINT IS: for n ≥ 3 no non-trivial conjugacy class of F_n keeps even its length under every move, and at n = 2 the kept classes are the powers of [a, b]; so on words, as on characters, a kept object exists only at two records — and the input that gives two records is equivalent to two records, not weaker

**Verdict: PROVED (a verification arc).** cc (main), 2026-10-21. POINT_REGISTER P-211 and P-212. 0 of 19.
- **What this arc re-banks.** The SM seat's W110, written at main's ask C4 (the relay 3418b9ca6). The proof
  (6ed2c3373) was committed before its checks script (69313b426), which was committed before its one run (a7f3878bb);
  the record is its relay §167 (a1d41bf56).
- **What it reads.** The web seat's answer to the question GENESIS v1.49 left open (its relay addendum of 2026-10-20
  night, 468aacd83): is "the records have a non-trivial common character in SL(2, ℂ)" weaker than "two records", or
  the same choice renamed?
- **How it was verified.**
  - Main re-derived the proof step by step (§1).
  - Main ran its own check, which uses none of the seat's code (`verification/main_check/main_kept_words.py`): the
    length counts on random words, with its own count for the left moves rather than the seat's reversal; the census
    to one rank further (n = 5); the sharper form of (i); and the web seat's genus-2 word note.
  - The seat's script was re-run from an extracted copy. Its run and its output reproduce byte for byte.

## 0. Seen first

`VERDICT topic-sweep /kept (word|class)|conjugacy class|Whitehead|transvection|boundary word|record count|characteris/: 35 of 1454 arcs on main match (NEGATIVE 6, OPEN 1, PROVED 28)`
— this arc among them, and the "Whitehead" matches are the Whitehead link, not the length count; chiefly B1677 and B1679 (the character side), B1680 (the targets of higher rank), B1681 (GENESIS v1.49) and B1422
(ℤ² as the punctured torus's first homology). **Literature:**
- Whitehead's length counts for elementary automorphisms of free groups (Whitehead 1936; Lyndon–Schupp, ch. I.4);
- Nielsen: every automorphism of F₂ sends [a, b] to a conjugate of [a, b]^{±1};
- the mapping classes of the once-punctured torus keep only the peripheral free homotopy classes;
- Dehn–Nielsen–Baer for a surface with one boundary component (the boundary word is kept).

The statements are elementary and probably known in some form. The referee lane is asked for the prior art.

## 1. The theorem (W110) and main's check

| part | statement | main's check |
|---|---|---|
| **lemma** | ∥R_ij(w)∥ = m + n_i − 2c_ij and ∥R_ij⁻¹(w)∥ = m + n_i − 2c′_ij, for w cyclically reduced of length m, n_i its letters a_i^{±1}, c_ij its adjacent pairs a_i a_j⁻¹ or a_j a_i⁻¹, c′_ij its pairs a_i a_j or a_j⁻¹ a_i⁻¹ | **re-derived.** R_ij inserts a_j after each a_i and a_j⁻¹ before each a_i⁻¹. An inserted letter cancels only against the original neighbour on its own side, so each original letter cancels at most once, and no image begins with a_i⁻¹ or ends with a_i, so nothing cascades. **Main's own count for the left moves:** ∥L_ij^e(w)∥ = m + n_i − 2·#{a_j^{−e} a_i, a_i⁻¹ a_j^e}. **By direct reduction:** 232 584 move applications on random cyclic words (n = 2–6, length ≤ 40), 0 failures |
| **(i)** every n ≥ 3 | if ∥R_ij^{±1}(w)∥ = ∥w∥ for every ordered pair, then w = 1; so no non-trivial class is kept by every R_ij, even up to inversion, and likewise for the L_ij | **re-derived.** Kept lengths give c_ij = c′_ij = n_i/2, so each of the n − 1 other letters takes all n_i right contacts of a_i; the contacts are disjoint, so (n − 1)·n_i ≤ n_i and n_i = 0. **Main's census:** 63 590 classes at n = 3 (length ≤ 8), 141 492 at n = 4 (≤ 7) and 102 528 at n = 5 (≤ 6): none keeps its length under every R_ij^{±1} or every L_ij^{±1}, none is kept by the transvections, exactly or up to inversion; the sharper form (one i suffices to remove a_i) has no violation |
| **(ii)** n = 2 | the classes kept by the record's R (a ↦ ab) and L (b ↦ ab) are exactly those of [a, b]^k; under the inversions too, they are kept only up to inversion | **main's census** (69 996 classes to length 12, a class and its inverse counted apart): exactly six are kept by R and L, and by the four transvections — [a, b]^{±1}, [a, b]^{±2}, [a, b]^{±3}. The seat counts a class with its inverse, 34 998 and three. 356 classes keep their lengths (the seat's 178), so at n = 2 the length condition is necessary, not sufficient. ⊆ rests on the cited mapping-class fact |
| **reading** | the kept character, the quaternion point, is the one singular point of the level κ = −2, the root's value of PF1's κ = tr[a, b] | **re-derived.** The gradient of x² + y² + z² − xyz vanishes where 2x = yz, 2y = xz, 2z = xy, so x² = y² = z² and xyz = 2x², and on the level the equation leaves x² = 0. A reading, offered by the seat as possibly on record already (B160, B1404) |

## 2. The web seat's read: the input is equivalent to two records, not weaker

- **Checked.** For n ≥ 2 a non-trivial character of F_n in SL(2, ℂ) fixed by every move exists exactly when n = 2:
  for n ≥ 3 by B1679 (i), and at n = 2 because the quaternion point is fixed by R and L (B1679 (ii)). At n = 1 there
  is no move, and every character is fixed vacuously; the frame presupposes more than one record. So, as a statement
  about the number of records, the input and GM1 are one proposition. The same holds on words, with no target at all
  (§1, W110).
- **So main's wording overstated.** "Follows from a weaker, stated input" (B1677 §2), "the first time a postulate
  … has been replaced by a consequence of a weaker input" (B1677 §2, CHANGELOG S148), the relay of 2026-10-20
  (the common point and the lifted register, §1) and GENESIS v1.49's status for GM1, "DERIVED given one input",
  read the input as weaker. It **characterises** two records. GENESIS's own sentence, "one postulate is exchanged for
  one input", was accurate and stays. GM1's status is regraded in GENESIS v1.50 (P-212), to the status the record's
  own legend gives an assumption: POSTULATED, now in an equivalent form.
- **The equivalence has content; it is not a renaming.**
  - A number is exchanged for an invariance: the records' moves keep something. That is the kind of statement PF1's
    "what remains" could mean, though whether PF1 requires a kept object stays a reading.
  - On words the kept object is the commutator, whose trace is PF1's κ, and at n = 2 the moves are the once-punctured
    torus's mapping classes (GM4). So GM1 is tied to GM4 and PF1. Nothing here derives GM4 or the puncture.
  - The word side needs no target. The rank-two price applies to the character side only (the SM seat's §167).
- **What the form assumes, named.**
  - **"Persistent" means fixed up to the target's conjugation.** Read as a finite orbit, every character with finite
    image persists at every n, since its orbit lies in the finite set Epi(F_n, G), and nothing is selected.
  - **The moves extend beyond two records democratically:** every a_i ↦ a_i a_j. A surface's moves are the other
    natural extension, and on words they keep the boundary word at every genus. Main's check confirms the web seat's
    exploratory genus-2 note: the handle twists keep [a₁, b₁][a₂, b₂] as a word, and all eight transvections between the
    handles move its class. So on words the count of two rests on democracy.
  - On characters in SL(2, ℂ), the web seat's exploratory computation (not banked) finds the surface's moves also give
    one handle, two records. Whether that is the prime's doing is P-211.
- **E82, the web seat's second point, taken.** The criterion is the property sought, not a test borrowed from another
  domain, so B1677 is not an E82 case. But B1679 (i) uses no solvability, and its steps 1 and 4 were in B1677's own
  preregistration (§0b item 4), so B1677's "it could have failed (2I is not solvable)" is weak for the character
  statement. The mathematics is elementary or classical; what is new is the reading.

## 3. P-211, the surface route: an argument, labelled, not banked

The web seat asked whether, under a surface's moves, an odd-p Heisenberg character is fixed at every genus, so that the
prime and not the extension gives two records on that route. Main's argument says yes, and says why p = 2 differs:
- **Odd p.** Send a₁, b₁, …, a_g, b_g to a symplectic basis of the Heisenberg group of (ℤ/p)^{2g} (exponent p,
  commutator pairing ω = the intersection form mod p). A mapping class acts on homology through Sp(2g, ℤ), keeps ω,
  and so induces an automorphism of the image that is trivial on the centre. By Stone–von Neumann the p^g-dimensional
  representation is fixed up to conjugation, at every genus.
- **p = 2.** The images' squares are central and record a quadratic form q with polar form ω, and the character sees
  q: tr ρ(y²) = ±2^g according to q(y). A mapping class keeps the character only if it keeps q. Sp(2g, 𝔽₂) keeps no
  such form once g ≥ 2: it is transitive on the forms of Arf invariant 1, of which there are 2^{g−1}(2^g − 1), one at
  g = 1 (the quaternion point, Q₈) and six at g = 2. So the 2-group character is fixed only at one handle.
- **If it holds,** on the surface route the prime 2 gives two records, while every odd prime is fixed at every genus;
  on the democratic route every target tested gives two records (B1679, B1680). The argument covers the Heisenberg
  family only. A sealed census (H(3) and the extraspecial 2^{1+4} at genus 2, with the genus-2 mapping-class
  generators) or the SM seat's proof would settle it. Queued, not computed.

## 4. What it says

- **On words, as on characters, a non-trivial kept object exists only at two records,** at every n ≥ 3 and every
  length: a count, not a search bound. At two records the kept word is the commutator.
- **GM1 is characterised, not derived from something weaker.** The price's count is unchanged, one input for one
  postulate, and its kind changes: a number for an invariance under a named extension of the moves.
- **Graded on the record's two axes.**
  - *Importance:* moderate. It corrects main's own grade of yesterday, and it ties the count of records to PF1's
    commutator on words. It fixes no number.
  - *Evidence:* a proof by hand, re-derived; two independent censuses that agree; the seat's run reproduced byte for
    byte. 0 of 19.

## 5. Files

- `verification/received/`: W110's proof, checks script, run and output, copied from the SM seat's branch at
  `a1d41bf56`; `SHA256_RECEIVED.txt` holds their hashes.
- `verification/main_check/`: main's own check, its run and its output.
- The lock: `tests/test_b1682_the_word_side_of_the_record_count_verified.py`.
