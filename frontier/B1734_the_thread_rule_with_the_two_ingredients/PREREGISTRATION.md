# B1734 — PREREGISTRATION: THE THREAD RULE WITH THE TWO INGREDIENTS (P-312) — at each thread's own point and its own order-5 and order-10 lines (both members of every pair counted), do the six charged-fermion ratios come out specifically?

cc (main), 2026-10-23, after B1733. **Sealed before `verification/census.py` and `verification/compare.py` run.** A
test of a structure with two ingredients put in by hand and a selection rule (the thread), not a value derived.
0 of 19.

## Why

- **The fit and where it lives.** B1726 found the two-ingredient fit specific on a grid of τ and lines: the
  Georgi–Jarlskog factor 3 on the leptons and a reading rule. Its good rows lie only on lines of order 5 and 10, where
  the frame sees SU(5)'s five-ality (B1728).
- **What a thread selects.** B1733 proved which lines a thread fixes: by the Smith invariants of A ∓ I; at order 5 one
  pair {v, 2v}, whose bit is real. So a thread selects its own point (B1720's apex) and its own lines, with no
  continuous number free; only the bit stays, and here it is counted in the menu.
- **The question:** do the two ingredients make the six specific when τ and the line are the thread's own, not
  scanned over a grid?

## The model (no data)

- **The frame:** as B1726 (B1656's four-channel coupling, B1667's canonical end at both horocycles, ∂R), through
  B1726's sealed compute().
- **The rows:** each of B1720's 121 thread classes whose own fixed lines include lines of order 5 or 10.
  - 49 classes, 190 points (98 on order-5 lines, 92 on order-10), at each thread's apex τ (Im τ = Lagrange/2), both
    horocycles: 380 rows.
  - Both members of every order-5 pair {v, 2v} are rows, so the bit is in the menu.
- **The restriction to orders 5 and 10:** the Georgi–Jarlskog 3 is an SU(5) Clebsch, and only lines of order 5 or 10
  make the frame SU(5)-like (B1728). Disclosed below as informed by B1726.
- **The readings and the menus:** as B1726. S and S̃; seat {(S̃, S, S), (S̃, S̃, S̃)} × c ∈ {1, 3}; cov (8
  assignments) × c ∈ {1, 3}; free (c continuous).
- **The measure and the calibration:** main's (B1695's random hierarchies, B1713's random mixings). Each cell is the
  mean over 20 fresh seeds, 1734–1753, 4 000 targets each; every random target gets the same 380 rows and the same
  menu.

## Cells

| cell | prediction | prior |
|---|---|---|
| **R1** | under the seat's menu, the best row puts all six ratios within a factor 2 | 45% |
| **R2, specific** | under the seat's menu, the mean fraction of random hierarchies as good is at most 1% | 25% |
| **R3, specific** | under the covariant menu, at most 1% | 15% |
| **R4, specific** | with the lepton factor free, at most 1% | 20% |
| **R5, specific** | the nine (six and ∣V_us∣, ∣V_cb∣, ∣V_ub∣) under the seat's menu: at most 1% | 10% |
| **R6, unfitted** | at the best nine-row (seat's menu), ∣J∣ within a factor 3 of PDG's 3.08 × 10⁻⁵ | 8% |
| **R7, unfitted** | at the best six-row (seat's menu), P-094's D within 3σ of 10.58 ± 0.11 | 3% |
| **C1, control** | (i) the instrument reproduces B1720's stored rows (reading S, both horocycles) at its first three points to 10⁻⁹ in log; (ii) B1726's census control: against B1725's verified census to 10⁻⁹, T-covariance to 10⁻⁶ | 95% |

Read-outs: the best six and nine rows under each menu (thread, line, order, horocycle, readings, factor, D, J); the
per-seed fractions.

**The reading, written before the run.**
- **R2 holds:** the thread rule with the two ingredients is specific with no continuous number scanned. τ and the line
  come from the thread, up to the bit. The frame's selection then reduces to "which thread", plus the ingredients
  (P-294, P-295).
- **R1 holds, R2 fails:** the thread's own points fit but not specifically; B1726's specificity needs the τ grid.
- **R1 fails:** the thread's own points do not carry the two-ingredient fit.
- **R7:** on order-5 lines D = 9 exactly (B1726, B1733), which P-094 excludes, so R7 can hold only on an order-10
  line.
- **C1 failing** stops the reading.

## Seen first

`VERDICT topic-sweep /thread rule|thread.s own (point|lines)|threads? with (the )?ingredients|own order-5|apex.*ingredient/ (full text): 2 of 1505 arcs on main match (NEGATIVE 1, PROVED 1)`.

Bearing on it:
- B1720 (sealed, NEGATIVE: the thread rule without the ingredients, the six within 1.80 at 1.65%);
- B1722 (no measure over threads selects);
- B1726 (the two ingredients on a grid);
- B1728 (five-ality);
- B1733 (the thread's own lines and the bit);
- the web seat's sealed THREADS_WITH_INGREDIENTS (HARVEST_LEDGER row 1308: every thread's own lines of every order,
  all four cells fail, six 3.22 at 26.6%).

None tests the ingredients on the threads' own order-5 and order-10 lines with the bit counted. **Literature:**
Georgi and Jarlskog (1979); Antusch, Hinze and Saad (P-094).

## Disclosed

- **Known before the seal:**
  - B1720 in full: its rows at these 190 points, read only with reading S for down and leptons, without the factor,
    compared with data;
  - B1726, B1732 and B1733;
  - the web seat's sealed all-lines test (failed) and an unsealed read-out with main's readings that reached 1.614 on
    an order-5 line (the L229 reader's report);
  - the order-5 D = 9 identity.
- **The restriction to orders 5 and 10 is informed by B1726's result** (its good rows lie only there), as well as by
  B1728's five-ality and the factor's SU(5) origin. The calibration counts the 380 rows and the menu, not this choice
  of orders.
- **Expected directions:** R1 about even; R2 below even; R6 and R7 likely to fail.
- **The trial count:** this is the twenty-fourth sealed test of this frame against data.
- **The run's size:** minutes.
- The instruments were import-tested before the seal; importing them computes nothing.

## Instruments

- `verification/census.py` (no data) → `census.json`, `control.json`.
- `verification/compare.py` → `comparison.json`.
- `ARTIFACT_HASHES.txt`: the instruments, and the files they read in place (B1720's census, B1726's census.py and its
  dependencies, the masses and the CKM data).
