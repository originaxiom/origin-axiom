# W-A1: the attack on selection and the dictionary. Under one counted postulate (D), the Weil representation's centre gives S(U(3) × U(2)) = (SU(3) × SU(2) × U(1))/ℤ₆ and one generation's hypercharges: SU(5)'s standard construction, on the Weil space. At τ = i, where the act's axis crosses the cone point of order 2, frame C's binaries of point and reading are settled: mark and twin agree, the axis's two crossings agree (a mirror symmetry of frame C), and S̃ = S (the Higgs triplet's third component vanishes there exactly). The end's convention still moves the outputs. What remains is counted below

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). It closes card W-A1
(`relays/cards/CHAT1_W-A1_the_attack_on_selection_and_the_dictionary.md`, b5117444c). It carries out the attack proposed
in this seat's view (`relays/CHAT1_VIEW_ON_SELECTION_AND_DICTIONARY.md`).

**Under the author's rulings of 2026-11-15:**
- the morning ruling: frame C's outputs may be computed and printed;
- the early-afternoon ruling: frame C may be evaluated at τ = i and near it on the act's axis.

Nothing in this note is compared with data. The look that followed is W-L1, a separate note under a later ruling.

**How it was checked.** Computed once; expectations committed first; tested against planted errors (2, both caught).
Recomputed independently by the referee:
- Part 1 on the referee's own code;
- Part 3's equalities, outputs and end sensitivity on main's frame code: B1724's frame, B1924's closed-form norm,
  B1932's Theorem-90 weight and B1691's triplet, with the same end tables, B1927's and B1667's.

**Provenance.**
- **The sealed scripts.** Part 1 (`wa1_weil.py`) and Part 3 (`wa1_tau_i.py`) were each sealed before their runs, and
  their outputs were committed before they were read.
- **Two post hocs** (`wa1_tau_i_posthoc1.py`, `wa1_tau_i_posthoc2.py`) were each committed before their runs, and are not
  blind.
  - The first followed an observation outside the expectations.
  - The second followed the referee of this seat's view, who found the axis's second crossing.

---

## Part 1. The dictionary from level 5's Weil representation

