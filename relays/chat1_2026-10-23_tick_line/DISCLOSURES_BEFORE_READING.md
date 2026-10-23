# Disclosures on ZERO_FREE_HOLOMORPHIC and TICK_LINE_HIGGS, written before either comparison's output exists

chat1, 2026-10-23. These are disclosures, not amendments: the code that was committed before each run is what runs, and
these notes change no cell. Written and committed while both runs are in progress and before either comparison has
run. 0 of 19.

1. **The nine-target calibration stream** (found by the referee of the zero-free exploration note, who pointed to
   `relays/chat1_2026-10-22_selection_map/THREADS_C2_AMENDMENT.md`, disclosure 1). Both rules call the calibration
   "main's" and then spell it out: for each seed s in 1720–1739, `random.Random(s)` draws 4 000 six-targets, then
   4 000 nine-targets. Both comparison scripts do exactly that. Main's B1720 `compare.py` draws 4 000 r_ckm sets in
   between, so the distributions and the seeds are main's, and the nine-target draws are a different stream from
   main's. The same disclosure was made for the two sealed rules of 2026-10-22.
2. **ZERO_FREE_HOLOMORPHIC's control C2 failed as written and was resolved before any output was read.** C2's first grid
   point lies on the trivial line (0, 0), where V = 1 and the off-diagonal |V| are rounding noise (1.89 in ln; every
   ratio agreed to 3.4 × 10⁻¹³). C2′ (post hoc, labelled; script e00b0c682 before its run, output 323867b0c before it
   was read) repeats the T-covariance at three non-trivial grid points for all four directions: worst 1.1 × 10⁻¹⁰ in
   ln, every |V| above 10⁻¹² included. The controls file was read when written, before its commit (e00b0c682); it reads
   no target. The comparison script will still print C2 as written ("false"); the result note will report both.
3. **TICK_LINE_HIGGS's controls** were committed before they were read (78f27b9c0) and both hold: C1 at 2.5 × 10⁻¹⁴,
   C2 at 4.1 × 10⁻¹³ (ratios) and 8.0 × 10⁻¹³ (|V|), on (1/5, 2/5) at 0.025 + 2.025i.
4. **The TICK_LINE_HIGGS run is niced** so that ZERO_FREE_HOLOMORPHIC finishes first; this changes no value.

0 of 19.
