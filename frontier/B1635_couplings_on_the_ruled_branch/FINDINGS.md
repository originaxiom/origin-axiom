# B1635 — THE COUPLINGS IN τ ALONE ON THE RULED BRANCH: the SM seat's W50 §3 verified on main by its own route (the dimensions by piece, its mixing distance 0.670933 exactly, non-permutation mixing at a generic τ), with two sealed cells failing — a threshold set too high, and "every coupling is degenerate at i", which is false: the lowest symmetric coupling at i has masses (1, 1/φ, 1/φ²); and the first count

**Verdict: NEGATIVE as sealed** (K1, K2, K4, K6 hold; K3 fails at its threshold; K5 fails in its clause (ii)). cc (main),
2026-10-09. Sealed `cf5f8dd08` before the run. No data. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /couplings in tau alone|vector-valued modular|ruled branch|free numbers|modular flavour/: 2 of 1406 arcs on main match (PROVED 2)`
— B1620, B1634; the SM seat's W50 (its N4, N5 and stored read-outs at i and ω, read before the seal). **Literature:** the
ring of modular forms of Γ(4); modular flavour symmetry (Feruglio 2017), for the shape of the count.

## 1. The sealed run (`couplings_on_the_ruled_branch.py`, unchanged)

The couplings are built as polynomial maps in u = (θ₂², θ₃², θ₄²) modulo θ₃⁴ = θ₂⁴ + θ₄⁴, equivariant under the weight-one
multiplier, with η¹⁸ cleared for T ⊗ T and the cusp condition imposed on exact q-series. The Borcherds–Skoruppa formula
runs beside them.

| cell | prediction | prior | result |
|---|---|---|---|
| **K1** | T ⊗ T dims = formula; D 0,0,1,1,2,2; O⁺ 1,1,2,2,3,3; O⁻ 0,1,1,2,2,3; laws hold, a random control fails | 85% | **HOLDS** — full dims 1, 2, 4, 5, 7, 8 = formula at every k; the pieces exactly the seat's; law errors ≤ 6·10⁻¹⁴; the random control 1.9 and 4.5 |
| **K2** | T̄ ⊗ T dims = formula; k = 0 the identity | 85% | **HOLDS** — 1, 2, 4, 5, 7, 8 at k = 0 … 10; k = 0 the identity |
| **K3** | D and O⁺ (k ≤ 7) and generic symmetric couplings non-degenerate at three generic τ (gap > 0.05); O⁻ always (s, s, 0) | 70% | **FAILS as sealed** — O⁻ (s, s, 0) everywhere, as stated; no coupling degenerate at a generic τ, but D at k = 5 (gap 0.046) and k = 7 (0.036), and one generic combination at each of k = 5, 7 (0.035, 0.028), fall under the sealed 0.05 at one of the three points |
| **K4** | (a) O⁺ k = 3 against D k = 5: 0.6709 ± 0.001; (c) D 5 against D 7: < 10⁻⁸ | 80% | **HOLDS** — 0.670933 (the seat's 0.670933054) and 0.0 |
| **K5** | (i) at ω every T ⊗ T coupling degenerate; (ii) at i every single piece degenerate; (iii) at i a generic k = 5 combination not | 60% | **FAILS in (ii)** — (i) holds (every one); (iii) holds (all five seeds); but at i, O⁺ at k = 1 has masses (1, 0.618033989, 0.381966011) and the O⁺ elements at k = 5 are non-degenerate |
| **K6** | d_sym 1,1,3,3,5,5; two sectors at k = 1, 3 leave 4; their masses distinct and their mixing not a permutation at generic τ | 55% | **HOLDS** — d_sym as predicted (d_full 1, 2, 4, 5, 7, 8; d_T̄T 1, 2, 4, 5, 7, 8); 2 + 1 + 1 = 4; mixing distances 0.54, 0.63, 0.56 |

## 2. Post seal (`post_seal_couplings.py`, written after the run; disclosed)

- **Q1 — the golden spectrum at i is exact.** O⁺ at k = 1 is one-dimensional, so it is canonical up to scale. At i its
  masses are (1, 1/φ, 1/φ²) to 1.1·10⁻¹⁶.
  - Its matrix there, normalized, is [[0, 1/√2, 1], [1/√2, 0, 1/√2], [1, 1/√2, 0]], with characteristic polynomial
    λ³ − 2λ − 1 = (λ + 1)(λ² − λ − 1).
  - That matrix comes from θ₂(i) = θ₄(i) and θ₃(i)² = √2·θ₂(i)².
- **Q2 — degeneracy at i depends on the weight.** Read basis-invariantly (a generic member, and the minimum gap over 400
  random members):
  - k = 1, 5, 9: O⁺ is non-degenerate at i;
  - k = 3, 7, 11: everything is degenerate at i;
  - D is degenerate at i at every k;
  - at ω every T ⊗ T piece is degenerate at every k.
- **Q3 — the sealed per-element readout is not basis-invariant for spaces of dimension ≥ 2.** The basis vectors an SVD
  returns are arbitrary. For T̄ ⊗ T the generic member is non-degenerate at the three generic τ, and each space also holds
  near-degenerate members (minimum gaps 0.012–0.052). K3 and K5 are graded on the one-dimensional pieces, which are
  canonical, and on generic members.
- **Q4 — read-out, not predicted.** O⁺ at k = 1 has masses (1, 0.618033989, 0.381966011) at all 13 sampled points of the
  tick's closed geodesic (the axis of LR, through i). Tested with controls in B1636.

## 3. What it says

- **The SM seat's W50 §3 is verified on main, with one sentence corrected.**
  - Its dimensions by piece hold exactly, and so does its mixing distance (0.670933).
  - Couplings in τ alone on the ruled branch give three distinct masses and non-permutation mixing at a generic τ.
  - Every coupling is degenerate at ω.
  - **"At i every coupling is degenerate" is false.** O⁺ at k ≡ 1 mod 4 is not, and its lowest member is golden.
- **The first count.** Given the sectors' weights, the flavour sector leaves 2 + Σ_s (2 d(k_s) − 1) free real numbers:
  τ, plus the coefficients modulo one phase per sector. At the lowest weights, two sectors leave 4 numbers. The weights,
  τ and the field dictionary are not fixed by the principle.

## 4. Disclosed

- Not blind: the seat's numbers were read before the seal.
- K3's 0.05 was a threshold chosen by me, not a physical bar. The couplings it caught are non-degenerate (gaps of 3–5%).
- The per-basis-element readout for spaces of dimension ≥ 2 was an instrument choice that is not basis-invariant (§2,
  Q3), so it was replaced post seal.

## 5. Files

`verification/couplings_on_the_ruled_branch.py` (sealed, unchanged) with `couplings_on_the_ruled_branch.json` and
`couplings_run.txt`; `verification/post_seal_couplings.py` with its json and run log; the lock
`tests/test_b1635_b1636_couplings_and_the_golden_spectrum.py`.
