# B1713 — PREREGISTRATION: THE COMPLEMENT AND THE MIXING (P-261; P-129, P-164, P-258) — on every flat line of order 1–7 do the six charged-fermion ratios come out specifically, and on every line of order 1–12 does the frame give the quark mixing, specifically, once the look-elsewhere is counted?

cc (main), 2026-10-22, after the owner's question of 2026-10-22 ("did we compute everything we planned, every lead we
discovered on the way?"). **Sealed before `verification/the_complement_and_mixing.py` and `verification/compare.py`
run, and before B1712's outputs are read.** A test of a structure, not a value derived. 0 of 19.

## Why

- **Part A (P-261).** B1712 takes the lines of order 8–12. The lines a principle selects (closure w = 0,
  move-invariance, the tick's order-5 lines, W63's tie lines) all have order ≤ 7, and the census left them out because
  each has a sector coincidence (B1703: d = e at N ∣ 4 or 5, u = d at N ∣ 6, u = e at N ∣ 2 or 7). P-261 completes the
  census: 62 lines up to sign (1, 3, 4, 6, 12, 12, 24 of orders 1–7).
- **Part B (the mixing).** B1660's preregistration wrote that this frame's test "must be sealed blind on unseen
  quantities (the CKM, J) before any use". No arc since has computed the quark mixing in B1656's four-channel frame
  (the sweep below). The owner's question about the Cabibbo zero (P-129) and the SM seat's ask for the CP phase as an
  observable (P-258) wait on it. P-164 asks which lines are CP-odd.

## The model

- **Lines.** Every line w = ατ + b of exact order 1 ≤ N ≤ 12, up to sign: **266 lines**. Orders 1–7 come first; orders
  8–12 follow as B1712's 204 lines, in B1712's order.
