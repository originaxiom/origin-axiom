# W27 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. Values already seen are listed.
Nothing here is a result.

## Why this route

- **The owner's choice** (2026-10-08, after W26): "State the link, write it up".
- **The task.**
  - Write the derivation of three generations with the one input W25 and W26 show the weave cannot supply, stated as
    an input.
  - Test what the link implies under a sealed rule.
  - Label the result honestly: derived given one stated link.

## The link, stated (Λ: the weave's form of GENESIS FK11)

> **Λ.** One generation of matter is a field on spacetime × the shared fibre, in F-MC's 27 of E₆. It carries the
> parity-twisted spin bundle 𝕎. Each parity sector is one generation, kept apart from the others at the puncture. Its
> left-handed states are the fibre's holomorphic zero modes; this hand is the records' orientation.

- **What Λ adds.** It names which field carries 𝕎, and the half that is left-handed: W24's Lagrangian half and W25's
  choice. It is one identification, the dictionary.
- **What Λ does not add.**
  - The count: the parities, W1.
  - The alikeness: Theorem G.
  - The forced end condition: W22, with W24's D0.
  - The flavor triplet: W21.
  - The gauge algebra, global form and hypercharge: F-MC, with its typed inputs (THE_CLAIM §1).

## The chain the write-up states (each link with its status)

1. **The principle to the grammar.** PF1–PF3 give the two records and the moves L, R (GENESIS, DERIVED / POSTULATED as
   GENESIS marks them).
2. **Three.** The three non-zero parities, the only three the moves leave undistinguished (W1, PROVED).
3. **Alike.** Whatever one parity carries, all three carry (Theorem G, PROVED).
4. **The common point and the bundle 𝕎** (W2, PROVED; W24 D1: 𝕎 ≅ ρ_Q ⊗ ℂ³).
5. **Chiral, odd, three.**
   - The end condition at the puncture is fixed by the moves up to the hand.
   - The index is odd, never 0.
   - It is ±3 when the parity sectors are kept apart (W22 with W24 D0, COMPUTED and PROVED). Λ keeps them apart.
6. **The flavor triplet.** The holomorphic zero modes are T = μ ⊗ 3′, which is the tangent space of the character
   variety at the common point (W21, W24 A3, PROVED and COMPUTED).
7. **The gauge structure.** F-MC: [SU(3) × SU(2) × U(1)]/ℤ₆, the hypercharge direction, and E₆'s 27 (THE_CLAIM §1,
   main's, with its five typed inputs, the chirality bit among them).
8. **Λ,** the one link (stated; W25 and W26: not derivable from the weave's local systems, the threads' geometry or
   F-MC's arithmetic).
9. **Conclusion (conditional on 1–8).** Exactly three chiral 27s of E₆, alike, forming the weave's flavor triplet,
   each containing one Standard Model generation with F-MC's hypercharge.

## The sealed tests (the script `the_link_tested.py`, exact rational arithmetic)

- **T1, anomalies.** The linked 4d spectrum, three 27s decomposed under SU(3) × SU(2) × U(1)_Y with F-MC's (the
  standard) hypercharge, cancels:
  - SU(3)³, SU(3)²Y, SU(2)²Y, Y³ and grav²Y;
  - the SU(2) global anomaly (an even number of doublets).
  - Per 27, and for three.
  - The control: one Standard Model generation alone (with ν^c) cancels too, and the 27's extra states (D, D^c, H_u,
    H_d, S) form an anomaly-free remainder.
  - **Prior 99%.**
- **T2, the count under Λ.**
  - With the parity sectors kept apart, the move-invariant end conditions give index −3 or +3 only (W24 D0's grading
    commutant 1).
  - Without the grading, ±1 is also possible.
  - So Λ's "each parity sector is one generation" is what makes the count three.
  - A recap of computed facts. **Prior 99%.**
- **T3, the six-dimensional reading** (Dobrescu–Poppitz, hep-ph/0102010: in six dimensions the SU(2) global anomaly,
  π₆(SU(2)) = ℤ₁₂, requires N(2₊) − N(2₋) ≡ 0 mod 6).
  - Read in six dimensions with one 6d chirality for the left-handed fields (Λ's single hand), each parity sector is
    a rank-2 bundle, so it carries 2 × 4 = 8 doublets of one 6d chirality (Q's three colours and L).
  - For k sectors, 8k ≡ 0 (mod 6) holds exactly when k ≡ 0 (mod 3). The weave's k = 3 passes; k = 1 and k = 2 fail.
  - Also stated, not a pass: with every field of one 6d chirality, the local 6d anomalies (gravitational: 16 per
    generation, unbalanced) do not cancel. The six-dimensional reading needs a completion that Λ does not supply. The
    four-dimensional reading (T1) is the one Λ asserts.
  - **Prior 95%** for the mod-3 statement.
- **T4, what Λ with F-MC implies beyond the three** (structural; no data contact).
  - Three right-handed neutrinos, ν^c in each 27.
  - Three vector-like pairs D + D^c, three Higgs-like pairs H_u + H_d, and three singlets S. They must be heavy, through
    F-MC's rank-closing VEV directions (THE_CLAIM §1).
  - In the exact flavor triplet, the three are degenerate (Schur). Masses need the triplet broken (BLIND).
  - Read off the 27's decomposition. **Prior 99%.**
- **Fenced: the mixing comparison.** The record fences any comparison of mixing angles with data (THREE_GENERATIONS
  §3). The covenant is spent (B1066), and reopening needs the owner, L91's functor and the full checklist. The
  group-theory reading stands (TM1 with the swap, TM2 with the sign; `the_mixing.py`). No comparison is made here.

## What each outcome means

- **All pass.** The derivation is written as: three chiral generations with Standard Model gauge content follow from
  the principle, F-MC's typed inputs and the one link Λ, and they are anomaly-free. Λ is the one input that W25 and
  W26 show the weave cannot supply. The label is "derived given one stated link", never "derived from the principle"
  alone.
- **T1 fails.** The hypercharge bookkeeping is wrong. Find the error.
- **T3's mod-3 statement fails.** The doublet count per sector is wrong. Re-derive it before writing anything.

## Seen before this was written

- **By hand:** the 27's anomalies vanish (E₆ has no cubic Casimir, and the Y³ sum was checked by hand); 8k ≡ 0 (mod 6)
  ⟺ k ≡ 0 (mod 3).
- **Dobrescu–Poppitz's condition,** as recalled.
- **THE_CLAIM §1,** and THREE_GENERATIONS §3's fences.
