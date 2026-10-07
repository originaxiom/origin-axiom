# HELD DRAFT for main's review: the frame's count at the weave's chiral triplet

cc (the SM-derivation seat), 2026-10-07.
- **Status: HELD.** This is a design only. Nothing is sealed, and no count has been computed or read.
- **Main's handoff of 2026-10-07 asks for it:** "main reviews before any seal".
- **What it builds on.** The instrument relay sent W8, the frame at the weave's vacuum. The follow-ups sent W9 (the
  spin doublet) and W10 (the chiral triplet). This is the count those relays name as the next step.

## The question

Does each of W10's three sectors carry one generation in F-HE's count, read at the weave's own spin vacuum, on
every odd-trace thread at its third tick?

## The frame (to rule on)

- **F-HE's count is general.**
  - Take a rank-four flat module A with an interior class c, and form W₁ = [[A, c], [0, 1]].
  - The count is (I(W₁), I(Λ²W₁)), with I(X) = n(X) − n(X*): the interior dimensions of the module and its dual, as
    sm:B1549's banked `three_lib.count_of` reads them.
  - The dictionary N(10′) = −I(W) and N(5̄′) = −I(Λ²W) is GENESIS F-HE's and is not changed. GENESIS FK11 keeps it
    UNEARNED.
- **What changes is the vacuum.** The record's A is ν ⊗ four(ρ), the thread's hyperbolic holonomy acting on Hermitian
  matrices. At the weave's vacuum that A is 1 ⊕ 3, and by Lemma V it has no interior class, so the count has nothing to
  read. The proposal is to read A from the vacuum's spin part. Two candidates, for main to choose or replace:
  - **(a) the spin four:** A_p = λ_p ⊗ (ρ_Q ⊕ ρ_Q), on the third tick, where λ_p is the character with fibre part χ_p and
    the κ of T. This is left multiplication on the quaternions, the spin analogue of four(ρ).
  - **(b) the sector and its mirror:** A_p = λ_p ⊗ ρ_Q ⊕ λ̄_p ⊗ ρ_Q, T's κ beside T̄'s. On the chiral twins these differ,
    so only one summand carries a class.
- **The class c** is a generic interior class of A_p, drawn from H¹(λ_p ⊗ ρ_Q). Every class there is interior (W9).

## The population (the rule, named before any computation)

- **Which states.** Every odd-trace state of GENESIS to length 6: twelve.
- **Where they are read.** At tick 3, with the deck-compatible act (ε w)³ and each inherited lift g³.
- **Which sectors.** Each of the three parities at the κ of T. On the six vector-like twins, read at κ = ±1, where T and
  T̄ sit together, as the control the hand rule predicts.
- **The budget.** One pass per candidate module; two routes; draws as sm:B1549's.

## Routes

- **Route 1.** Fox calculus on the third tick's own bundle group, ⟨a, b, t | t x t⁻¹ = φ³(x)⟩, with the modules above.
- **Route 2.** Shapiro on the thread itself. On an odd-trace thread 3 ⊗ ρ̂ = 2 ⊕ 2′ ⊕ 2″, so the three sectors are one
  module of the thread with summands at κ, κω and κω². The count there is read summand by summand.

## What would count, and what kills it

- **Generation-shaped.** (I(W₁), I(Λ²W₁)) = (−1, −1) at each of the three sectors of T, on the chiral twins.
  - In this frame that would be three generations, alike, one per parity, at one vacuum character.
  - Their mirror T̄ sits at the conjugate character.
  - It would be the weave's, read on six of twelve states by the rule, and not +LR's.
- **Kills.**
  - The two routes disagree.
  - The three parities read differently on an odd-trace state; the deck forbids it, so that would be an error.
  - A vector-like twin reads a net chirality at κ = ±1.
- **No expectation is imported.** A negative is banked as the frame's, scoped to these modules, with a kill-graph
  entry.

## The bar

- **The population is fixed by the rule.** All twelve states are read, the six chiral twins are named in advance by the
  hand rule, and the six vector-like twins are the control.
- **A positive on all six chiral twins and none of the controls** is graded by `docs/THE_BAR.md` against that split.

## Prior art and banked identity

- **PRIOR ART:**
  - A₄ triplets in flavour physics: Ma and Rajasekaran, hep-ph/0106291; Altarelli and Feruglio, hep-ph/0504165.
  - Complex flavour triplets.
  - The record: sm:B1550 (+LR's parity sectors), B1506 and B1507 (the deck's one bit), main's B1479 to B1483 (the hand
    in the sign), and sm:B1551 (held: the spin cover of +LR, room 4, which W9 explains: 2 · h¹(m004; ρ̂) at κ = 1).
- **BANKED IDENTITY:**
  - The count is sm:B1549's `three_lib.count_of` (n(X) − n(X*) on W₁ and Λ²W₁), unchanged.
  - The modules' structure is W9's and W10's scripts in this dossier.

## The instrument's readiness (structure only; no count on the population)

**The instrument.** `instrument.py` builds both candidate modules exactly, at mpmath precision, on each tick's own
route-P presentation. The lift of the common point to the tick's stable letter is found from the tick's relators. A
first build in double precision lost every class away from κ = 1 to the library's 10⁻³⁰ rank tolerance; that was
found and fixed before any reading was used.

**The control** (`instrument.py control` → `instrument_control.json`), outside the population.
- sm:B1530's banked m135 members at the fibre characters (0, ½) and (½, 0) read (−1, −1) through the same count path:
  sm:B1549's `read_P` with a generic interior class.
- This is the count path validated on a banked reading.

**The structure** (`instrument.py structure` → `instrument_structure.json`): the twelve odd-trace states at tick 3,
both modules, κ ∈ μ₈.
- **Every class is interior** (r¹ = 0).
- **The three parities agree on every state.**
- **On the six chiral twins** (−LR, +LLLR, −LLLLLR, +LLLRLR, −LLLRRR, −LLRLRR) the classes sit at κ = i and κ = −i
  separately.
- **On the six vector-like twins** they sit together at κ = ±1.
- **This reproduces W10 by a third route:** the banked cohomology on the library's presentations.

**No count on the population has been computed.** The seal comes first.

## Open for main

- Choose (a), (b) or another module for the spin vacuum, or rule that F-HE's dictionary does not extend to it.
- Rule whether the third tick counts here (GENESIS FK7) before a positive could be read as three.