**The construction.** ρ is a Weil representation of SL(2, 𝔽₅) on ℂ⁵, the functions on 𝔽₅.
- Two candidates out of 32 are representations.
  - They are complex conjugates of each other and equivalent: one Weil representation, the one whose ρ(T) has exponents
    {0, 2, 3} (B1934's k = 2).
  - The other (k a residue, B1934's k = 1) needs a Fourier kernel ψ(mxy) with m = 2 or 3, outside this search. Its ρ(−I)
    is the same parity, so Part 1 holds for it unchanged (the referee).
- This part uses the first: ρ(T) = diag(ψ(2x²)) and ρ(S) = −F, with F_xy = ψ(xy)/√5 and ψ(x) = e^(2πix/5).

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

**Further checks by the referee:**
- the Frobenius–Schur indicator is +1 on the 3 (real) and −1 on the 2 (quaternionic);
- SU(3)³ also cancels;
- the 4 doublets are an even number, so there is no global SU(2) anomaly.

**What it means.**
- **[E] The 3 + 2 split is canonical.** It is the eigenspace decomposition of ρ(−I), the image of SL(2, 𝔽₅)'s centre.
  No choice of ours enters. It is B1934 § 1's split into even and odd functions, the same in both Weil
  representations.
- **[E] Given that split, the rest follows from group theory:**
  - hypercharge is, up to scale and sign, the only traceless operator commuting with the object's level-5 symmetry on ℂ⁵;
  - the unitary determinant-one maps of ℂ⁵ that preserve the split form S(U(3) × U(2)) = (SU(3) × SU(2) × U(1))/ℤ₆. That is
    the Standard Model's gauge group in its ℤ₆ global form: the largest quotient its matter allows, and the one SU(5)
    gives. Its matter does not fix which of the four quotients is realised;
  - Λ^even(ℂ⁵) carries one generation with SIXY's hypercharges, anomaly-free, and Λ¹'s doublet has the Higgs's.
  - This is the standard SU(5) ⊂ SO(10) construction (Λ^even(ℂ⁵) = 1 + 10 + 5̄, SO(10)'s 16), with the Weil space as ℂ⁵.
    B1936 § 1 places the frame's charges in the even half. Nothing here is new as group theory.
- **[J] The postulate it rests on, D.**
  - "The matter Hilbert space is the exterior algebra of the Weil space: its even half for matter, its odd half for the
    Higgs. The gauge group is the group of unitary symmetries of determinant one of the Weil space that commute with
    ρ(−I)."
  - Without determinant one the group is U(3) × U(2), with one U(1) more (charges 0, 2, 4 on Λ⁰, Λ², Λ⁴).
  - That is one postulate, of three clauses (the matter space, the Higgs space, the gauge group). It replaces the
    record's typed-in SIXY, the sector pairing and the gauge group.
  - It is a postulate, to be counted, and it may yet be derivable from GENESIS's ground (SE3: level 5).
- **[J] What it does not deliver:**
  - **three families.** One copy of Λ^even is one family.
  - **the continuous colour group from the finite one.** On the 3, ρ acts as A₅ in SO(3), which is real; colour's 3 is
    complex. The continuous group here is the centraliser of P, not a closure of ρ.
  - **the frame's use of the triplet.** Frame C uses its triplet index for the generations (B1934); this dictionary uses
    the Weil 3 as colour. The two cannot both stand, as W-V1 § 4.2 says.
  - **the Higgs alone.** Besides Λ¹'s doublet, the odd half holds Λ¹'s colour triplet (6Y = −2) and Λ³ + Λ⁵ (a conjugate
    generation). D7 uses the doublet only.

---

## Part 2. The choices audit

The open choices of frame C and of the foundation under it are sorted into three bins: **settled by equivalence** (a
symmetry maps one option to the other), **settled by consistency** (one option passes a test the object imposes), or
**counted**. The deciding test or source is named for each. The τ = i column says what Part 3 changes.

| choice | options | bin in general | at τ = i (Part 3) | source |
|---|---|---|---|---|
| the root's homology (SE1, S03) | torsion-free H₁ or not | counted (POSTULATED) | unchanged | GENESIS § 4 |
| orientation (SE2, S02) | m004 or m000 | counted (CHOSEN; a named condition to derive) | unchanged | GENESIS § 4 |
| the ground's level (SE3) | the tick at level 5 | counted (POSTULATED) | unchanged | GENESIS § 4 |
| a flat bundle on the fibre (S01) | | counted (ANSATZ) | unchanged | the scoreboard |
| the dictionary's charges, pairing and gauge group | typed in (SIXY, SECT) | counted, as now built | would be replaced by postulate D (Part 1), one counted entry | Part 1 |
| the reading point's line (C02) | the act's fixed line, or any | counted inside SE3: given that the ground is the act, the act fixes exactly one line up to sign (B1943's theorem), and C02 is typed CHOSEN on that premise | unchanged | B1943 |
| mark against twin | the two classes of that line | counted at the cusp | **equivalence**: S fixes i and exchanges them (I1) | W-F25; Part 3 |
| the axis's two crossings of the cone point | (i, mark) and (1 + i, mark) | counted, a priori | **equivalence**, see below | Part 3, post hoc 2; the referee |
| the Higgs world (C04: S or S̃ per sector) | W₋ and W₊ | counted (C04; B1941: the functional decides). Under postulate D, B1936 § 2's parity argument would fix it as W₋ at every τ, since D's grading is its premise | **equivalence**: at τ = i the triplet's third component vanishes, so S̃ = S at every point of order 5 (H1, H3) | B1941; B1936; Part 3, post hoc 1 |
| the Higgs direction: the covariant triplet (C03) | | counted (CHOSEN) | unchanged | the scoreboard |
| S* | excluded or kept | consistency: one-turn periodicity (W-F22; the rule's A7 and A14) | unchanged | W-F22 |
| the point τ (C01) | an average, the cusp, i, ω | counted (the measure, R6), or one scale (the cusp) | **one counted rule in place of the measure (C01)**, see below | W-F24; W-F25; W-V1 § 3.3 |
| the end (C05) | the canonical end and its horocycle | consistency (B1927: covariant; analyticity picks L₂), counted as one declared choice (A5, C05) | **material**: moving L₂ by ±0.3 at (i, mark) moves the ratios by up to 21 % and |V| by up to 0.02 (H4) | B1927; Part 3, post hoc 1 |
| the channel weight (C06) | truncated or exact; its form | the truncation settled by accuracy (B1932: Theorem 90's form matches the exact horoball norm to about 1e-5); the weight's form itself (C06) stays CHOSEN | unchanged | B1932 |
| the generations' metric H = I (C07) | | counted (CHOSEN) | unchanged | the scoreboard |
| one coupling for all sectors (C08) | | counted (CHOSEN) | unchanged | the scoreboard |
| the Higgs's point in D1 | c = ±1, ±2 | consistency excludes ±1; ±2 counted (a convention) | not used (frame C) | W-B2 |
| the scale at which the frame speaks (C09) | tree level at M_Z, or a unification point | counted (A6's open premise) | unchanged | the rule's A6; W-V1 § 4.2 |
| generations | quaternion units (B1724's BLOCKS) | counted (typed in); tied to isospin (W-F26) | unchanged | W-F26 |

**The two crossings.** The mirror τ ↦ −τ̄, (a, b) ↦ (a, −b), fixes i and takes the mark to (2/5, 1/5), which is
(1 + i, mark) by T.
- Frame C is covariant under it in every reading. The referee computed this once on main's code: at most 2.3e-14 at
  three values of τ and four lines, with the end held equal.
- Composed with T it is the reflection τ ↦ 1 − τ̄, which reverses the act's axis and keeps the mark.
- In S* the crossings differ (0.76).

**The point τ.** The rule is: read frame C where the act's axis meets the cone point of order 2. That happens at i and
at 1 + i in each period, and at no point of order 3.
- The rule was proposed after the look (W-V1).
- The axis names other points too, such as its apex (1 + i√5)/2, which the reflection exchanging the crossings fixes.

**[J] The count.**
- One joint of the scoreboard moves from counted to settled: the Higgs world's global bit (C04), by equivalence.
- The measure (C01) is not needed. But it is replaced by a counted rule, the point where the act's axis meets the cone
  point of order 2, proposed after the look.
- A point read-out brings back two binaries that the average removed (B1928): mark against twin, and the two crossings.
  Both are settled at τ = i by equivalence (I1; G1).
- The typed-in charges would become one counted postulate (D).
- **What is left:**
  - the foundation: S01, SE1 (S03), SE2 (S02), and SE3 with C02;
  - the read-out: the point rule, the end's convention (C05, which matters, H4) and the scale (C09);
  - the frame's inputs: postulate D, the Higgs direction (C03), the weight's form (C06), the generations' metric (C07),
    and one coupling for all sectors (C08);
  - the family structure.

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
| post hoc 1, H4 | the end: L₂ (2.72 at i) moved by −0.3 and +0.3 moves the ratios by up to 21 % and 16 %, and |V| by up to 0.020 and 0.017 |
| post hoc 2, G1 | **the axis's second crossing**, (1 + i, mark) = (i, (2/5, 1/5)), agrees with (i, mark) to 1.4e-14 (ratios) and 8e-16 (|V|). The prediction that they differ was wrong |
| post hoc 2, G2 | it is not the conjugate reading: (i, (2/5, 1/5)) in S* differs from (i, mark) in S by 3.2. The hypothesis was wrong; the referee's mirror covariance explains G1 (Part 2) |

**Why S̃ = S at τ = i.** At τ = i the Higgs triplet's components are (c, −c, 0): the third vanishes.
- This was first seen in a diagnostic run outside the sealed scripts. It is exact.
- Under S the triplet's first two components are exchanged (θ₂ ↔ θ₄), with weight −1/2. So its Serre derivative obeys
  a(−1/τ) = (−iτ)^(−1/2) τ² P a(τ), where P is that exchange (B1724's triplet representation, not Part 1's ρ).
- At τ = i the factor is −1, so a(i) = −P a(i). Hence a₃(i) = 0 and a₁(i) = −a₂(i).
- On the imaginary axis a₁ and a₂ are real, so S̃ = ε conj(S) εᵀ = conj(c₁)Q_I + conj(c₂)Q_J + conj(c₃)Q_K equals S.
- Recomputed independently by the referee: the law holds to 6e-42, and a₃(i) = 0 at 40 digits.

**The outputs at (i, mark)**, frame C's at the point the rule names:
- **The ratios σ₂/σ₁, σ₃/σ₁:**
  - up: 0.496836 and 0.0932603;
  - down and leptons: 0.904554 and 0.0154505.
- **|V| (every reading pair):** rows 0.9737 0.2024 0.105 | 0.1918 0.4784 0.8569 | 0.1233 0.8545 0.5047.
- **[J]** These are frame C's pointwise numbers:
  - no measure;
  - the mark and the twin, and the two crossings, agreeing;
  - no Higgs world chosen.
  The rule that picks τ = i was chosen after the look, and the end's convention is still in the numbers and moves them
  (H4).
- They are tested against data in W-L1, under its own rule, and fail there.

---

## What it means, together

- **[J] Selection.** A rule names a point: τ = i, where the act's own axis crosses the cone point of order 2. It does so
  at two crossings, which frame C's mirror symmetry makes agree. The rule is one counted choice, made after the look.
  - **What is settled there.** The one binary the record's frame C carried, the Higgs world's global bit (C04), is
    settled there by equivalence, since S̃ = S. Mark against twin and the two crossings, which a point read-out brings
    back, are settled there too.
  - **What is not.** The end's horocycle (C05).
  - **The price.** The point is in the bulk, so frame C's hierarchy there is modest (I3). The end's convention matters
    there (H4), so B1927's analyticity argument is now load-bearing and should be re-checked as such.
- **[J] The dictionary.**
  - **What D yields:** one counted postulate (D) yields S(U(3) × U(2)) (the ℤ₆ global form), one generation's
    hypercharges up to scale, the Higgs's charge on Λ¹'s doublet, and anomaly freedom. That is SU(5)'s standard
    construction on the Weil space.
  - **What is not delivered:** three families, the continuous colour group from the finite one, a family structure
    separate from isospin, and a Higgs sector that is only the doublet.
- **[J] What would show the attack has failed:**
  - postulate D cannot be tied to the frame's own couplings: frame C uses the triplet for families, D uses the Weil 3 for
    colour;
  - the outputs at (i, mark) do not survive the end's convention, or fail against data (W-L1: they fail);
  - the same pipeline gives the same structure on a rival root.

## Typed

| statement | how checked |
|---|---|
| D1 to D7 (the Weil representation's centre, commutant, hypercharge, gauge group, one generation, anomalies, the Higgs's charge) | computed once; expectations committed first; tested against planted errors (1, caught); recomputed independently (the referee). D5 to D7 are standard group theory once D3 holds |
| postulate D as the dictionary | a hypothesis (one counted entry, of three clauses) |
| at τ = i the mark and the twin agree | computed once; expectations committed first (I1); recomputed independently (the referee) |
| no forced zero; no large hierarchy at τ = i | computed once; expectations committed first (I2, I3); recomputed independently (the referee) |
| at τ = i, S̃ = S at every point of order 5 | computed once (post hoc 1, not blind; outside the sealed run's expectations); recomputed independently (the referee) |
| the axis's two crossings agree at τ = i | computed once (post hoc 2, not blind; the prediction that they differ was wrong); explained by frame C's mirror covariance (the referee, computed once) |
| the triplet's third component vanishes at τ = i | recomputed independently (the referee: forced by the triplet's S-law at τ = i; 0 at 40 digits and in main's q-series); first seen in a diagnostic run, not sealed |
| the end's convention moves the outputs at τ = i | computed once (post hoc 1, H4); recomputed independently (the referee) |
| the choices audit | a reading of the record's entries and this card's results |
| the outputs at (i, mark) | computed once; recomputed independently (the referee, every printed digit) |

## Files

`relays/chat1_2026-11-15_wa1/`: `wa1_weil.py` and `wa1_tau_i.py` (sealed), `wa1_tau_i_posthoc1.py` and
`wa1_tau_i_posthoc2.py`, `SCRIPT_SHA256.txt`, the four outputs and their warnings files (all four empty).

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes;
the read's corrections are applied in this version.

0 of 19.
