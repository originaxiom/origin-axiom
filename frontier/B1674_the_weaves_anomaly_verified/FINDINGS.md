# B1674 — THE WEAVE'S ANOMALY, VERIFIED ON MAIN: the triplet's determinant character is χ_η⁹; if the moves act on the fermions as a symmetry they are free of the mixed anomaly with QCD exactly when they act on left- and right-handed quarks alike, never with SU(2), and with gravity only given ν^c; the couplings' determinants carry η^{6K} under a congruence, and the strong angle follows

**Verdict: PROVED (a verification arc).** cc (main), 2026-10-20. POINT_REGISTER P-197. 0 of 19.
- **What this arc re-banks.** The SM seat's W101, a WEAVE result. Its rule (12ffb5421) came before its script
  (ac37cbc8b), which came before its one run (b1f77ade9), recorded at d61faa0cc on the seat's branch. Main banks it
  under its own number so that the paper can cite it (draft 9, §4.1).
- **How it was verified.** One reading pass for main re-ran the seat's script and its post-hoc repair (both
  reproduce their outputs byte for byte). It then verified every claim with its own code, which derives ρ from the θ²
  triplet by a linear solve and does not import the seat's. Main checked the report and the logs.

## 0. Seen first

`VERDICT topic-sweep /anomal|determinant character|Dedekind counterterm|strong (CP|angle)|vectorial/: 48 of 1445 arcs on main match (NEGATIVE 5, OPEN 8, PROVED 35)`
— chiefly B1671 (det Y₁ = 8η⁶ and the phase law, the referee lane's arc) and B1635–B1637 (the couplings on the ruled
branch). **Literature:**
- the anomaly of modular symmetries and its cancellation by a moduli-dependent θ term in string compactifications
  (Dixon, Kaplunovsky and Louis 1991; Ibáñez and Lüst 1992);
- generalised CP in modular models (Novichkov, Penedo, Petcov and Titov 2019);
- the modular strong-CP models with reducible representations (Feruglio, Parriciatu, Strumia and Titov 2024; Penedo
  and Petcov 2024).

## 0b. Disclosed

- **One control failed as worded.** W101's control C1, the determinant character's sign on 30 words, failed on the 12
  words with ∣Re γτ∣ > 1. The cause was mpmath's principal branch of q^{1/4} in θ₂, as in B1634. A post-hoc repair
  summed θ₂ without a branch, and all 30 then agree to 10⁻²⁹. Main's own branch-free check passes on all 36 cases.
  A4, which needed C1, is not banked as stated.
- **The weight-3 interior zero curve was seen before W101's rule,** while reading the record. W101 restates it rather
  than predicting it.

## 1. What holds (main's independent code, `verification/main_check/`)

| claim | result |
|---|---|
| det ρ = χ_η⁹ | **holds.** The exponents on t are (1/8, 3/8, 7/8), so the determinant is 9/24 turns. The value on s agrees, and so do 200 random words. The image has order 96 |
| the moves' anomaly with SU(3) | **free exactly when s_u = s_d = −s_Q:** 16 of 64 assignments, the moves acting on left- and right-handed quarks by the same representation |
| with SU(2) | **never free:** n ∈ {6, 12, 18}. This binds only if the moves are gauged, since SU(2)'s angle is unphysical in the SM |
| with gravity | **given SU(3)-freedom, free exactly when s_e = s_ν = −s_L** (4 of 16); never without ν^c |
| det(Y_u Y_d) carries χ_η^m, m = −9(2s_Q + s_u + s_d); it is η^{6K} times a modular function iff 6K ≡ m (mod 24) | **holds:** K ≡ 2 (mod 4) with every quark in T; K ≡ 0 for the vectorial action; K ≡ 1 or 3 for the mixed assignments |
| det Y₁ = 8η⁶ | **holds** to 10⁻³¹ (also B1671) |
| with real coefficients and no counterterm, θ̄ − θ ≡ −12 arg η(τ) (mod π) | **holds:** π/2 exactly on Re τ = ½, and −π Re τ up to terms of order 12e^{−2π Im τ} |
| at weight 3 (all in T) and weight 2 (vectorial), each sector's determinant is a constant times η⁶E₆ and E₆; with the counterterm g ∝ E₆²/Δ = j − 1728 | **holds** (M₆ is spanned by E₆ alone) |
| without the counterterm at weight 3 the phase vanishes on an interior curve | **holds:** Re τ = 0.32415 at Im τ = 1 and 0.17212 at Im τ = 1.2; none for Im τ ≥ 1.3. The curve meets the imaginary axis near Im τ ≈ 1.25 |

## 2. What it says

- **A condition of consistency, not an identification.** If the moves are a symmetry of the fermions, they must act
  on left- and right-handed quarks alike. That constrains the dictionary without fixing a value, the way the SM's
  own hypercharges are fixed by anomaly cancellation.
- **The strong angle is tied to τ, not fixed.** θ̄ is one of the nineteen. With the counterterm it is a free constant
  θ₀. Without it, it is θ − π Re τ at large Im τ (B1671's sign convention is the opposite). 0 of 19.
- **Scope.** Tree level; the holomorphic ansatz on the ruled branch with real coefficients; the moves as a symmetry of
  the fermions, τ as a field and the counterterm are inputs (the paper's Table 1).

## 3. Files

- `verification/received/`: W101's rule, script, output and run, and the post-hoc repair, copied from the SM seat's
  branch at `ba48b718d`, with `SHA256_RECEIVED.txt`.
- `verification/main_check/`: main's independent scripts (`v1_independent.py`, `v4_curve.py`) and their runs, the
  re-run logs, and the reading pass's report.
- The lock: `tests/test_b1674_the_weaves_anomaly_verified.py`.
