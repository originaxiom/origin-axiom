# W42 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **Main's two asks** (relay THE_BREAKING_THE_WEAVE_ALLOWS, §3):
  1. "Verify B1620's three-tensor counts with your normal form (the cube's rotation group twisted by c): 57 / 24 / 16
     viable subgroups, and no residual of order 3 under Sym² T."
  2. "In the zero modes' language, is there a coupling that reads the word and not only τ?"
- **B1620 is load-bearing.** Main's write-up for outside review counts all 19 numbers as free on its strength.
- **Part A is a VERIFICATION, not blind.** Read before this rule:
  - B1620's FINDINGS (§0 to §5) and its relay;
  - the docstring and the `viable` function of B1620's `post_seal_tensors.py`, for the definition of a viable sector.

  B1620's code is not run here, and its group is not used. The group comes from this seat's construction.
- **Part B answers ask 2 with a census.** Main's B1621 (the clock and the tick) was read first.

## Weave or thread?

- **Part A** takes every subgroup of the weave's group as a possible residual, none chosen. Its quantity, viability
  under each tensor, is defined on the group of the joint action. Its claim is about all subgroups at once: weave-type.
  A residual, once chosen, is a vacuum's choice.
- **Part B** takes every thread up to a stated length, none chosen, and states one claim about all of them at once:
  weave-type as a census. Each row is one thread's mapping torus, a thread object, and is labelled so.

## The objects

- **The group.** G on the matter triplet T, from W21's construction (`the_couplings_verified.the_group`, W38), in W38's
  normal form (`the_couplings_exact.normal_form`). Every element is c(g) S(g), with S(g) a signed permutation of
  determinant one. It is encoded exactly as (k mod 24, S), with c = e^{2πik/24}.
