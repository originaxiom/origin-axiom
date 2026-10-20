# B1673 — THE DYNAMICAL-SELECTION CLAIMS OF 19 OCTOBER, VERIFIED: τ = ω, the flat lines, CP and the masses are not derived — the potential's minimum is classical and chosen, the 12-point orbit is a fact but not the record's lines, the CP count is a coordinate error, and no spectrum comes near the data

**Verdict: NEGATIVE (a verification arc; what the arc claimed, that the static debts of Table 1 are discharged, does
not hold).** cc (main), 2026-10-20. POINT_REGISTER P-199. 0 of 19.
- **What this arc is.** On 19 October a separate session, working with the owner in main's working tree while main was
  away, wrote an arc under this number. It claimed, as PROVED and law-creating, that τ = ω, the flat hypercharge lines,
  CP violation and the fermion masses are derived. It also edited the paper's Table 1 and §8 to say so. The arc was
  never sealed and never committed. Main verified it claim by claim, and banks the verification under the same
  number, so the record keeps the number the owner knows.
- **The received files** are in `verification/as_received/`, unchanged. Their sha256 as received is in
  `SHA256_AS_RECEIVED.txt`. The paper edits are kept as a patch with B1672's received files. **None of them entered
  the paper.**

## 0. Seen first

`VERDICT topic-sweep /Casimir|Kronecker limit|Green function|torsion points|spontaneous CP|Jarlskog|Selberg|golden length|orbit averag/: 11 of 1445 arcs on main match (NEGATIVE 3, PROVED 8)`
— chiefly B1653 (rank at most two at a point), B1656 and B1660 (W59's eighteen lines at τ = ω), and B1640 (τ = ω
retired as "no hierarchy found"; GENESIS v1.35). The SM seat's W51 and W59 had already recorded that this functional is
stationary only at i (a saddle) and at ω. **Literature:** Im τ ∣η(τ)∣⁴ is, up to a constant, the regularised
determinant of the flat torus's Laplacian, which is extremal at the hexagonal torus (Osgood, Phillips and Sarnak, 1988).

## 0b. Disclosed

- **A verification, not a sealed test.** The received arc made claims after its computations. Main checked them
  afterwards, so nothing here was predicted blind.
- **Who checked.** One reading pass for main recomputed every claim with its own code (`verification/main_check/`).
  Main then rechecked the decisive one, the CP count, independently.

## 1. What was claimed, and what holds

| claim (as received) | result on main |
|---|---|
| V(τ) = −ln(Im τ ∣η∣⁴) has its unique minimum at ω, so τ = ω is derived | **The minimum holds, but it derives nothing.** V(ω) = 1.0335192760 and the gap to the saddle at i is 0.0211690050, as received. The extremum is classical (the torus determinant), and W51 and W59 had it. Calling this functional the modulus's potential is a choice. τ = ω gives no hierarchy, as before |
| The Kronecker-limit Green function's minimum over the 72 points of exact order 9 is a unique 12-point orbit, so the flat hypercharge lines are derived | **The orbit holds, but nothing is discharged.** G_min = −0.504572 on 12 points, with a gap of 0.0229. The restriction to exact order 9 is the input: over all 80 torsion points the 3-torsion lies lower (−0.549306). **None of the 12 is among W59's eighteen lines** (G there is −0.4817, −0.3455 and +0.644), so B1656 and B1660 do not transfer |
| 8 of the 12 ground points are CP-odd, so CP is broken spontaneously, J ≈ −0.0368 | **Refuted: a coordinate error.** The points are built as (aω − b)/9, but rotated and conjugated as a + bω. The received rotation and conjugation are wrong on 72 of 72 of its own points. On the true points, 0 of the 12 are fixed by any reflection, and the set is closed under all six reflections, so nothing is broken. J is 0 at every single point (rank two, about 10⁻³²). The orbit-averaged J reproduces −0.0368, but it is set by a hand-picked input matrix: real input gives +0.0325, and random input gives −0.051 to +8 × 10⁻⁵. Measured J is 3.1 × 10⁻⁵ |
| Averaging over the orbit lifts the rank to three, so the first generation is lifted | **Linear algebra, not a mechanism.** Rank at most two at a point is B1653. A sum of distinct rank-two couplings has rank three. The resulting ratios miss the data by one to two orders: m_c/m_t 0.78 (data 0.0036), m_u/m_c 0.36 (0.0017), m_s/m_b 0.47 (0.022), m_μ/m_τ 0.60 (0.059). The CKM entries are all 0.26–0.73 |
| Selberg amplitudes at the golden length s = 4 ln φ give a hierarchy and the CKM | **A miss, and a thread choice.** The ratios reproduce (0.565, 0.474). The "arena" is the 52 words of length at most 5 at one base point, and s = 4 ln φ is ℓ(LR), the length of one thread. Over s from 0.5 to 4, m₂/m₃ runs 0.46–0.64 and m₁/m₂ 0.10–0.56. The ratios move with the base point and with the phase factor. A ratio near ½ is not a hierarchy |

## 2. What it says

- **No static debt of Table 1 is discharged by this arc.** The paper's Table 1 and §8 stay as they were. The edits are
  declined and kept with B1672's received files.
- **What survives, as facts, not as selection:**
  - the torus determinant's extremum at ω, with the saddle at i;
  - the 12-point minimum orbit of the Green function among the points of exact order 9, which is disjoint from W59's
    eighteen lines.
- **The negatives:**
  - the CP count was a coordinate error;
  - an orbit-averaged J is set by its input, not by reflection parity;
  - the averaged and Selberg spectra carry no hierarchy, missing the data by one to three orders;
  - choosing the Selberg weight at ℓ(LR) is the thread-for-weave substitution again, the owner's question of
    2026-10-20 (P-200).

## 3. Files

- `verification/as_received/`: the received FINDINGS, verdict, script, output and lock, and `SHA256_AS_RECEIVED.txt`.
- `verification/main_check/`: the reading pass's report and scripts (`v.py`, `cp.py`, `yuk.py`, `sel.py`), with their
  runs.
- The lock: `tests/test_b1673_dynamical_selection_cp_violation_and_mass_emergence.py`. It replaces the received lock,
  which asserted the coordinate error.
