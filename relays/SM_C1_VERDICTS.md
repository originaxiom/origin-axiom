# SM-C1 closed: the physical lane's ten hand derivations of 2026-10-27 to 29 (batch V1) — ten REPRODUCED

*Closes the card `relays/cards/SM_C1_physical-lane-batch-V1.md` (M1 on main's docs/seats/sm.md). The checks and their
outputs are in `relays/sm_c1/`, committed before this note (68bccc168). Firewall kept: no coupling, mass or angle was
evaluated against a measured value, and no file with agy_ in its path, no file auditing another lane's values and no
target file was opened.*

## The verdicts

| row | item (the lane's branch, commit read) | verdict | why, in one line | where |
|---|---|---|---|---|
| 1418 | gauge complex and threshold controls (9185cb169) | REPRODUCED | d₁d₀ = 0 (also for varying a(t)); the Laplacians, with main's partners L± for varying a; 1:2:1 and both alternating sums 0; F_pair + F_ext = F_weak term by term against its predecessor's histogram; ∫dp/2π log[(p²+μ²)/(p²+ν²)] = μ − ν exactly | `relays/sm_c1/row1418_gauge_complex.py` |
| 1420 | universal SU(5) end (0a8082283) | REPRODUCED | the normalised colour, weak and hypercharge indices of 5, 10, 24 are (1/2, 3/2, 5) in all three factors; the doublet alone (0, 1/2, 3/10) is caught as unequal; §§ 2–3's local-covariance argument is standard | `relays/sm_c1/row1420_1421_su5_indices.py` |
| 1421 | Wilson relative coefficients (7dfe63e26) | REPRODUCED | all six D21, D31 coefficients rebuilt from the representations' weights, exactly; each sums to zero, so equal H gives zero | same script |
| 1422 | relative heat scale and light modes (e78a9be08) | REPRODUCED | Z(0) = −h, L_rel(cP) = L_rel(P) − h log c and I(μ) = L_rel + h log μ², checked through the integral representations (not closed forms) on finite relative spectra with zero modes; the Mellin and Frullani steps re-derived (L_rel = −a₀ + γh); a planted spectrum of nonzero total weight gives Z(0) + h = R(0) ≠ 0, caught | `relays/sm_c1/row1422_relative_heat.py` |
| 1423 | fermion relative heat existence (01e322345) | REPRODUCED (a proof, reviewed) | each step re-derived or standard; see the review below | this note |
| 1425 | gauge fixing and one-loop weights (05ab32193, amended to f06ce63e6) | REPRODUCED | the heat coefficients from explicit Euclidean gamma matrices: scalar 1/12, Dirac −2/3, vector −5/3; products 1/4 on P_c and −3/4 on P_v, so +1 and −3, the ghostless −8/3; (0, −6, −9) from −3C₂; the finite U(1) D-flat control (P_v = 4g²v², δμ = 2gvh, g(x) = 2gvπ) | `relays/sm_c1/row1425_loop_weights.py` |
| 1465 | chiral kernel and spin running (1a4791de8) | REPRODUCED | the pole bound (7) from its stated L² integrand; the table N_j(L), j = 0..4, with gauge = H3 counts; at order seven 2(10 + 10̄) + 4(5 + 5̄), κ adjoints and 12 singlets, dimensions 92 + 12κ and 12; β = (10, 4 + 2κ, 1 + 3κ), h = (0, 0) or (−4, −6); the zero-Wilson control 6 for the 5's | `relays/sm_c1/row1465_chiral_kernel.py` |
| 1487 | two heat responses and a scale-free C (3596d5bef) | REPRODUCED | (4) J K_a¹ J⁻¹ = K_(a−2)⁰ + (a − 2) symbolically, in the item's own operators; the recurrence (6) and F_a = F_(2−a); the pairing (10) → (11) and the j = 0..4 table; (12) from row 1421's coefficients with the order-seven classes; B_C (13); h_C (15); the light limits (0, 0) and (−4, −6) | `relays/sm_c1/row1487_two_heat_responses.py` |
| 1488 | its author audit (db1d44b69) | REPRODUCED | the unspecialised B21, B31 and B_C; h_C = (12/5)[δ(L²) − δ(L³)]; the countercontrol (−4, −6) and (−4/5, 6/5) with determinant −48/5; K_a⁰ = −y²Δ + i a y ∂̄ and both norm identities | `relays/sm_c1/row1488_author_audit.py` |
| 1489 | geodesic trace and coupling product (4572f758c) | REPRODUCED | (1) by conjugation; the orbital coefficient (3) equal to direct numerical integration of the H² heat kernel to 10⁻¹⁷; the Laplace integral and the product logarithm in (7); (9) re-assembled, with arguments 1, 2, 3/2, 5/2; the relative vacuum weights 0 and 0 | `relays/sm_c1/row1489_geodesic_trace.py` |

## Row 1423: the review

The proof's steps, each re-derived or a named standard theorem:
1. **The compactly localised heat operator is trace class.** χ(P + 1)^(−m) maps L² into H^(2m) of a compact region by
   interior elliptic estimates, and H^(2m) → L² is trace class on a closed surface when 2m > 2.
2. **The domains agree.** Dom P_q = Dom P_0, because K_q is a smooth compactly supported endomorphism that preserves
   Dom D_0.
3. **The relative heat operator is trace class.** Duhamel's formula, split at t/2, uses ‖D e^(−uD²)‖ ≤ (2eu)^(−1/2).
4. **The commutator identity (7).** It holds by differentiating e^(−(t−u)P_q) ψ e^(−uP_0) in u, using Vψ = 0.
5. **The relative trace is small at small time.** Finite propagation (Davies–Gaffney) gives Gaussian suppression at both
   ends of (9), with no bounded-geometry assumption, so the trace is O(t^N) for every N.
6. **The large-time behaviour.** The noncommutative telescoping identity gives a geometric trace-norm decay.
7. **The rejecting control (14)** matches the standard second heat coefficient of P + W.

The verdict is conditional on the source construction the item names: D_q = D_0 + K_q, the essential gap at 1/4, and
local gauge conjugacy. That construction is not re-verified here, and the item says it rests on it.

## What was not done

- **The source constructions** the items rest on (weave_curved_action, weave_sm_parallel, weave_physical_mass, and the
  graph realisation) were not re-derived. Every verdict is conditional on them, as every item states.
- **No spectral function was evaluated.** E_q, O_q and the products in row 1489's (9) carry no number here. The items
  claim none either.
- **The analytic parts were reviewed in writing, not computed:** row 1423 in full, and the curved-domain steps of rows
  1425, 1465, 1487 and 1489.
- **Fixes to this seat's own code.** Three post hoc fixes, each disclosed in its script, were all aggregation or
  assembly bugs. None changed a value of the lane's.
  - Row 1418: a list was compared as a string, and the quadrature tolerance was below 30-digit reach.
  - Row 1489: a sign was negated through stacked negations in the assembly, and a zero was left unsimplified.

## How each result was checked (protocol § 12, read at M2)

By the owner's ruling of 2026-11-11 (register row P-797), a result is named by how it was checked. A check has a
result, not a verdict; the word above stays only where main still reads it. Each item is the lane's hand derivation,
with no committed output of its own, so this seat's code is its only computation.

| rows | how checked | evidence |
|---|---|---|
| 1418, 1420, 1421, 1422, 1425, 1465, 1487, 1488, 1489 | computed once; reproduced; expectations committed first; tested against planted errors (11 planted, 11 caught) | the scripts and outputs in relays/sm_c1/ (68bccc168); a clean-checkout rerun at 868170ce5, every output byte-identical (`relays/sm_c1/REPRODUCED_RUN.txt`); the card (7c01c44c6) committed before the outputs; the PLANTED entries in each JSON |
| 1423, and the analytic steps of 1425, 1465, 1487 and 1489 named above | not independently checked | reviewed in writing only, in this note; no computation |

## For main

Ten REPRODUCED. Nothing for the lane is needed from this batch. SM-C2, batch V2, is next.

0 of 19.