- **The second route for the group, by hand.** G′ = {z S : S one of the cube's 24 rotations, z⁸ = 1, z⁴ = sgn(S)}.
  - sgn(S) is the sign of S's permutation of the three axes, which is S₄'s sign through S₄ → S₃.
  - Reason: c is a character with c(L) = e^{−iπ/4}, c(R) = e^{iπ/4} and c(RL) = 1, so c(G) = μ₈. The kernel of
    g ↦ S(g) is the scalars μ₄. L, a quarter-turn, has c⁴ = −1.
- **The tensors** (CONVENTIONS.md §6):
  - T̄ ⊗ T: M ↦ g M g† = S M Sᵀ (c cancels);
  - T ⊗ T: M ↦ g M gᵀ = c² S M Sᵀ;
  - Sym² T: the same, on symmetric M.

  B1620 writes the dual convention, h† M h = M and hᵀ M h = M. Its invariants are the complex conjugates of these, with
  the same singular values, so viability is the same.
- **Viable (B1620's definition).** The singular values of a generic invariant M are three, distinct and non-zero.
- **K** comes from W40's construction: the inner automorphisms (conjugation by a and by b), lifted through
  `the_common_point.extend` and restricted to T.

## Part A: the cells (predictions and priors)

Every number here was derived by hand from G′: the abelian subgroups over each abelian subgroup of S₄, and the
non-abelian ones by the sign constraint z⁴ = sgn(S).

| | prediction | prior |
|---|---|---|
| **A0** | The 96 elements of G are exactly G′. Every k is a multiple of 3: c is an eighth root of unity. | 95% |
| **A1** | **68 subgroups in 26 conjugacy classes.** 57 are abelian, in 20 classes; 11 are not, in 6 classes. The abelian orders are 1, 2, 3, 4, 6, 8, 12 and 16, with 1, 7, 4, 11, 4, 19, 4 and 7 subgroups. The non-abelian ones are μ × A₄ for μ = 1, μ₂, μ₄ (orders 12, 24, 48); four of order 24 over the S₃'s; three of order 32 over the D₄'s; and G. | 95% |
| **A2** | **Viable under T̄ ⊗ T:** exactly the abelian subgroups, 57. **Under T ⊗ T:** exactly the abelian subgroups on which T's character is real, 24, of orders 1, 2, 3, 4, 6 and 8. **Under Sym² T:** exactly the subgroups of E = {±1} × V₄, the set of elements of order at most 2, so 16, of orders 1, 2, 4 and 8. | 90% |
| **A3** | No subgroup of order divisible by 3 is viable under Sym² T. Along each of the 8 elements of order 3 (the 3-cycles, all with c = 1), the Sym² T fixed space is {diag(a) ⊕ [[0, b], [b, 0]]} in the 3-cycle's eigenbasis, with spectrum (\|a\|, \|b\|, \|b\|). | 97% |
| **A4** | The inner automorphisms act on T as the parity signs. Their lifts with c = 1 generate K = V₄ = {1, diag(1, −1, −1), diag(−1, 1, −1), diag(−1, −1, 1)}, of order 4; all four lifts generate E, of order 8. **10 subgroups contain K**, of orders 4, 8, 12, 16, 24, 32 (three), 48 and 96, since G/K ≅ ℤ₃ ⋊ ℤ₈. Viable among them: orders 4, 8 and 16 under T̄ ⊗ T; 4 and 8 under T ⊗ T and Sym² T. Every invariant matrix of every viable one is diagonal in the parity basis. So every mixing pattern between two of them is a permutation. | 95% |

**How A2 is decided, two routes, subgroup by subgroup.**
- **Exact.** Each tensor acts monomially on the matrix units. The fixed space has one vector per orbit whose stabiliser
  acts with phase 1. Take a generic member, M = Σ t_O v_O, at random Gaussian-integer points with coordinates up to
  10⁶. Compute X = M M† in ℤ[ζ₈], exactly. A sector is viable at a point when det X ≠ 0 and the discriminant of X's
  characteristic polynomial is non-zero.
  - One such point proves the sector viable.
  - Three points where it fails prove it non-viable, up to a stated bound. Δ · det X is a polynomial of degree at most
    18 in the real coordinates, so by Schwartz–Zippel a non-zero one vanishes at three independent points with
    probability below 10⁻¹⁵.
- **The criterion, by hand.**
  - A non-abelian H has a 2- or 3-dimensional irreducible piece on T. Its invariant matrices are scalars there, so it
    has a degenerate pair.
  - For an abelian H with characters χ₁, χ₂, χ₃, the entry M_ij survives when χ_i χ_j = 1 (or χ_i = χ_j for T̄ ⊗ T).
  - Under T ⊗ T, M is non-singular exactly when the characters close under inversion, which happens when T's
    character is real. The blocks are then free, so the masses are distinct.
  - Under Sym² T, a pair χ ≠ χ̄ gives a symmetric block [[0, b], [b, 0]], which is degenerate. So every χ_i must be
    real, and every element squares to 1.

## Part B: the threads' own zero modes (main's ask 2)

- **The rule.** Every thread is one Lyndon word in L and R, of length 2 to 12. That is every primitive necklace, each
  thread once and no covers: 745 threads. Every such word contains both letters.
  - Its monodromy on T is g_w, the product of the record's lifts of its letters (`lift_choices()[0]`), read as in
    `the_mixing_patterns_verified.word` (CONVENTIONS.md §2).
  - The set of necklaces is closed under reversal, so the census as a whole does not depend on that convention.
- **The reading being tested.** A thread is the mapping torus of its word, with 𝕎 extended over the circle by the
  thread's lift. The record's extension uses one lift g on every parity summand; there are two, ε g_w with ε = ±1.
  - H⁰(F; 𝕎) = 0, so the Wang sequence gives H¹(mapping torus; 𝕎) = V^{ε g_w}, the monodromy's fixed space.
  - Its T part is the census's object: the thread's own zero modes on the matter, a coupling-free reading of the word.
  - The T̄ part is its conjugate whenever c(w) is real.

| | prediction | prior |
|---|---|---|
| **B1** | c(w) = e^{iπ(r − ℓ)/4} for every thread with r R's and ℓ L's. The exact product of L's and R's normal forms matches the float route on every thread. | 97% |
| **B2** | A thread has zero modes on T, for one of its two extensions, exactly when r ≡ ℓ (mod 4). Then S(w) is even. The extension with ε c = 1 gives the axis of S(w): a parity line if S is a face half-turn, a body diagonal if S is a 3-cycle, all of T if S = 1. The other extension gives the plane of two parity lines if S is a face half-turn, and nothing otherwise. | 90% |
| **B3** | **The census claim, about all 745 threads at once.** Every zero-mode space on T, for either extension, is either spanned by parity lines or is a body diagonal (±1, ±1, ±1)/√3, whose projector has every entry of modulus ⅓. The type is the same for every rotation of the word. So the only way a thread's own zero modes break the parity grading is democratically. | 85% |
| **B4** | **Under a general extension**, with independent phases on the three parity summands along the circle, a zero-mode line has equal moduli on one cycle of S's axis permutation and zero elsewhere. That gives parity lines, bimaximal lines (moduli² ½, ½, 0, for S of transposition type) and trimaximal lines (moduli² ⅓ each, for 3-cycles). Checked on all 24 rotations and every cycle. | 90% |
| **B5** | **Main's B1621 tick, in this language.** For the thread RL (c = 1, a 3-cycle), the Cesàro mean of g's powers, (1 + g + g²)/3, equals the projector onto the thread's zero modes. Every entry has modulus ⅓. That is B1621's T2 matrix: the tick's operator mean is the zero-mode projector of the tick's mapping torus. | 97% |

**The reading, written before the run.**
- If B1 to B5 hold, the zero modes' language has a coupling that reads the word: a thread's own H¹, the fixed space of
  its monodromy.
- Under the record's extension it breaks the parity grading only along a body diagonal, B1621's democratic line, and only
  for threads with r ≡ ℓ (mod 4) whose rotation is a 3-cycle.
- Which thread a sector reads is a choice: a thread result, never the weave's. The weave, read jointly, is invariant
  under the whole group, and so reads τ and the grading only (B1620's K cell).

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
