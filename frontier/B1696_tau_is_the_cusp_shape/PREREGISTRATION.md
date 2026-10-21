# B1696 — PREREGISTRATION: τ IS THE STATE'S OWN CUSP SHAPE (P-244) — with the weave's modulus set to the tick's cusp-torus shape 2√3 i, the unique section and one line, do the six charged-fermion ratios come out, specifically?

cc (main), 2026-10-21, after S167, at the owner's question ("are we sure it isn't hiding somewhere in our math already").
**Sealed before `verification/the_cusp_tau.py` and `verification/compare.py` run.** A test of a structure (B1637's
checklist), not a value derived. 0 of 19.

## Why

The sweep the owner's question demanded (topic_sweep, full text and the seats' lanes) found what the weave era never
used: the object's mathematics carries one canonical modulus. B357: on every E₆ block of the figure-eight's flat
connections the leading Neumann–Zagier data satisfy K(v, h) = τ K(u, h) with **one constant τ = the cusp shape**, 2√−3
(B712, B762: m004's cusp shape; B290: it predicts the core geodesics' ladder). The weave's τ (the fibre's modulus,
B1645–B1695) was always taken free; its selection was asked of dynamics (W62: runs to the cusp) and of the principle's
points (i, ω: no hierarchy), never of the state's own cusp torus. The fits put τ where the hierarchy is (Im τ 2.1–3.2;
B1694, B1695); the cusp shape sits at Im τ = 2√3 = 3.464. **The tagged hypothesis (H-cusp):** the weave's fibre modulus
is the state's own cusp shape; for the tick LR, τ = 2√3 i (Re τ = 0).

## The model and the cells

τ = 2√3 i fixed; the section ∂R (no free coefficient); B1667's canonical end at Im τ = 2√3 (L_max ≈ 0.645, L₂ ≈ 2.315,
interpolated); B1656's four-channel coupling with a flat line w = α τ, α = j/192 (j = 0…96), β = 0; six discrete choices
(the horocycle × B1660's three readings of the up sector). One continuous number (α) for six ratios.

| cell | prediction | prior |
|---|---|---|
| **H1** | some α and choice puts all six ratios within a factor of 3 | 35% |
| **H2, specific** | the data's best worst-factor is matched or beaten by at most 1% of 4 000 random hierarchical target sets (B1695's prior) | 10% |
| **H3** | the minimum χ² (σ² = the data's errors² + 10%²) is below 16.75 (5 degrees of freedom at 99.5%) | 3% |

Read-outs: the best α and choice, its six ratios, the calibration's median and quantiles.

**The reading, written before the run.** If H2 holds — the data fit at the cusp shape much better than random
hierarchies do, with one free number — the identification τ = the cusp shape would be the strongest structural result on
the record, graded a READING (Λ, H-cov, H-cusp, the weight and the six choices are tagged; the look-elsewhere count is 6
choices × 97 lines, inside the calibration), to be attacked before anything else: by the other word states' cusp shapes,
by a second section, by an independent route. If H2 fails, the cusp shape does not select τ in this frame, and the lead
from B357 is closed for it.

## Seen first

`VERDICT topic-sweep /cusp shape|cusp('s)? (modulus|shape)|2√−3|2√3 ?i|shape 2√|2\\sqrt\{-?3\}/ (full text): 56 of 1467
arcs on main match (NEGATIVE 10, OPEN 5, PROVED 41)` — chiefly B357 (the universal τ), B712, B762, B290, B859 (an
invariant evaluated at the cusp shape), B675 (the silver cusp lattice); and `VERDICT topic-sweep /selects? τ|fix(es|ed)?
τ|holds? τ|τ is (fixed|selected|forced)|stabili[sz](es|ed|ation) (of )?τ|select(s|ed|ion of)? the modulus/ (full text): 5
of 1467` — B1651, B1652, B1686, B1691, B366. The seats' lanes: the cusp-shape identification appears in none (their hits
are shared documents). **Literature:** the cusp shape as a geometric invariant (Thurston; Neumann–Zagier).

## Disclosed

- **What main knows before the seal.** The six measured ratios; B1694's curve at Im τ ≤ 3.6 on the four curves without a
  line (printed at 1.2, 1.8, 2.4, 3.0, 3.6); B1695's best point (Im τ = 3.15, α = 37/96) and that its grid has rows at
  Im τ = 3.45 and 3.5, **which main has not read**. No model value at Im τ = 2√3 has been computed.
- The identification is main's, made after the owner's question and the sweep, and after the fits had placed τ in this
  band — a post-hoc motive, stated. The calibration is sealed in to measure what the identification adds.

## Instruments

`verification/the_cusp_tau.py` (no data) → `the_cusp_tau.json`; `verification/compare.py` (the comparison and the
calibration) → `comparison.json`; B1656's functions copied verbatim; hashes in `ARTIFACT_HASHES.txt`.
