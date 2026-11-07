# THE READ-OUT BY A STATE (P-717's read-out) — pre-registration (the explore seat, 2026-11-07)

**For:** the owner's "yes please" (2026-11-07) to a test of the apex read-out by a principle genuinely different from
those already tried.

**Kind:** data-free. The script uses only:
- the hyperbolic geometry of the history's geodesic;
- the separated Laplacian of the flat-fibre bundle over the history;
- SL(2, ℤ/5) arithmetic;
- SnapPy length spectra and volumes.

It uses no frame value, no data and no held-out quantity.

**Written before** `read_out_by_a_state_check.py` is run. Its output is committed unread, then read.

## Seen first (swept 2026-11-07 over main's docs at bb5bcd616)

**What the record holds on the read-out:**
- **Point or weight is the remaining choice** (P-726, as corrected at Review 76).
  - The metric supplies a canonical point, the systole at the tube, and a canonical weight, ρ.
  - On L⁶RLR both sit at the tube. Which one the read-out uses is still open.
- **Fixed weights are blind** to the departure on the one-departure history:
  - every fixed-weight read-out (row 1601);
  - the arclength average (row 1593);
  - ρ, which dilutes like 1/k (B1846).
- **The symmetry** τ ↦ n − τ̄ fixes exactly one point of the history, the apex. With a point read-out, Curie's argument
  gives the apex (row 1593). That is a symmetry criterion, not a derivation.
- **Two routes failed:**
  - the Kähler weight is k = 1, far below the w ≳ 8 a read-out needs (P-720, NEGATIVE);
  - P-455's period average washes the hierarchy out (B1845).
- **Zero modes:** localizing them along the circle "needs a kinetic structure the record lacks" (P-717 S305q; FL-05).
  - The couplings, read as overlaps of the fibre's flux zero modes, are L251 and B1800.
- **Heights:**
  - apex heights are half the Lagrange values (row 1161);
  - the golden loop is Hurwitz-extremal, the bottom of the Lagrange spectrum (THEOREM_LEDGER C2);
  - in the fibre's Sol geometry, the position along an axis is a gauge (row 1450).

**Not found:**
- a read-out made by a *state* rather than a weight;
- the exact separation of the flat-fibre bundle's Laplacian, along a history, into one well per fibre class;
- the uniqueness of the lightest state as a criterion on departures;
- the finite-fibre smearing of the read-out.

## The principle and its setting

**The principle:** a read-out is made by a state, namely the history's lightest massive state, not by a weight laid
along the history.

**The bundle.**
- Over the history's geodesic τ(t) sits the bundle T² × ℝ with metric dt² + A·g_{τ(t)}.
  - g_τ is the unit-area flat metric of modulus τ, and A is the fibre area.
  - t is Sol time, half the hyperbolic arclength s.
  - On the closed golden bundle T_{LR} this is exactly the Sol metric, Thurston's geometry of that bundle.
- Its Laplacian separates exactly over fibre classes c = (m, n):

  H_c = −∂_t² + (4π²/A) ℓ_c(t)², with ℓ_c² = |mτ − n|²/Im τ.

- Along a geodesic, ℓ_c(s)² = cosh(s − s_c)/H_c, where H_c is the history's greatest height relative to the cusp of c.
- So each class is a confining well q_c cosh(2u), with q_c = 4π²/(A H_c) and u = t − t_c.
- The lightest massive state belongs to the deepest class.

**Why this is not one of the weights already tried:** the state's density is set by the history itself. It is not a
fixed weight, so row 1601's no-go does not cover it.

**Stated before any value:**
1. The principle reads τ through *massive neutral* tower states. Charged (flux) states have τ-independent Landau levels,
   and the record's matter are flux zero modes, which are flat along t. So the premise is a choice about what reads.
2. A, the fibre area against the Sol rate, is a free scale. The record does not fix it.

## Hypotheses, before computing

- **HS1 (exact).**
  - Each run's class has H_i = λ_i/2, where λ_i = a_i + [0; a_{i+1}, …] + [0; a_{i−1}, …]. Two methods are used:
    continued fractions on the bi-infinite history, and the axis of each cyclic rotation of a closed approximant at
    k = 30. They agree to 10⁻²⁰.
  - Every sampled primitive class obeys ℓ_c(s)² H_c = cosh(s − s_c), to a relative residual below 10⁻⁹.
  - The largest H_c over the sampled classes is max_i λ_i/2. *Likely:* every sampled class with H_c > 1 is a run class.
