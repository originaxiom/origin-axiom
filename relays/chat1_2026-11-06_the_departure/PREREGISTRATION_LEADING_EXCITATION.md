# THE PRINCIPLE'S LEADING EXCITATION — pre-registration (the web seat, 2026-11-06)

**For:** the owner's 11:33 "lets solve it". This follows this seat's finding (the clock note) that plenitude alone does
not return the record's candidate, which needs a selection: the principle's golden path (P-465) plus one departure in
the line sector.

**Kind:** data-free arithmetic on the principle's own measure. No coupling, scale ratio or held-out quantity is
computed, and nothing is compared with data. The six are not a criterion (P-708). The weight's strength |s| is generic.
**Written before** `leading_excitation_check.py` is run. The smoke copy uses reduced ranges (n ≤ 8, two values of
|s|), and its values are not read.

## The setting

**The principle's measure.** P-441's golden end ("the principle's golden path at s → −∞") counts words per move, with
weight e^{−s·ℓ} and s = −|s| large. Relative to the golden thread at the same number of moves, a single departure (a
run of n) has weight e^{−|s|·D_n}.
- D_n is the length it loses: D_n = (n − 1)·2 log φ − ΔS_n, with ΔS_n = 2 log((n − 1 + √5)/√5) (0772952e3; a34f5cdd1).
- 2 log φ is the golden thread's length per move (P-441).

**The line sector** (reading (ii), 904f19136): runs n ≡ 1 mod 5.

## Predictions (hand-derived)

**P1.** D_n is positive and increasing for n ≥ 2. Its derivative in n is 2 log φ − 2/(n − 1 + √5) > 0.
- D_2 = 0.2232;
- D_6 = 2.4634 ± 0.0005;
- D_11 = 6.2250 ± 0.001;
- D_16 = 10.351 ± 0.002.

**P2.** At every |s| > 0, the leading departure overall is the run of 2, outside the line sector. Within the sector it
is the run of 6.

**P3.** The run of 6's share of the sector, e^{−|s| D_6} / Σ_m e^{−|s| D_{5m+1}}, at |s| = 0.25, 0.5, 1, 2:
- at |s| = 1: 0.9776 ± 0.002;
- at |s| = 2: 0.9995 ± 0.0002;
- it rises monotonically to 1.

**P4, the dilute regime.** The expected number of departures per golden position, Σ_{n≥2} e^{−|s| D_n}, falls below
0.1 at |s| about 10.5 (between 9 and 12). There the run of 6 is a fraction e^{−|s|(D_6 − D_2)}, about 10⁻¹⁰, of all
departures.

**What would refute:** D_n not monotone; any value outside these ranges.

## What it bears on

It quantifies the chain's principle 4 (leading order) under principle 1 (the principle is the law):
- The principle's own measure makes departures rare (dilute) for large |s|.
- Its leading excitation is a run of 2, which changes the line.
- Only under matter conservation (principle 2, reading (ii)) is the leading excitation the run of 6. There it
  dominates for every |s| ≳ 1.
- So the run of 6 is selected by conservation plus least action within the sector, not by the measure alone.

0 of 19.
