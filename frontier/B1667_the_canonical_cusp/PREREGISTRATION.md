# B1667 — THE CANONICAL CUSP (does the fibre's own hyperbolic geometry fix the end radius, and at what size?): preregistration

cc (main), 2026-10-16. POINT_REGISTER P-185 (P-183 step 5, after P-184). 0 of 19.

- **The question.** B1654 found that the parity Higgs's only massless mode needs an end cutoff at the puncture, and that
  under the canonical end condition the first generation's lift is D(τ)/(2πL), L = log(1/ε). It called L a regulator: at
  a complete cusp there is no boundary on which to impose a condition (B1654; the paper draft's §6). That argument is in
  the flat metric. In the fibre's own complete hyperbolic metric (the uniformisation of the punctured torus) the
  puncture is a hyperbolic cusp, and a hyperbolic cusp has canonical neighbourhoods: the **maximal embedded horoball**
  and the **horocycle of length 2**. Either fixes ε, hence L, as a function of τ alone. Does it, at what size, and what
  does the first generation's lift become under it?
- **The construction.** The developing map of y″ + (℘(z)/4 + c)y = 0 on C/(ℤ + τℤ), with the accessory parameter c(τ) fixed
  by real monodromy and followed by continuation from the symmetric points (c = 0 exactly at τ = i and at τ = e^{iπ/3},
  by the lattice's rotation). The monodromy is conjugated into SL(2, ℝ) with the puncture's parabolic u ↦ u + λ at ∞.
  Near the puncture, u(z) = −(iλ/2π)(log z + g(z)) + B exactly (the Frobenius solution, g = O(z²)). The horoball
  {Im u > h} is {log(1/|z|) − Re g(z) > (2π/λ)(h − Im B)}. Hence:
  - L_max = (2π/λ)(h_max − Im B), with h_max = 1/min∣c_γ∣ over the group (the maximal embedded cusp);
  - L_2 = π − (2π/λ)·Im B (the horocycle of length 2, embedded by Shimizu's lemma).
- **The lift under the canonical cut.** The exact norm of each channel outside the horoball, N_r = ∫ over the Dirichlet
  cell minus the horoball of ∣S_r∣² dA, with B1654's own profiles S_r (route A of its sealed instrument, imported
  unchanged). The canonically normalised amplitudes are u_r = √N_r·R_r, and the first generation's lift relative to the
  heavy scale is **ρ_can(τ) = ∣Σ N_r R_r²∣ / Σ N_r ∣R_r∣²**. This is a function of τ alone; B1654's asymptotic form is
  f/(2πL), with f = ∣D∣/‖R‖².

## 0. Seen first

`VERDICT topic-sweep /horocycl|maximal cusp|Shimizu|cusp neighbo|end radius|canonical end|accessory parameter|Lam[eé]|uniformi[sz]|Fuchsian (once-)?punctured|developing map/: 7 of 1438 arcs on main match (NEGATIVE 3, PROVED 4)`
— B1654 (the end cutoff, read in full), B1656–B1658 and B1660 (they use B1654's canonical end condition at a free L),
B1075 and B523 (unrelated word matches), B1295 (the harmonic generator; not the cusp radius). No arc on main computes a
canonical end radius. **The web seat** (relay of 2026-10-16 13:10, harvest row 1250, not yet verified on main) found in
the *surface* frame that the scale-free regularisation of its units' norms is indefinite and that a cut at the standard
maximal cusp (c = 1) is positive: the same question asked of a different cusp. **Literature:** the accessory parameter
of the punctured torus's Lamé-type equation and its role in the moduli of punctured tori (Keen, Rauch and Vasquez,
1979); Shimizu's lemma for the embedded cusp neighbourhood; Maskit's comparison of hyperbolic and extremal length (used
only as a plausibility check below); B1654 for the profiles S_r, the residues R_r and the finite parts c_r.

## 0b. Disclosed

- **Three points were seen before the seal**, and the thresholds of T1 and T2 were set after seeing them:
  - τ = i: L_max 0.68839, L_2 2.71926, ρ_can 0.578 (maximal cusp) and 0.0762 (length 2), cusp area 4√2;
  - τ = e^{iπ/3}: L_max 0.69208, L_2 2.78648, ρ_can = 0 for both cuts (the order-three symmetry), cusp area 6;
  - τ = 0.25 + 1.3i: L_max 0.67258, L_2 2.59740, ρ_can 0.332 and 0.0501, cusp area 5.164.
  - τ = 0.25 + 1.3i is not a grid point; its neighbour 0.25 + 1.25i is.
- **An independent closed form at τ = e^{iπ/3}** (`before_the_seal/eta_control.py`). The punctured hexagonal torus is
  H/SL(2, ℤ)′, with LR and RL as free generators (index 12, checked by coset enumeration). Its cusp width is 6, its maximal
  cusp sits at Im w = 1, and dz = c·η(w)⁴dw. The η⁴ periods give L_max = 0.69208004049 and L_2 = 2.78647514288. The
  Lamé route agrees to every printed digit, and both values are gate controls.
- **Four instrument defects were found and repaired before the seal:**
  - the constant term of ℘ (+e₁, not −e₁);
  - the cusp conjugated to ∞ (the commutator of the cell's edges encircles 1 + τ, not 0; the parabolic is now taken from a
    small loop about 0);
  - the quadrature domain (the period parallelogram undercounts the maximal horoball's overflow, caught by the embedding
    margin; now the Dirichlet cell);
  - the θ series' overflow at large Im z (℘ is now evaluated after reduction to the central cell).
- **A wrong root, and the remedy.** At τ = 0.33 + 3.7i, an off-grid point checked for numerics only, Newton from c = 0
  converged to a real but non-uniformising root (c = −0.300, min Im u = −0.66 on the sample: a grafted structure). The
  continued root (c = 0.704) has tr a = 2.12, against about 2.18 from Maskit's bound, and Im u > 0. Hence the
  continuation from the symmetric points and the uniformisation check in the gate. A second off-grid point, 0.07 + 1.02i,
  was checked for the gate quantities only.
- **A plumbing smoke test of the sealed instrument on the two controls** (i and e^{iπ/3}) passed every gate tolerance.
- **The reviewing agent before the seal**, told to break the instrument and forbidden the grid, evaluated off-grid points
  near it: its ρ values (§4) inform T2–T4, so **no cell is blind**. The verdict is graded as a census informed by
  neighbours, and it is said so.

## 1. The cells

The grid: Re τ ∈ {0.05, 0.15, 0.25, 0.35, 0.45}, Im τ ∈ {0.95, 1.0, 1.25, …, 3.0} with ∣τ∣ ≥ 1.03. Column 0.25 is extended
to Im τ = 3.25, 3.5, 3.75, 4.0. The ray e^{iπ/3} + d·e^{2πi/3} has d ∈ {0.02, 0.05, 0.1, 0.2}. By the mirror τ ↦ −τ̄ the half
Re τ ≥ 0 covers the domain. The two symmetric points are controls.

| cell | prediction | kind |
|---|---|---|
| **L0**, plumbing | every task present, none failed. At every point: Newton residual ≤ 10⁻⁹; λ > 0 (the signed translation: a wrong root found by the review had λ < 0); ∣traces∣ > 2 and the Markov identity to 10⁻⁸; tr P₀ = −2 to 10⁻⁷; the normalised group real to 10⁻⁷; Im u > 0 on a 4 × 4 sample of the cell (uniformisation); Im B stable across two matching radii to 10⁻⁷; min∣c∣ the same at word lengths 6 and 8 (10⁻⁹); the maximal horoball touches the Dirichlet cell (−10⁻⁶ ≤ margin ≤ 2·10⁻³); the length-2 horocycle embedded (margin > 0); ρ_can(L_2) at 144 × 96 nodes within 10⁻³ of 96 × 64 on column 0.25 for Im τ ≥ 2. Controls: at i the traces (2√2, 2√2, 4) and area 4√2; at e^{iπ/3} the traces (3, 3, 6), area 6, L_max and L_2 equal to the η⁴ values to 10⁻⁶, and ρ_can = 0 to 10⁻¹⁰ for both cuts | gate |
| **T1**, the canonical radius is of order one | at every grid and ray point, 0.2 < L_max < 2 and 1.5 < L_2 < 4.5 | test (thresholds set after three points) |
| **T2**, no hierarchy from the canonical cut in the bulk | at every grid point with Im τ ≤ 1.5 and ∣τ − e^{iπ/3}∣ ≥ 0.15: ρ_can(L_2) ≥ 5·10⁻³ and ρ_can(L_max) ≥ 5·10⁻² | test (thresholds set after three points) |
| **T3**, the zero at ω is simple | on the ray, the log–log slope of ρ_can(L_2) against d over d ∈ {0.02, 0.05, 0.1} lies in [0.75, 1.25] | test (informed: the reviewing pass printed slopes 0.915 and 0.962 on two other rays from ω, §4) |
| **T4**, toward the cusp of moduli | on Re τ = 0.25, Im τ ∈ {2, 2.5, 3, 3.5, 4}: the slope of ln ρ_can(L_2) against Im τ lies in [−3.6, −2.2] (expected about −π + 1/Im τ from B1654's law f ∝ ∣q∣(8π² Im τ + K), with ∣q∣ = e^{−π Im τ}, and L_2 tending to a constant); and ∣L_2(4) − L_2(3.5)∣ < 0.05 | test (informed: the reviewing pass's off-grid values imply a slope near −2.6 and a drift near 0.02, §4) |
| read-outs | column 0.25 (L_max, L_2, ρ_can at both cuts, f); ρ_can(L_2)/(f/(2πL_2)), how good B1654's asymptotic form is at the canonical radius; the range of the maximal cusp area | — |

**If L0 fails, nothing after it is read as a result.** Verdict rule: PROVED if T1–T4 hold; NEGATIVE as sealed if any
of them fails, with the failing cell's reading. ρ_can(e^{iπ/3}) = 0 is the symmetry, an identity, reported apart.

## 2. What it would mean

- **If T1 and T2 hold:** the fibre's own geometry fixes the end radius up to a discrete choice of canonical horocycle,
  and fixes it at order one. B1654's free end datum L is then replaced by a discrete geometric choice. The canonical cut
  supplies no hierarchy, and the first generation's lift becomes ρ_can(τ), a function of τ alone. A large L, which
  B1654's bulk hierarchy needs (m₁/m₃ ≈ 0.15/L), means a cut far inside every canonical horoball: a scale the fibre's
  geometry does not supply.
- **T3 and T4** locate where a small lift can come from under the canonical cut: a simple zero at ω, and an exponential
  fall toward the cusp of moduli. A hierarchy is then a statement about τ (P-169), not about the end.
- **If T1 fails** (a canonical L that grows somewhere), the geometry itself can supply a large L, and a hierarchy from
  the cusp's own size becomes possible. **If T2 fails,** there is a small lift in the bulk away from ω, a zero of the
  lift that B1654 did not see.
- **What it cannot show:** that either canonical horocycle is the physical end (a choice between two discrete
  candidates remains); that the fibre frame is nature's (B1652); any value (0 of 19). It is a census over the grid, not
  a proof between grid points.

## 3. Files

`verification/the_canonical_cusp.py` (sealed), with `the_canonical_cusp.json` and `_run.txt` after the run;
`verification/before_the_seal/` (the η⁴ control and its output, the draft module, the smoke outputs, the commutator-
subgroup check). Launch: `nice -n 10`, seven worker processes, each with one BLAS thread.

## 4. The reviewing agent before the seal

One read-only pass (2026-10-16), told to break the instrument, forbidden the grid's values. **No blocker.**
- **Roots.** The tracked root is path-independent: an alternate path agrees to 3–5 × 10⁻¹⁴, and continuation from ω agrees
  with continuation from i to 2–4 × 10⁻¹³. At 0.4 + 2.2i Newton from many starts finds three real roots: c = 0.556 (Im u_min
  +0.124, λ > 0, the tracked one), −1.956 (Im u_min −0.297, λ < 0) and −8.077 (Im u_min −0.021). The 4 × 4 sample rejects
  both wrong ones; **taken:** λ > 0 added to the gate. Maskit's plausibility: tr a = 2.272, 2.144, 2.097 at Im τ = 2.2, 3.3,
  4.2, so π/ℓ − Im τ tends to about 0.86 and tr a tends to 2.
- **Orientation, Im B, Frobenius.** Im B is independent of the matching radius (0.3 to 0.02) and of the ray (scatter
  7 × 10⁻¹¹); the series is exact to r ≈ 0.6 (10⁻¹⁰).
- **h_max.** min∣c∣ is attained at word length 1 in all seven cases (checked to lengths 10–12); the 6-to-8 drift is under
  6 × 10⁻¹³. The touching margin is 1–9 × 10⁻⁵ everywhere it ran.
- **Gauss–Bonnet at 0.3 + 1.4i** (the strongest independent check): the hyperbolic area of the cell minus the horoball,
  integrated from the raw ODE transfer, is 1.23294241 against 2π − λ/h_max = 1.23294237 for the maximal cusp, and
  4.28318530 against 2π − 2 for the length-2 horocycle. This validates λ, Im B, h_max, g, the Dirichlet cell, the
  horocycle and the uniformisation jointly.
- **The cell, the import, ℘.** The Dirichlet-cell area equals Im τ to 5 × 10⁻⁸ at eight τ, and rmax matches a brute-force
  minimum to 10⁻¹⁶. The imported B1654 slice reproduces cA (K = 40 against 24: exact), and horoball_norms at a deep cut
  reproduces cA + 2πL to 10⁻¹⁴. ℘ agrees with an independent Lambert series to 10⁻¹⁵.
- **Warnings taken:**
  - the Dirichlet cell is valid for reduced τ only (now asserted; every planned point is reduced);
  - one BLAS thread is now set inside the script;
  - the dead leading-order code is removed;
  - λ > 0 is now gated.
- **What it saw (disclosed, see §0b):**
  - ρ_can(L_2) = 0.0415 at 0.3 + 1.4i, 0.0373 at 0.1 + 1.6i, 8.485 × 10⁻³ at 0.4 + 2.2i, 5.345 × 10⁻⁴ at 0.3 + 3.3i and
    4.372 × 10⁻⁵ at 0.3 + 4.2i;
  - ρ_can(L_max) = 0.29 and 0.27 at the first two;
  - L_2 = 2.322 at 3.3i and 2.286 at 4.2i;
  - log–log slopes 0.915 and 0.962 for ρ_can(L_2) on two rays from ω that are not the planned one.
