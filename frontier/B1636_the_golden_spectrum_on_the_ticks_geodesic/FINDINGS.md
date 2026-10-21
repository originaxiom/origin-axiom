# B1636 — THE GOLDEN SPECTRUM ON THE TICK'S GEODESIC: on the principle's own closed geodesic the weave's lowest symmetric coupling has the τ-independent masses 1 : φ⁻¹ : φ⁻², and nowhere else and for no other coupling tested; the coupling is the three theta constants placed off-diagonal, its spectrum a function of F = Σ|θ_p/η|⁴ alone, and the golden level set F = 8 is, to 10⁻⁹, the union of the geodesics of discriminant 5

**Verdict: PROVED** (G1, G2, G4, G5 hold; G3 a read-out). cc (main), 2026-10-09. Sealed `6d3c2ee30` (14:26:56) before the
run (14:28:15). The seal's push was blocked by the doc-currency gate (LAW_MAP lagging) and went out after the run, with
the separate commit `6c148ddd4` that cleared it. No data. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /golden mass|mass ratio.*phi|phi.*mass ratio|1 : 1/phi|geometric hierarch/: 1 of 1407 arcs on main match (PROVED 1)`
(B963, a word match); `already_banked` found no golden mass spectrum. B1629, B1630, B1635 with its post-seal Q1–Q4 (read
before the seal). **Literature:** none located for a golden spectrum of a vector-valued modular form on a closed
geodesic; golden-ratio *mixing* (tan θ₁₂ = 1/φ) is a known pattern of A₅ flavour models.

## 1. The sealed run (`golden_on_the_ticks_geodesic.py`, unchanged; it imports B1635's sealed instrument)

| cell | prediction | prior | result |
|---|---|---|---|
| **G1** | O⁺ at k = 1 has masses (1, 1/φ, 1/φ²) within 10⁻¹⁰ at 66 points of the tick's geodesic and its LR-images | 90% | **HOLDS** — the largest deviation 3.2·10⁻¹⁵ |
| **G2** | m₁ = m₂ + m₃ for every O⁺ coupling (k = 1, 3, 5, 7) at 12 random τ, within 10⁻¹² | 97% | **HOLDS** — the worst 1.1·10⁻¹³ |
| **G3** | read-out | — | the entries' moduli vary along the geodesic, and track the theta ratios |
| **G4** | not constant along five other closed geodesics nor the three reflection lines | 60% | **HOLDS** — spreads of the middle mass: L²R 0.326, LR² 0.321, L²R² 0.120, L³R 0.368, LRLR² 0.254; Re τ = 0 0.356, \|τ\| = 1 0.118, Re τ = ½ 0.469 (the tick: 5·10⁻¹⁵) |
| **G5** | the other couplings not constant on the tick's geodesic | 65% | **HOLDS** — spreads 0.14–0.46 for O⁺ k = 3, D k = 5, D k = 7 and generic members of O⁺ k = 5, D ⊕ O⁺ k = 5, O⁺ k = 9 |

## 2. Post seal: the mechanism (`post_seal_golden.py`, written after the run; disclosed)

- **M1 — the coupling is the theta constants.** At eight random points the ratios Y₁₂/θ₄², Y₁₃/θ₃² and Y₂₃/θ₂² are one and
  the same constant (spread 2.9·10⁻¹³), and the diagonal vanishes. So
  Y(τ) ∝ [[0, θ₄², θ₃²], [θ₄², 0, θ₂²], [θ₃², θ₂², 0]]:
  each pair of generations is coupled by the theta constant of the third parity.
- **M2 — the spectrum is a function of one number.**
  - Rephasing makes Y real, with characteristic polynomial λ³ − Pλ − Q, where P = Σ_p |θ_p|⁴ and
    Q = 2|θ₂θ₃θ₄|² = 8|η|⁶ (Jacobi: θ₂θ₃θ₄ = 2η³).
  - So the normalized spectrum depends only on F = Σ_p |θ_p/η|⁴, which the run confirms (cubic against computed spectrum:
    3·10⁻¹⁴).
  - The golden polynomial λ³ − 2λ − 1 is F = 8.
  - F is 8 on the tick's geodesic (between 7.99999999999999 and 8.00000000000001) and at i. Its minimum is at ω, at
    3·4^{2/3} = 7.5595, where the spectrum is (1, ½, ½).
- **M3 — the golden locus is the discriminant-5 geodesics.**
  - On 41 vertical lines, 88 solutions of F = 8 with y ∈ [0.3, 3] were found by bisection. 84 lie within 10⁻⁹ of a
    geodesic a|τ|² + b Re τ + c = 0 with b² − 4ac = 5, the images of the tick's axis (class number one). The other 4 lie
    within 1.2·10⁻⁸, at the elliptic point (±1 + i)/2, where two such geodesics cross and the bisection meets a double
    zero.
  - Controls: discriminant 8 matches 0 of 88 points, and discriminant 12 matches 4 (the same crossing points).
  - **Conjecture (numerical, not proved): Σ_p |θ_p(τ)/η(τ)|⁴ = 8 exactly on the geodesics of discriminant 5.** In
    Weber's functions: |𝔣|⁸ + |𝔣₁|⁸ + |𝔣₂|⁸ = 8 there. Read through Jacobi's identity θ₃⁴ = θ₂⁴ + θ₄⁴ as a triangle in ℂ:
    the golden locus is where that triangle's perimeter cubed is 32 times the product of its sides.

## 3. What it says

- **The principle's tick fixes one coupling's mass ratios.** On the ruled branch the lowest symmetric coupling allowed by
  the weave is the three theta constants placed off-diagonal. On the tick's own closed geodesic (the unique lowest
  closed geodesic of the weave, B1629, through the tick's point i, B1630) its masses are 1 : φ⁻¹ : φ⁻², whatever the
  point on the geodesic. Off it they vary; no other closed geodesic tested and no other coupling tested is constant.
- **Every coupling of that off-diagonal kind obeys m₁ = m₂ + m₃** (a theorem: zero diagonal, rephased to positive entries,
  eigenvalues summing to zero with signs + − −).
- **The φ of the masses meets the φ of the tick through discriminant 5:** LR's eigenvalues are φ^{±2}, its axis has
  discriminant 5, and the golden level set of the coupling is exactly the discriminant-5 geodesics (to 10⁻⁹; a
  conjecture until proved).
- **Not decided here:** whether anything in the principle puts τ on the tick's geodesic (the seat's W51 functionals pick ω,
  where this coupling is degenerate); whether the identity is a theorem; what the eigenvectors are along the geodesic
  (at i, by hand, a 45° rotation and a rotation with tan θ = 1/φ, the golden-ratio mixing pattern); and whether other
  discriminants fix other couplings (a metallic family). No data compared: as a whole sector's masses the golden spectrum
  is flatter than the charged-fermion hierarchies, a qualitative remark, not a sealed comparison.

## 4. Disclosed

- Not blind: the golden spectrum at 13 points and at i was seen before the seal (B1635 Q1, Q4); the controls were not.
- The seal was pushed after the run (§0). The seal commit's time precedes the run's output file by 79 seconds.
- M3's search is a sample (41 lines, y ≤ 3), not a proof; the conjecture is stated as one.

## 5. Files

`verification/golden_on_the_ticks_geodesic.py` (sealed, unchanged) with `golden_on_the_ticks_geodesic.json` and
`golden_run.txt`; `verification/post_seal_golden.py` with its json and run log; the lock
`tests/test_b1635_b1636_couplings_and_the_golden_spectrum.py`.

## Seen late (2026-10-21, Review 66; P-123)

> *Seen late.* This arc's sweep, in its own words, missed older arcs on its subject (vocabulary drift; the topic sweep now expands aliases, R65-6). B424 (PROVED: Gate B's Hessian spectrum golden to the last term, with no Standard Model mass ratio within 2%), B8 (NEGATIVE: a golden near-miss killed), B751 (NEGATIVE: a golden identification with α_s not earned) and B752 (NEGATIVE: φ⁻ⁿ hits at base rate) — the record's earlier golden spectra and their negatives.
> They warn that a golden ratio in a spectrum is not by itself contact with the Standard Model; this arc's grading is read with them. No cell changes.
