# B1684 — W59 ON MAIN (P-099, P-100): THE ONE-LOOP POTENTIAL'S CLOSED FORMS AND THE EIGHTEEN LINES VERIFIED; THE STATE THEY DEFINE IS NOT THE ONE THE SEAT'S LATER WORK SELECTS

**Verdict: PROVED (a verification arc).** cc (main), 2026-10-21. POINT_REGISTER P-099 and P-100, first in Q3 at the
owner's approval of 2026-10-21 ("all your recommendations approved"), before any new mass work. 0 of 19.
- **What is verified.** Every computed cell of the SM seat's W59 (D1, the one-loop potential on the shared fibre;
  rule 311f0cd96, script 39c6a5125, one run 3c4a98399, labelled post hoc a068e47ed and 6119e0da4), by main's own code
  written from W59's rule; the seat's two runs reproduce to machine precision (§3). That includes K4's failure as
  worded: at ω the 2-torsion points are shallow local minima, not saddles.
- **What is not.** That τ = ω and the Higgs-alone lines are the state. The seat's own later items say otherwise. W60
  finds the full potential's line at a half-period, and W62 finds that state not stationary in τ, with every content on
  record running to a cusp. Both are on main at headline level only. Main checks W62's structural point for the
  Higgs's closed-form term (M7): it holds.
- **So** the arcs that use W59's lines at τ = ω (B1653, B1656, B1660, B1673) rest on correct mathematics at a state
  that is an input, and that the seat's later potential does not select (P-214).

## 0. Seen first

