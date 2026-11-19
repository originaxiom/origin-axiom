# Card W-D2: two structures that could align frame C's cusp mixing: the shared doublet mode and the sector-odd singlet (P-860 (d); P-566). Data-free

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `card:` data-free. It was written at the author's word of
2026-11-19: both of the seat's options, the cheaper one first. This is the second option, after W-D1. The card is
committed before its script, and the script before its run. Nothing is compared, and no target is opened.

## 1. The question

- **The mixing.** High in the cusp, frame C's mixing is a permutation under the mixed Higgs readings (B1945 § 3b,
  B1946). P-860 (d) asks for a structure that aligns the two sectors' top rows. The level does not do it (B1945 § 3c),
  and neither does frame D1 (B1962).
- **The leptons.** On the act's line the lepton coupling is the down coupling transposed (B1934 § 3). So the leptons'
  ratios equal the down quarks' exactly, and P-862 says the split between them needs a change in the coupling.
- **Two structures named on P-860 (d) have not been computed in frame C:** D-1, a shared doublet mode, and D-2, P-566's
  sector-odd singlet.
- **For each, three questions:**
  - (a) Does it align the cusp mixing on the act's line?
  - (b) Where it aligns, does a heavy-pair hierarchy survive?
  - (c) Does it separate the leptons from the down quarks?

## 2. The definitions (fixed now)

