# B500 — the child hunt, depth 4: NO AIRLOCK; the wild ladder (S₅, S₉, S₁₀)
**Prereg'd target x⁴−x−1 (d_K=−283) NOT FOUND at depth 4** — all 36 three-verb words solved clean
(exact resultant eliminants + saturation; 0 timeouts; hunt_results.txt). The airlock never fired.
Depth 5 = the remaining zone before "the child is not a short word" banks as the negative.
**Discovery (W1 answered beyond its asking):** the wild register ESCALATES — depth 3 gave S₄; depth 4
births **S₅ quintics** (ord 120; ≥8 words), **S₉ at degree 9** (FFMD, FMDF), **S₁₀ at degree 10**
(FDDM, MFDD) — full symmetric groups of growing degree. The grammar writes arbitrarily wild
sentences; the value-lattice is a LADDER, not a bound. The live question is now SELECTION (why any
particular field): B501 (stationary measure = which fields a typical history births) and B502 (the
parity constraint) are the prereg'd answers. Firewalled; no value-matching performed.

## Depth 5 — the KILL fires: the child is not a short word (2026-07-11, banked)

The depth-5 sweep (`hunt_d5.py` → `hunt_results_d5.txt`, an ~18h streamed run) completed **141 of the
150** all-three-verb words. **ZERO hits:** no d_K = −283, no field isomorphism to ℚ[x]/(x⁴−x−1), the
B398 airlock **never fired** (grep-verified). The pre-registered **KILL condition is met — "the child is
not a short word."** The figure-eight's Meyerhoff child field is NOT reachable by any depth-≤5 combination
of the object's three verbs; the object does not generate its own child.

- **What the words DO produce (the wild ladder, extended):** generic large symmetric Galois groups —
  **S₇ ×15, S₁₁ ×10, S₆ ×5, S₈ ×5, S₅ ×5, S₉ ×4**, plus D₄ ×3. The monoid's arithmetic is generically
  *maximal/wild*, never the special −283 child. This is the same finding as the B499 wild census, now
  confirmed against the child target specifically.
- **The 9 unfinished words are tool-blocked, not skipped:** all nine are the **double-decimation tail**
  `DDFMD, DDFDM, DDMFF, DDMFM, DDMFD, DDMMF, DDMDF, DDDFM, DDDMF` — the D (decimation) verb squares the
  trace coordinates, so their resultant eliminants blow up to degree ~3000–9280, beyond in-sandbox `gp`
  (the run wedged on the first of them). NEEDS-SPECIALIST-tool corner (degree, not chance); the 141
  completed words already make the negative overwhelming (0/141, all generic Sₙ). *(process killed 2026-07-11.)*
- **Bearing on the project:** a third independent line — alongside the audit's Gate C (commensurator =
  trinification, not generation) and B519 (no crossing) — landing on the same terminus: **the object
  produces generic wild arithmetic, not the special values a generation/child reading would require.**
  Corroborates the Child Program's Inversion Law and the two-seat closure ([[B521]]/CLOSURE_2026-07-11).
  The depth-5 KILL retires the "child = short word" hypothesis; SELECTION (B501/B502) remains the only
  live child-related question. Firewalled; no value-matching. Lock: `tests/test_b500_kill.py`.
