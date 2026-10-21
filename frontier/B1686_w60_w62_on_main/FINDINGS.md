# B1686 — W60 AND W62 ON MAIN (P-222): THE LINE GOES TO A HALF-PERIOD, AND THE STATE IT SELECTS IS NOT STATIONARY IN τ — EVERY CONTENT ON RECORD RUNS TO A CUSP

**Verdict: PROVED (a verification arc).** cc (main), 2026-10-21. POINT_REGISTER P-222 (after B1684, W59 on main, at the
owner's approval of 2026-10-21). 0 of 19.
- **What is verified.** The SM seat's W60 (the quark sector with a Wilson line; rule 560c86dff, one run 752ce95ff, post
  hoc cf6cd4d8a) and W62 (what holds τ at the selected state; rule 90272b45b, one run b5810d240), by main's own code
  written from the two rules and the seat's recorded read-outs, not its scripts. Main's lattice is its own (one builder
  for both: the six-point Laplacian of the rules, the quaternion local system ρ_Q, the puncture's −1 as a half flux; the
  crossing convention fixed by the plaquette check, exactly one triangle at −1, the puncture's).
- **W60, every cell reproduced.** The quarks resist the colour-centre line; the content's net six-dimensional term has its
  global minimum on the three half-period lines, −147.64, where the matter sees nothing (a half-period line is no line
  for ρ_Q) and one parity copy of the Higgs is untwisted.
- **W62, every cell reproduced: the closed-form cells exactly, the lattice cells to 7 × 10⁻¹⁰ on all seventeen members at both sizes.** At the half-period line the Higgs's
  copies keep only the theta group, the selected state is not stationary in τ (the copies' term at ω is −1.553 with
  gradient (−7.52, −4.34), falling to −3.785 at i), and every content on record has a positive cusp coefficient, so it
  runs to a cusp.
- **So the state B1684 called an input moves, as the seat said:** W59's τ = ω and eighteen lines are not the potential's
  state; the line goes to a half-period, and then τ is not held anywhere the computed sectors can hold it. The arcs on
  W59's lines (B1653, B1656, B1660, B1673) stand as conditionals (P-214).
- **One observation of main's own (not a claim of the seat's).** On W60's grid the matter's six-dimensional line
  dependence has the periodic part's shape (correlation 0.9992) but a fifth of its size: at (⅙, ⅙) the diffraction at the
  puncture cancels 79% of the periodic part (fermion term 0.515 against 2.459 at N = 96).

## 0. Seen first

