# W-A1: the attack on selection and the dictionary. The Weil representation's centre gives the Standard Model's gauge group with its global form and every hypercharge. At τ = i, where the act's axis crosses the cone point, frame C has no binary left: mark and twin agree, the axis's two crossings agree, and S̃ = S at every point of order 5. What remains is counted below

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). It closes card W-A1
(`relays/cards/CHAT1_W-A1_the_attack_on_selection_and_the_dictionary.md`, b5117444c). It carries out the attack proposed
in this seat's view (`relays/CHAT1_VIEW_ON_SELECTION_AND_DICTIONARY.md`).

**Under the author's rulings of 2026-11-15:**
- the morning ruling: frame C's outputs may be computed and printed;
- the early-afternoon ruling: frame C may be evaluated at τ = i and near it on the act's axis.

Nothing is compared with data or with any value on record. The outputs below are printed and set beside nothing.

**How it was checked.** Computed once; expectations committed first; tested against planted errors (2, both caught).
- **Part 1** (`wa1_weil.py`): sealed before its run, with its output committed before it was read.
- **Part 3** (`wa1_tau_i.py`): sealed before its run, with its output committed before it was read.
- **Two post hocs** (`wa1_tau_i_posthoc1.py`, `wa1_tau_i_posthoc2.py`): each committed before its run, and not blind.
  The first followed an observation outside the expectations. The second followed the referee of this seat's view, who
  found the axis's second crossing.

---

## Part 1. The dictionary from level 5's Weil representation

**The construction.** ρ is the Weil representation of SL(2, 𝔽₅) on ℂ⁵, the functions on 𝔽₅. Two candidates out of 32
are representations: the two Weil representations. This part uses the first, ρ(T) = diag(ψ(2x²)) and ρ(S) = −F, with
F_xy = ψ(xy)/√5 and ψ(x) = e^(2πix/5).

