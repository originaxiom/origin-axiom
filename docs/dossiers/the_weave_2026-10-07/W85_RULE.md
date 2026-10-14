# W85 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat read and worked by
hand while drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a
result.

## Why this arc

- **The owner's rule: verify load-bearing math.** Main's B1651 ("where a Higgs can couple the zero modes", sealed at
  6d6f7f660, not yet run) is the first item of the owner's order P-136, "B1651, then the frame tribunal, before any
  further number-chasing". Its cells U3, U4 and U5 carry the reading the tribunal will use: no constant direction in M
  is covariant, and modulo the Klein group only the four body diagonals are.
- **§107 told main this seat would check U1–U5 on its own code.** Doing it now, before main's run lands, keeps the
  check blind to main's output. The cells are identities and exact group facts, so the check is of main's instrument and
  conventions, not of a fit.

## Weave or thread?

- **Weave-type, as B1651:** the zero modes are the weave's T on the fibre every thread shares, and the moves are the
  weave's L and R. The check reads one τ at a time, at random τ, and the claims are identities in τ.

## Seen before the rule (disclosed)

- **Main's B1651 preregistration, its instrument `where_a_higgs_couples.py` and its controls, read.**
  - The conventions: the π z convention (periods π, πτ), units (i, j, k) ↔ thetas (2, 4, 3), c = (−1, −1, i).
  - θ₁ and θ₂ are built from θ₄ and θ₃ with the nome root q^{1/4} := e^{iπτ/4} explicit, since mpmath's principal root
    puts −i on them when Re τ > 1.
  - The lifts g_L = (1 + i)/√2 and g_R = (1 − j)/√2 act on M as the quarter-turns about e_i and about e_j. The moves are
    L: τ ↦ τ + 1, z ↦ z, and R: τ ↦ τ/(τ + 1), z ↦ z/(τ + 1).
- **The seat's own hand derivations while drafting** (from the textbook transformation laws of the four thetas):
  - Under L, v(z | τ + 1) = e^{iπ/4}(v_i, v_k, −v_j)(z | τ) at every z, which is B1651's step 4.
  - Under S, v(z/τ | −1/τ) is a scalar times (v_j, v_i, v_k)(z | τ), the i–j swap that W64's K2 found for R(τ).
  - At the half-periods v is (θ₃θ₄/θ₂)(0, −1, i), (θ₂θ₃/θ₄)(i, 0, 1) and (θ₂θ₄/θ₃)(i, −1, 0), so its direction is
    independent of τ.
  - Under R = S T⁻¹ S, the composite of the two laws is (v_i, v_j, v_k) ↦ (−v_k, v_j, v_i) up to a scalar, the
    quarter-turn Ad(g_R) about e_j; the point goes to −z/(τ + 1), and v is odd.
  - Each unit's multipliers under z ↦ z + π and z ↦ z + πτ are (+, −), (−, +) and (−, −) for i, j and k.
- **The seat's own record that bears on it:**
  - W64's K2 failed as worded on mpmath's principal nome root, the trap B1651 discloses. Its labelled post hoc (PH2),
    on the direct series, found R(τ + 1) = e^{iπ/4} L⁻¹ R(τ) to 3 × 10⁻³¹, with L⁻¹ = [[1, 0, 0], [0, 0, 1],
    [0, −1, 0]], and R(−1/τ) = (−iτ)^{−½} P R(τ), with P the i–j swap.
  - W64's K1: the moves generate the cube group O on M. Its banked matrices, read while drafting, are
    L = [[1, 0, 0], [0, 0, −1], [0, 1, 0]] and R = [[0, 0, −1], [0, 1, 0], [1, 0, 0]]. By hand these are Ad(g_L)
    and Ad(g_R), so V6 below is known by hand.
  - W82: lemma A's commutants (V₄ makes a charge diagonal, S₃ makes it constant).
- **Nothing has been computed** for this arc.

## The method (fixed here)

- **The thetas are the seat's own:** each of the four is summed from its q-series at 60 digits, with q = e^{iπτ} and
  the nome root e^{iπτ/4} explicit, so no principal branch enters. A control compares them with mpmath's `jtheta` at
  |Re τ| < ½.
