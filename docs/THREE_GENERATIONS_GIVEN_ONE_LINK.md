# Three generations, derived given one stated link

The SM-derivation seat, 2026-10-08 (the weave dossier's W27; the rule committed first, 6da777ea). Written at the
owner's direction after W25 and W26 showed that one link cannot come from the weave.

**State, 2026-10-08.** The weave's arc is closed at W29. Its state, with main's grade (the flavour three is derived; the gauge three is a selection, GENESIS v1.28), is `docs/THE_THREE_GENERATIONS_STATE_2026-10-08.md`.

**The label, first.** This is a derivation **given one stated link**. It is not a derivation from the principle
alone. The link is named below, and W25 and W26 show why the weave cannot supply it.

## The statement

> From the Origin Axiom principle (GENESIS PF1–PF3), the McKay-cascade frame F-MC with its five typed inputs
> (THE_CLAIM §1), and one link Λ, the matter of the world consists of **exactly three chiral generations**. Each is a
> 27 of E₆ containing one Standard Model generation with F-MC's hypercharge. The three are alike, carry one common
> hand, form an irreducible complex flavor triplet of the cube's rotation group S₄, and the spectrum is free of gauge
> and gravitational anomalies.

## The one link

> **Λ (the weave's form of GENESIS FK11).** One generation of matter is a field on spacetime × the shared fibre, in
> F-MC's 27 of E₆. It carries the parity-twisted spin bundle 𝕎. Each parity sector is one generation, kept apart from
> the others at the puncture. Its left-handed states are the fibre's holomorphic zero modes; this hand is the records'
> orientation.

**Why it is an input, and cannot be derived from the weave.**
- **W25 (a theorem).** The weave's bundles have holonomy Q₈, whose irreducibles are real or quaternionic. So every
  gauge reading of them is self-conjugate, and a chiral one needs a choice of half. Λ is that choice.
- **W26.** The weave is mirror-symmetric: every thread's mirror is a thread, with opposite Chern–Simons. F-MC's
  order-3 orientation flips at every tick, and F-MC counts chirality as an input. So neither the threads' geometry nor
  F-MC's arithmetic supplies the choice.
- **W24.** No six-dimensional object the weave forces supplies it either.

## The chain

| step | what | status | where |
|---|---|---|---|
| 1 | the principle gives the grammar: two records, the moves L and R | as GENESIS grades it (PF1–PF3 POSTULATED; the grammar DERIVED from them) | GENESIS §1–§2 |
| 2 | **three**: the three non-zero parities of the records, the only three the moves leave undistinguished | PROVED | W1 |
| 3 | **alike**: whatever one parity carries, all three carry | PROVED | Theorem G (W6) |
| 4 | the common point ρ_Q (a ↦ i, b ↦ j), the one point every move fixes with the puncture parabolic; the bundle 𝕎 = ⊕_p χ_p ⊗ ρ_Q ≅ ρ_Q ⊗ ℂ³ | PROVED | W2; W24 D1 |
| 5 | **chiral**: at the puncture the moves fix the end condition up to the hand; the index is odd, never 0, and **exactly ±3 when the parity sectors are kept apart**, which follows from the end condition breaking no symmetry of the bulk problem (W28: the flavor group, or locality) | COMPUTED and PROVED | W22 with W24's D0; W28 |
| 6 | **the flavor triplet**: the holomorphic zero modes span T = μ ⊗ 3′, irreducible, not equivalent to its conjugate; T is the tangent space of the fibre's character variety at the common point | PROVED and COMPUTED (two routes) | W21; W24 A3 |
| 7 | **the gauge structure**: [SU(3) × SU(2) × U(1)]/ℤ₆, the hypercharge direction, E₆'s 27 | F-MC: a closed theorem with five typed inputs, one of them the chirality bit | THE_CLAIM §1 (main) |
| 8 | **Λ**, the one link | STATED (an input; shown not derivable from the weave) | this page; W25, W26 |
| 9 | **exactly three chiral 27s**, alike, in the flavor triplet, each with one Standard Model generation | follows from 1–8 | below |

## What the link implies, tested (W27; the rule committed first; exact)

- **Anomalies (T1, passed).**
  - One 27 under SU(3) × SU(2) × U(1)_Y with the standard hypercharge cancels SU(3)³, SU(3)²Y, SU(2)²Y, Y³ and
    grav²Y, and it has an even number of SU(2) doublets (6).
  - So do three 27s (18 doublets).
  - The controls hold: one Standard Model generation with ν^c, and the 27's remainder, are each anomaly-free.
- **The count (T2, passed).**
  - Without the parity grading, the moves alone also allow index ±1 (W24 D0, commutant 2).
  - With the grading Λ asserts, the commutant is 1, so the index is ±3 only.
  - This is the one place where Λ's "each parity sector is one generation" does work, and it makes the count three.
  - **W28 (after W27).** The grading is not needed as a separate postulate. The two ±1 conditions are the
    vector-spinor's spin-½ and spin-3/2 parts, and they break 𝕎's flavor group U(3) to a phase. So every end condition
    that breaks no symmetry of the bulk problem (the moves and the flavor group), or that is local (the puncture's
    holonomy is −1), has index ±3. That requirement is a naturality condition, stated, not derived.
- **The six-dimensional reading (T3, passed, with a stated limit).**
  - Read in six dimensions, each parity sector is a rank-2 bundle carrying 8 SU(2) doublets of one 6d chirality.
  - Dobrescu–Poppitz's global condition (hep-ph/0102010: N(2₊) − N(2₋) ≡ 0 mod 6, from π₆(SU(2)) = ℤ₁₂) then holds
    exactly when the number of sectors is a multiple of three. The principle's three passes; one or two sectors would
    fail.
  - The limit: with every field of one 6d chirality, the local gravitational count is unbalanced (32 Weyl fermions per
    sector). So a six-dimensional reading needs a completion that Λ does not supply. The four-dimensional reading (T1)
    is the one Λ asserts.
- **Beyond the three (T4).** Each 27 brings, besides its Standard Model generation:
  - a right-handed neutrino ν^c, so **three right-handed neutrinos**;
  - a vector-like pair D + D^c (colour triplets, Y = ∓1/3);
  - a Higgs-like pair H_u + H_d;
  - a singlet S.
  - The extra states must be heavy, through F-MC's rank-closing directions (THE_CLAIM §1).
  - In the exact flavor triplet the three generations are degenerate (Schur), so the mass hierarchy needs the triplet
    broken. That is BLIND here.
- **Mixing: fenced.** The record fences comparisons of mixing angles with data (THREE_GENERATIONS_AND_THE_WEAVE §3).
  The covenant is spent (B1066), and reopening needs the owner, L91's functor and the full checklist. The group-theory
  reading stands (TM1 with the swap, TM2 with the sign; `the_mixing.py`), and no comparison is made.

## What would show Λ wrong

- **A fourth chiral generation**, or a fourth light active neutrino.
- **No right-handed neutrinos at all.** Λ with F-MC puts one in each 27.
- **Light exotic colour triplets or extra Higgs pairs** that F-MC's directions cannot lift.
- **A flavor structure of the three that is not an irreducible triplet** of a group containing the cube's rotations.

## What is and is not derived

- **Derived from the principle** (no frame, no link):
  - three;
  - alike;
  - an odd net chirality, three when the end condition breaks no symmetry of the bulk problem (W28);
  - a complex flavor triplet;
  - the hand as the records' orientation.
- **Derived given F-MC's typed inputs:** the gauge group, its global form, and the hypercharge direction (main's
  theorem).
- **Derived given F-MC and Λ:** three chiral Standard Model generations, anomaly-free, alike, in a flavor triplet,
  with three right-handed neutrinos.
- **Not derived:** Λ itself.
  - W25 proves the weave's forced structures cannot supply it. W26 shows the threads' geometry and F-MC's arithmetic do
    not either.
  - Earning it is GENESIS FK11's open question: a frame derived from the principle, or main's ruling that Λ is the
    dictionary.
  - **W29 tested one candidate for the gauge side:** the weave's qubit with a qutrit flux (the ℤ₆ twist-eater), which
    is chosen, not forced.
    - It gives the Standard Model's SU(3) × SU(2) exactly, with complex quark doublets, and its flux is e^{2πiY}.
    - But the flux uses up the hypercharge, three is not forced (the moves allow 1, 3 or 5; locality gives 5), and
      there are no chiral leptons.
    - An echo, not a derivation. Λ stays the one link.
  - **W30 and W31 tested the remaining twist-eater candidates** (2026-10-08, the rules committed first).
    - An order-3 flux is allowed on the swap's fork, not forced (W30).
    - The ℤ₅ flux, the only one that keeps the whole Standard Model, gives complete SU(5) generations but no
      anomaly-free three for any flux (W31).
    - The puncture's end condition, the last computational route, does not make three in F-HE: its two sectors need
      opposite principles (W32).
    - Λ stays the one link.
  - **W34 asked whether the observer layer is the missing ingredient** (the owner's question, 2026-10-08, the rule
    committed first).
    - Its negatives belong to every thread, and the register carries neither hand.
    - It supplies neither the hand nor Λ. Λ stays the one link.
  - **The owner's ruling, 2026-10-08** (`docs/THE_OWNERS_RULINGS_2026-10-08.md`): Λ is a tagged working
    postulate. Results that use it carry "given Λ", and GENESIS FK11 stays formally open until it is
    earned. The observed branch is the even-tick weave ⟨L, R⟩ (ruling 1).

## Files

- `docs/dossiers/the_weave_2026-10-07/W27_RULE.md`, the rule, committed first.
- `docs/dossiers/the_weave_2026-10-07/the_link_tested.py` → `.json`, the tests.
- The steps' sources are the weave dossier's W1–W26 (`docs/dossiers/the_weave_2026-10-07/NOTE.md`) and THE_CLAIM §1.
