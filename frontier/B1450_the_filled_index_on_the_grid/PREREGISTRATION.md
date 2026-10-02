# B1450 PREREGISTRATION — THE FILLED INDEX ON THE GRID: the Gang–Yonekura formula applied to the 87 slopes of m004 on which the arithmeticity census was run

**Sealed 2026-10-02, before the formula is run on the grid. Seat: cc (main). Occasion: lead L225, question 1 —
"does the filled index separate the six arithmetic fillings from the rest?" — registered 2026-09-18 and never run.**

## 0. The quantifier (P0)

For every slope (p, q) with |p| ≤ 8, 1 ≤ q ≤ 8, gcd 1 — the 87 slopes of B1419's census, 78 hyperbolic and 9
exceptional — the q-series the formula below returns, to q¹⁰. The scope sentence names no slope.

## 1. What the source says, read before the seal (and a correction to the lead)

Celoria–Hodgson–Rubinstein, *The 3D index and Dehn filling*, arXiv:2509.09886, read from the PDF on this bench:

- eq. (32) and the compact form used in their Theorem 13.2: for a primitive α and a dual α\* (i(α, α\*) = 1),
  **I_{M(α)} = Σ_{k∈ℤ} (−1)^k [ q^{k/2}·I^{kα} − I^{2α\*+kα} ]**, with I^γ = 0 for γ outside the kernel of
  H₁(T; ℤ) → H₁(M; ℤ₂); for m004, I^{2xμ+yλ} = Σ_j I_Δ(j − x, j)·I_Δ(j + y, j − x + y) (their p. 55), which is B1428's
  verified boundary-class instrument.
- **Their Theorem 6.2 is proved for a manifold with at least two cusps, the filled manifold still cusped.** For a
  one-cusped manifold the filled manifold is closed and, in their words, "a rigorous definition of the 3D index of
  closed manifolds does not currently exist"; applying the formula there is "improper", supported by computation and
  stated as their Conjecture 14.1. **Lead L225 says this programme has "a proven transformation law for the 3D index
  under exactly that operation". For the grid of this lead — every filling closed — that is not what the source
  proves.** What is run here is the formula as a definition, on the same footing as the source's §13.

## 2. Instrument, control, reader

- `verification/filled_index.py` on B1428's `tet_index.py`: exact integer series in q^{1/2}; a term is included when
  its degree bound is within the truncation; a sum with unboundedly many such terms is returned as undefined.
- **Control (run before the seal, disclosed):** `control_published.py` — every figure-eight entry of the source's
  Tables 9 and 10 and the limit series below Table 9: (1,0) → 0; (0,1), (1,1), (2,1), (3,1) → 1; (4,1) undefined;
  (5,1) … (10,1), (1,2), (1,3), (1,4) and (40,1) against the limit series, to q¹⁰. **16 of 16 reproduced**
  (`control_run.txt`). One symbol of the printed (6,1) row ("t") is read as q^{1/2}.
- Reader `read_grid.py`, run twice on the thirteen grid slopes already seen (`control_index.json`), identical output
  (`reader_control.txt`).

## 3. What has been seen before the seal

The thirteen grid slopes of the control: (0,1), (1,1), (2,1), (3,1), (4,1), (±5,1), (6,1), (7,1), (8,1), (1,2),
(1,3), (1,4); and (9,1), (10,1), (1,0), (40,1) outside the grid. **On these the question of the lead is already
answered for the reader's six features:** (7,1), not arithmetic, and (8,1), arithmetic, both begin 1 − q², and no
feature takes disjoint values on the arithmetic and the other slopes (`reader_control.txt`). So P4 below is
recorded, not predicted. **Not seen:** the other 74 slopes.

## 4. Sealed predictions

| | prediction | prior |
|---|---|---|
| P1 | On all 78 hyperbolic slopes the sum is defined and is 1 + P(q), P ≠ 0 with positive exponents only. | 85% |
| P2 | On the nine exceptional slopes: 1 on (0,1), (±1,1), (±2,1), (±3,1); undefined on (±4,1). | 90% |
| P3 | All 43 mirror pairs (p, q), (−p, q) have identical series. | 95% |
| P4 | (decided on the control) None of the six features separates the six arithmetic slopes from the 72. | — |
| P5a | To q¹⁰ the series does not distinguish all 39 hyperbolic slopes with p > 0: at least two share one. | 70% |
| P5b | No arithmetic slope shares its series to q¹⁰ with a slope other than its mirror. | 90% |

## 5. What each outcome would mean (written before the data)

- P1 YES is 78 more instances of the source's Conjecture 14.1 on slopes it does not tabulate (it lists integer slopes
  and 1/n); a NO is a hyperbolic filling on which the formula fails, which the source would want to know.
- P4 as recorded: the filled index does not see arithmeticity through any simple feature; with P5b YES it still
  distinguishes the arithmetic fillings as manifolds. Neither is a statement about the Standard Model. 0 of 19.

## 6. Hashes at seal

See `ARTIFACT_HASHES.txt`.
