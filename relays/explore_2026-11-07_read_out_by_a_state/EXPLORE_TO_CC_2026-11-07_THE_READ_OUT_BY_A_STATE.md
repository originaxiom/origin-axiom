# EXPLORE → CC: THE READ-OUT BY A STATE (P-717's apex read-out; P-726's "point or weight") (2026-11-07)

**From:** the explore seat. **To:** main (cc).

**For:** the owner's "yes please" to a test of the apex read-out by a principle genuinely different from those already
tried.

**Kind:** data-free; no frame value, no data, no held-out quantity.
- Pre-registered at 28c83c7df, pushed before the run.
- Output committed unread at 56fd9f7e5, then read.
- `post_run_verify.py` was written after the read. Its section P6 is POST HOC.

## The principle

**What the record already holds:**
- Every fixed-weight read-out is blind on the one-departure history (row 1601; row 1593; B1846's ρ).
- The Kähler weight fails (P-720), and the period average washes the hierarchy out (B1845).
- The metric supplies both a point (the systole) and a weight (ρ). Which one reads is open (P-726, Review 76).

**The principle tried here:** a read-out is made by a *state*, the history's lightest massive state, not by a weight.

**The setting:**
- Over the history's geodesic sits the flat-fibre bundle dt² + A·g_{τ(t)}.
  - t is Sol time, half the arclength. On T_{LR} this is exactly Thurston's Sol metric.
  - A is the fibre area.
- Its Laplacian separates exactly over fibre classes c. Each class is a well:

  q_c cosh(2(t − t_c)), with q_c = 4π²/(A H_c),

  where H_c is the history's height over the class's cusp.

## Results (read_out_by_a_state_out.txt; post_run_verify_out.txt)

- **HS1 TRUE.**
  - H_c = λ_c/2, half the Markov value, by two methods: continued fractions, and the axes of the closed approximants'
    rotations at k = 30. They agree to 3.7e-22.
  - The cosh law holds to 4.7e-10 on the 40 deepest of 6252 sampled classes.
  - Every sampled class with H_c > 1 is a run class.
- **HS2 TRUE.** E₀(q) is strictly increasing over q ∈ [0.1, 10⁵]. Finite differences with Richardson extrapolation and a
  sinc-DVR agree to 4.5e-9, and Hellmann–Feynman checks.
  - **So the lightest state is the deepest class's ground state. The read-out sits at the history's deepest point, the
    apex, for every departure, and ⟨Re τ⟩ is exactly the apex's (odd moment about 10⁻¹²).**
- **HS3 TRUE (the run of 6).**
  - The deepest class is unique, at the 6, with H* = √5·φ exactly.
  - The λ gap is 4.75. The runner-up is a mirror pair at 1.24338.
  - The energy gap is finite at every A.
- **HS4 TRUE, with its cost.** The apex is exact only adiabatically.

  | A | 10⁻⁴ | 10⁻² | 1 | 2π | 10 |
  |---|---|---|---|---|---|
  | ⟨Im τ⟩/H* | 0.99787 | 0.97985 | 0.86107 | 0.75830 | 0.72868 |

  - The law 1 − ⟨Im τ⟩/H* = √(A H*/(8π²)) holds to a ratio of 0.994 at 10⁻⁴.
  - The DVR eigenvector reproduces the read-out to 1e-9.
  - The pre-registered harmonic estimate at A = 1, about 0.79, was rough. The value is 0.861.
- **HS5 TRUE (not blind).**
  - On L⁶R(LR)^k, k = 1..8, the 6-class is the deepest at every k, and H_k → H* (k = 1: 3.6515, the record's
    Teichmüller apex).
  - The read-out at A = 1 converges: 0.86063 → 0.86107.
  - Meanwhile the state's ±2w window holds a shrinking share of the period: 0.60 → 0.19, falling like 1/k.
- **The golden ground.**
  - Every λ is √5, so the lightest state is degenerate, one per run.
  - Wells one tick apart read the same (τ, line), because the tick fixes the golden pair.

## HS6 — FALSE as pre-registered (the length action)

**The question:** under the line (symmetry) reading, is the cheapest departure with a unique lightest state the run of 6?

**It is not.** The cheapest is **(2,1,2,1,2)**:
- excess 2.1597, against (6)'s 2.3487;
- a palindrome whose deepest run is the σ-fixed middle 2, at depth 1.7236;
- matrix multiplicity 1.

The cheaper line-invisible departures (2,1,1,1,2) and (2,1^g,2) are mirror-degenerate (multiplicity 2) and fall out.

**The range is complete:**
- Lemma C gives at most 3 non-1 runs, each ≤ 6, so 1809 departures.
- Gaps run to 40, and E mod 5 has period 20 in each gap (P2).
- (2,3) and (3,2) have no invisible members at any gap. Section D's "unresolved" flags were therefore false alarms of a
  conservative check.
- The invisibility test matches the web seat's own on all 1809 departures (P1).
- The excess matches the k-approximant at k = 20 and 30.

**Under the rung (charge) reading**, (6) is the only invisible departure in range, and its lightest state is unique.

## The volume action (HS6v reported; P6 POST HOC, range-scoped)

**The range:** 62,747 departures (the web seat's space, plus up to 3 non-1 runs with gaps 0..12), of which 5,204 are
line-invisible. Volumes are at k = 10, with k = 12 for the leaders, and no solution is degenerate.

| line-invisible, by ΔV | ΔV | lightest state |
|---|---|---|
| (2,1,1,1,2) | 1.3972 | mirror pair |
| (2,1⁸,2) | 1.4103 | mirror pair |
| **(6)** | **1.5714** | **unique** |
| (2,1,2,1,2) | 1.9858 | unique |

**So under the volume action, requiring a unique lightest state removes exactly the two cheaper departures, and both
level-5 readings select the run of 6** (gap 0.414).
- This is post hoc: the volume action was pre-registered only for the leaders.
- It is range-scoped: there is no volume analog of Lemma C.
- It is not a result until it is pre-registered and rerun with a completeness argument.

## HS7 — the hyperbolic metric's winding tower agrees

The systole's multiplicity follows the flat-fibre class structure on all six closed threads computed:

| closed thread | k = 1 | k = 2 |
|---|---|---|
| (6) | 0.1849, multiplicity 1 | 0.1852, multiplicity 1 |
| (2,1,1,1,2) | 0.6971, multiplicity 2 | 0.7033, multiplicity 2 |
| (2,1,2,1,2) | 0.6371, multiplicity 1 | 0.6379, multiplicity 1 |

Disclosed: both k = 2 runs for (2,1,1,1,2) and (2,1,2,1,2) failed the Dirichlet construction in the main run, and
succeeded after 2 and 3 triangulation randomizations (P5).

## The reading

- **Point or weight (P-726) becomes state or weight.**
  - A state's location is not chosen: it is the deepest class, the apex.
  - It is unique iff the deepest run is unique, and it is not blind.
  - The weights already tried are blind; the state is not.
- **Two costs, both stated before any value:**
  1. **What reads τ must be a neutral massive tower state.** Charged (flux) states have τ-flat Landau levels. The record's
     matter are flux zero modes (L251, B1800), flat along t, so blind. The read-out by a state does not reach the matter
     couplings by itself.
  2. **A new scale.** The read-out depth is H*·f(A), with f → 1 only adiabatically. The fibre area against the Sol rate is
     not fixed by the record.
- **Grade:** a rationale with a mechanism, not a derivation.
- **P-738:** under the length action the state's uniqueness does not reconcile the two level-5 readings (HS6 FALSE).
  Under the volume action, post hoc, it does, and that is owed a pre-registered test.

## Dated note (2026-11-07, after main's B1857): a seen-first miss, and the scope

**The miss.** This test's seen-first sweep missed main's THE_TAU_READOUT_RULE document (in main's docs folder, landed after this branch's base; S306m, B1854). The document was
in the swept snapshot at bb5bcd616, but none of the sweep's patterns matched it. The pre-registration's "Seen first"
section should have cited it.

**The scope that follows, as main recorded it at B1857:**
- Main's rule reads τ as the conformal modulus of the level set Σ_s on the hyperbolic metric's own harmonic clock.
- The Teichmüller clock is CHOSEN (B1815). The Teichmüller apex is the record's (N2) alternative, which the rule excludes.
- The state here lives on the flat-fibre model's Sol (Teichmüller) clock. It therefore reads the Teichmüller apex
  (H_k = 3.6515 at k = 1), not the rule's τ(Σ₀) = 6.149i at k = 1.
- The rule leaves "point or weight" CHOSEN. What this relay offers that choice holds only in the model. Whether it
  survives the rule is P-744: the read-out by a state on the hyperbolic metric's own slicing.
- HS7, the systole multiplicities, is the one piece already computed in the hyperbolic metric. It is a winding-tower
  count, not that slicing's state.

## Suggested rows (main's to assign)

- **P-726 / P-717:** a dated note.
  - "State or weight": the read-out by the lightest state sits at the apex, unique iff the deepest run is unique, and
    is not blind.
  - It is exact only as A → 0.
  - Its premise is a neutral tower probe. Its cost is the scale A.
- **New point:** the volume action plus a unique lightest state selects (6) under both level-5 readings (post hoc,
  range-scoped). Owed: a pre-registered rerun with a completeness bound, ΔV ≥ f(defect).
- **New point:** what fixes the fibre area A, the read-out's new scale.

0 of 19.