- **HS2 (exact).** The ground energy E₀(q) of −ψ'' + q cosh(2u) ψ is strictly increasing in q.
  - Finite differences with Richardson extrapolation and a sinc-DVR agree to 10⁻⁷.
  - Hence the lightest massive state is the ground state of the deepest class. It is unique iff the deepest run is
    unique.
- **HS3 (the run of 6).**
  - The deepest class is unique, at the 6, with H* = (5 + √5)/2 = √5·φ (to 10⁻⁴⁰).
  - The runner-up is a mirror pair at λ/2 ≈ 1.243.
  - The lightest state is unique, with a finite energy gap at every A.
- **HS4 (the read-out).**
  - ⟨Re τ⟩ is exactly the apex's Re τ, because the class well is symmetric about t_c.
  - ⟨Im τ⟩/H* → 1 as A → 0, with 1 − ⟨Im τ⟩/H* = √(A H*/(8π²))·(1 + o(1)), checked to within 2% at A = 10⁻⁴.
  - At A = 1 the harmonic estimate is about 0.79 (reported).
- **HS5 (not blind).**
  - On the closed approximants L⁶R(LR)^k, k = 1..8, the 6-class stays the deepest, and H_k → H*.
  - The lightest state's read-out converges with H_k.
  - The share of the period's arclength inside the state's window falls like 1/k.
- **HS6 (the risky one). Among line-invisible departures** (E ∈ ±⟨LR⟩ mod 5, the symmetry reading) with excess length up
  to excess(6), **is the cheapest one whose lightest state is unique the run of 6?**
  - **Prior: about 25%.** A two-run departure (2, 1^g, 3), line-invisible at some g, would cost about 2.0, below 2.349.
  - Also checked: among rung-invisible departures (the charge reading), (6) should be the cheapest, and its lightest
    state unique.
- **HS6v.** HS6's leaders under the volume action: SnapPy closed approximants at k = 10 and 12 (reported).
- **HS7 (the winding tower in the object's hyperbolic metric, reported).** The shortest geodesic of the closed threads
  of (6) at k = 1, 2 is unique. For (2,1,1,1,2)'s threads, and for HS6's winner, the prior is open.

**Range for HS6.**
- Departures are L-start with first and last runs ≥ 2. They have at most K non-1 runs, each ≤ r_max, with gaps of
  0..40 golden runs between them.
- K and r_max come from Lemma C: Q ≥ B(s) (P-737; the proof is cited, and its rebuild on main is owed as P-741).
  - B is checked on every enumerated departure.
  - Expected: K = 3 and r_max = 6 for excess ≤ excess(6) + 0.01.
- Any pattern whose large-gap limit, the sum of its single-run excesses, falls below the minimum found is reported as
  unresolved by the range.
- The excess comes from Lemma A, Q = vᵀEv/vᵀv with v = (1, φ), in 50-digit arithmetic. The leaders are cross-checked
  against the web seat's k-approximant excess at k = 20 and 30.
- Uniqueness means the largest λ_i over the history is attained once, with a gap > 10⁻³⁰.

## What follows

- **If HS1–HS5 hold:**
  - Under "the read-out is made by the history's lightest massive state", the apex read-out is where that state lives,
    not a convention.
  - It is not blind in the one-departure limit.
  - It is exact only adiabatically (A → 0). At finite fibre area the read-out is a smeared point on the apex's
    Re τ line, with its depth lowered by √(A H*/(8π²)), so one new scale enters.
  - The premise moves from "a point" to "a state". It is still a choice, and it does not reach the record's flux
    zero modes. Grade: a rationale with a mechanism, not a derivation.
- **If HS6 holds:** the state's uniqueness makes both level-5 readings select the run of 6, which gives P-738 a second
  ground. **If it fails:** the competitor is reported, and the charge reading stays needed, as B1856 found.
- **If HS2 or HS3 fails:** that would be an error in this setting, and it is reported as such.

0 of 19.
