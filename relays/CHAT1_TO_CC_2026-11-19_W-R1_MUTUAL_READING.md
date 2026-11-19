# W-R1: mutual reading. The weave's private records can read each other: every k ≤ 6 carries an invariant pairing that every orientation-preserving move keeps, the two ends' records read each other with a non-zero value, and records of different weight are tied by maps B1717 could not see. But every such reading is the torus's one symplectic form times finite-group data of S₃, the mirror reverses each one, and its scale-free values are integers (−4 and −1 here). On the weave's own records the silence on magnitudes is the group's, not a missing reader's

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free and exact. It closes card W-R1
(`relays/cards/CHAT1_W-R1_mutual_reading.md`), opened at the author's word of 2026-11-19 after a conversation on the
programme's wall. Nothing is set beside a measured number.

**Order of work.**
- The card, with the sweep, the derivation and every prediction: e3771b29e. It was rewrapped at c2eff6ba6, and its
  control C4 amended before the script at f039ca4df (the first C4 asked for forms that are not defined at a random
  pair).
- The script `relays/chat1_2026-11-19_wr1/wr1_mutual_reading.py`: 0d930579a, with `SCRIPT_SHA256.txt`. It was
  smoke-tested on control inputs only: Burnside's closure on Pauli matrices, the symplectic form of SL(2), St(L), and
  the private module k = 2, whose dimension is on record.
- Its output, `wr1_out.txt`, `wr1_err.txt` (empty) and `wr1_summary.json`: 946bb5938. A partial output was committed
  unread mid-run (be765727a). Both were committed before the output was read.

**Not blind.** B1675's, B1717's and W-C3's numbers for k ≤ 3 were known, and the predictions for k ≥ 4 were derived from
them before the run (the card, § 3).

**Typing.** [E] marks what the run, the record or a standard result establishes; [J] marks this seat's judgement.

---

## 0. In short

1. **[E] The derivation holds exactly for k = 1 to 6.** The private records factor as V_k ≅ St ⊗ M_k:
   - St is the torus's first cohomology, on which each move acts by its own 2 × 2 matrix;
   - M_k is the quaternion-fixed part of Sym^{2k}, on which each move acts through S₃ = Out(Q₈);
   - M_k = 0, σ, ε, 1 ⊕ σ, σ, 1 ⊕ ε ⊕ σ for k = 1 to 6.

   Every prediction of the card holds (P0 to P3), with Burnside's dimensions 16, 4, 20, 16, 24, and every control.
2. **[E] Records read each other.**
   - Every non-zero V_k carries an invariant pairing that L and R keep: alternating, non-degenerate, unique up to scale
     where M_k is irreducible. The intersection pairing of the punctured torus is one of them, and, where they are
     unique, it is the one.
   - The two ends' records read each other: in V₂ and V₅, B(x_L, x_R) ≠ 0.
   - Records of different weight are tied by linear maps the moves keep: V₂, V₄, V₅ and V₆ pairwise, V₃ with V₆, and
     V₄ with V₆ twice. B1717's "a record needs an end or another module" now has its other modules, inside the private
     classes.
3. **[E] But no reading carries a magnitude.**
   - Every invariant relation between private records is ω_St, the torus's one symplectic form, times S₃-equivariant
     data of the M_k.
   - So every scale-free value is fixed by the group. The two the card named are integers, R₁ = −4 and R₂ = −1, as
     predicted.
4. **[E] The mirror reverses every reading.** P sends each invariant pairing to its negative, so under ⟨L, R, P, −I⟩ no
   pairing survives. A reading is an oriented relation: its sign is the hand.
5. **[J] What it means.** On the weave's own records the silence on magnitudes is the group's, not a missing reader's.
   - The idea is not retired; this first and cheapest setting of it is.
   - The settings left are named in § 5: readers in other modules, and a reader of the frame.

---

## 1. What the record already had (the card's sweep)