- **The triplet:** v_r(z | τ) = c_r θ_r(0 | τ) θ_r(z | τ) / θ₁(z | τ), with B1651's c and unit order. At the puncture it
  is the residue triplet, c_r θ_r(0)² / θ₁′(0).
- **The points:** the four fixed points 0, π/2, πτ/2 and π(1 + τ)/2, and three generic points π(m + nτ) with fixed
  lattice coordinates (m, n): (0.13, 0.29), (0.41, 0.07) and (0.23, 0.61).
- **The fibres:** five random τ (seed 85) with |Re τ| ≤ ½ and 0.8 ≤ Im τ ≤ 1.8.
- **The moves' matrices on M** are B1651's: Ad(g_L) and Ad(g_R), as 3 × 3 rotations. The V₄ elements are the
  half-turns diag(1, −1, −1), diag(−1, 1, −1) and diag(−1, −1, 1).
- **R's point.** B1651 writes it as z/(τ + 1). This rule uses −z/(τ + 1), the composite of the laws. Since v is
  odd, the sign changes only the scalar.
- **U1 is not re-run.** It is the residue theorem, and a quadratic differential's coefficient scaling by λ, both by
  hand.
- **An overlap** is |⟨u, w⟩| / (|u| |w|).

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **V0, the multipliers** | each unit's pairing function has multipliers (+, −), (−, +) and (−, −) for i, j and k under z ↦ z + π and z ↦ z + πτ, to 10⁻⁴⁰, at every τ and generic point (B1651's U2) | 99% |
| **V1, isotropy (an identity)** | \|v·v\| / \|v\|² < 10⁻⁴⁰ at all seven points at every τ | 99% |
| **V2, the half-periods** | the triplet at π/2, πτ/2 and π(1 + τ)/2 has overlap > 1 − 10⁻⁴⁰ with (0, −1, i), (i, 0, 1) and (i, −1, 0) at every τ; at the puncture and the generic points the best overlap over V₄ between two τ is < 1 − 10⁻⁶ | 97% |
| **V3, L carries the triplet** | at all seven points, v(z \| τ + 1) = e^{iπ/4} Ad(g_L)⁻¹ v(z \| τ) to 10⁻⁴⁰ relative (at the puncture, the residue triplets), with no V₄ element; the half-periods' classes go as B1651 predicts | 97% |
| **V4, R carries the triplet** | at all seven points, the triplet at −z/(τ + 1) on the fibre τ/(τ + 1) (the residue triplet at the puncture) is proportional to Ad(g_R) v(z \| τ), with overlap > 1 − 10⁻⁴⁰ and no V₄ element; the scalar is one number at the six regular points; the half-periods' classes go as B1651 predicts | 90% |
| **V5, the group** | Ad(g_L) and Ad(g_R) generate 24 rotations; the elements fixing the three axes' classes are exactly V₄, and the image on them is S₃; over the 16 V₄-twisted pairs exactly four lines are common eigenlines, and they are the body diagonals (ρ, σ, 1), ρ, σ = ±1 (exact, in integers) | 95% |
| **V6, the seat's own record agrees** | B1651's Ad(g_L) and Ad(g_R) equal W64's banked L and R on M, which come from the common point's AUT, and V3's matrix at the puncture equals W64's post hoc τ + 1 matrix (exact, in integers) | 99% |

**The read-outs (no prior).** Each point's residual in V3 and V4, the scalar λ for R, and for each power of each move
every V₄ element whose overlap passes 1 − 10⁻¹².

## What a result means, fenced

- **If V1 to V5 hold,** B1651's U3a, U3b, U4 and U5 hold on a second instrument, with conventions fixed independently.
  The tribunal can lean on "no constant direction in M is covariant; modulo V₄ only the body diagonals are".
- **If V3 or V4 fails,** the seat says which convention differs (the lift's V₄ twist, a sign in c, or the nome root)
  and whether the failure changes B1651's reading or only its labels.
- **In every case:**
  - B1651's premise P1 is untested here, as there;
  - the count is unchanged, 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Main's output is not read before the run.** If it lands first, the seat records that and does not open it until
  this run's output is committed.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
