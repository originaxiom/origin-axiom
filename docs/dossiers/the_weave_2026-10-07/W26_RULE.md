# W26 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. Values already seen are listed.
Nothing here is a result.

## Why this route

- **The owner's choice** (2026-10-08, after W25): search beyond the weave.
- **The question.** Is there a forced structure outside the common point's local systems that fixes the gauge half? It
  would have to be a complex structure on the gauge side, the input W25 showed the weave's bundles cannot supply.
- **The two candidates the owner named.**
  - The threads' hyperbolic holonomies. They are complex, and they flip under the mirror.
  - Main's F-MC arithmetic route. The prime of norm three gives 2T (every odd-trace thread, B1601); McKay gives E₆;
    E₆'s 27 against 27̄ is the ℤ₃ = 2T/Q₈ character ω against ω².

## The cells, with predictions

The script is `the_weaves_mirror.py`, writing `.json` beside it. It is exact (integer matrices) except N2, which uses
SnapPy's hyperbolic structures (numerical, about 15 digits).

- **N1, the weave is closed under the mirror (exact).**
  - For every positive word φ in L and R with both letters, to length 10: S φ⁻¹ S⁻¹ equals the matrix of
    φ′ = reverse(φ) with L and R exchanged.
  - So the mirror of every thread is a thread: M_φ′ ≅ −M_φ, with the fibre's orientation kept and the ticks
    reversed.
  - Also counted: the amphichiral threads, where φ′ is a rotation of φ.
  - **Prior 99%.**
- **N2, the orientation-odd invariants pair up** (SnapPy, every hyperbolic thread to length 6, both signs).
  - Prediction: the volumes agree and the Chern–Simons invariants are opposite (mod ½) for every φ and φ′.
  - So the hyperbolic holonomies come in complex-conjugate pairs across the weave, and no net hand survives.
  - **Prior 95%.**
- **N3, the order-3 orientation alternates at every tick (exact).**
  - Each move is a transposition of the three parities mod 2: L fixes a and swaps b with ab, and R fixes b and swaps a
    with ab.
  - So rotating a cyclic word by one letter conjugates its image in S₃ by a transposition, which inverts a 3-cycle.
  - On every odd-trace thread to length 10, the direction of the 3-cycle the monodromy induces on the parities (in the
    shared basis) alternates at every tick.
  - So the ℤ₃ character of 2T (ω or ω²) is not a property of a thread but of a tick. It flips tick by tick.
  - **Prior 99%.**
- **N4, F-MC's chirality is an input in main's own hypothesis list** (a record fact; no computation).
  - THE_CLAIM §1 counts "two 𝔽₂ bits (time's arrow; chirality — the conjugation bit, = τ)" among the five typed
    external data.
- **N5, the verdict.**
  - Neither named candidate supplies a forced complex structure on the gauge side at the weave level.
    - The hyperbolic holonomies pair with their mirrors (N1, N2).
    - F-MC's ℤ₃ orientation flips at every tick (N3), and F-MC declares chirality an input (N4).
  - The weave's only hand is the records' orientation on the shared fibre (W21). It is forced only if the swap P is
    not a move (GENESIS GM5c, OPEN).
  - **Prior 90%.**

## What each outcome means

- **As predicted.** The search beyond the weave closes negative for these two candidates.
  - The gauge content of three generations needs F-MC's typed inputs (main's derivation of the gauge algebra, with the
    chirality bit) plus the identification FK11.
  - The weave contributes the count (three, the parities'; THE_CLAIM lists the generation count as open) and the
    consistent hand of the three (W22).
  - That is the record's best statement of the derivation. It is principle plus F-MC's inputs plus one named
    identification.
- **If N2 fails** (a thread whose mirror has a different complex volume): N1's algebra or SnapPy's census is wrong
  there. Find which before reading anything.
- **If N3 fails:** some odd-trace thread keeps one 3-cycle direction at every tick. That direction would be a forced
  ℤ₃ orientation, the candidate for F-MC's chirality bit. It would be read at once.

## Seen before this was written

- **By hand:** L and R mod 2 are transpositions; S L S⁻¹ = R⁻¹ and S R S⁻¹ = L⁻¹; LR and RL induce opposite
  3-cycles.
- **THE_CLAIM §1's hypothesis list,** read 2026-10-08.
- **SnapPy 3.3.2 is installed.** No manifold computed.
