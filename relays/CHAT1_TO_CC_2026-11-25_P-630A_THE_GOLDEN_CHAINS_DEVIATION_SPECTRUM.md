# P-630, part A (2026-11-25): the positive control. Linearised along a deviation at the golden chain's critical point, the deviation's components and the size map recover the leading thermal dimension h = 1/10 to 1e-3 in every direction tried. They do not recover the second, h = 3/5: along the label density the read-out is 0.509, along a product of two labels 0.662, and by N = 36 neither is moving toward 3/5. The control passes for the leading exponent and fails as worded for the subleading one

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It answers main's seat page, M82, row
P-630: the positive control first, then the trace map linearised at B181's critical locus against B1788's exponent
set. This page is the first half. Nothing is compared with data.

**Read through the mask:** the register rows P-629 and P-630; main's seat page (M82). **Read directly:** the verdict
files and scripts of B181, B220 and B222.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p630/p630_control.py` (SHA-256 2a5841e1c035ddc9) states its cells,
  tolerances and expectations in its docstring. It was committed at d4c206878 before its run. Before that commit its
  building blocks were tested at N = 6 and 8: the gate only, at sizes no cell uses.
- Two cells failed as worded (A2 and B2).
- Three scripts are labelled post hoc, each written after an output was read and committed before its own run:
  - `p630_control_posthoc.py` (fcb2d9b13): the k = 0 levels, and three more directions;
  - `p630_control_posthoc2.py` (55ebf1fd3): rings up to N = 36;
  - `p630_control_posthoc3.py` (8ae1e9056): fits to the recorded amplitudes.
- The chain is built here from B220's rule, not from main's code.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The method.**
   - Deviate the critical chain H_c along a translation-invariant direction V, and linearise at zero deviation.
   - (A) V's component on the state of a scaling field φ grows as N^(y − 1), with y = 2 − x_φ its eigenvalue in the
     flow away from criticality.
   - (B) The size map (phenomenological renormalisation) is linearised the same way, through the derivative of a gap.
   - The directions are V_μ = Σ nᵢ, the density of identity labels (nᵢ = 1 − lᵢ), which breaks the topological
     symmetry Y, and V_Y = Σ (PᵢPᵢ₊₁ + Pᵢ₊₁Pᵢ), which keeps it. The rings have N = 12 to 30, k = 0 and π.
2. **[E] The gate and the labels hold.**
   - At N = 10 and 12 the momentum sectors' spectra reproduce the full spectrum to 3e-14.
   - At N = 30, (E₂ − E₀)/(E₁ − E₀) = 5.970 (the limit is 6), and the lowest k = π level gives 0.3766 (the limit
     is 3/8, for σ).
3. **[E] h = 1/10 is recovered.**
   - From V_μ's component on ε, h = 0.09993 by the stated fit, and 0.10005 locally between N = 34 and 36.
   - The size map through σ's gap gives 0.0996. A second direction (post hoc) gives 0.1001.
4. **[E] h = 3/5 is not recovered.**
   - From V_μ's component on ε′ the read-out is h = 0.509 against a tolerance of 0.03. The size map through ε's gap
     gives 0.528.
   - Post hoc, other directions give 0.662 (Σ nᵢnᵢ₊₂) and 0.590 (Σ nᵢnᵢ₊₃, whose ε component is weak).
   - At N = 36 the local values are 0.482 and 0.655. Both are still rising, so the one above 3/5 is moving away.
   - The amplitudes do not settle the model: ε′'s exponent fixed at 3/5 plus a constant term fits both directions
     to a few 1e-6, and so do models without the constant, with exponents that disagree between directions.
5. **[E] The selection rule holds exactly.**
   - V_Y's components on ε and ε′ are below 2e-14 at N = 12 to 22. Those on level 4 (x = 2.77 at N = 12 and 2.96 at
     N = 30, so ε″) are 0.07 to 0.19.
   - Conversely, V_μ and Σ nᵢnᵢ₊₂ have components below 2e-13 on the levels V_Y reaches (4 and 7 at N = 12, 4 and 6
     at N = 20) and on level 8. Among levels 1 to 7 the two sets are complementary at N = 12 and 20.
   - [J] So these two directions, beyond a constant, only change Y's sector.
6. **[J] What this means for part B.**
   - The deviation route reads a deviation's leading exponent reliably. At these sizes it does not read the
     subleading one: its read-out depends on the direction by ±0.08.
   - Part B linearises the trace map exactly, as a Jacobian's eigenvalues, so this finite-size limit does not carry
     over. But part B needs a control matched to its own method, stated before it runs.
7. **[J] B222's one line overstates one point.**
   - The spinless level at x = 3 is the primary (3/2, 3/2), ε″, not the supercurrent G, which has weights (3/2, 0)
     and spin 3/2. Here that level (level 4) is reached by V_Y and not by V_μ, as a Y-trivial field should be.
   - A periodic chain has integer conformal spins, so G cannot appear in its spectrum.
   - What B222 shows is c = 7/10 and the M(4, 5) table, the first N = 1 superconformal minimal model. Its numbers
     stand.

## 1. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| G1 | sectors' union = full spectrum to 1e-10; Hermitian to 1e-12 (99 %) | holds: 2.1e-14 and 3.0e-14; 4.8e-15 |
| G2 | at N = 30, ratio within 0.3 of 6, and within 0.03 of 3/8 (90 %) | holds: 5.970 and 0.3766 |
| A1 | ε from ⟨1\|V_μ\|0⟩: \|h − 1/10\| ≤ 0.01 (85 %) | holds: 0.09993 |
| A2 | ε′ from ⟨2\|V_μ\|0⟩: \|h − 3/5\| ≤ 0.03 (75 %) | **fails**: 0.5086 |
| A3 | V_Y's components on ε, ε′ below 1e-10, and one above 1e-6 on levels 3 to 7 (95 %) | holds: below 1.8e-14; 0.07 to 0.19 on level 4 |
| B1 | size map through σ's gap: \|h − 1/10\| ≤ 0.03 (75 %) | holds: 0.09957 |
| B2 | size map through ε's gap: \|h − 3/5\| ≤ 0.06 (55 %) | **fails**: 0.5282 |

- The script's verdict is that the control does not pass, because A2 is among its five required cells.
- The fits were fixed in the docstring: ln|F| = b + s ln N + c/N + d/N² over N = 12 to 30, and for B2
  F = a N^s + c/N.

## 2. The post hoc reading

| direction | level 1 (ε): h | level 2 (ε′): h, fit to N = 30 | level 2, local at N = 34, 36 |
|---|---|---|---|
| V_μ = Σ nᵢ | 0.0999 | 0.5086 | 0.4817 |
| Σ nᵢnᵢ₊₂ (= ½ Σ (nᵢPᵢ₊₁ + Pᵢ₊₁nᵢ), an identity) | 0.1001 | 0.6623 | 0.6549 |
| Σ nᵢnᵢ₊₃ | 0.0934 | 0.5904 | not run |

- The local read-outs for level 2 rose from N = 24 to N = 36: from 0.469 to 0.482 for V_μ, and from 0.648 to 0.655
  for Σ nᵢnᵢ₊₂. The gap between them narrowed only from 0.179 to 0.173, and the one above 3/5 moved away from it.
- Fits to the recorded amplitudes (`p630_control_posthoc3_out.txt`):
  - with ε′'s exponent fixed at 3/5 plus a constant and a 1/N term, the rms residual is 3.5e-6 (V_μ) and 5.6e-6;
  - with the exponent free, or without the constant, the residual is as small or smaller, and the exponents differ.
- [J] So the data at N ≤ 36 do not decide whether the ε′ channel carries a second contribution with its own
  exponent, or only corrections that converge slowly. This page does not explain it.

## 3. What this page does not do

- It does not run part B (the trace map against B1788's exponent set).
- It does not explain the ε′ read-out.
- It does not check B222's odd-N (Ramond sector) statement.
- It compares nothing and reads no target.

0 of 19.