| line | result |
|---|---|
| D1 | ρ is faithful (120 distinct matrices). ρ(−I) = ρ(S)² = P, the parity f(x) ↦ f(−x), with eigenvalues +1 ×3 and −1 ×2 |
| D2 | the two eigenspaces of P are irreducible (character norm 1.000000 each). **The commutant of ρ is 2-dimensional, spanned by I and P** |
| D3 | **the commutant's unique traceless element, scaled to 3 on the 2, is 6Y = (I − 5P)/2**: −2 on the 3, 3 on the 2 |
| D4 | **the centraliser of P in su(5) has real dimension 12** (8 + 3 + 1). exp(2πi·Y) = diag(ω̄, ω̄, ω̄, −1, −1), with determinant 1: the ℤ₆ by which SU(3) × SU(2) × U(1) is divided |
| D5 | on Λ^even(ℂ⁵) the (6Y; colour, weak) content is **exactly SIXY's one generation**: Q (1; 3, 2), u (−4; 3̄, 1), e (6; 1, 1), d (2; 3̄, 1), L (−3; 1, 2), and a neutral singlet (0; 1, 1) |
| D6 | over those 16 states, ΣY = ΣY³ = SU(3)²Y = SU(2)²Y = 0 |
| D7 | on Λ¹, 6Y is 3 on the doublet (SIXY's H) and −2 on the triplet |
| plant | with ρ(T)'s 1-dimensional eigenspace in place of P's 3 + 2, the content is not D5's. **Caught** |

**What it means.**
- **[E] The 3 + 2 split is canonical.** It is the eigenspace decomposition of ρ(−I), the image of SL(2, 𝔽₅)'s centre.
  No choice of ours enters.
- **[E] Given that split, the rest follows from group theory:**
  - hypercharge is the only traceless operator commuting with the object's level-5 symmetry on ℂ⁵;
  - the unitary determinant-one maps of ℂ⁵ that preserve the split form S(U(3) × U(2)) = (SU(3) × SU(2) × U(1))/ℤ₆, the
    Standard Model's gauge group with its global form;
  - Λ^even(ℂ⁵) carries one generation with SIXY's hypercharges, anomaly-free, and Λ¹'s doublet has the Higgs's.
- **[J] The postulate it rests on, D.**
  - "The matter Hilbert space is the exterior algebra of the Weil space, its even half for matter and its odd half for
    the Higgs. The gauge group is the group of unitary symmetries of the Weil space that commute with ρ(−I)."
  - That is one postulate in place of the record's typed-in SIXY, the sector pairing and the gauge group.
  - It is a postulate, to be counted, and it may yet be derivable from GENESIS's ground (SE3: level 5).
- **[J] What it does not deliver:**
  - **three families.** One copy of Λ^even is one family.
  - **the continuous colour group from the finite one.** On the 3, ρ acts as A₅ in SO(3), which is real; colour's 3 is
    complex. The continuous group here is the centraliser of P, not a closure of ρ.
  - **the frame's use of the triplet.** Frame C uses its triplet index for the generations (B1934); this dictionary uses
    the Weil 3 as colour. The two cannot both stand, as W-V1 § 4.2 says.

---

## Part 2. The choices audit

Every open choice of the record is sorted into one of three bins: **settled by equivalence** (a symmetry maps one option
to the other), **settled by consistency** (one option passes a test the object imposes), or **counted**. The deciding
test or source is named for each. The τ = i column says what Part 3 changes.

| choice | options | bin in general | at τ = i (Part 3) | source |
|---|---|---|---|---|
| the root's homology (SE1) | torsion-free H₁ or not | counted (POSTULATED) | unchanged | GENESIS § 4 |
| orientation (SE2) | m004 or m000 | counted (CHOSEN; a named condition to derive) | unchanged | GENESIS § 4 |
| the ground's level (SE3) | the tick at level 5 | counted (POSTULATED) | unchanged | GENESIS § 4 |
| the dictionary's charges, pairing and gauge group | typed in (SIXY, SECT) | counted, as now built | replaced by postulate D (Part 1), one counted entry | Part 1 |
| the reading point's line | the act's fixed line, or any | consistency: the act fixes one line up to sign | unchanged | B1943 |
| mark against twin | two classes of that line | counted at the cusp | **equivalence**: S fixes i and exchanges them (I1) | W-F25; Part 3 |
| the axis's two crossings of the cone point | (i, mark) and (1 + i, mark) | counted, a priori | **equivalent in outputs** (G1); the map that does it is not identified | Part 3, post hoc 2 |
| the Higgs world (S or S̃ per sector) | W₋ and W₊ | counted (B1941: the functional decides) | **equivalence**: at τ = i the triplet's third component vanishes, so S̃ = S at every point of order 5 (H1, H3) | B1941; Part 3, post hoc 1 |
| S* | excluded or kept | consistency: one-turn periodicity (W-F22; the rule's A7 and A14) | unchanged | W-F22 |
| the point τ | an average, the cusp, i, ω | counted (the measure, R6), or one scale (the cusp) | **i is named by the object**: the act's axis meets the cone point of order 2 there, and at no point of order 3 | W-F24; W-F25; W-V1 § 3.3 |
| the end | the canonical end and its horocycle | consistency (B1927: covariant; analyticity picks L₂), counted as one declared choice (A5, C05) | **material**: moving L₂ by ±0.3 at (i, mark) moves the ratios by up to 21 % and |V| by up to 0.02 (H4) | B1927; Part 3, post hoc 1 |
| the channel weight | truncated or exact | consistency (B1932: the exact horoball norm) | unchanged | B1932 |
| the Higgs's point in D1 | c = ±1, ±2 | consistency excludes ±1; ±2 counted (a convention) | not used (frame C) | W-B2 |
| the scale at which the frame speaks | tree level at M_Z, or a unification point | counted (A6's open premise) | unchanged | the rule's A6; W-V1 § 4.2 |
| generations | quaternion units (B1724's BLOCKS) | counted (typed in); tied to isospin (W-F26) | unchanged | W-F26 |

**[J] The count at τ = i.** Three entries move from counted to settled: mark against twin, the two crossings, and the
Higgs world. The typed-in dictionary becomes one counted postulate (D). The measure is not needed.

What is left: SE1, SE2, SE3, postulate D, the end's convention (which matters, H4), the scale, and the family
structure.

---

## Part 3. Frame C at τ = i

**The frame:** W-F24's (this seat's transcription; the canonical end; Theorem 90's weight; L₂; S and S̃), with W-F26's
mixing. The point z(s₀) on the act's axis comes out as i to 15 digits.

| line | result |
|---|---|
| I1 | **at τ = i the mark and the twin agree**: ratios to 2.4e-15, |V| to 1.2e-15 |
| I2 | no ratio is forced to 0 or 1: all lie strictly between 1e-8 and 1 − 1e-8 |
| I3 | every σ₃/σ₁ is above 1e-3: there is no large hierarchy at τ = i |
| I4 | on the axis near i (arclength ±0.05, ±0.1) the mark–twin difference is 0.41 to 2.2 in the ratios, so the equality is special to i |
| plant | (i, mark) against (i, (0, 3/5)) differs by 1.0 and 0.52. **Caught** |
| post hoc 1, H1 | **at (i, mark), S̃ gives exactly S's outputs, and all four reading pairs the same |V|** (difference 0.0) |
| post hoc 1, H2 | the controls differ by 0.17 to 0.72: τ = 1.3i, 0.05 + 0.9i, and the axis at s₀ ± 0.05. So S̃ = S is special to i |
| post hoc 1, H3 | at τ = i, S̃ = S at all 24 points of order 5 |
| post hoc 1, H4 | the end: L₂ moved by −0.3 and +0.3 moves the ratios by up to 21 % and 16 %, and |V| by up to 0.020 and 0.017 |
| post hoc 2, G1 | **the axis's second crossing**, (1 + i, mark) = (i, (2/5, 1/5)), agrees with (i, mark) to 1.4e-14 (ratios) and 8e-16 (|V|). The prediction that they differ was wrong |
| post hoc 2, G2 | it is not the conjugate reading: (i, (2/5, 1/5)) in S* differs from (i, mark) in S by 3.2. The hypothesis was wrong |

**Why S̃ = S at τ = i.** At τ = i the Higgs triplet's components are (c, −c, 0): the third vanishes, to 1e-19 at 40
digits. This was checked in a diagnostic run, outside the sealed scripts. With c real, S̃ = ε conj(S) εᵀ = conj(c₁)Q_I +
conj(c₂)Q_J + conj(c₃)Q_K equals S. [J] That the third component vanishes at S's fixed point is the triplet transforming
by ρ(S), with the value at i an eigenvector of it. This is a reading, not derived here.

**The outputs at (i, mark).** They are printed here, frame C's at a point the object names. They are compared with
nothing, as the ruling requires.
- **The ratios σ₂/σ₁, σ₃/σ₁:**
  - up: 0.496836 and 0.0932603;
  - down and leptons: 0.904554 and 0.0154505.
- **|V| (every reading pair):** rows 0.9737 0.2024 0.105 | 0.1918 0.4784 0.8569 | 0.1233 0.8545 0.5047.
- **[J]** These are frame C's numbers with no τ chosen, no measure, no reading point chosen and no Higgs world chosen.
  The end's convention is still in them, and moves them (H4).
- Whether they mean anything is main's to test, under a rule sealed before any comparison. The rule must count this
  card's fork after the look and the end's convention as declared.

---

## What it means, together

- **[J] Selection.** The object names a point: τ = i, where the act's own axis crosses the cone point of order 2, at its
  two crossings, which agree.
  - At that point every binary the record carried in frame C is settled by equivalence: the reading point, mark against
    twin; and the Higgs world, since S̃ = S.
  - The price is that the point is in the bulk, so frame C's hierarchy there is modest (I3).
  - And the end's convention matters there (H4). B1927's analyticity argument is now load-bearing, and should be
    re-checked as such.
- **[J] The dictionary.** One counted postulate D, that matter is Λ^even of the Weil space, yields the gauge group with
  its global form, every hypercharge and the Higgs's charge, with anomaly freedom.
  - What is not delivered: three families, the continuous colour group from the finite one, and a family structure
    separate from isospin.
- **[J] What would show the attack has failed:**
  - postulate D cannot be tied to the frame's own couplings; frame C uses the triplet for families, D uses the Weil 3
    for colour;
  - the outputs at (i, mark) do not survive the end's convention;
  - the same pipeline gives the same structure on a rival root.
  Each is a sealed test main can run.

## Typed

| statement | how checked |
|---|---|
| D1 to D7 (the Weil representation's centre, commutant, hypercharge, gauge group, one generation, anomalies, the Higgs's charge) | computed once; expectations committed first; tested against planted errors (1, caught). D5 to D7 are standard group theory once D3 holds |
| postulate D as the dictionary | a hypothesis (one counted entry) |
| at τ = i the mark and the twin agree | computed once; expectations committed first (I1) |
| no forced zero; no large hierarchy at τ = i | computed once; expectations committed first (I2, I3) |
| at τ = i, S̃ = S at every point of order 5 | computed once (post hoc 1, not blind; outside the sealed run's expectations) |
| the axis's two crossings agree at τ = i | computed once (post hoc 2, not blind; the prediction that they differ was wrong) |
| the triplet's third component vanishes at τ = i | computed once (a diagnostic run, not sealed) |
| the end's convention moves the outputs at τ = i | computed once (post hoc 1, H4) |
| the choices audit | a reading of the record's entries and this card's results |
| the outputs at (i, mark) | computed once; printed, compared with nothing |

## Files

`relays/chat1_2026-11-15_wa1/`: `wa1_weil.py` and `wa1_tau_i.py` (sealed), `wa1_tau_i_posthoc1.py` and
`wa1_tau_i_posthoc2.py`, `SCRIPT_SHA256.txt`, the four outputs and their warnings files (empty or path-redacted).

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes.
The read's corrections follow in a later commit.

0 of 19.
