# THE EXACT END, THE LOOK — the rule, sealed before its script (chat1, 2026-10-28)

**Why.**
- The data-free half (`exact_end.py`, 6bf91b34a; read as it finished) found that at the maximal horoball the exact norms
  of the frame's twisted channel kernels lie 35–38% below the small-cut form 2πL_max + c_s, in every channel and at four
  of the six's rows.
- Read with the exact norms, the frame's down and lepton m₂/m₃ fall by −0.39 to −0.73 in ln. By the rule stated in the
  script, a look is warranted.
- At L₂ the two agree to 0.6%.
- The record's six-fits at "L_max" (B1726, B1741, B1749, B1786, and this seat's horocycle test) all use the small-cut
  form. This look asks whether the six survive at the maximal horoball itself.
- It answers the second question of this seat's relay THE CLASS AND THE END (422cd8ecd), on the owner's word of
  2026-10-28: "do them, go to end".

**The quantity.** χ²_six is B1741's seat measure, unchanged, imported from its compare.py:
- σ² = rel² + 0.10², at M_Z;
- the menu (S̃, S, S) and (S̃, S̃, S̃);
- c ∈ {1, 3}.

The frame is B1726's compute(), with one change. Each channel weight √(2πL + c_s) becomes √N_s, where N_s is the exact
norm of K_s = P_s/R_s over the Dirichlet cell minus B1667's maximal horoball at that τ. B1667's own geometry is used
(accessory parameter, Frobenius series, horocycle radius, cell), imported unchanged, as in `exact_end.py`.

**The rows.** Each is the best L_max row of one of the four mirror-pair families among the slope-2/5 carriers of orders
10, 25 and 30, as found by the horocycle test's Nelder–Mead (`horocycle_cells.json`, readout_nelder_mead), with
|Re τ| ≤ ½:

| row | line | τ | the horocycle test's χ²_six (small-cut) | family |
|---|---|---|---|---|
| A | (2/5, 23/30) | 0.2354 + 3.0233i | 2.409 | order 30 |
| B | (2/5, 1/10) | 0.3154 + 3.0349i | 2.658 | order 10 |
| C | (2/5, 23/25) | 0.4097 + 3.0653i | 4.775 | order 25, the 3/25 class |
| D | (2/5, 11/25) | 0.3032 + 3.0551i | 4.924 | order 25, the 11/25 class |

Mirror partners have equal χ²_six, so one member of each pair is enough.

**The procedure, per row.**
1. **Control.** χ²_six at the row with compute() as is (small-cut, column L).
2. **At the row.** χ²_six with the exact norms at the maximal horoball.
3. **Refit.** One Nelder–Mead over τ from the row:
   - box Re τ ∈ [Re₀ − 0.2, Re₀ + 0.2] and Im τ ∈ [Im₀ − 0.5, Im₀ + 0.5];
   - at most 40 evaluations, fatol 1e-3, initial step 0.05;
   - objective χ²_six with the exact norms.

   Where Re τ leaves [−½, ½], the configuration is moved back by T, (τ, a, b) → (τ ∓ 1, a, b ± a); χ²_six is
   T-invariant (B1726's T-law). The accessory parameter is continued by B1667's newton_walk from the nearest solved τ.

**The cells, with priors stated before any of them is computed.**

| cell | statement | prior |
|---|---|---|
| E0, control | step 1 reproduces the horocycle test's values in the table to 1e-6 (relative) | 97% |
| E1, decisive | the least χ²_six over the four refits, with exact norms, is above 16.75 | 55% |
| E2 | at every row, step 2's χ²_six is above 16.75 | 80% |
| E3, read-out | which of the six move most, and the refits' τ | none |

**What each outcome means (stated before the run).**
- **E1 holds:** the six's fit at "L_max" belongs to the small-cut formula, not to the maximal horoball.
  - The horocycle test's H4 is then restated: the six need the small-cut form at L_max.
  - The end's lever is a formula's, and the six do not survive the frame at its own maximal cusp.
- **E1 fails:** the six survive at the maximal horoball with a shifted τ. The refit's τ and χ²_six are reported.
- Either way, the L₂ results stand, since the exact and small-cut norms agree there to 0.6%.

**Accounting.**
- One look, the six only (no CKM).
- P-323's θ̄ is not recomputed here. The exact norms are still real, channel-dependent and non-holomorphic, so its
  mechanism stands. That is a reading, not computed.
- The rule was not refereed before the seal; the result note will be.
- The rows' small-cut values were seen before the seal (they are the horocycle test's). The exact-norm values at the four
  rows were not computed before the seal.
- The data-free read-out at nearby rows (`exact_end.py` C2) already shows the direction: down and lepton m₂/m₃ fall by
  0.39–0.73 in ln. E2's prior reflects that foreknowledge.

0 of 19.
