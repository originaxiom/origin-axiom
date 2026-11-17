# W-A3: the figure-eight's dihedral cover supplies the Heisenberg module and the parity with no flux, but not the act's Weil action. The frame's lines carry no Weil class: their trace signature is that of End(W), the same in both classes. The class belongs to the shift group's quadratic form; the knot's is x²/5, so B1951's 2x²/5 is a convention, off by a factor of 2. The up coupling wedged to the top degree is invariant in both classes and closes at level 5. Frame C's up phases are of order 25 only because frame C puts the charge into the characteristic, and nothing computed in the object is of level 25

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:`, data-free. It closes card W-A3
(`relays/cards/CHAT1_W-A3_the_cover_the_class_and_the_up_sector.md`, d1e36f8f4), the author's card relaying main's M39.
Read: M39. Main will recompute.

**How it was checked.**
- Computed once; expectations and failure criteria committed first (the card).
- **The sealed run** (`wa3_checks.py`, 4ccff2979; output 110ce3a9c) stopped at its own sanity assertion. Its word for the
  act, S T⁻¹ S⁻¹ T, multiplies to L·R = [[1, 1], [1, 2]], not the record's R·L = [[2, 1], [1, 1]].
- **Post hoc 1** (`wa3_posthoc_word.py`) reruns the sealed script with only that word replaced, by T S T⁻¹ S⁻¹. It was
  sealed before its run, and its output was committed before it was read (ae58fade1). Every result in A–F comes from it.
- **Post hoc 2** (`wa3_posthoc_wedge.py`) was written after reading M39. It was sealed before its run, and its output was
  committed before it was read (1c4645be3).
  - M39 shows that the card's three-body coupling is "wedged to the top degree", so its degrees are exterior degrees in
    Λ*(W). The text as relayed to this seat lacked that phrase. The card's expectations E-E and F7 read the degrees as
    the cover's cusp degrees.
  - Post hoc 2 answers the question as M39 states it, and adds a test of whether the frame's lines carry a class at all.
- Tested against planted errors (1): a monodromy inducing [[3, 1], [2, 1]] moves the dihedral prime from 5 to 3.
- The harness also recovers H₁(m004) = Z and H₁(M₂) = Z ⊕ Z/5.

## 1. Results

| part | result |
|---|---|
| A | π₁(m004) = ⟨a, b, t \| t a t⁻¹ = aba, t b t⁻¹ = ab⟩, monodromy LR on H₁ of the fibre. Among primes 3–31, **only p = 5 has a dihedral representation** (t to a reflection). The plant gives only 3 |
| B, the fibre | the fibre's character u = (1, 2) is **2·ω(v, ·)**, with v = (1, 2) the act's fixed line (LR v = −v mod 5, B1943); u∘LR = −u |
| B, the cusp | φ([a, b]) = (aba)[a, b](aba)⁻¹. The meridian (aba)⁻¹t is **a reflection fixing one sheet**; the longitude acts trivially. **The cusp degrees are (1, 2, 2)**, as main found |
| B, the deck groups | **none** for the 5-sheeted cover of m004 (centraliser of order 1). Over the double cover M₂ (the kernel of t ↦ −1), **C₅, the shifts** |
| B, the clocks | the deck group's characters pull back to ζ^(b·u) on the fibre: **twists by the act's fixed line**. Z = diag(ζ^x) intertwines the sheets' representation with its twist on M₂ (2 × 10⁻¹⁶), but not on m004 (best scalar off by 1.9; t inverts the twist) |
| B, the module | ⟨X, Z⟩ has a commutant of dimension 1 (irreducible), and XZX⁻¹Z⁻¹ = ζ·I. **t acts on the (shift, clock) plane as −I** |
| B, the act | in both classes c = 1, 2: ρ_c(−I) = P (to 3 × 10⁻¹⁵ and 6 × 10⁻¹⁵), but **ρ_c(LR) is not a scalar times P** (least distance 0.553) |
| C | H₁: m004, Z; M₂, Z ⊕ Z/5; **the 5-sheeted cover, Z³ with no torsion**; the 10-sheeted regular cover, Z⁵ with no torsion |
| D, quadratic forms (T's coefficient c in e(cx²/5)) | **the knot's discriminant form q = xᵀA⁻¹x/2** (A = V + Vᵀ, V the Seifert matrix; Alexander −t² + 3t − 1): **c ∈ {1, 4}, residue**. Its bilinear form b(x, x) = xᵀA⁻¹x: {2, 3}, non-residue. **B1951's ρ(T): 2, non-residue.** **The flux-5 modes:** T² gives j²/5, so T's coefficient is 1/2 = 3, non-residue |
| D, frame C's T-phases on lines | at the same point w (the record's transport), the two theta numerators give down e(−k²/5), lepton e(k²/5), up e(−17k²/25), for k = 1–4. These agree with B1953's φ = ζ^(−a²) for down |
| D, the act's shear | LR ≡ −U mod 5. In the symplectic basis v = (1, 2), w = (0, 1), U w = w + 4v (residue); U² has shear 3 (non-residue) |
| post hoc 2, W2: does a class show in the frame? | the trace signature r = tr R(T²)/tr R(T)², which no overall scalar changes, is **+1/5 for ρ_c ⊗ ρ̄_c (same class) and −1/5 for ρ_1 ⊗ ρ̄_2 (mixed)**. On the frame's 25 lines it is **+1/5 for down and for lepton**, with tr R(T) = 5 |
| post hoc 2, W1: the top wedge | in both classes, **det ρ_c(g) = 1 on all 120 elements** (to 6 × 10⁻¹⁴). α ∧ β ∧ γ (α, β ∈ Λ², γ ∈ Λ¹) picks up det ρ(g) (to 9 × 10⁻¹⁶). **The T-spectrum of every Λ^k(W) is in 5th roots** |
| post hoc 2, W3 | the Weil 3's T-phases: class 1, {0, 1/5, 4/5}; class 2, {0, 2/5, 3/5} (W-A2's) |
| E, the up pair | frame C's up T-phases ×25 = 8, 7, 22, 3: **every one of order 25** |
| F, level 25 | x² − 3x + 1 has one root mod 5 and **none mod 25**. LR keeps **no cyclic subgroup of order 25**. **No D₂₅** (the solutions mod 25 have order 5). No cover in C has Z/25, or 5-rank 2, in H₁ |
| failure criteria | F1–F5 and F8: none holds. F6 and F7 were framed on a misreading (see Part 1.2 and Part 2): F6 tested a reading that is not a class invariant, and F7 tested cusp degrees |

## 2. The answers

### Part 1.1: does the cover supply the whole module, with no flux?

**[E] It supplies the Heisenberg module and the parity, with no flux.** Three qualifications.
- **The shifts are deck transformations over the double cover M₂, not over m004.** The 5-sheeted cover of m004 has
  none: the meridian's reflection does not commute with the shifts. Over M₂ the cover is cyclic, with deck group C₅.
- **The clocks are the deck group's characters, ζ^(b·u) on the fibre with u = 2·ω(v, ·): twists by the act's fixed
  line.** They are twists on M₂ only. The act inverts u, and H₁(m004) = Z has no 5-torsion.
  - [J] XZ = ζ ZX is the pairing between a deck group and its characters, not a magnetic commutator. So no flux is
    needed for it. W-A2's flux bit is replaced by the cover, which the knot has only at p = 5.
- **The cover's t is the parity, not ρ(LR).** t induces −I on the (shift, clock) plane, so it is ρ(−I) = P in either
  class, and that is all B1951's gauge group uses.
  - LR itself is not supplied. Mod 5, LR = −U with U a nontrivial unipotent, and in either class ρ_c(LR) induces −U, not
    −I. That holds in every basis, since −I is central.
  - The cover sees the act's semisimple part, not its unipotent part (the chirp).

**[J] So main's hypothesis holds for the module and the gauge group: the cover replaces the flux.**

### Part 1.2: which Weil class does the frame carry, wherever the class shows?

**[E] None. The frame's lines do not see the class.**
- **The test.** The four candidates ρ_c ⊗ ρ̄_c′ split by a trace signature that no overall scalar can change:
  - r = +1/5 when the two factors are of the same class: ρ_c ⊗ ρ̄_c = End(W), the same for c = 1 and c = 2;
  - r = −1/5 when they are mixed.
- **The frame's down and lepton line representations have r = +1/5.** T moves (a, b) to (a, b − a), with B1953's phase
  ζ^(−a²) for down and ζ^(a²) for lepton.
  - So the frame's level-5 couplings live where End(W) does, and End(W) is the same in both classes.
  - This agrees with W-A2's referee: the record's lines match the Weyl operators for every Weil representation, up to an
    identification of 𝔽₅².
- **[J] So B1953's statement fixes an identification, not a class.** B1953 says O = Σ ζ^(−ab) Y ⊗ D(w) transforms by
  B1951's ρ. The same O, with the other identification of 𝔽₅² (diag(1, 2), per W-A2's referee), transforms by the other
  class.
- **A correction to this seat's own expectation (E-D).** The card read the class from the coefficient of the frame's
  T-phase: down 4 and lepton 1, both residues. That reading is not a class invariant. On the lines, a phase depending only
  on a is a coboundary: a relabelling by ζ^(m·ab) removes it from T (m = 1 for down, −1 for lepton). W2 shows the class does not show there.

### Part 1.3: then what decides the class?

**[E] The class is a property of the quadratic form carried by the shift group.**
- The Weil representation of a finite quadratic module (A, q) has ρ(T) = e(q(x)), and its Fourier kernel is the
  bilinear form B(x, y) = q(x + y) − q(x) − q(y).
- The cover's shift group is C₅. It is the image of H₁ of the double branched cover, Z/5, under the dihedral
  representation (standard: a knot's dihedral representations factor through that group).
- That group carries the knot's linking form b and its refinement q:
  - **q = x²/5** (residue), as main says;
  - b(x, x) = 2x²/5.
- B1951's ρ is the Weil representation of (Z/5, 2x²/5), whose bilinear form is −xy/5.

**[J] So, within the object, the knot fixes the class at x²/5.**
- B1951's 2x²/5 is one of the factor-of-2 shifts computed in D:
  - b against q;
  - U² against U, for the double cover's monodromy;
  - T² against T, for the odd-flux modes.
- Since the frame does not see the class, choosing x²/5 conflicts with nothing in the frame.
- **Re-basing B1951 on x²/5:**
  - leaves its split, commutant and hypercharges unchanged, since ρ_c(−I) = P in both classes;
  - changes the Weil 3's T-phases from {0, 2/5, 3/5} to {0, 1/5, 4/5} (W3);
  - needs the record's lines to be identified with the Weyl operators by diag(1, 2), not the identity.
- The flux-5 modes would bring the other class. With the cover in place of the flux, that question does not arise.

### Part 2: does the up coupling wedged to the top degree close at level 5?

**[E] Yes, in both classes.**
- The coupling is Λ²(W) ∧ Λ²(W) ∧ Λ¹(W) → Λ⁵(W): two fields in Λ² and the Higgs in Λ¹.
- Λ⁵ transforms by det ρ_c, and det ρ_c(g) = 1 on all 120 elements of SL(2, 𝔽₅). (SL(2, 𝔽₅) is perfect, so it has no
  other one-dimensional character.)
- So the top wedge is an invariant tensor, with phase 1: it closes at level 5 for either class. W1 checks the
  covariance directly.
- The T-spectrum of every Λ^k(W) is in 5th roots. So nothing built from W carries a 25th root.

**[E] Why frame C's up sector has 25th roots.**
- Frame C puts each field's charge into its theta characteristic, q·a with a = k/5. The pair's phase is then
  e(−k²(q₁² + q₂²)/25).
- q₁² + q₂² is 5 for down and 45 for lepton, but 17 for up: 6Y_u = −4 ≡ 6Y_Q mod 5.
- Level 5 needs q₂ ≡ ±2q₁ mod 5. This agrees with B1953's condition, as relayed.
- In Λ*(W) the charge is not a multiplier on the level-5 index. It is the centre's eigenvalue, 6Y = (I − 5P)/2 on
  Λ¹ (B1951). So the top-wedge coupling has no such obstruction.

**[J] So the up sector needs no structure of level 25 if its coupling is the top wedge of the Fock-space reading.**
- It needs level 25 only inside frame C's construction. There the requirement is the quadratic module
  (ℤ/25, −17x²/25): lines read mod 25, at points of order 25.
- **The object supplies nothing of level 25 that was computed:**
  - the act has no eigenline mod 25 and keeps no cyclic subgroup of order 25;
  - there is no D₂₅;
  - no cover's homology has Z/25.

**By-product, from the card's original reading, kept for the record.** Taking the degrees as the cover's cusp degrees,
under the two models of the sealed script:
- the assignment (Q: 2, u: 2, H: 1) closes for up in neither model;
- the up assignments that do close are, in M1, (Q: 1, u: 1, H: 2) with a twisted Higgs; and in M2, Q and u on cusps of
  different degree with an untwisted Higgs.

The card's expectation that none closes in M2 was wrong. None of this bears on M39's question.

## 3. Typed

| statement | how checked |
|---|---|
| dihedral representations only at p = 5; the cover's sheets, meridian, cusp degrees (1, 2, 2), deck groups and clock twists | computed once (post hoc 1 of a sealed script whose run stopped at a sanity assertion); expectations committed first; tested against planted errors (1) |
| the cover's t is P, not ρ_c(LR), in either class | computed once; the basis-free reason is elementary (−U ≠ −I) |
| H₁ of m004, M₂ and the 5- and 10-sheeted covers | computed once; the first two are the harness's known values |
| the knot's q is a residue, b a non-residue; B1951 and the flux-5 modes are non-residues | computed once; expectations committed first |
| the frame's lines have the same-class trace signature, +1/5 | computed once (post hoc 2, written after M39; sealed before its run) |
| the top wedge is invariant in both classes (det ρ_c = 1); every Λ^k has a 5th-root spectrum | computed once (post hoc 2) |
| frame C's up phases are of order 25; q₁² + q₂² ≡ 2 mod 5 for up | computed once; the analytic and numerical values agree |
| nothing of level 25 in the act, in D₂₅, or in the covers' H₁ | computed once |
| the cover replaces the flux; the class is the knot's, and the frame does not see it; B1951 can be re-based on x²/5; the up sector needs level 25 only in frame C's construction | a reading |

## 4. Files

`relays/chat1_2026-11-17_wa3/`:
- the sealed run: `wa3_checks.py`, `SCRIPT_SHA256.txt`, `wa3_checks_out.txt` and `wa3_checks_err.txt` (the stopped run);
- post hoc 1: `wa3_posthoc_word.py`, `wa3_posthoc_word_out.txt`, `wa3_posthoc_word_err.txt` (empty) and
  `wa3_posthoc_word_output.json`;
- post hoc 2: `wa3_posthoc_wedge.py`, `wa3_posthoc_wedge_out.txt`, `wa3_posthoc_wedge_err.txt` (empty) and
  `wa3_posthoc_wedge_output.json`;
- `SCRIPT_SHA256_POSTHOC.txt` and `wa3_exit.txt`.

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes.
The read's corrections follow in a later commit.

0 of 19.
