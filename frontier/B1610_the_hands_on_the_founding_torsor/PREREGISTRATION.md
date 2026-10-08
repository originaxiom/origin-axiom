# B1610 — PREREGISTRATION: THE HANDS ON THE FOUNDING TORSOR — B1607's two hands read on B1083's four rules and on the arrow: which bit each hand is

cc (main), 2026-10-08, after B1609. A weave arc: exact word arithmetic and exact finite-group facts at the common point,
and W21's Hodge–Riemann form on W10's space V, for the four Fibonacci-type rules (B1083's K₄-orbit under swap- and
reversal-conjugation) and the inverse rule. **Sealed before `hands_on_the_torsor.py` computes any cell** (its
`--controls` mode, run before the seal, reproduces banked numbers only). No physical quantity. 0 of 19.

## Seen first

`VERDICT topic-sweep /torsor|orientation of the records|reading direction|arrow|which hand|conventional|left is a convention|invariant selector/: 115 of 1381 arcs on main match (NEGATIVE 19, OPEN 11, PROVED 85)`
— read for this arc: **B1083** (the founding K₄-torsor: two spendable bits, C = swap-conjugation and P = reversal, the
reading direction; the arrow not on the torsor — forced by the monoid's non-surjectivity, `bb` has no preimage;
orientability and amphichirality bought together at tick two), **B1174** (the mirror is complex conjugation on ℚ(√−3),
the orientation leg), **B1182** (the frame V₄ ⟨c, r⟩ and the branch V₄ one torsor by a unique isomorphism), **B1327**
(an invariant selector cannot pick a point of its own orbit; four types replace "externally supplied"), **B1607** (the
two hands; the rule σ = L∘P; reversal = conjugation by ι), **B1609** (the three's hand is the records' orientation, not
the McKay one), W21 (B1600's `w21_check.py`: L, R and the sign keep Q, the swap reverses it), GENESIS SE2 (orientability
CHOSEN); the SM seat's lane at `621383064` — W31 (no ℤ₅ flux gives an anomaly-free three; its twist-eater programme closes NEGATIVE) and the W32 rule (the puncture's end condition in F-HE's two sectors, sealed, unrun; its moves L and R by B1607). **Literature:** none beyond the arcs (the facts are elementary; the construction is the record's).

**Controls run before the seal** (`--controls`, `controls.json`): the form Q on V is kept by L, R and the sign and
reversed by the swap, signature (3, 3), V = T ⊕ T̄ (W21); σ's order-6 lift has real part ½ and its parity sense is
"backward"; 2T has two classes of four order-6 elements (B1607). No cell computed.

## Disclosed

- **An incident during this arc's design** (not a cell): the first draft imported W10's module with `json.dump` patched,
  but the module opens its banked `w10_check.json` for writing before dumping, so the file was truncated for about a
  minute while S88's certifying suite ran; restored by `git checkout` (byte-identical), no test reads that file, and the
  instrument now redirects that one write to the null device at `open()`. Recorded on S88's log.
- The predictions were reasoned before the seal (conjugation by P swaps T and T̄ and inverts a 3-cycle; conjugation by ι
  keeps both; inversion inverts both); the arc is not blind. The values of the double tick's turns on T are not predicted.
- "Hand (i) of a double tick" is read as its eigenvalues on T (the Q-positive piece under ⟨L, R⟩); "hand (ii)" as the
  sense of its 3-cycle on the parities and the 2T-class of its order-6 lift. These are the instrument's definitions,
  stated here, not derived.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **H0** | the four rules σ, C(σ), rev(σ), C(rev(σ)) are distinct, closed under C and the reversal, all positive (B1083) | 98% |
| **H1** | hand (ii): σ and rev(σ) "backward", C(σ), C(rev(σ)) and σ⁻¹ "forward"; on the double ticks the senses are the inverses (σ² = LR forward); the order-6 classes of the double ticks follow the senses | 90% |
| **H2** | every rule and σ⁻¹ reverses Q on V; every double tick keeps Q and keeps T; the double tick's turns on T are the same for σ and rev(σ), and the conjugate (each turn t ↦ 1 − t) for C(σ), C(rev(σ)) and σ⁻¹ | 80% |
| **H3** | C flips both hands, the reversal keeps both, the arrow flips both; with the arrow fixed, both hands are the C bit; the pair (hand (i), hand (ii)) of a double tick is one of two pairs, the same pair exactly when the C bit and the arrow agree — the relative hand is fixed for every rule | 80% |

**The reading, written before the run (the cells can only lower it).** If H1–H3 hold: the two hands of B1607 are one
bit on the founding torsor, given the forced arrow — the C bit, which letter is called *a*, a spendable naming (B1083) —
and the reading direction touches neither. So **which hand the three has is a naming**, as which hand is called "left"
is a convention in physics; what is not a naming is that the hands exist at all, i.e. that the weave is restricted to
the double tick (P not a move: GM5c), the same choice that makes the root orientable (SE2, CHOSEN; B1083's purchase at
tick two). The goal's question about the hand is therefore not "which" but "why the double tick": a selection of type S
in B1327's ledger, located. Weave or thread: weave.

## Instruments

`verification/hands_on_the_torsor.py` (`--controls` before the seal; the cells after); hashes in `ARTIFACT_HASHES.txt`.
