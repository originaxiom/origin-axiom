# B1667 — THE CANONICAL CUSP: the fibre's own hyperbolic geometry fixes the end radius at order one (L_max ≈ 0.64–0.69, L_2 ≈ 2.3–2.8 on the whole grid), so the end supplies no hierarchy; under the canonical cut the first generation's lift is a function of τ alone, with a simple zero at ω and a fall like e^(−2.6 Im τ) toward the cusp of moduli

**Verdict: PROVED, as sealed (a census informed by neighbours).** Every cell holds. Three points were seen before the
seal and the reviewing pass printed off-grid neighbours, so no cell is blind. cc (main), 2026-10-16.
- Sealed `ca1c08efb` (sha256 83689a5d) before the run. The output was committed unread at `e68a87550`: one run of
  327 s, exit 0, the instrument unchanged since the seal (sha256 dd5fe689).
- **0 of 19.** POINT_REGISTER P-185 (P-183 step 5).

## 0. Seen first

As sealed: `VERDICT topic-sweep /horocycl|maximal cusp|Shimizu|cusp neighbo|end radius|canonical end|accessory parameter|Lam[eé]|uniformi[sz]|Fuchsian (once-)?punctured|developing map/: 7 of 1438 arcs on main match (NEGATIVE 3, PROVED 4)`
— B1654 read in full; B1656–B1658 and B1660, which use its canonical end condition at a free L. No arc on main computes a
canonical end radius. The web seat's relay of 2026-10-16 (harvest row 1250) asks the same question of the *surface*
frame's cusp. **Literature:** the accessory parameter of the punctured torus's Lamé-type equation (Keen, Rauch and
Vasquez, 1979); Shimizu's lemma; Maskit's comparison of hyperbolic and extremal length (a plausibility check only).

## 0b. Disclosed

As the preregistration's §0b and §4:
- three points seen (i, e^{iπ/3}, 0.25 + 1.3i), with T1's and T2's thresholds set after them;
- the η⁴ closed form at e^{iπ/3};
- four instrument defects repaired before the seal;
- a wrong (grafted) root found and excluded by continuation and the uniformisation check;
- a reviewing pass with no blocker, whose off-grid values inform T2–T4.

## 1. The sealed run (`verification/the_canonical_cusp.py`, unchanged; `.json`, `_run.txt`)

The run covers 54 points: 48 on the grid, 4 on the ray from ω and 2 controls. No task failed.

| cell | prediction | result |
|---|---|---|
| **L0**, plumbing | residual, Markov, tr P₀ = −2, λ > 0, realness, Im u > 0, Im B stable, min∣c∣ stable, the maximal horoball touches the Dirichlet cell, the length-2 horocycle embedded, quadrature; the controls at i and e^{iπ/3} with the η⁴ values | **HOLDS**, all 16 clauses. Im u ≥ 0.062 on every sample; touching margins 1.7–8.6 × 10⁻⁵; quadrature to 7 × 10⁻¹³; L at e^{iπ/3} equal to the η⁴ values (0.69208004, 2.78647514) |
| **T1**, the radius is of order one | 0.2 < L_max < 2 and 1.5 < L_2 < 4.5 everywhere | **HOLDS:** L_max ∈ [0.643, 0.691], L_2 ∈ [2.292, 2.777] |
| **T2**, no hierarchy in the bulk | ρ_can(L_2) ≥ 5 × 10⁻³ and ρ_can(L_max) ≥ 5 × 10⁻² at the 12 bulk points | **HOLDS:** ρ_can(L_2) ∈ [0.031, 0.065], ρ_can(L_max) ∈ [0.238, 0.410] |
| **T3**, the zero at ω is simple | log–log slope of ρ_can(L_2) in d ∈ [0.75, 1.25] | **HOLDS:** 0.962 (ρ_can(L_2) = 4.0 × 10⁻³, 9.8 × 10⁻³, 1.88 × 10⁻² at d = 0.02, 0.05, 0.1) |
| **T4**, the cusp of moduli | slope of ln ρ_can(L_2) in Im τ ∈ [−3.6, −2.2]; ∣L_2(4) − L_2(3.5)∣ < 0.05 | **HOLDS:** −2.628; L_2 = 2.312 → 2.292 |

**Read-outs** (no criterion):
- **Column Re τ = 0.25.**
  - L_max runs 0.687 → 0.643 and L_2 runs 2.718 → 2.292 for Im τ = 1 → 4.
  - ρ_can(L_2) runs 5.5 × 10⁻² → 7.8 × 10⁻⁵, and ρ_can(L_max) runs 0.41 → 8.4 × 10⁻⁴.
  - B1654's f = ∣D∣/‖R‖² runs 0.80 → 9.0 × 10⁻⁴.
- **B1654's asymptotic form f/(2πL), evaluated at the canonical radius,** is within 17–25% of the exact lift at every grid
  point (ratio 1.167–1.245).
- **The maximal cusp's area** runs from 4.21 to 5.95; it is 4√2 at i and 6 at ω.
- **On the ray from ω,** ρ_can(L_max) grows more slowly than linearly (log–log slope about 0.78). That is not tested.

## 2. What it says

- **The end datum is not a free continuous number in the fibre's own geometry.** B1654 called L = log(1/ε) a regulator
  because a complete cusp has no boundary on which to impose a condition. That is true in the flat metric. In the
  hyperbolic metric that uniformises the punctured fibre, the puncture is a cusp with canonical neighbourhoods. The two
  computed here fix ε as a function of τ alone:
  - the maximal embedded horoball;
  - the horocycle of length 2.
  What remains is a discrete choice between canonical horocycles, not a continuum.
- **The canonical radius is of order one everywhere,** for both choices. On the whole grid, up to Im τ = 4, it lies
  between 0.64 and 2.8, and it converges toward the cusp of moduli. B1654's bulk hierarchy, m₁/m₃ ≈ 0.15/L, needs L in
  the hundreds. That means a cut far inside every canonical horoball, at a scale the fibre's geometry does not supply.
  **The end supplies no hierarchy.**
- **Under the canonical cut, the first generation's lift is a function of τ alone,** with the end's normalisation
  computed exactly rather than assumed small. It vanishes only:
  - at the symmetric point, where the zero is simple (T3);
  - toward the cusp of moduli, where it falls as e^(−2.6 Im τ) (T4), B1654's ∣q∣(8π² Im τ + K) law at the canonical
    radius.
  A small first generation therefore needs τ near ω or high in the domain. The hierarchy is a statement about τ, not about
  the end (P-169).
- **What it does not show:**
  - which canonical horocycle, if either, is the physical end;
  - that the fibre frame is nature's (B1652);
  - any value. The read-out heights at which the lift crosses a given size are not compared with data here.
  - It is a census over the grid, not a proof between grid points.

## 3. Files

- `verification/the_canonical_cusp.py` (sealed), `the_canonical_cusp.json` and `the_canonical_cusp_run.txt` (the run).
- `verification/before_the_seal/`:
  - the η⁴ control and its output;
  - the draft module (not runnable in place);
  - the commutator-subgroup check;
  - the smoke test of the controls.
- The lock: `tests/test_b1667_the_canonical_cusp.py`.