`VERDICT topic-sweep /W60|W62|quark sector|Wilson line|half-period line|theta group|runs to (a|the) cusp|diffraction/ (full
text): 31 of 1457 arcs on main match (NEGATIVE 5, OPEN 1, PROVED 25)` — chiefly B1684 (W59 on main), B1653, B1656, B1660,
B1673 (the arcs on W59's lines), B1654 and B1667 (the cusp law and the canonical cusp), B1657 (the symmetric point).
**Literature:** the heat-kernel definition of the twisted determinant and the six-dimensional Casimir term; Kronecker's
second limit formula; Chowla–Selberg for E(τ, s); the theta group Γ_θ and its elliptic point i.

## 1. W60 (`verification/main_w60.py` → `main_w60.json`; spectra cached at K = 150)

| cell | the seat's record | main |
|---|---|---|
| lattice, N = 96, lowest eigenvalues at φ = 0 (W60 units) | 7.769432369, 29.680538204 | the same to the solver's precision |
| P1, abelian control | Δ log det to 2.6 × 10⁻¹⁰; ΔV₆ to 1.4 × 10⁻⁴ (N = 192), 5.5 × 10⁻⁴ (N = 96); (½, 0) a 0/0; PH1: largest absolute error 0.0043 | 2.6 × 10⁻¹⁰; 1.2–1.4 × 10⁻⁴ and 5.0–5.5 × 10⁻⁴; the same 0/0; 0.00427 |
| P2, symmetries | 4 × 10⁻¹⁴ in spectra, 3 × 10⁻¹¹ in potentials | 1.0 × 10⁻¹⁴ and 4.5 × 10⁻¹², directly at N = 96 on three generic φ; exact on small tori |
| P3, fermion 2d term, N = 192 | 0.0255982 at (⅙, ⅙), 0.0226978 at the quarter points | 0.025598, 0.022698 |
| P4, fermion 6d term, N = 192 | 0.5124173 at (⅙, ⅙), 0.4553173 at the quarter points; no grid point below φ = 0 | 0.512417, 0.455317; the grid's minimum at φ = 0 |
| convergence, lowest ten, N = 96 → 192 | 0.02% to 0.27% | 0.015% to 0.267% |
| net term (quarks −2 per state, Higgs +2 per parity sector), N = 192 | +36.9 at w₀; −126.5, −125.5 at the Higgs's lines; minimum −147.6 on the 2-torsion lines | +36.89; −126.54, −125.47; −147.64 on all three, below every point of a 180 × 180 grid of lines |

## 2. W62 (`verification/main_w62.py` → `main_w62_closed.json`, `main_w62.json`)

**The family.** The index-8400 sublattices of the triangular lattice with shapes on the imaginary axis (1 < y ≤ 2.1) or the
unit arc (0 < x < ½), the first in Hermite order for each shape, by exact Gram reduction: 11 on the axis (y = 1.031 to
2.021), 6 on the arc, and the two hexagonal sublattices — the seat's family.

**The closed-form cells.**

| cell | the seat's record | main |
|---|---|---|
| A1, the copies' identity and the theta group | to 2.5 × 10⁻¹²; S and T² to 10⁻¹⁵; T changes it except at ω, where ω + 1 is ω's mirror (failed as worded, PH1) | to the truncation (10⁻⁸ of E against the exact E); S and T² to 10⁻¹²; T changes it by 1.27, 1.80, 0.077, 3.06 and by 0 at ω, where it equals the mirror to 10⁻¹⁶ |
| A2, not stationary | −1.553 at ω, gradient (−7.52, −4.34), falling to −3.785 at i | −1.5530, (−7.518, −4.341), monotone to −3.7854 |
| A3, the cusps | to 4 × 10⁻⁵ of 2ζ(6); the comb to 10⁻⁶ | to 3.7 × 10⁻⁵; the comb to 1.1 × 10⁻⁶ |
| the contents' cusp coefficients (units of ζ(6)) | 9.57, 9.57, 1.70; 57.6; 66.6; 5.45 | exactly 9.574, 9.574, 1.699; 57.574, 49.699; 66.574, 58.699; 5.449 |

**The lattice cells** (`main_w62.json`; main's builder and solver, the seat's family; n = 8 400 and 4n = 33 600 sites).

| cell | the seat's record | main |
|---|---|---|
| M0, the builder | one triangle at −1 on every member at both sizes | the same (1 of 16 800 and of 67 200); Kramers at φ = 0 to 4.5 × 10⁻¹¹; the second hexagonal sublattice equals the reference to 9 × 10⁻¹¹ |
| M1, the abelian control | largest ∣ΔV_comb − ΔV_per∣ 1.45 × 10⁻⁴ (n), 3.6 × 10⁻⁵ (4n) | the same to 4 × 10⁻¹³ |
| M2, the diffraction is real | max ∣ΔD∣ = 0.1466 at 4n, above ten times M1's error | 0.1466 |
| M3, its sign and size | ΔD against ΔV_per at 4n, nine axis members | every member to 7 × 10⁻¹⁰; the ratio −0.475 on the arc, falling from −0.476 to −0.366 up the axis |
| M4, ΔV_ρ = β ΔE₃ | β = 0.018778, the largest residual 0.0057 at y = 2.02 | β to 3 × 10⁻¹¹; the same residual |
| M5, the copies' term | 0.0085 → 0.254 up the axis; 0.0011 → 0.0082 along the arc | every member to 7 × 10⁻¹⁰ |
| M6, n against 4n | ΔD moves by at most 0.78% (−0.1455 against −0.1466 at y = 2.02) | the same, 0.78% |
| PH2, the shape of D | E(τ, 2)'s coefficient −0.98 of 31/1024 (n), −0.988 (4n) | −0.9802 and −0.9878; with E(τ, 3) added, an rms of 4.8 × 10⁻⁴ |
| the truncation control (main's own) | — | the comb cut at λ_K against the full comb: 1.7 × 10⁻⁹ (n), 1.4 × 10⁻⁹ (4n) |

So W62's lattice confirms its closed form: at the selected line the matter's term changes with the shape only through a
diffraction that tracks the periodic part with a fixed negative ratio, and the Higgs copies' term rises toward the cusp
along both the axis and the arc.

## 3. Disclosed

- **Main's solver.** SciPy's shift-invert on the complex Hermitian operator lost about 3 × 10⁻⁷ per eigenvalue against a
  dense solve (found on a 1176-dimensional torus before any cell was read); main solves the real symmetric form instead,
  exact to 10⁻¹⁴. Spectra from before the fix were discarded.
- **K.** Main used K = 150 (W60) and K = 200 (W62) instead of the rules' 300 and 400, for time. W60's cutoff t₀ = 30/λ_K
  keeps the neglected part below e⁻³⁶, and three K = 300 spectra agree with K = 150 to 10⁻¹⁰. For W62, λ_K t₀ = 24.0 to 24.2, below the
  rule's 30 (a first estimate of main's said 55, on a wrong shortest vector); the truncation control (§2) bounds the
  effect at 1.7 × 10⁻⁹, and every cell agrees with the seat's K = 400 read-out to 7 × 10⁻¹⁰.
- **Two pools on one task list.** To use freed cores main started a second W62 pool from the far end of the list; the
  first pool had already taken three of the large members it reached, which were solved twice and written twice
  (identical within the solver's tolerance; every file loads and is checked). Main stopped the second pool once only
  one member was left. No output was read between the two writes.
- **Main's slips, caught before the record.** The order-3 rotation of the line torus was first guessed (four wrong maps)
  and then derived (φ ↦ (φ₂, −φ₁ − φ₂)); W62's family test first filed the hexagonal shape as an arc member; the W60
  reader's first convergence field compared lattice units across N.
- **Main read the rules and the read-outs before writing its code, not the seat's scripts.** The seat's recorded outputs
  were read for the comparison after main's own numbers existed.

## 4. Files

- `verification/lattice.py` (the builder), `verification/main_w60.py`, `verification/main_w62.py`, their outputs, and the
  received rules and read-outs (hashes in `SHA256_RECEIVED.txt`).
- The lock: `tests/test_b1686_w60_w62_on_main.py`.
