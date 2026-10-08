# B1606 — PREREGISTRATION: THREE ON THE WEAVE, GRADED — the SM seat's W22 as qualified (the puncture index is odd, never zero, and ±3 with the parity grading) checked on main's code, and the whole chain W19–W24 graded on GENESIS against THE_BAR: what is derived on the weave, what is a reading, what is a dictionary

cc (main), 2026-10-08, after S85. A weave arc: one computation (the seat's qualified W22, the last unverified link of
the chiral three) and one ruling (the grade). **Sealed before `puncture_condition.py` runs.** No physical quantity.
0 of 19.

## Seen first

`VERDICT topic-sweep /puncture|end condition|Lagrangian|local solution|Dirac|spin doublet|parity grading|chiral three|three on the weave/: 44 of 1378 arcs on main match (NEGATIVE 5, OPEN 2, PROVED 37)`
— B1600 (W1–W4, W10, W20–W21 verified), B1601 (WM2: the linear parts at the common point are the cube's rotations on
the three lines — the seat's "T₀𝒳 is the triplet" in another form), B1604 (no index on a thread), the seat's W19–W24
(rows 932–940). **Seen before the seal:** W21 verified on main (the holomorphic triplet is T; `w21_check.py`), W22's
irreducibility of 2O and the parity stabilisers on ℂ² (`w20_w22_check.py`). The six-dimensional action of the lifts
and its commutant are not computed before this seal. **Literature:** Riemann–Roch for parabolic bundles (the degree of
the extension at a puncture with holonomy −1); the seat's own.

## Disclosed

The six local solutions are modelled as ⊕_p ℂ² with the lifts acting by u_q⁻¹ g u_p from block p to block q = p∘m
(the seat's D1: χ_p ⊗ ρ_Q = u_p ρ_Q u_p⁻¹ with u = j, i, k); the index of a kept subspace Λ₊ is dim Λ₊ − 3 (the seat's
Riemann–Roch, taken as stated, not re-derived); the invariant subspaces are read from the isotypic decomposition of the
moves' group on ℂ⁶ (sums of isotypic pieces). Not blind to the seat's numbers (2 ⊕ 4; −3, −1, 1, 3; ±3 with the grading).

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **P1** | D1 holds: χ_p ⊗ ρ_Q = u_p ρ_Q u_p⁻¹ on the generators for u = j, i, k | 95% |
| **P2** | under the lifts of L and R the six local solutions have commutant 2 and split 2 ⊕ 4, so the kept dimensions are 0, 2, 4, 6 and the kept indices −3, −1, +1, +3 — never 0 | 80% |
| **P3** | −1 lies in the moves' group and acts as −1 on all six, so every kept index is odd | 85% |
| **P4** | with the parity grading added the commutant is 1 and only 0 and 6 are kept: the index is ±3 | 80% |

**The grade (the ruling, written before the run; the cells can only lower it).** On GENESIS v1.28, at FK14 and FK11:
- **Derived on the weave (PROVED or COMPUTED with main's verification):** the three (W1/W4: the parities, one
  irreducible triplet); the common point as each thread's geometry mod 3 (B1601); the even-dimensional object (W19:
  Aut⁺(F₂), M₁,₂) and on it an index-type count of E₆'s 27 equal to three, not chiral (W20); the hand by Hodge type
  (W21: the three holomorphic zero modes span T, one per parity — chirality under the weave's group); the puncture
  index forced odd and ±3 with the grading (W22, if P2–P4 hold).
- **Readings:** "the three generations are the triplet" (FK14); "holomorphic zero modes are the left-handed matter"
  (the compactification dictionary, FK11).
- **Dictionary, unearned:** which fields carry 𝕎 (W24's D4: the Lagrangian half is the frame choice); gauge chirality.
- **Negatives:** no index on a thread or its covers (B1604); the E₈ frames on the fibre give at most two complete
  generations (W23); no six-dimensional object the weave forces gives three by the heterotic dictionary (W24).
- **The owner's question, "did we derive three generations?":** no. What is derived is **three, alike, chiral under the
  weave's own group, one per parity** — the flavour structure — with its number forced by the records and its hand
  forced by the puncture; what is not derived is that these three are generations of a gauge theory: the dictionary
  that assigns gauge representations to 𝕎 is a choice (FK11), and the record's own frames cannot complete three on the
  fibre (W23). THE_BAR: a derivation of the flavour three; a selection for the gauge three. 0 of 19 stands.

## Instruments

`verification/puncture_condition.py`; hashes in `ARTIFACT_HASHES.txt`.
