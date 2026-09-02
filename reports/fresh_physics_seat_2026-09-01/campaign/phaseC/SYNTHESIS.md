# Phase C/D synthesis — recomputing what Phase B could not mark COMPUTED-and-reproducible (draft; counts refreshed when the last Phase C packets land)

## 1. What was done

- **C-1, agents (mechanical).** 59 packets / 398 COMPUTED-but-unreproduced load-bearing claims: one sonnet agent per
  packet reran the committed script in an isolated worktree of the right head and transcribed the printed numbers
  (`results/rerun_results.tsv`, `results/DIGEST.md`). Agents ran and transcribed; they did not judge.
- **C-3, seat (tool checks on ASSERTED / IMPORTED claims).** R43 (16 SnapPy/PARI matches, one digit slip), R44 (11
  Lie-theory matches; B549's "spectrum" is the E7 Perron eigenvector), R45 (class numbers), R42 (m = 12 class count).
- **D-1, agents.** 38 packets / 185 certificate scripts on `origin/codex/seat-r001` and `origin/claude/outside-bench`
  (`../phaseD/results/`). **D-2, seat.** The chain-critical ones rerun by hand (R46: 11 codex; R47: 17 outside-bench),
  plus R48–R50 on the three cases that needed judgment.

## 2. Seat's judgment on every DIFFERS (8)

| # | arc | agent's finding | seat's judgment |
|---|---|---|---|
| 10 | B59 | max-match 0.0061 vs banked 0.0101 | REPRODUCES: the factorisation reproduces and passes its own 0.03 gate; the quoted figure is a BLAS-dependent residual |
| 295 | B511 D3.3 | committed script → NaN | **R48**: scripts broken (φ^t error growth; banked 2.000000000000 percentiles are the same collapse); the claim reproduces on the exact trace map at 60 digits (0.93/0.04, 0.97/0.02, 0.85/0.08 vs ≥ 0.84 / ≤ 0.10). REPRODUCES IN SUBSTANCE, SCRIPT BROKEN |
| 553 | B775 V4 table | script says 0 amphicheiral, table says 4 | **R50**: table right (8/8 by direct SnapPy check), script's `symmetries()[0]` probe throws on this SnapPy → all misreported. REPRODUCES, SCRIPT BROKEN |
| 614 | B825 motif share | 6.17 % (70/1135) vs banked 8.3 % (62/750) | STALE NUMBER, METHOD REPRODUCES: the atlas is mined live and the corpus grew from 750 to 1135 probes; the arc's committed thresholds still pass |
| 624 | B835 lock repairs | post-B700 shares differ (0.236 vs 0.375 etc.) | same class as 614: live-mined snapshot; pre-B700 values match exactly, post values moved with the corpus |
| 731 | B967 retraction sweep | 2635 files / 0 violations vs 2210 / 11 | historical first-run snapshot; the 11 were fixed and the tree grew. REPRODUCES AS A METHOD |
| 938 | B1166 | Im(complex volume) 2.66e−15 vs quoted 1.8e−15 | NOISE: both are machine zero; CS = 0 reproduces |
| 991 | B1213 claim base | 827/1045 absent (79 %) vs banked 919/1031 (89 %); true 75 vs 55, false 143 vs 57 | STALE NUMBER: `claim_base.py` recomputes from the live corpus, which has changed since 2026-08-29 (B1211/B1214 corrections landed declared-law fields). The headline "creates_law absent on most settled arcs" stands (79 %); the specific figures in B1213's verdict file are out of date and should be re-banked with a pinned commit |

## 3. The PARTIAL class (52) and what it means

Three recurring shapes, none of which is a wrong number:
1. **Hardcoded record, live code absent or guarded** (B129 S1B_SCAN, B131 forks (1,3)/(2,3), B147 Bianchi ratios,
   B335 cover symmetry string-compare, B568 RECORD dict, B906 lock asserting stored strings): the number is banked but
   the committed script cannot regenerate it. The seat recomputed the ones that matter (B147 ratios in R35; B335 in
   R36) — they hold. Record point: the arc should ship the generator.
2. **Half the claim is code, half is prose** (B5's "10^120", B64's "no other obstruction", B313's `7*3+1*6 == 27`,
   B566 law at p = 3 only, B578 one of "two independent methods", B570 one principal instance): the code reproduces
   what it computes; the reader's flag ("claim exceeds computation") stands as written.
3. **Sage-only halves** (B142 find_field, B251 alexander_polynomial, B247 SnapPy cross-check crashes on API drift):
   CANNOT_RUN here by dependency, reproduced where the seat had another route (R33 shape fields).

## 4. CANNOT_RUN (139 of 398 so far)

By reason: no committed script for the claim (the largest class — the reader's "reproducible_from_committed: no" was
right), Sage/Magma/Regina dependencies, hardcoded machine paths, and data files not in the tree. These are record
findings, not correctness findings; the list is in `results/DIGEST.md`.

## 5. What Phase D adds (certificates on the two undigested heads)

- 187 PASS of 205 rows; the chain-critical ones pass by the seat's own hand (R46, R47). Nothing on the SM end of the
  chain fails to run: hypercharge ratios (r019; universal given SM multiplicities, "independently of E6" in codex's
  words), up-Yukawa rank 0 in the dressing (r017), unique breaking chain and SUSY no-go (cloud), the 27's invariant
  census (jordan_beat, tensor_invariant_counts), the twisted-double cohomology (h¹ = 3).
- **One certificate contradicts itself (R49):** `spacetime64.py` prints "(0,0) content: 2 (0 = NO hypercharge room)".
  The 2 are the two spare Cartan directions of e6 outside so(3,1) ⊕ su(3); the centraliser is at least u(1)², so the
  "no room" sentence is false by the certificate's own count while the 64-gluing theorem (memo 33) reproduces.
- **One mechanism disagreement (R47):** cloud's `yukawa_texture.py` (object kinematics allow a 6-entry up-Yukawa) vs
  codex r017 / main B1167 (heterotic dressing forces μ_u = 0). Both pass; different objects.
- Record items: pinned commit 3c58527b (fetch by SHA), `vol_hygiene.py` needs the B1137 path, `c3_ohtsuki_large.py`
  "fails" only as the record's own honest negative, `paired_summary_check.py` is BUILT-NOT-ADOPTED.

## 6. Bearing on the thesis

Nothing in C or D moves the seat's standing statement. The structural chain (m004 → ℚ(√−3) → 2T → E6 → 27 → SM-shaped
bookkeeping) reproduces on this bench wherever it is code, including on the two heads Phase B never read. What does not
reproduce is a scatter of banked *numbers* (B511's percentiles, B1213's shares, B549's unscripted eigenvector, the
Vol(4₁) digit slip) and one certificate's headline sentence (no hypercharge room) — none of them load-bearing for the
structure, one of them (spacetime64) pointing the other way from its author's reading. "No observable content" stands:
every certificate rerun here fences Gate 5 itself.
