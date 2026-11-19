# W-R1: mutual reading. The weave's private records read each other: every non-zero V_k carries invariant pairings that the orientation-preserving moves keep, the two ends' records read each other with a non-zero value, and records of different weight are tied by maps B1717 could not see (End_G(V₄) = 2: a non-scalar record exists). Where a reading is unique (V₂, V₃, V₅) its scale-free values are rationals fixed by the group (−4, −1, −1/16). Where the record has two or more isotypic parts (V₄, V₆) the moves keep a whole family of readings and pick none, so a value there would be chosen, not derived. The mirror reverses every reading. On the weave's own records a reader brings structure and, at most, a new free choice; it derives no magnitude

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free and exact. It closes card W-R1
(`relays/cards/CHAT1_W-R1_mutual_reading.md`), opened at the author's word of 2026-11-19 after a conversation on the
programme's wall. Nothing is set beside a measured number.

**Order of work.**
- The card, with the sweep, the derivation and every prediction: e3771b29e, rewrapped at c2eff6ba6.
- Before the script, at f039ca4df, its control C4 was amended (the first C4 asked for forms not defined at a random
  pair), and Burnside's dimensions were added as predictions. The card's note then named only C4. Its errata after the
  run say so (4e6d906d1).
- The script `relays/chat1_2026-11-19_wr1/wr1_mutual_reading.py`: 0d930579a, with `SCRIPT_SHA256.txt`.
  - It was smoke-tested on control inputs: Burnside's closure on Pauli matrices, the symplectic form of SL(2) and St(L).
  - It was also run on the private module k = 2, and only its dimension, which is on record, was looked at.
- The output: `wr1_out.txt` and `wr1_err.txt` (empty) at be765727a, and `wr1_summary.json` at 946bb5938, both committed
  before they were read. The run took 8 seconds, so the first commit already held the whole printed output.

**Not blind.** B1675's, B1717's and W-C3's numbers for k ≤ 3 were known, and the predictions for k ≥ 4 were derived from
them before the run (the card, § 3).

**Typing.** [E] marks what the run, the record or a standard result establishes; [J] marks this seat's judgement.

---

## 0. In short

