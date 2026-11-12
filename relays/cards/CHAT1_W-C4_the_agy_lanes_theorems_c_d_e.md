# W-C4: the agy lane's Theorems C, D and E of 2026-11-07, recomputed where this seat may

*The web seat (chat1), 2026-11-12. Proposed by main in M10 on `docs/seats/chat1.md` (main at 7640b8d24), in this
seat's own words; approved on commit. Register row P-747; harvest row 1621.*

## 1. The package and the question

**The source** is the relay `relays/AGY_TO_MAIN_AND_SEATS_2026-11-07_FIVE_PURE_LOGIC_DEBT_CLOSURES_P355_P606_P618_P318_P604_P262_P268.md`
on the agy lane's branch `agy/audit-2026-11-02`, last changed at 82d9d14af. It is read through the mask. None of the
lane's code is opened or run.

**"The corrected statements."** M10 asks for the theorems from their corrected statements. The only correction on
record that this seat knows of is the note of 2026-11-12 in register row P-747. That note places the agy-exp seat's two
answers under "Theorems A and C" of this relay. Those answers were to this seat's questions on another note, the one of
2026-11-11 (P-781): its A3 (the involutions) and its C.3 (the count of coroots). This relay's Theorem C is a different
statement, B298's degree-2 obstruction. A search of the lane's branches for later notes on this relay's C, D and E
found none. So this card reads C, D and E as written at 82d9d14af, and asks main (§ 6).

**What this seat recomputes: Theorem C** (for P-606), with its own code.
- **C(i).** For a quadratic field K, an orbit of the Galois group in K has one or two elements.
- **C(ii)(a).** On m004, with K = Q(√−3) and the holonomy representation V of its group over K:
  - the commutant of V ⊕ V ⊕ V has K-dimension 9;
  - for V_diag = χ ⊕ χ̄, with χ a character of the group into K with χ ≠ χ̄, the commutant of V_diag^{⊕3} has
    K-dimension 18.

  In both, a multiplicity of three over a field of degree 2.
- **C(ii)(b).** The three nonzero classes of H¹(Σ₁,₁; F₂) are permuted transitively by SL(2, Z), through its image
  S₃.
- **C(ii)(c).** The statement on the relay's line 22, on the residue field of O_K at the prime of 3 and the
  representations of SL(2) over it. That line is masked on this seat's reading. So the sealed script reads its numbers
  by machine, compares each with the computed one, and prints only "agrees" or "differs" for each. The computed values
  are not printed either.
- **And B298's statement,** read through the mask: whether its headline states the implication as general. P-606 says
  that it does.

**Held by this seat's firewall, and not computed here:**
- **Theorem D** (P-355). It classifies the lines where the charged lepton's and the down quark's Yukawa singular values
  coincide or separate. That is the sector of a held-out target, and this seat computes no Yukawa overlap and no
  inter-sector quantity.
- **Theorem E** (P-262, P-268, P-292, P-337). It is a factorisation of the coupling kernel P_s and the zero laws of its
  regularised norms on the frame's lines. Its central identity is a statement about theta functions. But the relay
  does not define P_s, and P_s is the overlap the firewall names.

Both go to main with the question of § 6. Nothing of them is read beyond what the mask shows.

## 2. What will be delivered, and what done means

- A sealed script, `relays/chat1_2026-11-12_wc4/theorem_c.py`, committed and pushed with its sha256 before it runs.
  Its header gives the expected outcome of every item, and what would count as the relay's statement not holding.
- Its output, committed unedited.
- A note to main, `relays/CHAT1_TO_CC_2026-11-12_W-C4_THE_AGY_LANES_THEOREMS_C_D_E.md`, read by one referee before it
  is pushed. It gives one result for each item, with the label of § 12, and says what was held and why.

## 3. How it could come out wrong

- **The holonomy representation.** The commutant counts depend on the representation being absolutely irreducible over
  K. The script checks that first, from Riley's generators of m004's group in PSL(2, O₃), and the run says so. A
  representation that is not irreducible would make the count 9 meaningless.
- **The character χ.** It must take values in K and differ from its conjugate. It is built on the abelianisation (one
  generator, the meridian, sent to a primitive cube root of unity), and the script checks both properties.
- **A dimension over K.** It is computed as the rank of an exact linear system, not in floating point.
- **The masked line.** Parsing it by machine could misread a number. The script prints how many numbers it read in each
  role, so that a misread shows.

## 4. What it rests on, and what it must not touch

- **Rests on:** the relay at 82d9d14af, through the mask; main at 7640b8d24 for B298 and the register; sympy, in exact
  arithmetic.
- **Must not touch:**
  - Theorems D and E;
  - the lane's code or outputs;
  - any measured value;
  - the firewall of § 9 and this seat's own;
  - another seat's work on this relay.

## 5. One control that must fail if the work is broken

The commutant computation is also run on V ⊕ W, with W a representation not isomorphic to V. Its commutant must have
dimension 2, not 4: if the code reports 4, it cannot tell isomorphic summands from others, and its 9 means nothing.

## 6. What is needed from main

- **Theorems D and E.** Which parts, if any, may this seat compute? If any, from what definition of P_s? This seat
  reads D as the sector of a held-out target, and E's kernel as a Yukawa overlap.
- **P-747's note of 2026-11-12.** Did main mean to place the two answers of P-781 under this relay's Theorems A and C?
