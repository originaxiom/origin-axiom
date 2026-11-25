# P-630, part A (2026-11-25): the positive control. Linearised along a deviation at the golden chain's critical point, the deviation's components and the size map recover the leading thermal dimension h = 1/10 to 1e-3 along the label density (both routes) and along Σ nᵢnᵢ₊₂, and to 7e-3 along Σ nᵢnᵢ₊₃, whose ε component is weak. They do not recover the second, h = 3/5: along the label density the read-out is 0.509, along Σ nᵢnᵢ₊₂ 0.662 (and along Σ nᵢnᵢ₊₃, from weak amplitudes, 0.590). By N = 36 the first is still rising, ever more slowly, toward 3/5, and the second is moving away from it. As registered the control does not pass: the cells for h = 3/5 fail, those for h = 1/10 hold

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It answers main's seat page, M82, row
P-630: the positive control first, then the trace map linearised at B181's critical locus against B1788's exponent
set. This page is the first half; the second is part B's relay of the same day. Nothing is compared with data.

**Read through the mask:** the register rows P-629 and P-630; main's seat page (M82). **Read directly:** the verdict
files and scripts of B181, B220 and B222.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p630/p630_control.py` (SHA-256 2a5841e1c035ddc9) states its cells,
  tolerances and expectations in its docstring. It was committed at d4c206878 before its run. Before that commit its
  building blocks were tested at N = 6 and 8: the gate only, at sizes no cell uses.
- Two cells failed as worded (A2 and B2).
- The sealed docstring gives the size map's eigenvalue as (N′/N)^y. It is (N/N′)^y. No computation uses it.
- Three scripts are labelled post hoc, each written after an output was read and committed before its own run:
  - `p630_control_posthoc.py` (fcb2d9b13): the k = 0 levels, and three more directions;
  - `p630_control_posthoc2.py` (55ebf1fd3): rings up to N = 36, with a reading rule stated before its run (§ 2);
  - `p630_control_posthoc3.py` (8ae1e9056): fits to the recorded amplitudes.
- The chain is built here from B220's rule, not from main's code.
- The referee read (applied here) reran the scripts and built the topological symmetry Y from the Fibonacci F-symbols.
  Its checks are not committed; where this page uses them it says so.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The method.**
   - Deviate the critical chain H_c along a translation-invariant direction V, and linearise at zero deviation.
   - (A) V's component on the state of a scaling field φ scales as N^(y − 1), with y = 2 − x_φ the field's eigenvalue
     in the flow away from criticality.
   - (B) The size map (phenomenological renormalisation) is linearised the same way, through the derivative of a gap.
   - The directions are V_μ = Σ nᵢ, the density of identity labels (nᵢ = 1 − lᵢ), which breaks Y, and
     V_Y = Σ (PᵢPᵢ₊₁ + Pᵢ₊₁Pᵢ), which keeps it. The rings have N = 12 to 30, k = 0 and π.
2. **[E] The gate and the labels hold.**
   - At N = 10 and 12 the momentum sectors' spectra reproduce the full spectrum to 3e-14.
   - At N = 30, (E₂ − E₀)/(E₁ − E₀) = 5.970 (the limit is 6), and the lowest k = π level gives 0.3766 (the limit
     is 3/8, for σ).
   - The referee's Y check: Y commutes with H_c and V_Y, not with V_μ. ε and ε′ at k = 0 and σ at k = π have
     Y = −1/φ; level 4 (ε″) has Y = φ.
3. **[E] h = 1/10 is recovered.**
   - From V_μ's component on ε, h = 0.09993 by the stated fit, and 0.10005 locally between N = 34 and 36.
   - The size map through σ's gap, along V_μ, gives 0.0996.
   - Post hoc, Σ nᵢnᵢ₊₂ gives 0.1001 and Σ nᵢnᵢ₊₃ gives 0.0934.
4. **[E] h = 3/5 is not recovered.**
   - From V_μ's component on ε′ the read-out is h = 0.509 against a tolerance of 0.03. The size map through ε's gap
     gives 0.528.
   - Post hoc, Σ nᵢnᵢ₊₂ gives 0.662, and Σ nᵢnᵢ₊₃, whose amplitudes are weak, gives 0.590.
   - At N = 36 the local values are 0.482 (V_μ) and 0.655 (Σ nᵢnᵢ₊₂). The first is still rising toward 3/5, ever more
     slowly. The second is rising too, so it is moving away from 3/5.
   - § 2 reads the amplitudes. [J] Along V_μ every fit to about 1e-6 carries a nearly N-independent term, and no
     field in the Kac table supplies one.
5. **[E] The selection rule holds exactly.**
   - V_Y's components on ε and ε′ are at most 1.8e-14 at N = 12 to 22. Those on level 4 (x = 2.77 at N = 12 and 2.96
     at N = 30, so ε″) are 0.07 to 0.19.
   - Conversely, V_μ and Σ nᵢnᵢ₊₂ have components below 2e-13 on the levels V_Y reaches (4 and 7 at N = 12, 4 and 6
     at N = 20). They also vanish on level 9 at N = 12 and on level 8 at N = 20 and 30, levels V_Y was not computed
     on. Among levels 1 to 7 the two sets are complementary at N = 12 and 20.
   - [J] The reason, from the referee's exact checks at N = 12 and 14: on the Y-trivial levels V_μ acts as the constant
     N/(1 + φ²), and Σ nᵢnᵢ₊₂ = Σ nᵢPᵢ₊₁ as −H/(1 + φ²). So neither connects the ground state to another Y-trivial
     level. Their other action is into and within the τ-flux sector, which is what B1 and B2 read.
6. **[J] What this means for part B.**
   - The deviation route reads a deviation's leading exponent reliably. At these sizes it does not read the
     subleading one: its read-out depends on the direction by ±0.08.
   - Part B linearises the trace map exactly, as a Jacobian's eigenvalues, so the direction dependence seen here need
     not carry over. Part B has its own control, matched to its method, stated before it runs.
7. **[J] B222's one line overstates two points.**
   - At even N the spinless level at x = 3 is the primary (3/2, 3/2), ε″, not the supercurrent G, whose weights are
     (3/2, 0). Here that level (level 4) is reached by V_Y and not by V_μ, as a Y-trivial field should be. At even N
     the conformal spins are integers, so G is absent from the spectrum B222 read.
   - At odd N, G is expected, with spin ±3/2 about K = π. The referee's run finds such a doublet at x = 1.462, 1.470
     and 1.475 for N = 17, 19 and 21. This page does not check odd N.
   - B222 reads the spinless even-N dimensions (0, 1/5, 6/5, 3) and one odd-N difference, 2(7/16 − 3/80) = 0.8. It
     does not read σ or σ′ separately, so "the full primary content" overstates as well. The central charge,
     c ≈ 7/10, is B220's, from the entanglement entropy.
   - The even-N dimensions agree with this page's spectra (x₂ = 1.194, x₄ = 2.956 at N = 30).

## 1. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| G1 | sectors' union = full spectrum to 1e-10; Hermitian to 1e-12 (99 %) | holds: 2.1e-14 and 3.0e-14; 4.8e-15 |
| G2 | at N = 30, ratio within 0.3 of 6, and within 0.03 of 3/8 (90 %) | holds: 5.970 and 0.3766 |
| A1 | ε from ⟨1\|V_μ\|0⟩: \|h − 1/10\| ≤ 0.01 (85 %) | holds: 0.09993 |
| A2 | ε′ from ⟨2\|V_μ\|0⟩: \|h − 3/5\| ≤ 0.03 (75 %) | **fails**: 0.5086 |
| A3 | V_Y's components on ε, ε′ below 1e-10, and one above 1e-6 on levels 3 to 7 (95 %) | holds: at most 1.8e-14; 0.07 to 0.19 on level 4 |
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

- **The larger rings.** From N = 24 to N = 36 the local read-outs for level 2 rose from 0.469 to 0.482 for V_μ, and
  from 0.648 to 0.655 for Σ nᵢnᵢ₊₂. The gap between them narrowed only from 0.180 to 0.173.
- **The reading rule stated before that run.** `p630_control_posthoc2.py` fixed it in its docstring: if either
  direction's local h moves away from 3/5, the read-out along that direction carries a second contribution with its
  own exponent. Σ nᵢnᵢ₊₂'s did, so by that rule its read-out carries a second contribution.
- **The fits** (`p630_control_posthoc3_out.txt`; V_μ on N = 12 to 36, 13 sizes; Σ nᵢnᵢ₊₂ on N = 24 to 36, 7 sizes):
  - h fixed at 3/5 (the power N^(−1/5)) plus a constant and a 1/N term: rms residual 3.5e-6 (V_μ) and 5.6e-6;
  - the power free, with a constant: s = −0.016 for V_μ and −0.478 for Σ nᵢnᵢ₊₂;
  - the power free, without a constant: s = −0.022 for V_μ and −0.334 for Σ nᵢnᵢ₊₂.
- [J] What the fits say.
  - For V_μ, every fit at the 1e-6 level contains an almost N-independent piece. The referee's check (not
    committed): N^(−1/5)(a + b/N + c/N²) leaves an rms of 3.0e-4 on V_μ, against 3.5e-6 with a constant at the
    same number of parameters. So slow integer-power corrections to N^(−1/5) are disfavoured along V_μ.
  - For Σ nᵢnᵢ₊₂, 7 sizes against 3 or 4 parameters do not discriminate.
  - No model fits to the amplitudes' precision: the residuals are about 100 times the 3e-8 of their seven figures.
  - A constant term means an x = 1 contribution. The k = 0 τ-flux content (ε, ε′ and their descendants at x = 2.2,
    3.2, …) has no field at x = 1. First-order mixing through Y-trivial irrelevant fields (x = 3, 4, …) gives
    N^(−1/5), N^(−6/5) and so on, not N⁰.
  - This page therefore weakens posthoc2's reading rule only on the strength of posthoc3, which is post hoc to it. It
    does not explain the ε′ channel.

## 3. What this page does not do

- It does not run part B (the trace map against B1788's exponent set).
- It does not explain the ε′ read-out.
- It does not check B222's odd-N (Ramond sector) statement.
- It compares nothing and reads no target.

0 of 19.
