# B1981 card — the canonical order-6 shell read on frame C at order 30

Written 2026-11-25, before any run, after B1979. Data-free. 0 of 19.

## Why

- **B1979.** At order 30 on the act's line, frame C's rates converge to 12 classes. No principle on record picks one
  (P-845).
- **agy-exp's claim card of 2026-11-24** (`CLAIM_2026-11-24_canonical_e6_prim_lepton_down_split.md`, 256f4294c):
  - the set E_τ[6]_prim of the 24 points of exact order 6 is preserved by all of GL(2, ℤ), so it needs no choice of
    coordinates;
  - its own construction averages over that set uniformly, with two doublets.
- **The web seat's CHK-2 (§ 0 item 6)** observed two things:
  - this set is exactly the set of the 24 values of the 6-part of B1976's points;
  - the uniform weight is an import.
- **The question.** Read frame C over the whole shell, not at one of its points. Does it pick a class, and does the weight
  do any work?

## The run

- **Blocks.** For each of the 4 nonzero points p₅ of the act's line ⟨(1/5, 2/5)⟩, take the 24 points p₅ + p₆ with p₆ in
  E_τ[6]_prim. These are B1976's 96 points, cut into 4 blocks. A fifth block is all 96 points.
- **Frame:** frame C, every sector reading S (B1945's `determinant_law.parts`), column 0.13, heights 30, 40 and 50.
  Each Y(p) is taken as the frame returns it, with no renormalisation.
- **Two declared readings of a block,** sector by sector:
  - **L (linear):** Y = Σ w_p Y(p). The masses are its singular values; U_L is from `cusp_mixing.U_of`, and
    V = U_L(up)† U_L(down).
  - **G (Gramian):** H = Σ w_p Y(p) Y(p)†. The masses are the square roots of its eigenvalues; U_L is its eigenvectors in
    ascending order, and V likewise.
- **Weights:**
  - uniform, w_p = 1 (the import);
  - three fixed positive alternatives, w_p = (1 + ((7i + 3k) mod 11)) / 6 for k = 1, 2, 3, with i the point's index
    in the block's sorted order.
- **Rates.** As in B1977, rate = −Δ ln x / (π Δy), read on 40–50; 30–40 is printed for convergence. The rates are for
  m₂/m₃ and m₁/m₃ in three sectors, and for |V₁₂|, |V₂₃|, |V₁₃|. The least diagonal is read at height 50.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| H1 | in each reading and block, every rate under each alternative weight equals the uniform one within 1e-3 (40–50) | L 0.7, G 0.8 |
| H2 | in reading L every sector has full rank in every block: every rate finite and below 3 | 0.6 |
| H3 | in each reading, every one of the 4 blocks' rates equals one of B1979's 12 classes within 1e-3 | 0.25 |
| H4 | in each reading the 4 blocks give the same rates within 1e-3 | 0.5 |
| H5 | in reading L, every block is aligned (least diagonal ≥ 0.9 at height 50), with m₂/m₃ rates ≥ 0.1 and m₁/m₃ rates ≥ 0.2 in both quark sectors | 0.5 |
| H6 | the lepton m₂/m₃ rate is 2/5 in both readings in every block | 0.6 |
| H7 | every rate of every reading and block is within 1e-3 of the grid of 1/60 | 0.75 |
| H8 | readings L and G give the same rates in every block, within 1e-3 | 0.35 |

## What each outcome means

- **H1 holds:** in the cusp limit the rates do not depend on the weight, so the uniform weight does no work on them. It
  could still act on order-one coefficients, which are not read here.
- **H3 and H4 hold, with one class:** the shell reading picks one class from B1979's menu. What then remains a choice is
  the reading, L or G, which is one declared bit unless H8 holds.
- **The rates are off the menu:** the shell reading is a new configuration, and it is reported as one.
- **Nothing here is compared with data,** and nothing derives level 30.