1. **[E] The derivation holds exactly for k = 1 to 6.** The private records factor as V_k ≅ St ⊗ M_k:
   - St is the torus's first cohomology, on which each move acts by its own 2 × 2 matrix;
   - M_k is the quaternion-fixed part of Sym^{2k}, on which each move acts through S₃ = Out(Q₈);
   - M_k = 0, σ, ε, 1 ⊕ σ, σ, 1 ⊕ ε ⊕ σ for k = 1 to 6.

   Every prediction of the card holds (P0 to P3, and Burnside's 16, 4, 20, 16, 24), and every control. The referee's
   own code found the same factoring by the natural map for k up to 8.
2. **[E] Records read each other.**
   - **Pairings.** Every non-zero V_k carries pairings that L and R keep.
     - For k ≤ 6 they are alternating and non-degenerate.
     - They are unique up to scale at k = 2, 3 and 5. At k = 4 they form a pencil, and at k = 6 a three-dimensional
       family.
     - That such a pairing exists is forced by Poincaré duality on the punctured torus's parabolic cohomology, a fact of
       its topology.
   - **The ends.** The two ends' records read each other: in V₂ and V₅, B(x_L, x_R) ≠ 0.
   - **Maps.** End_G(V₄) = 2 and End_G(V₆) = 3, so a non-scalar relational record exists in B1717's own sense once
     k ≥ 4. Records of different weight are tied too: V₂, V₄, V₅ and V₆ pairwise, V₃ with V₆, and V₄ with V₆ twice.
3. **[E] What the readings' values are,** for k ≤ 6, for bilinear pairings and linear maps.
   - Every invariant pairing is ω_St, the torus's one symplectic form, times an S₃-invariant pairing of the M_k. Every
     invariant map is the identity on St times an S₃-map.
   - **Where the reading is unique** (V₂, V₅), its scale-free values are rationals fixed by S₃ and SL(2, ℤ):
     - R₁ = −4 and R₂ = −1, as predicted;
     - B(x_L, x_R)²/(B(x_L, R²x_L)·B(x_R, L²x_R)) = −1/16 (the referee, checked here).
   - **Where it is not** (V₄, V₆), the values move with the reading. On V₄, with the readings W₁ + tW₂, the ratio R₁
     for a record L keeps runs continuously with t (for one such record, 32/(t + 6)). The moves fix no t.
4. **[E] The mirror reverses every reading.** P sends each invariant pairing to its negative, so under ⟨L, R, P, −I⟩ no
   pairing survives. [J] A reading is an oriented relation, and its sign is the hand.
5. **[J] What it means.**
   - A reader built from the weave's own records brings structure: pairings, maps, and the hand as their sign.
   - Where a record has more than one isotypic part, the reader also brings a new free parameter, the parts' relative
     weight. That is a choice, not a derivation.
   - It derives no magnitude. This is the programme's pattern again: the structure is forced and the value is chosen.
   - The idea is not retired. Its first and cheapest setting is retired as a source of derived magnitudes. The
     settings left are named in § 5.

---

## 1. What the record already had (the card's sweep)

The plan made in conversation had three tests. The sweep found the first two decided on record.
- **B1675's open question** (a relational record, Hom_G(W, V)) was answered by **B1717** (PROVED; P-278 DONE).
  - On V₂ and V₃ the moves act irreducibly, with scalar commutants, and Hom_G(V₂, V₃) = 0.
  - Nothing maps to or from the coefficient module.
  - Its scope stopped at k ≤ 3 and at linear maps. Pairings were never computed.
- **The qubit axis** is decided by B1687 (the moves generate the whole one-qubit Clifford group modulo phases) with the
  group-wall theorem: B1327's no-go (B1327 is OPEN; only its no-go is used), B1881 (A), and this seat's walls note of
  2026-11-11 (a project note, not on main). A condition the moves respect cannot pick an axis. It can fix only how two
  frames sit relative to each other, B1327's type R.
- **The record's earlier readings of the observer:**
  - B1614, the earlier awareness arc: the weave names itself but cannot sign itself;
  - B1169 and B1184: the object cannot close itself, and its boundary sees everything and chooses nothing;
  - B1750: the observer typed as closer, signer and identifier;
  - P-204: the author's argument that existence lives in the whole system's relations;
  - P-177: the author's view that reality is the interaction between existence and what pushes back; its item 5 is
    still open.

What was untested: a pairing between two records, each evaluating the other, kept by the moves. That is what this card
computes.

## 2. The derivation, and its check

**The derivation (the card, § 3).** At the common point ρ_Q has image Q₈. A non-trivial character of Q₈ adds nothing
private. The trivial part contributes H¹(F₂; ℂ) ⊗ M_k, all of it private. So V_k ≅ St ⊗ M_k, with dimension 2·m₀(k),
where m₀(k) = ((2k + 1) + 3(−1)^k)/4. This is B1675's "a thread acts on the private states as its hyperbolic matrix
tensored with a map of finite order", made exact. The S₃ action factors through reduction mod 2, GL(2, ℤ) → GL(2, F₂).

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

**So,** for k, k′ ≤ 6:
- dim End_G(V_k) = dim End_{S₃}(M_k), and dim Hom_G(V_k, V_k′) = dim Hom_{S₃}(M_k, M_k′).
- The invariant maps are id_St ⊗ (S₃-maps), and the invariant pairings ω_St ⊗ (S₃-invariant pairings of the M's).
- These are shown by the dimensions together with the evident inclusion. A general proof would use the density of
  Γ(2) in SL(2) and the first fundamental theorem; it is not written here.
- **Why the pairings are alternating.** ω_St is alternating. For k ≤ 6 M_k is multiplicity-free, and each of S₃'s
  irreducibles carries a single invariant form, which is symmetric. Without multiplicity-freeness this fails. At k = 8,
  M₈ = 1 ⊕ 2σ, and V₈ carries five invariant forms, one of them symmetric (the referee's code).
- **Why P reverses them.** P has determinant −1 on St.

## 4. The ends read each other (T2)

R₁ = B(x_L, R²x_L)/B(x_L, R x_L), and R₂ = B(x_L, x_R)²/(B(x_L, P x_L)·B(x_R, P x_R)).

| k | L keeps | R keeps | P keeps | B(x_L, x_R) | R₁ | R₂ |
|---|---|---|---|---|---|---|
| 2 | 1 | 1 | 2 | non-zero | −4 | −1 |
| 3 | 0 | 0 | 1 | — | — | — |
| 4 | 2 | 2 | 3 | — | — | — |
| 5 | 1 | 1 | 2 | non-zero | −4 | −1 |
| 6 | 2 | 2 | 4 | — | — | — |

- At V₃ the ends keep nothing.
- At V₄ and V₆ the values depend on the choice of the kept record and of the reading. On V₄, with the readings
  W₁ + tW₂, R₁ for the two basis records L keeps (in this seat's basis) is 32(35 − t)/(33t + 70) and 32/(t + 6). They
  run continuously with t (a post-hoc check of the referee's finding, with this seat's committed functions, outside the
  sealed run).

The values were predicted before the run.
- **R₁ = −4.** On St, the forms give (−2)/(−1). On σ, the fixed lines of the two reflections meet at 60°, so the
  reflected line makes 120°.
- **R₂ = −1.** P carries x_L to a multiple of x_R, P² = 1 and B is alternating.
- **The referee's third ratio,** B(x_L, x_R)²/(B(x_L, R²x_L)·B(x_R, L²x_R)), is −1/16 on V₂ and V₅. It was checked here
  with the same functions.

[E, a derivation, on V₂ and V₅] Where the reading and the kept records are unique, every scale-free number their
reading makes is a rational fixed by S₃ and SL(2, ℤ).

## 5. What it means [J]

**For the idea.**
- Records read each other in the weave. On the private classes a relational record exists both as a pairing and as a
  map: the pairings of § 3, and the non-scalar maps at k = 4 and 6. The pairings' existence is a fact of the punctured
  torus's topology.
- No reading derives a value. Where the reading is unique, its values are rationals fixed by the group. Where it is
  not, the moves leave a family of readings and pick none.
- So on the weave's own records a reader brings structure and, at most, a new free parameter: the relative weight of a
  record's isotypic parts. The value would be chosen, as every value in the programme so far has been.
- This is lesson 1 of the walls note again, now for readers: a reader built from the weave's own modules is still built
  from the moves.

**For the hand.** The mirror reverses every reading. A mutual reading needs an orientation, and its sign is the hand.
That is B1750's signer: the orientation is a convention the reader brings. And it is the walls note's lesson 2,
placing τ and getting a hand are one problem, met from the side of the reader.

**For B1717 and P-278.** P-278 asked whether a non-scalar relational record exists. In B1717's setting (k ≤ 3) it does
not. At k = 4 and k = 6 it does: End_G(V₄) = 2 and End_G(V₆) = 3, the projections onto a record's isotypic parts. And
records of different weight are tied by maps, each the identity on St times an S₃-map between recurring irreducibles.
B1717's "a module beyond these" is met inside the private classes.

**What stays open: the settings this card did not reach.**
- **Readers in other modules.**
  - At the common point the matter triplet T and ρ_Q's odd blocks have finite images (B1687), so no τ enters them, and a
    reading there would meet the same finiteness.
  - The frame's couplings, at the field stage, where τ enters, could carry a continuous reading. That is where the
    idea can still pay.
- **A reader of the frame:** the read-out I-33 itself, and two frames reading each other, such as the two vacua S and
  S̄. That is P-177's item 2, folded into P-277, which is DONE.
- **The free parameter found here:** whether any principle fixes the relative weight of a record's isotypic parts.

## 6. Typed

- **[E] by the run:** §§ 2, 3 and 4's tables, exact, with C1 to C4 holding:
  - C1, W-C3's numbers for k ≤ 3;
  - C2, B1717's commutants and Hom;
  - C3, End_G(V₂ ⊕ V₂) = 4;
  - C4, no lift at a random pair.
- **[E] by a derivation, checked by the run's dimensions:**
  - the forms of § 3's "So", for k ≤ 6;
  - § 4's last line, on V₂ and V₅ only.
- **[E] by post-hoc checks outside the sealed run** (the referee's code, and this seat's committed functions): −1/16;
  V₄'s family; P0 for k = 7 and 8; M₈.
- **[E] standard:** the decomposition of Q₈-modules; Schur's lemma; Poincaré duality on parabolic cohomology; S₃'s
  character table.
- **[E] by the record:** B1675, B1717, B1687, B1881, B1614, B1750, P-204, P-177 and P-278; this seat's W-C3.
- **Cited, not [E]:** B1327 (OPEN; only its no-go is used), and this seat's walls note (a project note, not on main).
- **[J]:** § 5; § 0's items 4 (the hand) and 5.

## Files

- `relays/chat1_2026-11-19_wr1/`: `wr1_mutual_reading.py`, `SCRIPT_SHA256.txt`, `wr1_out.txt`, `wr1_err.txt` and
  `wr1_summary.json`.
  - The summary file records "P_reverses": 0 under the full group, where it was not computed; the output prints "−".
  - Its "k" field is empty and unused.
  - The script's run command in its docstring lacks −B. The run left a `__pycache__` in W-C3's folder, which is
    ignored and not committed.
- The card: `relays/cards/CHAT1_W-R1_mutual_reading.md`, with its errata.
- The code imported unchanged: `relays/chat1_2026-11-11_wc3/w34_private_states_amendment_1.py` (W-C3).

## Provenance

The first version (d4fa293ec) was pushed before its referee read finished, following the author's word of 2026-11-15
on untracked notes. A referee who had not written it read it. The verdict was sound with corrections.

**What held.**
- The order of work and the SHA. A rerun of the script reproduced its output and its summary file.
- The derivation, checked by hand, and the script's conventions. V_k, St and M_k use the same pull-back, so the
  intertwiner test means what it says.
- Every number of the run, recomputed on the referee's own code: a different model of Sym, hand-made lifts, Fox calculus
  and exact arithmetic. P0 holds by the natural map for k up to 8.

**Nine corrections were required.**
1. "Integers", "every scale-free value is fixed by the group" and "nothing in a reading can be continuous".
   - −1/16 is scale-free and not an integer.
   - On V₄ and V₆ the readings form families, and their values move continuously.
   - The title and §§ 0, 4 and 5 now say where a reading's values are fixed (where it is unique) and where they are
     chosen.
2. The general claims of § 0's item 3 were typed [E] beyond what the run shows. They are now scoped to k ≤ 6 and to
   pairings and maps, and the magnitude claim is [J].
3. The reason given for "alternating" needs M_k to be multiplicity-free. It fails at k = 8.
4. "As a pairing and not as a map" contradicted the run's own maps and End_G(V₄) = 2. It is gone, and P-278's yes at
   k ≥ 4 is stated.
5. P-177.
   - A quotation of the author's words is now a paraphrase.
   - The two vacua are P-177's item 2, folded into P-277 (DONE), not its open item.
   - The card carries the same errata.
6. The first output commit was not mid-run. The run had finished in 8 seconds.
7. The amendment of f039ca4df also added the Burnside predictions. It is now disclosed.
8. The typing: the hand is [J]; § 4's last line is a derivation on V₂ and V₅; the walls note is not on main, and
   B1327 is OPEN.
9. "τ enters" the other modules was wrong for T and ρ_Q's odd blocks, which have finite images at the common point. It
   is now limited to the frame's couplings at the field stage.

**Smaller points, each applied:**
- the pairing's existence as Poincaré duality;
- V₃'s empty kept spaces;
- R₂'s sign from alternation;
- P-278's answer by End_G;
- B1717 "in its setting";
- the summary file's details;
- the run command's −B;
- the smoke test's disclosure;
- the card's P1 line and its "−I" wording.

**Checked at source here:** the −1/16 and the V₄ family, with this seat's committed functions (the referee's basis gives
32/(t + 6) for one record, which is one of the two here); P-177's items, through the mask; the commit times.

An older relay of this seat (2026-11-06, door C) carries the same quotation of the author's words. It is left as
registered, since its text and hash are in main's register; this note records it.

The read's corrections are applied in this version.

0 of 19.
