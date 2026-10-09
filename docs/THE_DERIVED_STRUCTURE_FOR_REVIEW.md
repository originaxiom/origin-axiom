# What the principle derives, and how many numbers it leaves — a report for outside review

*origin-axiom, main seat, 2026-10-08 (through B1620; GENESIS v1.35); corrected 2026-10-09 (B1625; GENESIS v1.36) with the SM seat's W42–W45 and relay §44.* This is the owner-agreed restatement of the goal
(2026-10-08): derive the Standard Model's **structure**, and say **how many free numbers** the principle leaves and why.
Every claim below is about the weave (every object the principle allows, none chosen), not about one member. Each item
names the arc that computed it; the arcs carry the code, the sealed predictions and the run logs. **The score on the
values is 0 of 19.** The reader is asked to check the derivations and the count, not to accept a value.

## 1. The setting, in five lines

1. **The principle** (GENESIS §1): existence is what remains when cancelling to nothing cannot complete. Its
   mathematical reading is a two-letter non-commutative word whose commutator never cancels.
2. **The rule** is the Fibonacci substitution σ: a → ab, b → a, which is L∘P with σ² = LR on F₂ = ⟨a, b⟩. It carries a
   forced arrow (B1083) and the inflation φ.
3. **The weave** is the joint action of the moves L and R on two records. Its threads are the positive words in L and R
   (the once-punctured-torus bundles of positive monodromy, the figure-eight knot complement among them). The weave is
   the object; no thread is chosen.
4. **The common point** is the quaternion representation ρ_Q: a ↦ i, b ↦ j, shared by every thread (B1601). Over it,
   V = ⊕_p H¹(F₂; χ_p ⊗ ρ_Q), summed over the three non-trivial parity characters χ_p, splits as T ⊕ T̄. T is the
   holomorphic triplet: one line per parity sector.
5. **The weave's group** G is the set of lifts of L and R acting on V. It has order 96 and acts faithfully and
   irreducibly on T, as the cube's rotation group twisted by a character c (B1611; the SM seat's W38). It is not of
   type I.

## 2. What is derived (structure)

