# B1659 — THE JOINT LAW: in B1656's twisted frame the coupling's determinant and adjugate factor through the Higgs's and the matter's defects, exactly, for every Higgs and every matter: preregistration

cc (main), 2026-10-15. POINT_REGISTER P-168, after B1658 (whose T1 is this law on the matter's null cone).
- **The coupling** is B1658's Y(S, M) in B1656's twisted, quaternionic frame: S ∈ M₂(ℂ) the Higgs, M ∈ M₂(ℂ) a sector's
  matter, Y bilinear and 3 × 3.
- **J1, J2, J2b and J2c are identities over M₂(ℂ) × M₂(ℂ). J4(a)–(c) and (e) are identities evaluated at random draws;
  J4(d) is a test of first order.**
- **J3** evaluates the identities with random complex S on B1656's sector matter: the weave's fibre at τ = ω on W59's
  lines, given Λ, the dictionary and B1654's premises with B1656's four channels, under the canonical end condition P4.
  It is a frozen piece.
- **No data.** This arc compares with nothing measured. The census of the inverse map against the data's mass ratios is
  not here. It waits for a search shown reliable in the data's own regime (§0b).

0 of 19.

## 0. Seen first

`VERDICT topic-sweep /joint law|adjugate|det Y|antisymmetric pairing|two defects|product of (the|their) defects|tr\(eps/: 7 of 1430 arcs on main match (NEGATIVE 2, OPEN 2, PROVED 3)`
— the precedents B1644 (the multiplicity-space Higgs, the structure proved) and B1658 (the twisted half bound; its T1 is
J2 on the null cone). B1023, B1205, B1206, B1216 and B931 use the words in other senses. Also read:
- B1656;
- B1657 (the untwisted frame's two vacuum laws);
- B1658;
- the SM seat's W90, W93 (B1658 on its own code) and W94, and its relays §138 (the lepton residue is R̄(ω) on W59's
  lines, verified on main) and §139 (the arena);
- its identity Y(v; v)² = (v·v)²𝟙 in B1657's frame (verified on main, harvest row 1219).

**Literature:** the adjugate of a bilinear family of 3 × 3 matrices; the polar form of a quadratic form; Cayley–Hamilton
for the singular values (e₁, e₂, e₃ from ∣∣Y∣∣², ∣∣adj Y∣∣², ∣det Y∣²).

## 0b. Disclosed

- **Main's exploration** (kept beside the seal, `verification/before_the_seal/`):
  - `joint_law.py` (B1658's), which found adj Y = det S·A(M) + det M·Ã(S) to first order;
  - `joint_exact.py`, numerical: the mirror of B1658's T1 on null S; det Y/(det S det M) bilinear; the decomposition
    exact;
  - `joint_symbolic.py`, sympy: both laws exact, with A and Ã read off;
  - `identity_on_matter.py`: both laws on B1656's sector matter.
- **Two readings withdrawn before the seal.**
  - Main's notes first wrote that the joint law "unifies B1657's two vacua".
  - They then wrote that the frames *differ*: the coupling "not symmetric in Higgs and matter", ℓ an "antisymmetric
    pairing", and "Higgs = matter gives a massless first generation here, geometric masses in B1657's frame". This went
    to the owner the same evening.
  - **The first reviewer showed this is an artefact of labelling** (blocker B1). Main verified it. With the matter
    labelled N = Mε (det N = det M), the coupling is symmetric in (S, N), and ℓ is −4 times the polar form of the
    determinant: the same form as B1657's (a·a)(v·v)(a·v). At the coincident point N = S the masses are exactly
    geometric, as in B1657's frame.
  - The point S = M of the old labelling is only a zero of polar(S, Sε).
  - A "not a linear image of B1657's Y" fit (residual 0.86) used the unrelabelled matter and is withdrawn. Whether the
    two frames are related by a linear map is not claimed either way.
  - J2c and J4(e) record the corrected statements.
- **A draft run of this instrument** in the audit room, in which every cell held. Its numbers are not written here.
- **The census attempts** (not part of this arc). Five scripts fitted one Higgs (and the up quarks on S̃ or S̄) under P4
  on W59's lines to the data's five non-electron ratios. Their optimisers disagreed (Nelder–Mead 86–89, trust region
  131–154, differential evolution 88–596 on the same line), so no census number is claimed. A reliable search, with
  planted controls in the data's hierarchy regime, comes first.
- **Reviewing agents before the seal:** §5.

## 1. The setting, and what follows by hand (motivation; the symbolic cells are the proof)

- **The coupling.** Y(S, M)_ab = Σ (C_aᵀ ε S C_b) ⊙ M, with C = (j, i, k) (B1644's blocks) and ε = j. It is B1656's
  `coupling`, loaded unchanged.
- **The determinant (motivation).**
  - det Y vanishes when det M = 0 (B1658: rank ≤ 2 on the null cone).
  - By the mirror statement it also vanishes when det S = 0. That statement is main's exploration, `joint_exact.py`,
    not B1658's T1.
  - Being of bidegree (3, 3), det Y is therefore det S·det M·ℓ(S, M) with ℓ bilinear (det is irreducible on M₂(ℂ)).
  - The claim (J1) is ℓ = 4 tr(εSMᵀ). In the variable N = Mε this is ℓ = −4 polar(S, N), with
    polar(S, N) = det(S + N) − det S − det N (J2c).
- **The adjugate (motivation).**
  - adj Y is of bidegree (2, 2), and on the null cone of M it is det S·A(M) (B1658's T1).
  - If it also factors on the null cone of S, its remainder is divisible by det S·det M. That remainder is a constant
    matrix C, absorbed as A ↦ A + C·det M, so A is fixed by the symbolic check.
  - The claim (J2) is adj Y = det S·A(M) + det M·Ã(S), with Ã = P A and P = diag(1, −1, −1). Here M = [[m₀, m₁], [m₂, m₃]]
    and:

    A(M) = [[m₀² + m₁² + m₂² + m₃², 2i(m₀m₂ + m₁m₃), −i(m₀² + m₁² − m₂² − m₃²)],
            [2i(m₀m₁ + m₂m₃), −4m₁m₂, 2(m₀m₁ − m₂m₃)],
            [−i(m₀² − m₁² + m₂² − m₃²), 2(m₀m₂ − m₁m₃), −m₀² + m₁² + m₂² − m₃²]]
  - On null M = pqᵀ, A(M) = q̃p̃ᵀ with p̃ = (p₀² + p₁², 2ip₀p₁, −i(p₀² − p₁²)), and q̃ the same in q.
- **The spectrum.**
  - For any 3 × 3 matrix, the squared singular values are the roots of x³ − e₁x² + e₂x − e₃, with e₁ = ∣∣Y∣∣²,
    e₂ = ∣∣adj Y∣∣² and e₃ = ∣det Y∣².
  - With J1 and J2: e₂ = ∣∣det S·A(M) + det M·Ã(S)∣∣², and e₃ = 16∣det S det M tr(εSMᵀ)∣².
  - Exactly, when m₂m₃ ≠ 0 (rank Y ≥ 2), m₁ = ∣det Y∣/(m₂m₃): the product of the two defects and the pairing, over the
    other two masses.
  - In the hierarchical limit (m₁ ≪ m₂ ≪ m₃), m₂ ≈ √e₂/m₃. The middle mass reads the sum of the two defects' terms,
    with interference.

## 2. The cells (the instrument `verification/the_joint_law.py`; one run; JSON after every cell)

| cell | prediction | identity or test |
|---|---|---|
| **J1**, the determinant law | sympy: det Y − 4 det S det M tr(εSMᵀ) expands to 0 over eight complex symbols | identity |
| **J2**, the adjugate law | sympy: adj Y − det S·A(M) − det M·P A(S) expands to the zero matrix | identity |
| **J2b**, on the null cone | sympy: A(pqᵀ) = q̃p̃ᵀ exactly, and the transposed form p̃q̃ᵀ is not. Numerically, at 200 random null M and complex S, adj Y = det S·A(M) to 10⁻¹² and ∣∣A(M)∣∣ = 2∣∣M∣∣² to 10⁻¹² (B1658's T1) | identity |
| **J2c**, the symmetric form | sympy: with M = Nε⁻¹, Y(S, Nε⁻¹) = Y(N, Sε⁻¹); tr(εSMᵀ) + polar(S, N) = 0; det(Nε⁻¹) = det N | identity |
| **J3**, on the sector matter | B1656's residues and channel norms on W59's 18 lines at ω, three sectors, P4 with L ∈ {5, 50, 500}. Each case pairs this matter with two random complex S (324 cases, every value asserted finite). The leptons' matter is null to about 10⁻¹⁴ (B1656's zero), so J1 and J2's det M term are tested non-trivially only on the up and down quarks J1 holds within 10⁻¹³ of ∣∣Y∣∣³ and J2 within 10⁻¹³ of ∣∣Y∣∣². The roots of x³ − e₁x² + e₂x − e₃ equal the squared singular values within 10⁻¹⁰ of σ₁². The leptons' ∣det M∣/∣∣M∣∣² is recorded | identity, evaluated |
| **J4**, the corollaries | at 40 random complex draws: (a) null M gives m₁/m₃ < 10⁻¹²; (b) null S gives the same; (c) S = M exactly (non-null) gives m₁/m₃ < 10⁻¹², the zero of polar(S, Sε); (e) at the coincident point N = S (M = Sε⁻¹) the masses are geometric, ∣m₁m₃/m₂² − 1∣ < 10⁻¹⁰; (d) on 10 cases S = S₀ + eX, M = M₀ + eZ with null S₀, M₀, from e = 10⁻⁴ to 10⁻⁵ both m₂/m₃ and m₁/m₃ fall by a decade (slopes within 0.1 of 1). Sanity floors, not tests: the draws' defects > 10⁻³ and generic m₁/m₃ > 10⁻⁴ | (a), (b), (c), (e) identities; (d) a test of first order |
| **J5**, controls that can fail | (a) the coupling plus a generic perturbation of 10% violates J1 by more than 10⁻⁵ of ∣∣Y∣∣³; (b) A(S) in place of P A(S) violates J2 by more than 10⁻³ of ∣∣Y∣∣²; (c) N ≠ S departs from the geometric law (median > 0.05); (d) a check: B1657's untwisted Y(a, v) = avᵀ + vaᵀ − (a·v)𝟙 has det = (a·a)(v·v)(a·v) (its proved law) to 10⁻¹², the form J2c gives here | (a)–(c) tests of the identities' specificity; (d) a check |

## 3. What it would mean

- **The joint law,** if every cell holds. In B1656's twisted frame, the coupling's spectrum is fixed in closed form by
  four quantities:
  - the Higgs's defect, det S;
  - the matter's defect, det M;
  - their pairing, tr(εSMᵀ) = −polar(S, Mε);
  - the quadratic A.

  The lightest mass is non-zero if and only if both defects are non-zero and tr(εSMᵀ) ≠ 0 (m₁ = 0 iff det Y = 0).
- **Restrictions to known cases.** B1658's T1 is the law's restriction to the null cone. B1656's electron zero is J4(a)
  applied to the leptons' matter, whose det M is recorded in J3.
- **The same shape as B1657's frame.** In the variable N = Mε the coupling is symmetric in Higgs and matter, and its
  determinant has the shape of B1657's (a·a)(v·v)(a·v): defect × defect × pairing. At the coincident point the masses
  are geometric (m₁m₃ = m₂², J4(e)), as they are in B1657's frame at Y(v; v). There the SM seat's identity
  Y(v; v)² = (v·v)²𝟙 holds; here Z(S, S)² is not proportional to 𝟙, so the geometric law is a separate statement. Whether
  the two frames are linearly equivalent is not claimed.

## 4. What it does not show

- Any value, or any comparison with data: the census waits (§0b).
- Which Higgs or which matter: the defects are free here.
- The first generation's size against nature.
- The interacting weave: one τ, the fibre frame, a frozen piece. The SM seat's §139 places ω on the arena's singular
  fibre.
- Which frame is the physical one.

## 5. Reviewing agents before the seal, and files

- **The first pass** (a read-only reviewing agent; its scripts kept in `verification/before_the_seal/review1/`).
  - J1, J2 and A = q̃p̃ᵀ reproduce independently, and every control has margin.
  - **B1, the blocker:** the "frames differ" and "antisymmetric pairing" claims are labelling artefacts. Taken: J2c and
    J4(e) were added, and §0b, §3 and J5 rewritten.
  - **B2:** this section was empty. Taken.
  - **S1–S10, taken:**
    - the hierarchical limit for m₂ stated;
    - "aligned" replaced by tr(εSMᵀ) ≠ 0;
    - J4(c) stated for S = M exactly;
    - J2b tests A = q̃p̃ᵀ exactly;
    - J4(d)'s 10 cases stated, and the sanity floors labelled;
    - finiteness asserted in J3, which pairs random S with the sector matter;
    - the preamble's cell classes corrected;
    - §1 labelled motivation, with the mirror statement attributed to main's exploration;
    - the leptons' det M recorded;
    - "geometric" used only for the coincident point, which J4(e) tests.
- **The second pass** (a read-only reviewing agent; its scripts kept in `verification/before_the_seal/review2/`).
  - Every first-review fix confirmed in both files. The J2c convention (M = Nε⁻¹) is the same in the sympy and the
    numeric cells. No blocker on the mathematics.
  - **Taken:**
    - J4(d) and J5(a) were fragile across 300 other seeds (worst slope deviation 0.089 against 0.02 at e = 10⁻³; J5(a)
      down to 9.9 × 10⁻⁵ against 10⁻⁴). J4(d) now uses e = 10⁻⁴ and 10⁻⁵ within 0.1, and J5(a) 10⁻⁵.
    - The geometric-mass sentence no longer identifies the twisted frame's law with the SM seat's Y² = (v·v)²𝟙.
    - The instrument's "antisymmetric pairing" wording removed.
    - The run log written by the instrument.
    - m₁ = ∣det Y∣/(m₂m₃) qualified for rank ≥ 2, and the §3 claim made "if and only if".
    - The leptons' vacuous share of J3 stated.
    - J5(a) no longer called "symmetric".
  - **Noted:** J1, J2, J2b and J2c are polynomial identities. The cells that can fail are J4(d) and J5(a)–(c).
- **Files:**
  - `verification/the_joint_law.py` (the instrument), with `.json` and `_run.txt` after the run;
  - `verification/before_the_seal/` (the exploration listed in §0b, and the reviewing agents' scripts).