- **D-1, the shared doublet mode.**
  - There are two Higgs doublets of opposite hypercharge: H_d for the down quarks and leptons, and H_u for the up
    quarks. Both carry one and the same fibre triplet, frame C's own S (B1964).
  - In frame C's terms every sector then reads S: the world (S, S, S).
  - With H_u carrying the up sector's charge, the hypercharge no longer forces the conjugation that frame C copied from
    the Standard Model (B1946's literature note).
  - **Its price:** a second doublet, and the choice that the two share one fibre mode.
  - **What is already on record:** B1946 finds (S, S) aligned at the column x = 0.13, heights 6 and 30 (PROVED), and
    W-F26 finds it at the mark and the twin.
  - **What is new here:** the rates of the off-diagonal moduli, J, three columns, and the typing.
- **D-2, the sector-odd singlet.**
  - A singlet is added to frame C's Higgs. The sector's Higgs matrix is R_sec(S) + σ_sec·s·1.
  - R_sec is the sector's reading in one of the two worlds the charge rule allows:
    - W₋: S̃ for the up quarks; S for the down quarks and the leptons;
    - W₊: S for the up quarks; S̃ for the down quarks and the leptons.
  - The reading acts on the triplet only. The singlet is added after it.
  - s = κ·e^(iφ)·|c_max|, where |c_max| is the largest modulus among the triplet's three components at that τ.
  - κ runs over 10^(k/2), k = −2⌈Im τ⌉, …, 2. φ runs over jπ/4, j = 0, …, 7.
  - **Odd:** σ_up = +1 and σ_down = σ_lep = −1, P-566's "odd between up and down".
  - **Even:** every σ = +1. This is a control: P-566 records that an even singlet does nothing for the corners.

## 3. What is computed

- **The points:** the mark (2/5, 4/5) and the twin (1/5, 2/5), on the act's line (B1943).
- **The heights:**
  - D-1: 6, 8, 10, 14, 20 and 30, at the columns x = 0, 0.13 and 1/4;
  - D-2: 10, 20 and 30, at x = 0.13.
- **The frame:** frame C as main's B1940 `frame_mp` computes it, at 30 + 2 Im τ digits, for the up, down and lepton
  sectors. That is:
  - B1906's closed-form residues, with exact zeros by rational characteristics;
  - B1919's norms, with Theorem 90's weight;
  - the canonical end, read from B1927's table;
  - the triplet, from the record's q-series.
  The script imports main's module and changes nothing in it. It adds the singlet, and the lepton sector by the same
  steps.
- **Read-outs per cell:**
  - each sector's ratios m₂/m₃ and m₁/m₃;
  - |V| = |U_uᴴ U_d|, with the singular vectors ordered light to heavy;
  - the class of |V|:
    - aligned: the least diagonal entry is at least 0.9;
    - deranged: the largest diagonal entry is at most 0.1;
    - partial: otherwise;
  - J = Im(V₁₂ V₂₃ V₁₃* V₂₂*), with the indices running light to heavy;
  - the lepton–down double ratios D₂ = (m₂/m₃)_lep / (m₂/m₃)_down and D₁ = (m₁/m₃)_lep / (m₁/m₃)_down.
- **For D-1:** the local rates of |V₁₂|, |V₂₃|, |V₁₃| and |J| between consecutive heights, in units of ε = e^(−π Im τ).
- **For D-2,** per point, world, parity and height:
  - the cells (κ, φ) that align;
  - among them, the least heavy-pair ratio, taking the larger of the up and down values in each cell;
  - the largest |ln D| over all cells;
  - the κ = 0 control.
- **Stability:** every D-1 cell at height 30, and the D-2 cells at height 30 with κ ≥ 1, are repeated at 20 more digits.

## 4. Controls and expectations (committed now)

| cell | prediction | prior |
|---|---|---|
| C1 | At κ = 0, W₋ and W₊ are deranged at both points and at every D-2 height (B1946; W-F26) | 90 % |
| C2 | Without the singlet, the leptons' ratios equal the down quarks' (\|ln D\| ≤ 1e-20) in both readings (B1934 § 3) | 95 % |
| C3 | (S, S) at x = 0.13 reproduces B1946's class, aligned, at heights 6 and 30 | 95 % |
| C4 | The repeats at 20 more digits change no class, and no \|V\| entry by more than 1e-15 | 90 % |
| X1 | D-1 is aligned at every height of 6 or more, at both points and every column | 85 % |
| X2 | Under D-1 every off-diagonal \|V_ij\| falls between heights 20 and 30, at a local rate above 0.1 | 75 % |
| X3 | Under D-1 the leptons stay tied to the down quarks (\|ln D\| ≤ 1e-20) | 95 % |
| X4 | Under D-2, every φ with κ ≥ 3 aligns, in both worlds and both parities | 70 % |
| X5 | Under D-2, no cell of either world is aligned with a heavy-pair ratio of at most 1e-2 in both up and down | 70 % |
| X6 | The odd singlet splits the leptons from the down quarks (\|ln D\| > 1e-6) at some cell. The even singlet does not, at any cell | 50 % |
| R | Read-outs, with no predictions: everything in § 3 | — |

The reason for X4: a Higgs dominated by the singlet reads the same in both sectors, up to a sign that |V| does not see.

## 5. What the outcomes mean (fixed now)

- **X1 and X2 hold.**
  - The shared doublet mode aligns the cusp mixing, with off-diagonal entries that fall with the height.
  - Its price is a second doublet and a shared fibre mode, a counted choice.
  - If X3 holds, the leptons stay tied, so the split between leptons and down quarks needs something else.
- **X1 fails.** (S, S) does not stay aligned where it is computed. The failing cells are named.
- **X4 and X5 hold.**
  - The singlet aligns the mixing only by dominating, and then the hierarchy goes.
  - B1968's dichotomy between alignment and hierarchy holds for this structure too.
- **X5 fails.**
  - A singlet aligns the mixing with a hierarchy, in a world the charge rule allows. The cells are named.
  - The singlet's size and phase then become the candidate's information budget, which P-566 asks for before any
    card.
- **X6.** It says, data-free, whether the singlet is a route to the split between leptons and down quarks.

## 6. What this card does not do

- It compares nothing and opens no target.
- It makes no claim about what in the object would make the singlet odd. P-566 lists three readings, and none is taken
  here.
- The singlet's value is free. A positive cell names a region, not a value.

0 of 19.