The plan made in conversation had three tests. The sweep found the first two decided on record.
- **B1675's open question** (a relational record, Hom_G(W, V)) was answered by **B1717** (PROVED; P-278 DONE).
  - On V₂ and V₃ the moves act irreducibly, with scalar commutants, and Hom_G(V₂, V₃) = 0.
  - Nothing maps to or from the coefficient module.
  - Its scope stopped at k ≤ 3 and at linear maps. Pairings were never computed.
- **The qubit axis** is decided by B1687 (the moves generate the whole one-qubit Clifford group modulo phases) with the
  group-wall theorem (B1327's no-go, B1881 (A), this seat's walls note). A condition the moves respect cannot pick an
  axis; it can fix only how two frames sit relative to each other, B1327's type R.
- **The record's earlier readings of the observer:**
  - B1614, the earlier awareness arc: the weave names itself but cannot sign itself;
  - B1169 and B1184: the object cannot close itself, and its boundary sees everything and chooses nothing;
  - B1750: the observer typed as closer, signer and identifier;
  - P-204: the author's argument that existence lives in the whole system's relations;
  - P-177: the author's "the interaction is the reality", still open.

What was untested: a pairing between two records, each evaluating the other, kept by the moves. That is what this card
computes.

## 2. The derivation, and its check

**The derivation (the card, § 3).** At the common point ρ_Q has image Q₈. A non-trivial character of Q₈ adds nothing
private. The trivial part contributes H¹(F₂; ℂ) ⊗ M_k, all of it private. So V_k ≅ St ⊗ M_k, with dimension 2·m₀(k),
where m₀(k) = ((2k + 1) + 3(−1)^k)/4. This is B1675's "a thread acts on the private states as its hyperbolic matrix
tensored with a map of finite order", made exact.

**The check (T0, P0).** St and M_k were built by their own routes:
- St from the moves on Hom(F₂, ℂ): L = [[1, 0], [1, 1]], R = [[1, 1], [0, 1]], P the swap, −I = −1;
- M_k from the normalised lifts on Sym^{2k}, restricted to the vectors Q₈ fixes.

For every k ≤ 6 there is an invertible map St ⊗ M_k → V_k that every move intertwines.

| k | dim V_k | M_k's character (id, L, LR) | M_k | dim Hom_G(St ⊗ M_k, V_k) |
|---|---|---|---|---|
| 1 | 0 | — | 0 | — |
| 2 | 4 | (2, 0, −1) | σ | 1 |
| 3 | 2 | (1, −1, 1) | ε | 1 |
| 4 | 6 | (3, 1, 0) | 1 ⊕ σ | 2 |
| 5 | 4 | (2, 0, −1) | σ | 1 |
| 6 | 8 | (4, 0, 1) | 1 ⊕ ε ⊕ σ | 3 |

## 3. The records and their readings (T1)

**Each record with itself,** under ⟨L, R⟩:

| k | End_G | invariant pairings | symmetric, alternating | rank of a generic one | P reverses | Burnside |
|---|---|---|---|---|---|---|
| 2 | 1 | 1 | 0, 1 | 4 | 1 | 16 |
| 3 | 1 | 1 | 0, 1 | 2 | 1 | 4 |
| 4 | 2 | 2 | 0, 2 | 6 | 2 | 20 |
| 5 | 1 | 1 | 0, 1 | 4 | 1 | 16 |
| 6 | 3 | 3 | 0, 3 | 8 | 3 | 24 |

Under ⟨L, R, P, −I⟩ the commutants and Burnside's dimensions are the same, and no invariant pairing is left.

**Records of different k,** under ⟨L, R⟩: Hom_G in both directions, and the invariant pairings between them.
- 1 and 1: (V₂, V₄), (V₂, V₅), (V₂, V₆), (V₃, V₆), (V₄, V₅), (V₅, V₆);
- 2 and 2: (V₄, V₆);
- 0 and 0: (V₂, V₃), (V₃, V₄), (V₃, V₅).

Under ⟨L, R, P, −I⟩ the maps are the same, and every pairing between different k is gone.

