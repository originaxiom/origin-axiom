# B1814 post-run referee (hostile, read-only, 2026-10-29) — saved by main from the referee's hand-back

**Verdict: PASS WITH CORRECTIONS.**
- The computation holds. The sealed instruments are the ones that ran:
  - all 13 ARTIFACT_HASHES entries match;
  - the instruments are unchanged since 86cb26b30;
  - census.jsonl, control.json and comparison.json are byte-identical to ea21be40f and 987a1f270.
- tasks() matches all 8 000 rows. 60 rows recomputed through B1740's compute() show no difference.
- control() and comparison.json regenerate byte-identically (r1, r7).
- **Independent re-implementation** (r3: cKDTree in the max norm, its own mid-rank Fisher, its own target, sigmas and
  random hierarchies) is identical in every decisive number:
  - p_nn: A1 unforced 0.071872, A1 by hand 0.093585, A0 0.034300;
  - p_F: A1 0.426005, A0 0.068600;
  - r: D1 0.72655, D2 0.564875, D1h free 0.4539.
- Each cell was decided correctly.
- **Main's verification:** r3 and r8 regenerated identically on main (main_rerun/).

## Required corrections (all applied in B1814's FINDINGS)
1. **Report the pre-listed "p_nn for D2" read-out.** By p_nn the six do separate the clocks (A1 0.072, A0 0.034), but
   67% of random hierarchies show that pattern (r = 0.6725), so it is not informative.
2. **Use the measured shares, and state D2's power.**
   - Both clocks were typical for 43.5% of random hierarchies, not "6 in 10". D1 holds for 73%, not "almost all".
   - D2's power was only 18.6% (p_F) and 18.8% (p_nn) of A1's draws atypical under A0, so a world from the critical
     clock fails D2 about 81% of the time. The test could not decide the clock.
3. **D1 rests on the chosen floor and the cusp tail.**
   - It fails at the floor 1e-8 (0.043).
   - The 219 draws as isolated as the data:
     - 74% sit at Im τ > 4, where the radii are held, against 11% of all resolved draws;
     - 79% have a ratio below 1e-6;
     - none is within 19.7σ of the data.
   - The nearest unforced world (Im τ 3.56) misses u/t by 6.8×, d/b by 4.0×, s/b by 2.3× and c/t by 1.9×.
   - Say "not atypical at the 5% level, at the chosen floor", not "typical".
4. **The W57 contrast is not like for like:** a different frame and measure, ten numbers, 10⁶ draws, and a p_nn that is
   post hoc and never recomputed on main. The closest analogue here is the nine: 0.085 unforced, 0.0017 by hand.
5. **The horocycle read-out agrees with row 1455 only in direction, by p_nn.**
   - p_F goes the other way.
   - Random hierarchies are typical for 1.5% at L_max and 3.3% at L₂.
   - Under a 48-configuration class-choosing null, 11.4% reach the data's 0.123 (7.0% over the 32 fixed-horocycle
     configurations).
   - Row 1455 is a different test.
6. **Apply the pre-written D1h-and-D1-hold reading with its resolution.** D1's q95 is 13.4σ, coarser than
   log 3/s6 = 11.0σ, so nothing about c follows.
7. **LOOK_LEDGER, as promised:**
   - row 1455's look;
   - row 1469's two, counted conservatively;
   - B1814's three, as looks 51–53.
8. **The verdict.** NEGATIVE as sealed, scoped to D2's prediction (B1792, B1811, B1740). The claim line carries "the
   clock is not decided by these numbers" with the power figure, and does not read as a negative for the critical clock
   or for typicality.

## Recommended (applied)
- Anarchy's p is the estimator's floor, 2.5e-4.
- "The direction is B1813's" is generic and was anticipated: every random hierarchy A0 rejects is rejected on the deep
  side.
- Three-deep among resolved draws: 34% (A1) and 15.6% (A0).
- The by-hand nearest draw's true configuration: L_max, (S̃, S, S), c = 3, τ 0.4036 + 3.2014i, line (2/5, 1/10).
- It adds no independent support, sitting where B1735's and B1749's best rows are.
- D2's failure is narrow but robust: p_F(A0) is 0.052–0.085 over 200 half-splits and 0.066–0.079 over 100
  configuration seeds, and D2 never holds.
- D1h is less robust than D1: it holds in 83% of subsamples.
- The pre-seal expectation "r_D1 near 1" was overstated (0.73).
- P-091's wording.
- The power the other way: A1 accepts almost any A0 world (0.4%, 1.6%).

Scripts r1–r8 and outputs beside this file.
