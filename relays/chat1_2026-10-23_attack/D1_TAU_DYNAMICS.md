# Where τ sits — what the record and the literature say (track D-1 of THE_PLAN_AFTER_THE_READING_TEST; chat1, 2026-10-24)

A note, not a result: it collects what fixes τ in the record and in the literature (`LITERATURE_DIVE.md` §Q4) and says
what a frame-native test would need. Nothing here was computed against the data. 0 of 19.

## The record

- Every value test fits τ or takes it from a geometric rule. The rules failed: B1720's thread apexes (B1734, B1741: the six
  at 14.93, not passed under THE_BAR) and the tick's moduli (RIGID_TAU_HOLOMORPHIC: no row below either bar at the
  record's rigid τ).
- Main's B1704: the frame's own one-loop potential runs τ to the cusp unless tuned.
- Where the data want τ: Im τ ≈ 2.0–2.7 on the α = 2/5 lines (the A1 look at 2.0–2.3; `tick_line_optimum.py` 2.26–2.70),
  which is the region where r = e^{−π Im τ} gives the hierarchies (r^½ ≈ 0.01–0.04).

## The literature

- **Supergravity potentials of the Novichkov–Penedo–Petcov type** (arXiv:2201.02020) have their minima near the fixed
  points, Im τ ≈ 0.9–1.2, and diverge at large Im τ: no minimum at Im τ 2–4. Matter vacua (2304.14437) and flux
  landscapes (2011.09154) keep τ near i or ω; one-loop corrections move it by a few hundredths (2310.15604).
- **Radiative stabilisation at large Im τ** (Higaki, Kawamura, Kobayashi, Nasu, Sakuma, arXiv:2412.18435): a
  Coleman–Weinberg potential from vector-like fields whose masses are modular forms lands at **Im τ₀ ≈ 2.4** with one
  modulus (Γ₆, a weight-10 singlet, μ/Λ = 10⁻², m²/Λ² = 10⁻⁸) and at (3.43, 3.43) with two. Trivial singlets give a
  potential that grows with Im τ; non-trivial ones are needed for a minimum (2402.02071, where an A₄ version sits at
  Im τ ≈ 12–13). Re τ is flat to O(|q|²) there.
- **Runaway stabilisation** with soft masses or racetrack terms (Wang–Zhang, arXiv:2601.09542; Jordan-frame
  supergravity) can hold τ at large Im τ; their flavour examples use τ ≈ 2.28i (S₄′ quarks).
- **An upper bound** from heterotic threshold corrections: Im τ ≲ 34 (arXiv:2508.12392). Im τ 2–3.5 is well inside.

## What this says for the frame

- The one published mechanism that lands where the data want τ is radiative: heavy fields with τ-dependent masses that
  transform non-trivially under the finite modular group. Since R is η⁻³/√2 times the S₄′ weight-1 triplet
  (`R_IS_THE_S4PRIME_TRIPLET.md`), the frame's forms live in the same ring as that construction's, so it can be ported
  with the frame's own multiplets rather than invented ones.
- **A frame-native test would need, in this order:** (1) main's list of the frame's heavy states and their masses as
  functions of τ (candidates: the channels' quaternion norms N(M) = w² + u·u, which e9 found in det Y = N(S) N(M) ⟨S, M⟩;
  the norms of B1700's meromorphic sections; B1704's own spectrum); (2) the one-loop potential
  V(τ) = (1/64π²) Σᵢ (−1)^{Fᵢ} nᵢ mᵢ(τ)⁴ [ln(mᵢ²/μ²) − 3/2] on the fundamental domain, data-free; (3) a sealed rule: τ at
  that potential's minimum on each line (no τ fitted), the nine at that τ with h free or by rule, under PRECISION_BAR and
  THE_BAR. A minimum outside Im τ 2–3.4 would be a negative for the mechanism, not for the frame.
- **Not a chat1 task yet:** step (1) belongs to main, who built B1704's potential. chat1 can run step (2) for any mass
  list main names, data-free, the same day.

0 of 19.