**So:** dim End_G(V_k) = dim End_{S₃}(M_k), dim Hom_G(V_k, V_k') = dim Hom_{S₃}(M_k, M_k'), and the invariant pairings
are ω_St ⊗ (S₃-invariant pairings of the M's). Each is alternating because ω_St is and S₃'s representations are real.
Each is reversed by P because P has determinant −1 on St.

## 4. The ends read each other (T2)

R₁ = B(x_L, R²x_L)/B(x_L, R x_L), and R₂ = B(x_L, x_R)²/(B(x_L, P x_L)·B(x_R, P x_R)).

| k | L keeps | R keeps | P keeps | B(x_L, x_R) | R₁ | R₂ |
|---|---|---|---|---|---|---|
| 2 | 1 | 1 | 2 | non-zero | −4 | −1 |
| 3 | 0 | 0 | 1 | — | — | — |
| 4 | 2 | 2 | 3 | — | — | — |
| 5 | 1 | 1 | 2 | non-zero | −4 | −1 |
| 6 | 2 | 2 | 4 | — | — | — |

Where L's and R's kept spaces are lines (V₂ and V₅) the ratios are defined; elsewhere they depend on a choice of line.

The values were predicted before the run.
- **R₁ = −4.** On St, the forms give (−2)/(−1). On σ, the fixed lines of the two reflections meet at 60°, so the
  reflected line makes 120°.
- **R₂ = −1.** P carries x_L to a multiple of x_R, and P² = 1.

[E] The two ends' records read each other, and every number their reading makes is an integer of SL(2, ℤ) times a
number of S₃.

## 5. What it means [J]

**For the idea.**
- Records read each other in the weave. B1675 asked whether a relational record exists; on the private classes it
  does, as a pairing and not as a map. The pairing is the intersection pairing the topology gives.
- But nothing in a reading can be continuous. Every invariant relation among these records is the torus's one
  symplectic form times finite-group data, so every scale-free number it makes is an algebraic constant fixed by the
  group. On the weave's own records, the silence on magnitudes is the group's, not a missing reader's. This is lesson 1
  of the walls note again, now for readers: a reader built from the weave's own modules is still built from the moves.

**For the hand.** The mirror reverses every reading. A mutual reading needs an orientation, and its sign is the hand.
That is B1750's signer: the orientation is a convention the reader brings. And it is the walls note's lesson 2,
placing τ and getting a hand are one problem, met from the side of the reader.

**For B1717.** Its "a record needs an end or another module" is answered within the private classes. The other modules
are the higher weights: V₂ maps into V₄, V₅ and V₆ equivariantly. B1717's scope (k ≤ 3, linear maps) is why it saw
none.

**What stays open: the settings this card did not reach.**
- **Readers in other modules:** the matter triplet T, ρ_Q's odd blocks, and the frame's couplings. These carry
  continuous data (τ enters the frame), so a reading there could be continuous. That is where the idea can still pay.
- **A reader of the frame:** the read-out I-33 itself, and two frames reading each other, such as the two vacua S and
  S̃ (P-177's open item).

## 6. Typed

- **[E] by the run:** §§ 2 to 4, exact, with C1 to C4 holding:
  - C1, W-C3's numbers for k ≤ 3;
  - C2, B1717's commutants and Hom;
  - C3, End_G(V₂ ⊕ V₂) = 4;
  - C4, no lift at a random pair.
- **[E] standard:** the decomposition of Q₈-modules; Schur's lemma; the intersection pairing of a punctured surface;
  S₃'s character table.
- **[E] by the record:** B1675, B1717, B1687, B1327, B1881, B1614, B1750, P-204 and P-177; this seat's W-C3 and walls
  note.
- **[J]:** § 5.

## Files

- `relays/chat1_2026-11-19_wr1/`: `wr1_mutual_reading.py`, `SCRIPT_SHA256.txt`, `wr1_out.txt`, `wr1_err.txt` and
  `wr1_summary.json`.
- The card: `relays/cards/CHAT1_W-R1_mutual_reading.md`.
- The code imported unchanged: `relays/chat1_2026-11-11_wc3/w34_private_states_amendment_1.py` (W-C3).

This relay is pushed before its referee read finishes, following the author's word of 2026-11-15 on untracked notes.
Its read's corrections are not yet applied in this version.

0 of 19.
