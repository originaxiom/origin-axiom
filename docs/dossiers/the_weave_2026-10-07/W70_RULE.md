# W70 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **The owner chose the cusp condensate** as the field's origin (the rulings page, after the reading of where the field
  comes from).
- **The audit lane's packets were read first** (repo first; `docs/RELAY_LEDGER.md` carries the lane's rows; the branch
  head read is bae2c38e6). They establish:
  - a stationary, finite-norm condensate at the cusp, the nilpotent root vector E_α with α = e₄ + e₆;
  - the condensate class is one per p-odd root, 112 of them, and the whole class shares one threshold histogram;
  - E_α keeps colour and breaks the old weak SU(2);
  - "58 of 112" counts lifted spectral channels, "NOT 58 massive particles".
- **What they do not establish.**
  - "No physical hypercharge is assigned" (the cusp packet).
  - The only global completion leaves G2 unbroken, with no U(1)_em (the global packet).
  - Generations and Yukawas are not addressed, and the mirror comparison was not carried out.
  - The lane names the duty itself: "the actual global gauge and charge map".
- **This arc does that charge map.** It asks whether any admissible hypercharge makes a cusp condensate the electroweak
  Higgs, and what such a hypercharge does to the three quaternion units.

## Weave or thread?

- **Weave-type.** It takes every one of the 112 condensate roots (none chosen), every admissible hypercharge (by a
  stated rule, none chosen), and the three quaternion units together.
- **The tags.**
  - Given the audit lane's registered E₈ embedding (`weave_registered_embedding_2026_10_13`), with colour the
    SU(3) factor, the weak SU(2) on e₃ − e₄, and the 6 of SU(6) read as ρ_Q ⊗ 3 in the field map's block order
    (b, a, ab).
  - Given Λ (GENESIS FK11).
  - **H-charge (new):** hypercharge lies in SU(6), as the commutant of colour × weak forces, and commutes with the
    weave's quaternion holonomies, so it is unbroken by the flat background.

## Seen before the rule (disclosed; by hand, from the audit lane's code and the seat's reading of it)