`VERDICT topic-sweep /W59|one-loop potential|twisted determinant|Wilson line|E\(tau, 3\)|3-torsion|eighteen lines/: 12 of
1455 arcs on main match (NEGATIVE 2, PROVED 10)` — chiefly the four arcs that use W59's lines (B1653, B1656, B1660,
B1673) and B1453 (the SM seat's harvest). **Literature:** Kronecker's second limit formula and the determinant of the
twisted Laplacian on a flat torus (Ray–Singer); the Chowla–Selberg expansion of the Epstein zeta function; the minimum
of the Epstein zeta function at the hexagonal lattice (Rankin; Cassels; Ennola; Diananda); the determinant of the
Laplacian on a flat surface with conical points (Kokotov), cited, not re-derived.

## 1. The checks (main's own code, `verification/main_check/main_w59.py`)

| cell | W59's claim | main's check | holds |
|---|---|---|---|
| M1 (K1) | det Δ_w = ∣θ₁(w∣τ)/η(τ)∣² e^{−2π(Im w)²/y}; the three parity sectors multiply to 4 | −ζ′(0) of the twisted Laplacian by an Epstein–Poisson evaluation (incomplete gamma functions on both lattices), against the theta formula with w = φ₂ − φ₁τ, at eight random (τ, φ): agree to 1.1 × 10⁻¹⁵ (the other three sign maps miss by 0.47 to 0.83); the product 4 to 4 × 10⁻¹⁵ at five τ | yes |
| M2 (K2) | genus 3; the differentials dx/w², dx/w³, x dx/w³; ζ_Σ(0) = −3/2 = −1 − p; S and T invariance of y^{1/2}∣η∣² | Riemann–Hurwitz and the superelliptic genus (both 3); the differentials by valuations at the roots and at infinity (exactly the three); the cone arithmetic in exact fractions; the invariance to 6 × 10⁻¹⁶ | yes (the Kokotov step itself cited) |
| M3 (K3) | log(y∣η∣⁴) and E(τ, 3) stationary only at i (saddle) and ω (max, min); E grows to the cusp; the joint parity sum = −(15/16) E(τ, 3) | Newton from a 12 × 14 grid over a neighbourhood of the fundamental domain to y = 6, mapped to F: exactly two critical points each, i a saddle, ω the maximum of log(y∣η∣⁴) and the minimum of E; E = 130.37, 439.56, 1041.80 at y = 4, 6, 8; Chowla–Selberg against the lattice sum to 4 × 10⁻¹¹; the parity identity exact (Σ_p (−1)^{2(mp₁+np₂)} is 3 or −1), numerically to the truncation (10⁻⁹) | yes |
| M4 (K4) | a joint-parity boson's stationary points on the torus: τ₀ four, minimum (½, ½); τ₁ six, with a shallow local minimum at (½, 0); ω twelve, the global minimum at both 3-torsion points, the 2-torsion points local minima; a fermion's minimum at 0 | τ₀: four, minimum (½, ½); τ₁: six, minimum (½, ½) at −6.1822, the shallow minimum (½, 0) at −5.4897 (Hessian 0.624 and 284), saddles at (0.4998, 0.0281) and its mirror at −5.4896; ω: twelve, −1.72552 at (⅓, ⅓) and (⅔, ⅔), −1.55297 at the three 2-torsion points (minima), −1.54959 at six saddles, 3.88243 at 0; a fermion's minimum at 0 at all three | yes, K4's failure as worded reproduced |
| M5 (K5) | at a nonzero 3-torsion line exactly Q, u^c, d^c are twisted; at a 2-torsion line exactly Q, L, H | exact, all eight and all three lines | yes |
| M6 (PH2) | the Higgs alone at ω (charge 3): eighteen lines, (1/9, 1/9) or (2/9, 2/9) plus ⅓ℤ²; at (1/9, 1/9) the twists Q 1/9, u^c 5/9, d^c 2/9, L 2/3, e^c 2/3, H 1/3 | eighteen lines in ninths, no lower point on a 180 × 180 grid; 3w at the order-3 rotation's fixed points on every line; d^c and e^c differ on every line; the twists as stated | yes |
| M7 (W62's point) | at the selected half-period line the Higgs's copies break the modular group to the theta group, so the state is not stationary in τ | the Higgs's six-dimensional term on each half-period line w₀: invariant under w₀'s stabiliser (for (½, ½): S and T², not T), and its τ-gradient at ω is 8.68, not zero; the joint parity sum (every copy alike) has gradient 9 × 10⁻⁸ at ω, as SL(2, ℤ)-invariance requires | yes, for the Higgs's closed-form term only |

Main's numbers agree with the seat's JSON to the truncation (the global minimum at ω −1.7255235613716 against
−1.7255235613771).

## 2. What it says

- **W59's mathematics is right, cell by cell.** The twisted determinant, the matter determinant's checkable steps, τ's
  critical points and the line's stationary points are as the seat recorded them, including the failure it recorded.
- **The state is an input.** The τ results hold sector by sector: for a content that treats the parities alike, τ sits
  at ω or runs to the cusp by the content's sign. The eighteen lines are the Higgs alone, at ω. Neither is selected
  here.
- **The seat's own later work moves it.** W60 (the quark sector with a line) puts the full potential's line at a
  half-period, where the matter sees nothing; W62 finds that state not stationary in τ. M7 checks W62's mechanism for
  the Higgs's closed-form term: on a half-period line the term keeps only the line's stabiliser, ω is not an elliptic
  point of it, and the gradient there is not zero. W60's lattice computation and W62's matter term are not checked
  here (P-222).
- **The arcs on W59's lines.** B1653, B1656, B1660 and B1673 use the lines at τ = ω. B1656 names both as stated inputs.
  Their mathematics stands as conditionals; dated scope notes follow under P-214, saying that the inputs are not the
  state the seat's later potential selects.
- **P-099's two named debts.** The matter's exponent −¼: its checkable steps verified, Kokotov's formula cited. The
  sign that decides ω against the cusp: a content's, a dictionary datum (W59); every content on record runs to a cusp
  (W62, headline; P-222).

## 3. Reproduction

The seat's script and its post hoc were re-run on main in the seat's own tree at a068e47ed (a detached checkout; the
scripts import W51's helper and, through it, the seat's libraries back to sm:B1549), with W59's recorded output moved
aside first. Both runs end as recorded ("every cell holds: False", K4 failed as worded). The two JSON files are not
byte-identical: 23 and 37 floats differ in the last digit (at most 7 × 10⁻¹⁶ relative); every other field, every
point, type and count, is identical. So the runs reproduce to machine precision, not byte for byte (the platform's
numerical library). The re-run outputs and logs are in `verification/rerun/`.

## 4. Disclosed

- **Main's own errors, caught before the record.** In a smoke test the Epstein–Poisson route first used the dual
  lattice's covolume as the Poisson prefactor and then the wrong incomplete gamma function; a direct Kronecker sum (a
  control computed beside it) located the error, and the route as written agrees with it and with the theta formula.
- **The first full run** (kept: `main_w59_run1_first.txt`, `main_w59_run1_first.json`) reported M3 and M7 false: both
  tolerances were set below the lattice truncation (the even sublattice at N = 120, about 10⁻⁹; the truncated box at
  N = 60, about 10⁻⁶), with every critical point, gradient and value as in the second run. Its Newton grid also missed
  τ₁'s shallow minimum at (½, 0), as the seat's own post hoc grid did; the second run seeds the 2-torsion and 3-torsion
  points, which are stationary by symmetry (V is even; ω's rotation), and finds W59's six.
- Main read W59's rule and its recorded read-out before writing the check, not its script.
- After the second run, one line of the Newton step's clipping was rewritten to avoid a harmless divide-by-zero
  warning (a zero step); main's check was re-run in place and its JSON is byte-identical to the second run's.

## 5. Files

- `verification/received/`: W59's rule, script, output, post hoc script and post hoc output (hashes in
  `SHA256_RECEIVED.txt`), and W51's helper as the re-run used it.
- `verification/main_check/main_w59.py` → `main_w59.json`, `main_w59_run.txt`; the first run kept.
- `verification/rerun/`: the seat's scripts' re-run, with its logs.
- The lock: `tests/test_b1684_w59_on_main.py`.