| | derived | status | arcs |
|---|---|---|---|
| **Flavour three** | T is three-dimensional, irreducible under G, one line per parity: three generations, alike | DERIVED on the weave | B1606 (GENESIS v1.28), the SM seat's W19–W22 verified |
| **Gauge three** | the S(U(3) × U(2)) frame | a SELECTION, given Λ (a Lagrangian half), not derived | B1606, FK11 (owner: Λ a tagged working postulate) |
| **The hand** | which of T, T̄ is called left | a CONVENTION: the orientation sheet chosen at SE2; the owner ruled "even ticks observed" | B1609, B1610, GM5c |
| **CP** | generalised CP is the record swap T ↔ T̄ | CP violation ALLOWED, not forced; the group fixes no phase | B1611 |
| **Mixing, by the group** | six fixed patterns from pairs of residual subgroups | none in the data (leptons or quarks) | B1612 |
| **Mixing, allowed** | a trimaximal relation: TM1 (first column ⅔, ⅙, ⅙) or TM2 (second column ⅓, ⅓, ⅓) | in the frame where all of G is flavour: TM1 or TM2 under T̄ ⊗ T, TM2 only under T ⊗ T, neither under Sym² T; where c is gauge, TM1 and TM2 under both and one relation under Sym² T (the SM seat's W43, W44) | B1612, B1613, B1620 |
| **Masses** | not in the group | Schur on G; on every subgroup the masses stay free | B1615–B1618, B1620 |
| **Mixing and the modulus** | with couplings depending on τ alone, every mixing matrix is a permutation | the observed mixing NEEDS a vacuum that breaks the parity grading | B1620 (the SM seat's §41, confirmed) |

**The falsifier (P10).** If the leptons' residual is the TM type, then sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃) ≈ 0.318. And with
θ₂₃ measured, δ_CP is fixed up to its mirror: 252.7°–292.9° over θ₂₃'s present 3σ range, central 262.5°,
J ≈ −0.034. Reactor precision on θ₁₂ tests (a); DUNE and Hyper-Kamiokande test (b). A failure kills the TM1 reading,
not the weave. **P10 is TM1's prediction, so it applies under T̄ ⊗ T.** Given Λ (T ⊗ T) in the frame where all of G is
flavour the family is TM2, with sin²θ₁₂ = 1/(3 cos²θ₁₃) ≈ 0.341, inside the present 3σ range; where c is gauge, TM1
returns under T ⊗ T. P10 therefore tests Λ, a frame (GENESIS FK11) and a Higgs content together.

## 3. How many numbers it leaves, and why

**The count: all 19 are free.** The reasons are theorems or exhaustive computations, not missing effort:

- **The 13 flavour parameters (B1620).** Take every one of G's 68 subgroups as a possible residual of a sector, none
  chosen:
  - three distinct masses need an abelian residual (57 of 68, exactly the abelian ones), and every such residual leaves
    the masses free;
  - no pair of residuals with a mixing family short of the full four reaches the CKM.
  - This holds under all three readings of the mass term: T̄ ⊗ T; T ⊗ T (given Λ every left-handed field lies in T, the
    SM seat's W39); and Sym² T (E₆'s cubic with one 27 Higgs). It holds in every frame on record (the SM seat's W44),
    and its CKM bound rests on a sample-free block test.
  - **The weave's symmetry reduces none of the 13.** The leptons' mixing, beyond the 19, reduces to two parameters as
    TM1 under T̄ ⊗ T and as TM2 under T ⊗ T (in the frame where all of G is flavour), and not at all under Sym² T.
- **A modulus does not help (B1617, B1618).** The owner's tagged postulate τ = ω was tested. The residual symmetry at ω
  keeps T irreducible, and for every weight the masses are degenerate at ω and quasi-degenerate near it, in both the
  Dirac and the Majorana term. The postulate is retired as tested (GENESIS v1.35).
- **No dimensionful number.** The object supplies no scale (B811, B1012), so the Higgs mass and vev are free.
- **The gauge couplings.** The gauge three is a selection given Λ (B1606), and the hypercharge normalisation is not
  derivable (B991).
- **θ_QCD.** No arc fixes it. CP is the swap, allowed and not forced (B1611); that it leaves the strong phase free is a
  reading, not a computation.

**Why: the obstruction is one fact, Schur's lemma on an irreducible group.** The weave's group acts irreducibly on the
three generations, so a value that a coupling invariant under it fixes is degenerate. At a given τ only the parity
grading survives, and couplings in τ alone give permutation mixing (B1620). Distinct values need
the symmetry broken, and on the whole lattice of its breakings the breaking itself is free. **The values therefore need
a state that breaks the weave's symmetry chosen by a dynamics** — an energy on what the weave allows, or end data at the
cusp — **not further objects.** "Forced to choose, not forced which" is the record's phrase for it.

## 4. The one forced asymmetry outside the weave

The rule's own fixed-point word, 𝔣 = abaababa…, separates the three parity sectors 1 + 2 (B1620 B1–B3):

- it visits the four parity classes equally (density ¼ each), so it selects no sector by frequency;
- the clock's parity (−1)ⁿ, which counts letters without reading them, is bounded; it lives on T's (−, −) line;
- the two letter-reading parities are unbounded logarithmic walks, two records per factor φ⁶ (exact ratios 1 + 2/√5 and
  5 + 2√5), and one is the other inflated by φ.

The split is forced and elementary, since its content is A + B = n. Whether it is physical (TM1's special column, or a
third-generation distinction) needs a coupling that reads the word and not only τ. That is the open question this
report hands to reviewers alongside the derivations.

## 5. What we ask of a reviewer

1. Check the group: G of order 96 on T, its 68 subgroups, the abelian criterion (code: B1611, B1620).
2. Check the count: that no residual pair short of the full four reaches the CKM under each tensor, and that the block
   test plus fit decides reach (B1620 `post_seal_tensors.py`).
3. Check P10's derivation (B1612, B1613), and its scope under Sym² T.
4. Tell us whether "the weave's symmetry reduces none of the 13" is already known for this group, or for discrete flavour
   groups of this kind. The literature we found (King–Luhn 2013; Feruglio–Romanino 2021) reports no model that reduces
   the 13 by a definite number.
5. Is there a natural coupling that reads the rule's word (§4) rather than the modulus? Candidates on record: a
   thread's own H¹, which reads the word through its letter counts and breaks the grading only democratically (the SM
   seat's W42), and the means of the principle's clock and tick (B1621).

*Scope: the record's lifts of L and R, in the frame where all of the weave's group acts as flavour (B1620's); the frame
where c is gauge is computed in the SM seat's W44, and in W24's frame only c is flavour and nothing is constrained.
GENESIS FK11 (the frame) is open; where c is gauge, Sym² T gains invariants, TM1 returns under T ⊗ T, and never under
Sym² T (W43). The weave's own surface gives index 0 in its canonical reading (W45): a chiral three there is one unit of
end data at the cusp.*
