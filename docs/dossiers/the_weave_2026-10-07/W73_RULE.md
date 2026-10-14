# W73 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat worked by hand while
drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **W72 left one thing undefined.** In the surface frame the Yukawa Y_αβ = ⟨G_αβ, h⟩ is parameter-free and of rank 3,
  but the three chiral modes grow at the cusp. So their Petersson norms diverge, and Y's singular values are not
  masses.
- **No standard regularisation applies.** The regularised Petersson products of Borcherds and of Bruinier–Funke need
  the x-averaged integrand to grow at most polynomially. Here the principal parts' diagonal terms grow like
  |c|² e^{4π|E|y}.
- **One natural candidate remains: the end's own pairing.** Each mode's principal part is one unit on one eigenline
  of the cusp's monodromy, with coefficient 1 (W72's PH2). The cusp's Hermitian pairing of the eigenlines is
  B[l]·B̄[l] = 1, 2 and 2 for e_i, v₊ and v₋.
  - **H-end (new):** the modes' kinetic metric is this pairing of their units, K = diag(1, 2, 2) in the basis
    (F_i, F₊, F₋). It reads the units at the edge as the modes' normalisable data, the edge carrying the source.
- **This arc reads the masses H-end gives, and tests them.** The owner's order is "we look what fixes τ then we count
  free numbers". Here τ is gone, so if H-end held, the ratios would carry no free number.

## Weave or thread?

- **Weave-type,** as W72: the surface frame's modes and overlap, every τ integrated, none chosen.
- **The tags.**
  - Given Λ (GENESIS FK11) and B1644's coupling (P-108 owed).
  - The surface frame with GENESIS FK10's unit, H-surf (W72) and H-end (new).
  - One coupling for every sector: the up, down and lepton sectors share R, as B1649's premise has them in Λ's frame.

## Seen before the rule (disclosed; this matters here)

- **W72's read-out was read before this rule.** Its Y at Y₀ = 2.0 in the basis (F_i, F₊, F₋) is, to four figures:

  | | F_i | F₊ | F₋ |
  |---|---|---|---|
  | **F_i** | −71 780 | 62.07 | 18 954 |
  | **F₊** | 62.07 | −56.95 | −55.58 |
  | **F₋** | 18 954 | −55.58 | −2 030 |

- **By hand after that, the seat rescaled Y by K^{−½} on both sides.**
  - The singular values come to about 74 233, 1 438 and 29, so m₂/m₃ ≈ 0.019 and m₁/m₃ ≈ 4 × 10⁻⁴.
  - The seat then noticed that 0.019 is close to the down sector's m_s/m_b = 0.0187 (W66's data).
- **So H-end was chosen after Y was seen,** and the closeness to the down sector was noticed after the hand estimate.
  Neither is a prediction. The cells below are set with that known.
- **What is still unseen:** the exact values, the comparison under W66's predicate, and the look-elsewhere figure.
  - With one coupling for every sector, H-end gives all three sectors the same ratios and the CKM matrix 1.
  - Up and leptons differ from down by factors of 5 and 3 in m₂/m₃. So the frame, under H-end and one coupling, is
    expected to fail the data as a whole.

## The method (fixed here)

- **Y** from W72's stored output (`the_surface_yukawa.json`): the matrix at Y₀ = 2.0, and the matrix at Y₀ = 1.25
  rebuilt from the stored parts above and below Y₀ for each entry.
- **Ŷ = K^{−½} Y K^{−½}** with K = diag(1, 2, 2). Its singular values s₁ ≥ s₂ ≥ s₃ give m₂/m₃ = s₂/s₁ and
  m₁/m₃ = s₃/s₁. The same is read out for K = 𝟙 (W72's basis), as an alternative.
- **The data are W66's** (`the_parameter_free_census.py`: Huang and Zhou 2021 at M_Z; PDG for the CKM matrix).
  - For the three m₂/m₃: z = (log m₂/m₃ − log data)/√(δ² + a²), with a = 0.10. The verdict uses the sum of the three
    z² against 7.81 (3 degrees of freedom).
  - The CKM matrix under one coupling is 1, so |V_us| = |V_cb| = 0, which W66's predicate scores as infinite.
- **The first generation, read out only:** m₁/m₃ against m_u/m_t, m_d/m_b and m_e/m_τ from the same Huang–Zhou file.
- **The look-elsewhere figure.** There are 12 comparisons: 2 normalisations, 3 sectors and 2 ratios. Under a
  log-uniform prior on [10⁻⁶, 1] for each predicted ratio, the chance that at least one lands within the observed
  smallest |Δ log| of its datum is p = 1 − (1 − 2|Δ|/log 10⁶)¹². This is a stated, crude figure, not a test of the frame.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **Z1, the values** | The two settings' Ŷ agree to 10⁻⁸ relative. Under H-end, m₂/m₃ lies in [0.0185, 0.0205] and m₁/m₃ in [3 × 10⁻⁴, 5 × 10⁻⁴] (the hand estimate, ±5% and ±25%). | 85% |
| **Z2, the verdict on the data** | Under H-end with one coupling, W66's predicate on the three m₂/m₃ fails: χ² > 7.81, with \|z_up\| > 5 and \|z_lepton\| > 5. With the CKM matrix it fails outright (V = 1). | 95% |
| **Z3, the down sector** | \|z_down\| < 1: the post hoc closeness holds in the exact numbers. | 75% |
| **Z4, the look-elsewhere figure** | p > 5%: the down-sector closeness is not significant once the 12 comparisons are counted. | 85% |

**The read-outs (no prior).**
- All six ratios (two normalisations) against all six data ratios (three sectors, m₂/m₃ and m₁/m₃), with z where
  defined.
- Ŷ's singular vectors: how much of each generation lies on F_i, F₊ and F₋.

## The reading, written before the run (predicted)

- **The surface frame under H-end fails the data as a whole.** One coupling gives the three sectors one set of ratios
  and no mixing, and the sectors differ.
- **Its m₂/m₃ sits near the down sector's, but that is not evidence.** H-end was chosen after Y was seen, the
  closeness was noticed after, and once the look-elsewhere is counted it is not significant.
- **What would make it a test:** a prediction made before any data are read. If the hypercharge Wilson line (main's
  P-128) gives the three sectors different R, the surface frame under H-end predicts three different sets of ratios
  and a mixing matrix, from τ-free data. That needs main's twisted zero mode, sealed on main's side, and a rule here
  before any comparison.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
- **This arc is post hoc in its choice of H-end,** and is recorded as such wherever it is cited.
