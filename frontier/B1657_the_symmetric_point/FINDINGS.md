# B1657 — THE SYMMETRIC POINT: at τ = ω the Higgs's symmetric vacua are the three axes of B1646's frame; the two isotropic ones are rank one, and a small departure obeys one of two laws — the conjugate vacuum's light masses are the two isotropy defects, the parallel vacuum's are their sum and product, a geometric hierarchy

**Verdict: PROVED.** Every cell holds as sealed. cc (main), 2026-10-15.
- Sealed `d4dcd0d50` (sha256 1e0a4bc9) before the run. The output was committed unread at `ab392d4da` (one run, 18 s,
  exit 0; the instrument unchanged since the seal, sha256 012bcf6d).
- No data. **0 of 19.** No cell was blind: every value was seen before the seal (§0b), and the arc's worth is the
  certified statement and its lock.
- POINT_REGISTER P-153 (main's audit of its negatives, B1655: the isotropic Higgs directions never tested as vacua; the
  near-ω regime uncomputed). The fibre frame, untwisted, one fibre and one τ at a time: a frozen piece.

## 0. Seen first

As sealed: `VERDICT topic-sweep /symmetric point|isotropic (vacu|eigenline|direction)|rank one at|two (isotropy )?defects|isotropy defect|order-3 (move|automorphism)/: 5 of 1427 arcs on main match (PROVED 5)`.
The precedents read (the preregistration's §0): B1645 (rank one on the whole cone; T4's ½ bound), B1646 (the frame
(R/∣R∣, R̄/∣R∣, n); s₁s₂ = ∣R∣²∣a·a∣), B1651 (the body diagonals), B1640 §2, B1630, B1654 (D and its `two_defects`
exploration), and the SM seat's W87 (D in closed form, the slope at ω). **Literature:** P is Γ(4) ≅ S₄'s order-3 element
in its triplet (the near-fixed-point mechanism of Novichkov, Penedo and Petcov).

## 0b. Disclosed