- **The frame, as B1712.** The section ∂R (one unit on v₊; B1700); B1667's canonical end; B1656's coupling.
- **The grid.** Re τ ∈ {0, ½}, Im τ = 1.5–3.5 (step 0.1), both horocycles, B1660's three up readings.
- **The mixing.** Y's rows are the doublet Q's generations: in `bil` the row index is the left field's theta index, and
  B1653's U4 found the up and down sectors sharing the left null vector.
  - V = U_u^H U_d, with U the left singular vectors in ascending mass.
  - ∣V_us∣ = ∣V₁₂∣, ∣V_cb∣ = ∣V₂₃∣, ∣V_ub∣ = ∣V₁₃∣, and J = Im(V_us V_cb V_ub* V_cs*).
  - The same from the right singular vectors is a read-out (B1659's convention question, I-33).
- **Pre-seal checks on the CKM function** (random matrices, no model values): unitarity; V = 1 when the up sector equals
  the down; invariance under rephasing and under a common left rotation; J's sign flips under conjugation. All hold.

## Cells

| cell | prediction | prior |
|---|---|---|
| **A-H1** | on orders 1–7, some point puts all six ratios within a factor of 3 | 80% |
| **A-H2, specific** | at most 1% of 4 000 random hierarchical target sets (B1695's prior) fit at least as well, with the same rows | 3% |
| **A-H3** | on orders 1–7, the minimum χ² is below 16.75 | 3% |
| **K1** | on orders 1–12, some point puts PDG's ∣V_us∣, ∣V_cb∣, ∣V_ub∣ all within a factor of 3 | 30% |
| **K2, specific** | at most 1% of 4 000 random hierarchical mixings fit the three moduli at least as well, with the same rows | 5% |
| **K3** | some point puts all nine (the six ratios and the three moduli) within a factor of 3 | 10% |
| **K4, specific** | at most 1% of 4 000 random nine-target sets (the two priors together) fit at least as well | 2% |
| **C1, control** | unitarity: max ∣VV† − 1∣ < 10⁻¹⁰ over every point | 99% |
| **C2, control** | on orders 8–12 the six ratios reproduce B1712's stored values to 10⁻⁹ relative | 97% |

- **The random mixings (K2):** log-uniform, ∣V_us∣ in [10^−1.5, 10^−0.2], ∣V_cb∣ in [10^−2.5, 10^−0.7] and ∣V_ub∣ in
  [10^−3.5, 10^−1.5], ordered ∣V_ub∣ < ∣V_cb∣ < ∣V_us∣. The seed is 1713.
- **Read-outs:**
  - J at the best three-moduli point and at the best nine;
  - the right-vector moduli at the best point;
  - the best per order;
  - the largest ∣J∣ on each line over the grid (P-164: which lines are CP-odd at these τ; only ∣J∣ is read, since the
    sign is the CP convention P-149 names);
  - the double ratio (y_μ y_d)/(y_s y_e) at Part A's best point and at the best nine (P-094; the target 10.58 ± 0.11,
    with Barger's 10.714 seen, P-101).

**The reading, written before the run.**
- **If K2 holds**, the frame gives the CKM's pattern more specifically than random hierarchies, with the whole census
  counted. K4 then decides whether the masses and the mixing come from the same point.
  - If K4 holds too, it is the first joint positive of the weave's frame, graded a READING with its tags: Λ, the unit,
    H-cov in R's module, and the census's choices.
  - Its point (line, τ, horocycle, reading) is then the question, attacked first by a principle that would select it and
    by an independent route.
- **If K1–K4 fail**, the frame's mixing does not reach the CKM. P-129 is then answered in this frame: the Cabibbo angle
  is either not produced or not produced specifically.
- **If ∣J∣ vanishes on every line at Re τ ∈ {0, ½}**, the CP phase needs τ off those two lines (P-164).
- **Part A** is read exactly as B1712.

## Seen first

`VERDICT topic-sweep /CKM|Cabibbo|Jarlskog|V_us|V_cb/ (full text): 45 of 1484 arcs on main match (NEGATIVE 13, PROVED 32)`

- **Bearing on the mixing:**
  - B1611–B1613, B1620 and B1625: the flavour group's mixing patterns, before this frame.
  - B1646 and B1649: B1649 found the Cabibbo zero at the puncture.
  - B1653's U4: the shared null state.
  - B1657: the Cabibbo angle at first order.
  - B1660: the blind rule.
  - B1671: no Cabibbo angle in the parameter-free sectors.
  - B1673 and B1689: the CKM needs all four parameters in every frame.
  - B1690: W74's V3, "one coupling, CKM = 1".
- **None computes the mixing in B1656's four-channel frame at the canonical end** with the end-data Higgs.
- **For Part A:** `VERDICT topic-sweep /CKM|Cabibbo|V_us|V_cb|Jarlskog|mixing matrix|complement/ (full text): 196 of 1484
  arcs on main match (NEGATIVE 36, OPEN 8, PROVED 151, RETRACTED 1)`. The arcs bearing on it are B1698 (the order-5
  lines), B1703 (the census and the coincidence laws) and B1712 (orders 8–12).
- **Literature:** PDG 2025 §12 (the CKM moduli, pinned in B1612's `data.json`, sha256 61ea1565…); Antusch, Hinze and Saad
  (arXiv:2510.01312v2), for the double ratio.

## Disclosed

- **Known before the seal:**
  - the six measured ratios;
  - PDG's CKM moduli to their common rounding (∣V_us∣ ≈ 0.225, ∣V_cb∣ ≈ 0.041, ∣V_ub∣ ≈ 0.0037) and J ≈ 3 × 10⁻⁵;
  - the double ratio's target and Barger's value;
  - B1694–B1711's results.
- **Model values seen on Part A's lines:**
  - B1698's eight order-5 lines on a finer grid that contains this grid's points (best factor 2.33, 1.7% of random
    hierarchies as good, d = e). A-H1's prior rests on that result.
  - B1703's census JSON holds unread values at three off-grid τ.
- **Not seen:**
  - B1712's outputs: its run was in progress at this seal, and its outputs are unread.
  - No model mixing value in this frame. B1659's pre-seal explorations computed CKM moduli on W59's lines with a fitted
    Higgs (P4), a different Higgs. They are not re-read for this seal.
- **The instruments were import-tested and the CKM function checked on random matrices.** Nothing else was computed.
- **C2 reads B1712's stored output** after that output is committed. If it is missing, C2 reports None and fails.

## Instruments

- `verification/the_complement_and_mixing.py` (no data) → `the_complement_and_mixing.json`.
- `verification/compare.py` → `comparison.json`.
- B1656's functions copied verbatim (as B1712's). The hashes are in `ARTIFACT_HASHES.txt`.
