# W87 — the rule, recorded before the code

The SM-derivation seat, 2026-10-15. Committed before the code that reads it exists. What the seat read, explored and
worked by hand while drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here
is a result.

## Why this arc

- **Main asked for it.** S129: "If you check one thing of main's next, check §3's end-condition reading against your
  C0." S130: "If you check one thing, check §1.2 of B1654's preregistration against your C0."
- **B1654's section 1** (sealed at 155959126) sets the parity Higgs as C0's boundary class at the puncture (C0 point 3).
  Its channel-r norm needs an end cutoff: ‖S_r‖²_ε = 2π ln(1/ε) + c_r(τ) + o(1). Its item 2 gives the coupling per
  unit norm and the three end conditions: P4 (equal canonical amplitudes), P4′ (equal framed data, read as C0's "one
  normalisation serves all three") and P4″ (equal unnormalised amplitudes).
- **Two questions for this seat.** Do item 2 and its consequences hold on this seat's own code? And does C0 say what
  main reads it as saying?

## Weave or thread?

- **Weave-type, given Λ, B1654's typing P1 and its boundary class P2.** The fibre is the one every thread shares. The
  three parity channels are taken jointly: D(τ) = Σ_r c_r R_r² exists only because the three residues satisfy R·R = 0
  together. The claims are identities in τ, checked at fixed τ.

## Seen before the rule (disclosed)

- **Main's B1654 preregistration, read in full: §0's disclosures, §1 and the cell table.** Its stated values were seen:
  1.09 at τ = i, K = 8π(1 − 4 ln 2) = −44.550, the cusp limits of c₂, c₃ and c₄, and N5's grid thresholds. Main's
  output files (cd3c046ae) and FINDINGS were not read. Its instrument and design draft were searched for a closed form
  and none was found; the lines that search printed were seen.
- **Main's relays of S129 and S130**, and its S130 commit message: |D|/|R|² ≥ 0.16 on main's grid away from the
  corners, and near-corner slopes 2.70 to 2.93.
- **The seat's own exploration, firewalled** (scratch scripts, not kept as evidence; double precision):
  - c_r(τ) by polar quadrature at five τ (i, 0.2 + 1.3i, ω, 2i, 0.1 + 0.9i). There, c_r + 2π ln|θ_r(0)|² was
    −2.837377819 for all three r and all five τ, to 3 × 10⁻¹⁴. That suggested the closed form of C1 below.
  - D(τ) from those c_r against the closed form of C2, at six τ: they agreed to 6 × 10⁻¹³. |D|/|R|² against the λ form,
    likewise. D/(q|R|²) at 2i and 3i, against main's cusp law: 111.69 against 113.36, and 192.20 against 192.32.
- **The seat's own hand derivations while drafting** (set out under "The derivations"): C1's closed form by Parseval;
  C2's closed form and its consequences; C3's end-condition family; C5's bound.
- **The seat's own record that bears on it:** C0 (the reading before W59); W85, whose triplet is B1651's pairing in the
  πz convention; and relay §107.

## The derivations (by hand; the cells test them)

1. **The channel norms in closed form.** For every τ in ℍ and every even spin structure r,
   **c_r(τ) = −2π ln((π/2)|θ_r(0 | τ)|²).**
   - In the strip 0 < Im z < Im τ, S_r(z) = −2πi Σ_k e^{2πikz}/(1 − ε_r q^{2k}). Here k runs over ℤ for r = 2 and over
     ℤ + ½ for r = 3, 4, and ε_r is S_r's multiplier under z ↦ z + τ (−1, −1, +1 for r = 2, 3, 4). The coefficient
     follows from the jump −2πi across the real axis, which is the residue 1 at each lattice point.
   - By Parseval at height t, ∫₀¹ |S_r(x + it)|² dx = 4π² Σ_k e^{−4πkt}/|1 − ε_r q^{2k}|².
   - Cutting at t = δ and t = Im τ − δ gives, up to o(1), the same regularised integral as cutting a disc of radius 2δ
     about the puncture, since ∫₀¹ arcsin(u) du/u = (π/2) ln 2.
   - Integrating in t, and using (1 − |q|^{4k})/|1 − εq^{2k}|² = 2 Re[1/(1 − εq^{2k})] − 1:
     - c₂ = −2π ln 2π + π² Im τ − 4π Re Σ_m (−1)^m ln(1 − q^{2m});
     - c₃ = 2π ln(2/π) + 4π Re Σ_m (−1)^m ln((1 + q^m)/(1 − q^m));
     - c₄ = 2π ln(2/π) + 4π Re Σ_m ln((1 + q^m)/(1 − q^m)).
   - Euler's identity ∏(1 + x^n)(1 − x^{2n−1}) = 1, and Gauss's θ₄ = ∏(1 − q^n)/(1 + q^n) with θ₃(q) = θ₄(−q), turn
     the three sums into −2π ln|θ_r(0)|². This gives the closed form.
2. **D in closed form.** With λ = θ₂⁴/θ₃⁴ and h(λ) = λ ln|λ| + (1 − λ) ln|1 − λ|:
   - D(τ) = Σ_r c_r R_r² = −θ₃⁴ h(λ)/(4πη⁶), since R·R = 0 removes the constant and θ₃⁴ = θ₂⁴ + θ₄⁴ (Jacobi);
   - |D|/|R|² = π|h(λ)|/(1 + |λ| + |1 − λ|).
   - **Consequences.**
     - The ratio is invariant under λ ↦ 1 − λ and λ ↦ 1/λ, so under SL(2, ℤ).
     - **D vanishes exactly on the orbit of ω, and nowhere else in ℍ.** Im h = Im λ · ln|λ/(1 − λ)|. If Im λ ≠ 0 this
       forces |λ| = |1 − λ|, and then Re h = ln|λ| = 0 gives λ = e^{±iπ/3}. If λ is real (and not 0 or 1), h is
       negative on (0, 1) and positive outside, by the symmetries above.
     - At τ = i, λ = ½ and |D|/|R|² = (π/2) ln 2 = 1.08879.
     - At the cusp (τ = iy, λ real in (0, 1)), D/|R|² = −(π/2)h(λ) exactly. With λ = 16q − 128q² + O(q³):
       D/(q|R|²) = 8π²y + 8π(1 − 4 ln 2) + 64πq(4 ln 2 − 1 − πy) + O(q² ln q). The first two terms are B1654's item 9,
       constant included; the third is the next order.
3. **The end conditions as one family.** A channel-blind end condition gives each channel's coupling the same function
   G of its own norm: u_r = G(2πL + c_r)R_r, with L = ln(1/ε).
   - P4 is G = √x, P4″ is G = x, and P4′ is G = 1.
   - u·u = Σ_r G(2πL + c_r)²R_r² = 2G(2πL)G′(2πL)·D(τ) + O(G′² + GG″). So **every G with G′ ≠ 0 lifts the first
     generation with the same τ-shape, D(τ)**. Only the size depends on G. For P4, u·u = D exactly; for P4″,
     u·u = 4πL·D + Σ_r c_r²R_r².
   - **The cutoff-free end conditions** (u's direction independent of L) are exactly G = A·e^{βx}, since
     G(x + c)/G(x) must not depend on x. Then u ∝ e^{βc_r}R_r and u·u ∝ Σ_r |θ_r(0)|^{−8πβ}R_r². It vanishes at
     every τ only for β = 0, which is P4′.
   - At τ = ω the three c_r are equal, so **every channel-blind end condition keeps the first generation massless at
     ω.**
4. **What C0 says** (C5, a reading).
   - C0 point 5(a)'s "one normalisation serves all three" is a covariance argument: the moves permute the channels.
     Every channel-blind G with one common cutoff (B1654's P3) meets it, so the argument does not choose among P4, P4′
     and P4″.
   - C0's next sentence, "The couplings are then numbers, … with the state (τ and the Higgs's direction h) as the only
     freedom", asks for cutoff-free couplings. By item 3 that selects the family e^{βx}. P4′ is its β = 0, the only
     member keeping the zero at every τ.
   - C0 point 3 left "whether a boundary class's profile is bounded at the puncture" to be computed. No closed
     representative is bounded. A closed representative's period on each small circle is the class's value on the
     puncture loop, z(c) ≠ 0. By Cauchy–Schwarz on circles, its norm on ε < |z| < ρ is at least
     (|z(c)|²/2π) ln(ρ/ε). The harmonic representative attains this (2π, for unit residue). So B1654's cut is forced
     on every closed representative; it is not an artefact of the harmonic choice.
   - So main's reading is right only with two additions: C0's "numbers" sentence, and β = 0. C0 wrote both sentences
     before the profile was known to be unbounded. The choice stays the parent's (clauses 4 and 6), as main says.

## The method (fixed here)

- **The thetas are W85's own series at 60 digits** (`the_b1651_cells_checked.py`, imported), in the πz convention. They
  are converted to B1654's z convention (periods 1 and τ) by w = πz. η³ = θ₁′(0)/2 in the w convention, with a control
  against η = q^{1/12}∏(1 − q^{2n}).
- **The residues:** R = (−θ₂², −θ₄², iθ₃²)/(2πη³), units (i, j, k) ↔ channels (2, 4, 3), as B1654 and B1651.
- **The fibres** (12): i, ω = −½ + i√3/2, 2i, 3i, and eight τ drawn with seed 87, uniformly with |Re τ| ≤ ½ and
  Im τ ∈ [0.9, 2.5], kept if |τ| ≥ 1.
- **Route A, the closed form,** at 60 digits.
- **Route B, polar quadrature** of the definition, in double precision:
  c_r = ∫₀^{2π} [ln r_max(θ) + ∫₀^{r_max(θ)} (r|S_r(re^{iθ})|² − 1/r) dr] dθ over B1654's P.
  - The angle is split at P's four corners, with 100 Gauss–Legendre nodes per piece and 60 radial nodes.
  - S_r comes from its own numpy theta series (40 terms), not from W85's.
- **Route C, the Parseval series** of derivation 1, before Euler's and Gauss's identities, at 60 digits.
- **The cusp points:** τ = 4i, 5i, 6i, 8i.
- **The grid:** 41 × 40 nodes over the fundamental domain |Re τ| ≤ ½, |τ| ≥ 1, Im τ ≤ 2, by route A.
- **The masses** follow B1654's item 10. Y(a; u) = a uᵀ + u aᵀ − (a·u)𝟙, with singular values by mpmath at 60 digits.
  The directions a are three seeded complex vectors (seed 87). The fibres are i and the first two seeded τ, and
  L ∈ {10³, 10⁴}.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **C1, the norms** | at all 12 τ and r = 2, 3, 4: route C equals route A to 10⁻⁴⁰; route B equals route A to 10⁻¹⁰. Control: θ₁′(0)/2 equals η³ from the product to 10⁻⁴⁰ | 97% |
| **C2, D in closed form** | (a) D from route B's c_r equals −θ₃⁴h(λ)/(4πη⁶) to 10⁻¹⁰ relative to \|R\|², at all 12 τ; (b) \|D\|/\|R\|² equals π\|h(λ)\|/(1 + \|λ\| + \|1 − λ\|) at 60 digits, and is the same at τ, −1/τ and τ + 1 to 10⁻⁴⁰; (c) at ω it is < 10⁻⁴⁰, at the 11 other τ > 10⁻², and at i (π/2) ln 2 to 10⁻⁴⁰; (d) at 4i, 5i, 6i and 8i, D/(q\|R\|²) − 8π² Im τ − 8π(1 − 4 ln 2) equals 64πq(4 ln 2 − 1 − π Im τ) within 1% of the latter, and its size at 5i is < 2 × 10⁻³ (B1654's N5(d) threshold); (e) on the grid, \|D\|/\|R\|² > 0.05 at every node farther than 0.1 from both corners (B1654's N5(c) threshold) | 95% |
| **C3, the family** | (a) W85's triplet at w = πz equals (R_r S_r(z))_r to 10⁻⁴⁰ at the 12 τ and W85's six regular points, which is B1654's N0 on this seat's code; (b) for X = 2πL with L ∈ {5, 20, 80}: under P4, u·u = D; under P4″, u·u = 2X·D + Σ c_r²R_r²; under P4′, u·u = 0; each to 10⁻⁴⁰ relative to \|u\|²; (c) for G = x^p with p ∈ {¼, ½, 1, 2}, at L = 10⁴, u·u/(2G(X)G′(X)D) is within 10⁻² of 1 at the 11 τ ≠ ω; (d) for β ∈ {−0.1, 0.05, 0.2}, u's direction under G = e^{βx} is the same at the three L to 10⁻⁴⁰; \|u·u\|/\|u\|² > 10⁻⁵ at the 11 τ ≠ ω and < 10⁻⁴⁰ at ω. Control: under G = √x the direction moves with L (> 10⁻⁶) | 95% |
| **C4, the masses** (B1654's item 10) | (a) det Y(a; u) = (a·a)(u·u)(a·u) for five seeded random complex a and u, to 10⁻⁴⁰ relative; (b) under P4, L·s₃/s₁ equals \|a·a\|\|D\|\|a·R\|/(2πσ₁²σ₂) within 10⁻² relative at L = 10⁴, and the error falls by a factor between 5 and 20 from L = 10³ to 10⁴, for the three directions at the three fibres | 85% |

**C5 is a reading** (derivation 4) and has no prior.

**The read-outs (no prior).**
- c_r at every τ.
- The grid's smallest far value, and where it lies.
- The exact directional slopes of |D|/|R|² at ω: the smallest and largest over directions of δτ, per unit |δτ|, from
  derivation 2. B1654's N5(c) window is [1.8, 3.4], and main's near-corner nodes read 2.70 and 2.93.

## What a failure would say

- **C1** fails if the closed form is wrong, or if the strip-to-disc conversion is. Route C against A tests the product
  identities; route B against A tests the whole derivation.
- **C2(d)** fails if the hand expansion's next order is wrong. The constant K is then still tested by (b) and by the
  limit.
- **C3(a)** fails on a channel-assignment slip between B1651, B1654 and W85.
- **C3(c)** fails if the leading order is slower than claimed at L = 10⁴.
- **C4(b)** fails if B1654's item-10 limit is wrong, or if the approach is not 1/L.

## After the run

- Record in the weave dossier's NOTE (section W87, the table), CHANGELOG, PROGRESS_LOG, the state page, and relay
  §114 to main (copied to chat1 and the audit lane), with a ledger extension.
- A test in `tests/test_b1552_the_chiral_triplets_count.py` that reads the JSON and recomputes the closed form against a
  short quadrature in process.
- A failed prediction is recorded as failed. Any further check is labelled post hoc.

0 of 19.