- **The conventions** (the lane's probes; 0-indexed eᵢ in ℝ⁸).
  - The SU(6) chain is e₆ − e₇, e₅ − e₆, e₆ + e₇, −½(1, …, 1), e₃ + e₄.
  - Colour is e₀ − e₁, e₁ − e₂, and the weak Cartan is e₃ − e₄.
  - The weights ws₀ … ws₅ of the 6 follow from the chain. The puncture's hq acts on them as (1, −1, 1, −1, 1, −1), so
    the blocks are (ws₀, ws₁), (ws₂, ws₃) and (ws₄, ws₅).
  - The condensate's α is the lane's `vector(3, 5, 1)`, that is e₃ + e₅ in 0-indexed coordinates (their "e₄ + e₆").
- **The admissible hypercharges.**
  - A Cartan element of SU(6) that commutes with each block's quaternion pair is scalar on each block:
    Y = (y₁, y₁, y₂, y₂, y₃, y₃) with y₁ + y₂ + y₃ = 0.
  - Requiring the five Standard Model fields with their charges among the 248's components gives five conditions:
    - Q (3, 2)_{1/6} in (6, 3, 2) needs some yᵢ = 1/6;
    - u^c (3̄, 1)_{−2/3} and d^c (3̄, 1)_{1/3} in (15, 3̄, 1) need pair sums −2/3 and 1/3;
    - L (1, 2)_{−1/2} in (20, 1, 2) needs a triple sum −1/2;
    - e^c (1, 1)_1 in (35, 1, 1) needs a difference of 1.
  - By hand these leave one solution up to permuting the blocks: (y₁, y₂, y₃) a permutation of (1/6, −5/6, 2/3).
- **So hypercharge tells the three quaternion units apart.** Under every admissible Y the three blocks carry 1/6, −5/6
  and 2/3: different charges. The weave's moves permute the three units, and Y breaks that permutation. In this
  embedding the three units of M cannot be three alike Standard Model generations. The generations must come from
  elsewhere, for example from the matter's own sections (W64, W65), not from the gauge embedding's 6.
- **The Higgs-like condensates.**
  - With the blocks at (1/6, −5/6, 2/3), the 20's weights with y-sum +½ are the two triples "both 2/3, one −5/6", and
    those with −½ are the two "both 1/6, one −5/6".
  - Each weight times a weak doublet gives two roots. Q = T₃ + Y vanishes on one of the two, so each admissible Y has
    **four neutral colour-singlet doublet roots.**
- **The published root.**
  - By the lane's chain, α = e₃ + e₅ has SU(6) weight ws₀ + ws₁ + ws₄ (Dynkin labels (0, 1, 0, −1, 1), from the digest
    of the lane's packet) and T₃ = +½.
  - Its Y is 2y₁ + y₃. That is −½, which makes α neutral, exactly when (y₁, y₃) = (1/6, −5/6), that is under the
    assignment (y₁, y₂, y₃) = (1/6, 2/3, −5/6).
  - **So the lane's own condensate is the neutral component of a Y = −½ doublet under exactly one admissible
    hypercharge, and charged under the other five.**
- **The local mirror.** The Weyl reflection s_α maps E_α to E_{−α} and H_α to −H_α. So the cusp-local condensate and its
  orientation reverse are gauge-equivalent locally. The lane's global mirror question stays with the lane.

## The method (fixed here)

- The 240 roots of E₈ in the lane's coordinates, exactly (sympy rationals). The branching is checked against the lane's
  `a5_roster` count: (35,1,1) + (1,8,1) + (1,1,3) + (20,1,2) + (6,3,2) + (6̄,3̄,2) + (15,3̄,1) + (15̄,3,1).
- **The admissible hypercharges:** every y = (y₁, y₂, y₃) with y₁ + y₂ + y₃ = 0 and each yᵢ ∈ {k/6 : |k| ≤ 12}
  (469 candidates), tested against the five field conditions on the actual roots.
- **The condensates:** for each admissible Y and each of the 112 p-odd roots:
  - colour (singlet when orthogonal to both colour roots);
  - T₃ = ½ r·(e₃ − e₄);
  - Y(r);
  - neutral when T₃ + Y = 0.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **N1, the branching** | The 240 roots plus 8 Cartans decompose as the lane's eight components, the 112 p-odd roots are exactly the weak doublets ((20,1,2), (6,3,2), (6̄,3̄,2): 40 + 36 + 36), and the 40 colour singlets among them are (20,1,2). | 97% |
| **N2, the admissible hypercharges** | Exactly six of the 469 candidates pass all five field conditions: the six permutations of (1/6, −5/6, 2/3). | 80% |
| **N3, the generations** | Under every admissible Y the three blocks (b, a, ab) carry three different hypercharges, so no admissible Y is invariant under permuting the three quaternion units. | 95% |
| **N4, the Higgs-like condensates** | For each admissible Y, exactly four of the 112 condensate roots are colour singlets with Q = T₃ + Y = 0 and \|Y\| = ½: two with Y = +½ and two with Y = −½. | 80% |
| **N5, the published root** | α = e₃ + e₅ (the lane's e₄ + e₆) is a colour-singlet weak-doublet root, and it is neutral (Y = −½, T₃ = +½) under exactly one admissible Y, the assignment (1/6, 2/3, −5/6) to the blocks (b, a, ab). It is charged under the other five. | 60% |

**The read-outs (no prior).**
- The full table of the 112 roots: colour, SU(6) weight, block content, and under each admissible Y the values of Y and
  Q.
- **The union over the six admissible Y:** how many distinct roots are ever neutral and Higgs-like.
- **For the published root,** under its neutral Y: which unbroken subgroup of the Standard Model it leaves. It should be
  SU(3)_c × U(1)_em, read off by which SM Cartan directions annihilate α.

## The reading, written before the run (predicted)

- **A cusp condensate can carry exactly the Higgs's quantum numbers.** For each admissible hypercharge, four of the 112
  are neutral colour-singlet doublets with |Y| = ½. The lane's own α is one of them under one admissible hypercharge:
  the neutral component of a Y = −½ doublet, the quantum numbers of H_d.
- **So the field's existence and charge can come from the weave's own end,** given the lane's embedding, H-charge and
  the stationarity the lane proved. This is the first place the record derives a field with the Higgs's quantum numbers
  rather than assuming one.
- **But the same hypercharge splits the three quaternion units.** In the gauge embedding, the three units cannot be
  three alike generations. The generations have to live in the matter's sections (W64–W69), not in the 6.
- **What stays open.**
  - The global completion that keeps U(1)_em (the lane's published one leaves G2), and the global mirror test: the
    lane's duties.
  - The Yukawas and the scale.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19. A derived Higgs charge is structural, not a
  number among the 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