In full in the preregistration's §0b: main's exploration (four scripts, beside the seal); v1 run twice (two errors of
main's draft corrected), v2 run twice; two passes of read-only reviewing agents. The first found the blocker that shaped
this arc — the two-defect law holds only in the conjugate vacuum — and main derived the parallel vacuum's law in answer;
the second found no blocker and re-derived the parallel law independently. Their scripts and v1 are beside the seal.

## 1. The sealed run (`verification/the_symmetric_point.py`, unchanged; `.json`, `_run.txt`)

**S0, plumbing** (not void): theta series against jtheta 2 × 10⁻¹⁶; ∣R·R∣/∣R∣² 1.9 × 10⁻¹⁶; B1654's c_r at ω equal to
1.4 × 10⁻¹⁴; W87's closed-form D against B1654's stored D 1.3 × 10⁻¹⁴.

| cell | prediction | identity or test | result |
|---|---|---|---|
| **S1**, the move | M fitted; M = P in R's basis; PᵀP = 𝟙, P³ = −𝟙; R, R̄, n eigenvectors (e^{∓iπ/3}, −1); Y covariant; controls | (a), (b), controls tests | **HOLDS:** fit 3.5 × 10⁻¹⁶; ∣M − P∣ 4.8 × 10⁻¹⁵; eigen-residuals ≤ 4.3 × 10⁻¹⁶, arg −⅓π; covariance 8.9 × 10⁻¹⁶; generic-τ control 0.590; graded ratios 10.18, 10.03, 10.004 |
| **S2**, the symmetric vacua | n: (1, 1, 0); R, R̄: (1, 0, 0); the same under P4; real directions s₂/s₁ ≥ ½ | spectra identities (B1645) | **HOLDS:** n (1, 1 − 6 × 10⁻¹⁶, 1.1 × 10⁻¹⁶); R, R̄ ≤ 3.2 × 10⁻¹⁶; control [0.5000041, 0.846] |
| **S3**, two laws | det Y = (a·v)(a·a)(v·v); conjugate law < 0.05/ε; parallel laws < 100/ε; cross-controls > 100 | (c), (d), cross-controls tests | **HOLDS:** det 2.9 × 10⁻¹⁵; conjugate 0.0080; parallel 27.5 (m₂) and 13.5 (m₁); conjugate law in the parallel vacuum 9.5 × 10³, parallel law in the conjugate vacuum 1.2 × 10⁷; normalisation control 0.75 |
| **S4**, the canonical end condition | Higgs on R̄ or R: s₃ = 0; L·s₂/s₁ → ∣D∣/(2π∣R∣²) or ∣D∣/(8π∣R∣²) within 10⁻³; zero at ω | (b), (c) tests | **HOLDS:** s₃/s₁ ≤ 1.9 × 10⁻¹⁶; the limits to 1.5–1.7 × 10⁻⁴ (relative); ω 6.6 × 10⁻¹³ |
| **S5**, D near ω | D(γτ)(τ + 1) = −D(τ); ∣D∣/(∣R∣²δ) isotropic, its mean W87's slope within 10⁻⁵; negative controls > 0.1 | (b)–(d) tests | **HOLDS:** covariance 2.2 × 10⁻¹⁴; spread 7.5 × 10⁻⁴ (from 3.0 × 10⁻³ at 10⁻³); mean vs 2.9491720: 1.6 × 10⁻⁷; controls 1.38 (i), 0.70 (t1) |

**Read-outs.** The conjugate limits ∣D∣/(2π∣R∣²): 0.17329 (i), 0.15852 (t1), 0.06587 (t2), 0.02032 (t3); the parallel
ones a quarter of each. Along the cone at t1, genuine isotropic Higgs directions a(s) = R̄ + s n − (s²/2)R give
L·s₂/s₁ = 0.146, 0.111, 0.079 (s = 0.3, 0.7, 1.2) with s₃ = 0: the zero belongs to the whole cone, the limit to the
line. arg κ reads π/4 in this convention (it moves with R's phase, so it is not a physical number).

## 2. What it shows

- **At the weave's order-3 point the Higgs's symmetric vacua are B1646's three axes.** The real one, n, gives the
  degenerate pair (1, 1, 0) — B1645's T4. The two isotropic ones, R and R̄, give rank one: one heavy generation and two
  massless. So τ = ω, retired only as "no hierarchy found" (B1640), has rank-one vacua in this frame; what the record
  tested there (real directions, and the weave's tensors with the inner automorphisms) did not include them.
- **Two laws for a small departure.**
  - **Conjugate vacuum** (a ≈ R̄, v ≈ R): the two light masses over the heavy are the two isotropy defects, ∣d_a∣ and
    ∣d_v∣, with coefficient one. The Higgs and the zero-mode triplet enter symmetrically (Y(a; v) = Y(v; a)).
  - **Parallel vacuum** (a ≈ R, v ≈ R): they are ∣d_a + d_v∣/4 and ∣d_a d_v∣/4, the defects' sum and product. One small
    breaking gives ε² : ε : 1, with m₁m₃/m₂² = 4∣d_a d_v∣/∣d_a + d_v∣² fixed by the ratio of the two defects.
  - Each law fails in the other's vacuum by orders of magnitude (the cross-controls), so the vacuum matters.
- **Under B1654's canonical end condition**, with the Higgs on either isotropic line, one generation is exactly massless
  at every τ, and the next is ∣D(τ)∣/(2πL∣R∣²) (conjugate) or a quarter of it (parallel). Near ω, by D's covariance,
  that is a cone: ∣κ∣∣τ − ω∣/(2πL) with ∣κ∣ = (π²√3/6)∣θ₃(ω)∣⁴ = 2.94917 (W87's slope).
- **So the hierarchy is the distance from the symmetric point, in two defects.** At ω on an isotropic line both vanish.
  The matter's defect is the end condition's D(τ)/(2πL) — known. The Higgs's defect needs the Higgs's own section or
  potential — not computed. Which vacuum is the Higgs's is a question of its weight (k ≡ 1, 3, −1 mod 6 → R, n, R̄; a
  reading, frame-dependent).

## 3. What it does not show

Which vacuum, which weight, or how near the line the Higgs sits; the sectors (untwisted here; the twisted channels are
B1656's, where the electron's first generation stays massless on W59's lines); the interacting weave; any value; the
Cabibbo angle (at first order the untwisted light states are R and R̄, or R and n).

## 4. Credit

Main's two read-only reviewing agents: the first found the scope blocker that led to the parallel law, the covariance
identity, the weight-selection reading and the precedents; the second re-derived the parallel law and the selection rule
near ω. The SM seat: W87's closed forms, which S5 tests.

## 5. Next

The Higgs's defect (P-163): its covariant section a(τ) of a given weight near ω, or its one-loop potential (B1655's
check put minima between the cone and the real locus) — with B1656's sector values, the first computation that could
turn this frame's structure into ratios of masses.
