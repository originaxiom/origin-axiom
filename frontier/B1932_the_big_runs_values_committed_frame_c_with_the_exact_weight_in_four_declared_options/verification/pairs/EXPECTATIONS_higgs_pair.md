# The Higgs pair: do the two worlds settle each other? Expectations, written before any run (main, 2026-11-14 ~14:30)

World 1 (the record's practice): up S~, down S, leptons S.  World 2 (its mirror): up S, down S~, leptons S~.
Frame: B1656's, as patched with the closed-form channel norm (B1928's fiber_grid import), canonical ends L_max and L_2.

Test: for 3 points tau and 3 lines of order 5, compare world 1 at (tau, line, end) with world 2 at the image under each
of the record's orientation-reversing moves: the mirror tau -> -conj(tau) and the swap tau -> 1/conj(tau) (end + log|tau|),
each with the 8 signed orders of the line's two coordinates. Control: the same maps from world 1 to world 1 (P-847 found a
mirror symmetry of one reading to 2e-15; the control must find it).

Outcomes (each a result, none preferred):
- SETTLED: some move maps world 1 onto world 2 on every point and line, max |log ratio| < 1e-9: the two worlds are one
  world seen from two sides, and the global bit is not a parameter.
- PHYSICAL: no move does (every move's max |log ratio| > 1e-3 somewhere): in this frame the bit is real, and only a
  change of frame (the Higgs's charge realised like matter's) could settle it.
- Anything between is reported as found.
Firewall: no output is compared with any measured value; only the two worlds with each other.

## Result (run ~14:45, higgs_pair_run.txt, higgs_pair.json)
- Control: the mirror with line (a, -b) or (-a, b) maps world 1 onto world 1 to 2.2e-6 (the canonical end's
  interpolation; P-847's 2e-15 used exact ends).
- No mirror line map takes world 1 to world 2: max |log ratio| 2.9 to 4.3 for every one of the 8.
- The swap family failed its own control (main's composite convention for the swap's end or line), so its numbers
  are not used. They are not needed: B1724 proved each reading SL(2, Z)-covariant (2e-7), and GL(2, Z) is SL(2, Z)
  together with the mirror times SL(2, Z).
- OUTCOME: PHYSICAL in this frame. No move of the act (the tick and the undoing included) exchanges the two worlds;
  the global bit can settle only through a frame whose Higgs carries its charge as matter does (the consistent frame).

# P-Q2 (the hand on the seven rows): expectations, written before the run (~15:10)
The averaged frame F-bar (B1928's fiber_grid_fine.json, both modes, both horocycles) at (x, y) and (-x, y). SAME if every
claimed key (up and down ratios, the three mixing moduli) agrees to the grid's own precision (the json stores values to
float precision; the pointwise mirror symmetry was 2e-15 with exact ends, 2.2e-6 with interpolated ends). Negative
control: world 1's keys against world 2's at the same point must differ by more than 1e-3.
